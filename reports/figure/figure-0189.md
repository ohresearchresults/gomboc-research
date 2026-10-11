# figure-0189

Historical AI scientific report · saved 2026-09-01 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Calm Quartz 90 — exact rank-five and genuine tube-exit determination

## Literal disposition

**RIGOROUS DELIMITED NONWINNER.** No strict own-centred `(S,U,H)=(1,1,0)` metric was found.

The exact, independently verified result closes:

- all 255 plaque-anchored rank-five systems obtained from the completed rank-four frontier;
- all 5,536 adjacent positive-radius rank-five orthant boxes;
- all 13,840 one-wall adjacencies in those rank-five stars;
- 173 exact rank-four-to-rank-five full-dimensional connector tubes;
- 49 all-wall-sign-distinct genuine off-plaque tube-exit boxes and their 49 exact source-to-exit connectors.

Every certified full-dimensional box and every certified connector piece has at least two stable equilibria. The result therefore materially advances the journal’s stated rank-five/tube-exit frontier, but it is not a global exclusion of every transverse direction in the remaining trace-one SPD core. The run’s acceptance gate requires a finite materialized own-centred polyhedron, strict positive margins, complete incidence and mechanics, an independent verifier, and OBJ/STL; no near-wall or auxiliary-centre object qualifies. :contentReference[oaicite:0]{index=0} The supplied journal records the complete rank-four atlas as nonwinning and identifies rank-five/tube-exit continuation as the exact open fixed-lattice frontier. :contentReference[oaicite:1]{index=1}

## What changed relative to the journal

The journal stopped after proving that five rank-four arrangements had no SPD plaque and that the other twenty retained two stable traps through 74 tubes and 320 orthant boxes. This continuation adds the missing fifth independent metric equation, reconstructs every corresponding rank-five intersection, and then leaves the rank-four tubes through actual outgoing trap-boundary walls.

The exact accepted advancement is:

```text
rank-five systems enumerated                 255
systems retaining rank five over a_* box     255
trace-one SPD common points                   173
exact no-SPD systems                           82
positive-radius adjacent rank-five boxes     5536
exact rank-five one-wall adjacencies         13840
rank-four-to-rank-five connector paths         173
connector pieces                              2700
verified off-plaque exit boxes                  49
verified source-to-exit connectors              49
verified off-plaque connector pieces           756
minimum certified stable count                   2
winner found                                  false
```

A larger finite-protocol atlas was also constructed from every strict numerical `(2,2,2)` sign class found in 184,940 first-boundary projection trials. It contains 1,710 exact pairwise all-wall-sign-distinct radius-`2^-80` boxes with zero construction rejects. Independent replay of that enlarged atlas and construction of all 1,710 connectors had begun but did not finish before the execution boundary: the verifier had replayed 90 boxes and the connector builder had completed 117 paths. Consequently the 1,710-box expansion is supplied as a machine-checkable provisional extension, not promoted to the independently verified disposition above.

## Exact Santaló-centred fixed family

The deterministic polar generator is

```text
Q=conv{q_i},
q_i=Qint_i/2^48,
i=0,…,4323.
```

Its unique Santaló point is isolated by the strict Krawczyk certificate

```text
a_* ∈ a_c+[-2^-90,2^-90]^3,

a_c=2^-120 * (
 -39878490350125864373364388380978345,
  88581653811863381217051,
  819441514472273259270856
).
```

All polar denominators remain positive throughout this box. Let

```text
P_*=(Q-a_*)^polar.
```

Santaló stationarity gives the exact ordinary-volume identity

```text
centroid(P_*)=0.
```

Use the five trace coordinates

```text
x=(K00,K11,K01,K02,K12),
K22=1-K00-K11,
K=[[K00,K01,K02],
   [K01,K11,K12],
   [K02,K12,K22]],
K ≻ 0.
```

Thus `tr(K)=1` identically. With `A=K^-1/2`, define

```text
P_K=A P_*.
```

The centroid remains exactly zero because

```text
∫_(P_K) y dy = det(A) A ∫_(P_*) x dx = 0.
```

The transformed finite representation is

```text
h_i(K)=A^-T(q_i-a_*),
v_f(K)=A y_f/(1-a_*·y_f),
```

where every baseline `y_f` is reconstructed from its exact active support triple. Translation by `a_*`, polarity, and the invertible map `A` prove that the incidence is the actual incidence in every accepted metric cell, not a frozen numerical assumption:

```text
(H,V,E)=(4324,8644,12966),
boundary triangles=17284,
8644-12966+4324=2.
```

## Complete mechanical wall system

For every directed adjacency of maximal faces,

```text
S_ij(K)=(q_i-a_*)^T K(q_i-q_j).
```

A maximal face `i` is stable exactly when all its outgoing `S_ij` are positive. There are 25,932 directed face primitives.

