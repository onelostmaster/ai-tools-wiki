# portal-coder-premium / portal-coder-mid profiles

- **Type:** plugin
- **Category:** Hermes add-ons, developer tools
- **Official URL:** https://github.com/notwitcheer/portal-coder-premium
- **GitHub repo:** [https://github.com/notwitcheer/portal-coder-premium (and https://github.com/notwitcheer/portal-coder-mid)](https://github.com/notwitcheer/portal-coder-premium)
- **Price:** Free config; Nous Portal model usage is paid (amount unknown)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a project a review, 2026-10-28): Looks safe. Pure config, no code. Heads-up: `config.yaml` `approvals.smart_policy` tells the approver that package installs and git push to feature branches are safe, so they auto-run without asking. Installing replaces that profile's config.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Hermes: `hermes profile install github.com/notwitcheer/portal-coder-premium --alias` (README:12). It replaces that profile's config; review the `approvals.smart_policy` line first (it auto-runs package installs and git push to feature branches).
