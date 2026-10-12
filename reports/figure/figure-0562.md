# figure-0562

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# FINAL76_G6 and H60_G6: both complete affine orbits exclude own110

## Outcome

**Both requested affine-orbit questions are closed by an executed, computer-assisted exact joint-metric obstruction.** For each literal physical body K in {FINAL76_G6,H60_G6}, and every nonsingular real affine map x↦Ax+b,

```text
S(AK+b) ≥ 2  OR  U(AK+b) ≥ 2,
```

at its own homogeneous volume centroid. The forced equilibria are **strict**. Thus neither orbit contains strict own110, even before imposing additionalweak000.

This is a joint S/U theorem, **not** a claim that every image has two unstable equilibria. It permits root turnover and covers arbitrary conditioning and disconnected metric regions. Its scope is these two exact G6 geometries—not their G8 roundings, projective images or support-moved descendants. The old INNER26 theorem is not an input to either new certificate.

Four new rational affine controls are retained, all under budget and additionalweak000/primitivezero000. Two have own121 and certified finite full-P descent intervals; the improvements are genuine but small. The other two use the simple determinant-one shear x↦x+y/500 and demonstrate proliferation of genuine small bars. Together the four controls have eight complete landscapes and **97 positive bars:32 P and65 Q**. No own110 construction is claimed.

## 1. Reading, inputs and source authority

The complete supplied journal, changed branch memory, both literal parent payloads and all97 files of the new interface source dictionary were read through EOF before substantive research. The journal actually matched492929 bytes and SHA-256 `48a0c0b6282521fd1a049ac1f7e3c5812383cfd8a77fb5691ecca01e45b93d71`.

The required immutable parents are `figure-0557`, supplied SHA-256 `4aa61caf7b0b2162e0f47154bc734ddad2dfc19578ff3c8504807864c1f75061`, and `figure-0558`, supplied SHA-256 `591c9bf0e892e454c2566a0257b301f874eb9874eaad8f4e9ae7f177e71cf156`. These are supplied outer-result identities; no unsupported outer-serialization hash verification is claimed.

The new parent's embedded `RECOVER_INTERFACE60.py` was independently checked:111080 bytes, SHA-256 `e3f9f12a9846722af605af00f7ef71722ca2ed3b81b2b989514303062fc8dfdc`. Its execution produced

```text
INTERFACE60_SOURCE_RECOVERY_PASS 97 306027 bab9e272fd592d81b9f26bf3290e7347e012a7a96c04615da3452d190951badb
```

The exact inputs used here are

```text
FINAL76_G6.json:2170 bytes
999919df48ea5fef75728a09403d9b59f2993ccfdc5c8f94679a69fd694040ae

H60_G6.json:1736 bytes
50f33c0acf09712bebc2196326164fe5ace75939fcbfeba9e050ec15b12ad4cc
```

Both specify **uniformly filled physical intersections n_i·x≤1000000**, with76 and60 literal integer normal rows. They are not uniformly filled polar hulls. FINAL76's stable hexagon is detached from U10/31 and its current defect is P49/cut41; H60 has U6/26 and P36/cut32, with its stable octagon containing the elder. These identities, not old26-root labels, govern the work.

Each complete true graph and actual mass is reconstructed from those halfspaces. FINAL76 has148 primal vertices,76 dual vertices and222 edges in each graph:444 directed arcs per graph. H60 has116 primal vertices,60 dual vertices and174 edges:348 directed arcs per graph. No old144-arc bank or old root refutation was reused. There is no unavailable continuation-critical dependency: the inline recovery includes both literal inputs and every required helper.

## 2. Global compatibility theorem

### A cut barrier forces two strict equilibria

For M positive definite, write f(x)=xᵀMx. Partition a polyhedron's vertices into C and its complement. Suppose a∈C and b∉C, and choose a fixed point z_e on **every** true edge crossing the partition, such that

```text
max_e f(z_e) < min(f(a),f(b)).
```

Choose v maximizing f among vertices of C. An incident edge v→w staying in C satisfies

```text
vᵀM(w−v) = [f(w)−f(v)−f(w−v)]/2 < 0.
```

On a crossing edge incident to v, its certified point has f(z_e)<f(v). Convexity of the edge quadratic forces its initial derivative at v to be strictly negative. Thus all incident edge escapes at v are negative, so v is strict U. The complementary part supplies a second strict U.

The nominated a and b need not themselves be equilibria. Consequently this certificate permits root turnover without fixing a root label. It also forces strict, not merely closed, equilibria.

### Coherent primal and dual metric

Let g be the actual homogeneous centroid, x_i=p_i−g, and q_f=n_f/(h_f−n_f·g) the vertices of the diagnostic own-centred polar. For a genuine affine image the primal metric is G=AᵀA and the dual metric is G⁻¹. Since det(G)>0, dual radial comparisons may use adj(G) instead of G⁻¹.

A strict U of this dual graph is a strict stable facet of the physical body: the strict dual inequalities put G⁻¹q_f/(q_fᵀG⁻¹q_f) in the relative interior of facet f. Thus a primal cut barrier forces U≥2, while a dual cut barrier forces S≥2. No independent primal/dual metric or reference-centre adjustment occurs.

Normalize tr(G)=1:

```text
G = [[a,c,d],[c,b,e],[d,e,1−a−b]],
0≤a,b≤1,  −1/2≤c,d,e≤1/2.
```

This closed five-dimensional box contains every normalized SPD matrix. Deterministic binary subdivision covers the whole box. Each terminal box has one of three exact certificates: a fixed rational vector satisfies vᵀGv<0 throughout, excluding PSD; a primal cut barrier holds throughout; or a dual adj(G) cut barrier holds throughout.

### Exact arithmetic and independent checks

The geometry exporter encloses every actual primal and dual coordinate between consecutive multiples of2⁻⁵⁰, giving midpoint denominator2⁵¹ and error at most2⁻⁵¹. These are enclosures of the **exact own-centred coordinates**, including the large rational centroid denominator. Crossing-edge parameters are fixed multiples of2⁻²⁰.

On the entire root box, |G_ij|≤1 and |adj(G)_ij|≤2. Both verifiers include rigorous coordinate-enclosure errors in every norm comparison, check every crossing edge and the two high-radius witness memberships, and verify strict separation and complete coverage.

`check_cover76.cpp` uses exact integer Taylor bounds for the linear primal and quadratic dual forms, plus a full binary coverage trie. `check_corners76.cpp` independently forms the cofactors at all32 corners. The pure quadratic coefficients of a dual norm in a,b,c,d,e are

```text
−p_y², −p_x², −p_z², −p_y², −p_x².
```

Separate concavity gives the corner minimum; the maximum is bounded by the largest corner value plus exact curvature allowances. This checker uses prefix-freeness and exact Kraft equality for coverage. Both use arbitrary-precision integers only.

The floating C++ generator only nominates boxes and edge points. Neither its eigenvalues nor its completion message is accepted as proof. Both exact verifiers actually accepted both full covers:

| Body | Terminal boxes | PSD-excluded | Primal barriers | Dual barriers | Checked cut edges | Max depth |
|---|---:|---:|---:|---:|---:|---:|
| FINAL76_G6 |12751|2310|7142|3299|362073|27|
| H60_G6 |19050|3570|10996|4484|405286|29|

Totals are31801 terminal boxes,767359 exact cut-edge checks and63600 binary-tree nodes. These are not spanning-tree counts or sampled-metric exclusions. The discovery limits of500000 nodes and depth80 were not reached; no unresolved box is accepted.

Observed markers:

```text
EXACT_COHERENT_FULL_METRIC_COVER_PASS 12751 2310 7142 3299 362073 25501 27
INDEPENDENT_COFACTOR_CORNER_COVER_PASS 12751 2310 7142 3299 362073
EXACT_COHERENT_FULL_METRIC_COVER_PASS 19050 3570 10996 4484 405286 38099 29
INDEPENDENT_COFACTOR_CORNER_COVER_PASS 19050 3570 10996 4484 405286
```

Each verifier also rejected three deliberately malformed certificates: a coverage hole, an incomplete crossing-edge cut, and a false PSD-exclusion vector. The complete accepted cover data regenerate from the inline source:

```text
FINAL76_COVER.txt:4954189 bytes
353e21d45a2450c90deb5793f3871bbe39af393d132f696bde8db8f42f5eb65b

H60_COVER.txt:5667209 bytes
cb7b4fc7dbbc80bf2737015c759e4ae2cabddcd07852a80e292a132acaa9ce4d
```

Singular matrices occur only in the containing box; no degenerate limit is promoted as a physical construction.

## 3. Nonlocal inverse-metric cages and constructive implications

A separate exact certificate identifies a six-wall inverse-metric cage for the identity-connected S1/no-extra-closed-S component of each body. Normalize H=G⁻¹ to tr(H)=3. The six required nonnegative dual escapes correspond to these ordered **input-support pairs**, with their physical edges:

```text
FINAL76_G6:
[73,4]  edge21–26       [7,69]  edge29–44
[70,13] edge38–97       [22,21] edge91–136
[33,34] edge114–133     [36,37] edge120–145

H60_G6:
[5,4]   edge12–22       [44,4]  edge20–22
[52,8]  edge25–38       [32,56] edge91–96
[28,31] edge72–95       [27,55] edge74–94
```

In canonical dual-face labels these are FINAL76 `(17,15),(20,19),(26,25),(47,53),(68,71),(74,72)` and H60 `(2,13),(16,13),(18,15),(28,56),(36,45),(46,44)`.

The cleared escape is linear in H:

```text
L_fk(H,g) = n_fᵀ H [s_f n_k − s_k n_f],
s_f = h_f−n_f·g.
```

The proof uses a rigorous2⁻⁸⁰ centroid box, a positive dependence among the six wall normals, and all six vertices of their five-dimensional outer simplex. Its maximum entrywise distance from I is less than1/1000: approximately .0006905792429746753 for FINAL76 and .0006098802201184858 for H60. Hence ||H⁻¹−I||op≤3/997. Exact Cauchy guards against **all** other material vertices retain both strict primal U throughout each cage:294 tests for FINAL76 and230 for H60.

All29 and43 alternative exits at the respective six source vertices are strictly negative throughout the cages. The existing stable facet is strict there too. Reaching a true cage wall therefore creates an additional closed stable equilibrium while the old strict S persists. The identity-connected S1/no-extra-closed-S component cannot leave, and throughout it U≥2.

The cage argument alone does not cover disconnected S1 components; the global cut cover does. The pairs provide a useful geometric diagnostic: most lie outside the currently named critical support block. FINAL76's present block is `[5,6,12,20,21,23,47,48,60]`, associated with the detached stable facet and current P49 interface.

These pairs are **not** a prescribed minimal surgery. Moving the actual centroid changes their coefficients; exchanging edges changes the witness graph. Losing one inequality is not sufficient for110. A support replacement should monitor these nonlocal restrictions together with the current roots and saddle, then rebuild the actual mass and full graph.

## 4. Four executed exact affine images

All matrices act on physical column vectors with no translation. Parent vertices and normals are not independently rounded. Halfspaces transform coherently by A⁻ᵀ, and the complete new H intersection is reconstructed.

```text
FINAL76_DESCENT_G9, applied to literal FINAL76_G6:
A = [[999998337,-3286,11161],
     [0,1000001010,-10927],
     [0,0,1000000656]] / 1000000000.

H60_DESCENT_G9, applied to literal H60_G6:
A = [[999997985,-2576,-4940],
     [0,999997561,-8612],
     [0,0,1000004454]] / 1000000000.

FINAL76_SHEAR500 and H60_SHEAR500, on their respective parents:
A = [[500,1,0],[0,500,0],[0,0,500]] / 500.
```

FINAL76's descent matrix is a printed-value freeze: its[1,1] numerator is3 above nearest-grid rounding of the numerical endpoint. The recovery records and verifies this explicit+3/10⁹ correction. It is not silently called the unrounded optimizer endpoint. H60 uses nearest-grid rounding.

| Exact image | True V/E/F; C | Strict S/U/H | Positive P/Q | Largest P depth | Largest Q depth |
|---|---|---|---|---:|---:|
| FINAL76_DESCENT_G9 |148/222/76;444|1/2/1|1/0|.2902382481603379|none|
| H60_DESCENT_G9 |116/174/60;348|1/2/1|1/0|.42047947468135705|none|
| FINAL76_SHEAR500 |148/222/76;444|38/18/54|17/37|.2905779253241606|2.691461814729966e-6|
| H60_SHEAR500 |116/174/60;348|29/14/41|13/28|.4206192629450934|2.8841092013121328e-6|

