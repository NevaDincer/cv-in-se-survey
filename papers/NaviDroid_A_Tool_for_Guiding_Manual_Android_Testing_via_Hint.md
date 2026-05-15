---
title: "NaviDroid: A Tool for Guiding Manual Android Testing via Hint Moves"
year: 2022
venue: "ICSE (Companion)"
doi: 10.1145/3510454.3516848
url: https://doi.org/10.1145/3510454.3516848
source: Snowball
snowball_from: "2443; 2805"
status: done
se_area: mobile app testing
se_task: manual testing guidance via visual hint moves
platform: Android
cv_technique: GUI screenshot analysis for state transition graph construction
visual_artifact: mobile app screenshot
rationale: CV analyzes runtime GUI screenshots to identify and visualize untested states as overlay hints for human testers
evaluation: user study showing more states and activities covered and more bugs detected in less time vs control group
challenge: manual testing is inefficient due to repeated actions and missed functionalities without structured guidance
---

## Notes

NaviDroid augments manual testing by overlaying visual hints on the live GUI, guiding testers toward unexplored states via a dynamic programming path planner. CV builds the STG by capturing and comparing screenshots at runtime. Interesting hybrid of automated analysis and human-in-the-loop testing. Demo paper with user study validation.