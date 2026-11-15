# TinyFish (MCP + Claude Code plugin + connector)

- **Type:** MCP
- **Category:** research, scraping
- **Official URL:** https://www.tinyfish.ai
- **GitHub repo:** [https://github.com/tinyfish-io/tinyfish-mcp-server](https://github.com/tinyfish-io/tinyfish-mcp-server)
- **Price:** Search and Fetch free; browser agent $0.016/step; $8 starting credit (tinyfish.ai, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude code read of the MCP proxy @7517089 (2026-11-14): safe with fixes. The local proxy only forwards to the hosted server. Hosted tools include top_up_wallet (agent-paid): deny it. Unverified at current version: the plugin's /tinyfish:doctor (unpinned npx @tiny-fish/cli@latest, telemetry; a review bot @b61e3df) -> Contain: don't run doctor. Don't sign in to Instagram or TikTok through its browser (their terms).

## Safe install

Safe install (fixes applied):
claude.ai connector as connected. Claude Code: deny mcp__TinyFish__top_up_wallet and Bash(npx @tiny-fish/cli*) in settings.json; env DO_NOT_TRACK=1 (safe-defaults); never run /tinyfish:doctor; no IG/TikTok logins in its browser.

## YOLO install

YOLO (your own risk): skips the wallet deny and the doctor block.
Install the plugin as its README says and allow every tool.

## Install notes

Ask the user before installing. claude.ai connector as connected. Claude Code: deny mcp__TinyFish__top_up_wallet and Bash(npx @tiny-fish/cli*) in settings.json; env DO_NOT_TRACK=1 (safe-defaults); never run /tinyfish:doctor; no IG/TikTok logins in its browser.
