# Microsoft Planetary Computer (STAC API + tiler)

- **Type:** API
- **Category:** research
- **Official URL:** https://planetarycomputer.microsoft.com/
- **GitHub repo:** https://github.com/microsoft/PlanetaryComputer
- **Price:** Free data and APIs, throttled for anonymous use (planetarycomputer.microsoft.com/docs, checked 2026-11-12)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Official Microsoft service, read-only. STAC API is anonymous; asset downloads need a free SAS token from its own token endpoint (no account needed), rate-limited outside Azure West Europe (official docs, checked 2026-11-12).

## Safe install

Safe install (fixes applied):
Nothing to install for the API itself: search https://planetarycomputer.microsoft.com/api/stac/v1 anonymously (answered 200 on 2026-11-14). In Claude Code (Windows) or the project container use a venv and `pip install pystac-client==0.9.1 planetary-computer==1.0.0` (PyPI latest 2026-11-14); planetary-computer signs asset URLs with a free SAS token from the token endpoint, no account and no subscription key needed. Downloads are rate-limited outside Azure West Europe (official docs): keep downloads small and use the tiler previews. claude.ai, Hermes and Android: plain HTTPS.

## YOLO install

YOLO (your own risk): skips the venv and the version pins.
pip install pystac-client planetary-computer

## Install notes

Claude Code / Windows: search https://planetarycomputer.microsoft.com/api/stac/v1 (pystac-client works); sign asset URLs with the planetary-computer package or the /api/sas/v1/sign endpoint. Keep downloads small; prefer the tiler previews.
