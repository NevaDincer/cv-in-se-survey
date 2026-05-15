---
title: "DesignRepair: Dual-Stream Design Guideline-Aware Frontend Repair with Large Language Models"
year: 2025
venue: ICSE
doi: 10.1109/ICSE55347.2025.00109
url: https://doi.org/10.1109/ICSE55347.2025.00109
source: ACM DL
snowball_from:
status: done
se_area: UI quality assurance
se_task: design guideline violation detection and frontend code repair
platform: web
cv_technique: rendered page analysis via Playwright
visual_artifact: rendered webpage screenshot
rationale: CV analyzes the rendered page visually alongside code analysis to detect Material Design violations that are only visible at runtime
evaluation: significant improvements in design guideline adherence, accessibility, and usability metrics on LLM-generated UIs
challenge: LLM-generated UIs often violate design principles that are not detectable from code alone without rendering
---

## Notes

DesignRepair runs two parallel streams, static code analysis and rendered page CV analysis, then uses RAG with GPT-4 to repair violations against a Material Design knowledge base. The dual-stream approach is the key insight: some design issues only manifest visually after rendering. 

Relevant for the "CV as design quality oracle" cluster.