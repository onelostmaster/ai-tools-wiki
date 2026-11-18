# rdr2-companion (Bagomojo)

- **Type:** app
- **Category:** 3D and games, voice and audio
- **Official URL:** https://github.com/Bagomojo/rdr2-companion
- **GitHub repo:** https://github.com/Bagomojo/rdr2-companion @ 3933bb9 (MIT; committed 2026-10-31; C# ScriptHookRDR2DotNet V2 mod + local Python bridge)
- **Price:** Mod free (MIT, github.com, checked 2026-11-02); Anthropic API pay-as-you-go, about 40-50 US cents per hour of play per the README; optional ElevenLabs paid plan for a cloned voice
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

a review bot (code read @3933bb9, a review, 2026-11-02): repo code is clean, caution for what it depends on. Bridge listens on 127.0.0.1:7777 only (`bridge/server.py:58`) and needs a per-start secret (`mod/DaveCompanion.cs:944`); network out only to Anthropic and ElevenLabs (`bridge/voice.py:128-135`); hash-pinned packages (`setup.cmd:7`); .env allowlist (`bridge/keys.py:21-41`). Needs ScriptHookRDR2, a closed-source DLL loader not reviewed; optional vault script runs PowerShell -ExecutionPolicy Bypass (`keys.py:56-60`). Story mode only, never Red Dead Online.

## Safe install

Safe install (fixes applied):
Windows: RDR2 on PC, Story mode only (never Red Dead Online). Install ScriptHookRDR2 only from its official site (closed-source DLL loader, not reviewed: unverified: what the loader does; contain it by using a game install with no other mods and no saved logins on that Windows account). Then ScriptHookRDR2DotNet V2, git clone https://github.com/Bagomojo/rdr2-companion, git checkout 3933bb9, run setup.cmd (hash-pinned packages, setup.cmd:7) and start-bridge.cmd. Put the Anthropic and ElevenLabs keys in bridge/.env (allowlisted, bridge/keys.py:21-41); skip the optional vault script, which runs PowerShell -ExecutionPolicy Bypass (bridge/keys.py:56-60). Needs an Anthropic API key with credit (Claude Pro/Max does not work). Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin and the no-vault-script rule.
Windows: latest clone, setup.cmd, and the optional vault script (runs PowerShell with -ExecutionPolicy Bypass).

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: RDR2 on PC + ScriptHookRDR2 + ScriptHookRDR2DotNet V2, then `setup.cmd` and `start-bridge.cmd` (README); needs an Anthropic API key with credit (Claude Pro/Max does not work). Never use in Red Dead Online. Android: no.
