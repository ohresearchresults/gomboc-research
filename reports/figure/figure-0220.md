# figure-0220

AI research report · 2026-09-02 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Nimble Comet 79 — exact J49 linked-double-octahedral terminal determination

## Finite verdict

**EXACT NONWINNER.** No homogeneous convex polyhedral Gömböc was produced. The strongest exact continuation is `J49_DO4_terminal8`, a finite rational uniform-density convex polyhedron at its exact ordinary-volume centroid with

`(H,V,E)=(8,12,18)`, equivalently primal `(V,E,F)=(12,18,8)`, and strict `(S,U,H)=(2,2,2)`.

This is nevertheless a genuine advance beyond `J48_C3_terminal7`. One connected positive-volume terminal three-ball replaces the whole old `6000` star and cap, deactivates `6000,6001,6002`, deletes the inherited forcing edge and every inherited non-target equilibrium, and preserves the intended stable face `2475` and intended unstable vertex `(2475,5000,5003)`. The transition contains two linked empty octahedral carrier cells and a fourth support that performs a nonserial stellar subdivision. The failure is an exact post-cell packet relay, not survival of the old witnesses.

The run-wide M42 exact `(2,1,1)` near-object remains the stronger equilibrium-count benchmark.

## Artifacts and integrity

- Complete exact archive (`Nimble_Comet_79_J49_DO4_terminal8_exact_NONWINNER.zip`)
- Archive SHA-256 receipt (`Nimble_Comet_79_J49_DO4_terminal8_exact_NONWINNER.zip.sha256`)
- Independent verification receipt (`Nimble_Comet_79_J49_DO4_terminal8_VERIFICATION_RECEIPT.json`)
- Expanded result report (`Nimble_Comet_79_J49_DO4_terminal8_exact_NONWINNER_RESULT.md`)
- Deterministic exact source (`J49_DO4_terminal8_exact_source.json`)
- Exact ordinary-centroid certificate (`J49_exact_ordinary_centroid.json`)
- Exact irredundancy certificate (`J49_exact_incidence_irredundancy.json`)
- Exact mechanics summary (`J49_exact_mechanics_summary.json`)
- Full exact mechanical ledger (`J49_mechanical_ledgers_point.json.gz`)
- Positive-volume transition complex (`J48_to_J49_DO4_positive_volume_cell.json`)
- Linked double-octahedral carrier certificate (`J49_linked_double_octahedral_carrier.json`)
- Residual forcing certificate (`J49_residual_forcing_obstruction.json`)
- Two-control exact response certificate (`J49_two_control_exact_response.json`)
- Perturbation-box summary (`J49_exact_metric_perturbation_box.json`)
- Complete exact perturbation ledger (`J49_exact_two_parameter_shape_box_full.json`)
- Fourth-support nonserial-minimality certificate (`J49_fourth_support_nonserial_minimality.json`)
- First remaining successor certificate (`J49_first_remaining_nonserial_successor.json`)
- Exact lattice tables: active H (`J49_H_active_exact.tsv.gz`), all supplied H (`J49_H_supplied_exact.tsv.gz`), V (`J49_V_exact.tsv.gz`), maximal-face cycles (`J49_maximal_face_cycles.tsv.gz`), true edges (`J49_true_edges.tsv`), all nonincidences (`J49_nonincident_all.tsv.gz`)
- Independent source code: main verifier (`verify_nimble_comet79_J49.py`), direct perturbation replay (`verify_j49_direct_shape_box.py`), standalone exact geometry library (`exact_geometry.py`)
- Meshes: watertight OBJ (`J49_DO4_terminal8.obj`), watertight binary STL (`J49_DO4_terminal8.stl`)

Archive SHA-256:

`b8cca0864928b2efcac9eaefdd23cc7c2d53f01e83fc0ddd5d1e2c387fa4d1dc`

Exact-source SHA-256:

`5b65e3d7c08863da5a7c6d400895ed7b2c8046d4176a725ee76d748185305ffb`

A clean extraction passed the manifest before and after execution. The main verifier ended with

`NIMBLE_COMET79_J49_DO4_ALL_INDEPENDENT_CHECKS_PASS`,

and the separately implemented complete perturbation replay regenerated its certificate byte-for-byte and ended with

`NIMBLE_COMET79_J49_SHAPE_BOX_EXACT_REPLAY_PASS`.

## Exact finite source

The endpoint supplies all thirteen inherited J48 rows plus four new rows `7000–7003`, for seventeen supplied supports. The exact direct-J48-chart coordinates of the new supports are

