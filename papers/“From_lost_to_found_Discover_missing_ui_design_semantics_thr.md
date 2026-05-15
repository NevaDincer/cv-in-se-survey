---
title: "From lost to found: Discover missing ui design semantics through recovering missing tags"
year: 2020
venue: PACM HCI
doi: 10.1145/3415194
url: https://doi.org/10.1145/3415194
source: Snowball
snowball_from: "2892; 2552"
status: done
se_area: requirements and design
se_task: missing tag recovery for UI design images
platform:
cv_technique: deep neural network encoding visual and textual features for tag prediction
visual_artifact: UI design image
rationale: CV encodes visual design features alongside textual tags to predict missing labels and improve design search retrieval
evaluation: "82.72% tag prediction accuracy; simulation on 5 queries returns hundreds more results than default Dribbble search"
challenge: designers provide incomplete and inconsistent tags, degrading retrievability of UI design examples on sharing platforms
---

## Notes

Addresses the tag sparsity problem on design sharing sites like Dribbble by jointly encoding visual design content and existing tags to recover missing ones. Relevant to the "CV for design knowledge management" cluster alongside Gallery D.C. and GUing.