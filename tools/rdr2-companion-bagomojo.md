# rdr2-companion (Bagomojo)

- **Type:** app
- **Category:** 3D and games, voice and audio
- **Official URL:** https://github.com/Bagomojo/rdr2-companion
- **GitHub repo:** https://github.com/Bagomojo/rdr2-companion @ 3933bb9 (MIT; committed 2026-10-31; C# ScriptHookRDR2DotNet V2 mod + local Python bridge)
- **Price:** Mod free (MIT, github.com, checked 2026-11-02); Anthropic API pay-as-you-go, about 40-50 US cents per hour of play per the README; optional ElevenLabs paid plan for a cloned voice
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-20

## Safety reason

Claude code read @3933bb9 (2026-11-20): safe with fixes. Bridge binds 127.0.0.1:7777 (bridge/server.py:58) with a per-start secret (mod/DaveCompanion.cs:945-946); packages hash-checked (bridge/setup.cmd:8); talks only to Anthropic and ElevenLabs (bridge/voice.py:129). The vault script runs PowerShell -ExecutionPolicy Bypass (bridge/keys.py:56-60) and is optional. Unverified: ScriptHookRDR2 (closed DLL) -> Contain: clean install, Story mode.

## Safe install

Safe install (fixes applied):
Windows: RDR2 on PC, Story mode only (never Red Dead Online). Install ScriptHookRDR2 only from its official site (closed-source DLL loader, not reviewed: unverified: what the loader does; contain it by using a game install with no other mods and no saved logins on that Windows account). Then ScriptHookRDR2DotNet V2, git clone https://github.com/Bagomojo/rdr2-companion, git checkout 3933bb9, run bridge\\setup.cmd (pip --require-hashes, bridge/setup.cmd:8) and bridge\\start-bridge.cmd. Put the Anthropic and ElevenLabs keys in bridge/.env (allowlisted, bridge/keys.py:21-41); skip the optional vault script, which runs PowerShell -ExecutionPolicy Bypass (bridge/keys.py:56-60). Needs an Anthropic API key with credit (Claude Pro/Max does not work). Android: no.

## YOLO install

YOLO (your own risk): skips the commit pin and the no-vault-script rule.
Windows: latest clone, setup.cmd, and the optional vault script (runs PowerShell with -ExecutionPolicy Bypass).

## Install notes

Ask the user before installing.
Windows: RDR2 on PC + ScriptHookRDR2 + ScriptHookRDR2DotNet V2, then `setup.cmd` and `start-bridge.cmd` (README); needs an Anthropic API key with credit (Claude Pro/Max does not work). Never use in Red Dead Online. Android: no.
