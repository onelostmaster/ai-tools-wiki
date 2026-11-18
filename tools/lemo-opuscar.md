# lemo-opuscar

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/lemomo-ai/lemo-opuscar
- **GitHub repo:** [https://github.com/lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)
- **Price:** Free (open-source code)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a review, 2026-10-29): Looks safe. No telemetry, exfiltration or obfuscation; installs only playwright-core, three and Python audio libs; `setup.sh` auto-updates from unpinned main.

## Safe install

Safe install (fixes applied):
Claude Code: git clone https://github.com/lemomo-ai/lemo-opuscar.git, cd lemo-opuscar, git checkout the commit you reviewed, then open it with claude (README:78-80). Do not run setup.sh as shipped: it pulls updates from unpinned main on each run ; install its playwright-core, three and Python audio packages yourself at fixed versions instead.

## YOLO install

YOLO (your own risk): skips the commit pin and skipping setup.sh.
git clone https://github.com/lemomo-ai/lemo-opuscar.git && cd lemo-opuscar && claude, and run setup.sh as shipped (auto-updates from main).

## Install notes

Claude Code: `git clone https://github.com/lemomo-ai/lemo-opuscar.git && cd lemo-opuscar && claude` (README:78-80, per a review bot). Note that `setup.sh` auto-updates from unpinned main.
