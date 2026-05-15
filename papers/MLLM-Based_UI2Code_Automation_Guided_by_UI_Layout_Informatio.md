---
title: MLLM-Based UI2Code Automation Guided by UI Layout Information
year: 2025
venue: PACM SE
doi: 10.1145/3728925
url: https://doi.org/10.1145/3728925
source: ACM DL
snowball_from:
status: done
se_area: code generation
se_task: UI-to-code generation from webpage screenshots
platform: web
cv_technique: multimodal LLM with layout tree parsing
visual_artifact: webpage screenshot
rationale: CV processes UI screenshots to extract element relations and layout trees that guide accurate code generation
evaluation: +10.14% BLEU, +3.95% CLIP score over best baseline on Snap2Code and Design2Code benchmarks
challenge: MLLMs struggle to preserve complex spatial layouts when generating code from real-world webpage images
---

## Notes

LayoutCoder decomposes UI2Code into three steps: grouping visually similar elements, building a layout tree, then fusing layout structure into code generation. The layout tree acts as a structural intermediary between the visual input and code output.

Good example of CV-derived structure explicitly guiding a downstream SE generation task.

