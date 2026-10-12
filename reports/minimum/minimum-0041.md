# minimum-0041

AI research report · 2026-09-10 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NOVA54_MP45_WHOLE_GRAPH_ACTUAL_MOMENTS_V4

## 1. Determination

**The remaining root0 orbit is completely excluded. Together with immutable parent E8, this establishes a whole-MP9:45 theorem:** every full-dimensional homogeneous convex polytope with the literal boundary triangulation below has at least **two strict unstable vertices at its own uniform-volume centroid, for every common positive-definite physical metric**.

The new result covers roots `{0,1,2,6,7,8}`. The parent supplies the already closed orbit `{3,4,5}`. The theorem includes genuine cofacial boundary triangulations with the same nine actual vertices, actual zero-volume cone cells, weak escape equalities, every norm tie, and unbounded shape and SPD-metric parameters. There is no remaining root, broom, norm chamber, generic-minor exception, or positive-volume realization stratum within this domain.

The new root0 proof uses **134 unconditional actual-moment certificates**. None needs a norm-order assumption or a squared-norm-ratio split. Their **3490 integer 9-by-9 blocks** pass independent scalar/direct reconstruction, integer Bareiss leading minors, and rational LDL checks. All successful coefficients were reconstructed again in an empty directory, with matching frozen output pins and completed terminal checks.

This is a graph-specific homogeneous **mono-unstable exclusion**, not a new universal nine-vertex obstruction. It supplies no attainer, V10/F10 theorem, or improved global complexity bound. No canonical C32 transport is claimed, and the older MP9:30/48 and 57-type claims are not restored.

```
root0_remaining = []
whole_graph_remaining = []
canonical_C32_transports = []
```

## 2. Authority and literal combinatorics

The immutable parent is `minimum-0039`, SHA-256 `a8dc9aab660b5e9b5a6b4db109797d548b9562b9dac14a8ca2fa04f55e999eee`. Its stated scope is whole roots3,4,5, including genuine cofacial triangulations, while root0 was explicitly open. This result uses that exact scope rather than treating the parent as an existing whole-graph theorem.

I authenticated the parent's **68993-byte** compact UTF-8 version2 JSON envelope, with the Markdown's final LF included, from the current `research-journal(7).md` checkpoint:

```
3486698 bytes
3fb11318fc0cab6a8742f00ff0af47b04490fef13d97ae4df84feb9a5fdad48d
```

The extracted parent recovery source reproduces:

```
recover_mp45_root3.py
41454 bytes
a9e3efea31bb10acbaa769ed2aa9603ba51417b6e4a6700af28da8df1052dc7b
```

Seven inherited source units match that authenticated capsule exactly. There was **no new incidence, alias, or source-pin conflict with E8**. Its corrected universal-output lengths, 1289123 and 41790 bytes, reproduce; the older erroneous late lengths 1330807 and 41787 are not used.

The complete oriented facet list, with indices0 through13 in this order, is

```
014,021,032,043,125,154,235,347,365,376,458,487,568,678.
```

The complete undirected edge list is

```
01,02,03,04,12,14,15,23,25,34,35,36,37,45,47,48,56,58,67,68,78.
```

This strict simplicial graph has `(V,E,F)=(9,21,14)`. **MP9:45 is neither canonical C32:45 nor canonical C32:139.** In a cofacial realization some displayed triangulation edges are diagonals, and the actual maximal-face/true-edge counts may be smaller. Such diagonals are never assumed available as physical escapes.

### What was and was not replayed

I did **not** rerun the closed root3 certificates or the historical multimillion-tree MP9 search. Root3 enters the whole-graph conclusion as the immutable E8 theorem. I freshly reconstructed and independently checked the small primal universal285 library and its terminal-cell omission certificate because they are the reduction dependencies for the new root0 proof. I then generated and solved root0's literal terminal-broom family from scratch. **No historical MP9 plan, serial offset, guessed root alignment, cap9 theorem, or C32 matching result is an input.**

## 3. Exhaustive root0 coverage

There are **36300 labelled spanning trees** of the literal graph, verified by the matrix-tree determinant. Two separate exhaustive enumerators—eight-edge subsets and rooted parent choices—give exactly the same **18150 root0 stabilizer-orbit representatives**. Parent arrays have `p[0]=0`; their representative is the lexicographically least relabeling under the root0 stabilizer, and indices are zero-based in the sorted representative list.

The complete root0 stabilizer is

```
[0,1,2,3,4,5,6,7,8]
[0,2,1,4,3,5,8,7,6].
```

A third enumeration traverses all permutations of the eight nonroot labels in the long-broom form. It independently recovers exactly 186 broom orbits, comprising 134 with the terminal listed triangle and 52 without it. Thus neither a numerical failure nor an inherited plan ledger defines the finite frontier.

| Exhaustive root0 class | Tree orbits | Exact exclusion |
|---|---:|---|
| Non-broom rooted shapes |17964|Reconstructed universal285 actual-fan certificates.|
| Brooms lacking the terminal listed boundary triangle |52|Reconstructed 55-block omission certificate.|
| Brooms with the terminal listed boundary triangle |134|New unconditional graph-specific certificates.|
| **Total** |**18150**|**No remainder.**|

The 134 terminal indices are listed completely here. Their complete literal parent arrays and broom-coordinate maps are deterministically generated by the inline capsule and frozen in `root0_enumeration.json` and `root0_report.json`.

```
1400,1403,1413,1421,1444,1451,1468,1475,1620,1622,1629,1630,1641,1646,
1649,1658,1661,1738,1743,1759,1765,1772,1782,1788,1793,1797,1878,1881,
1898,1901,1907,1914,1939,1942,1960,1970,1989,1992,2010,2020,2034,2036,
2044,2046,2050,2053,2061,2070,2073,2081,2142,2147,2172,2177,2202,2205,
2232,2235,2258,2269,2272,2283,2288,2296,3178,3180,3187,3188,3316,3321,
3456,3459,3662,3665,3675,3683,3752,3761,3778,3784,5501,5504,5522,5532,
6170,6172,6563,6585,7802,7804,7811,7812,7940,7945,8080,8083,8236,8239,
8249,8257,8864,8867,8882,9214,9217,9505,9514,9516,10767,10770,10788,
10798,10817,10820,10838,10848,10860,10863,10869,10876,10878,12130,12133,
12412,12674,12677,12687,12695,14539,14541,14543,14554,14564,14567.
```

These are **root0 ordinals**, not the parent's root3 ordinals.

### Certificate methods and what the search established

The complete 134-record library contains:

| Method | Records | Integer blocks |
|---|---:|---:|
| Ordinary two genuine apex fans |92|1826|
| Shared actual cells of two genuine fans |22|404|
| Complete oriented volume-cycle system, all nine fans |20|1260|
| **Total** |**134**|**3490**|

The 20 volume-cycle records have original root0 indices

```
3180,3188,3456,3662,3665,3752,3784,5501,5504,6172,
9214,9217,9516,10767,10770,12130,12133,12412,12674,12677.
```

They each have 1043 integer coefficients and 63 matrix blocks, using the apex order `[0,1,2,6,7,8,3,4,5]` and all ten oriented boundary-cycle directions. These records use the full cycle **volume** relations, each genuine fan's first moments, and common second moments. No record needed the stronger full-cycle first/second-moment locator, a norm disjunction, or a directed-redirection assumption.

The exploratory source tries the root fan, root-plus-one ordinary fans, root-plus-one shared fans, then all-nine volume-cycle and full-cycle systems. Every terminal broom was certified by the volume stage at latest. Failed earlier locator attempts are not infeasibility evidence; only the successful integer certificates are used. The final deterministic reconstruction runs the 134 recorded successful plans, not all unsuccessful proposals.

The new root0 component checks 31410 leading minors per arithmetic implementation. Including universal17416 blocks and omission55 blocks, the reconstructed root0 proof has **20961 blocks and 188649 minors**. Combining the new3490 graph-specific blocks with the parent's7477 graph-specific blocks and counting the shared reduction dependencies once gives a whole-graph proof of **28438 blocks and 255942 minors**. The latter is a composition count, not a claim that root3 was replayed in this assignment.

