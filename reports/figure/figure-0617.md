# figure-0617

Historical AI scientific report · saved 2026-09-29 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Vivid Comet 47 — executed routes, a six-U corridor obstruction, and a genuine own-U1 escape

Branch: `[internal-source-reference]`.

## Result and acceptance boundary

**No own strict(1,1,0)/additionalweak(0,0,0) body was obtained.** The frozen two-route proposal has now actually been executed and completely classified. Its combined body is V/E/F = **72/210/140**, own strict **(18,45,61)**, additionalweak **(0,0,0)**, with **44 positive P bars and 17 positive Q bars**. At the old reference centroid it is instead (6,1,5), with five positive Q bars. Neither classification is close enough to be called a target construction.

The strongest new result is an **exact finite-family exclusion with unrestricted actual centroid**: every homogeneous convex polytope containing the old host and both specified cover anchors, and contained in the complete frozen BOTH24 hull, has **at least six strict unstable vertices**, at old material indices **2, 6, 8, 12, 29, 60**. This covers arbitrary intermediate hulls, deletions of route points, insertion of other points inside that hull, changed incidences, and any vertex/edge budget. It is not merely the classification of three sampled route bodies or a small-centroid-box argument.

A real escape was also constructed and exactly audited: **VC47_HOST_ESCAPE_G10**, V/E/F = **71/207/138**, own strict **(14,1,13)**, additionalweak **(0,0,0)**, P empty and thirteen positive Q bars. It retains the two original exact cover anchors and the original raw U12 point, but changes the host and extends outside the frozen upper hull. Thus actual U1 can be restored by a finite physical deformation; full Q cancellation remains unresolved. Two further exact low-vertex nonwinners are preserved below rather than being misreported as cancellation.

## Input authority and completed reading

I read the complete supplied journal consecutively through its EOF, 2,126 lines. The mounted bytes match the supplied 413,548-byte SHA-256 `de84c7ac8e774efa64030153ed586cfd325ebb5927aa6bb646f1d0c1304d8ab0`.

The supplied parent is `figure-0611`. Re-encoding its complete embedded Markdown in the compact UTF-8 object `{"version":2,"result_markdown":...}`, with `ensure_ascii=False`, produces 34,570 bytes and the required SHA-256 `18da4f98d5716341eaefaf4f5d208fe4e8ac6fe28fc2d11b0421272b5bcad5a8`. Its extracted standalone Python source is 19,123 bytes, SHA-256 `f4d38340f7843c0adfe4a7792d51b12d6f305ec5b6aeb7889c0e210483d9204a`. The parent explicitly left the new route bodies unaudited; this handoff replaces that execution uncertainty with observed exact results. fileciteturn9file0L368-L374

The legacy Python constants `PARENT_ID` and `PARENT_SHA` identify the earlier Xbvm data lineage. They were preserved when reproducing its output files; they are not a claim that Xbvm is this assignment's supplied parent. I found no conflicting point data, class, or incidence in the required parent. No absent historical workspace or archive was used.

## 1. Complete execution of the proposed finite routes

All following censuses use exact maximal facets and actual homogeneous volume centroids unless the reference-center column explicitly says otherwise. P and Q contain every strictly positive exact bar, without a numerical cutoff. Their depth convention is `(birth2-death2)/birth2`.

| Body | V/E/F | Own strict S/U/H | Additional weak | Number of P / Q bars | Strict S/U/H at old G |
|---|---:|---:|---:|---:|---:|
| WIDE host | 54/156/104 | 5/1/4 | 0/0/0 | 0 / 4 | 5/1/4 |
| LEFT8 | 60/174/116 | 13/38/49 | 0/0/0 | 37 / 12 | 5/1/4 |
| RIGHT16 | 66/192/128 | 12/36/46 | 0/0/0 | 35 / 11 | 6/1/5 |
| BOTH24 | 72/210/140 | 18/45/61 | 0/0/0 | 44 / 17 | 6/1/5 |

The own-centroid and volume calculations are global closed-hull integrals:

| Body | Volume | Own centroid minus old G |
|---|---:|---|
| LEFT8 | 8.048087990157077 | (-0.094838273241522, +0.068183401253335, +0.120633630682395) |
| RIGHT16 | 8.229290526610004 | (+0.009465460193131, -0.195821125113959, +0.021396852639437) |
| BOTH24 | 9.783058334836452 | (-0.070057105102240, -0.108628905264843, +0.117238490436559) |

The host volume is 6.494320181930631. BOTH24 adds 3.288738152905821, or approximately 50.6402% of that volume. The respective added first-moment vectors about G are approximately

```
LEFT8  (-0.76326677, +0.54874601, +0.97087007)
RIGHT16(+0.07789402, -1.61146893, +0.17608092)
BOTH24 (-0.68537275, -1.06272292, +1.14695099)
```

The RIGHT16 increment genuinely has negative projection on the original J normal: the unit-normal projections are approximately +1.150333992528075 for LEFT8 and -1.268542898954971 for RIGHT16. This is a measured whole-hull moment result, not an inference from the cover point's projection. However, both increments have positive z moment, and their vector sum is far from zero. Opposing one scalar moment does not solve the three-component physical mass problem.

For these particular frozen bodies, both the nonadditive volume `V(BOTH)-V(LEFT)-V(RIGHT)+V(host)` and the analogous three-component first moment are **exactly zero**. These are checked identities of separately integrated complete hulls. They do not justify independently summing caps for a different geometry, nor establish disjointness merely from those identities.

### Entire Q landscape, not just retired old planes

All five original stable supporting planes, including the old elder plane, are violated by BOTH24 and hence retired. Nevertheless, at old G its six stable material cycles are

```
(2,56,87), (13,68,52), (32,39,68),
(32,79,60), (37,52,68), (59,76,65).
```

The complete reference-center Q-depth lists, in descending order, are:

```
LEFT8:
0.3642616669962460, 0.2074352662665481,
0.0668910617711111, 0.00131687253792305

RIGHT16:
0.6258470538141327, 0.0531919805103500,
0.00463104888407889, 0.00407357981642416,
0.0000214815587514411

BOTH24:
0.4287344799346611, 0.2074352662665481,
0.0668910617711111, 0.00463104888407889,
0.0000214815587514411
```

The complete own-center Q-depth lists are:

```
LEFT8:
0.5597692116729446, 0.1922561318097709, 0.0582654343959660,
0.00338673867430565, 0.00209400164098993, 0.00140857615785084,
0.00113113082894450, 0.000924837123470728, 0.000738944577013417,
0.000728859317514047, 0.000124757265421310, 0.000118641464257655

RIGHT16:
0.6265663220341252, 0.1697877418315421, 0.0713196332618947,
0.00667910402777838, 0.00496864920228607, 0.00239936169403248,
0.00221931950595833, 0.00202416252927979, 0.00161357818012406,
0.00115033666547109, 0.0000000281932622142913

BOTH24:
0.5243284073897135, 0.2722161815332205, 0.0537711964458972,
0.0179444074018793, 0.0127992792977864, 0.00598321188138052,
0.00159685750209279, 0.00102515977500814, 0.00101480007044569,
0.000916124810825428, 0.000493139804816016, 0.000336259153039684,
0.000216905100689901, 0.000180209773413637, 0.0000708701037647276,
0.0000673443934844979, 0.0000628740467634437
```

At the parent's separating support level 1297/1000, its exact polar-component classifier finds respectively **39, 40, and 40** surviving new polar vertices in the old J component. Consequently no case removes that entire old component at the stated reference center and level. The replay emits every survivor's new facet, old-component carrier, and exact polar coordinates; it also emits all exact P/Q roots, birth/death values, death edges, actual stable cycles and unstable vertices. The numerical lists above are display approximations, not substitutes for those exact reports.

## 2. New theorem: the entire two-anchor route corridor forces six strict U

Use raw coordinates translated by the original exact G. Let

- `K- = conv(old 68 host rows, BOTH24 raw row 68, BOTH24 raw row 76)`;
- `K+ = conv(all 92 BOTH24 submitted rows)`.

Rows 68 and 76 are the actual G6-snapped cover anchors produced by the specified 8-link and 16-link generators. They are not substituted with unsnapped ideal anchors.

**Theorem.** Every homogeneous convex polytope B satisfying `K- subset B subset K+`, at its own actual centroid `c(B)`, has strict unstable vertices at old material indices `{2,6,8,12,29,60}`. In particular no such B is own110, regardless of E and regardless of additional weak equilibria elsewhere.

### Exact integral proof

For a common extreme vertex u and an incident true K+ edge vector d, set

```
f_d(x) = (u-x).d
T_d = integral(K-, f_d) + integral(K+ minus K-, max(f_d,0)).
```

Since B contains K- and is contained in K+,

```
V(B) * (u-c(B)).d = integral(B,f_d) <= T_d.
```

The positive-part integral is computed exactly by clipping each complete hull with the halfspace `d.x <= d.u`, integrating the clipped hull globally, and subtracting the two clipped integrals. Explicitly, a clipped hull with volume v and first moment m contributes `(d.u)*v-d.m`. No independently overlapping cap sums enter the calculation.

For all 35 incident K+ edge rays at the six named common vertices, the exact T_d is strictly negative. Every vector from u to a point of B lies in the cone generated by the incident K+ edge rays. Therefore `(u-c(B)).(x-u)<0` for every x in B other than u. Also u remains an extreme vertex because it belongs to K- and is extreme in K+. This proves strict instability for every intermediate homogeneous B, with no assumption that its centroid remains near G.

