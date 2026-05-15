---
title: Understanding Screen Relationships from Screenshots of Smartphone Applications
year: 2022
venue: IUI
doi: 10.1145/3490099.3511109
url: https://doi.org/10.1145/3490099.3511109
source: Snowball
snowball_from: "2805"
status: done
se_area: mobile app testing
se_task: screen similarity detection and transition event classification
platform: iOS
cv_technique: "UI object detector with transformer for screen similarity; siamese network for transition classification"
visual_artifact: mobile app screenshot
rationale: CV models detect whether two screenshots represent the same screen and classify the type of UI transition between them
evaluation: "F1 0.83 on screen similarity; average F1 0.71 on transition events across 1K+ iPhone apps"
challenge: same screen instances vary visually due to content loading and scrolling; different screens share structural similarities
---

## Notes

Trains two complementary CV models — one for screen identity and one for transition type — enabling smarter automated app crawling. The screen similarity model informs when to explore versus revisit; the transition model handles dialogs and keyboards. Infrastructure contribution for GUI state abstraction in testing tools.
