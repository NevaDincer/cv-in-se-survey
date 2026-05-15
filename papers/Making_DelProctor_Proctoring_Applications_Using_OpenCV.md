---
title: Making DelProctor Proctoring Applications Using OpenCV
year: 2022
venue: ICOSNIKOM 2022
doi: 10.1109/ICOSNIKOM56551.2022.10034915
url: https://doi.org/10.1109/ICOSNIKOM56551.2022.10034915
source: Scopus
snowball_from:
status: done
se_area: Software Application Development
se_task: Online exam proctoring via face verification and fraud detection
platform: Desktop
cv_technique: Face detection and matching via OpenCV
visual_artifact: Webcam feed
rationale: CV used to verify examinee identity and flag cheating behavior during online exams
evaluation: Qualitative comparison against human supervisors and existing tools like Moodle Proctoring
challenge: Processing load distributed to client to reduce server burden; no quantitative accuracy metrics reported
---

## Notes

Builds a Moodle-integrated proctoring app where OpenCV handles face matching on the client side rather than the server. 

CV is essentially a deployment vehicle here rather than a research contribution; the paper's value is in the system architecture and integration with LMS. 

Edge case for inclusion scope as CV is used as an off-the-shelf tool with no novel CV methodology.