The following bounds are the largest, hence least favorable, values of `T_d/(V(K+)*||d||_1)` for each vertex. They upper-bound `(u-c(B)).d/||d||_1` uniformly over B and over every incident K+ edge at that vertex.

| Old material vertex | Incident rays checked | Worst uniform upper bound |
|---|---:|---:|
| 2 | 8 | -0.000300499655729897 |
| 6 | 5 | -0.002697399384912849 |
| 8 | 5 | -0.000647033669547038 |
| 12 | 4 | -0.10681739498127747 |
| 29 | 5 | -0.002809948249436164 |
| 60 | 8 | -0.002408535754975257 |

The common exact bound is strictly less than **-3/10000**. This is a signed projection per edge L1 length, not a dimensionless angular margin.

### Separate unavoidable centroid displacement

The same exact clipping calculation gives

```
Mz(B) >= Mz(K-) + Mz(K+ intersect {z<=0}) - Mz(K- intersect {z<=0})
      = Lz,

0.3379 < Lz < 0.3380,
0.034539 < Lz/V(K+) < 0.034540.
```

Thus in raw coordinates every B in this corridor satisfies

```
c(B)_z - G_z >= Lz/V(K+) = approximately 0.03453967424036848.
```

This is a capacity bound over **all** intermediate fillings, not a lower estimate on the added volume needed for a hypothesized controller. The six-U theorem is stronger than this centroid displacement consequence and does not depend on using the latter as a sufficient witness box.

The proof checks exact complete hulls, oriented manifold incidence, Euler identities, support inequalities, strict facet turns, positive centered tetrahedra, and zero centered first moments. The first moments are additionally checked using the component-wise divergence formula `sum(n_i*(a_i^2+b_i^2+c_i^2+a_i*b_i+a_i*c_i+b_i*c_i))/24`, where n is the triangle's unnormalized cross product. This is a second algebraic integration formula, not a claim of a second independent full equilibrium-verification implementation.

**Scope boundary:** the theorem does not exclude moving/deleting host geometry so that K- is no longer contained, changing either mandatory anchor, or adding geometry outside K+. It is not an exclusion of all finite outside-envelope routes, all E<=249 bodies, or the branch's overall objective. Six is a proved lower bound, not a claimed sharp minimum over the corridor.

## 3. Executed physical escape and preserved nonwinners

Before free coordinate motion I used the exact BOTH24 extreme index set to compact its 92 submitted rows to **72**. All subsequent point optimization therefore retained the unconditional V<=72, E<=210 bound, even when formerly redundant rows became extreme. The 92 original submitted rows were never freely moved under a 78-vertex bound.

A finite constrained least-squares deformation fixed old raw U12 and the two cover anchors, sought the actual global centroid at the old G, and preserved a positive primal witness forest. The numerical solver hit its iteration limit rather than proving an exact mass closure. Its frozen rational endpoint nevertheless passes the full own-centroid exact audit. The recovered raw-coordinate variant resets the three fixed points to their original exact G6 values, so their retention is exact, not approximate.

For **VC47_HOST_ESCAPE_G10**:

```
V/E/F                  = 71/207/138
own strict             = (14,1,13)
additional weak        = (0,0,0)
unique U               = compact 12 = old material 12
P                      = []
number of positive Q   = 13
volume                 = approximately 9.262327486758235
actual centroid - G    = approximately
                         (-5.504473566760e-9,
                          -4.183733205263e-9,
                          +2.161667836587e-9)
```

The exact body is not claimed to have centroid exactly G. Its census is evaluated at its own exact centroid.

Its full Q-depth list is approximately

```
0.5481935333915361, 0.2556492159960954, 0.0944310954236591,
0.0125903351081921, 0.00835778848422147, 0.00773098970151726,
0.00645814490644433, 0.00620443784241374, 0.00527556314087384,
0.00315215488167796, 0.00215675754918491, 0.000360399027046778,
0.000236152243180052.
```

There is no conflict with the corridor theorem: the replay proves **both** failed inclusions. New compact point 45 lies outside old upper facet `(56,65,83)` with signed support violation divided by the normal's L1 norm approximately **0.18873806809904473**. Old host point 21 lies outside new facet `(16,18,50)` with the same normalization approximately **0.3861901125814491**. The inequalities are stored as exact rationals. The only nonextreme input row of this 72-row escape is compact index 14.

Two further actual-U1 endpoints demonstrate the tradeoff in optimizing the whole Q spectrum:

| Exact frozen body | V/E/F | Own strict | Additional weak | P / Q counts | Largest Q depth | Sum of Q depths |
|---|---:|---:|---:|---:|---:|---:|
| VC47_FLOW_A_G10 | 58/168/112 | 31/1/30 | 0/0/0 | 0 / 30 | about 0.2012466573 | about 0.24354808393 |
| VC47_FLOW_C_G10 | 58/168/112 | 32/1/31 | 0/0/0 | 0 / 31 | about 0.2801239199 | about 0.28013651608 |

FLOW_A reduced summed Q depth but fragmented the landscape. FLOW_C used a regularized square-root penalty to emphasize smaller bars; those bars mostly shrank, but did not vanish, and the principal bar grew. Its smallest positive exact Q bar is approximately **7.05285125875e-12**; FLOW_A's is approximately **2.65686633415e-9**. A display threshold would conceal genuine equilibria. These are useful compact nonwinners, not record claims or near-110 acceptances.

The post-mass flow allowed all compact points to move, including the former anchors and root point. Although the surviving U label remains 12, the original anchor/root coordinates are only protected in HOST_ESCAPE, not in FLOW_A or FLOW_C. Exact hull reconstruction, rather than the floating optimizer's last facet labels, is authoritative after rounding.

The optional numerical producer uses NumPy 2.3.5, SciPy 1.17.0, PyTorch 2.10.0+cpu, Python 3.13.5, and one BLAS/OpenMP/Torch thread. SciPy's triangulated Qhull output is used only for nomination; exact maximal facets are reconstructed independently for every reported rational endpoint. citeturn156786view0

## 4. Most useful continuation

Do not continue compensating inside the frozen two-anchor corridor while retaining the old host: that entire mechanism now has a six-U exclusion, including arbitrary centroid movement. Change a hypothesis of that theorem explicitly and certify the change.

HOST_ESCAPE supplies one such finite change with the original anchors and U12 retained and actual U1 restored. Its remaining problem is the complete thirteen-bar Q landscape. Alternatively, exact compaction of FLOW_A's 72 rows to its reported 58 extremes permits **27 additional arbitrary material points** while preserving the universal V<=85, E<=249 budget. This compaction must occur before using that allowance; it is not permission to freely move 72 rows and then add 27.

A productive design test is to evaluate the new signed clipped-moment bounds before investing in another fixed-envelope route repair. When two inherited vertices already have uniformly negative bounds along every upper-hull incident ray, no intermediate homogeneous mass tuning can restore U1. For a genuinely escaped geometry, co-design actual first moments and all Q components rather than optimizing only the largest bar or retiring only the current stable planes. The present calculations establish neither feasibility nor infeasibility of that broader continuation.

## 5. Source-complete recovery and verification

The five complete source files below include all 68 original integer rows, the deterministic exact route generator, the exact hull/mass/equilibrium/bar verifier, the clipping certificate, and all three 72-row frozen integer endpoint tables. HOST_ESCAPE is reconstructed from the frozen mass endpoint by exact translation and exact reset of the three protected points. No journal, Library item, historical workspace, numerical optimizer, or download is required to recover and exactly verify the reported bodies and theorem.

Save each code block under its stated filename, as UTF-8 with one final LF. Run:

```sh
python -B -S replay47.py VC47_OUT
```

This source-only replay was actually run successfully. It reproduces eleven pre-existing scientific output hashes, tests a cube and a tetrahedron, verifies a clipped cube mass control, reconstructs both full primal and dual landscapes, and checks the six-U certificate. Expected terminal markers are:

```
VC47_FROZEN_OWN_U1_ENDPOINTS_FULL_Q_EXACT_PASS_NO_110
VC47_ENTIRE_TWO_ANCHOR_ROUTE_CORRIDOR_AT_LEAST_SIX_U_EXACT_PASS_NO_110 35
VC47_COLD_SOURCE_ONLY_REPLAY_PASS_NO_110 11
```

The exact replay uses Python's standard library only. All route parameters are fixed in the source: grid 10^6, rational square-root midpoint precision 60 decimal digits, 8 and 16 links, rational nearest ties-to-even rounding. Frozen endpoint denominator is 10^10. No numerical cutoff is used in its equilibrium or persistence classification.

To reproduce the floating discovery procedure rather than just recover the authoritative exact endpoints, use the additional complete numerical source files below, with the stated installed dependency versions:

```sh
cd VC47_OUT
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python ../num47.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python ../flow47.py MASS_CLOSED.json FLOW_A.json --iter 300 --bound 1 --power 1 --margin 0.00001 --smooth 0
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python ../flow47.py FLOW_A.json FLOW_C.json --iter 400 --bound 0.1 --power 0.5 --margin 0.000001 --smooth 0.0001
```

The mass producer uses 300 SLSQP iterations, coordinate bound 2, three fixed compact points and margin `min(initial_arrow/4,1e-5)`. The flow volume penalty coefficient is 0.01. No randomness is used. MASS_CLOSED and FLOW_A reached their iteration limits; FLOW_C returned numerical optimizer success, which is not equilibrium success. Optimizer replay can depend on platform arithmetic; the literal integer tables, not later rerun floating endpoints, are the exact recovery authority.

Critical output identities:

