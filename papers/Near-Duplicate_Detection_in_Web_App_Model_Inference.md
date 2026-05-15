---
title: Near-Duplicate Detection in Web App Model Inference
year: 2020
venue: ICSE
doi: 10.1145/3377811.3380416
url: https://doi.org/10.1145/3377811.3380416
source: IEEE Xplore
snowball_from:
status: done
se_area: web app testing
se_task: near-duplicate state detection for model inference
platform: web
cv_technique: image similarity / perceptual hashing
visual_artifact: webpage screenshot
rationale: CV-based similarity techniques are evaluated alongside IR and web testing approaches to detect near-duplicate webpage states during automated model inference
evaluation: "10 detection techniques compared on 9 open-source web apps; 493k webpage pairs from 6000+ websites"
challenge: no single algorithm achieves full accuracy without sacrificing state coverage
---

## Notes

Benchmarks 10 near-duplicate detection algorithms from three domains: IR, web testing, and CV -for web app model inference. CV techniques are one class among several being compared, not the sole method. 

==Good reference for surveys discussing how CV fits into the broader automated web testing toolbox.==