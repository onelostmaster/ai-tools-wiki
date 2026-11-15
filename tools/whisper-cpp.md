# whisper.cpp

- **Type:** library
- **Category:** voice and audio, a project
- **Official URL:** https://github.com/ggml-org/whisper.cpp
- **GitHub repo:** https://github.com/ggml-org/whisper.cpp @ d1be6fd (v1.9.5)
- **Price:** Free, MIT (github.com/ggml-org/whisper.cpp, checked 2026-11-07)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a project Claude (phase1-libraries.md §1, 2026-11-06) @ d1be6fd = v1.9.5: safe. MIT local STT; no network in the pin the project uses. User OK via PR #4. Repo/commit confirmed on github.com 2026-11-07.

## Safe install

Safe install (fixes applied):
Android: git submodule at android/third_party/whisper.cpp checked out at d1be6fd (v1.9.5), built into the APK through JNI as a project does. Windows: no install; only a source build at that same commit, and only after the user OKs it for that PC.

## YOLO install

Not written yet.

## Install notes

Android: git submodule under android/third_party/whisper.cpp, pin v1.9.5 (d1be6fd); build into the APK through JNI as a project does.
