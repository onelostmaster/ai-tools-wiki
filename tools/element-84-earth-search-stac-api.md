# Element 84 Earth Search (STAC API)

- **Type:** API
- **Category:** research
- **Official URL:** https://element84.com/earth-search/
- **GitHub repo:** https://github.com/Element84/earth-search
- **Price:** Free to use (element84.com/earth-search, checked 2026-11-12)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Official Element 84 service, read-only, no key; the product page calls it a free-to-use STAC API (checked 2026-11-12). The GitHub repo is information and issues only.

## Safe install

Safe install (fixes applied):
Nothing to install for the API itself: call https://earth-search.aws.element84.com/v1 over HTTPS (answered 200 on 2026-11-14), no key or account. In Claude Code (Windows) or the project container use a venv and `pip install pystac-client==0.9.1` (PyPI latest 2026-11-14). Sentinel-2 COGs are public on S3 and need no signing, so no AWS keys go in the environment. claude.ai, Hermes and Android: plain HTTPS from any tool that can fetch URLs.

## YOLO install

YOLO (your own risk): skips the venv and the version pin.
pip install pystac-client

## Install notes

Claude Code / Windows: STAC endpoint https://earth-search.aws.element84.com/v1 (pystac-client works). Sentinel-2 COGs are public on S3, no signing needed.
