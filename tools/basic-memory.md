# Basic Memory

- **Type:** MCP
- **Category:** Notion and productivity, Hermes add-ons
- **Official URL:** https://basicmemory.com
- **GitHub repo:** [https://github.com/basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory)
- **Price:** Free local (AGPL-3.0). Basic Memory Cloud: Cloud $19/month per workspace (1,900 credits included, extra credits $0.01 each; 7-day trial), Pro $99/month, Business $249/month, no per-seat charge (`basicmemory.com`, checked 2026-10-31). a review bot's review quoted $15/mo, which the pricing page no longer shows.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

Claude (code read, d7b1612, 2026-10-31): caution, 6/10. The `bm` CLI sends anonymous Umami telemetry by default (opt out: `BASIC_MEMORY_NO_PROMOS=1`); the MCP server silently self-upgrades with `--prerelease=allow` (auto_update is on by default); the agent can write, move and delete `.md` files in any project it registers; the Hermes plugin saves every turn by default. No note content is sent. a review bot : Looks safe.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code and Hermes: before the first launch, set `{"auto_update": false}` in `~/.basic-memory/config.json` and `export BASIC_MEMORY_NO_PROMOS=1`.
Claude Code: `claude mcp add -s user --env BASIC_MEMORY_AUTO_UPDATE=false basic-memory -- uvx basic-memory@1.0.0 mcp --project main` (pinned; add `--prerelease=allow` back only if uv refuses to resolve, and keep the pin).
Hermes: `uv tool install basic-memory==1.0.0` first, then `hermes plugins install basicmachines-co/basic-memory/integrations/hermes`, then `hermes memory setup basic-memory`; in `~/.hermes/basic-memory.json` set `"capture_per_turn": false, "capture_session_end": false` (it takes Hermes's single external memory-provider slot).
