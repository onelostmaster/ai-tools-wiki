# pyopenjtalk-plus

- **Type:** library
- **Category:** a project, voice and audio
- **Official URL:** https://pypi.org/project/pyopenjtalk-plus/
- **GitHub repo:** [https://github.com/tsukumijima/pyopenjtalk-plus](https://github.com/tsukumijima/pyopenjtalk-plus) (listed on PyPI, checked 2026-10-31)
- **Price:** Free (MIT, per PyPI, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-17

## Safety reason

Not code-reviewed. Open-source Japanese text-to-speech, reading and accent library, a pyopenjtalk fork (MIT per PyPI). PyPI: the OpenJTalk dictionary ships in the wheel; the optional `tsqyomi` extra downloads ONNX models from Hugging Face at first use. A project scout rejected it without a safety verdict.

## Safe install

Safe install (fixes applied):
Unreviewed: contain it: pip install pyopenjtalk-plus==<pinned version> only inside a throwaway virtual environment or devcontainer with no API keys in its environment; do not install the tsqyomi extra (it downloads ONNX models from Hugging Face at first use, PyPI); the base wheel ships its own dictionary so it needs no network after install. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: `pip install pyopenjtalk-plus` (PyPI); `huggingface.co` is blocked in a project sandbox.
