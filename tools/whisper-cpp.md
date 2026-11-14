# whisper.cpp

- **Type:** library
- **Category:** voice and audio, a project
- **Official URL:** https://github.com/ggml-org/whisper.cpp
- **GitHub repo:** https://github.com/ggml-org/whisper.cpp @ d1be6fd (v1.9.5)
- **Price:** Free, MIT (github.com/ggml-org/whisper.cpp, checked 2026-11-07)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-07

## Safety reason

a project Claude (phase1-libraries.md §1, 2026-11-06) @ d1be6fd = v1.9.5: safe. MIT local STT; no network in the pin the project uses. User OK via PR #4. Repo/commit confirmed on github.com 2026-11-07.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Android: git submodule under android/third_party/whisper.cpp, pin v1.9.5 (d1be6fd); build into the APK through JNI as a project does.
