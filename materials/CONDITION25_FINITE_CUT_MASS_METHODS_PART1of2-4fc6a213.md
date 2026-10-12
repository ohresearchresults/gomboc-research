# material-4fc6a21329b0

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# Recovery capsule part 1/2 — CONDITION25_FINITE_CUT_MASS_METHODS_V1

Read BOTH parts and concatenate only their no-whitespace base64 payloads, in order. Six complete files: SUPPORT_SCAN.py,CAP_FAMILY.py,PAIR_MERGE.py,MASS_COMP_PAIR.py,RUN_INPUTS.json,MANIFEST.json. Every method is complete, not an isolated fragment. Imports from parent source are closed by the THREE immutable parent materials [internal-source-reference],[internal-source-reference],[internal-source-reference]. Decode those24files into source/, and source REPLAY.py creates the exact original report. Exact deletion nonwinners are independently recoverable using [internal-source-reference] plus the same parents.

Methods enumerate136single-support deletions,19881count-saving cap grid cases plus9finite refinements,1455adjacent-support convex-combination replacements, and actual physical centroid compensation for the785underbudget pair replacements. All finite commands, exact input hashes and environment are in RUN_INPUTS.json. No finite failure proves an exclusion. A numeric equilibrium count is not a complete exact certificate. Only the separately exact-checked deletion bodies have accepted nonwinner classifications. No method in this capsule found a smaller accepted own110 body.

CPython3.13.5,NumPy2.3.5,SciPy1.17.0,OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=1. Source-only reconstruction uses standard library. Payload part1:7500characters SHA256d5faca47b854f19bcce09d5eecd64ce2b16393a98844aceb8ba486a9b0187a7f. Part2:3728characters SHA256c7a6b01968f9d619d13b91fa232cdfa90e5789a705550c629c8c9d0c07de0f2e. Joined11228 SHA2564bfcfdf3ff64d1e6759a763cdd3d3ed034f6bbb38c25178ff6422f27a04f0e42; decoded24853bytes SHA25638313eb77e19158db09479f56e9febf8a615df3cea4e49cca3c9b07e9f961a20.

Save both material texts as part1.md and part2.md, and this complete DECODE.py separately. Command `python -B -S DECODE.py part1.md part2.md RECOVERED_METHODS`:
```python
import sys,re,base64,zlib,json,hashlib
from pathlib import Path
H=lambda b:hashlib.sha256(b).hexdigest()
parts=[]
for path,n,h in zip(sys.argv[1:3],[7500,3728],['d5faca47b854f19bcce09d5eecd64ce2b16393a98844aceb8ba486a9b0187a7f','c7a6b01968f9d619d13b91fa232cdfa90e5789a705550c629c8c9d0c07de0f2e']):
 s=Path(path).read_text();m=re.findall(r'```base64\s*([A-Za-z0-9+/=\s]+)```',s);assert len(m)==1
 b=''.join(m[0].split()).encode();assert len(b)==n and H(b)==h;parts.append(b)
b=b''.join(parts);assert len(b)==11228 and H(b)=='4bfcfdf3ff64d1e6759a763cdd3d3ed034f6bbb38c25178ff6422f27a04f0e42'
r=zlib.decompress(base64.b64decode(b,validate=True));assert len(r)==24853 and H(r)=='38313eb77e19158db09479f56e9febf8a615df3cea4e49cca3c9b07e9f961a20'
d=json.loads(r);assert len(d)==6;o=Path(sys.argv[3]);o.mkdir(parents=True,exist_ok=False)
for name,text in d.items():
 assert Path(name).name==name;(o/name).write_text(text)
for name,w in json.loads(d['MANIFEST.json']).items():
 b=(o/name).read_bytes();assert len(b)==w['bytes'] and H(b)==w['sha256'],name
print('FINITE_CUT_MASS_METHOD_SOURCE_RECOVERY_PASS')
```
The recovered RUN_INPUTS.json specifies commands in dependency order. Expected algorithm terminal markers and numerical output names are in the complete sources. Hardware-dependent numerical trajectories may differ; their frozen finite status/selected endpoint evidence is a separate material, not implied by the source-method capsule.


[Encoded source block omitted; the code in this passage is incomplete.]
