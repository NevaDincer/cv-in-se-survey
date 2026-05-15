---
title: "Too Much Accessibility is Harmful! Automated Detection and Analysis of Overly Accessible Mobile UI Elements"
year: 2023
venue: ASE
doi: 10.1145/3551349.3560424
url: https://doi.org/10.1145/3551349.3560424
source: ACM DL
snowball_from:
status: done
se_area: accessibility testing
se_task: over-accessible UI element detection
platform: Android
cv_technique:
visual_artifact:
rationale: no CV involvement; OverSight uses Accessibility API interactions and dynamic AT verification rather than visual analysis
evaluation: detected previously unknown security threats and accessibility issues on real-world Android apps
challenge: over-access allows bypassing protected UI elements via assistive technologies, a security and accessibility dual problem
---

## Notes

OverSight detects the over-access problem, the opposite of under-accessibility, where assistive technologies expose functionality that should be hidden. 

Approach is API-based and dynamic, not visual. 

==Edge case for inclusion scope accessibility testing theme but no CV.==