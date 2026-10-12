from pathlib import Path
import tempfile,shutil,subprocess,csv,unittest
R=Path(__file__).resolve().parents[1]
class MutationResistance(unittest.TestCase):
 def run_mutation(self,rel,change,tool='verify_witness_links.py'):
  with tempfile.TemporaryDirectory() as temp:
   base=Path(temp)
   for d in ('docs','evidence','tools'):
    shutil.copytree(R/d,base/d,ignore=shutil.ignore_patterns('__pycache__'))
   f=base/rel
   before=f.read_bytes();after=change(before)
   self.assertNotEqual(before,after)
   f.write_bytes(after)
   s=subprocess.run(['python3',str(base/'tools'/tool)],capture_output=True,text=True)
   self.assertNotEqual(s.returncode,0,'Tampering escaped cross-source verification: '+rel)
 def test_changed_identity_reference_is_detected(self):
  self.run_mutation('evidence/identity/token_issuance.csv',lambda b:b.replace(b'sess-72bf',b'sess-9xxx',1))
 def test_changed_control_plane_record_is_detected(self):
  self.run_mutation('evidence/telemetry/config_audit.csv',lambda b:b.replace(b'true,false',b'true,true',1))
 def test_changed_collector_state_is_detected(self):
  self.run_mutation('evidence/telemetry/collector_health.csv',lambda b:b.replace(b'01:24:29Z,nb-dfs-02,missing',b'01:24:29Z,nb-dfs-02,healthy',1))
 def test_changed_dns_mapping_detected(self):
  self.run_mutation('evidence/network/dns.csv',lambda b:b.replace(b'198.51.100.77',b'198.51.100.66'),tool='verify_network_consistency.py')
 def test_changed_gateway_ip_detected(self):
  self.run_mutation('evidence/network/proxy.csv',lambda b:b.replace(b'198.51.100.77',b'198.51.100.65'),tool='verify_network_consistency.py')
if __name__=='__main__':unittest.main()
