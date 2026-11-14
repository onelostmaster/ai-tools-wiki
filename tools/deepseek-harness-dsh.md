# DeepSeek Harness (dsh)

- **Type:** app
- **Category:** developer tools, automation, 3D and games
- **Official URL:** https://deepseek.com/harness
- **GitHub repo:** https://github.com/deepseek-ai/deepseek-harness @ ce7073d (MIT; official DeepSeek org; pushed 2026-10-30; developer preview)
- **Price:** Harness free (MIT). DeepSeek API: deepseek-flash $0.30 per 1M input (cache miss), $1.20 per 1M output at peak, half off-peak; V4-Pro $1.32/$3.96; Search and Fetch $0.75 per 1,000 since 2026-11-01 (api-docs.deepseek.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-02

## Safety reason

a review bot (read of README/SAFETY.md @ce7073d, a review, 2026-11-02): caution. Its SAFETY.md says it can run model-written code and commands, load third-party plugins and reach network, processes, credentials and files (`SAFETY.md:9`); sandboxing "does not guarantee isolation" (`SAFETY.md:13`). Creator Mode installs agent-written plugins that persist. Developer preview with breaking changes (`README.md:11-13`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: needs Node.js; `npx @deepseek-ai/dsh web` opens a Web UI on 127.0.0.1:3080 (README.md:24-27); untested.
