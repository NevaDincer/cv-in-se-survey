"""
Chart generation script for the CV-in-SE survey extension.
Data is read directly from paper frontmatter (.md files).
Excluded papers (papers/exclude/) are skipped automatically.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os, re
from collections import Counter

# ── Paths ────────────────────────────────────────────────────────────────────
PAPERS_DIR = "/home/claude/cv-in-se-survey/papers"
OUTPUT_DIR = "/mnt/user-data/outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Global style ─────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size":   10,
    "figure.dpi":  180,
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.grid": False,
})

BLUE = "#2B6CB0"
GRAY = "#718096"

# ── Read frontmatter ─────────────────────────────────────────────────────────
files = [
    f for f in os.listdir(PAPERS_DIR)
    if f.endswith(".md") and f != "Untitled.md"
]

def get_field(content, field):
    m = re.search(rf"^{field}:\s*(.+)$", content, re.MULTILINE)
    return m.group(1).strip().strip('"').strip("'") if m else ""

raw = {"year": [], "venue": [], "se_area": [], "platform": [], "visual_artifact": []}

for fname in files:
    with open(os.path.join(PAPERS_DIR, fname)) as f:
        content = f.read()
    for field in raw:
        raw[field].append(get_field(content, field))

# ── Normalize: SE Area ───────────────────────────────────────────────────────
# Merge similar labels into clean top-level categories
SE_MAP = {
    # Testing bucket
    "Testing":              "Testing",
    "GUI Testing":          "Testing",
    "GUI testing":          "Testing",
    "web GUI testing":      "Testing",
    "GUI test automation":  "Testing",
    "model-based testing":  "Testing",
    "automated test generation": "Testing",
    "UI quality assurance": "Testing",
    "DL system testing":    "Testing",
    "crowdsourced testing": "Testing",
    "AR app testing":       "Testing",
    # Mobile app testing kept separate (large enough)
    "mobile app testing":   "Mobile app testing",
    # Game testing kept separate
    "game testing":         "Game testing",
    # Accessibility
    "accessibility":        "Accessibility",
    "accessibility testing":"Accessibility",
    # Maintenance
    "Maintenance":          "Maintenance",
    # Code generation
    "code generation":      "Code generation",
    # GUI design & requirements
    "GUI design":           "GUI design & requirements",
    "Design":               "GUI design & requirements",
    "UI Design":            "GUI design & requirements",
    "requirements and design": "GUI design & requirements",
    "Requirements":         "GUI design & requirements",
    "Requirements Engineering": "GUI design & requirements",
    # Development
    "Development":          "Development",
    "Software Application Development": "Development",
    "Web Development":      "Development",
    "UI automation":        "Development",
    # Bug reporting
    "bug reporting":        "Bug reporting",
    "Bug Reproduction":     "Bug reporting",
    # Web app testing -> Testing
    "web app testing":      "Testing",
    # Remaining small ones -> Other
    "documentation":             "Other",
    "documentation maintenance": "Other",
    "dataset and tooling":       "Other",
    "survey":                    "Other",
    "empirical SE / developer studies": "Other",
    "knowledge transfer":        "Other",
    "document understanding":    "Other",
}

se_normalized = [SE_MAP.get(a, "Other") for a in raw["se_area"] if a]

# ── Normalize: Platform ──────────────────────────────────────────────────────
# Filter out corrupted entries (cv_technique values in platform field)
def is_valid_platform(p):
    return bool(p) and not p.startswith("cv_technique")

PLAT_MAP = {
    "Android":                  "Android",
    "Mobile (Android)":         "Android",
    "Android, iOS":             "Android",
    "Android, Android TV":      "Android",
    "Android, iOS, AliOS, Harmony OS": "Android",
    "Android, VS Code":         "Android",
    "Android, iOS, mobile web": "Android",
    "Mobile":                   "Mobile (general)",
    "mobile":                   "Mobile (general)",
    "Mobile (Android, iOS)":    "Mobile (general)",
    "mobile, web":              "Mobile (general)",
    "mobile games":             "Mobile (general)",
    "iOS":                      "Mobile (general)",
    "Web":                      "Web",
    "web":                      "Web",
    "web, Android":             "Web",
    "web, Android, iOS":        "Web",
    "General":                  "General",
    "Cross-platform":           "General",
    "React Native, Flutter, ArkUI": "General",
    "Desktop":                  "Desktop",
    "desktop":                  "Desktop",
    "Game":                     "Game",
    "PC games":                 "Game",
    "Scratch":                  "Game",
    "AR mobile apps":           "Other",
}

plat_normalized = [
    PLAT_MAP.get(p, "Other")
    for p in raw["platform"]
    if is_valid_platform(p)
]

# ── Normalize: Venue ─────────────────────────────────────────────────────────
VENUE_MAP = {
    "PACM SE":                          "ESEC/FSE",
    "ACM Trans. Softw. Eng. Methodol.": "TOSEM",
    "ACM International Conference Proceeding Series": "Other",
    "ICSE-Companion 2022":              "ICSE",
}

venue_normalized = [
    VENUE_MAP.get(v, v) if v else ""
    for v in raw["venue"]
]

# ── Visual artifact ──────────────────────────────────────────────────────────
VA_MAP = {
    "Full-interface":        "App screenshot (full UI)",
    "mobile app screenshot": "App screenshot (full UI)",
    "GUI screenshot":        "App screenshot (full UI)",
    "Natural image":         "Natural image",
    "Component":             "UI component / widget",
    "mobile app icon":       "UI component / widget",
    "webpage screenshot":    "Web page screenshot",
    "mobile app screen recording": "Screen recording / video",
    "Document":              "Document image",
    "game screenshot":       "Game screenshot",
}

va_normalized = [VA_MAP.get(a, "Other") for a in raw["visual_artifact"] if a]

# ── Helper ───────────────────────────────────────────────────────────────────
def save(fig, name):
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, bbox_inches="tight", dpi=180)
    plt.close(fig)
    print(f"Saved: {path}")

def hbar(data_dict, xlabel, filename, min_show=2):
    """Sorted horizontal bar chart."""
    pairs = sorted(
        [(v, k) for k, v in data_dict.items() if v >= min_show],
        reverse=True
    )
    counts, labels = zip(*pairs)

    fig, ax = plt.subplots(figsize=(6.5, max(3, len(labels) * 0.45)))
    colors = [BLUE if c == max(counts) else
              "#4299E1" if c >= np.percentile(counts, 60) else GRAY
              for c in counts]
    bars = ax.barh(range(len(labels)), counts, color=colors, height=0.55)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=9)
    ax.invert_yaxis()
    ax.set_xlabel(xlabel, fontsize=10)
    ax.spines["left"].set_color("#CBD5E0")
    ax.spines["bottom"].set_color("#CBD5E0")
    for bar, val in zip(bars, counts):
        ax.text(bar.get_width() + 0.3,
                bar.get_y() + bar.get_height() / 2,
                str(val), va="center", fontsize=8.5, color="#2D3748")
    ax.set_xlim(0, max(counts) + 8)
    fig.tight_layout()
    save(fig, filename)

# ── FIG 1 — Papers per year ──────────────────────────────────────────────────
year_counts = Counter(y for y in raw["year"] if y)
years  = sorted(year_counts.keys())
counts = [year_counts[y] for y in years]

fig, ax = plt.subplots(figsize=(6, 3.5))
bars = ax.bar(years, counts, color=BLUE, width=0.55, zorder=2)

# Quadratic trend line (exclude partial year 2026)
x_idx = np.arange(len(years))
coeffs = np.polyfit(x_idx[:-1], counts[:-1], 2)
trend  = np.poly1d(coeffs)
x_fine = np.linspace(0, len(years) - 1.1, 300)
ax.plot(x_fine, trend(x_fine), color=GRAY, linewidth=1.4,
        linestyle="--", alpha=0.8, zorder=3)

for bar, val in zip(bars, counts):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            str(val), ha="center", va="bottom", fontsize=8.5, color="#2D3748")

ax.set_xlabel("Publication year", fontsize=10)
ax.set_ylabel("Number of papers", fontsize=10)
ax.set_ylim(0, max(counts) + 8)
ax.spines["left"].set_color("#CBD5E0")
ax.spines["bottom"].set_color("#CBD5E0")
fig.tight_layout()
save(fig, "fig1_papers_per_year.pdf")

# ── FIG 2 — Venue distribution ───────────────────────────────────────────────
venue_counts = Counter(v for v in venue_normalized if v)
# Keep top 12 + merge rest into Other
top_n = 12
pairs = venue_counts.most_common()
top_pairs  = pairs[:top_n]
other_sum  = sum(c for _, c in pairs[top_n:])
venue_dict = dict(top_pairs)
if other_sum:
    venue_dict["Other"] = venue_dict.get("Other", 0) + other_sum

hbar(venue_dict, "Number of papers", "fig2_venue_distribution.pdf")

# ── FIG 3 — SE Area distribution ─────────────────────────────────────────────
se_counts = Counter(se_normalized)
hbar(dict(se_counts), "Number of papers", "fig3_se_area_distribution.pdf")

# ── FIG 4 — Platform distribution ────────────────────────────────────────────
plat_counts = Counter(plat_normalized)
hbar(dict(plat_counts), "Number of papers", "fig4_platform_distribution.pdf")

# ── FIG 5 — Visual artifact distribution ─────────────────────────────────────
va_counts = Counter(va_normalized)
hbar(dict(va_counts), "Number of papers", "fig5_visual_artifact.pdf")

# ── Summary ──────────────────────────────────────────────────────────────────
print(f"\nTotal papers processed: {len(files)}")
print(f"SE area coverage: {sum(1 for a in raw['se_area'] if a)}/{len(files)}")
print(f"Platform coverage: {sum(1 for p in raw['platform'] if is_valid_platform(p))}/{len(files)}")
print(f"Venue coverage: {sum(1 for v in raw['venue'] if v)}/{len(files)}")
