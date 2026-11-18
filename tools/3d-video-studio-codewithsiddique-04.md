# 3d-video-studio (codewithsiddique-04)

- **Type:** skill
- **Category:** generating videos, 3D and games, voice and audio
- **Official URL:** https://github.com/codewithsiddique-04/3d-video-studio
- **GitHub repo:** https://github.com/codewithsiddique-04/3d-video-studio @ f26f4d7 (no license)
- **Price:** Free on GitHub, but no license file: all rights reserved by default (github.com, checked 2026-11-17); voiceover needs a Cartesia account (README.md:24)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-17

## Safety reason

Not code-reviewed for safety. setup.sh at f26f4d7: runs npm install for engine and kit (setup.sh:21,24), installs Playwright Chromium (setup.sh:24), creates a Python venv and pip installs numpy, scipy, pillow, sherpa-onnx unpinned (setup.sh:28-31), and downloads a ~500 MB Parakeet model from the official k2-fsa/sherpa-onnx GitHub release (setup.sh:36). README.md:35-37 suggests letting Claude clone and run setup for you. No license file (github.com metadata), so reuse of its code is not permitted. A project Tool Scout (Claude, 2026-11-17) read it: 2.5/5, ideas only. Repo and commit confirmed from github.com metadata, 2026-11-17.

## Safe install

Unreviewed: contain it: read only for ideas (no license, so do not copy its code). If you test it, clone at pinned commit f26f4d7 into a throwaway devcontainer, not your real ~/.claude/skills, run setup.sh yourself rather than letting Claude run it, no Cartesia or other keys, network only for the setup downloads. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
README.md\:41-43\: git clone into ~/.claude/skills/3d-video-studio, then bash setup.sh (Git Bash on Windows). Not recommended: no license.
