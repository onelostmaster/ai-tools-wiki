# claude-animation-skills (artemnovitckii)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://novitckii.com/resources/animation-skills/
- **GitHub repo:** https://github.com/artemnovitckii/claude-animation-skills @ 5dbea55 (MIT, LICENSE)
- **Price:** Free, MIT (LICENSE in repo, checked 2026-11-03); optional ElevenLabs voice is paid per use
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-20

## Safety reason

Claude code read @5dbea55 (2026-11-20): safe with fixes. GSAP is fetched from cdnjs without a hash only if kit/vendor/gsap.min.js is missing (kit/setup.sh:21-24), so placing a copy from npm gsap@3.12.5 (sha512-checked) first skips it. The render file server listens on all interfaces (skills/zach-d-films/engine/render.mjs:15); .listen(0, '127.0.0.1') keeps it local. npm deps are lockfile-pinned (kit/package-lock.json).

## Safe install

Safe install (fixes applied):
Windows (inside WSL2; README covers macOS/Linux): git clone the repo, git checkout 5dbea55. Edit skills/zach-d-films/engine/render.mjs line 15 from .listen(0) to .listen(0, '127.0.0.1') (it serves files with no ../ check). Get GSAP with its npm integrity check before setup: npm pack gsap@3.12.5, unpack, copy package/dist/gsap.min.js to kit/vendor/gsap.min.js; setup.sh then skips the unhashed cdnjs download (kit/setup.sh:21-24). Run ./install.sh (only symlinks the skills into ~/.claude/skills inside WSL2), then bash kit/setup.sh without --voice (--voice adds about 1 GB of models from GitHub releases, setup.sh:29-44). Use it from the WSL2 copy of Claude Code. A paid ElevenLabs key goes in an env var, never in chat. Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin and the 127.0.0.1 change.
Windows (WSL2): ./install.sh && ./setup.sh --voice; the render server listens on all interfaces with no ../ check.

## Install notes

Ask the user before installing.
macOS/Linux only per README; on Windows use WSL2 (untested). Claude Code: run install.sh inside WSL2 (it links the skills into ~/.claude/skills). Before rendering, change the server in render.mjs to listen on 127.0.0.1. Optional ElevenLabs voice is paid; keep its key in env, never in chat. Android: no.