| Output | Bytes | SHA-256 |
|---|---:|---|
| BASE/BOTH24_AUDIT.json | 177016 | e37fc757aceea0289a83cc8864ced38090dda1751f75c78afffb71e801c80b4f |
| CORRIDOR/VC47_SIX_U_CORRIDOR_EXACT.json | 456461 | d003cbffee002a2dcc3388c8d992940f177ead8ee99b01fc54fa2c7cc982713e |
| FROZEN/VC47_HOST_ESCAPE_G10_INPUT.json | 5727 | 3a49283067b91dbb41ae3f6a935e1f3f003724b5fab7df54454aa9c614475388 |
| FROZEN/VC47_HOST_ESCAPE_G10_EXACT.json | 91167 | 1d5d517614164abff94bb18406d8498b6284b5045775e3c6ea8de0d9d6594f33 |
| FROZEN/VC47_FLOW_A_G10_EXACT.json | 92272 | 781a1a0f0e195cb5e3a3ef785b6ddb6a34eafce9b567fc5d31fdf0fa7436071c |
| FROZEN/VC47_FLOW_C_G10_EXACT.json | 92857 | 4d0ce915cb56e1110bbba8b82de299e14f305a92addffccbbbe8ae5a9e4cd5b2 |

The replay writes a full manifest and checks the required hashes itself. The supplementary ZIP contains the same sources, computed reports, original parent driver and floating checkpoints; it is not the sole recovery source: [VC47 supplementary research package](sandbox:/mnt/data/VC47_RESEARCH_HANDOFF.zip).

### exact47.py

12245 bytes; SHA-256 `14431f428ffce4d3c19bfae1671529790bd41a4d4bf06cdb2117a2e4edffa473`.

```python
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

PARENT_ID='figure-0606'
PARENT_SHA='0dbde902d3fce9629f0d04fa5d29e8f50ed87d714f0be3d33a34991516b29d7b'
DATA='''
-1728005 -198144 -173888
-1694189 -558162 244129
-1687198 -7865 -362063
-1629034 -739811 455722
-1602162 204300 -530997
-1485397 346751 -695416
-1333475 500663 -838060
-1274114 -1007271 881539
-1154309 644386 -951012
-965730 -1078882 1016294
-952762 767036 -1038105
-1730720 -380964 33917
-1515614 -901503 662365
-733989 866405 -1098527
-661145 -1136863 1126381
-503985 940270 -1132088
-352619 -1140381 1204304
-267920 979817 -1145790
-185162 598383 457601
-101204 2876 -927988
-77285 -427199 -390459
-42066 -1117361 1226213
-34354 1012813 -1115615
260685 -1065285 1197104
196593 989084 -1087428
1031774 -299411 -381475
1005621 663758 -550728
174797 808617 513900
379698 -12013 -911170
791000 -864881 1020878
409640 982653 -999202
538640 -960620 1145240
1156095 -500665 769325
1150339 -185930 -70384
609688 935264 -905713
712781 -186856 -752235
775512 -346187 -665102
777769 627648 546500
787450 876941 -784930
876864 508220 537941
926820 786294 -646327
960274 427197 508420
998619 -690385 908777
1020515 365924 487039
1095093 -250440 -247510
1050077 516178 -370797
1222932 -286585 602369
1231657 -152023 412633
-799717 -701890 190312
-891236 -132425 1201276
1014590 559119 -692273
871557 733983 -657638
384467 1270036 -249011
396997 1179939 -665941
684942 -627207 -356073
282889 689836 -1229114
87907 159953 -1308090
1096812 -740853 215454
1001544 813751 -227422
1051119 263466 -739151
1300669 -127621 376455
1012837 -127737 -720637
1317569 -91630 76039
497173 440025 -1223202
767849 -462148 -771276
594564 62515 -1188432
1146747 449609 -463716
1096797 80251 -682947
'''
P=[tuple(Q(int(x),10**6) for x in line.split())
   for line in DATA.strip().splitlines()]
assert len(P)==68
G=tuple(Q(x,155863684366335143424000000) for x in
        (-5933080209329642826130933,
          1445293601728142474263729,
          1749166017940004894056942))
V0=Q(101473752842666109,15625000000000000)
ZERO=(Q(0),Q(0),Q(0))
J=(6,49,27); B=(27,49,37); C=(31,37,49)
E=(1,11,64); D=(62,67,66)
LEFT=tuple(Q(x,1000) for x in (-235,1005,1148))
RIGHT=tuple(Q(x,1000) for x in (1370,0,-490))
GRID=10**6
SQRT_DIGITS=60

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(s,a): return tuple(s*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def total(rows):
    r=ZERO
    for x in rows: r=add(r,x)
    return r

def tris(faces):
    for f in faces:
        for k in range(1,len(f)-1):
            yield (f[0],f[k],f[k+1])

def edges(faces):
    owners={}; directions={}
    for k,f in enumerate(faces):
        for a,b in zip(f,f[1:]+f[:1]):
            key=tuple(sorted((a,b)))
            owners.setdefault(key,[]).append(k)
            directions.setdefault(key,[]).append((a,b))
    assert all(len(v)==2 for v in owners.values())
    assert all(v[0]==v[1][::-1] for v in directions.values())
    return owners

def cycle(indices,x,n):
    drop=max(range(3),key=lambda k:abs(n[k]))
    axes=[k for k in range(3) if k!=drop]
    projected={}
    for i in indices:
        t=(x[i][axes[0]],x[i][axes[1]])
        projected[t]=min(i,projected.get(t,i))
    order=sorted(projected)
    def turn(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[]; hi=[]
    for v in order:
        while len(lo)>1 and turn(lo[-2],lo[-1],v)<=0: lo.pop()
        lo.append(v)
    for v in reversed(order):
        while len(hi)>1 and turn(hi[-2],hi[-1],v)<=0: hi.pop()
        hi.append(v)
    f=[projected[v] for v in lo[:-1]+hi[:-1]]
    assert len(f)>=3
    if dot(cross(sub(x[f[1]],x[f[0]]),sub(x[f[2]],x[f[0]])),n)<0:
        f.reverse()
    k=f.index(min(f))
    return tuple(f[k:]+f[:k])

def normal(points,f):
    a,b,c=(points[i] for i in f[:3])
    return cross(sub(b,a),sub(c,a))

def hull(points):
    den=math.lcm(*(v.denominator for p in points for v in p))
    x=[tuple(int(v*den) for v in p) for p in points]
    planes={}
    for i,j,k in itertools.combinations(range(len(x)),3):
        n=cross(sub(x[j],x[i]),sub(x[k],x[i]))
        if n==(0,0,0): continue
        h=dot(n,x[i]); sign=0; zero=[]
        for t,v in enumerate(x):
            d=dot(n,v)-h
            if d:
                s=1 if d>0 else -1
                if sign and sign!=s: break
                sign=s
            else:
                zero.append(t)
        else:
            if sign:
                planes[tuple(zero)]=tuple(-v for v in n) if sign>0 else n
    faces=sorted(set(cycle(ids,x,n) for ids,n in planes.items()),
                 key=lambda f:tuple(sorted(f)))
    assert len(faces)>=4
    ef=edges(faces)
    used=sorted(set(i for f in faces for i in f))
    assert len(used)-len(ef)+len(faces)==2
    adjacency=[set() for _ in faces]
    for a,b in ef.values():
        adjacency[a].add(b); adjacency[b].add(a)
    reached={0}; queue=[0]
    while queue:
        for j in adjacency[queue.pop()]:
            if j not in reached: reached.add(j); queue.append(j)
    assert len(reached)==len(faces)
    for f in faces:
        n=normal(points,f); a=points[f[0]]
        assert n!=ZERO
        assert all(dot(n,sub(v,a))<=0 for v in points)
        assert all(dot(n,sub(points[i],a))==0 for i in f)
        for i,j,k in zip(f,f[1:]+f[:1],f[2:]+f[:2]):
            assert dot(n,cross(sub(points[j],points[i]),sub(points[k],points[j])))>0
    return faces

def mass(points,faces):
    v=Q(0); m=ZERO
    for f in tris(faces):
        a,b,c=(points[i] for i in f)
        d=det(a,b,c)
        v+=d/6
        m=add(m,mul(d/24,add(add(a,b),c)))
    return v,m

def level(a,b):
    d=sub(b,a); dd=dot(d,d)
    assert dd>0
    t=max(Q(0),min(Q(1),-dot(a,d)/dd))
    z=add(a,mul(t,d))
    return dot(z,z)

def bars(points,edge_list):
    r=[dot(p,p) for p in points]
    parent=list(range(len(points)))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]; i=parent[i]
        return i
    events=sorted(((level(points[a],points[b]),(a,b)) for a,b in edge_list),
                  key=lambda x:(-x[0],x[1]))
    out=[]
    for death,e in events:
        i,j=root(e[0]),root(e[1])
        if i==j: continue
        if r[i]<r[j] or (r[i]==r[j] and i>j): i,j=j,i
        if r[j]>death:
            out.append(dict(root=j,edge=e,birth2=r[j],death2=death,
                            depth=(r[j]-death)/r[j]))
        parent[j]=i
    return sorted(out,key=lambda b:(-b['depth'],b['root'],b['edge']))

def polar(points,faces,c):
    out=[]
    for f in faces:
        n=normal(points,f); h=dot(n,sub(points[f[0]],c))
        assert h>0
        out.append(mul(1/h,n))
    return out

def census(points,faces,c):
    ef=edges(faces); used=sorted(set(i for f in faces for i in f))
    z=[sub(p,c) for p in points]
    normals=[normal(points,f) for f in faces]
    poles=polar(points,faces,c)
    S=[]; U=[]; H=[]; wS=[]; wU=[]; wH=[]
    for k,f in enumerate(faces):
        guards=[dot(normals[k],cross(z[i],z[j]))
                for i,j in zip(f,f[1:]+f[:1])]
        if min(guards)>0: S.append(k)
        elif min(guards)==0: wS.append(k)
    for i in used:
        s=max(dot(z[i],sub(z[j],z[i])) for j in used if j!=i)
        if s<0: U.append(i)
        elif s==0: wU.append(i)
    for e,inc in sorted(ef.items()):
        a,b=(z[i] for i in e); d=sub(b,a)
        t=-dot(a,d)/dot(d,d)
        if not 0<=t<=1: continue
        r=add(a,mul(t,d)); n,m=(normals[i] for i in inc)
        A,B,C=dot(n,n),dot(n,m),dot(m,m)
        den=A*C-B*B
        assert den>0
        alpha=(C*dot(n,r)-B*dot(m,r))/den
        beta=(A*dot(m,r)-B*dot(n,r))/den
        assert add(mul(alpha,n),mul(beta,m))==r
        if alpha<0 or beta<0: continue
        if 0<t<1 and alpha>0 and beta>0: H.append(e)
        else: wH.append(e)
    dual=sorted(set(tuple(sorted(v)) for v in ef.values()))
    Pbars,Qbars=bars(z,sorted(ef)),bars(poles,dual)
    strict=[len(S),len(U),len(H)]; weak=[len(wS),len(wU),len(wH)]
    if weak==[0,0,0]:
        assert strict[0]+strict[1]-strict[2]==2
        assert len(Pbars)==len(U)-1 and len(Qbars)==len(S)-1
    return dict(strict=strict,weak=weak,S=S,U=U,H=H,
                weakS=wS,weakU=wU,weakH=wH,
                stable_material_cycles=[faces[i] for i in S],
                P=Pbars,Q=Qbars,poles=poles,dual_edges=dual,
                active_material_indices=used,edges=sorted(ef))

def audit(points,faces=None):
    if faces is None: faces=hull(points)
    v,m=mass(points,faces)
    assert v>0
    c=mul(1/v,m)
    out=census(points,faces,c)
    z=[sub(p,c) for p in points]
    vv,mm=mass(z,faces)
    assert vv==v and mm==ZERO
    assert all(det(*(z[i] for i in f))>0 for f in tris(faces))
    out.update(V=len(out['active_material_indices']),E=len(out['edges']),
               F=len(faces),material_points=len(points),facets=faces,
               volume=v,first_moment=m,centroid=c)
    return out

def components(poles,edge_list,support_level):
    threshold=1/(support_level*support_level)
    alive={i for i,p in enumerate(poles) if dot(p,p)>threshold}
    parent=list(range(len(poles)))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]; i=parent[i]
        return i
    for a,b in edge_list:
        if a in alive and b in alive and level(poles[a],poles[b])>threshold:
            i,j=root(a),root(b)
            parent[max(i,j)]=min(i,j)
    return {i:root(i) for i in alive}

def sqrt_mid(x):
    assert x>=0
    if x==0: return Q(0)
    den=10**SQRT_DIGITS
    k=math.isqrt(x.numerator*den*den//x.denominator)
    assert Q(k*k,den*den)<=x<Q((k+1)*(k+1),den*den)
    return Q(2*k+1,2*den)

def unit(x): return mul(1/sqrt_mid(dot(x,x)),x)
def snap(x): return tuple(Q(round(v*GRID),GRID) for v in x)

def route(start,u,depth):
    directions=[unit(start),unit(u)]
    for _ in range(depth):
        new=[]
        for a,b in zip(directions,directions[1:]):
            new.extend((a,unit(add(a,b))))
        new.append(directions[-1]); directions=new
    n=2**depth
    r0=sqrt_mid(dot(start,start)); r1=sqrt_mid(dot(u,u))
    growth=r1/r0
    for _ in range(depth): growth=sqrt_mid(growth)
    out=[]; radius=r0
    for j in range(n):
        out.append(start if j==0 else snap(mul(radius,directions[j])))
        radius*=growth
    full=out+[u]
    assert all(dot(a,sub(b,a))>0 for a,b in zip(full,full[1:]))
    return out



def hole_test(old,parent,new,new_faces):
    c=parent['centroid']; z=[sub(p,c) for p in old]
    oldq=parent['poles']; s=Q(1297,1000); threshold=1/(s*s)
    comp=components(oldq,parent['dual_edges'],s)
    index={frozenset(f):i for i,f in enumerate(parent['facets'])}
    root=comp[index[frozenset(J)]]
    old_used=parent['active_material_indices']
    newq=polar(new,new_faces,c); holes=[]
    for k,q in enumerate(newq):
        if dot(q,q)<=threshold: continue
        i=max(old_used,key=lambda i:(dot(z[i],q),-i))
        support=dot(z[i],q)
        assert 0<support<=1
        owners=[j for j,f in enumerate(parent['facets']) if i in f]
        j=max(owners,key=lambda j:(dot(q,oldq[j]),-j))
        assert dot(q,oldq[j])>=dot(q,q)/support
        assert j in comp
        if comp[j]==root:
            holes.append(dict(new_facet=k,new_material_cycle=new_faces[k],
                              old_face_corner=j,old_physical_owner=i,
                              new_polar_vertex=q))
    return dict(reference_center=c,support_level=s,
                surviving_vertices_in_old_junior_component=holes,
                whole_old_component_removed_at_reference_center=(not holes),
                scope='Reference-center angular coverage; own census is separate')

def encode(x):
    if isinstance(x,Q): return str(x)
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [encode(v) for v in x]
    return x
```

