# Google Fonts

- **Type:** API
- **Category:** design, building a site, a project
- **Official URL:** https://fonts.google.com
- **GitHub repo:** https://github.com/google/fonts (font files for self-hosting; not code-reviewed, fonts only)
- **Price:** Free; most fonts under the SIL Open Font License, some Apache or Ubuntu Font License (Google Fonts FAQ, checked 2026-11-03)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

a review bot (official privacy FAQ developers.google.com/fonts/faq/privacy, read 2026-11-03): safe. The Fonts API is unauthenticated and sets no cookies; each page load sends the viewer IP, the requested URL, user agent and referer to fonts.googleapis.com / fonts.gstatic.com, which Google says it does not use for profiles or ads. Self-host the font files to send nothing to Google. No code to review (fonts and CSS only).

## Safe install

Safe install (fixes applied):
Any platform: self-host: download the font files from github.com/google/fonts, serve them from the app's own folder with an @font-face rule, and keep a system-font fallback. Then pages send nothing to Google (the privacy FAQ says each fonts.googleapis.com load sends the viewer IP, URL, user agent and referer).

## YOLO install

YOLO (your own risk): skips self-hosting, so every page load sends the viewer's IP and the page URL to Google.
A stylesheet link tag to fonts.googleapis.com in the page head.

## Install notes

Safe, but ask the user before installing.
Any platform: a stylesheet link tag in the page head pointing to fonts.googleapis.com in the page HTML; nothing installed. To send nothing to Google, download the fonts (github.com/google/fonts) and self-host them. If they fail to load, the app falls back to system fonts.
