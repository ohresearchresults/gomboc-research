# figure-0080

AI research report · 2026-08-26 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Rapid Atlas 90 — coupled P28 defect-patch handoff

## Determination

**No homogeneous convex polyhedral Gömböc was obtained.** I therefore do not claim a `(1,1,0)` winner.

The strongest fully materialized result is an ordinary, uniform-density, exactly own-centered rational polyhedron

```text
P17 = { y in R^3 : H_i · y <= 1, i=0,...,16 }
```

with

```text
(F,E,V) = (17,40,25)
Euler     = 25-40+17 = 2
complexity F+E+V-2 = 80
exact uniform-volume centroid = (0,0,0)
exact equilibrium class = (S,U,H) = (2,2,2)
```

It is a genuine post-circuit body, not a denser Sloan approximation, a weighted point construction, an auxiliary-center mechanism, or a wall point. Its complete exact H/V data, maximal-face cycles, true edges, exact moment identity, all-feature witnesses, interval stratum certificate, independent verifier, OBJ, and STL are in the attached bundle.

## What changed relative to the supplied journal

P28 began with the connected Euler-neutral excess block

```text
extra stable faces:       11 and 25
extra unstable vertex:    15, active [2,18,27]
extra saddle pairs:       [9,25], [11,27], [25,27]
intended stable face:     27
intended unstable vertex: 39, active [9,25,27]
```

The coupled Y-patch and ensuing circuit/deletion path accomplished all of the following simultaneously:

- intended stable face `27` survives;
- the intended vertex-39 lineage survives as one strict actual unstable vertex;
- old stable face `11` is deleted;
- row `25` remains active but is no longer stable;
- all three old saddle pairs `[9,25]`, `[11,27]`, and `[25,27]` disappear;
- raw inactive separation improves from about `9.90e-5` in P28 to about `7.14e-4` in P17;
- complexity falls from `156` to `80`.

The complete cancellation failed because the defect transferred to a smaller Euler-neutral block:

```text
new extra stable support:      35
persisting extra U triple:     [2,18,27]
new saddle pairs:              [15,27] and [25,32]
Euler excess:                  1 + 1 - 2 = 0
```

Thus the operation did not eliminate the extra unstable vertex; it retopologized the other five original excess features and transferred the remaining index-zero block.

For provenance, P28 local faces `11,25,27` were original Sloan source rows `32,66,69`. The 37-row patch and final P17 use the retained scaffold labels shown below.

## Exact finite object and deterministic generator

The retained 17 scaffold labels are

```text
[0,1,2,9,13,14,15,18,25,26,27,30,32,33,34,35,36].
```

`generate_p17_exact.py` contains the full compact input as 17 binary64 hexadecimal row triples. Each hexadecimal value is decoded as its exact dyadic rational value; it is not treated as a tolerance-valued float.

The intended target unstable vertex is preserved as an exact nonsimple vertex. The generator first solves the common intersection of core labels `[9,25,27]`. For the eight target-cone labels

```text
[9,25,27,30,32,33,34,36],
```

it keeps exact dyadic `x,y` coordinates and solves each `z` algebraically from

```text
a_i · t = 1,
```

where `t` is the exact common pretranslation target point. Their eight-way concurrence is therefore an identity, not a numerical merge. After exact own-centroid translation, this becomes actual P17 vertex `14`, with the same eight active labels.

The generator then uses exact `Fraction` arithmetic to:

1. enumerate all `C(17,3)=680` support-plane intersections;
2. retain every and only feasible exact vertex;
3. reconstruct complete active sets, maximal-face cycles, and true edges from raw exact incidences;
4. integrate uniform volume and all three first moments over maximal-face tetrahedra;
5. apply exact own-centroid support renormalization;
6. repeat the incidence and equilibrium audit and export OBJ/STL.

A clean-directory regeneration produced byte-identical certificate, H/V tables, incidence files, OBJ, and STL.

## Exact degree-one moment mechanism

Let `B_i · x <= 1` be the exact precenter support rows and let the exact maximal-face cycles give outward triangles `T=(v_0,v_k,v_{k+1})`. Define

```text
V = (1/6)  Σ_T det(v_0,v_k,v_{k+1}),
M = (1/24) Σ_T det(v_0,v_k,v_{k+1}) (v_0+v_k+v_{k+1}),
c = M/V.
```

All terms are rational. Set

```text
y   = x-c,
h_i = 1-B_i·c,
H_i = B_i/h_i.
```

Then `H_i·y <= 1` is exactly the translated finite polyhedron and

