# NumPy

- **Type:** library
- **Category:** research, developer tools
- **Official URL:** https://numpy.org
- **GitHub repo:** https://github.com/numpy/numpy
- **Price:** Free, BSD-3-Clause (numpy.org / PyPI, checked 2026-11-12)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-15

## Safety reason

Official NumPy project (numpy.org, PyPI 2.5.4 checked 2026-11-12); BSD-3-Clause core; no network use in normal operation. Not code-read by a review bot (very large, widely audited).

## Safe install

Safe install (fixes applied):
Claude Code (Windows) or the project container: in a venv, `pip install numpy==2.5.4` (PyPI latest on 2026-11-15, needs Python 3.12+), pinned in the project requirements; it installs from the official binary wheel, so nothing is compiled. unverified: the NumPy source itself (too large for a review bot read; widely audited); containment: the pin plus the venv. claude.ai, Hermes and Android: Python library, use it inside a project, no install route.

## YOLO install

YOLO (your own risk): skips the venv and the version pin.
pip install numpy

## Install notes

Claude Code / Windows: pip install numpy (pin the version in the project requirements). Usually pulled in by other science packages anyway.
