---
title: "Semantic GUI Scene Learning and Video Alignment for Detecting Duplicate Video-Based Bug Reports"
year: 2024
venue: ICSE
doi: 10.1145/3597503.3639163
url: https://doi.org/10.1145/3597503.3639163
source: Snowball
snowball_from: "2502; 2778; 1786"
status: done
se_area: Maintenance
se_task: Duplicate detection for video-based bug reports
platform: Mobile
cv_technique: "Vision Transformer (scene learning from GUI frames); video alignment with adaptive frame weighting"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "mRR/mAP 89.8%/84.7% on 7290 tasks from 270 video reports; outperforms prior work by 9%"
challenge: "Nuanced visual patterns in bug videos; frame weighting for bug manifestation timing"
---

## Notes

Full paper version of the research proposed in 1550. 

Janus uses ViT for GUI scene understanding and adaptive video alignment. Strong benchmark evaluation. 

Pairs with GIFdroid (989) and STIFA (744) in the video bug report cluster. ICSE 2024.