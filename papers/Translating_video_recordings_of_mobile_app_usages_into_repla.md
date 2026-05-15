---
title: Translating video recordings of mobile app usages into replayable scenarios
year: 2020
venue: ICSE
doi: 10.1145/3377811.3380328
url: https://doi.org/10.1145/3377811.3380328
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: video-to-test scenario translation
platform: Android
cv_technique: "object detection, image classification for user action recognition"
visual_artifact: mobile app screen recording
rationale: CV detects and classifies GUI-based user actions in screen recordings to automatically generate replayable test scenarios
evaluation: "89% replay success rate on 175 videos with 3,534 actions from 80+ apps; validated with 3 industrial partners"
challenge: screen recordings are graphical artifacts with no textual structure, requiring CV to extract actionable test steps
---

## Notes

V2S is an early and influential paper applying object detection and image classification to convert screen recordings into executable test scripts without app instrumentation. 

==Foundational for the "CV extracting SE artifacts from visual recordings" cluster alongside CAPdroid and SeeAction.==