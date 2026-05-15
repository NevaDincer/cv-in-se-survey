---
title: "SeeAction: Towards Reverse Engineering How-What-Where of HCI Actions from Action Screencasts"
year: 2025
venue: ICSE
doi: 10.1109/ICSE55347.2025.00144
url: https://doi.org/10.1109/ICSE55347.2025.00144
source: IEEE Xplore
snowball_from:
status: done
se_area: UI automation
se_task: user action recognition from screencasts for script generation
platform: desktop
cv_technique: "deep learning, multi-task learning, video understanding"
visual_artifact: screencast video
rationale: CV model recognizes commands, widgets, and locations from screen recordings to auto-generate UI automation scripts without OS or framework access
evaluation: 7260 video-action pairs across Word, Zoom, Firefox, Photoshop, Windows 10 Settings
challenge: non-intrusive action recognition without accessibility APIs or app source access
---

## Notes

SeeAction frames UI script generation as a CV problem over screencasts, jointly learning command type, target widget, and spatial location. 

Unlike record-and-replay tools that require OS hooks, it works ==purely from video.==

==Strong candidate for the "CV enabling non-intrusive SE tooling" cluster.==