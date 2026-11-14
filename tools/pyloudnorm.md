# pyloudnorm

- **Type:** library
- **Category:** voice and audio
- **Official URL:** https://github.com/csteinmetz1/pyloudnorm
- **GitHub repo:** https://github.com/csteinmetz1/pyloudnorm @ b8d67bf (2026-01-04, v0.2.0, MIT)
- **Price:** Free (MIT, per PyPI)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read @b8d67bf, v0.2. Pure numeric code, 509 lines in pyloudnorm/ (meter.py, iirfilter.py, normalize.py, util.py) importing only numpy, scipy.signal, warnings and textwrap; no network, file writes, subprocess, eval/exec, pickle, telemetry or hooks. Runtime dependencies are only scipy and numpy (`pyproject.toml:21-24`). Not used for loudness: Claude rejected it for accuracy (a mono downmix read about 3 dB too quiet), not safety.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `pip install pyloudnorm` (PyPI)
