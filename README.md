# Linear Transformations — Animated Teaching Video (M3 Internal Assessment)

**Presenter:** Ayush Sharma &nbsp;|&nbsp; **Student ID:** `E25B070912`

A ~5-minute (`04:59.6`, `1920x1080`, `30 fps`) Manim Community Edition animation teaching **Linear Transformations** in $\mathbb{R}^2$ through geometric grid deformations, basis vector tracking, step-by-step worked calculations, and determinant interpretation.

## Repository Contents

| File / Directory | Description |
|---|---|
| [`LT-animatedVideo.mp4`](LT-animatedVideo.mp4) | Final 1080p 16:9 MP4 animation with voice-over narration (`04:59.6`, `~20 MB`). |
| [`_Code/`](_Code/) | Complete modular Manim Python source code (`config.py`, `helpers.py`, `scene1_hook.py` – `scene6_summary.py`, `build_video.py`). |
| [`Storyboard.pdf`](Storyboard.pdf) | Official 6-scene storyboard PDF + mathematical verification summary. |
| [`Storyboard.md`](Storyboard.md) | Markdown source for the storyboard. |

---

## Reproducing the Full Render

Prerequisites: Python 3.12, `manim==0.22.1`, `ffmpeg`, and LaTeX + `dvisvgm` (e.g., TinyTeX).

```bash
source .venv/bin/activate
python _Code/build_video.py --quality 1080p
```

## References & Disclosures

- **Mathematical Inspiration:** 3Blue1Brown (*Essence of Linear Algebra*) & Gilbert Strang (*Introduction to Linear Algebra*).
- **Animation Tool:** Manim Community Edition v0.22.1.
- **AI Tool Disclosure:** Antigravity AI assisted with Manim Python code generation, layout scripting, and storyboard drafting. All mathematical formulas, numerical derivations, and geometric checks were independently verified.
