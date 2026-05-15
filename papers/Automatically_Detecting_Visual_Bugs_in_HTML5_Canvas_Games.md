---
title: Automatically Detecting Visual Bugs in HTML5 Canvas Games
year: 2023
venue: ASE
doi: 10.1145/3551349.3556913
url: https://doi.org/10.1145/3551349.3556913
source: ACM DL
snowball_from:
status: done
se_area: game testing
se_task: visual bug detection in HTML5 canvas games
platform: web
cv_technique: "image similarity metrics (MSE, SSIM, embedding similarity, overlap) on decomposed object images"
visual_artifact: canvas game screenshot
rationale: CV compares decomposed game object images against oracle assets to detect visual bugs without DOM access
evaluation: "100% accuracy on 24 injected visual bugs vs 44.6% for traditional snapshot testing"
challenge: canvas game contents are absent from the DOM, making standard web testing tools inapplicable
---

## Notes
Decomposes canvas snapshots into individual game object images and compares each against its sprite oracle, bypassing the DOM-inaccessibility problem. 

Clean accuracy improvement over whole-image snapshot comparison. 

Good complement to WDTEST in the "CV for game testing" cluster -- covering web games specifically.