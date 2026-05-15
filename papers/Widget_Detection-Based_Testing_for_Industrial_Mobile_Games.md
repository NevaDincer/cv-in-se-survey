---
title: Widget Detection-Based Testing for Industrial Mobile Games
year: 2023
venue: ICSE-SEIP
doi: 10.1109/ICSE-SEIP58684.2023.00021
url: https://doi.org/10.1109/ICSE-SEIP58684.2023.00021
source: ACM DL
snowball_from:
status: done
se_area: game testing
se_task: automated GUI testing for mobile games
platform: "Android, iOS"
cv_technique: widget detection from screenshots
visual_artifact: mobile game screenshot
rationale: CV detects GUI widgets from screenshots as the sole input to enable non-intrusive automated testing without source code modification
evaluation: "3x more unique UI coverage than Monkey on gaming scenarios at NetEase Games; generalizes to general mobile apps without fine-tuning"
challenge: dynamic loading and visual effects in games make standard app testing tools unreliable; functionality testing coverage remains limited
---

## Notes

WDTEST is deployed at NetEase Games using the largest game GUI dataset built to date. The accompanying developer survey reveals that testers trust CV-based testing for compatibility but not for functional coverage 

Practical limitation to cite in survey discussions on industrial CV adoption.