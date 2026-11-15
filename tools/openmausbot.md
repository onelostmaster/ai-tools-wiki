# OpenMausBot

- **Type:** app
- **Category:** automation, developer tools
- **Official URL:** https://www.openmausbot.com/
- **GitHub repo:** https://github.com/milind-soni/OpenMausBot @ 6ae15f25 (v0.1.157, Apache-2.0)
- **Price:** Free, open source (Apache-2.0); uses your existing agent subscriptions; boat.dev cloud computers and Composio connections may cost extra (unknown) (github.com, checked 2026-11-01)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (spot-check @6e32504, ~6,400 files) and Claude (@6e32504), 2026-11-01: caution. Approval mode full runs Claude Code with bypassPermissions (default acceptEdits, `server/drivers/claude.ts:654, 1027`); computer control via bundled cua-driver; PostHog analytics on unless opted out; updates install on quit; apps via Composio, cloud computers via boat.dev; prepare sets git hooksPath. No malware signs.
Claude re-review @6ae15f25 (v0.1.157), 2026-11-14: still caution. PostHog analytics on unless switched off (src/lib/analytics.ts:21-30); hourly announcements feed from the repo's main branch; Windows installer unsigned; some keys stored plaintext (SECURITY.md); Full access = bypassPermissions (server/drivers/claude.md); about 1M lines of TypeScript, several releases a day, 1,056 open issues, so reviews go stale fast.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: no install steps given (the source withholds them until the tool is rated safe); see the official repo https://github.com/milind-soni/OpenMausBot.