### corridor47.py

6836 bytes; SHA-256 `5d5187a462c9b8bab978772b284ba6180ea4a187d619c7b6db4e288071e2130e`.

```python
"""Exact finite-envelope uniform-mass obstruction, VC47. Standard library only.
"""
import json,hashlib,sys
from pathlib import Path
import exact47 as E
Q=E.Q
ZERO=E.ZERO

def flux_moment(points,faces):
    m=[Q(0),Q(0),Q(0)]
    for t in E.tris(faces):
        a,b,c=(points[i] for i in t);n=E.cross(E.sub(b,a),E.sub(c,a))
        for k in range(3):
            A,B,C=a[k],b[k],c[k]
            m[k]+=n[k]*(A*A+B*B+C*C+A*B+A*C+B*C)/24
    return tuple(m)

def check_surface(points,faces):
    owners=E.edges(faces);used=sorted({i for f in faces for i in f})
    assert len(used)-len(owners)+len(faces)==2
    adj=[set() for f in faces]
    for a,b in owners.values():adj[a].add(b);adj[b].add(a)
    seen={0};todo=[0]
    while todo:
        for j in adj[todo.pop()]:
            if j not in seen:seen.add(j);todo.append(j)
    assert len(seen)==len(faces)
    for f in faces:
        n=E.normal(points,f);p=points[f[0]]
        assert n!=ZERO
        assert all(E.dot(n,E.sub(x,p))<=0 for x in points)
        assert all(E.dot(n,E.sub(points[i],p))==0 for i in f)
        for i,j,k in zip(f,f[1:]+f[:1],f[2:]+f[:2]):
            assert E.dot(n,E.cross(E.sub(points[j],points[i]),E.sub(points[k],points[j])))>0
    vol,mom=E.mass(points,faces);assert vol>0
    assert flux_moment(points,faces)==mom
    c=E.mul(1/vol,mom);z=[E.sub(p,c) for p in points]
    assert E.mass(z,faces)==(vol,ZERO)
    assert all(E.det(*(z[i] for i in t))>0 for t in E.tris(faces))
    return vol,mom

def clip(points,faces,n,h=Q(0)):
    """Intersect the represented convex hull with n.x <= h, exactly."""
    vals=[E.dot(n,p)-h for p in points]
    used={i for f in faces for i in f}
    if all(vals[i]<=0 for i in used):return points,faces,*E.mass(points,faces)
    if all(vals[i]>=0 for i in used):return [],[],Q(0),ZERO
    new=[];index={}
    def put(x):
        if x not in index:index[x]=len(new);new.append(x)
        return index[x]
    fs=[]
    for f in faces:
        poly=[]
        for i,j in zip(f,f[1:]+f[:1]):
            if vals[i]<=0:poly.append(put(points[i]))
            if vals[i]*vals[j]<0:
                x=E.add(points[i],E.mul(vals[i]/(vals[i]-vals[j]),E.sub(points[j],points[i])))
                assert E.dot(n,x)==h
                poly.append(put(x))
        if len(set(poly))>=3:
            fn=E.normal(points,f)
            # On a proper clipped facet, polygon vertices are non-collinear.
            if any(E.cross(E.sub(new[b],new[poly[0]]),E.sub(new[c],new[poly[0]]))!=ZERO for b in poly[1:] for c in poly[1:]):
                fs.append(E.cycle(poly,new,fn))
    cap=[i for i,p in enumerate(new) if E.dot(n,p)==h]
    assert len(cap)>=3
    fs.append(E.cycle(cap,new,n))
    fs=sorted(set(fs),key=lambda f:tuple(sorted(f)))
    assert all(E.dot(n,p)<=h for p in new)
    # Every new point lies in every original closed halfspace.
    assert all(E.dot(E.normal(points,f),E.sub(p,points[f[0]]))<=0 for f in faces for p in new)
    vol,mom=check_surface(new,fs)
    return new,fs,vol,mom

def make_inputs():
    u=E.sub(E.P[12],E.G);left=E.route(E.LEFT,u,3);right=E.route(E.RIGHT,u,4)
    raw=list(E.P)+[E.snap(E.add(E.G,p)) for p in left+right]
    hi=[E.sub(p,E.G) for p in raw]
    lo=[hi[i] for i in list(range(68))+[68,76]]
    return raw,lo,hi

def certify(outdir='CORRIDOR_EXACT'):
    out=Path(outdir);out.mkdir(exist_ok=True);raw,lo,hi=make_inputs();fl=E.hull(lo);fh=E.hull(hi)
    vl,ml=check_surface(lo,fl);vh,mh=check_surface(hi,fh)
    assert all(E.dot(E.normal(hi,f),E.sub(p,hi[f[0]]))<=0 for f in fh for p in lo)
    def half(x,f,n,h):
        pts,fc,v,m=clip(x,f,n,h)
        return dict(V=len({i for a in fc for i in a}),E=len(E.edges(fc)) if fc else 0,F=len(fc),volume=v,moment=m)
    zaxis=(Q(0),Q(0),Q(1));ln=half(lo,fl,zaxis,Q(0));hn=half(hi,fh,zaxis,Q(0))
    lower_z=ml[2]+hn['moment'][2]-ln['moment'][2]
    lower_center_z=lower_z/vh
    assert Q(3379,10000)<lower_z<Q(3380,10000)
    assert Q(34539,10**6)<lower_center_z<Q(34540,10**6)
    # Each common H-vertex remains an extreme point of every intermediate convex L.
    roots=[2,6,8,12,29,60]
    hu={i for f in fh for i in f};lu={lo[i] for f in fl for i in f}
    edge=E.edges(fh);records=[];allbounds=[]
    for i in roots:
        assert i in hu and hi[i] in lu
        neighbors=sorted({b if a==i else a for a,b in edge if a==i or b==i})
        guards=[];u=hi[i]
        for j in neighbors:
            d=E.sub(hi[j],u);off=E.dot(d,u)
            a=half(lo,fl,d,off);b=half(hi,fh,d,off)
            fixed=vl*off-E.dot(d,ml)
            positive_lo=off*a['volume']-E.dot(d,a['moment'])
            positive_hi=off*b['volume']-E.dot(d,b['moment'])
            assert positive_lo>=0 and positive_hi>=positive_lo
            upper=fixed+positive_hi-positive_lo
            assert upper<0
            norm1=sum(abs(t) for t in d)
            normalized=upper/(vh*norm1)
            assert normalized<0
            allbounds.append(normalized)
            guards.append(dict(neighbor=j,d=d,offset=off,low_clip=a,high_clip=b,
                               fixed_moment=fixed,added_positive_capacity=positive_hi-positive_lo,
                               upper_integral=upper,uniform_chord_per_edge_l1_upper=normalized))
        records.append(dict(vertex=i,raw_point=raw[i],neighbors=neighbors,guards=guards,worst=max(g['uniform_chord_per_edge_l1_upper'] for g in guards)))
        print('VC47_CORRIDOR_ROOT',i,len(neighbors),float(records[-1]['worst']),flush=True)
    worst=max(allbounds)
    assert worst<Q(-3,10000)
    report=dict(parent_assignment='figure-0611',parent_payload_sha256='18da4f98d5716341eaefaf4f5d208fe4e8ac6fe28fc2d11b0421272b5bcad5a8',
                original_center=E.G,lower_material_indices=list(range(68))+[68,76],upper_material_indices=list(range(92)),
                lower_facets=fl,upper_facets=fh,lower_volume=vl,lower_moment=ml,upper_volume=vh,upper_moment=mh,
                lower_negative_z=ln,upper_negative_z=hn,all_intermediate_z_moment_lower=lower_z,all_intermediate_center_z_lower=lower_center_z,
                six_uniform_unstable_vertices=roots,root_records=records,worst_uniform_chord_bound=worst,
                scope='Every homogeneous convex polytope B with conv(host,LEFT_anchor,RIGHT_anchor) subset B subset frozen BOTH24; unrestricted actual centroid, topology and point/facet count. Not arbitrary host motion or extension outside BOTH24.')
    data=(json.dumps(E.encode(report),sort_keys=True,indent=2)+'\n').encode();path=out/'VC47_SIX_U_CORRIDOR_EXACT.json';path.write_bytes(data)
    print(path.name,len(data),hashlib.sha256(data).hexdigest(),flush=True)
    print('VC47_ENTIRE_TWO_ANCHOR_ROUTE_CORRIDOR_AT_LEAST_SIX_U_EXACT_PASS_NO_110',len(allbounds),flush=True)
    return report

if __name__=='__main__':certify(sys.argv[1] if len(sys.argv)>1 else 'CORRIDOR_EXACT')
```

