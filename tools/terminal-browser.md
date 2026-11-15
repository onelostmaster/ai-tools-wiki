# Terminal Browser

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/zenbu-labs/terminal-browser
- **GitHub repo:** [https://github.com/zenbu-labs/terminal-browser](https://github.com/zenbu-labs/terminal-browser) (read at ecc462f)
- **Price:** Free (MIT open-source code)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude code read @e459feb (2026-11-14): safe with fixes, Skip (no need). PostHog usage events and crash reports are on by default; off with DO_NOT_TRACK=1 or TERMINAL_BROWSER_NO_TELEMETRY=1 (shared/src/config/telemetry.ts:1, README telemetry section). Install with Homebrew (README:21) instead of the curl|bash script. The mod's agent tool stays off (default).

## Safe install

Safe install (fixes applied):
brew install terminal-browser (macOS/Linux; Windows only via WSL) with env DO_NOT_TRACK=1; leave the agent tool off.

## YOLO install

YOLO (your own risk): skips telemetry off and the script read.
curl -fsSL https://terminal-browser.sh/install | bash.

## Install notes

Ask the user before installing. brew install terminal-browser (macOS/Linux; Windows only via WSL) with env DO_NOT_TRACK=1; leave the agent tool off.
