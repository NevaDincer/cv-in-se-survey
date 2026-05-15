---
title: "Psychologically-inspired, unsupervised inference of perceptual groups of GUI widgets"
year: 2022
venue: ESEC/FSE
doi: 10.1145/3540250.3549138
url: https://doi.org/10.1145/3540250.3549138
source: ACM DL
snowball_from:
status: done
se_area: GUI design
se_task: perceptual widget group segmentation
platform: mobile
cv_technique: unsupervised image-based perceptual grouping inspired by Gestalt principles
visual_artifact: mobile app screenshot
rationale: CV groups GUI widgets into higher-order perceptual units using only pixel images, without runtime data or training labels
evaluation: outperforms heuristic baselines on 1,091 GUIs from 772 apps and 20 design mockups
challenge: existing methods depend on runtime DOM data or supervised labels, limiting generalizability across GUI implementations
---

## Notes

Applies Gestalt perceptual principles (proximity, similarity, connectivity) as a computational grouping algorithm on raw GUI images. 
Fully unsupervised and implementation-agnostic. 

Foundational for downstream se tasks that need semantic UI structure without accessibility API access.