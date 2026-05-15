---
title: "Vision-Based Widget Mapping for Test Migration across Mobile Platforms: Are We There Yet?"
year: 2023
venue: ASE
doi: 10.1109/ASE56229.2023.00068
url: https://doi.org/10.1109/ASE56229.2023.00068
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: cross-platform GUI test migration via visual widget mapping
platform: "Android, iOS"
cv_technique: vision-based widget similarity matching
visual_artifact: mobile app screenshot
rationale: CV compares visual appearance of widgets across iOS and Android to identify semantically equivalent pairs for test migration
evaluation: 89 configurations across 5 vision-based methods on 6,730 bi-directional widget pairs from iOS and Android
challenge: widgets with the same semantics often display inconsistent visual content across platforms, limiting vision-only approaches
---

## Notes

Comprehensive empirical study benchmarking vision-based widget mapping for cross-platform test migration, revealing that appearance inconsistency is a fundamental bottleneck.

Useful as a critical counterpoint to papers like LIRAT bcs shows the limits of pure visual matching and frames open problems for the field.