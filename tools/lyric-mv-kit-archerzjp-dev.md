# lyric-mv-kit (archerzjp-dev)

- **Type:** skill
- **Category:** generating videos, voice and audio
- **Official URL:** https://github.com/archerzjp-dev/lyric-mv-kit
- **GitHub repo:** https://github.com/archerzjp-dev/lyric-mv-kit @ 18f5e6e (MIT code; docs under LICENSE-docs.md)
- **Price:** Free on GitHub, MIT for code (LICENSE file, checked 2026-11-21); Suno songs for commercial use need a paid Suno plan per the README (check suno.com)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-21

## Safety reason

Not code-reviewed for safety. README (18f5e6e) line 33/92: install.sh copies the skill and starter into ~/.claude/skills/ (all projects); line 17: npx hyperframes is fetched on demand. Unverified: install.sh, starter/tools/*.mjs and demo-audio.sh -> Contain: no install.sh, copy the skill into one project, pin hyperframes, no keys. Checked 2026-11-21.

## Safe install

Unreviewed: contain it: clone into a separate project folder on Windows, git checkout 18f5e6e, don't run install.sh (it targets all projects and is bash); copy skill/lyric-mv-director into that project's .claude\\skills\\ by hand, run starter tools only after reading them, use a pinned hyperframes version instead of bare npx hyperframes, add no API keys. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Contain it: clone into a separate project folder on Windows, git checkout 18f5e6e, don't run install.sh (it targets all projects and is bash); copy skill/lyric-mv-director into that project's .claude\\skills\\ by hand, run starter tools only after reading them, use a pinned hyperframes version instead of bare npx hyperframes, add no API keys.
