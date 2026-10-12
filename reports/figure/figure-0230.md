# figure-0230

AI research report · 2026-09-02 UTC

---

# Clear Willow 25 — exact row-54-deactivating determination beyond the M42 K7 atlas

## Verdict

No literal homogeneous convex polyhedral Gömböc was obtained. The required acceptance gate remains a finite uniform-density body evaluated at its own exact ordinary-volume centroid with strict `(S,U,H)=(1,1,0)`, complete all-feature verification, and matching finite geometry; auxiliary-centre mechanics, wall points, and unexpanded constructions do not qualify. :contentReference[oaicite:0]{index=0}

I did construct and independently verify an exact rational/dyadic **row-54-deactivating full-hull endpoint** that lies beyond the fixed-old-row K7 families. It destroys the old K7 route cell, deletes the previously created stable carrier `[1000,1025,3000]`, and deletes the previously created saddle carrier `(1027,3001)`. The complete actual hull nevertheless contains a new strict stable–saddle pair, so the topology transfer remains Euler-neutral.

The promoted endpoint is therefore an exact nonwinner, not a near-solution claim.

## Exact finite endpoint

The construction starts from the exact 91-vertex M42 transfer body and performs the following literal replacement:

```text
old supplied rows removed:
  54, 247, 1027, 1028, 1029, 3000, 3001

new exact-dyadic rows supplied:
  5000, 5001, 5002, 5003, 5004, 5005, 5006

new rows that are actual extreme vertices:
  5000, 5006

new rows strictly inactive:
  5001, 5002, 5003, 5004, 5005
```

Thus the supplied set still has 91 rows, while the reconstructed irredundant hull has

```text
(V,E,F) = (86,216,132)
86 - 216 + 132 = 2.
```

The body is represented by exact rational coordinates: inherited M42 rows retain their original exact fractions and the newly introduced rows are interpreted as their exact binary64 dyadic rationals. The complete supplied/active ledger and exact coordinates are available here:

- [Exact supplied and active coordinates](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/coordinates_exact.csv)
- [Exact own-centred coordinates](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/coordinates_own_centered_exact.csv)
- [Single common integer lattice](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/coordinates_common_lattice.csv)
- [Simplified common-lattice table](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/coordinates_common_lattice_simple.csv)
- [Deterministic exact builder](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/build_exact_endpoint.py)
- [Machine-readable exact certificate](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/certificate.json)

## Exact ordinary volume and centroid

The independently reconstructed uncentred body has

```text
ordinary volume ≈ 1048.397710822473
ordinary centroid ≈
  (-0.9083402836195011,
    2.4251502111682655,
   -0.15290179974096546).
```

The exact rational volume and all three exact rational centroid coordinates are stored in `certificate.json`. Translating every supplied point by the negative of that exact centroid gives the promoted own-centred representation. Direct exact signed-tetrahedron summation then gives

```text
first moment Mx = 0
first moment My = 0
first moment Mz = 0
```

as rational identities, not numerical tolerances.

## Complete incidence reconstruction

All maximal faces and true edges were reconstructed from the complete 91-row supplied set rather than inherited from a local ledger:

- [All 132 maximal-face cycles](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/face_cycles.json)
- [Tab-separated maximal-face cycles](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/face_cycles.tsv)
- [Exact supporting planes](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/face_planes_exact.json)
- [All 216 true edges](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/true_edges.csv)

The minimum normalized active-face/nonincident-row separation is

```text
5.890532760102717e-8.
```

The minimum normalized separation of the five inactive supplied rows from the actual hull is

```text
0.02401538984408422.
```

The small active nonincidence value is positive exactly, but it makes this endpoint less numerically comfortable than the original parent transfer.

## Exhaustive own-centroid equilibrium audit

The exact full-normal-cone classification is

```text
(S,U,H) = (2,1,1).
```

### Stable maximal faces

