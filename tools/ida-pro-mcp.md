# ida-pro-mcp

- **Type:** MCP
- **Category:** security, developer tools
- **Official URL:** https://github.com/mrexodia/ida-pro-mcp
- **GitHub repo:** https://github.com/mrexodia/ida-pro-mcp @ c133c38 (2026-09-26; MIT)
- **Price:** Free, MIT; needs IDA Pro: Essential from €1,099/year, Expert from €4,999/year, Ultimate €8,599/year, IDA Home $365/year non-commercial (hex-rays.com, checked 2026-11-02; Home support not stated).
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (code read @c133c38, a review, 2026-11-02): caution. Localhost only by default (`src/ida_pro_mcp/server.py:57`). Headless server hides unsafe tools (py_eval, debugger) unless --unsafe (`idalib_server.py:289-291`), but the IDA GUI plugin turns every tool on by default, unsafe ones included (`ida_mcp/http.py:51-72`); untick unsafe. Installer writes MCP config into `~/.claude.json` and other clients (`installer_data.py:115`). Sample binaries can carry prompt injection.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code / Hermes: MCP server per its README; untick "unsafe" tools in the IDA plugin config page and review the MCP config it writes. Needs paid IDA Pro 8.3+. Only reverse-engineer software you own or are allowed to.
