# material-87f50fb4a73c

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J101 — exact C468 own211 and protected-degree cut budgets

## Result and exact identity
J99_R82_PRUNED6_C468 is exactly V154/E234/F82, C468, own strict(S,U,H)=(2,1,1), additionalweak000, zero directed primal/polar chord equalities, P=[], and one positive Q in(116009428126328,116009428126329)/10^15. It is NOT own110 and does not replace accepted C622. It is a six-deletion prefix of the coordinator's actual-mass J99 pruning, distinct from the25-deletion C464 body and from unchanged R82. Source lineage is fully read immutable result figure-0581, SHA f4d4df1390c5e9bd18047aad823f3cd12e8c85751a66dbfc62ae50f67c779461.

The deleted exact original-H triples are [40,42,46], [13,79,81], [57,79,81], [18,26,29], [36,41,45], [38,72,73]. Numerical original indices were44,19,18,36,81,92. The complete exact generator in [internal-source-reference] starts from the already preserved C464 input checkpoint and restores the19 intervening vertices, reproducing all154 retained triples and all82 maximal oriented facets with the exact original input hash. This recovery choice does not identify the two different bodies.

F82 is a preserved COUNT, not an unchanged set of facet planes. Exactly77 original supporting planes remain as facets; old supports26,41,42,72,81 disappear and five new triangular facets replace them. The first five supplied face cycles are those new facets. Future cuts or projectivities must use the reconstructed C468 face lattice, not blindly reuse the original82 H-rows as its entire boundary.

Exact own volume lies in(1712648555677736,1712648555677737)/10^15. Centroid coordinates lie in(24957417581923,24957417581924), (3217640348240,3217640348241), (-6770910157456,-6770910157455), all /10^15. Maximum centroid denominator length15516bits. In the supplied new face ordering, S25 is a6-gon on oldH7 and S69 a21-gon on oldH18. Unique U is localvertex15; unique H localedge4--83. These local labels are not the parent's canonical auditor vertex labels.

The unchanged exact99 audit with GMP exact rationals verified supporting inequalities, complete maximal coplanar faces, strict polygon convexity, a closed oriented connected face lattice, positive tetrahedral uniform mass, the actual own-centred polar, all strict/additionalweak S/U/H and every positive P/Q without a cutoff. A second tetrahedral sum about the computed centroid gives the same volume and exactly zero first moments. This is the coordinator's exact computation, not an independent worker audit or a second physics implementation. Two Fraction-backend runs hit execution timeouts before completion; the same audit completed with GMP. No completed C468 Fraction audit is claimed.

## Protected-degree theorem
For a convex3D polyhedron P, define D(P)=sum_v(degree(v)-3). Handshake and Euler give D=2E-3V=3F-6-E. Valid invertible affine/projective maps with positive projective denominators preserve the face lattice and D.

Select old vertices T with d_T=sum_T(degree(v)-3). Intersect P, or its valid projective image, with k new physical halfspaces, EACH STRICTLY CONTAINING EVERY protected vertex. Assume the intersection remains full dimensional. A sufficiently small neighborhood of each protected vertex is unchanged, so its degree survives. Every other surviving or new vertex has degree at least3; therefore D(new)>=d_T. Convex intersection cannot split one facet into several facets, so F(new)<=F(P)+k. Consequently

E(new)<=3(F(P)+k)-6-d_T.

In particular, protecting ALL old nonsimple vertices gives E(new)<=E(P)+3k. Removed old facets only improve the bound. This is a conditional combinatorial guarantee, NOT a mass or equilibrium certificate. Preserving an unstable vertex geometrically does not preserve its instability after the own centroid moves. Final actual filled-intersection mass and all strict/weak equilibria must still be recomputed.

C468 has148 degree3 vertices and exactly SIX degree4 vertices. Their new local indices and exact original-H triples are12:[57,79,80],15:[13,33,79],36:[29,36,45],37:[18,29,45],40:[40,46,67],87:[38,73,74]. Thus D=6. Protecting all six strictly against all new planes permits FIVE cuts with E<=234+15=249. Protecting any three permits FOUR cuts, because3(82+4)-6-3=249. Three cuts remain within the unconditional facet-count bound. Its unique current U is one of the six protected vertices; this does not establish ownU1 after cutting.

