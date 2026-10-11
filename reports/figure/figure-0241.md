# figure-0241

Historical AI scientific report · saved 2026-09-03 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Clear Willow 25 — exact active connected shared-volume determination

## Verdict

**No homogeneous convex polyhedral Gömböc was obtained.** The promoted object is an exact finite nonwinner of strict own-centroid class `(S,U,H)=(2,1,1)`.

The supplied journal left this topology genuinely open: the previous `(86,216,132)` endpoint had residual stable `[258,5000,1025]`, saddle `(248,5006)`, no active edge joining its two tips, and a positive radial obstruction at `5000`. :contentReference[oaicite:0]{index=0} This continuation realizes the requested finite-thickness active connection, makes `5000` strictly nonextreme, deletes both inherited carriers from the rebuilt hull, and then proves that the Morse packet transfers rather than annihilates.

[Complete exact archive](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final.zip) — SHA-256 `618b92913dc0b45a3944ba260b01e61ab5aafee101ebd849d209c6f6305faf3f`  
[Readable report](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/README.md) · [machine summary](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/result_summary.json) · [clean-room transcript](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/CLEANROOM_VERIFY.log)

## Exact finite endpoint

From the exact 91-row parent, row `5006` is removed, row `5000` is retained as a supplied row, and exact dyadic rows `6001,6004,6006,6007,6008,6009` are inserted. All six new rows are actual extreme vertices. The complete 96-row source and deterministic regeneration are in [exact_finite_source.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/exact_finite_source.json) and [build_exact_connected_endpoint.py](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/build_exact_connected_endpoint.py).

Exact coordinate and certificate files: [supplied coordinates](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/coordinates_exact.csv), [own-centred coordinates](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/coordinates_own_centered_exact.csv), [common lattice](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/coordinates_common_lattice.csv), and [endpoint certificate](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/certificate.json).

Fresh reconstruction from all supplied rows gives

```text
supplied rows     96
active vertices   68
true edges        182
maximal faces     116
Euler             68-182+116 = 2
complexity        364
face sizes        113 triangles, 2 quadrilaterals, one 17-gon
```

Complete incidence: [maximal faces](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/face_cycles.json), [exact face planes](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/face_planes_exact.json), and [true edges](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/true_edges.csv). The minimum normalized nonincident support margin is `3.869169282446657e-6`; minimum inactive-row separation is `1.0761399066994322e-4`.

### Direct row-5000 certificate

Row `5000` is present among the 96 supplied rows but occurs in no maximal face or true edge. All 116 exact endpoint facet inequalities are strict at it. Its minimum normalized interior separation is `0.21989804041867403`, attained against face `[257,258,6001]`. Hence old stable `[258,5000,1025]` is literally absent. Row `5006` is not supplied, so old saddle `(248,5006)` is literally absent. This satisfies the assignment's radial gate by actual deactivation, not by auxiliary-centre mechanics.

## Exact mass and own centroid

The exact volume is

```text
25874357284211505115697712780783702769606753215138796745543722538509532823265868548244919621884521893871586833803539776554324258119634243963470850330046302881633054892706740431241477567601740439042833129735376934199980817563965296082250635567249467599792421362861601209
/
19378107118177208733281682747470556117321049727625577588019006745439306181586947750020720665582301839258873392667945554227247516603556907140671913886944533882593293482783397054124215787124095847234874390913696875450277939485081600000000000000000000000000000000000000
```

approximately `1335.2365701364417`. The exact uncentred centroid is recorded as three fractions in `certificate.json`, approximately

```text
(-1.092939858407019, 2.9717937651429343, -0.19478244810909262).
```

Exact tetrahedral summation verifies `M(P+τ)=M(P)+Vτ`; with `τ=-C`, all three centred first moments are exactly `0/1`.

## Exhaustive equilibrium classification

The exact own-centroid class is `(2,1,1)`:

