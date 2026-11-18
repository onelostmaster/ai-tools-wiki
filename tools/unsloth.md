# Unsloth

- **Type:** library
- **Category:** developer tools
- **Official URL:** https://unsloth.ai
- **GitHub repo:** https://github.com/unslothai/unsloth @ 1c23549 (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (light code read @1c23549, a review, 2026-11-02): caution. README installs with curl | sh or irm | iex (`README.md:64,69`). On load it downloads a small file from Hugging Face to count your environment; off with UNSLOTH_DISABLE_STATISTICS (`unsloth/models/_utils.py:5183,5233-5237`).

## Safe install

Safe install (fixes applied):
Windows: in a venv, uv pip install unsloth==<release matching 1c23549> --torch-backend=auto (NVIDIA GPU); do not use the README's curl | sh or irm | iex installer (README.md:64,69). Set the user env var UNSLOTH_DISABLE_STATISTICS=1 before first use; otherwise each load downloads a small file from Hugging Face to count your environment (unsloth/models/_utils.py:5183,5233-5237). Android: no.

## YOLO install

YOLO (your own risk): skips the version pin, the script-installer ban and UNSLOTH_DISABLE_STATISTICS.
Windows: irm | iex installer from the README; the load-time stats download stays on.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: `uv pip install unsloth --torch-backend=auto` (README), not the script installer; NVIDIA GPU; set UNSLOTH_DISABLE_STATISTICS=1. Android: no.
