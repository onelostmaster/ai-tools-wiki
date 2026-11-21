# 2d-character-sketch (yenceesanjeev)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/yenceesanjeev/2d-character-sketch
- **GitHub repo:** https://github.com/yenceesanjeev/2d-character-sketch @ 46ef64e (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-13)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-20

## Safety reason

a review bot code read @46ef64e: safe with the fixes in Safe install. No package.json, so no npm packages and no install hooks; the renderer draws SVG in code and runs only rsvg-convert, ffmpeg, ffprobe, git, rhubarb, macOS say and the openvoice Python, each through spawn with an argument list and no shell (scripts/sketch.mjs:55-71). Network: only the paid voices: api.elevenlabs.io (sketch.mjs:444,549,1367) and api.sarvam.ai (sketch.mjs:558); a paid send stops unless --max-chars covers it (sketch.mjs:516) and sounds/music unless --max-credits covers it (sketch.mjs:1358-1365). No telemetry. Verified behaviour and fixes: (1) API keys are read from the environment, then .env.local, .env in the working folder, then ~/.2d-character-sketch/keys.env (sketch.mjs:396-412); a key file inside a git repo that git does not ignore is refused (sketch.mjs:405-407); fix: use the free voices, or put a low-limit ElevenLabs/Sarvam key only in a gitignored .env.local. (2) install-rhubarb.sh downloads Rhubarb 1.14.0 from the official GitHub release and checks size, but the Linux build has no SHA-256 recorded (scripts/install-rhubarb.sh:17,34) and the script exits on Windows (line 18); fix: download the release zip yourself and compare its SHA-256 with the digest on the GitHub release page before unzipping. (3) install-openvoice.sh (optional, about 2 GB) pins MeloTTS to commit 2091453 and torch 2.8.0 (lines 13,23,27) but upgrades boto3/botocore unpinned (line 29), resolves MeloTTS's own requirements at install time (line 28) and downloads NLTK data and the voice model (lines 37,40); the tool calls the venv's venv/bin/python (sketch.mjs:525), a Linux/macOS path, so on Windows openvoice works only inside WSL; fix: skip openvoice, or install it only in WSL. (4) It writes into the working folder and ~/.2d-character-sketch only, and deletes only its own temp/scratch files (sketch.mjs:526,567,571,1203-1220). No fix needed beyond these.

## Safe install

Safe install (fixes applied): Claude Code on Windows: run it inside WSL Ubuntu (its tool paths and install scripts are Linux/macOS only). In WSL: sudo apt install librsvg2-bin ffmpeg (the commands the tool itself prints, sketch.mjs:48-51) plus Node 20 or newer; git clone https://github.com/yenceesanjeev/2d-character-sketch ~/.claude/skills/2d-character-sketch && git -C ~/.claude/skills/2d-character-sketch checkout 46ef64e. Use the free voices (no keys). Lip sync: download Rhubarb-Lip-Sync-1.14.0-Linux.zip from https://github.com/DanielSWolf/rhubarb-lip-sync/releases, check its SHA-256 against the release page, unzip it into ~/.2d-character-sketch/rhubarb and set RHUBARB to the rhubarb file inside, instead of running install-rhubarb.sh. Skip install-openvoice.sh unless you want the 2 GB local voice. Paid voices only with a low-limit key in a gitignored .env.local, and only with --max-chars / --max-credits after reading the printed estimate. claude.ai: no (needs local Node, FFmpeg and rsvg-convert). Hermes: no. Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin, the manual Rhubarb checksum and the WSL-only openvoice rule. Copy the skill folder into %USERPROFILE%\.claude\\skills\\ (or ~/.claude/skills), then let Claude run bash scripts/install-rhubarb.sh and bash scripts/install-openvoice.sh when it asks (SKILL.md:35,149).

## Install notes

Ask the user before installing. Safe with the fixes in Safe install applied. Local Claude Code skill: draws simple 2D cartoon characters in SVG and renders short talking sketch videos with FFmpeg; free voices need no key, paid ElevenLabs/Sarvam voices are capped by --max-chars/--max-credits.
