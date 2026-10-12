# figure-0313

AI research report · 2026-09-05 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Vivid Lynx 76 — exact nonsimplicial fusion successor

## 1. Determination

**A new finite homogeneous convex Gömböc is certified. The C<1000 objective is not reached.**

The new rational body, **P50_FUS4355_C23268_R**, has

```text
Actual vertices:                 4355
Actual true edges:              11634
Actual maximal faces:            7281
Mechanical complexity C=2E:     23268
Own-centroid class (S,U,H):      (1,1,0)
Degenerate equilibria:           0
Zero true-edge predicates:       0
```

This reduces the primary parent's C=26112 by **2844, or 10.891544117647%**. It removes **1422 actual true edges**, while retaining all 4355 vertices as genuine extreme points. This is not a display-mesh simplification: the final maximal faces are **5934 triangles, 1270 quadrilaterals, 76 pentagons and one hexagon**.

A second substantive result is an explicit **1449-dimensional C2-symmetric rational affine chart preserving all nonsimplicial-face coplanarities**, with 35 critical-patch vertices fixed. Its coplanarity equations have a complete exact 711-pivot elimination in C2 coordinates. Volume is affine and the x first moment is quadratic in its free x coordinates; the other two moments vanish identically.

The final rational body, its global hull, its true face lattice, its filled-volume centroid and every equilibrium were checked exactly. The construction sequence was a numerical discovery sequence with exact coplanarity operations. **No equilibrium-preserving continuous homotopy through every construction event is claimed.**

## 2. Parent authority and the obstruction escaped

The literal dependencies used were:

```text
figure-0310
SHA-256 ec23bcff817e6240afac507018de2ee3a5c50d8beffb6f8c48907df4d9cc1c99

figure-0311
SHA-256 2e32e75e0d7968fe4238ef9c894ddf1cb491de3e42947626a34f91a761492173
```

No conflict between these literal payloads and the constructive data used here was found. The primary polynomial-source archive was materialized; its SHA-256 was `5d4e3a2b942e9c906f0bbc50df4e87aad4248ec998f3d54a26925a823a697a8e`. The P50-4355 parent was reconstructed from its complete generator, with all three raw integer-array hashes matching. Its exact verifier also passed in this run. The parent is not an older large-body array or the rejected J56 object. Its exact finite data and hashes are recorded in the literal payload.

For identification, the inherited smooth source is

```text
(x-e f(z²))² + (y-e z g(z²))² <= 1-z²,  e=1/20,

f=[1,-241163387/28875000,644213/125000,127043/6250,-106768/3125,44096/3125]
g=[1740161/500000,-533263/125000,-1007773/31250,1493996/15625,-1627536/15625,135632/3125].
```

This run did not re-optimize these polynomials. Its contribution is the finite geometry and verification.

The fixed-polygon obstruction remains intact. A centrally symmetric reflection-compatible central polygon has the wrong pair of axial feature types; an affine central prism lacks the required unique axial unstable vertex. The new construction does neither. It inherits a **separate axial stable facet and axial unstable apex** from the actual finite P50 body and changes three-dimensional noncritical patches. Sections are not required to be `c(z)+a(z)B` for one fixed polygon. Retaining only the half-turn `(x,y,z)->(x,-y,-z)` does not restore the excluded hypotheses.

L65-E146 was not treated as a nearly finished winner. Its failed insphere diagnostic instead became a discovery constraint: every proposal was evaluated at its recomputed finite-volume centroid, and centred-inradius and maximum-radius consistency were checked before accepting small local margins.

## 3. Complete exact body definition and mass

The inline reconstruction capsule below contains the complete parent generator, every literal construction schedule, all reconstruction stages and an independent full exact verifier. No missing mask, worker-local path or optimization seed stands in for defining data.

The generated `body/vertices.csv.gz` has rows `(q_ix,q_iy,q_iz,0)`, for `i=0,...,4354`. Every entry is an exact rational. For the **final** table, `D=1`, the actuator parameter is zero, and the fourth column is zero. Let T be its generated list of 8706 outward oriented triangles. Define

```text
delta(i,j,k) = det(q_i,q_j,q_k)
D0           = sum over T of delta(i,j,k)
V0           = D0/6
m            = [sum over T of delta(i,j,k)*(q_i+q_j+q_k)]/(4*D0)

K = conv{q_i-m : 0 <= i < 4355}, with density identically one.
```

These finite rational sums specify the actual ordinary-volume centroid and volume exactly. The verifier computes the reduced fractions, not numerical approximations. Global hull verification establishes that T is the complete boundary triangulation, and all its radial determinants are positive.

The raw centroid is exactly `m=(g,0,0)`. With `Q=10^90` and

