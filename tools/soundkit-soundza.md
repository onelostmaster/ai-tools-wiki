# SoundKit (Soundza)

- **Type:** skill
- **Category:** voice and audio, generating videos
- **Official URL:** https://soundza.com/soundkit
- **GitHub repo:** https://github.com/soundza/soundkit @ 6d59c27 (code MIT, audio CC0)
- **Price:** Free on GitHub, MIT code + CC0 audio (github.com, checked 2026-11-25); Soundza account features: price unknown
- **Decision:** Later
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-25

## Safety reason

Not code-reviewed for safety. README: sounds install with npx shadcn add @soundza/<name> (or the full soundza.com/r/<name>.json URL); music beds print a curl download into public/sounds/; skill installs with npx skills add soundza/soundkit; the helper (Node 18+) has signin, search, add and generate commands against the wider Soundza library, whose sounds come under the Soundza License (not CC0). Repo, license and latest commit confirmed from github.com metadata, 2026-11-25.

## Safe install

Unreviewed: contain it: use only the CC0 files from registry/soundza/sounds/ at the pinned commit 6d59c27 inside a devcontainer or sandbox project; skip the helper's signin and generate commands (they need a Soundza account); network on only for the shadcn/curl downloads. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: npx skills add soundza/soundkit (README). Single sound: npx shadcn add @soundza/air-whoosh in a Remotion project.
