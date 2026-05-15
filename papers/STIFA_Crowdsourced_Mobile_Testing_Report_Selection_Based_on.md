---
title: "STIFA: Crowdsourced Mobile Testing Report Selection Based on Text and Image Fusion Analysis"
year: 2020
venue: ASE
doi: 10.1145/3324884.3415300
url: https://doi.org/10.1145/3324884.3415300
source: Scopus
snowball_from:
status: done
se_area: Testing
se_task: Duplicate bug report detection in crowdsourced mobile testing
platform: Mobile
cv_technique: "Image feature extraction (screenshot analysis for bug context)"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "95.23% text feature extraction; 84.15% image feature extraction; 87.64% duplicate detection accuracy on 150 reports"
challenge: "Existing tools treat screenshots and text independently; duplicate report noise reduces efficiency"
---

## Notes

Fuses screenshot and text features to build a unified bug context for duplicate detection. 

Connects to [[Adaptive_attention_fusion_network_for_cross-device_GUI_eleme]] in crowdsourced testing theme but focuses on report deduplication rather than test reproduction.

ASE venue, solid accuracy results.