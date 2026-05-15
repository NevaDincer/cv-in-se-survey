---
title: "Widget Captioning: Generating Natural Language Description for Mobile User Interface Elements"
year: 2020
venue: EMNLP
doi: 10.18653/v1/2020.emnlp-main.443
url: https://doi.org/10.18653/v1/2020.emnlp-main.443
source: Snowball
snowball_from: "2552; 2464; 1786"
status: done
se_area: accessibility
se_task: natural language caption generation for mobile UI widgets
platform: mobile
cv_technique: multimodal deep learning on UI images and structural representations
visual_artifact: mobile app screenshot
rationale: CV processes widget images alongside structural UI metadata to generate natural language descriptions for accessibility and language-based interaction
evaluation: "162,860 phrases for 61,285 UI elements across 21,750 screens; benchmark models evaluated across feature modality combinations"
challenge: accessibility descriptions are systematically missing in mobile UIs with no automated generation approach
---

## Notes

Defines widget captioning as a new multimodal task combining image and structural UI input to generate natural language element descriptions. The large crowdsourced dataset is a significant contribution. Foundational for the accessibility captioning cluster alongside LabelDroid and Screen Recognition.