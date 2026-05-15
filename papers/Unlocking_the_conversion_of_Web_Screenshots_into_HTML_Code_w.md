---
title: Unlocking the conversion of Web Screenshots into HTML Code with the WebSight Dataset
year: 2024
venue: arXiv
doi: 10.48550/arxiv.2403.09029
url: https://doi.org/10.48550/arxiv.2403.09029
source: Snowball
snowball_from: "2523; 2290"
status: done
se_area: code generation
se_task: screenshot-to-HTML code generation
platform: web
cv_technique: vision-language model fine-tuned on screenshot-HTML pairs
visual_artifact: webpage screenshot
rationale: VLM processes webpage screenshots to generate corresponding functional HTML code
evaluation: fine-tuned VLM demonstrates proficiency on 2M synthetic screenshot-HTML pairs from WebSight dataset
challenge: lack of high-quality paired screenshot-HTML datasets limited prior progress on this task
---

## Notes

Introduces WebSight, a 2M synthetic screenshot-HTML dataset, and shows a fine-tuned VLM can convert webpage screenshots to working HTML. Dataset contribution is the main value. Complements DCGen and LayoutCoder in the screenshot-to-code cluster with a data-centric rather than architectural contribution.