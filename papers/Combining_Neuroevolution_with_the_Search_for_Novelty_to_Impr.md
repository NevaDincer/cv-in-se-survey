---
title: Combining Neuroevolution with the Search for Novelty to Improve the Generation of Test Suites for Games
year: 2024
venue: "ACM International Workshop on Foundations of Applied Software Engineering"
doi: 10.1145/3663532.3664467
url: https://doi.org/10.1145/3663532.3664467
source: ACM DL
snowball_from:
status: done
se_area: automated test generation
se_task: neural network-based test suite generation for games
platform: Scratch
cv_technique:
visual_artifact:
rationale: no CV involvement; neural networks act as test agents playing games, not as vision models processing visual input
evaluation: case study on two Scratch games
challenge: deceptive fitness landscapes in game-based code coverage search
---

## Notes

Extends Neatest by adding novelty search to neuroevolution-based test generation for Scratch games. CV is not used. 

Edge case for inclusion scope bcs the system under test happens to be a game with visual output, but CV plays no role in the approach.