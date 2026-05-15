---
title: Context-Aware Bug Reproduction for Mobile Apps
year: 2023
venue: ICSE
doi: 10.1109/ICSE48619.2023.00196
url: https://doi.org/10.1109/ICSE48619.2023.00196
source: ACM DL
snowball_from:
status: done
se_area: bug reporting
se_task: automated crash reproduction from textual bug reports
platform: Android
cv_technique: multimodal neural matching of GUI screenshots and text
visual_artifact: mobile app screenshot
rationale: CV extracts visual context of GUI components to supplement missing text labels when matching bug report steps to GUI events
evaluation: "63.7% crash reproduction rate on 102 reports from 69 apps; +32.6% and +38.3% over two state-of-the-art baselines"
challenge: "75% of GUI components lack display text and 81% lack content descriptions, making text-only matching unreliable"
---

## Notes

ScopeDroid builds a state transition graph enriched with visual component context, then uses a multimodal neural network to fuzzy-match bug report steps to GUI events. 

CV fills the gap left by missing accessibility metadata on real-world Android apps. 

Relevant for the "CV bridging NLP and GUI interaction" cluster alongside CAPdroid.
