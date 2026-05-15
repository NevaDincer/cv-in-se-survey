---
title: A compatibility test method for Android applications based on multimodal large models
year: 2025
venue: "Conference on Computer Network Security and Software Engineering"
doi: 10.1145/3732365.3732402
url: https://doi.org/10.1145/3732365.3732402
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: automated test script generation for compatibility testing
platform: Android
cv_technique: multimodal LLM (Qwen2-VL fine-tuned)
visual_artifact: mobile app screenshot
rationale: multimodal model processes GUI screenshots to generate platform-independent test scripts without manual coding
evaluation: improved test coverage and reduced cost on multi-device Android setup (no precise metrics reported)
challenge: model generalization limited by training data quality; natural language ambiguity between developers and LLM
---

## Notes
Fine-tunes Qwen2-VL on an intermediate scripting language (AppCheck) to auto-generate Android test scripts from GUI screenshots. 

CV is the input modality enabling script generation without accessibility APIs. 

Thin on evaluation numbers  likely a workshop/early-stage paper.


