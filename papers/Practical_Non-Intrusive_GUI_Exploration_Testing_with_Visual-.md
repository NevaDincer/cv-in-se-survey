---
title: Practical Non-Intrusive GUI Exploration Testing with Visual-based Robotic Arms
year: 2024
venue: ICSE 2024
doi: 10.1145/3597503.3639161
url: https://doi.org/10.1145/3597503.3639161
source: Scopus
snowball_from:
status: done
se_area: Testing
se_task: Non-intrusive GUI exploration testing via robotic arm and CV
platform: Mobile
cv_technique: "CV-based screen and widget detection (adaptive to different screen sizes)"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "Tested on 20 real-world mobile apps; industrial embedded system case study"
challenge: "Fixed screen assumption in prior work; XY-plane only robotic arms; compatibility bugs ignored"
---

## Notes

Physical 4-DOF robotic arm clicks the screen — no framework injection needed. 

CV detects widgets from screenshots. 

Targets embedded/custom OS where intrusive testing is impossible. 

More sophisticated version of [[Image_Processing-Enabled_Validation_for_Robotic_Test_Automat]] paper, from ICSE. 

