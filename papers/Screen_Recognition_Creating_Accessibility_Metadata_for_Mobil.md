---
title: "Screen Recognition: Creating Accessibility Metadata for Mobile Applications from Pixels"
year: 2021
venue: CHI
doi: 10.1145/3411764.3445186
url: https://doi.org/10.1145/3411764.3445186
source: Snowball
snowball_from: "2610; 2892; 2552; 2685; 2365; 2290; 2782; 2805"
status: done
se_area: accessibility
se_task: accessibility metadata generation from UI screenshots
platform: iOS
cv_technique: "UI element detection, content and state recognition from pixels"
visual_artifact: mobile app screenshot
rationale: CV detects UI elements and infers their type, content, state, and interactivity purely from pixels to generate VoiceOver accessibility metadata
evaluation: "model trained on 77,637 screens from 4,068 iPhone apps; user study with 9 screen reader users confirming accessibility improvements"
challenge: many apps lack sufficient accessibility metadata; pixel-based inference is the only approach that works across all apps regardless of implementation
---

## Notes

Screen Recognition is deployed as an iOS system feature augmenting VoiceOver, making it one of the most impactful real-world CV-for-accessibility deployments in the literature. Complements LabelDroid (label generation for Android) as the iOS counterpart with broader metadata scope beyond just labels.