For adjacent vertices `f,g`, set

```text
d_f=1-a_*·y_f,
W_fg(K)=d_g y_f^T adj(K)y_f-d_f y_f^T adj(K)y_g.
```

A vertex `f` is unstable exactly when all its outgoing `W_fg` are positive. There are 25,932 directed vertex primitives.

For a true edge with incident faces `(i,j)` and endpoints `(f,g)`, the saddle condition is the four-component conjunction

```text
S_ij>0,
S_ji>0,
W_fg>0,
W_gf>0.
```

Every explicit box audits all 51,864 directed primitives and all four components of all 12,966 true-edge cones. Triangulation diagonals are never counted as physical edges.

## Complete plaque-anchored rank-five atlas

For each all-minus rank-four chamber, every outgoing death wall of every currently stable row was appended to its four parent walls. This gives exactly 255 systems

```text
[7919,17700,bA,bB,w5].
```

All 255 coefficient matrices have exact rank five. Perturbation of the Santaló point across its complete radius-`2^-90` box is handled by a Neumann-series inverse bound, so the common point remains unique for every admissible `a_*`.

The exact disposition is:

```text
173  trace-one SPD common points
 82  no-SPD common points
```

The 82 exact failures split as

```text
K00 nonpositive                 30
leading 2×2 determinant ≤ 0     37
full determinant ≤ 0            15
```

Each failure records an exact nonpositive interval upper bound. No undecided system remains.

Around every one of the 173 SPD points, an exact collar was constructed in which only the five nominated face walls can vanish. All other face walls and all vertex walls remain strict over the full Santaló uncertainty. The collars have coordinate radii between `2^-30` and `2^-38`.

All 32 sign orthants of each five-wall plaque were realized as positive-radius dyadic boxes, producing 5,536 boxes. Their radii range from `2^-46` to `2^-54`. The exact five-cube adjacency contains 80 one-wall edges per plaque, hence 13,840 certified adjacencies. No orthant has `S=1`.

Global exact lower bounds over the 5,536 boxes are

```text
minimum face/target-wall clearance
=561033643258560049255783490703254428141701665311244803983016837097577697336102376923336362370131230470066604916039187
 /181709681073901722637330951972001133588410340171829515070372549795159822028349480831547762678440891390190630401566544483383650407153664
≈3.087527532616088e-18

minimum vertex-wall clearance
≈2.7255478008050507e-14

minimum determinant lower bound
≈9.045167510903417e-06.
```

The all-minus rank-five endpoints include eleven `(2,2,2)` cells and no `(2,1,1)` cell. Across all 5,536 orthants, the minimum stable count is two.

## Exact connectors from rank four

Each of the 173 SPD rank-five boxes was connected to its accepted rank-four all-minus source by a straight trace-coordinate segment thickened coordinatewise by `2^-100`. Adaptive exact subdivision produced 2,700 pieces, with maximum depth 12.

Every piece has positive Sylvester lower bounds and two disjoint stable trap sets. Internal face and vertex walls are allowed to cross in arbitrary order; the proof uses only strictly positive outgoing boundaries of the two trap components. The minimum exact physical trap-boundary clearance is

```text
122356299896574147792642867380344154315250734264170972951029187193250954038701700463066543045101522485527468875382671526997723319
/23258839177459420497578361852416145099316523541994177929007686373780457219628733546438113622840434097944400691400517693873107252115668992
≈5.260636567587257e-09.
```

Therefore every point in these full-dimensional connected tubes has `S≥2`.

## Genuine off-plaque tube exits

The rank-four trap cover contains 74 parameter intervals and 18,494 outgoing boundary-wall instances, involving 7,930 distinct directed face walls. For each instance, the exact common line was sampled at its two endpoints and midpoint candidates, and the wall was crossed in its exact `L∞` descent direction using five rational crossing factors. This defines a finite protocol of

```text
184,940 first-boundary projections.
```

The initial independently verified subset consists of 49 pairwise all-wall-sign-distinct strict boxes. Each has radius `2^-80`, is trace-one SPD, and has exhaustive class

```text
(S,U,H)=(2,2,2).
```

All 49 are joined to their accepted rank-four all-minus sources by exact radius-`2^-100` tubes. The 756 connector pieces retain two disjoint stable traps. Their minimum exact physical boundary margin is approximately

```text
5.093201089321578e-08.
```

The expanded finite-protocol computation found 4,852 projections with numerical `S=2`. Complete numerical face/vertex/edge audits identified 1,775 `(2,2,2)` hits in 1,710 sign-distinct classes. Every one of the 1,710 classes was then rebuilt from the exact rank-four line, an exact rational wall crossing, a 120-bit dyadic centre, and full integer interval arithmetic. All 1,710 exactifications succeeded at radius `2^-80`; no group was rejected. Their internally certified global lower bounds are

