# Open WebUI

- **Type:** app
- **Category:** research, developer tools
- **Official URL:** https://openwebui.com
- **GitHub repo:** https://github.com/open-webui/open-webui @ f7ac7ee (custom Open WebUI licence)
- **Price:** Free (custom Open WebUI licence with a branding clause) (github.com, checked 2026-11-01); paid model APIs cost extra
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-01

## Safety reason

a review bot (pattern scan plus targeted reads @f7ac7ee, a review), 2026-11-01; Claude fit review only (scan stands): Looks safe. Version check to GitHub on by default (`env.py:1250`); admin-installed Tools/Functions run Python on your server (`plugin.py:242`); branding clause in licence (LICENSE §4).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Windows: Python 3.12, then `pip install open-webui` and `open-webui serve`, or Docker: `docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main` (README).