```text
M_y = M - Vc = 0
```

identically in all three coordinates. This is the body's own ordinary uniform volume; there are no external cubature weights. During discovery, every accepted candidate was likewise evaluated only after recomputing its own volume centroid, so topology and equilibrium were never scored at the auxiliary origin.

For P17:

```text
exact first moment                 (0,0,0)
exact centroid                     (0,0,0)
exact volume, decimal view         6.645845461842211
minimum raw inactive H/V slack     7.141057884511406e-4
minimum oriented tetra determinant 1.367519044713817e-3
```

## Complete reconstructed lattice

The independent standard-library verifier reconstructs the following directly from the exact support inequalities:

```text
17 maximal faces
40 true edges
25 actual vertices
Euler characteristic 2
```

At every vertex it verifies every active equality exactly and every inactive inequality strictly. The minimum inactive slack occurs at exact vertex `18` against exact row `11` and is approximately

```text
0.0007141057884511406.
```

Face boundary cycles reconstruct the same 40 undirected edges as the true-edge table, and every true edge belongs to exactly two maximal faces. No triangulation-piece edge or tolerance-merging rule is used as a polyhedral feature.

## Exhaustive exact equilibrium audit

### Stable maximal faces

```text
retained label 27: raw strict margin 1.0037524370155905
retained label 35: raw strict margin 0.002489790738374313
```

Every other maximal face has a stored exact row that cuts its perpendicular foot. The closest nonstable witness is

```text
label 36 cut by label 35: -0.00023617566790293875.
```

### Unstable actual vertices

```text
extra vertex, active labels [2,18,27]:
    raw strict tangent-cone margin 0.0015512562109863478

intended vertex-39 lineage, active labels [9,25,27,30,32,33,34,36]:
    raw strict tangent-cone margin 165084536.28044325
```

The intended vertex is nonsimple, so the verifier checks every actual incident true edge, not merely three selected generators. Every other actual vertex has a stored incident-edge witness with negative radial derivative. The closest non-unstable witness is approximately

```text
-0.0022122551693759315.
```

### Saddle true edges

```text
incident labels [25,32]: raw minimum component 0.03384404324843791
incident labels [15,27]: raw minimum component 0.031656978188144246
```

For every true edge, the verifier computes exact `t`, `1-t`, and both coefficients of the full two-face normal cone. A saddle is counted only when all four exact quantities are positive. Every nonsaddle edge has a stored nonpositive limiting component; the closest nonsaddle witness is approximately

```text
-0.006949331417083719.
```

The exhaustive exact result is therefore

```text
(S,U,H) = (2,2,2),
S+U-H   = 2.
```

The independent verifier terminates with

```text
PASS_EXACT_POST_CIRCUIT_NOT_GOEMBOC
```

The exact certificate SHA-256 is

```text
9ef432b04729190f7a4a9a611ec6740c308f9df5765d9ba59bd305ebea584ffc.
```

## Certified perturbation radius

Because the intended target vertex has eight exactly concurrent support rows, no full independent 51-coefficient ambient ball can preserve that incidence: a generic perturbation splits it. The correct open certificate is a 43-dimensional box inside the target-incidence stratum.

Independent parameters are:

```text
8 target rows × independent (x,y) = 16
9 remaining rows × independent (x,y,z) = 27
total = 43.
```

For each target row, `z` is solved algebraically from the common target equation. Over the entire box

```text
|delta parameter| <= 3e-10,
```

an outward-rounded interval verifier proves:

```text
same 17 faces, 40 edges, and 25 vertices;
exact target concurrence preserved algebraically;
own uniform-volume centroid recomputed for every member;
first moment after the dependent centroid translation identically zero;
class remains exactly (2,2,2);
minimum inactive-slack lower bound       7.140865323952125e-4;
minimum face-orientation lower bound     1.648348853701745e-3;
minimum active-triple determinant bound  1.590125235300459e-3;
minimum equilibrium-sign lower bound     1.028282628459156e-3.
```

The radius `3e-10` is certified but not claimed maximal.

## Topology path

The corrected stored path is:

```text
P28 exact:
    (F,E,V,C)=(28,78,52,156), class (3,2,3)

37-row coupled Y seed, all rows active:
    (30,84,56,168), class (3,3,4)

centroid/covariance-corrected cells:
    representative cells (3,3,4)

row-scan and chamber search:
    first strict (2,2,2) cells

23-active-row Y endpoint:
    (23,56,35,112), class (2,2,2)

inactive/redundant deletion and exactification:
    P17 = (17,40,25,80), exact class (2,2,2)
```

