**BEACON OF THE EAGLE LLC | CENTINELL SUITE DEFENSE**  
*Original simulated forensic case | Northbridge Systems | 26-NB-0918*

# System, service and account catalog

This is the **pre-investigation scope** provided to the analyst; it does not label any particular event malicious. All identifiers are invented training fixtures.

| Host | Operating context | Relevant processes and services | Investigative role |
|---|---|---|---|
| `nb-dfs-02` | Simulated Linux archive server | `/usr/bin/tar` for staging, `/usr/bin/stat` for catalog checks, `nb-collector` forwarding client, restricted-data mount | Source-side file and collection audit |
| `nb-jump-03` | Simulated Linux admin jump host | scheduled `/usr/bin/logger` health checks and scripted administrative process (`jump_process.csv`) | Session/process trace; host clock offset |
| `nb-backup-01` | Linux scheduling worker | `backup-index-rebuild` service job | Approved maintenance comparison |
| `nb-proxy-01` | Managed outbound inspection gateway | HTTPS CONNECT proxy, TLS-inspection request body spool, gateway request logger | Outbound upload evidence; proxy clock offset |
| `nb-vault-01` | Segmented evidence witness (simulated) | append-only witness signer and SQLite index | Limited cryptographic witness; not a real HSM |
| `nb-idp-01` | Workload identity broker | mTLS token service and identity/session logging | Service-principal grants and origin claims |
| `nb-sensor-02` | DNS/network sensor | DNS export, selected CONNECT pcap | Network corroboration |
| `nb-collector-01` | Remote log collector | heartbeat monitoring and config audit | Missing source collection and restoration |
| `nb-fw-01` | Boundary firewall | egress flow logs | Network path corroboration |

## Relevant synthetic accounts and claims

| Principal | Intended role | Interpretation limits |
|---|---|---|
| `NB\svc_archive` | Non-human archive service identity | Use on approved asset does not authorize activity at other origins, scopes or times |
| `NB\svc_monitor` | Synthetic monitoring identity | Health/export operations only |
| `NB\svc_ops` | Synthetic local ops/background identity | Benign health-check events included for realism |
| `NB\ir_oncall` | Simulated authorized responder | Later recovery action is recorded but identity-of-human is not authenticated by this case |
| `n.vale` | Synthetic change approver label | Approval label only, not a real person's details |

## CVE declaration
**No CVE is exercised or claimed.** The investigation concerns authorization scope, token misuse indications, archive handling, outward transfer, and telemetry suppression—not exploitation of a known software vulnerability. Absence of a CVE is intentional; do not invent one for the write-up.

## Environment notes
These are exported investigation snippets and working data rather than a bootable enterprise environment. The dataset does not demonstrate a real PKI, HSM, remote malware, cloud entitlement or destination-side server verification.
