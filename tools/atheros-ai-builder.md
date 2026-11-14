# Atheros AI Builder

- **Type:** app
- **Category:** design, developer tools
- **Official URL:** https://builder.atheros.ai/
- **GitHub repo:** unknown
- **Price:** Online checked official /pricing and /docs 2026-11-08; inconsistent! Pricing shows Free $0 with 100 credits, AI Pass $15/mo billed annually, Ultra $39/mo billed annually; docs instead list 30/500/2000 credits and $15/$39 monthly, $144/$374 annual. Do not treat these conflicting advertised rates/quotas as a final quote: verify checkout before purchase. MCP requires paid Pass/Ultra, unavailable Free. Proprietary hosted-service terms, not MIT. Docs allow commercial generated end products; catalog components cannot be resold as component libraries or used to seed competitors.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-08

## Safety reason

Official docs only; public implementation repo unknown after targeted search, so no code clone or file-line audit possible. Prompts, screenshots and component source go to vendor/model providers; server logs/telemetry/retention/dependencies/hooks/update behavior unverified. MCP https://mcp.atheros.ai/v1 uses bearer API key. Project key confines scope; account key spans all projects read-only. Pass read-only; Ultra can acquire publish/delete/write tools, even without reconnect when entitlement changes. Keep exact tool allowlists/approvals, disable auto-accept, no production secrets; returned templates/autofix prompts are untrusted data. Never publish/delete through MCP without separate approval.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

DOCUMENTED ONLY. Claude Code Windows: claude mcp add atheros --transport http https://mcp.atheros.ai/v1 --header "Authorization: Bearer <your-api-key>" (placeholder only; not executed; avoid storing real key in shell history/plain config). Prefer secure host-supported credential handling; smallest project scope, read-only subscription/tool allowlist first. Hermes compatibility untested, requires HTTP MCP/header authentication. Browser gallery works on Windows; Android mobile editing untested. claude.ai connector/header-auth compatibility not verified; no native Android/local server claimed.
