# Cua Spaces plugin

- **Type:** plugin
- **Category:** Hermes add-ons, automation
- **Official URL:** https://github.com/trycua/hermes-cua-spaces
- **GitHub repo:** [https://github.com/trycua/hermes-cua-spaces](https://github.com/trycua/hermes-cua-spaces)
- **Price:** unknown (Cua cloud pricing not verified)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, repo head 82bb8d3, a review): Looks safe. Small (1.6k lines), only shells out to the cua CLI, no telemetry of its own. It needs Cua's own curl/sh installer, which was not reviewed; the cua package has opt-out telemetry.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Hermes: `hermes plugins install https://github.com/trycua/hermes-cua-spaces`
Hermes: it also needs Cua's own curl/sh installer, which was not reviewed; ask the user before running it.
