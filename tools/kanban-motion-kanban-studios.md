# Kanban Motion (Kanban Studios)

- **Type:** plugin
- **Category:** generating videos
- **Official URL:** https://github.com/4waiz/kanban-motion
- **GitHub repo:** https://github.com/4waiz/kanban-motion @ 443d5db (MIT code; studio marks and example projects excluded)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-25)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-25

## Safety reason

Not code-reviewed for safety. README: /plugin install kanban-motion@kanban-motion then npm install --prefix ~/.claude/skills/kanban-motion/scripts; needs Node 18+, ffmpeg with libx264 and uv, which installs the Python audio tools on first use. LICENSE is MIT; the Kanban Studios name/logo and the example projects in examples/ are not covered. Bundled sound effects CC0. Repo, license and latest commit confirmed from github.com metadata, 2026-11-25.

## Safe install

Unreviewed: contain it: clone at the pinned commit 443d5db inside a devcontainer or sandbox, npm install there, no API keys (it needs none), network on only for npm and the first uv download; do not reuse anything from examples/. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: /plugin install kanban-motion@kanban-motion, then npm install --prefix ~/.claude/skills/kanban-motion/scripts (README).