### replay47.py

16659 bytes; SHA-256 `9dc6b94533febd64db4825705290b90223bc2f4a269f00f9e98336af831141e3`.

```python
"""Frozen endpoints plus original route replay. Python 3.13.5, standard library."""
import sys,json,hashlib
from pathlib import Path
import exact47 as E
from corridor47 import certify,flux_moment,clip
Q=E.Q

VC47_MASS72_G10='''
-17442714265 22984194 -991893865
-17168392084 -4315563559 3210635918
-16870063695 1760345503 -3112772450
-16227740797 -6709497761 5023006159
-15907213735 3197871302 -5181453995
-14614816077 4321774173 -7145101540
-13088135414 5222876758 -8867620454
-12387940315 -10260020587 7447964351
-11312925868 6265137997 -10196723822
-9878857780 -12229167963 7541484291
-9365898184 7358003922 -11113946026
-17567395110 -2022750503 1152725226
-14775481719 -9107758053 6511425910
-7304524507 8372329314 -11676176897
-6861139105 -13915483770 7155559628
-5131373703 9077851593 -12069422919
-2799819643 -14806416494 6891276319
-2928909882 9586773229 -12198256435
1332726118 -14440902402 6857757508
-728835507 9688483608 -12248688656
4767245655 -13103834809 7021113166
1359911754 9462266966 -12191244537
9126373863 -9186266315 7639362814
3557002303 10200405535 -10765935639
7338603641 -11242462161 7302621320
11773245326 -4477143235 7248630592
6036579841 9632746926 -9796116125
8840143635 7571491479 5327907752
8127119419 9091397065 -8350904783
9825174533 5127164662 6976296724
9641888482 9108023792 -5811699171
11018157070 4969260000 5412229071
10561648755 -6991177104 7663763343
12176955792 2617913498 5212121842
12769996947 -3750228861 5394321407
9940591512 6336173289 -8282095477
3560423610 13237652181 -2989494778
3882086297 12194064791 -7227670920
2582575326 6642703702 -13357028180
751882201 1295335163 -13952086325
10646484110 8789743183 -2167185201
11877446616 1231655730 -7561979022
12724372549 -1036685871 5768912337
14328337230 -290237896 -395284511
5018583815 4343245760 -13187266157
8002983247 -7590376733 -9192369289
6674884615 1197470781 -12609182795
12944384744 3505412930 -4319504013
-2350001719 10050001947 11479995910
-4834922983 9513017016 11441452592
-7237005307 8456617888 11304762864
-9619690898 6759482199 11049028673
-11762305216 4352627058 10656082891
-13349462309 1335494224 10136604517
-14490294749 -1888075215 9058942030
-14954266115 -5795533647 7502476640
13699998281 1947 -4900004090
14181747376 -3228311382 -3553180370
13202381141 -5557400532 -5346099026
12223262383 -8210501709 -5006185500
11753499085 -9971144213 -3265673417
10422847150 -11832002795 -2373151200
8775574379 -13468441537 -1449199538
6866720386 -14820619931 -441723111
4784673707 -15820333673 733496337
2894045181 -16312860151 2443848384
708061974 -16467206114 4002439506
-1716265790 -16247283849 5336263631
-4260891264 -15642610969 6358986892
-6755649960 -14699286458 7007933164
-9626497528 -13215502934 7352783880
-12294613841 -11360811246 7193205081
'''

VC47_FLOW_A_G10='''
-16575201919 3059339961 -6800873434
-17478618980 1133734828 -1994948468
-15837839556 3617547035 -8724389947
-17392951880 -255483128 507749155
-14877285236 3995142214 -10614823194
-13706308940 4485443189 -12276778385
-12355012721 5058308447 -13706900336
-10955352739 -7986408857 6877160695
-10851914717 5665982177 -14911009369
-8264261454 -9705842718 6557795697
-9219465469 6261749159 -15900986585
-17168147837 2257816228 -4516736183
-16114085948 -4344938443 6532127066
-1679647933 11111837602 -1677373210
-5574893973 -11311315776 8278107471
-7475789098 6808247119 -16687152993
-2306002885 -13047011697 5849915993
-5649236396 7405368978 -17194975954
1269616726 -14084125328 5632717764
-3723065141 7751360450 -17604031750
5177202356 -12876969896 7254835545
-1750293897 7988186046 -17808458969
9753135815 -9667995617 6792231607
412602583 9883203950 -16300441315
7677932474 -10840248647 7568792143
12469432913 -5314156404 6214958272
3477045590 9608212868 -15849669842
4607515333 10452349065 -390105482
6946637131 9452248765 -13922368631
8182870421 3209727162 4013488653
7616380435 11034135677 -10665762500
5946652988 1331868390 2596474854
11589357655 -8111502781 5927481771
5266622356 5789450452 4043684095
13943688922 -3450133501 4454445688
6340138502 6351810494 -16375314478
1077154222 10442239853 47307645
633594405 12860712374 -9445184773
-197031084 4678010507 -19039861799
-2088783367 -712072267 -18649704954
8048468139 11768605654 -6626029678
8441141289 537293560 -4987132815
10210107522 1499121578 5169574747
14801958267 -3651587826 96515487
3522910292 1277301436 -18787358804
7539571143 -14136254119 -5976357675
8382204919 3596007950 -13302918288
8356450104 1603877645 -1955361199
459623268 5213006473 6126417964
43869989 2502274480 7428112610
-2796635663 4546861839 6665118859
-4778542095 7761680712 1126522546
-6443887448 2081077413 5889599834
-9487372106 1480438818 4760377170
-11154876543 -1901032328 5333443797
-14043123733 -5704610864 6447309368
12159279890 -4035050816 -8155755120
15254718219 -4814428218 -3383334992
14095629508 -8879519445 -4532309001
11205183000 -12475204873 -4963248815
13409950899 -10307564516 -1713570717
11486662053 -12683795362 -1011722010
9805888045 -13835801064 591565532
8018548401 -14553991037 2188761251
6127204321 -14893559143 3746045494
4181361575 -14835158330 5283591194
2197351470 -14394434947 6754827459
-101556779 -14027532416 7563329894
-2488732551 -13438447696 8087671733
-4941276449 -12625649562 8298237107
-7391677619 -11385781466 8375862323
-10180296444 -9392055244 8270658409
'''

VC47_FLOW_C_G10='''
-16795831193 3241748119 -6280675763
-17589421368 1120899856 -1426306154
-16082452212 3846083416 -8285571474
-17432598872 -355578520 1048230313
-15121676511 4267779253 -10275255810
-13953145644 4692900514 -12051814860
-12580473673 5237654946 -13575250494
-10955352739 -7986408857 6877160695
-11040339622 5835379743 -14853574269
-8030813879 -9557620002 6778796488
-9359671411 6429859321 -15900818363
-17337923204 2353309388 -3979665006
-16059605100 -4400773450 6624322175
-2019198761 10986881486 -1707026386
-5574893973 -11311315776 8278107471
-7559172160 6975426535 -16730591565
-2210565067 -12796856244 5911347968
-5657293009 7302673345 -17429959264
1269616726 -14084125328 5632717764
-3662490031 7686235575 -17829632932
5261427280 -13010318668 7273379898
-1619203018 7952759516 -18011586291
9903650957 -9782355235 6758010164
567310323 9851463600 -16501393394
7833429094 -10914451210 7578227818
12693739273 -5516989886 6070434710
3730136890 9331117139 -16170580764
4396723724 10829253693 -1388884372
6974735823 9453977271 -14139536046
8182870421 3209727162 4013488653
7312584831 11223422496 -10987529377
5946652988 1331868390 2596474854
11749731006 -8260632330 5847177894
5560873468 5275623430 3888891415
13948507073 -3556008577 4790690052
6809798679 6366795608 -16341119613
899817897 10668358476 -632698418
578799079 12874440723 -9309348612
79181586 4897050040 -19174652879
-2160233346 -88955735 -18919741238
7419953569 12213937111 -7019898537
8441141289 537293560 -4987132815
10153657679 1329042259 4975825420
15014136969 -3886591508 699941469
3838881089 1707035088 -18909559419
7616997296 -14301630771 -5647833092
8382204919 3596007950 -13302918288
8356450104 1603877645 -1955361199
352634267 4961307471 6020183133
-29515302 2340562323 7376757964
-2437207512 4342930735 6659772460
-4672139629 7853508090 1060366451
-6443887448 2081077413 5889599834
-9487372106 1480438818 4760377170
-11154876543 -1901032328 5333443797
-14047748348 -5711181100 6443796281
12981969683 -4082459857 -7416489916
15378847196 -4373522895 -3075614058
14286444991 -8823687467 -4363992877
11512453369 -12509556336 -4591129460
13793597778 -9901600406 -1380383631
11778499612 -12578013401 -757611426
10024417003 -13819761519 790420967
8175416729 -14593235220 2347384333
6220202776 -14977257670 3868058178
4207233424 -14954566499 5371047941
2160727079 -14536959943 6814191221
-198338437 -14154055419 7635564759
-2641965058 -13530469571 8171766124
-5146419692 -12658167771 8399066182
-7647398628 -11348182574 8476866048
-10454567875 -9295642134 8340202829
'''

def raw_json(data):
    return (json.dumps(E.encode(data),sort_keys=True,indent=2)+'\n').encode()

def global_zeros(rep,points):
    z=[E.sub(points[i],rep['centroid']) for i in rep['active_material_indices']]
    return [sum(E.dot(a,E.sub(b,a))==0 for i,a in enumerate(v) for j,b in enumerate(v) if i!=j) for v in (z,rep['poles'])]

def main(outdir='VC47_OUT'):
    out=Path(outdir);out.mkdir(parents=True,exist_ok=True);manifest={}
    def save(name,obj):
        path=out/name;path.parent.mkdir(parents=True,exist_ok=True)
        data=raw_json(obj);path.write_bytes(data)
        manifest[name]=dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    def checked(points):
        rep=E.audit(points)
        assert flux_moment(points,rep['facets'])==rep['first_moment']
        return rep
    cube=[tuple(Q(t) for t in p) for p in E.itertools.product((0,1),repeat=3)]
    tet=[E.ZERO,(Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(1))]
    for x,vef,suh,v,c in [(cube,[8,12,6],[6,8,12],Q(1),(Q(1,2),)*3),
                           (tet,[4,6,4],[4,4,6],Q(1,6),(Q(1,4),)*3)]:
        a=checked(x)
        assert [a[k] for k in ('V','E','F')]==vef and a['strict']==suh and a['weak']==[0,0,0]
        assert a['volume']==v and a['centroid']==c
    centered_cube=[E.sub(x,(Q(1,2),)*3) for x in cube]
    pts,ff,v,m=clip(centered_cube,E.hull(centered_cube),(Q(0),Q(0),Q(1)))
    assert v==Q(1,2) and m==(Q(0),Q(0),Q(-1,8))
    parent=checked(E.P)
    assert [parent[k] for k in ('V','E','F')]==[54,156,104]
    assert parent['strict']==[5,1,4] and parent['weak']==[0,0,0]
    assert parent['centroid']==E.G and parent['volume']==E.V0
    save('BASE/PARENT_EXACT.json',parent)
    u=E.sub(E.P[12],E.G);left=E.route(E.LEFT,u,3);right=E.route(E.RIGHT,u,4)
    reports={};inputs={}
    expected={'LEFT8':([60,174,116],[13,38,49],[5,1,4],39),
              'RIGHT16':([66,192,128],[12,36,46],[6,1,5],40),
              'BOTH24':([72,210,140],[18,45,61],[6,1,5],40)}
    for name,groups in [('LEFT8',[left]),('RIGHT16',[right]),('BOTH24',[left,right])]:
        points=list(E.P);paths=[]
        for group in groups:
            start=len(points);points.extend(E.snap(E.add(E.G,p)) for p in group)
            path=list(range(start,start+len(group)))+[12]
            scores=[E.dot(E.sub(points[a],E.G),E.sub(points[b],points[a])) for a,b in zip(path,path[1:])]
            assert min(scores)>0
            paths.append(dict(indices=path,scores=scores))
        report=checked(points);ref=E.census(points,report['facets'],E.G)
        coverage=E.hole_test(E.P,parent,points,report['facets'])
        assert ref['U']==[12] and not ref['P'] and not ref['weakU']
        report.update(reference_census=ref,reference_routes=paths,reference_coverage=coverage,
                      relative_first_moment=E.sub(report['first_moment'],E.mul(report['volume'],E.G)))
        vef,suh,rsuh,holes=expected[name]
        assert [report[k] for k in ('V','E','F')]==vef
        assert report['strict']==suh and report['weak']==[0,0,0] and ref['strict']==rsuh
        assert len(coverage['surviving_vertices_in_old_junior_component'])==holes
        rows=[[int(v*E.GRID) for v in q] for q in points]
        save('BASE/'+name+'_INPUT.json',dict(denominator=E.GRID,vertices=rows,parent_assignment=E.PARENT_ID,parent_payload_sha256=E.PARENT_SHA))
        save('BASE/'+name+'_AUDIT.json',report)
        reports[name]=report;inputs[name]=points
    L,R,T=(reports[name] for name in ('LEFT8','RIGHT16','BOTH24'))
    dvol=T['volume']-L['volume'];dm=E.sub(T['first_moment'],L['first_moment'])
    assert T['volume']-L['volume']-R['volume']+E.V0==0
    assert E.add(E.sub(E.sub(T['first_moment'],L['first_moment']),R['first_moment']),parent['first_moment'])==E.ZERO
    save('BASE/GLOBAL_MASS_COMPARISON.json',dict(left_added_volume=L['volume']-E.V0,right_added_volume=R['volume']-E.V0,
        combined_added_volume=T['volume']-E.V0,right_after_left_volume=dvol,
        right_after_left_relative_moment=E.sub(dm,E.mul(dvol,E.G)),nonadditive_volume=Q(0),
        scope='Differences of complete convex-hull integrals, not independently summed caps'))
    both=inputs['BOTH24'];keep=T['active_material_indices'];assert len(keep)==72
    lo=[both[i] for i in list(range(68))+[68,76]]
    save('ANCHOR2_EXACT.json',checked(lo))
    for f in (E.E,E.J,E.B,E.C,E.D):
        n=E.normal(E.P,f)
        assert max(E.dot(n,E.sub(p,E.P[f[0]])) for p in both)>0
    tables={'VC47_MASS72_G10':VC47_MASS72_G10,'VC47_FLOW_A_G10':VC47_FLOW_A_G10,'VC47_FLOW_C_G10':VC47_FLOW_C_G10}
    target={'VC47_MASS72_G10':([71,207,138],[14,1,13]),'VC47_FLOW_A_G10':([58,168,112],[31,1,30]),'VC47_FLOW_C_G10':([58,168,112],[32,1,31])}
    frozen={}
    for name,text in tables.items():
        rows=[list(map(int,line.split())) for line in text.strip().splitlines()];assert len(rows)==72
        points=[tuple(Q(t,10**10) for t in row) for row in rows];frozen[name]=points
        rep=checked(points);rep['global_directed_chord_zero_counts']=global_zeros(rep,points)
        vef,suh=target[name]
        assert [rep[k] for k in ('V','E','F')]==vef and rep['strict']==suh
        assert rep['weak']==[0,0,0] and rep['U']==[12] and not rep['P']
        assert rep['global_directed_chord_zero_counts']==[0,0]
        save('FROZEN/'+name+'_INPUT.json',dict(denominator=10**10,vertices=rows))
        save('FROZEN/'+name+'_EXACT.json',rep)
    shift=tuple(Q(round(v*10**10),10**10) for v in E.G)
    points=[E.add(p,shift) for p in frozen['VC47_MASS72_G10']]
    for old in (12,68,76):points[keep.index(old)]=both[old]
    rep=checked(points)
    assert [rep[k] for k in ('V','E','F')]==[71,207,138]
    assert rep['strict']==[14,1,13] and rep['weak']==[0,0,0] and rep['U']==[12] and not rep['P']
    assert global_zeros(rep,points)==[0,0]
    rep['old_raw_ids']=keep;rep['fixed_raw_material_ids']=[12,68,76]
    rep['centroid_drift_from_G']=E.sub(rep['centroid'],E.G)
    assert max(abs(v) for v in rep['centroid_drift_from_G'])<Q(1,10**8)
    outside=[];missing=[]
    for f in T['facets']:
        n=E.normal(both,f);h=E.dot(n,both[f[0]])
        for i,p in enumerate(points):
            value=E.dot(n,p)-h
            if value>0:outside.append((value/sum(abs(v) for v in n),i,f))
    for f in rep['facets']:
        n=E.normal(points,f);h=E.dot(n,points[f[0]])
        for i,p in enumerate(E.P):
            value=E.dot(n,p)-h
            if value>0:missing.append((value/sum(abs(v) for v in n),i,f))
    rep['outside_upper_witness']=max(outside);rep['missing_old_host_witness']=max(missing)
    assert rep['outside_upper_witness'][0]>Q(18,100) and rep['missing_old_host_witness'][0]>Q(38,100)
    rows=[[int(v*10**10) for v in p] for p in points]
    save('FROZEN/VC47_HOST_ESCAPE_G10_INPUT.json',dict(denominator=10**10,vertices=rows,
        construction='Translate VC47_MASS72_G10 by ties-even rounded G at grid1e10; reset compact rows corresponding to raw12,68,76 to original BOTH24 G6 exact values.',material_map=keep))
    save('FROZEN/VC47_HOST_ESCAPE_G10_EXACT.json',rep)
    print('VC47_FROZEN_OWN_U1_ENDPOINTS_FULL_Q_EXACT_PASS_NO_110',flush=True)
    certify(out/'CORRIDOR')
    p=out/'CORRIDOR'/'VC47_SIX_U_CORRIDOR_EXACT.json';b=p.read_bytes()
    manifest[str(p.relative_to(out))]=dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
    for name,sha in REQUIRED_HASHES.items():
        assert manifest[name]['sha256']==sha,(name,manifest[name])
    save('MANIFEST.json',manifest)
    print('VC47_COLD_SOURCE_ONLY_REPLAY_PASS_NO_110',len(REQUIRED_HASHES),flush=True)

REQUIRED_HASHES={
  "BASE/BOTH24_AUDIT.json": "e37fc757aceea0289a83cc8864ced38090dda1751f75c78afffb71e801c80b4f",
  "BASE/GLOBAL_MASS_COMPARISON.json": "36e25ac3eb7f9dfcf112365c9919af8abcf8d77a8c3bec532f40a9a4dd95fcf0",
  "BASE/LEFT8_AUDIT.json": "9c2e0702e92fd607e68cf7984feb3cac92af27d302a08ece26cb47fbcca36178",
  "BASE/PARENT_EXACT.json": "6c372ae6aea4997e603f19c7cd06a1e5489c1fbb3d758220c0772ec3eb327a36",
  "BASE/RIGHT16_AUDIT.json": "5567efb10b3760b232cdd8e744bed02042bb7023e5c60a7e1995b72163bfd954",
  "CORRIDOR/VC47_SIX_U_CORRIDOR_EXACT.json": "d003cbffee002a2dcc3388c8d992940f177ead8ee99b01fc54fa2c7cc982713e",
  "FROZEN/VC47_FLOW_A_G10_EXACT.json": "781a1a0f0e195cb5e3a3ef785b6ddb6a34eafce9b567fc5d31fdf0fa7436071c",
  "FROZEN/VC47_FLOW_C_G10_EXACT.json": "4d0ce915cb56e1110bbba8b82de299e14f305a92addffccbbbe8ae5a9e4cd5b2",
  "FROZEN/VC47_HOST_ESCAPE_G10_EXACT.json": "1d5d517614164abff94bb18406d8498b6284b5045775e3c6ea8de0d9d6594f33",
  "FROZEN/VC47_HOST_ESCAPE_G10_INPUT.json": "3a49283067b91dbb41ae3f6a935e1f3f003724b5fab7df54454aa9c614475388",
  "FROZEN/VC47_MASS72_G10_EXACT.json": "d1c40c759bdae74c6bb689560f5e776a17b46ec858761fc5178af88e8159e986"
}
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'VC47_OUT')
```

