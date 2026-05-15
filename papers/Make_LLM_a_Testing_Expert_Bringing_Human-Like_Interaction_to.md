---
title: "Make LLM a Testing Expert: Bringing Human-Like Interaction to Mobile GUI Testing via Functionality-Aware Decisions"
year: 2023
venue: ICSE
doi: 10.1145/3597503.3639180
url: https://doi.org/10.1145/3597503.3639180
source: Snowball
snowball_from: "2778; 2805; 23"
status: done
se_area: mobile app testing
se_task: LLM-driven automated GUI exploration and testing
platform: Android
cv_technique: GUI screenshot understanding for LLM context
visual_artifact: mobile app screenshot
rationale: GUI screenshots are parsed and passed to an LLM as context to elicit human-like test interactions and functional reasoning
evaluation: "+32% activity coverage and 31% more bugs than best baseline on 93 Google Play apps; 35/53 new bugs confirmed and fixed"
challenge: learning-based approaches require large labeled data and generalize poorly; LLMs need structured GUI context to reason about app functionality
---

## Notes

GPTDroid frames mobile GUI testing as a conversational Q&A loop where GUI state is passed to an LLM to generate and execute test actions iteratively. The functionality-aware memory mechanism enables long-horizon reasoning across screens. Good example of CV serving as the perception layer for LLM-driven test agents.