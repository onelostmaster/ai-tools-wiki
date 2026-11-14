# motion-pack (ANVEAI)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/ANVEAI/motion-pack
- **GitHub repo:** https://github.com/ANVEAI/motion-pack @ 33f36b3 (MIT code, CC0 media per LICENSE-MEDIA; committed 2026-10-26 14:54 ET, still HEAD on 2026-11-09)
- **Price:** Free, MIT code + CC0 media (github.com, checked 2026-11-05)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-09

## Safety reason

a review bot (targeted code read @33f36b3, 2026-11-09, no-intake review): Safe. Plugin manifest (.claude-plugin) declares only skills; no hooks, no MCP config, no settings.json, no permission-skipping instructions in the six SKILL.md files; no eval, obfuscated or base64 code outside cloud/lyria.py decoding returned audio. Network, all opt-in or pinned: tools/pack_home.mjs downloads the pack release from github.com/ANVEAI/motion-pack and checks SHA-256 against SHA256SUMS and refuses tar paths with .. before unpacking (lines 37, 46-84); scripts/fetch-external.sh and terminal/fetch-cbirds.sh fetch third-party icon and terminal sets at pinned commits with SHA-256 from scripts/external.lock; tools/refstudy.py downloads a reference video with curl and X post metadata from the public fxtwitter API only when you pass it a URL (lines 63, 77-86); tools/lottie/validate.py fetches the Lottie schema; cloud/ (optional) uses your own Google Cloud login. Renders use npx -y hyperframes@0.8.142 (pinned); seekcheck may run npx puppeteer browsers install chrome. Not reviewed: all 583 code files line by line (grep-led read of network, process and install paths), the media and the hyperframes package.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @33f36b3 (safe, targeted read). Claude Code on Windows: /plugin marketplace add ANVEAI/motion-pack, then /plugin install motion-pack@anve (README lines 228-229). The skill's find-pack.sh is a shell script, so run Claude Code with Git Bash available; on first use it runs mp init, which downloads the v0.6.0 release tarball from GitHub into %USERPROFILE%\.motion-pack\\0.6.0 and refuses it unless the SHA-256 matches the release's SHA256SUMS. Needs Node 22+ (renders call npx -y hyperframes@0.8.142, pinned), ffmpeg on PATH (e.g. winget install Gyan.FFmpeg) and Python 3.11 in a venv for pip install -r requirements.txt (3.13+ cannot install the pins). Skip the optional cloud/ folder unless you want Google Cloud voice or music billed to your own project.
