#!/usr/bin/env python3
"""Read-only offline exhibit audit; Python 3.10+ stdlib; optionally verifies witness with OpenSSL."""
from pathlib import Path
import hashlib, csv, json, sqlite3, subprocess, shutil, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
manifest=ROOT/'manifest/SHA256SUMS.txt'
for ln in manifest.read_text().splitlines():
    if not ln.strip(): continue
    expected,filename=ln.split('  ',1)
    p=ROOT/filename
    if not p.is_file(): errors.append('missing '+filename);continue
    got=hashlib.sha256(p.read_bytes()).hexdigest()
    if got!=expected: errors.append('digest mismatch '+filename)
archive=(ROOT/'evidence/artifacts/diag-bundle-0918.tgz').read_bytes()
body=(ROOT/'evidence/network/tls_inspection_body.bin').read_bytes()
if archive!=body: errors.append('archive and gateway captured body differ')
p=ROOT/'evidence/vault/vault_index.sqlite'
try:
    with sqlite3.connect('file:'+str(p)+'?mode=ro',uri=True) as c:
        if c.execute('PRAGMA integrity_check').fetchone()[0]!='ok':errors.append('SQLite integrity failed')
        cnt=c.execute('SELECT COUNT(*) FROM witness_index').fetchone()[0]
        if cnt!=5:errors.append('vault index row count')
except Exception as e:errors.append('SQLite: '+str(e))
if shutil.which('openssl'):
    run=subprocess.run(['openssl','pkeyutl','-verify','-pubin','-inkey',str(ROOT/'evidence/vault/vault_public.pem'),'-sigfile',str(ROOT/'evidence/vault/witness.sig'),'-rawin','-in',str(ROOT/'evidence/vault/witness.json')],capture_output=True,text=True)
    if run.returncode:errors.append('vault signature verification failed')
else: print('OpenSSL unavailable: detached signature verification SKIPPED')
if errors:
    print('FAILED\n'+'\n'.join(errors));sys.exit(1)
print('PASS: SHA-256 manifest, archive/body match, SQLite integrity and 5 witness rows'+(' and Ed25519' if shutil.which('openssl') else ''))
