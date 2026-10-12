> **BEACON OF THE EAGLE LLC — CENTINELL SUITE DEFENSE**  
> Synthetic case material · Editorial publisher seal · NOT a live incident

# CASE 26-NB-0918 — The Last Evidence Standing

**Investigation window:** 2026-09-18 00:45–02:05 UTC  
**Enterprise:** Northbridge Systems (fictional)  
**Classification:** simulated, no live systems or real customer information

At approximately 01:26 UTC, the SOC received a missing-telemetry alert for an internal evidence/archive host. The on-call engineer reports that a scheduled backup-index maintenance window was in progress. A separate gateway alert flags a small outbound HTTPS request, but the initial note attributes it to routine update traffic. Several host-side historical records are now unavailable.

**Your mission:** reconstruct the trustworthy sequence, determine whether the transfer and logging changes were permitted, identify the exact evidence that supports or contradicts exfiltration, preserve surviving material, and distinguish service-account use from proof of a human operator.

Do not assume all observed clocks agree. Do not trust an artifact solely because it has an internal-looking filename. Use independent exhibits for consequential claims. Provide exact UTC times, IDs, paths and SHA-256 digests where asked. Treat null results and missing logs as uncertainty rather than proof of absence.

### In scope
- `nb-dfs-02`: protected Linux archive/file host; 10.24.18.22
- `nb-jump-03`: privileged administration host; 10.24.12.13
- `nb-backup-01`: authorized scheduled backup worker; 10.24.12.45
- `nb-proxy-01`: managed HTTPS inspection gateway; 10.24.40.12
- `nb-vault-01`: segmented append-only evidence witness; 10.24.50.10
- `nb-idp-01`, `nb-sensor-02`: independent identity and network observers

### Starting clue
Monitoring incident `INC-26-0918-441` was opened at 01:26:08 UTC. The host-side audit export is incomplete; use the source registry and clock model before interpreting event order.

### Allowed tools
Text/CSV/JSON viewers, `sha256sum`, `openssl`, `tar`, Wireshark/tshark (optional), SQLite utilities (optional), and any local offline analysis. No virtual machine or Internet connectivity required. The pcap is a selected vantage-point slice, **not** full TLS payload capture.
