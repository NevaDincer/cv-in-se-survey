---
title: "Seenomaly: Vision-based linting of GUI animation effects against design-don't guidelines"
year: 2020
venue: ICSE
doi: 10.1145/3377811.3380411
url: https://doi.org/10.1145/3377811.3380411
source: Scopus
snowball_from:
status: done
se_area: GUI Testing
se_task: Linting GUI animations against design guidelines
platform: Mobile
cv_technique: "Unsupervised adversarial autoencoder for screencast classification"
visual_artifact: GUI animation screencast
rationale: CV model watches unlabeled animation recordings and groups them to detect design-don't violations without manual labeling
evaluation: "Experiments on synthetic and real-world GUI animation datasets; effectiveness and practicality assessed"
challenge: Insufficient labeled GUI animations; static analysis and image comparison tools cannot perceive motion
---

## Notes

Frames animation linting as unsupervised multi-class screencast classification, sidestepping the labeled data problem with an adversarial autoencoder. 

The model learns to reconstruct normal animations, flagging ones that deviate as guideline violations. 

Strong venue (ICSE 2020) and a rare focus on temporal visual artifacts rather than static screenshots.