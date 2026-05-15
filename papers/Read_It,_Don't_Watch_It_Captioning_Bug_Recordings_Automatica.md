---
title: "Read It, Don't Watch It: Captioning Bug Recordings Automatically"
year: 2023
venue: ICSE
doi: 10.1109/ICSE48619.2023.00197
url: https://doi.org/10.1109/ICSE48619.2023.00197
source: ACM DL
snowball_from:
status: done
se_area: bug reporting
se_task: automatic captioning of bug screen recordings
platform: Android
cv_technique: "video segmentation, CNN-based action attribute inference, GUI element detection"
visual_artifact: mobile app screen recording
rationale: CV segments recordings into action clips and infers spatial and temporal action attributes from frames to generate natural language step descriptions
evaluation: automated experiments on action inference accuracy plus user study confirming usefulness for bug replay
challenge: translating spatial and temporal video information into compact semantic descriptions without app instrumentation
---

## Notes
Treats bug recordings like movie scenes, segmenting them into TAP/SCROLL/INPUT clips then inferring attributes to generate subtitle-style descriptions. 

Purely image-based and non-intrusive.

Pairs with [[SeeAction_Towards_Reverse_Engineering_How-What-Where_of_HCI]] for the "CV extracting SE-relevant actions from visual recordings" cluster.