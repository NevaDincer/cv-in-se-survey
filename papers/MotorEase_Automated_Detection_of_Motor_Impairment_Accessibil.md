---
title: "MotorEase: Automated Detection of Motor Impairment Accessibility Issues in Mobile Apps"
year: 2024
venue: ICSE
doi: 10.1145/3597503.3639167
url: https://doi.org/10.1145/3597503.3639167
source: ACM DL
snowball_from:
status: done
se_area: accessibility testing
se_task: motor impairment accessibility issue detection
platform: Android
cv_technique: "UI element detection, visual distance and size measurement"
visual_artifact: mobile app screenshot
rationale: CV measures visual properties of UI elements (touch target size, icon spacing, expanding sections) to detect accessibility guideline violations
evaluation: "~90% accuracy, <9% false positive rate on 555 annotated violations across 1599 screens from 70 apps"
challenge: motor impairment guidelines require spatial and geometric reasoning about UI elements not captured by text analysis alone
---

## Notes

MotorEase targets an underserved group in accessibility research by detecting four motor-impairment-specific UI violations using CV-based geometric analysis. 

Complements vision/hearing accessibility tools with a different set of guidelines. 

