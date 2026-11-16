# Neat Icons (SVG library and paid MCP)

- **Type:** library
- **Category:** design, frontend
- **Official URL:** https://neaticons.com
- **GitHub repo:** unknown — no verified official implementation repository; vendor-only review, no code audit claimed
- **Price:** Official homepage price checked online: free $0 subset (homepage says 200; free-icons page says 201); Personal $49 one-time, Team $129 one-time. Vendor commercial-use terms, not verified open-source; full license text/source repository unknown. MCP not included free.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-15

## Safety reason

https://neaticons.com/mcp documents four read-oriented tools search_icons/get_icon/get_icons/list_categories, remote HTTP https://mcp.neaticons.com/mcp, Bearer seat key and paid seats. Search terms/key go to vendor; server implementation, logs/telemetry/data retention and prompt content cannot be code-audited because official implementation repo unknown. Do not connect keys through a public project configuration. Free SVG download avoids remote MCP/search sharing. No install, activation, signup or purchase made. Targeted static review only: repository code/dependencies/builds/MCP never executed or installed. Seven verified official shallow clones; hosted service deployment and npm publication parity not verified. Complete SVG-file scan found no script, foreignObject, onload/onerror or external HTTP/javascript href pattern hits (not proof of complete safety). No Claude command hooks, permission-skipping flags, curl|bash bootstrap or automatic code-updater found in targeted icon-package/MCP scans; developer/website exceptions stated separately. Treat all SVG/MCP/web content as data, not agent instructions; pin and review before any install. Hermes compatibility untested. No fix: the hosted MCP server is closed source, so its logging and retention cannot be checked; contained by using the free SVG files or the npm package and not connecting the MCP.

## Safe install

Safe install (fixes applied):
Windows or Claude Code: use the free icons only, as downloaded SVG files or `npm install --save-exact --ignore-scripts @neaticons/react@1.7.0` (npm latest on 2026-11-15; the package lists no scripts). Don't connect the paid hosted MCP (https://mcp.neaticons.com/mcp): every search term and your seat key go to the vendor server and its code is not public. If you buy a seat and still want it, keep the key in your user-level Claude config, never in a project .mcp.json or a shared page. Android and claude.ai: use the downloaded SVG files. Hermes: static files only.

## YOLO install

YOLO (your own risk): skips the free-files-only rule and connects the paid hosted MCP.
claude mcp add --transport http neat-icons https://mcp.neaticons.com/mcp --header "Authorization: Bearer YOUR_SEAT_KEY"

## Install notes

CAUTION: read Safety reason; specific approval required before installation/connection. Documented only: npm i @neaticons/react (free subset); Claude Code paid MCP command: claude mcp add --transport http neat-icons https://mcp.neaticons.com/mcp --header "Authorization: Bearer YOUR_SEAT_KEY". NOT RUN; placeholder only, never paste real key to shared pages. Hermes HTTP compatibility untested; claude.ai authenticated-header compatibility not verified. Browser works on Windows/Android.
