# vite-plugin-pwa

- **Type:** library
- **Category:** building a site
- **Official URL:** https://github.com/vite-pwa/vite-plugin-pwa
- **GitHub repo:** [https://github.com/vite-pwa/vite-plugin-pwa](https://github.com/vite-pwa/vite-plugin-pwa) (confirmed via the npm package vite-plugin-pwa, 2026-10-31)
- **Price:** Free (MIT)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot code read @355cf3d: safe with the fixes in Safe install. No network calls, no child processes, no telemetry and no install hooks: package.json scripts have no preinstall/install/postinstall (prepack runs only when the authors publish); npm publish uses provenance (package.json publishConfig).; src/plugins/dev.ts:160-170,255-259). Verified behaviour and fixes: (1) runtime dependencies use ^ ranges (debug, pretty-bytes, tinyglobby, workbox-build, workbox-window in package.json); fix: pin vite-plugin-pwa@2.0.0 and install with the lockfile (npm ci). (2) The generated service worker caches the built site in the visitor's browser; with the default registerType 'prompt' (src/options.ts:50) the new version loads only after the user accepts the update prompt, with 'autoUpdate' it reloads on its own; fix: keep 'prompt' or show the reload toast, and use selfDestroying: true (src/modules.ts:55-71) to remove a broken worker and clear its caches. No fix needed beyond these; Node 20.19+ required (package.json engines).

## Safe install

Safe install (fixes applied): Claude Code on Windows, inside an existing Vite project: npm i -D vite-plugin-pwa@2.0.0 --save-exact, commit package-lock.json and use npm ci afterwards; add VitePWA(\{ registerType: 'prompt' \}) to vite.config; leave devOptions off unless testing the worker (it then writes a dev-dist folder; add it to .gitignore). Needs Node 20.19+. If a deployed worker misbehaves, ship once with selfDestroying: true to remove it and its caches. claude.ai: no (build tool). Hermes: no (not an agent tool). Android: the built app installs from Chrome as a PWA (Add to home screen); nothing to install for the plugin itself.

## YOLO install

YOLO (your own risk): skips the exact version pin, the lockfile install and the update prompt. npm i vite-plugin-pwa -D (README), then VitePWA(\{ registerType: 'autoUpdate' \}).

## Install notes

Ask the user before installing. Safe with the fixes in Safe install applied. Dev dependency of a Vite web project only; it runs at build time and adds a web manifest and service worker (offline use, installable on Android).
