---
title: "Seeing is Believing: Vision-Driven Non-Crash Functional Bug Detection for Mobile Apps"
year: 2025
venue: TSE
doi: 10.1109/TSE.2025.3614469
url: https://doi.org/10.1109/TSE.2025.3614469
source: Scopus
snowball_from:
status: done
se_area: Testing
se_task: Non-crash functional bug detection via visual GUI logic analysis
platform: Mobile
cv_technique: "MLLM (multi-agent; screenshot annotation + visual-textual alignment)"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "590 non-crash bugs; 14-112% recall boost over 12 baselines; 43 unknown bugs found on Google Play"
challenge: "No reliable oracle for non-crash bugs; MLLM hallucination; token limit in exploration history"
---

## Notes

61.3% of GitHub bug reports are non-crash — massively underexplored.

VisionDroid uses 3 MLLM agents (Explorer/Monitor/Detector) to understand GUI page transition logic, not just visual state. 

Functionality-aware chain-of-thought reduces hallucination.

==read afterwards== TSE venue, strong results.