### num47.py

6552 bytes; SHA-256 `0453e56e55bec35a2c58049985adebf869fbc86aeb25da7676fe2018cc546294`.

```python
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import json,sys,math
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
import torch
torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)

def geometry(x):
    h=ConvexHull(x)
    f=h.simplices.copy()
    cr=np.cross(x[f[:,1]]-x[f[:,0]],x[f[:,2]]-x[f[:,0]])
    rev=np.einsum('ij,ij->i',cr,h.equations[:,:3])<0
    f[rev]=f[rev][:,[0,2,1]]
    # Deterministic material cycles and facet ordering; all selected runs are simplicial.
    f=np.array([np.roll(a,-int(np.argmin(a))) for a in f])
    f=np.array(sorted(f.tolist(),key=lambda a:tuple(sorted(a))))
    own={}
    for k,fa in enumerate(f):
        for i,j in zip(fa,np.roll(fa,-1)):
            own.setdefault(tuple(sorted((int(i),int(j)))),[]).append(k)
    assert all(len(v)==2 for v in own.values())
    e=np.array(sorted(own));du=np.array([own[tuple(a)] for a in e])
    used=np.unique(f)
    a,b,c=x[f[:,0]],x[f[:,1]],x[f[:,2]]
    det=np.einsum('ij,ij->i',a,np.cross(b,c))
    vol=det.sum()/6;cent=(det[:,None]*(a+b+c)).sum(0)/(24*vol)
    p=x-cent
    n=np.cross(b-a,c-a);q=n/np.einsum('ij,ij->i',n,a-cent)[:,None]
    return dict(f=f,e=e,du=du,used=used,vol=vol,g=cent,p=p,q=q)

def persistence(x,e,floor=1e-14):
    r=np.einsum('ij,ij->i',x,x)
    d=x[e[:,1]]-x[e[:,0]];den=np.einsum('ij,ij->i',d,d)
    t=np.clip(-np.einsum('ij,ij->i',x[e[:,0]],d)/np.maximum(den,1e-300),0,1)
    z=x[e[:,0]]+t[:,None]*d;levels=np.einsum('ij,ij->i',z,z)
    levels=np.minimum(levels,np.minimum(r[e[:,0]],r[e[:,1]]))
    par=list(range(len(x)))
    def root(i):
        while par[i]!=i:par[i]=par[par[i]];i=par[i]
        return i
    out=[]
    for k in sorted(range(len(e)),key=lambda k:(-levels[k],tuple(e[k]))):
        i,j=(root(int(v)) for v in e[k])
        if i==j:continue
        if (r[i],-i)<(r[j],-j):i,j=j,i
        dep=(r[j]-levels[k])/r[j]
        if dep>floor:out.append(dict(root=j,edge=e[k].tolist(),birth2=r[j],death2=levels[k],depth=dep))
        par[j]=i
    return sorted(out,key=lambda d:(-d['depth'],d['root'],d['edge']))

def arrow_matrix(x):
    d=x[None,:,:]-x[:,None,:]
    den=np.linalg.norm(x,axis=1)[:,None]*np.linalg.norm(d,axis=2)
    a=np.einsum('ik,ijk->ij',x,d)/np.maximum(den,1e-100)
    np.fill_diagonal(a,-np.inf)
    return a

def info(x,center=None):
    d=geometry(x);p=d['p'] if center is None else x-center
    if center is not None:
        f=d['f'];a,b,c=x[f[:,0]],x[f[:,1]],x[f[:,2]]
        n=np.cross(b-a,c-a);q=n/np.einsum('ij,ij->i',n,a-center)[:,None]
    else:q=d['q']
    pa=arrow_matrix(p);qa=arrow_matrix(q)
    U=[int(i) for i in d['used'] if max(pa[i,d['used']])<-1e-10]
    S=np.where(qa.max(1)<-1e-10)[0].tolist()
    P=persistence(p,d['e']);Q=persistence(q,d['du'])
    return dict(V=len(d['used']),E=len(d['e']),F=len(d['f']),S=S,U=U,vol=d['vol'],g=d['g'].tolist(),P=P,Q=Q,
                minU=float(np.min(np.delete(pa[:,d['used']].max(1),np.argmax(np.linalg.norm(p,axis=1))))),
                stable_cycles=d['f'][S].tolist())

def t_mass(x,f):
    a,b,c=x[f[:,0]],x[f[:,1]],x[f[:,2]]
    det=torch.sum(a*torch.linalg.cross(b,c),dim=1);vol=det.sum()/6
    cent=(det[:,None]*(a+b+c)).sum(0)/(24*vol)
    return vol,cent

def t_ang(a,b):
    d=b-a
    return (a*d).sum(-1)/(torch.linalg.vector_norm(a,dim=-1)*torch.linalg.vector_norm(d,dim=-1)).clamp_min(1e-30)

def dump(path,data):
    def enc(x):
        if isinstance(x,np.ndarray):return x.tolist()
        if isinstance(x,np.generic):return x.item()
        if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
        if isinstance(x,(tuple,list)):return [enc(v) for v in x]
        return x
    Path(path).write_text(json.dumps(enc(data),sort_keys=True,indent=2)+'\n')

class MassClose:
    def __init__(self,x,fix,margin=1e-5):
        self.x=x.copy();self.fix=fix;self.free=np.array([i for i in range(len(x)) if i not in fix]);self.root=int(np.argmax(np.linalg.norm(x,axis=1)))
        ar=arrow_matrix(x);self.sons=np.array([i for i in range(len(x)) if i!=self.root]);self.parents=ar[self.sons].argmax(1)
        vals=ar[self.sons,self.parents];assert min(vals)>0
        self.margin=np.minimum(vals*.25,margin);self.last=None;self.calls=0
    def unpack(self,z):
        x=self.x.copy();x[self.free]=z.reshape(-1,3);return x
    def calc(self,z):
        if self.last is not None and np.array_equal(z,self.last):return self.out
        self.last=z.copy();x=self.unpack(z);f=geometry(x)['f'];free=self.free
        base=torch.tensor(self.x)
        def con(zz):
            tx=base.index_copy(0,torch.tensor(free),zz.reshape(-1,3))
            vol,g=t_mass(tx,f)
            ar=t_ang(tx[self.sons],tx[self.parents])-torch.tensor(self.margin)
            return torch.cat((g,ar))
        zz=torch.tensor(z,requires_grad=True)
        val=con(zz).detach().numpy();jac=torch.autograd.functional.jacobian(con,zz,vectorize=True).detach().numpy()
        self.out=val,jac;self.calls+=1;return self.out
    def solve(self,maxiter=300,bound=2):
        z0=self.x[self.free].ravel()
        def fun(z):return ((z-z0)**2).sum()/2,z-z0
        res=minimize(fun,z0,jac=True,method='SLSQP',bounds=[(z-bound,z+bound) for z in z0],
                     constraints=[dict(type='eq',fun=lambda z:self.calc(z)[0][:3],jac=lambda z:self.calc(z)[1][:3]),
                                  dict(type='ineq',fun=lambda z:self.calc(z)[0][3:],jac=lambda z:self.calc(z)[1][3:])],
                     options=dict(maxiter=maxiter,ftol=1e-12,disp=True))
        return self.unpack(res.x),dict(success=bool(res.success),message=res.message,nit=int(res.nit),fun=float(res.fun),calls=self.calls,
                                       constraint=self.calc(res.x)[0].tolist(),parents=self.parents.tolist(),sons=self.sons.tolist(),margin=self.margin.tolist(),free=self.free.tolist())

if __name__=='__main__':
    from fractions import Fraction as Q
    r=json.load(open('BASE/BOTH24_INPUT.json'));a=json.load(open('BASE/BOTH24_AUDIT.json'));g=np.array([float(Q(v)) for v in json.load(open('BASE/PARENT_EXACT.json'))['centroid']])
    keep=a['active_material_indices'];x=np.array(r['vertices'],float)[keep]/r['denominator']-g
    fix=[keep.index(i) for i in [12,68,76]]
    print('before',info(x),flush=True)
    model=MassClose(x,fix)
    y,res=model.solve(maxiter=300,bound=2)
    print('after',info(y),flush=True)
    dump('MASS_CLOSED.json',dict(x=y,info=info(y),solver=res,material_map=keep,initial_center=g,fix=fix))
```

