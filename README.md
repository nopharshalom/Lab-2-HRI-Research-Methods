# INFO 5356-030 Lab 2: HRI Research Methods

## Team Members
Nophar Shalom, Bailey Carlson, Wiam Salih

---

## 1. Teleoperation on the Physical Robot

### Final App Cycle Clip

### Stage Markers (Screenshot / Log Excerpt)

### Sim-to-Real Comparison

---

## 2. Hello World Application

### Demonstration Clip

### Stage Markers (Screenshot / Log Excerpt)

### Changes, Expected Outcomes, and Actual Outcomes

---

## 3. Custom App on the Physical Robot

### Final-Project Topic and App Capabilities

### Integration Map

| Source App | Capability Reused / Modified | Interaction Goal | Final-Project Connection |
|---|---|---|---|
| | | | |

### Manipulation Parameter

| Parameter | Units | Condition A | Condition B |
|---|---|---|---|
| | | | |

### Setup, Launch, and Stop Instructions

### Robot-Only Demonstration

#### Condition A

#### Condition B

---

## 4. HRI Research Questions

### Problem Statement
When people talk to someone, they rely on small listener signals, like nods, to judge whether they are being heard. These signals are called backchannels (Yngve, 1970). Social robots are increasingly deployed as conversational partners in homes, schools and care settings, yet many stay motionless while a person speaks. A robot that stays still while listening may come across as inattentive or less socially present, even if its spoken responses are appropriate. Prior work shows that nonverbal backchanneling from virtual agents increases rapport (Gratch et al., 2007) and that robot backchanneling affects how engaged speakers are (Park et al., 2017). Less is known about whether a simple, low-degree-of-freedom robot like Reachy Mini can produce this effect with head nods alone. This pilot study tests whether adding active-listening nods changes how sociable adults perceive Reachy Mini to be during a short conversation, and whether nods affect how long participants choose to speak.

### Construct Map

| Claim | Manipulation | Measures | Expected Evidence |
|---|---|---|---|
| Active-listening nods make Reachy Mini seem more sociable | `nod_amplitude_deg`: 0° (A) vs 10° (B), triggered at speech pauses | HRIES sociability (primary) | Higher sociability scores in Condition B than in Condition A for most participants |
| Participants notice the listening behavior | Same as above | Manipulation-check item | Higher agreement in Condition B than in Condition A |
| Nods encourage participants to keep talking | Same as above | Speaking time (s) | Longer speaking time in Condition B than in Condition A |
| Nods may feel unnatural if mistimed (exploratory) | Same as above | HRIES disturbance; open-ended responses | No predicted direction; qualitative comments on timing or naturalness |

#### Independent Variable

`nod_amplitude_deg` is the peak downward head pitch, in degrees, of the nod the robot performs when it detects a pause in the participant's speech.

- **Condition A (baseline):** 0°. The pause detector still runs and logs each pause event, but no movement is produced.
- **Condition B (comparison):** 10°. The robot performs one nod down and back to neutral over 0.6 s.

In both conditions, a pause is detected when the microphone registers at least 700 ms of silence following speech. Consecutive nods are separated by at least 3 s.

#### Outcomes

- **Primary outcome:** HRIES sociability score. This is the mean of the four sociability items, each rated on a 7-point scale, so scores range from 1 to 7. Higher values mean the robot was perceived as more sociable.
- **Secondary outcomes:** HRIES animacy, agency and disturbance scores, each the mean of its four items. Higher values mean greater animacy, agency or disturbance, respectively.
- **Objective outcome:** total participant speaking time in seconds during the 3-minute conversation window, computed from the app's audio log.

#### Manipulation Check

After each condition, participants rate the statement "The robot responded to what I was saying with head movements" from 1 (strongly disagree) to 7 (strongly agree). The manipulation is considered salient if ratings are higher in Condition B than in Condition A.

#### Controls

- The pause-detection threshold (700 ms) and minimum nod interval (3 s) are the same in both conditions.
- The robot's idle pose, antenna position, gaze direction, and start and end pose are identical in both conditions.
- Two conversation prompts of similar difficulty are used, and the pairing of prompt to condition is counterbalanced.
- Each conversation window lasts 3 minutes.
- The room layout, participant seat distance from the robot, lighting and facilitator position are the same for every session.
- The facilitator reads a standardized script and does not react to the robot's behavior.
- Condition order is counterbalanced (AB, BA, AB, BA).

