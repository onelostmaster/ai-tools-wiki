# claude-mem

- **Type:** plugin
- **Category:** Notion and productivity, Hermes add-ons
- **Official URL:** https://docs.claude-mem.ai
- **GitHub repo:** [https://github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
- **Price:** Free, open-source engine (Apache-2.0, per a review bot's code read); it uses your own LLM, by default your Claude subscription. Optional CMEM Pro (hosted observation, cloud sync, private MCP recall): 30-day free trial, then $30/month; TeamBrain team pricing not announced (`cmem.ai`, checked 2026-10-31).
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (code read, a review / Hermes a review, 70aa400, 2026-10-31): Use with caution. Hooks on every prompt and tool call feed all tool output to an observer LLM, which stores it; stored observations are re-injected at SessionStart, so poisoned tool output can persist. Setup runs bun install; a self-heal step edits your shell rc or Windows PATH (PowerShell -ExecutionPolicy Bypass). Worker binds 127.0.0.1; cloud sync to cmem.ai off by default. No fix: hooks send every tool result to the memory model (plugin/hooks/hooks.json lines 80-86, matcher *) and stored memories are re-injected at SessionStart (line 20), so poisoned tool output persists; this is the tool's core design and cannot be turned off; the install-script and telemetry risks are fixed in Safe install.

## Safe install

Safe install (fixes applied):
Windows (Claude Code; checked @4412033, v15.21.0): install Bun (winget install Oven-sh.Bun) and uv (winget install astral-sh.uv) yourself first; otherwise setup pipes bun.sh and astral.sh install scripts into PowerShell (src/npx-cli/install/setup-runtime.ts lines 150-153, 187-192, 297-302, 351-353). Then run npx claude-mem@15.21.0 install --ide claude-code and turn usage analytics off with npx claude-mem telemetry disable (README.md line 149: on by default). It will add its bin folder to your Windows user PATH through a hidden PowerShell -ExecutionPolicy Bypass call (src/launcher/install-launcher.ts lines 386-390, 896-899); this cannot be skipped. Leave cloud sync off (empty token by default, src/shared/SettingsDefaultsManager.ts line 735). The worker stays on 127.0.0.1 (src/npx-cli/commands/install.ts line 1195). No fix: hooks send every tool result to the memory model (plugin/hooks/hooks.json lines 80-86, matcher *) and stored memories are re-injected at SessionStart (line 20), so poisoned tool output persists; review or clear ~/.claude-mem after sessions on untrusted repos or web pages. Hermes: npx claude-mem@15.21.0 install --ide hermes replaces your active Hermes memory provider. Android: no.

## YOLO install

YOLO (your own risk): skips the Bun/uv pre-install, the version pin and the telemetry opt-out.
Claude Code: /plugin marketplace add thedotmack/claude-mem, then /plugin install claude-mem; setup pipes the Bun and uv installers into PowerShell and analytics stay on.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: a review bot gave no formal steps (not Looks safe); if you try it: `/plugin marketplace add thedotmack/claude-mem`, then `/plugin install claude-mem`.
Hermes: if you try it: `npx claude-mem install --ide hermes` (replaces your active Hermes memory provider; uninstalling restores it).
