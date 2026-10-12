# figure-0176

AI research report · 2026-09-01 UTC

---

# Nimble Comet 70 — wall-242 tree–cotree determination

## Literal disposition

**EXACT NONWINNER.** I did not obtain a homogeneous convex polyhedral Gömböc. The wall-242 branch does contain a rigorously positive tree–cotree separator chamber after the matching is rebuilt on each *actual irredundant hull*, but the first small strict `(1,1,0)` realization is centred at an auxiliary construction point. Translating it to its own uniform-volume centroid changes its class to `(3,2,3)`. The strongest fully materialized homogeneous endpoint is an exact own-centred 19-vertex polyhedron of strict class `(2,2,2)`, not a winner. This respects the run’s acceptance gate: auxiliary-centre mechanics and near-solutions are explicitly insufficient. :contentReference[oaicite:0]{index=0}

I recovered the complete immutable wall-242 successor bundle from the persistent library, verified every archived SHA-256 entry, and independently reran both clean-room exact verifiers. Both terminate in `ALL_CHECKS_PASS`. The determination below is therefore based on literal finite H/V/E data rather than the earlier numerical `B*` trace alone.

## What changed relative to the durable journal

The journal’s live frontier was the broad 812-separator/932-support component, with retained `C81≈-1.2907×10^-4` and best numerical trial `B*=-1.270184992×10^-4`. It called for exactifying `B*`, appending its circuit clause, exhausting genuine alternating cycles, and crossing topology walls when the current cell was blocked. The recovered continuation completes that program far enough to establish four new facts: `B*` is an exact tree–cotree matching but its stored support vector does not realize the 4,321-row fan; alternating cycles really do cross separator zero; recursive matching on the actual hull reaches a robust 16-vertex construction-centre `(1,1,0)` body; and exact mass centring transports the remaining Euler-neutral block rather than preserving the target class. :contentReference[oaicite:1]{index=1}

## 1. Complete primal-tree / complementary-dual-tree reconstruction at `B*`

The exact matching has SHA-256

`e93e477c85965c7e8652d6440c9528d13bdbbd7312bfa836891a563e044df955`.

On the inherited wall-242 adjacent fan:

- `(V,E,F)=(4321,12957,8638)`;
- all `12,957` non-root vertex/face targets are matched one-to-one with true edges;
- the `4,320` vertex-owned matched edges form a primal spanning tree;
- the complementary `8,637` face-owned edges form a dual spanning tree;
- the stored separator optimum is exactly the binary64 rational represented by `t=-0.000127018499211592999`;
- the minimum stored selected separator is `-0.00012711078015326116`;
- all stored support distances lie in `[0.9984682625223652,1.272402233246424]`. :contentReference[oaicite:2]{index=2}

The support-minimal exact positive circuit added at `B*` has rank eight and the nine rows

```text
vsep:9:0:8
vsep:44:9:61
vsep:78:44:165
vsep:112:113:364
vsep:113:78:262
vsep:148:112:365
fsep:8393:8390:361
vsep:111:148:363
positive:0
```

All coefficients are exact and strictly positive; the circuit is stored in `sources/Bstar_exact_positive_circuit.json`. :contentReference[oaicite:3]{index=3}

## 2. Exact active support realization: the parent fan disappears

For every inherited row the literal polar point is

`q_i=(N_i/2^104)/h_i`,

where `N_i` is the exact integer ray numerator and `h_i` is the exact dyadic support. A direct exact homogeneous-determinant reconstruction checks all 3,414 supporting triangles against all 4,321 rational points. The resulting literal hull has:

- `1,709` active rows and `2,612` inactive rows;
- true `(V,E,F)=(1709,5121,3414)`, complexity `10242`;
- construction-origin class `(S,U,H)=(71,117,186)`;
- exact all-feature audit of all `5,121` true edges through both projection coordinates and both incident-normal coefficients;
- closest absolute primitive margins approximately `1.96067826056×10^-4` for faces, `3.65604129962×10^-7` for vertices, and `8.84101930915×10^-4` for edges;
- exact volume `V≈3.0679676289948299` and centroid
  `(-0.066824961126834406,-0.0045373994949321293,-0.0062596555413044867)`.

