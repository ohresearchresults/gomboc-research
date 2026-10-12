# minimum-0009

AI research report · 2026-09-07 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# RAVEN_C30_CONE_FRONTIER_V1

## Determination

**C30 is not excluded.** This continuation gives a completely enumerated, substantially smaller necessary frontier and a rigorous boundary for the dimension-independent cone relaxation.

Of the inherited **1,994,223** surviving complementary tree-pair branches, **1,816,092 are now excluded** and **178,131 remain**. The exclusion proportion is 91.0676489% of these labeled branches, not of geometric realizations. Exactly **three complete joint stable-facet/unstable-vertex root-pair orbits** are closed. All **74 graph types** still have survivors, and **4,369 of 4,372 root-pair orbits** remain. The canonical bound is unchanged: **30 ≤ C_min ≤ 1374**. No homogeneous C30 realization, entire graph exclusion, F≥9 theorem, or C≥32 theorem is claimed.

The new proof uses **367 reusable rational shifted-positive-definite matrices**, plus two inherited four-deep matrices independently checked here. It allows different valid triangulations of nonsimplicial facets while retaining **one common separating direction for the entire actual root-volume cone**. The recovered predecessor's three individual graph0 branches are also excluded by the new predicate; they are not the three whole root-pair orbits reported below. The predecessor explicitly distinguished its three branches from whole root or graph closures. :contentReference[oaicite:0]{index=0}

A second exact result prevents overinterpreting the remaining search: a labeled graph3 rank-two configuration satisfies **all 104 combinations of apex and nonincident-facet triangulations**, with strictly positive exact independent cone weights. A rank-three lift satisfies all nine fixed-fan apex systems but violates a required maximal-facet coplanarity. These are relaxation controls, not actual homogeneous bodies.

## 1. Exact coverage

The counting convention is inherited unchanged: a representative of each joint root-pair orbit is fixed, but tree-pair equivalence under its stabilizer is not factored out. The original complete catalogue and its necessary filters are the source of the initial 1,994,223 count. :contentReference[oaicite:1]{index=1}

| Unit | Before this screen | Excluded | Remaining |
|---|---:|---:|---:|
| Unrooted face lattices | 74 | 0 | 74 |
| Joint root-pair orbits | 4,372 | 3 | 4,369 |
| Selected complementary tree pairs | 1,994,223 | 1,816,092 | 178,131 |
| Distinct labeled primal `(root,parent)` cases, counted separately in each graph | 513,962 | 467,456 | 46,506 |

The three completely closed joint root-pair orbits are:

| Graph index | Canonical dual mask | Stable facet s | Unstable vertex u | Previously surviving pairs, now all excluded |
|---:|---:|---:|---:|---:|
| 5 | 5675518 | 1 | 7 | 390 |
| 23 | 6215917 | 2 | 5 | 488 |
| 48 | 14858559 | 7 | 6 | 424 |

Facet and vertex labels are zero-based. Their complete ordered primal maximal-facet cycles are:

```text
graph5:
(0,3,2,1,4,5); (4,8,7,6); (0,5,6,7); (1,2,7,8);
(2,3,7); (0,7,3); (1,8,4); (4,6,5)

graph23:
(0,3,1,2,4); (0,4,6,5); (2,7,5,6); (1,3,5,8);
(1,8,7,2); (5,7,8); (0,5,3); (2,6,4)

graph48:
(0,2,1,4,3,5); (0,5,6,7); (1,2,8,6); (0,7,8,2);
(3,4,6); (1,6,4); (3,6,5); (6,8,7)
```

These exclusions cover every Euclidean realization with the stated joint equilibrium roots, not just a selected numerical metric. They do not exclude the same unstable vertex with every possible stable facet.

Every unresolved branch is regenerated, without truncation, in `raven_remaining.bin`. Each record is exactly five bytes, Python format `<BBBH`: `(graph_index, stable_facet, unstable_vertex, dual_tree_mask)`. The last field selects seven of the fifteen ordered `Q_edges` in the pinned catalogue. Its complement selects the eight corresponding `P_edges`; both parent arrays are reconstructed by traversal toward their respective roots. The file has **178,131 distinct records**, **890,655 bytes**, SHA-256 **5d3329d312adf3db48d9e22314d6cec046f4ec9b00b29fe248fa96f699bb3f1f**. The full per-root counts, including every unresolved case, are regenerated in `raven_counts.json`.

## 2. Actual-volume exclusion theorem

Let P be an actual full-dimensional convex 3-polytope of the indicated face lattice, with its ordinary uniform-volume centroid at 0. Let u be its sole unstable vertex, and select a true-edge escape parent at every other vertex. Put

`D_i = v_i · (v_parent(i) − v_i) ≥ 0`.

Distinctness gives `|v_parent(i)|²−|v_i|² = 2D_i+|v_parent(i)−v_i|² > 0`, so all parent paths terminate at u. Weak shadows suffice for the exclusion.

Choose a genuine triangulation of each actual maximal facet not containing u. Coning these triangles from u partitions P into positive-volume tetrahedra. Their **actual normalized tetrahedral volumes**, not freely selected weights, satisfy

`Σ_T w_T (v_u + Σ_(i∈T) v_i) = 4g(P) = 0`,
`w_T > 0`, `Σ_T w_T = 1`.

This includes nonsimplicial facets; their triangulation diagonals never become escape-tree edges. It is exactly the physical cone identity supplied by the parents. :contentReference[oaicite:2]{index=2}

It therefore suffices to exhibit one vector d for which every triangle in one such complete triangulation has

`d · (v_u + Σ_(i∈T) v_i) > 0`.

The certificate family tests d equal to the root, its sole child when it has one, or `v_u+t v_c` for a root child c and `t∈{1/4,1,4,16}`. Different triangles may use different shadow multipliers, but **d is never changed between triangles or facets**.

### 2.1 Elementary positive triangles

For depth d from a tree root r, the projection-chain estimate is

`−v_r·v_i ≤ cos(π/(d+1))^(d+1) |v_r|²`

when the left side is positive. The following rational upper numerators, divided by 256, suffice for depths 0 through 8:

`B = (0,0,32,64,89,108,128,144,160)`.

Thus a triple with `Σ B_depth < 256` has positive root-plus-triple projection.

At depths 2,3,4,5 the bounds are respectively `1/8,1/4,(11+5√5)/64<89/256,27/64`. For depths 6,7,8, use `log cos x ≤ −x²/2`, `π>157/50`, and the exact finite exponential lower sums proving `exp(7/10)>2`, `exp(3/5)>16/9`, `exp(1/2)>8/5`. The executable checks the rational inequalities, including the Machin arctangent lower bound for π.

A second elementary rule accepts a triple whose ancestor closure has at most four nodes at depth at least two. The parent four-deep lemma gives `v_r·Σ_T v_i > −15|v_r|²/16`. Its only exceptional patterns beyond individual depth bounds are the six-node chain marked at depths 3,4,5 and the fork marked at depths 3,4,4. The two integer matrices in the recovery source, divided by 80, are exactly

`15|v_r|²/16 + v_r·Σ_T v_i − Σ λ_i D_i`.

Their positive leading principal determinants are, respectively,

`(75,5504,333632,15370240,434778112,56623104)` and
`(75,5504,333632,9116672,817229824,5266866176)`.

The program verifies both identities and positive definiteness independently. Every other four-deep pattern is bounded by `229/256`, `217/256`, `210/256`, or `3/4`. This is the inherited lemma, not a new claim that arbitrary shallow trees cover the remaining domain. :contentReference[oaicite:3]{index=3}

### 2.2 New reusable exact matrices

Prune a rooted tree to the root, the marked triangle, their ancestors, and, when needed, the distinguished root child. Canonically encode a node by `b[sorted_child_encodings]`, where bit 1 of b marks membership in the triangle and bit 2 marks the distinguished child. Preorder parses the resulting key into a complete parent array. There is no missing graph-specific labeling table.

For each key, let `w=e_root+Σ_(i∈T)e_i`, and let `C=e_root`, or `C=e_root+t e_child`. Define S_i by

`xᵀS_i x = x_i x_parent(i) − x_i²`.

Every literal checkpoint row reconstructs the exact matrix identity

`Q_T = (Cwᵀ+wCᵀ)/2 − Σ_i λ_Ti S_i`,

or equivalently

`xᵀQ_Tx = (C·x)(x_root+Σ_(i∈T)x_i) − Σ_i λ_Ti(x_i x_parent(i)−x_i²)`.

The checkpoint contains **56 root-direction rows** and **311 endpoint rows for 156 root-plus-child keys**. Every multiplier has denominator 1000; the smallest is **501/1000**. All are positive. Exactly **363** matrices satisfy `Q_T−I/1024 ≻ 0`; the other **4** satisfy `Q_T−I/1048576 ≻ 0`.

The verifier reconstructs the matrices and, separately, their polynomial coefficients. It then checks rational Schur/LDL pivots and integer Bareiss leading principal determinants after common-denominator clearing. It does not accept numerical eigenvalues as proof. Summing the verified scalar identity over physical coordinates gives

`d·(v_root+Σ_T v_i) > μ Σ_retained |v_i|² + Σ_i λ_Ti D_i > 0`.

The retained root is nonzero, so pruning cannot remove strictness.

Where a key has two certified endpoint values t0≤t1, convex interpolation of C, λ, and Q certifies every t between them, with shift at least the smaller endpoint shift. The screen only uses the four stated grid values. Endpoint order is checked exactly.

