# BCM BTC1 Purity Node (Beta)

Public beta candidate: Purity1.1.2, 0% SOLO pool, selectable pruning, full BCM dashboard, persisted Block Smasher reset and genuine miner telemetry. Separate chain/settings/pool data; RPC private, wallet disabled, embedded DATUM disabled. Mainnet mining requires Purity activation checkpoint961637.

Dashboard8092; Stratum3390/4390. Node budget3GiB RAM, two CPUs, dbcache512MiB. Pruning2048MiB default or unpruned; total storage and initial bandwidth exceed the prune target. Use a fresh dedicated app data directory and sync sequentially with existing apps. No personal peer overrides, assumevalid/minimum-work changes or preloaded chain snapshots. Native installation and real ASIC testing remain pending.

Initial-sync telemetry remains visible below activation height961637. Mining waits for verified Purity identity, completed IBD and a fresh template. Native installation, real ASIC and lifecycle checks are beta acceptance tasks. Update normally; never reinstall as a routine update step. Coffee support is optional and is never a fee recipient.
