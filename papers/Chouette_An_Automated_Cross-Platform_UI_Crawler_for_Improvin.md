---
title: "Chouette: An Automated Cross-Platform UI Crawler for Improving App Quality"
year: 2023
venue: ASEW 2023
doi: 10.1109/ASEW60602.2023.00029
url: https://doi.org/10.1109/ASEW60602.2023.00029
source: IEEE Xplore
snowball_from:
status: done
se_area: Testing
se_task: Cross-platform automated UI crawling and screenshot collection
platform: General
cv_technique: "Canny edge detection; morphological operations (closing) for tappable area detection"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "200 bug reports over 6 months across Android, iOS, and Web at Duolingo"
challenge: "Multi-platform feature disparity; 26 UI languages; frequent releases break traditional tests"
---

## Notes

Industrial paper from Duolingo. Simple CV (Canny edges) instead of ML because Duolingo's design is clean with clear item separation. 

Cross-platform from a single tool. Screenshot collection serves multiple internal teams (localization, design, marketing). 

