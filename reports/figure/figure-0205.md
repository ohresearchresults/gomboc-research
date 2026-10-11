# figure-0205

Historical AI scientific report · saved 2026-09-02 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Steady Quartz 25 — exact five-point shared-volume handoff

## Disposition

**EXACT NONWINNER.** No strict homogeneous convex polyhedral Gömböc was obtained. The journal’s accepted predecessor had 3,490 supplied / 1,631 active rows, primal `(V,E,F)=(3258,4887,1631)`, strict own-centred `(2,2,2)`, and an external-positive forcing edge `(2811,500008)`; the required successor was a genuine five-point higher-valence shared volume deleting that edge and absorbing the replacement packet. :contentReference[oaicite:0]{index=0} The construction below realizes that topology exactly but recreates an Euler-neutral block, so it does not pass the materialized `(1,1,0)` gate. :contentReference[oaicite:1]{index=1}

**Artifacts:** [complete archive](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER.zip), [SHA-256](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER.zip.sha256), [full handoff](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/STEADY_QUARTZ_25_FIVEPOINT_HANDOFF.md), [result certificate](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/certificates/result_summary.json), [verifier](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/verify_steady_quartz25_fivepoint.sh). Archive SHA-256: `f29ddea4e33fc32e60d89347ca823bebbf7fe83a1af838b221f82ef5f1a61407`.

## Exact promoted body

The normative raw body is `P_raw={x:q_i·x<=1, i=1,...,3492}`. Every row is an exact binary64 dyadic in [the complete H file](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/data/supplied_endpoint_rows.hex), equivalently on a common `2^109` integer lattice [here](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/data/supplied_endpoint_rows_integer.csv). Exact all-row reconstruction gives

```text
supplied/active/inactive rows = 3492/1630/1862
primal (V,E,F)                = (3256,4884,1630)
surface triangles             = 6508
Euler                          = 2
nonincident exact checks       = 11,360,184
extra coplanar/outside rows    = 0/0
minimum nonincident slack      = 1.4689227575116868179e-9
minimum inactive-row slack     = 3.1422919088378113046e-4.
```

The complete [active H rows](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/data/raw_polar_rows.hex), [exact Cramer vertices](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/geometry/primal_vertices_exact.csv.gz), [maximal-face cycles](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/geometry/maximal_face_cycles.json), and [true edges](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/geometry/true_edges.csv) are materialized.

The exact own-centroid equilibria are

```text
S: 3911, 500008
U: (1836,500009,500010), (2024,2377,500004)
H: (1802,500005), (2592,500002),
```

hence `(S,U,H)=(2,2,2)`. The intended `S3911` and `U(2024,2377,500004)` survive. The predecessor carriers `S500007`, `U(1836,2811,500008)`, `H(1802,500007)`, `H(2592,500003)`, and edge `(2811,500008)` disappear; the packet is recreated on `S500008`, `U(1836,500009,500010)`, `H(1802,500005)`, `H(2592,500002)`.

## Genuine higher-valence interior cell

The active support configuration contains the exact empty convex octahedral regular-subdivision cell

```text
O=conv{2811,500002,500006,500008,500009,500010}.
```

Its eight facets are `(2811,500002,500006)`, `(2811,500002,500010)`, `(2811,500006,500009)`, `(2811,500009,500010)`, `(500002,500006,500008)`, `(500002,500008,500010)`, `(500006,500008,500009)`, and `(500008,500009,500010)`. It has 12 edges, all vertices degree four, positive exact volume `1.569728734981196616…e-3`, and missing opposite diagonals `(2811,500008)`, `(500002,500009)`, `(500006,500010)`.

It contains two overlapping exact five-point Radon circuits:

```text
{2811,500008,500006,500009,500010}
{2811,500008,500002,500009,500010}.
```

Both old buttresses `500002,500006` and both new supports `500009,500010` are active. Exact affine coefficients and equal `2`-tetrahedron/`3`-tetrahedron decompositions are in [the circuit certificate](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/certificates/exact_higher_valence_shared_volume.json). [The regular-cell certificate](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/certificates/exact_empty_regular_octahedral_cell.json) proves exact emptiness against all other 1,624 active supports and supplies a lower regular-subdivision lift meeting exactly these six points, with projected dimension three. This is a true finite-thickness nonsimplicial interior volume, not a boundary-concurrency or triangulation proxy.

## Exact ordinary centroid and controls

A direct GMP rational sum over all 3,256 exact vertices and 6,508 oriented triangles gives

```text
V=5.309756377272709531519308992181835355568156230330145942684929708864423481263882461080383610…
c_raw=(-0.06476292098569717359368532824631514579…,
        0.03245106886429303335513180165814670504…,
        0.06192397204072527452178501235275831802…).
```

[The exact mass certificate](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/certificates/exact_mass_centroid.json) stores full reduced rationals and proves `Mx-Vcx=My-Vcy=Mz-Vcz=0`; therefore `P=P_raw-c_raw` has exact ordinary-volume centroid zero. The exact local shape rank is 34 via a literal identity minor. The dependent moment system `F(a,m)=M(P_raw(a))-V(P_raw(a))m=0` has `dF/dm=-V I_3`, exact rank three and determinant `-V^3<0`, so all 34 shape dimensions survive moment elimination. [Control certificate](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/certificates/control_space.json).

