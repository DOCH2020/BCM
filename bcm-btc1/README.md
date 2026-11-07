# BCM BTC1 Purity Node (Beta) — 0.1.0-beta.2

Bitcoin Purity 1.1.2 node, selectable pruning, zero-fee SOLO pool and BCM dashboard. AMD64 beta.

## Sync peers

Open the app, expand **Node status**, then select **Sync peer settings**. Historical assistance defaults to enabled with seven public archive candidates. You can disable it or save up to seven public IPv4 endpoints using your Umbrel app password. Changes apply within 20 seconds and the settings file persists in the existing settings volume across restarts and upgrades.

The helper retries archive peers only while downloading shared pre-fork history. It removes its retry hints when height 961631 is reached, initial download ends, or assistance is disabled. Existing connections may remain connected normally. Ordinary peer discovery continues. Peer availability and download speed vary; the address list is not a guarantee of service or a source of chain trust. Purity's consensus and activation identity checks remain authoritative.

## Update

Use Umbrel's normal app update. Do not uninstall to update. Existing chain, storage settings, payout and pool data mounts are unchanged; the daemon resumes its existing chain database. Applying the update restarts this app. Native beta.1-to-beta.2 lifecycle acceptance remains pending.

Dashboard: 8092. Stratum: 3390 / 4390. RPC remains private; node wallet and embedded DATUM remain disabled. The 0% SOLO pool starts only after current Purity chain identity and template checks pass.

Validation: 21 Linux/image tests; isolated two-node pruned mining/block acceptance checks; peer persistence, authentication, disable behavior, wrong-chain rejection and shared-history cutoff tests; mobile settings in both themes. No mainnet shares or blocks were submitted during testing.
