---
title: Learning to Denoise Raw Mobile UI Layouts for Improving Datasets at Scale
year: 2022
venue: CHI
doi: 10.1145/3491102.3502042
url: https://doi.org/10.1145/3491102.3502042
source: Snowball
snowball_from: "2892; 2685"
status: done
se_area: dataset and tooling
se_task: mobile UI layout dataset denoising and annotation
platform: Android
cv_technique: deep learning on screenshot-layout pairs for node validity and type classification
visual_artifact: mobile app screenshot
rationale: CV cross-references screenshots against raw UI layouts to remove invalid nodes and assign semantic types at scale
evaluation: "F1 82.7% for invalid node detection, 85.9% for type recognition on 59,555 annotated screens from Rico"
challenge: raw UI layout datasets contain noisy nodes that lack visual representation and generic types that hinder semantic analysis
---

## Notes

CLAY improves UI layout dataset quality by using screenshots as ground truth to clean and retype raw accessibility tree nodes. Infrastructure paper — not a testing or development tool itself, but foundational for downstream CV-based SE research that depends on clean UI layout data. Useful to cite when discussing dataset quality in the survey.

