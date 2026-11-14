# claude-animation-skills (artemnovitckii)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://novitckii.com/resources/animation-skills/
- **GitHub repo:** https://github.com/artemnovitckii/claude-animation-skills @ 5dbea55 (MIT, LICENSE)
- **Price:** Free, MIT (LICENSE in repo, checked 2026-11-03); optional ElevenLabs voice is paid per use
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @5dbea55, 2026-11-03; Claude re-checked SKILL.md and render.mjs 2026-11-03 20:12): caution. Code clean: no telemetry, hooks, eval or prompt-injection text found; `install.sh:8-16` only symlinks the skills into ~/.claude/skills. But `setup.sh:16-44` downloads via npm/npx/curl (about 1 GB with --voice; GSAP with no hash check; hyperframes@0.8.34 pinned, `anim.py:19`), and while rendering `render.mjs:12-15` runs a file server that listens on all interfaces with no ../ path check, so render only on a trusted home network or bind it to 127.0.0.1.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
macOS/Linux only per README; on Windows use WSL2 (untested). Claude Code: run install.sh inside WSL2 (it links the skills into ~/.claude/skills). Before rendering, change the server in render.mjs to listen on 127.0.0.1. Optional ElevenLabs voice is paid; keep its key in env, never in chat. Android: no.
