# Network and identity capture assumptions

The range `192.0.2.0/24` (TEST-NET-1) describes a **simulated external-origin value** recorded in the identity broker's forwarding metadata. It is *not* a routable production address. `198.51.100.0/24` (TEST-NET-2) similarly describes the fabricated external destination; `.example` domains are reserved for illustrations.

`source_ip` in identity records represents the **client-origin value supplied by the access broker**, not the archive host's immediate TCP peer. The machine-name client claim and device certificate fingerprint are not independently verified proof of a unique physical jump host or a specific employee. Treat their reliability as disputed until corroborated.

Proxy records use the gateway's **local wall clock** (92 seconds fast), jump records the jump host's wall clock (43 seconds slow); all other files use UTC within the documented uncertainty bands. Centralized event-reception UTC is independent of the event's originating clock.

The inspection gateway was configured to decrypt traffic for internal managed systems using a lab enterprise CA and to preserve selected policy-matched request bodies. The capture includes benign synthetic bytes only. The `.pcap` contains **only a short client-to-proxy HTTP CONNECT slice** and provides timing/destination corroboration, not decrypted HTTPS content. A received 201 response confirms that the gateway saw a successful HTTP upload response, but does not prove a human adversary later accessed those bytes.

## Clock uncertainty and replay caution

`offset_ms` is a best-estimate wall-clock adjustment; uncertainty is specified in `error_bound_ms`. A corrected timestamp is a point estimate, **not** a zero-width interval. When interpreting two close events, consider the sum of uncertainties before alleging exact temporal causality. The synthetic data does not include packet-complete TLS decryption or a destination-side authenticated receipt. No sensitive real-world data is present.
