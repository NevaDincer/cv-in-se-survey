---
title: "GUing: A Mobile GUI Search Engine using a Vision-Language Model"
year: 2025
venue: ACM Trans. Softw. Eng. Methodol.
doi: 10.1145/3702993
url: https://doi.org/10.1145/3702993
source: ACM DL
snowball_from:
status: done
se_area: requirements and design
se_task: text-to-GUI retrieval for design inspiration and prototyping
platform: Android
cv_technique: vision-language model (GUIClip) with contrastive learning
visual_artifact: mobile app screenshot
rationale: CV encodes GUI screenshots into a multimodal embedding space for semantic text-to-image retrieval of relevant UI designs
evaluation: "Recall@10 up to 0.69, HIT@10 of 0.91; outperforms prior text-based retrieval approaches on multiple datasets"
challenge: prior text-only approaches ignore visual information; runtime-crawled datasets miss auth-gated and data-dependent screens
---

## Notes

GUing trains a CLIP-style model on 303k Google Play app introduction screenshots with vendor-written captions, creating the first GUI-specific vision-language model. 

Also shows promising results on GUI classification and sketch-to-GUI retrieval. 

==Strong dataset contribution==

