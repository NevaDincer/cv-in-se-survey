---
title: Data Analysis Tools Affect Outcomes of Eye-Tracking Studies
year: 2024
venue: EMSE
doi: 10.1145/3674805.3686672
url: https://doi.org/10.1145/3674805.3686672
source: ACM DL
snowball_from:
status: done
se_area: empirical SE / developer studies
se_task: eye-tracking data analysis standardization
platform:
cv_technique:
visual_artifact:
rationale: no CV involvement; eye-tracking hardware captures gaze data but no computer vision processing is applied
evaluation: systematic mapping study plus reproduction on 3 public eye-tracking datasets using Tobii, iTrace, and Ogama
challenge: lack of standardization across analysis tools leads to non-reproducible study conclusions
---

## Notes

Highlights that tool choice (Tobii, iTrace, Ogama) significantly changes eye-tracking study results in SE research. CV is not used. 

Edge case for inclusion scope bcs eye-tracking involves visual data collection but the paper is about statistical analysis tool comparability, not CV.