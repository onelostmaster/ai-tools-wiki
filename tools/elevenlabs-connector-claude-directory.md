# ElevenLabs connector (Claude directory)

- **Type:** connector
- **Category:** voice and audio, generating videos, creative tools
- **Official URL:** https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp
- **GitHub repo:** unknown
- **Price:** Uses your ElevenLabs plan credits (one pool with the API): Free 10k credits/mo, Starter $6, Creator $22 (121k), Pro $99 (600k) per elevenlabs.io/pricing, checked 2026-11-11. Per use: about 190 credits per image, about 16,800 per 5 s video (estimates, 2026-11-11).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Claude fix-mode re-review (2026-11-14): safe with fixes. Official hosted MCP, OAuth. Costs share one credit pool with the API (about 190 credits per image, 16,800 per 5 s video, checked 2026-11-11): ask the user before any video. ElevenLabs' Prohibited Use Policy counts refused attempts: never retry a refused prompt. Agent tools can publish and delete voice agents: grant only needed scopes.

## Safe install

Safe install (fixes applied):
Already connected. House rules: ask before any video; images in small numbers; never retry a refused prompt; grant only the OAuth scopes you need. Episode builds use the API from code.

## YOLO install

YOLO (your own risk): skips the ask-before-video rule and scope limits.
Connect with every permission and generate freely.

## Install notes

Ask the user before installing.
claude.ai: already connected by the user (Settings, Connectors, 2026-11-11). To add elsewhere: claude.ai/customize/connectors, sign in with OAuth and grant only the permissions you need. House rule: ask the user before any video generation; images in small numbers are fine; never retry a refused prompt through it. Episode builds keep using the API from code.
