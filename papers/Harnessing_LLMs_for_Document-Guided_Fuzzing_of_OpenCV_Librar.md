---
title: Harnessing LLMs for Document-Guided Fuzzing of OpenCV Library
year: 2025
venue: ICSME 2025
doi: 10.1109/ICSME64153.2025.00017
url: https://doi.org/10.1109/ICSME64153.2025.00017
source: IEEE Xplore
snowball_from:
status: done
se_area: Testing
se_task: LLM-guided fuzz testing of OpenCV library APIs
platform: General
cv_technique: "OpenCV APIs (as subject under test)"
visual_artifact: Natural image
rationale: Context-driven
evaluation: "17 new bugs found in 330 OpenCV APIs; 10 confirmed; 5 fixed"
challenge: "OpenCV APIs have strict parameter dependencies; many APIs poorly or undocumented"
---

## Notes

Tenth edge case: OpenCV library is what is being tested via LLM-guided fuzzing. SE method (fuzzing) applied to CV library. ICSME 2025, strong results. 

Same boundary group as [[DeltaNN_Assessing_the_Impact_of_Computational_Environment_Pa]], [[DecompoVision_Reliability_Analysis_of_Machine_Vision_Compone]], [[MT4Image_An_efficient_metamorphic_testing_approach_for_image]] group. 


==Notable that LLMs parse API docs to extract parameter constraints.==