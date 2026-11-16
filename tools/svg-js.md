# SVG.js

- **Type:** library
- **Category:** generating videos, design
- **Official URL:** https://github.com/svgdotjs/svg.js
- **GitHub repo:** https://github.com/svgdotjs/svg.js
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted source read, not a full dependency/binary audit; svgdotjs/svg.js @4b8809b. SVG drawing and animation. Source scan found no telemetry/install hooks; src/main.js:55-64 exports drawing utilities; README.md:12 MIT. CDN installation is optional; use pinned local assets.

## Safe install

Safe install (fixes applied):
Windows Claude Code or any web project: `npm install @svgdotjs/svg.js@3.2.8` (current npm release; its package.json has no preinstall/install/postinstall scripts and no runtime dependencies) and bundle it locally instead of loading it from a CDN. It runs in the browser sandbox; the reviewed source has no telemetry (src/main.js:55-64 exports drawing utilities only). Not a claude.ai or Hermes tool.

## YOLO install

YOLO (your own risk): skips the version pin and local bundling.
<script src="https://cdn.jsdelivr.net/npm/@svgdotjs/svg.js"></script>

## Install notes

Not installed. Ask the user before any installation, including Try. Windows development; the result is a web page that runs in any modern browser, Android included (plain SVG/DOM animation, no GPU requirement). No native Claude skill/MCP in this repo.
