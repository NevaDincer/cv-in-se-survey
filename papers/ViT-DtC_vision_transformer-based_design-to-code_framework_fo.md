---
title: "ViT-DtC: vision transformer-based design-to-code framework for code generation from generated UI designs and hand-drawn sketches"
year: 2025
venue: Neural Computing and Applications
doi: 10.1007/s00521-025-11565-z
url: https://doi.org/10.1007/s00521-025-11565-z
source: Scopus
snowball_from: database
status: done
se_area: Development
se_task: Automated UI code generation from design images and hand-drawn sketches
platform: General
cv_technique: ViT (classification + feature extraction); GPT-2 (decoding for sketches)
visual_artifact: Component
rationale: Context-driven
evaluation: DSL token accuracy (web 97.28%; iOS 82.4%; Android 81.1%; sketch 84.8%)
challenge: Cross-platform design variability; complex bounding box annotations for sketches
---

## Notes

Two-layer pipeline: ViT classifies design type (web/iOS/Android/sketch) then generates DSL tokens. 

Extends pix2code line of work. 

Covers both high-fidelity designs and low-fidelity sketches in one framework.