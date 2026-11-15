# PySceneDetect

- **Type:** library
- **Category:** editing, research
- **Official URL:** https://www.scenedetect.com
- **GitHub repo:** [https://github.com/Breakthrough/PySceneDetect](https://github.com/Breakthrough/PySceneDetect) (confirmed via the PyPI package scenedetect, 2026-10-31)
- **Price:** Free (BSD-3-Clause, per PyPI)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude (a project tool scout, 2026-10-30): safe ('Yes'). Version 0.7.2 runs locally in `pipeline/audit_video.py` for cut and shot-length QA; no risks recorded.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: inside the project's virtual environment `pip install scenedetect==0.7.2` (the version a project uses). Android: not used.

## YOLO install

YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install --upgrade scenedetect`

## Install notes

Claude Code: `pip install --upgrade scenedetect` (PyPI; it suggests `scenedetect-headless` for servers). a project uses 0.7.2.