#### Potential Confounds

- **Prompt content:** One prompt may be easier to talk about. Counterbalancing prompts across conditions mitigates this.
- **Order and novelty effects:** Participants may talk more or rate the robot differently in the second session simply because the robot is no longer novel. Counterbalancing condition order mitigates this.
- **Detection errors:** Missed or false pause detections may change the number and timing of nods across participants. Each pause event is logged so this can be examined.
- **Individual talkativeness:** Some participants naturally speak more than others. The within-subjects design means each person is compared with themselves.
- **Facilitator presence:** Participants may speak to please the facilitator rather than responding to the robot. The facilitator sits out of the participant's line of sight.

#### Measurement Scales and Construct Validity

The HRIES (Spatola, Kühnlenz & Cheng, 2021) has 16 items rated on a 7-point scale, with four items per dimension:

- **Sociability:** warm, likeable, trustworthy, friendly
- **Animacy:** human-like, real, alive, natural
- **Agency:** self-reliant, rational, intentional, intelligent
- **Disturbance:** scary, strange, creepy, weird

The scale was developed and validated through factor analysis across multiple studies, and each dimension is scored separately. With only four participants, internal-consistency statistics such as Cronbach's alpha would not be meaningful, so they are not reported. Construct validity is supported instead by three things: the manipulation check, the objective speaking-time measure, and the open-ended responses. Together these indicate whether participants noticed the nods and interpreted them as listening behavior.

### Research Questions and Hypotheses

**H1 (confirmatory):** Participants will report higher HRIES sociability scores in the nodding condition (B, 10°) than in the still condition (A, 0°).

**H2 (confirmatory):** Participants will speak longer in the nodding condition (B) than in the still condition (A).

**RQ1 (exploratory):** How do active-listening nods affect participants' HRIES disturbance ratings and their descriptions of the robot's behavior?

---

## 5. HRI User Study

### Conditions Table

| Element | Condition A | Condition B | Held Constant |
|---|---|---|---|
| Primary factor | | | |
| Robot behavior | | | |
| Interaction | | | |

### Participants

#### Target Population and Sampling Rationale

#### Demographics, Robot Familiarity, and Condition Order

| Participant ID | Demographics | Robot Familiarity | Condition Order |
|---|---|---|---|
| P01 | | | |
| P02 | | | |
| P03 | | | |
| P04 | | | |

#### Limits on Transferability

### Study Task

#### Task and Standardized Instructions

#### Trial Definitions

| Trial Status | Definition |
|---|---|
| Completed | |
| Interrupted | |
| Failed | |
| Repeated | |

#### Setting and Environmental Controls

### Facilitator Script

### Measures

#### HRIES Questionnaire

#### Manipulation-Check Item

#### Objective Behavioral Measure

#### Open-Ended Question

### Interruptions, Missing Data, Robot Faults, and Protocol Deviations

---

## 6. Research Data

### Datasets

### Data Dictionary

| Variable | Definition | Response Scale | Units | Missing-Data Code |
|---|---|---|---|---|
| | | | | |

### Scoring Calculations

### Missing Data, Exclusions, and Corrections

---

## 7. Analysis and Reflection

### Participant Accounting

### Results Table

| Measure | Condition A | Condition B | Within-Participant Difference (A − B) |
|---|---|---|---|
| HRIES Sociability | | | |
| HRIES Animacy | | | |
| HRIES Agency | | | |
| HRIES Disturbance | | | |
| Objective Measure | | | |

### Participant-Level Paired Figure

### Interpretation by HRIES Dimension

### Qualitative Coding Table

| Category | Definition | Summary of Findings | Example Excerpt / Paraphrase |
|---|---|---|---|
| | | | |

### Answers to Research Questions / Hypotheses

### Convergence and Disagreement Among Evidence

### Alternative Explanations

### Threats to Validity

### Proposed Interaction Improvement

### Proposed Follow-Up Study

---

## 8. Report

### Introduction

### Method

### Results

### Discussion

### References

### Appendix

---

## How to Reproduce the Analysis
