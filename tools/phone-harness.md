# Phone Harness

- **Type:** plugin
- **Category:** Hermes add-ons, automation
- **Official URL:** https://github.com/ShawnPana/phone-harness
- **GitHub repo:** [https://github.com/ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness)
- **Price:** unknown
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude code read @4bebff1 (2026-11-16): safe with fixes. Model-written Python runs with exec and full phone control (src/phone_harness/run.py:437): that is the product, so use a spare Android phone. The CLI's PostHog telemetry is on by default; DO_NOT_TRACK=1 or phone-harness config set telemetry false turns it off (telemetry.py:15-17); under Hermes it is off until you opt in. PHONE_HARNESS_NO_UPDATE_CHECK=1 stops update checks (update.py:140).

## Safe install

Safe install (fixes applied):
Spare Android phone only; env DO_NOT_TRACK=1 and PHONE_HARNESS_NO_UPDATE_CHECK=1; uv tool install --python 3.12 phone-harness==0.3.3; Hermes: hermes plugins install phone-harness/phone-harness/integrations/hermes and leave telemetry off.

## YOLO install

YOLO (your own risk): skips the spare phone and both switches.
Install with --upgrade on your main phone as install.md says.

## Install notes

Ask the user before installing. Spare Android phone only; env DO_NOT_TRACK=1 and PHONE_HARNESS_NO_UPDATE_CHECK=1; uv tool install --python 3.12 phone-harness==0.3.3; Hermes: hermes plugins install phone-harness/phone-harness/integrations/hermes and leave telemetry off.
