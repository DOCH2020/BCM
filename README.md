# BCM App Store

Community applications from Bluefields Cryptocurrency Mining for Umbrel.

## BCM ECX Node (Beta) — 0.1.0-beta.1

The Linux AMD64 beta is listed in this community store with the gold 3D ECX icon.
It includes an unpruned ECX node, repaired enforcer, zero-fee SOLO Stratum V1
pool and BCM dashboard, with light/dark themes and owner-specific first-run setup.
ECX is separate from BTC and XEC. PPLNS and ARM64 are not included.

Add this community store in Umbrel's App Store settings:

https://github.com/DOCH2020/BCM

Select BCM ECX Node (Beta). Each installer supplies their own ECX receiving
address and uses the setup password shown by Umbrel. No private key is required.
Mining waits for synchronized, verified chain and current templates.

Use a separate Linux AMD64 Umbrel with 16 GB RAM; a 2 TB SSD is recommended.
The unpruned chain requires substantial free storage (at least 950 GB at the
prepared preflight baseline). Ports 3334/3335 must be unused. These Stratum
ports are published on host interfaces; control remote access with your network
firewall. No router forwarding is configured. Administrative RPC remains private.

## Beta testing status

The runtime image is publicly pullable and pinned by digest. Private image
audits, source checks and isolated setup/browser tests passed. A real Umbrel
fresh install, authentication, restart, upgrade, relocation and ASIC acceptance
still need independent testing. This is an untested Umbrel beta, not an official
Umbrel endorsement or a claim of production readiness. See TEST-RESULTS.md.

The owner approved public image publication on November 5, 2026. Upstream
enforcer redistribution clearance remains unconfirmed; publication approval
does not establish a third-party license grant. Component notices are retained.

The only bundled addresses are optional public donation addresses for display;
they never replace the installer's mining payout. No wallet material, personal
installation settings, miner endpoints, chain or ledger is bundled.

Run `python3 check_store.py` for static metadata checks. These do not certify
installation. Removing the `bcm-ecx/` catalog entry rolls back listing without
deleting an installed user's data. Preserve app ID and data on upgrades.
