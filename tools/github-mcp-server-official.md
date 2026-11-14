# GitHub MCP server (official)

- **Type:** MCP
- **Category:** developer tools
- **Official URL:** https://github.com/github/github-mcp-server
- **GitHub repo:** https://github.com/github/github-mcp-server @ 3366807 (MIT; pushed 2026-11-02)
- **Price:** Free with a GitHub account
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Official vendor
- **Last checked:** 2026-11-02

## Safety reason

a review bot (light read @3366807, a review, 2026-11-02): caution. Official, but a token gives the agent wide powers over your repos (`README.md:199`), and issue or PR text can carry prompt injection. Use --read-only or GITHUB_READ_ONLY=1 (`README.md:1685-1698`) and a fine-grained token. Code not reviewed line by line.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Claude Code: use the remote server or the local binary/Docker image, in read-only mode with a fine-grained token.
Hermes: works as a plain MCP server.
Windows: Docker, binary or remote server. Android: no.
