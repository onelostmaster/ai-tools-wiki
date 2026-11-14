# angr

- **Type:** library
- **Category:** security, 3D and games, developer tools
- **Official URL:** http://angr.io
- **GitHub repo:** https://github.com/angr/angr @ d816a4f (BSD-2-Clause)
- **Price:** Free, BSD-2-Clause (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (light code read @d816a4f, a review, 2026-11-02): safe. Only an optional local OpenTelemetry extra (`pyproject.toml:73`, `misc/telemetry.py:6-11`). The docs (installing.rst) have a curl | bash line: use pip.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `pip install angr` in a venv per its docs (not tested). Android: no.
