# VoiceStudio

- **Type:** app
- **Category:** voice and audio
- **Official URL:** https://github.com/debpalash/VoiceStudio
- **GitHub repo:** [https://github.com/debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)
- **Price:** Free (AGPL)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code scan, da74a6f, a project a review, 2026-10-31): Use with caution. `curl|sh` installer; some engines load Hugging Face models with `trust_remote_code=True`, which runs model-repo code; PostHog analytics are opt-in; the server binds `127.0.0.1`; it ships a Claude skill plus an MCP at `localhost:3900/mcp`. About 6 months old, single developer.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
