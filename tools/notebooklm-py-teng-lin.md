# notebooklm-py (teng-lin)

- **Type:** library
- **Category:** research, Notion and productivity
- **Official URL:** https://github.com/teng-lin/notebooklm-py
- **GitHub repo:** https://github.com/teng-lin/notebooklm-py @ 7db1000 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02); uses your own Google NotebookLM account
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light code read @7db1000, a review, 2026-11-02): caution. Unofficial; uses undocumented Google APIs that can break or break terms (`README.md:20-26`). Logs in through a Playwright browser and keeps your Google cookies in `~/.notebooklm/storage_state.json` (`src/notebooklm/auth.py:5,165`, `paths.py:6-23`); guard that file like a password.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: install as its README says (Python package plus the bundled skill).
Windows: Python in a venv (not tested). Android: no.
