# Ace Data Cloud plugin

- **Type:** plugin
- **Category:** Hermes add-ons, generating videos
- **GitHub repo:** unknown
- **Price:** unknown
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read of AceDataCloudMediaHermes @4ebf0fa (2026-11-15): safe with fixes, Skip. Each generate call spends credits with no Hermes approval prompt (__init__.py:24-26) and only calls https://api.acedata.cloud (client.py:15). Fix: a dedicated API key with Usage Limitation and Allowed APIs set (README:70), and only the toolsets you need selected in hermes tools (README:95). Prompts and reference URLs go to Ace Data Cloud.

## Safe install

Safe install (fixes applied):
Hermes catalog install (catalog pin eee9a15); create a dedicated key with Usage Limitation and Allowed APIs set; store it as ACEDATACLOUD_API_KEY in Hermes secrets; in hermes tools select only the toolsets you use.

## YOLO install

YOLO (your own risk): skips the key limits and toolset choice, so the model spends credits freely.
Install from the catalog with your general key and all 17 toolsets.

## Install notes

Ask the user before installing. Hermes catalog install (catalog pin eee9a15); create a dedicated key with Usage Limitation and Allowed APIs set; store it as ACEDATACLOUD_API_KEY in Hermes secrets; in hermes tools select only the toolsets you use.
