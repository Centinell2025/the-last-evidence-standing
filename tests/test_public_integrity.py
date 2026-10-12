from pathlib import Path
import hashlib, subprocess, unittest, tempfile, shutil
R=Path(__file__).resolve().parents[1]
class ExhibitIntegrity(unittest.TestCase):
    def test_offline_verifier(self):
        run=subprocess.run(['python3',str(R/'tools/verify_student.py')],capture_output=True,text=True)
        self.assertEqual(run.returncode,0,run.stdout+run.stderr)
    def test_manifest_covers_all_evidence(self):
        rows=(R/'manifest/SHA256SUMS.txt').read_text().splitlines()
        listed={ln.split('  ',1)[1] for ln in rows if ln.strip()}
        actual={p.relative_to(R).as_posix() for p in (R/'evidence').rglob('*') if p.is_file()}
        self.assertLessEqual(actual,listed)
    def test_seal_not_in_binary_exhibits(self):
        seal=(R/'branding/BEACON_SEAL.png').read_bytes()
        self.assertNotIn(seal,(R/'evidence/vault/witness.json').read_bytes())
    def test_expected_binary_signatures(self):
        self.assertTrue((R/'evidence/artifacts/diag-bundle-0918.tgz').read_bytes().startswith(b'\x1f\x8b'))
        self.assertTrue((R/'evidence/vault/vault_index.sqlite').read_bytes().startswith(b'SQLite format 3'))
if __name__=='__main__':unittest.main()
