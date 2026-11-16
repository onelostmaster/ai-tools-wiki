# Basic Memory

- **Type:** MCP
- **Category:** Notion and productivity, Hermes add-ons
- **Official URL:** https://basicmemory.com
- **GitHub repo:** [https://github.com/basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory)
- **Price:** Free local (AGPL-3.0). Basic Memory Cloud: Cloud $19/month per workspace (1,900 credits included, extra credits $0.01 each; 7-day trial), Pro $99/month, Business $249/month, no per-seat charge (`basicmemory.com`, checked 2026-10-31). a review bot's review quoted $15/mo, which the pricing page no longer shows.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @c853f5f = 1.0.0 (2026-11-15): safe with fixes. Umami analytics is on unless BASIC_MEMORY_NO_PROMOS=1 (cli/analytics.py:40-43). The stdio MCP server self-upgrades in the background with --prerelease=allow (cli/commands/mcp.py:118-126) unless auto_update is false (config_models.py:685; env BASIC_MEMORY_AUTO_UPDATE=false). Hermes plugin saves every turn unless capture_per_turn is false (integrations/hermes/__init__.py:1328).

## Safe install

Safe install (fixes applied):
Env BASIC_MEMORY_NO_PROMOS=1 and BASIC_MEMORY_AUTO_UPDATE=false. Claude Code: claude mcp add -s user --env BASIC_MEMORY_AUTO_UPDATE=false --env BASIC_MEMORY_NO_PROMOS=1 basic-memory -- uvx basic-memory@1.0.0 mcp --project main. Hermes: uv tool install basic-memory==1.0.0, plugin install, then "capture_per_turn": false in ~/.hermes/basic-memory.json. Give it its own notes folder.

## YOLO install

YOLO (your own risk): skips the pin and both switches, so it sends analytics and upgrades itself to prereleases.
uvx basic-memory mcp with defaults.

## Install notes

Ask the user before installing. Env BASIC_MEMORY_NO_PROMOS=1 and BASIC_MEMORY_AUTO_UPDATE=false. Claude Code: claude mcp add -s user --env BASIC_MEMORY_AUTO_UPDATE=false --env BASIC_MEMORY_NO_PROMOS=1 basic-memory -- uvx basic-memory@1.0.0 mcp --project main. Hermes: uv tool install basic-memory==1.0.0, plugin install, then "capture_per_turn": false in ~/.hermes/basic-memory.json. Give it its own notes folder.
