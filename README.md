# BCM App Store

## Independent SOQ SOLO app

**BCM SOQ Node (Beta) 0.1.0-beta.4** runs one SOQ node and a 0% SOLO Scrypt pool without waiting for LTC or DOGE. Includes pruning, peer assistance, worker settings and the 3D SOQ coin. Dashboard 8095; ASIC/rentals 3402/4402. Linux AMD64 beta. See [setup and validation notes](bcm-soq/README.md).

## Scrypt merged SOLO apps

| App | Version | ASIC / rentals | Dashboard |
| --- | --- | --- | --- |
| [BCM Scrypt Hub — LTC + DOGE + SOQ + PEP + BEL](bcm-ltc-merged/README.md) | 0.1.0-beta.3 | 3400 / 4400 | 8093 |
| DGB Scrypt + DOGE + SOQ | 0.1.0-beta.1 | 3401 / 4401 | 8094 |

Scrypt Hub updates the existing LTC merged app in place, preserving its app ID and original three chains, settings and history. Add your own PEP/BEL receiving addresses after updating; mining waits for completed setup and all five synchronized nodes. Includes five matching 3D coins and a new store icon. **0% SOLO**, Linux AMD64 beta; BEL uses an upstream release candidate. Native lifecycle and mainnet payout acceptance remain beta testing tasks. See the [upgrade and resource notes](bcm-ltc-merged/README.md). The DGB triple app remains separate and unchanged.

## Current sync-assistance updates

| App | Version |
| --- | --- |
| BCM FRIO Node (Beta) | 0.1.0-beta.7 |
| BCM BCH Node (Beta) | 0.1.0-beta.3 |
| BCM Tarcoin Node (Beta) | 0.1.0-beta.2 |
| BCM ECX Node (Beta) | 0.1.0-beta.3 |
| BCM BTC1 Purity Node (Beta) | 0.1.0-beta.5 |

All five apps include automatic chain-specific peer discovery, persistent peer settings and measured sync progress. Open Node status → Sync peer settings after updating. Existing data mounts and pool fee policies are preserved. Images are published for Linux AMD64; native lifecycle acceptance remains pending. See each app directory for current notes.

## Earlier release notes

The following sections describe earlier releases and setup history. The table above lists current versions.


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


## BTC1 Bitcoin Purity beta

**BCM BTC1 Purity Node (Beta)**, version **0.1.0-beta.1**, is available for Linux AMD64. It uses the verified official Purity1.1.2 release, a selectable pruned/full node, a0% direct-coinbase SOLO pool, and the BCM dashboard with3D coin artwork. Dashboard8092; standard/high Stratum3390/4390. Purity activation checkpoint961637 is required before mining; initial-sync metrics stay visible before activation. Wallet and embedded DATUM are disabled. Native lifecycle and actual hardware sync/miner acceptance remain beta checks. The image passed18 tests and independent two-node pruned block acceptance. Sync one substantial node at a time; pruning does not remove initial download/validation or cap total disk use.

BCH beta.2 also fixes unavailable initial-sync telemetry before its BCH fork checkpoint. Existing data and mining gates are preserved during a normal update.


