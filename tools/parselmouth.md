# Parselmouth

- **Type:** library
- **Category:** a project, voice and audio
- **Official URL:** https://github.com/YannickJadoul/Parselmouth
- **GitHub repo:** [https://github.com/YannickJadoul/Parselmouth](https://github.com/YannickJadoul/Parselmouth) (confirmed on PyPI `praat-parselmouth`, 2026-10-31; not in any Notion source)
- **Price:** Free (GPL-3.0)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot code read @b5e97e7: safe with the fixes in Safe install. The bindings (src/) make no network calls; the only URL in src/ is the bug-report link in an error message (src/parselmouth.cpp:168). The package's only dependency is numpy (pyproject.toml). Verified behaviour and fixes: (1) parselmouth.praat.run and run_file execute Praat scripts (src/parselmouth/praat.cpp:454-477), and the Praat script language has runSystem, runSubprocess and runSystem_nocheck, which run shell commands (praat/sys/Formula.cpp:304, 4240-4259); fix: only run Praat scripts you or Claude wrote and read first, never a downloaded .praat script unread; for pitch and tone analysis use the Python API (Sound.to_pitch etc.) or praat.call with built-in commands, which need no script. (2) Version 0.4.6 fixed a vulnerability in Praat's bundled opusfile decoder (CHANGELOG.md, 0.4.6, issue #141); fix: pin 0.4.7 (current PyPI release, 2025-11-27), never older.; code you distribute that links it must be GPL.

## Safe install

Safe install (fixes applied): Claude Code on Windows: python -m venv parselmouth-env, activate it, then pip install --require-hashes -r req.txt where req.txt holds the line praat-parselmouth==0.4.7 with its PyPI wheel hash (Python 3.12: --hash=sha256:7cfd6941a4e8dd1d8398260f1269a831b84e9f230b03c569993e144a20704f99; Python 3.13: --hash=sha256:e3bfe1fc8d0f0252766978affa2e7f9b68876540688dfb9c56535fcaa2f4776a) plus a hashed numpy line (pip download numpy, then pip hash). Use the Python API (parselmouth.Sound(...).to_pitch()) or praat.call with built-in commands; only run Praat scripts (praat.run / run_file) that you wrote and read, because scripts can run shell commands. No keys; no network after install. claude.ai: not available (needs local Python). Hermes: same venv install. Android: nothing to install; show the pitch plots it produces as images in the PWA.

## YOLO install

YOLO (your own risk): skips the hash pin and the script rule. pip install praat-parselmouth (README).

## Install notes

Ask the user before adding it. Safe with the fixes in Safe install applied. Opt-in visual pitch/tone check for a project lessons, never scored.
Official docs: https://parselmouth.readthedocs.io/