```text
minimum face-wall clearance    ≈3.049397374523314e-11
minimum vertex-wall clearance  ≈1.6371239549834258e-12
minimum determinant lower      ≈9.126423360021172e-07.
```

This 1,710-box atlas is exhaustive for the explicitly stated 184,940-point projection protocol, not for all continuous transverse directions. Because its independent replay and complete connector construction were interrupted before completion, it is not included in the rigorous promoted count of 49 exits.

## Representative actual exit polyhedron

A representative genuine exit starts from rank-four arrangement `(bA,bB)=(7920,17901)`, trap interval 1, and crosses wall

```text
12258: face 2020 → face 2091 on true edge 6129.
```

Its exact dyadic trace-coordinate centre is

```text
K00=252604928917574288960604053345342063/1329227995784915872903807060280344576
K11=197025496561034546647550071490650653/664613997892457936451903530140172288
K01=-47998011437989293107020221520959775/1329227995784915872903807060280344576
K02=7108651247779946236629304392432505/166153499473114484112975882535043072
K12=380109397710997321912754319630966761/1329227995784915872903807060280344576.
```

A coordinatewise box of radius `2^-32` is certified. Approximate centre eigenvalues are

```text
0.07391305082791728,
0.21482299116145828,
0.7112639580106246.
```

The whole box has

```text
class               (2,2,2)
stable rows          {2092,2180}
unstable vertices    {2028,2693}
saddle true edges    {1603,11125}
determinant lower    ≈0.011293607381219713
minimum face margin  ≈2.4249246337158333e-07
minimum vertex margin≈4.903981761937698e-10.
```

Its deterministic materialization reconstructs

```text
4324 H rows,
8644 vertices,
12966 true edges,
17284 boundary triangles.
```

The numerical realization has centroid norm `4.8e-15`; the zero-centroid statement is exact and structural. Maximum active-incidence residual is below `9e-16`, maximum halfspace violation below `5e-16`, and every triangulated mesh edge has multiplicity two.

## Attempts to break the negative conclusion

The following were used only for discovery, not as exact exclusions:

- 23,280 linearized simultaneous cancellation proposals from the first 49 exact exits, 10,720 of them SPD-valid, followed by 114,579 polishing evaluations: no `(1,1,0)` point;
- a compact-core direct metric search through 420 iterations: no winner, best hard defect about `2.1850e-5`;
- a full-SPD search through 280 iterations: no winner, best hard defect about `1.3225e-7`, attained near the singular boundary;
- 14,287 points in a representative coordinated joint cone: minimum stable count three;
- a sequential LP search over 300 exit sign cells and 10,874 witness LPs: no unique-stable metric; its best optimized unique-stability margin remained negative at approximately `-1.3608e-4`.

These observations reinforce the exact nonwinner atlas but do not expand its rigorous scope. A separate apparent winner generated by an unconstrained joint-manifold extrapolation was rejected because the extrapolated matrix was not positive definite.

## First genuinely unclassified coordinated cell

At the representative `(2,2,2)` exit, the nearest mechanically relevant walls are:

```text
stable row 2092:
  face wall 12479, 2092→2057, edge 6239

stable row 2180:
  face wall 13216, 2180→2215, edge 6608

unstable vertex 2028:
  vertex wall 16496, 2028→2029, edge 8248

unstable vertex 2693:
  vertex wall 9214, 2693→2719, edge 4607

saddle edge 1603:
  nearest segment wall 3207, 7246→7245

saddle edge 11125:
  nearest segment wall 22251, 6714→6712.
```

The sharpest next cancellation target is to preserve stable row 2092 and unstable vertex 2693 while jointly crossing

```text
face wall     13216,
vertex wall   16496,
segment wall   3207,
segment wall  22251.
```

This consists of one affine face equation and three adjugate-quadratic vertex/segment equations in the five trace coordinates. Generically it leaves a one-dimensional joint locus with one transverse chamber direction. No exact connector, isolated algebraic locus, or positive-radius box for this four-mechanism event has yet been certified. It is the first genuinely unclassified cell after the accepted rank-five/tube-exit atlas. Symmetric alternatives obtained by exchanging the two stable or unstable components remain secondary branches.

## Independent verification

The independent main verifier reconstructs the complete fixed lattice from the active triples and maximal-face cycles, recomputes all wall coefficients from the integer generator, verifies all Santaló perturbation bounds, reconstructs all 255 rank-five systems, checks the 82 no-SPD certificates, recomputes all 5,536 box ledgers and 13,840 adjacencies, verifies all 173 connector tubes, and rebuilds the representative exit materialization. It returned `PASS` in 194.815 seconds.

The separate off-plaque verifiers independently rebuilt all 49 accepted exit boxes and all 756 connector pieces. Both returned `PASS`.

