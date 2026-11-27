# app-launch-video (renthelautomations)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/renthelautomations/app-launch-video
- **GitHub repo:** https://github.com/renthelautomations/app-launch-video @ 6d0776b (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-25); Remotion has its own company license
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-26

## Safety reason

a review bot read @6d0776b: safe with these fixes. A Claude Code skill that builds an app launch video as a Remotion project; it needs no API keys, the template code makes no web calls of its own, and every subprocess call passes a fixed argument list to ffmpeg, ffprobe or potrace (audio.py:209, :349; qa/_video.py:9, :34; trace_logo.py:32). Verified 1: SKILL.md:78 tells Claude to copy template/ and run bun install (or npm); package.json pins its five direct packages exactly (Remotion 4.0.546, React 19.3.1) but the repo ships no lockfile, so the rest of the dependency tree resolves to whatever is newest that day. Fix: run the install yourself, keep the package-lock.json it writes, and use npm ci from then on. Verified 2: fetch_kenney.sh:7-10 downloads three sound zips from opengameart.org and fetch_hrtf.sh:6 downloads kemar.sofa from sofacoustics.org, both over https with no checksum; they are audio data, not programs. Fix: run them once, note the sha256 of sfx/kenney and hrtf/kemar.sofa, and reuse those files. Verified 3: Film.jsx:5-10 loads the Inter font through @remotion/google-fonts, so renders fetch it from Google Fonts. Fix: none needed; to render offline, swap in a local font file. Verified 4: deliver.sh:13 and :17 delete only its own intermediate renders inside out/. The bash scripts (deliver.sh, fetch_*.sh) need WSL or Git Bash on Windows. Remotion's own license terms apply (see the Remotion row). MIT (LICENSE).

## Safe install

Safe install (fixes applied):
Claude Code (Windows): git clone https://github.com/renthelautomations/app-launch-video ; cd app-launch-video ; git checkout 6d0776b59aa7a10476907af9cfba7037f501017e ; copy the app-launch-video folder into %USERPROFILE%\.claude\\skills\\ . In each video project, run npm install yourself in the copied template, keep the package-lock.json and use npm ci after that; install ffmpeg, potrace and Node yourself; Python packages (numpy scipy pillow h5py) go in a venv. Run fetch_kenney.sh and fetch_hrtf.sh once (WSL or Git Bash), note the files' sha256 and reuse them.
claude.ai: zip the app-launch-video folder from the pinned commit and upload it in Settings → Capabilities → Skills (README:93); rendering needs a local Node, ffmpeg and Python, so use Claude Code for real renders.
Hermes, Android: not supported (local Remotion and ffmpeg pipeline).

## YOLO install

YOLO (your own risk): skips the pinned commit, the kept lockfile and the asset checksums. README: git clone https://github.com/renthelautomations/app-launch-video.git ; cp -R app-launch-video/app-launch-video ~/.claude/skills/ , then let Claude run bun install and the fetch scripts.

## Install notes

Safe with fixes: copy the skill from pinned commit 6d0776b; no API keys needed; run the template's npm install yourself and keep the lockfile (the repo has none); fetch the CC0 sounds and HRTF file once and keep their sha256; renders load Inter from Google Fonts. Bash scripts need WSL or Git Bash on Windows. Fits launch/promo videos; for the faceless channel it is a Remotion reference rather than a direct fit.