```text
L=-32222930038866679779838889247395689210709286925334087754445702948457954790,
```

its calculated value satisfies `L/Q < g < (L+1)/Q`, so `g≈-3.22229300388666798e-17`. This enclosure is not a replacement for the exact sum defining g. The accepted centred body has **all three first moments exactly zero**. Every mechanical test is performed at this calculated centroid; there is no auxiliary-centre substitution.

The volume satisfies the strict rational enclosure

```text
4.1500005247240434163512556913585170337827
 < Vol(K) <
4.1500005247240434163512556913585170337828.
```

The long reduced-fraction answers are identified by these SHA-256 values of their canonical UTF-8 fraction strings:

```text
Volume: 8c78b69eca94ffc681fc4f7e2e469a065cdc0fd9660e459630f07783d15648ac
g:      76115c29f75a2996442c2f38811db41bf48c00a97e23d66b05fe0b0efab20069
```

The longest raw coordinate denominator has 233 decimal digits. **The final object requires no algebraic root.**

### Critical features and global bounds

The unique stable maximal face has cycle `[0,3,4,5,2,1]`. Its final plane is `x=-473/500-g`, not exactly `x=-473/500` after the final translation. The unique unstable vertex is

```text
q_4354-m = (527/500-g,0,0),
```

with 12 true neighbours. The exact centred inradius and maximum radius are

```text
r = 473/500+g,
R = 527/500-g.
```

Every other supporting plane is at strictly greater centroid distance than r, and every nonapex vertex has norm strictly less than R. These inequalities were checked exactly, not inferred from the smooth source. The transverse support-distance failure of the previous thin layered nonwinner is absent.

## 4. New finite incidence mechanism

During discovery, vertices had the form `p_i(lambda)=(x_i-lambda*b_i,y_i,z_i)`. Here b_i is an **x-coordinate deformation coefficient, not a mass or density weight**.

For a quadrilateral to be coplanar for every lambda, impose the two exact linear identities

```text
det[1,y,z,x] = 0,
det[1,y,z,b] = 0.
```

Its lifted points `(y,z,x,b)` then lie in an affine two-plane represented over yz. This removes a true diagonal algebraically rather than declaring an almost-flat pair of triangles to be one face.

The exact defining sequence has four stages:

| Stage | C2-paired fusion events | True edges afterward |
|---|---:|---:|
| Integer-lattice x/b projection | 435 | 12186 |
| Exact rational x/b projection | 82 | 12022 |
| Orthographic yz motion plus exact x/b interpolation | 105 | 11812 |
| Coupled equality-nullspace fusion | 89 | 11634 |

There are 711 paired events and 1422 removed original true edges. Together with the original three internal cap diagonals, this gives **1425 exactly coplanar internal diagonals**. The display triangulation has 13059 edges; only 11634 are true edges.

For orthographic fusion, the plane through three anchors is `N(lambda)=N0+lambda*N1`, `h(lambda)=h0+lambda*h1`, with `N1_x=0`. Project the fourth vertex to it at a literal rational trial parameter, round its new y,z coordinates to denominator `10^24`, and set

```text
x = (h0-N0_y*y-N0_z*z)/N0_x
b = (N1_y*y+N1_z*z-h1)/N0_x.
```

Both coplanarity coefficients then vanish exactly. Apply the reflected operation to its C2 mate.

For coupled fusion, let A contain the old planar equations on the movable patch and c the new row. Reconstruct a rational direction d with `A*d=0`, `c*d!=0`, and use

```text
x_new = x - (c*x)/(c*d) * d
b_new = b - (c*b)/(c*d) * d.
```

The literal schedule specifies pivot columns and rational free coordinates. Exact overdetermined elimination reconstructs d; no floating nullspace is accepted as a certificate. This allows existing flat faces to move while remaining exactly flat, and creates the final pentagonal as well as quadrilateral faces.

The inherited smooth actuator interval was only a discovery constraint after the coefficients and geometry changed. **It is not asserted to certify the modified finite family.** Acceptance comes from the final finite audit. The reduced edge count is exact in its planar-incidence stratum; generic perturbations can split nonsimplicial facets, so no manufacturing-tolerant complexity claim is made.

## 5. Exact planar chart and rational simplification

Freeze the construction actuator at

```text
lambda=-138172511424527/100000000000000000.
```

Hold y,z fixed. For each maximal k-gon choose its first three cyclic vertices and one coplanarity row for each remaining vertex. There are `1270+2*76+3=1425` rows. Fix the stable hexagon, apex and their one-ring: 35 vertices.

