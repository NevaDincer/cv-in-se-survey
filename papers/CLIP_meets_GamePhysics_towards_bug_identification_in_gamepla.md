---
title: "CLIP meets GamePhysics: towards bug identification in gameplay videos using zero-shot transfer learning"
year: 2022
venue: MSR
doi: 10.1145/3524842.3528438
url: https://doi.org/10.1145/3524842.3528438
source: ACM DL
snowball_from:
status: done
se_area: game testing
se_task: bug-related gameplay video retrieval
platform: PC games
cv_technique: "CLIP zero-shot vision-language retrieval"
visual_artifact: gameplay video
rationale: CLIP encodes video frames and text queries into a shared embedding space to retrieve bug-relevant gameplay videos without any training data
evaluation: evaluated on GamePhysics dataset of 26,954 videos from 1,873 games across simple, compound, and bug queries
challenge: large gameplay video repositories lack structured metadata; content-based retrieval requires understanding visual game physics events
---

## Notes

Uses CLIP zero-shot transfer to search gameplay videos by natural language, requiring no labels or fine-tuning. 
The GamePhysics dataset is a significant open contribution for game SE research. 

Good example of a foundation CV model being repurposed for a niche SE task with zero task-specific training.