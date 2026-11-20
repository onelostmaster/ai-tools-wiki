# awesome-reverse-engineering (morluto)

- **Type:** library
- **Category:** security, 3D and games, developer tools
- **Official URL:** https://github.com/morluto/awesome-reverse-engineering
- **GitHub repo:** https://github.com/morluto/awesome-reverse-engineering @ b32dcde (CC0-1.0; last commit 2026-11-15, checked on github.com 2026-11-19)
- **Price:** Free, CC0-1.0 (github.com, checked 2026-11-19)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

a review bot code read: safe as a reading list with fixes. README.md is a CC0-1.0 link list (LICENSE) with no install step. The repo also ships runnable example checks in examples/resource-intake/: verify.py pip-installs 12 reverse-engineering packages from requirements.txt (versions pinned, no hashes), downloads the Vineflower and CFR jars and the hermes-compiler npm tarball (verify.py:26-38, each SHA-256 checked at :99, :463, :603) and runs node, javac/java and hermesc on its own fixtures (verify.py:86-142, 466-479, 607-612); pylingual/run.py:34 exec()s decompiled output of its own fixture and :46-47 runs uv run --python, which downloads Python builds. Fix: read README.md only and do not run the examples or tests on your own machine. The linked tools (about 225 links) are not vetted by this review; each needs its own wiki row and review.

## Safe install

Safe install (fixes applied): nothing to install. Read https://github.com/morluto/awesome-reverse-engineering in a browser on Windows or Android (claude.ai: paste the README link for reading). Do not clone-and-run examples/resource-intake/verify.py, pylingual/run.py or tests/ (they pip-install unhashed packages, download jars/compilers and run them). Before using any linked tool, check its own wiki row; tools without one need a review first. Claude Code and Hermes: read-only use of README.md only.

## YOLO install

YOLO (your own risk): skips the no-run rule: in a throwaway venv, python -m pip install -r examples/resource-intake/requirements.txt then python examples/resource-intake/verify.py (needs Node and JDK 17; downloads hash-checked jars and hermes compilers).

## Install notes

Safe as a reading list with the fix applied (read README.md only; don't run examples/ or tests/). Curated reverse-engineering links (binary analysis, debugging, firmware, file formats, AI analysis, practice), useful for game modding on games you own.
Official repo: https://github.com/morluto/awesome-reverse-engineering (CC0-1.0). Linked tools are not covered by this review.
