# Google Fonts

- **Type:** API
- **Category:** design, building a site, a project
- **Official URL:** https://fonts.google.com
- **GitHub repo:** https://github.com/google/fonts (font files for self-hosting; not code-reviewed, fonts only)
- **Price:** Free; most fonts under the SIL Open Font License, some Apache or Ubuntu Font License (Google Fonts FAQ, checked 2026-11-03)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-04

## Safety reason

a review bot (official privacy FAQ developers.google.com/fonts/faq/privacy, read 2026-11-03): safe. The Fonts API is unauthenticated and sets no cookies; each page load sends the viewer IP, the requested URL, user agent and referer to fonts.googleapis.com / fonts.gstatic.com, which Google says it does not use for profiles or ads. Self-host the font files to send nothing to Google. No code to review (fonts and CSS only).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Any platform: a stylesheet link tag in the page head pointing to fonts.googleapis.com in the page HTML; nothing installed. To send nothing to Google, download the fonts (github.com/google/fonts) and self-host them. If they fail to load, the app falls back to system fonts.
