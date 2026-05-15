---
title: "Avgust: automating usage-based test generation from videos of app executions"
year: 2022
venue: ESEC/FSE
doi: 10.1145/3540250.3549134
url: https://doi.org/10.1145/3540250.3549134
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: usage-based test generation from screen recordings
platform: Android
cv_technique: neural image understanding for UI screen and action classification
visual_artifact: mobile app screen recording
rationale: CV processes video frames to classify UI screens and user inputs, encoding app usage semantics into a state machine for test synthesis
evaluation: "69% test success rate on 374 videos across 18 apps; classifiers outperform state of the art"
challenge: generating usage-based tests requires understanding UI screen semantics and user input intent, not just maximizing coverage
---

## Notes
Avgust generalizes V2S by targeting usage-based tests rather than simple replay, it encodes video-derived usage patterns into an app-agnostic state machine then migrates them to new target apps.

CV for video-to-test generation cluster after V2S.