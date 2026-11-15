# UI SDK (vercel-labs/ui)

- **Type:** library
- **Category:** design, building a site, developer tools
- **Official URL:** https://ui-sdk.dev
- **GitHub repo:** https://github.com/vercel-labs/ui @ adc59ce (Apache-2.0)
- **Price:** Free, Apache-2.0 (beta under Vercel beta terms)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude code read (light) @adc59ce, 2026-11-14: zero runtime dependencies, no network calls in packages/*/src; beta 0.1.0-beta.2, first on npm 2026-11-12; the no-bundler Artifact route loads https://ui-sdk.dev/web.js from Vercel's site, so pin web@0 or self-host. Not code-read by a review bot.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: when needed, in the project folder `npm install --ignore-scripts @ui-sdk/react@0.1.0-beta.2 @ui-sdk/core@0.1.0-beta.2` (or the vue/svelte/solid/web adapter at the same pin). If you use the no-bundler Artifact route, pin `@ui-sdk/web@0` or self-host `web.js`; do not load unpinned https://ui-sdk.dev/web.js. Set `DO_NOT_TRACK=1`. Prefer copying the skill from a clone at `adc59ce` over an unpinned `npx skills add`. Use the shared settings file github.com/onelostmaster/skills-wiki/blob/main/safe-defaults/claude-settings.json. Re-review before bumping the pin.

## YOLO install

YOLO (your own risk): skips the pin, --ignore-scripts, and the pin-or-self-host rule for web.js.
`npm install @ui-sdk/react @ui-sdk/core` (or the adapter) and `npx skills add vercel-labs/ui --skill ui-sdk` (README).

## Install notes

None now. When needed: npm install @ui-sdk/react @ui-sdk/core (or the vue/svelte/solid/web adapter) inside that project, pinned; agent skill: npx skills add vercel-labs/ui --skill ui-sdk (per the README). Ask the user before installing.