The 23-row and 17-row endpoints have the same residual feature labels. Deletion therefore simplified the realized object and enlarged raw incidence separation without hiding another topology transfer.

## Search performed and result-breaking check

The branch tried:

- a three-arc coupled Y support scaffold spanning both original stable basins and the extra-U sector;
- own-centroid covariance and moment corrections;
- differential evolution and targeted support scans;
- random search across neighboring `(2,2,2)` cells;
- automatic bridge rows;
- exhaustive deletion of inactive/redundant rows;
- fixed-17-row local support scaling;
- generic one-row and targeted two-row residual bridges.

Fixed-center linear inequalities can make two bridge rows cover the four residual witness points, but after the actual hull is rebuilt and its uniform centroid is recomputed, the rows become critical themselves or split the residual cone. No two-row endpoint improved on `(2,2,2)`.

A serious apparent success was deliberately broken. An earlier floating evaluator ordered maximal-face fans with tolerances on an aggressive bridge topology and integrated the wrong volume centroid. It reported `bridge_pair_best.npy` as `(1,2,1)`. Recomputing the hull with convex-hull tetrahedra gave `(1,4,3)`. That false endpoint was rejected. The exact P17 generator uses exact incidences and positive exact tetrahedra; the independent verifier reconstructs the lattice separately. No claim here relies on that numerical false positive.

## Localized obstruction

The remaining block is now sharply localized:

```text
stable sink:           row 35
extra U circuit:       [2,18,27]
saddle sector A:       [15,27]
saddle sector B:       [25,32]
```

Sequentially crossing one of these incidence circuits exposes another and preserves Euler excess. The obstruction is no longer global centering, cubature, raw-incidence ambiguity, or excessive complexity. It is the failure of one- and two-row patches to cross all three adjacent circuits while preventing their own rows from becoming new stable sinks under the body's recomputed centroid.

## Next nonredundant operation

The next operation should be a **four-support, three-circuit bistellar replacement**, not another local polish:

1. delete residual stable row `35` as part of the simultaneous circuit event, not beforehand;
2. retopologize the three sectors around intended face `27` bounded by rows `[14,15]`, `[2,18]`, and `[25,32]`;
3. insert four rows `r1,...,r4` as two cross-coupled Y arms;
4. require `r1,r2` jointly to cut the row-35 foot and the `[15,27]` saddle cone;
5. require `r3,r4` jointly to reverse the `[2,18,27]` tangent ray and cut the `[25,32]` saddle cone;
6. impose cross-arm witness inequalities so no `r_i` terminates as a new stable face;
7. preserve the current exact target concurrence, or deliberately replace it by a strict three-face target cone at the same target point;
8. reserve three mechanically inactive coefficients with a full-rank volume-moment Jacobian and solve all three first-moment equations as dependent equations in every enumerated cell;
9. enumerate every adjacent active-triple cell through the simultaneous circuits and accept only a strict `(1,1,0)` cell with raw inactive slack above `1e-4` before exactification.

This is the smallest operation not already subsumed by the failed one-sided, isolated-row, two-row, or fixed-lattice searches.

## Reproducible artifacts

- Complete exact fallback bundle (`p28_double_y_exact_fallback_bundle.zip`) — SHA-256 `32bc03d1a07e98dc54127d3d4ca598269e4b39c75d3218025448c6b863af1fac`.
- Bundle README (`README.md`)
- Full exact certificate (`p17_exact.json`)
- Deterministic exact generator (`generate_p17_exact.py`)
- Independent exact verifier (`verify_p17_exact.py`)
- Directed interval stratum verifier (`verify_stratum_radius.py`)
- Exact H rows (`H_exact.csv`)
- Exact V coordinates (`V_exact.csv`)
- Maximal-face cycles (`faces.txt`)
- True-edge list (`edges.txt`)
- OBJ export (`p17_exact.obj`)
- STL export (`p17_exact.stl`)
- Exact verification transcript (`verification.txt`)
- Interval-radius certificate (`stratum_radius.json`)
- Search record and continuation (`SEARCH_RECORD.md`)
- Integrity manifest (`manifest.json`)
- Original exact P28 bundle (`sloan_cubature_fallback_bundle.zip`)

Reproduction commands are

```bash
cd p28_double_y_exact_fallback
python generate_p17_exact.py
python verify_p17_exact.py
python verify_stratum_radius.py
```

The materialized result is therefore an exact, independently reconstructible `(2,2,2)` post-circuit body and a sharply delimited four-support continuation—not a claimed Gömböc.
