# pyopenjtalk-plus

- **Type:** library
- **Category:** a project, voice and audio
- **Official URL:** https://pypi.org/project/pyopenjtalk-plus/
- **GitHub repo:** [https://github.com/tsukumijima/pyopenjtalk-plus](https://github.com/tsukumijima/pyopenjtalk-plus) (listed on PyPI, checked 2026-10-31)
- **Price:** Free (MIT, per PyPI, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-01

## Safety reason

Not code-reviewed. Open-source Japanese text-to-speech, reading and accent library, a pyopenjtalk fork (MIT per PyPI). PyPI: the OpenJTalk dictionary ships in the wheel; the optional `tsqyomi` extra downloads ONNX models from Hugging Face at first use. The a project scout rejected it without a safety verdict.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Claude Code: `pip install pyopenjtalk-plus` (PyPI); `huggingface.co` is blocked in the a project sandbox.
