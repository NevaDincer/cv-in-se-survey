---
title: "VRDSynth: Synthesizing Programs for Multilingual Visually Rich Document Understanding"
year: 2024
venue: ISSTA
doi: 10.1145/3650212.3680314
url: https://doi.org/10.1145/3650212.3680314
source: ACM DL
snowball_from:
status: done
se_area: document understanding
se_task: entity relation extraction from visually rich documents
platform:
cv_technique: spatial relation analysis via DSL
visual_artifact: visually rich document
rationale: spatial layout of document elements is used as the primary signal for program synthesis, replacing visual deep learning with symbolic spatial reasoning
evaluation: "outperforms LayoutXLM in 5/8 languages; +42% F1 on FUNSD; 1M params vs 1.48GB model size"
challenge: flexible layouts across vendors and languages without access to pre-training data
---

## Notes

VRDSynth synthesizes programs using a DSL that captures spatial and textual relations between document entities, requiring zero pre-training data. Interestingly beats a large pre-trained CV model (LayoutXLM) on several languages with drastically lower memory.

==Good counterpoint in survey discussions about whether deep CV models are necessary for document SE tasks.==