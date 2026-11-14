# Jev (TypeSafe)

- **Type:** API
- **Category:** automation, developer tools
- **Official URL:** https://typesafe.ai
- **GitHub repo:** unknown (hosted model; the vendor's agent skill is https://github.com/typesafe-ai/skills)
- **Price:** $0.042 per million input tokens; output tokens free (`docs.typesafe.ai`, checked 2026-10-31)
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-01

## Safety reason

a review bot (vendor docs, 2026-10-31): caution. Hosted, closed model, so no code to read. Every request sends your text to `api.typesafe.ai` with your `TYPESAFE_API_KEY` and is billed per input token. Vendor says it does not train on requests; zero data retention is only for enterprise customers. Early-access service.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai` (TypeSafe docs); the Python SDK is `pip install typesafe-sdk` in a virtual environment. Create the key at https://console.typesafe.ai/keys and set `TYPESAFE_API_KEY` yourself; never paste it into chat.
