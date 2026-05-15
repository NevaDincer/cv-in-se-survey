---
title: "Screen Parsing: Towards Reverse Engineering of UI Models from Screenshots"
year: 2021
venue: UIST
doi: 10.1145/3472749.3474763
url: https://doi.org/10.1145/3472749.3474763
source: Snowball
snowball_from: "2523; 2290"
status: done
se_area: GUI design
se_task: UI element detection and hierarchical grouping from screenshots
platform: mobile
cv_technique: deep learning for joint UI element detection and semantic relationship prediction
visual_artifact: mobile app screenshot
rationale: CV predicts UI elements and their structural groupings from raw pixels to enable downstream SE tasks without developer-provided metadata
evaluation: outperforms current systems by up to 23% in UI model accuracy
challenge: inferring semantic groupings between elements from pixels requires both detection and relational reasoning
---

## Notes

Defines screen parsing as a combined detection and grouping task, enabling UI similarity search, accessibility enhancement, and code generation from a single model. Foundational infrastructure paper — downstream applications map directly to multiple clusters in the survey. Precursor to EGFE and the Gestalt grouping work.

