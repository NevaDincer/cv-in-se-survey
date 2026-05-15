---
title: Enhancing GUI Exploration Coverage of Android Apps with Deep Link-Integrated Monkey
year: 2024
venue: ACM Trans. Softw. Eng. Methodol.
doi: 10.1145/3664810
url: https://doi.org/10.1145/3664810
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: GUI exploration coverage enhancement
platform: Android
cv_technique:
visual_artifact:
rationale: no CV involvement; approach uses Android deep links and intent triggering to escape exploration loops
evaluation: "+27.2% activity coverage, +21.13% method coverage, +23.81% crash detection over state-of-the-art baselines"
challenge: testing tools get stuck in loops and miss activities with hidden or hard-to-reach entry points
---

## Notes

Delm integrates deep link triggering into Monkey to escape GUI exploration loops and reach concealed activities. 

==No CV used. GUI testing paper but purely interaction-based without visual analysis. Edge case==
