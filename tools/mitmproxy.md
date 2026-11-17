# mitmproxy

- **Type:** app
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://mitmproxy.org
- **GitHub repo:** https://github.com/mitmproxy/mitmproxy @ b08148b (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @b08148b, a review, 2026-11-02): safe. Trusting its CA certificate lets it read all your HTTPS traffic, so remove the cert when done. It blanks Firefox telemetry in its browser helper (`addons/browser.py:189`).

## Safe install

Safe install (fixes applied):
Windows (Python 3.12+, pyproject.toml:5): installer mitmproxy-12.3.1-windows-x86_64-installer.exe from downloads.mitmproxy.org (release v12.3.1, 2026-10-25), or in a venv `pip install mitmproxy==12.3.1`. Verified risk: once you trust its CA certificate (created in %USERPROFILE%\.mitmproxy), mitmproxy can read all HTTPS traffic sent through it. Fix: install the cert only into the Current User store, run the proxy only while testing, and remove the cert afterwards (certmgr.msc, Trusted Root Certification Authorities, delete "mitmproxy"). Its browser helper blanks Firefox telemetry (addons/browser.py:189); nothing else to change. Unverified: 12.3.1 itself (review read the 13.0.0.dev main at b08148b) -> contain: same cert steps, listen on localhost only (default). Android: route only a test device through it and install the cert on that test device only. claude.ai, Claude Code, Hermes: no.

## YOLO install

YOLO (your own risk): skips removing the CA cert after testing (it keeps the ability to read HTTPS traffic routed through the proxy).
Run the Windows installer and trust the cert system-wide.

## Install notes

Safe, but ask the user before installing.
Windows: official installer from mitmproxy.org. Android: route a test device through it; install its CA cert only on a test device.