## 4. Continuous physical proof

### 4.1 Weak true-edge escapes give a covered tree

Translate the actual homogeneous body by its actual uniform-volume centroid. Let `X` have vertex rows `x_i`, take any common SPD metric `M`, and write `G=X M X^T` and `n_i=x_i^T M x_i`.

A strict unstable vertex has `x_i^T M(x_j-x_i)<0` along every incident true edge. If0 were the sole such vertex, each other vertex would have an incident true-edge neighbor `p(i)` with

```
D_i=x_i^T M(x_p(i)-x_i)>=0.
```

Distinct endpoints and positive definiteness give

```
n_p(i)-n_i=2D_i+||x_p(i)-x_i||_M^2>0.
```

The chosen arrows cannot cycle and therefore form a rooted spanning tree toward0. This includes `D_i=0`. There is no imposed total ordering among incomparable vertices. A maximum-norm vertex is always strictly unstable, so excluding a unique strict unstable vertex at every possible root proves at least two.

### 4.2 Universal and terminal-omission reduction

The reconstructed universal285 theorem excludes every nine-node rooted shape except

```
T=(0,0,1,2,3,4,5,6,0).
```

The complete rooted-shape enumeration is independently checked using multisets of rooted subtrees, yielding counts `[1,1,2,4,9,20,48,115,286]`. Its coefficient matrices use supersets of genuine apex fans. A slot absent from the chosen genuine fan has **incidence coefficient zero**: it is not assigned a fictitiously zero geometric tetrahedron volume. The same actual determinant mass is retained whenever a cell occurs.

For the surviving broom, label its vertices `b0,...,b8`, with `b0` the root, long arrows `bj -> b(j-1)` for1<=j<=7, and short arrow `b8 -> b0`. The omission certificate checks every root-apex four-set except `[b0,b5,b6,b7]`. If the terminal triangle `b5,b6,b7` were absent from the listed boundary triangulation, all cells of the actual root fan would lie in the 55 checked slots, giving the same positive-definite contradiction below. Hence the terminal listed triangle must be present. In the cofacial extension this means a triangle of the **genuine boundary triangulation**, not an unsupported assertion that it is an actual maximal triangular face.

These two reductions leave exactly the 134 newly certified parent arrays.

### 4.3 One actual determinant-mass family and all common moments

Cone every oriented boundary triangle not containing apex `a` to `a`. Do **not** remove a triangle merely because its original maximal facet contains the apex: a triangle elsewhere in that facet produces a flat tetrahedron with genuinely zero volume. Supporting-plane inequalities make every oriented cone determinant nonnegative. Rays from the apex show that these cones partition the body up to lower-dimensional overlaps.

There are 63 distinct unordered tetrahedra in the union of the nine fans. For `t={a,b,c,d}`, define one common actual six-volume

```
d_t=|det(x_b-x_a,x_c-x_a,x_d-x_a)|>=0.
```

Use this same `d_t` in every occurrence, every fan and every cycle identity. Let `f_at` indicate membership in fan `a`, let `chi_t` be the nine-entry vertex indicator, and put `J_t=chi_t chi_t^T+diag(chi_t)`. With `D=6 Vol(P)>0`, actual uniform-simplex integration gives

```
Σ_t f_at d_t = D,
X^T Σ_t f_at d_t chi_t = 0,
Σ_t f_at d_t X^T J_t X = 20 D Cov(P).
```

The total over the union of 63 cells is not asserted equal toD. The fan indicators and the same physical covariance tensor are retained.

The full oriented boundary matrix has 84 triple rows, 63 columns, rank53 and kernel dimension10. Signs are determined by the occurrence `(apex,outward triangle)` relative to the sorted four-set. Every relation used is independently checked by exact boundary annihilation, and modular rank lower bounds together with the annihilating independent rows prove that the complete rational kernel has been supplied.

For every cycle vector `beta`, the actual masses satisfy the full identities

```
Σ_t beta_t d_t = 0,
X^T Σ_t beta_t d_t chi_t = 0,
Σ_t beta_t d_t X^T J_t X = 0.
```

Indeed, the associated oriented tetrahedral chain has zero boundary. Integrating a polynomial by the divergence theorem cancels every boundary flux. For a homogeneous polynomial `q` of degree `k`, the vector field `x q(x)/(3+k)` has divergence `q`; this proves all three displayed identities. Degenerate tetrahedra have zero oriented integrals, so the argument includes flat cells exactly.

These are necessary identities of the **given realized body**, not a sufficiency claim for a fitted weight system. No independently feasible scalar masses, independent per-cell geometries, generic-minor inversion, or moment-rank assumption is used. In particular, exceptional shapes where degree-two moments do not determine the masses are fully retained: the proof substitutes the actual determinants directly.

### 4.4 Exact positive-definite contradiction

The integer escape form is

```
L_i=2e_i e_i^T-e_i e_p(i)^T-e_p(i)e_i^T,
tr(G L_i)=-2D_i<=0.
```

Each record supplies integer symmetric matrices `Q` composed of free first-moment terms, free fan-volume or cycle-volume offsets, common second-moment terms where applicable, and nonnegative multiples of these escape forms. The independent checker rejects any added comparison/order field in the new 134 unconditional records.

Weight the matrix contractions by the actual `f_at d_t` for ordinary fan occurrences, or by the common actual `d_t` for shared-cell records. Free first-moment terms cancel by actual centering. Offset terms cancel by the genuine fan/cycle volume equalities. Second-moment terms cancel by the common actual covariance tensor. Thus the weighted contraction equals a sum of nonpositive escape terms.

But every `Q-I` is strictly positive definite, verified with exact integer Bareiss leading minors and a separate rational LDL calculation. Since `G` is nonzero PSD and the actual total fan mass is positive, the same weighted contraction is strictly positive. This is the contradiction. It uses no positive lower bound on an individual cell mass, and remains valid when any allowed cells are flat.

## 5. Complete shape, metric and cofacial scope

The geometric domain consists of all full-dimensional convex hulls of the nine distinct **actual vertices** whose boundary is genuinely triangulated by the fourteen listed triangles, coherently oriented, with disjoint triangle interiors and true edges contained in the displayed graph. In the strict simplicial case the triangles are the maximal facets. In the cofacial case some are pieces of larger actual facets. Weak supporting determinants alone, without the genuine boundary and actual-vertex conditions, are not asserted to characterize this domain.

There is a complete ten-chart description at root0. Its fan triangles are

```
125,154,235,347,365,376,458,487,568,678.
```

Choose any one with positive cone determinant from0; at least one exists because the sum is `6 Vol(P)>0`. Put the **uncentered** apex `q0` at0 and that triangle's three vertices at the coordinate unit vectors. The remaining five vertices provide 15 unrestricted real shape parameters. This does not assume the tetrahedron0123 is nonflat. All ten possible positive choices are retained, including cofacial strata on which0123 is flat.

For each root0-fan triangle `f`, let

```
tau_f=det(q_f0-q0,q_f1-q0,q_f2-q0),
D=Σ_f tau_f,
B=Σ_f tau_f(q0+q_f0+q_f1+q_f2),
y_i=4D q_i-B.
```

The actual centered vertex is `x_i=y_i/(4D)`. The 15 shape parameters satisfy all actual support and genuine-boundary conditions; strict simplicial realizations satisfy the 84 strict nonincident supporting-tetrahedron tests. Cofacial equalities are allowed with the stated geometric conditions and positive selected chart determinant.

After an irrelevant positive metric scaling, all SPD metrics are represented by

```
M=[[1,u,v],[u,w,z],[v,z,t]],
w-u^2>0,
det(M)>0.
```

The five metric parameters have no upper or conditioning bound. Escapes are the polynomial inequalities `y_i^T M(y_p(i)-y_i)>=0`. The proof covers this entire unbounded 15-shape/5-metric domain in every chart, all weak escape walls, all norm ties and all exceptional moment-rank strata. Singular metrics, lower-dimensional hulls, nonvertices and nonuniform density are outside the stated problem, not unclosed branches inside it.

## 6. Independent actual-geometry controls

