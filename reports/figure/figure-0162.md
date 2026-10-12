# figure-0162

AI research report · 2026-08-29 UTC

---

# Rapid Quartz 69 — AQ32-CR3D580 exact support-connected endpoint

## Literal verdict

**No homogeneous convex polyhedral Gömböc was obtained.**

The strongest post-event object is the completely expanded exact-dyadic endpoint **AQ32-CR3D580**. Its point polytope `Q`, evaluated relative to its unique Santaló point, has strict class

```text
(S,U,H)_Q = (587,2075,2660).
```

Consequently, the homogeneous own-centred polar

```text
P=(Q-s(Q))°
```

has strict class

```text
(S,U,H)_P = (2075,587,2660),
```

not `(1,1,0)`. This is a rigorous finite nonwinner, not a wall point or an auxiliary-centre construction. The journal’s predecessor endpoint had class `(2611,901,3510)` and left the two packets assigned here; AQ32-CR3D580 removes both named packets and reduces the total equilibrium count by `1700`, but a new outlet packet remains.

## What changed

The construction couples the former terminal stable–saddle packet to the remote sectors `2/10` unstable–saddle packet in one finite rank-three replacement. It is not a surface subdivision or two independent serial rails:

- `2,452` predecessor coordinates move.
- `206` old rows become strictly interior.
- All `898` inserted half-sector rows are extreme.
- The exact displacement field has rank three.
- Q volume changes by a nonzero exact rational, approximately `0.0020177509023718452`.
- Each half-turn component contains an actual true-edge path from the remote packet to the terminal packet.
- The predecessor’s sectors `2/10` U-H packet and its terminal sectors `4/5` and `12/13` S-H packet are absent from the final exact audit.

The endpoint nevertheless contains a direct changed-region Q packet `(12,0,10)` and a later coarse-background U-H ladder whose first pair lies in sectors `7/15` near `gamma≈0.9977..0.9997`.

## Exact generator and incidence

Every coordinate is dyadic with common denominator

```text
D=2^118
 =332306998946228968225951765070086144.
```

The support recurrence begins at ring `J0=340`, uses separator factor `1.1`, and has terminal ring indices

```text
sector:  2   2.5   3   3.5   4   4.5   5   5.5   6
end:    580  480  570  480  515  480  570  480  580
```

plus the half-turn copies shifted by eight sectors. The exact counts are

```text
predecessor rows              23,107
candidate rows                24,005
modified predecessor rows      2,452
inserted candidate rows           898
strictly interior old rows        206
active inserted rows              898
final irredundant Q rows       23,799.
```

A fresh floating hull is used only as a seed. Exact integer four-point predicates then perform `513` diagonal repairs. The reconstructed lattices are

```text
Q: (V,E,F)=(23799,71390,47593)
P: (V,E,F)=(47593,71390,23799).
```

There is one coplanar triangulation edge, `(21447,21448)`, inside the stable square; it is removed from the true-edge list. Euler’s identity is exactly `2`.

All `206×47,593=9,804,158` inactive-row/maximal-face pairs were checked by exact integer slack and exact squared-distance comparison. The minimum inactive boundary distance is

```text
2.45725847415223e-6,
```

at candidate row `14850` against face `14843=[14797,15012,14766]`.

## Directed normalized Santaló root

The unique Santaló point is isolated in a coordinate box of radius `1e-50` around

```text
(
 0.00004565401395854277071585415637218610069075183893091810686032874340768677897006729131678,
 0.00000000000000003637846452823841022797819340372280865851000327205218560951006354475639485519092802431,
 0.00000000000000007115689829037904209027204913571232629017346422208500927402442776601668969152271099168
).
```

At its midpoint,

```text
polar volume =
4.243994245216138392444149916695582093609289762906498365428202160246927833813075652113

||M||/V =
1.112640086144269834627045371018140664721736018578946515313524627405222e-87

||F|| =
1.888815249037227862988970095839366803746885733616270971420803214140941791714223655929e-86.
```

The directed projective denominator interval is

```text
[0.9749665677930168650781716365874494779696480376346740075193108753561171,
 1.006395049123773963453326401490634909473075301712527951791468995359855].
```

The strong-monotonicity lower bound is `16.229537453140625`, giving a root-ball radius below `1.164e-87`. The positive-definite Santaló Jacobian proves global uniqueness. A separate 70-digit verifier obtains normalized residual `2.0799017172372879e-70` and root radius `2.1755619207402754e-70`, still far inside the box.

## Exhaustive full-cone mechanics

Every actual maximal face, every actual vertex tangent cone, and both normal-cone components of every true edge were evaluated over the complete root box.

The protected stable square, unstable apex, all `5,952` critical-collar rows, and the first 16-row seam ring have no unintended equilibrium. Their directed exclusion minima are

