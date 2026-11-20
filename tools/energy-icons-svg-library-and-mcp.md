# Energy Icons (SVG library and MCP)

- **Type:** library
- **Category:** design, frontend
- **Official URL:** https://energyicons.com
- **GitHub repo:** https://github.com/Sam-r-passmore/energy-icons @3278ae9c, 32 stars; latest default-branch commit 2026-10-20 10:36 ET; original nonfork; archived=False
- **Price:** Free icons and source, MIT; README.md:29 and LICENSE. Optional donations separate. Official sources searched/opened online 2026-11-08; no MCP fee/auth indicated in source.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @3278ae9 + npm energy-icons 1.6.0 tarball (2026-11-19): safe with fixes. The npm package has no scripts, no dependencies and no network or eval code; only the optional hosted MCP sends search text and your IP to energyicons.com (src/app/mcp/route.ts:1-18). Fix: pinned npm package or downloaded SVGs, bundled artwork only, hosted MCP not connected.

## Safe install

Safe install (fixes applied):
Windows or Claude Code: npm install --save-exact --ignore-scripts energy-icons@1.6.0 (npm latest on 2026-11-15; no scripts, no dependencies) and use individual imports (src/dynamic.tsx lines 17-18). Render only the bundled artwork; never feed your own or uploaded SVG into its components (create-icon.tsx lines 12-32 use dangerouslySetInnerHTML). Skip the hosted MCP at https://energyicons.com/mcp: it is unauthenticated and every search text and your IP go to their server (src/app/mcp/route.ts lines 1-18); download SVGs instead. Android and claude.ai: use the SVG files. Hermes: static files only.

## YOLO install

YOLO (your own risk): skips the version pin and uses the hosted MCP.
npm install energy-icons claude mcp add --transport http energy-icons https://energyicons.com/mcp

## Install notes

CAUTION: read Safety reason; specific approval required before installation/connection. Documented README.md: npm install energy-icons. Use individual imports to avoid including the full registry (packages/energy-icons/src/dynamic.tsx:17-18). Free remote MCP URL is source-documented https://energyicons.com/mcp, custom connector for claude.ai claimed in route.ts:4-6, untested. Windows Claude Code/local terminal or HTTP client; Hermes compatibility untested. Downloaded SVG works in Android browser/apps.
