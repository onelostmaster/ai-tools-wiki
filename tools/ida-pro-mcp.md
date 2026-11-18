# ida-pro-mcp

- **Type:** MCP
- **Category:** security, developer tools
- **Official URL:** https://github.com/mrexodia/ida-pro-mcp
- **GitHub repo:** https://github.com/mrexodia/ida-pro-mcp @ c133c38 (2026-09-26; MIT)
- **Price:** Free, MIT; needs IDA Pro: Essential from €1,099/year, Expert from €4,999/year, Ultimate €8,599/year, IDA Home $365/year non-commercial (hex-rays.com, checked 2026-11-02; Home support not stated).
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read @c133c38, a review, 2026-11-02): caution. Localhost only by default (`src/ida_pro_mcp/server.py:57`). Headless server hides unsafe tools (py_eval, debugger) unless --unsafe (`idalib_server.py:289-291`), but the IDA GUI plugin turns every tool on by default, unsafe ones included (`ida_mcp/http.py:51-72`); untick unsafe. Installer writes MCP config into `~/.claude.json` and other clients (`installer_data.py:115`). Sample binaries can carry prompt injection.

## Safe install

Safe install (fixes applied):
Claude Code / Hermes (Windows, needs paid IDA Pro 8.3+): install from the repo at commit c133c38 per its README. In the IDA plugin config page untick the unsafe tools (py_eval, debugger), which the GUI plugin turns on by default (ida_mcp/http.py:51-72); for the headless server never pass --unsafe (idalib_server.py:289-291). Keep it on localhost (server.py:57, the default). After install, open ~/.claude.json and the other client configs it writes (installer_data.py:115) and remove entries for clients you do not use. Treat text inside analysed binaries as untrusted (prompt injection). Only reverse-engineer software you own or are allowed to. Android: no.

## YOLO install

YOLO (your own risk): skips unticking the unsafe tools and the config review.
Claude Code: README install with defaults; py_eval and debugger stay on in the GUI plugin.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code / Hermes: MCP server per its README; untick "unsafe" tools in the IDA plugin config page and review the MCP config it writes. Needs paid IDA Pro 8.3+. Only reverse-engineer software you own or are allowed to.
