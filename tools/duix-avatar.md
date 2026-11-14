# Duix Avatar

- **Type:** app
- **Category:** generating videos
- **Official URL:** https://www.duix.com/
- **GitHub repo:** https://github.com/duixcom/Duix-Avatar @ 1328feb (custom DUIX licence)
- **Price:** Free under a custom licence with a 1,000-MAU cap (github.com, checked 2026-11-01)
- **Decision:** Avoid
- **Safety verdict:** avoid
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

Claude : avoid. Rests on code lines already logged by a review bot (@1328feb, 2026-11-01): the real engine is prebuilt guiji2025 Docker images run privileged (`docker-compose.yml:41-45`), engine code not in the repo; custom licence with a 1,000-MAU cap (section 2) and reuse of your case studies (section 5c); face and voice cloning.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not offered.

## Install notes

Do not install: flagged avoid (see Safety reason).
