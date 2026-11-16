# SudachiPy + jaconv

- **Type:** library
- **Category:** a project
- **Official URL:** https://github.com/WorksApplications/sudachi.rs
- **GitHub repo:** [https://github.com/WorksApplications/sudachi.rs](https://github.com/WorksApplications/sudachi.rs) (SudachiPy's current home, per PyPI); [https://github.com/ikegami-yukino/jaconv](https://github.com/ikegami-yukino/jaconv) (per PyPI)
- **Price:** Free (Apache-2.0, MIT; confirmed on PyPI)
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-14

## Safety reason

Not code-reviewed. Open-source Japanese libraries on PyPI: SudachiPy (Works Applications' morphological analyzer, Apache-2.0) and jaconv (kana converter, MIT). Claude's a project scout (2026-10-31) listed them under Later with no safety check.

## Safe install

Unreviewed: contain it: inside a project container or a Python venv only, `pip install sudachipy==0.7.0 sudachidict_core==20261015 jaconv==0.5.0` (latest on PyPI 2026-11-14; SudachiPy needs Python >= 3.10; the core dictionary package is about 77 MB), pinned in requirements.txt, no API keys in that environment, network only while installing. unverified: whether either library makes network calls at runtime. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: `pip install sudachipy sudachidict_core jaconv` (PyPI; the core dictionary is about 77 MB, and PyPI says SudachiPy 0.7.x is unstable, so pin the exact version)
