---
title: "GIFdroid: An Automated Light-weight Tool for Replaying Visual Bug Reports"
year: 2022
venue: ICSE
doi: 10.1145/3510454.3516857
url: https://doi.org/10.1145/3510454.3516857
source: Scopus
snowball_from:
status: done
se_area: Bug Reproduction
se_task: Automated bug replay from video/GIF bug reports
platform: Mobile (Android)
cv_technique: "Keyframe extraction via SSIM; GUI mapping via SSIM + ORB feature matching"
visual_artifact: Screen recording (GIF/video)
rationale: CV extracts keyframes from bug recordings and maps them to app GUI states to auto-generate a replay trace
evaluation: "82% successful reproduction on 61 recordings from 31 apps; user study on 10 real GitHub reports"
challenge: "Most recordings lack touch indicators, start mid-flow, and vary in resolution"
---

## Notes

Three-stage pipeline: keyframe extraction from video, mapping to UTG states via combined SSIM+ORB similarity, then LCS-based trace completion back to app launch. 

Handles the common real-world case where recordings start partway through an interaction. 



