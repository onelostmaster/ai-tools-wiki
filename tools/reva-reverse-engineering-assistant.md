# ReVa (reverse-engineering-assistant)

- **Type:** MCP
- **Category:** security, developer tools
- **Official URL:** https://github.com/cyberkaida/reverse-engineering-assistant
- **GitHub repo:** https://github.com/cyberkaida/reverse-engineering-assistant @ a2fcd94 (release v7.3.1; Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @a2fcd94, a review, 2026-11-02): caution. MCP server binds 127.0.0.1:8080 with no API key by default (`ConfigManager.java:69-74`) and blocks a public bind without a key (:74). Its run-script tool runs any Python the agent writes inside Ghidra (`ScriptToolProvider.java:146-178`), on by default (`ConfigManager.java:75`). Sample binaries can carry prompt injection; use a VM. No telemetry or curl|bash.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code / Hermes: install as a Ghidra extension per its README and add its MCP endpoint; consider turning the script tool group off. Only reverse-engineer software you own or are allowed to.
