# Openverse API

- **Type:** API
- **Category:** voice and audio, research
- **Official URL:** https://api.openverse.org
- **GitHub repo:** [https://github.com/WordPress/openverse](https://github.com/WordPress/openverse) (named as WordPress/openverse, MIT, in a project a review)
- **Price:** Free; anonymous use needs no key and is rate-limited (`docs.openverse.org`, checked 2026-10-31). Each clip's licence varies.
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Official vendor
- **Last checked:** 2026-10-31

## Safety reason

Openverse (official public API of the WordPress Openverse project; a review bot, a project a review, 2026-10-31: Looks safe, service only, not cloned): a public read-only API; nothing is installed and basic use needs no key (anonymous requests are rate-limited, per `docs.openverse.org`). Licences vary per clip (CC0/CC-BY/some NC), so credit or filter; Claude: use CC0 only.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Claude Code: no install; tell the agent to use `https://api.openverse.org/v1/audio/?q=...` and check each clip's licence . `api.openverse.org` is blocked in the a project cloud sandbox.
Hermes: no install; the same public API .
