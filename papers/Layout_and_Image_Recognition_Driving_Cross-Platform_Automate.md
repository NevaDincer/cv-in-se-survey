---
title: Layout and Image Recognition Driving Cross-Platform Automated Mobile Testing
year: 2021
venue: ICSE
doi: 10.1109/ICSE43902.2021.00139
url: https://doi.org/10.1109/ICSE43902.2021.00139
source: IEEE Xplore
snowball_from:
status: done
se_area: mobile app testing
se_task: cross-platform test script replay
platform: "Android, iOS, mobile web"
cv_technique: "widget feature matching, layout hierarchy extraction"
visual_artifact: mobile app screenshot
rationale: CV extracts UI structure from screenshots to enable platform-independent widget localization during test replay
evaluation: "65.85% replay accuracy on Android (+8.74%), 35.26% on iOS (+35%) over state-of-the-art"
challenge: same app has structurally similar but platform-divergent UI layouts across Android, iOS, and mini-programs
---

## Notes

LIRAT uses CV to parse screenshot layout hierarchies and match widgets across platforms, converting recorded test scripts into platform-independent form.

The core bet is that visual UI similarity across platforms is exploitable even without access to source code or platform APIs. 

Strong example of CV enabling cross-platform test portability.