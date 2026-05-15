---
title: "Divide-and-Conquer: Generating UI Code from Screenshots"
year: 2025
venue: PACM SE
doi: 10.1145/3729364
url: https://doi.org/10.1145/3729364
source: ACM DL
snowball_from:
status: done
se_area: code generation
se_task: screenshot-to-UI code generation
platform: web
cv_technique: screenshot segmentation for MLLM-based code generation
visual_artifact: webpage screenshot
rationale: CV segments screenshots into smaller visual units to reduce element omission and distortion in MLLM-generated UI code
evaluation: "up to 15% visual similarity and 8% code similarity improvement over baseline MLLMs on real-world websites"
challenge: MLLMs generate omitted, distorted, or misarranged elements when processing full-page screenshots as a single input
---

## Notes

DCGen decomposes a screenshot into manageable segments, generates code per segment, then reassembles them that is solving the visual granularity problem for UI code generation. 

Complements LayoutCoder and DeclarUI in the screenshot-to-code cluster, with a simpler segment-based decomposition strategy rather than explicit layout trees.