**Every row has additionalweak000 and primitivezero000.** Depth means(birth−death)/birth. The smallest positive P bars in the two shear controls are approximately4.253142039569435e-10 and5.340921279027019e-10. They remain in the exact outputs; smallness does not make them weak or removable.

FINAL76_DESCENT_G9 retains S=[4], U=[10,31], H=[[80,83]], detached stable hexagon, and P49/cut41. H60_DESCENT_G9 retains S=[1], U=[6,26], H=[[54,57]], and P36/cut32. Both large defects survive.

### Actual homogeneous mass

The literal input geometry gives approximately

```text
FINAL76_G6:
V=.2788245400252212,
g=(.013844503590742194,.013215342984698406,-.005494475097812719).

H60_G6:
V=.3080065838504582,
g=(.013318519792907147,.017713826473192158,.005744200528759818).
```

The complete rational values regenerate from the literal halfspaces. For every new image, independent tetrahedral integration verifies exactly

```text
V_new = det(A) V_parent,
g_new = A g_parent,
M_new = det(A) A M_parent.
```

The descent determinants are respectively

```text
6250000018736825005613517/6250000000000000000000000
99999999998507649088956159/100000000000000000000000000.
```

Their actual volumes are approximately .2788245408611071 and .30800658384586166; their centroids are

```text
FINAL76_DESCENT_G9:
(.013844375817879107,.013215416370324213,-.0054944787021883835).

H60_DESCENT_G9:
(.013318418948922158,.017713733800114435,.005744226113428973).
```

Both shear images have exactly unchanged volume and centroid `(g_x+g_y/500,g_y,g_z)`. The complete exact input and generator recover every rational first-moment component; no virtual centre or nonuniform ballast is introduced.

### Verification level

Acceptance uses exhaustive exact Cramer enumeration, maximal polygonal facets, two edge owners and positive area balance. Integration fans are not counted as edges. The exact A-induced vertex/facet/edge bijection is independently checked against the reconstructed H complex.

Two complete mechanics calculations agree: the primary factor-cancelled primitive auditor and a separate all-halfspace facet-foot/true-adjacent vertex/cross-product cone checker. They directly check strict and closed conditions; Euler is only a post-check. Three integration origins agree. Integer graph-weight bars and a separate Fraction segment-minimum implementation agree on all97 exact positive barcode endpoint pairs. Every bar's exact birth, death, lifetime, relative depth, full component, complete cut and attaining path regenerates without a floor.

This is not represented as two independent black-box hull libraries. Likewise, the global cover checkers share the exact geometry exporter but use different polynomial bounds and coverage implementations.

## 5. Two entire finite descent intervals

For each descent matrix above, set A(t)=(1−t)I+tA,0≤t≤1. The full closed interval consists of nonsingular physical affine images with **strict own121, additionalweak000, Q0**, and strictly decreasing unique full P-bar depth.

The interval certificates check all888 and696 directed primal/linked-dual edge signs by exact Bernstein inequalities, including rigorous coordinate-enclosure error. These signs remain nonzero. Hence no vertex/face degeneracy or mixed-edge endpoint/cone-boundary event can change the mechanical class. Primitivezero000 for all nonadjacent auxiliary tests is claimed at the audited endpoints, not independently for every intermediate t.

For the current saddle edge, let a be its first centred endpoint and d its direction. In G(t)=A(t)ᵀA(t), put

```text
B(t)=x_juniorᵀG(t)x_junior,
D(t)=dᵀG(t)d,
N(t)=(aᵀG(t)a)D(t)−(aᵀG(t)d)².
```

The death/birth ratio is N/(DB). Integer-polynomial Bernstein checks prove that the edge foot stays interior, the elder ordering persists, and `(N/(DB))' > 0` throughout[0,1]. Thus the entire remaining P depth decreases, not merely one escape. The actual homogeneous centroid is A(t)g_parent throughout. Root, elder and saddle carriers remain fixed; this does not separately assert invariant death-component/cut labels at every intermediate parameter. Complete endpoint interfaces are audited.

Observed markers:

```text
EXACT_AFFINE_INTERVAL_121_WEAK000_FULL_P_DESCENT_PASS FINAL76_DESCENT_G9 888 900392 ae3f80e15dfafe73eed6c5c0d38797abdba6e7776e4963bfa86991f4f5ff89f7
EXACT_AFFINE_INTERVAL_121_WEAK000_FULL_P_DESCENT_PASS H60_DESCENT_G9 696 701211 2c2ce71fb5b78f2b908d89b1b85966b1bda467b338159433c7b4ef2af67c2e67
```

## 6. Executed limits and next geometry question

The preliminary root-free metric search completed24 L-BFGS-B starts:8 joint P/Q starts on FINAL76 with maxiter300,8 P-only starts on FINAL76 with maxiter400, and8 P-only starts on H60 with maxiter400. Seed260926; identity first start; remaining five coordinates normally distributed with scales[.4,.4,.35,.35,.35]. Upper-Cholesky log diagonals were bounded[-4,4], off-diagonals[-5,5]; ftol1e-16,gtol1e-11,maxls40,maxcor20. The full source preserves current-true-edge cosine loss, linked inverse metric, root-free omission of the worst witness, and margin1e-5. No numerical110 nomination was obtained. This finite search is not the global proof.

Constructive descent used five trace-zero inverse-metric coordinates at scale1e-4, each bounded[-20,20], AD of the live full-P objective, margin1e-7 on selected current P2/Q1 guards, SLSQP maxiter200 and ftol1e-12. FINAL76 actually completed39 iterations/314 evaluations; H60 completed21/147. Complete observed matrix pins and explicit freeze corrections are in the inline source; full floating ledgers and callback traces are also in the ZIP. Numerical bar filtering at1e-13 was discovery guidance only, absent from exact acceptance. Six-wall nominations used70 and52 floating deletion tests; exact cage proofs do not rely on LP status.

The next constructive step must change **actual geometry**, not continue SPD sweeps of these two G6 checkpoints. The cut certificate can be replayed diagnostically after label-preserving deformation; following an edge or facet exchange its graph and cuts must be rebuilt. Failure of an old certificate is only loss of a sufficient obstruction, not evidence of110. The nonlocal support pairs identify constraints to monitor alongside P49/P36, the stable carrier and the actual moment. Projective and genuinely support-moved directions remain outside the theorem.

## 7. Complete recovery capsule

Save the full source below as `RECOVER_METRIC76.py` with LF endings. It has **32572 bytes**, SHA-256 `cc881f9638ae2d5294b715403b6128e8ff2d68aa35ec9c96e406a1d49e6f5846`. It decodes27 complete files,70591 file bytes, from a72900-byte dictionary, SHA-256 `1a563f4b3b378ef99c767fb5bf09744423340528c3fc9b05c5b8297d191e8dd4`.

It contains both full literal H inputs, all new exact matrices and numerical pins, cover generator and both exact verifiers, complete H/mass/mechanics/bar helpers, cage and interval proofs, producing-method sources and20 pinned output receipts. No previous archive, network or source ID is required.

```sh
python -B -S RECOVER_METRIC76.py METRIC76_SOURCE
cd METRIC76_SOURCE
python -B -S replay76.py
```

Fresh extraction and the complete replay were actually executed, ending with

```text
METRIC76_SOURCE_RECOVERY_PASS 27 72900 1a563f4b3b378ef99c767fb5bf09744423340528c3fc9b05c5b8297d191e8dd4
BOTH_NEW_PHYSICAL_BODIES_GLOBAL_COHERENT_AFFINE_EXCLUSION_PASS
TWO_EXACT_VERIFIERS_REJECT_THREE_MALFORMED_CONTROLS_PASS 6
TWO_OBSERVED_AFFINE_MATRIX_FREEZES_PASS
METRIC76_TWO_GLOBAL_ORBITS_FOUR_AFFINE_CONTROLS_TWO_INTERVALS_COLD_PASS 20
```

Default replay needs CPython standard library and C++17 with Boost.Multiprecision headers. Tested:CPython3.13.5, GNU g++14.2.0, flags`-O3 -std=c++17`. Optional producing-method replay uses NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu and one BLAS/OMP/Torch thread:

```sh
python -B setup76.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B orbit76.py FINAL76_G6 --runs 8 --steps 300 --seed 260926 --mode joint
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B orbit76.py FINAL76_G6 --runs 8 --steps 400 --seed 260926 --mode P
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B orbit76.py H60_G6 --runs 8 --steps 400 --seed 260926 --mode P
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B core76_discover.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B descent76.py
```

A different compiler may nominate a different cover; the exact checker never trusts floating nominations, and default replay additionally pins the observed cover hashes rather than silently accepting a changed artifact.

Convenience copies supplement the inline source: recovery program (`RECOVER_METRIC76.py`) and complete source, observed certificates, full audits and numerical ledgers (`METRIC76_COMPLETE_HANDOFF.zip`). The ZIP has9108812 bytes, SHA-256 `aacd9c57b65416f5a45847c1646152bf5265edde427de8a6858fdcd2b52e28d3`.

