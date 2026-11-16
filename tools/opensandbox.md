# OpenSandbox

- **Type:** MCP
- **Category:** coding, agents
- **Official URL:** https://github.com/opensandbox-group/OpenSandbox
- **GitHub repo:** https://github.com/opensandbox-group/OpenSandbox @2e145ffb (2026-11-08 08:14 ET; original, nonfork/nonarchived; 16,637 stars observed; old alibaba/OpenSandbox API resolves to same official opensandbox-group repository)
- **Price:** Self-hosted open-source code is free under Apache-2.0 (README.md:274-276, root LICENSE). Online checked 2026-11-08: https://open-sandbox.ai/ advertises own-infrastructure Docker/Kubernetes; no managed-hosting price verified—unknown, not presumed free cloud. Your compute/storage/network, Docker/Desktop eligibility, Windows guest licence, model/API subscriptions and third-party services are separate costs. Documentation contributions CC BY 4.0 (CONTRIBUTING.md:678), distinct from Apache-2.0 code.
- **Decision:** Try
- **Safety verdict:** caution
- **Safety basis:** Code read
- **Last checked:** 2026-11-15

## Safety reason

Caution: privileged agent-execution infrastructure, NOT automatic containment. runc containers are default; stronger runtimes require separate setup (docs/guides/secure-container.md:27-53). Lifecycle default binds all interfaces, generated sample uses loopback; Docker guest ports still default 0.0.0.0 (server/opensandbox_server/config.py:611-613,1393-1402). Set API key and private ingress; no insecure YES. Omitted networkPolicy ALLOWS ALL (specs/sandbox-lifecycle.yml:2363-2372); use deny + narrow allowlist, dns+nft for packet enforcement/vault, validate runtime compatibility. Empty storage allowlist actually REJECTS host binds despite stale sample comment (config.py:920-927; services/validators.py:424-438). No home/drive-root/Docker-socket mounts. Example injects real model token into guest and installs latest Claude CLI (examples/claude-code/main.py:67-86); optional MITM Credential Vault needs trust/configuration and has memory/plaintext snapshot storage surfaces (docs/guides/credential-vault.md:19-29,55-66). Do not use bypass-permission example. MCP command tools and lifecycle hooks run arbitrary commands (sdks/mcp/sandbox/python/src/opensandbox_mcp/server.py:490; components/execd/pkg/lifecycle/runner.go:36-50). SDK metrics to own server default on (connection.py:133-137), opt out OPENSANDBOX_DISABLE_METRICS=1; external server OTLP defaults off (config.py:213-226). Build Dockerfile:35 uses curl|sh; no build/run performed. No autonomous updater found in scoped runtime; unpinned packages/images change code. Release umbrella signing/provenance gap explicitly acknowledged (README.md:249). SQLite, logs/outputs/snapshots need retention controls.; static targeted review, not sandbox-escape certification. No fix: the default runc runtime shares the host kernel, so a container escape reaches the WSL host; stronger runtimes need separate setup (docs/guides/secure-container.md lines 27-53). Contained by WSL2, no host mounts, deny network policy and local-only binding.

## Safe install

Safe install (fixes applied):
Windows only, inside WSL2 with Docker: `uv tool install opensandbox-server==1.2.1` and `uv pip install opensandbox==1.2.1` (PyPI latest on 2026-11-15, Python 3.10+), never unpinned uvx. Before the first start, edit the config: set an API key, bind the lifecycle server and Docker guest ports to 127.0.0.1 (config.py lines 611-613 and 1393-1402 default to 0.0.0.0), and give every sandbox a networkPolicy of deny plus a narrow allowlist (an omitted policy allows all, specs/sandbox-lifecycle.yml lines 2363-2372). Never mount your home folder, a drive root or the Docker socket. Set OPENSANDBOX_DISABLE_METRICS=1 (SDK metrics are on by default, connection.py lines 133-137). Don't run the claude-code example (it injects your model token and installs the latest Claude CLI, examples/claude-code/main.py lines 67-86) or any bypass-permission flag. Optional MCP: `pip install opensandbox-mcp==1.2.1` over stdio, server key from an environment variable. claude.ai and Android: no route (needs a local server). Hermes: same pinned stdio MCP, unreviewed for Hermes.

## YOLO install

YOLO (your own risk): skips the version pins, the 127.0.0.1 binding, the deny network policy and the metrics opt-out.
uvx opensandbox-server init-config ~/.sandbox.toml --example docker
uvx opensandbox-server
uv pip install opensandbox

## Install notes

CAUTION: NOT installed; show Safety reason and get explicit setup approval first. On approved Windows WSL2+Docker host with Python>=3.10 and approved uv, documented README.md\:51-68\: uvx opensandbox-server init-config ~/.sandbox.toml --example docker ; uvx opensandbox-server ; uv pip install opensandbox. These commands would install/start code: documented only, NOT RUN; edit/authenticate/harden config BEFORE server start and pin verified versions. Optional official MCP (README:220-237): pip install opensandbox-mcp ; opensandbox-mcp --domain localhost:8080 --protocol http. Prefer stdio; pass server key through approved environment/secret management, not literal CLI args or shared JSON. Do not paste insecure YES, bypass-permission flags, arbitrary image/env/mount commands or quoted remote curl/iex bootstrap. Claude Code official MCP client supported; Hermes generic MCP compatibility untested, no drop-in routing of existing agent processes. claude.ai needs an authenticated reachable remote endpoint/client support, cannot directly use this localhost stdio server. Android not a native execution host. Windows guest KVM path is separate/advanced (docs/guides/windows-sandbox.md:8-30), requires Windows media/licence and virtualization; no Mac/iPhone workflow recommended.
