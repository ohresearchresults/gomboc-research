# figure-0275

AI research report · 2026-09-03 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# Keen Quartz 89 — global eight-vertex synthesis determination

## Disposition

**USED EXACT NONWINNER. No literal homogeneous convex polyhedral Gömböc was obtained.**

This continuation does materially change the low-vertex frontier. It provides:

- a complete exact combinatorial enumeration of all eight-vertex convex 3-polytope types;
- one exact generic realization anchor for every simplicial eight-vertex type;
- a new exact uniform-density eight-vertex polyhedron at its own ordinary-volume centroid with strict class `(S,U,H)=(2,1,1)` and a six-dimensional positive chamber;
- a clean identification of the first incidence mechanism not represented by the completed simplicial and affine atlases.

No global eight-vertex impossibility theorem is claimed. The inherited exact theorem still proves only that a strict homogeneous polyhedral Gömböc needs at least eight vertices. It exactly closes all systems through seven vertices, while the eight-vertex simplicial ledger retains 24,835 unresolved labeled necessary systems. The prior numerical continuation closed none of those systems exactly, so its unresolved counts remained unchanged. 

## 1. Complete eight-vertex combinatorial atlas

I generated and independently verified **all 257 unlabeled simple 3-connected planar graphs on eight vertices**. By Steinitz, these are exactly the combinatorial types of convex three-dimensional polytopes with eight vertices.

```text
all eight-vertex types     257
simplicial types            14
nonsimplicial types        243
```

The finite generation is exact:

1. Begin with one maximal-planar graph on eight vertices.
2. Close its legal diagonal-flip graph; exact canonicalization over all `8!` labelings yields precisely 14 maximal-planar types.
3. Recursively delete every edge whose removal preserves minimum degree at least three and vertex-connectivity at least three.
4. Canonicalize every descendant over all vertex permutations.
5. Verify planarity, 3-connectivity, face walks, Euler characteristic, pairwise nonisomorphism, and closure under every admissible one-edge deletion.

This establishes complete **incidence coverage**, not complete semialgebraic realization-space coverage.

- Complete 257-type combinatorial atlas (`complete_8vertex_combinatorial_atlas.json`)
- Independent combinatorial verifier (`verify_combinatorial_atlas.py`)
- Independent verification transcript (`verify_combinatorial_atlas.log`)

The verifier ends with:

```text
INDEPENDENT_COMPLETE_V8_COMBINATORIAL_ATLAS_PASS
types=257 simplicial=14 nonsimplicial=243
```

## 2. Exact realization anchors for every simplicial type

The package contains one exact integer-coordinate, generic convex realization for each of the 14 simplicial combinatorial types. For every anchor, the reconstruction independently:

- enumerates all 56 point triples;
- recovers exactly 12 maximal triangular faces and 18 true edges;
- computes the exact ordinary volume and own centroid;
- translates to exact zero first moments;
- audits every stable-face barycentric component;
- audits every vertex normal cone;
- audits all four components of every true-edge saddle cone.

None of the 14 selected exact anchors is `(1,1,0)`. These are exact representative chambers, not exclusions of the complete realization space of any type.

- Exact 14-type anchor atlas (`anchor_certificates.json`)
- Anchor-atlas summary (`atlas_summary.json`)
- Independent exact anchor verifier (`verify_exact_anchor_atlas.py`)

The exact inherited accounting therefore remains:

```text
labeled simplicial necessary systems     3,237,069
exactly excluded before this direction   3,212,234
remaining labeled systems                   24,835
remaining rooted automorphism orbits        17,253
remaining stable-face chambers              207,036
```

## 3. Strongest promoted exact endpoint

The strongest exact body found in this direction is an affine image of the exact eight-vertex wall cage. It is dramatically smaller than the 61-vertex M42 benchmark while attaining the same equilibrium class:

```text
supplied vertices       8
active vertices         8
true edges             18
maximal faces          12
Euler characteristic    2
complexity              36
(S,U,H)              (2,1,1)
```

All maximal faces are actual triangles. The display mesh therefore contains no artificial face diagonal.

### Exact source and reconstruction formula

Let

```text
D = 2^24.
```

The uncentred exact source rows are

```text
0  = (  2382238,  -6308946,  46171779)/D
C  = (-19656014, -12570508, -84150451)/D
H  = ( -1678613,  11935619, -25478204)/D
Z  = (  8010895, -10409701,  39298476)/D
AB = (  1683954,  13081292, -39025397)/D
AD = (  2466433, -19765281,  18154812)/D
AE = (  5834590,  17237355, -20273721)/D
AG = (  7455840,   3175317, -13504557)/D.
```

Their exact ordinary-volume centroid is

```text
c = (
 -692401880820759385581342313
 /11535075208344777980868558848,

 -258294341305269210560387714509
 /1476489626668131581551175532544,

 -531543412465115174050553320847
 /738244813334065790775587766272
).
```

Set `q_i=r_i-c`. Let `A` be the literal exact positive-determinant lower-triangular dyadic matrix stored in both files below. The final exact vertices are

