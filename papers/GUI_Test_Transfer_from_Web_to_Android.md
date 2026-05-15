---
title: GUI Test Transfer from Web to Android
year: 2022
venue: "International Conference on Information Control Systems"
doi: 10.1109/ICST53961.2022.00011
url: https://doi.org/10.1109/ICST53961.2022.00011
source: Snowball
snowball_from: "2719; 2805"
status: done
se_area: mobile app testing
se_task: cross-platform GUI test transfer from web to Android
platform: "web, Android"
cv_technique: "template matching and deep learning for GUI event mapping"
visual_artifact: mobile app screenshot
rationale: CV matches GUI elements across web and Android screenshots to map test events and oracles during cross-platform transfer
evaluation: "77% transfer success rate; 82% precision, 99% recall on GUI event and oracle mapping on real-world apps"
challenge: web and Android UIs differ structurally despite shared functionality, requiring visual matching to bridge the platform gap
---

## Notes

TransDroid extends cross-app test migration to the web-to-Android dimension using CV-based widget matching. Complements LIRAT and TEMdroid in the cross-platform test migration cluster but specifically targets the web-to-mobile transfer scenario.