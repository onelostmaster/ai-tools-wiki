# notebooklm-py (teng-lin)

- **Type:** library
- **Category:** research, Notion and productivity
- **Official URL:** https://github.com/teng-lin/notebooklm-py
- **GitHub repo:** https://github.com/teng-lin/notebooklm-py @ 7db1000 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02); uses your own Google NotebookLM account
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @85143f0 v0.8.6 (2026-11-17): safe with fixes. Unofficial, on undocumented Google APIs (README.md:20-27). Login keeps Google cookies in a profile folder, chmod 700 except on Windows (src/notebooklm/paths.py:111,143); --browser-cookies and --all-accounts copy cookies from your browser (docs/cli-reference.md:592-594). Fix: a spare Google account, Playwright login only.

## Safe install

Safe install (fixes applied):
Own venv; pip install "notebooklm-py[browser]==0.8.6"; notebooklm login with a spare Google account, never the Google AI Pro family account; never --browser-cookies, --all-accounts or --master-token; notebooklm skill install for Claude Code.

## YOLO install

YOLO (your own risk): skips the spare account and the login limits.
Import cookies from your main browser account.

## Install notes

Ask the user before installing.
Claude Code: install as its README says (Python package plus the bundled skill).
Windows: Python in a venv (not tested). Android: no.
