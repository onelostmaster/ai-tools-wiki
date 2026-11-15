# RustDesk

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://rustdesk.com
- **GitHub repo:** https://github.com/rustdesk/rustdesk (AGPL-3.0; latest release 1.5.3, 2026-11-09)
- **Price:** Free and open source (self-hosting Free plan $0); Server Pro from $11.88/month billed annually (rustdesk.com/pricing, checked 2026-11-13)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Official AGPL-3.0 project, signed MSI 1.5. It is full remote control, so: latest release only, permanent password plus 2FA, direct IP access limited to the Tailscale range. The '2026 CVEs' note is unconfirmed (no GitHub advisories) and is dropped; staying on the latest release covers it.

## Safe install

Safe install (fixes applied):
Windows: official MSI from github.com/rustdesk/rustdesk/releases with SHA-256 check; permanent password + 2FA; direct IP whitelist = Tailscale range only; update on each release. Android: GitHub APK or F-Droid.

## YOLO install

YOLO (your own risk): skips 2FA and the Tailscale whitelist.
Default install with the public ID server and one-time passwords.

## Install notes

Ask the user before installing.
Windows: official MSI from github.com/rustdesk/rustdesk/releases (check the SHA-256); enable 2FA and a permanent password; if using direct IP access, whitelist only the Tailscale range. Android: not on Google Play; official APK from GitHub releases or F-Droid. Keep updated. Ask the user before installing on a new device.