```text
p_i = A q_i.
```

- Exact affine matrix (`affine_map_exact.csv`)
- Frozen self-contained source and matrix (`frozen_source.json`)
- Frozen-source verifier (`verify_frozen_source.py`)

The exact volume satisfies

```text
Vol(P) = det(A)
       * 44002819856051551745867
         /14167099448608935641088
       > 0.
```

Because the source centroid after subtraction of `c` is exactly zero, affine covariance gives

```text
C(P) = A C(Q) = 0
```

identically. A separate oriented-boundary tetrahedral sum independently returns all three first moments exactly zero. The expanded rational volume and exact determinant are included in `certificate.json`.

### Actual maximal faces

```text
[0,H,C]       [0,C,AD]      [0,AE,H]      [0,AD,Z]
[0,Z,AE]      [C,H,AB]      [C,AB,AG]     [C,AG,AD]
[H,AE,AB]     [Z,AD,AG]     [Z,AG,AE]     [AB,AE,AG]
```

### Actual true edges

```text
[0,C] [0,H] [0,Z] [0,AD] [0,AE]
[C,H] [C,AB] [C,AD] [C,AG]
[H,AB] [H,AE]
[Z,AD] [Z,AE] [Z,AG]
[AB,AE] [AB,AG] [AD,AG] [AE,AG]
```

Every edge belongs to exactly two maximal faces, and

```text
8 - 18 + 12 = 2.
```

### Exhaustive own-centroid mechanics

The complete exact classification is

```text
stable maximal faces   [0,H,C], [C,AG,AD]
unstable vertices      C
saddle true edges      [C,AD]
```

Thus this is one stable–saddle pair from the target and already has the desired unique unstable vertex.

Every other face has an exact negative barycentric witness. Every other vertex has an exact negative directed support. Every other true edge has an exact negative member among

```text
edge-foot parameter t,
1-t,
incident-normal coefficient beta1,
incident-normal coefficient beta2.
```

All normalized endpoint nonincidence, active-equilibrium, and inactive-feature margins exceed the conservative common reported lower bound

```text
10^-12.
```

The underlying signs are exact rational signs; the decimal lower bound is only a compact presentation.

- Principal exact certificate (`certificate.json`)
- Exact own-centred V-data (`vertices_centered_exact.csv`)
- Complete irredundant H-data (`H_irredundant.json`)
- Maximal-face cycles (`face_cycles.json`)
- True-edge incidence (`true_edges.csv`)
- Every face cone (`faces_full_cones.json`)
- Every vertex cone (`vertices_full_cones.json`)
- Every four-component edge cone (`true_edges_full_cones.json`)

### Complete directed-arrow census

The exact arrow audit includes both directions of all 18 primal true edges and all 18 adjacent-face edges in the polar. Mutual arrows are checked against the exact squared-distance identity rather than inferred from equilibrium labels.

- Complete primal and polar arrow census (`complete_external_arrow_census.json`)
- Arrow-census constructor (`build_external_arrow_census.py`)

## 4. Positive exact chamber

The six nonzero lower-triangular entries of `A` vary independently through

```text
|delta A_ij| <= 2^-80.
```

Throughout the complete box:

- `det(A)>0`;
- the own centroid remains exactly zero by affine covariance;
- the 12 maximal faces and 18 true edges remain unchanged;
- every face, vertex, and four-component edge-cone sign remains strict;
- the class remains `(2,1,1)`.

The interval certificate supplies a strictly positive rational lower bound for every active witness and a strictly negative rational upper bound for every selected exclusion witness.

- Exact six-dimensional perturbation certificate (`affine_perturbation_certificate.json`)
- Independent exact endpoint verifier (`verify_independent.py`)
- Verification transcript (`verify_independent.log`)

The verifier ends with

```text
INDEPENDENT_EXACT_V8_211_AFFINE_ENDPOINT_PASS
class=2,1,1 centroid=0 mesh=watertight box=2^-80
```

## 5. Watertight display mesh

The promoted endpoint mesh contains exactly the eight certified vertices and the twelve certified maximal triangular faces. Independent replay obtains 18 mesh edges, each with multiplicity two, and Euler characteristic two. OBJ and STL contain the same triangle set.

- Watertight OBJ (`body.obj`)
- Watertight STL (`body.stl`)

## 6. Search architecture and honest scope

The completed empirical work includes:

```text
generic topology-free eight-point clouds across simplicial types;
exact realization-anchor generation for all 14 simplicial types;
500,000 random determinant-normalized affine metrics;
12 global affine target differential-evolution runs;
48 dedicated affine U-H cancellation searches;
targeted fixed-feature and differentiable searches;
a dedicated seven-gonal-pyramid search;
32 global differential-evolution runs on the first coplanar
saddle-diagonal gate.
```

No robust numerical `(1,1,0)` point passed the complete hull classifier in those recorded searches. These nonhits are empirical and remove no unresolved exact necessary system.

- Numerical search-scope ledger (`numerical_search_scope.json`)
- Inherited broad-search report (`inherited_global_search_report.json`)
- Unchanged exact frontier counts (`inherited_V8_frontier_counts.json`)

