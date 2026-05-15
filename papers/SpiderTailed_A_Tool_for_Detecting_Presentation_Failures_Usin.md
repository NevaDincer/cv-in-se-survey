---
title: "SpiderTailed: A Tool for Detecting Presentation Failures Using Screenshots and DOM Extraction"
year: 2023
venue: Learning and Analytics in Intelligent Systems
doi: 10.1007/978-3-031-17583-1_4
url: https://doi.org/10.1007/978-3-031-17583-1_4
source: Scopus
snowball_from:
status: done
se_area: Testing
se_task: Presentation failure detection in web GUI regression testing
platform: Web
cv_technique: "Image processing (visual property extraction per DOM element)"
visual_artifact: Component
rationale: Context-driven
evaluation: "Comparison with manual observation test"
challenge: "Direct image comparison causes misdetections due to large pixel differences"
---

## Notes

Extracts abstract visual properties per DOM element instead of raw pixel diff — smarter than naive screenshot comparison. Targets regression testing in agile contexts. Similar motivation to 90_Tricentis paper but simpler and element-level.