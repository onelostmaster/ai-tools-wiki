# Vibe Kanban (BloopAI)

- **Type:** app
- **Category:** developer tools, automation
- **Official URL:** https://github.com/BloopAI/vibe-kanban
- **GitHub repo:** https://github.com/BloopAI/vibe-kanban @ 7c38070 (Apache-2.0; committed 2026-10-28; community-maintained since the company shut down)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); the paid cloud closed in May 2026
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (code read @7c38070, a review, 2026-11-02): caution. The company shut down on 2026-04-10 and the repo is community-maintained (README.md:19-22); analytics on by default (crates/services/src/services/config/versions/v8.rs:76,144), turn off in settings; Sentry crash reports when a DSN is built in (crates/utils/src/sentry.rs:26). No fix: the company shut down on 2026-04-10 and the repo is community-maintained (README.md:19-22), so there is no vendor security response; pinning the reviewed 7c38070 limits but does not remove this. Analytics and Sentry are fixed in Safe install. Caution stands for maintenance only.

## Safe install

Safe install (fixes applied):
Windows: npx vibe-kanban@<version built from the reviewed 7c38070> (Node needed) rather than the unpinned latest, since the repo is community-maintained after the company shut down (README.md:19-22). On first start open Settings and turn analytics off; it is on by default (crates/services/src/services/config/versions/v8.rs:76,144). Crash reports go to Sentry whenever the build has a DSN built in (crates/utils/src/sentry.rs:26); this cannot be switched off in settings, so if you want none, block sentry.io for it in your firewall. Android: no.

## YOLO install

YOLO (your own risk): skips the version pin, the analytics switch and the Sentry block.
Windows: npx vibe-kanban with default settings; analytics and Sentry crash reports stay on.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `npx vibe-kanban` (README), needs Node; turn analytics off in settings. Android: no.
