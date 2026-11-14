# pixelfx

- **Type:** plugin
- **Category:** 3D and games, design
- **Official URL:** https://patch-gg.github.io/pixelfx/
- **GitHub repo:** https://github.com/patch-gg/pixelfx @ a841596 (MIT)
- **Price:** Free, open source (MIT; the Patch Pixel font is excluded) (github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (code read @a841596) and Claude (@a841596), 2026-11-01: Looks safe. Plain JS plus local Node tools; only dev dep esbuild, no postinstall, no network calls. Only exec is optional ffmpeg for GIF/MP4 via spawnSync, no shell (`tools/lib/fxlib.mjs:258`). Gallery server (`tools/serve.mjs`) blocks path traversal but listens on all interfaces: trusted networks only. Bundled Patch Pixel font is not MIT.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `/plugin marketplace add patch-gg/pixelfx` then `/plugin install pixelfx@pixelfx`, or copy `skills/pixelfx` into `~/.claude/skills/` (Windows: `%USERPROFILE%\.claude\skills\`) (README).
Library (any Node project): `npm i github:patch-gg/pixelfx` (README; unpinned, from GitHub).
Hermes: unconfirmed: copy `skills/pixelfx` into `~/.hermes/skills/` and start a new session.
