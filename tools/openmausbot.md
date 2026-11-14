# OpenMausBot

- **Type:** app
- **Category:** automation, developer tools
- **Official URL:** https://www.openmausbot.com/
- **GitHub repo:** https://github.com/milind-soni/OpenMausBot @ 6e32504 (Apache-2.0)
- **Price:** Free, open source (Apache-2.0); uses your existing agent subscriptions; boat.dev cloud computers and Composio connections may cost extra (unknown) (github.com, checked 2026-11-01)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (spot-check @6e32504, ~6,400 files) and Claude (@6e32504), 2026-11-01: caution. Approval mode full runs Claude Code with bypassPermissions (default acceptEdits, `server/drivers/claude.ts:654, 1027`); computer control via bundled cua-driver; PostHog analytics on unless opted out; updates install on quit; apps via Composio, cloud computers via boat.dev; prepare sets git hooksPath. No malware signs.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: no install steps given (the source withholds them until the tool is rated safe); see the official repo https://github.com/milind-soni/OpenMausBot.
