# awesome-ai-reverse-engineering (zhuyansen)

- **Type:** library
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://github.com/zhuyansen/awesome-ai-reverse-engineering
- **GitHub repo:** https://github.com/zhuyansen/awesome-ai-reverse-engineering @ 07255d9 (CC0-1.0 per LICENSE)
- **Price:** Free (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-21

## Safety reason

a review bot read @07255d9: safe. The repo has no code: README.md, README.zh-CN.md, data/skills.json (116 entries), LICENSE (CC0 1.0 for the list text) and an empty preview index (assets/previews/index.json is \{\}). No scripts, no workflows, no package files, no installer lines (0 npx/curl/pip/git clone lines in either README). Verified point and fix: every entry carries a grade from a third-party site (data/skills.json field security_grade; README.md:5 says each repo is 'security-graded by Agent Skills Hub (agentskillshub.top)'; 113 SAFE and 3 CAUTION badges, e.g. README.md:114,119,172); fix: treat those grades as not a review; a listed tool is used only after it has its own wiki row and review, and reverse-engineering tools only on binaries you own or may analyse.

## Safe install

Safe install (fixes applied): nothing to install. Read it on GitHub (https://github.com/zhuyansen/awesome-ai-reverse-engineering) or read data/skills.json. Ignore the list's SAFE/CAUTION badges (third-party grades, not a code review) and look up a listed repo's own wiki row before using it. All platforms (claude.ai, Claude Code, Hermes, Android, Windows): browser read only.

## YOLO install

YOLO (your own risk): skips ignoring the list's third-party grades. Trust an entry's SAFE badge (README.md:5, agentskillshub.top) and install the listed tool without a wiki review.

## Install notes

Safe: a CC0 curated list (116 entries @07255d9) of AI reverse-engineering tools (Ghidra/IDA/x64dbg MCP servers, jadx/Frida mobile tools, RE skills) with no code in the repo. Use it as a discovery list for game modding ideas. Its SAFE/CAUTION badges come from a third-party grader, not a review: check each listed repo's wiki row (e.g. ida-pro-mcp already has one) before using it.
