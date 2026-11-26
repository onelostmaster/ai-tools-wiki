# Content Skills (Blotato)

- **Type:** plugin
- **Category:** generating videos, editing, social posting
- **Official URL:** https://www.blotato.com/contentskills
- **GitHub repo:** https://github.com/blotato/contentskills @ d137fbf (AGPL-3.0-only)
- **Price:** Free on GitHub, AGPL-3.0 (github.com, checked 2026-11-25); kie.ai footage is a separate paid service (price not checked)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-25

## Safety reason

Not code-reviewed for safety. README: install with /plugin install contentskills --marketplace blotato/contentskills; setup runs npm run setup, which downloads voice and transcription models, Python environments and a headless browser into .tools/, writes your name and handle to settings/user.json and opens a local dashboard; optional generate step calls paid kie.ai. AGPL-3.0-only. Repo, license and latest commit confirmed from github.com metadata, 2026-11-25.

## Safe install

Unreviewed: contain it: clone at the pinned commit d137fbf inside a devcontainer or sandbox, run npm run setup there, no kie.ai key (footage generation is optional), network on only for setup downloads. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: /plugin install contentskills --marketplace blotato/contentskills, then "setup blotato/contentskills" (README).
