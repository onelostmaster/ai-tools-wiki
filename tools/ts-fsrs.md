# ts-fsrs

- **Type:** library
- **Category:** a project
- **Official URL:** https://github.com/open-spaced-repetition/ts-fsrs
- **GitHub repo:** https://github.com/open-spaced-repetition/ts-fsrs @ f582c1d (2026-10-29; packages/fsrs is version 6.0.0, the npm latest; MIT; repo confirmed via the npm package ts-fsrs)
- **Price:** Free (MIT, per the source and npm)
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-02

## Safety reason

a review bot (code read of packages/fsrs and packages/srs-kit @f582c1d, ts-fsrs 6.0.0, 2026-11-02): Looks safe. Pure scheduling maths: no fetch, eval, new Function, child_process, WebSocket or telemetry in either src/. The only environment read is an optional rounding flag (fsrs/src/help.ts:8). No install scripts; the npm package ships dist and docs only, with one dependency (srs-kit). MIT. The optional Rust optimizer binding was not reviewed.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: `npm install ts-fsrs` (npm); in the a project container, npm installs last one session.
Note: the reviewed code is ts-fsrs 6.0.0 (npm latest on 2026-11-02) plus its one dependency @open-spaced-repetition/srs-kit 1.0.0. The optional native optimizer (@open-spaced-repetition/binding, Rust) is a separate package and was not reviewed.
