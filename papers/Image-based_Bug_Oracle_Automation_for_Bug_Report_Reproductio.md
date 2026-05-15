---
title: Image-based Bug Oracle Automation for Bug Report Reproduction Using Widget Detection
year: 2021
venue: ICSE
doi: 10.1109/SEAI52285.2021.9477528
url: https://doi.org/10.1109/SEAI52285.2021.9477528
source: Scopus
snowball_from:
status: done
se_area: Bug Reproduction
se_task: Automated bug oracle verification via screenshot comparison
platform: Mobile (Android)
cv_technique: "Object detection for GUI widget extraction; structural tree comparison"
visual_artifact: Bug report error screenshot
rationale: CV parses oracle and runtime screenshots into widget hierarchies to check semantic equivalence without pixel-level sensitivity
evaluation: "80.8% accuracy on 52 real-world Android bug reports; compared against pixel-level tools"
challenge: "Pixel-level comparison fails across devices, edited images, and dynamic content (usernames, dates)"
---

## Notes

Reframes bug oracle verification as structural image comparison rather than pixel diff, making it robust to device scaling and user-specific data. 

Widget detection builds a dummy hierarchy tree from both screenshots and checks tree similarity within a deviation threshold. 

==Solid empirical setup on real Android apps with a clear baseline comparison.==

