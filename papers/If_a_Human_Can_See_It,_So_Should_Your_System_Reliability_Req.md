---
title: "If a Human Can See It, So Should Your System: Reliability Requirements for Machine Vision Components"
year: 2022
venue: ICSE
doi: 10.1145/3510003.3510109
url: https://doi.org/10.1145/3510003.3510109
source: Scopus
snowball_from:
status: done
se_area: Requirements Engineering
se_task: Defining and verifying reliability requirements for ML-based vision components
platform: General
cv_technique: Image classification models under image transformations
visual_artifact: Transformed images (brightness, blur, rotation etc.)
rationale: Proposes SE-style reliability requirements for CV components using human performance as a correctness baseline
evaluation: "13 pre-trained image classification models; ~2000 human participants across 8 transformation types"
challenge: ML-based MVCs lack formally specified requirements; existing testing methods miss reliability gaps detected by this approach
---

## Notes

Frames CV component quality as a requirements engineering problem rather than just a benchmark problem. 
Human performance data from 2000 participants is used to set the reliability bar, making requirements both principled and machine-verifiable. 

==Strong fit for surveys covering testing or quality assurance of ML/CV components in software systems.==