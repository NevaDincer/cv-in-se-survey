---
title: On Using GUI Interaction Data to Improve Text Retrieval-Based Bug Localization
year: 2023
venue: ICSE
doi: 10.1145/3597503.3608139
url: https://doi.org/10.1145/3597503.3608139
source: Snowball
snowball_from: "2502; 2778; 2805"
status: done
se_area: Maintenance
se_task: GUI-augmented text retrieval for bug localization
platform: Mobile
cv_technique: "GUI screenshot interaction data (for file filtering; boosting; query reformulation)"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "Hits@10 improvement of 13-18% on 80 bug reports from 39 Android apps"
challenge: "Semantic gap between bug report text and source code identifiers"
---

## Notes

Uses GUI interaction screenshots from bug reproduction to augment text retrieval for bug localization. 
==Not pure CV==  bridges visual and textual information. 
Practical gain: 13-18% improvement in top-10 file retrieval. 
Connects GIFdroid (989) reproduction line to bug localization research. ICSE 2023.