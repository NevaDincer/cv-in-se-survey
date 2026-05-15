---
title: "LLM Code Customization with Visual Results: A Benchmark on TikZ"
year: 2025
venue: "International Conference on Evaluation and Assessment in Software Engineering"
doi: 10.1145/3756681.3757003
url: https://doi.org/10.1145/3756681.3757003
source: ACM DL
snowball_from:
status: done
se_area: code generation
se_task: LLM-based code customization with visual output verification
platform:
cv_technique: visual feedback for output correctness assessment
visual_artifact: TikZ-rendered figure
rationale: visual comparison of rendered outputs is used as the correctness signal for evaluating LLM code edits
evaluation: empirical evaluation of state-of-the-art LLMs on vTikZ benchmark with parameterized ground truths
challenge: LLMs struggle to align code modifications with visual intent even for structured graphics languages
---

## Notes

vTikZ is a benchmark where LLMs must edit TikZ code to match a visual target, using rendered image comparison as the oracle. 

Highlights that current LLMs lack reliable visual-code alignment. 

