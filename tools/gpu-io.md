# gpu-io

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/amandaghassaei/gpu-io
- **GitHub repo:** https://github.com/amandaghassaei/gpu-io
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted source read, not a full dependency/binary audit; amandaghassaei/gpu-io @14a6081. GPU particle/physics building blocks, not a ready-made physics studio. No telemetry/install hooks found; src/index.ts:64-87 exports GPU utilities. Latest commit January 2024: stale and GPU/browser compatibility needs testing. No fix: unmaintained since January 2024; contained by pinning 0.2.7 and running only in the browser.

## Safe install

Safe install (fixes applied):
Windows Claude Code or any web project: `npm install gpu-io@0.2.7` (README.md:37) inside the project, then build your page as usual; it runs in the browser sandbox. It has no install scripts or telemetry in the reviewed source (src/index.ts:64-87 exports only GPU utilities). unverified: WebGL2/GPU support on your target phone; test the page on the phone before relying on it. claude.ai artifacts: import it only if the artifact allows npm packages. Not a Hermes tool.

## YOLO install

YOLO (your own risk): skips the version pin.
npm install gpu-io

## Install notes

Not installed. Ask the user before any installation, including Try. Browser library for your own web pages; runs on Windows and Android browsers with WebGL; unverified: your phone's GPU support (test the page on it). No native Claude skill/MCP in this repo.
