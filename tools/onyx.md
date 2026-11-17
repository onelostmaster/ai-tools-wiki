# Onyx

- **Type:** app
- **Category:** research, Notion and productivity
- **Official URL:** https://onyx.app
- **GitHub repo:** https://github.com/onyx-dot-app/onyx @ 3eb6420 (MIT Community Edition plus a separate Enterprise Edition; latest commit on 2026-10-31; the post's card links `senlindesign/taste-skill` by mistake)
- **Price:** Community Edition free to self-host; Business $20 per user/month billed annually; Enterprise custom (`onyx.app`, checked 2026-11-01).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (vendor README and pricing page, 2026-11-01): safe. Official product of Onyx, MIT Community Edition. Quick install is `curl -fsSL https://onyx.app/install_onyx.sh | bash` (read it first); it indexes your connected documents and sends queries to the LLM you configure; Onyx Cloud keeps your data with Onyx.

## Safe install

Safe install (fixes applied):
Windows (Docker Desktop, local only): install Docker Desktop yourself first (winget install Docker.DockerDesktop). Do not pipe install.ps1 into iex: when Docker is missing it relaunches itself as Administrator and installs Docker Desktop and WSL with winget (deployment/docker_compose/install.ps1 lines 626-632, main on 2026-11-16), and the Linux/macOS install_onyx.sh fetches the newest onyx-cli and adds ~/.local/bin to your shell profile (lines 12-19). Instead download docker-compose.yml and env.template from github.com/onyx-dot-app/onyx/tree/main/deployment/docker_compose, copy env.template to .env, set IMAGE_TAG=v5.1.3 (latest release, 2026-11-16 ET) instead of latest (docker-compose.yml line 48), and change the nginx ports (lines 510-511) to "127.0.0.1:80:80" and "127.0.0.1:3000:80" so only your PC can reach it. Then docker compose up -d and open http://localhost:3000. Connect only the document sources you want indexed; queries go to the LLM provider you configure. Claude Code: add your Onyx server's MCP endpoint (Onyx docs).

## YOLO install

YOLO (your own risk): skips the version pin, the localhost-only ports and installing Docker yourself.
Windows: irm https://raw.githubusercontent.com/onyx-dot-app/onyx/main/deployment/docker_compose/install.ps1 | iex (install.sh line 137). Linux/macOS: curl -fsSL https://onyx.app/install_onyx.sh | bash (README), image tag latest, ports open on all interfaces.

## Install notes

Server (Docker): `curl -fsSL https://onyx.app/install_onyx.sh | bash`, or the Docker, Kubernetes and Helm guides at https://docs.onyx.app (README).
Claude Code: point it at your Onyx server's MCP endpoint (README; steps in the Onyx docs).
