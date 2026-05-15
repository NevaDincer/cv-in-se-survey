---
title: Comprehensive Semantic Repair of Obsolete GUI Test Scripts for Mobile Applications
year: 2024
venue: ICSE
doi: 10.1145/3597503.3639108
url: https://doi.org/10.1145/3597503.3639108
source: Snowball
snowball_from: "2778; 2805"
status: done
se_area: mobile app testing
se_task: GUI test script repair after app evolution
platform: Android
cv_technique: "deep learning and feature matching for GUI element recognition"
visual_artifact: mobile app screenshot
rationale: CV extracts external semantic information from GUI screenshots to identify widget correspondences across app versions during repair
evaluation: outperforms METER and GUIDER on 20 Android apps
challenge: existing image and layout-based repair methods fail when GUI changes between versions are substantial
---

## Notes

COSER combines visual GUI semantics with source code internal semantics to handle larger structural changes than prior repair tools. Extends GUIDER's vision-structure fusion approach with additional source code context. Relevant for the "GUI test repair" cluster alongside GUIDER, UITestFix, and Semter.