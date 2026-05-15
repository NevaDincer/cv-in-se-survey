---
title: An Empirical Investigation into the Use of Image Captioning for Automated Software Documentation
year: 2022
venue: SANER
doi: 10.1109/SANER53432.2022.00069
url: https://doi.org/10.1109/SANER53432.2022.00069
source: Snowball
snowball_from: "2552; 2464"
status: done
se_area: documentation
se_task: automated natural language description generation from GUI screenshots
platform: Android
cv_technique: neural image captioning models
visual_artifact: mobile app screenshot
rationale: CV generates functional natural language descriptions of software from GUI screenshots, bridging the lexical gap between code and natural language in documentation
evaluation: "45,998 descriptions for 10,204 screenshots; quantitative MT metrics plus large-scale user study across 4 captioning models"
challenge: lexical gap between abstract natural language and structured code limits text-only documentation approaches
---

## Notes

One of the first empirical studies connecting GUIs to functional software descriptions via image captioning. The 45k description dataset is a significant open contribution. Frames GUI screenshots as a bridge between code and natural language for documentation tasks. Relevant for the "CV for software documentation" cluster alongside DOSUD.
