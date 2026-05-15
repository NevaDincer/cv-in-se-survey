---
title: "GLIB: towards automated test oracle for graphically-rich applications"
year: 2021
venue: ESEC/FSE
doi: 10.1145/3468264.3468586
url: https://doi.org/10.1145/3468264.3468586
source: ACM DL
snowball_from:
status: done
se_area: game testing
se_task: GUI glitch detection as automated test oracle
platform: mobile games
cv_technique: image-based glitch detection with code-based data augmentation
visual_artifact: game screenshot
rationale: CV detects non-crashing graphical glitches in game GUIs where no programmatic oracle exists
evaluation: "100% precision, 99.5% recall on 20 real-world games; 48/53 bugs confirmed on 14 additional games at NetEase"
challenge: existing tools only detect crashes; graphical glitches are non-crashing bugs requiring visual inspection
---

## Notes

GLIB uses code-based data augmentation to generate glitch training data without manual labeling, then trains a CV model to serve as a test oracle for graphical bugs.

Industrial validation at NetEase makes this a strong companion to WDTEST for the game testing cluster. 
