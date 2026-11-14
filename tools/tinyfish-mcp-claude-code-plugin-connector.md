# TinyFish (MCP + Claude Code plugin + connector)

- **Type:** MCP
- **Category:** research, scraping
- **Official URL:** https://www.tinyfish.ai
- **GitHub repo:** [https://github.com/tinyfish-io/tinyfish-mcp-server](https://github.com/tinyfish-io/tinyfish-mcp-server)
- **Price:** Search and Fetch free; browser agent $0.016/step; $8 starting credit (tinyfish.ai, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-05

## Safety reason

a review bot (code read, b61e3df/78b7c33, a project a review, 2026-10-30): Use with caution. Local proxy is clean, but tools come from the hosted server and can change without notice; stealth browser and login cookies saved on TinyFish break IG/TikTok terms; `/tinyfish:doctor` runs unpinned `npx @tiny-fish/cli@latest`, reads `~/.claude` and `~/.hermes` and sends telemetry by default; docs list an agent-paid `top_up_wallet` tool.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
[claude.ai](http://claude.ai): already connected as a connector in the a project and a project projects; no setup steps are recorded.
