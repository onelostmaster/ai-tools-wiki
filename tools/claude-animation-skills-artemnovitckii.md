# claude-animation-skills (artemnovitckii)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://novitckii.com/resources/animation-skills/
- **GitHub repo:** https://github.com/artemnovitckii/claude-animation-skills @ 5dbea55 (MIT, LICENSE)
- **Price:** Free, MIT (LICENSE in repo, checked 2026-11-03); optional ElevenLabs voice is paid per use
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read @5dbea55, 2026-11-03; Claude re-checked SKILL.md and render.mjs 2026-11-03 20:12): caution. Code clean: no telemetry, hooks, eval or prompt-injection text found; `install.sh:8-16` only symlinks the skills into ~/.claude/skills. But `setup.sh:16-44` downloads via npm/npx/curl (about 1 GB with --voice; GSAP with no hash check; hyperframes@0.8.34 pinned, `anim.py:19`), and while rendering `render.mjs:12-15` runs a file server that listens on all interfaces with no ../ path check, so render only on a trusted home network or bind it to 127.0.0.1.

## Safe install

Safe install (fixes applied):
Windows (inside WSL2; the README supports macOS/Linux only): git clone the repo, git checkout 5dbea55. Before any render, change the file server in render.mjs (lines 12-15) to listen on 127.0.0.1; otherwise it listens on all interfaces with no ../ path check. Run ./install.sh (lines 8-16 only symlink the skills into ~/.claude/skills inside WSL2), then ./setup.sh without --voice (setup.sh lines 16-44 download via npm/npx/curl; --voice adds about 1 GB). Claude Code: use it from the WSL2 copy of Claude Code. If you add the paid ElevenLabs voice, put the key in an env var, never in chat. Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin and the 127.0.0.1 change.
Windows (WSL2): ./install.sh && ./setup.sh --voice; the render server listens on all interfaces with no ../ check.

## Install notes

Caution: read the Safety reason and ask the user before installing.
macOS/Linux only per README; on Windows use WSL2 (untested). Claude Code: run install.sh inside WSL2 (it links the skills into ~/.claude/skills). Before rendering, change the server in render.mjs to listen on 127.0.0.1. Optional ElevenLabs voice is paid; keep its key in env, never in chat. Android: no.
