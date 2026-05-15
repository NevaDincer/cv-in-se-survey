---
title: Prioritize Crowdsourced Test Reports via Deep Screenshot Understanding
year: 2021
venue: ICSE
doi: 10.1109/ICSE43902.2021.00090
url: https://doi.org/10.1109/ICSE43902.2021.00090
source: IEEE Xplore
snowball_from:
status: done
se_area: crowdsourced testing
se_task: test report prioritization
platform: Android
cv_technique: "widget detection, feature point extraction, deep learning classifier"
visual_artifact: mobile app screenshot
rationale: CV extracts widgets and their properties from screenshots to build a rich feature representation that drives duplicate-aware report prioritization
evaluation: outperforms state-of-the-art with less than half the overhead on a large-scale crowdsourced test report dataset
challenge: screenshot similarity alone is unreliable because many app functions share similar UI layouts
---

## Notes

DeepPrior combines CV-extracted widget features with NLP-processed text into a unified DeepFeature, then prioritizes reports by maximizing pairwise dissimilarity. 

The key insight is treating screenshots not as whole images but as structured collections of widgets with types, coordinates, and intents. 

Useful for the "multimodal SE artifact analysis" angle where CV and NLP are jointly applied.
