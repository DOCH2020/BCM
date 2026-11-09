# BCM SOQ Node (Beta)

A standalone Soqucoin node, wallet-free **0% SOLO Scrypt pool**, and BCM dashboard. It does not run or wait for Litecoin, Dogecoin or DigiByte, and it pays SOQ only. The SOQ node constructs the reward transaction and all chain-specific commitments; accepted blocks pay the miner's receiving address directly, subject to SOQ's coinbase maturity. There is no pool balance, payout threshold or mandatory pool fee.

## First run

1. Open the app from Umbrel and use its app password to select storage. Default retained block-file target: **3072 MiB**; minimum **2200 MiB**. Zero selects unpruned. Total disk usage exceeds the target, and initial sync still downloads and validates historical blocks.
2. Enter your SOQ Dilithium witness-v1 receiving address (`sq1p...`). The app validates the chain and spendability. Never enter wallet seeds or private keys. The node runs with its wallet disabled.
3. Wait for the SOQ node to synchronize. Mining requires the expected genesis, `initialblockdownload=false`, matching blocks/headers, and a current node-built job. It is independent of any merged app you have installed.

SOQ Core 2.6.1 always reports its native `verificationprogress` as 1.0. This dashboard instead labels its block/header ratio as **Header catch-up progress**, and keeps mining gated until the actual node readiness checks pass. A displayed header ratio is not a full verification-work estimate.

## ASIC connection

- Algorithm: **Scrypt**.
- URL: `stratum+tcp://YOUR_UMBREL_IP:3402`.
- Rental listener: `stratum+tcp://YOUR_UMBREL_IP:4402`.
- Username: `YOUR_SOQ_ADDRESS.worker`.
- Password: `x`.

Only SOQ is mined. The service uses one-chain AuxPoW work carriers with `createauxblock` / `submitauxblock`; no separate parent-chain node or reward is involved. Optional `d=...` sets starting Stratum difficulty within the listener's bounds; it does not change the reward split.

## Controls and data

The dashboard includes worker cards, live share filtering, peak difficulty, round timer, effort, persisted Smasher reset, candidate history, optional miner-reported latency, and voluntary BTC coffee support. The app icon and dashboard coin use the approved teal-and-silver 3D SOQ artwork.

Open **Node status** for storage, peer assistance and worker latency settings. Pruning changes apply after a normal app restart. Switching an already-pruned archive back to unpruned is blocked when old blocks have been removed; the setting never erases or reindexes a chain automatically. Peer assistance uses SOQ's own upstream seeds and can be disabled. Miner telemetry reads supported LAN APIs without changing the miners.

Separate persistent mounts hold the node, installation settings, mining candidate journal and dashboard telemetry. RPC stays loopback-only inside the app namespace. The node, pool and dashboard run as UID 1000 with read-only container filesystems and no Docker socket. Dashboard port: **8095**. Linux AMD64 beta only.

## Validation and beta limits

Private-network tests with the official SOQ 2.6.1 node accepted a SOQ-only block through a real TCP Stratum subscription, authorization and share submission. Duplicate rejection and candidate journaling passed. The tests passed with wallets disabled, both unpruned and pruned. In the unpruned indexed test, the decoded coinbase had one full-value miner output and no pool fee. No mainnet share or block was submitted during development.

20 embedded Linux tests passed, including setup, pruning, spendability, peers and mining, plus source/binary/license audits and anonymous image download verification. Desktop/mobile setup and dashboard checks passed in both themes. Native Umbrel install/restart/update/relocation and real-ASIC/mainnet acceptance remain beta tests. Configured service memory limits total about 2.4 GiB; actual destination use has not been measured. Creating this package does not install it or change an existing merged app.

Official references: [SOQ release 2.6.1](https://github.com/soqucoin/soqucoin/releases/tag/v2.6.1), [pool integration](https://github.com/soqucoin/soqucoin/blob/v2.6.1/doc/pool-integration.md), [AuxPoW consensus implementation](https://github.com/soqucoin/soqucoin/blob/v2.6.1/src/auxpow.cpp).

## Beta.3 panel repair

Goldshell settings accept mixed case and use the read-only MCB pool API. When miner-reported response time is unavailable, active authenticated workers can show **Stratum RTT**, measured with Linux TCP_INFO on their existing connection. This is the smoothed TCP round trip to the direct peer (a relay/proxy if present), not a miner-reported share response time or a ping. Stale, closed, and ambiguous connections do not receive a fabricated reading. Miner API samples take precedence when valid.

Single-address journal entries now populate miner views; a bounded, checkpointed repair backfills beta.2 entries from the original journal without deleting retained history or Smasher reset boundaries. Candidate address filters are corrected. Worker rates are visibly labeled 5 min; pool rates remain 15 min. Tiny positive effort displays <0.01%; the one-minute SOQ round help now agrees with its clock. The 1M log/chart display filter remains in place.

## Beta.4: show shares at every difficulty

The Live Share Log shows the latest 80 events without a minimum proof difficulty, including rejected events whose proof difficulty is unavailable. The Peak Share Difficulty chart retains its time-bucket peak view and now includes every recorded positive accepted peak, with automatic log/linear scales. Empty periods stay blank. Totals and retained history are unchanged. Compact k/M/G/T/P formatting remains. This is a display-only change; mining and fee settings are unchanged.