```text
stable [0,1,...,16]       margin 0.9325642554896598
stable [257,258,6001]     margin 0.0010073105755025922
all other faces excluded  margin 4.424823146303871e-6

unstable vertex 8         margin 0.17166970101185264
all others excluded       margin 5.287494161872802e-5

saddle (248,6009)         four-component margin 0.0009077498413994302
all others excluded       margin 0.0008435651537273164
```

Every true edge was tested with all four cone components `(t,1-t,beta1,beta2)`. Exact exhaustive ledgers: [faces](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/faces_mechanics_exact.json), [vertices](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/vertices_mechanics_exact.json), [edges](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/edges_mechanics_exact.json).

## Active connected disk exchange

The parent and endpoint share 64 maximal faces. Their differing parts are two connected combinatorial disks with the same boundary:

```text
removed parent disk    (V,E,F)=(64,131,68), Euler 1
inserted endpoint disk (V,E,F)=(46,97,52),   Euler 1
common boundary        38 edges
```

Boundary cycle:

```text
[228,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,
 263,264,246,245,244,243,242,241,240,239,238,237,236,235,234,233,
 232,1004,1003,1002,230,1026].
```

The removed disk contains the previous carriers; the inserted disk contains route face `[228,248,1026]`. Row `198` becomes inactive, while `228` and `1026` remain active. Full exact comparison: [disk_exchange_certificate.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/disk_exchange_certificate.json).

The new-new true edges are

```text
6001-6004, 6004-6006, 6004-6007,
6006-6007, 6007-6009, 6008-6009.
```

Thus `6001-6004-6007-6009` is a literal active stable-to-saddle path. The inactive-arc defect of the prior endpoint is gone.

## Oriented matroid and regular cell

The six new rows have affine rank four. Their convex hull has exact positive volume

```text
1039486235736092120462114703723735079598280721287
/
91343852333181432387730302044767688728495783936
```

approximately `11.379925514248209`; tetrahedron `[6001,6004,6007,6009]` alone has volume about `7.716531952032243`.

[The exact oriented-matroid/regular-subdivision certificate](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/new_cell_oriented_matroid.json) contains the complete rank-four chirotope, all six minimal five-point circuits with integer coefficients and signs, all facets, exact lifting slacks, and the squared-norm regular triangulation

```text
[6004,6008,6001,6006]
[6004,6008,6001,6009]
[6007,6004,6008,6006]
[6007,6004,6008,6009].
```

This is a full-dimensional positive-volume active cell, not a ribbon or assumed local flip.

## Exact open chamber

[verify_full_18d_box.py](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/verify_full_18d_box.py) certifies by exact rational intervals that all 18 uncentred coordinates of the six new active vertices vary independently by

```text
±2^-36 = ±1/68719476736.
```

Throughout this Cartesian box, the complete 96-row hull remains `(68,182,116)`, `5000` remains inactive, exact centroid translation remains valid, and the full class stays `(2,1,1)` with the same features. The exact certificate is [full_18d_box_certificate.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/full_18d_box_certificate.json). This is an open 18-dimensional shape chamber, not a wall point.

## Exact death-before-birth obstruction

The requested ordering was not achieved. I certified the whole straight segment from the promoted endpoint to a second exact dyadic relay endpoint. [relay_chronology_certificate.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/relay_chronology_certificate.json) proves, using exact recursive Bernstein coefficients, that for every `t∈[0,1]`:

- all 116 maximal faces persist;
- 10,772 nonincident determinant polynomials retain their signs;
- 16 intended coplanarity polynomials vanish identically;
- volume remains positive;
- the target base, `U8`, inherited stable `[257,258,6001]`, and inherited saddle `(248,6009)` remain strict.

At exact `t=4/5`, adjacent face `[258,259,6001]` and edge `(258,6001)` are non-equilibria, while the class is `(2,1,1)`. At exact `t=9/10`, the inherited stable and saddle still have margins `0.0010024478086958577` and `0.0008934093142236396`, but the adjacent face is stable with margin `4.6152585026300475e-7` and the shared edge is saddle with margin `0.0004601870128842549`, giving `(3,1,2)`.

