---
title: "Efficiency Matters: Speeding Up Automated Testing with GUI Rendering Inference"
year: 2023
venue: ICSE
doi: 10.1109/ICSE48619.2023.00084
url: https://doi.org/10.1109/ICSE48619.2023.00084
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: GUI rendering state inference for test event scheduling
platform: Android
cv_technique: deep learning model for GUI rendering state classification from screenshots
visual_artifact: mobile app screenshot
rationale: CV infers whether a GUI is fully rendered from real-time screenshots to dynamically time test events
evaluation: improved activity coverage and event execution rate demonstrated by integration with existing testing tools
challenge: fixed inter-event waiting times either waste time on over-waiting or cause failures on partially rendered GUIs
---

## Notes
Treats GUI rendering completion as a CV classification problem, feeding real-time screen frames to a DL model that signals when the next test event can safely fire. 

Simple but practically impactful, addresses a timing problem that affects all screenshot-based testing tools. 

CV improving testing infrastructure rather than test generation itself