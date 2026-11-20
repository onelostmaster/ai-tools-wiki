# Rune Icons (SVG library and local MCP)

- **Type:** library
- **Category:** design, frontend
- **Official URL:** https://runeicons.com
- **GitHub repo:** https://github.com/Runeicons/runeicons @2f2a86a3, 727 stars; latest default-branch commit 2026-10-11 07:07 ET; original nonfork; archived=False
- **Price:** Free icons and packages Apache-2.0 (LICENSE:9-24); website/editor software separately Apache+visible attribution+Commons Clause (:27-70), not unrestricted resale. Brand logos excluded (:75+). Official terms/privacy searched/opened online; no required icon fee.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @2f2a86a + npm runeicons-mcp 0.1.0 tarball (2026-11-19): safe with fixes. Compared the package with the repo: dist/index.js, icons.js and brands.js only read bundled files (dist/icons.js:26, dist/brands.js:52); no fetch, child_process or eval; no install hooks. Six read-only tools over stdio. Fix: pinned 0.1.0 with --ignore-scripts and a local node path instead of npx -y.

## Safe install

Safe install (fixes applied):
Claude Code on Windows (Node.js 20+): in a dedicated folder, npm install --save-exact --ignore-scripts runeicons-mcp@0.1.0 (npm latest on 2026-11-15; the package has no install hooks, only build/test scripts), then claude mcp add runeicons -- node <folder>\\node_modules\\runeicons-mcp\\dist\\index.js instead of the README's unpinned npx -y runeicons-mcp (packages/runeicons-mcp/README.md lines 29-33). It runs over stdio with six read-only lookup tools and no network (src/index.ts lines 91-291). Icons only: copy SVGs from packages/ at commit 2f2a86a; don't reuse editor or landing-page code for resale (Commons Clause, LICENSE lines 27-70); brand logos follow each owner's rules. claude.ai and Android: use downloaded SVG files (claude.ai cannot launch a local stdio MCP). Hermes: same pinned node command over stdio, unreviewed for Hermes.

## YOLO install

YOLO (your own risk): skips the version pin and the local node path.
claude mcp add runeicons -- npx -y runeicons-mcp

## Install notes

CAUTION: read Safety reason; specific approval required before installation/connection. Documented only, NOT RUN: claude mcp add runeicons -- npx -y runeicons-mcp (packages/runeicons-mcp/README.md:29-33). Safer later: approve/pin audited npm package and point local node to dist/index.js (:81-90), no blanket -y auto-download. Windows Claude Code/Desktop stdio documented; claude.ai cannot directly launch local stdio; remote bridge not supplied. Hermes stdio compatibility untested. Android: website/assets, not native CLI host.
