# pyloudnorm

- **Type:** library
- **Category:** voice and audio
- **Official URL:** https://github.com/csteinmetz1/pyloudnorm
- **GitHub repo:** https://github.com/csteinmetz1/pyloudnorm @ b8d67bf (2026-01-04, v0.2.0, MIT)
- **Price:** Free (MIT, per PyPI)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot: Looks safe. Pure numeric code, 509 lines in pyloudnorm/ (meter.py, iirfilter.py, normalize.py, util.py) importing only numpy, scipy.signal, warnings and textwrap; no network, file writes, subprocess, eval/exec, pickle, telemetry or hooks. Runtime dependencies are only scipy and numpy (`pyproject.toml:21-24`). Not used for loudness: Claude rejected it for accuracy (a mono downmix read about 3 dB too quiet), not safety.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: inside the project's virtual environment `pip install pyloudnorm==0.2.0` (the reviewed v0.2.0, b8d67bf). Pure numeric code with no network or file writes (pyloudnorm/ read in full), so no other fix is needed. Android: not used.

## YOLO install

YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install pyloudnorm`

## Install notes

Claude Code: `pip install pyloudnorm` (PyPI)
