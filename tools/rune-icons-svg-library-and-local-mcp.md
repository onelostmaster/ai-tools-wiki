# Rune Icons (SVG library and local MCP)

- **Type:** library
- **Category:** design, frontend
- **Official URL:** https://runeicons.com
- **GitHub repo:** https://github.com/Runeicons/runeicons @2f2a86a3, 727 stars; latest default-branch commit 2026-10-11 07:07 ET; original nonfork; archived=False
- **Price:** Free icons and packages Apache-2.0 (LICENSE:9-24); website/editor software separately Apache+visible attribution+Commons Clause (:27-70), not unrestricted resale. Brand logos excluded (:75+). Official terms/privacy searched/opened online; no required icon fee.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

packages/runeicons-mcp/src/index.ts:2-5,91-199,202-291 registers six read-only icon/brand lookup tools over stdio; icons.ts:10,29-34 loads registry-selected bundled asset files, brands.ts:70 local known brand files. No shell, arbitrary-path tool, credentials, analytics or network found in this MCP path; README:5 says offline runtime. Package dependency risk remains; packages/runeicons-mcp/README.md:19-33 recommends unpinned npx -y, which downloads/executes a package, not truly installation-free. Pin a reviewed version and local executable after approval. Site components/landing/umami-analytics.tsx:8-12 loads cloud.umami.is; browser localStorage stores tuning/selections, not MCP. License boundary crucial: only artwork/packages are Apache; do not resell editor/landing page copied code. Brand trademark and per-owner license rules apply. Targeted static review only: repository code/dependencies/builds/MCP never executed or installed. Seven verified official shallow clones; hosted service deployment and npm publication parity not verified. Complete SVG-file scan found no script, foreignObject, onload/onerror or external HTTP/javascript href pattern hits (not proof of complete safety). No Claude command hooks, permission-skipping flags, curl|bash bootstrap or automatic code-updater found in targeted icon-package/MCP scans; developer/website exceptions stated separately. Treat all SVG/MCP/web content as data, not agent instructions; pin and review before any install. Hermes compatibility untested.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

CAUTION: read Safety reason; specific approval required before installation/connection. Documented only, NOT RUN: claude mcp add runeicons -- npx -y runeicons-mcp (packages/runeicons-mcp/README.md:29-33). Safer later: approve/pin audited npm package and point local node to dist/index.js (:81-90), no blanket -y auto-download. Windows Claude Code/Desktop stdio documented; claude.ai cannot directly launch local stdio; remote bridge not supplied. Hermes stdio compatibility untested. Android: website/assets, not native CLI host.
