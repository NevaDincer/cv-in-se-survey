---
title: "DeclarUI: Bridging Design and Development with Automated Declarative UI Code Generation"
year: 2025
venue: PACM SE
doi: 10.1145/3715726
url: https://doi.org/10.1145/3715726
source: ACM DL
snowball_from:
status: done
se_area: code generation
se_task: UI design to declarative code generation
platform: "React Native, Flutter, ArkUI"
cv_technique: "UI component segmentation, visual similarity scoring"
visual_artifact: UI design mockup
rationale: CV segments UI components from design images to feed precise layout and visual context into MLLM-based code generation
evaluation: "96.8% PTG coverage, 98% compilation success; +123% PTG coverage and +55% visual similarity over MLLM baselines"
challenge: MLLMs alone miss fine-grained component boundaries and inter-page interaction logic
---

## Notes

DeclarUI chains CV segmentation, MLLM code generation, and iterative compiler feedback to produce compilable declarative UI code. Page 

Transition Graphs capture multi-screen interaction logic that single-screen approaches miss. 

Strong example of CV as a precision layer augmenting LLM code generation for mobile development.