from pathlib import Path
import csv,subprocess,unittest
R=Path(__file__).resolve().parents[1]
class ScopedWitness(unittest.TestCase):
 def test_witness_links_verified(self):
  v=subprocess.run(['python3',str(R/'tools/verify_witness_links.py')],capture_output=True,text=True)
  self.assertEqual(v.returncode,0,v.stdout+v.stderr)
 def test_clocks_defined_for_active_sensors(self):
  with (R/'docs/CLOCK_MODEL.csv').open(newline='') as f:clock=list(csv.DictReader(f))
  self.assertTrue(clock)
  self.assertTrue(all(int(c['error_bound_ms'])>=0 for c in clock))
  self.assertTrue(any(int(c['offset_ms'])!=0 for c in clock))
 def test_no_instructor_documents_inside_learner_docs(self):
  self.assertFalse(any((R/'docs'/n).exists() for n in ('HTB_HANDOFF.md','CONFIDENCE_AND_LIMITS.md','INDEPENDENT_REVIEW_PROTOCOL.md')))
if __name__=='__main__':unittest.main()