The additional `physical0.py` checker imports neither the numerical locator nor the root0 generator. It independently assembles all 3490 matrices directly and compares them with the scalar-polynomial construction, then repeats both exact positivity checks. It also reintegrates three exact convex bodies, reconstructing every supporting maximal face, its polygon cycle, all true edges, all nine actual vertices, actual centroid, all 63 determinant masses, all fan moments and every component of the cycle second tensor.

The common strict fixture is

```
0=(5,2,-6)   1=(5,5,-6)   2=(2,5,-6)
3=(0,0,0)    4=(12,0,0)   5=(0,12,0)
6=(2,5,6)    7=(5,2,6)    8=(5,5,6).
M=[[5,1,2],[1,4,1],[2,1,6]].
```

The metric's leading principal minors are5,19,97. The three exact controls are:

| Control | Complete modification of the fixture | Actual six-volume | Actual centroid | Flat cell / removed true edge |
|---|---|---:|---|---|
| Strict |None.|2700|`(4,4,0)`|None.|
| Cofacial1 |Multiply all vertices by4, then set vertex0 to`(11,-1,-33)`.|196560|`(5829/364,5301/364,-537/260)`|`0235` flat; edge23 removed.|
| Cofacial2 |Only set vertex3 to`(0,0,-6)`.|2700|`(4,4,-3/5)`|`0123` flat; edge02 removed.|

In cofacial1, triangles032 and235 form the actual polygon0352. In cofacial2, triangles021 and032 form the actual polygon0321. Both retain all nine actual vertices and have 13 maximal facets and 20 true edges. The second control explicitly tests a valid realization where a fixed0123 gauge would fail.

All 134 weighted certificate identities are checked on each control using its **actual** determinant masses and common metric. These controls test the physical identity implementation; they are **not** escape-tree feasible witnesses or mono-unstable counterexamples. The whole-domain theorem comes from the symbolic identities and exact matrices, not extrapolation from the three controls.

The independently matched scalar/minor stream SHA-256 is

`3e6e729fc59bae7f2accacaa12ad7546110c6fcc9b2b579a476b28b842621a10`.

The actual weighted-identity stream SHA-256 is

`525e05ee83b7a050aff739f044b15cec07ab7305effb79fc80feb89ab75738af`.

## 7. Exact root and automorphism transport

The full automorphism group is checked both by the boundary-incidence algorithm and by an independent degree-preserving permutation enumeration. Its twelve literal vertex maps are

```
[0,1,2,3,4,5,6,7,8]
[0,2,1,4,3,5,8,7,6]
[1,0,2,5,4,3,6,8,7]
[1,2,0,4,5,3,7,8,6]
[2,0,1,5,3,4,8,6,7]
[2,1,0,3,5,4,7,6,8]
[6,7,8,5,3,4,1,2,0]
[6,8,7,3,5,4,0,2,1]
[7,6,8,4,3,5,1,0,2]
[7,8,6,3,4,5,2,0,1]
[8,6,7,4,5,3,0,1,2]
[8,7,6,5,4,3,2,1,0].
```

The exact new root transports are:

```
0->1
vertices [1,0,2,5,4,3,6,8,7]
facets   [0,1,4,5,2,3,6,10,8,12,7,11,9,13]
orientation -1

0->2
vertices [2,0,1,5,3,4,8,6,7]
facets   [2,1,4,6,0,3,5,8,10,12,7,9,11,13]
orientation +1

0->6
vertices [6,7,8,5,3,4,1,2,0]
facets   [9,13,12,8,11,7,10,6,5,4,3,2,0,1]
orientation -1

0->7
vertices [7,6,8,4,3,5,1,0,2]
facets   [9,13,11,7,12,8,10,3,5,0,6,2,4,1]
orientation +1

0->8
vertices [8,6,7,4,5,3,0,1,2]
facets   [12,13,11,10,9,8,7,5,3,0,6,4,2,1]
orientation -1.
```

Every facet, every graph edge and the common orientation sign are checked. Relabeling an arbitrary realization is not an assumption that it is geometrically symmetric. A global orientation reversal changes no absolute determinant mass or physical equilibrium condition.

The other orbit is exactly `{3,4,5}`, already covered by E8's explicit maps. The two orbits exhaust all nine roots, giving the whole-graph theorem. **There is no canonical C32 transport in this result.** Applying it to a canonical C32 map still requires literal polygon facets, a genuine cofacial triangulation, true-edge containment, zero-cell accounting and canonical vertex/root maps. The graph number45 supplies none of those automatically.

## 8. Reconstruction parameters and observed terminal checks

The numerical environment was CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Linux x86-64, glibc2.41 and OpenBLAS0.3.30 with `OPENBLAS_CORETYPE=SkylakeX`. One BLAS thread was set **before subprocess startup**, with `OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`; four fork workers were used. Assertions remain enabled. No random input or geometric sample is needed.

All 134 successful records use rounding power8. Ordinary locators use `eps=1e-7,maxouter=11`; shared and volume-cycle locators use `eps=1e-8,maxouter=14`. The inherited barrier schedule is `.05*.18**iteration`, with at most70 inner Newton iterations and60 line-search halvings; the decrement threshold is `min(1e-7,tau*.001)` and the least-squares fallback uses `rcond=1e-14`. The complete source preserves the remaining normalization and solver details; `plans0.json` specifies every successful kind, apex selection and rounding input.

Both a standalone source capsule and the smaller exact-parent patch below completed **fresh cold reconstruction and separate frozen standard-library verification**. The patch was cold-run against the current journal and frozen-run against the literal parent source. Their corresponding transcripts and all frozen output pins agree byte-for-byte. No result is inferred from an elapsed time, partial case check or optimizer margin.

The literal completed cold-patch transcript is:

```text
NOVA54_ROOT0_THIRTEEN_SOURCE_AND_INPUT_FILES_EXTRACTED 80530 8a3421f9f44b1a0851fd4f6c116388d7d330bffd4de9bb1fcf7b7505975a1d02
SOURCE_MANIFEST0 1252 25a365649e6b00fd696eaef11de7cc3dfbe574d8b0ce1fcfc02b9ec3ef9c87eb
ROOT0_THREE_ENUMERATIONS_36300_LABELLED_18150_ORBITS_186_BROOMS_134_TERMINAL_PASS
RECONSTRUCTED universal
RECONSTRUCTED omission
RECONSTRUCTED_ROOT0_134 449498 2852b3ca0a214ace43a2c65492d219f2e1a60def8c50cbe5ba53a37ad489aa67
UNIVERSAL_285_STANDARD_LIBRARY_CHECK_EXECUTED
ROOT0_134_ACTUAL_CERTIFICATES_BAREISS_LDL_PASS 3490 31410 {'ordinary': 92, 'shared': 22, 'volume': 20}
ROOT0_REPORT 26278 4a017ae51b78938caae4bd40024fb7e39269275d2eb76366554d51945f05ea09
ROOT0_COVERAGE_17964_PLUS_52_PLUS_134_EQUALS_18150_PASS
NOVA54_MP45_ROOT0_ALL_CONTINUOUS_AND_GENUINE_COFACIAL_DOMAINS_PASS
NOVA54_WHOLE_MP45_BY_NEW_ROOT0_AND_IMMUTABLE_E8_ROOT3_PASS_NO_C32_TRANSPORT
ROOT0_INDEPENDENT_DIRECT_MATRIX_RECONSTRUCTION_PASS 134 3490
ROOT0_ACTUAL_DETERMINANT_ALL_FAN_AND_FULL_CYCLE_TENSOR_IDENTITIES_PASS
ROOT0_GENUINE_COFACIAL_0235_ZERO_CELL_TRUE_EDGE_23_REMOVED_PASS
ROOT0_GENUINE_COFACIAL_0123_ZERO_GAUGE_TRUE_EDGE_02_REMOVED_PASS
PHYSICAL0_REPORT 3579 fe338d01536c4bc7815b8203005f5a899b38de960e9f7aceed2762d3513c677b
NOVA54_MP45_ROOT0_ALL_FROZEN_OUTPUT_PINS_PASS
NOVA54_MP45_ROOT0_RECOVERY_ALL_SOURCE_OUTPUT_PINS_AND_EXACT_CHECKS_PASS
```

