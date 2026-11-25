# yumurta-stili (kodlaciz)

- **Type:** skill
- **Category:** generating videos
- **Official URL:** https://github.com/kodlaciz/yumurta-stili
- **GitHub repo:** https://github.com/kodlaciz/yumurta-stili @ 0f66ed7 (MIT; reference frames in referans/ excluded)
- **Price:** Free on GitHub, MIT except referans/ (github.com, checked 2026-11-24)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-24

## Safety reason

Not code-reviewed for safety. README: needs Node 18+, Python 3.10+, ffmpeg and Google Chrome (or CHROME_PATH); setup is cd engine && npm install and pip install -r requirements.txt; install by copying the folder to ~/.claude/skills/yumurta-stili/. The reference frames in referans/ belong to their owners and are not MIT; README says use the reference videos only for study and do not republish them. Repo, license and latest commit confirmed from github.com metadata, 2026-11-24.

## Safe install

Unreviewed: contain it: clone at the pinned commit 0f66ed7 inside a devcontainer or sandbox, Python packages in a venv there, no API keys (it needs none), network on only for npm and pip; do not publish anything from referans/ (not MIT). Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: copy the repo folder to ~/.claude/skills/yumurta-stili/, then cd engine && npm install and pip install -r requirements.txt (README). Codex and other agents start from AGENTS.md.
