# Microsoft Planetary Computer (STAC API + tiler)

- **Type:** API
- **Category:** research
- **Official URL:** https://planetarycomputer.microsoft.com/
- **GitHub repo:** https://github.com/microsoft/PlanetaryComputer
- **Price:** Free data and APIs, throttled for anonymous use (planetarycomputer.microsoft.com/docs, checked 2026-11-12)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-12

## Safety reason

Official Microsoft service, read-only. STAC API is anonymous; asset downloads need a free SAS token from its own token endpoint (no account needed), rate-limited outside Azure West Europe (official docs, checked 2026-11-12).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code / Windows: search https://planetarycomputer.microsoft.com/api/stac/v1 (pystac-client works); sign asset URLs with the planetary-computer package or the /api/sas/v1/sign endpoint. Keep downloads small; prefer the tiler previews.
