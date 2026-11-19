# Atheros AI Builder

- **Type:** app
- **Category:** design, developer tools
- **Official URL:** https://builder.atheros.ai/
- **GitHub repo:** unknown
- **Price:** Online checked official /pricing and /docs 2026-11-08; inconsistent! Pricing shows Free $0 with 100 credits, AI Pass $15/mo billed annually, Ultra $39/mo billed annually; docs instead list 30/500/2000 credits and $15/$39 monthly, $144/$374 annual. Do not treat these conflicting advertised rates/quotas as a final quote: verify checkout before purchase. MCP requires paid Pass/Ultra, unavailable Free. Proprietary hosted-service terms, not MIT. Docs allow commercial generated end products; catalog components cannot be resold as component libraries or used to seed competitors.
- **Decision:** Try
- **Safety verdict:** unreviewed
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-18

## Safety reason

No code (hosted). Claude docs read (2026-11-18): MCP at mcp.atheros.ai/v1 with a bearer key; a project key limits scope, an account key reads all projects; Ultra adds write, publish and delete tools. Unverified: server-side logging and retention -> Contain: project key, read-only plan, approvals per call.

## Safe install

Unreviewed: contain it: project-scoped key in env, never an account key; claude mcp add atheros --transport http https://mcp.atheros.ai/v1 --header "Authorization: Bearer $ATHEROS_KEY"; keep tool approvals; no production secrets in prompts. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Contain it: project-scoped key in env, never an account key; claude mcp add atheros --transport http https://mcp.atheros.ai/v1 --header "Authorization: Bearer $ATHEROS_KEY"; keep tool approvals; no production secrets in prompts.
