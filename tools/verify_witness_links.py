#!/usr/bin/env python3
"""Cross-check exercise witness digests with external case exhibits; no private key/answers embedded."""
from pathlib import Path
from datetime import datetime,timedelta
import csv,json,hashlib,subprocess,shutil,sqlite3,sys
R=Path(__file__).resolve().parents[1]
errors=[]
def digest(value):return hashlib.sha256(value).hexdigest()
def rows(rel):
    with (R/rel).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def lookup(rel,col,value):
    found=[r for r in rows(rel) if r.get(col)==value]
    if len(found)!=1:raise ValueError('non-unique or missing witness reference in '+rel)
    return found[0]
def parse(value):return datetime.fromisoformat(value.replace('Z','+00:00'))
try:
    witness=json.loads((R/'evidence/vault/witness.json').read_text())
    assertions=witness['assertions']
    assert len(assertions)==5 and [a['seq'] for a in assertions]==list(range(1,6))
    archive=(R/'evidence/artifacts/diag-bundle-0918.tgz').read_bytes()
    body=(R/'evidence/network/tls_inspection_body.bin').read_bytes()
    clock={r['source']:int(r['offset_ms']) for r in rows('docs/CLOCK_MODEL.csv')}
    assert archive==body,'Captured body differs from physical archive'
    def check(a,expected,event_time):
        assert a['digest']==expected,'Scoped witness digest does not match external source'
        assert parse(a['observer_event_utc'])==parse(event_time),'Witness event time diverges from external event'
        assert parse(a['observer_event_utc'])<=parse(witness['sealed_utc']),'Claim after seal'
    for a in assertions:
        ref=a['ref']
        if ref.startswith('tok-'):
            r=lookup('evidence/identity/token_issuance.csv','token_id',ref) if len([r for r in rows('evidence/identity/token_issuance.csv') if r['token_id']==ref])==1 else next(r for r in rows('evidence/identity/token_issuance.csv') if r['token_id']==ref and r['outcome']=='issued')
            val='|'.join(r[x] for x in ('token_id','session_id','principal')).encode()
            check(a,digest(val),r['event_utc'])
        elif ref.startswith('a-'):
            r=lookup('evidence/host/archive_audit.csv','event_id',ref)
            fim=[v for v in rows('evidence/host/file_integrity.csv') if v['path']==r['object_path'] and v['sha256']==digest(archive)]
            assert len(fim)==1 and int(fim[0]['size_bytes'])==len(archive),'Staged archive FIM discrepancy'
            check(a,digest(archive),r['event_utc'])
        elif ref.startswith('req-'):
            r=lookup('evidence/network/proxy.csv','request_id',ref)
            assert int(r['request_body_bytes'])==len(body) and r['request_body_sha256']==digest(body),'Gateway inspected body discrepancy'
            origin=r['src_asset'];stamp=parse(r['observed_proxy_time'])-timedelta(milliseconds=clock['nb-proxy-01'])
            check(a,digest(body),stamp.isoformat().replace('+00:00','Z'))
        elif ref.startswith('cfg-'):
            r=lookup('evidence/telemetry/config_audit.csv','revision',ref)
            val='|'.join(r[x] for x in ('key','before','after','revision')).encode()
            check(a,digest(val),r['event_utc'])
        elif ref.startswith('pulse-'):
            r=lookup('evidence/telemetry/collector_health.csv','observer_id',ref)
            val='|'.join(r[x] for x in ('source_asset','heartbeat_state','observer_utc')).encode()
            check(a,digest(val),r['observer_utc'])
        else:raise ValueError('unknown digest family')
    index=R/'evidence/vault/vault_index.sqlite'
    with sqlite3.connect('file:'+str(index)+'?mode=ro',uri=True) as c:
        assert c.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
        observed=c.execute('SELECT seq,ref,event_time_utc,origin,digest_sha256 FROM witness_index ORDER BY seq').fetchall()
    expected=[(a['seq'],a['ref'],a['observer_event_utc'],a['observer'],a['digest']) for a in assertions]
    assert observed==expected,'Unsigned secondary SQLite index mismatches witness'
    metadata=json.loads((R/'evidence/vault/seal_metadata.json').read_text())
    assert metadata['witness_sha256']==digest((R/'evidence/vault/witness.json').read_bytes())
    if shutil.which('openssl'):
        v=subprocess.run(['openssl','pkeyutl','-verify','-pubin','-inkey',str(R/'evidence/vault/vault_public.pem'),'-sigfile',str(R/'evidence/vault/witness.sig'),'-rawin','-in',str(R/'evidence/vault/witness.json')],capture_output=True)
        assert v.returncode==0,'Detached witness signature invalid'
    else:print('WARNING: OpenSSL missing; signature validation not performed')
except Exception as exc:
    print('FAIL: witness-link cross-check: '+repr(exc));sys.exit(1)
print('PASS: five scoped witness claims correlated to independent exhibits; index and seal metadata internally consistent')
