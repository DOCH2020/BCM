# BCM App Store

Community applications from Bluefields Cryptocurrency Mining for Umbrel.

**Status: store foundation. No installable apps yet.**

The first planned app is **BCM ECX Node**: a local ECX full node, mining
enforcer, SOLO Stratum service and BCM dashboard. ECX is distinct from XEC
and Bitcoin BTC. The intended interface is English with light/dark themes.

## Adding the store

Open the Umbrel App Store, find its Community App Stores setting and add:

**https://github.com/DOCH2020/BCM**

UI labels can differ between Umbrel versions. The store currently has no
installable applications; BCM ECX Node is still a draft.

An app will appear only after its installable manifest and public runtime
images pass the release checks. The draft below is intentionally outside
the app catalog, so Umbrel cannot offer an incomplete installation.

## Repository layout

```text
umbrel-app-store.yml           Store identity: bcm / BCM
ecx-draft.json     Planned app metadata; not an install manifest
ECX-RELEASE.md       Requirements before listing the app
ecx-icon.png        Existing BCM 3D ECX artwork
check_store.py           Local metadata and privacy checks
```

When ready, a top-level `bcm-ecx/` directory will contain `umbrel-app.yml`,
`docker-compose.yml` and persistent data directory placeholders. The app ID
starts with this store's `bcm` prefix. The draft does not claim an official
Umbrel endorsement or a completed installation test.

The store does not include a blockchain, personal payout address, miner
endpoints, API credentials, wallet backup or private key. Each owner must
configure their own ECX receiving address during first-run setup.

## Development

Run `python check_store.py` from this store directory. This checks the
store foundation; it is not a substitute for Umbrel installation testing.
The current running OptiPlex containers are separate and remain unchanged.

Packaging conventions follow the official community-store template:
https://github.com/getumbrel/umbrel-community-app-store
