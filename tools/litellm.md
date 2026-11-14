# LiteLLM

- **Type:** app
- **Category:** developer tools
- **Official URL:** https://github.com/BerriAI/litellm
- **GitHub repo:** https://github.com/BerriAI/litellm @ acd084ab (MIT core, enterprise folders separate)
- **Price:** Free to self-host, MIT core; enterprise and hosted plans (prices not checked today, 2026-11-02)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (light code read @acd084ab, a review, 2026-11-02): caution. Official advisory GHSA-5mg7-485q-xm76 and the LiteLLM blog (docs.litellm.ai/blog/security-update-march-2026) confirm PyPI 1.82.7 and 1.82.8 (2026-03-24) carried credential-stealing malware; both removed, 1.83.0+ from a hardened pipeline. Never install those two versions. --telemetry flag is now a no-op (`proxy/proxy_cli.py:975-980`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: pip (pin 1.83.0 or newer, never 1.82.7/1.82.8) or Docker. Claude Code: can sit between Claude Code and other models.