When the root has a sole child r, every triangle vertex in the original root cone belongs to r's subtree, and

`v_r·(v_u+Σ_T v_i) = D_r + |v_r|² + v_r·Σ_T v_i`.

The same subtree certificates therefore apply. If r belongs to T, the other two vertices have strictly smaller norm than r, directly giving strict positivity.

### 2.3 Nonsimplicial facets and complete enumeration

For each fixed direction d, a polygon-interval dynamic program tests every admissible diagonal split and returns a full triangulation precisely when all its triangles have positive certificates. Each actual nonincident maximal facet must admit such a triangulation using the **same d**. This is existential selection of a valid physical integration triangulation, not replacement of a face by independently chosen triples.

The copied, hash-pinned `e15_graphs.py` regenerates the entire catalogue from the tetrahedral sphere. It enumerates all one-, two-, and three-triangle disk replacements, obtaining the 1,2,5,14 maximal planar types at 5,6,7,8 dual vertices, then all allowed edge deletions, obtaining 38,76,74 types at 17,16,15 edges. A minimum-degree-3/4/5 deletion argument supplies completeness of the maximal-sphere step; triangulating every target polygonal face without new vertices supplies completeness of edge deletion. The program checks sphere links, opposite edge uses, facet intersections, Euler, and connectivity after deletion of up to two vertices. It explicitly enumerates all graph automorphisms, all root-pair orbits and all dual spanning trees. :contentReference[oaicite:4]{index=4}

The inherited filters reject dual height≤4 trees and height-5 trees with a sole root child, and the stated primal four-deep cases. Every other pair is subjected to the new exact predicate. The journal's proved slope-matching theorem supplies existential completeness of complementary sign-compatible trees on an actual strict110 body; no fixed matching is silently imposed. :contentReference[oaicite:5]{index=5}

Consequently every actual C30 candidate must have at least one record in the new 178,131-record remainder. Zero remaining records at one joint root-pair representative proves exclusion of its entire orbit.

## 3. Exact barriers: more independent apex cones do not suffice

### 3.1 All apices and all triangulations in rank two

Use graph3, canonical dual mask 5675263, with ordered abstract primal facets

```text
(0,5,2,3,4,1,6); (0,6,8,7); (1,4,7,8); (2,5,7);
(2,7,3); (3,7,4); (0,7,5); (1,8,6).
```

Its primal root is 6 and parent array is

`(6,8,3,4,1,7,−1,2,6)`.

The complementary dual tree rooted at proposed stable label 3 has parents

`(3,6,1,−1,5,2,0,0)`.

The latter passes the inherited reflection tree-shape filter. **No realization of dual poles or dual shadow inequalities is asserted.** The exact unresolved record is `(graph,s,u,mask)=(3,3,6,17892)`.

Assign the following integer planar rows, divided by 1000, to labels `(6,8,1,4,3,2,7,5,0)` in that order:

```text
(1000,0), (517,499), (151,591), (-153,496), (-331,295),
(-376,79), (-344,-71), (-256,-189), (445,-496).
```

All nine points are vertices of their planar convex hull. Their minimum selected primal shadow is exactly **9/62500**. For every apex a and every complete triangulation of all abstract nonincident facets, 0 lies strictly inside the planar convex hull of `v_a+v_i+v_j+v_k`. The numbers of triangulation combinations at apices 0 through 8 are

`(2,2,4,4,2,4,2,42,42)`, totaling **104**.

Using integer, unscaled barycenter-sum coordinates, the corresponding minimum oriented boundary guards are

`(209663,137765,741502,487162,268348,294631,1959,1959,2847)`.

All 104 systems also receive explicitly reconstructed **strictly positive rational weights**. The deterministic rule assigns ε=1/10^9 to every triangle, enumerates triples of cone points lexicographically, solves the remaining affine system exactly, and uses the first nonnegative solution. The complete exact weights, not only hull guards, are emitted in the report.

This is a genuine feasible control for the **dimension-independent, independent-weight incidence-cone relaxation**, even after adding every apex and every triangulation. It blocks a universal exclusion using only those conditions. It has zero 3D volume and does not realize the stated facets as a convex 3-polytope.

### 3.2 Rank three alone does not repair the fixed-fan relaxation

Let Y be the preceding integer planar array in graph-label order. Set

`Z=(71,311,573,−39,468,704,0,−999,0)`

and take

`v_i=(1000Y_ix,1000Y_iy,Z_i)/10^6`.

The vectors have rank three, strict selected shadows with minimum **35912331/250000000000**, and strictly positive exact cone weights at all nine apices when each polygon uses the fan from its first displayed vertex. Exact weights are again regenerated, now by lexicographic four-point affine solves.

But the purported heptagonal facet 0 is not planar. In integer coordinates the determinant of differences from vertex0 to vertices5,2,3 is **46742535000000**, hence the physical determinant is that numerator divided by 10^18 and is nonzero. Thus this control establishes only the boundary of the rank-three **fixed-fan** relaxation. It does not establish rank-three feasibility for all 104 triangulations together, full facet incidence, a shared primal/dual metric, or physical volume compatibility.

### 3.3 The additional information that is actually missing

Fix one global triangulation of the actual boundary of an actual centered P, and write q_f for its physical facet poles, so `q_f·v_i=1` exactly on facet f. Let

`ω_t=Vol(conv(0,T_t))/Vol(P)`.

For every actual apex a, extending zero weights to incident facets, physical geometry forces the **same** weights and poles to satisfy

`w_(a,t)=ω_t(1−q_f(t)·v_a)`.

This follows because tetrahedral volume is base area times apex-to-plane distance divided by three. The normalizing total is the same Vol(P) at every apex. In particular, for any two apices a,b,

`w_(a,t)(1−q_f(t)·v_b)=w_(b,t)(1−q_f(t)·v_a)`.

Moreover, actual surface integration gives

`Σω_t=1`, `Σω_t q_f(t)=0`, `Σω_t σ_t q_f(t)ᵀ=I`, `Σω_t σ_t=0`,

where `σ_t=Σ_(i∈T_t)v_i`; the last identity is precisely ordinary volume centering. The matrix identity is the divergence theorem applied componentwise. These coupled identities are necessary, though treating all displayed ω as free numbers still requires the appropriate area/volume compatibility to obtain sufficiency.

In fact, expanding the common-weight apex sum gives

`Σ_t ω_t(1−q_f(t)·v_a)(v_a+σ_t)=v_a+Σω_tσ_t−Iv_a=Σω_tσ_t`.

Thus, once the common physical structure is retained, the apex identities express the same first moment. The substantive multi-apex information is **compatibility of the weights and geometry**, not additional independent copies of a convex-hull condition.

The controls above deliberately do not enforce this common physical structure. The productive continuation is therefore a certificate on the exact remainder incorporating genuine facet coplanarity/support incidence, shared apex-volume ratios or determinant volumes, or compatible primal/dual pole geometry. Merely adding further independent apex-containment tests is blocked by the rank-two control.

## 4. Recovery, execution, and provenance

### Parent identities

The supplied conceptual parents are:


[Encoded source block omitted; the code in this passage is incomplete.]


Their roles remain distinct: actual V≥9, reflection-based F≥8, and the actual-volume/four-deep foundation. No polar-centroid substitution is used. :contentReference[oaicite:6]{index=6}

The supplied full journal used here has 2,150,394 bytes and SHA-256 `9f7e61c88422983e3dc838bf7202cd18208c5dcc0a32ec58b60490748ffb3502`. There is a provenance discrepancy worth preserving: the extracted rendered parent bodies do not reproduce the supplied envelope hashes. The V9, Atlas and earlier Nova rendered bodies have respectively `(41815,b94dcc8efa2f91899075ea5d407774c63f7e3196aa7efc1a741764e838ec765b)`, `(31797,f9def19362115c4dbb967b99d637ab212d7309d8d911285351745d22a471f6b5)`, and `(31127,821e3cb40fc6b537dd147dded82b8faebd04684a9e76458cf1f193526b550229)`. I do not infer different mathematical parents from these rendered-byte differences. The exact embedded capsule source hashes actually used in the computation do match, and the complete graph catalogue reproduces its advertised bytes. No mathematical alias/incidence conflict was found.

### Executed checks

The numerical locator used CPython3.13.5, NumPy2.3.5 and SciPy1.17.0, with `OPENBLAS_NUM_THREADS=1`. It optimizes all eigenvalue inequalities with SLSQP, maximum250 iterations, `ftol=1e-10`, nonnegative λ bounded by100 for root-only and1000 for root-plus-child; initial λ is `1+t`, initial δ is `−2−4t`. It tries rational denominators 1000,10^6,10^9 and shifts 1/1024,1/1048576,1/1073741824, accepting only an exact positive-definiteness check. The final literal checkpoint uses only denominator1000 and the first two shifts. A fresh optional replay exactified all367 endpoint inputs. Floating replay coefficients and solver tie choices are not the durable checkpoint.

The authoritative reconstruction and exhaustive verification use **CPython3.13.5 standard library only**, assertions enabled. A clean-directory decode followed by catalogue regeneration, both sweep ranges, exact matrix checks, the join, and both controls reproduced all deterministic hashes below. The optional numerical replay is not needed for any exclusion.

