# Reason (Reason Machines)

- **Type:** plugin
- **Category:** developer tools, automation
- **Official URL:** https://reasonmachines.com
- **GitHub repo:** https://github.com/reason-machines/reason-network @ bcf045c (2026-10-30, MIT/Apache-2.0) · https://github.com/reason-machines/reason-plugins @ a6c511e (2026-10-16, MIT); the cloud agent is closed source
- **Price:** Network and plugin free; cloud sessions use Reason plan credits, no plan prices published (`reasonmachines.com`, checked 2026-11-01); your own Claude/ChatGPT plan pays for turns run on it
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read network @bcf045c, plugins @a6c511e, a review, 2026-11-01): Use with caution. Unpinned curl|bash / irm|iex installers; daemon self-updates every 6 h by default; setup adds MCP plus an always-allow rule and hooks that inject other agents' messages (prompt-injection path); account-linked usage upload (DO_NOT_TRACK=1); skill pushes work to its paid cloud. Cloud agent closed source.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: plugin is a remote MCP server (`mcp.reasonmachines.com/mcp`); if tried, set DO_NOT_TRACK=1 and auto_update = false and don't let it auto-allow tools.
Hermes: Network plugin needs unreleased Hermes plugin APIs (`integrations/hermes/README.md`).
Windows: Network engine has a PowerShell installer (`README.md:44`); the desktop app is macOS only.
