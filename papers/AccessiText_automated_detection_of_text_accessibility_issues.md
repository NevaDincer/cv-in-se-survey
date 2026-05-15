---
title: "AccessiText: automated detection of text accessibility issues in Android apps"
year: 2022
venue: ESEC/FSE
doi: 10.1145/3540250.3549118
url: https://doi.org/10.1145/3540250.3549118
source: Snowball
snowball_from: "2778; 2805"
status: done
se_area: accessibility testing
se_task: text accessibility issue detection for Text Scaling Assistive Service compatibility
platform: Android
cv_technique: "OCR and screenshot analysis for text rendering and layout issue detection"
visual_artifact: mobile app screenshot
rationale: CV analyzes UI screenshots to detect text scaling issues that only manifest visually when TSAS is active
evaluation: "88.27% precision, 95.76% recall on 30 real-world Android apps"
challenge: text accessibility issues only appear under TSAS activation and require visual inspection of rendered output
---

## Notes

AccessiText detects five categories of text scaling accessibility issues by combining screenshot analysis with dynamic metadata, targeting TSAS incompatibility. Complements MotorEase in the accessibility testing cluster with a focus on low vision users rather than motor impairment.
