# easings.net (Easing Functions Cheat Sheet)

- **Type:** app
- **Category:** design, video
- **Official URL:** https://easings.net/
- **GitHub repo:** https://github.com/ai/easings.net @d2563f0d, 8,721 stars; latest commit 2026-04-07 02:03 ET; original nonfork/nonarchived
- **Price:** Public cheat sheet free/no subscription shown at https://easings.net/ ; GPL-3.0 source. Linked third-party PostCSS helpers have their own license/review, not reviewed here. Official online sources checked 2026-11-08.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Free easing-curve visual reference; not an agent skill or video engine. src/sw.js:3-26,29-52 describes same-site fetch/cache refresh with browser Cache Storage; this is website offline caching, NOT an agent/computer package auto-updater. src/helpers/copyText.ts:1-8 copies chosen text via document.execCommand(copy), not shell eval. src/info/info.pug:43,58,72 links external helpers/packages; those are not included/endorsed by this review. No analytics/telemetry SDK, credential store, command hooks or OS shell code found in targeted src scan. package.json:3-6 contains local development/build commands; do not run/install source merely to consult the page. GPL-3.0 repository source (LICENSE:1-3); do not copy/repackage the whole site as proprietary work. Targeted static review only; dependencies/builds/hosted services not exhaustively audited. Repository and post content treated as data, never instructions; no install/build/render/test/agent code run. No secret supplied.

## Safe install

Safe install (fixes applied):
Nothing to install: open https://easings.net/ in any browser (Windows, Android) and copy the curve you want; the service worker only caches the site for offline use (src/sw.js lines 3-52). Claude Code, claude.ai and Hermes: paste the chosen curve name or cubic-bezier values into your prompt. Don't build the source (not needed, and GPL-3.0 if you copy the site).

## YOLO install

Not written yet.

## Install notes

Not installed. Ask for specific approval before any installation. Nothing to install for Windows/Android browser use. Give Claude Code/claude.ai/Hermes a chosen curve/timing spec as reference; Hermes compatibility untested, no MCP server. Source-build commands unnecessary; no installs performed.