## Exhaustive mechanics and open neighborhood

[The directed interval audit](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/certificates/full_interval_mechanics_radius_2^-100.json) perturbs every active H coordinate independently by `±2^-100`, recomputes interval vertices, all mass terms, the ordinary centroid, all 1,630 face tests, all 3,256 vertex cones, and all four components of all 4,884 true-edge cones. No feature is ambiguous. Minimum positive intervals remain above `7.4024e-4` for stable faces, `1.6499e-1` for unstable cones, and `1.2754e-1` for saddle cones; closest excluded upper bounds are below `-3.3406e-4`, `-9.6229e-3`, and `-6.7802e-3` respectively.

[The exact topology-radius certificate](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/certificates/exact_topology_radius_2^-100.json) applies to all 3,492 supplied rows and proves that the full coordinate box `|delta q_ij|<=2^-100` preserves the active set and complete H/V/E lattice. Together these establish an open strict `(2,2,2)` cell.

## Adjacent cells and actual wall ordering

[The exact/directed atlas](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/certificates/adjacent_open_cells_atlas.json) materializes seven relevant cells:

```text
t=0.00  (F,V,E)=(1633,3262,4893)  (2,2,2)
t=0.06  (1633,3262,4893)          (2,2,2), H1 transferred
t=0.12  (1632,3260,4890)          (2,2,2), H2 transferred
t=0.24  (1630,3256,4884)          (2,2,2)
t=0.26  (1630,3256,4884)          (3,2,3), birth S500008-H(500007,500008)
t=0.32  (1630,3256,4884)          (2,2,2), death S500007-H relay
t=0.36  (1630,3256,4884)          (2,3,3), new U-H birth on (1836,500009).
```

The exact predecessor/final boundary symmetric difference has two vertex-connected components: a 52-triangle main cross-cap component and a separate 12-triangle H2 component. [The decomposition](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/certificates/exact_boundary_event_component_decomposition.json) shows why the internal octahedron couples both buttresses but the actual boundary Morse event remains split: both saddles transfer before the stable death, then the stable relays, then a new U-H pair appears.

## Rigorous residual obstruction

The promoted endpoint contains true Q edge `(1836,500009)` with endpoints `A=(1836,500009,500010)` and `B=(1836,2811,500009)`. [The exact obstruction proof](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/certificates/exact_forced_unstable_edge_obstruction.json) shows all nonmutual endpoint supports are positive, with minima `0.08849093532888678559…` and `0.09581781835674139935…`, and proves exactly

```text
A_toward_B+B_toward_A=||A-B||^2
||A-B||^2=1.320947976834277579…e-3>0.
```

The mutual supports cannot both be nonpositive, so at least one endpoint is strictly unstable in every chamber retaining these incidence/sign data. The protected unstable vertex is separately strict; therefore `U>=2` throughout the certified open chamber. This is a local architecture-specific theorem, not a global exclusion.

## Verification, mesh, and next topology

[The clean-room verifier](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/src/verify_independent.py) rebuilds all 3,492 rows, exact incidences, Cramer equalities, centroid, mechanics, structural certificates, seven adjacent cells, and meshes without importing construction/search helpers. Its final ordinary replay passed with `INDEPENDENT_EXACT_FIVEPOINT_SHARED_VOLUME_RECONSTRUCTION_PASS`. Exact C++ and GMP engines separately passed. A later optional `DEEP=1` wrapper exceeded its execution window; no claim is made that that convenience run completed.

The [OBJ](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/geometry/fivepoint_shared_volume_own_centered.obj) has 3,256 vertices and 1,630 maximal polygon faces. The [STL](sandbox:/mnt/data/Steady_Quartz_25_fivepoint_shared_volume_exact_NONWINNER/geometry/fivepoint_shared_volume_own_centered.stl) has 6,508 consistently oriented triangles, every edge incidence two, Euler two, and is watertight.

The smallest nonrepeating successor is a **one-boundary-component double-octahedral or triangular-prismatic terminal cell** joining the forcing wedge `{1836,2811,500009,500010}`, extra stable star `500008`, H1 star `{1802,500005,500006}`, and H2 star `{2592,500002,500003}`. It must delete the full edge/component `(1836,500009)` in the same actual boundary-incidence event that kills `S500008` and both saddles while retaining `S3911` and `U(2024,2377,500004)`. At least one further extreme support is topologically necessary; two connected supports are preferable for finite thickness, H2 bridging, diagonal choice, and anti-U-birth freedom. No global minimality or nonexistence theorem is claimed.

```text
WINNER: NO
DISPOSITION: EXACT NONWINNER
TRUE HIGHER-VALENCE SHARED VOLUME: PASS
OLD FORCING EDGE (2811,500008): DELETED
FINAL (V,E,F): (3256,4884,1630)
FINAL CLASS: (2,2,2)
EXACT CENTROID / HVE / FULL-CONE AUDIT / OPEN BOX: PASS
MECHANICAL EFFECT: EULER-NEUTRAL PACKET RECREATED
FIRST FORCING COMPONENT: TRUE EDGE (1836,500009), LOCALLY U>=2
INDEPENDENT REPLAY AND WATERTIGHT MESH: PASS
NEXT CELL: ONE-COMPONENT DOUBLE-OCTAHEDRAL / TRIANGULAR-PRISMATIC TERMINAL.
```
