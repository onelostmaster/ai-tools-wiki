# E2B

- **Type:** API
- **Category:** developer tools
- **Official URL:** https://e2b.dev
- **GitHub repo:** https://github.com/e2b-dev/E2B @ fd72526 (Apache-2.0 SDKs)
- **Price:** Hobby free with a one-time $100 credit; Pro $150/mo + about $0.17 per hour per default sandbox (e2b.dev, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @fd72526, a review, 2026-11-02): safe. No telemetry in the SDKs; code runs in E2B's cloud (third-party storage of what you send there). Needs an E2B API key.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `pip install e2b` or `npm i e2b` (README); API key as an env variable. Android: no.
