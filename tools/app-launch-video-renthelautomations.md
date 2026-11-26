# app-launch-video (renthelautomations)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/renthelautomations/app-launch-video
- **GitHub repo:** https://github.com/renthelautomations/app-launch-video @ 6d0776b (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-25); Remotion has its own company license
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-25

## Safety reason

Not code-reviewed for safety. README: copy app-launch-video/ into ~/.claude/skills/ (or a project's .claude/skills/, or zip and upload in claude.ai Settings → Capabilities → Skills); needs Node 18+ or Bun, ffmpeg/ffprobe, Chrome (Remotion fetches a headless shell), Python 3.10+ with numpy scipy pillow h5py, and potrace; downloaded assets keep their own licenses. Repo, license and latest commit confirmed from github.com metadata, 2026-11-25.

## Safe install

Unreviewed: contain it: copy the skill from the pinned commit 6d0776b, run its Remotion project inside a devcontainer or sandbox with Python packages in a venv, no API keys (it needs none), network on only for npm/pip and the headless shell download. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: copy the app-launch-video folder into ~/.claude/skills/. claude.ai: zip the folder and upload it in Settings → Capabilities → Skills (README).
