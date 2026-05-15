---
title: Test Script Intention Generation for Mobile Application via GUI Image and Code Analysis
year: 2025
venue: ACM Trans. Softw. Eng. Methodol.
doi: 10.1145/3722105
url: https://doi.org/10.1145/3722105
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: GUI test script intention generation
platform: Android
cv_technique: "widget detection from screenshots, OCR, deep learning widget image classifier"
visual_artifact: mobile app screenshot
rationale: CV extracts widget images and infers non-textual widget intent from screenshots to complement source code analysis for test script understanding
evaluation: outperforms baselines on multiple metrics; saves ~80% of developer time for test script comprehension
challenge: test scripts lack business logic and are only loosely coupled to app behavior via widget selectors
---

## Notes

TestIntention combines CV-based GUI understanding (widget extraction, OCR, image classification) with static code analysis to generate natural language descriptions of what GUI test scripts are testing.

CV fills the semantic gap left by XPath-identified widgets that have no textual labels. 
