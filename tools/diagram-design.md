# Diagram Design

- **Type:** skill
- **Category:** design
- **Official URL:** https://diagramdesign.dev
- **GitHub repo:** https://github.com/cathrynlavery/diagram-design @ f2496ac (MIT; plugin 2.6.153; HEAD on 2026-11-12)
- **Price:** Free (MIT LICENSE file, checked at commit f2496ac on 2026-11-12)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-12

## Safety reason

a review bot (code read @f2496ac, 2026-11-12, no-intake review): Safe. The plugin is markdown instructions, HTML templates and local Python scripts under skills/diagram-design; it has no hooks, no MCP server and no keys (.claude-plugin/plugin.json). The shipped scripts only parse and write local files: the draw.io, Mermaid, Excalidraw and PlantUML importers, export_svg.py (writes the SVG, line 1615) and self_check.py (urlparse only checks font links, line 470); none of them opens a network connection or runs a shell command. export_png.py opens the local HTML file in Playwright's Chromium with its default sandbox (lines 35-41). Generated HTML loads Google Fonts (SKILL.md section 12; references/style-guide.md line 101), and PRIVACY.md states no server, analytics or telemetry. The repo-root scripts/ folder is maintainer tests and builds (subprocess to git and python, a local test server in lint-render.py line 637, and build-icons.py fetching icon sets at line 182); a normal plugin user does not run them. Caveat: the README suggests marketplace auto-update (lines 66-71); keep it off. Not reviewed: the 224 asset files beyond a check for external script tags (none found).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @f2496ac (plugin 2.6.153, safe). Claude Code on Windows: /plugin marketplace add cathrynlavery/diagram-design then /plugin install diagram-design@diagram-design (README lines 60-61). Leave marketplace auto-update off, although the README suggests turning it on (README lines 66-71): with it on, new versions install without a review. PNG export is optional and needs pip install playwright and playwright install chromium (README line 517); SVG and HTML output need nothing extra. Generated diagrams link Google Fonts, so opening one makes a font request to Google; that is the only outside link the skill adds.
