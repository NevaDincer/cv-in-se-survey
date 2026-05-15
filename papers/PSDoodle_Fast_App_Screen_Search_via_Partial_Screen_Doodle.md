---
title: "PSDoodle: Fast App Screen Search via Partial Screen Doodle"
year: 2022
venue: MOBILESoft
doi: 10.1145/3524613.3527816
url: https://doi.org/10.1145/3524613.3527816
source: Snowball
snowball_from: "2464"
status: done
se_area: requirements and design
se_task: doodle-based app screen retrieval
platform: Android
cv_technique: deep learning for sketch-to-screen matching
visual_artifact: hand-drawn doodle
rationale: CV matches partial hand-drawn doodles of UI elements against a screenshot repository to retrieve similar app screens
evaluation: similar top-10 retrieval accuracy as SWIRE with ~50% less time in study with third-party developers
challenge: keyword search is too coarse and full-screen queries are too slow; partial sketching needs robust partial-match CV
---

## Notes

PSDoodle enables interactive app screen search through incremental doodling, combining Rico screens with QuickDraw icon doodles and a custom DoodleUINet dataset. Retrieval-speed focused alternative to full-screen sketch queries. Relevant for the "CV enabling sketch-based design search" subcluster alongside VINS and GUing.

