# caveman

- **Type:** plugin
- **Category:** developer tools
- **Official URL:** https://github.com/JuliusBrussee/caveman
- **GitHub repo:** [https://github.com/JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)
- **Price:** Free (open-source)
- **Decision:** Skip
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code read, 9b68f7e, a review): Use with caution. Hooks on SessionStart, SubagentStart and UserPromptSubmit; its CLI sends usage stats including your IP by default (telemetry); curl|bash install; Caveman Cloud proxy; its caveman-setup skill says to send a billable request without asking.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

No install steps: the source withholds them until the tool is rated safe. Read the Safety reason and ask the user first.
