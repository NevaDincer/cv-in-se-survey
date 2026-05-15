---
title: "Object detection for graphical user interface: Old fashioned or deep learning or a combination?"
year: 2020
venue: ESEC/FSE
doi: 10.1145/3368089.3409691
url: https://doi.org/10.1145/3368089.3409691
source: Scopus
snowball_from:
status: done
se_area: Testing
se_task: GUI element detection from screenshots
platform: General
cv_technique: "Hybrid: traditional image processing (canny edge; contours) + deep learning (text detection)"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "Empirical study on 50k+ GUI images; final evaluation on 25k images; outperforms 7 baselines"
challenge: "CV methods not designed for GUI-specific characteristics; localization accuracy demands higher than natural images"
---

## Notes

First large-scale empirical comparison of GUI element detection methods (7 baselines, 50k images). 

Key finding: neither pure traditional nor pure deep learning is best

hybrid coarse-to-fine approach wins

Foundational paper for GUI understanding research. 

129 citations, ==read later on==