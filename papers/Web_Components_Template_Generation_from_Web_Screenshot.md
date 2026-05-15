---
title: Web Components Template Generation from Web Screenshot
year: 2021
venue: ACM International Conference Proceeding Series
doi: 10.1145/3468784.3468787
url: https://doi.org/10.1145/3468784.3468787
source: Scopus
snowball_from:
status: done
se_area: Web Development
se_task: Automated web component generation from screenshots
platform: Web
cv_technique: "Object detection with deep learning (FPN-based, bounding box + category label)"
visual_artifact: Web page screenshot
rationale: CV detects UI objects in screenshots and maps them to React Web Components automatically
evaluation: "Validation loss of 1.873"
challenge: Generalizing across diverse web layouts; loss metric alone is weak evidence of practical utility
---

## Notes

Combines object detection (FPN-style deep learning) with the W3C Web Components standard to auto-generate React component templates from a screenshot. 

Closest prior work is pix2code; this paper extends the idea toward a component-based output rather than raw code. 

 
 only validation loss is reported, no end-to-end usability or accuracy benchmark.