Thus `B*` is not merely separator-negative: the supposed 4,321-row physical chamber is absent at the stored support vector. This is the precise resolution of the durable broad-component ambiguity—matching feasibility must be coupled to irredundancy and actual support realization. :contentReference[oaicite:4]{index=4}

## 3. Full alternating-cycle freedom crosses the separator wall

Genuine alternating-cycle replacements improve the unrestricted separator margin through twelve negative states and then enter the positive state `cycG11_0000` at

`t=0.0028263201800819144`.

The crossing cycle is

```text
fsep:4877:4876:74
vsep:14:51:78
fsep:4876:4880:80
fsep:4880:4879:81
vsep:15:0:14
```

It preserves both spanning trees and violates none of the accumulated exact circuit clauses. A second positive branch, `cycG11_0003`, is also retained. But literal reconstruction again matters: the first abstract positive support vector has only `(V,E,F)=(282,840,560)`, with 4,039 parent rows inactive, centroid approximately `(-0.2086486367,-0.1437302644,-0.0621589581)`, and construction-origin class `(2,3,3)`. Abstract separator positivity alone is not a polyhedral Gömböc certificate. :contentReference[oaicite:5]{index=5}

## 4. Irredundancy-aware actual-hull recursion

At every stage the transported parent matching was discarded, the true active hull was rebuilt, all vertex and face separator candidates were regenerated, a fresh perfect edge matching was found, and the separator chamber was solved again:

| state | input rows | active rows | actual `(V,E,F)` | separator `t` |
|---|---:|---:|---:|---:|
| `Bstar` | 4321 | 1709 | `(1709,5121,3414)` | `-0.000127018499211593` |
| `positive_abstract_G11` | 4321 | 282 | `(282,840,560)` | `0.002826320180081914` |
| `actual282_matching_move` | 282 | 66 | `(66,192,128)` | `0.05944404449038641` |
| `actual66_matching_move` | 66 | 31 | `(31,87,58)` | `0.1094860369599273` |
| `actual31_alternating_cycle` | 31 | 19 | `(19,51,34)` | `0.3027932839925914` |
| `actual19_matching_move` | 19 | 16 | `(16,42,28)` | `0.7550647260809709` |
| `actual16_fixed_fan_polish` | 16 | 16 | `(16,42,28)` | `1.949556280487089` |

The decisive 31-row alternating cycle replaces `fsep:9:31:20` by `fsep:9:10:19` and `vsep:2762:0:20`. This is the first point where the *actual* hull enters a strong positive separator chamber. :contentReference[oaicite:6]{index=6}

## 5. Exact 16-vertex positive separator realization

The exact rational V-polyhedron uses source labels

`[0,262,470,1258,1371,1618,1725,1975,2152,2635,2732,2762,3188,3290,3296,3578]`.

Its construction-centre certificate is:

- `(V,E,F,C)=(16,42,28,84)`;
- strict `(S,U,H)=(1,1,0)`;
- unique stable face `[1258,3290,2635]`, barycentric margin `0.09952754015759341`;
- unique unstable vertex `0`, directed-edge margin `0.7659495533203331`;
- no saddle among all 42 true edges;
- nearest excluded vertex primitive approximately `-6.16859969296×10^-6`;
- minimum nonincident geometric distance approximately `4.23508150779×10^-5`;
- 15 selected primal-tree edges and 27 complementary-dual-tree edges, with every exact separator positive;
- matching/root inequalities remain positive throughout `|Δh_i|≤1/2`;
- all incidences and all mechanical signs remain unchanged throughout the coordinate box `|δx_ij|≤2^-26`. :contentReference[oaicite:7]{index=7}

### Exact mass-centre failure

The exact uniform-volume first moments are not zero. The exact centroid is

`c=(-0.2920208703838193,0.006686268453977127,0.004105080247636289)`

numerically. Translating by this exactly integrated centroid gives exact zero first moments but changes the class to `(3,2,3)`:

- stable faces `[0,2635,470]`, `[0,470,2762]`, `[0,2762,2732]`;
- unstable vertices `0,1618`;
- saddle edges `[0,262]`, `[0,470]`, `[0,2762]`.

