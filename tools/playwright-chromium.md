# Playwright + Chromium

- **Type:** library
- **Category:** building a site, developer tools
- **Official URL:** https://playwright.dev
- **GitHub repo:** [https://github.com/microsoft/playwright](https://github.com/microsoft/playwright) (Microsoft; per its npm listing, 2026-10-31); Python package: [https://github.com/microsoft/playwright-python](https://github.com/microsoft/playwright-python) (per PyPI)
- **Price:** Free (Apache-2.0, per npm and PyPI)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude (a project tool scout, 2026-10-31): safe ('Yes: local'). Runs locally in the project container to test a project app; no risks recorded. a review bot listed Playwright among official apps it did not audit .

## Safe install

Safe install (fixes applied):
Claude Code (Windows): `py -m venv .venv`, `.venv\Scripts\pip install playwright==1.65.2` (PyPI latest, checked 2026-11-14), then `.venv\Scripts\playwright install chromium` so only Chromium downloads, not every browser (Playwright docs: `playwright install <browser>`). a project container: same commands inside the container; they last one session.

## YOLO install

YOLO (your own risk): skips the venv and version pin, and downloads every browser.
pip install playwright
playwright install

## Install notes

Claude Code: `pip install playwright` (PyPI), then `playwright install` to download the browsers (official Playwright docs); in the a project container, installs last one session.
