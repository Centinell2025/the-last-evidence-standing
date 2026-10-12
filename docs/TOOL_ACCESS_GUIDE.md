**BEACON OF THE EAGLE LLC | CENTINELL SUITE DEFENSE**  
*Original simulated forensic case | Northbridge Systems | 26-NB-0918*

# Cross-platform learner toolbox

No paid software or Internet connection is required. All commands below run against *read-only copies* of included exhibits. Python 3.10+ is sufficient for the included verifiers.

## Verify exhibit bytes before interpreting them
From the extracted root:
```bash
python3 tools/verify_student.py
python3 tools/verify_witness_links.py
python3 tools/verify_network_consistency.py
```
Linux/Ubuntu/Kali/macOS (if `sha256sum` exists):
```bash
sha256sum -c manifest/SHA256SUMS.txt
openssl pkeyutl -verify -pubin -inkey evidence/vault/vault_public.pem -sigfile evidence/vault/witness.sig -rawin -in evidence/vault/witness.json
```
PowerShell on Windows:
```powershell
py -3 tools/verify_student.py
Get-FileHash evidence/artifacts/diag-bundle-0918.tgz -Algorithm SHA256
```
If OpenSSL is not installed, the Python verifier explicitly warns that signature verification was skipped. Do not report the signature as verified in that case.

## Investigate using only Python stdlib
```bash
python3 -m csv --help   # optional; CSV can also be read with a text editor
python3 -c "import csv; print(next(csv.DictReader(open('evidence/change/approved_change.csv'))))"
python3 -c "import sqlite3; c=sqlite3.connect('file:evidence/vault/vault_index.sqlite?mode=ro',uri=True); print(c.execute('PRAGMA integrity_check').fetchone())"
python3 -c "import tarfile; print(tarfile.open('evidence/artifacts/diag-bundle-0918.tgz').getnames())"
```
The optional `sqlite3`, `tshark` and `tar` command-line programs are useful but not necessary. The pcap contains a proxy CONNECT slice, not decrypted TLS. `docs/CLOCK_MODEL.csv` defines offsets: **UTC = observed wall time - offset**.

## If the verification fails
- Confirm you extracted the ZIP without editing any included files or converting text line endings.
- Run the commands from the root folder, not `docs/`.
- `python` may replace `python3` on Windows. Start with `py -3` if available.
- Never repair the originals. Extract a second clean copy and compare digests.
- Report an actual integrity error instead of changing an expected hash.
