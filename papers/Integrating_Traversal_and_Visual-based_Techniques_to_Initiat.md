---
title: Integrating Traversal and Visual-based Techniques to Initiate UI Exploration Scripting
year: 2020
venue: "3rd International Conference on Computers in Management and Business"
doi: 10.1145/3383845.3383890
url: https://doi.org/10.1145/3383845.3383890
source: ACM DL
snowball_from:
status: done
se_area: GUI test automation
se_task: automated UI test script generation via traversal and visual element detection
platform: desktop
cv_technique: OpenCV-based GUI element detection as fallback when Accessibility API is unavailable
visual_artifact: application screenshot
rationale: CV detects GUI elements from screenshots when platform accessibility APIs are inaccessible, enabling test script generation across diverse platforms
evaluation: demonstrated on two open-source applications
challenge: accessibility APIs are unavailable on some OS and application combinations, requiring a visual fallback
---

## Notes
Lightweight framework that combines API-based traversal with OpenCV as a fallback for GUI element detection when accessibility support is absent. 
Thin on evaluation. 

Useful as an early example of CV as a platform-agnostic fallback strategy in test automation tooling.