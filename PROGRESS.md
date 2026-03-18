# Survey Progress

**CV in SE: 2020–2026** — Extension of Bajammal et al. (2022)

---

## Status

| Stage | Status | Details |
|-------|--------|---------|
| Database search | Done | IEEE Xplore, ACM DL, Scopus, Springer |
| First pass | Done | Inclusion/exclusion on title + abstract |
| Second pass | Done | 157 papers included |
| Backward snowballing | Done | +42 papers → **199 total** |
| Data extraction (RQ1–RQ4) |  Done | synthesis_matrix_199.csv |
| Paper reading & notes | In progress | Obsidian vault |
| Figures (Fig 3–10) | Done | See /figures |
| Writing — Methodology | Next | |
| Writing — Findings (RQ1–RQ4) | | |
| Writing — Discussion | | |

---

## Collection Summary

| Source | Papers |
|--------|--------|
| Database search (IEEE, ACM, Scopus, Springer) | 157 |
| Backward snowballing | +42 |
| **Total** | **199** |

---

## Key Findings (Preliminary)

### RQ1 — SE Areas & Tasks
| Area | n | % |
|------|---|---|
| Testing | 135 | 67.8% |
| Maintenance | 23 | 11.6% |
| Development | 20 | 10.1% |
| Design | 14 | 7.0% |
| Requirements | 3 | 1.5% |

Top platforms: Mobile (63), Web (19), Game (8), Desktop (4)

### RQ2 — Rationale
| Rationale | n |
|-----------|---|
| Context-driven | 191 |
| Robustness | 19 |
| Ease of use | 12 |

### RQ3 — CV Techniques
| Technique | n |
|-----------|---|
| Deep Learning / Neural Network | 174 |
| Template Matching / Feature Matching | 20 |
| Image Differencing | 18 |
| OCR | 13 |
| Color / Spatial Transformation | 13 |
| Representation Learning / Embedding | 13 |

Dominant artifact type: Full-interface screenshots (167/199)

### RQ4 — Evaluation & Challenges
Top challenge: Requires large labeled training data (72 papers)

---

## Comparison with Bajammal et al. (2022)

| | Bajammal (2022) | This survey |
|--|--|--|
| Period | 2001–June 2020 | 2020–2026 |
| Pool size | 66 | **199** |
| Snowball yield | +9 | +42 |
| Top SE area | Testing | Testing |
| Top CV technique | Machine Learning (few) | Deep Learning (174/199) |
| Top platform | Web / Desktop | **Mobile** |

---

## Repository Structure

```
papers/        <- 199 paper notes (Obsidian .md)
protocol/      <- methodology.md, criteria.md
data/          <- synthesis_matrix_199.csv
figures/       <- Fig 3–10 (PDF + PNG)
```