For the separate exact C464 body, degrees93x3,31x4,6x5,4x6,1x7 give D59 and42 nonsimple vertices. Protecting all42 permits five cuts with E<=232+15=247. More generally, five cuts require protected surplus at least57 under this bound. This is a CONDITIONAL five-cut route on F99, not the unconditional three-cut guarantee that F99 lacks. Six cuts with all surplus protected give only E<=250 unless additional facet loss or surplus gain is proved. No such six-cut construction is claimed.

C468 is a useful Pareto alternative: slightly larger E and Q than C464, but only six protection constraints for five cutting-plane controls. It supplies two more possible cuts than the unpruned R82's unconditional three-cut budget. This is not cancellation of its surviving Q. The next constructive question is finite whole-basin surgery satisfying those geometric protection inequalities while allowing actual mass and critical carriers to change.

## Complete recovery dependency set and commands
The new capsule consists of [internal-source-reference] (complete source-only generator) AND this audit/theorem material, together with two unchanged complete native source dependencies:

1. [internal-source-reference], J99_EXACT_PRUNED_C464.md,15613B/SHA2917d67d175739a0e6aa086a3734c4a184153bf44ccf99bb95bbd96ceb8fa46b: extract KH93_C434_R82_G6.txt, J99_PRUNED25_INPUT.json and exact99.py from its complete FILE fences.
2. [internal-source-reference], J98_EXACT_GEOMETRY_CORE.md,24401B/SHAebbf64fe9441d3a320e8f673941436f186af46f8f5b25464c1ebc78a9c5e42fa: extract its complete gmpq98.py FILE unit. This core was fully read and the extracted unit hash checked before use.

Save the entire plaintext of [internal-source-reference] unchanged as reconstruct6_99.py, and extract the two FILE fences below beside all dependencies. Preserve one final newline in each source. Observed exact environment: CPython3.13.5 and GMP6.3.0, through public mpq ctypes operations; no numerical fallback, gmpy2 or flint package. Run:

```sh
python -B -S reconstruct6_99.py
python -B -S gmpq98.py
python -B -S fast_exact99.py J99_PRUNED6_INPUT.json
python -B -S degree_reserve99.py
```

Expected terminal markers:
J101_EXACT_C468_INPUT_RECONSTRUCTION_PASS 3959 cb5150c5ace22ab9350b0cebc72f22088bcaa0533e3495d02f4cc954916b1939
GMPQ98_EXACT_ADAPTER_TEST_PASS
J99_EXACT_VERTEX_SUBSET_AUDIT_PASS J99_R82_PRUNED6_C468 154 234 82 [2, 1, 1] [0, 0, 0] [0, 0]
J99_EXACT_DEGREE_RESERVE_PASS J99_R82_PRUNED6_C468 154 234 82 6 6 249
J99_EXACT_DEGREE_RESERVE_PASS J99_R82_PRUNED25_C464 135 232 99 59 42 247

All these computations completed. The adapter self-test compares100 seeded rational operations with Fraction; it is not independent physics certification. The degree checker assumes the separately audited facet lattices, while the theorem above supplies the conditional cut implication.

Input/source manifest:
KH93_C434_R82_G6.txt1888B SHA9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7.
J99_PRUNED25_INPUT.json3684B SHAd67d882bfee515e445afdccda95668c259b83b1ae2d14af1f760899a56b4f36c.
exact99.py6606B SHA62590494bd5c9e01368ce20336f2eb8c93b9dac8f0e7a9c0ea5f7da300e7d135.
gmpq98.py4537B SHA3e72f475aa26e26526e2ecb4f752e17c090daa294c2da9498502ca6793e2b3f8.
reconstruct6_99.py3105B SHAcad0b83d1b3093b6ce8c21eb3ef2a4c649e55f99453238e1780f20f9e3122105.
fast_exact99.py464B SHA5c34155ff84e64870454a9110e2cc6f0ca504a9e9b7b6e8d80472371d1ac5be3.
degree_reserve99.py1595B SHAa61514d0e98c806a63bda31adb891d0ac0744a56362b59073d1597a4a191bdfe.

