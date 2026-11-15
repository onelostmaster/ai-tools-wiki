# Claude Quickstarts

- **Type:** library
- **Category:** developer tools, agents, coding
- **Official URL:** https://github.com/anthropics/claude-quickstarts
- **GitHub repo:** https://github.com/anthropics/claude-quickstarts @ 4a4224b (MIT; official Anthropic repo, not a fork, not archived; default-branch commit 2026-11-06 14:37 ET; 20,919 stars at check)
- **Price:** Sample code is free, MIT (LICENSE, checked 2026-11-14). Running the samples requires a Claude API key billed on Anthropic's published API rates (README.md:8-10; official pricing at platform.claude.com/docs/en/about-claude/pricing, checked 2026-11-14).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot: safe with the Install notes fixes. Official Anthropic MIT sample code, not a product; API use is billed (README.md:8-10). Verified risks, each fixed: computer-use agents follow on-page instructions (computer-use-demo/README.md:6-16; fix: run only its Docker container, sign in to nothing); the browser demo launches Chromium with --no-sandbox (browser-use-demo/browser_use_demo/tools/browser.py:266-274; fix: run it only in its Docker Compose container, browser-use-demo/README.md:3,31); the Docker demo mounts $HOME/.anthropic and the key (computer-use-demo README.md:51-58; fix: mount nothing else, key only in ANTHROPIC_API_KEY); Managed Agents samples need 30-day retention and are not zero-data-retention (managed-agents/copilot-kit-ag-ui/README.md:18, knowledge-wiki notebook :84; fix: skip them for data that must not be kept). computer-use-best-practices is native macOS only (README.md:26): skip it.

## Safe install

Safe install (fixes applied):
Windows/Claude Code: clone or download the official repo pinned at commit `4a4224b`. Run only the Docker samples (`computer-use-demo`, and `browser-use-demo` with Docker Compose). Pass the key only as `ANTHROPIC_API_KEY`. Mount no other host folders, and sign the agent in to no accounts. Set `DO_NOT_TRACK=1`. Skip `computer-use-best-practices` (macOS only) and the Managed Agents samples when data must not be retained for 30 days. Use the shared settings file github.com/onelostmaster/skills-wiki/blob/main/safe-defaults/claude-settings.json.

## YOLO install

YOLO (your own risk): skips the commit pin, Docker isolation, the no-extra-mounts rule, and skipping Managed Agents and macOS-native samples.
Clone https://github.com/anthropics/claude-quickstarts and follow each sample's README, including the `docker run` that mounts `$HOME/.anthropic` (computer-use-demo/README.md:51-58).

## Install notes

Ask the user before installing or spending API credit. Windows: run only the Docker samples (computer-use-demo, browser-use-demo with Docker Compose); pass the key only as the env var `ANTHROPIC_API_KEY`, mount no other host folders, and sign the agent in to no accounts. Skip computer-use-best-practices (macOS only) and the Managed Agents samples when data must not be retained for 30 days. Android: no. Hermes compatibility untested.
