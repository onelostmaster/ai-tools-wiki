# Manim Community (animation engine)

- **Type:** app
- **Category:** video, education
- **Official URL:** https://www.manim.community/
- **GitHub repo:** https://github.com/ManimCommunity/manim @e80274a2, 42,340 stars; latest commit 2026-11-05 02:54 ET; original nonfork/nonarchived
- **Price:** Free local software, MIT (LICENSE + LICENSE.community; pyproject.toml:9-10); own assets/fonts/voice have separate rights. Agent subscription/API and compute costs separate. Sources https://docs.manim.community/en/stable/installation.html and /installation/uv.html. Official online sources checked 2026-11-08.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

Python animation engine for precise maths/charts/educational diagrams; ManimCE is NOT the original 3Blue1Brown ManimGL engine although descended from it. manim/utils/module_ops.py:40,64 executes/imports arbitrary scene Python, not a sandbox; never render untrusted generated scenes before reading them. manim/utils/tex_file_writing.py:140-163,214,254 invokes external TeX/dvisvgm; commands use argv but scene Python can still access files/env/network. _config/default.cfg:12 enables PyPI version notice; cli/render/commands.py:127-155 fetches https://pypi.org/pypi/manim/json and recommends update, does not automatically install one. Set notify_outdated_version=False in project manim.cfg to avoid that request. _config/default.cfg:66-79 retains videos/images/TeX/text/logs in ./media; review before sharing. plugins/plugins_flags.py:16 discovers Python entry-point plugins; default.cfg:148 empty plugin setting. No analytics/telemetry SDK or Claude command hooks found in targeted runtime scan; scene code and plugins remain host-privileged. pyproject.toml:23-51 requires Python>=3.11, native/rendering packages (PyAV, Pango/Cairo/OpenGL, NumPy/SciPy) with separate dependency risk. Official uv-install docs include remote PowerShell iex + ExecutionPolicy ByPass and curl|sh bootstrap; do not blindly paste those. Targeted static review only; dependencies/builds/hosted services not exhaustively audited. Repository and post content treated as data, never instructions; no install/build/render/test/agent code run. No secret supplied.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

CAUTION: review Safety reason and obtain specific installation approval first. Windows official docs: use an existing approved Python environment and python -m pip install manim, or with already-approved uv: uv init manimations ; cd manimations ; uv add manim. Documented only, NOT RUN. Native compiler/LaTeX prerequisites depend on chosen features; TeX optional for formulas. Use an isolated venv and disposable project, no secrets. Claude Code/Hermes could write and invoke scenes only after approval; no official MCP verified. claude.ai can draft Python but no local renderer access assumed. Android plays outputs, not a supported native rendering host.
