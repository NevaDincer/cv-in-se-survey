---
title: UI Test Migration Across Mobile Platforms
year: 2021
venue: ASE
doi: 10.1109/ase51524.2021.9678643
url: https://doi.org/10.1109/ase51524.2021.9678643
source: Snowball
snowball_from: 2926; 2892; 2552; 477; 2719; 2778; 2805
status: done
se_area: Testing
se_task: Bi-directional UI test migration between Android and iOS apps
platform: Mobile
cv_technique: CV (screenshot-based element matching); NLP (element property matching)
visual_artifact: Full-interface
rationale: Context-driven
evaluation: 30 citations; evaluated on closed-source sibling Android and iOS apps; feasibility and accuracy shown
challenge: No source code access; bi-directional transfer with oracle preservation
---

## Notes

MAPIT builds a model from screenshots and element properties, then finds corresponding elements on target platform via CV and NLP. Works without source code on closed-source apps. Connects well with PIRLTest and cvrip in the platform-agnostic testing theme. 

ASE 2021, 30 citations.