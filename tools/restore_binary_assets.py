#!/usr/bin/env python3
"""Rehydrate public student assets from checked, documented Base64 archive slices.
No remote downloads. No private instructor materials. Python stdlib only.
"""
from pathlib import Path
from hashlib import sha256
import base64
import io
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / '.binary-seed'
EXPECTED_STUDENT_SHA256 = '27de88fdc5a61cf57507b6f670fcd8795c85ce04a8178af2404c2b9531f35287'
STUDENT_REL = 'downloads/The-Last-Evidence-Standing-STUDENT.zip'
ROOT_IN_ZIP = 'The-Last-Evidence-Standing/'
ASSETS = (
    'branding/BEACON_SEAL.png',
    'docs/NETWORK_DIAGRAM.png',
    'docs/THE_LAST_EVIDENCE_STANDING_STUDENT_DOSSIER.pdf',
    'evidence/artifacts/diag-bundle-0918.tgz',
    'evidence/network/selected_proxy_slice.pcap',
    'evidence/network/tls_inspection_body.bin',
    'evidence/vault/vault_index.sqlite',
    'evidence/vault/witness.sig',
)


def main():
    parts = sorted(SEED.glob('part-*.b64'))
    if len(parts) != 21:
        raise SystemExit(f'Expected 21 public asset chunks; found {len(parts)}')
    archive = base64.b64decode(''.join(p.read_text('ascii') for p in parts), validate=True)
    digest = sha256(archive).hexdigest()
    if digest != EXPECTED_STUDENT_SHA256:
        raise SystemExit(f'Archive digest mismatch: {digest}')
    checks = {}
    for line in (ROOT / 'manifest/SHA256SUMS.txt').read_text().splitlines():
        if line.strip():
            checksum, name = line.split('  ', 1)
            checks[name] = checksum
    with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
        if zipped.testzip() is not None:
            raise SystemExit('Student archive CRC check failed')
        content = {}
        for relative in ASSETS:
            data = zipped.read(ROOT_IN_ZIP + relative)
            actual = sha256(data).hexdigest()
            if checks.get(relative) != actual:
                raise SystemExit(f'Manifest hash mismatch: {relative}')
            content[relative] = data
    content[STUDENT_REL] = archive
    for relative, data in content.items():
        destination = ROOT / relative
        if destination.is_file() and destination.read_bytes() != data:
            raise SystemExit(f'Refusing to overwrite conflicting asset: {relative}')
    for relative, data in content.items():
        target = ROOT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        print(f'RESTORED {relative} ({len(data):,} bytes)')
    print(f'PASS: restored 9 exact public binary assets; student ZIP SHA256 {digest}')


if __name__ == '__main__':
    main()