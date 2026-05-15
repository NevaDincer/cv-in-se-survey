---
title: Automated Fixing of Web UI Tests via Iterative Element Matching
year: 2023
venue: ASE
doi: 10.1109/ASE56229.2023.00048
url: https://doi.org/10.1109/ASE56229.2023.00048
source: ACM DL
snowball_from:
status: done
se_area: web app testing
se_task: broken web UI test repair
platform: web
cv_technique: visual similarity for element matching
visual_artifact: webpage screenshot
rationale: visual information is one of three signals (alongside DOM and attributes) used to match UI elements before and after page updates
evaluation: "81.9% element matching accuracy (+16.1% over SFTM); 68% test case repair rate on open-source and industrial apps"
challenge: industrial tests with complex control flow and Page Object patterns break existing single-flow repair tools
---

## Notes
UITestFix improves web UI test repair by iteratively refining element matches using DOM path and region similarity, where earlier high-confidence matches guide later ones. 

Visual matching is a supporting signal rather than the core contribution. 

