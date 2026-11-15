# llama.cpp

- **Type:** library
- **Category:** a project, research
- **Official URL:** https://github.com/ggml-org/llama.cpp
- **GitHub repo:** https://github.com/ggml-org/llama.cpp @ 67107ac (b12164)
- **Price:** Free, MIT (github.com/ggml-org/llama.cpp, checked 2026-11-07)
- **Decision:** Install
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a project Claude (phase1-libraries.md §2, 2026-11-06) @ 67107ac = b12164: safe. MIT local inference; pin used for on-device translate. User OK via PR #4. Repo/commit confirmed on github.com 2026-11-07.

## Safe install

Safe install (fixes applied):
Android: git submodule at android/third_party/llama.cpp checked out at 67107ac (b12164), built through JNI as a project does. Windows: no install; only a source build at that same commit, and only after the user OKs it for that PC.

## YOLO install

Not written yet.

## Install notes

Android: git submodule under android/third_party/llama.cpp, pin b12164 (67107ac); build through JNI as a project does.
Windows: follow the repo README for desktop builds.
