# BCM FRIO Node (Beta) — 0.1.0-beta.1

Install through the BCM community store after publication. This beta is for Linux AMD64 and owner-run installation testing. It is not an official Umbrel endorsement or a claim of production readiness.

On first launch, enter the app password shown by Umbrel and select blockchain storage: pruned (default2048MiB, minimum550MiB) or unpruned. The node waits for that choice before connecting and downloading. Then enter your own FRIO receiving address. Mining remains gated until the FRIO chain and template are ready.

A block-file prune target is not total app disk usage and does not avoid the initial blockchain download/validation. Existing installations without a storage preference retain the prior2048MiB default. Change the target later from Node status → Blockchain storage settings; restart the app in Umbrel to apply a saved change. This screen never automatically stops mining, erases chain data, or reindexes a pruned archive into an unpruned one.

The app uses a wallet-disabled node and 0% mandatory pool fee. In private regtest, a pruned FRIO mining node synchronized from an archival peer and its full-value miner coinbase block was accepted by both nodes. Standard and high-difficulty Stratum use3370/4370; these host ports must be unused. Ports are bound on host interfaces; no router forwarding is configured. Administrative RPC remains on loopback in the private app network namespace.

Included UI: all ECX-style panels, identical Block Smasher motion/keyframes, 3D FRIO coin, silver dark/light themes, 1M+ live-share-log filters and optional coffee support. The display-only public coffee addresses are never pool fee recipients or fallback mining payouts. Unknown miner latency is explicitly not reported, never simulated.

Private unit, HTTP setup, prune-mode block, persistent-state and browser tests have passed. Fresh native Umbrel install, first synchronization on your hardware, restart, upgrade, data relocation and real ASIC acceptance are not yet certified. Record those results during the beta test. No ECX app or VPS chain/payout configuration was migrated.
