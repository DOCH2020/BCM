# BCM ECX Node release gates

The existing personal deployment is operational. That is not yet proof that a
new owner's Umbrel can install this app. Do not promote this draft into the
catalog until the following work is complete.

- Configure the real GitHub repository and support URLs, icon URL and release
  version. Retain the store prefix `bcm` and app ID `bcm-ecx`.
- Produce clean runtime images from the pinned verified node/enforcer releases
  and simplepool commit. Do not reuse image layers containing personal config.
  Include upstream copyright/license notices and identify BCM-owned assets.
- Publish version-tagged images pinned by digest in a public registry. No
  `latest`, local Docker image IDs, private credentials or runtime Compose builds.
- Implement browser first-run configuration with an owner-provided address,
  node validation and persistent settings. No bundled payout fallback.
- Keep separate node, enforcer, Stratum and dashboard processes. Persist app
  data under `${APP_DATA_DIR}/data`, with `storage.dataRoot: data` in the app
  manifest. Preserve ledger and settings across restarts and updates.
- Use authenticated `app_proxy` for the dashboard. Keep node RPC, enforcer
  RPC/gRPC and ZMQ on loopback within the private service namespace. No Docker
  socket, host networking or privileged containers.
- Test conflicts for 8088, 3334 and 3335 before installation. Never displace
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
