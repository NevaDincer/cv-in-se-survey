"""
Paper collection workflow diagram for the CV-in-SE survey extension.
Style reference: Bajammal et al. 2022, Fig. 2.
Uses matplotlib patches and annotations only (no external dependencies).
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUTPUT = "/mnt/user-data/outputs/fig0_paper_collection_workflow.pdf"

fig, ax = plt.subplots(figsize=(11, 5))
ax.set_xlim(0, 11)
ax.set_ylim(0, 5)
ax.axis("off")

# ── Color palette ─────────────────────────────────────────────────────────
C_BOX    = "#FFFFFF"   # box fill
C_BORDER = "#2B6CB0"   # box border
C_DARK   = "#1A365D"   # header fill
C_TEXT   = "#1A202C"   # main text
C_GRAY   = "#718096"   # sub-text
C_ARROW  = "#4A5568"

def box(ax, x, y, w, h, label, sublabel=None, dark=False):
    """Draw a rounded box with optional sublabel."""
    fc = C_DARK if dark else C_BOX
    tc = "white" if dark else C_TEXT
    patch = FancyBboxPatch(
        (x - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.05",
        linewidth=1.4,
        edgecolor=C_BORDER,
        facecolor=fc,
        zorder=3
    )
    ax.add_patch(patch)
    if sublabel:
        ax.text(x, y + 0.13, label, ha="center", va="center",
                fontsize=8.5, color=tc, fontweight="bold", zorder=4)
        ax.text(x, y - 0.18, sublabel, ha="center", va="center",
                fontsize=7.5, color=C_GRAY, zorder=4)
    else:
        ax.text(x, y, label, ha="center", va="center",
                fontsize=8.5, color=tc, fontweight="bold", zorder=4)

def arrow(ax, x1, y1, x2, y2):
    ax.annotate("",
        xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="-|>",
            color=C_ARROW,
            lw=1.3,
            mutation_scale=12
        ),
        zorder=2
    )

def label_on_arrow(ax, x, y, text):
    ax.text(x, y, text, ha="center", va="center",
            fontsize=7.5, color=C_GRAY,
            bbox=dict(fc="white", ec="none", pad=1.5))

# ── Row 1: Search sources ─────────────────────────────────────────────────
sources = [
    (1.1, 4.2, "IEEE Xplore"),
    (2.6, 4.2, "ACM DL"),
    (4.1, 4.2, "Scopus"),
    (5.6, 4.2, "Snowballing"),
]
for x, y, lbl in sources:
    box(ax, x, y, 1.3, 0.55, lbl, dark=True)

# ── Row 2: Raw results pool ───────────────────────────────────────────────
box(ax, 3.35, 3.1, 2.8, 0.58,
    "Automated Search Results", "2,716 candidate papers")

# Arrows from sources to pool
for x, y, _ in sources[:3]:   # IEEE, ACM, Scopus
    arrow(ax, x, y - 0.28, 3.35 + (x - 3.35)*0.3, 3.1 + 0.29)
# Snowball points separately to the right of pool
arrow(ax, 5.6, 3.94, 5.6, 3.39)

# ── Pipeline boxes (right side, top to bottom) ────────────────────────────
pipeline = [
    (8.0, 4.35, "Remove Duplicates",      "→ 1,482 papers"),
    (8.0, 3.40, "Apply Inclusion Criteria","→ 151 papers"),
    (8.0, 2.45, "Apply Exclusion Criteria","→ 57 papers"),
    (8.0, 1.50, "Snowballing",             "+ 11 papers"),
    (8.0, 0.58, "Final Corpus",            "187 papers"),
]

for x, y, lbl, sub in pipeline:
    dark = (lbl == "Final Corpus")
    box(ax, x, y, 2.6, 0.58, lbl, sub, dark=dark)

# Arrow from pool to first pipeline step
arrow(ax, 4.75, 3.1, 6.7, 4.35)

# Arrows down the pipeline
for i in range(len(pipeline) - 1):
    x, y = pipeline[i][0], pipeline[i][1]
    xn, yn = pipeline[i+1][0], pipeline[i+1][1]
    arrow(ax, x, y - 0.29, xn, yn + 0.29)

# ── Manual search box (lower left) ────────────────────────────────────────
box(ax, 2.0, 1.50, 2.6, 0.58,
    "Manual SE Venue Search",
    "14 target venues")

# Arrow from manual search to Snowballing step
arrow(ax, 3.3, 1.50, 6.7, 1.50)
label_on_arrow(ax, 5.0, 1.60, "venue papers fed\ninto snowballing")

# ── Section labels ────────────────────────────────────────────────────────
ax.text(2.7, 4.72, "Study Identification", ha="center", va="center",
        fontsize=9, color=C_BORDER, fontweight="bold")
ax.text(8.0, 4.72, "Study Selection", ha="center", va="center",
        fontsize=9, color=C_BORDER, fontweight="bold")

# Bracket lines under section labels
for x1, x2, y in [(0.4, 5.0, 4.60), (6.65, 9.35, 4.60)]:
    ax.plot([x1, x2], [y, y], color=C_BORDER, lw=1.2, zorder=2)
    ax.plot([x1, x1], [y, y - 0.08], color=C_BORDER, lw=1.2, zorder=2)
    ax.plot([x2, x2], [y, y - 0.08], color=C_BORDER, lw=1.2, zorder=2)

fig.tight_layout(pad=0.3)
fig.savefig(OUTPUT, bbox_inches="tight", dpi=180)
plt.close(fig)
print(f"Saved: {OUTPUT}")
