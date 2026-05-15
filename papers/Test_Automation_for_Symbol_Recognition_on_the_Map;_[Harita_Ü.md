---
title: Test Automation for Symbol Recognition on the Map
year: 2023
venue: Conference on Signal Processing and Communications (SIU)
doi: 10.1109/SIU59756.2023.10223831
url: https://doi.org/10.1109/SIU59756.2023.10223831
source: Scopus
snowball_from: database
status: done
se_area: Testing
se_task: Automated visual verification of military map symbols in software testing
platform: Desktop
cv_technique: Template Matching; HOG+SVM; Faster R-CNN; YOLOv5
visual_artifact: Natural image
rationale: Context-driven
evaluation: mAP (Faster R-CNN 0.915; YOLOv5 0.865)
challenge: Overlapping symbols; scale variation; transparent symbols on complex backgrounds
---

## Notes
Manual symbol verification is error-prone and costly in military software CV automates visual test oracle.

Faster R-CNN best performer. 

(Turkish paper) ITU + Aselsan.