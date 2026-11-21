# VBASE (ekanshvcpkg)

- **Type:** plugin
- **Category:** editing
- **Official URL:** https://github.com/ekanshvcpkg/VBASE
- **GitHub repo:** https://github.com/ekanshvcpkg/VBASE @ a7163f1 (MIT)
- **Price:** Free on GitHub, MIT (LICENSE file, checked 2026-11-20); ElevenLabs music and voice optional and off without a key (README); Remotion licence free for individuals and small teams
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-20

## Safety reason

Not code-reviewed for safety. Unverified: scripts/setup.sh, which README says installs ffmpeg, Node, uv, auto-editor, Python 3.11 tools and models (about 5 GB) -> Contain: WSL2 or devcontainer, pinned commit, read setup.sh before running, no ElevenLabs key. Commit and LICENSE confirmed on github.com, 2026-11-20.

## Safe install

Unreviewed: contain it: run it in WSL2 or a devcontainer, not on bare Windows; clone and git checkout a7163f1 instead of the marketplace install, read scripts/setup.sh before /vbase:setup (it installs about 5 GB of tools and models), add no ElevenLabs key, keep Claude Code's normal permission prompts on (never --dangerously-skip-permissions). Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Contain it: run it in WSL2 or a devcontainer, not on bare Windows; clone and git checkout a7163f1 instead of the marketplace install, read scripts/setup.sh before /vbase:setup (it installs about 5 GB of tools and models), add no ElevenLabs key, keep Claude Code's normal permission prompts on (never --dangerously-skip-permissions).
