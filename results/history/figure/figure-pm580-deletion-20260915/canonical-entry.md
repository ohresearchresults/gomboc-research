
## 2026-09-15T17:00:59.656Z

## Recovery capsule: COORD_PM598_DEL_3_5_6_C580_OWN222 — finite deletion opens a healthier two-pair frontier

The exact combined PM598_RECOVER.py from16:48:11.005Z,3517bytes/SHAce93a45eda31171f603d17133a5c8de885cbdb24d5c5ef63b62195d3874c3276, has now completed its direct source-only cold execution. All parent/new A/B identities and the independent third-mass check matched, terminal marker PM598_EXACT_TWO_AUDITS_WHOLE_COMPLEX_AND_CENTRED_MASS_PASS. The previous entry's pending combined-driver check is therefore resolved.

**New exact finite nonwinner, now fully recoverable:** COORD_PM598_DEL_3_5_6_C580_OWN222 is the convex hull of all164 exact raw-lex vertices of COORD_C598_PROJECTIVE_METRIC_OWN334_G1E12 except indices3,5,6. Recalculate the actual uniform filled-volume centroid of that smaller hull; do not retain the PM598 centroid. It has V161/E290/F131,C580,own strict(S,U,H)=(2,2,2),additional weak-only000. It is NOT a Gömböc and does not replace accepted S8/C624. It leaves21 true-edge additions before E311, compared with12 for its parent, and removes one extra S/U/H pair from parent334.

The exact own equilibria are stable sorted-input facets94,99 (corresponding to parent supports104,114); unstable final raw-lex0,159 (parent raw0,162); saddles final true edges(2,89),(3,4) (parent edges(2,92),(4,7)). Every face-side, complete vertex-cone, and all four saddle primitives on every true edge have been tested independently, not inferred from Euler. Face, vertex and edge primitive-zero counters all vanish. Both complete independently implemented exact auditors reconstructed identical records. Third centred-integer integration used318 positive tetrahedra, returned all three first moments exactly zero, and agreed on volume.

The full minimal source below was cold-executed in a fresh directory. Its only inputs are the independently regenerated PM598 A.json504653bytes/SHAd01383b4720b9615d019f4a229429b97a57f16755998b305033b5ff3506b2752 and the three exact core modules already literal in FOUR_FRONTIERS_EXACT_CORE_20260915 (parts14:47:44.818Z/14:54:38.487Z/14:56:12.493Z). PM598 itself is completely recoverable by16:48:11.005Z and its canonical C598 parent15:33:50.633Z. These exact dependencies, the three deletion indices and all21 new supporting-facet triples below are the full new construction input. No Qhull, SciPy, hidden coordinates or originating sandbox is needed in exact recovery. The independent rebuilt vertex set is checked to equal precisely the161 retained parent vertices, certifying that these halfspaces give their convex hull rather than a larger circumscribed solid.

Save as PM580_RECOVER.py, UTF8/LF with one terminal newline,3036bytes/SHA281d5dbba9510c39e85159eb969e421d7b5a9b3f96486ae4a2748880ac832f4c:

