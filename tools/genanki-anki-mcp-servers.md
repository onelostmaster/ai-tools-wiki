# genanki / Anki MCP servers

- **Type:** library
- **Category:** a project
- **Official URL:** https://github.com/kerrickstaley/genanki
- **GitHub repo:** [https://github.com/kerrickstaley/genanki](https://github.com/kerrickstaley/genanki)
- **Price:** Free (MIT)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-17

## Safety reason

Not code-reviewed. genanki is an open-source Python library for generating Anki decks (MIT per PyPI); the Anki MCP servers are unnamed third-party servers nobody reviewed. a project rejected both for fit, without a safety verdict.

## Safe install

Safe install (fixes applied):
Unreviewed: contain it: Claude Code (Windows): pip install genanki inside a venv (python -m venv anki-env), no keys, no network after install. Do not install any Anki MCP server: none is named or reviewed. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: `pip install genanki` (PyPI; genanki only, the Anki MCP servers are unnamed in the source).
