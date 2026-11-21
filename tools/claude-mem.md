# claude-mem

- **Type:** plugin
- **Category:** Notion and productivity, Hermes add-ons
- **Official URL:** https://docs.claude-mem.ai
- **GitHub repo:** [https://github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
- **Price:** Free, open-source engine (Apache-2.0, per a review bot's code read); it uses your own LLM, by default your Claude subscription. Optional CMEM Pro (hosted observation, cloud sync, private MCP recall): 30-day free trial, then $30/month; TeamBrain team pricing not announced (`cmem.ai`, checked 2026-10-31).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-20

## Safety reason

Claude code read @4412033 v15.21.0 (2026-11-20): safe with fixes. Correction: capture has switches. CLAUDE_MEM_SKIP_TOOLS (src/shared/SettingsDefaultsManager.ts:567) keeps web and MCP tool output out of memory, CLAUDE_MEM_EXCLUDED_PROJECTS (:683) excludes untrusted repo paths, so untrusted text never reaches the store re-injected at SessionStart (plugin/hooks/hooks.json:20,80-86). Telemetry and installer fixes as before.

## Safe install

Safe install (fixes applied):
Windows (Claude Code; checked @4412033, v15.21.0): install Bun (winget install Oven-sh.Bun) and uv (winget install astral-sh.uv) yourself first; otherwise setup pipes bun.sh and astral.sh install scripts into PowerShell (src/npx-cli/install/setup-runtime.ts lines 150-153, 187-192, 297-302, 351-353). Then run npx claude-mem@15.21.0 install --ide claude-code and turn usage analytics off with npx claude-mem telemetry disable (README.md line 149: on by default). It will add its bin folder to your Windows user PATH through a hidden PowerShell -ExecutionPolicy Bypass call (src/launcher/install-launcher.ts lines 386-390, 896-899); this cannot be skipped. Leave cloud sync off (empty token by default, src/shared/SettingsDefaultsManager.ts line 735). The worker stays on 127.0.0.1 (src/npx-cli/commands/install.ts line 1195). In ~/.claude-mem/settings.json add WebFetch,WebSearch and the MCP tools that read outside content to CLAUDE_MEM_SKIP_TOOLS (default list at SettingsDefaultsManager.ts:567) and put the folders where you open untrusted repos in CLAUDE_MEM_EXCLUDED_PROJECTS (comma-separated globs, :683), so their output is never stored and never re-injected at SessionStart (hooks.json lines 20, 80-86). Wrap anything private in <private> tags (README.md:229). Hermes: npx claude-mem@15.21.0 install --ide hermes replaces your active Hermes memory provider. Android: no.

## YOLO install

YOLO (your own risk): skips the Bun/uv pre-install, the version pin and the telemetry opt-out.
Claude Code: /plugin marketplace add thedotmack/claude-mem, then /plugin install claude-mem; setup pipes the Bun and uv installers into PowerShell and analytics stay on.

## Install notes

Ask the user before installing.
Claude Code: a review bot gave no formal steps (not Looks safe); if you try it: `/plugin marketplace add thedotmack/claude-mem`, then `/plugin install claude-mem`.
Hermes: if you try it: `npx claude-mem install --ide hermes` (replaces your active Hermes memory provider; uninstalling restores it).
