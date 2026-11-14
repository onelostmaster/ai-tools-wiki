# Open Notebook

- **Type:** app
- **Category:** research, Notion and productivity
- **Official URL:** https://www.open-notebook.ai
- **GitHub repo:** https://github.com/lfnovo/open-notebook @ a0f6f30 (MIT)
- **Price:** Free, open source (MIT) (github.com, checked 2026-11-01); model APIs you connect may cost extra
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (pattern scan plus targeted reads @a0f6f30, a review), 2026-11-01; Claude fit review only (scan stands): Looks safe. No login unless OPEN_NOTEBOOK_PASSWORD is set (`api/auth.py:15-16`); ports 8502/5055 open (`docker-compose.yml`); change the encryption key.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Windows (Docker): download the repo's `docker-compose.yml`, set OPEN_NOTEBOOK_ENCRYPTION_KEY and OPEN_NOTEBOOK_PASSWORD, then `docker compose up -d` (README).
