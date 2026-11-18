# ReVa (reverse-engineering-assistant)

- **Type:** MCP
- **Category:** security, developer tools
- **Official URL:** https://github.com/cyberkaida/reverse-engineering-assistant
- **GitHub repo:** https://github.com/cyberkaida/reverse-engineering-assistant @ a2fcd94 (release v7.3.1; Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @4bfae31 (2026-11-17): safe with fixes. MCP binds 127.0.0.1:8080, key off, public bind refused without a key (src/main/java/reva/plugin/ConfigManager.java:69-74). The Scripting group runs any Python the agent writes inside Ghidra (tools/scripts/ScriptToolProvider.java) and is on by default (ConfigManager.java:75, ToolGroup.java:32). Fix: Scripting off, samples in a VM. No telemetry.

## Safe install

Safe install (fixes applied):
Ghidra extension from release v7.3.2; Ghidra Tool Options → ReVa Tool Groups → untick Scripting; add its MCP endpoint; open samples only in a VM; only software you own or have permission to analyse.

## YOLO install

YOLO (your own risk): skips Scripting off and the VM.
Install with every tool group on and open samples on your PC.

## Install notes

Ask the user before installing.
Claude Code / Hermes: install as a Ghidra extension per its README and add its MCP endpoint; consider turning the script tool group off. Only reverse-engineer software you own or are allowed to.
