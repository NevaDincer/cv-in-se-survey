---
title: Learning-based Widget Matching for Migrating GUI Test Cases
year: 2024
venue: ICSE
doi: 10.1145/3597503.3623322
url: https://doi.org/10.1145/3597503.3623322
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: GUI test case migration via widget matching
platform: Android
cv_technique: visual widget feature extraction combined with BERT-based contextual matching
visual_artifact: mobile app screenshot
rationale: widget visual features are combined with contextual text embeddings to learn a matching model for cross-app widget identification
evaluation: "76% Top1 event matching accuracy (+17% over baselines); 89% F1 on test case migration on 34 apps"
challenge: static word embeddings miss contextual semantics; class imbalance between positive and negative widget pairs degrades matching
---

## Notes

TEMdroid uses BERT with a two-stage hard-negative mining strategy to learn widget matching for test migration. 

Complements the empirical study in [[Vision-Based_Widget_Mapping_for_Test_Migration_across_Mobile]] by proposing a learned solution to the visual-only limitations identified there. Good pair for the "cross-app widget matching" cluster.