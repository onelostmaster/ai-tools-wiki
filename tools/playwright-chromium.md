# Playwright + Chromium

- **Type:** library
- **Category:** building a site, developer tools
- **Official URL:** https://playwright.dev
- **GitHub repo:** [https://github.com/microsoft/playwright](https://github.com/microsoft/playwright) (Microsoft; per its npm listing, 2026-10-31); Python package: [https://github.com/microsoft/playwright-python](https://github.com/microsoft/playwright-python) (per PyPI)
- **Price:** Free (Apache-2.0, per npm and PyPI)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

Claude (a project tool scout, 2026-10-31): safe ('Yes: local'). Runs locally in the project container to test a project app; no risks recorded. a review bot listed Playwright among official apps it did not audit .

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `pip install playwright` (PyPI), then `playwright install` to download the browsers (official Playwright docs); in the a project container, installs last one session.
