---
title: "GUIGAN: Learning to Generate GUI Designs Using Generative Adversarial Networks"
year: 2021
venue: ICSE
doi: 10.1109/icse43902.2021.00074
url: https://doi.org/10.1109/icse43902.2021.00074
source: Snowball
snowball_from: "989; 2649; 299; 1550; 2805"
status: done
se_area: Design
se_task: Automated GUI design generation from existing app screenshots
platform: Mobile
cv_technique: "GAN (SeqGAN-based component selection and composition)"
visual_artifact: Component
rationale: Context-driven
evaluation: "30.77% improvement in FID; 12.35% in 1-NNA over baselines; user study"
challenge: "Gap between textual query and visual intent; IP concerns with direct reuse; outdated design styles"
---

## Notes

Formulates GUI generation as sequence generation (like NLP) rather than pixel generation. Reuses real component subtrees from existing apps to compose novel designs. 

Bridges Gallery D.C. (548) search and sketch-to-code generation. 

ICSE 2021, strong quantitative and user study evaluation.
