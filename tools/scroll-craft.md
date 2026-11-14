# scroll-craft

- **Type:** plugin
- **Category:** building a site, design
- **Official URL:** https://github.com/nateherkai/scroll-craft
- **GitHub repo:** https://github.com/nateherkai/scroll-craft @ 75d81f7 (MIT; plugin 0.3.1; HEAD on 2026-11-12, last commit 2026-09-30)
- **Price:** Free (MIT LICENSE, checked at commit 75d81f7 on 2026-11-12); optional kie.ai image and clip generation spends paid credits (.env.example lines 9-13).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-12

## Safety reason

a review bot (code read @75d81f7, 2026-11-12, no-intake review): Safe. The plugin is one skill (SKILL.md plus references and a browser scroll engine) with no hooks, no MCP server and no install-time scripts (.claude-plugin/marketplace.json, plugins/nateherk-design/.claude-plugin/plugin.json). Its helper scripts only run when asked: doctor.mjs runs ffmpeg with -filters and -encoders to check the build (lines 22-33, 73, 84); serve.mjs is a static file server on 127.0.0.1 that refuses paths outside the build folder (lines 27-49), and --lan opens it to the local network (lines 28-29, 72); shoot.mjs and worldflight-assert.mjs drive headless Chrome against that local page and write screenshots and report.json (shoot.mjs lines 70-100, 465), then ffmpeg makes a contact sheet (lines 647-652). The only outside network use is kie.mjs, which reads KIE_AI_API_KEY from the environment or a .env file (lines 47-58) and sends it only to api.kie.ai and kie.ai's documented upload host kieai.redpandaai.co (lines 26-27, 69, 83, 96, 139; host confirmed on docs.kie.ai), then saves results (lines 117-120). The engine's fetch only loads the page's own clips (scrollcraft.js line 660). No telemetry, no other keys. Not reviewed: the media files and EXAMPLES builds.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Code-reviewed by a review bot @75d81f7 (plugin nateherk-design 0.3.1, safe). Claude Code on Windows: /plugin marketplace add nateherkai/scroll-craft then /plugin install nateherk-design (README lines 125-129), then /reload-plugins if asked; run scripts/doctor.mjs first. Needs Node; for its checks it needs playwright-core in the build folder plus Chrome (it looks in LOCALAPPDATA on Windows) and a full ffmpeg build (WinGet Gyan.FFmpeg works). No key is needed for a build from your own photos and footage. Only add KIE_AI_API_KEY (in a .env file, never committed) if you want it to generate images or clips, which spends paid kie.ai credits. Use serve.mjs --lan only on a trusted network: it shares the whole build folder with anyone on that network until stopped. Installs are unpinned, so later versions arrive without a review.
