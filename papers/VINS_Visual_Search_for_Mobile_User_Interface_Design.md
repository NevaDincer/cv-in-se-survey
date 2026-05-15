---
title: "VINS: Visual Search for Mobile User Interface Design"
year: 2021
venue: CHI
doi: 10.1145/3411764.3445762
url: https://doi.org/10.1145/3411764.3445762
source: Snowball
snowball_from: "2685; 2464"
status: done
se_area: requirements and design
se_task: visual UI design retrieval from screenshot queries
platform: mobile
cv_technique: object detection-based image retrieval with UI hierarchy modeling
visual_artifact: mobile app screenshot
rationale: CV detects UI components and models hierarchical layout structure to retrieve visually similar design examples
evaluation: "76.39% mAP for UI component detection; high performance on similar UI design retrieval"
challenge: "text-based search ignores UI structure and visual content; designers need image-to-image retrieval for design inspiration"
---

## Notes

VINS extends screenshot-based design search by incorporating detected component hierarchy into the retrieval model, going beyond pixel-level similarity. Precursor to GUing in the "CV for design search" cluster, but uses object detection rather than vision-language contrastive learning.