Therefore this exact same-incidence continuation creates a replacement stable-saddle pair **before** either inherited carrier dies. Exact bracket coordinates: [pre-birth](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/pre_birth_coordinates_exact.csv) and [post-birth](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/post_birth_coordinates_exact.csv).

The rigorous exclusion covers the full `2^-36` 18-coordinate box and the complete certified affine segment. It is not a global exclusion of every realization of this abstract face lattice.

## Independent verification and mesh

The independent GMP verifier [verify_exact_hull_gmp.cpp](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/verify_exact_hull_gmp.cpp) enumerates all `C(96,3)=142880` triples and performs `2,607,588` exact support-sign checks:

```text
INDEPENDENT_GMP_ALL_TRIPLE_HULL_PASS
rows=96 facets=116 edges=182
```

The independent Fraction verifier [verify_exact_mass_mechanics.py](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/verify_exact_mass_mechanics.py) rebuilds incidence, exact mass, exact centroid, and every equilibrium cone:

```text
INDEPENDENT_EXACT_MASS_MECHANICS_PASS
fvector 68 182 116 Euler 2
class 2 1 1
```

Meshes: [OBJ](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/body.obj), [STL](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/body.stl), and [mesh verifier](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/connected_shared_volume_endpoint/verify_mesh.py). The OBJ has 68 vertices, 132 triangles, 198 triangulated edges, Euler two, every edge multiplicity two, volume `1335.236570136442`, and centroid norm `2.44e-15`. The clean extraction replay ends with all eight expected PASS markers.

## Exhausted scope and empirical screens

[search_scope.json](sandbox:/mnt/data/M42_slot1_Clear_Willow_25_active_connected_final/search_scope.json) records full-hull screens of 8,699 ribbon bodies, 5,812 specified local-deletion subsets, 4,472 fan/arc deletions, 1,000 two-buttress bodies, and 3,686 two-cut/two-page bodies; none was `(1,1,0)`. These are finite empirical screens, not continuum proofs. The exact exclusions promoted here are only the certified 18-dimensional chamber and same-incidence relay segment.

## Precise surviving forcing component

The left boundary relay is

```text
inherited stable       [257,258,6001]
adjacent stable birth  [258,259,6001]
shared saddle birth    (258,6001)
```

while the independent right carrier remains saddle `(248,6009)`, with incident faces `[248,6007,6009]` and `[248,6009,6008]`. The active cell communicates geometrically, but its two complete stars do not have independent interior timing control; the left boundary relay becomes strict first.

## Smallest nonrepeating successor

The smallest unclassified successor is a **two-boundary or internally linked prismatic/cubical 3-ball** that changes both complete residual stars before the relay wall:

1. deactivate or move at least one of `{258,6001}` so inherited and adjacent stable carriers cannot coexist;
2. simultaneously deactivate or move at least one of `{248,6009}` and replace both saddle-incident faces;
3. link the pages through an actual interior quadrilateral, edge, or tetrahedral face rather than only a boundary path;
4. stay attached to `228,1026`, permitting coordinated motion or deactivation of one route row;
5. retain at least two independent antibirth/timing controls after solving the three exact ordinary moments.

A robust minimal model uses eight connected new extreme supports as two triangular prisms sharing an interior quadrilateral. Six supports remain possible only with simultaneous old-row motion involving `258` and `248` or `1026`. A leaf buttress, inactive interpolation arc, another one-boundary strip, serial stellar insertion, or same-incidence motion of `6001` repeats a certified mechanism.

## Final disposition

**EXACT ACTIVE CONNECTED SHARED-VOLUME NONWINNER.** The new endpoint resolves the first unclassified row-54 successor constructively: `5000` is strictly nonextreme, the previous pair dies, all six new supports are active and form a positive-volume regular connected cell, exact own-centering leaves a full 18-dimensional chamber, and all incidence, mechanics, and mesh checks pass independently. The remaining obstruction is now exact and localizable: the one-boundary active cell births a left-relay stable-saddle pair before the inherited stable and independent right saddle can die. The next topology must couple both stars through an interior shared volume with separate antibirth timing controls.
