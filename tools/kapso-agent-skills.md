# Kapso agent skills

- **Type:** skill
- **Category:** messaging, automation
- **Official URL:** https://kapso.ai
- **GitHub repo:** [https://github.com/gokapso/agent-skills](https://github.com/gokapso/agent-skills)
- **Price:** Kapso free plan: 2,000 WhatsApp messages/mo; paid tiers on its pricing page (`kapso.ai`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, 415c1b4, a review): Looks safe. Skill code only calls `api.kapso.ai` with your `KAPSO_API_KEY`; no telemetry, exec or hooks. Caveats: it can send real WhatsApp messages and make paid calls, the repo has no license, and deps and the installer are unpinned.

## Safe install

Safe install (fixes applied):
Claude Code: git clone https://github.com/gokapso/agent-skills, git checkout 415c1b4 (the reviewed commit, a review) and copy the skill folders into %USERPROFILE%\.claude\\skills instead of the unpinned npx installer. Put KAPSO_API_KEY in an env var, never in chat. It sends real WhatsApp messages and makes paid calls , so keep Claude's permission prompt on for its send commands. The repo has no license .

## YOLO install

YOLO (your own risk): skips the commit pin and folder copy.
npx skills add gokapso/agent-skills (unpinned installer, follows main).

## Install notes

Claude Code: `npx skills add gokapso/agent-skills` (as shown in the post; a review bot notes the installer is unpinned).
Claude Code: it needs a `KAPSO_API_KEY`; add it as a secret or env var, never paste keys into chat.
