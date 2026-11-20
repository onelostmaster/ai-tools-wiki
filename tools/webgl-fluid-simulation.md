# WebGL Fluid Simulation

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/PavelDoGreat/WebGL-Fluid-Simulation
- **GitHub repo:** https://github.com/PavelDoGreat/WebGL-Fluid-Simulation
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @a2d2929 (2026-11-19): safe with fixes. A WebGL demo with no install. The official page loads Google Analytics (index.html:195) and script.js sends ga() events (lines 44,50,156,241-270). In a self-hosted copy, deleting the analytics.js tag at index.html:195 leaves the ga() stub (:190-194) queuing locally, so nothing leaves the page. Fix: tracker blocker on the demo; self-host the pinned copy without line 195.

## Safe install

Safe install (fixes applied):
Any browser (Windows or Android Chrome): open the official demo https://paveldogreat.github.io/WebGL-Fluid-Simulation/ (README.md:3) with a tracker blocker on (it loads Google Analytics, index.html:195); nothing to install. To use it in your own page, copy index.html, script.js and dat.gui.min.js from the official repo pinned at a2d2929, delete only the analytics.js script tag (index.html:195); the local ga() stub at :190-194 then keeps script.js's ga() calls harmless. The app-store apps are a separate, unvetted product. Check smoothness on your phone before relying on it.

## YOLO install

YOLO (your own risk): skips the tracker blocker and the analytics removal.
Open the official demo or copy the repo files as they are.

## Install notes

Not installed. Ask the user before any installation, including Try. Runs in any browser with WebGL, including Android Chrome; unverified: performance on your phone (open the demo to check). No native Claude skill/MCP in this repo.
