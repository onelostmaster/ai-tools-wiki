# OpenDuet

- **Type:** app
- **Category:** automation, Notion and productivity
- **Official URL:** https://copilotkit.ai/openduet
- **GitHub repo:** https://github.com/CopilotKit/OpenDuet (MIT)
- **Price:** Free, open source (MIT); needs a CopilotKit Intelligence account: free hosted tier 1,000 interactions a month, paid hosted from $49/month (copilotkit.ai, checked 2026-11-01), plus your own model key or Claude subscription.
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (code read @f52288f) and Claude (@f52288f), 2026-11-01: caution. Docker socket mounted into 2 services (`openbot/docker-compose.yml` l.181, 252; host-level control); agents get a shell; hosted CopilotKit account required, stores threads and memory; telemetry on, forced to 100% sampling; root postinstall runs bun install; setup uses unpinned `npx copilotkit@latest`.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: no install steps given (the source withholds them until the tool is rated safe); it runs as a self-hosted Docker app on the Claude Agent SDK, see the official repo https://github.com/CopilotKit/OpenDuet.
