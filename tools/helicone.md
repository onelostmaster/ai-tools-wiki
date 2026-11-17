# Helicone

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://github.com/Helicone/helicone
- **GitHub repo:** https://github.com/Helicone/helicone @ 7720d28 (Apache-2.0)
- **Price:** Free to self-host; hosted plans (prices not checked today, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (light code read @7720d28, a review, 2026-11-02): safe (light read). Web app loads PostHog only if NEXT_PUBLIC_POSTHOG_API_KEY is set (`web/pages/_app.tsx:41-45`). As a proxy it sees every prompt and response, so self-host it or trust the cloud.

## Safe install

Safe install (fixes applied):
Windows (Docker Desktop): download the repo at commit 7720d28, `cd docker`, `cp .env.example .env` and run `./helicone-compose.sh helicone up` in WSL or Git Bash (README.md:64-76). Verified: docker-compose.yml hard-codes default secrets (POSTGRES_PASSWORD testpassword line 14, MINIO_ROOT_PASSWORD minioadmin line 61, REDIS_PASSWORD line 99, BETTER_AUTH_SECRET falls back to your-secret-key lines 167,200) and publishes ports on all interfaces (5432 as 54388, ClickHouse 18123/19000, MinIO 9000/9001, Redis 6379, web 3000, worker 8787). Fix: before the first start, set your own values for every secret in .env (.env.example:1-4 says you must change them) and the hard-coded ones in docker-compose.yml, and prefix every port with 127.0.0.1: (e.g. "127.0.0.1:3000:3000"). The web app loads PostHog only if NEXT_PUBLIC_POSTHOG_API_KEY is set (web/pages/_app.tsx:41-45): leave it empty. As a proxy it stores every prompt and response: self-host for private data. Hosted cloud: your prompts go to Helicone. Claude Code, claude.ai, Hermes: point the model base URL at your Helicone proxy. Android: dashboard in a browser.

## YOLO install

YOLO (your own risk): skips changing the default secrets and the localhost-only ports.
git clone https://github.com/Helicone/helicone.git; cd docker; cp .env.example .env; ./helicone-compose.sh helicone up

## Install notes

Safe, but ask the user before installing.
Windows: self-host with Docker (not tested) or use the hosted cloud. Android: dashboard in a phone browser.
