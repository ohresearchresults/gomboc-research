# figure-0148

Historical AI scientific report · saved 2026-08-29 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Result: exact P9 reconstruction and a connected prismatic nonwinner

## Outcome

I did **not** obtain a strict homogeneous polyhedral Gömböc. The acceptance target `(S,U,H)=(1,1,0)` therefore remains unmet. What is new is a fully materialized exact fallback at the intended frontier:

- the journal's nine-support P9 seed reconstructed exactly from its hexadecimal dyadic rows;
- an independent exact P9-to-successor path with **47 isolated hull-circuit crossings**;
- a genuine finite-width, transversely cross-linked quadrilateral/prismatic belt in one actual three-dimensional incidence complex;
- an exact 22-support, 40-vertex own-centred endpoint with exhaustive H/V/face/edge/full-normal-cone audit, positive perturbation radius, independent verifier, and watertight OBJ/STL;
- a rigorous endpoint-local theorem excluding every **one-new-row relay**, which identifies the smallest still-unexcluded continuation.

The durable journal records P9's exact rows, incidence, `(2,2,2)` audit, norm-reversal obstruction, and the need for a communicating 10–14-support replacement. :contentReference[oaicite:0]{index=0} It also records the prior Bright-Comet 11-support endpoint and its desired four-circuit double-Y successor, but not that endpoint's coordinates or its 18-event path. :contentReference[oaicite:1]{index=1} Consequently, that particular predecessor could not be reconstructed literally from the durable state; I instead reconstructed P9 exactly and built a new exact path to a stronger, explicitly prismatic endpoint. This does not alter the journal's global status: no certified `(1,1,0)` object existed at the assignment boundary. :contentReference[oaicite:2]{index=2}

## Exact reconstruction of P9

Take support constant one and interpret each binary64 hexadecimal coefficient as its exact dyadic rational:

```text
o9   = [ 0x1.f9b5a727c027ap+2, -0x1.81e6cb4c6d6eap+1, -0x1.4a0af64ced04fp-2 ]
o13  = [ 0x1.2312b52c53f2cp+3, -0x1.59f7623ebb977p+2, -0x1.f2e1addf798e5p+0 ]
o15  = [ 0x1.1e27bebfbb450p+3, -0x1.609be75d7e57bp+2, -0x1.02e2854657074p+1 ]
o26  = [ -0x1.825d860acd07ep+0, 0x1.16d2525ea2eb7p+2, 0x1.dfe0ae19e623ap+0 ]
o27  = [ -0x1.5ed34a3e982c2p+3, 0x1.2c70c33c74c4ep+1, -0x1.cf8630f42f365p-7 ]
o32  = [ -0x1.16a333bb56517p+3, 0x1.bc6717ba18082p+1, 0x1.5ed14b53bf699p+0 ]
o100 = [ 0x1.4dbecdd9c4575p+1, -0x1.c5781d3f7120ap+1, -0x1.70ccef918f03ap+0 ]
o102 = [ -0x1.8f22b39e7cba9p+2, 0x1.069f7cc4abd26p+2, 0x1.4ed4b718d4723p+0 ]
o103 = [ -0x1.120c08072fbc0p+3, 0x1.6ca725454c6cep+1, 0x1.002b4abeac9d2p+0 ]
```

I enumerated all `C(9,3)=84` intersections with exact `Fraction` arithmetic, retained the 14 feasible vertices, integrated the ordinary uniform-volume centroid exactly, translated by that centroid, and renormalized each support row by

`H_i = B_i/(1-B_i·c)`.

The reconstructed seed has `(F,E,V,C)=(9,21,14,42)`, raw volume `0.44114661530081456`, raw centroid approximately `(0.09557254662666256, 0.4389030282873355, -0.8807270244051993)`, exact own-centroid zero, and inactive slack `0.011478213633221768`. Its strict audit is exactly the journal audit:

- stable rows: `o15`, `o27`;
- unstable triples: `(o9,o100,o103)`, `(o15,o26,o27)`;
- saddle row-pairs: `(o13,o26)`, `(o27,o100)`.

Complete exact P9 data and meshes are in [p9_exact.json](sandbox:/mnt/data/p9_exact.json), [p9_source_rows_exact.csv](sandbox:/mnt/data/p9_source_rows_exact.csv), [p9_geometry.py](sandbox:/mnt/data/p9_geometry.py), [OBJ](sandbox:/mnt/data/p9_exact.obj), and [STL](sandbox:/mnt/data/p9_exact.stl).

