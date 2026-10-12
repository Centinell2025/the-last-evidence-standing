> **BEACON OF THE EAGLE LLC — CENTINELL SUITE DEFENSE**  
> Synthetic case material · Editorial publisher seal · NOT a live incident

# Evidence use and integrity

## Preserve first
Work on local copies. Record filename, SHA-256, source ID and access time. **Do not modify original exhibits**. Confirm manifest matches before solving.

Run from the directory containing this file's parent project:
```sh
sha256sum -c manifest/SHA256SUMS.txt
openssl pkeyutl -verify -pubin -inkey evidence/vault/vault_public.pem \
  -sigfile evidence/vault/witness.sig -rawin -in evidence/vault/witness.json
```

Also run `python3 tools/verify_network_consistency.py` to validate DNS, gateway, firewall and host trace joins. Run `python3 tools/verify_witness_links.py` as a second, logically distinct check of five digest references and their source event times. This validates local exhibit bytes and the **simulated** signed vault witness. A signature does not prove an assertion's factual accuracy, independent origins, legal chain of custody or which human held a token. Evaluate corroboration and source trust separately.

## Suggested pivots
- Identify the legitimate change and its **explicitly excluded operations**.
- Normalize event clocks with `docs/CLOCK_MODEL.csv` (correct time = observed time minus offset).
- Compare identity broker, source-side audit, independent network observers and the sealed vault witness.
- Distinguish archive *creation*, HTTP *request upload*, HTTP *response*, remote *access* and attacker *identity*.
- Investigate misleading benign update traffic and the time of last healthy collector ingestion.

## Packet capture limitations
The included pcap contains a valid selected TCP CONNECT exchange only; it cannot independently prove the HTTPS request body. The lab's simulated gateway had decryption enabled for managed hosts and wrote `tls_inspection_body.bin` under its policy. Confirm its SHA-256 is equal to the staged payload and gateway digest.

## Package controls
There are no real employee credentials, malware binaries, third-party secrets, or targets. Reserved domains/IPs are nonoperational fixtures. The package is intentionally offline-friendly. There is no external login or flag server.
