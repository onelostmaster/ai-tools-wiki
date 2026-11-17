# explainer-skill (jdrurka)

- **Type:** skill
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/jdrurka/explainer-skill
- **GitHub repo:** https://github.com/jdrurka/explainer-skill @ 56f95a6 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-16); Fish Audio voice is a separate paid service (price not checked)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-16

## Safety reason

Not code-reviewed for safety. A project Tool Scout (Claude, 2026-11-16) listed it but did not read or rate it (skipped by description). Repo and commit confirmed from github.com metadata, 2026-11-16.

## Safe install

Unreviewed: contain it: git clone into %USERPROFILE%\.claude\\skills\\explainer-video pinned to commit 56f95a6 (not npx -g), and use a separate Fish Audio key with a low spend cap in .env only, never in chat. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
README:20,42-49: needs a Fish Audio account and FISH_API_KEY in a .env file (paid third-party voice service; README links carry a referral tag). README\:26-38\: git clone into ~/.claude/skills/explainer-video or `npx skills add ... -g`, plus remotion-dev/skills.