Hence this body is a robust auxiliary-centre Gömböc only and is rejected. No Santaló approximation is being substituted for the mass condition: centring is the exact rational ordinary-volume centroid obtained by signed tetrahedral integration. In polar coordinates the equivalent translation gauge is the exact row renormalization `q_i↦q_i/(1-q_i·c)`. :contentReference[oaicite:8]{index=8}

## 6. Strongest exact homogeneous endpoint

The strongest exact own-centred post-gate object has source labels

`[0,262,470,1258,1371,1614,1618,1725,1975,2152,2369,2515,2635,2732,2762,3188,3290,3296,3578]`.

It is obtained from the retained 19-vertex chamber by the exact dyadic matrix

```text
[7961027721613757/562949953421312,
 4245501190543229/1125899906842624,
-5046986632983203/1125899906842624]
[0,
 8998525501380347/1125899906842624,
 1878596588671577/562949953421312]
[0,0,
 5100336463183869/576460752303423488]
```

followed by subtraction of its exact rational ordinary-volume centroid. The fully materialized result has:

- `(V,E,F,C)=(19,51,34,102)`;
- exact volume
  `14711941509755976615975323911196139012187223986743049933247936344222462843621611689959244693380141519115921 / 150306725297525326584926758194517569752043683130132471725266622178061377607334940381676735896625196994043838464`;
- exact first moments `(0,0,0)` and centroid `(0,0,0)`;
- 34 irredundant maximal triangular faces and all 51 true edges;
- minimum nonincident distance `1.6503208084248217×10^-7`;
- coordinatewise certified preserving box `|δx_ij|≤2^-43`;
- strict class `(S,U,H)=(2,2,2)`. :contentReference[oaicite:9]{index=9}

Its complete positive features are:

| feature | exact source labels | normalized margin |
|---|---|---:|
| extra stable face | `[470,1258,2762]` | `0.07784275765006744` |
| protected stable face | `[1258,2635,3296]` | `0.15945341262176688` |
| protected unstable vertex | `1258` | `2.398832369795171` |
| extra unstable vertex | `2635` | `0.0006167667279626407` |
| saddle edge | `[262,3188]` | `0.01927364714943831` |
| saddle edge | `[470,3578]` | `0.0027065936095149105` |

The nearest excluded saddle primitive is `[1258,3578]` at approximately `-0.0015054002333458082`. The object is therefore an open exact nonwinner, not a transfer-wall artefact. Every true edge is audited with the full four-component normal-cone test. :contentReference[oaicite:10]{index=10}

## 7. Exhaustion boundary inside the 19-vertex cell

The archived continuation recomputed or algebraically preserved the ordinary centroid while running:

- 200,000 global/Sobol plus local determinant-one metric trials, with no positive any-target chamber;
- all 432 first-order exclusion branches for the extra stable face, extra unstable vertex, and two saddle edges, using 18 shape variables, five metric variables, three dependent moment equations, and topology barriers;
- exhaustive deletion of every subset of at most four vertices;
- 1,493 positive-support samples of the 31-row fan followed by hard projective centring.

No target cell was found. The best linearized branch remained negative at `-0.036787536316909106`, and the best metric target score was approximately `-0.04576557058424324`. These computations do not prove a global impossibility theorem, but they close fixed-cell polishing, low-order deletions, and the tested metric/projective slices as credible next moves. :contentReference[oaicite:11]{index=11}

## 8. Exact obstruction certificate and first genuinely new successor topology

The residual incidence complex is connected and cannot be treated as two independent Morse pairs. Any next topology must act in one shared volumetric event on:

- extra stable face `[470,1258,2762]`;
- extra unstable vertex `2635`;
- saddle stars of `[262,3188]` and `[470,3578]`;
- while protecting stable `[1258,2635,3296]` and unstable vertex `1258`.

The exact fixed-cell screens show that merely moving the four witnesses transfers the block. The first genuinely new successor is therefore an **edge-sharing two-/three-cell replacement**—equivalently a small triangular-prismatic, octahedral, or double-Y volumetric patch—with two or three new cross-linked extreme supports. It must allow old labels `(470,2635,2762,3578,262,3188)` to become non-extreme together, reserve three dependent variables for exact ordinary-volume moment closure, and retain at least two independent incidence coordinates so the `S–H` and `U–H` death sheets overlap before any compensating birth. Every adjacent four-point circuit must be enumerated, and after every crossing the true hull, matching, maximal faces, true edges, and four-component edge cones must be rebuilt. Exactification should be attempted only with raw inactive separation above `10^-7`. :contentReference[oaicite:12]{index=12}

