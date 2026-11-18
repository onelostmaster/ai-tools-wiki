# portal-coder-premium / portal-coder-mid profiles

- **Type:** plugin
- **Category:** Hermes add-ons, developer tools
- **Official URL:** https://github.com/notwitcheer/portal-coder-premium
- **GitHub repo:** [https://github.com/notwitcheer/portal-coder-premium (and https://github.com/notwitcheer/portal-coder-mid)](https://github.com/notwitcheer/portal-coder-premium)
- **Price:** Free config; Nous Portal model usage is paid (amount unknown)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read, a project a review, 2026-10-28): Looks safe. Pure config, no code. Heads-up: `config.yaml` `approvals.smart_policy` tells the approver that package installs and git push to feature branches are safe, so they auto-run without asking. Installing replaces that profile's config.

## Safe install

Safe install (fixes applied):
Hermes: hermes profile install github.com/notwitcheer/portal-coder-premium --alias (README:12) into a profile you do not already use, because installing replaces that profile's config. Then open its config.yaml and delete the approvals.smart_policy lines that mark package installs and git push to feature branches as safe (a review bot, a review), so Hermes asks before those.

## YOLO install

YOLO (your own risk): skips removing the smart_policy auto-approvals.
hermes profile install github.com/notwitcheer/portal-coder-premium --alias and keep its config.yaml as shipped (package installs and feature-branch pushes run without asking).

## Install notes

Hermes: `hermes profile install github.com/notwitcheer/portal-coder-premium --alias` (README:12). It replaces that profile's config; review the `approvals.smart_policy` line first (it auto-runs package installs and git push to feature branches).
