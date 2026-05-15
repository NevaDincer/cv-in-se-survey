---
title: Towards LLM-Based Automatic Playtest
year: 2025
venue: "ACM International Conference on the Foundations of Software Engineering"
doi: 10.1145/3696630.3728700
url: https://doi.org/10.1145/3696630.3728700
source: ACM DL
snowball_from:
status: done
se_area: game testing
se_task: automated playtesting of match-3 games
platform: desktop
cv_technique: screenshot-to-matrix conversion for game state extraction
visual_artifact: game screenshot
rationale: CV parses game board screenshots into numeric matrices to make visual game states consumable by an LLM for action planning
evaluation: higher code coverage and more crashes than 3 baseline tools on CasseBonbons open-source game
challenge: non-text games lack APIs for state description, making direct LLM application impractical without visual parsing
---

## Notes

Lap converts match-3 game screenshots into numeric matrices as a lightweight CV preprocessing step, then feeds them to ChatGPT-O1-mini for move generation. 

CV role is minimal (image-to-matrix conversion), with the core contribution being LLM-driven game logic reasoning.

Edge case for inclusion scope bcs CV is a thin preprocessing layer rather than a substantive technique.