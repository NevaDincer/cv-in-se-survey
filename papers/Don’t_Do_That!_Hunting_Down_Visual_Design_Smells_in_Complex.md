---
title: "Don't Do That! Hunting Down Visual Design Smells in Complex UIs Against Design Guidelines"
year: 2021
venue: ICSE
doi: 10.1109/icse43902.2021.00075
url: https://doi.org/10.1109/icse43902.2021.00075
source: Snowball
snowball_from: "989; 2892; 2502; 2778"
status: done
se_area: Design
se_task: Automated visual design smell detection against Material Design guidelines
platform: Mobile
cv_technique: "Multi-modal analysis (component metadata; typography; iconography; color; edge detection)"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "Precision 0.81; recall 0.90 on 60756 UIs from 9286 apps; user study"
challenge: "7 design dimensions; 4 component aspects; developer lack of training on don't-guidelines"
---

## Notes

Extends code smell concept to UI: "visual design smells" from violating Material Design don't-guidelines. UIS-Hunter detects violations across 60k real app UIs. 

Multi-modal (visual + metadata) approach. Connects to MotorEase in the accessibility/design quality space but more comprehensive in scope. 

ICSE 2021.