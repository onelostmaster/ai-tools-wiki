# Kapso agent skills

- **Type:** skill
- **Category:** messaging, automation
- **Official URL:** https://kapso.ai
- **GitHub repo:** [https://github.com/gokapso/agent-skills](https://github.com/gokapso/agent-skills)
- **Price:** Kapso free plan: 2,000 WhatsApp messages/mo; paid tiers on its pricing page (`kapso.ai`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, 415c1b4, a review): Looks safe. Skill code only calls `api.kapso.ai` with your `KAPSO_API_KEY`; no telemetry, exec or hooks. Caveats: it can send real WhatsApp messages and make paid calls, the repo has no license, and deps and the installer are unpinned.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `npx skills add gokapso/agent-skills` (as shown in the post; a review bot notes the installer is unpinned).
Claude Code: it needs a `KAPSO_API_KEY`; add it as a secret or env var, never paste keys into chat.