## Exact prismatic endpoint

After deactivating `o13,o15,o100,o103`, the final active raw source rows are the following exact dyadics. Every displayed integer triple is multiplied by `2^-20`; this is a complete compact H-source specification before own-centering:

```text
o9   : (8297915, -3166025, -338468)
o26  : (-952965, 2750839, 1183612)
o27  : (-61317545, 13127809, -79116)
o32  : (-6025484, 2402531, 948295)
o102 : (-6905877, 4543925, 1448318)
A0   : (11858931, -8049060, -3869247)
B0   : (11718289, -8699049, -2720465)
A1   : (9255979, -10800645, -6177983)
B1   : (9111926, -11917244, -4417135)
A2   : (5591554, -12803663, -8140907)
B2   : (5349805, -14272332, -5824990)
A3   : (1123184, -13817768, -9546601)
B3   : (782088, -15420996, -6761011)
A4   : (-3803431, -13678070, -10222893)
B4   : (-4141953, -15272092, -7145319)
A5   : (-8779467, -12310067, -10052711)
B5   : (-9060864, -13881607, -6970165)
A6   : (-13360792, -9740720, -8987164)
B6   : (-13659976, -11268738, -6213351)
A7   : (-17101179, -6106254, -7056186)
B7   : (-17491829, -7432545, -4829378)
B8   : (-19979876, -2560203, -2843795)
```

The exact raw centroid is stored as three rational numbers in the endpoint file and is approximately

`c_B=(0.0743044472425449, 0.03775199780352192, 0.44122857390810344)`.

The final own-centred rows are exactly

`H_i=B_i/(1-B_i·c_B)`.

The expanded rational H-data, all exact vertices, active triples, maximal face cycles, and true edges are supplied rather than truncated in prose:

- [complete exact endpoint JSON](sandbox:/mnt/data/belt_222_dyadic20_exact.json);
- [compact dyadic source rows](sandbox:/mnt/data/belt_222_source_rows_dyadic20.csv);
- [expanded centred H rows](sandbox:/mnt/data/belt_222_centered_H.csv);
- [expanded exact V-data](sandbox:/mnt/data/belt_222_vertices.csv);
- [compact incidence complex](sandbox:/mnt/data/belt_222_incidence_compact.json).

The endpoint has `(F,E,V,C)=(22,60,40,122)`, Euler characteristic two, exact ordinary centroid zero, volume `0.21481741875733254`, and exact centred inactive separation `0.00034337080922406646`.

## Actual common incidence and four-lineage communication

The polar hull graph is connected, has no articulation vertex, and is in fact 3-vertex-connected. The A/B rails are joined by actual transverse facets. The first five finite-width quadrilateral cells are:

| cell | quadrilateral boundary | actual polar triangles |
|---:|---|---|
| 0 | `A0-B0-B1-A1` | `(A0,B0,B1)`, `(A0,A1,B1)` |
| 1 | `A1-B1-B2-A2` | `(A1,B1,A2)`, `(B1,A2,B2)` |
| 2 | `A2-B2-B3-A3` | `(A2,B2,A3)`, `(B2,A3,B3)` |
| 3 | `A3-B3-B4-A4` | `(A3,B3,A4)`, `(B3,A4,B4)` |
| 4 | `A4-B4-B5-A5` | `(A4,B4,A5)`, `(B4,A5,B5)` |

Thus this is not three independent surface forks. The four residual packets communicate inside one incidence complex:

- extra stable `o9` and extra unstable face `(o9,o32,B3)` share `o9`;
- extra stable `o9` and inherited saddle `(o9,o26)` share `o9`;
- inherited saddle `(o9,o26)` and target unstable lineage `(o26,A2,A3)` share `o26`;
- the extra unstable face reaches the return saddle through the real facet chain
  `(o9,o32,B3) → (o32,B3,B4) → (B3,A4,B4) → (A4,B4,A5) → (B4,A5,B5)`;
- the A-rail and the cross-links connect that return branch back to `(o26,A2,A3)`.

This resolves the requested **communication** requirement, although it does not annihilate the Euler-neutral block.

