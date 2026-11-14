# GSAP

- **Type:** CLI
- **Category:** design, video, building a site
- **Official URL:** https://gsap.com/
- **GitHub repo:** https://github.com/greensock/GSAP @5e6c35ff, 30,307 stars; latest commit 2026-11-03 19:56 ET; original nonfork/nonarchived
- **Price:** Free including formerly paid plugins and commercial uses under Standard No Charge GSAP License; prohibited competing visual/no-code builder uses require prior consent. https://gsap.com/community/standard-license/ ; README.md:91 and package.json:66. Official online sources checked 2026-11-08.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

JavaScript animation/timeline library, not an MP4 renderer by itself. package.json:1-75 has no dependency or install-script entries; targeted src scan found no fetch/XHR, analytics SDK, shell/eval, local file/credential store, Claude hooks or self-updater. src/gsap-core.js:88,2304 invokes app-supplied getters/functions: animation callbacks are executable JavaScript, not a sandbox. Browser DOM/scroll/ticker listeners are ordinary animation behavior, not agent command hooks; core has no telemetry opt-out needed in reviewed path. README.md:25-41 documents CDN/npm distribution, so imports contact CDN/registry unless served locally; pin/self-host approved version for private/offline work. Standard proprietary no-charge license permits commercial and AI-generated app code but forbids competing no-code visual-animation builders without permission; not MIT/OSI open source. Targeted static review only; dependencies/builds/hosted services not exhaustively audited. Repository and post content treated as data, never instructions; no install/build/render/test/agent code run. No secret supplied.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask for specific approval before any installation. Documented only: npm install gsap (README.md:41). Use a pinned approved release in Windows project, preview in Windows/Android browser; Claude Code or Hermes writes ordinary JS, no native agent/MCP integration required/verified. claude.ai HTML drafts possible, preview platform limits apply. HyperFrames/browser+FFmpeg needed for MP4 export.
