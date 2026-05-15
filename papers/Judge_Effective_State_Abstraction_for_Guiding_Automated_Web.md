---
title: "Judge: Effective State Abstraction for Guiding Automated Web GUI Testing"
year: 2026
venue: ACM Trans. Softw. Eng. Methodol.
doi: 10.1145/3736162
url: https://doi.org/10.1145/3736162
source: ACM DL
snowball_from:
status: done
se_area: web GUI testing
se_task: state abstraction for automated web testing
platform: web
cv_technique: contrastive learning for DOM-based page embedding
visual_artifact:
rationale: contrastive learning embeds page structure into vectors for state classification, though input is DOM not screenshots
evaluation: "8.95–28.90% F1 improvement over 13 baselines; 2.62–14.12% code coverage gain on 6 web apps"
challenge: dynamic content and varied design styles make threshold-based or classifier-based state grouping unreliable
---

## Notes

Judge merges DOM subtrees to normalize dynamic content, then uses contrastive learning plus SVM to classify page states. Input is structural DOM, not visual screenshots, so CV involvement is indirect at best. 

Edge case for inclusion scope bcs contrastive learning is borrowed from CV but applied to DOM structure.
