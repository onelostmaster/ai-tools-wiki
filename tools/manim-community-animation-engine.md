# Manim Community (animation engine)

- **Type:** app
- **Category:** video, education
- **Official URL:** https://www.manim.community/
- **GitHub repo:** https://github.com/ManimCommunity/manim @e80274a2, 42,340 stars; latest commit 2026-11-05 02:54 ET; original nonfork/nonarchived
- **Price:** Free local software, MIT (LICENSE + LICENSE.community; pyproject.toml:9-10); own assets/fonts/voice have separate rights. Agent subscription/API and compute costs separate. Sources https://docs.manim.community/en/stable/installation.html and /installation/uv.html. Official online sources checked 2026-11-08.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

Claude code read @e80274a (2026-11-19): safe with fixes. The PyPI update check (manim/_config/default.cfg:12, manim/cli/render/commands.py:127-133) turns off with notify_outdated_version = False. Scenes are Python you run (manim/utils/module_ops.py:40,64), like any Python library, so reading a scene before rendering is the fix. No telemetry. Fix: venv, pin 0.22.1, update check off, read each scene.

## Safe install

Safe install (fixes applied):
Windows or Claude Code: in a new folder, uv init manimations, cd manimations, uv add manim==0.22.1 (PyPI latest on 2026-11-15, Python 3.11+), or python -m venv .venv then .venv\\Scripts\\pip install manim==0.22.1. Install uv from winget (winget install astral-sh.uv), never the docs' iex/ExecutionPolicy Bypass one-liner. Add [CLI] notify_outdated_version = False to the project manim.cfg so it stops calling pypi.org on each render (_config/default.cfg line 12, cli/render/commands.py lines 127-155). Read every scene file before rendering: manim runs it as normal Python with your rights (utils/module_ops.py lines 40 and 64). Keep plugins empty. Check ./media before sharing (it keeps logs, TeX and frames). claude.ai: can draft scenes, can't render. Android: plays the output only. Hermes: same venv, run only reviewed scenes.

## YOLO install

YOLO (your own risk): skips the version pin, the update-check opt-out and reading scenes first.
pip install manim

## Install notes

CAUTION: review Safety reason and obtain specific installation approval first. Windows official docs: use an existing approved Python environment and python -m pip install manim, or with already-approved uv: uv init manimations ; cd manimations ; uv add manim. Documented only, NOT RUN. Native compiler/LaTeX prerequisites depend on chosen features; TeX optional for formulas. Use an isolated venv and disposable project, no secrets. Claude Code/Hermes write scene files and run manim only through their command tool, and only after your approval; no official MCP verified. claude.ai can draft Python but no local renderer access assumed. Android plays outputs, not a supported native rendering host.
