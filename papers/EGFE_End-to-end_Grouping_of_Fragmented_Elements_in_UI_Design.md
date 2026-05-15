---
title: "EGFE: End-to-end Grouping of Fragmented Elements in UI Designs with Multimodal Learning"
year: 2024
venue: ICSE
doi: 10.1145/3597503.3623313
url: https://doi.org/10.1145/3597503.3623313
source: ACM DL
snowball_from:
status: done
se_area: code generation
se_task: fragmented UI element grouping for design-to-code generation
platform: mobile
cv_technique: multimodal Transformer encoder for UI element relationship modeling
visual_artifact: UI design prototype
rationale: CV models visual and structural relationships between fragmented UI elements to group them before code generation
evaluation: "+29.75% precision, +31.07% recall, +30.39% F1 over baselines on 4,606 UI prototypes from professional designers"
challenge: visually overlapped and tiny UI elements make rule-based grouping unreliable in real design files
---

## Notes

EGFE frames element grouping as a sequence prediction problem using a Transformer over multimodal UI representations. Addresses a practical bottleneck in design-to-code pipelines where design files lack strict component hierarchy. 

Complements [[Divide-and-Conquer_Generating_UI_Code_from_Screenshots]] and [[MLLM-Based_UI2Code_Automation_Guided_by_UI_Layout_Informatio]] as a preprocessing step for the UI code generation cluster.