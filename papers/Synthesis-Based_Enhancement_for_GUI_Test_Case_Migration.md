---
title: Synthesis-Based Enhancement for GUI Test Case Migration
year: 2024
venue: ISSTA
doi: 10.1145/3650212.3680327
url: https://doi.org/10.1145/3650212.3680327
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: GUI test case migration and synthesis
platform: Android
cv_technique: GUI state matching via screenshots
visual_artifact: mobile app screenshot
rationale: GUI states are identified and sequenced using visual screen representations to align and merge migrated test cases
evaluation: "86%, 333%, 300% improvement over Craftdroid, AppFlow, ATM on 30 apps, 34 functionalities, 127 test cases"
challenge: individually migrated test cases are incomplete and require synthesis to become directly executable
---

## Notes

 synthesizes a single functional test case by merging multiple imperfect migrations from different source apps, using GUI state sequences to align events and assertions. CV role is supporting state identification rather than central. 

Relevant for the "cross-app test reuse" cluster.