# The Last Evidence Standing

<p align="center"><img src="branding/BEACON_OFFICIAL.svg" alt="Beacon of the Eagle LLC editorial seal" width="155" /></p>
<p align="center"><strong>BEACON OF THE EAGLE LLC</strong> · <strong>CENTINELL SUITE DEFENSE</strong><br/>Original Synthetic DFIR Training Laboratory · Case 26-NB-0918</p>


**QA-corrected v1.5 (binary evidence upload pending) | HTB Sherlock candidate · Advanced DFIR / Network Forensics · Target difficulty: Insane**

> An expert attacker erased critical forensic traces after a network breach. Investigators must correlate fragmented logs, recover hidden evidence, reconstruct the attack timeline, and prove what happened.

## Scenario

At **fictional Northbridge Systems**, investigators confront a legitimate maintenance window overlapping apparent unauthorized access to a restricted archive, an outbound inspected HTTPS upload and impaired logging. An independently preserved signed vault witness remains while ordinary source telemetry is incomplete. The case demands evidence reconciliation, not speculative attribution.

**Core investigation:** *Why was access allowed? What bytes moved? When did visibility fail? Which conclusions still stand once the logs disappear?*

## Student start

1. Obtain the student ZIP v1.5 from the author while GitHub binary upload is pending. Only use GitHub downloads once the binary upload is verified.
2. Follow `docs/CASE_BRIEF.md`, `docs/EVIDENCE_HANDLING.md`, and [30 investigation tasks](questions/INVESTIGATION.md).
3. Verify exhibit SHA-256 hashes and the detached Ed25519 signature before drawing conclusions.
4. Keep original evidence immutable and report trace IDs and normalized UTC.

## Dataset

- Identity broker session and workload token exports
- Linux jump-process and archive host audit excerpts, normal background activity
- Scoped maintenance approval and legitimate backup executions
- Gateway POST metadata, actual inspected request body, DNS and firewall records
- Valid selected PCAP showing client-to-proxy CONNECT (not plaintext HTTPS body)
- Collector health, file integrity snapshots and configuration revisions
- Independent vault witness + detached Ed25519 signature + actual SQLite index
- Clock calibration and chain-of-custody metadata, checksum manifest

**Artifact digest reference:** calculated by the learner; not printed in this public README.

## Design principles

* 30 exact-response tasks + 6 optional non-graded analyst-board determinations
* Interdependent UTC clock offsets; false maintenance/update leads; competing identity interpretations
* Real on-disk gzip/tar, SQLite, PCAP, and signed evidence witness
* Explicit proof boundaries: no claim that an account name identifies a human
* All hosts, domains, addresses, activity, content and signatures are fictional training fixtures

## Safety and authorship

Created for ethical forensic education by **Centinell Suite Defense**. This training is **not** a report of a real attack on Northbridge Systems or any customer. External addresses use documentation networks and reserved `.example` domains. There is no malware, exploitation workflow, credential attack, or Internet-dependent target. 

**Submission readiness:** author-side tested (expanded audit performed) but **not yet independently playtested or accepted by HTB**. Target difficulty and any dollar valuation are editorial goals, not a contractual promise. Store instructor answers only in separate private materials.

## Reviewer and publisher controls

- Branded student case dossier (PDF) is distributed inside the reviewed student ZIP.
- [Beacon publisher seal](branding/BEACON_OFFICIAL.svg) — editorial authorship mark, not a cryptographic signature.

**Seal distinction:** The Beacon mark identifies the publisher. It does not certify source evidence or prove an investigation conclusion. Exhibit integrity is assessed independently using the hash manifest and synthetic Ed25519 witness key.

**Confidentiality:** `INSTRUCTOR_PRIVATE/` must never be included in the learner ZIP or the public GitHub repository. The separately delivered instructor packet has the answer key, grading rationale and worked walkthrough.

## Quality-assurance edition — v1.1

- Additional [evidence claim verifier](tools/verify_witness_links.py) cross-checks the **five witness assertions** against independently provided event exhibits. A witness hash can be valid even when the upstream source is inaccurate; see the [digest-scope contract](docs/WITNESS_DIGEST_CONTRACT.md).
- [Investigation report template](docs/INVESTIGATION_REPORT_TEMPLATE.md) gives students an evidence matrix, confidence statements, provenance and an explicit observation-versus-inference split.
- [Release integrity tester](tools/verify_release.py) checks solution segregation, unsafe paths, missing members and exact manifest coverage.
- [Independent network-link checker](tools/verify_network_consistency.py) cross-references DNS, gateway, firewall, and source process trace.
- Instructor grading, calibration and platform handoff notes are **private** and deliberately absent from downloadable public materials.
- Difficulty remains **unverified** until blind expert solutions; a high number of tasks does not independently establish Insane.

**Recommended distribution:** send the learner ZIP, not the repository, to players. The repository contains QA code and editorial context; the ZIP is the authoritative student distribution.

## Student and examiner workflow | v1.2

Read the [narrative](docs/SCENARIO_STORY.md), [network diagram](docs/NETWORK_DIAGRAM.svg), [system catalog](docs/SYSTEM_AND_ACCOUNT_CATALOG.md), [synthetic-data policy](docs/SYNTHETIC_DATA_DISCLOSURE.md), and [tool guide](docs/TOOL_ACCESS_GUIDE.md). The 30 numbered questions are platform-compatible exact-response tasks. The optional analyst board is an enrichment exercise.

**Examiner-only:** deliver separately the private 30-answer worksheet, the screenshot-supported intended-path PDF and requirement matrix. They are not included in the GitHub-ready archive or the learner ZIP. Please do not publish challenge artifacts before the receiving editor authorizes public release.


## Binary publication status
Text-based material and synthetic logs are published. Binary exhibits, PDF and student ZIP must still be uploaded. **Do not submit as a complete GitHub download yet.** See [upload guide](docs/GITHUB_BINARY_UPLOAD.md). Instructor materials are excluded.


### Corporate image attribution
The emblem above is the **official image supplied by Beacon of the Eagle LLC** (white eagle, lighthouse, ocean and gold ring). The original PNG is embedded losslessly in `branding/BEACON_OFFICIAL.svg` for display in this text-only GitHub publication. The complete v1.4 ZIP also contains the unchanged original `branding/BEACON_SEAL.png`.
