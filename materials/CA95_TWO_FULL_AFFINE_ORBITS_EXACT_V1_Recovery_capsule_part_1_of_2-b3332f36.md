# material-b3332f368a5a

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# Recovery capsule part 1/2 — CA95_TWO_FULL_AFFINE_ORBITS_EXACT_V1

All nonsingular affine images of the exact CA95 integer126_g100 and integer174_g200 bodies are excluded from S=1 with no weak face equilibria about their own ordinary filled centroid, hence from own110/weak000. Not a projective/nonlinear exclusion; degenerate S1 with weak equilibria is not excluded. No improvement to canonical C622. The complete parent result is figure-0399, SHA c30ee459df73233920d909ab76375f089eae0cb264d9520a9db9ac700549c7da; the selected exact reports are included literally within this capsule, with no external source dependency.

This is a source-only capsule: the exact inputs plus the complete pinned deterministic producer, two exact certificate checkers and original full hull/mass input replay are sufficient to reconstruct the precise certificates without the originating sandbox. A cold source-only replay reconstructed all100root cases, reproduced both canonical compact certificate hashes byte-identically and passed both exact checkers. Discovery uses CPython3.13.5,NumPy2.3.5,SciPy1.17.0,one BLAS/OpenMP/MKL thread,two root jobs per body; no cross-platform numerical bit-identity is claimed. The final compact proof verification is entirely rational standard-library arithmetic and does not trust optimizer status/tolerances. The complete theorem/proof, all numeric options, input/output hashes and commands are in the decoded README, source and manifests.

Save the complete following decoder as RECOVER_AFFINE.py, save both raw payload blocks as AFFINE_PAYLOAD_1.b64 and AFFINE_PAYLOAD_2.b64 beside it (both parts are mandatory), and run `python -B -S RECOVER_AFFINE.py NEW_DIRECTORY`. Terminal markers: AFFINE_SOURCE_DICTIONARY_RECOVERY_PASS, CA95_TWO_FULL_AFFINE_ORBITS_SOURCE_ONLY_100_ROOTS_PASS, CA95_TWO_FULL_AFFINE_ORBITS_IMMUTABLE_CAPSULE_PASS. Generated proof/<body>_CERT.json and proof/<body>_VERIFIED.json remain directly verifiable using `python -B -S source/VERIFY_COMPACT.py source/<body>_REPORT.json proof/<body>_CERT.json OUT.json`.

{"b64_chars":24144,"b64_sha256":"fd9f54abc6dc61bb9643103069a838d91fef1027ca5f7fa1059f122c410c0577","decoder_bytes":1769,"decoder_sha256":"59738dbd782bc005d718167dcdfbbe8f3faecd06c1c63fa1b0772e1cb9f30bfd","dictionary_bytes":53842,"dictionary_sha256":"8d7e4b702ee3a6da61c4aeb3121fdcd2712c799fc89e1f2a64a6fc62bc2ae764","files":13,"payload_parts":[{"chars":12072,"name":"AFFINE_PAYLOAD_1.b64","sha256":"57b8ece977ad727d3e6a61136517680e2b2f0aadb23ab31f31a560c2550aca51"},{"chars":12072,"name":"AFFINE_PAYLOAD_2.b64","sha256":"6906b02c33534a0837e017a0893ae6ccdcf64310176fdfa9826633210d649250"}],"xz_bytes":18108,"xz_sha256":"2eb1be8bfbc7bab7379f2d48c2c6e037a18953a57eb82ca17de8a84660b72f06"}

## Complete decoder
```python
#!/usr/bin/env python3
"""Two-part exact source capsule CA95_TWO_FULL_AFFINE_ORBITS_EXACT_V1.
Usage: python -B -S RECOVER_AFFINE.py NEW_DIRECTORY
Extracts complete sources and inputs, then reconstructs and exactly verifies
all100root certificates. Discovery requires the pinned versions in README;
verification of the reproduced compact certificate is standard-library only.
"""
import base64,lzma,json,hashlib,sys,subprocess
from pathlib import Path
assert __debug__
def main(out):
 here=Path(__file__).resolve().parent
 e=b''.join(b''.join((here/f'AFFINE_PAYLOAD_{i}.b64').read_bytes().split())for i in (1,2))
 assert len(e)==24144 and hashlib.sha256(e).hexdigest()=="fd9f54abc6dc61bb9643103069a838d91fef1027ca5f7fa1059f122c410c0577"
 z=base64.b64decode(e,validate=True)
 assert len(z)==18108 and hashlib.sha256(z).hexdigest()=="2eb1be8bfbc7bab7379f2d48c2c6e037a18953a57eb82ca17de8a84660b72f06"
 raw=lzma.decompress(z)
 assert len(raw)==53842 and hashlib.sha256(raw).hexdigest()=="8d7e4b702ee3a6da61c4aeb3121fdcd2712c799fc89e1f2a64a6fc62bc2ae764"
 data=json.loads(raw);assert len(data)==13
 out=Path(out).resolve();out.mkdir(parents=True,exist_ok=False);src=out/'source';src.mkdir()
 for name,text in data.items():
  assert Path(name).name==name and name not in('.','..')
  (src/name).write_text(text)
 manifest=json.loads(data['SOURCE_MANIFEST.json'])
 for name,m in manifest.items():
  b=(src/name).read_bytes();assert len(b)==m['bytes'] and hashlib.sha256(b).hexdigest()==m['sha256'],name
 print('AFFINE_SOURCE_DICTIONARY_RECOVERY_PASS',len(data),flush=True)
 subprocess.run([sys.executable,'-B',str(src/'REBUILD.py'),str(out/'proof')],check=True)
 print('CA95_TWO_FULL_AFFINE_ORBITS_IMMUTABLE_CAPSULE_PASS',flush=True)
if __name__=='__main__':main(*sys.argv[1:])
```

## AFFINE_PAYLOAD_1.b64

[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
