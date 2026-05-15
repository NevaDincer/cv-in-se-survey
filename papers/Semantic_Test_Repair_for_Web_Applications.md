---
title: Semantic Test Repair for Web Applications
year: 2023
venue: ESEC/FSE
doi: 10.1145/3611643.3616324
url: https://doi.org/10.1145/3611643.3616324
source: ACM DL
snowball_from:
status: done
se_area: web app testing
se_task: automated web test script repair
platform: web
cv_technique: visual appearance matching
visual_artifact: webpage screenshot
rationale: visual element appearances are used alongside semantic similarity to locate broken web elements during test repair
evaluation: "84% average repair ratio on 6 real-world web apps, outperforms 3 baselines"
challenge: DOM-based and visual locators both fail when semantic context of elements is ignored
---

## Notes

Semter captures semantic information from test executions to repair broken locators, complementing rather than replacing visual approaches. CV is one signal among several; semantics is the main contribution. 