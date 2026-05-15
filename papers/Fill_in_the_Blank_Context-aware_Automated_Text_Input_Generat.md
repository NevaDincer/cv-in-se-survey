---
title: "Fill in the Blank: Context-aware Automated Text Input Generation for Mobile GUI Testing"
year: 2022
venue: ICSE 2023
doi: 10.1109/ICSE48619.2023.00119
url: https://doi.org/10.1109/ICSE48619.2023.00119
source: Snowball
snowball_from: "2552; 2788; 2778; 2805"
status: done
se_area: Testing
se_task: Semantic text input generation for mobile GUI testing
platform: Mobile
cv_technique: "GUI context understanding from screenshots for prompt extraction"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "87% passing rate on 106 apps; 42% more activities; 52% more pages; 122% more bugs vs baseline"
challenge: "Text input fields block automated exploration; diverse semantic input requirements per field"
---

## Notes
LLM generates contextually appropriate text inputs by reading GUI screenshots. Addresses a concrete gap: most GUI testing tools skip text fields, missing large portions of app functionality. 

Strong quantitative results. Same author group as Guided Bug Crush (S004). ICSE 2023.