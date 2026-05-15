---
title: "The Metamorphosis: Automatic Detection of Scaling Issues for Mobile Apps"
year: 2023
venue: ASE
doi: 10.1145/3551349.3556935
url: https://doi.org/10.1145/3551349.3556935
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: UI scaling issue detection
platform: Android
cv_technique: visual inconsistency detection between default and scaled UI screenshots
visual_artifact: mobile app screenshot
rationale: CV compares screenshots at different display scales to detect text truncation and component overlap caused by font/size scaling
evaluation: "97% precision and recall for issue page detection; 84% precision, 91% recall for issue view detection; 21 new bugs found on F-droid"
challenge: existing UI display issue techniques do not handle scaling-specific inconsistencies like text truncation under enlarged fonts
---

## Notes

dVermin frames scaling issue detection as a visual inconsistency problem between two display configurations, requiring no source code access. 

Relevant to the "CV for accessibility-related UI testing" cluster alongside [[MotorEase_Automated_Detection_of_Motor_Impairment_Accessibil]], but focuses on display scaling rather than interaction patterns.