---
title: "Semantic matching of GUI events for test reuse: are we there yet?"
year: 2021
venue: ISSTA
doi: 10.1145/3460319.3464827
url: https://doi.org/10.1145/3460319.3464827
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: semantic GUI event matching for test reuse
platform: Android
cv_technique:
visual_artifact:
rationale: no CV involvement; approach relies purely on semantic text similarity between widget labels and event descriptions
evaluation: "253 matching configurations, 337 queries, 8,099 GUI events; SemFinder outperforms existing solutions"
challenge: textual widget information alone is often insufficient for reliable cross-app event matching
---

## Notes

Comprehensive empirical study benchmarking semantic GUI event matching configurations for test reuse, proposing SemFinder as the best performer. 

==Edge case for inclusion scope bcs no CV used, but frequently cited alongside vision-based widget matching papers in the test migration cluster.==