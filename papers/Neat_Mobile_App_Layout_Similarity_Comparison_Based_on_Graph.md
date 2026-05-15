---
title: "Neat: Mobile App Layout Similarity Comparison Based on Graph Convolutional Networks"
year: 2024
venue: "Companion ACM International Conference on the Foundations of Software Engineering"
doi: 10.1145/3663529.3663832
url: https://doi.org/10.1145/3663529.3663832
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: GUI layout similarity verification across devices and versions
platform: mobile
cv_technique: "GUI element detection, GCN-based layout feature extraction"
visual_artifact: mobile app screenshot
rationale: CV detects UI elements and extracts layout features to automate cross-device layout assertion without source code access
evaluation: empirical evaluation plus industrial application deployment reported
challenge: multi-model cross-version layout verification is too resource-intensive for manual testing
---

## Notes

Neat treats layout comparison as a graph similarity problem that ğs UI elements become nodes, spatial relations become edges, then GCN encodes the structure for comparison. 

Non-intrusive and end-to-end, making it deployable in CI pipelines. 

Close relative to [[Cross-Device_Difference_Detector_for_Mobile_Application_GUI]] but with a graph-structural rather than pixel-level approach.

