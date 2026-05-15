---
title: "BAGEL: An Approach to Automatically Detect Navigation-Based Web Accessibility Barriers"
year: 2023
venue: CHI
doi: 10.1145/3544548.3580749
url: https://doi.org/10.1145/3544548.3580749
source: ACM DL
snowball_from:
status: done
se_area: accessibility testing
se_task: keyboard navigation accessibility barrier detection
platform: web
cv_technique:
visual_artifact:
rationale: no CV involvement; approach detects keyboard navigation barriers through interaction testing rather than visual analysis
evaluation: high precision and recall on real-world web applications (exact metrics not in abstract)
challenge: modern websites frequently violate keyboard navigability guidelines despite their importance for users with disabilities
---

## Notes

BAGEL automatically tests keyboard navigation paths on web pages to find accessibility barriers. 

No CV is used - the approach is interaction-based. ==Edge case for inclusion scope; accessibility testing theme overlaps with [[MotorEase_Automated_Detection_of_Motor_Impairment_Accessibil]] but the method is purely behavioral rather than visual.==
