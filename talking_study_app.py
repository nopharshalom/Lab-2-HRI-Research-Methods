cat > talking_study_app.py << 'EOF'
import argparse
import csv
import itertools
import select
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

from reachy_mini import ReachyMini
from reachy_mini.utils import create_head_pose

NOD_AMPLITUDE_DEG = {"A": 0.0, "B": 10.0}
CONVERSATION_SECONDS = 180
NOD_DURATION_S = 0.6
VOICE_RATE = 175
PROMPTS = {"place": "Can you tell me about a place you like to visit?",
           "meal": "Can you tell me about a memorable meal you have had?"}
GREETING = "Hi there! I'm Reachy. It's nice to meet you."
BACKCHANNELS = ["Got it.", "I see.", "Tell me more.", "That sounds interesting.",
                "Oh, really?", "Go on."]
CLOSING = "Thank you for sharing that with me. Goodbye!"
LOG_FILE = Path(__file__).resolve().parent / "logs" / "trials.csv"

def speak(mini, text, voice, wait=True):
    print(f'[SAY] "{text}"')
    if voice == "robot":
        try:
            wav = Path(tempfile.gettempdir()) / "reachy_say.wav"
            subprocess.run(["say", "-r", str(VOICE_RATE), "-o", str(wav),
                            "--data-format=LEI16@16000", text], check=True)
            mini.media.play_sound(str(wav))
            if wait:
                time.sleep(0.08 * len(text.split()) * 5)
            return None
        except Exception as e:
            print(f"[WARN] robot speaker failed ({e!r}); using laptop voice")
    proc = subprocess.Popen(["say", "-r", str(VOICE_RATE), text])
    if wait:
        proc.wait()
    return proc

def neutral(mini, duration=1.0):
    mini.goto_target(head=create_head_pose(), antennas=[0.0, 0.0], duration=duration)

def greet(mini):                       # from Greetings app: bow with antennas open
    mini.goto_target(head=create_head_pose(z=-0.02, pitch=15, degrees=True),
                     antennas=[-1.0, 1.0], duration=0.8, method="ease_in_out")
    mini.goto_target(head=create_head_pose(pitch=5, degrees=True),
                     antennas=[-0.6, 0.6], duration=0.8, method="ease_in_out")
    neutral(mini)

def listening_pose(mini):              # from Conversation app: attentive listening
    mini.goto_target(head=create_head_pose(pitch=-5, degrees=True),
                     antennas=[0.3, -0.3], duration=1.0)

def nod(mini, amplitude_deg):
    if amplitude_deg <= 0:
        return
    mini.goto_target(head=create_head_pose(pitch=-5 + amplitude_deg, degrees=True),
                     antennas=[0.3, -0.3], duration=NOD_DURATION_S / 2)
    mini.goto_target(head=create_head_pose(pitch=-5, degrees=True),
                     antennas=[0.3, -0.3], duration=NOD_DURATION_S / 2)

def goodbye(mini):
    for a in (0.5, -0.5, 0.5):
        mini.goto_target(antennas=[a, -a], duration=0.4)
    neutral(mini)

def conversation(mini, amplitude_deg, voice):
    print(f"\n[STAGE] listening -- {CONVERSATION_SECONDS}s. "
          "Press Enter at each participant pause; type q + Enter to end.")
    replies = itertools.cycle(BACKCHANNELS)
    start, pauses = time.monotonic(), 0
    while (remaining := CONVERSATION_SECONDS - (time.monotonic() - start)) > 0:
        ready, _, _ = select.select([sys.stdin], [], [], min(1.0, remaining))
        if not ready:
            continue
        if sys.stdin.readline().strip().lower() == "q":
            print("[STAGE] ended by facilitator")
            break
        pauses += 1
        print(f"[PAUSE] #{pauses} at {time.monotonic() - start:.1f}s -> nod {amplitude_deg} deg")
        proc = speak(mini, next(replies), voice, wait=False)
        nod(mini, amplitude_deg)
        if proc:
            proc.wait()
    return round(time.monotonic() - start, 1), pauses

def write_log(row):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    new = not LOG_FILE.exists()
    with open(LOG_FILE, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(row.keys()))
        if new:
            w.writeheader()
        w.writerow(row)

def main():

    p = argparse.ArgumentParser()
    p.add_argument("--participant", required=True)
    p.add_argument("--condition", choices=["A", "B"], required=True)
    p.add_argument("--prompt", choices=["place", "meal"], required=True)
    p.add_argument("--voice", choices=["laptop", "robot"], default="laptop")
    args = p.parse_args()
    amp = NOD_AMPLITUDE_DEG[args.condition]
    start_time = datetime.now().isoformat(timespec="seconds")
    status, error, duration_s, pauses = "Completed", "", "NA", "NA"

    with ReachyMini() as mini:
        mini.enable_motors()
        try:
            print(f"[STAGE] start participant={args.participant} "
                  f"condition={args.condition} nod_amplitude_deg={amp}")
            neutral(mini)
            input("Facilitator: press Enter when the participant is seated...")
            print("[STAGE] greeting")

            if args.condition == "A":
                # ---- CONDITION A: talking only (no head tracking, no gestures) ----
                print("[STAGE] condition A: voice only")
                speak(mini, GREETING, args.voice)
                speak(mini, PROMPTS[args.prompt], args.voice)
                duration_s, pauses = conversation(mini, 0.0, args.voice)
                print("[STAGE] closing")
                speak(mini, CLOSING, args.voice)

            else:
                # ---- CONDITION B: talking + head tracking + gestures ----
                print("[STAGE] condition B: voice + head tracking + gestures")
                mini.start_head_tracking()

                proc = speak(mini, GREETING, args.voice, wait=False)
                greet(mini)
                if proc:
                    proc.wait()
                speak(mini, PROMPTS[args.prompt], args.voice)
                listening_pose(mini)
                duration_s, pauses = conversation(mini, amp, args.voice)
                listening_pose(mini)
                print("[STAGE] closing")
                mini.stop_head_tracking()

                proc = speak(mini, CLOSING, args.voice, wait=False)
                goodbye(mini)
                if proc:
                    proc.wait()

        except KeyboardInterrupt:
            status, error = "Interrupted", "Stopped by operator"
        except Exception as e:
            status, error = "Failed", repr(e)
            print(f"[ERROR] {error}")
        finally:
            neutral(mini)
            print("[STAGE] neutral")

    write_log({"participant_id": args.participant, "condition": args.condition,
               "nod_amplitude_deg": amp, "prompt": args.prompt, "voice": args.voice,
               "start_time": start_time,
               "end_time": datetime.now().isoformat(timespec="seconds"),
               "trial_status": status, "conversation_s": duration_s,
               "pause_events": pauses, "error": error})
    print(f"[STAGE] done status={status}")

if __name__ == "__main__":
    main()
EOF
