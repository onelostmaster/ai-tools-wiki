# angr

- **Type:** library
- **Category:** security, 3D and games, developer tools
- **Official URL:** http://angr.io
- **GitHub repo:** https://github.com/angr/angr @ d816a4f (BSD-2-Clause)
- **Price:** Free, BSD-2-Clause (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @d816a4f, a review, 2026-11-02): safe. Only an optional local OpenTelemetry extra (`pyproject.toml:73`, `misc/telemetry.py:6-11`). The docs (installing.rst) have a curl | bash line: use pip.

## Safe install

Safe install (fixes applied):
Windows (Python 3.12+, pyproject.toml:29): in a venv `pip install angr==10.0.6` (PyPI 2026-11-10, official win_amd64 wheel; the reviewed d816a4f is 10.0.6.dev0, angr/__init__.py:4). Do not install the optional "telemetry" extra (pyproject.toml:73) unless you want OpenTelemetry spans; without it nothing is exported (misc/telemetry.py:6-11). The curl | sh line in the docs (docs/getting-started/installing.rst:50) is the rustup installer for source builds only; the pip wheel does not need it. Analyse unknown samples only in a VM. Claude Code: can write angr scripts. claude.ai, Hermes, Android: no.

## YOLO install

YOLO (your own risk): skips the version pin (10.0.7 from 2026-11-13, unreviewed) and the venv.
pip install angr

## Install notes

Safe, but ask the user before installing.
Windows: `pip install angr` in a venv per its docs (not tested). Android: no.