```text
7000 = (-1203081022784012502/576196925684131303,
        -5672338339765836994/576196925684131303,
        -60921047923148321/576196925684131303)

7001 = (-9540761699299717/18586997602713913,
        -18155605738992798/18586997602713913,
        -218646460958993/18586997602713913)

7002 = (1202299813626418175/576196925684131303,
        362116832908959110/576196925684131303,
        -88696653757511017/1152393851368262606)

7003 = (-1005129898980827784/576196925684131303,
        -5102155061118048175/576196925684131303,
        -115720110929777695/1152393851368262606).
```

They are obtained by pulling a dyadic discovery chart back through the exact rational linear map recorded in the source. Its determinant is

`576196925684131303/576460752303423488 > 0`,

so orientation and convex incidence are preserved.

The raw active rows are exactly

`[2475,0,5000,5003,7000,7001,7002,7003]`.

All other supplied rows, including `6000,6001,6002`, are strictly inactive.

The ordinary-centering map is the exact projective translation gauge

`q_i(c)=q_i/(1-q_i·c)`.

For the raw polar body, `c=M_raw/V_raw`, numerically

`c=(0.24064298961073358,-0.13584212074046590,8.615302317870185)`,

and the exact moment equation is

`M(u)=M_raw−V_raw u`.

Its Jacobian is exactly `−V_raw I_3`, hence the root is globally unique in the positive-denominator chart. The minimum exact projective denominator is positive, approximately

`0.74443082549665285`.

## Exact ordinary volume and moments

The exact centred volume, stored without abbreviation in the source and centroid certificate, is positive and equals approximately

`55.795443933007029`.

The independent verifier reconstructs the twelve exact primal vertices and sixteen oriented boundary triangles and evaluates

`V = Σ det(v_a,v_b,v_c)/6`,

`M = Σ det(v_a,v_b,v_c)(v_a+v_b+v_c)/24`.

It obtains the exact identities

`M_x=M_y=M_z=0`.

Thus the origin used for every mechanical classification is the body's own uniform-volume centroid, not an auxiliary point.

## Irredundant endpoint lattice

The active maximal-face labels are

`2475, 0, 5000, 5003, 7000, 7001, 7002, 7003`.

The topology signature is

`8781c2e817177d3e2ffeb74e26ac924ab8a8e00ff06397bc040bee0b088390cf`.

The exact minimum supplied-row/nonincident-vertex slack is positive, approximately

`0.017018726670748351`.

The actual maximal primal faces, written as oriented cycles of primal vertex indices, are

```text
2475 : 0,1,5,4,3,2
0    : 6,1,0
5000 : 0,2,7,8,9,6
5003 : 2,3,7
7000 : 3,4,10,11,8,7
7001 : 4,5,10
7002 : 6,9,11,10,5,1
7003 : 11,9,8
```

All eighteen true primal edges, expressed by their incident maximal-face labels, are

```text
2475–0
2475–5000
2475–5003
2475–7000
2475–7001
2475–7002
0–5000
0–7002
5000–5003
5000–7000
5000–7002
5000–7003
5003–7000
7000–7001
7000–7002
7000–7003
7001–7002
7002–7003
```

The display triangulation contains twelve vertices, thirty mesh edges, and twenty oriented triangles; every mesh edge has multiplicity two and

`12−30+20=2`.

After grouping coplanar pieces, the true lattice satisfies

`12−18+8=2`.

Triangulation diagonals are excluded from the mechanical edge ledger.

## Exhaustive strict mechanics

Every one of the eight maximal faces, twelve vertices/full normal cones, and eighteen true edges/full four-component cones was classified exactly.

The complete equilibrium set is

```text
stable faces:
  2475
  7000

unstable vertices, by incident H labels:
  (2475,5000,5003)
  (2475,7001,7002)

saddle true edges:
  (2475,7000)
  (7000,7002)
```

Point margins, reported as minimum positive / closest excluded, are

```text
stable:   +0.10822913275772070 / -0.12112849911755748
unstable: +0.0018454527177737101 / -0.0019085427242467336
saddle:   +0.073727902728979708 / -0.0004837698372148955
```

The endpoint is therefore an open, well-separated `(2,2,2)` cell rather than a wall or floating-point near-claim.

## What the J48-to-J49 operation actually removes

The parent and endpoint dual boundaries share only the protected two-triangle disk

```text
(2475,0,5000)
(2475,5000,5003).
```

The old complementary J48 attachment disk has

`(V,E,F)=(7,14,8)`

