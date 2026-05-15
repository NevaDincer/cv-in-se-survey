# PROGRESS_NOTES.md

## CV in SE Survey — Personal Research Log

---

## Progress Note #2

**Date:** April 2026 **Stage:** Data extraction review + Obsidian vault setup

### What I did

After completing the first pass (title + abstract screening) and second pass (157 included papers + 42 from backward snowballing = 199 total), I went back through all 199 papers in the Obsidian vault to review and correct the data extraction fields (RQ1–RQ4).

The paper notes are numbered (e.g., `11_Exploiting_Vision-Language_Models_in_GUI_Reuse`). These numbers come from the original screening order — papers were numbered sequentially as they were added to the vault during the first and second pass, so the prefix reflects inclusion order, not ranking or relevance.

### Field extraction criteria

I used the following rules to fill each field, based on a reading guide developed iteratively during extraction:

**RQ1 — SE Area**

- **Testing** → bug detection, test generation, coverage, fuzzing, glitch/anomaly detection
- **Maintenance** → bug reports, change detection, refactoring, code review
- **Development** → code generation, UI implementation, design-to-code
- **Requirements** → UI prototyping, reuse, specification
- **Design** → visual design evaluation, layout analysis

**RQ1 — Platform** Filled from methodology or experimental setup section. If multiple platforms or unspecified → General.

**RQ2 — Rationale**

- **Context-driven** → CV used because the artifact is inherently visual (screenshots, UI images); no explicit justification needed beyond the nature of the input
- **Performance-driven** → authors explicitly argue CV outperforms non-visual alternatives
- If authors give no justification → Context-driven by default

**RQ3 — Visual Artifact Type**

- **Full-interface** → entire app screen or screenshot
- **Component** → isolated UI element (button, icon, widget)
- **Document image** → receipt, form, scanned document
- **Natural image** → benchmark dataset images (e.g., ImageNet), not SE artifacts
- **Code** → source code rendered as image

**RQ4 — Challenges** Taken from Limitations, Discussion, or Threats to Validity sections. If none explicitly stated, inferred from experimental setup constraints.

### What I did not include

**Summary field:** The template includes a 2–3 sentence summary section. I intentionally left this blank for all 199 papers at this stage. Given the volume, filling summaries would require full paper reads which is not feasible within the current timeline. The RQ1–RQ4 fields contain all information needed for the synthesis matrix and figures. Summaries can be added selectively for papers that appear prominently in the findings or discussion sections.

### Current state of the vault

All 199 paper notes exist in `/papers/` with RQ1–RQ4 fields populated. The `synthesis_matrix_199.csv` in `/data/` reflects the same extractions. Summary fields are blank. Status field is set to `to-read` for papers where only skim-level reading was done.

---

## Progress Note #1

**Stage:** Initial screening + vault setup

Database search across IEEE Xplore, ACM Digital Library, Scopus, and Springer yielded 157 papers after inclusion/exclusion on title and abstract. Backward snowballing on the included set added 42 further papers, bringing the total to 199. Papers were added to the Obsidian vault sequentially and assigned numeric prefixes reflecting inclusion order. First-pass RQ fields were filled during skim reading (abstract + figures + section headers). These were later reviewed and corrected in Progress Note #2.