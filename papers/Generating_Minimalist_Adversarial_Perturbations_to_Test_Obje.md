---
title: "Generating Minimalist Adversarial Perturbations to Test Object-Detection Models: An Adaptive Multi-Metric Evolutionary Search Approach"
year: 2024
venue: ICSTW 2024
doi: 10.1109/ICSTW60967.2024.00015
url: https://doi.org/10.1109/ICSTW60967.2024.00015
source: IEEE Xplore
snowball_from:
status: done
se_area: Testing
se_task: Adversarial robustness testing of object detection DL models
platform: General
cv_technique: "DETR; Faster R-CNN (as subject under test); adversarial perturbation generation"
visual_artifact: Natural image
rationale: Context-driven
evaluation: "60% less noise than EvoAttack baseline on COCO and KITTI datasets; DETR and Faster R-CNN"
challenge: "Balancing attack effectiveness with minimal perturbation; black-box model access constraints"
---

## Notes

Eleventh edge case: CV object detection models (DETR, Faster R-CNN) are what is being robustness-tested via adversarial examples. 

Genetic algorithm generates minimally perturbed attack images. Same boundary group as [[DeltaNN_Assessing_the_Impact_of_Computational_Environment_Pa]], [[DecompoVision_Reliability_Analysis_of_Machine_Vision_Compone]], [[MT4Image_An_efficient_metamorphic_testing_approach_for_image]]. 

Workshop paper.