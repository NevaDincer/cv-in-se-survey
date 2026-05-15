---
title: Web pages from mockup design based on convolutional neural network and class activation mapping
year: 2023
venue: MTA
doi: 10.1007/s11042-023-15108-3
url: https://doi.org/10.1007/s11042-023-15108-3
source: Snowball
snowball_from: "2523; 2290"
status: done
se_area: code generation
se_task: web element segmentation and classification from mockup screenshots
platform: web
cv_technique: "CNN with Class Activation Mapping for weakly-supervised element segmentation"
visual_artifact: webpage screenshot
rationale: CV classifies and segments web UI elements from screenshots using CAM to avoid expensive pixel-level annotation
evaluation: "95.71% accuracy on 2,200 screenshots across 10 web element classes with 10-fold cross-validation"
challenge: traditional segmentation requires costly in-image annotation; CAM enables weakly supervised segmentation from classification labels only
---

## Notes

Validates CNN plus CAM as a low-annotation-cost approach to web element segmentation, a prerequisite step for mockup-to-code pipelines. Preliminary work — authors note heatmap clarity needs improvement before real-time deployment. Useful as a methodological reference for the UI element detection component of screenshot-to-code systems.
