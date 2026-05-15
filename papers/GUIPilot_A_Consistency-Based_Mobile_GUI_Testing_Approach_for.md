---
title: "GUIPilot: A Consistency-Based Mobile GUI Testing Approach for Detecting Application Bugs"
year: 2025
venue: PACM SE
doi: 10.1145/3728909
url: https://doi.org/10.1145/3728909
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: design-to-implementation consistency checking
platform: Android
cv_technique: "widget alignment via partial order matching, vision-language model for GUI transition inference"
visual_artifact: mobile app screenshot
rationale: CV compares screen widget layouts against design mock-ups and uses a VLM to infer widget actions for validating GUI transitions
evaluation: "99.8% precision, 98.6% recall on 80 apps and 160 mock-ups; 9 confirmed bugs in industrial trading app; +66.2% and +56.6% over GVT"
challenge: validating both visual layout consistency and behavioral transition consistency between design and implementation requires multimodal reasoning
---

## Notes

GUIPilot separates screen consistency (widget alignment) from process consistency (transition validation), using a VLM for the latter. The widget alignment formulation as an optimization problem is a clean contribution. 

Strong example of CV bridging design intent and runtime behavior for industrial GUI testing.