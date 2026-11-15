# librosa

- **Type:** library
- **Category:** voice and audio, research
- **Official URL:** https://librosa.org
- **GitHub repo:** [https://github.com/librosa/librosa](https://github.com/librosa/librosa) (not in the Notion source; confirmed on PyPI, 2026-10-31)
- **Price:** Free (ISC, per PyPI, checked 2026-10-31)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude (a project tool scout, read before use, v1.0.0, 2026-10-30): safe. Local Python audio-analysis library used to check whether cuts land on the beat; no network or telemetry finding recorded.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: inside the project's virtual environment `pip install librosa==1.0. Android: not used.

## YOLO install

YOLO (your own risk): skips the virtual environment and the exact pin.
`pip install librosa`

## Install notes

Claude Code: `pip install librosa` (PyPI, checked 2026-10-31). In a project it runs inside `pipeline/audit_video.py`.
