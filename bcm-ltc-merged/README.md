# BCM LTC + DOGE + SOQ (Beta) — 0.1.0-beta.1

Three self-contained nodes, a wallet-free **0% SOLO** Scrypt merged pool, and the full BCM dashboard. No PPLNS or mandatory pool fee. Each chain pays its own full miner coinbase reward directly to the chosen receiving address, subject to that chain's maturity rules.

## Setup

Open the app from Umbrel. Use its app password to configure storage, then supply one receiving address for LTC, DOGE and SOQ. Use a transparent LTC address for the LTC app; an MWEB-only destination is unsupported. SOQ requires a spendable witness-v1 Dilithium address (`sq1p...`). Never enter wallet seeds or private keys.

Pruning defaults: parent 2048 MiB, DOGE 3072 MiB, SOQ 3072 MiB. Minimums: parent 550 MiB, DOGE/SOQ 2200 MiB; zero chooses unpruned. These are retained block-file targets, not total disk or initial bandwidth limits. Changing running-node storage requires a normal app restart. Switching an already-pruned chain to unpruned requires a separate rebuild and is blocked by the app. All three chains must synchronize before mining starts.

## ASIC connection

- Algorithm: **Scrypt**.
- URL: `stratum+tcp://YOUR_UMBREL_IP:3400`; rental listener `4400`.
- Username: `YOUR_LTC_ADDRESS.worker`, using exactly the parent address saved during setup. This selects the saved DOGE and SOQ destinations.
- Password: `x`.

Advanced users can explicitly supply all three destinations as `PARENT_ADDRESS+DOGE_ADDRESS+SOQ_ADDRESS.worker`. A different parent-only username is rejected. A qualifying proof may solve any subset of the three coins; it does not guarantee all three rewards.

## Dashboard and operation

Coin tabs show separate network statistics, round effort, candidate history and Smasher cycles. Shared physical hashrate is not added three times. Worker cards, live shares, charts, optional miner latency, coffee support, pruning and per-chain peer settings are included. Automatic peer discovery uses each chain's upstream seeds and bounded helper rotation. More peers cannot guarantee faster validation.

Settings, each blockchain, the candidate journal and telemetry use separate persistent data mounts. RPC stays private inside the app namespace. The app has no wallet or custodial balance. Use normal Umbrel restart/update actions and keep app-data backups; do not uninstall to update.

## Beta validation

Each image passed 11 isolated Linux tests and source/binary/license audits. Both combinations accepted merged parent/DOGE/SOQ blocks on private networks with wallets disabled, including pruned runs. Real TCP Stratum acceptance and duplicate rejection passed; full-value coinbase outputs were inspected. Desktop/mobile dashboard checks passed in both themes. Published images were anonymously downloadable before this store entry was created.

Native Umbrel install/restart/update/relocation, mainnet initial-sync duration and real ASIC/mainnet operation remain acceptance tasks. Container memory limits total about 5.4 GiB per app, plus the host and other apps; actual steady-state use has not been measured on the destination. Linux AMD64 beta only.

## Beta.2 sync tuning

LTC uses 512 MiB of database cache (previously 256 MiB); DOGE uses 384 MiB (previously 128 MiB). SOQ stays at 128 MiB. The total increase is 512 MiB; container memory limits remain unchanged. Two script-validation threads per node are retained. Connection capacity is 20, with existing bounded DNS peer assistance and normal peer selection. More slots do not guarantee more useful downloads.

This update preserves existing data mounts, pruning preferences, receiving addresses, private RPC and zero-fee mining rules. It requires an ordinary app restart and never deletes, reindexes or replaces a chain. It changes only the LTC merged app. Increased database cache can reduce disk work during initial validation; throughput still depends on current block density, peers, CPU and storage. 13 embedded image tests passed, including private mining/runtime tests and startup-option regression checks.
