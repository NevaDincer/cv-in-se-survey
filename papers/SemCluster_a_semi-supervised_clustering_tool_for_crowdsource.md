---
title: "SemCluster: a semi-supervised clustering tool for crowdsourced test reports with deep image understanding"
year: 2022
venue: ESEC/FSE
doi: 10.1145/3540250.3558933
url: https://doi.org/10.1145/3540250.3558933
source: ACM DL
snowball_from:
status: done
se_area: crowdsourced testing
se_task: duplicate test report clustering and deduplication
platform: Android
cv_technique: deep image understanding with semantic text-image binding
visual_artifact: mobile app screenshot
rationale: CV extracts deep screenshot features that are semantically bound to textual descriptions to improve duplicate report clustering
evaluation: improves six clustering metrics over state-of-the-art on crowdsourced test report dataset
challenge: prior methods treat screenshots shallowly and ignore semantic connections between text and image content
---

## Notes

SemCluster combines deep screenshot understanding with semantic binding rules to link visual and textual features before clustering. 

Close relative to DeepPrior but focuses on deduplication via clustering rather than prioritization.

Useful pair in the "multimodal crowdsourced test report analysis" cluster.