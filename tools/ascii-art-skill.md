# ASCII art skill

- **Type:** skill
- **Category:** generating videos, design
- **Official URL:** https://github.com/0xSero/ascii-art
- **GitHub repo:** [https://github.com/0xSero/ascii-art](https://github.com/0xSero/ascii-art)
- **Price:** Free (MIT)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a review, 0968699): Looks safe. No network code, telemetry, eval/exec, subprocess, hooks or install scripts; scripts only read and write local files; `grab_frames.py` drives a local headless Chromium on a `file://` page. `SKILL.md` tells the agent to save the MP4 to `~/Downloads` and open it.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): copy the repo folder to %USERPROFILE%\.claude\\skills\\ascii-art\\ (README has no command). Install its Python deps in a venv: python -m venv ascii-env, then pip install numpy scipy pillow scikit-image playwright and python -m playwright install chromium; ffmpeg on the PATH. No network code . SKILL.md has the agent save the MP4 to Downloads and open it (that is how it works). Hermes: same folder under ~/.hermes/skills/creative/ascii-art/.

## YOLO install

Not written yet.

## Install notes

Claude Code: unconfirmed (the README has none): put the repo folder at `~/.claude/skills/ascii-art/`; needs `pip install numpy scipy pillow scikit-image playwright`, `python -m playwright install chromium` and ffmpeg
Hermes: put the folder at `~/.hermes/skills/creative/ascii-art/` (same dependencies)
