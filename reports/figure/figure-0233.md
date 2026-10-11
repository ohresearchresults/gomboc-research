# figure-0233

Historical AI scientific report · saved 2026-09-02 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Nimble Comet 79 — J51 all-sector Y-cross-link determination

## Disposition

**EXACT NONWINNER.** I advanced `J50_XL2_terminal10` through a genuine connected all-sector topology change, but did not obtain `(S,U,H)=(1,1,0)`. The strongest endpoint is the rational, uniform-density polyhedron `J51_Y3_terminal11`, at its own exact ordinary-volume centroid, with irredundant

`(H,V,E)=(11,18,27)`, equivalently primal `(V,E,F)=(18,27,11)`, complexity `54`, and strict `(S,U,H)=(2,2,2)`.

The acceptance gate remains a finite own-centred body with one stable maximal face, one unstable vertex, no saddle true edges, exact incidence and mass data, positive margins, independent verification, and matching meshes. :contentReference[oaicite:0]{index=0} The parent J50 packet and the required all-sector successor are recorded in the journal. :contentReference[oaicite:1]{index=1}

## Exact artifacts

- [Complete archive](sandbox:/mnt/data/Nimble_Comet_79_J51_Y3_terminal11_exact_NONWINNER.zip) — SHA-256 `dd44e3d94964cb7fd444df3e63da58222dac5a163ca324bded0bb3ef58e44f72`
- [Expanded mathematical report](sandbox:/mnt/data/Nimble_Comet_79_J51_Y3_terminal11_exact_NONWINNER_RESULT.md)
- [Archive hash receipt](sandbox:/mnt/data/Nimble_Comet_79_J51_Y3_terminal11_exact_NONWINNER.zip.sha256), [independent verification receipt](sandbox:/mnt/data/Nimble_Comet_79_J51_Y3_terminal11_VERIFICATION_RECEIPT.json), and [transcript](sandbox:/mnt/data/Nimble_Comet_79_J51_Y3_terminal11_VERIFICATION_TRANSCRIPT.txt)
- [Deterministic exact source](sandbox:/mnt/data/J51_Y3_terminal11_exact_source.json), [centroid certificate](sandbox:/mnt/data/J51_exact_ordinary_centroid.json), [incidence certificate](sandbox:/mnt/data/J51_exact_incidence_irredundancy.json), [mechanics summary](sandbox:/mnt/data/J51_exact_mechanics_summary.json), and [full mechanics ledger](sandbox:/mnt/data/J51_mechanical_ledgers_point.json.gz)
- [Connected shell](sandbox:/mnt/data/J50_to_J51_connected_positive_volume_shell.json), [Y-spine](sandbox:/mnt/data/J51_Y_shaped_cross_link_spine.json), [feature genealogy](sandbox:/mnt/data/J50_to_J51_feature_genealogy.json), [external-arrow census](sandbox:/mnt/data/J51_complete_external_arrow_census.json), [forcing proof](sandbox:/mnt/data/J51_residual_forcing_obstruction.json), and [chronology obstruction](sandbox:/mnt/data/J51_death_before_birth_chronology_obstruction.json)
- [Two-control certificate](sandbox:/mnt/data/J51_two_control_exact_response.json), [perturbation certificate](sandbox:/mnt/data/J51_exact_metric_perturbation_box.json), [full perturbation ledger](sandbox:/mnt/data/J51_exact_two_parameter_shape_box_full.json), and [next-topology certificate](sandbox:/mnt/data/J51_first_remaining_nonserial_successor.json)
- Exact tables: [active H](sandbox:/mnt/data/J51_H_active_exact.tsv.gz), [supplied H](sandbox:/mnt/data/J51_H_supplied_exact.tsv.gz), [V](sandbox:/mnt/data/J51_V_exact.tsv.gz), [face cycles](sandbox:/mnt/data/J51_maximal_face_cycles.tsv.gz), [true edges](sandbox:/mnt/data/J51_true_edges.tsv), [nonincidences](sandbox:/mnt/data/J51_nonincident_all.tsv.gz)
- Meshes: [watertight OBJ](sandbox:/mnt/data/J51_Y3_terminal11.obj), [watertight STL](sandbox:/mnt/data/J51_Y3_terminal11.stl)

