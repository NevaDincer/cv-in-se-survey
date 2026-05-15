---
title: Feature Matching-based Approaches to Improve the Robustness of Android Visual GUI Testing
year: 2021
venue: TOSEM
doi: 10.1145/3477427
url: https://doi.org/10.1145/3477427
source: Snowball
snowball_from: 2805
status: done
se_area: Testing
se_task: "Feature matching for Android test robustness"
platform: Mobile
cv_technique: "Template Matching; Feature Matching"
visual_artifact: Full-interface
rationale: "Context-driven; Robustness"
evaluation: "Accuracy metrics"
challenge: "Sensitivity to resolution, scale, and device fragmentation"
---

## Notes

Compares fullscreen vs. cropped widget locators for cross-device visual GUI testing on Android, benchmarked against EyeAutomate and Sikuli. The fullscreen approach wins, yielding a 30% increase in passing tests across devices. Good reference for the argument that CV-based locators outperform coordinate-based ones when device fragmentation is the bottleneck.