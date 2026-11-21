# coolray-video-qc (ShakeJ)

- **Type:** skill
- **Category:** editing, generating videos
- **Official URL:** https://github.com/ShakeJ/coolray-video-qc
- **GitHub repo:** https://github.com/ShakeJ/coolray-video-qc @ 4ecab08 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-15)
- **Decision:** Later
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-20

## Safety reason

a review bot code read @4ecab08: safe with the fixes in Safe install. Python standard library only, no dependencies, no API keys, no telemetry and no network code (imports at scripts/media_audit.py:3-12 and scripts/captions.py:3-12). The only programs it starts are your own ffmpeg and ffprobe, without a shell and with input limited to local files (protocol_whitelist file,pipe, scripts/media_audit.py:39,154,211,278). It never edits or deletes your videos or captions: the video audit refuses an output folder that already exists (scripts/media_audit.py:276) and the caption report refuses to overwrite a file (scripts/captions.py:203). The skill is instructions only, no hooks (SKILL.md). Verified behaviour and fixes: (1) the commands are written as python3 (SKILL.md:17,30; README.md:73,79); on Windows python3 can open the Microsoft Store alias instead of your Python (Python docs, Using Python on Windows); fix: run the same commands with py. (2) The contact sheet uses FFmpeg glob input (scripts/media_audit.py:222), which needs an FFmpeg build with glob support (README.md:24); without it the run records only a contact_sheet_failed warning and the single frames are still written (scripts/media_audit.py:226); fix: open the frames folder instead, or run it in WSL. (3) Reports contain the full local paths of your files (SKILL.md:37); fix: don't share report.json publicly. Unverified: Windows behaviour beyond the two points above (the author tests macOS and Linux CI only, README.md:24); containment: first run on copies of a video in a test folder.

## Safe install

Safe install (fixes applied): Claude Code on Windows: winget install Python.Python.3.12 and winget install Gyan.FFmpeg (or any ffmpeg/ffprobe on PATH; the scripts never install anything). Download the v0.1.0 release ZIP from https://github.com/ShakeJ/coolray-video-qc/releases/tag/v0.1.0 (tag v0.1.0 = reviewed commit 4ecab08), extract it, keep the folder named coolray-video-qc and copy it to %USERPROFILE%\.claude\\skills\\coolray-video-qc. Run it with py instead of python3, e.g. py scripts\\media_audit.py video.mp4 --out qa\\video-v1 (a new folder each run) and py scripts\\captions.py captions.srt --duration 60 --profile latin --out qa\\captions.json; first run on copies in a test folder; if the contact sheet fails, open qa\\video-v1\\frames instead. Don't share report.json (it holds your local paths). Hermes: same ZIP, copy the folder into your Hermes skills folder. claude.ai: no (needs local Python and ffmpeg). Android: no.

## YOLO install

YOLO (your own risk): skips the pinned release, the test folder and the Windows python3/py fix. git clone https://github.com/ShakeJ/coolray-video-qc (moving main branch) and copy it to ~/.claude/skills/coolray-video-qc with the README one-liner (README.md:79).

## Install notes

Ask the user before installing. Safe with the fixes in Safe install applied. Checks finished videos and subtitles for decode errors, black/frozen/silent parts, loudness, caption timing and reading speed before upload; local only, no keys, never edits your files. Fits the faceless video channel QC step.
