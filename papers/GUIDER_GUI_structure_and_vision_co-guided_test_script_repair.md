---
title: "GUIDER: GUI structure and vision co-guided test script repair for Android apps"
year: 2021
venue: ISSTA
doi: 10.1145/3460319.3464830
url: https://doi.org/10.1145/3460319.3464830
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: GUI test script repair after app evolution
platform: Android
cv_technique: visual widget appearance matching
visual_artifact: mobile app screenshot
rationale: CV provides visual widget features that are combined with structural DOM information to identify widget correspondences across app versions
evaluation: "88.8% and 54.9% more test actions repaired correctly over visual-only and structure-only baselines on WeChat"
challenge: neither visual nor structural information alone is sufficient to reliably match widgets after app updates
---

## Notes

GUIDER fuses visual and structural widget features for test repair, showing that the combination outperforms either signal alone by a large margin.
Clean ablation story. 

Good reference for the "multimodal widget matching" cluster alongside UITestFix and Semter.