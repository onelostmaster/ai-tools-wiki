# Duix Avatar

- **Type:** app
- **Category:** generating videos
- **Official URL:** https://www.duix.com/
- **GitHub repo:** https://github.com/duixcom/Duix-Avatar @ 1328feb (custom DUIX licence)
- **Price:** Free under a custom licence with a 1,000-MAU cap (github.com, checked 2026-11-01)
- **Decision:** Avoid
- **Safety verdict:** avoid
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude fix-mode re-review (2026-11-14): avoid. No fix: the engine is prebuilt guiji2025 Docker images (code not in the repo) that docker-compose.yml:41-45 runs privileged, and a privileged container has full access to the host. Without the engine source there is nothing to read before dropping that.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not offered.

## Install notes

Do not install: flagged avoid (see Safety reason).
