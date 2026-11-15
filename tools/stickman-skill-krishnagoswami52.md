# stickman-skill (krishnagoswami52)

- **Type:** skill
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/krishnagoswami52/stickman-skill
- **GitHub repo:** https://github.com/krishnagoswami52/stickman-skill @ d3f9321 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-14)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-14

## Safety reason

Not code-reviewed for safety. A project Tool Scout (Claude, 2026-11-14) rated it ⏳ ★2 (idea only). Repo and commit confirmed from github.com metadata, 2026-11-14.

## Safe install

Unreviewed: contain it: make a venv first (`py -m venv .venv` then `.venv\Scripts\activate`) so doctor.py installs into it and never into the system Python (doctor.py:6-21); have ffmpeg on PATH; pin commit d3f9321; no keys needed. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
On first use scripts/doctor.py pip-installs numpy, scipy, pillow, playwright (and imageio-ffmpeg when ffmpeg is missing) into the current Python, retrying with --user and then --break-system-packages (doctor.py:6-21), and runs `playwright install chromium` when Chromium is missing (doctor.py:24-33).
