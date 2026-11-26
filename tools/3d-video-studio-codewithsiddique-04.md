# 3d-video-studio (codewithsiddique-04)

- **Type:** skill
- **Category:** generating videos, 3D and games, voice and audio
- **Official URL:** https://github.com/codewithsiddique-04/3d-video-studio
- **GitHub repo:** https://github.com/codewithsiddique-04/3d-video-studio @ f26f4d7 (no license)
- **Price:** Free on GitHub, but no license file: all rights reserved by default (github.com, checked 2026-11-17); voiceover needs a Cartesia account (README.md:24)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-25

## Safety reason

a review bot read @f26f4d7: safe with these fixes. A Claude Code skill plus a local three.js engine rendered by Playwright Chromium and FFmpeg, with Python audio and QA tools. No hooks, MCP server, API keys, eval, pickle or shell=True; the only network calls are in setup.sh. The render server listens on 127.0.0.1 only (engine/film.mjs:43). Cartesia is used by hand: the skill writes a script you paste into Cartesia yourself (story/voice-cartesia.md:1-3), so no key is stored. Word timing runs locally with sherpa-onnx (kit/words.py:2, 34-39). Verified 1: SKILL.md:27 runs bash setup.sh by itself when three.js or the venv is missing, so Claude runs the installer on first use. Fix: run setup.sh yourself once before the first /3d-video-studio. Verified 2: setup.sh installs pinned three 0.187.0 and playwright 1.49.1 (engine/package.json, kit/package.json; engine has a lockfile, kit does not), runs npx --yes playwright install chromium (setup.sh:24), upgrades pip and installs numpy, scipy, pillow and sherpa-onnx unpinned (setup.sh:30-31), and curls a ~500 MB Parakeet model from the official k2-fsa/sherpa-onnx GitHub release with no checksum (setup.sh:36); unverified: that file's hash. Fix: before running setup.sh, change line 31 to pinned versions you choose, and run it inside a devcontainer or Windows Sandbox. Other: no LICENSE file, so its code is all rights reserved: use it for ideas, don't copy or publish its code (not a safety issue). README.md:33-37 suggests letting Claude clone and set it up; use the by-hand route instead.

## Safe install

Safe install (fixes applied):
Claude Code (Windows, Git Bash), inside a devcontainer or Windows Sandbox: git clone https://github.com/codewithsiddique-04/3d-video-studio ~/.claude/skills/3d-video-studio ; cd ~/.claude/skills/3d-video-studio ; git checkout f26f4d7f38cf2629072e5d93bf4a867d3b57fb75 ; edit setup.sh:31 to pin numpy, scipy, pillow and sherpa-onnx versions ; bash setup.sh yourself (needs Node 18+, FFmpeg, Python 3.9+; downloads Chromium and a ~500 MB model once). Then start /3d-video-studio. Make the Cartesia voice by hand as the skill asks; no keys needed. No license: ideas and personal use only, don't reuse its code.
claude.ai, Hermes, Android: not supported (needs local Node, Playwright, FFmpeg and Python).

## YOLO install

YOLO (your own risk): skips the pinned commit, the pinned pip versions and the sandbox. README.md\:39-43\: git clone into ~/.claude/skills/3d-video-studio and bash setup.sh, or let Claude install and run setup for you.

## Install notes

Safe with fixes: Claude Code skill that makes ~60 s vertical 3D cartoon Shorts (fake origin story of an invention) in code with three.js, Playwright and FFmpeg, local word timing, and a Cartesia voice you make by hand. Pin f26f4d7, pin setup.sh:31's pip packages, run setup.sh yourself in a sandbox. No license: ideas only; Decision Skip kept. Reference for the faceless video channel idea.