## Exhaustive strict equilibrium audit

The clean exact audit gives:

- stable `o9`, normalized face margin `0.3465012010373353`;
- stable target `o27`, normalized face margin `0.1588146388928916`;
- extra unstable `(o9,o32,B3)`, minimum unnormalized cone coefficient `0.5797260162856321`;
- target unstable lineage `(o26,A2,A3)`, minimum unnormalized cone coefficient `0.688562411197249`;
- saddle `(o9,o26)`, minimum of its four exact edge components `0.021882772568280074`;
- saddle `(B4,B5)`, minimum of its four exact edge components `0.03338125137722773`.

Every other face is certified nonstable, every other vertex cone has a strictly negative coefficient, and every other true edge has at least one strictly negative endpoint or normal-cone component. Hence the endpoint is strict `(S,U,H)=(2,2,2)`, not a wall point.

## Exact P9-to-prism circuit atlas

I used a fixed 26-row affine raw-support homotopy. New rail rows begin as generic dyadic interior points; obsolete P9 rows end as generic dyadic interior points. At every parameter value the three ordinary moments are eliminated by the exact dependent projective translation control described below. All affine 4-row determinant polynomials were enumerated and every actual hull event was isolated.

There are 47 events: 26 `2→2` flips, 17 `1→3` activations, and 4 `3→1` deactivations. The complete exact integer polynomials and rational root intervals are in [p9_to_prism_circuit_atlas_exact.json](sandbox:/mnt/data/p9_to_prism_circuit_atlas_exact.json). The circuit identities are:

| # | type | `t` decimal locator | exact circuit row set |
|---:|:---:|---:|---|
| 0 | `2->2` | `0.033119790413804` | `(o9,o32,o100,o103)` |
| 1 | `1->3` | `0.048593668095254` | `(o15,o26,o27,A5)` |
| 2 | `1->3` | `0.059245664868855` | `(o15,o26,A4,A5)` |
| 3 | `2->2` | `0.090295358287191` | `(o13,o15,o26,A4)` |
| 4 | `3->1` | `0.106861960159428` | `(o27,o32,o100,o103)` |
| 5 | `1->3` | `0.119185447223451` | `(o27,o32,o100,B5)` |
| 6 | `2->2` | `0.124044597520177` | `(o9,o32,o100,B5)` |
| 7 | `1->3` | `0.131397527685978` | `(o9,o100,B4,B5)` |
| 8 | `2->2` | `0.135026546026658` | `(o15,o27,o100,A5)` |
| 9 | `2->2` | `0.142799736124675` | `(o27,o100,A5,B5)` |
| 10 | `2->2` | `0.144982643209201` | `(o15,o100,A5,B5)` |
| 11 | `2->2` | `0.148731836114553` | `(o15,o100,B4,B5)` |
| 12 | `1->3` | `0.148814051051630` | `(o13,o26,A3,A4)` |
| 13 | `3->1` | `0.152816839728313` | `(o9,o15,o100,B4)` |
| 14 | `2->2` | `0.167135298971085` | `(o15,B4,A5,B5)` |
| 15 | `2->2` | `0.170226684786345` | `(o15,A4,B4,A5)` |
| 16 | `2->2` | `0.174712081108362` | `(o9,o32,B4,B5)` |
| 17 | `2->2` | `0.194994132733417` | `(o13,o15,A3,A4)` |
| 18 | `1->3` | `0.219787702656138` | `(o13,o26,A2,A3)` |
| 19 | `1->3` | `0.230633039787234` | `(o9,o15,B3,B4)` |
| 20 | `2->2` | `0.269110043810965` | `(o15,B3,A4,B4)` |
| 21 | `1->3` | `0.270754486375306` | `(o13,o26,A1,A2)` |
| 22 | `2->2` | `0.278438690379796` | `(o15,A3,B3,A4)` |
| 23 | `1->3` | `0.303203868130567` | `(o13,o26,A0,A1)` |
| 24 | `2->2` | `0.313875480979307` | `(o13,o15,A2,A3)` |
| 25 | `1->3` | `0.339904424965906` | `(o9,o15,B2,B3)` |
| 26 | `2->2` | `0.345859652134582` | `(o9,o13,o26,A0)` |
| 27 | `2->2` | `0.347644840937282` | `(o15,B2,A3,B3)` |
| 28 | `2->2` | `0.353656664187527` | `(o15,A2,B2,A3)` |
| 29 | `2->2` | `0.362647333955619` | `(o9,o15,A2,B2)` |
| 30 | `3->1` | `0.368747295121672` | `(o9,o13,o15,A2)` |
| 31 | `2->2` | `0.374954367971332` | `(o9,o13,A1,A2)` |
| 32 | `3->1` | `0.377717568350274` | `(o9,o13,A0,A1)` |
| 33 | `1->3` | `0.423750564039129` | `(o27,o32,B5,B6)` |
| 34 | `1->3` | `0.430986005369550` | `(o26,o27,A5,A6)` |
| 35 | `1->3` | `0.467324342346505` | `(o9,B1,A2,B2)` |
| 36 | `2->2` | `0.469301393234901` | `(o9,A1,B1,A2)` |
| 37 | `2->2` | `0.551065924821929` | `(o26,o27,o102,A6)` |
| 38 | `2->2` | `0.567746198402149` | `(o9,A0,A1,B1)` |
| 39 | `1->3` | `0.574967484469308` | `(o9,A0,B0,B1)` |
| 40 | `2->2` | `0.679053721704490` | `(o26,o102,A5,A6)` |
| 41 | `2->2` | `0.799861080912706` | `(o9,o32,B3,B4)` |
| 42 | `1->3` | `0.803917698038871` | `(o27,o32,B6,B7)` |
| 43 | `2->2` | `0.880766353286070` | `(o26,o102,A4,A5)` |
| 44 | `1->3` | `0.951875050352612` | `(o27,o102,A6,A7)` |
| 45 | `1->3` | `0.968694140328589` | `(o27,o32,B7,B8)` |
| 46 | `2->2` | `0.995816366843816` | `(o26,o102,A3,A4)` |

