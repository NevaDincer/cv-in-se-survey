---
title: Cross-device record and replay for Android apps
year: 2022
venue: ESEC/FSE
doi: 10.1145/3540250.3549083
url: https://doi.org/10.1145/3540250.3549083
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: cross-device test script record and replay
platform: Android
cv_technique: GUI visual structure analysis for widget matching
visual_artifact: mobile app screenshot
rationale: visual GUI structure is used to adapt recorded interactions to different screen sizes and orientations during replay
evaluation: over 1,000 replay settings; competitive with state-of-the-art on same-device replay and beyond known non-search-based tools on cross-device cases
challenge: apps restructure their GUIs responsively across screen sizes, breaking naive locator-based replay
---

## Notes

Rx uses a greedy one-pass algorithm guided by the least-surprise principle in GUI design to resolve widget identity across devices. 

CV role is supporting widget matching rather than central. 

Relevant alongside LIRAT for the "cross-device test portability" cluster, but simpler and Android-only.