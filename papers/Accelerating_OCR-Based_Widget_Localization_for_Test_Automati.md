---
title: Accelerating OCR-Based Widget Localization for Test Automation of GUI
year: 2023
venue: ASE
doi: 10.1145/3551349.3556966
url: https://doi.org/10.1145/3551349.3556966
source: ACM DL
snowball_from:
status: done
se_area: GUI test automation
se_task: widget localization via OCR acceleration
platform: desktop
cv_technique: OCR with Label Text Screening preprocessing
visual_artifact: GUI screenshot
rationale: CV pipeline accelerates label text localization on GUI screens to make OCR-based test automation practical without GPU
evaluation: "below 0.5s for ~60% of 4K cases on CPU; 4x+ faster than Tesseract, PaddleOCR, and EasyOCR baselines"
challenge: OCR too slow for real-world test automation use on GPU-free machines at 4K resolution
---

## Notes

LTS avoids running full OCR on entire screens by pre-filtering regions unlikely to contain short label texts, breaking open the OCR black box. Practical engineering contribution for GUI test tooling rather than a novel ML approach. 

Useful reference for the "CV performance bottlenecks in SE tools" discussion