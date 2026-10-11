# material-4f77de5b7b74

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: unreviewed-encoded-blocks-omitted.

---

# Recovery capsule part 1/4 — COORD_ROOTED_THALES_NUMERICAL_METHODS_V1

All FOUR parts are mandatory, order1,2,3,4. Complete15-file dictionary contains seven full numerical producers/companions, literal C126/D100 inputs, every continuation input, all nondefault settings,21 compact best-checkpoint records, deterministic23-checkpoint restorer, run-by-case helper, per-source and reproduced-checkpoint byte/SHA manifests, campaign index and scientific README. No own110 winner or family exclusion. This is separate from the two-part exact-five-body capsule. Literal retained checkpoint counts/losses override earlier transient prose.

Save the text block as ROOTED_THALES_NUMERIC_1.b64. This part has 11764 ASCII payload bytes (whitespace ignored), SHA256 653487e617e5958fc8bd7d3bc28d3f2c2df0d8ece2f3828a5a9079636809d749.

Save the Python block as RECOVER_ROOTED_THALES_NUMERIC.py beside all four payloads. Run `python -B -S RECOVER_ROOTED_THALES_NUMERIC.py NEW_SOURCE_DIRECTORY`. Stdlib recovery, tested3.13.5, assertions enabled. Numerical use requires NumPy2.3.5,SciPy1.17.0,Torch2.10.0+cpu,binary64,one thread. Different optimizer builds need not reproduce trajectories; the frozen checkpoint inputs and separately audited rational definitions are authoritative. Final marker: COORD_ROOTED_THALES_NUMERICAL_METHODS_V1_IMMUTABLE_CAPSULE_PASS.

```python
from pathlib import Path
import base64,hashlib,json,lzma,sys,subprocess
assert __debug__
HERE=Path(__file__).resolve().parent
s=''.join(''.join((HERE/f'ROOTED_THALES_NUMERIC_{i}.b64').read_text().split())for i in (1,2,3,4))
assert len(s)==47056 and hashlib.sha256(s.encode()).hexdigest()=='aa86fe6492a1ea4900e908d1e78f69b00b11e47fd947b689959994b3da139fe7'
z=base64.b64decode(s,validate=True)
assert len(z)==35292 and hashlib.sha256(z).hexdigest()=='aa2dcab769f7a2265ce00b9ae348b0d2ac1431645f391298c01b0822f415f282'
b=lzma.decompress(z)
assert len(b)==147499 and hashlib.sha256(b).hexdigest()=='8cc2809c341cee93a574276799cc1e0bc292d08f38e567e5e64bbce09784205b'
d=json.loads(b);assert len(d)==15
out=Path(sys.argv[1]).resolve();out.mkdir(parents=True,exist_ok=False)
for name,text in d.items():
 p=out/name;assert p.resolve().is_relative_to(out)
 p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode())
for name,e in json.loads(d['SOURCE_MANIFEST.json']).items():
 c=(out/name).read_bytes();assert len(c)==e['bytes'] and hashlib.sha256(c).hexdigest()==e['sha256'],name
print('ROOTED_THALES_NUMERICAL_15_SOURCE_FILES_RECOVERY_PASS',flush=True)
subprocess.run([sys.executable,'-B','-S',str(out/'RESTORE_CHECKPOINTS.py'),str(out/'WORKING')],check=True,cwd=out)
print('COORD_ROOTED_THALES_NUMERICAL_METHODS_V1_IMMUTABLE_CAPSULE_PASS',flush=True)
```


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
