---
title: "image2emmet: Automatic code generation from web user interface image"
year: 2021
venue: JSEP
doi: 10.1002/smr.2369
url: https://doi.org/10.1002/smr.2369
source: Snowball
snowball_from: 2523
status: done
se_area: Development
se_task: "Web UI image to code generation"
platform: Web
cv_technique: "CNN; LSTM; Faster R-CNN"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "Accuracy metrics"
challenge: "Handling complex layout hierarchies and custom widgets"
---

## Notes

Uses Faster R-CNN to detect UI components in webpage screenshots, then a CNN+LSTM model to translate detected components into HTML-CSS code. Achieves 80% precision on component detection but only 60% on code generation, suggesting the vision-to-code mapping is the harder bottleneck. A classic image-to-code pipeline paper useful for benchmarking against later LLM-based approaches.