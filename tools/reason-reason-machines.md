# Reason (Reason Machines)

- **Type:** plugin
- **Category:** developer tools, automation
- **Official URL:** https://reasonmachines.com
- **GitHub repo:** https://github.com/reason-machines/reason-network @ bcf045c (2026-10-30, MIT/Apache-2.0) · https://github.com/reason-machines/reason-plugins @ a6c511e (2026-10-16, MIT); the cloud agent is closed source
- **Price:** Network and plugin free; cloud sessions use Reason plan credits, no plan prices published (`reasonmachines.com`, checked 2026-11-01); your own Claude/ChatGPT plan pays for turns run on it
- **Decision:** Skip
- **Safety verdict:** unreviewed
- **Safety basis:** Code read
- **Last checked:** 2026-11-17

## Safety reason

Claude code read network @5442c8b v0.12.17, plugins @b9417b9 (2026-11-17): the daemon self-updates every 6 h, off with auto_update = false (src/daemon/update.rs:1-10, config.rs:83). Setup auto-allows only ask_user (src/setup.rs:374-387). Other agents' messages reach the model via check_inbox. Unverified: the cloud agent behind mcp.reasonmachines.com is closed -> Contain: no private repos.

## Safe install

Unreviewed: contain it: build the network daemon from source at v0.12.17, set auto_update = false; plugin only on test repos, no secrets; skip curl|bash and irm|iex. Get a review before real use.

## YOLO install

Not offered.

## Install notes

Not code-reviewed yet: ask a review bot or Claude to review it before installing.
Contain it: build the network daemon from source at v0.12.17, set auto_update = false; plugin only on test repos, no secrets; skip curl|bash and irm|iex.
