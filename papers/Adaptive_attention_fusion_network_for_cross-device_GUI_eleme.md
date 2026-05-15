---
title: Adaptive attention fusion network for cross-device GUI element re-identification in crowdsourced testing
year: 2024
venue: Neurocomputing
doi: 10.1016/j.neucom.2024.127502
url: https://doi.org/10.1016/j.neucom.2024.127502
source: Scopus
snowball_from:
status: done
se_area: Testing
se_task: GUI element re-identification across devices for crowdsourced test reproduction
platform: Mobile
cv_technique: "CNN (ERINet); attention mechanism with learnable factor"
visual_artifact: Component
rationale: Context-driven
evaluation: "Accuracy on 115704 test GUI element images across 67 backgrounds"
challenge: "Background variation across devices causes misidentification; cross-device code differences"
---

## Notes
Automates reproduction testing in crowdsourced platforms. workers find bugs, CV re-identifies the same GUI element on different devices to verify fix. 

Large dataset (31k train / 115k test).

Attention mechanism explicitly suppresses background noise.