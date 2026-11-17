# Open WebUI

- **Type:** app
- **Category:** research, developer tools
- **Official URL:** https://openwebui.com
- **GitHub repo:** https://github.com/open-webui/open-webui @ f7ac7ee (custom Open WebUI licence)
- **Price:** Free (custom Open WebUI licence with a branding clause) (github.com, checked 2026-11-01); paid model APIs cost extra
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

a review bot (pattern scan plus targeted reads @f7ac7ee, a review), 2026-11-01; Claude fit review only (scan stands): Looks safe. Version check to GitHub on by default (`env.py:1250`); admin-installed Tools/Functions run Python on your server (`plugin.py:242`); branding clause in licence (LICENSE §4).

## Safe install

Safe install (fixes applied):
Windows (Python 3.11 or 3.12; PyPI requires >=3.11,<3.13): in a fresh venv run pip install open-webui==0.12.5, then set OFFLINE_MODE=true (turns off the GitHub version check and Hugging Face downloads, backend/open_webui/env.py:1250-1255) and run open-webui serve, then open http://localhost:8080. v0.12.5 is the exact reviewed commit f7ac7ee (GitHub compare: identical); v0.13.0 to v0.13.3 are not reviewed. Leave login on (WEBUI_AUTH defaults to True, env.py:785) and make the first account yourself, since it becomes admin. Fix: add no community Tools or Functions, because admins' Tools and Functions run Python on your PC (utils/plugin.py:242).
Docker Desktop alternative: docker run -d -p 127.0.0.1:3000:8080 -e OFFLINE_MODE=true -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:v0.12.5 (127.0.0.1 bind instead of the README's network-wide -p 3000:8080; no --restart always).

## YOLO install

YOLO (your own risk): skips the 0.12.5 pin, OFFLINE_MODE, the localhost bind and the no-plugins rule.
The README Docker command: docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main.

## Install notes

Windows: Python 3.12, then `pip install open-webui` and `open-webui serve`, or Docker: `docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main` (README).
