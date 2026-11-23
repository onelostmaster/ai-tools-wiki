# HookLab (CoolerGit)

- **Type:** skill
- **Category:** research, social posting
- **Official URL:** https://github.com/CoolerGit/HookLab
- **GitHub repo:** https://github.com/CoolerGit/HookLab @ 2cd09ae (Apache-2.0)
- **Price:** Free on GitHub, Apache-2.0 (GitHub API, checked 2026-11-22); needs paid Apify credits per fetch (README line 50; Apify price not checked: unknown)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-22

## Safety reason

Not code-reviewed for safety. README line 50: needs an Apify account and APIFY_TOKEN env var; Apify actors cost credits per run. README line 35: ingest.py fetches transcript, thumbnail and stats via Apify. Unverified: ingest.py -> Contain: separate folder, pinned commit. Checked 2026-11-22.

## Safe install

Unreviewed: contain it: clone into a separate project folder on Windows, git checkout 2cd09ae, read ingest.py and each SKILL.md first, put an Apify token with a spending limit only in that session (not setx), install Python packages in a venv, keep Claude Code's normal permission prompts on (never --dangerously-skip-permissions). Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Contain it: clone into a separate project folder on Windows, git checkout 2cd09ae, read ingest.py and each SKILL.md first, put an Apify token with a spending limit only in that session (not setx), install Python packages in a venv, keep Claude Code's normal permission prompts on (never --dangerously-skip-permissions).
