---
title: GUI Widget Detection and Intent Generation via Image Understanding
year: 2021
venue: IEEE Access
doi: 10.1109/access.2021.3131753
url: https://doi.org/10.1109/access.2021.3131753
source: Snowball
snowball_from: 2805
status: done
se_area: Testing
se_task: "GUI widget detection and intent generation"
platform: Desktop
cv_technique: "CNN; Encoder-Decoder; Image Matching"
visual_artifact: "Localized; Full-interface"
rationale: Context-driven
evaluation: "Accuracy metrics"
challenge: "Scalability to large and diverse application corpora; Limited ground truth data"
---

## Notes

Targets aerospace control software testing — detects GUI widgets via image matching, then uses a CNN encoder-decoder to generate natural language intent descriptions for each widget. Achieves IoU of 0.81 for detection and BLEU-1 of 0.567 for intent generation. Niche domain (aerospace) but the pipeline is generalizable; useful as an example of combining widget localization with NL intent labeling for test automation.