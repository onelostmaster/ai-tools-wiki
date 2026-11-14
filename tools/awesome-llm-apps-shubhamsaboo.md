# awesome-llm-apps (Shubhamsaboo)

- **Type:** library
- **Category:** research, developer tools
- **Official URL:** https://github.com/Shubhamsaboo/awesome-llm-apps
- **GitHub repo:** https://github.com/Shubhamsaboo/awesome-llm-apps @ 6c16b23 (Apache-2.0; 178 app and tutorial folders + 8 agent skills; committed 2026-10-21)
- **Price:** Free, Apache-2.0 (github.com, checked 2026-11-02); each app needs paid model keys (OpenAI, Gemini, Anthropic) and often a paid API
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code scan of the whole repo @6c16b23, a review, 2026-11-02): safe to read and learn from. No real keys or telemetry in its own code. Know before running a folder: postinstall `npm run install:agent` in 4 generative-UI apps; ai-shadcn-component-generator ships `.claude/settings.json` (Render plugin) and an unpinned shadcn MCP in `.mcp.json`; beifong runs stored commands with shell=True (`beifong/scheduler.py:97-99`).

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Safe, but ask the user before installing.
Windows: read folders in a browser; run one only after reading it (Python or Node, your own API keys). Claude Code: open a single folder, not the whole repo. Android: read only.