Two structurally important deactivations remain distinct rather than sharing one wall:

- event 30: `(o9,o13,o15,A2)`, deactivating `o15`;
- event 32: `(o9,o13,A0,A1)`, deactivating `o13`.

This reproduces the journal's obstruction in a new explicit path: communication can be achieved without forcing those two old rows onto one shared circuit.

## Exact/interval chamber atlas

The 47 roots partition the path into 48 open hull cells. In each cell I chose a low-denominator dyadic sample and, with 80-decimal directed interval arithmetic, reconstructed every active triple, integrated the centroid, rebuilt the centred rows, proved every inactive inequality, and audited every face, vertex cone, and all four components of every true edge.

All 48 samples have positive certified inactive and mechanical-decision lower bounds. The strict class distribution is:

- 22 cells of `(2,2,2)`;
- 1 cell of `(2,3,3)`;
- 14 cells of `(3,2,3)`;
- 5 cells of `(3,3,4)`;
- 6 cells of `(4,2,4)`.

No open cell has `(1,1,0)`. The final open-cell sample has centred inactive lower bound `2.5954823185313247e-4` and mechanical decision lower bound `1.2042992929909779e-4`. The complete atlas is [p9_to_prism_chamber_audit_interval.json](sandbox:/mnt/data/p9_to_prism_chamber_audit_interval.json).

## Isolated ordinary-moment root and rank-three controls

For every raw body in the path, introduce three dependent controls `u∈R^3` by

`H_i(u)=B_i/(1-B_i·u)`.

This is not a numerical centring heuristic: exactly `P(u)=P(B)-u`. Therefore

- centroid map: `G(u)=c_B-u`;
- Jacobian: `DG=-I_3`, determinant `-1`;
- ordinary first moment: `M(u)=V(c_B-u)`;
- Jacobian: `DM=-V I_3`, rank three, determinant `-V^3`.

The unique positive-denominator root is the exact rational `u=c_B`. For the final endpoint it is isolated in a dyadic box of width `2^-120≈7.52316384526264e-37`. Full exact data are in [belt_222_moment_root_box.json](sandbox:/mnt/data/belt_222_moment_root_box.json).

## Positive perturbation radius

Directed interval arithmetic certifies independent `L∞` perturbation of **every coordinate of every raw support row** by

`ε=2^-28=3.725290298461914e-9`,

followed by recomputation of the exact dependent centroid control. On that entire box:

