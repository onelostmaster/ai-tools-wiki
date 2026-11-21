# gflow-cli (ffroliva)

- **Type:** MCP
- **Category:** generating videos
- **Official URL:** https://ffroliva.github.io/gflow-cli/
- **GitHub repo:** https://github.com/ffroliva/gflow-cli @ 8f8ac2c (MIT)
- **Price:** Free, MIT (LICENSE file, checked 2026-11-20); video spends your own Google Flow credits, images count against a daily quota (README)
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Inferred (unreviewed)
- **Last checked:** 2026-11-20

## Safety reason

Not code-reviewed for safety. Unverified: the Python package and its Playwright browser automation. README (8f8ac2c) states it drives your own signed-in Google Flow session in a real Chrome window, bills your Flow credits, is not affiliated with Google, and that Google's terms apply to your account (see its DISCLAIMER and ACCOUNT_SAFETY docs) -> Contain: separate Chrome profile and a Google account you can afford to lose, pinned version. Commit and LICENSE confirmed on github.com, 2026-11-20.

## Safe install

Unreviewed: contain it: install a pinned version in its own venv (pip install gflow-cli==<reviewed version>), sign in with a separate Chrome profile on a Google account that holds nothing important, read docs/ACCOUNT_SAFETY.md first, do not use the marketplace plugin until reviewed, keep Claude Code's normal permission prompts on (never --dangerously-skip-permissions). Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Contain it: install a pinned version in its own venv (pip install gflow-cli==<reviewed version>), sign in with a separate Chrome profile on a Google account that holds nothing important, read docs/ACCOUNT_SAFETY.md first, do not use the marketplace plugin until reviewed, keep Claude Code's normal permission prompts on (never --dangerously-skip-permissions).
