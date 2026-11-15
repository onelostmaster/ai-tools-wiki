# claude-mem

- **Type:** plugin
- **Category:** Notion and productivity, Hermes add-ons
- **Official URL:** https://docs.claude-mem.ai
- **GitHub repo:** [https://github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
- **Price:** Free, open-source engine (Apache-2.0, per a review bot's code read); it uses your own LLM, by default your Claude subscription. Optional CMEM Pro (hosted observation, cloud sync, private MCP recall): 30-day free trial, then $30/month; TeamBrain team pricing not announced (`cmem.ai`, checked 2026-10-31).
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read, a review / Hermes a review, 70aa400, 2026-10-31): Use with caution. Hooks on every prompt and tool call feed all tool output to an observer LLM, which stores it; stored observations are re-injected at SessionStart, so poisoned tool output can persist. Setup runs `bun install`; a self-heal step edits your shell rc or Windows PATH (PowerShell `-ExecutionPolicy Bypass`). Worker binds 127.0.0.1; cloud sync to `cmem.ai` off by default.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: a review bot gave no formal steps (not Looks safe); if you try it: `/plugin marketplace add thedotmack/claude-mem`, then `/plugin install claude-mem`.
Hermes: if you try it: `npx claude-mem install --ide hermes` (replaces your active Hermes memory provider; uninstalling restores it).
