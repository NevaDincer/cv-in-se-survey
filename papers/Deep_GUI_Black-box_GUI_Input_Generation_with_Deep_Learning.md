---
title: "Deep GUI: Black-box GUI Input Generation with Deep Learning"
year: 2021
venue: ASE
doi: 10.1109/ase51524.2021.9678778
url: https://doi.org/10.1109/ase51524.2021.9678778
source: Snowball
snowball_from: "2926; 477; 299; 2805; 23"
status: done
se_area: Testing
se_task: Black-box GUI input generation for Android apps via screenshot-based deep learning
platform: Mobile
cv_technique: "Deep learning (GUI interaction model from screenshots)"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "Monkey++ vs Google Monkey on complex UI apps; cross-platform model reuse demonstrated"
challenge: "Random testing (Google Monkey) insufficient for complex UIs requiring specific inputs"
---

## Notes
Learns valid GUI interaction patterns purely from screenshots, no implementation access needed. Model is platform-independent and reusable across apps without retraining. 

Extends Google Monkey with intelligent input generation. Connects to PIRLTest and cvrip in the visual-only testing theme. 

ASE 2021.