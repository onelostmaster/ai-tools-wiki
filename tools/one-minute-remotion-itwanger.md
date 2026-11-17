# one-minute-remotion (itwanger)

- **Type:** skill
- **Category:** generating videos, education
- **Official URL:** https://github.com/itwanger/one-minute-remotion
- **GitHub repo:** https://github.com/itwanger/one-minute-remotion @ 02dbfc4 (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-16)
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-16

## Safety reason

Not code-reviewed for safety. A project Tool Scout (Claude, 2026-11-16) read it: 3/5, idea to port its export check (frame count, decode errors, voice sync in 6 windows). Repo and commit confirmed from github.com metadata, 2026-11-16.

## Safe install

Unreviewed: contain it: do not use the -g flag (README:56 installs globally); git clone into a test skills folder pinned to commit 02dbfc4 and read the export check there, no keys added. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
README\:56-60\: `npx skills add itwanger/one-minute-remotion -g` (global install to all agents) or `-a claude-code -y`.
