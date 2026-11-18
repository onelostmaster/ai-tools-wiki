# Puppeteer

- **Type:** library
- **Category:** automation, developer tools
- **Official URL:** https://pptr.dev
- **GitHub repo:** unknown
- **Price:** Free (Apache-2.0, per npm, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-17

## Safety reason

Puppeteer (official npm package; not code-reviewed: a review bot listed it under 'not audited: official apps, CLIs or connectors', a project a review, 2026-10-31): safe. `npm i puppeteer` runs a postinstall script that downloads Chrome for Testing (npm, `pptr.dev`). a review bot's Bang Motion review (#68) flagged that tool's unpinned puppeteer ^25 with no lockfile.

## Safe install

Safe install (fixes applied):
Claude Code: npm i puppeteer@<exact version from npm> --save-exact and commit package-lock.json (fixes the unpinned ^25/no-lockfile problem a review bot flagged in #68). The install downloads Chrome for Testing into ~/.cache/puppeteer (pptr.dev); to control that, use npm i puppeteer-core@<version> --save-exact and run npx puppeteer browsers install chrome yourself.

## YOLO install

YOLO (your own risk): skips the exact pin and lockfile.
npm i puppeteer (pptr.dev).

## Install notes

Claude Code: `npm i puppeteer` (`pptr.dev`); it downloads Chrome for Testing into `~/.cache/puppeteer` during install. `npm i puppeteer-core` skips the browser download; if install scripts are blocked, run `npx puppeteer browsers install`.
