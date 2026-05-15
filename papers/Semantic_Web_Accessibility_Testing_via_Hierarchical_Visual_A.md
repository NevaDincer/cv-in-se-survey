---
title: Semantic Web Accessibility Testing via Hierarchical Visual Analysis
year: 2021
venue: ICSE
doi: 10.1109/ICSE43902.2021.00143
url: https://doi.org/10.1109/ICSE43902.2021.00143
source: Snowball
snowball_from: "2746; 2365"
status: done
se_area: accessibility testing
se_task: semantic web accessibility testing via visual region grouping
platform: web
cv_technique: deep learning for hierarchical visual region segmentation and semantic role inference
visual_artifact: webpage screenshot
rationale: CV infers semantic groupings and roles of webpage regions to assess high-level accessibility properties that syntactic tools miss
evaluation: "F-measure 87% for semantic grouping, 85% accuracy for accessibility failure detection on 30 real-world websites"
challenge: existing tools only check syntax; semantic accessibility requires understanding how users with disabilities perceive page structure
---

## Notes

AXERAY uses hierarchical visual analysis to infer semantic page regions and detect accessibility failures that DOM-based tools cannot catch. Web accessibility counterpart to MotorEase and AccessiText in the accessibility testing cluster. The semantic grouping approach is conceptually related to the Gestalt-based work in 2610.

