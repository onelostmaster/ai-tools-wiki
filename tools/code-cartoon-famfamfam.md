# code-cartoon (famfamfam)

- **Type:** plugin
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/famfamfam/code-cartoon
- **GitHub repo:** https://github.com/famfamfam/code-cartoon @ 76ab9f7 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-24); fal.ai is a separate paid service (price not checked)
- **Decision:** Later
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-24

## Safety reason

Not code-reviewed for safety. README (v1.4.0): needs Node.js 22+, FFmpeg, Python 3.9+ with numpy, scipy and pillow; optional piper-tts for local narration, optional paid fal.ai key or any OpenAI-compatible key for pictures and video; downloads dependencies, headless Chrome and Piper voices on first use; tested on Windows 11 with Git Bash. Bundled three.js, GSAP, fonts and a sample photo keep their own licenses. Repo, license and latest commit confirmed from github.com metadata, 2026-11-24.

## Safe install

Unreviewed: contain it: clone at the pinned commit 76ab9f7 inside a devcontainer or Windows Sandbox, install Python packages in a venv there, no fal.ai or OpenAI keys (local Piper narration needs none), network on only for the first dependency, Chrome and voice downloads. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code on Windows (README, use Git Bash): claude plugin marketplace add famfamfam/code-cartoon then claude plugin install code-cartoon@famfamfam; or git clone and copy skills/code-cartoon to ~/.claude/skills/. Check with skills/code-cartoon/scripts/cartoon doctor.
