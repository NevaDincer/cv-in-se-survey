---
title: "DeepLSH: Deep Locality-Sensitive Hash Learning for Fast and Efficient Near-Duplicate Crash Report Detection"
year: 2024
venue: ICSE
doi: 10.1145/3597503.3639146
url: https://doi.org/10.1145/3597503.3639146
source: ACM DL
snowball_from:
status: done
se_area: bug reporting
se_task: crash report deduplication and bucketing
platform:
cv_technique: Siamese DNN with locality-sensitive hashing
visual_artifact:
rationale: no CV involvement; Siamese DNN operates on crash report text/stack traces, not visual data
evaluation: experiments on a newly released crash report dataset comparing LSH approximation quality across similarity metrics
challenge: deriving locality-sensitive hash functions for advanced crash bucketing metrics like Jaccard and Cosine
---

## Notes

DeepLSH adapts Siamese networks and LSH from CV/retrieval literature to crash report bucketing, but the input is textual crash data not images. 

Edge case for inclusion scope bcs the DNN architecture originates from CV but is applied to a purely textual SE task.