Save the following complete stream as `raven_capsule.b85`, discarding ASCII whitespace. It is **20550 bytes**, SHA-256 **f3fa7774ce124b35b8358211437a1495447fc413be9eda8e2586d2353cf8209e**. It is base85 of an XZ/LZMA stream produced with preset6. The decompressed JSON source bundle is **65756 bytes**, SHA-256 **673877e4fb7b06ff8abc907055f90b7f7efa1538bd8ca8555cff5bf8b3004ce2**.

Save this complete decoder as `unpack_raven.py`:

```python
from pathlib import Path
import base64, lzma, json, hashlib
b = b''.join(Path('raven_capsule.b85').read_bytes().split())
assert len(b) == 20550
assert hashlib.sha256(b).hexdigest() == 'f3fa7774ce124b35b8358211437a1495447fc413be9eda8e2586d2353cf8209e'
s = lzma.decompress(base64.b85decode(b))
assert len(s) == 65756
assert hashlib.sha256(s).hexdigest() == '673877e4fb7b06ff8abc907055f90b7f7efa1538bd8ca8555cff5bf8b3004ce2'
files = json.loads(s)
assert set(files) == {'e15_graphs.py', 'raven_frontier.py', 'raven_controls.py', 'raven_locator.py', 'raven_tables.json'}
for name, text in files.items():
    Path(name).write_bytes(text.encode('utf-8'))
print('RAVEN_CAPSULE_DECODE_PASS')
```

Run:

```sh
python -S unpack_raven.py
python -S e15_graphs.py
python -S raven_frontier.py verify
python -S raven_frontier.py sweep 0 40
python -S raven_frontier.py sweep 40 74
python -S raven_frontier.py join
python -S raven_controls.py
# Optional, with the numerical dependencies stated above:
OPENBLAS_NUM_THREADS=1 python raven_locator.py
```

The five recovered source/checkpoint files are:

```text
e15_graphs.py 9750 b8ad1bc65302aeb46a818031c45854135edf15ac1586ef5a4fec2fbc90061199
raven_frontier.py 9945 c57be0041656ff31c04d301763a606105d71ad9554817862994bf71614f39708
raven_controls.py 5378 8f8fa51c5c34b347aeb35bda95dfedfe72bf8c1cf0fffc512b78453e05fd5841
raven_locator.py 2718 e9f4c6c0938a9ff6b85fb05435145126b266df707dd47b58534dc432e87585f0
raven_tables.json 32592 981268e6175b21de54ef96e4e5100af11c11001a5650b8a130cd8054ea7d19f5
```

Expected deterministic outputs, stated as filename, byte count, SHA-256:

```text
e15_frontier.json 106553 9b7354d49fa9fb07ede494140fc0cde9a06f994f0359cb0a26b6ee3e8debe833
raven_counts.json 61070 ef01153db5e3c26c8fa81473f3dba6ca501899f3e91a7e99914f5c05f218edf8
raven_remaining.bin 890655 5d3329d312adf3db48d9e22314d6cec046f4ec9b00b29fe248fa96f699bb3f1f
raven_pd_ledger.json 221916 820a07f172516f60b88e1d2bda9b078a29eb23fd1f3bc858680953cae522d297
raven_controls.json 27203 5d65cc903b13171c95c78259123ee596dba4f8398ba55a4c189ee8af33e3acaa
```

Observed terminal markers:

```text
ROOT_PAIRS 4372 WITH_NECESSARY_TREES 4372 TREE_PAIRS 1994223
E15_GRAPH_AND_NECESSARY_TREE_FRONTIER_PASS
ALL_367_SHIFTED_PD_IDENTITIES_AND_TWO_FOUR_DEEP_MATRICES_PASS
SWEEP_PASS 0 40 97118
SWEEP_PASS 40 74 81013
ALL_74_GRAPHS_4372_ROOT_PAIRS_EXHAUSTIVELY_SCREENED_PASS
EXCLUDED 1816092 REMAINING 178131 CLOSED_ROOT_PAIR_ORBITS 3 CLOSED_GRAPHS 0
RAVEN_C30_CONE_FRONTIER_RECOVERY_PASS
ALL_104_ALL_APEX_ALL_TRIANGULATION_PLANAR_CONES_PASS
ALL_9_RANK3_FIXED_FAN_CONES_PASS
ACTUAL_MAXIMAL_FACET_COPLANARITY_FAILS_AS_REQUIRED 46742535000000
RAVEN_C30_RELAXATION_BARRIERS_PASS
```

The optional locator replay printed `EXACTIFIED 367 OF 367` and `LOCATOR_FINISHED_NO_INFEASIBILITY_CLAIM`; its observed output was 51353 bytes, SHA-256 `5f70e4f3c5cc97edb6404f4c7415d25e7033c74d1e2edc9722e813313320a62a`. Cross-platform floating replay is not required to reproduce that hash.

## 5. Complete capsule stream