This transcript is 1336 bytes/SHA-256 `c4e74d383a76165b62639c7eb4f9810c91a1779d6a6768097e402401d754752a`. The completed frozen-check transcript is exactly the same text with the three reconstruction lines removed:1193 bytes/SHA-256 `cb1f306abca8b51da5dcc147f3739e1153f323226f6abcf0aa287ec6be8309b1`.

The separately completed universal-check transcript is:

```text
INDEPENDENT_ROOTED_MULTISET_ENUMERATION_PASS [1, 1, 2, 4, 9, 20, 48, 115, 286]
SCALAR_POLYNOMIAL_INTEGER_BAREISS_AND_FRACTION_LDL_PASS 17416 156744
ACTUAL_NINE_FAN_VOLUME_FIRST_COVARIANCE_AND_WEIGHTED_IDENTITY_PASS 285
BROOM_34_STRICT_REDIRECTIONS_AND_ONLY_ALTERNATE_2_TO_8_PASS
UNIVERSAL_285_EXCLUSION_PASS_ONE_BROOM_REMAINS_NO_V10_CLAIM
REPORT 41790 067c8ae69857aece263ccaeb5b1e05e4d401d90f13f5d8ee8d64e3847358acec
```

It is 417 bytes/SHA-256 `057d386eecaf3101d628a4ca46d38fcda69f7c3b92892aa81c60b78055bc6207`. Its redirection check is incidental to this proof; the new root0 records use only the eight selected escapes.

The optional source-provenance audit also completed:

```text
IMMUTABLE_E8_PARENT_68993_BYTES_AND_41454_BYTE_RECOVERY_AUTHENTICATED_PASS
SEVEN_INHERITED_SOURCE_UNITS_IDENTICAL_TO_E8_PASS
NO_ROOT3_REPLAY_AND_NO_HISTORICAL_MULTIGRAPH_PLAN_INPUT
```

That transcript is 181 bytes/SHA-256 `fe8f1d61a1228a0ef3ad608e65367d4815f7603fd523c92faf8233a64e19c0fb`.

### Exact source and output identities

| File | Bytes | SHA-256 |
|---|---:|---|
|`root0.py`|8838|`7ad258b13a9ecd7e7ef42d4aad4e8a7943e314c6036b912ff33444b20c00fe91`|
|`physical0.py`|8077|`8b304b6385b0a376242b98f0c0ed165d6104306942a650a1800d728bcd9dbd53`|
|`explore0.py`|1470|`9384301be85f1fec731834aa001b3427b9089d7c55c47834388d03026538fbaf`|
|`provenance0.py`|1964|`a55d9401feb4e3f727dded390559e3a2ace73138cc6994028350a512d7ee86d5`|
|`plans0.json`|4792|`c9eaa894ae17759dc01f0421e7fdb9bb144a26f2b872dfd8fdd353a956225b29`|
|`expected0.json`|809|`f265a21b49cf6a15e387248e4565537f785a2bde18a3a5922c0cbad9c70ae46e`|
|`source_manifest0.json`|1252|`25a365649e6b00fd696eaef11de7cc3dfbe574d8b0ce1fcfc02b9ec3ef9c87eb`|
|`root0_enumeration.json`|373296|`b2e204cbabc4cdb2351d3b2c8f7d1264966d2431639d3da627fd0283bc932bab`|
|`root0_certificates.json`|449498|`2852b3ca0a214ace43a2c65492d219f2e1a60def8c50cbe5ba53a37ad489aa67`|
|`root0_report.json`|26278|`4a017ae51b78938caae4bd40024fb7e39269275d2eb76366554d51945f05ea09`|
|`physical0_report.json`|3579|`fe338d01536c4bc7815b8203005f5a899b38de960e9f7aceed2762d3513c677b`|
|`omission.json`|4150|`60cbe644efafa3cec29c1a1a98173afc186de0563a1878d9acc621f58e99805c`|
|`quad_recovery/universal285.json`|1289123|`3a00b679c994255debd3acbe5d3230e336d1e292b9cf88507dc1d2c61fc94496`|
|`quad_recovery/universal285_verification.json`|41790|`067c8ae69857aece263ccaeb5b1e05e4d401d90f13f5d8ee8d64e3847358acec`|

These are computer-assisted exact-arithmetic checks, not proof-assistant formalization or external peer review. Their mathematical force is exact positivity plus the physical identities, not the numerical locator's diagnostics.

## 9. Complete runnable successor capsule

The following is an **exact patch against the fully literal, reconstructible E8 parent**, not a download-only dependency. It contains all six new source/input units, including every helper added in this assignment and every successful plan. It extracts only seven unchanged helpers from E8's authenticated source capsule. The input may be either the41454-byte `recover_mp45_root3.py` from immutable E8 Section7 or the exact current journal checkpoint identified above. Neither an old sandbox directory nor a historical coefficient archive is required.

Save it as `patch_mp45_root0.py`, UTF-8/LF including the final LF:

```
15249 bytes
708d64f7b3061fdc5d65b9e3807559893dd85eec13b3eb3b8d309888cfe96b7c
```

Reconstruct and independently check in an empty directory:

```text
python -S patch_mp45_root0.py 'research-journal(7).md'
python -S patch_mp45_root0.py 'research-journal(7).md' check
```

The equivalent commands may replace the journal argument with `recover_mp45_root3.py`. The patch does not launch the parent root3 search or check. Its `extract` mode only writes sources and is not a verification. The optional provenance command, after extraction, is:

```text
cd mp45_root0_recovery
python -S provenance0.py '/path/to/research-journal(7).md'
```

The new encoded source/input JSON is 26745 bytes/SHA-256 `e4cd21e7c6f62f39bdaa4c21b8698a7fb0e901f538a57f84c24e142889e47af5`. Combined with the seven exact parent helpers, the complete13-file JSON is 80530 bytes/SHA-256 `8a3421f9f44b1a0851fd4f6c116388d7d330bffd4de9bb1fcf7b7505975a1d02`. These checks bind the complete literal generator, checker and input, not only their filenames.

```python
"""NOVA54_MP45_WHOLE_GRAPH_ACTUAL_MOMENTS_V4, exact E8 successor patch.
Input: the literal E8 recover_mp45_root3.py (41454 bytes, pin below), OR
research-journal(7).md (3486698 bytes, pin below) containing immutable E8.
Save as patch_mp45_root0.py, UTF-8/LF/final LF, in an empty directory.
python -S patch_mp45_root0.py PARENT_SOURCE_OR_JOURNAL          # build + checks
python -S patch_mp45_root0.py PARENT_SOURCE_OR_JOURNAL extract  # sources only
python -S patch_mp45_root0.py PARENT_SOURCE_OR_JOURNAL check    # frozen checks
Numerical replay: CPython3.13.5, NumPy2.3.5, SciPy1.17.0, Linux x86_64,
glibc2.41, OpenBLAS0.3.30, SkylakeX, ONE thread set before startup, four fork workers.
No random input. All six new source/input units are encoded below.
Seven unchanged helpers come from the authenticated, literal E8 source checkpoint.
No old multimillion-tree plan or C32 transport is an input or an output.
"""
from pathlib import Path
import base64,zlib,json,hashlib,subprocess,sys,os
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
old=Path(sys.argv[1]).read_bytes()
source_pin=[41454,'a9e3efea31bb10acbaa769ed2aa9603ba51417b6e4a6700af28da8df1052dc7b']
if pin(old)!=source_pin:
 assert pin(old)==[3486698,'3fb11318fc0cab6a8742f00ff0af47b04490fef13d97ae4df84feb9a5fdad48d']
 s=old.decode('utf-8');a=s.index('## Parent minimum-0039')
 a=s.index('# NOVA54_MP45_ROOT3_WHOLE_DOMAIN_V3',a);body=s[a:].rstrip()+'\n'
 e=json.dumps(dict(version=2,result_markdown=body),ensure_ascii=False,separators=(',',':')).encode()
 assert pin(e)==[68993,'a8dc9aab660b5e9b5a6b4db109797d548b9562b9dac14a8ca2fa04f55e999eee']
 a=body.index(chr(34)*3+'NOVA54_MP45_ROOT3_WHOLE_DOMAIN_V3: complete source-only recovery.')
 e=body.index('\n```',a);old=(body[a:e]+'\n').encode()
