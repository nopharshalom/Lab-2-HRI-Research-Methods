# INFO 5356-030 Lab 2: HRI Research Methods

## Team Members
Nophar Shalom, Bailey Carlson, Wiam Salih

---

## 1. Teleoperation on the Physical Robot

### Final App Cycle Clip
[▶️ Watch the physical Reachy control demo](images/reachy-control.mov)

### Stage Markers (Screenshot / Log Excerpt)
<img src="images/sim-screenshot.jpeg">

### Sim-to-Real Comparison

The real robot didn't move as smoothly as it did in the simulation. Its motions were often a bit jerky or hesitant, probably because of things the simulation didn't account for, like motor delays, friction in the joints, and small quirks in the hardware. It was also fairly noisy. The motors and gears made sounds with every movement, so you could tell what the robot was doing just by listening to it.

---

## 2. Hello World Application

### Demonstration Clip
[▶️ Watch the application demo](images/hello-world.mov)

```
python - <<'PY'
import time
from reachy_mini import ReachyMini

with ReachyMini() as mini:
    mini.enable_motors()
    mini.goto_target(antennas=[0.3, -0.3], duration=1.0)
    mini.goto_target(antennas=[-0.3, 0.3], duration=1.0)
    mini.goto_target(antennas=[0.0, 0.0], duration=1.0)

   
    mini.start_head_tracking()
    time.sleep(0.1)

    try:
        for _ in range(100):         
            face = mini.get_tracked_face()
            detected = face[0] if isinstance(face, (tuple, list)) else getattr(face, "detected", False)
        
        else:
            print("No face seen")
    finally:
        mini.stop_head_tracking()      
    print("Done")
PY
```
### Stage Markers (Screenshot / Log Excerpt)

<img src="images/export.jpg">

### Changes, Expected Outcomes, and Actual Outcomes

With the Hello World code, we edited it to include face tracking alongside the antenna movements from the original code. When a participant moves their head, Reachy could now move its head in regards to their movement, creating a more immersive conversation experience. In this case, because it was a simple change, our expected outcomes seemed to match the actual outcomes.

---

## 3. Custom App on the Physical Robot

[Check out our Custom App code here!](talking_study_app.py)

### Final-Project Topic and App Capabilities

In any case, our final project topic will include interactive features that enable the user to converse with Reachy Mini. Those conversations will require both conversation feedback and face tracking to keep the user engaged. Because our target audience will be middle school children, we want the experience to be as intuitive as possible. This includes making sure that they feel heard and supported by the Reachy Mini, regardless of the task at hand. We are incorporating the capabilities from the Conversational App and the Greetings App for Reachy Mini.

### Integration Map

| Source App | Capability Reused | Modified | Interaction Goal | Final-Project Connection |
|---|---|---|---|---|
| Reachy Mini Conversation App | We used the verbal greetings from the beginning and end of the conversation. | We modified the prompt that the user recieves (e.g. the question asked) as well as the feedback responses provided to the user from Reachy as they converse.| The goal was to make sure that the user feels verbally assured as they speak, to make sure that they know they're heard.| In a normal conversation, the user would need to know that they are being heard and engaged with.|
| Gestures Library | We used the initial greeting gestures (head nodding, antenna crossing, etc.)| We added facial tracking for a smoother user experience overall. | The goal was for maximum attentiveness from the robot, almost as if they are human.| Immersiveness and human-like attention is the goal, especially when it comes to children because they like to get attention.|

### Setup, Launch, and Stop Instructions

### Robot-Only Demonstration

[▶️ Watch the condition A demo](images/conditionA.mov)

[▶️ Watch the condition B demo](images/conditionB.mov)

---

## 4. HRI Research Questions

### Problem Statement
When people talk to someone, they rely on small listener signals, like nods, to judge whether they are being heard. These signals are called backchannels (Yngve, 1970). Social robots are increasingly deployed as conversational partners in homes, schools and care settings, yet many stay motionless while a person speaks. A robot that stays still while listening may come across as inattentive or less socially present, even if its spoken responses are appropriate. Prior work shows that nonverbal backchanneling from virtual agents increases rapport (Gratch et al., 2007) and that robot backchanneling affects how engaged speakers are (Park et al., 2017). Less is known about whether a simple, low-degree-of-freedom robot like Reachy Mini can produce this effect with head movement alone mimicking eye contact. This pilot study tests whether adding active-listening movements changes how sociable adults perceive Reachy Mini to be during a short conversation, and whether these movements affect how long participants choose to speak.

