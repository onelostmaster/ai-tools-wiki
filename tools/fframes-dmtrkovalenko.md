# fframes (dmtrKovalenko)

- **Type:** library
- **Category:** generating videos
- **Official URL:** https://github.com/dmtrKovalenko/fframes
- **GitHub repo:** https://github.com/dmtrKovalenko/fframes @ 49b7606 (MIT)
- **Price:** Free, MIT (github.com / crates.io, checked 2026-11-05)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-17

## Safety reason

Not code-reviewed for safety. A project Tool Scout (Claude, 2026-11-05) rated it ❌ ★1.5 for fit. Repo and commit confirmed from github.com metadata, 2026-11-05.

## Safe install

Safe install (fixes applied):
Unreviewed: contain it: read it on GitHub first (https://github.com/dmtrKovalenko/fframes @ 49b7606); if you try it, add it as a dependency pinned to that exact commit in a throwaway project inside a devcontainer or WSL sandbox (not your main Windows projects), no API keys in its env, and skip package install scripts (npm: --ignore-scripts). Get a review before real use. Android: no.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: the repo ships an agent skill via `npx skills add https://fframes.studio` (pin and review before running); Rust toolchain needed to build.
