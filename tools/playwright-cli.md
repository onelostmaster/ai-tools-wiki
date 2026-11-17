# Playwright CLI

- **Type:** CLI
- **Category:** developer tools, automation
- **Official URL:** https://playwright.dev
- **GitHub repo:** https://github.com/microsoft/playwright-cli @ 0a80807 (Apache-2.0; latest commit on 2026-10-31)
- **Price:** Free (Apache-2.0, `github.com`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (vendor README, 2026-10-31): safe. Official Microsoft product, Apache-2.0. It controls a real browser: it can click, type, upload your files and read cookies and localStorage of the pages it opens, so keep it off signed-in sessions you care about. Installed globally with `@latest` (unpinned).

## Safe install

Safe install (fixes applied):
Claude Code (Windows, local only): npm install -g @playwright/cli@0.1.24 (pinned; latest on npm 2026-11-16, instead of @latest in README line 26). This installs globally (npm -g); that cannot be avoided for the playwright-cli command. Then playwright-cli install --skills in your project (README line 38). Keep the default in-memory profile: it starts with no cookies and saves nothing to disk (README line 80); do not use --persistent or --profile=<path> (README lines 330-331), so it never sees your signed-in browser sessions.

## YOLO install

YOLO (your own risk): skips the version pin and the in-memory profile.
npm install -g @playwright/cli@latest, playwright-cli install --skills (README), and open --persistent or --profile pointed at your own browser profile.

## Install notes

Claude Code (local only): `npm install -g @playwright/cli@latest`, then `playwright-cli install --skills` (README).