and contains the entire residual packet:

- stable row `6000`;
- unstable facet `(2475,6001,6002)`;
- saddles `(2475,6000)` and `(6000,6002)`;
- true forcing edge `(6000,6001)`.

The new free disk has

`(V,E,F)=(8,17,10)`

with the same oriented boundary cycle

`2475 → 0 → 5000 → 5003 → 2475`.

At J49, rows `6000,6001,6002` are strictly inactive. Every old packet feature and the old forcing edge are absent. The intended stable row `2475` and intended unstable facet `(2475,5000,5003)` remain strict.

## One connected positive-volume terminal three-ball

The exact symmetric difference of the old and new attachment disks is filled by one tetrahedral three-ball with

```text
vertices              11
edges                  33
triangular faces       37
tetrahedra             14
internal faces         19
boundary faces         18
Euler characteristic    1
```

Its tetrahedron-adjacency graph is connected. Every internal triangular face has multiplicity two; every boundary face has multiplicity one and belongs to exactly one of the old or new disks.

The exact support-space volume is positive, approximately

`0.07188005824557390`,

and the minimum exact tetrahedron volume is positive, approximately

`0.00011636036486088677`.

The shelling inserts the four new extreme rows in four connected stages:

```text
7000 : 5 positive tetrahedra
7001 : 3 positive tetrahedra
7002 : 5 positive tetrahedra
7003 : 1 positive tetrahedron
```

At every stage the certificate identifies all visible facets and proves exactly that the sum of the coned tetrahedron volumes equals the convex-hull volume increment. Consequently this is one finite-thickness boundary-disk replacement, not a supporting-face coincidence and not a stack of unconnected serial sheets.

## Linked double-octahedral carrier structure

Inside the full terminal ball are two exact empty octahedral carriers.

Carrier A has vertices

`{2475,5003,6000,6001,7000,7001}`

and exact positive volume approximately

`0.019681700647939646`.

Its three missing opposite pairs are

```text
(2475,6000)
(5003,7001)
(6001,7000).
```

Carrier B has vertices

`{5000,5003,6000,6002,7002,7003}`

and exact positive volume approximately

`0.014421573084169860`.

Its missing opposite pairs are

```text
(5000,6002)
(5003,7003)
(6000,7002).
```

Both octahedra are empty against the other terminal vertices. They share the old-star edge `(5003,6000)`, jointly touch every old residual row `6000,6001,6002`, and use all four new supports. They certify genuine linked finite-thickness communication between the stable/saddle star and the old cap sector.

The complete transition is the larger fourteen-tetrahedron ball above; no unsupported claim is made that the ball is merely the union of these two octahedra.

## Why four new supports are the first nonserial realization in this chart

Deleting `7003` leaves the exact three-support endpoint on

`[2475,0,5000,5003,7000,7001,7002]`.

Its dual triangulation is combinatorially isomorphic to J48 under

```text
6000 → 7000
6001 → 7001
6002 → 7002.
```

The entire `(2,2,2)` packet is therefore merely substituted.

Support `7003` performs a genuine dual stellar `1→3` subdivision of face

`(5000,7000,7002)`,

replacing it by

```text
(5000,7000,7003)
(5000,7002,7003)
(7000,7002,7003).
```

The lattice change is

`Δ(H,V,E)=(+1,+2,+3)`.

Thus the fourth support is the first actual nonserial topology change in this fixed preserved-disk J48 chart. This is a rigorous local minimality result, not a global theorem excluding unrelated three-support geometries.

## Two independent mechanical controls after exact moment elimination

The construction retains two explicit physical controls after all three ordinary moments are eliminated by the projective centering root.

Let

`d=e_z A^{-1}`

in the exact pullback chart. Its exact components are

```text
(-1081469758066393088/576196925684131303,
 -2739083357291806720/576196925684131303,
  571752848256139264/576196925684131303).
```

Control `a` moves row `7000` by `a d`; control `b` independently moves row `7001` by `b d`. At each `(a,b)`, the exact projective root recentres the body, so the three centred first moments and their first derivatives vanish identically.

The two response functions are

1. the incidence determinant
   `D=det(q7000−q2475,q7001−q2475,q7002−q2475)`, governing the forcing-edge/circuit sector;
2. the cap barycentric owner `λ`, the selected coefficient of the radial foot in facet `(2475,7001,7002)`.

At the endpoint their values are approximately

`(D,λ)=(0.8012458012441008,0.06121348703079533)`.

Their exact response Jacobian has decimal representation

