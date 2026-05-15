---
title: "VLM-Fuzz: Vision Language Model Assisted Recursive Depth-First Search Exploration for Effective GUI Testing of Android Apps"
year: 2026
venue: EMSE
doi: 10.1007/s10664-026-10816-4
url: https://doi.org/10.1007/s10664-026-10816-4
source: Scopus
snowball_from: database
status: done
se_area: Testing
se_task: Automated Android GUI fuzzing for code coverage and crash detection
platform: Mobile
cv_technique: VLM (on-demand GUI reasoning)
visual_artifact: Full-interface
rationale: Context-driven
evaluation: Code coverage (class/method/line); crash detection (52 crashes in 12 apps)
challenge: Complex dynamic GUI layouts; coordination between test states
---

## Notes

VLM is not used for every screen, only triggered on-demand for visually complex cases. 

Hybrid with heuristic DFS. Outperforms APE and DeepGUI. 

Good example of selective CV integration in Testing.