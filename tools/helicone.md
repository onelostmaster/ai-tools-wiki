# Helicone

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://github.com/Helicone/helicone
- **GitHub repo:** https://github.com/Helicone/helicone @ 7720d28 (Apache-2.0)
- **Price:** Free to self-host; hosted plans (prices not checked today, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @7720d28, a review, 2026-11-02): safe (light read). Web app loads PostHog only if NEXT_PUBLIC_POSTHOG_API_KEY is set (`web/pages/_app.tsx:41-45`). As a proxy it sees every prompt and response, so self-host it or trust the cloud.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: self-host with Docker (not tested) or use the hosted cloud. Android: dashboard in a phone browser.
