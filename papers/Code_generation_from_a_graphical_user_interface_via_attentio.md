---
title: Code generation from a graphical user interface via attention-based encoder-decoder model
year: 2021
venue: Multimedia Systems
doi: 10.1007/s00530-021-00804-7
url: https://doi.org/10.1007/s00530-021-00804-7
source: Snowball
snowball_from: "2523; 2290"
status: done
se_area: code generation
se_task: GUI screenshot-to-code generation via attention encoder-decoder
platform:
cv_technique: attention-based encoder-decoder for image-to-code generation
visual_artifact: GUI screenshot
rationale: CV encodes GUI screenshots and an attention mechanism selects salient visual features to guide token-by-token code generation
evaluation: outperforms prior models on pix2code benchmark dataset
challenge: decoder must selectively attend to relevant GUI regions rather than processing the full image uniformly
---

## Notes

Extends the pix2code paradigm with an attention mechanism that improves code token accuracy by focusing on relevant image regions. Incremental improvement over early GUI-to-code baselines. Useful as a historical reference point in the screenshot-to-code cluster before the LLM-era approaches like DCGen and LayoutCoder.