## Reusable artifacts

Core exact rank-five atlas:

- [Structured rank-five result](sandbox:/mnt/data/calm_quartz_rank5/CALM_QUARTZ_RANK5_RESULT.json)
- [All 255 exact common-point systems](sandbox:/mnt/data/calm_quartz_rank5/RANK5_COMMON_POINT_ATLAS.json)
- [The 82 exact no-SPD certificates](sandbox:/mnt/data/calm_quartz_rank5/RANK5_NO_SPD.json)
- [The 5,536-box all-wall atlas](sandbox:/mnt/data/calm_quartz_rank5/RANK5_LOCAL_ALL_WALL_ATLAS.json)
- [The 13,840-edge adjacency atlas](sandbox:/mnt/data/calm_quartz_rank5/RANK5_LOCAL_ADJACENCY.json)
- [The 173 exact connector tubes](sandbox:/mnt/data/calm_quartz_rank5/RANK5_CONNECTOR_TRAP_COVER.json)
- [Independent main verifier](sandbox:/mnt/data/calm_quartz_rank5/verify_calm_quartz_rank5.py)
- [Main verifier PASS receipt](sandbox:/mnt/data/calm_quartz_rank5/CALM_QUARTZ_RANK5_VERIFY_OUTPUT.json)

Accepted genuine exits:

- [Verified 49-box exit atlas](sandbox:/mnt/data/calm_quartz_rank5/TRUE_EXIT_EXACT_ATLAS.json)
- [Verified 49-path connector atlas](sandbox:/mnt/data/calm_quartz_rank5/TRUE_EXIT_CONNECTOR_ATLAS.json)
- [Exit-box verifier PASS receipt](sandbox:/mnt/data/calm_quartz_rank5/TRUE_EXIT_BOXES_VERIFY_OUTPUT.json)
- [Exit-connector verifier PASS receipt](sandbox:/mnt/data/calm_quartz_rank5/TRUE_EXIT_CONNECTORS_VERIFY_OUTPUT.json)
- [Representative exit box certificate](sandbox:/mnt/data/calm_quartz_rank5/TRUE_EXIT_BOX_CERTIFICATE.json)
- [Representative exit H table](sandbox:/mnt/data/calm_quartz_rank5/true_exit_H.csv)
- [Representative exit V table](sandbox:/mnt/data/calm_quartz_rank5/true_exit_V.csv)
- [Representative true-edge table](sandbox:/mnt/data/calm_quartz_rank5/true_exit_edges.csv)
- [Representative OBJ mesh](sandbox:/mnt/data/calm_quartz_rank5/true_exit_mesh.obj)
- [Representative STL mesh](sandbox:/mnt/data/calm_quartz_rank5/true_exit_mesh.stl)
- [First unresolved joint frontier](sandbox:/mnt/data/calm_quartz_rank5/TRUE_EXIT_NEXT_FRONTIER.json)

Provisional enlarged finite-protocol extension:

- [All 1,710 constructed exact exit boxes](sandbox:/mnt/data/calm_quartz_rank5/TRUE_EXIT_EXACT_ATLAS_ALL.json)
- [Exactification builder](sandbox:/mnt/data/calm_quartz_rank5/build_true_exit_atlas_all.py)
- [Exactification transcript](sandbox:/mnt/data/calm_quartz_rank5/build_true_exit_atlas_all.log)
- [Independent enlarged-box verifier](sandbox:/mnt/data/calm_quartz_rank5/verify_true_exit_boxes_all.py)
- [Enlarged connector builder](sandbox:/mnt/data/calm_quartz_rank5/build_true_exit_connectors_all.py)
- [Enlarged connector verifier](sandbox:/mnt/data/calm_quartz_rank5/verify_true_exit_connectors_all.py)

Fixed-family reconstruction inputs:

- [Exact integer generator](sandbox:/mnt/data/calm_quartz_rank5/generator.json)
- [Actual topology and incidence](sandbox:/mnt/data/calm_quartz_rank5/topology.json)
- [Complete mechanical wall manifest](sandbox:/mnt/data/calm_quartz_rank5/wall_system_manifest.json)
- [Santaló Krawczyk certificate](sandbox:/mnt/data/calm_quartz_rank5/santalo_krawczyk_certificate.json)

## Final statement

**NONWINNER, rigorously delimited.** The complete plaque-anchored rank-five frontier and 49 connected genuine off-plaque tube-exit chambers contain no own-centred polyhedral Gömböc. The expanded finite projection protocol has constructed 1,710 further exact `(2,2,2)` boxes but awaits complete independent replay and connector certification. The first unresolved mechanism is the coordinated affine/quadratic four-wall cancellation locus `[13216,16496,3207,22251]` beyond the representative exit, not another rank-four or one-wall scan.
