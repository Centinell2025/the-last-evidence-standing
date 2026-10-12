"""Public checks validate the evidence carrier, never encode the challenge solutions."""
from pathlib import Path
import hashlib
import shutil
import struct
import subprocess
import tempfile
import unittest
import zipfile

R=Path(__file__).resolve().parents[1]


def internet_checksum(payload: bytes) -> int:
    if len(payload)%2:
        payload += b'\0'
    arr=struct.unpack('!%dH' % (len(payload)//2),payload)
    total=sum(arr)
    while total>>16:
        total=(total & 0xffff)+(total>>16)
    return (~total)&0xffff

class TrustBoundaries(unittest.TestCase):
    def test_tampered_signed_witness_is_rejected(self):
        if not shutil.which('openssl'):
            self.skipTest('OpenSSL not installed')
        orig=(R/'evidence/vault/witness.json').read_bytes()
        with tempfile.TemporaryDirectory() as td:
            damaged=Path(td)/'modified.json'
            damaged.write_bytes(orig[:-2]+b' '+orig[-2:])
            result=subprocess.run([
                'openssl','pkeyutl','-verify','-pubin','-inkey',str(R/'evidence/vault/vault_public.pem'),
                '-sigfile',str(R/'evidence/vault/witness.sig'),'-rawin','-in',str(damaged)
            ],capture_output=True)
            self.assertNotEqual(result.returncode,0,'Tampered witness unexpectedly verified')
    def test_payload_tamper_detectable(self):
        original=(R/'evidence/artifacts/diag-bundle-0918.tgz').read_bytes()
        flip=bytearray(original)
        flip[len(flip)//2]^=0x01
        self.assertNotEqual(hashlib.sha256(flip).digest(),hashlib.sha256(original).digest())
    def test_pcap_packet_structure_and_checksums(self):
        cap=(R/'evidence/network/selected_proxy_slice.pcap').read_bytes()
        magic,major,minor,tz,sig,caplen,link=struct.unpack_from('<IHHIIII',cap)
        self.assertEqual((magic,major,minor,link),(0xa1b2c3d4,2,4,1))
        i=24; n=0
        while i<len(cap):
            self.assertLessEqual(i+16,len(cap))
            sec,us,inc,orig=struct.unpack_from('<IIII',cap,i)
            self.assertEqual(inc,orig)
            frame=cap[i+16:i+16+inc]
            self.assertEqual(len(frame),inc)
            self.assertEqual(frame[12:14],b'\x08\x00')
            ip=frame[14:]
            hlen=(ip[0]&15)*4
            self.assertEqual(ip[0]>>4,4)
            self.assertEqual(ip[9],6)
            self.assertEqual(internet_checksum(ip[:hlen]),0)
            total=struct.unpack_from('!H',ip,2)[0]
            self.assertEqual(len(ip),total)
            tcp=ip[hlen:total]
            pseudo=ip[12:20]+bytes([0,6])+struct.pack('!H',len(tcp))
            self.assertEqual(internet_checksum(pseudo+tcp),0)
            n+=1;i+=16+inc
        self.assertEqual(i,len(cap))
        self.assertGreaterEqual(n,5)
    def test_student_archive_has_no_instructor_answers(self):
        p=R/'downloads/The-Last-Evidence-Standing-STUDENT.zip'
        if not p.exists():self.skipTest('Source checkout lacks prebuilt archive')
        with zipfile.ZipFile(p) as z:
            self.assertIsNone(z.testzip())
            self.assertFalse(any('INSTRUCTOR_PRIVATE' in name or 'ANSWER_KEY' in name or 'WALKTHROUGH' in name for name in z.namelist()))

if __name__=='__main__': unittest.main()
