# Research Log
## CV in SE Survey — 2020–2026

---

### Entry #2
**Date:** April 2026
**Stage:** Data extraction review

After the two screening passes (157 papers + 42 from snowballing = 199 total), I went back through all 199 notes in the Obsidian vault to review and fix the RQ1–RQ4 fields.

Paper notes had numeric prefixes (e.g., `11_Exploiting_Vision-Language_Models_in_GUI_Reuse`). These reflect the order papers were added during screening, not any ranking. I removed the numbers to distingused which of the papers i skimmed and which ones i did not.

#### How I filled each field

**RQ1 — SE Area**
- Testing → bug detection, test generation, coverage, fuzzing, glitch detection
- Maintenance → bug reports, change detection, refactoring, code review
- Development → code generation, UI implementation, design-to-code
- Requirements → UI prototyping, reuse, specification
- Design → visual design evaluation, layout analysis

**RQ1 — Platform**
Taken from the methodology or experimental setup section. If unspecified or multiple → *General*.

**RQ2 — Rationale**
- Context-driven → CV is used because the artifact is visual by nature; no further justification needed
- Performance-driven → authors explicitly argue CV outperforms non-visual methods
- If no justification is given → Context-driven by default

**RQ3 — Visual Artifact Type**
- Full-interface → entire app screen or screenshot
- Component → isolated UI element (button, icon, widget)
- Document image → receipt, form, scanned document
- Natural image → benchmark images (e.g., ImageNet), not SE artifacts
- Code → source code rendered as an image

**RQ4 — Challenges**
Taken from limitations, discussion, or threats to validity. If nothing is stated explicitly, inferred from the experimental setup.

#### What I skipped

Summary fields are intentionally left blank for all 199 papers. Full reads are not feasible at this scale. The RQ1–RQ4 fields are enough for the synthesis matrix and figures. Summaries can be added later for papers that are central to the findings.

#### Current state

All 199 notes are in `/papers/` with RQ1–RQ4 filled. `synthesis_matrix_199.csv` in `/data/` reflects the same data. Status is `to-read` for papers where only skim-level reading was done.

---

### Entry #1
**Stage:** Initial screening + vault setup

Search across IEEE Xplore, ACM DL, Scopus, and Springer gave 157 papers after title/abstract screening. Backward snowballing added 42 more, totaling 199. Papers were added to the vault in order and assigned numeric prefixes. RQ fields were filled during skim reading, then corrected in Entry #2.
