---
title: Automated Mapping of Adaptive App GUIs from Phones to TVs
year: 2023
venue: TOSEM
doi: 10.1145/3631968
url: https://doi.org/10.1145/3631968
source: Snowball
snowball_from: "2778; 2805"
status: done
se_area: GUI design
se_task: cross-device GUI adaptation from phone to TV
platform: "Android, Android TV"
cv_technique: deep learning for GUI classification and grouping
visual_artifact: mobile app screenshot
rationale: CV classifies and groups phone GUI elements to apply empirically derived adaptation rules for generating TV layouts
evaluation: accuracy evaluation and user study confirming generated GUI quality and developer usefulness
challenge: substantial differences in screen size, aspect ratio, and interaction style make direct GUI porting infeasible
---

## Notes

Proposes a semi-automated rule-based pipeline where CV classifies phone GUIs to drive TV layout generation and source code output. Extends cross-device GUI adaptation beyond Android-iOS to the phone-TV dimension. Relevant for the "CV for cross-platform GUI adaptation" cluster alongside LIRAT and CdDiff.