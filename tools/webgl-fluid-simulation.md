# WebGL Fluid Simulation

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/PavelDoGreat/WebGL-Fluid-Simulation
- **GitHub repo:** https://github.com/PavelDoGreat/WebGL-Fluid-Simulation
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted source read, not a full dependency/binary audit; PavelDoGreat/WebGL-Fluid-Simulation @a2d2929. Interactive fluid effect demo, not an export pipeline. No telemetry/install hooks found; script.js:45-51 links separate mobile apps, not required for browser demo. Latest commit November 2024: stale. Mobile app is a separate product, not vetted. No fix: unmaintained since November 2024; contained by running it only in the browser sandbox.

## Safe install

Safe install (fixes applied):
Any browser (Windows or Android Chrome): open the official demo https://paveldogreat.github.io/WebGL-Fluid-Simulation/ (README.md:3); nothing to install. To use it in your own page, copy index.html/script.js from the official repo pinned at a2d2929. Ignore the app-store links in the demo (script.js:45-51): those apps are a separate, unvetted product. unverified: how smoothly it runs on your phone; open the demo page on the phone to check.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Runs in any browser with WebGL, including Android Chrome; unverified: performance on your phone (open the demo to check). No native Claude skill/MCP in this repo.
