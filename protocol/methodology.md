---
title: "Survey Methodology"
type: protocol
created: 2026-03-17
---

# Survey Methodology

Extension of Bajammal et al. (2022) — *A Survey on the Use of Computer Vision to Improve Software Engineering Tasks* — covering the period **2020–2026**.

---

## Research Questions

| RQ | Question |
|----|----------|
| RQ1 | What are the main SE areas and tasks for which CV approaches have been used (2020–2026)? |
| RQ2 | Why are CV approaches adopted in SE? |
| RQ3 | How are CV approaches applied to software and its visual artifacts? |
| RQ4 | How are SE tasks leveraging CV evaluated, and what challenges are reported? |

---

## Paper Collection

### Databases Searched
- IEEE Xplore
- ACM Digital Library
- Scopus
- Springer Link

### Search Period
January 2020 – March 2026

### Search Query
```
[computer vision OR image processing OR image analysis OR visual OR screenshot OR GUI]
AND
[requirements OR design OR development OR testing OR maintenance OR comprehension]
```

---

## Collection Process & Statistics

| Stage | Count |
|-------|-------|
| Initial pool (post-dedup) | ~2,716 |
| After second pass | 157 |
| Snowball candidates analyzed | 203 |
| Snowball included | +42 |
| **Final pool** | **199** |

---

## Snowballing

- **Method:** Backward snowballing (Wohlin 2014)
- **Source:** Reference lists of 154/157 papers (via Semantic Scholar API)
- **Total references fetched:** 3,296
- **Candidates after CV+SE keyword filter:** 203
- **After IC/EC application:** 42 included

---

## Data Extraction Fields (Bajammal Table 2)

| Field | YAML key | RQ |
|-------|----------|----|
| SE area | `se_area` | RQ1 |
| SE task | `se_task` | RQ1 |
| Target platform | (in `rq1_notes`) | RQ1 |
| Rationale | `rq2_notes` | RQ2 |
| Visual artifact type | `visual_artifact` | RQ3 |
| CV algorithm | `cv_technique` | RQ3 |
| Evaluation method | `rq4_notes` | RQ4 |
| Challenges/Limitations | `rq4_notes` | RQ4 |

---

## Comparison with Bajammal et al. (2022)

| Aspect | Bajammal (2022) | This Survey |
|--------|-----------------|-------------|
| Period | 2001–June 2020 | 2020–2026 |
| Final pool | 66 papers | 199 papers |
| Databases | 6 | 4 |
| Snowball yield | +9 | +42 |
| RQ framework | RQ1–RQ4 | Same RQ1–RQ4 |