```text
target stable face:
  [0,1,2,...,16]
  normalized margin 0.8868554507903854

sole additional stable face:
  [258,5000,1025]
  normalized margin 2.6609545351382626e-5
```

Every other maximal face is strictly nonstable. The minimum normalized exclusion margin over those faces is

```text
1.2229937063283072e-5.
```

### Unstable vertices

```text
unique unstable vertex:
  8
  normalized margin 0.17168435006110283
```

Every other actual vertex is strictly nonunstable. The minimum normalized exclusion margin is

```text
1.1274271999090956e-5.
```

### Saddle true edges

```text
sole saddle edge:
  (248,5006)
  normalized four-component cone margin 3.878130296391596e-5
```

Every other true edge is strictly nonsaddle. The minimum normalized exclusion margin is

```text
6.86983568159999e-5.
```

The exhaustive exact ledgers are:

- [All face mechanics](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/faces_mechanics_exact.json)
- [All vertex mechanics](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/vertices_mechanics_exact.json)
- [All four-component true-edge cone mechanics](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/edges_mechanics_exact.json)

## Proof that the previous replacement carriers crossed their walls

The parent transfer's unwanted stable triangle was `[1000,1025,3000]`. Row `3000` is absent from the new supplied set, so that maximal face cannot survive even as a hidden coplanar subdivision.

The parent transfer's unwanted saddle was `(1027,3001)`. Both endpoints `1027` and `3001` are absent from the new supplied set, so the true edge and its complete normal cone are destroyed literally.

Old row `54` is also absent. Consequently the K7 cell

```text
{3000,258,54,69,228,1026,3001}
```

and each of its three assignment-critical facets containing row `54` are absent from the actual full hull. This is a genuine move outside the fixed-old-row one-support/page families closed in the preceding K7 atlas.

The equilibrium packet transfers to different carriers:

```text
new stable carrier: [258,5000,1025]
new saddle carrier: (248,5006).
```

No stale old-label argument is used in this conclusion; both the old deaths and the new births follow from the independently reconstructed full hull.

## Exact forcing obstruction in the promoted chamber

The strongest new exact obstruction is a radial-order inequality. Let `C` be the exact ordinary centroid before translation, let `B` be the affine plane of the intended 17-gonal base, and let `p5000` be the exact new vertex. The certificate reconstructs the exact positive rational quantity

```text
d(C,B)^2 - ||p5000-C||^2
  = positive exact rational
  ≈ 0.0035276841191570272.
```

Thus `p5000` lies strictly closer to the body's own centroid than every point of the intended base plane. Since `p5000` is an actual boundary vertex, the target base cannot be the sole radial minimum of the boundary. In the present strict incidence/mechanics chamber, the forced competing minimum is realized by `[258,5000,1025]`.

Therefore every continuation that preserves all of the following is excluded from being a Gömböc:

```text
1. the intended 17-gon remains the target stable face;
2. row 5000 remains an actual boundary vertex;
3. the exact radial inequality above remains positive;
4. the hull remains in a strict, nondegenerate equilibrium chamber.
```

A successful continuation must cross at least one of these walls. In particular, polishing the stable-face barycentric margin alone is insufficient: row `5000` must become nonextreme, cross the target-base radial level, or be absorbed into a larger simultaneous degeneracy that changes the boundary minimum carrier.

This is a sharply scoped exact obstruction. It is not a no-go theorem for arbitrary two-page or moving-old-row surgeries.

## Independent clean-room verification

### All-triples exact hull reconstruction

The independent GMP verifier enumerates all `C(91,3)=121485` supplied-row triples and performs 2,167,360 exact support-sign checks. It reports:

```text
INDEPENDENT_GMP_ALL_TRIPLE_HULL_PASS
rows=91
triples=121485
nondegenerate=121485
supporting_triples=877
facets=132
edges=216
```

Files:

