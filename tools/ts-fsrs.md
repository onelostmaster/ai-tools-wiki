# ts-fsrs

- **Type:** library
- **Category:** a project
- **Official URL:** https://github.com/open-spaced-repetition/ts-fsrs
- **GitHub repo:** https://github.com/open-spaced-repetition/ts-fsrs @ f582c1d (2026-10-29; packages/fsrs is version 6.0.0, the npm latest; MIT; repo confirmed via the npm package ts-fsrs)
- **Price:** Free (MIT, per the source and npm)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-14

## Safety reason

a review bot (code read of packages/fsrs and packages/srs-kit @f582c1d, ts-fsrs 6.0.0, 2026-11-02): Looks safe. Pure scheduling maths: no fetch, eval, new Function, child_process, WebSocket or telemetry in either src/. The only environment read is an optional rounding flag (fsrs/src/help.ts:8). No install scripts; the npm package ships dist and docs only, with one dependency (srs-kit). MIT. The optional Rust optimizer binding was not reviewed.

## Safe install

Safe install (fixes applied):
Claude Code (Windows) or a project container: `npm install ts-fsrs@6.0.0 --save-exact` (the reviewed version, still the npm latest on 2026-11-14; its one dependency @open-spaced-repetition/srs-kit is pinned at 1.0.0 by ts-fsrs itself, npm view). Do not add the optional native optimizer @open-spaced-repetition/binding: it is a separate package nobody has reviewed. No keys or network needed at runtime (no fetch or telemetry in src/, per the code read). claude.ai, Hermes and Android: it is a code library, use it inside a project, no install route.

## YOLO install

YOLO (your own risk): skips the exact pin and allows the unreviewed native optimizer.
npm install ts-fsrs @open-spaced-repetition/binding

## Install notes

Claude Code: `npm install ts-fsrs` (npm); in a project container, npm installs last one session.
Note: the reviewed code is ts-fsrs 6.0.0 (npm latest on 2026-11-02) plus its one dependency @open-spaced-repetition/srs-kit 1.0.0. The optional native optimizer (@open-spaced-repetition/binding, Rust) is a separate package and was not reviewed.
