# keeran.ai skills (kjagsadvisors)

- **Type:** skill
- **Category:** generating videos, editing, social posting
- **Official URL:** https://github.com/kjagsadvisors/keeran.ai
- **GitHub repo:** https://github.com/kjagsadvisors/keeran.ai @ 3135813 (MIT)
- **Price:** Free on GitHub, MIT (github.com, checked 2026-11-18); context.dev is a separate service (price not checked)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-18

## Safety reason

Not code-reviewed for safety. README: the link-edit and reverse-video skills scrape sites and reels through context.dev (a third-party service); match-frame uses Blender. Repo, license and latest commit confirmed from github.com metadata, 2026-11-18.

## Safe install

Unreviewed: contain it: copy only the one skill folder you want from the pinned commit 3135813 into a test project's .claude\\skills\\ (not your user-wide folder), give it no API keys until reviewed, and skip the context.dev skills (link-edit, reverse-video) so nothing goes to that service. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: copy one skill folder into %USERPROFILE%\.claude\\skills\\ (or <project>\.claude\\skills\) and follow that skill's README for its one-time setup (README).
