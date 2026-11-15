# last30days skill

- **Type:** skill
- **Category:** research
- **Official URL:** https://github.com/mvanhorn/last30days-skill
- **GitHub repo:** [https://github.com/mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)
- **Price:** Free (open-source)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude code read @f087650 (2026-11-14): safe with fixes, Skip (value 1/5 stands). The X cookie read is now opt-in and has off switches: FROM_BROWSER=off makes cookie extraction return nothing (scripts/lib/env.py:1097-1101) and AGENTCOOKIE=off stops the agentcookie sidecar (scripts/lib/agentcookie.py:13-15). With both set, no browser cookie is read. Earlier avoid was for the cookie decryption.

## Safe install

Safe install (fixes applied):
Pin @f087650 and set env FROM_BROWSER=off, AGENTCOOKIE=off and BROWSER_CONSENT=false before the first run. Never run its setup with --allow-browser-cookies.

## YOLO install

YOLO (your own risk): skips the pin and the cookie switches, so it reads your browser's X cookies.
Install the latest skill as its README says and run setup with --allow-browser-cookies.

## Install notes

Ask the user before installing. Pin @f087650 and set env FROM_BROWSER=off, AGENTCOOKIE=off and BROWSER_CONSENT=false before the first run. Never run its setup with --allow-browser-cookies.