- every affine determinant of every four-row subset excludes zero, so the oriented matroid is fixed;
- all raw and centred inactive inequalities remain strict;
- the exact same two stable, two unstable, and two saddle features persist;
- centred inactive lower bound is `0.00026136851897556066`;
- mechanical decision lower bound is `2.0432197503427553e-05`.

The enclosure at `2^-27` was inconclusive and is not claimed. Certificate: [belt_222_perturbation_radius_interval.json](sandbox:/mnt/data/belt_222_perturbation_radius_interval.json).

## Independent verifier and meshes

The clean-room verifier [verify_p9_prismatic_cleanroom.py](sandbox:/mnt/data/verify_p9_prismatic_cleanroom.py) imports none of the construction routines. Using exact `Fraction` arithmetic, it independently:

1. reconstructs all feasible intersections among `C(22,3)` triples;
2. proves 40 simple vertices, 22 irredundant maximal faces, 60 true edges, and Euler consistency;
3. integrates the ordinary volume and centroid exactly;
4. applies exact own-centering;
5. checks every inactive inequality;
6. audits every stable face, every full vertex normal cone, and all four components of every true edge;
7. checks the OBJ vertex/facet inventory.

It returns `PASS`; canonical source-row SHA-256 is `516658719e00416c0f9aa75347f5a79128e47dd9ebaac123ae62e4f1e31b23a1`. Report: [verify_p9_prismatic_report.json](sandbox:/mnt/data/verify_p9_prismatic_report.json).

The endpoint [OBJ](sandbox:/mnt/data/belt_222_dyadic20.obj) and [STL](sandbox:/mnt/data/belt_222_dyadic20.stl) independently load as watertight, consistently wound genus-zero volumes with 40 merged vertices, 76 triangles, Euler number two, and volume `0.2148174187573326`. Mesh report: [mesh_validation_report.json](sandbox:/mnt/data/mesh_validation_report.json).

## First remaining obstruction

Let `q=H_o9`. A first relay `c` can destroy stable `o9` only if

`q·c>||q||²`.

Suppose an existing endpoint row `w` immediately witnesses `c`, so `w·c>||c||²`. Completing the square puts `c` inside the open ball `B(w/2,||w||/2)`. The maximum possible `q·c` over its closure is

`(q·w+||q||||w||)/2`.

For every existing row `w`, exact rational arithmetic proves both

`2||q||²-q·w>0`

and

`(2||q||²-q·w)²-||q||²||w||²>0`.

Hence the maximum is strictly below `||q||²` for every `w`. The tightest row is `B0`, but even it reaches only the ratio `0.6697348948348723`. Therefore **one new relay row is impossible** at this endpoint. Full exact guards are in [belt_222_one_relay_obstruction_exact.json](sandbox:/mnt/data/belt_222_one_relay_obstruction_exact.json).

There is a second coupled obstruction: `||H_o9||≈12.6811593` exceeds `||H_o27||≈12.1902311`. Any strict witness chain has increasing projected radius, so the continuation must simultaneously reverse the target norm/support-centroid ordering rather than merely append a local cap.

## Smallest nonrepeating continuation

The smallest topology not excluded by the exact atlas and the one-relay theorem is:

- at least two new extreme supports `C0,C1`;
- a shared `C0-C1` cross-edge embedded transversely in the existing finite-width belt, not two serial one-face stacks;
- one activation circuit beyond extra-U face `(o9,o32,B3)`;
- one circuit that retopologizes saddle edge `(o9,o26)` while sharing `C0,C1`;
- a bridge circuit through the real cross-linked cell `(B3,A4,B4)`;
- one circuit that retopologizes return saddle `(B4,B5)` through `C1`;
- simultaneous increase/reorientation of target `o27` sufficient for the norm reversal;
- preservation of target unstable `(o26,A2,A3)` and target stable `o27`;
- the same exact rank-three dependent moment controls throughout.

This is an endpoint-local lower bound and continuation design, not a claim of global topological minimality. A serial cap or isolated surface fork is now rigorously insufficient and empirically only transfers the `(2,2,2)` packet.

## Reusable artifact bundle

The complete bundle, including README and SHA-256 manifest, is [p9_prismatic_research_bundle.zip](sandbox:/mnt/data/p9_prismatic_research_bundle.zip). The archive contains `SHA256SUMS_P9_PRISMATIC.txt` for every member.
