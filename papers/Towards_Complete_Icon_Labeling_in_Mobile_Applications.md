---
title: Towards Complete Icon Labeling in Mobile Applications
year: 2022
venue: CHI
doi: 10.1145/3491102.3502073
url: https://doi.org/10.1145/3491102.3502073
source: Snowball
snowball_from: "2610; 2502; 2805"
status: done
se_area: accessibility
se_task: mobile app icon type classification and labeling
platform: iOS
cv_technique: "image classification for common icons, few-shot learning for long-tail icons"
visual_artifact: mobile app icon
rationale: CV classifies icon types and detects contextual information to generate semantic labels for accessibility, UI search, and agent tasks
evaluation: "96.3% accuracy on common icons, 78.6% on long-tail; 99.5% coverage of 327,879 icons from iPhone apps; validated with 23 workers"
challenge: highly uneven icon distribution with 331+ long-tail types averaging only 67 examples each makes standard classification insufficient
---

## Notes

Addresses the long-tail problem in icon recognition using a two-model system: standard classification for common types and few-shot learning for rare ones. The 327k icon dataset and near-complete 99.5% coverage are significant contributions. Directly extends LabelDroid's scope from buttons to all icon types.