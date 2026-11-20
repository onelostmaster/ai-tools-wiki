# underthesea

- **Type:** library
- **Category:** a project
- **Official URL:** https://undertheseanlp.com/
- **GitHub repo:** https://github.com/undertheseanlp/underthesea @ 22bdc17 (9.5.0; underthesea_core source in extensions/underthesea_core; confirmed on github.com 2026-11-19)
- **Price:** Free (underthesea Apache-2.0; underthesea_core declares GPL-3.0 in Cargo.toml:7 but Apache-2.0 on PyPI; checked 2026-11-19)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-19

## Safety reason

a review bot code read: safe with the fixes in Safe install. The functions a project wants run offline on model files shipped inside the wheel: word_tokenize loads the bundled CRF model ws_crf_vlsp2013_20230727 from the package folder (underthesea/pipeline/word_tokenize/__init__.py:41-45), viet2ipa is pure Python rules (pipeline/ipa/__init__.py:1-33), restore_diacritics reads the bundled rd_model_2026_08_19.bin (pipeline/restore_diacritics/restorer.py:16,47-49). No telemetry or analytics code found (searched the package for telemetry, analytics, posthog, sentry). underthesea_core is Rust with no process, network or socket calls in src/. Verified behaviour and fixes: (1) model and dataset downloads (underthesea download-model / download-data, and functions that need them such as dependency_parse, classify, sentiment, lang_detect, translate, tts) fetch files from GitHub releases, dl.fbaipublicfiles.com and Hugging Face with no checksum check (file_utils.py:84 requests.get, models.yaml:49,57) and load torch checkpoints with weights_only=False (models/model.py:64, modules/nn.py:32), which runs pickled code from the file; fix: use only word_tokenize, viet2ipa, sent_tokenize, text_normalize and restore_diacritics and don't run the download commands. (2) The agent module's default_tools include a shell tool (subprocess with shell=True, agent/default_tools.py:207) and a python tool that exec()s code (agent/default_tools.py:284), guarded only by a short blocklist; underthesea agent runs npm install (cli.py:134,139); agent calls write traces to ~/.underthesea/traces by default (agent/agent.py:41-55); fix: don't use underthesea.agent or the agent/chat/wiki CLI commands and don't install the [agent-server], [prompt], [deep], [voice] or [trace] extras (importing underthesea still imports the agent code, __init__.py:36-50, but nothing runs until called). (3) Licence: underthesea is Apache-2.0 (pyproject.toml), but underthesea_core declares GPL-3.0 in extensions/underthesea_core/Cargo.toml:7 while its PyPI page says Apache-2.0; fix: treat underthesea_core as GPL-3.0 if you ever ship code that bundles it (personal study use is unaffected).

## Safe install

Safe install (fixes applied): Claude Code on Windows or a project container (Python 3.10-3.14), in a venv: py -m venv .venv then .venv\\Scripts\\pip install --only-binary=\:all\: underthesea==9.5.0 underthesea_core==3.3.2 (Linux: python3 -m venv .venv && .venv/bin/pip install --only-binary=\:all\: underthesea==9.5.0 underthesea_core==3.3.2). Check the two wheel hashes first (pip download --no-deps --only-binary=\:all\: underthesea==9.5.0 underthesea_core==3.3.2 -d wheels, then PowerShell Get-FileHash <file> -Algorithm SHA256): underthesea-9.5.0-py3-none-any.whl 81400f41b75ceff6f80c52b4ad043806c80f5899ec555d8e6374d468a59bce56; underthesea_core-3.3.2-cp312-cp312-win_amd64.whl c003ea761dddaf8cb502fdd4cace58a53797083cfaac8fce2b5b2877a479c4e5; cp313 win_amd64 906437c03216a7a816067fd05792dfd56c58655cd80070a591d9c6952a822fbf; cp312 manylinux x86_64 a80ddbedbb3e2092ea9a5c3fba09fb1c66c5ebbc7695c42a4b789933ef58f99b (PyPI digests, checked 2026-11-19). No extras. Use only word_tokenize, viet2ipa (from underthesea.pipeline.ipa import viet2ipa), sent_tokenize, text_normalize and restore_diacritics; don't run underthesea download-model, download-data, agent, chat or wiki, and don't call dependency_parse, classify, sentiment, lang_detect, translate or tts. No API keys in the venv; no network needed after install. claude.ai and Android: not installable; use its output (segmented words, IPA) in cards. Hermes: same venv steps on the Hermes host.

## YOLO install

YOLO (your own risk): skips the hash check, version pins and function limits: pip install underthesea (latest, any extras), and use download-model, deep models and the agent as documented.

## Install notes

Safe with the fixes in Safe install applied. Vietnamese word splitting (word_tokenize) and Northern or Southern IPA with tone numbers (viet2ipa, dialect="north") from bundled models, offline.
Official docs: https://undertheseanlp.com/ and https://github.com/undertheseanlp/underthesea. In a project container, pip installs last one session.
