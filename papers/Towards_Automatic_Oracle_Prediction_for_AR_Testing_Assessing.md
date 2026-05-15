---
title: "Towards Automatic Oracle Prediction for AR Testing: Assessing Virtual Object Placement"
year: 2024
venue: ISSTA
doi: 10.1145/3650212.3680315
url: https://doi.org/10.1145/3650212.3680315
source: ACM DL
snowball_from:
status: done
se_area: AR app testing
se_task: virtual object placement error detection
platform: AR mobile apps
cv_technique: hybrid neural network for image classification
visual_artifact: AR app screenshot
rationale: CV model serves as automated test oracle to judge correctness of virtual object placement, replacing human perception
evaluation: "99.34% accuracy, 96.92% precision, 100% recall on 304 screenshots; 38 real-world errors found"
challenge: test oracle problem — correctness depends on human spatial perception with no ground truth API
---

## Notes

VOPA instruments real AR apps to capture screenshots, crowdsources labels, then trains a classifier to flag misplaced virtual objects. It directly solves the oracle problem for AR testing using CV. 

==Strong example of CV enabling automated quality assessment in a domain where no programmatic oracle exists.==