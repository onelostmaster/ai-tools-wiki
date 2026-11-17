# Jev (TypeSafe)

- **Type:** API
- **Category:** automation, developer tools
- **Official URL:** https://typesafe.ai
- **GitHub repo:** unknown (hosted model; the vendor's agent skill is https://github.com/typesafe-ai/skills)
- **Price:** $0.042 per million input tokens; output tokens free (`docs.typesafe.ai`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-16

## Safety reason

Claude fix-mode re-review (2026-11-16; plugin @302eea6): safe with fixes. The plugin is one SKILL.md of docs links, no hooks or scripts. The model is hosted: requests and TYPESAFE_API_KEY go to api.typesafe.ai, billed per input token; zero retention is enterprise-only per its docs. Fix: key in env, no confidential text.

## Safe install

Safe install (fixes applied):
claude plugin marketplace add typesafe-ai/skills#302eea6, claude plugin install typesafe@typesafe-ai; set TYPESAFE_API_KEY in env yourself; send no confidential text.

## YOLO install

YOLO (your own risk): skips the pin and the data rule.
Install from the marketplace and send anything.

## Install notes

Ask the user before installing.
Claude Code: `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai` (TypeSafe docs); the Python SDK is `pip install typesafe-sdk` in a virtual environment. Create the key at https://console.typesafe.ai/keys and set `TYPESAFE_API_KEY` yourself; never paste it into chat.
