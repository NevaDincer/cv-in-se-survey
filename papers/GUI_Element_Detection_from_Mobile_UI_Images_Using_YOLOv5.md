---
title: GUI Element Detection from Mobile UI Images Using YOLOv5
year: 2022
venue: MobiWIS
doi: 10.1007/978-3-031-14391-5_3
url: https://doi.org/10.1007/978-3-031-14391-5_3
source: Snowball
snowball_from: "2805"
status: done
se_area: GUI design
se_task: GUI element detection from mobile UI screenshots
platform: "mobile, web"
cv_technique: YOLOv5 object detection
visual_artifact: mobile app screenshot
rationale: CV detects GUI elements from UI images to enable downstream automation and cross-platform design tasks
evaluation: "+15.69% mAP over SSD baseline on VINS dataset (450 UI samples for testing)"
challenge: GUI element detection must handle diverse element types across platforms while remaining fast enough for practical automation
---

## Notes

Benchmarks YOLOv5 for GUI element detection using the VINS dataset, outperforming the prior SSD-based approach. Technical contribution is incremental — swapping in a newer detector. Useful as a methods reference for the GUI element detection infrastructure that underlies many other papers in the survey.