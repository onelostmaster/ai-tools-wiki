# Booking.com connector

- **Type:** connector
- **Category:** research
- **Official URL:** https://claude.com/marketplace/connectors/booking
- **GitHub repo:** unknown
- **Price:** Free to connect; Claude connectors are on all plans; stays are paid on Booking.com (claude.com, checked 2026-11-02)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-18

## Safety reason

Booking.com (official vendor connector, made by Booking BV; not code-reviewed; docs checked 2026-11-02): safe. Search only (one tool, accommodations_search); no Booking.com account access, no bookings, payments or reservation changes inside Claude; Booking.com says it does not receive your Claude chat history. Bookings finish on booking.com, where signing in is your choice.

## Safe install

Safe install (fixes applied):
claude.ai and Android: already connected on the Claude account; elsewhere add Booking.com from claude.com/connectors. One search-only tool (accommodations_search), no account access or bookings inside Claude (developers.booking.com), so nothing to fix. To remove it, disconnect it in Settings > Connectors.
Claude Code: not supported (Booking.com docs).

## YOLO install

Not written yet.

## Install notes

claude.ai: already connected on the Claude account; elsewhere open the connectors directory at `claude.com/connectors`, find Booking.com and select Connect; no sign-in needed to search (official Booking.com developer docs).
Android: the Claude app uses the same connector once it is added (Booking.com docs list Claude Mobile).
Claude Code: not supported (Booking.com docs).
