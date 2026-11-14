# Playwright CLI

- **Type:** CLI
- **Category:** developer tools, automation
- **Official URL:** https://playwright.dev
- **GitHub repo:** https://github.com/microsoft/playwright-cli @ 0a80807 (Apache-2.0; latest commit on 2026-10-31)
- **Price:** Free (Apache-2.0, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-10-31

## Safety reason

a review bot (vendor README, 2026-10-31): safe. Official Microsoft product, Apache-2.0. It controls a real browser: it can click, type, upload your files and read cookies and localStorage of the pages it opens, so keep it off signed-in sessions you care about. Installed globally with `@latest` (unpinned).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code (local only): `npm install -g @playwright/cli@latest`, then `playwright-cli install --skills` (README).
