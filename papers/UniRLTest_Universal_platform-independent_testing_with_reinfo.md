---
title: "UniRLTest: Universal platform-independent testing with reinforcement learning via image understanding"
year: 2022
venue: ISSTA
doi: 10.1145/3533767.3543292
url: https://doi.org/10.1145/3533767.3543292
source: Scopus
snowball_from:
status: done
se_area: GUI Testing
se_task: Automated platform-independent GUI exploration and testing
platform: Cross-platform
cv_technique: Widget detection from screenshots to build widget tree
visual_artifact: App screenshot
rationale: CV extracts widgets and layout from screenshots to enable RL-based testing without platform-specific APIs
evaluation: 25 apps across platforms; outperforms baselines in efficiency and effectiveness
challenge: Platform diversity makes framework-dependent tools impractical; RL exploration must work from visual input alone
---

## Notes

Uses CV to build a widget tree from screenshots, then drives exploration with Deep Q-Network treating each screen as an MDP state. The platform-independence angle is the key contribution since the system never accesses platform APIs. 



