# figure-0154

AI research report · 2026-08-29 UTC

---

# Rapid Quartz 69 — AQ32-FBR380 exact four-branch return cell

## Literal verdict

**No homogeneous convex polyhedral Gömböc was obtained.** The strongest endpoint is the fully expanded exact-dyadic AQ32-FBR380 body. It is a rigorous finite nonwinner, not a near-wall or auxiliary-centre claim. The run’s acceptance gate requires a materialized finite uniform-density polyhedron at its own exact volume centroid, strict `(S,U,H)=(1,1,0)`, complete H/V incidence and true-edge/full-normal-cone auditing, an independent exact or directed verifier, and matching OBJ/STL.

AQ32-FBR380 directly continues the journal’s exact AQ32-A2 frontier: AQ32-A2 had 22,541 rows, own-centred class `(2871,903,3772)`, removed the original sectors `6/14` packet, and transferred it to sectors `4/12` near `gamma=0.4417..0.4437`; the assigned successor was a genuine two-dimensional half-turn four-branch return cell with independent axial leverage.

The new endpoint has

```text
Q: (V,E,F) = (23107,69314,46209), root-box class (901,2611,3510)
P=(Q-s(Q))°: (V,E,F) = (46209,69314,23107), own-centred class (2611,901,3510).
```

It therefore fails the target decisively. However, it genuinely removes the assignment-named sectors `4/12` unstable–saddle packet, preserves the complete protected collar, and reduces the own-centred P counts from `(2871,903,3772)` to `(2611,901,3510)`. The realized four-branch terminal creates a new exact Q packet of 12 stable faces and 20 saddle true edges, while the first remaining remote Q unstable–saddle packet lies in sectors `2/10` near `gamma=0.6577..0.6597`.

## Complete reusable artifact

- Complete exact archive (`RQ69_AQ32_FBR380_exact_endpoint.zip`) — SHA-256 `af6576d817e1c1bbc3712b8814c90a4917c82fd84547dd64f7f313ff09969c98`; `unzip -tq` passes.
- Full handoff (`AQ32_FBR380_complete_handoff.md`) — SHA-256 `392c7652d266779dda7eb1909382303ae96db4279f460743bc9b68307dd2ae9f`.
- README and reproduction commands (`README.md`) — SHA-256 `07d027e35fc9663799c71ff8f3fa6717df5995524958ecb4c1449019c7edbddd`.
- Consolidated certificate (`AQ32_FBR380_certificate.json`) — SHA-256 `0029aad2e9f506051a0822c6719ac9b0c4ac8a47f903f7547121b52a7c3c0a96`.
- Deterministic exact generator (`generate_AQ32_FBR380_exact.py`) — SHA-256 `c4161c693213a1b8879686a68dafc494c9d9c6bf858f67e851644a8188bfe6e0`.
- Independent verifier (`verify_AQ32_FBR380_exact.py`) — SHA-256 `0b3b4a14c794a4461ab4cc6cfdcd9e81be1e1d2493b74577e366f1f40a36a14a`.
- Verifier transcript (`VERIFY_OUTPUT.json`) — SHA-256 `3c4bb3a5efe09c10ffe3a4b5cbd63636273b20f9cf298cb21b79d9dfc00085f9`.
- Canonical exact arrays (`AQ32_FBR380_exact_data.npz`).
- SHA-256 manifest (`SHA256SUMS.txt`).

A clean-room extraction of the ZIP independently passed `sha256sum -c SHA256SUMS.txt` and reran the verifier to `PASS` with the same f-vectors and class.

## Exact generator

Every Q coordinate is dyadic with common denominator

```text
D=2^118=332306998946228968225951765070086144.
```

The cell begins at ring `J0=309`, uses terminal index `J1=380`, and applies the inherited separator recurrence with factor `1.1`. Its integer-sector branches are

```text
core 4,5,12,13 through ring 379;
side 3,6,11,14 through ring 377.
```

Its half-sector branches are

