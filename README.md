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

## BCM FRIO Node (Beta) — 0.1.0-beta.3

The Linux AMD64 FRIO beta is now listed with its 3D FRIO app icon, silver dashboard,
0% pool-fee SOLO engine, and selectable pruned or unpruned blockchain storage.
It uses the same panel layout and Block Smasher animation as BCM ECX.

On first launch, use the Umbrel app password to choose storage (default 2,048 MiB
retained block-file target; minimum 550 MiB, or an unpruned archive), then enter
your own FRIO receiving address. Changes to a running node apply on the next app
restart. Initial sync still downloads and validates the chain; total app storage
is larger than the prune target. An already-pruned archive is never erased or
reindexed automatically by the settings screen.

The registry image is pinned by digest and its manifest and layers are anonymously
pullable. Private image tests, authenticated setup/storage tests, browser checks,
and a pruned-node zero-fee block test passed. Native Umbrel lifecycle and real ASIC
acceptance remain beta testing tasks. See [FRIO beta notes](bcm-frio/README.md).

Ports 3370/4370 must be unused. Administrative RPC is private; no router forwarding
is configured. ECX app files and installed data are unchanged by this listing.


Beta.3 removes the live-log minimum-difficulty dropdown: only proof values of 1M
or higher appear in that log, while totals still include all shares. Panel outlines
now match the green in the 3D FRIO coin, and peak tooltips use compact suffixes.
These are display changes; mining difficulty, payout rules and app-data paths
are unchanged. Update the existing app through Umbrel; do not reinstall it.


## BCH and Tarcoin Umbrel betas

The BCM community store now includes **BCM BCH Node (Beta)** and **BCM Tarcoin Node (Beta)**, version **0.1.0-beta.1**, for Linux AMD64. Each provides selectable pruning, owner receiving-address setup, a zero-fee SOLO pool and the BCM dashboard with its own 3D coin. BCH panel outlines are dark green; Tarcoin outlines are orange.

BCH uses dashboard port8090 and Stratum3360/4360. Tarcoin uses dashboard8091 and Stratum3380/4380. These avoid the ECX and FRIO app ports. Pruned mode defaults to2048MiB retained block files (minimum550MiB), with an unpruned choice before first start. Pruning still requires initial download and validation.

Both images passed17 tests and isolated two-node pruned mining/block-acceptance checks. Native installation, destination initial sync, real ASIC/rental acceptance and lifecycle tests remain beta checks. Tarcoin's official1.2.6 package reports internal daemon version1.0.0; this discrepancy is recorded. Install/sync one new app at a time. Existing ECX/FRIO installations are unchanged.