### Construct Map

| Claim | Manipulation | Measures | Expected Evidence |
|---|---|---|---|
| Active-listening movements make Reachy Mini seem more sociable | Verbal responses only vs verbal responses and head movement | HRIES sociability (primary) | Higher sociability scores in Condition B than in Condition A for most participants |
| Participants notice the listening behavior | Same as above | Manipulation-check item | Higher agreement in Condition B than in Condition A |
| Movement encourages participants to keep talking | Same as above | Speaking time (s) | Longer speaking time in Condition B than in Condition A |

#### Independent Variable

The presence or absence of head movements mimicking active listening.

- **Condition A (baseline):** The conversational engagement responses from Reachy continue, but no movement is produced.
- **Condition B (comparison):** The robot performs head tracking in addition to responses.

In both conditions, the Reachy Mini responds to the user with the same prompts, questions, tone of voice, verbal greetings, and order of comments.

#### Outcomes

- **Primary outcome:** HRIES sociability score. This is the mean of the four sociability items, each rated on a 7-point scale, so scores range from 1 to 7. Higher values mean the robot was perceived as more sociable.
- **Secondary outcomes:** HRIES animacy, agency and disturbance scores, each the mean of its four items. Higher values mean greater animacy, agency or disturbance, respectively.
- **Objective outcome:** total participant speaking time in seconds during the conversation window.

#### Manipulation Check

After each completed run, participants rate the statement "The robot responded to what I was saying with head movements" from 1 (strongly disagree) to 7 (strongly agree). The manipulation is considered noticeable if ratings are higher in Condition B than in Condition A.

#### Controls

- The robot's idle pose, antenna position, gaze direction, and start and end pose (neutral) are identical in both conditions.
- The conversation topic (place) and verbal responses are the same across all participants and within-subject conditions.
- The room layout, participant seat distance from the robot, lighting and facilitator position are the same for every session.
- The facilitator reads a standardized script and does not react to the robot's behavior.
- All participants receive both condition in the same order (A, then B)

#### Potential Confounds

- **Prompt content:** The prompt may be difficult to talk about.
- **Order and novelty effects:** Participants may talk more or rate the robot differently in the second session simply because the robot is no longer novel.
- **Detection errors:** Facilitator robot response timing may cause disruptions in the conversational flow between the user and robot.
- **Facilitator presence:** Participants may speak to please the facilitator rather than responding to the robot. The facilitator sits out of the participant's line of sight.

#### Measurement Scales and Construct Validity

The HRIES (Spatola, Kühnlenz & Cheng, 2021) has 16 items rated on a 7-point scale, with four items per dimension:

- **Sociability:** warm, likeable, trustworthy, friendly
- **Animacy:** human-like, real, alive, natural
- **Agency:** self-reliant, rational, intentional, intelligent
- **Disturbance:** scary, strange, creepy, weird

### Research Questions and Hypotheses

**H1 (confirmatory):** Participants will report higher HRIES sociability scores in the movement condition (B) than in the still condition (A).

**H2 (confirmatory):** Participants will speak longer in the movement condition (B) than in the still condition (A).

**RQ1 (exploratory):** How do active-listening movements affect participants' HRIES disturbance ratings and their descriptions of the robot's behavior?

---

## 5. HRI User Study

### Conditions Table

| Element | Condition A | Condition B | Held Constant |
|---|---|---|---|
| Primary factor | No active listening movements. | Head tracking, active listening movements. | Reachy's verbal responses to each user comment. |
| Robot behavior | The robot holds its neutral pose for the whole conversation. | The robot does not hold its neutral pose and tracks the user's head movements. | Starting and ending poses are positioned at neutral. |
| Interaction | The participant talks to the robot about assigned prompts. | Same task. | Instructions, room setup, facilitator, and operator. |

### Participants

#### Target Population and Sampling Rationale

Our target population is adults who might talk to a social robot in everyday settings, such as at home, at a front desk or in a classroom. For this pilot, we recruited four adult volunteers from the Cornell Tech community who are not members of our team. We used a convenience sample because the goal of a pilot is to test whether the task, the robot behavior and our measures work before running a larger study, not to make claims about the general population.

