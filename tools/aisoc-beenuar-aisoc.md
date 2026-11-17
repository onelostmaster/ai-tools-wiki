# AiSOC (beenuar/AiSOC)

- **Type:** app
- **Category:** security
- **Official URL:** https://github.com/beenuar/AiSOC
- **GitHub repo:** https://github.com/beenuar/AiSOC @ 0c0e6fc (MIT)
- **Price:** Free, MIT (github.com, checked 2026-11-02)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-16

## Safety reason

Claude targeted read @9074c83 = 23.4.0 (2026-11-16): safe with fixes, Skip (no need). The 66 committed .whl binaries are gone (none in the tree). Compose binds ports to AISOC_BIND_ADDR, default 127.0.0.1 (docker-compose.yml:134). The README's one-line installers pipe to iex or bash (README.md:48); the clone route skips them (line 44).

## Safe install

Safe install (fixes applied):
git clone https://github.com/beenuar/AiSOC, check out 9074c83, make up (Docker); keep AISOC_BIND_ADDR at 127.0.0.1; never the irm|iex or curl|bash line.

## YOLO install

YOLO (your own risk): skips the clone route.
Run the iwr | iex one-liner from the README.

## Install notes

Ask the user before installing.
Do not use the irm | iex installer. Claude says skip it anywhere.
Windows: not recommended. Android: no.