```text
4.5,12.5 through ring 379;
3.5,5.5,11.5,13.5 through ring 373;
2.5,6.5,10.5,14.5 through ring 368.
```

This is not four independent one-dimensional rays. The staggered integer and half-sector branches rebuild into transverse cross-links and shared terminal faces. The candidate contains 23,173 rows: 552 AQ32-A2 rows are changed and 632 gap candidates are inserted. Exact hull reconstruction proves 66 candidates redundant—44 central rows and 22 gap candidates—and all 23,107 emitted rows irredundant.

The stable square, unstable apex, all 5,952 critical-collar rows, and the first 16-row seam ring are copied without coordinate change. The exact coordinates and source mappings are in the expanded Q row table (`AQ32_FBR380_Q_vertices_exact.csv`) and the canonical NPZ.

## Actual exact incidence

A new floating hull is used only as a seed. Exact integer 4-point predicates repair every locally nonconvex diagonal. The clean-room rebuild performs 513 exact 2–2 flips and reproduces the canonical maximal faces and true edges.

```text
Q vertices              23,107
Q triangulation edges   69,315
Q true edges            69,314
Q triangles             46,210
Q maximal faces         46,209
Euler value             2.
```

There is one exact zero triangulation edge, `(21653,21654)`, the internal diagonal of the stable square; it is removed from the true-edge list. The minimum nonzero adjacent orientation is attained at edge `(166,181)` and has exact integer determinant

```text
127147975046385277374519693584517482939106762318038021311082705465281036499853312,
```

physical magnitude `3.464902217509549e-27`.

Expanded incidence is available as:

- Q maximal faces (`AQ32_FBR380_Q_maximal_faces_exact.jsonl`) and Q true edges (`AQ32_FBR380_Q_true_edges.csv`).
- P halfspaces over the root box (`AQ32_FBR380_P_H_rows_root_box.csv`), P root-midpoint vertices (`AQ32_FBR380_P_vertices_root_midpoint.csv`), P maximal faces (`AQ32_FBR380_P_maximal_faces.jsonl`), and P true edges (`AQ32_FBR380_P_true_edges.csv`).

The 66 omitted candidate rows have minimum directed distance `1.2696884279123912e-6` from the final boundary. The final H/V representation itself is irredundant.

## Directed normalized Santaló root

The unique Santaló point is isolated in a coordinate box of radius `1e-50` around

```text
( 0.00003968671156876139059142740795643495183096515370874834067377684642771770902517328485011,
 -0.00000000000000001209639472495655499431307739705696960892281766453998909493468414384164352137761206195,
 -0.000000000000000007229130001648687727322862731853569790190050908014431315491706572655207995400789076084 ).
```

At the midpoint:

```text
V                = 4.242716106556353851947899784424233246648852735656530002109915829273410180581290425245
||M||/V          = 6.5875043668281759e-86
||F||            = 1.1179564351660887e-84
lambda_min(DF)   >= 16.2300186174107053744
root radius      <= 6.8882018038279031e-86.
```

Every projective denominator is positive and lies in

```text
[0.97641842346198369859,1.00638908182215616523].
```

Positive definiteness of the Santaló Jacobian gives global uniqueness. The independent verifier uses a separate 70-digit recomputation and still obtains radius `1.9219394921111856e-71 < 1e-50`. The full data are in the high-precision Santaló certificate (`AQ32_FBR380_santalo_high_precision.json`).

## Exhaustive full-cone mechanics

Every actual maximal face, every vertex/full tangent cone, and every true edge/full normal cone is evaluated over the complete Santaló box. The directed result is

```text
Q relative to s(Q): (901,2611,3510)
P own-centred:       (2611,901,3510).
```

The protected target/collar/seam set has no extra equilibrium. Its directed exclusion minima are

```text
maximal faces  8.639125627780842e-6
vertices       2.127254139355520e-6
true edges     2.127254139355520e-6,
```

