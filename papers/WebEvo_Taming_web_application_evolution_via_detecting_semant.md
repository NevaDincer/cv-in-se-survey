---
title: "WebEvo: Taming web application evolution via detecting semantic structure changes"
year: 2021
venue: ISSTA 2021
doi: 10.1145/3460319.3464800
url: https://doi.org/10.1145/3460319.3464800
source: Scopus
snowball_from:
status: done
se_area: Maintenance
se_task: Semantic web page change detection for IR and RPA tool maintenance
platform: Web
cv_technique: "CV-based GUI widget mapping (element-by-element visual matching)"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "13 real-world websites across 9 categories; outperforms DOM-based and pixel-based baselines"
challenge: "DOM-based tools misreport dynamic content changes; cannot detect GUI widget refactoring"
---

## Notes

Distinguishes content changes (expected, ignore) from structural/widget changes (need repair). CV maps widgets between old and new page versions for locator repair in RPA tools. 

Good Maintenance example bcs motivated by real IR/RPA breakage, not just visual regression.