```text
maximal faces  8.758983889107709e-6
vertices       2.130231161092027e-6
true edges     2.130231161092027e-6.
```

The vertex and edge values exceed the inherited required threshold

```text
1.915868198716011e-6
```

by a factor of approximately `1.1118881573`. The stable-square margin is `0.0019531249999999289`, and the apex margin is `0.000502079342110764`.

The direct changed region has exact Q packet

```text
(S,U,H)=(12,0,10).
```

Its stable margins range from `0.0031012666357258852` to `0.009912858585424454`; its saddle margins range from `0.00011823961843194444` to `0.003357625059460366`. Every other changed-region feature is excluded with minima

```text
face    0.0016497897624357981
vertex  2.643288499157033e-5
edge    2.643288499157033e-5.
```

The first surviving coarse-background unstable vertex is row `13115`, sector `7`, at `gamma=0.9997242886757832`, with margin `2.8077380615201448e-5`. Its paired saddle is edge `(13099,13115)`, mean `gamma=0.9977242886757832`, with the same limiting primitive. Rows `13123` and edge `(13107,13123)` are their sector-`15` half-turn copies.

## Support-connected three-dimensional certificate

The moved predecessor rows have exact displacement-rank witness

```text
-18831305206160039155465074726254294055164708748814203224064 != 0.
```

The changed one-ring has two half-turn components of `2,032` vertices each and contains `7,260` cross-sector true edges. Recorded remote-to-terminal paths include

```text
A: 11778 -> 22344 -> 11779 -> 22405 -> 11812 -> 22471
B: 11786 -> 22649 -> 11787 -> 22711 -> 11820 -> 22776.
```

Every consecutive pair is an actual final true edge. The independent verifier reconstructs alternate valid shortest paths.

The exact class path is

```text
Q: (901,2611,3510) -> (595,2179,2772) -> (587,2075,2660)
P: (2611,901,3510) -> (2179,595,2772) -> (2075,587,2660).
```

The Santaló x-coordinate follows

```text
predecessor  0.00003968671156876139
central      0.0003361890199287764
final        0.00004565401395854277.
```

Thus the central volumetric move has a substantial axial response, and the inserted half-sector return rows supply a genuine opposite axial correction rather than merely cancelling transverse response by half-turn symmetry.

## Finite topology atlas

The exact construction has two recorded stages.

The simultaneous central replacement changes `2,452` coordinates and produces

```text
start Q:   (23107,69314,46209), class (901,2611,3510)
central Q: (22901,68696,45797), class (595,2179,2772).
```

Its exact incidence delta contains

```text
206 old-row deactivations
2,480 removed true edges
1,862 added true edges
3,208 removed maximal faces
2,796 added maximal faces.
```

There are `1,238` endpoint-recognizable `2–2` circuits. Each has an exact cubic determinant and one rational root interval of width at most `2^-100` on the linear coordinate homotopy.

The return stage then inserts all `898` final new rows one at a time. Every event records its exact visible patch, horizon, removed triangles, added triangles, and positive outside-plane primitive. Replaying all events reproduces the canonical final triangulation exactly.

The archive therefore contains `2,136` explicit exact event records.

**Atlas limitation:** the central linear homotopy also contains the `206` deactivations and higher-valence star changes. Exact start and endpoint cells, every deactivated row, and the complete incidence difference are materialized, but the continuous micro-order of every non-`2–2` wall and an interval Santaló root in every such microcell were not completed. The central replacement is certified as an exact simultaneous post-event endpoint, not as a fully enumerated continuous chamber path.

## Perturbation and support-error ledgers

The coordinatewise preserving box is

```text
|delta q_ij| <= 2^-400
             = 3.8725919148493183e-121.
```

Directed multilinear estimates preserve topology, positive projective denominators, root isolation, every decisive feature sign, the protected chamber, and the global nonwinner class. The smallest proof ratio is `1.4771594238854177e84`.

The conservative global smooth-support error remains far outside the earlier conditional approximation budget:

```text
rigorous L1 upper  0.4191762172559928
allowed budget     3.1342152657311286e-7
violation factor   1,337,419.99740471.
```

The actual Santaló displacement is `4.565401395854277e-5`, or `23.82941268566359` inherited local-margin units. The old global support-error theorem therefore does not apply, even though the protected local geometry survives by direct exact audit.

## Independent checks performed

- The deterministic generator was rerun from the predecessor data.
- All 14 regenerated NPZ arrays match the canonical endpoint exactly, including object-valued incidence arrays.
- The independent verifier reran to `PASS` and reconstructed the stated f-vectors, classes, root box, protected margins, packet removal, true-edge cross-incidence, event counts, perturbation box, and watertight meshes.
- The independent inactive-row proof reran all `9,804,158` exact pairs to `PASS`.
- Q has `47,594` mesh triangles and P has `95,182`; every mesh edge has incidence exactly two.

