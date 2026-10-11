# material-a591c12d1865

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: unreviewed-encoded-blocks-omitted.

---

# Recovery capsule part 1/2 — COORD_RATIONAL_THALES_AND_DUAL_FIVE_NONWINNERS_V1

Both parts are mandatory and ordered 1,2. Self-contained 18-file exact source dictionary; five NONWINNERS, no new own110. Exact C126312, C132211, two distinct C324121 rational-halfspace bodies, and rational-tree C132312; all weak000. Canonical C622 unchanged. Source README contains proof of the rational guarded Thales tree and scopes the two fixed-finite-set rooted-basin barriers. Complete independent A/B hull/true-incidence/own-filled-mass/all-feature audits, positive centered integration, controls and output byte/SHA identities are included.

Save this part's text block as RATIONAL_THALES_VERIFIED_1.b64 (whitespace ignored). Payload in this part: 11396 ASCII bytes, SHA256 6b0252f21f50fa4fe774e54bae40de94717a8b1b8a23d8092aa1651e27b1b1ac.

Save the Python block as RECOVER_RATIONAL_THALES_VERIFIED.py next to BOTH payload files. Run `python -B -S RECOVER_RATIONAL_THALES_VERIFIED.py NEW_SOURCE_DIRECTORY`. Stdlib only, tested CPython3.13.5; assertions enabled, no -O. SOURCE_MANIFEST.json fixes every recovery source/input; EXPECTED_GENERATOR.json and EXPECTED_EXACT.json fix all regenerated output bytes/hashes. Final marker: COORD_RATIONAL_THALES_AND_DUAL_FIVE_NONWINNERS_V1_IMMUTABLE_CAPSULE_PASS.

```python
from pathlib import Path
import base64,hashlib,json,lzma,sys,subprocess
assert __debug__
HERE=Path(__file__).resolve().parent
s=''.join(''.join((HERE/f'RATIONAL_THALES_VERIFIED_{i}.b64').read_text().split()) for i in (1,2))
assert len(s)==22792 and hashlib.sha256(s.encode()).hexdigest()=='19af21748e584bce86d6e0ed04b10e53fd5d09eef8c889d3e9a944580a07d6cd'
z=base64.b64decode(s,validate=True)
assert len(z)==17092 and hashlib.sha256(z).hexdigest()=='75491e9cfd6f1f760df22bac8ea9bc9ef62ac8e0b1799a3b593ca47f9c646cd0'
b=lzma.decompress(z)
assert len(b)==53149 and hashlib.sha256(b).hexdigest()=='a01a7f5b6aa5dd27207d116822feb2d64a26bb73048eec7c29cfb75eda0a265e'
d=json.loads(b);assert len(d)==18
out=Path(sys.argv[1]).resolve();out.mkdir(parents=True,exist_ok=False)
for name,text in d.items():
 q=out/name;assert q.resolve().is_relative_to(out)
 q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(text.encode())
m=json.loads(d['SOURCE_MANIFEST.json'])
for name,e in m.items():
 c=(out/name).read_bytes();assert len(c)==e['bytes'] and hashlib.sha256(c).hexdigest()==e['sha256'],name
print('RATIONAL_THALES_VERIFIED_18_FILES_RECOVERY_PASS',flush=True)
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY_VERIFIED.py'),str(out/'PROOF')],check=True,cwd=out)
print('COORD_RATIONAL_THALES_AND_DUAL_FIVE_NONWINNERS_V1_IMMUTABLE_CAPSULE_PASS',flush=True)
```


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
