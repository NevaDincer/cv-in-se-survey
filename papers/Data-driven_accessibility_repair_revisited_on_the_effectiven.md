---
title: "Data-driven accessibility repair revisited: on the effectiveness of generating labels for icons in Android apps"
year: 2021
venue: ESEC/FSE
doi: 10.1145/3468264.3468604
url: https://doi.org/10.1145/3468264.3468604
source: Snowball
snowball_from: "2365; 1786"
status: done
se_area: accessibility
se_task: context-aware icon label generation for accessibility
platform: Android
cv_technique: deep learning with multi-source context for icon image classification
visual_artifact: mobile app icon
rationale: CV classifies icon images enriched with contextual usage information to generate accurate accessibility labels
evaluation: outperforms LabelDroid in both user study and automatic evaluation; shows icon images alone are insufficient
challenge: icon images lack sufficient information for accurate label prediction without surrounding usage context
---

## Notes

COALA directly extends and critiques LabelDroid, showing that icon image alone is insufficient and that usage context significantly improves label quality. The finding that automatically extracted labeled data requires caution is an important methodological note for the survey. Key paper for the "CV + context for accessibility labeling" discussion.