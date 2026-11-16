# sgp4 (python-sgp4)

- **Type:** library
- **Category:** research, developer tools
- **Official URL:** https://pypi.org/project/sgp4/
- **GitHub repo:** https://github.com/brandon-rhodes/python-sgp4 @ 8e234f8
- **Price:** Free, MIT (PyPI and GitHub, checked 2026-11-12)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot read-only scan @ 8e234f8 (2026-11-12, PyPI 2.27): pure maths package with optional C++ extension; no network, subprocess or eval in sgp4/ (setup.py only eval-compiles its own __init__ to read the version). MIT, official repo by the author, active.

## Safe install

Safe install (fixes applied):
Claude Code (Windows) or the project container: in a venv, `pip install sgp4==2.27` (the reviewed release, still the PyPI latest on 2026-11-15); the wheel ships the C++ extension, so nothing compiles and no network is used (code read @8e234f8). Feed it CelesTrak elements cached under the CelesTrak row's 2-hour rule. claude.ai, Hermes and Android: Python library, no install route.

## YOLO install

YOLO (your own risk): skips the venv and the version pin.
pip install sgp4

## Install notes

Claude Code / Windows: pip install sgp4==2.27 in the project venv (wheels include the fast C++ extension). Feed it fresh elements from CelesTrak (one download per 2 hours at most).
