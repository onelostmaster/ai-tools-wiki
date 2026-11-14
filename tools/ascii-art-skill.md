# ASCII art skill

- **Type:** skill
- **Category:** generating videos, design
- **Official URL:** https://github.com/0xSero/ascii-art
- **GitHub repo:** [https://github.com/0xSero/ascii-art](https://github.com/0xSero/ascii-art)
- **Price:** Free (MIT)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a review, 0968699): Looks safe. No network code, telemetry, eval/exec, subprocess, hooks or install scripts; scripts only read and write local files; `grab_frames.py` drives a local headless Chromium on a `file://` page. `SKILL.md` tells the agent to save the MP4 to `~/Downloads` and open it.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: unconfirmed (the README has none): put the repo folder at `~/.claude/skills/ascii-art/`; needs `pip install numpy scipy pillow scikit-image playwright`, `python -m playwright install chromium` and ffmpeg
Hermes: put the folder at `~/.hermes/skills/creative/ascii-art/` (same dependencies)
