# papertalk (AmirMakir)

- **Type:** plugin
- **Category:** generating videos, voice and audio, research
- **Official URL:** https://github.com/AmirMakir/papertalk
- **GitHub repo:** https://github.com/AmirMakir/papertalk @ 036cfb6 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-26); Remotion license applies to rendering; ElevenLabs optional (price not checked)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-26

## Safety reason

Not code-reviewed for safety. README: /plugin install papertalk --marketplace AmirMakir/papertalk; setup asks for a voice and, only if you pick ElevenLabs, your ElevenLabs key; first run installs Remotion and the local voice (about 1 GB, Node 20+) and the plugin works in ~/papertalk; the plugin starts its MCP server (mcp/server.mjs). Remotion has its own license (free up to 3 people). Repo, license and latest commit confirmed from github.com metadata, 2026-11-26.

## Safe install

Unreviewed: contain it: clone at the pinned commit 036cfb6 and load it with claude --plugin-dir . inside a devcontainer or sandbox, pick the local Kokoro voice (no ElevenLabs key), leave marketplace auto-update off, network on only for the first ~1 GB engine download. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: /plugin install papertalk --marketplace AmirMakir/papertalk, choose the free local voice (README).
