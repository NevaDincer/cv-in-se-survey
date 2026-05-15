---
title: Detecting Outdated Screenshot from GUI Document
year: 2025
venue: ACM Trans. Softw. Eng. Methodol.
doi: 10.1145/3750041
url: https://doi.org/10.1145/3750041
source: ACM DL
snowball_from:
status: done
se_area: documentation maintenance
se_task: outdated screenshot detection in GUI documents
platform: "Android, VS Code"
cv_technique: image classification for screenshot currency detection
visual_artifact: GUI documentation screenshot
rationale: CV classifies whether screenshots in software documentation match the current application UI
evaluation: "high F1 on 10-app benchmark; 20 outdated screenshots found on 50 Android app websites; 17 in VS Code docs, all confirmed and fixed"
challenge: outdated screenshots differ subtly from current UIs, requiring targeted region analysis rather than whole-image comparison
---

## Notes

DOSUD automatically detects stale screenshots in software documentation by training a classifier on extracted screenshot-UI pairs. 

VS Code developers confirming and fixing all reported bugs is strong industrial validation.

CV for documentation quality