assert pin(old)==source_pin
s=old.decode();b=''.join(s.split("B=r'''",1)[1].split("'''",1)[0].split()).encode()
assert pin(b)==[38698,'4e58d9936af4d3e1afff389806b2fdec3f482dbdbd7ec8353c440a6a71989a63']
raw=zlib.decompress(base64.b85decode(b))
assert pin(raw)==[101132,'18ee40d76bb29a630350dc639999008553fefe1ecad361b01293d6606340b5e6']
parent=json.loads(raw)
names=['nova54_recovery/comb.py','nova54_recovery/locator.py','nova54_recovery/exact_check.py',
 'quad_recovery/engine.py','quad_recovery/build_universal.py','quad_recovery/verify_universal.py','omission.py']
S={n:parent[n]for n in names}
B=r'''
c-qx{YjfK;vgr5oD>&KOqG;1zz905-s~lTNJQLfAC1*BAR&hZRvYAMfhNPU=$$!7y07#LPY-Td&emIrHCW%I)(dZW*jeL7XKd)$9
(nLG_P%N`&N6)_9K3gu*qDYq+`*i#4XkzKMrrthtv^b)UWziX#5i_Q-;m11BiSOyINoKL`ISJKl$0WMvdWlcs*fI2(?NQ(NG&{b1
HU%uJ`!7Wrlere=bhXUOx)sxQeJGz%)ASNew@oLuqS*CxJMs+8)HHi$6VLY}D5k!nQGe!=n9{^>9V0Pq-HaXAjYKPRk`>yf2d;0x
*Vv~7P*{ZOu50^Atm!k&GIZ+BlE{xD-Li<`%#6r$jbxU1vjp&(#J3&8up`6gxc^v_1c;B94>bSsk9C&9?}E$?&#v3k4bRsN6M#*k
X_4dlvF}@kZ6`EJOagqg6Vos?=&O_H)bNeSk7u4|Yi<(ji4i;cEcPwSclw$P;VGQ~L(BGvxjqh==D4v(sN;LKOK40D$Bbh_BRkSz
q^Olxnx6RDOgCqC;!)})jzvw+a!uO<-ijg1m&;NMW15$|C0cA6vV6<;00u}gA~Pl$F?0*6S|)*B*p_c3hVIV{suM>`=*)|46eBw#
z*y5IiRJl(IBv5gnynW!Z}-S_O~ZEpBr>R>S#d<7*ou?LfPqiU$cVj}o9KoEEOQdWGIhuF6Eh)>0b{Efo*BiyX+W)JLmde;02upX
5lshn*?Q!9zUjq;P%8pfX@)h6Tx$A;;~TD>7&LMn({XIuN^IS?>>2QsXecJ%Z?k7AYS(<3Q|)l|1yt*n{TY+|j)KNXj09=E1com2
L+O&<L60A(M9PvbR%IcPoJ!fUl+tWQNs&hBJT1RS@tmZK;*cY|&C&&SL0T5K*=(6h9|2k#$X9QMm(O3HjKa&Ci*WqvdU$d+l2!TY
;!Wqv#c!`$UzDR|aY(a=G+$<ukJCWbWk8%S7t)H9_wzK8M1ybOwQjxmQmDv8b+Mk8=_+5w6f8(~cbh@UA=W%hvjXI2ps8}Ud?2<}
OS7!hXyWA}Qt4+BmtlNQ<Bt+4q|@8%EI{0c^Cd}&0k%7kcgu;a9Oe`hCHev)I#873m%-UYzRSt#UY_1&w;9Nv^l6!Y9OTPS%F%6B
bw&&Veo$8d6i(z6fIrJqmA$NBD6&$X9#>-%OaPz6j7%_@$jdxQGXi~4C)#v6-S2!-$#jZ?LvV0%lHJjPuKEgtEA9bz(g*dhoI_V-
b)FXGfS37-GF2yX{3V`m7a(;^98|*4F-oz+Qkj2Yza`**Pzm3He57nZ@?`K*)zp=W6;)5YTxL{Z;F)?KoF1}ap~(PX)t3`_28v!5
@|1%t*JY5TaXHxA1FoqYUx1(sQsybhM3AWkn0}In(Cy$}MY4hkZ)>X7%&i_c+UAIJoW(!>&MlDq_f$Fjl&2*XV~!F8;u|j$AQI?N
IEq!CX5~P>zPcJ~;ft%A%QIO`c^@-%HeVO_!8l)wp60Y%=Na|}U+L$Vu1e{oK=B1Z8|FEVQ6W*z#){TMvRctB8Svf|Wj>$^<4cDt
J3IME7uVUxZ22ks6J2d}^yc!n%d6inv8(MqHhT!lH<Q9JBMTaaK_G|Wf}~j(%168D0v%g?Oj79HXArq?`LV|ODJ}1%jsZ9XQy0d|
tfZfTERe{LQ2)(xIUiUG@NflBjE%sVB49F%pAORnSq)H8RnXs(<_l1zIfz-8SKPj~48Wr-!X~zPG(Ne0IUEnq!q-=)C*!N@@WuJ%
`RLUU1Y}M#UP&$13uuw`Uq;<zs+BV}W#ujIg4wS_oTlAB2ZMqV0)|8a{z23wF}3)Nnz+nBV%9NsL?T%tfeBob`2kmZ2^p9#=V0`+
Q3=H)Pb4tKIhYq|na#hT^8n`4Tw(?ho32b6IFMX;nmd}Iv4r=u5QdK?fO33KrCItJM1mF)x4S7)nU*OnROW#eG`=Sp!`pO4%b7$$
pH~#D3Z+P1<&_@y7_0<_C@*24D>|6vhcU+f7XoIM6UL7k=7sox%J*X1_1u#JTT|oZd`@G5>3_rhych-LdNrp5{u4zL1V{y8LNO>%
3}j8WB+bwz%`_y<G9}%xCEd0ph)yKaawXG&->xHBwkKJhE7^`GIj$!k7AxT70Oj%m9Eq*!ssUDAS1nbC-v+!p)7o_v>u5mKNI4P;
JXs$+Fj-uy4@kz>bj8Z296ZjKMbWN6CWCZeSN?8J_ab~W@bQ4ukNhhGK)mV36`2**WLdUwqH?VFcG97U8kE&g<GK#V!Rf>A0+5UQ
;GJ4B=gjJ;NicagNjKz_)8h&Y;6;{1DnT8M266R}z=Kk8O~^J_18`R<nKRt)7`F}ezyUVfs?8sa>Oli1sNp~u;z3jKQGoC|hFaBS
LnMJ6t(ph|otZUk#oGJKc=H*Fe_;J!OnNsxeh1M)Fwu4O0REaLBBApZ8sq5Q#GFoyX>i~`>0Q2DuZrN?_hV4&1)1Zc@bn*43>2j*
B%*^CBi2zV3pk&VFYhMhM4wJo{0)H$XBNH~jgQJPVa`s<ehCC45YGe9Gr@t&SgnT*e6vfU>VkY8Km{cTG-l7hfV201YKUqk6e?wu
r(9?@lp`Q;;Q=Zu$Gppj1ubDL33!*mOr1=X%H4iYDppKp(;!2sna_Dx5<s1SBG|*2)3h>mu%wzl%O|V_bY?-trXw`eX||?6%rAjr
!=8UuoNM8#`*cW>WbnhxLkh)!Y`DVM!ns;8r=jM)a#YpGz6?;q_Oe3x1%?p;vto;llMVY3Vuk=5J9dm=o=t(r*cP}rn6BSZF*L_4
b``NSs|=PLD-_H%2_g@{Su8M`XQM=ehJ8OgU9KUt$Om9d%E{m(H(ZRr9}o{<tHyrvVl?@{<7)`e+AI@MVg&A;=D~!SE*6NZ5d*}I
&<VUv|3xPehUsifIGZp^;59+m@nxnk2R@$<c%1`Y2TX$0Kq{&rA_&9omJloPC{Yv~H_%rAbptGp4<;xzGldcJ={}v)8WRZG0f_G}
0SX)sQ_D(WIxww<O68x87DNFKRjF{X;RRdW5Rq^#X#*7drZz>WHKf*~SiCCgMtGEeaS@A|#4uwjCcl*{!Cq7X)X)PVEF6l%ak;8`
Tq@iugk1E#wX2md%WVn|S5IaxUW}xAN?kd@?;DlcNOMqQKNx%)7$EK6+s**YdO@Xc5Ple)B7+w(ePHUyXO!KpDf?xcFhD{Cf50Pl
rj0%mikQy9K?oe*O0Ho{Ke3UGRh-Sfx1@m8g8_F;K#~Bzj!0At8oqf$2m@`fWKv4)GG-rv%4AYbK?MdAWPxg`wldwtAuQGrpi?Zk
G?}(7+J-2>qJIfH)#AmYY(r#c0md&#-i9B*9nc%)_<1m?3it2<!w?YLO(ddh)#)_Of+p!bivrH}ME!&30!bTi%MfE#6xSn0#rvI&
Z=-0B%df2dq<}6!<vsR0n(j9c?y=ud7jd+OxUZ?jasiWurZul+?Wk!^w%9!bSv!*|qq*TYr@0NcHN4!hRE^h@@Xf&e%F&1(R+xUI
iyc{e8w8>i7-)oki_qc|v-!+hUI3N8%er#`fbe(k0%8gHd%)iH>E50J0`CL%m%*etwgAWog(3M+5!@nai|UQ5tA%E#7}aYKwMtbF
YEC}k5^~9wXWprN;u%5|0(0<rC}IX~P*t>e!ioyBQrkd9<%>%xv<jeMx$NSYWVi<KK?JL_whQJBVBo^t%|C^^X)5oOHBqFWL$3D0
Sw(G3aekb_Oaa$jUciI^)J@s2>-khg5Sr5@jF)_6uB0JftC*+Y^Z}k>Ur=1A3NBzuPhb|vEa=llt)c<xTA;W<g_eA?DxCIpmcr*n
Sm1;|2}_y*8$-c_W!{jl#wraPw<Ji^_rZJhW$;o3=BvL3zp6N>xb9QUbNHeHF3qt}X@x6qjit-4{QWCDeoV83zu^;nC{{G)A5dN4
!wHK6@H2Btv!8THYRJMlK*Nj~Tj~t3&0m7e0_m|BPW+DUzFzDUYnv=iWTinMKJnQW$H$DzPG84$z2WG<&&^Wk3a<a~FCAAlZPc3{
r&$3})&SQ))v^mIB6pzY2yxC*jP3Us4|6)_!Ew#VS*ozPT|tioQX(*tt|rVHG|jM;EN3XXm|2j|mxq{dJUP&hi<0DJ;P0IrgAoka
+rGDlwXxNPJ;P65!B7F%zGd%a`ThXvZ+Oa4YDzVA`#NFBjsSj&P8KlzwlVY#la%E=On(bp2FvHO@~~x&j!9Xy8&%O{dji5jy^du|
RVa9icJjkCc#HNiod#bg1T6f(U^9&%_`u25A(|=o10B))R(XWC)m&$-GTyg%&bY(n=pM!r#iQX0x2&mj#{&Zx^JqF*Pxrn~{Jm(O
uTeCZaiZ*~-{CP<B}edY-)E@r!F)u3bAzfg?$ge=Pbw-7-~l4~R$WfUfxgu&>mvz*NI4Ks2(_ysn{<@~cwGz25&QTDi=3bcJyw@W
PSUn;C|qSk(7UNW*zUzHYLu>oR<d>n;;;vU2ZFJG2S3<z$^)JIz2CXqAi{g~_iBaezEFQtlzn6GkG%m0uP`tH0C`dbnjdwu64)T2
Dxi1kqv~m}-WQx~Oxcly%`T4$Avc$ApgJ)29*)_|3Vuuv0(@hS@DJV))0dRa6RA|+Le0tp;L81g339cbi-w7>ex=Ixg5EJ(c7J4Z
ZEL%?ySv6*6fT@ThM}>$y0tUcFhpz(9U>yrLLX5A+#(Q*xrZ>=hV2ZL<7^RV$JM&}c5y9w;9F_dTKTEh>G?(jI=V@<m|w3~arp(R
<!QBK)$*PJR;pf@o^I1nqzN({*Mg?C*{cR(dK}G{@kg=Aae64W!K#fhwxRZ71dK@pNW+`AxW&<krGNw<fU*jWTnpKNONOHUQOR0T
sG@Fbx(;FOAIDJ?oE}Edy%eVGZ|nBpGkl*XbNqIHxLzeJR%`C6Ox~(dglmS`LYQ2!k^`DoR83b*P#KFv`w~V=!E7SKFhIO?{1TsE
!jN<V7Y>Z*z@zL3Sc}cZgfrNCxl!)4JMC-ftkS@wH!*>>?G0XX-8*<$tDW+svNo4UaC(5oluu&BLWWo&;ax`HN_uzmG2d)Cvnq{s
*!#nK`Z-A<$_A-s<GtBL<^17V(~DS$jM_rDS;%Y{aPD~cKy3wwonY&+xUdoZNsq>f-}$I~q+eQ_ERpi41LPF|3Dn``P1SELn|8|B
q7l?mYB7z#{p@N(Na!XS6ap;1H|Mesd$kC&PHyCdu}Q@y6r8!Xt5#FpMs<8D*i$v_eH7Otv*2FzzgFn0>F}RuVSDnqi6_B22i)3E
gzev0B-9BZpKUP~@RckxkdRwbxix7OyOCc4`SR-BiEV{^>-PNeZ1`pfKQ71N#mV^k{NLfp<yrXV)%(%;>B(#OHX4N|H)rSL@SQG;
;|K-%nZ|j91)o&zpdr{MTCG$#tVrrqsa3pLso{$!GIUCwZpjs&?~zZz)~5b3cc?oL&2@IWq5jtPc9TbE=hws2npN<8bvYVe-<*!m
uP(zkz${rs-T+J5rv+LFPfo`-z}vIoczAtret80TPhP(cUz}Vr=D)asm(%yBuZQ7ycsaVd4$rae^YQs`B-(fa`OD$u&H3dpJiU5x
a(WKUXohKr|2@3E3QvcC7^oeF!?Tye&@iC`7gz6wXFr2ghw2RL%aa>Gwn3{IKZ3TBFb#m;TwRZ4b&rkP3ZgF@gm$gR4_NSUjh`6U
99MjH^lUQGEe((FRdeLqXSf4tOjVEn#+^w^Gy5R)UI;_)gRrbV2)h@D<Mlzfb`OMOXuS|dFNEI*VfMCS>Aet6FGMdLHgb&5ba=Tf
%57fm=ueirW*^60t4}suyN^oO=^HiI?Hd!<>xby=i*I(g(Jgm-FnDfX8=luU?w<ejnE9ICQ{G3VuUk*{(>J$AOcxM3hp>!32uJIK
aC;%VKFRU@o>4b6UF(A|dLc~fX-WaY>4WIAe*oe1LD*VfE4JAO;plx3ZZAJvvk#(A$_>3wf&jwpgXpsg0MVlh1`K~sE5Ot~2(yn4
2tWEDY_G2s$M1va<%i*!y%4>0_&u_2>aN!Z;h~K2<wsG@wsS2!1f{xoh}WyWvUgr4>bf24)y3`oG;UMx>ziqGt*<M}T~=<{&QG^)
F;Dq;&m712Y1|I;u|HYY?a=_!@ysVFckQ32+}(;%I=FkK&GoFGZQZt+xBc0=f1zC#g+AJA+ctabmZLK}{wM~AThE`O&as^yKLdfM
{gj@#p4MZl0K)2n(Dh!3zE*ro>xJmC-Ja%Yy%0Ti*E39~7sBs@uzDfv9)IY0PB%8RM7br(-KWbv<Ee7r(0^JdpsxGVb#1L@6n$H_
dLe$=w(FYfxPPIttNn$_p7)d?006(og6a^@^-U@?uXkn*THy79Sp6V7rWP$BLlCnc#P4m$b^1ZPo`wwF{Q0qi%I42kwshm?D?6_B
S1P-Ip|ZCvYo@4R3J|~RUD^Pay~9|x$HlTOy$6S7_TsRu9vn_DfcsP<Q@*N~FCS<|vbdcAdbPrB1~Qjeu8Bm}<vp$@^Aui8s!11%
bxEQ*m4+VMQ%XzROS`AI+M7tla-GK%PZO1xb90`p*5#3u(}I#bzCZW?#ejX_Du;_il}yWX9N&}JBC#rsUY!`WBSmz+{KS%f(n1n7
FfR!AWk?2%0Zyr0N<dm8si>2ww9G{pc!CjhcRBl^B%sG~cfR6}h!oVZsy%I7RBa@%uq{wU?QFhAN^3{!Hp8`awsMXMKqS9=nCR2?
7W8c<_AaVb+aQ<-R;jW%i*y}kB(qqHN#qdEwTzjj&1M>zS#G3Rmaom|Og9tXCDcl0o;9P9PwZKO3C#)aUlajgJxnOB<qza_IXm!V
<(LG;A={1{$bb7Aa0B-^B~sjlL+``=_3-+{e+Yl`4&J{av(txHZ~r~Q{G?_jN$i1Kys>Py5n_hFzq)!o49~7EPR=jGcc!co<v3a<
UxH#nj;4n>3|P7vDEsp5Z6@DlG>iF;eX?GxiUHeV!E|yM(ZEnajMnoqT#)=@viy_<h)7XsR;+Uxk|Ivi;02i%R4wR=uw!dQFpyRF
b0jN@*t@9v+u|~mA(tJ`_f1tMUK0BRxa(+<P5sCwPGlvKuKBL-Cbs28n06oe35j)!crh_%M6+f#!1_L=6nRV-d4f0beLgTPWzXD~
dwFz(NertwEve9^1I(k7s-&<(q?|U9Bk%t6pZ_r4@*2Sai-E&*$~pUV=XoXUzlA0W`tMVd&L}bU2s%yTh!EHDX<`uKJDM302yApW
a;QZdR|CN_yaaeQ(>2>jVmHG6V_IdvF>gs)6v*=7hb1(PP$JRn_Sy3wmt`3Ymac$K)Sv5b+O*C|tNX)-z0;qFDU8R|#iF*Cz@R#y
9f?VGGMmjz&-XMZGG;)RIkP+?iQtb*W6!kB*s?U@5EqvUiDP0{R^$twAPLX}u)Zu-Ad1C+TZ6;MvqcA4E<l42Q4z_}HPBi^m35C&
OG{iQiVVcBnYNb1jtPR}Ynlg>Fi>8q)0iZtqeq%<_+|of=$IDDBHMl(HBYrvZQN$KjZ*}ZZWiG`_y*7yc`Lv0A61U^&ca5vAp^M0
B)NUp1I_NzjPly;l4zaIld!%EViyRz8{$hBroP_;-lqK80PGfSNV4u#89>Z{;+MAN41&=FzfQaIt`6k$%U8qebIhk5UEN%t4#U$|
CzmfVo0j2$Vdh(C=NA_@<CEv0l0z?ib8?OQlguuJ&)<)SBes{w^n|^$&B}Mf>-XWw&G;4WC!U^+t3A36($VnU@G{&Y;pXyuJQDkm
xGy}u;*GZIUS0`9aXozV`s6($0KUCCAC0fB`F8Tn>+$)^>ytOHLV&<_-rS63zJ161U(>}m4G=dyyr$Sby|}snYDVEZOBKEo<$VdJ
xdi_?<Y56g`}+ljxPT|+(p>mZbkf_2zK7D~QUYfVkL>fs8=q(W|0RdqNVZbzq}}c<517>>-qhv)t)$y=Fu>HkW|XVJXD*R}{G?+B
uvfufcVktcLl;03YKgjxKCm-VQRg@Sd_HdIWOMI7QmUlbdM7%n4~DY~F!;GZO4WQ>a=d94<1vPqrHUSJ&h&5Pzp(^3^3RAJ_*e%M
c0P@4@=q8xh+^@`KLiwjZQ4kkSO-A`5T=_P_yOff6RfPf&nd-w0y1_P(E!iyQOZu3%*je*Nu)d(51VDSisuV#&i%5JtnJfCsro@t
6b{=t59V#1;q(~U8K)L=IiTrHE^H8(;7GL2xqOk^@M5I$v<Qf>p`QU+t1Kfv$m&6eK+hM06&r>49=fzSBe<##QUkf|!{8j89dG_6
_;3{8Pd-em6U}MoJU0|-Q!vg3GL4d1!1689&G~8uAW|3LIh`uU503%~fGC)->|dT=h$k8tK~Y7-L!AW6kv>e1BJdR-I|-7k1kZRv
i|m<WZ60fcQa;zgv5%Dh`G$S?&eIN?C-~~7vAiCh$!Zc+`JL^9x&fZ29`7#O3}#eo;pR#it}%CkP@m&f!9{}~Obpoo5AMKTR73!P
&{&X#MmhEh`?zAqTs_^^ST1ZDd;^306+&y4^3pgW_x(7EIVR>`$I5YxiLS-Y+*jqex*#K%Opn30mmvC^!}+PY>c~`43)QBHmGVmv
#YemujBYX}ukv&s#;kdyE($6^#>2znd=^H?0W`!IBd+mKR0bGCm4s~i8cpmYZ;EOOOgO5juf`Rx<~gni+1&jhPM5MA3em}(HL$FL
7ULo^pRgPTfW1{640P9rsea8tJOG6l0^2~k|0cowI8T~VaU@anU|^SE3O$F}_<Wh&f#{Qz-`tU;1qR*VOYhmuLLjAwXn1+fGx{-R
qSU*I%uI&N4tkPcLN-V4pp4)-F*Lh)ML?iUkE2o~O_TXNst-6<MwSHZ;PKXK4X${pc$<U?-#qx{)K>$QB%NbpwOc=20T<R~D?J`h
yK-@f&{Hb=SgWD(c+RkGa#0Ocp>dV%?Iv?@tWB|61uR{pI=$Rd(<7nVfxya>54a0k5Mbe8r4qs!!;X0V(I;|Ixq+*WI+sC}8QeJO
t<(p|D+&2tDKoal)Y)mJ2}TEfn1t|tZ=P^uCMLL3F%}Fop-4rrDmIc?J*X^#f^G**v2OIF4gj_<2*Mc~zeY{|tGB4J6Phe!dF(DO
mFK2)uG@KaJ%pJ5^5y~}Dm-{N3Yl9CU!Oc5zJ3isJF}1B)%9}>+JU>_bEtU%kERuhGl#Et9?sibYNQGl*RGdMlpwkul%)8$``$0S
nu*;;g&@bwqN$j2rsDBsb+!CNbG4vz7M=tMxM4Uqf2~`?P)JxEaB7US-B)c1&jJBx>z1)c8^&&K-@^s*RwpVE2AOq280B^Ytf%<n
2QKNVBbX8tvS1UC!5w2Fif`>_m~0OkOT*l3tnSkQGsvE@Zu}aA+2ZLGQRt>f55+{_Z!4CWv&mZi-bxkanWA@D5q#4(o(^*dg}Lfh
N9AY$y%<eq3ueN2XsJJX$IACksKZ)ip-yoZu$RNtay96t3;Z-e$b-8&VP4o7bV&t>!-i~;8oYzxCMBK2`<w=K#j>CT3K5fT+?9yQ
c6%~$pGD=FnKUw^maBD=F`!pP+&o*TFkJ<iWOgGc?wW?IN-$vJGs&l00<^KIm8<x!u)A2y>DDD@D8OW$fW1mcNh%8=B0T(5-xIhA
r}*bh2!atH|0WEyytxE$D+Q`?qIWC#>93|;HN=fIBeH=uiBv2SftZ*lBCYBh05KZg<b!NEw?<5kU|6LAh3EkRL)4e4wV>twGI=au
ouj<u4co!RlqK0fBem00o=n-Q`w;|X%kt*Uysfg8#MMkJs*}9xyf17meBA8UEU8Ek8Oze3aob~kq2pE>bH^#58GyGW_{IrPE5cNs
m96r08&&=)fB&Dsw?=vj-XQX5vUK}8k>({Xm`cX3D#2DaDQ-LkJmBfq^;e$igHa_B>1<5(Dqb)HyVDg3-VC4+S{t;I)6`DtlJX~V
mjGXtW|mdrH9?x$6opGvef>kXUN;QEU_va#oer<Z=P%fT;wXH6ay>jBjl$PwRg94>RDTbCFiR$y?HurzcC2@`mSJV(Si~FM^;lf&
x&aL9ZEMhT$?%p<Vbe`D3~mllnrI^CpGrrih3wZ#y{;4sQ;P$!w$qr5GA!sp%U^;qj{4nl2_n0hIqr;cn^?a$vlp>8u2Fb)`*Mxu
Of=<<;O=7cbI_U*Z|oXNuB&dr6)W4w*DH)rw)xt+-1@P!)Me9XFqVv&`Y!qW64=XhL*o;zhS|J2<U>4IvYQrw=;c<nUimp_g;JY5
+TGbs{fo%5i1I?90wNB)L?Ylzm{ozuPkQr;r8{+3tu`JUSFe_fWez^NSg-=-X;to<ijv^Xk6+PtKRsP#%~VrlE{c5pOklz<;WCd>
AcIBxjcE<@u+=NHy*&l07CFRkmER!RxTKWL<J*a7nCiv9z?2+}^<4<KaPyL>H`nY?EVHzgT@0UaTKw0a${MS>T#b29eiq+i@D+G9
3KKDY@xyGBC8<?ek~7ZF`UF52&zBJHg@^=d^D`J~Mn8258qqk6?0nuXZeJPPVj^ZH;f-XIsru=DIj13ujoJk<$(HO&(D2kWn!THF
Y8w;65T>KS?s+MWHZ<OddfLE$Dl}s4qKn>z<B5Q*x}1fZ*j<(Xq%~G6E3*sNlNM;pRn;kG&B=B%2~g!P%2O$DZ1?Qs<uGK+UE!P8
H>1!t_;2)u!?$2iMq=*$MCMy}UtMF#f2UWM<MYd#s~f&=x0P?lcil%nfS6l3hW`2c@N)Qj)e4|(Z5i^tIz))ObSQx1>yyh7XVuPi
0nVjrDv+<m^6mnpFlZbS0kvbZIPpdK7oTX!Yz;xKueXF+Ec)V~A^5@|2!7WyEer(NaU9(0lA3dlptZ!zZ?a)j1dZC_yi2Q8;Ny$8
+}~CA%OC%#i<*D>rsiF@G}l+$v+J6>QzjmSw$_QdS2n9`+QKyV|L4Wb$2&O6M~~ktnLTi`zq$Ti-F1mRUWl)DuF+@TIv444xC+7P
)%9@v{>?CuM<2h;$w&HcxxPuUBzJ23DN#Y(*tX_mAlLS#yP+?u6M4tB{}i|0E3*Q14rNuEw6^(G(buUWa@&~*ELV8xBe~m`Lskrd
(j9<)l5xc0`DnATdx#n{LA9WtY0OWjP4|&zBtF0n6lH=dLQoGMX`Tm->Z9@5)y-H%Hp4%a=}Y6z^=jxhNy#|S$ePaW?0<f?-IxXa
_>8zK$J769wW-%6RdzQ=r#Y2R>y?&TG<g%&^O%lj*!Gd?jyuX5!@m(WaSY|p$$%;!;C~~r`=H6TpPVvj=?e9aNKRW~1W#@*&%v>c
z{lYKgfbd~pE$V&lX3q1`sDh3c=~F1`dc{s_we+F$y1vLJC=iRGWR3hZC>z>eQMDL_Js>&`~TL#^I>R-3+{NN>e!9C!c7>wthOW5
Th&`)U0sWN)Lr&}<kSvKMW7Vy1Tgc>%{Y8>ei>ezk1kHer?2YMInvXP{>Amxe-AIi4ThaQ{qcl%=5=qgXW#$p{{aaP;`s
'''
b=''.join(B.split()).encode('ascii');assert pin(b)==[11093, '128d93032dad8e79c65f408b6927f06134576806ef4156262dc8cb0e063c82b2']
raw=zlib.decompress(base64.b85decode(b));assert pin(raw)==[26745, 'e4cd21e7c6f62f39bdaa4c21b8698a7fb0e901f538a57f84c24e142889e47af5']
new=json.loads(raw);assert len(new)==6 and not set(new)&set(S);S.update(new)
raw=(json.dumps(S,sort_keys=True,separators=(',',':'))+'\n').encode()
assert pin(raw)==[80530,'8a3421f9f44b1a0851fd4f6c116388d7d330bffd4de9bb1fcf7b7505975a1d02']
root=Path('mp45_root0_recovery');root.mkdir(exist_ok=True);manifest={}
for name,text in sorted(S.items()):
 p=Path(name);assert not p.is_absolute() and '..'not in p.parts
 data=text.encode();manifest[name]=pin(data);p=root/p;p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():assert p.read_bytes()==data,('SOURCE_CHANGED',name)
 p.write_bytes(data)
