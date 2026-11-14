# mitmproxy

- **Type:** app
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://mitmproxy.org
- **GitHub repo:** https://github.com/mitmproxy/mitmproxy @ b08148b (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

a review bot (light code read @b08148b, a review, 2026-11-02): safe. Trusting its CA certificate lets it read all your HTTPS traffic, so remove the cert when done. It blanks Firefox telemetry in its browser helper (`addons/browser.py:189`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: official installer from mitmproxy.org. Android: route a test device through it; install its CA cert only on a test device.