Prior global low-vertex work likewise reported all fourteen simplicial graph types, differentiable fixed-cell searches, topology-free searches, controlled splits, and nonsimplicial cube/prismatoid scans without an exact target; its nonhits were explicitly numerical rather than exclusions.

## 7. Rigorous conclusions and nonclaims

The following statements are exact within their stated scopes:

1. Every strict homogeneous polyhedral Gömböc has at least eight vertices.
2. Exactly 257 combinatorial convex-polytope types have eight vertices.
3. Exactly 14 of those types are simplicial; 243 are nonsimplicial.
4. Every simplicial type has one exact reconstructed anchor in this package.
5. None of those 14 selected anchors is `(1,1,0)`.
6. The promoted six-dimensional affine box is entirely strict `(2,1,1)`.
7. The exact 24-dimensional source-cage box is entirely strict `(2,2,2)`.
8. No numerical nonhit is counted as an exact exclusion.
9. The inherited 24,835 labeled necessary systems remain unresolved.

What is **not** proved:

```text
No global impossibility of an eight-vertex Gömböc is claimed.
No complete realization-space atlas for the 257 types is claimed.
No full exclusion of any simplicial type follows from one anchor.
No full exclusion follows from the affine, pyramid, or coplanar searches.
```

## 8. First genuinely unrepresented incidence mechanism

The exact `(2,1,1)` endpoint has the ideal unique unstable vertex already. Its remaining stable face and sole saddle share the diagonal `[C,AD]`:

```text
extra stable triangle  [C,AG,AD]
sole saddle edge       [C,AD]
adjacent face          [0,C,AD].
```

The smallest incidence change capable of deleting both at once is the **QCAD carrier-free quadrilateral gate**.

At the wall, merge

```text
[0,C,AD]
[C,AG,AD]
```

into the actual maximal quadrilateral

```text
[0,C,AG,AD].
```

The wall has

```text
(V,E,F) = (8,17,11),
```

and true edge `[C,AD]` is absent. On the opposite simplicial side the replacement diagonal is `[0,AG]`.

A winning QCAD realization must satisfy simultaneously:

```text
only stable face       [0,H,C]
only unstable vertex   C
no saddle true edge
quadrilateral [0,C,AG,AD] strictly nonstable
replacement diagonal [0,AG] nonsaddle on the adjacent side
no nonprotected all-positive inserted or star-changed carrier.
```

This mechanism is genuinely outside the completed affine atlas. For every invertible affine map,

```text
det(Ap0,ApC,ApAD,ApAG)
  = det(A) det(p0,pC,pAD,pAG),
```

so a nonzero four-point circuit cannot become coplanar inside the affine chamber.

A targeted eight-parameter family—two coplanar shape controls plus six affine controls—was searched with 32 global differential-evolution runs. It produced no numerical winner, but that is not an exact exclusion.

- Exact next-incidence specification (`first_uncovered_quadrilateral_gate.json`)
- Coplanar-gate search report (`quadrilateral_gate_search_report.json`)
- Reproducible search implementation (`search_quad_gate.py`)

### Required continuation

Branch exactly over the finite face, vertex, and four-component edge exclusion disjunctions of the `E=17` QCAD graph. Eliminate translation through exact ordinary-centroid formulas, fix an affine gauge, and use rational interval branch-and-bound on the remaining plane-shape and metric controls. Promote only an isolated box with a common positive target margin.

If every QCAD chamber transfers the pair, the next unrepresented type is a codimension-two **two-quadrilateral shared-edge or shared-vertex gate** in which both the old saddle diagonal and its replacement carrier are absent before the three ordinary moments are closed. Another generic simplicial metric screen would repeat the completed atlas.

## 9. Independent package verification

The complete replay executes:


[Encoded source block omitted; the code in this passage is incomplete.]


- Complete exact package (`Keen_Quartz_89_global_V8_exact_atlas_NONWINNER.zip`)
- Archive SHA-256 (`Keen_Quartz_89_global_V8_exact_atlas_NONWINNER.zip.sha256`)
- Full research handoff (`RESEARCH_HANDOFF.md`)
- Run all exact verifiers (`RUN_ALL.sh`)
- Current replay transcript (`CURRENT_SESSION_REVERIFY.log`)
- Package manifest (`manifest.json`)
- SHA-256 manifest (`SHA256SUMS.txt`)

## Bottom line

No exact eight-vertex Gömböc was found, but the low-vertex frontier is substantially sharper. The full eight-vertex incidence universe consists of 257 types, and all 14 simplicial types now have exact reconstructed anchors. More importantly, the promoted exact eight-vertex body has strict own-centred class `(2,1,1)`: stable faces `[0,H,C]` and `[C,AG,AD]`, unique unstable vertex `C`, and sole saddle `[C,AD]`, with a certified six-dimensional `2^-80` chamber and complete independent verification. The first nonrepeating move is therefore the QCAD nonsimplicial quadrilateral gate that deletes `[C,AD]` and the adjacent extra stable triangle in the same actual incidence event.
