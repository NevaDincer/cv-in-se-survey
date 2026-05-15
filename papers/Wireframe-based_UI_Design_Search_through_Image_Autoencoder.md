---
title: Wireframe-based UI Design Search through Image Autoencoder
year: 2020
venue: TOSEM
doi: 10.1145/3391613
url: https://doi.org/10.1145/3391613
source: Scopus
snowball_from:
status: done
se_area: UI Design
se_task: UI design retrieval from wireframe sketches
platform: Mobile (Android)
cv_technique: Deep learning image autoencoder trained on real-app UI screenshots
visual_artifact: UI wireframe sketch
rationale: CV encodes wireframes and real UI designs into a shared latent space to enable similarity-based search
evaluation: "Experiments on artificially created relevant UI pairs and human evaluation; outperforms image-similarity and component-matching baselines"
challenge: Large variation in UI designs makes keyword and pixel-similarity search unreliable against rough wireframe input
---

## Notes

Trains an autoencoder on unlabeled real-app UIs so that a rough wireframe sketch can retrieve visually and structurally similar designs. No manual labeling needed and it outperforms both image-similarity and component-matching baselines. 

Same research group as [[Seenomaly_Vision-based_linting_of_gui_animation_effects_agai]]

useful for survey sections on CV-assisted UI design activities beyond testing