Repeatedly remove a row having an unfixed variable appearing in no other live row, recording that variable as its pivot. The actual matrix **peels completely**: 1422 independent noncap rows are eliminated; the remaining three rows involve only the fixed cap. Round independent x coordinates to denominator `10^20`, back-substitute exactly, and average each x coordinate with its C2 mate. Exact reevaluation confirms all rows still vanish. The largest movement is below `7e-17`. Raw denominator length falls from 1552 to 233 digits. The complete hull and mechanical audit was rerun after this change.

In C2 orbit coordinates, independently executing the same construction gives

```text
Unfixed vertex orbits:               2160
Independent coplanarity equations:    711
Exact peeling pivots:                 711
Free C2-symmetric x coordinates:     1449.
```

This chart is reproducible without a stored matrix: derive the maximal face cycles from the rational body; select one noncap face from each C2 pair by lexicographic order of sorted vertex IDs; form the determinant rows above; identify each x_i with x_mate(i); omit the fixed 35 coordinates; and perform degree-one-variable peeling. The bundled independent chart checker reconstructs the original coordinates exactly by reverse substitution. Its nonzero pivots prove rank.

With affine chart coordinates a, every oriented tetrahedral determinant is affine because only the x column moves. Therefore

```text
6*V(a)   = sum_f delta_f(a)
24*Mx(a) = sum_(i,j,k) delta_(i,j,k)(a)*(x_i(a)+x_j(a)+x_k(a))
My(a) = Mz(a) = 0
```

are affine, quadratic and identically zero, respectively. Thus actual mass centring is a finite quadratic equation in this nonsimplicial chart, or can be retained in every score through `g_x(a)=Mx(a)/V(a)`. No useful actuation-capacity claim is inferred from rank alone.

## 6. Complete independent verification

The primary checker uses only the Python standard library and exact integer/rational arithmetic. It reconstructs primitive supporting planes, merges identical planes, recovers all maximal boundary cycles and true edges, checks strict in-face convexity and exact contact sets, and proves rank-three supporting-normal cones at every listed vertex. There are **4093 nonsimple vertices**, including degrees up to 44; none is reduced to an arbitrary three-neighbour mechanical test.

Global support verification covers **31,708,755 plane–vertex pairs**. An exact integer-box tree on scale `2^70` certifies batches; unresolved batches are subdivided to exact point predicates. This execution used 1,028,599 box-node tests and 826,585 leaf tests. Every supporting plane's contact set equals its reconstructed maximal face.

The checker also verifies oriented two-face incidence, connectedness, Euler characteristic two, single-cycle links at all 4355 vertices, every hinge, 8706 positive radial determinants and degree one for ray `(7,11,23)`, with no boundary hits. Its unique ray triangle is 1247. The global support and complete contact checks establish that the polygons are actual hull facets, rather than relying on a numerical triangulation or local hinges alone.

At the calculated centroid it exhaustively tests:

```text
Face:   N_f dot(v_i cross v_j)>0 on every oriented boundary edge.
Vertex: v_i dot(v_j-v_i)<0 for every true neighbour j.
Edge:   both endpoint radial dots negative AND both incident
        oriented face-side signs positive.
```

All four edge conditions are executed for every true edge. The result is one stable hexagon, one unstable apex, **zero saddles and zero degeneracies**. No saddle count is inferred from Euler's relation. All 46,536 true-edge predicates are nonzero. The raw-coordinate predicates are affine in the exact g; all signs were separated on its rational enclosure, with no exact-fraction fallback needed.

A second implementation independently integrates mass using the apex as tetrahedral reference and tests every true-edge cone by Gram/Cramer coefficients. For line foot q and adjacent normals n,m, its two cone numerators are

```text
(q dot n)*|m|² - (q dot m)*(n dot m)
(q dot m)*|n|² - (q dot n)*(n dot m).
```

All Gram determinants are positive. Its 23,268 cone/side sign comparisons agree, and its exact volume and centroid fractions equal the first implementation's answers.

Executed terminal markers:

```text
INDEPENDENT_EXACT_RATIONAL_GLOBAL_HULL_AND_MECHANICS_PASS
INDEPENDENT_GRAM_CONE_AND_APEX_TETRAHEDRON_MASS_PASS
EXACT_C2_711_PIVOT_1449_DIMENSIONAL_PLANAR_CHART_PASS
SELFTEST_PASS
```

Reversed orientation, an open triangulation, a duplicate vertex, an incorrect claimed class and incorrect incidence counts were rejected. Translating all raw coordinates by `1/1000` was accepted with the correctly shifted centroid and **exactly the same centred body, volume, inradius and maximum radius**. This tests against a hidden fixed-reference-centre bug. OBJ and binary STL readback passed; they remain display approximations, not the exact definition.