#### Demographics, Robot Familiarity, and Condition Order

We collected only information that could reasonably affect how someone talks to or judges a robot: age range, how comfortable they are speaking English, and how familiar they are with robots, rated from 1 (never interacted with a robot) to 7 (work with robots regularly). Each participant was given a unique ID. All participants receive condition A then B and get the same verbal prompts.


| Participant ID | Age | English Comfort | Robot Familiarity (1–7) |
|---|---|---|---|
| P01 | 22| fluent| 4|
| P02 | 23| fluent| 1|
| P03 | 25| fluent| 3|
| P04 | 27| fluent| 3|

#### Limits on Transferability

With only four participants, all drawn from a tech-focused graduate campus, our results can't tell us how people in general would react to an actively listening robot. Our participants are likely more comfortable with technology and more curious about robots than most people. They also know they are taking part in a class study, which may make them more patient or more generous in their ratings. Any pattern we find should be treated as a reason to run a larger study, not as a conclusion

### Study Task

#### Task and Standardized Instructions

#### Trial Definitions

In each condition, the participant sits facing Reachy Mini and has a conversation about the following topic:

- **Place:** "Tell the robot about a place you like to spend time, and why you like it."

We chose this topic because anyone can talk about it without special knowledge, and they're personal enough to encourage natural, flowing speech. The facilitator reads the same instructions before each condition:

> "Please respond to the robot's prompts. Speak to it as you would to someone who is listening to you. There's no right or wrong way to do this."

If the participant stops talking for more than 15 seconds, the facilitator can say once: "Feel free to keep going, or add anything else that comes to mind."

| Trial Status | Definition |
|---|---|
| Completed | The full conversation ran, the robot behaved as intended for each condition, and the participant filled out the questionnaire. |
| Interrupted | The conversation was paused because of a noise, a question from the participant, or the operator pressing stop, and then resumed. |
| Failed | The condition couldn't be delivered as designed, for example the robot moved in Condition A, didn't move in Condition B, or lost connection, or the participant chose to stop. |
| Repeated | A failed condition that we ran again from the start. We only repeat a condition if the failure happened in the first 30 seconds, and we note the repeat in the session record. |

#### Setting and Environmental Controls

Every session takes place in the HRI Lab. Reachy Mini sits on a table at roughly the participant's seated eye level, and the participant's chair is placed at about 1 meter in front of it. The facilitator sits to the side, out of the participant's direct line of sight, so the participant naturally speaks to the robot rather than to a person. A second team member sits at the laptop with the stop control, also out of direct view.

### Facilitator Script

**Before the participant arrives**

We power on the robot, confirm the battery and motors look normal, and run a short test of both conditions to make sure the robot stays still in Condition A and nods and head tracks in Condition B. We check that the log is recording and put the robot in its neutral pose.

**Welcome and agreement to participate**

> "Thanks for participating! Today you'll have two short conversations with a small robot called Reachy Mini, and after each one you'll fill out a brief questionnaire. We're interested in how people experience talking to robots. This interaction will not be recorded. Your responses to the questionnaire will be stored and you can skip any question or stop at any time without any problem. Do you have any questions?"

**Background questions**

We ask the participant their age range, how comfortable they are speaking English, and how familiar they are with robots (1–7).

**Conversations**

We read the standard instructions and signal the operator team member to start the conversation. After the first condition conversation, the operator will begin the second condition conversation. After each conversation is complete, we will verbally administer the questionnaire, meaning each participant will complete the questionnaire twice.

**Debrief**

> "Thank you. Now we can tell you what we were looking at. During the first conversation, the robot had only verbal responses. During the second conversation, the robot had both verbal responses and head movements mimicking active listening. We wanted to know whether the presence/absence of movement changes how friendly or attentive the robot seems, and whether they affect how much people talk. Do you have any questions?"

### Measures

#### HRIES Questionnaire

Participants rate how well each word describes the robot on a 7-point scale, from 1 (not at all) to 7 (very much). The 16 words are shown in a mixed order, and the same order is used every time. Each dimension is scored separately.

| Dimension | Items |
|---|---|
| Sociability (primary outcome) | Warm, Likeable, Trustworthy, Friendly |
| Animacy | Human-like, Real, Alive, Natural |
| Agency | Self-reliant, Rational, Intentional, Intelligent |
| Disturbance | Scary, Strange, Creepy, Weird |

