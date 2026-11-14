# ElevenLabs sound-effects plugin (official Hermes)

- **Type:** plugin
- **Category:** Hermes add-ons, voice and audio
- **Official URL:** https://github.com/NousResearch/hermes-official-plugins/tree/main/elevenlabs-sound-effects
- **GitHub repo:** [https://github.com/NousResearch/hermes-official-plugins](https://github.com/NousResearch/hermes-official-plugins)
- **Price:** Free plugin; uses ElevenLabs credits
- **Decision:** Try
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-10-31

## Safety reason

a review bot (code spot-check, a review, 2026-10-28): Looks safe. Official Nous plugin; it only calls `api.elevenlabs.io` and converts locally with ffmpeg using list args.

## Safe install

Not written yet: use Install notes and the fixes in the Safety reason.

## YOLO install

Not written yet.

## Install notes

Hermes: `hermes plugins install elevenlabs-sound-effects`; it uses your ElevenLabs credits, so keep the key in Hermes secrets and never paste it into chat.
