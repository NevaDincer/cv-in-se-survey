---
title: Automating GUI Testing with Image-Based Deep Reinforcement Learning
year: 2020
venue: International Conference on Autonomic Computing and Self-Organizing Systems
doi: 10.1109/acsos49614.2020.00038
url: https://doi.org/10.1109/acsos49614.2020.00038
source: Snowball
snowball_from: 2805
status: done
se_area: Testing
se_task: "Image-based DRL GUI testing"
platform: General
cv_technique: "Deep Reinforcement Learning; CNN"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "Accuracy metrics"
challenge: "Requires large labeled training data"
---

## Notes

Uses A3C reinforcement learning directly on GUI screenshots — no DOM or accessibility tree needed, just pixels in and actions out. Achieves up to 6x better exploration efficiency than baseline algorithms and rivals experienced human testers. Strong case for purely vision-driven test agents; useful contrast against tools that rely on widget metadata.