---
title: GUI-Guided Test Script Repair for Mobile Apps
year: 2022
venue: TSE
doi: 10.1109/TSE.2020.3007664
url: https://doi.org/10.1109/TSE.2020.3007664
source: Scopus
snowball_from:
status: done
se_area: GUI Testing
se_task: Automated repair of broken GUI test scripts after app updates
platform: "Mobile (Android, iOS)"
cv_technique: Screenshot-based GUI change detection via CV matching
visual_artifact: App screenshots across versions
rationale: CV infers GUI changes between app versions to guide test script repair without source code access
evaluation: "63.7% test action preservation on 22 Android apps; 38.8% on 6 iOS apps"
challenge: Mobile apps often lack accessible source code; image-heavy GUIs make static analysis insufficient
---

## Notes

Meter treats mobile apps as black boxes and uses CV on screenshots to detect GUI changes between versions, then repairs broken test scripts accordingly. First CV-based approach to mobile test script repair and it works on both Android and iOS. The 63.7% preservation rate leaves room for improvement but the black-box framing is a practical strength for real-world applicability.
