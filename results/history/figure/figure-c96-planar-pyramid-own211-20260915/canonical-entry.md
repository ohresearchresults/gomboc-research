
## 2026-09-15T21:42:01.239Z

### Complete recovery capsule — COORD_C96_PLANAR24_PYRAMID_OWN211

Executed the planar-coalescence test suggested in the previous C138 capsule. The new **uniform filled pyramid over a24-gon** has **V25/E48/F25, C96, strict own211/weak000**,24 triangular side facets and one genuine24-gonal maximal facet. The21 fewer true edges relative to C138 come from exact facet coalescence, not counting triangulation diagonals differently. It is a useful small arithmetic/architecture nonwinner, NOT a Gömböc or a new own110 record. Both full exact auditors and third centred integer-tetrahedron integration passed. No theorem excluding all pyramids is asserted.

The exact construction orthogonally projects the24 non-apex C138 points onto the plane4x+11y=0, keeps C138 input15 as the off-plane apex, multiplies all coordinates by137 and makes an integer translation. It does NOT use an affine change of the whole body, and its filled centre is recomputed.

**Complete generator planar25.py**,1383bytes,SHAf60b6aa912c78bffc96a70f9273988f829e5f6c8e2ea1d87c3b1e09340da989e, UTF-8/LF with final newline. Dependencies: exact POINTS25.json425bytes/SHA1be5293390fbabf8b86b02805771d0fed82fddd2c61678b58d36c7bab9f93cd8 fully given in preceding21:35:59 capsule; unchanged complete exact_points.py and three exact core sources with hashes there. CPython3.13.5 stdlib only.

```python
"""Exact orthogonal planar-base coalescence of the C138 integer25 body."""
import hashlib,json,sys
from pathlib import Path
from exact_points import encoded,make
sys.set_int_max_str_digits(0)
def main():
 b=Path(sys.argv[1]).read_bytes();assert hashlib.sha256(b).hexdigest()=='1be5293390fbabf8b86b02805771d0fed82fddd2c61678b58d36c7bab9f93cd8';P=json.loads(b)['points'];n=(4,11,0);nn=sum(t*t for t in n);Y=[]
 for i,p in enumerate(P):
  d=sum(p[j]*n[j] for j in range(3));Y.append([nn*p[j]-(d*n[j] if i!=15 else 0) for j in range(3)])
 shift=[sum(p[j] for p in Y)//len(Y) for j in range(3)];Y=[[p[j]-shift[j] for j in range(3)] for p in Y];raw=make(Y);sys.path.insert(0,str(Path(sys.argv[2]).resolve()));import check_A,check_B,centred_mass
 A=check_A.run(raw);B=check_B.run(raw);assert A==B;M=centred_mass.run(A);out=Path(sys.argv[3]);out.mkdir(exist_ok=False)
 for f,o in [('POINTS.json',{'object':'COORD_C96_PLANAR24_PYRAMID_OWN211','points':sorted(Y)}),('raw.json',raw),('A.json',A),('B.json',B),('MASS.json',M)]:
  b=encoded(o);(out/f).write_bytes(b);print(f,len(b),hashlib.sha256(b).hexdigest(),flush=True)
 print('C138_PLANAR_BASE_AB_MASS_PASS',A['V'],A['E'],A['F'],A['counts'],A['weak'],flush=True);print('SHIFT',shift,'FACES',sorted(map(len,A['faces'])),'ROOTS',A['stable_face_ids'],A['unstable_vertices'],A['saddle_edges'],'BITS',M,flush=True)
if __name__=='__main__':main()
```

Executed `python -B -S planar25.py POINTS25.json core exact96`. Expected and observed terminal marker `C138_PLANAR_BASE_AB_MASS_PASS 25 48 25 [2,1,1] [0,0,0]`; translation shift=[-8135,2600,20971]. Reproduced POINTS.json582bytes,SHAb49d24fda9620582ca3a011efd07d45a6550aa4e748bdaca32e3f343de822742; raw.json951bytes,SHA9071c5c16df9d342e68a97c9720e73b8c52b1317c0531734f14d01a0783c2f43; A.json/B.json each4305bytes,SHAa6c33c9f089de95cbbe52ebe51ecb4351306575df32f2aced706f62774793093; MASS.json216bytes,SHA91636c316a2f18f8a79558431e5df4ae000430ff4d6480a692fabbcbcd95f06c.

Volume44086905700293. Own centre=(23694796297/3276041,-59026233271/13104164,-283800727279/13104164). Unique unstable raw-lex14=(8861,-2864,67120), stable maximal faces7,23; saddle edge(15,22), all in this new body's exact ordering. Third integration has46 positive tetrahedra; common centred denominator24bits, integer coordinate numerators<=41bits. These numbers do NOT describe the distinct C138 source.

The geometric reduction makes the limitation clearer: monounstability survives even exact24-facet planar coalescence, but the opposed stable pair survives too. A quantitative central disk/slab obstruction, rather than an unproved universal pyramid exclusion, is the useful next diagnostic.
