# Remotion Motion Graphics Skills

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/Liamrjohnston/remotion-motion-graphics-skill
- **GitHub repo:** https://github.com/Liamrjohnston/remotion-motion-graphics-skill @ b860c79 (MIT LICENSE file; committed 2026-07-23 20:01 ET, still HEAD on 2026-11-09)
- **Price:** Free (MIT, `github.com`, checked 2026-10-31); Remotion licensing applies (see the Remotion row).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @b860c79, 2026-11-09, no-intake review): Safe. Four markdown skills (motion-graphics, cinematic-camera, terminal-inserts, article-highlights) plus reference media, bundled logos and one script; no hooks, no MCP config, no settings.json, nothing asks for keys. The only code is skills/motion-graphics/scripts/promptible-gate.mjs (45 lines): it imports only node:fs, path, crypto and url (lines 2-5), makes no network calls and runs no other programs; it validates https source URLs as text (line 31), checks bundled reference videos by SHA-256 (lines 11-17, 29) and writes JSON only under the project's .promptible folder (lines 26-27). SKILL.md tells the agent to run that gate, ffmpeg/ffprobe for a contact sheet (lines 136-143) and to read 1 to 3 official pages for logos and UI (lines 35-43), with no permission-skipping instructions. Caution on install only: install.sh (curl | bash in the README) runs unpinned npx create-video@latest and npx -y skills add for this repo and remotion-dev/skills (lines 41-48). Not reviewed: the media files and the remotion-dev/skills companion.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): skip the curl | bash one-liner (install.sh runs unpinned npx create-video@latest and npx -y skills add, lines 41-48). Make a Remotion project yourself (npx create-video@latest, Node needed), download the repo at reviewed commit b860c79 (github.com/Liamrjohnston/remotion-motion-graphics-skill/archive/b860c79.zip) and copy the four folders under skills/ into that project's .claude\\skills folder; add the official Remotion skill from remotion-dev/skills the same way (not reviewed). Stage 5 needs ffmpeg/ffprobe on PATH (winget install Gyan.FFmpeg). The skills make the agent read 1 to 3 official web pages for logos and screenshots and cache them under .promptible in the project. Remotion licensing applies (see the Remotion row).

## YOLO install

YOLO (your own risk): skips the commit pin and the manual copy.
Run the README one-liner curl ... install.sh | bash in Git Bash or WSL (bash script), which installs both skill sets at HEAD with npx -y.

## Install notes

Code-reviewed by a review bot @b860c79 (safe). Claude Code on Windows: skip the curl | bash one-liner (it is a bash script and runs unpinned npx create-video@latest and npx skills add). Instead make a Remotion project yourself (npx create-video@latest, Node needed), download the repo at commit b860c79 and copy the four folders under skills/ into that project's .claude\\skills folder; add the official Remotion skill from remotion-dev/skills the same way. The motion-graphics gate script needs only Node; Stage 5 also needs ffmpeg/ffprobe on PATH (e.g. winget install Gyan.FFmpeg). The skills make the agent read 1 to 3 official web pages for logos and product screenshots and cache them under .promptible in the project. Remotion licensing applies (see the Remotion row).