### flow47.py

3633 bytes; SHA-256 `260e191a82b10d66f545d2a936fba784658d86c59f2ba152efd3111960e7323e`.

```python
from num47 import *

class Flow:
    def __init__(self,x,power=1.0,margin=1e-5,volweight=.01,smooth=0):
        self.shape=x.shape;self.smooth=smooth;self.power=power;self.margin=margin;self.vol0=geometry(x)['vol'];self.volweight=volweight;self.last=None;self.calls=0;self.history=[];self.best=None
    def calc(self,z):
        if self.last is not None and np.array_equal(z,self.last):return self.out
        self.last=z.copy();x=z.reshape(self.shape);geo=geometry(x);f=geo['f'];q=geo['q'];p=geo['p']
        ar=arrow_matrix(p);root=int(np.argmax(np.linalg.norm(p,axis=1)));sons=np.array([i for i in range(len(x)) if i!=root]);pars=ar[sons].argmax(1)
        bar=persistence(q,geo['du'],floor=1e-16)
        idx=np.array([b['root'] for b in bar],int);ee=np.array([b['edge'] for b in bar],int).reshape(-1,2)
        def quantities(zz):
            tx=zz.reshape(self.shape);vol,g=t_mass(tx,f);pp=tx-g
            a,b,c=tx[f[:,0]],tx[f[:,1]],tx[f[:,2]];n=torch.linalg.cross(b-a,c-a)
            qq=n/torch.sum(n*(a-g),dim=1)[:,None]
            if len(idx):
                d=qq[ee[:,1]]-qq[ee[:,0]];t=(-torch.sum(qq[ee[:,0]]*d,dim=1)/torch.sum(d*d,dim=1)).clamp(0,1)
                dead=qq[ee[:,0]]+t[:,None]*d;birth=torch.sum(qq[idx]**2,dim=1)
                dep=(1-torch.sum(dead**2,dim=1)/birth).clamp_min(1e-24)
                loss=((dep+self.smooth).pow(self.power)-self.smooth**self.power).sum()
            else:loss=tx.sum()*0
            loss=loss+self.volweight*torch.log(vol/self.vol0)**2
            guards=t_ang(pp[sons],pp[pars])-self.margin
            return torch.cat((loss.reshape(1),guards))
        tz=torch.tensor(z,requires_grad=True);val=quantities(tz).detach().numpy();jac=torch.autograd.functional.jacobian(quantities,tz,vectorize=True).detach().numpy()
        self.out=val,jac;self.calls+=1
        if min(val[1:])>=-1e-8 and (self.best is None or val[0]<self.best[0]):
            self.best=(val[0],x.copy(),self.calls);self.history.append([self.calls,val[0],len(bar),float(min(val[1:])),geo['vol'],geo['g'].tolist()])
        return self.out
    def solve(self,x,maxiter=200,bound=.5):
        z0=x.ravel()
        def cb(z):
            if self.calls%25==0: print('progress',self.calls,self.calc(z)[0][0],min(self.calc(z)[0][1:]),flush=True)
        res=minimize(lambda z:self.calc(z)[0][0],z0,jac=lambda z:self.calc(z)[1][0],method='SLSQP',
             constraints=[dict(type='ineq',fun=lambda z:self.calc(z)[0][1:],jac=lambda z:self.calc(z)[1][1:])],
             bounds=[(float(v-bound),float(v+bound)) for v in z0],callback=cb,
             options=dict(maxiter=maxiter,ftol=1e-11,disp=True))
        y=res.x.reshape(self.shape)
        chosen=self.best[1] if self.best is not None else y
        return chosen,dict(success=bool(res.success),message=res.message,nit=int(res.nit),fun=float(res.fun),calls=self.calls,history=self.history,
                          last_x=y,last_info=info(y),best_calls=self.best[2] if self.best else None)

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');ap.add_argument('--power',type=float,default=1.0);ap.add_argument('--smooth',type=float,default=0);ap.add_argument('--margin',type=float,default=1e-5);ap.add_argument('--iter',type=int,default=200);ap.add_argument('--bound',type=float,default=.5);args=ap.parse_args()
    inp=json.load(open(args.input));x=np.array(inp['x']);fl=Flow(x,args.power,args.margin,smooth=args.smooth)
    y,rs=fl.solve(x,args.iter,args.bound);r=info(y);print('FINAL',r,flush=True)
    dump(args.output,dict(x=y,info=r,solver=rs,settings=vars(args)))
```

## Final boundary

No new own110 result or E<=249 target acceptance is asserted. The durable successors are the exact six-U corridor exclusion, the finite own-U1 host escape, and the fully classified low-vertex nonwinners above. No scheduler or journal operation was performed.
