# BCM ECX Node (Beta) — 0.1.0-beta.3

The existing node, 0% SOLO pool and BCM dashboard now include automatic initial-sync peer assistance. Node binaries, mining policy, ports and data mounts are unchanged by this update.

Open **Node status → Sync peer settings**. Assistance uses ECX mainnet, with its upstream seed list and P2P port 8533. Normal discovery continues. At most four automatic helper addresses are tried, within a total cap of seven including your optional addresses. Failed or idle automatic helpers are periodically replaced. Only public IPv4 endpoints are accepted.

Use the Umbrel app password to save preferences. Settings survive restarts and upgrades, apply within 20 seconds, and can disable automatic discovery or all assistance. Turning assistance off removes retry hints without dropping existing connections. Connected peers and peers downloading blocks are shown separately. The displayed blocks/second value is a measured recent sample, not a completion forecast. More peers do not guarantee faster sync.

The helper is limited to initial block download and checks expected chain identity. All consensus validation and mining readiness gates remain enabled.

## Updating

Use the normal Umbrel **Update** action; do not uninstall to update. The existing chain, settings and mining ledger volumes are reused. Updating restarts this app. Native install/update, relocation and real-ASIC lifecycle acceptance remain beta testing tasks.

ECX remains unpruned for its enforcer. External relay sidecars sharing the node container network namespace must be reattached after a node-container update; check that integration before updating a live upstream installation.

Validation: 8 embedded Linux tests, settings authentication and persistence, chain cutoff and idle rotation tests, mobile pages in both themes, source-hash/image-state audit and anonymous image download verification. Upstream seed reference: https://github.com/ecash-com/bitcoin/blob/c8474e0b4f2be9b470c46598a5a6a3e55a85b765/src/kernel/chainparams.cpp.

## Worker latency fix

Open **Node status → Worker latency settings**. The dashboard now starts the telemetry collector automatically. Existing ECX_MINER_SOURCES and ECX_LAN_HOST overrides remain the fallback until settings are explicitly saved. Save Harlo, AxeOS or LuxOS LAN endpoints using the Umbrel app password; settings persist across restarts. Readings update every 10 seconds and expire after 30 seconds. Only active connections on ECX ports 3334/3335 and configured pool hosts match the complete worker username. Numeric AxeOS fallback flags are supported. LuxOS APIs that expose no pool latency show Unsupported; ping is never substituted. A saved empty source list disables polling.

This release passed 17 embedded Linux tests, including authenticated HTTP settings, legacy migration, duplicate names, stale and foreign-pool exclusion, numeric fallback flags and unsupported APIs.
