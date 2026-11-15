# Tailscale

- **Type:** app
- **Category:** developer tools, security
- **Official URL:** https://tailscale.com
- **GitHub repo:** https://github.com/tailscale/tailscale (BSD-3-Clause; latest release v1.104.7, 2026-11-12)
- **Price:** Personal plan free (non-commercial, up to 6 users, unlimited user devices); Standard $8 and Premium $18 per user per month (tailscale.com/pricing, checked 2026-11-13)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Official vendor (Tailscale Inc., open-source client, BSD-3-Clause), installed from the official winget package Tailscale.Tailscale 1.104.7. Coordination servers are Tailscale-hosted (account sign-in needed); keep key expiry and device approval in mind. Not code-read by a review bot.

## Safe install

Safe install (fixes applied):
Windows: `winget install --id Tailscale.Tailscale -e` (official winget package), sign in; turn on "Run unattended" only if the PC must stay reachable. Android: the official Tailscale app from Google Play. Same account on each device; ask the user before adding a new device.

## YOLO install

Not written yet.

## Install notes

Windows: winget install Tailscale.Tailscale (official), sign in, then set run unattended if the PC must stay reachable. Android: official Tailscale app from Google Play. Sign in with the same account on each device. Ask the user before installing on a new device.
