---
title: "Inclusion & Exclusion Criteria"
type: protocol
created: 2026-03-17
---

# Inclusion & Exclusion Criteria

Same framework as Bajammal et al. (2022), applied to 2020–2026 literature.

---

## Inclusion Criteria

| ID | Criterion |
|----|-----------|
| IC1 | Contributes to any SE lifecycle stage (requirements, design, development, testing, maintenance) |
| IC2 | Uses CV/image processing on visual software artifacts (screenshots, videos, sketches, UI images) |
| IC3 | Full technical research paper with detailed description of the visual approach |
| IC4 | Contains quantitative/qualitative evaluation or use-case illustration |

**Decision:** INCLUDE if IC1 ∧ IC2 ∧ IC3 ∧ IC4 = YES

---

## Exclusion Criteria

| ID | Criterion |
|----|-----------|
| EC1 | Software **visualization** only — no CV input, only visual output |
| EC2 | Tool/service **without** a peer-reviewed publication |
| EC3 | **Duplicate** of an already-included paper |
| EC4 | **Not peer-reviewed** (arXiv preprint with no published venue) |
| EC5 | Published **before 2020** (outside survey period) |

**Decision:** EXCLUDE if any EC = YES

---

## Boundary Cases

| Case | Decision | Rationale |
|------|----------|-----------|
| Extended journal version of included conference paper | EXCLUDE | Avoids duplication |
| Short/demo paper with detailed approach section | INCLUDE | IC3 satisfied if approach described |
| Survey/SLR about CV-in-SE | INCLUDE | Contributes to landscape (RQ1/RQ4) |
| DL testing (testing DL models, no visual SE artifact) | EXCLUDE | IC1 fails — subject is not SE visual artifact |
| Accessibility paper using CV on UI screenshots | INCLUDE | IC1 + IC2 both satisfied |
