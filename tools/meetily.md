# Meetily

- **Type:** app
- **Category:** voice and audio, Notion and productivity
- **Official URL:** https://meetily.ai
- **GitHub repo:** https://github.com/Zackriya-Solutions/meetily @ a2cb62e (MIT; formerly meeting-minutes)
- **Price:** Free (MIT) (github.com, checked 2026-11-01); PRO plan price unknown
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (pattern scan plus targeted reads @a2cb62e, a review), 2026-11-01; Claude fit review only (scan stands): Looks safe. PostHog analytics opt-in, default off (`AnalyticsProvider.tsx:34-53`); PRO upsell (README:47). Get consent before recording any call.

## Safe install

Safe install (fixes applied):
Windows: download meetily_0.4.1_x64-setup.exe from github.com/Zackriya-Solutions/meetily/releases/tag/v0.4.1 (released 2026-09-12, two days after the reviewed commit a2cb62e; v0.5.0 from 2026-11-14 is not reviewed) and run it; needs an AVX2 CPU (README). Leave analytics off: PostHog is opt-in and off by default (AnalyticsProvider.tsx:34-53). Turn off auto-update in its settings if you want to stay on the reviewed version (unverified: whether the app has that setting; if not, it will offer v0.5.0). Get consent from everyone before recording a call.

## YOLO install

YOLO (your own risk): skips the v0.4.1 pin.
Install meetily_0.5.0_x64-setup.exe from the latest release.

## Install notes

Windows: `x64-setup.exe` from `https://github.com/Zackriya-Solutions/meeting-minutes/releases/latest` (needs an AVX2 CPU) (README). Get consent before recording calls.
