# AG2

- **Type:** library
- **Category:** developer tools, automation
- **Official URL:** https://ag2.ai
- **GitHub repo:** https://github.com/ag2ai/ag2 @ 9cfbb69 (Apache-2.0)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); model calls are paid
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @9cfbb69, a review, 2026-11-02): safe. Telemetry is OpenTelemetry spans you export yourself (`ag2/network/hub/telemetry.py:5-20`); no phone-home found in the paths read.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: `pip install ag2[openai]` (README); `pip install ag2-classic` for old AutoGen code. Android: no.
