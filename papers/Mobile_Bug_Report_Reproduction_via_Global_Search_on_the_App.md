---
title: Mobile Bug Report Reproduction via Global Search on the App UI Model
year: 2024
venue: PACM SE
doi: 10.1145/3660824
url: https://doi.org/10.1145/3660824
source: ACM DL
snowball_from:
status: done
se_area: bug reporting
se_task: automated bug report reproduction for mobile apps
platform: Android
cv_technique: GUI screenshot-based UI model construction
visual_artifact: mobile app screenshot
rationale: CV captures UI states as screenshots to build the app UI model used for global Markov-based step matching
evaluation: "94% reproduction rate on 72 real-world bug reports; 93% on reports with missing steps; outperforms ReCDroid, Yakusu, ReproBot"
challenge: missing or inaccurate bug report steps cause greedy search approaches to fail at incorrect UI states
---

## Notes

Roam reframes bug reproduction as a Markov model search problem, using dynamic programming to find globally optimal step-to-event matches rather than greedy local matching. 

CV's role is building the UI state graph. 


Relevant for the "bug reproduction" cluster alongside ScopeDroid and CAPdroid.