A clean extraction passed `MANIFEST.sha256` before and after all independent replays.

## Exact source and own centroid

The exact source supplies the ten J50 rows plus three dyadic rows:

```text
9000 = (-146631473/16777216, 0, 2125189/16777216)
9001 = (-12870813/16777216, -64610123/16777216, -713945/16777216)
9002 = (2152201/524288, 0, -987683/8388608)
```

Active labels are

`[2475,0,5000,5003,7002,7003,8000,8001,9000,9001,9002]`;

supplied rows `7001` and `8002` are strictly inactive. The exact-source SHA-256 is `862972deacd67b18fb902bf35a8c6d043a1c52ef27c6a7acf3981cd1262cb1db`.

For the raw polar primal, exact oriented tetrahedral identities give volume `V_raw` and moment `M_raw`. Applying

`q_i -> q_i/(1-q_i·c)`, where `c=M_raw/V_raw`,

represents primal translation by `-c`; hence `M(u)=M_raw−V_raw u`, with nonsingular Jacobian `−V_raw I`. The unique root is approximately

`c=(1.3479470316902615,-1.1091046233747999,62.415855532817204)`.

The exact rational volume is stored verbatim in the source and centroid certificate and is approximately `12.878154625745886`; all three centred first moments are exactly zero. Every projective denominator is positive, with minimum about `0.41893077022153802`.

## Irredundant incidence

The topology signature is `f6ccee235fed175ae2639a3a3a24c9e81c0ea0c5ff0474488a6483a39006559a`. The exact minimum supplied-row/nonincident-vertex separation is positive, approximately `3.3956062190448113e-4`.

Actual maximal primal face cycles are:

```text
2475: 0,1,6,5,4,2,3
0:    7,1,0
5000: 8,3,2
5003: 2,4,9,10,8
7002: 12,11,13,14,10,9
7003: 11,12,15
8000: 5,6,16,13,11,15
8001: 16,17,14,13
9000: 4,5,15,12,9
9001: 0,3,8,10,14,17,7
9002: 7,17,16,6,1
```

All true edges, excluding triangulation diagonals, are:

```text
(2475,0) (2475,5000) (2475,5003) (2475,8000) (2475,9000)
(2475,9001) (2475,9002) (0,9001) (0,9002) (5000,5003)
(5000,9001) (5003,7002) (5003,9000) (5003,9001) (7002,7003)
(7002,8000) (7002,8001) (7002,9000) (7002,9001) (7003,8000)
(7003,9000) (8000,8001) (8000,9000) (8000,9002) (8001,9001)
(8001,9002) (9001,9002)
```

The display surface has 18 vertices, 48 triangulation edges, and 32 triangles, so Euler characteristic is 2; the true lattice obeys `18−27+11=2`.

## Exhaustive mechanics

Every maximal face, every full vertex normal cone, and every full four-component true-edge cone was audited exactly.

```text
stable faces:      2475, 9001
unstable vertices: (2475,5000,5003), (2475,8000,9000)
saddle true edges: (2475,9000), (9001,9002)
```

Point margins, minimum positive / closest excluded:

```text
stable:   +0.26347908536174197 / -0.12140490113168247
unstable: +0.12979420196412034 / -0.22450908071969636
saddle:   +0.04090798717028311 / -0.02192743949785302
```

## The all-sector event

The exact transition uses the complete J50 raw dual hull scaled by `1/64` as the inner boundary and the exact J51 active hull as the outer boundary. The resulting connected annular shell has

`(vertices,edges,triangular faces,tetrahedra)=(21,91,127,55)`,

93 internal triangles, 34 boundary triangles, two spherical boundary components, and Euler characteristic 2. Every tetrahedron has positive exact volume. Shell volume is exactly

`48903548380853457667687116359/3713820117856140824697372672 ≈ 13.167990594300452`,

and the minimum tetrahedron volume is exactly

`966680395434974137769/7427640235712281649394745344 > 0`.

An exact eleven-tetrahedron Y-spine connects: the `9000` cap/first-saddle arm; a `9002` central bridge; and the `9001` remote-saddle/forcing arm touching both `(0,5000)` and `(7002,9001)`. This is a genuine all-sector full-boundary replacement, not a stellar page or supporting-face coincidence.

