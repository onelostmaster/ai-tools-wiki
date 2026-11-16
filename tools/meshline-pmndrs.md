# MeshLine (pmndrs)

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/pmndrs/meshline
- **GitHub repo:** https://github.com/pmndrs/meshline
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted source read, not a full dependency/binary audit; pmndrs/meshline @4df8778. Stylized 3D lines/trails. No telemetry/network/install hooks found; src/index.ts:1-2 exports geometry/material. Latest repo commit June 2024: stale, check compatibility with your three.js version before use. No fix: unmaintained since June 2024; contained by pinning 3.3.1 and running only in the browser.

## Safe install

Safe install (fixes applied):
Windows Claude Code or any three.js web project: `npm install meshline@3.3.1` (README.md:17; 3.3.1 is the current npm release, no install scripts) inside the project, alongside three >=0.137 (its peer dependency). It runs in the browser sandbox with no network calls (src/index.ts:1-2 exports only geometry/material). unverified: compatibility with your three.js version (last commit June 2024); test the page before relying on it. Not a claude.ai or Hermes tool.

## YOLO install

YOLO (your own risk): skips the version pin.
npm install meshline

## Install notes

Not installed. Ask the user before any installation, including Try. Browser library for your own three.js pages; runs on Windows and Android browsers with WebGL; unverified: your phone's GPU support (test the page on it). No native Claude skill/MCP in this repo.
