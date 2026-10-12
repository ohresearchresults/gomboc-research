# material-6359c938c108

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 2/2 — CONDITION25_FINITE_CUT_MASS_METHODS_V1

Pair with [internal-source-reference]. IMPORTANT TRANSPORT CORRECTION: part1's literal base64 contains one accidental extra I in the unique substring Tp3T4kFIGIIko. Before validating or decoding its payload, replace that exact substring with Tp3T4kFIGIko. This is a complete exact one-character repair, not an omitted data dependency. The corrected payload must satisfy the original7500length/SHA256d5faca47b854f19bcce09d5eecd64ce2b16393a98844aceb8ba486a9b0187a7f. No other changes are authorized. Use the complete corrected decoder below, which supersedes part1's uncorrected decoder.

Part2 length3728 SHA256c7a6b01968f9d619d13b91fa232cdfa90e5789a705550c629c8c9d0c07de0f2e. Joined11228 SHA2564bfcfdf3ff64d1e6759a763cdd3d3ed034f6bbb38c25178ff6422f27a04f0e42; decoded24853bytes SHA25638313eb77e19158db09479f56e9febf8a615df3cea4e49cca3c9b07e9f961a20. Six complete source/config/manifest files. Explicit parent closure and finite-method evidence boundary are in part1. No smaller own110 body is asserted.

Command `python -B -S DECODE.py part1.md part2.md RECOVERED_METHODS` with this complete DECODE.py:
```python
import sys,re,base64,zlib,json,hashlib
from pathlib import Path
H=lambda b:hashlib.sha256(b).hexdigest()
parts=[]
for i,(path,n,h) in enumerate(zip(sys.argv[1:3],[7500,3728],['d5faca47b854f19bcce09d5eecd64ce2b16393a98844aceb8ba486a9b0187a7f','c7a6b01968f9d619d13b91fa232cdfa90e5789a705550c629c8c9d0c07de0f2e'])):
 s=Path(path).read_text();m=re.findall(r'```base64\s*([A-Za-z0-9+/=\s]+)```',s);assert len(m)==1
 b=''.join(m[0].split()).encode()
 if i==0 and b'Tp3T4kFIGIIko' in b:
  assert b.count(b'Tp3T4kFIGIIko')==1;b=b.replace(b'Tp3T4kFIGIIko',b'Tp3T4kFIGIko')
 assert len(b)==n and H(b)==h,(i,len(b),H(b));parts.append(b)
b=b''.join(parts);assert len(b)==11228 and H(b)=='4bfcfdf3ff64d1e6759a763cdd3d3ed034f6bbb38c25178ff6422f27a04f0e42'
r=zlib.decompress(base64.b64decode(b,validate=True));assert len(r)==24853 and H(r)=='38313eb77e19158db09479f56e9febf8a615df3cea4e49cca3c9b07e9f961a20'
d=json.loads(r);assert len(d)==6;o=Path(sys.argv[3]);o.mkdir(parents=True,exist_ok=False)
for name,text in d.items():
 assert Path(name).name==name;(o/name).write_text(text)
for name,w in json.loads(d['MANIFEST.json']).items():
 b=(o/name).read_bytes();assert len(b)==w['bytes'] and H(b)==w['sha256'],name
print('FINITE_CUT_MASS_METHOD_SOURCE_RECOVERY_PASS')
```


[Encoded source block omitted; the code in this passage is incomplete.]
