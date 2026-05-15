---
title: "Beyond Manual Modeling: Automating GUI Model Generation Using Design Documents"
year: 2024
venue: ASE
doi: 10.1145/3691620.3695032
url: https://doi.org/10.1145/3691620.3695032
source: ACM DL
snowball_from:
status: done
se_area: model-based testing
se_task: automated GUI model generation from design documents
platform: mobile
cv_technique: pre-trained CV models for GUI element recognition
visual_artifact: UI/UX design document
rationale: CV identifies GUI elements and their intended behaviors from design documents to construct formal IFML models without reverse engineering code
evaluation: evaluated with an industry partner on commercial apps; comparative analysis of manual, automated, and hybrid modeling for MBT
challenge: reverse-engineered models are consistent with code and thus unsuitable for detecting functional issues in MBT
---

## Notes
DemGen extracts GUI models from design documents rather than runtime code, using CV to bridge the gap between design intent and formal model. 

This makes generated models useful for finding functional bugs that code-derived models would miss.