All inherited unwanted J50 features disappear: stable `7001`, cap `(2475,7003,8000)`, saddles `(2475,7002)` and `(0,5000)`, and forcing edge `(7001,7002)`. Intended stable `2475` and unstable `(2475,5000,5003)` remain strict.

The literal unscaled three-row local insertion is not an alternative: all six insertion orders are disconnected pinched complexes with three degree-four boundary edges. Exhaustion of all `C(11,6)=462` active six-subsets finds 315 octahedral subhulls but zero proper face-linked octahedral pairs covering all sectors; the Y-spine is the honest minimal equivalent.

## External arrows and exact obstruction

All 16 endpoint true edges incident to `9000/9001/9002` were exhaustively checked. Fourteen possess a certified nonpositive external face-stability arrow. Exactly two are all-positive: `(2475,9001)` and `(7002,9001)`.

Together with `(2475,0)`, the all-positive component is

`{(2475,0),(2475,9001),(7002,9001)}`.

The row-disjoint edges `(2475,0)` and `(7002,9001)` force distinct stable endpoints. For an all-positive true edge `(a,b)`, nonstability of both endpoints would imply

`||q_a||²−q_b·q_a <= 0` and `||q_b||²−q_a·q_b <= 0`,

whose sum is `||q_a−q_b||² <= 0`, contradicting its exact positive value. Thus `S>=2`, attained by the audit.

The new packet is stable `9001`, unstable cap `(2475,8000,9000)`, saddles `(2475,9000)` and `(9001,9002)`, with forcing edge `(7002,9001)`.

## Chronology, controls, and perturbation

For the exact common-scale ingress `q_900k(t)=tq_900k`, re-centred exactly at each rational `t`, the inherited packet is intact and no replacement feature exists at `t=5/12`. At `t=1/2`, replacement saddle `(5000,9002)` is already strict while inherited stable `7001`, cap `(2475,7003,8000)`, saddle `(2475,7002)`, and forcing edge `(7001,7002)` remain strict. This exactly proves that the realized ingress fails death-before-birth chronology. A `13^3` scale-cube falsification found no winner or old-gone/replacement-free state, but that grid is only empirical support.

After eliminating the three moments exactly, two controls remain independent: move `9001` in raw `+x` and `9000` in raw `+z`. The response Jacobian for the `(7002,9001)` circuit and cap-owner wall has determinant approximately `-0.7141400315565372`, exactly nonzero, hence rank 2.

The inverse-dual anisotropic box `|x−1|,|y−1|<=2^-20` preserves exact centroid and incidence. Exact polynomial intervals retain class `(2,2,2)` with lower positive margins `0.2634778713`, `0.1297942013`, `0.0409078311` for stable, unstable, and saddle tests respectively.

## First unclassified successor

The first genuinely nonrepeating topology is a **two-interior-edge four-arm anti-carrier cross-link**. It must simultaneously delete `(7002,9001)`, destabilize `9001`, break `(2475,9001)`, remove cap `(2475,8000,9000)` and both saddles, preserve `2475` and `(2475,5000,5003)`, give every new nonprotected carrier a nonpositive external arrow before activation, retain at least two post-moment timing controls, and exhibit an actual death-before-birth chamber.

Within this branch, the smallest robust architecture requires at least two additional connected extreme supports plus simultaneous motion/deactivation of `9000,9001,9002` and one neighbour of `2475`, forming two branching interior edges or a shared interior face. This is branch-local, not a global nonexistence theorem.

## Reproduction

From the archive root run `bash [internal-source-reference].sh`. The clean-room suite reconstructs the endpoint, exact mass identities, full lattice and mechanics, arrow census, chronology samples, rank-two response, perturbation box, 55-tetrahedron shell, six pinching orders, 462-subset octahedral census, and both meshes. It terminates with:

`NIMBLE_COMET79_J51_ALL_INDEPENDENT_CHECKS_PASS`.

`J51_Y3_terminal11` is **USED as an exact all-sector topology-changing nonwinner**. The exact rational M42 `(2,1,1)` body remains the run-wide equilibrium-count benchmark.
