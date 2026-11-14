# Vibe Kanban (BloopAI)

- **Type:** app
- **Category:** developer tools, automation
- **Official URL:** https://github.com/BloopAI/vibe-kanban
- **GitHub repo:** https://github.com/BloopAI/vibe-kanban @ 7c38070 (Apache-2.0; committed 2026-10-28; community-maintained since the company shut down)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); the paid cloud closed in May 2026
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @7c38070, a review, 2026-11-02): caution. The company shut down on 2026-04-10 and the repo is community-maintained (`README.md:19-22`); analytics on by default (`crates/services/src/services/config/versions/v8.rs:76,144`), turn off in settings; Sentry crash reports when a DSN is built in (`crates/utils/src/sentry.rs:26`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `npx vibe-kanban` (README), needs Node; turn analytics off in settings. Android: no.