which exceed the inherited threshold `1.915868198716011e-6` by factors `4.50925`, `1.11033`, and `1.11033`. The stable square margin is `0.0019531249999999879`; the apex margin is `0.0005020763650901561`.

The direct four-branch terminal region has exact Q packet

```text
(S,U,H)=(12,0,20).
```

Every other direct-FBR feature is excluded with minimum components

```text
face    2.079354706512303e-5
vertex  1.8866343285545124e-5
edge    1.8866343285545124e-5.
```

The complete directed audit is in the root-box summary (`AQ32_FBR380_exact_rootbox_audit.json`), face ledger (`AQ32_FBR380_faces_rootbox_ledger.csv.gz`), vertex ledger (`AQ32_FBR380_vertices_rootbox_ledger.csv.gz`), and edge ledger (`AQ32_FBR380_edges_rootbox_ledger.csv.gz`).

## Precise first remaining packets

The original sectors `4/12` unstable–saddle pair is absent.

The first surviving Q unstable packet is

```text
row 11794: sector 2,  gamma 0.6597242886757829,
row 11802: sector 10, gamma 0.6597242886757829,
margin 3.6032527557642276e-5 and 3.6032527557650787e-5.
```

The paired first Q saddles are

```text
edge (11778,11794), mean gamma 0.6577242886757829,
edge (11786,11802), mean gamma 0.6577242886757829,
```

with the same limiting exact primitive.

The first remaining stable feature is already part of the new terminal packet:

```text
face 5374, cycle (11877,22747,11993),
core sector 5 ring 370 / gap 5.5 ring 369 / coarse sector 5 ring 380,
minimum gamma 0.6757242886757829,
margin 0.00560197341578711.
```

The first pure coarse-background stable strip remains

```text
face 1698, cycle (14390,14391,14406),
gamma 1.3197242886757834,
margin 9.761144118731246e-5.
```

The complete exact terminal packet is in AQ32_FBR380_changed_terminal_packet.json.

## Exact finite atlas and its honest boundary

The 552-row central replacement has independently rebuilt exact endpoint cells:

```text
AQ32-A2:         (22541,67616,45077), Q class (903,2871,3772)
central endpoint:(22497,67484,44989), Q class (905,2637,3540).
```

Exactly 44 old rows deactivate; 466 true edges and 690 maximal faces are removed, while 334 true edges and 602 maximal faces are added.

Among these changes, 284 are endpoint-recognizable 2–2 circuits. On the exact linear coordinate homotopy, every one has an integer polynomial and a unique rational root interval of width at most `2^-100`; the 284 roots are totally ordered in the exact central root file (`AQ32_FBR380_central_2x2_roots.json.gz`). The full endpoint incidence delta is in the central batch atlas (`AQ32_FBR380_central_batch_atlas.json.gz`).

The 610 final-active gap rows are then inserted one at a time in increasing `(gamma,azimuth)` order. Each exact event records the visible patch, horizon, removed and added triangles, and positive outside-plane distance. The final incremental triangulation equals the canonical final triangulation exactly; both set differences are zero. See the insertion atlas (`AQ32_FBR380_gap_incremental_atlas.json`).

Thus `284+610=894` transition events are fully explicit and exactly ordered within their stated paths.

**Atlas limitation:** the central linear homotopy also has 44 vertex deactivations and higher-valence star changes. Their exact start and endpoint incidences are materialized, but this archive does not claim a complete continuous order for those non-2–2 walls. This is the exact unclosed atlas boundary; no counterfactual complete-cell claim is made.

## Support-error and axial response

The four-branch cell provides real axial leverage: the Santaló displacement decreases from AQ32-A2’s approximately `8.5551940e-5` to `3.968671156876139e-5`. But the support approximation remains far outside the inherited global budget.

```text
maximum corresponding-row displacement  0.004053922342280897
baseline AQ16 L1 upper                    0.354016237585653
added Hausdorff-to-L1 term                0.05094309059493277
final rigorous L1 upper                   0.4049593281805858
allowed budget                            3.1342152657311286e-7
violation factor                          1,292,059.7146224403.
```

