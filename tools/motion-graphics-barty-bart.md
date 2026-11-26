# motion-graphics (Barty-Bart)

- **Type:** skill
- **Category:** generating videos, editing, voice and audio
- **Official URL:** https://github.com/Barty-Bart/motion-graphics
- **GitHub repo:** https://github.com/Barty-Bart/motion-graphics @ 3d83d98 (MIT per LICENSE)
- **Price:** Free on GitHub, MIT; bundled sounds CC0 (github.com, checked 2026-11-25)
- **Decision:** Later
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-25

## Safety reason

Not code-reviewed for safety. README: install with npx skills add Barty-Bart/motion-graphics. skills/sound-effects/SKILL.md: the default kit is bundled CC0 .ogg files; the typing sound (Mixkit #1392) is downloaded at runtime into <out>/sound-effects-cache/ under the Mixkit licence (not CC0, do not commit it). Repo, license and latest commit confirmed from github.com metadata, 2026-11-25.

## Safe install

Unreviewed: contain it: copy only skills/sound-effects from the pinned commit 3d83d98 into a devcontainer or sandbox project, no API keys (it needs none), network off except the one Mixkit typing download; keep Mixkit files out of anything you publish or commit. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: npx skills add Barty-Bart/motion-graphics (README); or copy one skill folder (e.g. skills/sound-effects) to ~/.claude/skills/.
