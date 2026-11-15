# oh-my-hermes

- **Type:** plugin
- **Category:** Hermes add-ons
- **Official URL:** https://github.com/rlaope/oh-my-hermes
- **GitHub repo:** [https://github.com/rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes)
- **Price:** Free (open-source code)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

Claude targeted read @7907622 (2026-11-14; too big to read fully): safe with fixes. The installer pulls the latest release wheel with no checksum; pin it with OMH_VERSION (install.sh:11-12). Update check off with omh update-check set --mode off (docs/INSTALLATION.md:543). Unverified: the full plugin hook code -> Contain: test in one spare Hermes profile first. Leave omh_jev_ask off (sends questions plus key to a third party).

## Safe install

Safe install (fixes applied):
Download install.sh from commit 7907622, read it, run OMH_VERSION=4.0.7 sh install.sh; then omh update-check set --mode off; first in a spare Hermes profile; don't enable omh_jev_ask.

## YOLO install

YOLO (your own risk): skips the pin, script read and test profile.
curl -fsSL https://omher.app/install | sh with the auto update mode.

## Install notes

Ask the user before installing. Download install.sh from commit 7907622, read it, run OMH_VERSION=4.0.7 sh install.sh; then omh update-check set --mode off; first in a spare Hermes profile; don't enable omh_jev_ask.
