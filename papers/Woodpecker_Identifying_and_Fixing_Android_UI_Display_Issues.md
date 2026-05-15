---
title: "Woodpecker: Identifying and Fixing Android UI Display Issues"
year: 2022
venue: ICSE-Companion 2022
doi: 10.1145/3510454.3522681
url: https://doi.org/10.1145/3510454.3522681
source: IEEE Xplore
snowball_from:
status: done
se_area: Maintenance
se_task: Automated detection and repair of Android UI display issues
platform: Mobile
cv_technique: CV-based screenshot analysis for UI display issue detection
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "87% detection; 77% repair on 30 real issues; 112 new issues in 256 apps; 76 repairs accepted by developers"
challenge: "Android fragmentation; diverse UI component combinations; locating buggy source code from screenshot"
---

## Notes

Detects UI display bugs from screenshots, localizes them to source code, and auto-repairs with templates. 

Strong real-world validation: 76 developer-accepted fixes. 

Unique in combining CV detection with automated code repair. 

ICSE Companion 2022.