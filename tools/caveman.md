# caveman

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/JuliusBrussee/caveman
- **GitHub repo:** [https://github.com/JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)
- **Price:** Free (open-source)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @b4ee71d = v4.1.0 (2026-11-15): safe with fixes, Skip. The plugin hooks have no network code (src/hooks/*.js). The separate caveman CLI sends usage events with your IP by default; DO_NOT_TRACK=1 or caveman telemetry off stops it (SECURITY.md:45, 133-139). The caveman-setup skill rewires your app's LLM calls through Caveman Cloud and sends a billable request (skills/caveman-setup/SKILL.md:173): don't run it.

## Safe install

Safe install (fixes applied):
claude plugin marketplace add JuliusBrussee/caveman#v4.1.0, claude plugin install caveman@caveman; env DO_NOT_TRACK=1; never run /caveman-setup or the Caveman Cloud proxy; skip the curl|bash installer.

## YOLO install

YOLO (your own risk): skips the pin, telemetry off and the setup ban.
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/v4.1.0/install.sh | bash and run /caveman-setup.

## Install notes

Ask the user before installing. claude plugin marketplace add JuliusBrussee/caveman#v4.1.0, claude plugin install caveman@caveman; env DO_NOT_TRACK=1; never run /caveman-setup or the Caveman Cloud proxy; skip the curl|bash installer.
