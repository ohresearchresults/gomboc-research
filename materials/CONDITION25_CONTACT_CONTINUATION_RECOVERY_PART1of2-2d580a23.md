# material-2d580a230214

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# Recovery capsule part 1/2 — CONDITION25_CONTACT_CONTINUATION_V1

Read BOTH parts completely and concatenate only the no-whitespace base64 payloads in order. This preserves seven complete runnable source units plus RUN_INPUTS.json and MANIFEST.json,9files total: EDGEFLOW.py,EDGE_HOMOTOPY.py,MAKE_V2.py,EDGE_LP_PROBE.py,DELETE_REPAIR.py,BAD_ROOT_CONTINUATION.py,inspect_start.py. MAKE_V2.py is a complete SHA-checked deterministic patch producing EDGE_HOMOTOPY_V2.py. All helpers imported by these units are in the exact parent source closure below; no omitted code or originating sandbox dependency.

Parent source dependencies ALL3: [internal-source-reference],[internal-source-reference],[internal-source-reference]. Decode their exact24-file source dictionary into source/. Run its REPLAY.py to create exact/B.json. For exact C616 deletion parent reports, also use [internal-source-reference], reconstructing its99/A.json and117/A.json as del99_exact/A.json and del117_exact/A.json. No worker result is silently renamed. These two deletion generators are exact reindexings: the methods assert RECONSTRUCT equality with the literal removed-support H before optimizing.

Versions CPython3.13.5,NumPy2.3.5,SciPy1.17.0; OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1. All initial inputs, non-default finite commands, provenance hashes and dependency IDs are in RUN_INPUTS.json. Numerical QP/HiGHS trajectories can vary with hardware/time limits; no finite failure is an exclusion. Rounded geometry is not exact acceptance. Frozen useful endpoint capsules are separate from this source-method capsule.

Integrity: part1 length7500 SHA25678f142f7b6b48b4584ed1612771593860cceffc0b5a598eaa294a50cb1ed8b83; part2 length3560 SHA256528c67562559850d22b385014127d9356bf91db3f39ad67cecfe87f7d478a912. Joined length11060 SHA256b2329054b5aa11ec23835357129c6b4ffcbb81ed82b5500cc554543eaa489fa4. zlib-decoded dictionary32598bytes SHA256f71e5cd90327345456d5070abe61ed836083497cb3d69bb1cd784a1d278699f8.

Save the two material texts as part1.md and part2.md, then run this complete standard-library decoder as `python -B -S DECODE.py part1.md part2.md RECOVERED_METHODS`:
```python
import sys,re,base64,zlib,json,hashlib
from pathlib import Path
H=lambda b:hashlib.sha256(b).hexdigest()
parts=[]
for path,n,h in zip(sys.argv[1:3],[7500,3560],['78f142f7b6b48b4584ed1612771593860cceffc0b5a598eaa294a50cb1ed8b83','528c67562559850d22b385014127d9356bf91db3f39ad67cecfe87f7d478a912']):
 s=Path(path).read_text();m=re.findall(r'```base64\s*([A-Za-z0-9+/=\s]+)```',s);assert len(m)==1
 b=''.join(m[0].split()).encode();assert len(b)==n and H(b)==h;parts.append(b)
b=b''.join(parts);assert len(b)==11060 and H(b)=='b2329054b5aa11ec23835357129c6b4ffcbb81ed82b5500cc554543eaa489fa4'
r=zlib.decompress(base64.b64decode(b,validate=True));assert len(r)==32598 and H(r)=='f71e5cd90327345456d5070abe61ed836083497cb3d69bb1cd784a1d278699f8'
d=json.loads(r);assert len(d)==9;o=Path(sys.argv[3]);o.mkdir(parents=True,exist_ok=False)
for name,text in d.items():
 assert Path(name).name==name;(o/name).write_text(text)
for name,w in json.loads(d['MANIFEST.json']).items():
 b=(o/name).read_bytes();assert len(b)==w['bytes'] and H(b)==w['sha256'],name
print('CONTACT_CONTINUATION_SOURCE_RECOVERY_PASS')
```
Run `python -B -S MAKE_V2.py` in recovered directory; expected EDGE_HOMOTOPY_V2_EXACT_SOURCE_PATCH_PASS. Execute selected complete finite commands in RUN_INPUTS.json with the decoded parent source and exact reports placed as specified. EDGE_HOMOTOPY_V2 changes only stage length tolerance (default1e-7), not physical/polar escape or convexity acceptance; it does not make a finite approximate collision exact. BAD_ROOT_CONTINUATION raises its one negative angular floor with positive additive safety, preserving all other physical/polar escape floors, unlike multiplying a negative target by>1 or unconstrained loss fitting. Expected algorithm terminal markers appear in each complete source; BAD_ROOT_CONTINUATION_FINITE_DONE and DELETE_FULL_GEOMETRY_FINITE_DONE are numerical results only.


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]