- [Independent GMP verifier source](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/verify_exact_hull_gmp.cpp)
- [Independent GMP verifier transcript](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/verify_exact_hull_gmp.log)

### Exact mass and mechanics replay

A separate Fraction-based verifier rebuilds the exact maximal faces and true edges, reintegrates the volume and first moments, translates to the exact centroid, and reclassifies every face, vertex and edge cone. It reports:

```text
INDEPENDENT_EXACT_MASS_MECHANICS_PASS
fvector 86 216 132
Euler 2
class 2 1 1
stable [0..16], [258,5000,1025]
unstable [8]
saddles [(248,5006)]
```

Files:

- [Independent exact mass/mechanics verifier](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/verify_exact_mass_mechanics.py)
- [Independent exact mass/mechanics transcript](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/verify_exact_mass_mechanics.log)

## Meshes

Finite OBJ and binary STL exports were generated from the reconstructed maximal-face cycles:

- [OBJ mesh](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/body.obj)
- [STL mesh](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/body.stl)

The exact hull reconstruction proves that the intended underlying boundary complex is a convex two-sphere with Euler characteristic two. I did not complete a separate byte-level OBJ/STL parity and edge-multiplicity replay before the run boundary, so these exports should be treated as generated meshes accompanying the exact hull certificate, not as independently mesh-certified artifacts.

## Perturbation certification status

Every incidence and mechanics primitive at the exact endpoint is a strict rational inequality. Since the relevant family is finite, this proves existence of a nonzero open neighbourhood preserving `(86,216,132)` and `(2,1,1)`.

An explicit all-coordinate interval verifier was written:

- [Interval verifier](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/verify_interval.py)

It attempted to propagate rational intervals through all 132-by-91 incidence tests, exact mass integration, centroid division, and all face/vertex/edge cone formulas. Two executions, including a ten-minute execution, did not finish and produced no passing transcript. Consequently I do **not** claim an explicit certified coordinate-box radius for this endpoint. This is the principal missing acceptance item in the promoted artifact, although it does not affect the exact pointwise hull, centroid, or equilibrium determination.

## Finite search landscape explored

The following searches used complete actual-hull reconstruction and recomputed the body's own centroid at every valid sample:

```text
independent two-support replacements:
  30,000 tested
  29,604 valid full hulls
  0 strict (1,1,0) bodies

delete-and-arc / moving-old-row replacements:
  30,000 tested
  28,765 valid full hulls
  0 strict (1,1,0) bodies

representative K7 two-page chamber pairs:
  3,276 actual full hulls
  0 strict (1,1,0) bodies
```

The delete-and-arc search also found a smaller-residual non-row-54 endpoint with extra stable margin about `6.50e-7` and saddle margin about `1.79e-7`, but it was not promoted because it remains extremely close to a topology wall and does not cross the row-54 frontier.

Fixed-topology optimization around that state compressed selected residuals further but rebuilt as `(2,2,2)` near a multi-feature degeneracy. It was rejected rather than rationalized.

A final targeted local actual-hull search was started but failed because its ranking code assumed target-face and target-vertex fields were present even when a sampled hull had lost a protected target. It raised `KeyError: 'face_bad'` before writing a result file. It contributes no search evidence.

These numerical collections are empirical finite screens, not continuous chamber exclusions. The only new rigorous family exclusion from this continuation is the exact radial-order chamber described above. The preceding fixed-old-row one-support/page Gordan closures remain separate inherited results.

## What changed relative to the supplied journal

The prior journal frontier left two possibilities genuinely unclassified: two communicating support positions or an event in which row `54` moves or deactivates. This continuation resolves the second possibility constructively at an exact finite endpoint:

