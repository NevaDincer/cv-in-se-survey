---
title: Mobile App Crowdsourced Test Report Consistency Detection via Deep Image-and-Text Fusion Understanding
year: 2021
venue: TSE
doi: 10.1109/tse.2023.3285787
url: https://doi.org/10.1109/tse.2023.3285787
source: Snowball
snowball_from: "397; 2805"
status: done
se_area: crowdsourced testing
se_task: crowdsourced test report consistency detection
platform: Android
cv_technique: deep learning for GUI screenshot feature extraction in image-text fusion
visual_artifact: mobile app screenshot
rationale: CV extracts screenshot features to detect whether bug descriptions are consistent with their attached screenshots
evaluation: evaluated on 22k+ test reports; user study confirming practical value for report review efficiency
challenge: only 18.07% of crowdsourced reports are consistent; inconsistency wastes developer review effort
---

## Notes

ReCoDe first classifies reports by bug type from text, then applies type-specific strategies combining screenshot CV features to judge text-image consistency. Complements SemCluster and DeepPrior in the crowdsourced testing cluster, targeting report quality rather than deduplication or prioritization.