# TruLens

- **Type:** library
- **Category:** developer tools
- **Official URL:** https://github.com/truera/trulens
- **GitHub repo:** https://github.com/truera/trulens @ 915e3ab (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @915e3ab, a review, 2026-11-02): caution. Its OpenCode connector writes a plugin that spawns sh -c COMMAND for every event (`src/apps/opencode/.../client.py:124-130`): only use it with a command you set.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: pip in a venv (not tested); skip the OpenCode connector unless you set its command.
