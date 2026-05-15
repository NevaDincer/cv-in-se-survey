---
title: "Unblind Your Apps: Predicting Natural-Language Labels for Mobile GUI Components by Deep Learning"
year: 2020
venue: ICSE
doi: 10.1145/3377811.3380327
url: https://doi.org/10.1145/3377811.3380327
source: Snowball
snowball_from: "772; 636; 2794; 1779; 989; 2649; 2610; 2746; 2552; 299; 478; 2365; 1786; 2782"
status: done
se_area: accessibility
se_task: automatic accessibility label generation for image-based GUI components
platform: Android
cv_technique: deep learning image classifier for button label prediction
visual_artifact: mobile app screenshot
rationale: CV classifies image-based button icons to predict natural-language accessibility labels for screen reader support
evaluation: "outperforms real Android developers in label quality; trained on large-scale Google Play apps; analysis of 10,408 apps showing 77%+ have missing labels"
challenge: over 77% of Android apps have missing accessibility labels due to developer unawareness and lack of visual context for description
---

## Notes

LabelDroid learns from commercial app icons to generate screen reader labels for unlabeled image buttons, directly improving app accessibility at scale. 

Foundational paper for the "CV enabling accessibility" cluster

predates MotorEase and complements it by addressing the label generation rather than violation detection problem.
