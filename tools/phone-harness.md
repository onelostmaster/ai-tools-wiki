# Phone Harness

- **Type:** plugin
- **Category:** Hermes add-ons, automation
- **Official URL:** https://github.com/ShawnPana/phone-harness
- **GitHub repo:** [https://github.com/ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)
- **Price:** unknown
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, a project a review, 2026-10-28): Use with caution. Runs model-written Python locally via exec with full phone control. The standalone CLI's telemetry is ON by default and sends task text, output and steps to PostHog; the Hermes plugin forces it off unless you opt in.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
Hermes: a review bot gave no steps (verdict isn't Looks safe). It is a Hermes plugin that drives the phone, not an Android app.