The actual Santaló displacement is `20.714739978125262` required local-margin units. Local exact geometry survives; the old conditional global support-error theorem does not apply. See the support-error ledger (`AQ32_FBR380_support_error_ledger.json`).

## Perturbation certificate

The exact coordinatewise open box is

```text
|delta q_ij| <= 2^-400 = 3.8725919148493183e-121.
```

Directed multilinear bounds preserve topology, root enclosure, projective interiority, target/collar signs, terminal-packet signs, and the global class. The smallest proof ratio is `1.4771594238854177e84>1`, from the edge-cone denominator. The root remains inside the `1e-50` box. See the perturbation proof (`AQ32_FBR380_perturbation_proof.json`).

## Independent verifier and meshes

`verify_AQ32_FBR380_exact.py` regenerates every row, independently rebuilds and exact-repairs the hull, reconstructs grouped maximal faces and true edges, recomputes the root box, audits every full cone, and checks the atlas, perturbation proof, manifest and meshes. It returns `PASS` with the numbers above.

- Q OBJ (`AQ32_FBR380_Q.obj`) and Q STL (`AQ32_FBR380_Q.stl`): 23,107 vertices, 46,210 triangles.
- P OBJ (`AQ32_FBR380_P_at_santalo_midpoint.obj`) and P STL (`AQ32_FBR380_P_at_santalo_midpoint.stl`): 46,209 vertices, 92,414 triangles.

Every mesh edge has incidence exactly two.

## What was tried and rejected

The selected endpoint followed finite tests of compact bumps, one more near-side recurrence, uniform 32-sector bands, smooth return tapers, scalar far-side return belts, terminal point controls, cut-plane controls, and stagger/end-shift searches. The alternatives either created larger S/U/H packets, overshot the axial Santaló response and reopened critical-region packets, or transferred the defect to the patch exit. None produced fewer than 3,510 Q saddle edges while retaining the protected chamber. These are finite experiments, not global exclusions.

## Strongest inference and smallest continuation

**Observation:** the named sectors `4/12` packet can be removed while preserving every protected feature and reducing global counts substantially.

**Observation:** attaching the staggered return directly to the coarse ring creates an exact terminal Q S-H packet before the old remote stable strip, while a separate Q U-H packet survives in sectors `2/10`.

**Inference:** sequentially refining the sectors `2/10` packet alone is redundant; it would leave the exact terminal packet untouched. Another half-turn-even scalar belt is also structurally inadequate because it lacks independent axial sign control.

The smallest evidence-supported next cell must therefore:

1. replace the complete terminal S-H stars around sectors `4.5/5/5.5` and `12.5/13/13.5`, approximately `gamma=0.6757..0.7197`;
2. connect them in the same genuine two-cell/three-dimensional event to the sectors `2/10` U-H stars near `gamma=0.6557..0.6597`;
3. allow terminal core, side, gap, and selected coarse-ring rows to deactivate together rather than joining each temporary rail separately to the background;
4. carry two independent transverse controls and one axial control whose degree-one response is not forced to add under half-turn pairing;
5. solve all three normalized Santaló equations as dependent equations after every actual incidence rebuild;
6. if that centred path reaches the remote stable wall, incorporate the sectors `2/3` and `10/11` strip near `gamma=1.3197243` into the same connected event.

## Disposition

**Use AQ32-FBR380 as a rigorous exact finite nonwinner and a sharper topology/centering obstruction.** It closes the assignment-named sectors `4/12` defect, validates a genuine two-dimensional adaptive mechanism, and preserves the certified critical collar. It also proves that this realized staggered terminal architecture does not enter the open `(1,1,0)` chamber: the first unclosed topology is the support-connected union of the terminal Q S-H packet and remote sectors `2/10` Q U-H packet. The global acceptance gate remains unmet.