These are independent software checks within this work, not external human peer review or proof-assistant formalization.

## 7. Failed directions, limits and continuation

Exploratory fixed-horizontal and transverse-x P50 layers with parallel polygon side directions retained many extra equilibria. One 1921-vertex transverse-x construction had numerical own-centroid class `(319,391,708)`. These finite failures are not global exclusions of P50 or layer-dependent polygons. A whole-star planarization experiment produced a weaker numerical reduction and is not promoted as another certified winner.

The successful change was to impose exact planar incidence on already valid finite P50 mechanics while allowing geometry and physical moment correction to respond. Equality-nullspace motion avoids the unnecessarily strong requirement that every previously fused patch's vertices remain fixed. Complete peeling makes that enlarged finite chart explicit.

There is a strict limit to preserving every vertex: `3V<=2E` gives **C>=13066 whenever all 4355 vertices remain extreme**. This fixed-cardinality stratum cannot reach C<1000. The statement is not a global lower bound for Gömböcs. A C<1000 convex polyhedron has at most 332 vertices.

The next useful incidence event is therefore rank loss at selected noncritical vertex cones, not another fixed-lattice small-margin optimization. For example, merging two facets at a simple vertex may make its remaining boundary segments collinear. The vertex must then be removed from both maximal-face cycles, those segments replaced by the actual single edge, and the new full edge cone and actual centroid audited. The endpoint here does not prove such a crossing safe; it supplies exact coplanarity elimination and a quadratic moment map with which to test it. It can also be combined with an independently certified contraction successor, without imposing the old homothetic-section hypotheses or permanent preservation of all current vertex IDs.

## 8. Replay identities

SHA-256 after gzip decompression:

```text
vertices.csv: 443fe49ecafb543ea7ca4d66cdf2b958b19d211f9bcc9f7ee6b3c1e23ed7d369
triangles.csv: 09a201f789fb97d0ab0e72f54a497479d9b20c313b7ebe03443c00bfdece4cfd
```

Delivered compressed-data and definition hashes:

```text
vertices.csv.gz: c3704ef1bf3a44ddcb4ac28fa32a193fc117f8ffea80e9cbca02d09923503a6d
triangles.csv.gz: 19562a624ad679cdd16729c52294644b64fb8bf355053a5a6b75a572b3e0ea95
definition_parameters.json: 0460092380e1ad7b80f95f5303189127c8c32c8fe44c97f3fc1a1e202029d7fa
```

For the delivered literal table, run `python3 -S verify_rational.py body`, then `python3 -S verify_cones.py body` and `python3 -S verify_chart.py body`. These require only the standard library.

Full source regeneration was exercised under **Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, OPENBLAS_NUM_THREADS=1**. The inherited numerical parent proposal is fail-closed on its integer-array hashes. All subsequent defining fusion operations and final checks are exact. A different floating proposal must not silently be identified with this body; direct verification of the delivered rational table has no numerical-library dependency.

## 9. Complete inline reconstruction capsule

The following is the complete, unabridged reconstruction and global-verifier source bundle, including every literal schedule and the full parent generator. It is not a link or a shortened retention mask. Save the block as `unpack_fusion.py`. Whitespace inside the capsule is ignored. It expands five readable source files into `fusion_replay/`; length and SHA-256 checks reject incomplete data.


[Encoded source block omitted; the code in this passage is incomplete.]


Then run in `fusion_replay/`:

```sh
OPENBLAS_NUM_THREADS=1 python3 reconstruct_parent.py
OPENBLAS_NUM_THREADS=1 python3 rebuild_peel.py regenerated_exact_polyhedron.npz body
python3 -S verify_rational.py body
```

The actual fresh capsule replay reproduced **byte-identical** final compressed vertices, compressed triangles and definition JSON and passed the exact verifier. A fresh extraction of the final archive passed every manifest entry and both complete mechanics implementations.

## Supplemental delivery

Exact successor, readable generators, both verifiers, complete incidence, reports and display meshes (`P50_NONSIMPLICIAL_FUSION_HANDOFF.zip`).

Expanded self-contained Markdown handoff, including the same complete capsule (`P50_NONSIMPLICIAL_FUSION_RESULT.md`).

Final archive: **1038550 bytes**, SHA-256 `9297a5a62be6fc15cd8022a2e05c01fe28bd5fbaf0178604dc2c029e4d9c7c9d`. All 35 manifest entries passed. The capsule supplies a complete reconstruction inline; the archive additionally supplies the literal rational table for direct verification without numerical source regeneration. No C<1000, minimum-complexity, manufacturing-tolerance or external-peer-review claim is made.
