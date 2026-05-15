---
title: "PredART: Towards Automatic Oracle Prediction of Object Placements in Augmented Reality"
year: 2023
venue: ASE
doi: 10.1145/3551349.3561160
url: https://doi.org/10.1145/3551349.3561160
source: ACM DL
snowball_from:
status: done
se_area: AR app testing
se_task: virtual object placement quality prediction as test oracle
platform: AR mobile apps
cv_technique: hybrid neural network for image regression
visual_artifact: AR app screenshot
rationale: CV predicts human perception scores for virtual object placements to serve as an automated test oracle
evaluation: "85.0% accuracy, MAE 0.047, RMSE 0.091 on 480 screenshots"
challenge: placement correctness is subjective and perceptual, requiring crowd-sourced ground truth and regression rather than classification
---

## Notes

PredART is the direct predecessor of VOPA same AR placement oracle problem but framed as regression over human rating scores rather than binary classification. 
Reading both together shows the evolution from score prediction to error detection in AR testing. 


