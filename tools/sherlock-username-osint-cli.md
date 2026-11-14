# Sherlock (username OSINT CLI)

- **Type:** CLI
- **Category:** developer tools, research
- **Official URL:** https://github.com/sherlock-project/sherlock
- **GitHub repo:** https://github.com/sherlock-project/sherlock
- **Price:** Free/open-source MIT (LICENSE:1-17; pyproject.toml:13), verified by online search and official GitHub/installation pages 2026-11-08. No subscription/API key required for normal public checks. Network/proxy/container hosting costs, if chosen, are separate. Dependencies: requests, requests-futures, certifi, colorama, PySocks, stem, pandas, openpyxl, tomli (pyproject.toml:45-55), Poetry-core build backend (:1-3); dependency vulnerabilities/binaries not independently audited.
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-08

## Safety reason

Targeted read @c588d7c (version 0.16.2), not a full audit. CAUTION: checks disclose the searched handle and request metadata to many third-party sites. Unless a proxy is configured, requests use the machine network connection/public IP (sherlock_project/sherlock.py:212-224,248,314-332). Up to 20 concurrent workers (:215-224); rate limits, bot blocks and false results are expected. The manifest controls URLs, headers, payloads and methods including GET/HEAD/POST/PUT (:243-282); bundled entries include POST. Do not treat it as a passive local search or automatically permit arbitrary custom manifests. No username lookup was performed in this vet. Default network also includes live manifest https://data.sherlockproject.xyz (sites.py:11,117-137), false-positive exclusions fetched from GitHub (:12,161-180), and GitHub latest-release lookup (sherlock.py:701-714). That last check only prints an update notice; no automatic package installation seen. --local uses bundled data and skips exclusions (:739-743), but DOES NOT disable release checks or target-site requests. No telemetry SDK, general eval/exec, runtime subprocess shell launcher, agent hooks, permission-skipping mode or curl|bash installer found in targeted package/docs scan; not a full dependency audit. Request-response hooks (:49-108) measure response timing, not Claude hooks. tests/sherlock_interactives.py:17 uses shell=True in tests, not the reviewed CLI runtime; tests were not run. Optional --browse opens result URLs (notify.py:207; default off at sherlock.py:657-662). notify.py:271 prints a sponsor link; printing it is not evidence of a tracking request.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

CAUTION: not installed; show this Safety reason and ask the user before installation or actual lookup. Documentation only, NOT executed. Windows with Python and pipx available: pipx install sherlock-project (official docs/README.md:40 and https://sherlockproject.xyz/installation); alternative pip install --user sherlock-project. Optional Windows pipx bootstrap from official pipx docs: py -m pip install --user pipx; add pipx to PATH/ensurepath and restart terminal. Docker: docker pull sherlock/sherlock; documented one-off example docker run --rm -t sherlock/sherlock user123 (example only, not a real lookup). Docker Desktop/container runtime needed separately; Docker does not hide network IP or guarantee target safety. Avoid unnecessary host-folder mounts. Sherlock declares Python ^3.9 (pyproject.toml:46); installed pipx may require a newer Python. No Android-native install or direct claude.ai browser integration verified. CLI, not an official Claude plugin or bundled MCP server: pyproject.toml:67-68 exposes sherlock entrypoint. Claude Code/Hermes could invoke the installed CLI via their command-execution tool; both integrations untested. No native MCP integration found in this repo. Any future wrapper should pass a fixed argv list (not interpolate shell), require per-request approval and user-owned/authorized handles, allowlist selected sites, cap target count/output/runtime, reject remote/custom --json manifests and treat output/URLs as untrusted. Keep --browse off, do not use --dump-response, do not expose proxy credentials in logs (sherlock.py:717-718 prints configured proxy). Protect local --txt/CSV/XLSX reports (sherlock.py:825-935); do not publish personal-account lists.