```text
{Wp48S^xk9=GL@E0stWa761SMbT8$j;Q-q|^<4lxh=`*@(^Fob>}|UjN*N-ygr7zB#bpoa<O1|aa@BP6ii{YMJ`R^>Lb8^#n8}H;
kw?kic9jPaWQ#3EQ<clM{d)Xm!}*F@yvI1>w91}dCAvEU=+s;)Uzc&}H0tFJYx7>U7SxM9Z!|@a+R`JM9-*!>@*g?-FR<wVNJ1@v
w*)~um%39j8*G)%h;j*ZGUnSr*Z3RogDJQkg7s13M@Z%gL1UOP{XGAb0w=3GVGKUP?NkGmeRCvJUS<gqmBKTL1pC?G03-N3mG&5X
b@)du;bMSW<^zH%_NuN8KxKs3B2ubO2VfSWGOeRtdzH2Tfax_X|8(qDT!d@3KD>>&$It3M@Ub$Eyl=W8XotUqWL%stJye%d8r@iV
Ia^E;cMe$T2s^mc&XR~|u7@Sj>lLwI#@THkszjrozDzQA%ge5CpySw7=Gz~T&l%s#ww1~vOnmL_E*#723@_30v7n!lHG`Y4V^Rn(
x*1BQA98H%zG+s7qKDTl@AQPiJjkY~W$>6r+<v`Rl!l!cVB;;&0X9}4F&NO0{X^)Vh?JK-H3?RS*NfWQjq+LDVKRwhmA+XV==F&@
oCl2?xo__K(GzcfuG09NJLwVykU8SCDaSC<jYC+rPq7AT@Q9PNRioIE7|l>ZmwQzO-orXJt?Sk`$K~zv%f2bPZ!RUjG*8e(0w7rx
C4@U-|AR9|w{x<&)D78-6#sEXD`*|c!HRu4ia?|&1$Eq8L6V(S*fm<LQcrBkvUyD~A^&;jzovCLFk-L5z{tI@4YsGCFUf?RS5aqg
V?K%*9ve{i+ER_!?tn$WuWA)v7!{2#myS=HLZN8VouzfmrT@v{a3%b1b@Sn8?5F(_*E2#B7U5&z2COXqo+jCv?=?y%h|BHiw{<Pp
a$^4MTJ?MOB+wm|s9cQ|$abJ5hZzhpH&I!{sAi!S(_y*^`fYJ5L2Qv_wZ!hui4-U}TfPBr!ZSAM#k+3V6AW<+_L5+;^8@Hxnc@{?
&{u0FdzK~u1|iURQ?C9{GXilR=d)3-R%;85;2denU>Te&VfG|U-*-wvFkttPE~N}DF1@G0tc-o3U%}w8XX)NTW8HO^&4gX=mYv;I
1j45kBdHRNPBBG&DJZ)dw}!z1jd^ZmrQOd~xlGW(O{XPB!TXf~@EeiIrNBz}<rAJ!4gl-px@f(au-J$HBngVbK?}PB{~-X~dc?X)
-fmNY;ES#aZ4s~#@wwPj)1i^BZRjYe0tE3FvC}6*3Hjr58)KkeO9C`IsBd$_iUbGS+I@kFAxHWfTF2ulKrh6CM?-iDY06)vlpA2-
MkG)oMQ8xHWP2f?j;P3^f3Sgr@4D*W9BQ{L!!6ZRO(-vtI#0n)C#o72F`hgwwIwJw{}3eE+YOf-6oBCW)2@yf=&om^wJ^*jf{H+q
#)e*${{Vo>eA_$(^g1~Te#pB5pts2T3xh=~7|^7ds@Pw(z+LX(iJ?yf>-9U5L@-gw5)HSJ(((R|&16foNi1W&>x^CWf=pjeYIY-O
;mj&Gf%dk<bxw+)I?fd{Q}$hKH%uIXMtxb!?UT2OBa7u-ye7A0h?kVvvmZ$71Fmjc#j4QfdusR^%*27vo)AdeT{G$Scm#?RKWe?*
zqSihc*R{DnGP>L)ey2OwkuXO79x9K#TA&G&nn4W$X#cmF<f4B;IF|N6DR?#ou_DMB&T__Po6!CyFb|EK{L->FhY^%e)B_^{Kpzr
&X5T>fv}hHgMAKd#0m*c)Q)&)8t)|O7V%|37(@M06gI}!3w7kS7;%Xq^=Vihgx;J<QDUF=|FFL+tehfZcc{$0j7x2~j_K!%=0D~R
w>kQv?SaAeQR2sRdsxIbFN&h^V<4(L=gZK&lv6IWXUrDO>r$XB)GM`w1vC!PD3I79Zuh^Wgk3{n?FW(wR9+OiGmomZ=FtMRL1&y9
E@s97#syFdD*@?Xk+2|2<Rlc`BER>9CQ`PyJXO(2RirI+W`+>^tdNlIkpAzTNujr2$!L#ts%u$*m@Ia`N4GPaB`4n*gOdX(z1HsJ
ljcTw`i<iLQ0}<oj&iv$;#_N@-O(_Ic#o~2AI_hHP8s?z-=So~0pvYKyCK;3Qo7t$DLALTsb{U$)`a^~djkl`Fo&i~dQiv_fm!o4
yK0B39e|=QEp&{^uCn4f)yYI8hcP+DR1mP~+YRmr7yS(&XQdZntBu_>^m36ArHIr^wosJz6!BiE>)*!h6siqUFLp*&*FejzezpWl
-J0ir)r)5Z@-B+U#Xxm}6<8l{M@TUK_Wnx~zG~9W7KSd?rvk4=Tcb;td)RIu-VL8@Ei6Tmy@BU?|K&`z?AAVt$m-_Ggn?4A^awy<
j~v`BjX`Db%?_RDM0urg7zV1Y{%p=9kuDHl`>los(@o;5?XgK4cm}F|(Wdh1a2cTqOH2j~oz`!HW>*-~Zr@4BXM|t4Y@-@%E#BR%
eoJcWlOP3+6C9z{a6#GY7X`lqt!N}pm`Bhj<~Vb@DqQG{9NpBUb^t9)kZ^huv==OI*{Yo$v{Kki02aOVxOhz?mQ;+<tum@2rkx{v
j+9O)C_F2px$4Q`S=$Z;+nAqiJ5a_bv;&Um;0kHkr5Ry?l$`nZdXtC@<Gfvq*yDy|!y_>?RVkMn5VQv7X!CEfC7`#H*k2M6vohzY
2n*u`+G-NDR#VvpYGy)a66apwDdA2rIAZn;rinKhP*6z<-~67&OypUoLX*W(2f`^>r`XN(VvK~hv2uix7j7H~PKARWz)PNNPPUzh
M<NF>3DcUQ)y6={ONz2%z$?+F^=|?5pFx<n39@|7LN9$y+P&sc2QwHQ>r@T%OYujXG>5pG4Kj+`)MavDSZfPDMS4e{>dnuIAx_0^
TbAAw!XUvw(8U)4CW}@H=F*;e(l4=%U5YQj;O{2bz{8wDehswYOGp0?A@O3WbKX|5P`9=<{TJcRzQ};&#VC98W>VE%KzYin8<NFy
I-LmSefQrK^bBe3jyAT8Lrybko0;KyIbL_t+U&U%ey~Tz!?4IE3ZH6a9EtQK)ImIK>m?UsQ5e95`wP@&cg3Q_HKK#_$_OTnKH~fS
&o3S(4|>Od_U_@TjqQ_2|LQ6~F-htNIhCpj=HcxWbfn4a%f{6m$V)*f_@!L|#a?b8(U|h?M2q=bc<$N*E0HVFa?T;PlLDpB$Tw;`
?>rU(@3dfkzgOgQI>m3DZq#1>Opg2xf)Ma5j*Rj!da?dYV46&<w~t?*eepyb5dua9JKn@pF?3cvrhOM7PU=(9fY=K#by!LVT6N`4
J6!0`xGJXX*_D#cV#7I?>}YKex!K3_vktH$1|n@}=1$^-IFv`vPz@9yzpp~tK8euLN@R-pl-fWLBZ8q#DyjMoqY8CK@;BrYoaiO6
N(=~1+87UUiwxfo=}{uEkL`PJw$Dn^mU^wgdoscGXv6P0YzDu1L8J`Qi;ElOK6i6@Mu<=?t{A%@+f@+ff?FkM*h!L2|7vamw})u{
OWhltkZQ*PYkl|&WrJyxmGn$=V}ifKJztvRv7=c`?(hXK^VNIJ%TtaAucBNg#<P5p?uDd28@dz#1m+q;9}K!2qo8-KIbA|}cO!YR
>O6)9;Ul`xn%&5$%N|XYrlQIZSK-O;G%;6g{HL;Lq*?Q>OnyhW+`QdnheUN-Zak7^91&arC{MKYBs_(UXjVhF@LFB*JTJDN0Zfe;
b)hTVrF4wGfxzT0STiw0w4WM9pQ+r;ec<ax%mLzR;#1If>3etel_<_~!e}%h3bl>t^Bie(ukyzs5>U5t@Y>j2Nwo|E%GG?gPd}ad
+DgfbI9LNW<)wRq15~lw2_J`~d>$??;im08x)HYs2PlL4Mr0SA`jqeDw_nfAu!MBdG57eCp-aGb{@MiE>W^gyhCBP<Z1n&jU>OVJ
a!ej&*vq3K7gK4v9}_x?fq??9P3{}cYRz`s8K#(MT6L^H>~-ZB54e+|E8QN(cXCZ}(Mz5`upM!n7UjBJzXO8;YLR>NYo^`!HPWhO
0b7`o`a8$mMjpo7r=3O@gYujVCYKx6ce9y9d4@o%lSZIns;?a?_z#>g<p;&9L$NO(;WF?JrEAzMKp@;<8ZKB!^HS#?k9DORqNe?~
P`DE>xI|CN0exnT;Cr!&#klvl<#)_ykkB)<8>VCr;FU%yiF^@&ShL!J5HXk<M1Zd)`2EDD#Uk1?awnxqE`n<v5E0x1S_?UYL@Zk*
iG(ZO`NkY9I358sqb@RXGdFh2yQ?2U7lDBhg@v$ZCJ^_#PnV=G_=YG#PQmxC@~#;)_QonY6XIg;ntFyR`3?iM6*a%S0wRRpvPWTD
;{^myb1S5z>g#jVu}`8DGd0^qJaVKqFX>t`36}V38RfJdiXs`~S-QNoyM541pr&Ur^id(oxcxqkzLz&JL?9pNKSC0Iz>(?;mK_ml
eaT&!+aRo!pF%8epMej<p<8EIoy0WcZdPE($r#53+Roq*N3w?^HeccdWFAaA-BhbGDQsu*i&mWrPJ!(&-iVqeODWL11qs3P^v8-2
Zn-%s!JG=*ix5uvu-qP_<-zp{ZQMRs{wj4DDW8xRZ`7JP_iMiWp0;L&GD%dJn6~ef?wQYzy0VOiNMVR7?q}+}>1OQn4Y1N`NBkU|
Zo3jfB-CFw<TXTIv9gMHHY(g*Y$ydubGL1IB7Hq#>bF94lB;84Ai{zW?}kP_&DGvssyUsJ`ve;LJhW&MP$O}~rH`SKoPraJL-y~1
1$Ejb(?|A|te3fJh;(g-;;T83NlU{tEiA-`E>1JoQ2SYSpbHX<1;a_@R1z;o2xFDm3OH{}AKATP5zuIz0T!+bIojy?Fox9TT29cE
{{$KzCZ+ghl8+N$;9LJ*jHb{X2i<oYs`nt5u4#dUbp;V8@IYju3@JovwIaG=jTJKm6C}_4;oBrJUj9wwp3oN@q@|L(9@#IeL8dZ!
>WhvH!UrL}t~7Af^=|3o@?e?~oPncifgrL1i+l@B5_E{|`XDg@46+1`aG$~>#c70o_TOy<hWmeNe|910DYS-R%NX+U4IhZ65CVI`
Cq;DuGpVhl7D|<Ck@6|l*@2Jp^bEuYQ>7m6oJa>p3;R>{{7g?V)3dKr<q#}aKY!9End-OGPJk4`2pwYoFtpBIZwsBrb9=E~cY;vv
3I~EUrnghZ>-+^}Gm?hU)O|-u{(8V<KvxtPrG}pG`Ng3?Mt4rxq>a~8HbE%oj-KZE7#i2pw-HKZri%tQwIuJ|#$dg@5y~AP$-bt{
m}VRw#HwgL?I_|@(o4`!B!LNcuyb2kF*}JdS6<D)PF{vSt=_Y$mdl!BO}p%$4P^YYxXH7nwd08}gf#aLgc*$QRlNCxd&1u@SK204
3DD^9y{*&XvUZJCIk<~|+BpzlIf?$p!5*nM+GKL*Bi`{~Fo!dzh!i647zxD$I8l=2sm7^)pEe6ka{TEy?P(-m-I%(937By*=ZtF3
8f!VCdP2~Of;v?oBX4*dY%$HVjTD$_3B{)tN!lh3y&F#5h$^Q%52c0gb}5B#K4vZBm_9|*_aqd=dlchrq>7^)`Mw>Nro;Iae=|<>
x2Ej=Zy<!VILKcLo0Wl{m!h{DwktnAI8)!S2SyAzskpsS(5Zy#h^t7QiaY@L?RU2pe+r4I_oRp?V6pXPD7}QUN<daA^!eO)DTJnn
fQsjwW}WK6dJN3CpkQsBg6oee2q=~^*tH7oTdCdq;;ME7eZop8XecfDUmVGEE7i`v3W_g%fsBbXu+gyoZp)=sMyT&6ax+0c+*qWL
#G*gI=c|jvkjnN~fTH;Y=_rudv)2>ffC3F~{P5E^W{%k4|3)r+`1cZgFsR(?K$f=!>LUv4u9p4fcjZ*-?#KpWYSfwCn?smB2QE`0
Jm?K8r@aw2qtu++$l#Q5H`vf6d~MXhAafR;S%ZRHH)dLEtYNNpQDOvrP_u3L0;aDHc3`#d`xge~)6R#qy8AZqQ49V%xQ<sL+NOkV
5vb$zyXq=)FvF1rY>9kPK=9<j>Y{);Js98Gyy!Ieq*kpz-J3CMnLP;DWt1R_iR5%G`6$=4wl!df!5}Zm2R_s5Nh&pFkBa6ISHU8d
(buYP-&Unm11bqI5f1sc(RG5NFEipQ_HrUF>{dNH%G7NjpUGdTCmRi9o126}1<iKEN8$)IHJJy2MY<mqH<oD7DT5sb`OHZzfX007
>aQ^{rsbG^eeY!oRz&D#lsH%1X|YWY?ucZqQh^YMT!M$CNow8bmA`dZ&Qh~={=DP~TNw6$wogKh_-b-L07>X|<23$Uu`%DQ^tfwW
e&HcborF&N;1PQFQWCe@GgRz+C>KS>afaXiF<~1<6|3<D0a1+xuq||8i%secOko~fEG^R5QS9FEeuexix}~~6O-w*sD*8)J_;h5L
L;v2M_O$Mo5-L;d^5G7TBq{-CR(8cBn6oTs(0I5TgMrko<q*X>qm4F*mquN>Ch!)PR`f&lhIL#hdI-29^Q7u^M#UlE7$jJ#Dux!E
xOH577-&OJp#P(`%=%({l9JnLeWJAXijZduE}0}5=3gpXU2PrD78|a!<bX>32iFvJ+t{&$N}l*Pp4cY?aPtk?Srf@wE;ufiax$RC
T)1XgEU+DQR<QS{-uc#ndD-iqp;_ypV@?8GagHpMx?xyhjGa8J>*rg?x}^mpnuW}&NUE2G{u~}eNu<gT5+kjbWh6n*rK5@p%tJsW
iI8}rjqz1u3|3p|wn|<O-w4`J8zZ-(V47mvk5tK4RX5kw3wzQoIX>azOi>?+dIqgMnwvr*@sT}jfXx~i`M{z~+^m7ja-Br+%>(h}
+8D{#e2q$utEypxYHgLoGMX<s`DE67z)Gg^2|0Mn1mjaWZa^1#oD%KBOFTi4&d_|<rSa<q!M(-@3oSJQ&;k*gEcuw0l2dn96y;>X
jnS0bi@5qSbPgEn02+me`~7H}e!4G6PQTJO%L6$d$TZ_c2C_5_Yhl)7naF=fIa1vyCBJU%NaOxy!*mFaL}+nSDF8`9fYNHl<_s0=
d}04IX5d)}($`VtL}XJY^TS!c`V)g?tfM*CBn+k}yqrMojgBH*U_<AO>UY>H>VSCBz>+s}j(V1HoIO>+gtrZy<U;gmSgDgZO-eZ-
s+|BF*dzaCJL;|IZ(1N!{JJy)XDCbMoAoI?E0xgVMIDWvB_3&9B~|{4VnGD8sK??Rdl~>>A?{QqmpI(qk;}hY`XS=6V+t{dsjQxw
5v!>~r(@aj)UjQW63nzC?J#G-KtQOR#@Bn$;v^`Xu2E#EdqF5ax;fx-M@&=E;Thmh(>|K?E*u7f6IvW8i-86k2Tw5Ig$Q@!aND?J
jw(4oix72pt&Ha`tsmvQ)LOxnh@=+<w~+69q1je3^346fdQ%CL!=MXTx8o6Lcuv>_*!<ux3){BqZK)jH`jZ_y;$g2y1qtdlI`-nG
<g)uf_1(W0OL&0Th$s*=JVN5nS)WyvggqYUPN4n)?Oc}#nStC=qc5xx;(}vs+Tbk$G0l3*XWm0IDF!F@^uM@1Q=3a`x1xst@ORV2
9|%ge982wSOWTY;DbW^kC$&t?IWfG3Re{C*&0mH}{maaa^Pj8VJv)+n1w1-HxyTE#g9r0WJe~G#aN~psSVy1Cs2}RMTjq+@`LIe*
%gvgawNy)_rL;a%SY5mi=oA80JiC$O%UZR?r1oJc<MyMnkxO!@{?ls%AvOMjq$@nGF>)`ODMDf1C-<(miHv{a-!W982skUe@`}%k
Up@R=om|`$V<2sCd>6{ss~vWg+RSL6gIs<qng4pk=~ad?i;Q3aX6JmGf#DHq(!p`6HBWGtC^JHOnd>yx4uovmNf2rtTL(fqQRxEm
9@$ZSZL9*>S{@U0Nwrr)LbyRA`{)uP_wu3O%n5xxH18Mlbg>)>tl89b*rv(l%T&zqPnBUX;)I0Q-jVwxKa7oQ1&!Dwix(FAt5lrU
>Y94KM)b;j@!0i8hpOTcg&K2Ye#XcBRQdfPoQrB_PllwqI-6?Q`1O3)&Hbb_@=K8eU=kn2WD#+ON=nkib*S2lP0Wd+3y**`9im<c
D@T5}cz~-;BoUA;*4m2?z$Fx^$VSnHn!O&3o~Z8`VWObb&Gr+vs3m*qHd@bO0bDHU?Mxe0xq=%@t56X4&RXaJg8%1aW7JG+sLR7B
>p4zc(AS)&L@oz$wa+7Y?Ed$%2KH@FDsMsL*WvG0J0)<9g_^C>Fug<Q>apQ#d9jWyln?&1m13fu>Q7miXbUTJ7G_dSS&L1`(VmfS
0^Zq6VOZ08IXqy}of-B&ECJ;FG(0CX;X5gS#cM2lMbk8<z=UkoD$3)yZqUwUa#~**$lE3SQ)9`0-ZC)oVG^f(J9ncu)PeKdNpRso
%86eE%3`l3&D>VPdY@_<2~MOr6~jvs<ZxwYM-7q9Jc@mXROOu?QSw>LbUsfC=I`=ZzJpzEX*0F9g6DNXM$2nd;%Fvn9a}E$*?T{h
^*(I-!GSMsQ`0XZdpwuPjs@MqL8PdoXo^J>ZMS-EY+i%ns<Y18@g`0#rWi%mq5hS~Z2=3H6}>5FsrYBQ<<0OJu=J86P@BGF)c2My
M2xqW(kx}PA(zuNdxrj3<WqTRUHHN(-*2>LY_F;=|L=fJ06p8TkEDG4V(@j^C*+gjyAW3kS5b}6<@4PzHkZ6gfo2YD2-!OVl{4ZO
NSAbmS%G>!lajR9*n{RN+>Bl=l=pYzv<-|lSUuKssPQ%QWmz4N{)2ij)<|$CXa<TB=vF3AvHX**wG9+6yoRxAiw=hw(u~!DWV|N?
it#z{a@Nr9s<-dE*;moQNr=eqGtD6JECqGjpd>FM>E6Aft8(rTR+4{s;w_UopGS9ICV>jRjZ}9^V(K6m<5x*V+Zp^l5<8W={YK%=
bbl_1)Wcj&{)DuZZRiBPJOUrLBFRr6{z+gYZRbIeHFD3%E3NB--o;gRKE-+D!J&X1D^bGyB%H5C^<5<$f9h-ImBej?{Txdkim{iT
+?^c06ycTFpYl{3tB@>MqFSY|x0wnzniLpbKD2I~2kJqj`Gy!hfun5nK-q~G&BkLe@h}?W7-fx~8DW^w!^wf{Ntv)E$cbFIx~Xp4
y<gC%$Y;0My~6L^4XyXtg2?$fiwzo$2iaa^TIW4&3&MyYST78jc*srN3%RqJmr0=itMD3tQPEwCdvmk^W1$&;0q-q&0t`@0$2{Ww
7E1XWnhsDCdbF-@!g*Y9HHE@T0Utl}Pyvq@JpuKtyX{9{PgxAi4eM2*9B_8Z769F4Y<`ym!cwRHC5UQrdFrFxEA^>2y@1FNe#Y75
1fX!LurE~t)mVj$TqYsRz%Jy@6BlY-cfV139D{s}8^cn2cwVtc=E)6;II#$F>E%f5Gb&w8X33SSW4wX3G{U`2KF9#nwB?eNIVm+Q
Eee+u&b)^I7=@t#s)-MfhZE_)x`_PZKfKx?N|+-nS69&c^;M`Z&RmxCa9V^>FNP?>GJAZA-1DRQYuKk5)d!jFi6=Enc_)9u>8$Cz
^~rxTUNm%COv5ozr5<LBbR6Tpcn4OwSO4%rLtF@rR!xIho6~60IjS0c7g7OrBS6tYpGw?kQcnYN^5aIPd$aMeBfmfbx)@xRior5n
)S!Wagc7pDEUWZ=y{Nc&-WYZOZ1i~JS%rU_+mR+Cgm`S827L^2w}5$g@UpTY!PEG9+hHdxiSTg*JvpLYTFPJT$OV1vNP+O%o4~td
u(a{xSLN)2he^sHyyvsrX{8Q*Z5UlyE*0wg4)<fczF+8$6(561rjJX9%??(P5d`-92)c$4De!W@Tw;VadfhpXTm{MPv3p`VpJ1D^
yQN{#&m~&%SO2&RzSE0zp%mEyD28Z(jUECON!VMtzLipuz?4lTIm61j8(!1$WVjxZdP3lp?k}YN@&xdPUOs^>dH<{`qlJU{R9gwT
6s|IQ@~7T{H*OuD0;y@1$2-mRx2K!5Mj3RUk#}fEsZ|^kFDb@WNOE;9{g;-Mfmas$KN?q9XdMTIRCz_Kg;4Xq+?cXp$_n#1I(=qa
yUP)$!3-$)WKf;Z7=mCbKGhH>U0Tq2*c=p+VW5eab9ayJ4yhJt@a0_(Jibgs<YVt1jl*G8$ZH{go!Xsne|<6f1KV)~5UEug=qjy~
EKcH=2cJOS6dLiaUV0=TfNzCKmtmQCw_C}6IPqYY*jf(*3;X?EAb4aC$O2&|4*^HHn>7O&*f@KHuSaSjkFp&GeNCfZ^)G%GL^y1!
G_j=esSqOA)#KFF>*_z+Xp6zvAp2{1AbdbIv&UVpOA%sYvo>EX_QZq6mzJ+CLg;amq@0W<KnO;=jI^;?k=w`rn4`r$Ce2Dr0u+K5
gD(t%f;GjLY+8iQdmh^=AQJ&F2xrL;Uhbc}-1whCI%B<eN9>E&hEip4K#P=m_!vK^4mFrjR;uDTJ^Hu~CsfWqlyaS3_=pMhLU)B0
_el~PGiYwJPk)_zDlpSP550iJMTk1(&kSFnzH{k>!bfoOMc?x#EVaoPhVCyTCG4UTbFWC+h1&GybB6&GI-Nsa07A*BvY}HCS3S%X
!`uqqAAM?=+u#l0GPC6#Ikf<hLH8e7k(CccpI<ElNZ5DMcqYsu>R`~xU7vs)38*01WP_Zk>jFa+uq$BwX`F%9bre!T1|sjAvwfqY
SrjnK>AcyA3!p*qJ~blLjjY_?`*P$$Xt+wlDqcXjifMsI!;D`jOm&Q3#TS%*1QgEwg#OxH)NrtCl1SO^Dv2UPsOg-)W7dZ69dF8e
a*@{zv=mC_47;H36Rrn+x&pq534UYWHkz69l5;%Jr%0g|Y;%MB$4u|t9z#(}+?Ba}#NYOHe;8<b+__St(B8O9g|4bPlKT&?Vo~-i
ycuXTJQ0J+A!j2$(=yJGq`HiM8dzz|E-7mv!^3PfVeB0`8#aTZlKr+b;mVrwdGa;6fmGSHwB4kwu)0E=xlkeN0H?#hK*@V-GN(t5
ko%=wLY`wjG$g^@hN=0tNSGDX^~M*&#V6nBI1c&GH%z@KBxKFplx(Eo8VZ~+1t1VgND|?t3C?0uMs&F}FkKjP9b_TdK&E{0Uj?F>
vhQ#aA{*lexE35Y$a<0|lToabSCp0Ha#Ylj{#b9}y^DYbo!CMfF3V3C)9~qz^di}FLWOvCTT4^3&0lQZ+VzOuONcc+o!ontSdW9;
bK209sK-xbGw!{vyLFUH?l55-O6Lk2+N-6fATBSeSoL1Qll)MZW#JPPhdqE~_oqJ@mB(LVRPy7!gdW15(B5Bohb`Z>{l_09-c(SX
0*tN#O)yfauJ7oK-l?=gFhDhh`{`g5at?Q}*FrCG3+hqYf7d4mv&alF)!f9#9Ms`<S2i<uJ=xS*5LZ26o%NIy4a{?NMB};e=j)G5
FxVa!Fx_U4fUknAqBgSEZs+7Y<nDH#_5HRIFwL`FmyoE`D-)V(j4G`<?^CTo%5DyB$F8+F3@9Wi=~lBkkL&Cc@thq^CNgTefb?nb
!2RTux|kWUcd}c@TQAO@zR0ykD;;J{Q;@|Zn7mAQeXpEB=lwTICy9CUWb`T!wIjAn^&xi(`35Jnl*L|=MPx*8@%@Yi7(Rf9GaYzY
#{yflQuyO5QuIM8TU$Q+CMuZsM^=6xET7;aCr$!?cM`Zt((c9sDj&A?UxOf1DNg_#tVgDt329T&y1S0lB}RUMHy|}BQ;#Z(UdZh-
e36j`R<AM;Lhr)(gjUwD|6oL$xQc+69k!y0{4Y5yb^xLIoI2Va)UD0m_OZBk|48EKygAU*#%IO!#*-O_mE~N|Mkb+VA0G(@WYM8}
#~j?X(5Q3*|G2V;y}#^uk99*=?Rgxw@z+9J&Mcp@!oV0)dz`w1FELIsFMxFKC^;Hk(cO(Il%GemomLop<xvLq*nG9Fle=mrlEY)4
L6d9O79~H_6BxmkiIVw(XC)VZM(^8g{CaPNdiGr^G5c@q0W-n+T!m~+;pOCPHxdLooU3h$mNx@nQUzsW8-S808&04-Llkom9=vCe
Kwg2N^_aDI^7$jXL@JMdd$CUFg$E-4>a3`O#%iMCo$T9P?b=Qc60#4z`qy_sLzz8*Hx#nuu)l&~?~0PKTz|~<cp+9RMXOSt#TCmh
a0PT>UXK>4BGQj5FmO01$4XD@1M8>?MG;9#`k3rd>7cQU6L}@?4`&qMSv83AAygOAk>~BSRx`+_>;}p@V}Ro&34Db0yP~gu&gxU~
PW#&q5S&Zo>ay6cV?u}=b>8$)&$7-Mzq8W&Myn{E{bt1_Tp#zgyRhpqLq9TBf#N3~Cq6SCfgPIOJmEbO1lP<PO#?4IMoI?CgJG`8
#*EshT~c?yj(Ue)0^H&&VhaPH&B2VecLaXU@unh*%ZlS^Bee6Wl^%afH3v{s8FLc9JU33{uahh?mW9ZTRji&=_{~QT+kc>sv|&Rh
duU)E%(d*VtB2oBFdQ9&+aQ|L=vE~SmCJns7K2`WslePSkQQF|kUd#zDrw78q(_nhbRPuJ$;jeR;0R`jq*wjE>+*S?G@9%T2W2M8
Y5n2S8-pnEOM~@83!8Ew3?&b!8Ok-v245=yi(uJ6R1C%>GEK>MRXTl3QNp?Z09>3A!fM+^SwuoqYk%Y+?PwMDR$TTpetr!?OFlAW
`_2zs!W)&%r)`{A_9MqvzSumGfcWL;>h{|3@<BflfcpU+@FbcloKyOvx*T!98}mv^0GrSqCvu!~m^#;<2xI{tnFJD7TZocU-@^9C
uw%1J66#nB8o`M1x(Qy?HcI5h8d0vi*OQbOo=x7&7GVD`CywqcEmt(^{qP$NhrQ-{Ab->mdDjn0Zw>Umtz|qi?nMy_pfA-dCa$2R
TTJ3vr$5~}1k&R|r^%muIVje+gueDC)6mIe%XR)#u1ROHk#8*#=VF>GkHj2XpJ}zkV?$fMG;4bA&tQGFI6rI`dtd4>Z|!tA<xrRY
{MQ2kxpzSZuuuFZZRwQ}%mogZ&&rzhPQ0w@|5A;mv3F8KTzMp(5yFX!e_SYeM>Uv~F8@8Mgwe8O`N6>IFW|eD1~!_`fxP`L=8&n?
<CbuXLAkzf9fPd1xV+NPB+phg(upxxR~-<3qO>Pa=eShR@AR=acKB4<=jcM^2^iMbcrFp-8~A2_fOa@ND8lDtL2-7p{G{Oj1P7l%
=q}L`>QFn?rw6I)(`q&2k-e~Ow*fj5k#$<^uI3XJp;*+%KN(K{S0zS_zlP74YmNVvgM<nFbFE%nzw5ZKqAihs7N>;me#2bZBQ52K
p<}<0iHgDNi{&~#w^}ikBSp2%(+sfug_ljk8qr$h>fw}W*1=glXP`H(z)3#c-WY8zQhMi{P<hu<N}j@Cu}Abvh^UpTie`XylfME4
m%HNH`yM&6z@=l1OMHEANIdZO^hj?_BK|?J2|it`@ik_cOXr9?vlsO6bOo3(bX5CZj*ul?nkAo5(Q)E(KY1D8<pz`h7S**d?l_5r
z8VT66=Ipj6{EYa8*+-Or&M>~jIxLcdsdegdogCAL6&KCHybvqe0|3g$BnL!+lMm1J1`a5g?v5Pw~QL?LTOSRV9vOyPN2}PXQ6)|
`W0JUDU+eca67^B6Zywp@Jz6A9mpa#u-1+~>K0xvwE&t(apVdHahwYZZ>p*+A(a(QdmCHOFVYg?6bFcN)&KF{dCqhBO;G&cWAL61
1|ZN$v$HonR8#P6aY0Q)BuRzntXnRu|M9|jva=EMBVr&>E#$C!g{ib=G}qn(aT-E_i>QJE3`Wy+UuAHD2UCNiICMr&m?#AHW`Hy|
TV8{dXR(JN-Cqi7ly{DDh$t7OrbuQnwyI{qKHPe7xJ<ZxO3)<H3`t{(tdyDr4=3Cg<8TVnaZx8pr@@rkp{|~#c@lipmPk^FH&QL4
6(3z88I6mbsNf~pFbCc&U;7@awSHis?3;#aMT^Jk5A)j)+V!g}^;#5a#5jiuL$Fz3N6Wbax|{dVZajbpfDOKH63LM0y>cJ$=Dq$&
RRd8g{L??XT=}(lbUp}5iB@zx*EA@Pg&RQ!6>}L7?Ns`Zovs(4311aQ%LP;{PE)>6f;s+j>*m0ZE|7`LnY-Rco>rh9=VTQrFI`p|
FNgVocBt~>>7m|9HV_y=ENDAELu5`=-1pSTczW6+Gl)cr*eaO&@mwB7iv6mBxKHtLJy-=U_&(tx<+}xber%p-TIo_%{SOsewKTed
KalipQX&8t>P=@;KdeZUnU=2{?9F=0z~BNbp1aIb+sBq&-i2-<VsWxE*ROi@O3nWYjy|kF7wk<Gs4Z}`|4=P_2cp-6UcvPMy6^j(
wBuic0cK_>e1VQMR`@F?H!5l{j+QtXQDQ}m#xU7$B@revPK2592gB<to<bIs<&Zl>4Nx<CS@whjhKf?#Ap(iT5nIh&p)_xZ&E18z
z<$>}mw&Il>UdFpzfVzU-YXHcp)a?!i2De&t+B`8H4P*6IyXn?w^7rcFxb5+kW)voU8%yRH*w-dibQ)ouG3<je<I98Z#<rugCSo0
t-YCQ7Pyt{q^y&^{+FL|%6OZKu0JXVCASxsqH3MA@omF|x{->-BZ0KbZ~iAi6E#6+46)gNP;}%IzT0#uJ|M<qc`oqVht1We`;l?C
6ZDKZpe9juySmb8?Ri_&Wi+6C`Tf`MgD==j0`|;z+}#>o3N|D7*tXtCQJ6FNnKjt$56>Np68~$wxy6g*J%XsiK61p!3m;5S7PpGr
>sX<Esoe;GxB}H5P6PVU5_-qu1(<YLV?|zFiN=))qfFKsM8{3LwQ$)d`44=z?OT`<O!SCuCktua!nZEMCF<=xnP0I(Fe*6<cWwUd
7U+iD6%Nd!>T+3Q!C&XtlBkGnf<Xk-oXcBYVtd?59gQtnN`QDd;lGXE0E}@RD(a5>y_lhoVqaY3R^wqOdFsR!{o#K0z>gzcUVag<
icX{|`%(I&Jc?9<I-ME()2GIruA&ru1G*<WQO{<hcQb>KT88!q|KGKzRGd&Y*BBUfgd{2D|JQmo1gI9mU^MX#+W~_vx&c3e;iC56
=VcSr?p@V!qa3E?D|iF7i(t=_@SaNuQA1G>5uX0aNDp=|nxu?%DSxknyJ#aeIRwQa(0w<b`q&cI^y0)raU9{@7S)L8aR$t3dQKK<
Q&y};-^Xm?g8f9%IA)Du3BJnj?mGr6+@xAvqkZ()bYibRk%GmwOtd+tQvxQ`g5cEax1=M^M>xj_2v;GAOc^pS#9&PT){eIz3y}q=
L1d91sr2xPKJCunb2W`s6<l-Gv^^ks?&rS$QSx4nN69Gk<G=y6w+wPQ-#1#deH1-s183Xe?a-d@cZGj87-u(#7p`2VbZQ~KbeQs`
QA!}YViyn4SV-&8?GqIT410Rs@iTW<zO74(_w+3J!m-Wqe_R+2h3k^v+P43@EhcLW38kJbgmJK9GoB*B7rYZitCuN3^Xa{TQ1>ZV
v}nG`@hR32xZg)9wS0AKJqtC}B#n@ec8xes-WR*Y(<cZbn#Q>Zi7rn}6PT|8<V36C^*H3oUCCZ3;f;DT)Fo*(q9ai1td3j#ry1|(
UPHES#q@B}X4P3&C=Qx-<d)eMYXXqdWv~n!=`?hkQBT6-SX-!}oN)^pb-D*6slybJ&gU{gG=mn}vb%S-VS#CSrr4sM=KrT?ZRW$m
J+d-m67x-P`tI{d&54vH@3%aa@z01~zE3st{u{xJvja=NlK<J1c`4W`$|p=!oK16sVA#iLtVMxobI8{`N`+y&JWWQ9t3GsE>=Nhe
#K1)cDjVrd{T{^g>T=9{=_d^O2Yk&+5~_#P^6qMF4;#*EexgV_Ya&*DKW%1K%VQ*_mts4n(&%L8i_h`tQ2b-g=yhRwzTW+Hlx~0(
27gqgO7;$poo(zfyU{1EmQ1H@19z@<1>&TozeH92u>!v~&UBWwm(r;7h1n!d;dFu6hIcTW=7IeGs5N&<C3k_FRKv@U{`jCq*p>iP
m>>$jEUa_E{z#5bkNEVfD?mP`XzY-#F(gD2FiIZmNXIw@Pm~hO^S7|t@rQ3w_FB5PI8u8jtn;<yuQgq8%%y_@oCeCMb)82WPC4^e
BUf7WyeoeGzJUffAX)j~OPG^sPZW14yUB^5q!v^bw0xQk7jZn>!NpRTGcOI2;1Rw+edL+N-@AI~zCYnKLCA2e#pky4;R#Po@UG-v
D(j4So>}WwO{8{N_nh-%rYo*j<4!kdJV71l7<UN4w(Y%WkRd{Gr_i<P5-n_~&v}o3{DoKj1D!L8M#YYBpDF%c2XUPIY)G!`hWH=s
gEGIi7&7C(A28)>Mwk37@U7mR+`9PV3B;UO#<}${1YPu=OLQtghg7%5ct8g`_faX}{0c`_A!C0BC%J2{HL54pKwD`df)ed-U)d>>
DtQI^>v$m1RJS#<>V{u7(JwpoWQ#0x^fpVbF)=)vQ-jylFSUcmIv#EMPszKWx5gqXdp~4{hPa|BQk_BP)%y6lwG6adzYAxh0%B!P
0C!>8jJ%{N7Mr14+!$P{H4aG%^u9fk4vAZ@i)PA%Xgg@wW?$R3`=|akK;tF*o%5g#t0(-9H=!Z_FM_nXo}w>ax~qipq?G#UBS~$Y
ei~8jE&r7{rU-NBduo$*QLbfUrVqAzE59Mos6Bu}x;iFF!y>z<6hW~FpaaXWm7Gp0Jf4gb7(F<cVM+`tk95QhkzeEH!2t%zBfo))
1DXu4>m9A?yw*$hAp~DH+w_deqs>vsw2*ROSE26pWt{j;N<^v0>9RR*9Wz$Y#NL`zwcx)*rx(WoO93GuT>{e1s`T@VS9Wed{bIB7
LVVFddNH_@fkMos6?dZy&yhr~U?-U-IE7BfZ5gyn9TDNxIQM`(<gHt)DJMXW_!eWFp#{>O0;a9m0AM!@c~G+HITwjvYP|EX3F}NW
`9GCS5Uwg<r^iA&eu-U1;%5tf@?8N_m8&k&!xwHZ7^M3Cpl2iHef;2@l(-)-oAcRIHRuafqFgkr)L_cOg2>mtaS!|TZ*@LTBj}md
4E_zxQ-Y>B0O!7=V+tn)`3u8cv=^pS<+nJ##x}b9)z^K+2cjrIJe-5NN0`GGm;L7uxgepr;yx+&_F!7CBXbm%;`HEJpRs5im|t#l
07vEzpQ9g}5sdDFRH0LG6GiWW<-QREUgyW-9iz};RIz7bca_3}eQ?)Gu6a8PEJU;pzpSzB=d<+&0nI7J)lyhcAft)>r;Q1;iX+c7
oYsZ0R{&uu4Yt)Mt$cnd{Q_6$_h&;8iOBv|SKHP>?>}`yP3SQeOlWZSysw)C;Nn;RE#Xu3%3KJib`^?|1>zhtQv4LebmI!#u4nFZ
L}K3ytHuMlu0`A~tMZXpF}(RHQh0oipLy^WfH0vgjeEK*DzR5|$?DG_HH&;cLMZ>WrP@UWp*R9*&=Qd6q<DM3Ro+%PSAS@%3Q2Sa
wBi%^7*TpL==ow!hjmS>Ya={3e;W1w44a*0-N_-E!z}#@7r}+;lv035)2yWsWJ5mt+6xbCk~dJ#bG6wS&S8SGX*BQD3_RuO_9g9@
^8G9QUi;)O3y!(+YPq?~Hu4Qvk5fZwl}zsXaZy@5hDp)nxFv7wV4ymfZbeubn4th56c_lmIyDn~1Ou>=O_T*}8IlM8VG<>F8p~W>
fB_JY&^Fp&vb=StC+gb)nyYPSv!_x+N_UWJm5XjvxvSwX$6LLQLink#XDYq9#xeHupA+xss)tefG{2T+G+`Ri0<(8<u>@i4Bw%Ly
gvP5K81ILeg%5-<GjZ_CBtV14f1WTLd!jctu@4gNJ#xXmA9<98_cmq-LmP}-@Iyfz4_<OJFIjm=ezYsz`KfhK6LJC>KNL+Se$69|
P_#Eb!$TYx0m*7rZ)m(8c@~LAYjJMYVo>gh#-suxFc?5>KzDVYfcFvR5>#+42@>Pvtzp0lii77#TqXs)n;0z(6)f6}k)CmRT;szC
n}xv?+HF65Z*Y3%&;QQ%Q|+Od#fu~D<1Xb-N{{i6gJ>hLQ3Kzx9>K(j8=Ocn`-nc~kJulLYh!Y@fs<_G6&xgHsc9@`Zr2SrWZ87%
d}Yj$qG1tX6z_Q;2SDt`mnNS;Nz8Yo8!j-(`#|7-B6odo;#$`Yo8iT(52_elFzLBv)I>oH00rXnWQKtDQxMR@%s5=UAe--~Zh$EW
Mio{PkOE)r$6E$yD#RY_iRpp_&I#$<DFpcqgX(c<u(SuCxVbl-LR@0|BxqJAU}|DtRMaZxP4N{KmrKLn&eRz2TwDL@KKN-$b3~nE
-Yn4{Vv=L74c^k1len43*l6D2?HT-3=4X+c;c2(K>R$Z6WE`LqcAsZcBoN~y+}e(yik0ZDKKxcr6k+0>T}!QbFjiOnWNyT^NNrd%
;aa|QN{NuUE>mA3O0n>@jlb*GhGGH8D`QI)3ocwQSKFxsPhqjNF-yO@e$vJ@`mK%L!uT=hl6v{`o&|yrJb16m<VA{q;))q?asId7
5Ldy9;-l3m{4=2)f$-~hN#qhUB6~Ycrooond!J+gVi;kX)lgA}^~=7X*(k4(>N5LTTJN+I=7sOxkTg~|pSXKa-AIC(hh`?7l2B@Q
c_n=jqTc+=GoOjtalZsKprm7}Gc^=s49JHavZ!|hsxG~x%MJ0?`W4m_8?opEFJVenN16K6o2iQ=(Hu~j`2i+7=E{5O^B2swKvABJ
usjL`V*V@PuJ$tLV~Sa$=cpSkpk8h=iKbsHyiAs&Ure|);AZ7SNnZ~mjV_Mbcs$~rCjkUCX^NA?5mEDfW8bl>(7NvI{vIy+xn29{
6TMe)@ekENnNB~kEOOTwdjQCss{gsIHJN&Us5<t5*dtPlj-j{Cfi4+Dg9QFu0o^osumQROSiC5LxW<kvVT}00@d+qWrPl0wT(_aq
-wAu?c(yTfI0pf2hefOEU}yY1-D4HFVF%PMHOEpOl|eESB75bP=O+0ob+0s)<T~L1xx=k@T&4vl_#z}hc7x3pA(cUg-Xgrit@(pF
uvnG|@2wQON|UK!dmNT$B!)wHXj&AvkekXPMEW6>0>*rgBZJ|QF;*b1@AT@P(?*ovnA5?Vyf07I5!$viyXixInr8M<1F}DbpE4ny
a0iMq)s!Vv9U@8RQUB1x_EXB;eSapHJ<Uf-0;;uI{)rEkR-5G+t65gKF~Q@BFcz0{t_TR-^)j(bz1^Oep*-b|a#*kg5^<&$LtiOV
fNFv2=Y0?0E)DScu>)1m+jvbXy_2R%{*r&0&LI{1F!FQqO0D<ckKnjiO2X5aB3lDSdtnRfG2s_A^r2UqE3U-PHN))kbRXf@=rse^
@u-%(klm@O@&Su{Fr3xjp8&HRi)wjtgauIDuOVM^1o)MopYX<EwAznS*Sp>L{<$t&a|9)=te<s&(ZM=wBF*CVBd(Jh38Van+|=Cb
VK$+s%#9`bicx9<mr;*SUnZ<AK-a<)T^ld-rE^EhbLT=7c|9b-Ynxvh6!47OX2bKaefjwULFts}4RH@u6k2-x`ATUyaZwNqq4?gd
WyYf>9G@pv#un+edF>;CQLKf#nJD|ijdf;O_;^VSFdNI>Vj>UI@~fZusTuJ}uqlaAFDAzER$J%-I7DLphO+5_d}M4T{9EF8o>E2r
@kVbKOQ1lP;F<hZHRVv%4kj;ANR+Tri1tT`D9+2)n=ZRKddznim8|@)N5T8`6hG_%C|+bmn*Ey(c)^sl{XkR1Wr`$Q$@#lv=BDLQ
zqL?D^@WP<o6~gY<?FeEENqH6&c&)*Vb{{Ydi;Xr>Nl}=?sm?up5cN`p8y{XO&o|(?pB;AU}p@pb^VufGPXL%r4$_M{+eeKf(s#L
Rww@|dSpqB)S`HQ*H}<Y-O`HdiAwsOOF^0y8Kr+F8{Y1Xb1(%%Np;@0B-4L;hFyR1zKj+6Ic1@KGz>q#=mAFhaDx#q#5^nQ4Ibfe
4oQ=kl$TrslBP$3H}b*6yqV9C7G^M_U|9OGM*~0=SWw~pHQ@bc@1PpW=l1>1{mg3J-+vZqB>tSBDb8GqHP{u!hu6^UT*ho|XNBL7
mI{nTt9&^+iB?7WTIsAXtm9Z19`!NWZ{G!_^H`DB#2{|y(j)1-^Lv4^scyy&T1VpN^i5v^)Vf6Gb{*uq90OXs5j8^AXmMxAU{)8i
S5nbLAX18B<@PxRuLyj?{Z`O35TP+H1>OMMop(nJJ9g>9qAD0WF{iv+Xav1(EVJLH4i1RWvmIZMnS4N+5sz(@a54Xc<3)K-0>~w*
lW4~xaNvYM61mi4PM#!gGaogWC>&vfM=Va~nH6w8cP}x&^1@0w?aaj56@Ho2^_>FrVL7gq7_9yrkz@AL<U{mX#70@=InBA|u5KZE
q+DK;6}TmPVu9YVLIBMfaM#dtAUTcr=ovIg`$Zt^+B8&<QPQ&=zwWK)EEbLOQId2QbD_BKnoC^c1M8de6d1waC0}MtU*9t56F!l4
DyDk8FTS+ERP0RWsoXEGO^v6W(2_c^D+r#2XMOmwEVqJviF|;XHPC^*_-$d#_dsm1XlA+n9gT8sIZuiGQ-V^8(troLNY6{K6d?5i
(ofzpAL57cBXDu{vx)O|UfbrR<nX>F7;bC)kx2C}@3O=_Hq)dO4!QvJCMdt$*y^#mHZ;a5oQ9hR4yN?jJ)b#PB(WLdnld$)kS(V)
s}duBR1_D_)lSvSX#H(W4SAW6kG2VSy9It0f>O{3qJZ_d>lYkK;#HU^aZvOP3jvx({YX(WsBAXDkt#xM!u|$I2-E0L2NrDOSRYB5
O9xn7E3@PP5{qp1*kl?o6RDRU5`lvcj*2D)%?xHD&iHN1^49!poTHX`d70gabu#P#_Oyg<<N!lB>4SK1*@b?o-v^}>Eegm;PM{CJ
ig`I8v)B$MVaVMWPPK4c#nR!T?0R6cCR`UV1y=14fh^~%eN-@vgmUDJ<v~?p#*mvooK45mZQ>JCZhM$*Q)k&0RLBJngn?n17tMn}
-++B9%m#QsgjIoa#FH`SWFh4H1+`%4Fn>(gIAjf5d&blY=&t61Q33n>&@d^~3&H@M_t^AKeu@avMFpR3q@`iC?%RHtLz<NI1B7dp
%3G=K9d_&qL-w&!F|f<^Z=QvzLZzL$NYcH{C$DHA@dlDZ-R^L?d*2TLjGE}w<aQ;GPAt3odIfXLahXe&MQZ=H$?R5G?uhEkdk+c5
7;?={z+p&n(d>v{koc}!0pvrHVH_Ia@}p-Rt*w29%d<7``W8h>@2~~txi>)I?r}q2v!D93wYNGPpK+@Ban@V-<MXYD!QDieg>?w*
iT(fp00000f}FIH-#ssk00EJJ0o;KEi)T~4vBYQl0ssI200dcD
```

Convenience archive: [sources, complete exact remainder, and verification ledgers](sandbox:/mnt/data/c30_raven/raven_c30_recovery.zip). The archive is 561031 bytes, SHA-256 `882ee7c9d806ec8b944b327a65de8b2e7e506251822410b6049eee43c18264d1`.

The remaining 178131 branches are not inferred impossible from any nonpositive solver output. The most useful continuation is a coupled actual-facet/physical-volume or primal–dual certificate on that exact remainder, rather than another independent-apex screen.
