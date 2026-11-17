# OpenMontage

- **Type:** app
- **Category:** generating videos
- **Official URL:** https://github.com/calesthio/OpenMontage
- **GitHub repo:** [https://github.com/calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) (not in any Notion source; a web search names it the original repo, checked 2026-10-31)
- **Price:** Free (open source); license unconfirmed (not in any Notion source)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude targeted read @2e003e6 (2026-11-16; large repo): safe with fixes, Skip (a project has its own pipeline). AGPL-3.0 (LICENSE). No telemetry, curl|bash or shell=True found in the code. Paid model tools take a --max-credits cap and config.yaml has a budget block (line 9). Fix: set the budget before the first run and keep keys in .env.

## Safe install

Safe install (fixes applied):
Clone at 2e003e6; set the budget in config.yaml before the first run; API keys in .env, never in chat; npm install (not -g) inside remotion-composer.

## YOLO install

YOLO (your own risk): skips the budget, so paid tools run uncapped.
Clone and run as the README says.

## Install notes

Ask the user before installing. Clone at 2e003e6; set the budget in config.yaml before the first run; API keys in .env, never in chat; npm install (not -g) inside remotion-composer.
