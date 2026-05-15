---
title: Improving Code Extraction from Coding Screencasts Using a Code-Aware Encoder-Decoder Model
year: 2023
venue: ASE
doi: 10.1109/ASE56229.2023.00184
url: https://doi.org/10.1109/ASE56229.2023.00184
source: ACM DL
snowball_from:
status: done
se_area: knowledge transfer
se_task: code extraction from tutorial screencasts and screenshots
platform:
cv_technique: OCR with CodeT5-based post-processing
visual_artifact: code screenshot / screencast frame
rationale: OCR extracts text from code screenshots and video frames; a fine-tuned LLM then corrects OCR errors using code-aware language understanding
evaluation: outperforms baselines on 585K OCR-ground truth pairs from 10K+ Java GitHub projects
challenge: OCR accuracy degrades on code due to syntax complexity and varied screencast formatting
---

## Notes

CodeT5-OCRfix treats OCR-extracted code as a noisy sequence and fine-tunes CodeT5 to correct it, framing code extraction as a seq2seq repair problem.

Good example of CV (OCR) and code LLM being pipelined for a developer knowledge reuse task.

Pairs well with [[SeeAction_Towards_Reverse_Engineering_How-What-Where_of_HCI]] in the "CV for extracting SE artifacts from visual media" cluster.
