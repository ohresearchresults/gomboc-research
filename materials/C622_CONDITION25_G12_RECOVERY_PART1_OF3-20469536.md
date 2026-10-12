# material-20469536cc44

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# Recovery capsule part 1/3 — COORD_C622_CONDITION25_G12

All three ordered parts form one complete standalone 24-file exact recovery and producer unit. This is a distinct same-C own110 rational body, NOT an edge-complexity record. Do not use a partial capsule. This part has 12500 base64 characters; SHA256 50dca34f775fb0b723842e98a1a1ad79c2705951dfbfbbb536cbec1fc81b0889.

Exact object: V176/E311/F137,C622,strict110/weak000, no primitive zero signs,348 positive centered tetrahedra and exactly zero filled first moments. Sole S original support3; sole U raw-lex94 apex(0,0,1). Both exact balanced rooted systems have every arrow >1/2250000, depths94/75. Fraction tradeoff: common centered denominator57069bits, versus56802canonical and36033G8M2. The canonical C622 record identity is unchanged.

Inputs: base64 concatenation36568characters SHA2566311ad9802f5a98c2600fa2d856a64af0f7a19d055c2d9849e0080c141f00c50; LZMA-decoded UTF-8 source dictionary93169bytes SHA256631fae9cb3d532ace34aa06230c4a5a1c03aec1d99055805e536d2442cb697b3. The dictionary includes all coordinates, exact contact dependencies, independent exhaustive-triple A and support-pair B, centered-mass integrator, exact balanced gates, complete numeric producer and local dependencies, original producer input, all25 stage outcomes/counts and frozen exact endpoint. Intermediate numerical history is not needed to reconstruct the body and is omitted from this compact unit. No ancestor sandbox, archive, or external material is required.

Save the complete Python block as RECOVER_JOIN.py and retain these three material texts as part1.md,part2.md,part3.md. Run `python -B -S RECOVER_JOIN.py part1.md part2.md part3.md C622_CONDITION25_SOURCE`, then `python -B -S C622_CONDITION25_SOURCE/REPLAY.py exact_output`. Reconstruction marker C622_CONDITION25_STANDALONE_SOURCE_RECOVERED24. Verification marker C622_CONDITION25_G12_COLD_EXACT_AB_MASS_BALANCED_PASS. Expected GENERATOR.json11841bytes SHA8b8c74c7995098ff531e5d7652da20c1afa9cbaefaeea42cd78ea54e3e7e86f5; raw.json15551bytes SHA99b773cbcf09fe227a1c19850e778dfca7f1124820b72b77c53883219e1cb697; A.json=B.json313272bytes SHA41b440d3a557a88f0abfc4b2e1bde8b99c8793b173d433c7dfad162fefd4878d. Full source/input/output byte and hash manifests are embedded and checked.

Numerical producer: `python -B C622_CONDITION25_SOURCE/REPLAY_NUMERICAL.py numerical_output`. CPython3.13.5, NumPy2.3.5, SciPy1.17.0, BLAS/OMP1thread, stages25,factor1.6,endpoint grid1e12; every other parameter is in the complete code. The exact frozen generator, not platform-dependent floating iteration identity, defines the body.

RECOVER_JOIN.py 1172bytes SHA25623476537adbb7d02316a06f0fc8e6b221cdfefb5c8f29e92666b7affcb87d3ce.

```python
"""Recover the complete C622 CONDITION25 source unit from its three materials."""
from pathlib import Path
import sys,re,json,base64,lzma,hashlib
assert __debug__
assert len(sys.argv)==5,'Give part1.md part2.md part3.md output_directory'
parts=[]
for i,name in enumerate(sys.argv[1:4],1):
 t=Path(name).read_text(encoding='utf-8');assert 'Recovery capsule part '+str(i)+'/3' in t
 matches=re.findall(r'```text\s*([A-Za-z0-9+/=\s]+?)```',t);assert len(matches)==1
 parts.append(''.join(matches[0].split()))
p=''.join(parts);assert len(p)==36568 and hashlib.sha256(p.encode()).hexdigest()=='6311ad9802f5a98c2600fa2d856a64af0f7a19d055c2d9849e0080c141f00c50'
b=lzma.decompress(base64.b64decode(p,validate=True));assert len(b)==93169 and hashlib.sha256(b).hexdigest()=='631fae9cb3d532ace34aa06230c4a5a1c03aec1d99055805e536d2442cb697b3'
d=json.loads(b);assert len(d)==24;out=Path(sys.argv[4]);out.mkdir(parents=True,exist_ok=False)
for name,t in d.items():
 q=Path(name);assert not q.is_absolute() and '..' not in q.parts;p=out/q;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(t,encoding='utf-8')
print('C622_CONDITION25_STANDALONE_SOURCE_RECOVERED',len(d),flush=True)
```

## Ordered base64 payload


[Encoded source block omitted; the code in this passage is incomplete.]
