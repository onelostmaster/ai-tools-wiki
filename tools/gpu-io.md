# gpu-io

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/amandaghassaei/gpu-io
- **GitHub repo:** https://github.com/amandaghassaei/gpu-io
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @14a6081 + npm gpu-io 0.2.7 (2026-11-19): safe with fixes. GPU utility exports only (src/index.ts:64-87); no network, eval or install scripts; npm 0.2.7 pulls four small dependencies (changedpi, file-saver, float16, type-checks). An old commit date is not a risk for browser-sandboxed GPU code. Fix: pin 0.2.7 with a lockfile and test on your target phone.

## Safe install

Safe install (fixes applied):
Windows Claude Code or any web project: npm install --save-exact --ignore-scripts gpu-io@0.2.7 (README.md:37) inside the project, then build your page as usual; it runs in the browser sandbox. It has no install scripts or telemetry in the reviewed source (src/index.ts:64-87 exports only GPU utilities). Test the page on your target phone (WebGL2) before relying on it. claude.ai artifacts: import it only if the artifact allows npm packages. Not a Hermes tool.

## YOLO install

YOLO (your own risk): skips the version pin.
npm install gpu-io

## Install notes

Not installed. Ask the user before any installation, including Try. Browser library for your own web pages; runs on Windows and Android browsers with WebGL; unverified: your phone's GPU support (test the page on it). No native Claude skill/MCP in this repo.
