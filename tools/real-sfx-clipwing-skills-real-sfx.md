# Real SFX (Clipwing skills/real-sfx)

- **Type:** skill
- **Category:** voice and audio, editing
- **Official URL:** https://github.com/Clipwing/skills
- **GitHub repo:** [https://github.com/Clipwing/skills](https://github.com/Clipwing/skills) (folder `skills/real-sfx`) @ edbefcb (cited in a project a review; scripts MIT per README, no LICENSE file)
- **Price:** Free (scripts MIT per its README, no LICENSE file; per a review). No vendor site found to confirm (web search, checked 2026-10-31).
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, edbefcb, 2026-10-31): Looks safe. No telemetry, no hooks; optional setup steps do unpinned installs (`npm install uisfx`; `pip install onnxruntime numpy` plus a YAMNet model from Hugging Face `main`, size-check only); a 3.1 GB model install needs `--yes` and is pinned; `listen_page.py serve --lan` exposes the page on your Wi-Fi (opt-in). Claude: no LICENSE file (scripts MIT per README) and unpinned installs.

## Safe install

Safe install (fixes applied):
Claude Code (Windows PowerShell): git clone https://github.com/Clipwing/skills.git clipwing-skills; cd clipwing-skills; git checkout edbefcb (the reviewed commit); Copy-Item -Recurse skills\\real-sfx "$HOME\.claude\\skills\", restart. Needs Python 3.9+ and FFmpeg (winget install Gyan.FFmpeg). Skip the optional unpinned setup steps (npm install uisfx; pip install onnxruntime numpy plus the YAMNet model from Hugging Face main) unless you need them, and do not run listen_page.py serve --lan (it opens the page to your Wi-Fi; a review bot code read).
Hermes: unconfirmed: copy the same pinned real-sfx folder into ~/.hermes/skills/.

## YOLO install

YOLO (your own risk): skips the commit pin and the optional-step limits.
Clone main and copy skills\\real-sfx as in the Install notes; run any optional setup the skill asks for.

## Install notes

Claude Code (Windows PowerShell): `git clone https://github.com/Clipwing/skills.git clipwing-skills` then `Copy-Item -Recurse clipwing-skills\skills\real-sfx "$HOME\.claude\skills\"`, restart; needs Python 3.9+ and FFmpeg (`winget install Gyan.FFmpeg`) .
Hermes: unconfirmed: copy the `real-sfx` skill folder into `~/.hermes/skills/` .
