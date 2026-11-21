# ida-pro-mcp

- **Type:** MCP
- **Category:** security, developer tools
- **Official URL:** https://github.com/mrexodia/ida-pro-mcp
- **GitHub repo:** https://github.com/mrexodia/ida-pro-mcp @ c133c38 (2026-09-26; MIT)
- **Price:** Free, MIT; needs IDA Pro: Essential from €1,099/year, Expert from €4,999/year, Ultimate €8,599/year, IDA Home $365/year non-commercial (hex-rays.com, checked 2026-11-02; Home support not stated).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-20

## Safety reason

Claude code read @c133c38 (2026-11-20): safe with fixes. The GUI plugin enables every tool, py_eval and debugger included, unless unticked (src/ida_pro_mcp/ida_mcp/http.py:51-73); headless drops them without --unsafe (idalib_server.py:289-291); host 127.0.0.1 (server.py:57). Text from a sample reaches the agent as data, and Claude Code's permission prompts gate every action. Fix: untick unsafe tools, approvals on, prune client configs.

## Safe install

Safe install (fixes applied):
Claude Code / Hermes (Windows, needs paid IDA Pro 8.3+): install from the repo at commit c133c38 per its README. In the IDA plugin config page untick the unsafe tools (py_eval, debugger), which the GUI plugin turns on by default (ida_mcp/http.py:51-73); for the headless server never pass --unsafe (idalib_server.py:289-291). Keep it on localhost (server.py:57, the default). After install, open ~/.claude.json and the other client configs it writes (installer_data.py:115) and remove entries for clients you do not use. Keep Claude Code's permission prompts on (never --dangerously-skip-permissions) so text inside an analysed binary can't trigger actions on its own; analyse copies of samples. Only reverse-engineer software you own or are allowed to. Android: no.

## YOLO install

YOLO (your own risk): skips unticking the unsafe tools and the config review.
Claude Code: README install with defaults; py_eval and debugger stay on in the GUI plugin.

## Install notes

Ask the user before installing.
Claude Code / Hermes: MCP server per its README; untick "unsafe" tools in the IDA plugin config page and review the MCP config it writes. Needs paid IDA Pro 8.3+. Only reverse-engineer software you own or are allowed to.
