# TruLens

- **Type:** library
- **Category:** developer tools
- **Official URL:** https://github.com/truera/trulens
- **GitHub repo:** https://github.com/truera/trulens @ 915e3ab (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (light code read @915e3ab, a review, 2026-11-02): caution. Its OpenCode connector writes a plugin that spawns sh -c COMMAND for every event (`src/apps/opencode/.../client.py:124-130`): only use it with a command you set.

## Safe install

Safe install (fixes applied):
Windows: in a venv, pip install trulens==<release matching 915e3ab>. Do not enable the OpenCode connector; if you do, set its command yourself, because the plugin it writes runs sh -c COMMAND on every event (src/apps/opencode/.../client.py:124-130). Android: no.

## YOLO install

YOLO (your own risk): skips the version pin.
Windows: pip install trulens; still leave the OpenCode connector off unless you set its command.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: pip in a venv (not tested); skip the OpenCode connector unless you set its command.
