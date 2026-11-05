# BCM ECX independent Umbrel test report

Status: NOT YET RUN. Enter PASS, FAIL or NOT RUN for every row; attach evidence for each PASS.

Tester/date:
Umbrel version:
CPU architecture / RAM / storage:
App version / package SHA256:
Registry image reference and digest:
Destination preflight result:

| Check | Result | Evidence / issue |
| --- | --- | --- |
| Package lint, anonymous image pull, AMD64 runtime | NOT RUN | |
| Clean install and Umbrel authenticated launch | NOT RUN | |
| HTTP and HTTPS setup; app password works | NOT RUN | |
| Invalid address/password rejected; valid owner persists | NOT RUN | |
| Sync visible; mining gated before verified current templates | NOT RUN | |
| ECX chain identity verified; node/enforcer healthy | NOT RUN | |
| ASIC accepted shares on selected private interface | NOT RUN | |
| SOLO coinbase destinations and zero fee verified | NOT RUN | |
| Dashboard figures, worker lookup, charts, copy buttons | NOT RUN | |
| Desktop/mobile; light/dark; no script errors | NOT RUN | |
| Restart retains owner, chain, ledger and best-share history | NOT RUN | |
| Upgrade retains app ID, data and history | NOT RUN | |
| Umbrel storage relocation retains data and operation | NOT RUN | |
| Conflicting ports refuse install without disrupting services | NOT RUN | |
| RPC/enforcer remain private; setup cannot replace owner | NOT RUN | |
| Graceful stop/start; no unexpected OOM or crash loop | NOT RUN | |

Known exclusions: ARM64 and PPLNS. Internet rental access is not configured.

Problems found / reproduction steps:

Resolution / retest evidence:

Tester recommendation: NOT YET ASSESSED.
