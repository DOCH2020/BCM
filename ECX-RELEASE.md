# BCM ECX Node release gates

The existing personal deployment is operational. That is not yet proof that a
new owner's Umbrel can install this app. Do not promote this draft into the
catalog until the following work is complete.

## Completed in isolated development tests

- Clean private AMD64 image built and OCI-audited, with pool unit suites and
  seven in-image checks passing. No public image is available yet.
- Browser first-run setup validates an owner-provided address against the node
  and keeps settings across process restarts. Synthetic RPC tests cover owner
  isolation and rejection of invalid or repeated setup requests.
- SOLO only, zero pool fee, separate services, authenticated app-proxy package
  contract, persistent data directories, and graceful shutdown configuration.
- Five local browser workflows and twelve setup/package tests passed. These
  do not exercise a real Umbrel proxy or lifecycle.
- Read-only destination capacity/interface/port preflight and fresh-report LAN
  rendering gate, with three synthetic regression groups passing. No real
  destination has been qualified; owner-facing selection remains unfinished.

## Remaining release gates

- Resolve enforcer redistribution terms; the bounded pinned-source review did
  not establish a license grant. Do not publish its executable until resolved.

- Retain the configured repository/support URLs, store prefix `bcm` and stable
  app ID `bcm-ecx` when generating the final versioned install manifest.
- Preserve the clean-image source provenance and dependency/license notices.
  Do not reuse image layers containing personal configuration.
- Publish version-tagged images pinned by digest in a public registry. No
  `latest`, local Docker image IDs, private credentials or runtime Compose builds.
- Verify the existing first-run configuration and persistent settings through
  real Umbrel authentication over HTTP and HTTPS. No bundled payout fallback.
- Verify that the persistent settings, chain, ledger and best-share history
  survive real Umbrel restarts, upgrades and storage relocation.
- Retain authenticated `app_proxy` and loopback-only administrative endpoints.
  No Docker socket, host networking or privileged containers.
- Finish owner-facing LAN interface selection and run destination preflight
  for ports 8088, 3334 and 3335 immediately before installation. Never displace
  another installed app or take over the existing personal deployment.
- Keep synchronization, ECX fork-identity and current-template mining gates.
  Re-run isolated coinbase/commitment tests and verify actual ASIC submissions.
- Run native Umbrel fresh install, first launch, authentication, setup, restart,
  persistence, upgrade and relocation tests. Record exact OS and architecture.
- State AMD64-only beta support until ARM64 builds and tests are complete.
  Meeting official Umbrel App Store requirements is a separate milestone.
- Run final privacy and artifact checks. Do not upload credentials, miner
  endpoints, personal payout files, wallet material or chain/ledger databases.

Publishing this store foundation does not imply the draft app is ready to
install. No production node, pool or data volume should be replaced for these
preparation steps.
