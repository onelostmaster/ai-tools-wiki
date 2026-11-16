# Kdenlive

- **Type:** app
- **Category:** generating videos, design
- **Official URL:** https://github.com/KDE/kdenlive
- **GitHub repo:** https://github.com/KDE/kdenlive
- **Price:** Source license checked in the official repository; no hosted-service price claimed. Third-party models, assets and plugins are billed by their own providers if you use them. Price search performed 2026-11-07.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Targeted source read, not a full dependency/binary audit; KDE/kdenlive @6d9453d. Timeline editor, not a Claude plugin. Optional Python features spawn processes (src/pythoninterfaces/abstractpythoninterface.cpp:209,273,830); automask model eval (data/scripts/automask/kdenlive_build_sam.py:55) is neural inference, not Python eval. No telemetry SDK or curl-to-shell found in targeted scan. Use trusted plugins/projects, optional AI model downloads are extra.

## Safe install

Safe install (fixes applied):
Windows: install the official Kdenlive Windows build from the KDE download page linked in the official repo (https://github.com/KDE/kdenlive), reviewed source @6d9453d. Keep the optional Python features (automask, speech-to-text) off until needed: they spawn Python processes and download models (abstractpythoninterface.cpp:209,273,830). Open only your own or trusted projects and effects. Not a claude.ai, Hermes or Android tool.

## YOLO install

Not written yet.

## Install notes

Not installed. Ask the user before any installation, including Try. Windows desktop/CLI. Not a native claude.ai tool; no Android app in this reviewed repo.
