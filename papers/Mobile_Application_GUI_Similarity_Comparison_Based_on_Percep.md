---
title: Mobile Application GUI Similarity Comparison Based on Perceptual Hash for Automated Robot Testing
year: 2021
venue: International Conference on Applied Algorithms
doi: 10.1109/icaa53760.2021.00052
url: https://doi.org/10.1109/icaa53760.2021.00052
source: Snowball
snowball_from: 397
status: done
se_area: Testing
se_task: "GUI similarity comparison"
platform: Mobile
cv_technique: "Image Differencing; Perceptual Hashing; YOLOv3"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "Accuracy metrics"
challenge: "Distinguishing meaningful visual changes from cosmetic ones"
---

## Notes

Uses YOLOv3 to extract UI component info, then perceptual hashing to detect isomorphic GUIs and merge redundant nodes in the test model. The core CV contribution is reducing the exploration graph for black-box automated testing on closed-source apps. Perceptual hashing here is doing structural deduplication, not traditional visual testing.