# OpenProject

- **Type:** app
- **Category:** Notion and productivity
- **Official URL:** https://www.openproject.org
- **GitHub repo:** https://github.com/opf/openproject @ 0c3d492 (GPL-3.0; latest commit on 2026-10-31)
- **Price:** Community edition free to self-host; Enterprise cloud or on-premises priced per user (`openproject.org/pricing`, checked 2026-10-31).
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

a review bot (vendor site and README, 2026-10-31): safe. Official product of OpenProject GmbH, GPL-3.0, with a private security-disclosure process. Self-hosting means running and patching a server yourself; the cloud edition stores your data with OpenProject.

## Safe install

Safe install (fixes applied):
Windows (Docker Desktop, local only): docker run -d -p 127.0.0.1:8080:80 --name openproject -e OPENPROJECT_HOST__NAME=localhost:8080 -e OPENPROJECT_HTTPS=false -e SECRET_KEY_BASE=<random, e.g. openssl rand -hex 64> -v C:\\openproject\\pgdata:/var/openproject/pgdata -v C:\\openproject\\assets:/var/openproject/assets openproject/openproject:17 (openproject.org Docker guide, with the port bound to 127.0.0.1 and Windows folders for the data). The guide says this one-container setup turns HTTPS off and is not for production, so keep it on localhost; for access from other devices put it behind a TLS reverse proxy and set OPENPROJECT_HOST__NAME to the real public name (the guide warns about HOST header injection otherwise). Keep SECRET_KEY_BASE out of chats and shared pages.

## YOLO install

YOLO (your own risk): skips the localhost-only port and the data folders.
docker run -it -p 8080:80 -e SECRET_KEY_BASE=<secret> -e OPENPROJECT_HOST__NAME=localhost:8080 -e OPENPROJECT_HTTPS=false openproject/openproject:17 (quick start in the guide; reachable from your network, data lost when the container is removed).

## Install notes

Server (Docker): follow the official guide at https://www.openproject.org/docs/installation-and-operations/installation/docker/ (`openproject.org`).
