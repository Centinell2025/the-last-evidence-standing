> **BEACON OF THE EAGLE LLC — CENTINELL SUITE DEFENSE**  
> Synthetic case material · Editorial publisher seal · NOT a live incident

# The Last Evidence Standing — Investigation Worksheet

**Target:** advanced DFIR / network forensics, difficulty **Insane (proposed; unvalidated)**  
**Estimated effort:** 4–7 hours (author estimate, no external playtest yet)  
**30 exact-response investigation tasks + optional analyst report**  
**All dates:** 2026-09-18 UTC unless asked for a source-local timestamp.

**Ground rules:** Work entirely from the enclosed artifacts. Exact-identifier answers must be copied from exhibits; no guessing. For optional explanatory reports cite the exact filename, ID/row and timestamps from **at least two independent sources**. A single copied witness assertion is not corroboration. Clearly label verified facts, plausible hypotheses and unresolved questions. Time normalization must show the applied offset.

## Phase I — Why was the archive host touched?
1. What is the exact SOC incident identifier that opened this investigation?
2. Which hostname is the archive host affected by the missing telemetry?
3. Which approved change ticket overlaps the investigated window?
4. State the exact approved UTC maintenance window as `HH:MM–HH:MM`.
5. Which operation is explicitly approved by the change board? Return its hyphenated operation value.
6. Which host actually ran the legitimate scheduled backup-index job?

## Phase II — Who had apparent access, and how certain is it?
7. Correlate the approved scheduled job with the independent suspicious workload-token record: which exact service principal appears in both, despite the different origin and scope?
8. Exclude the approved job token using the asset, issuance time and granted scope. What is the exact anomalous workload token ID?
9. Join the anomalous token issuance to an observed jump process without relying on the client device label. Which exact session ID is common to both?
10. Which **client-origin** IP does the broker report for that anomalous session?
11. What exact certificate-fingerprint *claim* is recorded for the anomalous session?
12. Give the raw `observed_host_time` for process `jp-402`, including the date and `Z`.
13. After applying the documented jump-host clock offset, give the UTC time of `jp-402`, including the date and `Z`.

## Phase III — What was staged and where did the bytes go?
14. Starting from the anomalous jump-host session, pivot to the archive-side audit trace. Which full protected source path did that linked export read?
15. Using the shared trace rather than a filename keyword, identify the full destination staging path created by the archive process.
16. Recompute SHA-256 over the provided physical TAR.GZ bytes and compare with FIM and proxy records. Which 64-character lowercase digest survives all three comparisons?
17. Reconcile the physical TAR.GZ file size with the FIM scan and gateway recorded body length. What single integer byte count is shared by all three?
18. Which destination hostname received the suspicious inspected POST?
19. What is the documented external destination IP associated with that request?
20. Exclude the benign update GETs and match the inspected POST to the host-side transfer trace and destination IP. What is its exact gateway request ID?
21. Give the *uncorrected* proxy wall-clock timestamp for this POST, including date and `Z`.
22. Correct the proxy time to UTC. Give the timestamp including date and `Z`.

## Phase IV — What survived the attempted concealment?
23. Among the control-plane revisions, which ID changed `forwarding.enabled` from `true` to `false` and precedes the collector disappearance?
24. Compare all observations for the affected host, not the alert-creation time. At which UTC timestamp did the collector first record `missing`?

## Phase V — Survivability and restoration (exact-response tasks)
25. The detached Ed25519 signature must verify under the provided vault public key. What exact `witness_id` is associated with the signed object containing five observation references?
26. After the collector impairment, which UTC FIM **scan timestamp** first records a zero-byte `forwarded.log`? Answer in `YYYY-MM-DDTHH:MM:SSZ` format; do not mistake scan time for the time of the truncation command.
27. Which exact configuration revision restores `forwarding.enabled` from `false` to `true`?
28. What UTC time does the collector first record `healthy` **after** the period of missing heartbeats? Answer in `YYYY-MM-DDTHH:MM:SSZ` format.
29. At what exact UTC time does the identity broker record the anomalous token as `revoked`? Answer in `YYYY-MM-DDTHH:MM:SSZ` format.
30. Of the change-board's explicit exclusions, which hyphenated operation specifically forbids disabling collector forwarding? Answer the exclusion label exactly as recorded.

## Optional analyst board — non-graded investigative report
These six analytical challenges are **not** submitted as exact HTB answers. They form an optional training debrief for the instructor, not prerequisites for the 30 numbered responses.

A. **Authorization:** distinguish sanctioned backup-index work from unauthorized read, transfer and logging modification; cite the ticket, job, token, process and gateway traces.
B. **Transfer proof:** compare staged archive to inspected gateway request body byte-for-byte and determine exactly what the HTTP 201, DNS, firewall and CONNECT capture prove or cannot prove.
C. **Signed evidence:** verify the detached signature, cross-check five referenced observations, and separate the cryptographic guarantee from source correctness and human attribution.
D. **Anti-forensics:** build an uncertainty-aware UTC timeline from configuration changes, collector pulse loss, two FIM scans and restoration; do not equate a scan time with an execution time.
E. **Competing explanations:** challenge the benign update traffic and routine maintenance interpretations and evaluate whether a client name/certificate *claim* identifies a human.
F. **Incident commander:** recommend containment, check that token revocation was already recorded, preserve exhibits and plan follow-on collection without asserting unobserved retrieval or actor identity.

A completed optional report can use `docs/INVESTIGATION_REPORT_TEMPLATE.md` and should cite two independent sources per consequential conclusion. The signatures and hashes demonstrate local byte integrity **within the training assumptions**, not real-world event authenticity.

## Evidence-integrity checkpoint
From the extracted root run `python3 tools/verify_student.py`, then inspect `docs/CLOCK_MODEL.csv`, and only afterward interpret event times. For independent OpenSSL, SHA-256 and SQLite commands consult `README_FIRST.md`. All evidence, domains, IPs and companies are simulated.
