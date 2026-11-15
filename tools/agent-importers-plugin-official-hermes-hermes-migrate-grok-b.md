# agent-importers plugin (official Hermes, hermes migrate grok-bot)

- **Type:** plugin
- **Category:** Hermes add-ons
- **Official URL:** https://github.com/NousResearch/hermes-official-plugins/tree/main/agent-importers
- **GitHub repo:** https://github.com/NousResearch/hermes-official-plugins @ 471acd3 (folder `agent-importers`, plugin v1.2.1, HEAD on 2026-11-02; repo MIT, not a fork); started by `hermes migrate grok-bot` in NousResearch/hermes-agent @ 5e7c2b25
- **Price:** Free, open source (MIT; `github.com`, checked 2026-11-02). Model costs depend on your Hermes provider.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read @471acd3 + hermes-agent @5e7c2b25, Hermes a review, 2026-11-02): Looks safe. Pinned catalog install, no tools or hooks; no network calls (`grok_bot.py:18`); only subprocess is a clipboard read (`668-681`); secret-looking export keys refused and tokens redacted (`146-155`, `246-266`); routines imported paused. Reads the Grok Bot app UI cache, not logins or cookies. Imported text becomes trusted Hermes context: read the preview.

## Safe install

Safe install (fixes applied):
Hermes (Windows or the a project container): `hermes plugins install agent-importers` once per profile (official docs, import-from-other-agents.md), then `hermes -p <profile> migrate grok-bot --dry-run` first (writes nothing). Check the export has no keys or personal details, run it again without --dry-run, read the preview and confirm. Imported routines come in paused: turn the Grok Bot routine off before `hermes cron resume <id>`.

## YOLO install

Not written yet.

## Install notes

Hermes: run `hermes migrate grok-bot --dry-run` first (writes nothing), paste the printed prompt into the Bot, save its JSON export, then run `hermes migrate grok-bot` again, read the preview and confirm. Turn the Grok routine off before `hermes cron resume <id>` (the id Hermes lists for the imported job). Check the export has no personal details or keys. Ask the user before running anything.
Profiles (official docs: hermes-agent website/docs/user-guide/import-from-other-agents.md, read by the wiki 2026-11-02): install the plugin once per profile with `hermes plugins install agent-importers`; import a Bot into its own profile with `hermes -p <profile>` (<profile> = that Bot's Hermes profile name), because without -p it lands in the default profile; a downloaded export is imported with `hermes import-agent grok-bot --source <file>`.