```text
[[19.702643315013024, -43.553731824022115],
 [ 1.8433228767244354,  3.4005388666015968]]
```

with exact nonzero determinant, approximately

`147.28319460543096`.

Hence the post-centering physical response rank is exactly two. Forcing-edge incidence and cap/antibirth timing are not the same control disguised by the moment gauge.

## Exact open perturbation chamber

A separate, independently replayed anisotropic shape box uses

`p → diag(x,y,1)p`,

`q → q diag(1/x,1/y,1)`,

where

`x=1+s`, `y=1+t`, `|s|,|t|≤2^-16`.

The determinant interval is exactly

`[4294836225/4294967296, 4295098369/4294967296]`,

so every map is invertible. Incidence products are preserved exactly and the origin remains the ordinary-volume centroid.

The full interval ledger proves the complete class remains `(2,2,2)` throughout. Interval minimum-positive / excluded-upper bounds are

```text
stable:   +0.10822252662584148 / -0.12112849935316122
unstable: +0.0018454134455186315 / -0.0019084923987583654
saddle:   +0.07372563899847853 / -0.0004837718099626136
```

The separate replay program recomputed this ledger byte-for-byte without importing the builder.

## Exact residual obstruction

Both inherited J48 forcing mechanisms are gone. The post-cell endpoint, however, contains a new row-disjoint true-edge matching:

```text
(2475,0)
(7000,7001).
```

For each edge `(a,b)`, all face-stability primitives from every external neighbour at both endpoints are exactly positive. If neither endpoint were stable, the two mutual failures would imply

`||q_a||²−q_b·q_a ≤ 0`,

`||q_b||²−q_a·q_b ≤ 0`.

Adding gives

`||q_a−q_b||² ≤ 0`,

contradicting the exact positive squared difference. Each row-disjoint edge therefore forces a distinct stable endpoint. Hence

`S≥2`,

and the exhaustive audit attains equality.

The new exact Euler-neutral packet is

```text
extra stable:   7000
extra unstable: (2475,7001,7002)
saddles:        (2475,7000), (7000,7002)
forcing edge:   (7000,7001)
```

The operation deletes the old packet but does not annihilate its Morse index; it recreates the same packet on the new free disk.

## Chronology limitation

The positive-volume ball proves one connected incidence replacement and exact deletion of all inherited labels. It does **not** prove that a one-parameter path reaches all four old mechanical deaths before every new critical birth. At the materialized new free disk, the replacement packet is already strict.

Therefore the assignment's strongest chronology gate—old packet cancellation before any replacement birth—is not met, and no winner is claimed.

## First genuinely unclassified successor

The first branch not excluded by the exact endpoint, the forcing theorem, the local three-support substitution result, and the perturbation chamber is a **cross-linked two-circuit terminal volume spanning the entire `7000` star and the cap `(2475,7001,7002)`**.

In one actual incidence event it must simultaneously:

1. delete true forcing edge `(7000,7001)`;
2. destroy stable face `7000`;
3. destroy saddle `(2475,7000)`;
4. destroy saddle `(7000,7002)`;
5. destroy unstable vertex `(2475,7001,7002)`;
6. suppress every replacement U–H or S–H birth until those deaths have occurred;
7. preserve stable face `2475`;
8. preserve unstable vertex `(2475,5000,5003)`.

The generic local codimension is at least three: one new finite-volume incidence condition plus two independent mechanical response walls. The exact rank-two control certificate shows these latter walls are genuinely independent after moment elimination.

Within this branch, the smallest unexcluded realization is one additional extreme support coupled to simultaneous motion of existing terminal rows. The more robust realization is two connected supports forming a third octahedral/prismatic page, so the `7000–7001` forcing sector and the cap sector communicate through the same interior cell rather than through another stellar relay.

Excluded as repetitions are:

- the exact three-support substitution topology;
- an isolated fifth stellar page;
- another supporting-face concurrence;
- deformation restricted to the certified anisotropic endpoint box.

This is a sharp branch-local frontier, not a global nonexistence theorem.

## Verification scope and final disposition

`J49_DO4_terminal8` is **USED as an exact nonwinner and as the strongest realized J48 successor**. It satisfies the finite source, exact own-centroid, irredundant incidence, exhaustive full-cone mechanics, positive-volume connected terminal-ball, independent-control, perturbation, verifier, integrity, and watertight-mesh requirements. It does not satisfy the literal Gömböc gate because the exact row-disjoint post-cell forcing matching gives `S≥2`, attained by the full audit.
