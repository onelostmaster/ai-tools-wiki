# chorono-editor (codie1982)

- **Type:** app
- **Category:** generating videos, editing
- **Official URL:** https://github.com/codie1982/chorono-editor
- **GitHub repo:** https://github.com/codie1982/chorono-editor @ 4e0e8ff (package 0.2.0; MIT; committed 2026-11-08 13:31 ET, HEAD on 2026-11-10)
- **Price:** Free, MIT (github.com, checked 2026-11-09)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

a review bot (code read @4e0e8ff, 2026-11-10, no-intake review): Safe for local use. Next.js 14 editor plus a Node CLI. MCP route src/app/api/mcp/route.ts lines 12-23 and 54-67: off unless CHORONO_MCP_ENABLED=1, loopback Host only, same-origin checks, bounded body, and a random 64-hex bearer token (src/lib/mcp/storage.ts lines 9-21) for tool calls. CLI packages/cli/lib/editor.mjs: spawns git and npm with shell:false (line 20), clones its own repo only when no checkout exists (lines 133-137), and starts next on 127.0.0.1 (line 205); never kills a busy port (line 150). Things to know: the Script console runs your own JavaScript with new Function, not a sandbox (src/lib/script/ScriptRunner.ts line 61), so paste only scripts you trust; /api/ai (src/app/api/ai/route.ts lines 70-80, providers.ts line 191) lets a request pick the custom endpoint URL and borrows CUSTOM_AI_KEY, which matters only if the server is reachable from your network (plain npm run dev), so use chorono start. Anthropic and OpenAI URLs are hardcoded. Not reviewed: scripts/perf/, the React UI and dependencies.

## Safe install

Safe install (fixes applied):
Windows (Node.js 20+, Git) in PowerShell, pinned to the reviewed commit (main is now a4d4e64, not reviewed): git clone https://github.com/codie1982/chorono-editor.git; git checkout 4e0e8ff; npm ci; npm run cli:build; npm run chorono -- setup --agent claude-code (only Claude Code, Codex and Claude Desktop settings untouched); npm run chorono -- start --background --open (serves on 127.0.0.1 only, editor/cli line 205). Never use npm run dev, npm start or reset-and-run.sh (the first two listen on the whole network and leave /api/ai able to borrow CUSTOM_AI_KEY; the script force-kills port 2000). Paste only your own scripts into the Script console (new Function, ScriptRunner.ts line 61). MCP bridge: native Windows refuses the token file (storage.ts line 18 needs mode 0600, which Windows cannot report), so for the Claude Code MCP workflow run the same steps inside WSL. Any CUSTOM_AI_KEY goes in .env.local only. claude.ai, Hermes and Android: no install route.

## YOLO install

YOLO (your own risk): skips the commit pin and the 127.0.0.1 start command.
git clone https://github.com/codie1982/chorono-editor.git
npm install
npm run dev

## Install notes

Code-reviewed by a review bot @4e0e8ff (package 0.2.0) (safe). Windows (Node.js 20+, Git) in PowerShell: git clone https://github.com/codie1982/chorono-editor.git, then git checkout 4e0e8ff to stay on the reviewed commit, then npm ci, npm run cli:build, npm run chorono -- setup --agent claude-code (only Claude Code, so it does not touch Codex or Claude Desktop settings), then npm run chorono -- start --background --open. The chorono start command serves the editor on 127.0.0.1 only. Skip npm run dev, npm start and reset-and-run.sh: the first two listen on your whole network, and the .sh script force-kills whatever is on port 2000 (and is bash-only). npm run dev:mcp also won't work in PowerShell (it uses Unix-style env syntax). The local MCP workflow needs no AI key. If you ever use the built-in chat with a CUSTOM_AI_KEY, keep it in .env.local, never in chat. On native Windows the MCP bridge refuses its own token file: src/lib/mcp/storage.ts line 18 rejects any token file whose mode has group or other bits, and Node on Windows reports writable files as 0o666 (Node fs docs: on Windows only the write permission can be changed). So the editor runs on Windows, but the MCP bridge for Claude Code works only inside WSL.
