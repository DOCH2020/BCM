# BCM ECX Node beta catalog change

This change adds the `bcm-ecx` catalog layout with the existing gold 3D ECX icon.
It is prepared for review, not merged into the public store yet.

The runtime image is still private. Before merging, publish the audited
0.1.0-beta.1 AMD64 image to `ghcr.io/doch2020/bcm-ecx`, confirm anonymous pull,
and replace every Compose image reference with the verified registry digest.
The current digest is the audited private archive's manifest, not a claim that
the registry tag is publicly available.

The manifest explicitly identifies an untested AMD64 beta. Real Umbrel lifecycle
testing is delegated to the owner's helper. The app uses SOLO with zero fee;
each owner configures their own receiving address. Ports 3334/3335 are published
on host interfaces for miners; no router forwarding or administrative RPC
exposure is configured. Node, enforcer, pool and dashboard retain the separated
service/storage layout. Never install onto the existing personal mining host
without its own capacity and port-conflict checks.

Publication approval needed: expose the audited 98,810,880-byte OCI archive at
`https://bcmpool.online/bcm-ecx-0.1.0-beta.1-amd64.oci.tar`, then import it into
GHCR using a repository workflow. This makes the bundled executable software
public; upstream enforcer redistribution clearance remains unconfirmed. The
archive checksum is `72a140b64a71b0c6fe72351eacda6d6c95a8243af21de4b21556d1ebfaa37c7d`.

No runtime image has been published by this catalog preparation.