```python
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from hashlib import sha256
import json,subprocess,sys
sys.set_int_max_str_digits(0)
assert __debug__
core=Path(sys.argv[1]).resolve()
parent=Path(sys.argv[2]).resolve()
out=Path(sys.argv[3]).resolve()
assert not out.exists()
out.mkdir(parents=True)
def digest(p):
 b=p.read_bytes()
 return len(b),sha256(b).hexdigest()
def dump(p,a):
 p.write_text(json.dumps(a,sort_keys=True,separators=(',',':')))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
assert digest(parent)==(504653,'d01383b4720b9615d019f4a229429b97a57f16755998b305033b5ff3506b2752')
P=json.loads(parent.read_text())
X=[tuple(map(F,r)) for r in P['raw_vertices']]
removed={3,5,6};keep=[i for i in range(len(X)) if i not in removed]
I=[]
for p in X:
 d=lcm(*(v.denominator for v in p));I.append(tuple(int(v*d) for v in p)+(d,))
rows={tuple(n)+(d,) for n,d,cy in zip(P['normals'],P['offsets'],P['faces']) if len(set(cy)-removed)>=3}
triples=[[4,23,26],[4,30,32],[4,26,30],[4,36,44],[4,32,36],[4,8,7],[4,16,19],[7,13,16],[4,19,20],[4,9,8],[4,11,10],[4,20,23],[1,11,4],[4,7,16],[7,12,13],[1,55,58],[4,49,50],[4,50,55],[1,58,65],[4,54,49],[1,4,55]]
for ids in triples:
 a,b,c=[I[i] for i in ids]
 u=tuple(b[i]*a[3]-a[i]*b[3] for i in range(3))
 v=tuple(c[i]*a[3]-a[i]*c[3] for i in range(3))
 n=cross(u,v);r=tuple(x*a[3] for x in n)+(dot(n,a[:3]),)
 g=gcd(*r);assert g
 r=tuple(x//g for x in r)
 if r[3]<0:r=tuple(-x for x in r)
 assert r[3]>0
 assert all(dot(r[:3],I[i][:3])<=r[3]*I[i][3] for i in keep)
 rows.add(r)
assert len(rows)==131
dump(out/'raw.json',{'H':sorted(rows)})
assert digest(out/'raw.json')==(40168,'5fa9c4c33a0a45df541edbfce74ec52d077ce47aca01c17f2ed2463ad8a9b57a')
for script,dst in [('check_A.py','A.json'),('check_B.py','B.json')]:
 subprocess.run([sys.executable,'-B','-S',str(core/script),str(out/'raw.json'),str(out/dst)],check=True)
assert digest(out/'A.json')==(499908,'e1913a7610265741039439577f3513073c36578a6646144595e1e0dfdbae273c')
assert (out/'A.json').read_bytes()==(out/'B.json').read_bytes()
A=json.loads((out/'A.json').read_text())
assert [A[k] for k in ('V','E','F')]==[161,290,131]
assert A['counts']==[2,2,2] and A['weak']==[0,0,0]
assert A['active_input_indices']==list(range(131))
assert A['stable_face_ids']==[94,99] and A['unstable_vertices']==[0,159]
assert A['saddle_edges']==[[2,89],[3,4]]
assert all(A[k]==0 for k in ['face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count'])
assert set(tuple(map(F,r)) for r in A['raw_vertices'])=={X[i] for i in keep}
sys.path.insert(0,str(core))
from centred_mass import run as mass
M=mass(A)
assert M['tetrahedra']==318 and M['filled_first_moments']==[0,0,0]
assert M['common_centred_denominator_bits']==91696
dump(out/'MASS.json',M)
assert digest(out/'MASS.json')==(223,'bde47f45a7b626e4cf98e2840165369515981bab97658f3c91e9c0b351338282')
print('PM580_EXACT_HULL_TWO_AUDITS_AND_CENTRED_MASS_PASS')
```

Reconstruction and verification: `python -B -S PM580_RECOVER.py CANONICAL_CORE RECONSTRUCTED_PM598_A_JSON NEW_OUTPUT`. Python3.13.5 standard library only, assertions enabled. Observed final marker PM580_EXACT_HULL_TWO_AUDITS_AND_CENTRED_MASS_PASS. Output raw.json40168bytes/SHA5fa9c4c33a0a45df541edbfce74ec52d077ce47aca01c17f2ed2463ad8a9b57a; A.json=B.json each499908bytes/SHAe1913a7610265741039439577f3513073c36578a6646144595e1e0dfdbae273c; MASS.json223bytes/SHAbde47f45a7b626e4cf98e2840165369515981bab97658f3c91e9c0b351338282. Both the original audit and this fresh source replay reproduced these bytes.

Arithmetic maximum numerator-or-denominator lengths: primitive supports596bits; raw vertices950; actual centroid91693; volume45878; raw first moments91779; common centred denominator91696 (parent92094). The arithmetic reduction is modest; the substantial change is nine fewer true edges and a simpler own-equilibrium census. The remaining C580 S–H and U–H pairs must still both be removed with actual mass.

Discovery used a complete64-case exact-supporting-complex/numerical-mechanics deletion screen on PM598: all subsets of size0..3 of raw indices[1,3,5,6,65,162,163]. The selected deletion[3,5,6] was then independently completely audited as above. Other screened rows are not silently promoted to full exact equilibrium results. The screen's full runnable source, fixed selectors, dependency hashes and all64 finite outcomes are still pending in the coordinator methods capsule; exact PM580 reconstruction itself is now fully canonical. The next useful search is this physically changed, less fragile own222 normal/contact complex, with21-edge headroom, rather than repeating the original near-singular healthy-guard cells.