```python
"""Two exact global coherent affine-orbit exclusions; four physical affine controls."""
import base64,hashlib,json,lzma,sys
from pathlib import Path
DATA="""\
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;T*$ZnOy)qh=jzFlUDV(U+gW*{yy`nGyY}*qm~~yg#H20**el~Alu#tOfN-hxvE8{`w-dO
FQ}5)+hkUr52u&IZ_(V;*3@>LVsZ%pbEJ*o`!e&B_B5w!CGHqW7Fg5;nvkHiG1DGlW%c+)7N%gduR~Q8fesISuX2e1Bf`_=U(h%a
lsyV>+zi(HP$^}zue!m?8lsHL8p{vo{%vxg8>x~vB{BX`@OcaaM3`!pvKSq>w?YmXBxvbZ^CKIUAp?q98w7;HY`tC93mM}Q{F}Xm
1x-5<5Lb%1u90v$WPiBZcyn>fx*UqVtlv@CZH5Kn^1bKtSNGe^C3Zn`y^NRsH(ap}OgRmrmcU3YO{#oL(b7@C0%c4$C!ReDSHX!#
#AxyIJU=3<VwQfOb++%BXQPG02f|vJ-*57FPz+mYt6vo3`Exjw=mQ?mDf^d%;m5n~V-w8~H*tcv?OuB+0^+tf+g2tnGB_nbgae|I
B9E-7vvOUq*0|S~<n{vg6%?bT)_gXHf3JzO)2=*j5T3}vuA}+_C6Se48VSTxfB(dJm0`NSGhf0xRO$!h_Z;hb4~50!KW66MxMDf*
`|ij<xYDX(!a9!!gbvsX_NT<O(!aFIOH}lJ=&f67cbUna5}2pM0|ScE>2q{o>r=xq=%=lggkViG^>U=L&n1!ag%xJFaCctT2~|y;
#&>b!);e3T1va|2Tk3+yvTW4M%=zC=UT?pG9rNH?6-7}9CUnR*WYYX7bP|0F@gkd_O1N964WFwD*}p8FVdfh?8e{64o#z-jov`Im
&`M}Ct#I=l%4KgtCt1?y<C1_@-wXHRpWjm}YVMWNZGyRPrNsVkjOl9YC>J>gDax9iTv<&Vh@;7Jf%gR`d6--#HvK!R?hbHEY8YYE
Tt+a=ap%%J9$+uM^!)4Vbtc45{GzB5-g;4BSLUU%WRRF{d*o^A-lfHpsjVjtLSR$FB&#0%YOJ#RY?evCth58|(6!6Bu3Uv5q9FgV
dS-}rDqq>eRkUS(*Js+vN&Oiv&7E499~>XHepDXZVz3C^fbHP(R}YY6&2J<`4N18vn}+!@pu=?BMPw@Y2G0&!41}X4;B@-jviabu
5*?@Jr48B=wPzeMxBMZivY{}s0#MWl$|jF&Qkinj>V@^lxt5q1vWyNNqoVe4-t&_`&Mh#vIH=d<UB!|FLR?^PQfH)rk_1T0tZa(u
DWwbP42t8Ir!r>2%N3u{mGq->d^A#t)81r4M$!1{f(DCqldr7zi#UV3xjI=Rsfs4X&(g}p1N^46_gzq^QZp5(_@-LFHkxl8zrR7}
er(ubw9WhKP+-<DA1gM34#yF%OQF2O_%c3Y|8^>2hgxlAN9Z@a(Xh5&q`e6vz{sZSY<rUJWzs@N6Kw&4TA`tE0VJ}+{jSFrk#WmQ
8-ntbCJo;FMzLD?2P+(bKiVQ3-IZG<v5*M%jnd$TH;wMRtO0`Eu`nYK>(7V$<fWBljx;sFsVHtK*&bmu4g2d7--Y?|9JiQg71-^q
*5jBza4uVMO~5BtBHWERQ0K@6NM|*-zFh?}_4yqR%W+8#KI9TCMzmRAhk8SsR-&18v2OB0CwwzRyf{~?r`MLq-@jGh%M@b(#03VE
`E5gk>RdB0Q{f|pBPHU?O`|8aAa;y2x}7=iEdu4=D#O4gcjG`&r313)Pbb<~9$#;)Ncz{%p)G=_*$2wj=4})L%}|O?$GMl%wjLd@
DRjvYYz!6MH5PEFX{Z$*@+=q=H|PVE_BQf)Ep16kv8$_fq-O?falr5_GrLbB3uz`?&_SWg&4X`(7&{9a(>U`>2qp#%sgKah-p+iT
F8AfMs9<%#bTRG`i59y+PdsbycuQYnf<cIc%GQ*y<{eD*Oa6zZkgVsFr3#lxVSg8Y+PjDHH3Nd>fcl8kA=s8M-%pn^g#3rnZO<mz
-Xl^G5J$XoU{q&S|0+;a-|FT6IX6Y&+~PqAr4{q7H%ZL<#@YR)>ef0S8W&Tf+5$5zT}|gtudHG@mmR7XJD}z%8z&BxZ6a;Fq<p<L
_wQ#GMd~8{RE6--qFqw>CjQy{Er{ynZ*zNpuZm!-B+Ax@S+Rzp-Pu48<_Z<sJHR`REbLNj9kg@&ix_i(pKSRA(sZ&Y2|(czNuZQ|
aqtg24S<xHJ_It~UUSgN^TT`?sf!Ku{KeNVNIoIK(cN?-wb1{Q8@tAri`Ui=YYMX#a8~XOhRkUdOgkeGn6NxBl9(a0lt#LcA*yDd
_Oiun;L-grR$Q><)1`}H_Ew`%5{Z*oq0`ont^$1IPEs7^kJ!fdjjl|J-iTwvqMw^D3$H1QN!NY8oUaakpOs(cy*%b(4YOt=)q*qI
m&0e9+!-sgFE`-k(g#XVWQ14Fb5+j7_?#FrFW0@~WEt@}di$6VG*DG@*bll9!1j!sV<hr$Cb{9_x6^gxm97b6EJDPe!hqtv1(B7)
1)#f%@QZ*(@wnFDM^BsvZe;Q;EtDh=z&Sbw-XB$m0^`DfRn`fgQ~%V%1s1HVEVz8SDXd9gmb?xw!eT-mQG9F(8Y1fVC#WGkj95M;
tD?v|+VeT9%onBui}rJ&uuaAcK6UO6>CpMAKOxq>Ga;S$Tw$LMRX~@O`qB)2l(xE^d;-JS+51f@vl6FeW@pZlrr|fnk>{dwBb-N4
Ig?iIpo||KV@rdJ?60JeGpRh&5n1|yA_G%ctOBkS!v{fp8F6MC)9WXh6lFEW#2u!{wigPJbFjRCfAq4VM|k)6{PF)tO%**9c|f$i
+m~pRj7J+Zhvz6?!elvFYWr^j>N_gI`wm~a<(_2uKQ(szkqN!djm+(Z^~0PG|33$r9CBRSBBBplRY1Y8L#aV*p$Xi2z`#K!*((_l
jMiDt0Gp60=+d&Cd5=txQ^lW<g5+lH<+qi~<~Xr>M<C3Uvgb%fS%SdqY_9C+$>*cPu$>UY+SBcCYL{|hqMAgacJ{$`<PL<uD?Gio
xxhBA+h6*T(fDTrUKRgEZMe8q1#}~~=j6y(=}4ctj6u`1im1HOvqQ#KPnEpw<Egai(}=Rcg;0_9=CWPcN^cD5ZxGdB22m=<gwx0p
;&$GJP=^VM>)V!KfdSZ%wwr0DHvQgFkqejMg~4)Ek-{3S%_^u2^h^w-WW<NpfTI?q%YY!+)IL&vZ@;iFFcakhzSvir7cG~A5$S7d
pq+^?wkFC02WunX{ctrB<9d)<{wk%)RnrDekW|-V&*m~3t*1>%ob6aj!Z1R-O6u=7#FqjwH%18tX8;cDeF+2>nN>mCt(nDR%?r4F
7^FU@C$}cx*dsEo77Mz0Kl~*;?R!>K&D`XT>@k7?(6bV2e?_6p#fjVlFSe%D6C!tFU_Dq$tesVyt3lRMS-DLFbXu2(UFa9>MTa8#
#-5t9cdHRK>>NbORm?=4OZ}4LZV_Kh<`uhhu&?5W2W8JfLf7Wa$vCq;ajmnOG#$CI%>fz(Adu1STg9u`)EPSx09YS`0|&97FC4j&
X6agFlTIKnjx{Bo&NF|k70S{;9iqfgUCkMrDc6p3<WpdTjv%hD)ItK0`*aZqj5<d3E%t3z_`v@czs2R4k;pddgZs&#(zIsz3zb<M
Sqo2@QTTu)WPzn&vl>bf!4&fRO|o$6fou>hzq`Xu0Kf`ycGJapSKVqvo%t)MTswlhZaN_htJi>qH&NK`?n@-w58$XM1`g{_Z@IfQ
kfgjYPm($NYqF?!Wi^+_PstzV!N$(V1BW?kp5|?(T4W#HT=HH<@5BcW9xAB4wUuRK2y5`eFN^!V8Y_Qbi|@cU&DY`OI=5nKv7om?
S5h!ienx1*3od#fIAfLh04G57TX@~96$@9Z^Vuude0yi*+GSG;(`&8a`6(;r1aCtiV2~&aiYQcx&j2M<v&lecNFvXZF-ac4I(Zme
h%d$tQ(CwU?k)H6ub}?{pOnxk_ea7frJ0;wN*H&(>A!i$2X|_Se6v+kjeM&1Yd)X9OcvY$VKvi#R)E4xT(6a{$be@Z9f^Q?jUd8P
e<jwUeHaL5e%R%)-;J*Rc!yxyxM047hD$q)d3dCX@O04GMt*fkxCo3Q2Iu>bVV)|G`#hbfOJS;JmJP<r@v`P8XH>ky2w2heK2H;d
+je_0qI@L8&}y&M#dw<~ZxoIn$wU1?_u#%-Q#@zDfH}$YfbP_Ax}6;wc7EIPQ7AN9x{XDJo>FXZ&SjH!ZAia)<X;G>+PCL(k{$GP
`E>#aJIh`6J>q`&8_(=r1nW0G>v?-fGCJtUXI*|Uy`kYkGI#)hp-Xz)EK_^-c6KNS-XB^v5FTM;d^mk1_1^3gqOUiDuGVa?0+KSy
u^HtF=taw@pnv`}6J*3(xJ`ZdTHRF={7pZs@4^@!7Qok=aA$FSfnYWxztSmPMK=3`RA1CS5w(J71Z&J;fY*sFB%)E23AWt5LI<yL
BYzr-$Dn_YaH$aD6Ff%7fz(<*-Z!c@G$Oe8+c(@u>@n^W_!}&}bM6yk;Ni$2Aiwxapz)h7lY6%Li#SAK;4>R^2mhm3G;m2B?S+@Q
s)ziOV0_W-B~bz2=Fm1P<>8p7;ZjDf-DBv$x}ts9bh(y%q6y9+6{1Kp-%Egm_ujcOrHbAsbc|fN?JFKQat2M^HpSKiC%<e?tNh2%
*M*EWGxyFcp!W+rf8~WBaq}Ua<WP$0!LgClqf(2cCqiV`ao>}<;&-L>EpW~2OTE`;&F=LH?i40SHgsk-L;FE0V#)*5BXWMk4Xsvu
n{CY_6PmS0j=X3uLF5zWKLA}hJXAR1cWT8x9c~j$*Dt9)iyJkHimk1Cg-pe}JNbWRIMm|lh{MrIPoDgVO|E;)gkpd_|8URxGm$Z|
0D*OO$L;gb04$gnO;-A6c$VF@m`d&u#3;xO3ICw`8kgbU9%fj=@&L}j@!)IKP!%(-1*8(SpH(h3cB|-Z_<}8dv@HtqP__Oj6r^iH
uaY%z#POxIwolROvG$Z;UgCl$8inJz)?}3?O^wLzaXbED)v#bEhh8LZPd3xXM=F3N*cPaa!%7OI2b?4e-=Akn7M=8`@z}cAJLWRw
sb!XdF#grw$%O^w-3psP@Nr?`o#V9!%Y5j0y`(PxNF9H^{yea;N!+JNYPk~9D;>5ap-()mD&ow2(8=~zDbC{6SrjZz%LsGB6oq85
4lt&QgV#Of(15$by@ZCOf{4)ZoPfj`ME;FwJ&<GWq1>0&kkTJU4{)Kmp(B3a`Yaw%3*wQwrODwb%v2{NU0`;;bZ?%0uV@&BBY6>9
8c5rQEs(J^zM=?id4zj&U?1@y?LFaM*InQRWCP+Wkzg|5?$2bo)TNwC{WZPf(7z9Crs>Sz2H+r*1Y%kZ*I+_JZiJ|J39rpn1r?-U
$a?q<I~(dd6urcalCV>r$2p<T`sH_)X2U*Vigo*K|1{29=E3JoOkiRrtsZ7<i`AcBK^wmwD6;)d2c$3kbtpLP7!j>cj#j~CC7l@*
|D)r_{RXys`rUOjJJP;uv?&keLEwVC<K(lZ51i7u@tZ(}bZFPkKvNXWTdud%3W#a~{ciAvw}{2$LStU4BOR%01z@dXI4iY`He=S^
-v`I|n3@^h4K4%oadLH0&qVv@oAr=Lt_#UIknl*^7HV>?rsy=1Z#-955Zuwt1d!$H9%~T8SEtIb^L|`K!l&!`uCx7^(}n7eqvqLb
#ID<L1!_{@`rIj;nKl>)cF!yoX+pQ?;+t1%R=XHYLzEc7m@w+>j6xv~zpsv7-o~g*TxjA&WlZM#^+}>IjK6OfBFnL81Mtg9lg3np
?xkZW@odRR?}0r2O+}1tyWnFADG8Z3c9prGygDoaSQ7G57qa=)hNMEgc;J-v=!?*lv33X`S_Ea_3lx;rs#0Zq1|)htsbyUfZ6@-f
*yL&=KRLmekU<3gV$cfxCe~Dzh!07c)s*O&bo$NsAk*cBTF#oP!hv*p`L;eF{x7_V1M}%CiWaAq2qagX!TeQGzdJN0aN-H*vyuZA
TO}_~l=B%6R=5*boXJ(7+=p#``<Lp-2NcnYIftv+M-CST=%0?@yA=U~7uwjo+w2fXJj<5_5|YGs$TeftX%(>PbTP=7f3s_Gq>+T5
b5El;z{&yY`N3z&)YVqvEP)6ihth$=61?OOXp#%S6n3SarNL}~Ifxy{EH@y(Q?r*yydjlI(7%z?2OpBx;;Bhw`7;2a+N7yrV{8dp
K>IOv3d>mFGtf70kK~4*`BCj*l)gCKuw$#<K@IB`vIaznu*W#3`-f*0PW!2Gb0P!TwlxN@RAYf}#8Ob}&rKuc$bX(2GVm2iel@8)
66N(s>+EYa<x&YVrzEcK@}^x-8Fk||{vZ4Zz~%id{O`(Xlduxv3y~o+gX0dqcHwscv+?yVfFzC0_^YwsI5Lb6QasOqGz{3-$u7_L
MgP>}*G{s!a=oVd{;;Ka86@6tzk0xsmWC~;#WnyN$|$UdGxpu6@i<LEUt$tmA{}yj+)C1r|AMp@jVN`{mnOAUsL$ETTKr`<9@bu`
wgL4k;jK~sT<rDfodDb?>92Q*7p9@{tq0($WH~zicEFT-S><Il-ugf;10dv6YeiNG=Ks>l7@|@f>DTRdR^V|U>4@bGMOgDxRYL#@
mB_`&a`W`o>(?ZjT!gb++z_GK$L<Z}k~2rCnea&@v2}JC#-*`HhE4b@7ci_%;XGB%eah`tGzrJmZ5Ve(jPeQ=XFCutRri_dn^{f3
P@3n_vrwXB#Xfu?|FMY{A<LPR0->e7G^vj(n94m!1@E#+=4n_YT!{~5x5TqD#Iyx!H<g00XXJNH!X!dUq=4lDc`wH{#|0f!l5WwQ
9Si9GY?&o>)jJ1>_TjAeY-?WgXa_qVb?^=57iw}H?H_;jn($YuQyr=tN6^9}UwK^X=KitmH5}DUiHm-gfF{$8iMw<n09)?2;T@pW
$Vh{XG32sH2CbhglPtgEbFWT7sXp+_+hyW%$N?JuxKT7w>hqkAW($42$$Q1CVD<m!55}j~z!cu&GFdI<l@ITv8nVc^gNWFkL}Tah
{*38W&N0A}qV=b0`#Y~B7d}td+7|-d{m}7zjUxT1wrO@)_B~a0HgIot2pi4MWOjtH2plhMgpi^m_5B;NI9xzA^;md!rr5tZe;qy;
%cj`gVvmlya2L!$yeP0Scu5~kuNfLgJ*UB;vUC?xQ>C&{tC*s&8u$4Ci^o)WySZ_SSfAP3!2vflQtbIY<+>mFDt3l%jZkvGztX?2
@MdFlkjl-B()5xl#H!<DOch90{PE}RiBOAFw4C~VDkzGXcnvwGl7w3ivbHNwMg>?evIV0+oRGbgF(8maJAP?!{yeZ}U~G)O_Ab2#
QSO_o^%hN|bx7|DCUSO$krb5M64-f2V?<HW0(;jJ4=@`~E@X7bqOKSFesHFgV7g<w2Te2}m&%%l)S6J=4%ud9bNWO#{7YPOUj?^y
<IvZJLcMY!1MNyw+Ct&Kc%^ove(TEVjvqY|pt)pxDz$Tv1r8S1#&YYMHpk|z5|1~u-`QDJRES0*9tyiw*c`9Fo?`i>!7p)r299b!
CL8P+D?!&ddZR&%c_gcLX1=kId9EptAz~{-uBNSdkWt*ITa$iS!*5vahZ7ZdMEUDQG<!C@H{yBZzOo<e+*h`RXz=MOyWytd8xA@a
12~NU*R&@|Ad%}BJ4i2@bTT?8rGBrH<N&~Iyhbyvtw?RBFmePK`vcCuJ}}zDgS^z;&;oGY;&sGhW%sR*Rv`6rT}r9kJ%{HlpnKz2
TIKROfCM*9s$-y$9W4wl2d#<kQ3k(Z?PPIjv86iAb^`X!<>o{BHn_6c!`v}(DJ^}b&o|9Rg*XliRfdyI!uFcR#mtrmkhlRhh!f_9
^E_!b#=kL4GEw$A#NlZJY+$t9Ev^rP-$XZqK*|%mpur}Q89!H(`j(<Rhn}9#;0(sgy|8w6dvLm4EYAzi2n&<H*mtdyOd<TZ^*K^6
pg9)te<6*F1RC9)`n$pCHpD*dE^Ri{Rkz;A$n(CRzqLN4PKpaMNWm-_v0ee%9odWGmDSZ$%VJ_WmbzfM%lyDRBD2mEr!YlsZ%@=r
(P|d%f?E?QR|QNIVc^DcEBwV{9+vO`R=XDml7ilTP##TG0|k}u;?#D^tz$8=fM5|@*2YNju@xf=%Gs-@FV@o^&t7CF8d^+{?oI$g
qP32QJc5On+fBp4j`U|argY^(*!pTxURtIV?gysOu(;%s%K~dEi%5exExlk@f(FQu$DulihVm~(Z17mQ-}7RbLqZhgDlonVX-D`G
X~)3C9&<F&N0pg<zIB7HP=_mxBH?hwa3iOIUnB6NUFPiZNlU+eGg;WHcL`0_afcMqhuA#?gh65mY4Ph1+G5Vi__xFjWOR~I6<<Gu
sCuNz`RJDNo@+3f4`7ve<1FOnLg}kxRXi5;GfEl@6Y$Ro|MLk}dXQF9@w&8A$o7d8`2C<?pKMBkiq+Py`;ZpF6@BeJm$VD>00Lpu
I9>mejq)1Q+W!$keh{)Zg}2M5ca;5VK|nYI&L;$ryc!?3`4LtW3WO}F8BJ=pJ3ET{{q2`){TJSbqJXRNAfo+QHA=Fpf&v5eO<D5?
kHmfaAwGZW@8Lv6P`>vFLwoN=sBkV#GNqau$LfqSc6kSI5XE#I39m;EKIZ-x^s36e!gAg|T(SzD*4b3r0fLqm(*#N+HD-NjLP<`G
xHkdHJ!D0am+9xbEGSXF-BRz+XSafL)|n-_g;h3@aawo{737hA<ZX7AN?EzI3Bum#Lc2}gjFe6!F43QTfGsteXmY%i4z&M%dE^xQ
oC@;FmF%bw)`S*IsQ3cegJ#sDM@sZTFE8&Z#-hP5krO~ckBajm_5r`2Iq@iNp2Iq+`M9%1317m+%Ej2On0;S^<=9PY3`2b=s{ZZc
Lp3h&r017FRODCJ%C*)9S<4u4WK9LnevJ9Q7!{KV`<{T^h;VYuT<*i9GuzaadLh_P3U`G$WN=4t8Zj)5_foG&t7OEwZ}?gB*PUv;
ux5<){U#|-@1Z`T+wbvCPsuEA?(}kdk6vc+4=A6)Cp7PjghPN-ZRD`Uw{^AX3jp458Rpucr1GAz3MGhpMldC=&ze|7f;y<w7``EC
df+5Z+%6$R*{$KbgUg0NPbAj;iQA|XA#mLKlni3kyaNk)ab_K0eQ|4BmP<<l*xqbLnO=L(M5WQ`6HQdN7ViErgJyiUXTICI2g0L6
^5}w870`lc6=b%2&pQ!5xPb-YAb@<F&5oJ0Uu073-R>wQ20^Ycwh85S#Q%gqjgZ6ruF!kQd%PntVWPv_v`yTWOG=R7UBsf(7jgis
mN%x-dJ4*YqqSLzMrJX~;sI%-nxeR!TMPof^yd@Rz`XjB1({_2S16_tbGvM#1C)H%K1bGd#?^2$J9;JDV*WtVuC@N&m?a+-Z42aN
GuM&SsdaA|!#t6+l5Av=jGL|ZvVf`U`iBJ1IK6W!?qzJRg_Ci>EZ9tnCdPUC>2B|s`hA9=g-P-t<=wUf^9NFrHIr9r^K4cECZ*I$
;majjynUn_e{=x@(t-2}83f@Ko>g<^@!rBcD?=1rb%)<d6fm*7iC{QVM8b4qm*W5B-tpea79{_5BMRpYJ;-|Wx9btPp}TSu$l)Y6
tq-RkI5j?gma74m2|%6hSNRnXLaNieK#|k%&+7vM!k+aVDZ;5dsiYPyI*%tkUU5Q~IwXcGrtnr+S#?kGV%r2y6tyKphZbo?ZQBo5
<pt4ftPy@bk;=0`rl1~Vx~4(VtXui7L#^`Bl&EXHTucqA%eyix+MK(0%ivpI%76(jVS(~SbTkSlTnKH6P(EN88V~-$0^-mk_Hj1&
YM^j35mZL-eI!A9m=qPrHUTAHQjG_@`*);iWhy#c3F`S@t}~3Hq-+i22r{u6igT%u&1)i#`QyscNhst6!mQ;G6x7B;1QJ=oYBnRK
sl`qE4JcfLe%v(N$uZ~8uVGsNu)c-Y%9#IM&MGfDU0IiemilM*ZQDztYj-l<pUwY3eCLS`J4qEyO3A!NXsay}t>UhD^ns(Vghlg0
)NEUeaaRJsGdhR-DlSekGe*)OGrFF&Pd9daVcm$3-@Fe76`OU6?>8>k3q=zy^C21R>c|sp{h86WmAz_A8wcBL`OXsfG;ZEAP=aZo
3vnxOO-6JzW&CN10I#6f-+p#^qGBZ%c(C1wYFaHt#OB_0U;QLdFGnzH$ieuU5SFXM>W;AqKqmm_5VyjkpebT#uuG8!Z(ZEmeI|yr
F+;J3+PtNER31Jc-U9gxtK%4}`||}0z^%k`prF1P|3%V9rZ3YM)-TLeZ=?IMB2&&4F0bedMxZ>elIAr3W1c$t`M_NbXhq{%T67yI
`=o~lt*1G7!|0EAs&P9zeWz%4h~xfEwznK!jWY>kw~^i~ED2_1m7r__nET{v*-ilG@taY0L-bE<^~{ZJZFA;Mm$ID?WGb}8?E*Gf
tWMtF&NMlM^Hdgs69OLTv9i|8cC|vZUzR4!NM6p%7Mo(aAnw<9UBPD7D-~pmSY20N+Eg7QpUy;cc9k0A$+QsS-0Ei#pFXI8rrE=-
4X~a#=pV&R)vFA%K-%=&=x~mSY*lA@A1;aQk!Ef^VlB7($zTGJLf22q!4BOL>S)|{tBO2FP`TP}U52Y&AHC!SmrO%Z#M9VA>j`jS
-l*eaDh}w`jNM5K<Bxk7s<bP#LWQ`5!r<hRnRSYU*8!A-;S!UhsqKb}aSt}>`~}n=b68M2&b0jMA5UR|5I&J9*h~M;OIO+78NzZg
H?Meq=q6uibNvQ5ooWdA@Sb-Zv5YZ?wG5k8u3xnx0AlCrFV-M^m24(FKE<PE+Nh@M%Ov8W8N+n?-Op_*^ClF~^D?JO<4ix+V<BL{
ESX-J^sT;)mk&?WbV#QN7|XnYB!}^!NE6)hPlykdy~Z|Fro$_GTseLNj599!#CJx|JP>hrg9ky@UgE#mwq`M#vV5Qd6oS$BzeSF$
5lZrm*rh@(Nni;`n&`aWz)U0t4an^+!!aGhuofZ_s+uXA&5f5TyQcJQynObiWD(8d*>AEYg##~vF##7k*pTx__IGp60OYG!ws1*o
(<^j?93TP@N6#3>`~Zm;)<Q*x|NrqhvnuA?N+=EmO0*Z-8~E=AxFijiNh?(MP0IT=Qypa>h6F5cwQpe<v1A88RQmYCB)->(9m{ZQ
iZ40Hrrz}p%zs^Zlsd0-moH9bKum2{wC$sQ0gVrUqT2-a+m|^b31AM>!<fjy3bL}cL)GhCJAMCjvEFx@iLO>*XaLk7Y0RKXsC0_p
4irkOLj%w5nVhK$yI}EWkbvV5@eG%~pfe#7dKSXA*e32G{P$_>%eo#!{rA*Ygq%O#cxW(f<Kr^-j7Iao`e-ZDk$<$y({+R2%T#+}
S;ta-=;`CY%N)9h*^lDcM|7t^Pt=hC=?#7fG(?}7@=VU@U6nvGO|+w7+lDce@qutIxQkUeNl;+fHWXY;hT=gx%r2ZU9r*OL##Ftk
6A+Jv1VW<%MBjS`fAJ4a5JGGi!-ifQHpQ)-B@^qD@21*7m_d=O2wWYlb*2(uY;U=d!wA>ZIZhW<z9#^9sM-8P#91Jw_6qg_B|2E7
*<7Xo)hRB8t_*r2QvFNyEr~E!s>kVC6PoYaA2`|t@DT_u&ai%)*ntR%IBAIUw3`<xu!aX|%%n-0MvPTX+cd@P1%;5$G>j!<UFXr2
1;MAxz&EdM8}YppP}oK=vCzgM2L@KboO>e#CJ#SZ1zm?P(+S7V<24HEq&TKQ{^`)tolva;4OO*^)}uLA#{m=nl!&7b)7-2r2?%B*
0x~MbKp<GgnhX#Wn7Lc({yX%w(7*>)nMQ?w#7|ZZrK_}6fx=qLI@;Bdbij*f3zBMXqnRXC*&|lQFA&W&k4e1_$G;lN{V1CD44qfY
lH8{h0`L)wd$HU>8$u96bHFQ2U2GN4*&ZenWtOFux@b9jjSgBZ*#w<O0pYpzd#%mDu|dTb+*FquC049QZ$hOuKwC+*o+pk>-;4I7
EUNbMnaB^g6t5&6LD18WJ+Da%DcRJyL{|E|vki3(DSd%eAL$f7k{M#6E%vy9eKF%Nbo6>2#g6|HTou1J7yQkKL2sW0)uR9cKdBet
y5>wHsP9T(EMAR!k$@<MJeUjr*kko~lzEc1jFK`M8EdHNianIPjg*v|4IFXLGdStLV;&tlX>^amm>iVDHU(9xUv}8DWx;?-N3KdU
BnR*mNGc?^9s$dR0|CVg`6?jB|4YWwGWbNPs%&~aUg`l*NaO8V@dTT#`()1@o+t}i<@%u5t>u?j8EGYQTQB?BPm3qQghy=_>Aou}
E7exQjz+9GL=a@JFpC$$B7f>M|B)=O5~Ip1(_AeR#kXpn_hw~Rw{SMD_6ATw=kZfdRGyBuBQg>5n)21DMdFV<elP_^4i7^6T}7^V
+w>TXVT?x<CY*IgcG||AdG-iw@{;hehyiDfJI55JvgFC3(n>22h&PY#D-4{Vq@;@e)=-a!#U@SX1Z_1l%l@+ua(`w4Y8@xvrXY^s
*cpS3ix0A3<Q2YUMZJ9!tV4GOJg)D)9OmLqj~uB(r&nql@OV7yM>wohv2VrnHEzFE^4;kgw!^Du8MtV~k!g%;+-2P7Q&wGb&&h>&
d?ind0r<!)i2fPU%WgS;-F;ueRyYHqAI10OvP;B5TuH;^L;2^xsJPxh9rD#oV?OEw{mv>~8QWfo8bX*txjvgx15C>Q?*ofjh<(XU
$FztQRq(g(zhG*=rH6?~aWERc<g99St{G>1z*ug|f0w}`XR_h}>5{C22P@*WjO!HvYpj`LVw_Vp6TU)#azhb^=9qEFxX32BWkbSN
2=5-~aXiFR*3TPR;TO_t!vW=me@~z0ST$nZ5KLY^@5~|jc=4G9H5EMpAhCaq_cAoP$>}e(VvUjts~YE!KejlmJH-7>qDRMyh|6{f
!|BW9j<x<=r3%jS1fF=W%h+7Dbzq8$1AMtw4v8+c(tY^!_umK;V|_b5RuHl#QK1LtzgmG}CI&n|JHhr<g`?bFo+R%Ws?Cd~#F*lw
*hSZQ<Yf9wv|FqLj@_^DhAOAIOAHl!OY6Ss2ceGH<}Z6^I`XNAe;zI=&E;@H8zF@Mw8aBHkB4$6Ow7!CMr1$Pge2PRMHyf_i-At_
s9O^b(A8)NOqf?rAv-NB(L3jgi2!;ldZYk%p{`-76w5MvJnSiDDgecZSe`5by84E9!c)}j2V1iM6!nP?|A-h0A2C26j6wE(`TBmA
2RR>8M1w2kS4_ATZzIGjeKYRUYFiX(5C38JEoh-YQ?8i(e8xbpj5$)!c@NTv8gq_{C<g2VH<Y5=9L6&2ME(KnP1nfwy4;|5-Pn&X
0FmvwV|!X2OQ)Y1-*?GbClwuJ&h|M<M&&rHD{cSOEX&>ch0&*6DjlLUzq;t+*YtVcMQJS2X5rv*N%2qJ^}xL4Ldebg4rSKgo{(Pt
M#{B*iKxK-yPRY&-sl}?`h4yo@L3d(u%mg84-}hW$haASk?gPs|L@j+?`KFXL)0qp%GT@m6`Fk@Zxqh11id6@dDi3!+&3n~PcWvC
gfV=Ci;i6+_N=9*W=Z#2_S1)W?@+p$-P$KnpVhQ2+!ATWTC-V=?kjm0x0sA***h&x_`ykG@%fma6=}Bii{jLmxw<{V{SsQd+s^bX
3qM&)g)?Tkjy#sMd&8hvXAS)3!P63kkMyu?F70;m);j@-XUZV_(ank1Rw;dFP0KvcG6n7Cc_P;{QF{%d0A5TpZC_C?B6@Ah16NVs
%^mpx531tC=$T{l>@C!EJm42uV#`gl@O;eELq7CRmCQB`r`cUI3|D0h2*J2-LtAQDHIA)sRu|?u<!RT%Olqj=e#N%A)-l!a(B1b2
I84mNSTpH~iY>63by(NJLqlLe%5wPZUK+*zTSQ8>13QCJ{7!47vF2|e+Ue`$R&99bqXPYmR#ImfyoSBKhKrCfW6AZ|L*V{cVGg{3
0Rb*GFv|W)j`v1*#>@Y5gVT4`f=ZC>`nZAx9!v`KkF4q~=ME8nCj}U(%+>$ACojj9C6a1l1kW`8r&iRAkJxarO(qKWOt7&NnQpfp
<2i>)`m7X33oXt5dR<QL%C~3|!JX0Bl=03$6}m}=at-Ion{*p9bT2S<Z3eQl$TSd7s&D;O{c)|{N*McoEH$&sZ7|T~AU}j}?u$>m
OdcSFnbZv1#o_QR0I#*AVzcdUf(l(YKr;B;&oh)KnRxWgD;>kJH^SDtd5n5vqQ(SE*xsq^=xqe-)NI5<#lWklBs=!z+pT7jX0QcJ
c4?$l7@#Qz(;2iq>yNoRvWO0}V)U;ZYQj`xx*B4E3wNsHK@BRb+syO7%HMfn0kMK&2czRz<#yv$o#<Wjh4E{1N~fDVZl8S##zO;!
?{#J8u2i0A)k}kIucV|W{2I8SSN5a<K=ONgC|SG_h-x?lneC<umHe2`<21r#xEFA7geXZCR!&Yt2ZU$9`2Xzs-$RoAj>-J0c!YDu
<RG$;zxr`GA#%rXU-l4snM%t}CiOG(qx60jAKSACtPQ>`st0M>9*A~xzvr1!I#eIenSev0V)@nbxK+16s7ps_ayK!>v)+7}Yy%4U
ruR|`F5NtRzz^Wmdn%Vc=$UGFy~^K){6(i9USwa4lvM)V$H<74gRCnvcWVH0it=9K5;fk_Bh`1(bWmO@Y#G1m-TX`&HKau}FV0ko
K4~DgBJDd^_(e4Pr-V(%jE>-GnA1`ajfNVl35EZF%8q7gC_#KK+PLqFZv)zp`(*|OS<B&|%I`#iPO#l^g1@x%IFJQM6tc>_N<#R~
?c^|kvfH(=H|MC$)qc2LKQG8=ylpT0D=TG|LpP26pUQJNS#{tBRogN)`>geRRe@cw+QolP7pCZr<gl&H=O-d-j(GLf&Roibdwzp(
+j43m!}Lh{rB0sTg_6BXA6}(j1n@XRky!BGF8h}>a2E={<oV>m35rl8u*nGC73vDlj5II1p$~-_D+~X@0-On+=Q_y@(>1)uqB`ht
34&Iy0h%omqy8v;0+S3nPe~6EewLR{PO^6i2deK)sQP()=@%(oY+E+9G!0ECxZAO?SQeUWzik0}xzTU$9k+{yyDA<TWk9=wDx#v0
Wved!(U4Jnvv%~N0WiQFTD?dBp~5e%?A?Ha=i=d!ujjt5yDnkKbL1<?7D%E$j*ULLKW@AR5<lTKQQIU9jSSQr$2B4|S2CjqffP)^
^U2C(2a<RU`BMX^_zRk0C`S8>(m&%n_PWc?k$7%(;iDsT<F&)iVT~{M+7$8dXeWio5WGm5jWl*<Ddb#uyEU*Gy(P&XhcZ~s3-33e
2CGHUr+~XG@94F`fyc!#P^0_|!2Y(j8ln^xZD(Tq4J?ezj?avR+~l0l&O@roR_T-l!MIBd8F3S_WRMvISH}BH2~+30T0gTrv@@O<
&MaqR%-Uk%KysJ!3|J!qa(*N6ESV%E)r^TB1g}IN(6FjaikYEk%Hqd~ZQc~JETz~CK4pYbW7uyF#<)_YZL#fJXSVuJNM*}Dn?Pv6
-<cKh#FrhJ1q$yu8b?n+U-z%RT9ouvVFIb5p$DK0V2h69Zp(8W?l~&!EP$aeA{U<tCppQ%VRXYAklIf46L$p2_?W!O;}?+)8(+An
Xy1==VP7A~m_K-6VB5o$<k%awOE2PIO%9RwNe44|>S|D#t!kJ^p;lN4%zjxj99<0yQRZdEknEjN9R=_gTsS`QyhJO~vPoc@KorUn
PDHopf_(xgtwM)4*$@lAIUPv7Sv#w4L3CR$6FQoc0=8!G_+%CU1RE(=BK#$t^4t{xwd9q1pqd^<oK_s8=4Jrov3?uso~$A~FwT*l
SyVa|Bwq`MAYN?ZEo(dHhox>E6dLU0JKK|jC_7+Y%S+FA@rZ25H4-FDH+6(msgiPd`BxhOo1i~hv?sv~cg1ODJ&MsMobB8i6p_;k
i3%p6pamt^5Kgt64~gnbR+-*JT*0OD3`IS3jlF`gpy-2l>}k<Yb<?|2GER+dw}MO3_&Di>eYJBb<`qB*JfHfDn0X%JnikPx`+nXI
r{9CYB~qab;vF<+Y-a$kAJ%Lg0;3na$KzieeRP!--nIT2k`wxApjV2;`(}=ERz=3<3n`$oHl{0g<HrPY1?OVRqL4-XD-r_0inj-d
Nmm8h^WX<8ME=v2cpr+9ayV{cUD{uH&k4)tg|L!TuZeUIs-|K>rGq0K7{OD(;cDA;g$?HxYi`n!qk6d5Sk{KozXTLV!tEHo>{uMe
pcQ1$west4aH~-p%_+`gffZw!d#wv$M&ExLOla6@ayhasfKpC*a`6=AUsoiLCL#;kWhAESD6gRs>>{q<Y0+~|`q9t5pyQ%9FHoSl
fig_4BBmC62l#=OV)wQCu2Yhu<_nO!-RE#Z+4-m>Z=HvZ6TdkJChQVYc$4rYp&b~Z1ees)7A3~i9dh%1Eqz9hclBgEgtd)VRlq0a
)Gm;mxt3Xn+YHYM5mgXkzJNEG59!S226~;10K}V$zlB2qILud1;5ki!Z2A{M+nAR6yR9$?y@0U!)5m!u4emU?i~wpRs@acy@l}gQ
(|dzYExc-UvIQA4zq@)W#S@S)>>hQ_t}Ey+FWZOSOczVhT*h|9f}1+;(xMYq$!kJr^uj?T*tvgUoi=V@BCzpQkST8mg1{Tbe6%Pn
&`PFtcl^Gn|E!H}?8e-DtS|P4w#Vu8?fOIM8Jre(eOw}qzo^o214`CigvCkHqhvz{6y;z2qBc`;t;J41^zcLlg5xqcEFJEFeYQ^t
$X6c`%WAQ&`}(P>AFakI=l!uBLJ?A416<4RXd&UP&1lx1YH9r#rBh9)jOF|w|Gc{W;qr_{v;$0ta#V-2?}I(vd!3ERC1ik#+?QL;
Ug&O9sI|>Gh^BQ`zI%d}QL9xOVi{2R_;v;fVuDW+cOUSAI4O~bb#waJ;o*G|FQw%NzIaRAF<;G-QPzz!^K);7gGXGTRsvPiz2W2O
s^NyK^DMjrfle^oa_+-#N?9R_m^y)&-mel^kcTclP}=J*NTPjA6AB;0eCYk2r_Dt<!DlOveWnl*u`;x({7l=J5E$zS0ZNLDTO1^!
fcSsp_ay>vPF-SK8n3N-0Ew(C;Zp_!Y|ema4St#_ho0A<A1Q<&jUobuh9_xZ0^qyy6}@^!|AWjyLY)6o#;6t%-iCz@3~O6V_kf~<
yeyrHY#VLa0Ley$H-0cD6C`jRxMn&)VpfUEAeQZ{8*%RjAl<|NQ}y3sf&bVgQth(uvQJRP5IUhlK(v3A=A<?#|8OLQ-^K|c_Xq;;
TmF*cWOL(6wvE~gtdfrdvrup(qTDzNB*zfu_p<zkG%8I{nfk!}%z2<$U3xl)x$!qbJ(in6Ow!W=r37rG*XB`{uZ%^FrP2gM4}_8W
lq_DO%dZQW;^$Zv#Vqy^`W4^zO4DnD$wyFYBYtbloe9@aTBRn}%vs_1qwkpW_Sp_ytbuy62985k)J*CnXN7L81=_uL{TAO!5PJ0_
XQ^{$>&?lI56h&5tif6uPDx`9uU?$;tQKjpV`ENXA^8ZmKnS(iAE8;^js27If?u5NI=YZNH29TGbB1630-i6uBX)7?jztH=p+?I$
GhR7~bvwQB7ZJs=gU}KK+SQ{nx{<<vzH-$40jbiTBuN&E;UrLxMKTKof}!*f5br>!!bBcmzM`cAJLC{o>oI62;m_eO2g<%dEnQR8
2XsROlqTg9snPgUQ+r`|{Y9`}Z@>Z8f^`HqXXS=o_HBe(rpqHF6j8*0T+N1Vw8&UclH-IqbAkGjFPYO;Ga4NpM9JkEJ@h0=TVyl&
K<lp1p3U&n3To(Z`v-UXf|T!BHBt$1C&=`|&UcE#>sGf$rU_L2%2W2Xj;95{07Yv^k|vw+ZBx<keiH5RGF<@F=jQ}Um9(_jeRC&I
aO*k%>=gYT2Q(Kn+Dpw-_hHLDvo9(p;C7Wp$v*?Y^wN}XG3_qCO`kV~ugo{&_iC)JhxPRU^=svJ9jG{zchT+@CQ<eO%eTi6v08#^
Q3atuyu9*ZZDX?Ta7zP)c^!|{rDU5;=*EOYfabEQR%j(sF~Lw3E^GRy=vazEZ{77Gw3@VqDDyJI4xXlz(F(u*(z(5ox0P*!SV|Sa
m^NPf*ZhFzH5j&GB4U55{VcDwX>x;cIa(3~zF@|{qz%yHl5b5k^${)&JHaBuHMdL+JPlmu_t7x|v|b7V`VVN%Up|tYtso&%6nM>P
3$+UMQOHddvbK^0D5PyLKfujmM=o%0s{e%KmsP2s#1GW9sw)k^2T`KpHLyx5D$gGAukF8btyB^3CW+EebCcEv6E3E&1J-UMb?}&Z
2wg<qgE_g*)jxiRA8ylNd*oo1ySmdRpqADk$_c`D#Gk&QsJ)~a*|F?3xDf+rO-ARrBjv{6Jv`4c`)~N(`3#jKh|K747eEc)M~|KG
b(<7**RmJ91l&UJ^NYa)iXYId97jdSv#dYHv8NUqkuY~y+zUl${SRFX*t<59s5vo&b*R~<##W?<sE(2rpD(b1`c0Z1CAB@81n&CA
j1v!RvVSFLJ;!Sg$LC1@f4Pfl%#r9xgZ&E0mbjQ<bbc#ahbN|!-99BIHUn2Mmg?YXlJqp}<n4$l@h4jc{Q^%w&HhqJORH$)wd{`7
k>jssS<rE#p>?ZsQ0>Z+$<i~cJOO}4l-QLVRj%8qK<DH^{)~x2d1*3JGMYPxH&vFSCRPtyg42hiA?vdg(4v4JOAy(NSGLT$q3Z^L
9O5H*JjvytQ()0AfA$i*EddKDYH0^qbJ33w3+R;5V5<QRm#UC06nGR7k*T$UclJ4W3pGhi$P=Ds^M<v?n9tUzSs$R&*`YUvzKbee
ACePxthTC>L$tCLCR8lzD(yw4k_;G@^snMmAW786K*VOlyaH`_6P~=(@Vmbad3hiOd6-)8v-c}Cw8rB(MfsEP64Qu9E@He)^YgGA
!!?8z-#rt2u!LhlO%Yxp&Um2|)F&BOaYA?4+;KH#++TrWFQFAO<jKrJE6XrOmyts}p8Tdb(MsA|8*h)7TU3XgK9+#LdC8V2^2F&h
LE8%Nz;=g_RtIMNtF0x1R*1rDQ<e@<SdcTo8Bk4LR;>)0$i1Z=J156v?gs*j&+*`TuR>ZIVz8iJQBO2aKqRkNI_GxrCP0U7z)O{_
4NXRhMD6EQ|K%@8@JG~DmT<=!G3p;x{~MC~i%e3O8d+ybUOT4o-5q?>Ox@y2%3bJ~U>!Ex*IQb4es(J+XAKwLSB6SWO(GA>A0}hy
LKj(=dK(WJhP)ozlpOGdt(dxTcsDM2!6zs{(olE!cw1ZvDwC3@L(#<DS-a4IjvOBL^+qd<h4r(pn1X!*lIMQSx%#iA8Bw4@raIfv
EXD<7dpV0}@P{mYbR6#Qc``;|4pmZUUR4BgM%O#>C~bSE@{ct&=s_%xn?J$=@R)R5Pcb5<x3BR1c|!~xqSTmY!Y2LyDr+FTs%M2&
Dkw4JW}`sE<Q>IJyr{MK+bId|Ky<nXt+j1jeb7C37}gIhc+|lzT{Sn^7MBBHR%yHfFFa8%o6#k&uXohQ?Is2h#fN{Vl(;YFrOQyg
0*ZE)uorbXe6z>ujBdTiT5S?~fIR5zaD?Ajw)YqHqrsvtBL1;)q13gb;I71W58?M;lkRoF-KN~k%Zv7&*lmu|H-EwvfkPe$NAC;x
wHtO8hPMR!j0RNn{$KP8%Qb13ZI><M-enqjz@-oD<*g4#ElBy|6=R1iBI+PZD<%QavDrBWATg<tCAY4EJwLv3C&3s(QVd2e9s~?3
`kbI+e}8E>lg97N$}Rw(sn!Nt)v^7kz(Xlbu#9EfP!3q-jpwLp0(AR*P?Z5K5U~7b+4dBFHJJx#e;-b#B=pNZvi^oR7?1{3lLTPu
`z6wKR1RxbzsPa4T1789#!QLf7@Bg++HKnT`ib{92A4Nhu;XwtpJox~*){B7=3+5Ee7s6lsz=woP*KNG2#>o=j8?Y&Z;U;u57Qpj
H#zV~o@<SG<>{zsp88$#gHd*SpbfL^SIcrR#vhz{KOlAx^tX)lBsurANzaQ5-uTMNw@|T1B-?<o!@tDaIr#+x;arPS8f%+~1QYTv
_yOf>GIwgmHpw85kM3b4e1V(+-BK<6`|@19P8MX%c;5wa=|`$AD{H;uq)z+WvCx&@U4kHg_>TlxtN?3*?j&QEkZ<i%8wO2(jV!e-
L>h=B#HUx1X79S>!=Y><a08S)bdW`AtN)=DZ|N|ch+7G(M0>W;O)pla%u8~`|7iq!1Qu0i7G1no(ykFFYkD&6?7qUgFJ1bvTGRIJ
%-Tw+aUDFXosa#8kpYCjK=E`g&BjJ*{a$uOXJeb-iVtSjF$cEO!<n|#?yeVU*X>;UoD<ewB`psUMCY^?lz{<Fp=)yNo;E)vhO|U)
lI>2w&oQs`jaZ~it6lnAzreH)fr|3*iwDX=F7zbJ$F$^kY0{|X){p5=g2EGKrb#)mbL3d5m@1`cwwVge7#3V}nzI)84kdGWU`a96
_`tmcRE86o_}}_OcXFvgD*p&>6=mYU8~}0IIw8qY&IQ@!#3RUXYhp`0Ubu3o=laY+EKchp4^rLL=UL#u*rMceGLH&Q<U~2#r&~XA
yuwnBy1Jo*Q~#or<O13kBrd-=FDnL|SB3DN%VxNz;u?~B1U4x{yN^GEVnj{D3&naS>f)T(Qp7(2>>kz#X?A_X0K+S|AW8-n_p5Uj
=*stDd|?=*j5DL}kSY#-j1`Tr&+Lopt21xqzf*X#ow(qET(2%{V&a<?=BUPYTtJcSjP)OkmHuj97JNO?H_~9Z?ClrK8ok+gt|cmS
5r-nKT$O)Rphbq%MG4FBHjODG%@P)es`}CfXP(vRl6(7WyKafjKViVZce2l2ql00YEkZQnzjv$Lc&Qz2TtluxW!>|LLS6$=A1#F@
o-9@nJYbw3qZmvjQ>qc*HwV)6;TcyrqBNPzvF3*<1;OOXd&H`|;SD@$jS(X|=Emt*v)0Z4&-VlQO#O;3LQXT5!vsErrcclv^tg?o
53?_gLoJy*NfgcqwM1Hwghp3-!sdJ$$b(TLrKuk4IMNCk7@@}{mPoX72{4kW-%4{8DA3@r_DeX`pIUcczwZ9Ifkof|t+*dZtuEHR
AIRxh37c_qgk99Lr9{ZRJxWU`;(MrG)MpCLuFk^psFQ=xd`>3%yKT0bn{aC5d!?#+kJI0MM;&ph!C;J%xaE3@x^EVakz6>5<<nXo
aJW@&2aMPANJg&4bWHjat){MJ7M5Uq)VN+)^jc&7Rg72BmiuwO>DuQ|ni-jqS=-cF(IsS`YYrDe;1RBIYmOKZEb`G+p2LF)7Te!0
FfIu4p@y(Fnk(Y(>GArywh`BPPvC1Veq87~B_P@`nfXfEc*}HONS}ypS!;r8j13aS_Zg#9>l^bWAN$yS40s*I{9fNRMg1*GU}|9n
S?{pIorpCvfK)MlrNOS3!c2qZy^S`GmzoyWsY0*91KXSI-aDboZ|}lvQWO_zWc(gjZts%Y+2gp!jZ~7?1+4k6c;ok>ts74I-LDpp
xDum)uZE^!QQbuMZs+AA5@(E;TPX1L@c&7+zv<lR$*SM3P1ldZ%7qypHpWo`nlSL;L9`Ql)q5GU5h;8woc@U~mN)2}E=yYIk8==9
AP7tR;UIEV_QxQMO-6|5YN)gD2vKUwG6vb}Mro-(ke-D8nBw%xY(h3RuV}DMCQXKubDjI7CNd0YvT^Fa>W~@(;=v+m9u*<?MP+fq
U_jETnJL)Wco!6=4P#v5Ysnuwzxh;)(5f%sgwB^81_%Y;r9t5Wr@Ju3J80}8yT|M~1EvaNm93V(?7z@W{&$Y2Svh*Y0-U_ajH1)Q
dJludpE?2pDBe)VD!Tq*bKxmSb|%F|d?Q9EgI#;j(;N-VWJ?rryf{5#Y<eJEfY?s>cL5Ac27^NEXf9AADQ9V|<yjv>t=>u>^J6|6
V*w6;3}3#H?B0MShQ6H!R{G_jiZN@CZHaBd^5o5iD#&!t?~~!fZxQ21w0^H~#~U=h758eGR%ORG7_?T}xomb0@+e}_(`I@7-Y^B0
mGmS}M(d}GcR}1{a!%d$IHL3<6fay9F{x`HkYQdWQg1dF^5BX1?f*)702GA;^EE5%j3p09r4HGKuxFqm%=jb+^~rI@KKARQS=TU-
I!34z<zD77aG_y!O(CAS9Y2EH^4ml(|LHb=uaf^I>~njFcn<${TUxws?yJ_UijT#=ArintWnqvT58-RZuD7kOWJ0g*9^X4k=brfu
Lxnc~g@WYb;hRV9^^mq4k;1u24c$h0N|Xh1qQ${c(Zgr^fAs^ou#QhmlYcJ~j~5;R$$4^yl;7P;6!|6dNbBPa3gPV4_S?)s$R7A0
T1z^cspv`Q#UybE(Q2!?LpoCevC1jh_Ps?LpD6|X(jJpN>8k)oD~_e`g1`#&>EXzW#w`nhL}w@kC+!`PzfYV><PN)#C=HLjZR5$V
K0#L1??EqtR#h0HwKbW#Y<C$>TXC_vx}?xkR7il-Hq)%uYq@0)oxBpIfDGp0!<FSuR!v7`D}12e>kZ5Hx^Ih=F;EUx4>q!7Oo}bF
WrVOPj2)ksl|nkPyNk<qu}RPWL|rKnN;}{T`Eu748DaSP=4T&X;g8$$e!jGXNtO4eGRpP1*VRn*o6MC#6R3#beae?&G>G8{+ryN}
f+H?K8TgPc@)#1&#!^37V;hYo3{gJ$j`+YlS{5{RnyEox6eILlnh;cS;q`O4uy%E}^_>%1IL6@}vx8WF3Pat0m?JuQK#kdkZSWQJ
56$2pNnxlBnXOsbVKbPXc3NU%MTiq88nI8dF}g&4NklpJy3OhxcKgs7p<UH#(1U${XLK~i>3dhyJ7Dk-bPvXmW74T{n|a_dM1S&&
8_^=@42{I|K_Vq^oq`&ZC;z){zFuXA(j2Cea!y1cQI`>j^Ff6iQA43lW@X>$l{)4pM%qAHNv-VO{6X6Nbn=IqcuYS}o>*%|vfrkb
p${&x^Pat*iaq*vcO&!tsU80Z))!(Uxu#h3UkDCf^K&f%EK%gHg=(yWY&rpvJmPGEIf1p)!NP6FCwOiGo3#jWq4&1HK03m`*mH|q
n`<<6dXb=~z9Jql`ljq}27fO7FSv#tmcV%I#@Rq{xp{@Z@wd@^C_F$%_OameCGP;1(n2;T{{?VNI1-AzUxbs3Fi2`-;lO(M5aHk-
@8U*@w`@APBrZ>@6AiFCYddH`$L{%@G&hAE>n1eMJLoeO)Y}il!T!k-t6Fyf@&?8pkt$5%Zl$`&3F>2*LSgG{m^hoxjH*lGdX_$>
CTy@b_51Dzm)DBrO&~F3u3rcn3rg@p!ac*lQ#&Kf{|?si`1q0|MDgqnBu~&F|LY9_`#8!VBN%<XxU9qSNC|ahv|i>S`s<p^9vA3u
DG*v%?3h&|e7cTLs*{~QHj%_`I+GHHJ<8O@5j3s)T-l4x*mb<@z2%z7A*klO>qo1329eGh0_9M~v986?Yt$ZT0ic+Cp^+pc0yVWO
;rS`ceoM9wPa16ok*&wD4J%Mn7iW$KYu|^PNda`E5W6Z0xLS{!Dbi>WY;-95n(4ULy;e_*z=ICd4S*OQ%Pz>8eHV9=bjOCsNNRHX
8+1^aaVDzZ!<`rxhXPkxnV`-pC%i{|(qi*4MFc_5Y*8`0XUn4HUl4T6-fUZ_3((P)yC_?=<3{1iWf_*-JzW4JbUl?0b~O$xl=!vD
5ZVK(D?2KpMW?yNmhZ+D8j{rvVrdo0qaqXd;|4LvJyi{7u`(PvIKPZrMGIrZP`C+-T+`1$FzDYlH#EiD*#kCf=OX;(Kh^As?pcL>
U1y}#GEEtqZde2Fy$}vA?BF`O_*kKdL8a)D;xRMGEW$eCzX0B(^V_6lzRO39;!8jBnQ(A|T-vJzXnvmNYO1zn#IxtW$M{RH6L^1B
(Ro&su%M%Ws8S|peSiz)=q5p=xqDIZ(jMD%Z{EUfQC*P*64O0Ep}i_2V$0cbOcQb*qMb+O+HB+VUk<8(?4yrRWDx>H`SlrFDOX-V
<<AD&x$?jO9s>;5v<>&Eci3+!KzxdL0NM}*>K>o<%MHWgp7Fb|qQhG)o~LgB!~(3Q_d@U%Wg#<7*<Y?lEI4<b76uT+O@kFvZ8Crg
PG^VnL<q57pLd)CP6@mUO0ogQ^y55FoXD?^tK~j5c3Ak+!dutYad=UQ$@;XJ(GB2O-7Z64t-8Wz!Ig!&!FAtJS7E5|=NnU1TYlxg
BrG>IVGePpc;Bk7WMc+@9)xc;i&mG1K@!!A+-BKBum!4m34~r$ftv*CJTTyXeaQIq0&z%~oX1x)Man&;Og%R11WjpLMMN0x4kQEg
+A7>`=#U-uT=vr`#hTJ*+AD3e9+Hp_8n;IMkQX#j$CsmlK6t-;T=>-gYSyZh`G4A>Jt6%Fu9u46>m`t;G)oOPT_Q($u6J$$C$^!U
D+WDuksAF$zLsPhV@fVlDpRgQ!SQY)ttP;l!g(Q3h>lOHj1%l}wQhf8Q)HDP&7-wXE>g=8ESofVlC|v!(lh~+Lg}h#FomjgUfV}!
aab!=E9@mwjNn)`j@GaQ-X~%J{*&6pVDQs)mPF^Fe1WsY^VU}PHs9H0f5+K2b^1drG&M$gdKm43E+xOd<0n>`G3185aN^{7PL~st
^%*Q7v?1T6=!0RXBw7oId2KI$x6Lv)HVuT+d|lM%oerps{nB6KC_^Bc#PEqA>4T$y=1)yPJmKY0$**=Ggd{7XYtN8tjqen@ab?YM
9G}L@+wzCEJh#j1L~p}xoi2KpaaoajG@<<U?8YsSxWc2okMOL@l9YI-4MM?})e<)M$9*Ktu%n1flAo5h2*tg*=_qko4=HKhuQG_a
Q3$KCmBZ8XEa!!ZI?=mpk|Va0Hpluy<}(k0-LmoS&}qNwUBAN+qY}4PGVxJplcz954d%`heXLO<$vkO<#cd^zg5JBLt^5KVQUtoH
`w$U)Zs<ckJaueZ?|!Jnr_`l;KxIN3`2{7BCQgX_C|aQ4O2sN%7e7NTcm2|QPzsFWyktJ0=byewt&;2|@HxdSUS2wA|CZZWs^ei+
!5*Gz?$(QXJ`)fVGN`USNsBhnrE_P!qSf!wG7N2Mo#~fg?pz&s>dxR?C!n;Lxeop?EFf2e53!RmiWJ5O_GU7K@5$dmC-++4+P%DG
J{1zQzencLg?yG42VT}C1gUx&fFj10lc$ViJNZZEeqQj@g5Bt3Civz)2=;c(W~XjO;&G?W9F;)?)n1)(t$3l6%23E-K)39nGrKGs
r`wM70W*=xv2y=jC(J)TH%{O;pDlr$d(IvBFEj@0Pd=9w4CXz4TE#*e5UcA(Bnr7V(OH@aRme`=UFVySzqgsVO7jQdXYy6OvmLtT
ZOYAB{m>tMVsMm6%XY`<w_FkQn(~o67ietuNAPQ9?F(v3Mw=u07#?CkpWQFawOR>uCXrU{2!%f}eNZ3t`ei$tz|KliWOErG9wd@q
^Jo{h-g*Wn_?x}_c3J!IKlFKqJseZAI~3~oAgH!MlE46OL5DJ(32AcAmfznT(WZd!A$mPt&#ZZY17Ffn11MSz2ibi#<n6<kAX{9#
j+1g)RTT4(yH{IFliea$Rq)T|+RGx)js$cbijX}`@e(}zqr135z)wOyH;&+#P2}DABtnI#v-X}hvOCr1%1fU@`^xKU;EHoSxE2>c
7{J5WRm8`3oGHSJS2au3&5|v0yi2Bmi|>c^ViBVRDV7EzVTyW^|De3NTmQ|9a$B29#s;Vk2Cz`@?4@(s9C@fYBOceNhR~_iH)5d=
Dq>{Itqtz|3@^B{7ol?Q{t;@p{)Oojaym3z-%F-@3S#viaf40XqYh-$uEfIe(L2#4Wo;`P8~i$0ud5ZaD_GzHr@PIjtB@4TCOo<C
F}=MoBoi{Ms>|AG#cDQ&4=ta~{_uQfwd_Lkw?s_@qNRnbk!~`jvVGPOgc2V*hUz|vrHWK7glx%sYl>Y0Gd`s$-15l>%9VWEug<rA
TX5zERs7E3kYYW?YMrk`t<1US6w=&b3-l9(Y%uyyaQ}Fg79Wmz%pEiN!NAF<DQ%4N{N5JgywINiQNbf91YKS$joeYsMWpW1X+dA4
Fws^&o_}0eABr}Yw=7CGsMbU6aM;@*EdnYCtk8b<)EO)8&v{9PzK0Ikx0cPrgv!;`LmjDx5THgfso{y!lA~p?^g!6^PG9kpL7%&s
@(ue5rN0(x4)BX)?>4(}bI&IyRnNza0RR%29S|FNzIZOQ<hCl}HP|Rg*0Q$e#h9mC@Vn}CMn2xKJ}y_)otH|`dSnk`qQwn!FeXK7
eQyn>OyuFou?%j6Cjz1CWIsz<kmBxgOT46s*S->9j5fe3r=W1zLf?PP{;ZEmG^R#w!apknIb(oW<m|qfnwnp1-THFl2CjLl`5k>)
5H6)GC<m5vV7i3e{0%wvW|7?pf$qFzz-jo0(p1#CnFWrrr9dZhU#!H}GTI`tjwXugM?FkiK8xNGC->46yYoeg)lXjt4`-0j;k8<I
)<rfNc9WQ!^5A_<y5o&~b{T9P#lI=WDZ-k}MNU~=UyWPgUJzP+<5F_LV?oCh%N)0H+h~wp9&(bV4~y{Yya($Dd(t1op<wAfDv$@7
?t|&{fP#XotbkMtJnhlSV~tog35&Oe9Q49&URNm%Q-|z56>Jj8PCJ?%WMcRTnA^qt-+~>8zMy=@*MqCWpyw;oT(?OL0UUgnTPp_P
NsckEMnwC`9hHa?Wm7Bjy7{D-8c9y58T9c^Af~KyI1H8@zqJtWP{QL?0hMh*+FT>P<RV>%Uo}OAf6c!YCj`_Abj1a4reDLHIT`W1
*NuwZted2VY5l*g{PJ_CMC^r2a7vehlPI~j4Xi>tEC`wT0{K^nVuI_RCyRXop9zN7l*!YZY(0Aw=HQVEch7geQ!$ua-78yjDeaJI
J2`tQ?@*=9>LL~JRbbZkU-M$QKro#GyiAazA-L+=?--nJVxG{d^jrQ`P%ra}O#1sK$8jRqq9k9YTkk3jhhO$qIIQsFB(tz>gt&Oo
yC!4|7d*P*3?3Yr<gCP|D?`519F2(y%c`>1eInOMFQy;`I<l=N)}%8>`rAcWr*I2v<1B2ac2M8>HiHkxj@c<N3<`gA-Bn3v@-*+i
_Pw&dcJus)C@Xmfp$crUyMYd<^0(vZ=;goMB(_42eG8C3+?dL!xA<wk?BgQNeekt$$dSbcIR7*#{1Z#Fk?1~2c_e4YU<n(p6D$dw
Yei+2wC+hqA{1qL)Hj3pBYC|XV9y21M)}A)JVIB2`{|H9Q3Y)nIhUu5u~=pzokP|F>q=5(`dKZNkK!ZTT3MqMyCv9gb&FhuT-#kv
O$gyfZ3x&h03PUY2U@|@?yS-jyjp?GYzj;Ckg$~$VNIUKD}`i#>;#7I4i+JkR4Q8S!6!Jp>=F0da=}<Tc9A;Q8EfJyh{LdCjAjh_
;q|d}bd^^Y;VRcXGB&+wn~iQTxFoHriP2>~`=cOgU?sx97qtm3LsuF>5CmR7e)<NIGB)A8Oe_Ezc}|7+Rh(d;I|9fL=OAHsFNP8;
y9YHktIx!U&21}Y?8bR0Jvhcg-<`X#I0BH-_f?muvt{dlo5{XYO562#>XswY;?32yq0`-ejzyvu%cCpK=6Mr;Uqx6}V?0TN!9G2y
MKgCAY!J!lTd>@4nzu8?LY4J^_S0{%+YL3?iTQn$1vL|fvU2?&y6o(ltQ8AR(Jb%#y>8lGc|vAiAy_nU+upjo*v-SK$s`-x2)cxU
DHa)El~#K95k9E@40`q<0bhZGZ%d8ti9vEJYA18?1Y{_io*G*oUWX#~S&~P&ZF%s>FcvG?QGtUk1_bj_oJKTp9M_e=KGA``{hY2p
we&?t87f{endW0JTfyG~ztlSAIdK+JKM+S^8Pnv&xLst3PXCpPc}gDg6187q?P7Do4YEy*5BZ%sLO_H6dDAVuMAF27Q>Z&okSV7m
E}zra#hL4*wsnkAgj&*0H|2{*5_qVB6F0~~apIbf>?Hmo3()VWpcsm|+&!UBV<b!*dk>@9hE&+wmADxMPDn8E5WUC<>O*qPEcGJ~
Q$98b^BZ=?Z~K0Jz|ioreaN<*3MHxg4vyKQ$G3IjSz-Q;*OQzu>YBH?n!L!|$wWEC>ios<Y_gH!ZbrSoDbqRZ{Iwd~AEzo$)M4}j
(pk1HrQhwspLd%viqlt(TxYGUg$og4A$egwd2Vr{tYj9|tu07)5JG{pt8&MIr6&+K+o+2z8mKH-6$5UKDz`vIC4BS&Kbkh%R*#dC
AaB)Tkml>n{hEG^-{<SIKt0&UQ-}4B%P@8#%QISXCDVaiv_%!_Qv>_#B#?CqR7^AjLiub}nP@>%wn}`#xzT@qC2xpB<Kd)W2z%Ue
3pq9oC-?2M!tDlUv<fX>D6p?>Q4wa%OAj(H9^!V|g>HE+5rL%NNXA{NR`LMGhdy7W1>J99Jmaw}@S6H0`9kntU@|2+txnSY-#{U|
igwPeo%IbFJ~1C=9*X`n$ED{LgRtD?aKj+~lIly?VO&+vD-1Z><Ut#?E$Q}N^C!xr4i0t_o?m?4F4-wky2pjzIj+@1VKcQx90_?k
hmxY%W{JIVH)j4+&CJk%s@9a#-DQDk3h|sPi&5$=Tt=<`gtLQtgacb#|4fT{_pDy(T`q@=-KBll<DYm-$u<k*@ibWC5Ccshee<1?
S?1H3f>u4=u?P-@YF+KOB{L_9?mG{d!Jr8R7-O3QMnd1OFrj1OQxvmj9l!e4@N8F<$Z4?_!W|`8*1Nq13>Sn#$ymI>7lAm&X^-kA
$;-YCyCBv3T>{r8ymGlWfQu_v!qVu>=v?zyE{1@0ni*7HL~X3;(5r~>uCOc<y04eoO!m)muTcO`xH7RMh`g_b^Bu%g-C5ftxIQ{}
4wX=><pLO))SF`AOjrh%gjEz^yI@U%P?lx!>>+N)!jGc@lGuk4$vG9kKk@3Z+q?|GPMiDpOs`j~zV_DmQnIH=M8U+V`$${PBNLGZ
=%LmGEg_bWi{`+0LF!h`ns&XA4+Dw|4@=`>W3}3}>Dl<1`k|MG^r!ok#h{NvGch1o$XAXO@1>&QvA>X3N<{#I=&UQ1E>Oky0a>a-
B-M7^Agj-u1+7q)PQ7qnfUcd$;8&lZMR6a9_%NYo(J%l|esl;)QwhWhB`ZV%l+u%*2F%6oi_ljj81P!64%ebqj0o{DOhC3VnNY8V
0ue)h_e9Z7bsK09<w@V=0;iXr@>p1(1_>2k5Z9vR+BReLC9!7XuLR;4@zxT>ssL0(Xrv#NeN}MqIPZRpM@q-H%11D_Vl6&39#{Xv
<H#FwZ6oXf+6~aRDeD7B<f=10RFgREC@Qmzr|96MzixLzu79KGOnAt2C;bVvawmYNkZ&MJvwIT=2-@SL=sT-|wvM)@QGe~DTkq7l
lNjeMb>vhg=|72$k)$F6Je1r*FlRQ7Xw?Oqo`xy`_jPN;+Iy+kR#+<R>AMD?RG+!>4B0SUuLSQE98YL9wNzBnt1??%3AW|J;VCC#
RilFiZcNXU3x~WabdMoWRs}g10ug|JHJ%xhf<JJ-8yBHu#)?f+0u&~S!)i_guT!OgbzQ;L(o10#fC>Nu1@1@pBvgW&<uI6$JmvdV
LNSDLU6+IxtfOWx!PGkTd?YvWYs&n$M#9d$tX5p<X~IEM_<9372>-i2-WxWFOx$-0y8`Bv2>6OboNkLwUSWeXh2GChGQ5st?raj|
{H(6ceofRyq}!h#XXeH_-A->@@Bz`aB0+WeMYIhA^53)b^fA21$J~Om4Q?1ys3cXb{HyRJ*jwZBBRnEeHj_BNo=7CW)ih+u0O2va
v?x08*i6|_RwT|3{zL@%MnIepk-}QePoo7uM78Lg25}9g{yJBV%nG9av=`Z9lxMI-5zMs?lY`DYd^YR4e(TqH^C4bf3K8rU-bPhG
h)k6H6N$%VN8R%PEt7SIh@Y(Lty{Mn@^ZXdb(`w4ODFR8XITV*<F;M>?E(hQV8&o;2RGZJcD#xH%g?j>6KubZh+N}5*fwJT`+?+?
OiE)ETvDpzL~J~P`MA=sFU5o(Hp&I;@Cb-FXaV!|HFak)rN$GeSo0p1ShB3N=5E2|h5zaD)CDAo32cPiKcoA}q#>Iz`Di@K+?W+M
h^f{j59DKHibFjJqvA(6+0e#c05?zYQH7oy2FXIFGUPteYHyR6&A7e0H`5>4F3Ny;454_ig7*Bam<<6!k6>Zn@S?U%jKaxi8oaQi
BJGK4s^$-1=k8TM!dr2p$m8+5=?Ya|a9k}AUEriXSqBP9Izp4L)Oj~>XuEQ2sO1Lz4zcrMWa%JEBMn17mvoHGCOx{@?7p@GjBl65
H450LUV3r{)M-dW{fkZpF8QW^ptKI?zNrY@o5iADrQ$=eYtE|~$Vd2|K1Asw(buFuqVKJDnK<dg0r)Eo{Xmzkg}ES%^T645uiMT*
VB{L<^MdbXi%-Noj>&G4EB1SImTB7s1{l3kz?yN0?Ehe7)Qv*fVVvW4*$oNK%BEn!i?Yl&s|lN{%Z^kzI!{5XiQ35Yx5NqGRhmrs
^p7{iuESx19urXU=z{Z+_2=WR>>AB)2k!U0QU{u(nRYOn3s&%}m2FQP*~M0M$K%jDjHL!pArOk(y+ra5xLrXuP3kwO_%qpydR7av
7KVNVJy2TmcgM3Zz)lPqkySjBxbI%DxTZ%CA2lo5Nr*_O5E!i#vpHm=&PXKz(rb+yl3StH88Qs<$-&e1BbIWXlTQ{WrW_`|pNIOm
))FgsewzN#prS1kD|mUUt86TrqUvo328c3l>@uBpocqCPfq7k!v9NfdBVMoPNpy8-pclhNe(c8W?^C32P24#XPJ#tt^*tu;+%)n?
v1(W-j-Rk^gGwU6`+ggTZKtEW?RUdt(K-Pnl+~`IVBKk_O{GrJ*h2!THlwT;D==k)>616y3G?-G)&s+pX04*QJqbj^{L|VR=lCLQ
wjW)_r=9RsQ-Y@!_U6GS>_@nmG9(a7-0XAGK&Cm@Uz{>zFM;(p_TQEpcy6sl>tXw3q*`D|ca~8#`-8SlNc#`{&PbVm+g|fb%|$dE
kS=S6D!D<rDW6Rn@D75&2$I_^OT1}7Ri2RATV`;7e8L9<3j!bRq@c}DO2N`Q3_7a9g0bh+jX6puA9oiKH)8<+bKJq1uUJ8bvEZnG
a>HcF?nA+(ce}A(d{OqE76j?f*}pMaeo&NmXjsW;K=2JiBGz<p6_>%fHG#!xxXm>myHLlPA|mF|L=;-N`C`JefaIZL2Q#LK6Bh=I
KnZ(W+k-Dv5-+RD)sEQis!BReEcS+SqYe?97^hMhhYdd$+?M7K!AV})J(=-|0^T_+SZll@+JoGZ^dc642p&{!7<DMcWg>4P)k||x
$4g7vZ9iTPqoa6h@18N0?D^Uke^n|a_<^e1j^WhLQ>A$Oe+)cU`%K*`>bJ9dExUz>`znlK%Uiuue)dP`6b#eN%+HI}Nb&--!E8m`
hPbM@9y(?y*i@p(o=BXzJ3m2=c5B7A!y0Ej*B10+h%EN|a>3oDkEELB-cRRuImiE>cvo4wfuBa;f`7}bTg0ky!?+l1fw!>c*X!@m
cx8h6{%Pi3UD;w@X(jBuOXoKQ?Y4%&4iAv>ZJDtp2^7_%+`h#J>KvYRc&R{Aq!`7xy0BY`#cBJTDYl(u;GJh#9-cu;d)w3u54d5G
oz;nT5Q-wgv2#mFET`Zb^LPD5+jrZsRJemtICE+27yBAgY*rz1&o}GyqHQ#q08P}vB0JiGwFpiGJX#$TikR7d=1`Pr^_x!HuJ}NX
R@NheWeQf>@(my6$b`P`F2{2kf_v3y>J3v}-{J|q&U1~GcEz&t*P2#P>0Xh2iM=zuDTjI8vRHT`_m;hUgoq&zOj9AXj0<?PDe+y%
D_V>U9Z?dF)p6&fS?~8i7G3W6g;VZjc%>i@`!0J7Bwf3)eTr<+K7rGK@f^0jzT|pKwChJOlxjwhg+Fo?BRZb5g-0hAzFto0O*bVs
Mu)v->%<c!r)^n-99w;1G2rr@`%;MgkNq*X0}Pl$=u7?%1Xma0e$dL?hK-xxViyN5s6)ThZ>I7pmZ2xE^edv&*G%H^yjV?~SDQCB
;*mW_GIB$H;FVmQa_%@b3(JBj!R!@f02115rM)qeoKNv;3&a2*&K=}{VQcSQNodc;+qMqUe;ogt%dswCnRr9WO$Rm)-s)$raY61D
9r-<lLJ?}}%~s(olP<UFu`1x`@I?%fcxZgfT0cbLruhMC9v>yX9(k)g<7^n;j_QI{PoAiHCVRyh24!7VmG1F4!z6QNsbAewH$jZ$
ORnCk-3f%S2zD)Y_<fd7{h%HL8-`1|`CH>Y%#y0K_Tfq8FrGk{W|Dq~uDPvu{Y$B>*gZ%B00000!1|W$)E(ko00Fhb0mQik0Zf-W
vBYQl0ssI200dcD
"""
SIZE=72900
SHA='1a563f4b3b378ef99c767fb5bf09744423340528c3fc9b05c5b8297d191e8dd4'
def main():
 raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
 assert len(raw)==SIZE and hashlib.sha256(raw).hexdigest()==SHA
 files=json.loads(raw);manifest=json.loads(files['MANIFEST76.json'])
 out=Path(sys.argv[1]if len(sys.argv)>1 else'METRIC76_SOURCE');out.mkdir(parents=True,exist_ok=True)
 for name,text in sorted(files.items()):
  assert Path(name).name==name and name not in('.', '..')
  b=text.encode('utf-8')
  if name in manifest:
   r=manifest[name];assert len(b)==r['bytes']and hashlib.sha256(b).hexdigest()==r['sha256']
  (out/name).write_bytes(b)
 print('METRIC76_SOURCE_RECOVERY_PASS',len(files),len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__':main()
```
