---
title: Deep learning-based prototyping of android GUI from hand-drawn mockups
year: 2020
venue: IET Software
doi: 10.1049/iet-sen.2019.0378
url: https://doi.org/10.1049/iet-sen.2019.0378
source: Snowball
snowball_from: "2523; 2805"
status: done
se_area: code generation
se_task: hand-drawn sketch-to-Android GUI prototype generation
platform: Android
cv_technique: YOLOv5 object detection for GUI element detection and classification
visual_artifact: hand-drawn mockup
rationale: CV detects and classifies hand-drawn GUI elements via YOLOv5 then aligns them to generate Android prototypes
evaluation: "98.54% recognition accuracy on hand-drawn GUI structures from 5 developers"
challenge: hand-drawn input is underexplored compared to computer-generated mockups; irregular strokes require robust detection
---

## Notes

Uses YOLOv5 to detect and classify hand-drawn GUI components then assembles them into Android prototypes matching the sketch layout. One of the few sketch-to-code papers using hand-drawn rather than wireframe input. Useful early reference for the sketch-based GUI generation subcluster.