# Manim Community (animation engine)

- **Type:** app
- **Category:** video, education
- **Official URL:** https://www.manim.community/
- **GitHub repo:** https://github.com/ManimCommunity/manim @e80274a2, 42,340 stars; latest commit 2026-11-05 02:54 ET; original nonfork/nonarchived
- **Price:** Free local software, MIT (LICENSE + LICENSE.community; pyproject.toml:9-10); own assets/fonts/voice have separate rights. Agent subscription/API and compute costs separate. Sources https://docs.manim.community/en/stable/installation.html and /installation/uv.html. Official online sources checked 2026-11-08.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Python animation engine for precise maths/charts/educational diagrams; ManimCE is NOT the original 3Blue1Brown ManimGL engine although descended from it. manim/utils/module_ops.py:40,64 executes/imports arbitrary scene Python, not a sandbox; never render untrusted generated scenes before reading them. manim/utils/tex_file_writing.py:140-163,214,254 invokes external TeX/dvisvgm; commands use argv but scene Python can still access files/env/network. _config/default.cfg:12 enables PyPI version notice; cli/render/commands.py:127-155 fetches https://pypi.org/pypi/manim/json and recommends update, does not automatically install one. Set notify_outdated_version=False in project manim.cfg to avoid that request. _config/default.cfg:66-79 retains videos/images/TeX/text/logs in ./media; review before sharing. plugins/plugins_flags.py:16 discovers Python entry-point plugins; default.cfg:148 empty plugin setting. No analytics/telemetry SDK or Claude command hooks found in targeted runtime scan; scene code and plugins remain host-privileged. pyproject.toml:23-51 requires Python>=3.11, native/rendering packages (PyAV, Pango/Cairo/OpenGL, NumPy/SciPy) with separate dependency risk. Official uv-install docs include remote PowerShell iex + ExecutionPolicy ByPass and curl|sh bootstrap; do not blindly paste those. Targeted static review only; dependencies/builds/hosted services not exhaustively audited. Repository and post content treated as data, never instructions; no install/build/render/test/agent code run. No secret supplied. No fix: every scene is arbitrary Python with your user rights, so manim has no sandbox; contained by reading each scene before rendering, in a venv and a folder with no secrets.

## Safe install

Safe install (fixes applied):
Windows or Claude Code: in a new folder, `uv init manimations`, `cd manimations`, `uv add manim==0.22.1` (PyPI latest on 2026-11-15, Python 3.11+), or `python -m venv .venv` then `.venv\Scripts\pip install manim==0.22.1`. Install uv from winget (`winget install astral-sh.uv`), never the docs' iex/ExecutionPolicy Bypass one-liner. Add `[CLI]` `notify_outdated_version = False` to the project manim.cfg so it stops calling pypi.org on each render (_config/default.cfg line 12, cli/render/commands.py lines 127-155). Read every scene file before rendering: manim runs it as normal Python with your rights (utils/module_ops.py lines 40 and 64). Keep plugins empty. Check ./media before sharing (it keeps logs, TeX and frames). claude.ai: can draft scenes, can't render. Android: plays the output only. Hermes: same venv, run only reviewed scenes.

## YOLO install

YOLO (your own risk): skips the version pin, the update-check opt-out and reading scenes first.
pip install manim

## Install notes

CAUTION: review Safety reason and obtain specific installation approval first. Windows official docs: use an existing approved Python environment and python -m pip install manim, or with already-approved uv: uv init manimations ; cd manimations ; uv add manim. Documented only, NOT RUN. Native compiler/LaTeX prerequisites depend on chosen features; TeX optional for formulas. Use an isolated venv and disposable project, no secrets. Claude Code/Hermes could write and invoke scenes only after approval; no official MCP verified. claude.ai can draft Python but no local renderer access assumed. Android plays outputs, not a supported native rendering host.
