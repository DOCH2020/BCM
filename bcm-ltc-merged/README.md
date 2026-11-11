# BCM Scrypt Hub (Beta) — 0.1.0-beta.4

LTC + DOGE + SOQ + PEP + BEL. Five independent nodes share one wallet-free **0% SOLO** Scrypt mining connection. Each chain pays its full miner coinbase reward directly to its configured receiving address, subject to consensus and maturity. A proof may qualify for only a subset of coins. No PPLNS or custodial balance is included.

## Update the existing app

Back up your app data, then update the existing LTC + DOGE + SOQ entry through Umbrel. Its app ID remains `bcm-ltc-merged`; do not uninstall or create a second copy. Existing LTC/DOGE/SOQ chain directories, pruning settings, original receiving addresses, pool history and telemetry mounts are retained. No chain deletion or automatic reindex occurs.

Open the app after updating. Upgrade setup displays the original three destinations read-only; add your own valid PEP and BEL receiving addresses using the Umbrel app password. Never enter private keys or seed phrases. LTC must be transparent, and SOQ must be a spendable Dilithium witness-v1 address. An original-settings backup is kept before migration.

**Mining pauses until setup is complete and all five chains are synchronized and verified.** Existing owner `LTC_ADDRESS.worker` and matching legacy three-address logins select the five saved destinations after upgrade. Other miners must use all five addresses: `LTC+DOGE+SOQ+PEP+BEL.worker`.

## Connection and storage

- Algorithm: Scrypt. ASIC: `stratum+tcp://YOUR_UMBREL_HOST:3400`; high-difficulty rentals: port `4400`. Password `x`. Dashboard port `8093`.
- Existing ports are unchanged; no additional host ports or router forwarding are configured. Administrative RPC stays private.
- Retained block-file defaults: LTC 2048 MiB; DOGE, SOQ and PEP 3072 MiB each; BEL 2048 MiB. Zero selects unpruned before initial sync. Old pruning choices are retained. Pruning does not limit initial download, chainstate or total disk use.
- Container memory caps total about 7.4 GiB, plus the host and other apps. They are limits, not reserved or measured steady-state usage. Two additional chains need additional storage, CPU, bandwidth and initial-sync time. Linux AMD64 only.

## Beta validation and upstreams

The published image is pinned by digest and its manifest/layers were verified anonymously downloadable. Twenty-two isolated Linux regression tests passed, including settings migration, wrong-chain rejection, stale-tip/peer gates, candidate journaling and duplicate rejection. Official daemons accepted all five chains' blocks through real loopback Stratum with pruning both enabled and disabled; unpruned coinbases were inspected for full direct payouts. No mainnet test shares or blocks were submitted. Dashboard artwork was verified in a real browser with synthetic data.

PEP uses official v1.1.0; BEL uses official **v3.1.1-rc2, an upstream prerelease**. Existing LTC/DOGE/SOQ pinned versions remain. Native Umbrel lifecycle, mainnet synchronization, ASIC acceptance, matured payouts and recovery after an auxiliary daemon loses its work cache still require beta acceptance testing. This is not a production-readiness claim.

Per-chain tabs show that coin's network, blocks, effort and round; shared physical hashrate is counted once. New PEP/BEL crystal-metal 3D coins and a matching five-coin store icon are included. Existing Umbrel dashboard styling remains separate from the public VPS pool website.

Runtime source, tests, license notices and exact input lock: [beta.3 source archive](https://bcmpool.online/bcm-scrypt-hub-0.1.0-beta.3-source.tar.gz). Upstream node source/version references are recorded in its input lock. Official PEP source: https://github.com/pepecoinppc/pepecoin/tree/v1.1.0 ; BEL: https://github.com/BellsChain/bellscoin/tree/v3.1.1-rc2 .

## Beta.4 installer permissions repair

Umbrel upgrades do not copy new `data/` directories from the store package. Docker can then create missing PEP/BEL bind sources as root, while the nodes run as UID/GID 1000. The node cannot create its lock/cookie and setup cannot validate the new receiving addresses.

Executable `hooks/pre-install` and `hooks/pre-start` now initialize the eight known app directories with owner 1000:1000 before Docker starts. The startup hook also repairs existing root-owned directory inodes. It uses Umbrel's `APP_DATA_ROOT` when available, including relocated storage, and otherwise the legacy `APP_DATA_DIR/data` path. It requires Python 3 on the Umbrel host (present on the tested umbrelOS 2.0.1 system). An unavailable external data root is not replaced by internal storage. Symlinked roots/children and non-directory mount sources are refused.

Only top-level directory ownership and missing owner access bits are repaired. It never recursively changes chain files, deletes data, reindexes, overwrites settings, substitutes receiving addresses or runs nodes as root. This does not repair unrelated ownership problems inside an existing chain.

Update **the existing app in place**. The store version is beta.4, but its container references intentionally retain the same digest-pinned beta.3 runtime: this is a host installer fix, not a node/consensus update. Your currently repaired installation does not need another immediate restart. The patch will apply during a normal Umbrel update/start.

Linux tests reproduce fresh installation and the root-owned PEP/BEL upgrade failure, prove UID 1000 can write lock files, preserve existing chain/settings bytes and metadata across repeat runs, and cover relocated/unavailable storage and symlink rejection.