m=(json.dumps(manifest,sort_keys=True,separators=(',',':'))+'\n').encode()
assert pin(m)==[1252,'25a365649e6b00fd696eaef11de7cc3dfbe574d8b0ce1fcfc02b9ec3ef9c87eb']
(root/'source_manifest0.json').write_bytes(m)
print('NOVA54_ROOT0_THIRTEEN_SOURCE_AND_INPUT_FILES_EXTRACTED',*pin(raw),flush=True)
print('SOURCE_MANIFEST0',*pin(m),flush=True)
mode=sys.argv[2]if len(sys.argv)>2 else'build';assert mode in('build','extract','check')
if mode!='extract':
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',OPENBLAS_CORETYPE='SkylakeX')
 args=[sys.executable]+(['-S']if mode=='check'else[])+['root0.py',mode]
 subprocess.run(args,cwd=root,env=env,check=True)
 print('NOVA54_MP45_ROOT0_RECOVERY_ALL_SOURCE_OUTPUT_PINS_AND_EXACT_CHECKS_PASS',flush=True)
```

## 10. Continuation and boundaries

**Retire all roots of the literal MP9:45 graph**, including root0's134 terminal brooms and the parent's eleven formerly difficult root3 trees. No further numerical sampling of these realization-and-metric domains is needed for the mono-unstable question.

The useful next application is a separately verified cofacial transport: provide a canonical map's actual polygon facets, explicitly triangulate them into this literal sphere with a vertex map, retain every true escape edge, and identify all flat cone cells. The new whole-graph theorem removes the need to route the unstable root into a particular MP9 orbit, but it does not remove any incidence or canonical-label obligation. Such transports have not been computed here and should not be confused with the separate eleven-dual-frame matching work.

The theorem's remaining uncertainty is the ordinary auditability of a finite computer-assisted proof, not an unclosed continuous branch: all new coefficients, coverage and physical cancellations have completed exact checks with cold-reconstruction pins. Root3's proof remains an explicitly identified immutable premise, rather than a falsely claimed new replay. The global bound and the accepted canonical-type register are unchanged by this handoff alone.

Supplementary files: Exact successor patch (`patch_mp45_root0.py`), standalone root0 recovery (`recover_mp45_root0.py`), and frozen proof bundle (`NOVA54_MP45_WHOLE_GRAPH_ACTUAL_MOMENTS_V4.zip`).

The standalone recovery contains all13 source/input files without requiring a parent-source argument:33979 bytes/SHA-256 `6c3afa9a8a0a0853e0dbd6309d0dfac338fbf8cb172976e565b7a99ac2ef5cd2`. It produced the same cold and frozen transcripts as the inline exact-parent patch.

The archive is814729 bytes/SHA-256 `00cb9761b0876da9de465c84f8d298208cf4a517932153061060d5102fe47800`; its34 manifest entries and ZIP integrity were checked. It includes the parent recovery source, new sources, frozen coefficients, reports and completed transcripts. The archive is a convenience; the inline patch and exact literal parent source are the complete durable reconstruction input.
