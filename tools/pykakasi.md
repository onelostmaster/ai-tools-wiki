# pykakasi

- **Type:** library
- **Category:** a project
- **Official URL:** https://pykakasi.readthedocs.io/
- **GitHub repo:** https://codeberg.org/miurahr/pykakasi @ 4f26c75 (GPL-3.0-or-later; last commit 2024-12-06; PyPI 2.3.0 from 2024-06-24; official source per PyPI, not GitHub)
- **Price:** Free, GPL-3.0-or-later (pypi.org, checked 2026-11-03)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

No network, subprocess or eval in the package; pickle loads only its own dictionaries built from bundled data at build time (`src/pykakasi/kanji.py:76,102`, `src/pykakasi/scripts.py:293`, `setup.py` build step). Dependencies jaconv and deprecated. Maintenance mode: no release since 2.3.0 (2024-06).

## Safe install

Safe install (fixes applied):
Windows/Claude Code: inside the project's virtual environment `pip install pykakasi==2.3.0` (the reviewed release; offline after install, no key). Android: not used.

## YOLO install

YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install pykakasi`

## Install notes

Safe, but ask the user before installing.
Windows / Claude Code: `pip install pykakasi` (offline after install, no key). a project installs it per session for verify_genki.py. Android: no.
