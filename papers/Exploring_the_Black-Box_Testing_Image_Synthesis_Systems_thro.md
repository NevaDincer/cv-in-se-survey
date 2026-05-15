---
title: "Exploring the Black-Box: Testing Image Synthesis Systems through Metamorphic Exploration"
year: 2025
venue: COMPSAC
doi: 10.1109/COMPSAC65507.2025.00317
url: https://doi.org/10.1109/COMPSAC65507.2025.00317
source: IEEE Xplore
snowball_from:
status: done
se_area: DL system testing
se_task: metamorphic testing of image synthesis networks
platform:
cv_technique: visible-infrared image fusion network
visual_artifact: synthesized image
rationale: CV model (image synthesis network) is the system under test; metamorphic relations are defined over image inputs/outputs to detect defects without a test oracle
evaluation: identified tensor dimension manipulation error in a visible-infrared fusion network
challenge: defining valid metamorphic relations for image synthesis without destroying contextual semantics
---

## Notes

Applies Metamorphic Exploration to test deep learning image synthesis systems where traditional oracles fail. 

Uses a visible-infrared fusion network as case study and shows that hypothesized metamorphic relations can expose subtle implementation bugs like tensor dimension errors. 

edge case: Relevant for the "testing AI/CV systems" angle in the survey rather than CV-as-tool.