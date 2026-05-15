---
title: "TestFlow: Advancing Mobile UI Testing through Multi-Step Reinforcement Learning"
year: 2025
venue: ISSTA
doi: 10.1145/3713081.3732930
url: https://doi.org/10.1145/3713081.3732930
source: ACM DL
snowball_from:
status: done
se_area: mobile app testing
se_task: automated GUI task completion for UI testing
platform: Android
cv_technique: multimodal GUI agent with SFT and reinforcement learning
visual_artifact: mobile app screenshot
rationale: CV processes UI screenshots as state observations to drive RL-based test action selection across multi-step tasks
evaluation: "33.69% WTSR and 55.37% SSR in cross-page test scenarios, outperforms baselines"
challenge: greedy step-by-step agents accumulate errors and miss long-horizon task dependencies
---

## Notes

TestFlow trains a multimodal agent with a two-phase pipeline, supervised fine-tuning then task-aware RL, to handle complex multi-step mobile UI testing. The reward function combines process and outcome signals to avoid shortsighted action choices. 

Relevant for the "RL-driven CV agents for SE" cluster.