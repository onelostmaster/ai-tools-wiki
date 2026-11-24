# Shotkit (whystrohm)

- **Type:** plugin
- **Category:** generating videos, editing
- **Official URL:** https://whystrohm.com/shotkit
- **GitHub repo:** https://github.com/whystrohm/shotkit @ da8edbf (Apache-2.0)
- **Price:** Free on GitHub, Apache-2.0 (github.com, checked 2026-11-23); fal generation is paid per job (price not checked)
- **Decision:** Later
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-23

## Safety reason

Not code-reviewed for safety. README: plugin installs with /plugin install shotkit --marketplace whystrohm/shotkit, or ./install.sh which puts tools at ~/.claude/shotkit-tools; Canvas is macOS-only, needs Python 3.10+ and a Claude API key (kept in the macOS Keychain); generation runs paid jobs on fal only after you approve the price; it fetches Google Fonts. Rendering uses Remotion (company use needs a Remotion license). Repo, license and latest commit confirmed from github.com metadata, 2026-11-23.

## Safe install

Unreviewed: contain it: install the plugin from the pinned commit da8edbf in a test project inside a devcontainer or sandbox, no fal or Claude API keys until reviewed, and skip Canvas (macOS only). Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: /plugin install shotkit --marketplace whystrohm/shotkit (older Claude Code: /plugin marketplace add whystrohm/shotkit then /plugin install shotkit@shotkit) (README). Canvas is Mac-only, so not for this user (Windows).
