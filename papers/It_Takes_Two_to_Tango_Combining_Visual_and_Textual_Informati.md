---
title: "It Takes Two to Tango: Combining Visual and Textual Information for Detecting Duplicate Video-Based Bug Reports"
year: 2021
venue: ICSE
doi: 10.1109/ICSE43902.2021.00091
url: https://doi.org/10.1109/ICSE43902.2021.00091
source: ACM DL
snowball_from:
status: done
se_area: bug reporting
se_task: duplicate video-based bug report detection
platform: Android
cv_technique: "video frame analysis, OCR, visual similarity"
visual_artifact: mobile app screen recording
rationale: CV analyzes screen recording frames and combines with OCR and text retrieval to identify duplicate bug report videos
evaluation: "83% top-2 accuracy on 4,860 duplicate detection tasks across 180 videos from 6 apps; 60%+ developer effort reduction"
challenge: screen recordings lack textual structure, making standard duplicate detection techniques inapplicable
---

## Notes
Combines CV frame analysis, OCR, and text retrieval to match duplicate bug videos without manual annotation. 

Foundational for the "CV for video bug report analysis" cluster alongside V2S and CAPdroid.