#!/usr/bin/env python3
"""Validate a student or public-source release ZIP without embedding solutions."""
from pathlib import Path
import sys,zipfile,hashlib
R=Path(__file__).resolve().parents[1]
if len(sys.argv)<2:raise SystemExit('usage: python3 tools/verify_release.py path/to/student.zip [repo.zip]')
manifest=(R/'manifest/SHA256SUMS.txt').read_text().splitlines()
expected={n:hashh for hashh,n in (l.split('  ',1) for l in manifest if l.strip())}
assert len(expected)==len(manifest) and all(len(h)==64 for h in expected.values())
for item in sys.argv[1:]:
 p=Path(item)
 assert p.exists(),str(p)
 with zipfile.ZipFile(p) as z:
  names=z.namelist()
  assert z.testzip() is None,'Corrupt archive member'
  assert len(names)==len(set(names)),'Duplicate zip members'
  assert not any(n.startswith('/') or '..' in Path(n).parts or '\\' in n for n in names),'Unsafe path'
  assert not any(any(k in n.lower() for k in ('instructor_private','answer_key','walkthrough','quality_audit_private','review_findings_and_corrections','independent_review_protocol','confidence_and_limits','htb_handoff','blind_playtest')) for n in names),'Reviewer/answer contamination'
  prefix='The-Last-Evidence-Standing/'
  assert all(n.startswith(prefix) for n in names)
  if 'STUDENT' in p.name:
   content={n[len(prefix):] for n in names}
   assert content==set(expected)|{'manifest/SHA256SUMS.txt','README.md'},f'Unlisted or absent student member: {content.symmetric_difference(set(expected)|{"manifest/SHA256SUMS.txt"})}'
   assert z.read(prefix+'README.md')==(R/'README.md').read_bytes(),'Student README not synchronized with repository README'
   assert z.read(prefix+'manifest/SHA256SUMS.txt')==(R/'manifest/SHA256SUMS.txt').read_bytes()
   for name, sha in expected.items():
    assert hashlib.sha256(z.read(prefix+name)).hexdigest()==sha,'Digest mismatch in ZIP: '+name
  assert any(n.endswith('/branding/BEACON_SEAL.png') for n in names)
 print('PASS: public release safety and manifest membership: '+p.name)
