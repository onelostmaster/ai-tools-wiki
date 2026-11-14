# rdr2-companion (Bagomojo)

- **Type:** app
- **Category:** 3D and games, voice and audio
- **Official URL:** https://github.com/Bagomojo/rdr2-companion
- **GitHub repo:** https://github.com/Bagomojo/rdr2-companion @ 3933bb9 (MIT; committed 2026-10-31; C# ScriptHookRDR2DotNet V2 mod + local Python bridge)
- **Price:** Mod free (MIT, github.com, checked 2026-11-02); Anthropic API pay-as-you-go, about 40-50 US cents per hour of play per the README; optional ElevenLabs paid plan for a cloned voice
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-03

## Safety reason

a review bot (code read @3933bb9, a review, 2026-11-02): repo code is clean, caution for what it depends on. Bridge listens on 127.0.0.1:7777 only (`bridge/server.py:58`) and needs a per-start secret (`mod/DaveCompanion.cs:944`); network out only to Anthropic and ElevenLabs (`bridge/voice.py:128-135`); hash-pinned packages (`setup.cmd:7`); .env allowlist (`bridge/keys.py:21-41`). Needs ScriptHookRDR2, a closed-source DLL loader not reviewed; optional vault script runs PowerShell -ExecutionPolicy Bypass (`keys.py:56-60`). Story mode only, never Red Dead Online.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Caution: read the Safety reason and ask the user before installing.
Windows: RDR2 on PC + ScriptHookRDR2 + ScriptHookRDR2DotNet V2, then `setup.cmd` and `start-bridge.cmd` (README); needs an Anthropic API key with credit (Claude Pro/Max does not work). Never use in Red Dead Online. Android: no.
