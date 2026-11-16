# Lots of Sounds (lotsofsounds)

- **Type:** plugin
- **Category:** voice and audio
- **Official URL:** https://www.lotsofsounds.com
- **GitHub repo:** https://github.com/lotsofsounds/agent-skills @ 342a2bf (MIT; the scout gave only the name; this is the vendor's own agent plugin, matching its "unpinned npx CLI")
- **Price:** Free tier (10 downloads/day, no API); Pro $15/month or $150/year; Enterprise $49/month (lotsofsounds.com, checked 2026-10-31)
- **Decision:** Skip
- **Safety verdict:** safe
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Claude code read @342a2bf (2026-11-15): safe with fixes, Skip. Only a SKILL.md that runs npx -y lotsofsounds (skills/lotsofsounds/SKILL.md:28-54), unpinned. Fix: pin the CLI version. Login is a browser device-code flow that saves the key in ~/.config/lotsofsounds; search words go to api.lotsofsounds.com. Downloads need the $15/month plan.

## Safe install

Safe install (fixes applied):
Copy the skill at 342a2bf and change each npx -y lotsofsounds to npx -y lotsofsounds@0.1.0; sign in with the device-code login or set LOTSOFSOUNDS_API_KEY in env.

## YOLO install

YOLO (your own risk): skips the pin.
/plugin marketplace add lotsofsounds/agent-skills and /plugin install lotsofsounds@lotsofsounds.

## Install notes

Ask the user before installing. Copy the skill at 342a2bf and change each npx -y lotsofsounds to npx -y lotsofsounds@0.1.0; sign in with the device-code login or set LOTSOFSOUNDS_API_KEY in env.
