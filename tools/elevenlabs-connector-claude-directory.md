# ElevenLabs connector (Claude directory)

- **Type:** connector
- **Category:** voice and audio, generating videos, creative tools
- **Official URL:** https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp
- **GitHub repo:** unknown
- **Price:** Uses your ElevenLabs plan credits (one pool with the API): Free 10k credits/mo, Starter $6, Creator $22 (121k), Pro $99 (600k) per elevenlabs.io/pricing, checked 2026-11-11. Per use: about 190 credits per image, about 16,800 per 5 s video (estimates, 2026-11-11).
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-12

## Safety reason

ElevenLabs official hosted MCP in Claude's directory (vendor docs; hosted, no code to review). Caution, not unsafe code: (1) cost: one ElevenLabs credit pool shared with the API row; about 190 credits per image (default makes 4) and about 16,800 per 5 s video (the wiki estimate_only checks, 2026-11-11), so a few videos can empty a month's credits; (2) ElevenLabs' Prohibited Use Policy (updated 2026-10-09) covers images, video and music, counts attempts and allows account suspension, which would stop every project's ElevenLabs use, so never use it to retry refused prompts; (3) agent tools can publish and delete voice agents. OAuth with scoped access.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
claude.ai: already connected by the user (Settings, Connectors, 2026-11-11). To add elsewhere: claude.ai/customize/connectors, sign in with OAuth and grant only the permissions you need. House rule: ask the user before any video generation; images in small numbers are fine; never retry a refused prompt through it. Episode builds keep using the API from code.
