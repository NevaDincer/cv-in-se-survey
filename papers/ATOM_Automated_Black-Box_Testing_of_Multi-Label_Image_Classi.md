---
title: "ATOM: Automated Black-Box Testing of Multi-Label Image Classification Systems"
year: 2023
venue: ASE
doi: 10.1109/ASE56229.2023.00156
url: https://doi.org/10.1109/ASE56229.2023.00156
source: ACM DL
snowball_from:
status: done
se_area: DL system testing
se_task: black-box testing of multi-label image classification systems
platform:
cv_technique: metamorphic testing with image processing operations as metamorphic relations
visual_artifact: real-world image
rationale: CV classification systems are the systems under test; metamorphic relations are applied to images to detect label combination errors
evaluation: "6,049 errors across VOC and COCO datasets with 5 DNN models each; 92% of 587 industrial errors confirmed by developers"
challenge: exponential label combination space makes exhaustive testing infeasible; realistic test images needed for industrial acceptance
---

## Notes

Uses image search and NLP to collect realistic test images for k-label combinations, then applies metamorphic testing to detect classification errors. 

==CV system is the SUT rather than the tool. Edge case for inclusion scope bcs testing of CV systems rather than CV used for SE tasks.==