#### Objective Behavioral Measure

Total speaking time, in seconds, during the conversation. The app measures this from the microphone by adding up the time the participant was speaking. We also record how many times the facilitator had to prompt the participant to keep going.

#### Open-Ended Question

"How would you describe the robot's behavior while you were talking?"

#### Manipulation-Check Item

"The robot responded to what I was saying with head movements." Rated from 1 (strongly disagree) to 7 (strongly agree).

---

## 6. Research Data

### Datasets

[Raw Data Google Sheet Found Here](https://docs.google.com/spreadsheets/d/1r0SRfQDrf8Qvk5bd2O6SjLyphTbME4_NkkX86LKy_M8/edit?gid=618784505#gid=618784505)

### Data Dictionary

| Variable | Definition | Response Scale | Units |
|---|---|---|---|
| participant_id | De-identified participant ID | P01–P04 | none |
| age | Participant's age | whole number | years |
| english_comfort | How comfortable the participant is speaking English | self-described (e.g., "fluent") | none |
| robot_familiarity | Prior experience with robots | 1 (never interacted with a robot) to 7 (work with robots regularly) | points |
| condition | Which robot behavior this row describes | A (speech only, no movement) or B (speech with greeting bow, listening pose, face tracking, nods and goodbye gesture) | none |
| movement | Whether robot movement was turned on | off (A) or on (B) | none |
| nod_amplitude_deg | Size of the robot's nod | 0 (A) or 10 (B) | degrees |
| warm, likeable, trustworthy, friendly | HRIES sociability items | 1 (not at all) to 7 (very much) | points |
| human_like, real, alive, natural | HRIES animacy items | 1 to 7 | points |
| self_reliant, rational, intentional, intelligent | HRIES agency items | 1 to 7 | points |
| scary, strange, creepy, weird | HRIES disturbance items | 1 to 7 | points |
| sociability | Average of the four sociability items; higher means the robot seemed more sociable | 1 to 7 | points |
| animacy | Average of the four animacy items; higher means the robot seemed more alive | 1 to 7 | points |
| agency | Average of the four agency items; higher means the robot seemed more capable of acting on its own | 1 to 7 | points |
| disturbance | Average of the four disturbance items; higher means the robot seemed more unsettling | 1 to 7 | points |
| manip_check | Agreement with "The robot responded to what I was saying with head movements" | 1 (strongly disagree) to 7 (strongly agree) | points |
| open_response | Participant's answer to "How would you describe the robot's behavior while you were talking?" | free text | none |
| trial_status | Outcome of the trial | Completed, Interrupted, Failed, or Repeated | none |

### Scoring Calculations

Each HRIES dimension score is the average of its four items:

- **Sociability** = (warm + likeable + trustworthy + friendly) ÷ 4
- **Animacy** = (human_like + real + alive + natural) ÷ 4
- **Agency** = (self_reliant + rational + intentional + intelligent) ÷ 4
- **Disturbance** = (scary + strange + creepy + weird) ÷ 4

For each participant, we calculate the within-person difference on every measure as their Condition B value minus their Condition A value. A positive difference means the score was higher when the robot moved.

In the Google Sheet, these calculations are done with formulas in the Responses and Summary tabs, so anyone can check them by entering the raw ratings.

---

## 7. Analysis and Reflection

### Results Table

Values are mean (SD) [median]. The difference column is Condition B minus Condition A, so a positive value means the score was higher when the robot moved. All HRIES scores and the manipulation check are on a 1–7 scale; higher values mean more sociable, more alive, more capable of acting on its own, and more unsettling, respectively. n = 4 in each condition.

| Measure | Condition A (speech only) | Condition B (speech + movement) | Mean Within-Participant Difference (B − A) |
|---|---|---|---|
| HRIES Sociability | 4.44 (1.52) [4.38] | 4.44 (1.92) [4.63] | 0.00 |
| HRIES Animacy | 2.44 (0.43) [2.38] | 2.75 (1.14) [2.50] | +0.31 |
| HRIES Agency | 3.50 (1.40) [3.25] | 3.81 (1.71) [3.88] | +0.31 |
| HRIES Disturbance | 1.44 (0.72) [1.13] | 1.69 (0.85) [1.50] | +0.25 |
| Manipulation Check | 2.50 (2.38) [1.50] | 5.50 (1.29) [5.50] | +3.00 |

### Participant-Level Paired Figure

Each line shows one participant's score in Condition A (speech only) and Condition B (speech + movement). Scores range from 1 to 7.

![Sociability by participant](figures/paired_sociability.png)
![Animacy by participant](figures/paired_animacy.png)
![Agency by participant](figures/paired_agency.png)
![Disturbance by participant](figures/paired_disturbance.png)

### Interpretation by HRIES Dimension

**Sociability (primary outcome; higher = warmer and friendlier).** The average was identical in both conditions (4.44). Three of four participants rated the moving robot slightly more sociable, each by only 0.25 points, while P04 rated it 0.75 points lower. Participants differed far more from each other (from 2.75 to 6.25 in Condition A) than any participant changed between conditions, so movement did not noticeably change how sociable the robot seemed.

**Animacy (higher = more alive and natural).** Animacy was low in both conditions (2.44 in A, 2.75 in B), meaning participants did not see the robot as very lifelike either way. The small increase in B came almost entirely from P03, whose score rose by 2.25 points; P01 and P04 rated the moving robot slightly lower, and P02 did not change. The effect of movement on animacy was therefore inconsistent across people.

**Agency (higher = more capable of acting on its own).** Agency rose slightly in B (3.50 to 3.81), and three of four participants gave higher scores there. P04 was again the exception, rating the moving robot lower. This suggests movement may make the robot seem a little more intentional to some people, but the change is small.

**Disturbance (higher = more unsettling).** Disturbance stayed low in both conditions (1.44 in A, 1.69 in B), so neither version of the robot was found very unsettling. The slight increase in B was driven by P04, whose score rose by 1.5 points and who described the movement as bug-like. P01 and P02 did not change, and P03's disturbance went down. Because higher disturbance is the undesirable direction, this shows that movement can backfire for some people even when others find it appealing.

**Manipulation check.** All four participants agreed more strongly in Condition B that the robot responded with head movements (2.50 in A, 5.50 in B), confirming that participants noticed the difference between conditions. P02 gave a high rating (6) even in Condition A, when the robot did not move, which may mean they interpreted the item loosely.

### Within-Participant Differences (B − A)

| Participant | Sociability | Animacy | Agency | Disturbance | Manipulation Check |
|---|---|---|---|---|---|
| P01 | +0.25 | −0.50 | +0.50 | 0.00 | +2 |
| P02 | +0.25 | 0.00 | +0.50 | 0.00 | +1 |
| P03 | +0.25 | +2.25 | +1.00 | −0.50 | +5 |
| P04 | −0.75 | −0.50 | −0.75 | +1.50 | +4 |
| Participants higher in B | 3 of 4 | 1 of 4 | 3 of 4 | 1 of 4 | 4 of 4 |

### Qualitative Coding Table

| Category | Definition | Summary of Findings | Example Paraphrase |
|---|---|---|---|
| Endearing appearance | The participant describes the robot as cute, adorable or likeable in its look or features. | Mentioned in 1 of 4 Condition A responses and 2 of 4 Condition B responses. In B, the cuteness was tied to the antennas ("ears") and their movement. | P03 (B) found the robot adorable and especially liked its little ears. |
| Generic or repetitive speech | The participant says the robot's replies were generic, plain, repeated, or unrelated to what they said. | The most consistent theme, appearing in 2 of 4 responses in each condition (P02 and P04 both times). Movement did not change this impression. | P02 (A) said every reply was generic and nothing was specific to what they had said. |
| Conversational timing | The participant comments on when or how quickly the robot responded. | Mentioned in 3 of 4 Condition A responses and none in B. Comments were mixed: replies felt oddly timed or fast to some, while one participant was impressed that it knew when they stopped talking. | P01 (A) felt the robot's responses came at odd moments. |
| Reaction to robot movement | The participant notices the robot's movement, or its absence, and says how it felt. | Mentioned in 1 of 4 Condition A responses (noting no movement) and 3 of 4 Condition B responses. Two participants found the movement pleasant and natural; one found it bug-like. | P04 (B) said the movements looked like those of an insect, such as a roach. |

### Answers to Research Questions / Hypotheses

### Convergence and Disagreement Among Evidence

### Alternative Explanations

### Threats to Validity

### Proposed Interaction Improvement

### Proposed Follow-Up Study

---

## 8. Report
