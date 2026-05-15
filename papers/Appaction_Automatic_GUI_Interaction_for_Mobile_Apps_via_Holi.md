---
title: "Appaction: Automatic GUI Interaction for Mobile Apps via Holistic Widget Perception"
year: 2023
venue: ESEC/FSE
doi: 10.1145/3611643.3613885
url: https://doi.org/10.1145/3611643.3613885
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: automatic GUI interaction and valid input generation
platform: Android
cv_technique: multimodal model for GUI widget understanding
visual_artifact: mobile app screenshot
rationale: CV analyzes GUI screenshots holistically to understand widget semantics and generate contextually valid test inputs
evaluation: deployed at Meituan with 600M+ users; demonstrated effectiveness on numerous commercial form pages
challenge: diverse and complex commercial GUIs (e.g., order forms) require understanding widget context beyond simple element detection
---

## Notes

Appaction learns from human GUI perception experience to infer valid inputs for form-heavy commercial apps, going beyond click-based exploration to semantic input generation. 

Another industrial-scale deployment paper alongside [[Visual_Test_Framework_Enhancing_Software_Test_Automation_wit]]; useful for contrasting CV adoption patterns across different companies and app types.