#!/usr/bin/env python3
"""Validate network/DNS/correlation constraints without leaking instructor answers."""
from pathlib import Path
from datetime import datetime,timedelta
import csv,sys
R=Path(__file__).resolve().parents[1]
def read(name):
 with (R/name).open(newline='') as f:return list(csv.DictReader(f))
def dt(value):return datetime.fromisoformat(value.replace('Z','+00:00'))
try:
 clocks={x['source']:int(x['offset_ms']) for x in read('docs/CLOCK_MODEL.csv')}
 proxies=[p for p in read('evidence/network/proxy.csv') if p['method']=='POST' and int(p['request_body_bytes'])>0]
 dns=read('evidence/network/dns.csv');flows=read('evidence/network/firewall.csv')
 jump=read('evidence/host/jump_process.csv');audit=read('evidence/host/archive_audit.csv')
 assert proxies,'No inspected POST available'
 for p in proxies:
  t=dt(p['observed_proxy_time'])-timedelta(milliseconds=clocks['nb-proxy-01'])
  resolution=[d for d in dns if d['client_ip']==p['src_ip'] and d['qname']==p['host'] and d['answer_ip']==p['resolved_ip'] and dt(d['event_utc'])<=t]
  assert resolution,'No prior consistent independent DNS resolution'
  transit=[f for f in flows if f['dst_ip']==p['resolved_ip'] and f['action']=='allow' and dt(f['start_utc'])<=t<=dt(f['end_utc']) and int(f['out_bytes'])>=int(p['request_body_bytes'])]
  assert transit,'No matching egress window/byte-count in independent firewall'
  assert any('diag-ship' in a['process'] and a['trace_id']==p['trace_id'] and dt(a['event_utc'])<=t for a in audit),'No matching staged host transfer evidence'
  assert any(p['request_id'] in j['command_line'] and 'diag-ship' in j['command_line'] for j in jump),'No matching process intent in jump log'
except Exception as exc:print('FAIL: independent network correlation: '+repr(exc));sys.exit(1)
print('PASS: DNS -> inspected POST -> independent firewall transit -> host/jump trace consistency')
