> **BEACON OF THE EAGLE LLC — CENTINELL SUITE DEFENSE**  
> Synthetic training case · Integrity guide; **not** a real-world certificate

# Witness assertion digest contract

The five signed witness assertions are an **exercise-specific summary**, not signatures over complete log streams. Their `digest` fields use intentionally different scoped constructions, defined here so students can reproduce them using independent evidence records:

| Evidence family | SHA-256 input, exact UTF-8 bytes |
|---|---|
| Identity token | `token_id + "|" + session_id + "|" + principal` from the matching issuance row |
| Archive operation | The bytes of the physical staged `.tgz`, **not** the CSV audit event row; verify the audit creation path against the FIM scan |
| Proxy inspected request | The binary retained inspection body, **not** the proxy CSV row; compare size/digest from gateway, and normalize the gateway timestamp |
| Config change | `key + "|" + before + "|" + after + "|" + revision` from the matching config audit row |
| Collector observation | `source_asset + "|" + heartbeat_state + "|" + observer_utc` from the matching observer row |

Each ASCII vertical bar is one byte (0x7C). No trailing newline is hashed. The detached signature covers the **literal bytes** of `witness.json` and does not cover the original CSV or binary exhibits. The vault SQLite index repeats digests and metadata, but the index file itself is not signed by this witness. The provided training public key has no independently certified issuer.

Use `python3 tools/verify_witness_links.py` to check that the asserted references, digest scope and observed times can be reproduced from the student exhibits. Passing these checks strengthens the *internal consistency* of the supplied material, not the external authenticity or factual truth of its creators.
