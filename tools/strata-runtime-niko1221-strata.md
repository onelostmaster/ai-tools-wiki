# Strata runtime (Niko1221/Strata)

- **Type:** app
- **Category:** Hermes add-ons, developer tools
- **Official URL:** https://github.com/Niko1221/Strata
- **GitHub repo:** https://github.com/Niko1221/Strata @ 13eedf5 (MIT; HEAD on 2026-11-14, latest commit 2026-11-12 01:18 ET; docs say version 0.2.13)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (partial code read @13eedf5, 2026-11-14, no-intake review): Caution. Very large repo (about 350,000 lines: Python setup/server plus a C++/CUDA/SYCL engine and binary data); I read the launchers, the download and checksum paths in setup.py, the server's listen and auth code and the agent docs, not the engine. No telemetry or analytics code found. Good: the server listens on 127.0.0.1 unless you change it (serve/server.py line 10212), API keys are compared in constant time (lines 9333-9335), and model downloads are checked against pinned SHA-256s (setup.py verify_sha256, line 3712). SECURITY.md describes a signed (Ed25519) update feed for the Terminal and app (lines 66-71; not verified here) and says there has been no outside audit (line 95). Why caution: (1) the engine download fails open: if GitHub's published SHA-256 can't be fetched, setup warns and installs the engine unverified (setup.py lines 5807-5811); (2) START-HERE.bat silently installs Python via winget or runs the python.org installer with no checksum (lines 18-26); (3) the documented install is irm | iex from the latest release, which SECURITY.md itself says trusts only HTTPS and the release (lines 87-90); (4) AGENTS.md tells agents to set up and serve 'without questions' with --yes, downloading tens of GB (lines 51-55). Third-party, single-maintainer project. Replaces the earlier not-reviewed status.

## Safe install

Safe install (fixes applied):
Windows (NVIDIA or AMD GPU): install Python 3.10+ yourself first, so START-HERE.bat does not silently install Python via winget or an unchecked python.org installer (lines 18-26). Use the desktop app installer from the GitHub release matching 13eedf5, or save install.ps1 and read it before running it (never irm | iex, SECURITY.md lines 87-90). Never set STRATA_SKIP_SHA256=1; if setup warns an engine was NOT verified, stop and retry later (setup.py lines 5807-5811 fail open). Keep the server on 127.0.0.1 (serve/server.py line 10212); set an API key before any --host 0.0.0.0, LAN, Tailscale or Cloudflare sharing. Hermes or Claude Code: tell the agent to ask you before running strata launch --yes, which AGENTS.md says downloads tens of GB without questions (lines 51-55). unverified: the C++/CUDA engine and the signed update feed (not read); contain it by keeping it on localhost with no API keys from other services in its run config. claude.ai and Android: no.

## YOLO install

YOLO (your own risk): skips the read-before-run, the Python pre-install and the agent ask-first step.
Windows (PowerShell): the README's irm | iex install from the latest release; START-HERE.bat installs Python silently if missing. Still never set STRATA_SKIP_SHA256=1.

## Install notes

Code-reviewed by a review bot @13eedf5 (caution; see Safety reason). Partial read: the installers, setup.py download checks, the server's network defaults and the agent instructions; the C++/CUDA engine was not read. Windows: needs an NVIDIA or AMD graphics card and driver; models are tens of GB. Prefer the desktop app installer from the official GitHub release page, or save install.ps1 and read it before running it instead of piping it into PowerShell (irm | iex). START-HERE.bat silently installs Python 3.12 for your user (winget, or the python.org installer with no checksum) if Python 3.10+ is missing; install Python yourself first if you want control over that. Do not set STRATA_SKIP_SHA256=1. If setup warns that an engine was NOT verified (no published SHA-256 reachable), stop and retry later rather than continuing. Keep the server on 127.0.0.1 (the default); set an API key before using --host 0.0.0.0, LAN, Tailscale or Cloudflare sharing. MCP tools in the run config run with your user's rights. Hermes or Claude Code: the repo's AGENTS.md tells agents to run strata launch ... --yes (downloads the engine and tens of GB of model 'without questions'); tell the agent to ask you before installing or downloading anything. claude.ai and Android: not a fit (runs a model on a local GPU PC).
