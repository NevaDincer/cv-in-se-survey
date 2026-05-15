---
title: "GIFdroid: Automated Replay of Visual Bug Reports for Android Apps"
year: 2022
venue: ICSE
doi: 10.1145/3510003.3510048
url: https://doi.org/10.1145/3510003.3510048
source: Scopus
snowball_from:
status: done
se_area: Maintenance
se_task: Automated bug report replay from screen recordings
platform: Mobile
cv_technique: "Image processing (keyframe extraction; GUI state matching via image similarity)"
visual_artifact: Full-interface
rationale: Context-driven
evaluation: "Automated experiments + user study on accuracy and efficiency"
challenge: "Screen recordings are long and contain unclear actions; non-technical users cannot write precise bug descriptions"
---

## Notes

Extracts keyframes from bug report GIF/video, maps them to GUI Transition Graph states, generates replay trace. Lightweight CV approach. 

Connects to [[Translating_Video_Recordings_of_Complex_Mobile_App_UI_Gestur]] which also translates video to replayable scenarios but for general testing rather than bug reproduction specifically. ICSE 2022.