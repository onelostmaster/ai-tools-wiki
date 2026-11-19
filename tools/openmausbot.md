# OpenMausBot

- **Type:** app
- **Category:** automation, developer tools
- **Official URL:** https://www.openmausbot.com/
- **GitHub repo:** https://github.com/milind-soni/OpenMausBot @ 6ae15f25 (v0.1.157, Apache-2.0)
- **Price:** Free, open source (Apache-2.0); uses your existing agent subscriptions; unverified: whether boat.dev cloud computers and Composio connections charge, and how much (unknown); containment: stay on local runs and your existing subscriptions (github.com, checked 2026-11-01)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @35d0442 v0.1.169 (2026-11-18): safe with fixes. Full access maps to bypassPermissions; default acceptEdits (server/drivers/claude.ts:630,989). PostHog is on until you opt out (src/lib/analytics.ts:21-30); updates download only on request (electron/updater.mjs:206). On a hosted or shared workspace a bot shell reaches Full-access threads (SECURITY.md:20-27). MCP env values stay plaintext (:31). Fix: local desktop, no Full access.

## Safe install

Safe install (fixes applied):
Windows desktop from the official GitHub releases; Settings → analytics off; never Full access or shared Full access; no hosted or shared workspace; no secrets in MCP env or headers; download updates by choice.

## YOLO install

YOLO (your own risk): skips analytics off and the Full-access ban.
Run it hosted with Full access on.

## Install notes

Ask the user before installing.
Windows: no install steps given (the source withholds them until the tool is rated safe); see the official repo https://github.com/milind-soni/OpenMausBot.
