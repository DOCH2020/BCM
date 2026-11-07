# BCM BCH Node (Beta) — 0.1.0-beta.2

Install through the BCM community store. Linux AMD64 beta; not an official Umbrel endorsement or production-readiness certification.

On first launch use the app password shown by Umbrel, choose pruning (2048 MiB default, minimum550 MiB) or an unpruned archive, and enter your own receiving address. Mining stays gated until the node verifies the correct synchronized chain and a fresh template. Pruning does not eliminate initial blockchain download/validation or cap total app storage. An already-pruned archive needs a separate redownload to become unpruned; the app never automatically erases/reindexes it.

BCH dashboard8090; standard/high Stratum3360/4360. Uses BCHN29.2.0 and verifies BCH fork identity, CashAddr, non-witness blocks and canonical transaction ordering. Dark-green panel outlines.

Full winning-miner coinbase reward, 0% mandatory pool fee, wallet disabled. Coffee support is optional and never a mining fee recipient. Includes all BCM panels, fixed1M live-log/peak-chart display filters, compact difficulty values, persisted Block Smasher reset after a confirmed pool block, and optional Harlo/AxeOS worker latency settings under Node status. Telemetry polls every10seconds, expires after30seconds and excludes wrong-pool/ambiguous readings. No miner configuration is written.

Each image passed17 tests and an isolated two-node block-acceptance test with pruning enabled on the mining node. No mainnet test shares, blocks or payments were sent. Native store install, initial sync on your hardware, real ASIC/rental acceptance, restart, upgrade and storage relocation remain beta acceptance checks. Install/sync the apps sequentially while observing resource headroom. Update existing installations normally; do not reinstall or delete chain/settings/pool data as a routine update step.

Beta.2 keeps initial-sync telemetry visible before the BCH checkpoint can be verified. Mining remains gated until the actual BCH fork and current chain/template are verified. Existing chain/settings data are preserved by a normal update.
