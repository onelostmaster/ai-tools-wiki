# Blockbench (JannisX11)

- **Type:** app
- **Category:** 3D and games, design
- **Official URL:** https://www.blockbench.net
- **GitHub repo:** https://github.com/JannisX11/blockbench @ ec0b282 (GPL-3.0; v5.2.2)
- **Price:** Free, GPL-3.0 (github.com, checked 2026-11-03)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @ec0b282, 2026-11-03): safe. Two anonymous counter pings with empty bodies (new install, 3rd launch) to blckbn.ch (`js/boot_loader.js:104-123`) and a plugin-install counter (`js/plugin_loader.ts:488`). Auto-updater checks but downloads only after you allow it (`electron/main.js:299-310`). Plugins load from the official blockbench-plugins repo via jsDelivr (`js/plugin_loader.ts:40,1148`) and run as full-access code (`js/plugin_loader.ts:809`; nodeIntegration on, contextIsolation off, `electron/main.js:80-81`), so install only well-known plugins.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: installer from blockbench.net, or use web.blockbench.net in the browser. Install only well-known plugins. Android: web app in a browser (touch support limited, not checked).
