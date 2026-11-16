# E2B

- **Type:** API
- **Category:** developer tools
- **Official URL:** https://e2b.dev
- **GitHub repo:** https://github.com/e2b-dev/E2B @ fd72526 (Apache-2.0 SDKs)
- **Price:** Hobby free with a one-time $100 credit; Pro $150/mo + about $0.17 per hour per default sandbox (e2b.dev, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (light code read @fd72526, a review, 2026-11-02): safe. No telemetry in the SDKs; code runs in E2B's cloud (third-party storage of what you send there). Needs an E2B API key.

## Safe install

Safe install (fixes applied):
Windows (Python): in a venv pip install e2b==2.62.0 (the Python SDK version at the reviewed fd72526, packages/python-sdk/pyproject.toml:3), or Node npm i e2b@2.62.1 (packages/js-sdk/package.json:3); neither has an install script. Put the E2B API key in the E2B_API_KEY environment variable for that session only, never in a file you share or commit. Code and files you send run and stay in E2B's cloud sandboxes: send no secrets, personal files or other API keys into a sandbox. Stay on the Hobby plan (one-time $100 credit) and watch the credit in the E2B dashboard. claude.ai, Hermes, Android: no direct install.

## YOLO install

YOLO (your own risk): skips the version pin (gets 2.64.0 from 2026-11-13, unreviewed) and the venv.
pip install e2b

## Install notes

Safe, but ask the user before installing.
Windows: `pip install e2b` or `npm i e2b` (README); API key as an env variable. Android: no.
