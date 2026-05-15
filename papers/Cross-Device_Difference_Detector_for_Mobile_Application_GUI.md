---
title: Cross-Device Difference Detector for Mobile Application GUI Compatibility Testing
year: 2022
venue: "ICST (Workshop)"
doi: 10.1109/ICSTW55395.2022.00052
url: https://doi.org/10.1109/ICSTW55395.2022.00052
source: IEEE Xplore
snowball_from:
status: done
se_area: GUI testing
se_task: Cross-device compatibility testing
platform: "Android, iOS"
cv_technique: "image differencing, element detection"
visual_artifact: mobile app screenshot
rationale: CV is used to detect visual differences between screenshots from different devices, directly automating a manual visual inspection task
evaluation: "accuracy: 0.924 on 725 screenshot pairs from 3 Baidu apps across 10 devices"
challenge: resolution normalization across devices with different screen sizes
---

## Notes

CdDiff takes screenshot pairs from two devices, extracts UI elements via a page understanding module, then matches them to localize visual discrepancies. 

It frames GUI compatibility testing as an image difference detection problem, bypassing the need for source code or device-specific metadata. 

Good example of CV replacing tedious manual visual QA in mobile testing pipelines.