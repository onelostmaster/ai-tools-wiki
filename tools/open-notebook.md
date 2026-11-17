# Open Notebook

- **Type:** app
- **Category:** research, Notion and productivity
- **Official URL:** https://www.open-notebook.ai
- **GitHub repo:** https://github.com/lfnovo/open-notebook @ a0f6f30 (MIT)
- **Price:** Free, open source (MIT) (github.com, checked 2026-11-01); model APIs you connect may cost extra
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (pattern scan plus targeted reads @a0f6f30, a review), 2026-11-01; Claude fit review only (scan stands): Looks safe. No login unless OPEN_NOTEBOOK_PASSWORD is set (`api/auth.py:15-16`); ports 8502/5055 open (`docker-compose.yml`); change the encryption key.

## Safe install

Safe install (fixes applied):
Windows (Docker Desktop): download docker-compose.yml and .env.example from github.com/lfnovo/open-notebook, copy .env.example to .env and set OPEN_NOTEBOOK_ENCRYPTION_KEY (a long random string), OPEN_NOTEBOOK_PASSWORD, SURREAL_USER and SURREAL_PASSWORD. Fix: without a password there is no login (api/auth.py:15-16) and the default key is a public placeholder (docker-compose.yml); the password and key above close both. Fix: change the ports to "127.0.0.1:8502:8502" and "127.0.0.1:5055:5055" so only your PC can reach it (the compose file publishes them to your network). Fix: change the image to lfnovo/open_notebook:1.15.0 and remove pull_policy: always so it does not update itself (1.15.0 is the release one day before the reviewed commit a0f6f30; 1.15.1 from 2026-11-04 is not reviewed). Then docker compose up -d and open http://localhost:8502.

## YOLO install

YOLO (your own risk): skips the localhost ports and the 1.15.0 pin.
Use the compose file as shipped (v1-latest image, ports open to your network), still with your own key and password in .env.

## Install notes

Windows (Docker): download the repo's `docker-compose.yml`, set OPEN_NOTEBOOK_ENCRYPTION_KEY and OPEN_NOTEBOOK_PASSWORD, then `docker compose up -d` (README).
