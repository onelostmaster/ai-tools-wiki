# RVC WebUI (Retrieval-based Voice Conversion)

- **Type:** app
- **Category:** voice and audio
- **Official URL:** https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI
- **GitHub repo:** https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI @ 81eed5e (MIT; last push 2026-08-04)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read @81eed5e (2026-11-17): safe with fixes. The UI listens on 0.0.0.0 with no auth (webui.py:128). Voice .pth files load with torch.load (infer/vc/modules.py:174); the CPU/DirectML set pins torch 2.4.1 (requirments_cpu_py312.txt:15), so a shared voice model runs pickle code. Fix: block inbound for its python, use only voices you trained. Clone only voices with consent.

## Safe install

Safe install (fixes applied):
Windows: launch go-webui.bat; New-NetFirewallRule -DisplayName "RVC block inbound" -Direction Inbound -Program "<RVC folder>\\runtime\\python.exe" -Action Block; train your own voices, never load downloaded .pth; consent for every voice.

## YOLO install

YOLO (your own risk): skips the firewall rule and the own-voices rule.
Load community voice models with the UI open on your LAN.

## Install notes

Ask the user before installing.
Windows: ships Windows launchers and DirectML for AMD/Intel GPUs (README.md:53).
