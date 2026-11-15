# Node.js

- **Type:** CLI
- **Category:** developer tools
- **Official URL:** https://nodejs.org
- **GitHub repo:** unknown
- **Price:** Free, open source (`nodejs.org`, checked 2026-10-31)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Node.js (official vendor, OpenJS Foundation; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. a project runs its stills and renders on it (`node scripts/render.mjs`, Pipeline & commands). No risks recorded.

## Safe install

Safe install (fixes applied):
Windows: the LTS release only, `winget install OpenJS.NodeJS.LTS` or the LTS installer from https://nodejs.org/en/download. Claude Code cloud: preinstalled, nothing to do. Android: not used. Install project packages locally with exact pins, never `npm install -g`.

## YOLO install

Not written yet.

## Install notes

Claude Code: preinstalled in the Claude Code cloud container; elsewhere no confirmed command yet; follow the official docs at [https://nodejs.org/en/download](https://nodejs.org/en/download)
