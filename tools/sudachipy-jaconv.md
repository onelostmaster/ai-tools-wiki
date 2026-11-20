# SudachiPy + jaconv

- **Type:** library
- **Category:** a project
- **Official URL:** https://github.com/WorksApplications/sudachi.rs
- **GitHub repo:** [https://github.com/WorksApplications/sudachi.rs](https://github.com/WorksApplications/sudachi.rs) (SudachiPy's current home, per PyPI); [https://github.com/ikegami-yukino/jaconv](https://github.com/ikegami-yukino/jaconv) (per PyPI)
- **Price:** Free (Apache-2.0, MIT; confirmed on PyPI)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

a review bot code read: safe with the fixes in Safe install. No network code at runtime: the Rust core (sudachi/Cargo.toml dependencies) and the bindings (python/Cargo.toml: pyo3, scopeguard, thread_local) have no HTTP or socket crate, and python/py_src has no urllib, requests, socket or subprocess use; the dictionary is found by importing the installed sudachidict_core package (python/py_src/sudachipy/__init__.py:44-55). jaconv is pure string conversion that imports only unicodedata, warnings and re (jaconv/jaconv.py:4-8, conv_table.py:4). Verified behaviour and fixes: (1) a Sudachi config file can name plugins by library path, and any plugin name that is not a bundled com.worksap.nlp.sudachi.* plugin is loaded as a native library (sudachi/src/plugin/loader.rs:127-141, 170); fix: use the default config (Dictionary() with no config_path) or a config you wrote, never a downloaded sudachi.json. (2) The sudachidict_core sdist's setup.py downloads the dictionary zip from a CloudFront URL with no hash check when pip builds from source (setup.py:30-51); fix: install wheels only with hashes (--only-binary=\:all\: --require-hashes), so setup.py never runs. Licenses: SudachiPy and the dictionary Apache-2.0, jaconv MIT.

## Safe install

Safe install (fixes applied): Claude Code on Windows (Python 3.10 or newer): python -m venv sudachi-env, activate it, then pip install --only-binary=\:all\: --require-hashes -r req.txt where req.txt holds: sudachipy==0.7.0 --hash=sha256:8d0429db2d02d408daa7dccd062a6d8c2984a07f8e448b49a3ea694377617658 (win_amd64 wheel), sudachidict_core==20261015 --hash=sha256:6d7774b518e64c88a0578975d569590b3dae3b3c834f166486aa611879ee9d98 (wheel), jaconv==0.5.0 --hash=sha256:2914114fe761ca49fc7089e25e6ad4a400c26f262ffce84e13b176916b71610a (wheel) (PyPI, checked 2026-11-19). Use sudachipy.Dictionary() with the default config, or a config you wrote; never load a downloaded sudachi.json, because configs can load native plugin libraries. No keys; no network after install. claude.ai: not available (needs local Python). Hermes: same venv install. Android: nothing to install; the readings it produces go into the cards.

## YOLO install

YOLO (your own risk): skips the wheel-only hash pin. pip install sudachipy sudachidict_core jaconv (PyPI; the dictionary package is about 77 MB).

## Install notes

Ask the user before adding it. Safe with the fixes in Safe install applied. Batch Japanese readings (furigana, kana conversion) for a project card generation.
Official docs: https://worksapplications.github.io/sudachi.rs/python/