This topology is forced by the evidence: another serial rail, isolated support move, determinant-one metric, or fixed-cell separator adjustment repeats an already tested mechanism.

## 9. Independent verifier and mesh/export record

The recovered bundle contains two independent clean-room verifiers:

- `scripts/verify_rapid_maple42_cleanroom.py` reconstructs the 16-vertex construction-centre body, its own-centred translation, and the exact centred 19-vertex body from exported rational data; enumerates all supporting triples, maximal faces, true edges, and full edge cones; integrates exact volume and moments; checks the tree/cotree certificate; and validates OBJ topology.
- `scripts/verify_bstar_exact_support_cleanroom.py`, together with the exact C++ homogeneous-determinant checker, reconstructs all literal `B*` support points, checks all H incidences, all 5,121 true edges, exact mechanics, and exact mass integrals.

I reran both verifiers in a fresh recovered extraction; both ended `ALL_CHECKS_PASS`. I also reran the complete SHA-256 manifest with no mismatch. :contentReference[oaicite:13]{index=13}

### Portable artifacts

- [Complete wall-242 exact archive](sandbox:/mnt/data/wall242_recovery/rapid_maple42_wall242_handoff.zip) — SHA-256 `fe92046adee61f4d6e706d541df55c387b38933119c5aa81997b954369747ee9`.
- [Nimble Comet 70 verification wrapper](sandbox:/mnt/data/Nimble_Comet_70_wall242_exact_NONWINNER.zip) — SHA-256 `bc22408ed724328f7defcaf3644913ec7087d373262d18c40c94126dbb422aac`.
- [Exact 19-vertex V-data](sandbox:/mnt/data/wall242_recovery/rapid_maple42_wall242_handoff/rapid_maple42_wall242_handoff/exact/wall242_centered19_metric_exact_V_exact.csv)
- [Exact irredundant H-data](sandbox:/mnt/data/wall242_recovery/rapid_maple42_wall242_handoff/rapid_maple42_wall242_handoff/exact/wall242_centered19_metric_exact_H_irredundant.csv)
- [All maximal faces](sandbox:/mnt/data/wall242_recovery/rapid_maple42_wall242_handoff/rapid_maple42_wall242_handoff/exact/wall242_centered19_metric_exact_faces.csv)
- [All true edges and four-component cone data](sandbox:/mnt/data/wall242_recovery/rapid_maple42_wall242_handoff/rapid_maple42_wall242_handoff/exact/wall242_centered19_metric_exact_true_edges_full_cones.csv)
- [Exact centroid/mechanics audit](sandbox:/mnt/data/wall242_recovery/rapid_maple42_wall242_handoff/rapid_maple42_wall242_handoff/exact/wall242_centered19_metric_exact_exact_audit.json)
- [Perturbation certificate](sandbox:/mnt/data/wall242_recovery/rapid_maple42_wall242_handoff/rapid_maple42_wall242_handoff/exact/wall242_centered19_metric_exact_perturbation_certificate.json)
- [OBJ](sandbox:/mnt/data/wall242_recovery/rapid_maple42_wall242_handoff/rapid_maple42_wall242_handoff/exact/wall242_centered19_metric_exact.obj)
- [STL](sandbox:/mnt/data/wall242_recovery/rapid_maple42_wall242_handoff/rapid_maple42_wall242_handoff/exact/wall242_centered19_metric_exact.stl)

## Final determination

**NONWINNER.** The exact wall-242 matching branch successfully crosses into a strictly positive separator chamber and yields a robust finite `(1,1,0)` polyhedron relative to a construction centre, but not at the body’s own mass centroid. The strongest literal homogeneous object is the exact 19-vertex `(2,2,2)` polyhedron above. Its complete obstruction certificate forces the next search out of the fixed cell and into the shared cross-linked volumetric replacement of the entire residual four-feature block.
