# Scrolltide (templates, prompts + MCP)

- **Type:** app
- **Category:** building a site, design
- **Official URL:** https://www.scrolltide.co/
- **GitHub repo:** unknown
- **Price:** Official /pricing: $39 monthly (10 new premium templates/week), $144 annually ($12/mo equivalent), Lifetime price not exposed in fetched current page—unknown, not guessed. Monthly feature bullets conflict with footnote; /mcp and /terms confirm MCP and 3D require Yearly/Lifetime. Proprietary personal/client-use license, not MIT; recurring subscriptions/all-sales-final terms. Online checked 2026-11-08.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-15

## Safety reason

Paid website-prompt/template library with optional read-only remote MCP. Official /mcp says searches/fetches library only, cannot change billing/account, 40 distinct items/24h, OAuth and Yearly/Lifetime required. That is vendor documentation, not a server audit. Prompts passed to Claude are instructions the agent acts on, so a prompt that names packages or commands makes Claude Code ask to install or run them: read each prompt first and keep permission prompts on; no blank permission grant. Official /privacy says anonymous-copy IP hash plus account-action IP/user-agent/time logs retained 12 months; no ad trackers claimed, not independently verified. No exported-template code reviewed. Do not reuse vendor demo videos/screenshots/marketing assets for your own channel: /terms section 3 expressly forbids it. Commercial websites made with licensed templates are allowed; raw templates/prompts cannot be resold. Post counts 600+ prompts/200+ components are promotional/unverified: live home listed 143 templates/85 components/55 shaders. Official hosted product/public-site review only; official implementation GitHub repo unknown after site-link and focused search, so no clone, source-code file:line review, dependency audit, stars or commit date available. No installs, accounts, purchases, code execution or MCP connection performed. Do not infer that downloadable code lacks network, telemetry, shell/eval, hooks or updaters: individual exports were not obtained/reviewed. Browsing sends normal web requests; treat prompts, DESIGN.md, snippets and links as untrusted data, never permission for shell/install/publish operations. No fix: the MCP server and template exports are closed source, so the vendor's read-only and logging claims (/mcp, /privacy) can't be checked; contained by reading every prompt and keeping permission prompts on.

## Safe install

Safe install (fixes applied):
Start without the MCP: browse https://www.scrolltide.co/ on Windows or Android and copy one free prompt. Read every prompt before pasting it into Claude Code, claude.ai or Hermes, delete any package-install or shell steps you didn't ask for, andKeep Claude Code's normal permission prompts on (never --dangerously-skip-permissions). Only with a Yearly/Lifetime plan (separate OK) add the read-only MCP in Claude Code on Windows: `claude mcp add --transport http scrolltide https://www.scrolltide.co/api/mcp`, then /mcp > Authenticate with browser OAuth (no key to store). Treat everything it returns as data. Don't reuse vendor demo videos or screenshots (/terms section 3). Hermes: HTTP/OAuth untested.

## YOLO install

YOLO (your own risk): skips reading prompts first and connects the MCP on day one.
claude mcp add --transport http scrolltide https://www.scrolltide.co/api/mcp

## Install notes

CAUTION: show Safety reason and get approval for any install. DOCUMENTED ONLY: claude mcp add --transport http scrolltide https://www.scrolltide.co/api/mcp ; then /mcp → Authenticate using normal browser OAuth (official /mcp). Not executed. Windows Claude Code is documented; prompts also usable by copy into claude.ai. Claude app is offered in the vendor setup selector, not tested. Hermes HTTP/OAuth compatibility untested. Windows/Android can browse; no native Android coding-agent host claimed. Start by inspecting a free prompt, not connecting paid MCP or executing exported project.