## Artifacts

- Complete mathematical handoff (`AQ32_CR3D580_complete_handoff.md`)
- Machine-readable certificate (`AQ32_CR3D580_certificate.json`)
- README (`README.md`)
- Deterministic exact generator (`generate_AQ32_CR3D580_exact.py`)
- Independent verifier (`verify_AQ32_CR3D580_exact.py`)
- Verifier output (`VERIFY_OUTPUT.json`)
- Canonical exact arrays (`AQ32_CR3D580_exact_data.npz`)
- Expanded exact Q rows (`AQ32_CR3D580_Q_vertices_exact.csv`)
- Q maximal faces (`AQ32_CR3D580_Q_maximal_faces_exact.jsonl`)
- Q true edges (`AQ32_CR3D580_Q_true_edges.csv`)
- Expanded P halfspaces (`AQ32_CR3D580_P_H_rows_root_box.csv`)
- P root-midpoint vertices (`AQ32_CR3D580_P_vertices_root_midpoint.csv`)
- P maximal faces (`AQ32_CR3D580_P_maximal_faces.jsonl`)
- P true edges (`AQ32_CR3D580_P_true_edges.csv`)
- High-precision Santaló certificate (`AQ32_CR3D580_santalo_high_precision.json`)
- Complete root-box audit (`AQ32_CR3D580_exact_rootbox_audit.json`)
- Face ledger (`AQ32_CR3D580_faces_rootbox_ledger.csv.gz`)
- Vertex ledger (`AQ32_CR3D580_vertices_rootbox_ledger.csv.gz`)
- True-edge ledger (`AQ32_CR3D580_edges_rootbox_ledger.csv.gz`)
- Residual packet (`AQ32_CR3D580_changed_packet.json`)
- Support connectivity (`AQ32_CR3D580_support_connectivity.json`)
- Rank-three coupling certificate (`AQ32_CR3D580_coupling_certificate.json`)
- Exact inactive-row separation proof (`AQ32_CR3D580_inactive_separation_exact.json`)
- Atlas summary (`AQ32_CR3D580_atlas_summary.json`)
- Central batch atlas (`AQ32_CR3D580_central_batch_atlas.json.gz`)
- Exact central circuit roots (`AQ32_CR3D580_central_2x2_roots.json.gz`)
- Exact incremental insertion atlas (`AQ32_CR3D580_incremental_atlas.json`)
- Perturbation proof (`AQ32_CR3D580_perturbation_proof.json`)
- Support-error ledger (`AQ32_CR3D580_support_error_ledger.json`)
- Finite numerical-search ledger (`AQ32_CR3D580_numerical_search_ledger.json`)
- Q OBJ (`AQ32_CR3D580_Q.obj`) and Q STL (`AQ32_CR3D580_Q.stl`)
- P OBJ (`AQ32_CR3D580_P_at_santalo_midpoint.obj`) and P STL (`AQ32_CR3D580_P_at_santalo_midpoint.stl`)

A monolithic ZIP and final SHA-256 manifest were not completed before this handoff. The README’s manifest command should therefore be disregarded unless a manifest is generated subsequently; the linked endpoint files themselves are complete and the generator/verifier reruns passed.

## Smallest not-yet-realized connected cell

Another scalar return belt, one-ray recurrence, or sequential sectors `7/15` refinement is not evidence-supported: it would leave the direct `(12,0,10)` packet intact or create another patch-exit relay.

The next finite cell must replace the support-connected union of:

1. all 12 stable and 10 saddle complete stars in the changed packet, spanning approximately `gamma=1.19..1.52`;
2. the first sectors `7/15` coarse U-H ladder, beginning at rows `13099,13107,13115,13123` near `gamma=0.996..1.000`;
3. their connecting routes, while allowing coarse anchors around rings `516,548,552,563,571,581` to deactivate.

It should use two edge-sharing nonsimplicial cells or an equivalent finite-thickness three-cell replacement. Temporary half-sector rails, especially `6.5/14.5` and potentially `1.5/9.5`, must be absorbed into shared terminal cells rather than attached separately to the coarse background. At least two independent transverse modes and one independent axial mode are required. The normalized Santaló equations must be re-isolated after every claimed actual incidence rebuild.

## Disposition

**Use AQ32-CR3D580 as a rigorous exact finite nonwinner and as positive evidence that the two assignment-named packets can be removed in one genuinely support-connected, rank-three volumetric event.** It preserves the complete critical chamber and substantially lowers the class, but the acceptance gate remains unmet. The exact unclosed geometry is now the outlet union of the new 12-stable/10-saddle terminal packet and the sectors `7/15` coarse unstable–saddle ladder; the continuous non-`2–2` central microcell order is also not yet materialized.
