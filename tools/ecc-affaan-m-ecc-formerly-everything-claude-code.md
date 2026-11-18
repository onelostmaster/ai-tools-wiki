# ECC (affaan-m/ECC, formerly everything-claude-code)

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/affaan-m/ECC
- **GitHub repo:** https://github.com/affaan-m/ECC @ b38be6a (MIT; v2.2.3)
- **Price:** Free, MIT (github.com, checked 2026-11-02); ECC Tools app for private repos from $19 per seat a month per README.md:85 (unconfirmed on its site)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @3f14a10 v2.2.3 (2026-11-17): safe with fixes. 28 hooks on 8 events (hooks/hooks.json); the hook scripts make no network calls (scripts/hooks/). Hook profile defaults to standard (scripts/lib/hook-flags.js:7); minimal trims them and ECC_DISABLED_HOOKS turns single hooks off. scripts/auto-update.js pulls new code only when you run it. Fix: pin the commit, ECC_HOOK_PROFILE=minimal.

## Safe install

Safe install (fixes applied):
/plugin marketplace add affaan-m/ECC#3f14a10, /plugin install ecc@ecc; env ECC_HOOK_PROFILE=minimal; never run scripts/auto-update.js; read hooks/hooks.json before the first session.

## YOLO install

YOLO (your own risk): skips the pin and the minimal profile.
Install from main with all 28 hooks on the standard profile.

## Install notes

Ask the user before installing.
Claude Code: install only the parts you need per its README, after reading the hooks.
Hermes: has a Hermes hooks folder (not tested).
Windows: works in Claude Code on Windows (not tested). Android: no.