1. Row `54` can be deleted while preserving the 17-gonal target base and unique unstable vertex `8`.
2. The complete old K7 cell and both previous replacement equilibrium carriers can be destroyed in that event.
3. The actual hull does not cancel the pair. It transfers the stable carrier to `[258,5000,1025]` and the saddle carrier to `(248,5006)`.
4. The transfer is not caused by insufficient centroid rank: exact own-centering is completed.
5. The new decisive obstruction is radial ordering. Vertex `5000` is closer to the exact centroid than the complete target-base plane by the exact squared-distance gap `0.0035276841191570272`.
6. The surviving active additions `5000` and `5006` are not joined by a true cross-branch edge. The attempted finite-thickness arc collapsed combinatorially to two disconnected active tips; the intermediate rows became strictly interior.

Thus **row-54 deactivation by itself is not the missing cancellation mechanism**. Connectivity must be present in the actual active hull, not merely in the supplied construction rows.

## Smallest genuinely nonrepeating successor

The smallest still-unclassified operation is a true shared-volume two-page event replacing the complete new stable and saddle stars together. It may be described as an eight- or nine-vertex nonannular cell built around

```text
stable side:  {258,5000,1025}
saddle side:  {248,5006} and its two incident maximal faces
shared old route sector: {198,228,1026} or a moved/deactivated subset.
```

The event must satisfy all of the following simultaneously:

```text
1. create at least one actual true cross-branch edge between the stable-side
   and saddle-side additions;
2. deactivate 5000 or move it beyond the exact target-base radial level;
3. cross the stable death wall of [258,5000,1025];
4. cross one of the four strict saddle-cone components of (248,5006);
5. permit 5006 and at least one of 258,248,1025,1026 to deactivate in the
   same incidence event if required;
6. preserve the 17-gonal base and vertex 8 with their large existing margins;
7. rebuild the complete hull and exact ordinary centroid after every circuit
   crossing, rather than transporting a local ledger.
```

Two isolated connectors with an inactive interpolating arc are now repetitive. The next cell needs finite **active** thickness: either two new communicating vertices replacing `5000,5006` while one old route row moves, or three new vertices with a cross-edge and an interior tetrahedral/octahedral overlap. Its topology should be enumerated as a coupled regular subdivision, not as serial stellar insertion.

The first quantitative wall for that successor is already exact: the stable-side operation needs enough macroscopic radial leverage to reverse the squared-distance gap

```text
0.0035276841191570272,
```

not merely the much smaller current stable barycentric margin. This explains why near-wall polishing repeatedly changes the carrier without allowing the intended base to become the sole stable equilibrium.

## Reusable artifact index

Primary endpoint files:

- [Exact certificate](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/certificate.json)
- [Exact coordinates](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/coordinates_exact.csv)
- [Exact own-centred coordinates](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/coordinates_own_centered_exact.csv)
- [Maximal faces](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/face_cycles.json)
- [True edges](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/true_edges.csv)
- [Face mechanics](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/faces_mechanics_exact.json)
- [Vertex mechanics](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/vertices_mechanics_exact.json)
- [Edge mechanics](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/edges_mechanics_exact.json)
- [Independent exact hull verifier](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/verify_exact_hull_gmp.cpp)
- [Independent exact mechanics verifier](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/verify_exact_mass_mechanics.py)
- [OBJ](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/body.obj)
- [STL](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_two_page_final/row54_deactivating_endpoint/body.stl)

## Final disposition

**NONWINNER, exact and reusable.**

The requested strict `(1,1,0)` object was not reached. The strongest promoted endpoint is an exact own-centred row-54-deactivating polyhedron with `(V,E,F)=(86,216,132)` and strict `(2,1,1)`. It proves that the old K7 cell and both previous replacement carriers can be destroyed together while preserving the intended base and `U8`, but it also proves that the resulting chamber is radially forced to retain an additional stable equilibrium. The smallest unclassified successor is therefore a genuinely active, connected shared-volume two-page cell that simultaneously crosses the radial, stable, saddle and incidence walls; another disconnected pair of tips, inactive arc, local flip, or fixed-cell polish is redundant.
