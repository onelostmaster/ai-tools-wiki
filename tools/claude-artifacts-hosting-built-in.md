# Claude Artifacts (hosting, built in)

- **Type:** MCP
- **Category:** building a site
- **Official URL:** https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them
- **GitHub repo:** none (built into Claude)
- **Price:** Included on all Claude plans (Free to Enterprise); connecting apps and storing data in an artifact need Pro or higher (`support.claude.com`, checked 2026-10-31)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-14

## Safety reason

Anthropic (first-party, built into Claude; not code-reviewed): safe. Artifacts start private to you (Anthropic docs); a project app app is a private Artifact (LL hub). a project ships its ElevenLabs audio as artifact files so the API key never goes into the page (LL Lessons, 2026-10-26).

## Safe install

Safe install (fixes applied):
claude.ai: built in; turn on "Create and edit files" in Settings > Capabilities (Anthropic docs). Claude Code: built in. Keep artifacts private (the default) and never put an API key in artifact code; ship generated audio or data as artifact files instead, as a project does.

## YOLO install

Not written yet.

## Install notes

[claude.ai](http://claude.ai): built in; nothing to install. It needs 'Create and edit files' (Cloud code execution and file creation) on in Settings > Capabilities (Anthropic docs).
Claude Code: built in; nothing to install (Claude Code can publish session output as an artifact, per Anthropic's docs).
