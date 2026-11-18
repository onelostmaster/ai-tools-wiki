# manim-skill

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/Yusuke710/manim-skill
- **GitHub repo:** [https://github.com/Yusuke710/manim-skill](https://github.com/Yusuke710/manim-skill)
- **Price:** Free (local Kokoro voice, no API key)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a project a review, 2026-10-29): Looks safe. About 800 lines; the local viewer binds 127.0.0.1 with fixed routes; no telemetry; the Kokoro voice model downloads from Hugging Face on first use.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): git clone https://github.com/Yusuke710/manim-skill, then git checkout the commit you reviewed so later pushes do not arrive unreviewed; install the README's Python packages inside a venv (README:15-22). The viewer binds 127.0.0.1 only and the Kokoro voice model downloads once from Hugging Face on first use ; no keys needed.

## YOLO install

YOLO (your own risk): skips the commit pin and venv.
git clone https://github.com/Yusuke710/manim-skill and install the README packages globally (README:15-22).

## Install notes

Claude Code: `git clone https://github.com/Yusuke710/manim-skill`, then install the README's system libraries and Python packages (README:15-22).
