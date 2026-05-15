---
title: Automated visual testing for mobile apps in an industrial setting
year: 2022
venue: ICSE-SEIP
doi: 10.1145/3510457.3513027
url: https://doi.org/10.1145/3510457.3513027
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: automated visual test generation
platform: "Android, iOS, AliOS, Harmony OS"
cv_technique: screenshot-based UI element detection and interaction
visual_artifact: mobile app screenshot
rationale: CV processes device screenshots as the sole input to enable cross-platform test generation without platform API access
evaluation: "+87.6% activity coverage over Monkey on Taobao with ~1B monthly active users; deployed at Alibaba and Software Green Alliance"
challenge: non-standard UI elements whose internal structure is inaccessible via platform accessibility APIs
---

## Notes

VTest is a rare industrial-scale deployment paper where CV-driven visual testing replaced API-dependent tools on a billion-user app across four OS platforms. 
