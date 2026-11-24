# HookLab (CoolerGit)

- **Type:** skill
- **Category:** research, social posting
- **Official URL:** https://github.com/CoolerGit/HookLab
- **GitHub repo:** https://github.com/CoolerGit/HookLab @ 2cd09ae (Apache-2.0)
- **Price:** Free on GitHub, Apache-2.0 (GitHub API, checked 2026-11-22); needs paid Apify credits per fetch (README line 50; Apify price not checked: unknown)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-23

## Safety reason

a review bot read @2cd09ae (commit 2026-11-13; read: ingest.py, server.py, library.py, db_export.py, requirements.txt, .mcp.json, .env.example, CLAUDE.md, AGENTS.md, README.md, the 5 skills in .claude/skills (identical copy in .agents/skills); nothing run): safe with these fixes. Verified 1: library.py:12-19 ensure() runs pip install <package> (no version) into whichever Python runs the script when an import is missing; called at ingest.py:17-19 (requests, apify-client, Pillow) and server.py:11 (flask). requirements.txt:1-4 is also unpinned. Fix: make a venv and pip install -r requirements.txt into it first, so ensure() finds everything and installs nothing; run pip freeze > lock.txt once to record versions. Verified 2: server.py:236 starts the Flask dashboard on 0.0.0.0:5000 with no login, and /api/delete (server.py:133-161) and /api/favourite (:168) change your library; anyone on the same network can delete rows and thumbnails. Fix: in your copy change server.py:236 to host="127.0.0.1" (phone access then stops), and answer No/Cancel to the Windows Defender Firewall prompt. Verified 3: .mcp.json:3-14 defines a project MCP server that runs npx -y @apify/actors-mcp-server (no version) with your APIFY_TOKEN; none of the skills use it (ingest.py calls Apify directly via apify-client, ingest.py:342-350). Fix: decline this project MCP server when Claude Code asks to enable it. Verified 4: Apify is paid and every ingest of a TikTok/Instagram/YouTube URL runs an Apify actor that uses credits (README Requirements; ingest.py:342-350, :429). README Setup uses setx, which stores the token permanently for every program under your Windows user. Fix: set it only for the session ($env:APIFY_TOKEN=... in that PowerShell window) and ingest one URL at a time. Verified 5: hooklab SKILL.md:166 lets the agent edit the pipeline code itself when an ingest hits a bug, and the dashboard skill starts server.py hidden in the background (hooklab-dashboard SKILL.md:21). Fix: keep Claude Code's permission prompts on and approve each command; stop the dashboard with Task Manager (python.exe) when done. Verified 6: /hooklab-edit runs npx hyperframes doctor/lint/snapshot/render with no version (hooklab-edit SKILL.md:11,38) plus ffmpeg. Fix: install HyperFrames pinned as its own wiki row says before using /hooklab-edit, or skip that skill. Other: ingest.py:316 sends a HEAD request only to URLs you give it; hooks.db and thumbnails/ stay local (README). Apache-2.0; Pally font under the ITF Free Font License (NOTICE).

## Safe install

Safe install (fixes applied):
Windows + Claude Code (Python 3.10+): git clone https://github.com/CoolerGit/HookLab C:\\Projects\\HookLab ; cd C:\\Projects\\HookLab ; git checkout 2cd09ae2a9e794e3b7ba650d5ed767cef4de19b6 ; py -m venv .venv ; .venv\\Scripts\\Activate.ps1 ; pip install -r requirements.txt ; pip freeze > lock.txt ; edit server.py line 236 to host="127.0.0.1". Each session: $env:APIFY_TOKEN="<your Apify token>" in that window only (not setx), then open Claude Code in this folder from the activated venv with normal permission prompts (never --dangerously-skip-permissions); decline the project MCP server "apify" from .mcp.json; ingest one URL at a time (each costs Apify credits). Answer No to the Windows Firewall prompt for python.exe. Use /hooklab-edit only after installing HyperFrames pinned per its wiki row.
Codex on Windows: same steps; skills load from .agents/skills.
claude.ai, Hermes, Android: not supported (needs local Python and Claude Code or Codex).

## YOLO install

YOLO (your own risk): skips the venv, the 127.0.0.1 edit, session-only token and declining the Apify MCP server. Windows: git clone the repo, pip install -r requirements.txt, setx APIFY_TOKEN "<token>", open Claude Code in the folder and use /hooklab <url> and /hooklab-dashboard (dashboard reachable from any device on your Wi-Fi, which can delete library rows).

## Install notes

Safe with fixes: Claude Code/Codex skills that fetch a TikTok/Instagram/YouTube post through Apify (paid credits), have the agent score its hook and save it to a local SQLite library, then write scripts, SEO text and edits from it. Pin commit 2cd09ae, install into a venv from requirements.txt, change server.py:236 to 127.0.0.1, set APIFY_TOKEN for the session only, decline the .mcp.json Apify server, keep permission prompts on. Fits the faceless video channel idea.
