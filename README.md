# BCM App Store

Community applications from Bluefields Cryptocurrency Mining for Umbrel.

**Status: private AMD64 app build tested. No installable apps in the store yet.**

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

## ECX development update — November 4, 2026

The private Linux AMD64 image is built and audited. Pool unit suites and seven
in-image checks passed. Browser setup, per-install receiving-address validation,
owner isolation, persistent settings, and retained pool/worker best shares have
isolated test coverage. The app is SOLO only with a zero pool fee.

Twelve local setup/package tests and three destination-preflight regression
groups pass. The destination check requires adequate RAM and free storage,
the selected private LAN address, and unused app/Stratum ports. This is a
developer test gate; the owner-facing LAN selection flow is still unfinished.

These results do not establish Umbrel installation or upgrade compatibility.
The image is private and has not been published or installed through this
store. Enforcer redistribution clearance, a separate real Umbrel install/update
test, public images, and ARM64 build/test coverage remain release requirements.
See [ECX-RELEASE.md](ECX-RELEASE.md) for the remaining gates and
[ecx-build-status.json](ecx-build-status.json) for the recorded build identity.

## Repository layout

```text
umbrel-app-store.yml           Store identity: bcm / BCM
ecx-draft.json     Planned app metadata; not an install manifest
ecx-build-status.json   Private build identity and bounded test status
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
