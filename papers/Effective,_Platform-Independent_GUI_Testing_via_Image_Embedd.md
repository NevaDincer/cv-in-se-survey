---
title: "Effective, Platform-Independent GUI Testing via Image Embedding and Reinforcement Learning"
year: 2024
venue: TOSEM
doi: 10.1145/3674728
url: https://doi.org/10.1145/3674728
source: Scopus
snowball_from:
status: done
se_area: Testing
se_task: Platform-independent automated GUI exploration testing
platform: General
cv_technique: "CNN (widget extraction + type classification); RNN (layout embedding)"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "6.3-41.4% more code coverage on mobile; 1.5-51.1% on web; 128 unique bugs detected"
challenge: "Hybrid/custom widgets invisible to layout parsers; reward function design for RL"
---

## Notes

Key insight: mobile and web widgets are visually identical across platforms — CV extracts them without layout file access. 

Combines microscopic (widget) + macroscopic (layout tree) state embedding for RL reward design. 

First platform-independent RL-based GUI testing tool. 

==read this later on==