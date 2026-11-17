# pixelfx

- **Type:** plugin
- **Category:** 3D and games, design
- **Official URL:** https://patch-gg.github.io/pixelfx/
- **GitHub repo:** https://github.com/patch-gg/pixelfx @ a841596 (MIT)
- **Price:** Free, open source (MIT; the Patch Pixel font is excluded) (github.com, checked 2026-11-01)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (code read @a841596) and Claude (@a841596), 2026-11-01: Looks safe. Plain JS plus local Node tools; only dev dep esbuild, no postinstall, no network calls. Only exec is optional ffmpeg for GIF/MP4 via spawnSync, no shell (`tools/lib/fxlib.mjs:258`). Gallery server (`tools/serve.mjs`) blocks path traversal but listens on all interfaces: trusted networks only. Bundled Patch Pixel font is not MIT.

## Safe install

Safe install (fixes applied):
Claude Code (Windows): copy skills/pixelfx from reviewed commit a841596 of github.com/patch-gg/pixelfx into %USERPROFILE%\.claude\\skills\\pixelfx and start a new session. Library: npm i github:patch-gg/pixelfx#a841596 (pinned to the reviewed commit). Fix: the gallery server tools/serve.mjs listens on all network interfaces (listen(PORT) with no host, tools/serve.mjs:29), so do not run it; view the gallery with python -m http.server 8080 --bind 127.0.0.1 from the repo folder instead. ffmpeg is needed only for GIF/MP4 export and is run without a shell (tools/lib/fxlib.mjs:258). The Patch Pixel font is not MIT: do not ship it in your own game.
Hermes: copy the same folder into ~/.hermes/skills/<category>/pixelfx/.

## YOLO install

YOLO (your own risk): skips the commit pin and the localhost-only gallery.
/plugin marketplace add patch-gg/pixelfx, then /plugin install pixelfx@pixelfx (README), and node tools/serve.mjs for the gallery (reachable from your whole network).

## Install notes

Claude Code: `/plugin marketplace add patch-gg/pixelfx` then `/plugin install pixelfx@pixelfx`, or copy `skills/pixelfx` into `~/.claude/skills/` (Windows: `%USERPROFILE%\.claude\skills\`) (README).
Library (any Node project): `npm i github:patch-gg/pixelfx` (README; unpinned, from GitHub).
Hermes: unconfirmed: copy `skills/pixelfx` into `~/.hermes/skills/` and start a new session.
