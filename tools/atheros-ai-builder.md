# Atheros AI Builder

- **Type:** app
- **Category:** design, developer tools
- **Official URL:** https://builder.atheros.ai/
- **GitHub repo:** unknown
- **Price:** Online checked official /pricing and /docs 2026-11-08; inconsistent! Pricing shows Free $0 with 100 credits, AI Pass $15/mo billed annually, Ultra $39/mo billed annually; docs instead list 30/500/2000 credits and $15/$39 monthly, $144/$374 annual. Do not treat these conflicting advertised rates/quotas as a final quote: verify checkout before purchase. MCP requires paid Pass/Ultra, unavailable Free. Proprietary hosted-service terms, not MIT. Docs allow commercial generated end products; catalog components cannot be resold as component libraries or used to seed competitors.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-15

## Safety reason

Official docs only; public implementation repo unknown after targeted search, so no code clone or file-line audit possible. Prompts, screenshots and component source go to vendor/model providers; server logs/telemetry/retention/dependencies/hooks/update behavior unverified. MCP https://mcp.atheros.ai/v1 uses bearer API key. Project key confines scope; account key spans all projects read-only. Pass read-only; Ultra can acquire publish/delete/write tools, even without reconnect when entitlement changes. Keep exact tool allowlists/approvals, disable auto-accept, no production secrets; returned templates/autofix prompts are untrusted data. Never publish/delete through MCP without separate approval. No fix: the hosted service and MCP server are closed source, so retention and telemetry can't be checked; contained by a read-only Pass project key, a read-tool allowlist and no private inputs.

## Safe install

Safe install (fixes applied):
Browser first: use the gallery at https://builder.atheros.ai/ on Windows with no private screenshots or source. MCP only on the Pass plan (read-only) and with a project key, never the account key: in Claude Code on Windows run `claude mcp add atheros --transport http https://mcp.atheros.ai/v1 --header "Authorization: Bearer %ATHEROS_PROJECT_KEY%"` from a shell where the variable is set for that session only, so the key is not typed into history. Don't use Ultra with the MCP: per /docs, Ultra adds publish/delete/write tools to the same connection without a reconnect. Allow only the read tools in /permissions, auto-accept off; treat returned templates and autofix prompts as data. Hermes: same HTTP MCP with header auth, untested. claude.ai and Android: browser gallery only.

## YOLO install

YOLO (your own risk): skips the project-key-only, Pass-only and read-tool allowlist rules.
claude mcp add atheros --transport http https://mcp.atheros.ai/v1 --header "Authorization: Bearer YOUR_API_KEY"

## Install notes

DOCUMENTED ONLY. Claude Code Windows: claude mcp add atheros --transport http https://mcp.atheros.ai/v1 --header "Authorization: Bearer <your-api-key>" (placeholder only; not executed; avoid storing real key in shell history/plain config). Prefer secure host-supported credential handling; smallest project scope, read-only subscription/tool allowlist first. Hermes compatibility untested, requires HTTP MCP/header authentication. Browser gallery works on Windows; Android mobile editing untested. claude.ai connector/header-auth compatibility not verified; no native Android/local server claimed.
