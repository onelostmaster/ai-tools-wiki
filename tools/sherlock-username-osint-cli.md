# Sherlock (username OSINT CLI)

- **Type:** CLI
- **Category:** developer tools, research
- **Official URL:** https://github.com/sherlock-project/sherlock
- **GitHub repo:** https://github.com/sherlock-project/sherlock
- **Price:** Free/open-source MIT (LICENSE:1-17; pyproject.toml:13), verified by online search and official GitHub/installation pages 2026-11-08. No subscription/API key required for normal public checks. Network/proxy/container hosting costs, if chosen, are separate. Dependencies: requests, requests-futures, certifi, colorama, PySocks, stem, pandas, openpyxl, tomli (pyproject.toml:45-55), Poetry-core build backend (:1-3); dependency vulnerabilities/binaries not independently audited.
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

Claude code read @c588d7c v0.16.2 (2026-11-18): safe with fixes. Each lookup sends the handle to hundreds of sites from your IP unless --proxy is set (sherlock_project/sherlock.py:315-316,596-600). The bundled manifest decides URLs and methods; a custom --json manifest can send anything. No telemetry. Fix: proxy, bundled manifest only, only handles you own or have consent for.

## Safe install

Safe install (fixes applied):
pipx install sherlock-project==0.16.2; run with --proxy <your proxy URL>; bundled manifest only, no --json from others; search only your own handles or with consent.

## YOLO install

YOLO (your own risk): skips the proxy, manifest and consent rules.
pipx install sherlock-project and look anyone up from your IP.

## Install notes

CAUTION: not installed; show this Safety reason and ask the user before installation or actual lookup. Documentation only, NOT executed. Windows with Python and pipx available: pipx install sherlock-project (official docs/README.md:40 and https://sherlockproject.xyz/installation); alternative pip install --user sherlock-project. Optional Windows pipx bootstrap from official pipx docs: py -m pip install --user pipx; add pipx to PATH/ensurepath and restart terminal. Docker: docker pull sherlock/sherlock; documented one-off example docker run --rm -t sherlock/sherlock user123 (example only, not a real lookup). Docker Desktop/container runtime needed separately; Docker does not hide network IP or guarantee target safety. Avoid unnecessary host-folder mounts. Sherlock declares Python ^3.9 (pyproject.toml:46); unverified: the minimum Python of the pipx release you install; containment: install pipx with py -m pip install --user pipx on the same Python 3.9+ you use for Sherlock. No Android-native install or direct claude.ai browser integration verified. CLI, not an official Claude plugin or bundled MCP server: pyproject.toml:67-68 exposes sherlock entrypoint. Claude Code/Hermes run the installed CLI only through their command-execution tool (unverified: both integrations untested; containment: approve each command). No native MCP integration found in this repo. Any future wrapper should pass a fixed argv list (not interpolate shell), require per-request approval and user-owned/authorized handles, allowlist selected sites, cap target count/output/runtime, reject remote/custom --json manifests and treat output/URLs as untrusted. Keep --browse off, do not use --dump-response, do not expose proxy credentials in logs (sherlock.py:717-718 prints configured proxy). Protect local --txt/CSV/XLSX reports (sherlock.py:825-935); do not publish personal-account lists.