Reproduced outputs:
J99_PRUNED6_INPUT.json3959B SHAcb5150c5ace22ab9350b0cebc72f22088bcaa0533e3495d02f4cc954916b1939.
J99_PRUNED6_INPUT_EXACT.json90092B SHA81bfd039bffdf5159d542d8d29bf7ca8f60a1070fdbc3d5026c311c671522058, containing full exact mass fractions and every positive bar.
J99_DEGREE_RESERVES.json7554B SHAfa2d24d1b9d55b39e1a16cb402ef25b74ba560c8f9ce873652b86cb64e98b4ee, containing every protected vertex for both bodies.

The optional original numerical nomination used the complete geom99.py already preserved in [internal-source-reference], NumPy2.3.5/SciPy1.17.0, OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. Its entire producing invocation was the following. It is not required for exact recovery, and Qhull ordering portability is not assumed:

```python
from pathlib import Path
import json
from geom99 import load,hull
base=load()
deleted=[44,19,18,36,81,92]
ids=[i for i in range(len(base['v'])) if i not in deleted]
b=hull(base['v'][ids])
spec=dict(identity='J99_R82_PRUNED6_C468',retained_incident_supports=[base['incident'][i] for i in ids],retained_original_indices=ids,faces=b['faces'])
Path('J99_PRUNED6_INPUT.json').write_text(json.dumps(spec,separators=(',',':'))+'\n')
```

## FILE fast_exact99.py
```python
"""Exact GMP backend for the unchanged exact99 audit; no numerical fallback."""
from pathlib import Path
import hashlib,sys
import exact99
from gmpq98 import Q
for n,h in [('exact99.py','62590494bd5c9e01368ce20336f2eb8c93b9dac8f0e7a9c0ea5f7da300e7d135'),('gmpq98.py','3e72f475aa26e26526e2ecb4f752e17c090daa294c2da9498502ca6793e2b3f8')]:
    assert hashlib.sha256(Path(__file__).with_name(n).read_bytes()).hexdigest()==h
exact99.F=Q
exact99.main(Path(sys.argv[1]))
```

## FILE degree_reserve99.py
```python
"""Exact combinatorial degree reserves; geometric/equilibrium audit is separate."""
from pathlib import Path
from collections import Counter
import hashlib,json
root=Path(__file__).parent
inputs=[('J99_PRUNED6_INPUT.json','cb5150c5ace22ab9350b0cebc72f22088bcaa0533e3495d02f4cc954916b1939',(154,234,82,6)),
        ('J99_PRUNED25_INPUT.json','d67d882bfee515e445afdccda95668c259b83b1ae2d14af1f760899a56b4f36c',(135,232,99,59))]
records=[]
for name,sha,expected in inputs:
    raw=(root/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
    s=json.loads(raw);edges=set()
    for f in s['faces']:
        for a,b in zip(f,f[1:]+f[:1]):edges.add(tuple(sorted((a,b))))
    degree=Counter(v for e in edges for v in e)
    V=len(s['retained_incident_supports']);E=len(edges);F=len(s['faces'])
    assert len(degree)==V and min(degree.values())>=3 and V-E+F==2
    D=sum(d-3 for d in degree.values());assert D==3*F-6-E
    assert (V,E,F,D)==expected
    protected=[dict(vertex=i,degree=d,incident_old_supports=s['retained_incident_supports'][i])for i,d in sorted(degree.items())if d>3]
    records.append(dict(identity=s['identity'],V=V,E=E,F=F,degree_surplus=D,degree_histogram=dict(sorted(Counter(degree.values()).items())),
                        protected_vertices=protected,five_cut_E_bound_if_all_protected=E+15))
    print('J99_EXACT_DEGREE_RESERVE_PASS',s['identity'],V,E,F,D,len(protected),E+15)
text=json.dumps(records,indent=2)+'\n';dest=root/'J99_DEGREE_RESERVES.json';dest.write_text(text)
print('OUTPUT',dest.name,len(text.encode()),hashlib.sha256(text.encode()).hexdigest())
```
