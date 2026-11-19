# LiteLLM

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://github.com/BerriAI/litellm
- **GitHub repo:** https://github.com/BerriAI/litellm @ acd084ab (MIT core, enterprise folders separate)
- **Price:** Free to self-host, MIT core; enterprise and hosted plans (prices not checked today, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-18

## Safety reason

a review bot (light code read @acd084ab, a review, 2026-11-02): caution. Official advisory GHSA-5mg7-485q-xm76 and the LiteLLM blog (docs.litellm.ai/blog/security-update-march-2026) confirm PyPI 1.82.7 and 1.82.8 (2026-03-24) carried credential-stealing malware; both removed, 1.83.0+ from a hardened pipeline. Never install those two versions. --telemetry flag is now a no-op (proxy/proxy_cli.py:975-980). Fix-rule re-rate 2026-11-18: every verified risk has its exact fix in Safe install (one exact version 1.83.0 or newer pinned, never 1.82.7 or 1.82.8, keys in a proxy-only env file, proxy bound to localhost); with those fixes applied: safe.

## Safe install

Safe install (fixes applied):
Windows: in a venv, pip install "litellm>=1.83.0" pinned to one exact version 1.83.0 or newer; never 1.82.7 or 1.82.8, which carried credential-stealing malware (GHSA-5mg7-485q-xm76; docs.litellm.ai/blog/security-update-march-2026). Or Docker with a pinned 1.83.0+ image tag. Put provider keys in an env file read only by the proxy, and bind the proxy to localhost. Claude Code: point it at the local proxy to route to other models. Android: no.

## YOLO install

YOLO (your own risk): skips the exact version pin and localhost binding.
Windows: pip install litellm (latest); still never 1.82.7/1.82.8.

## Install notes

Ask the user before installing. Safe only with the fixes in Safe install applied.
Windows: pip (pin 1.83.0 or newer, never 1.82.7/1.82.8) or Docker. Claude Code: can sit between Claude Code and other models.
