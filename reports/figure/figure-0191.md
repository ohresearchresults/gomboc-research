# figure-0191

AI research report · 2026-09-01 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Quiet Raven 13 — exact all-outlet volumetric continuation

## Disposition

**NONWINNER. No homogeneous convex polyhedral Gömböc was obtained.** The acceptance gate remains a literal finite uniform-density body at its own exact volume centroid, with strict `(S,U,H)=(1,1,0)`, complete actual H/V/incidence, exhaustive face/vertex/four-component-edge mechanics, independent verification, and matching meshes. :contentReference[oaicite:0]{index=0}

This continuation does complete the next geometric step left open in the journal: the exactified `AQ32-CR3D580` outlet is replaced by one nonannular, finite-thickness, genuinely three-dimensional event spanning all four residual stable–saddle channel combinations. The result `AQ32-ALL-OUTLET-C48` is an exact-dyadic own-centred endpoint, but its class is `(2,2,2)`, not `(1,1,0)`. The old packet is destroyed and a new compact Euler-neutral packet is born at the shared terminal. This is therefore a materialized topology advance, not a winner. The journal explicitly identified the all-outlet volumetric cell as this branch’s next frontier. :contentReference[oaicite:1]{index=1}

**Artifacts:** [complete exact archive](sandbox:/mnt/data/AQ32_ALL_OUTLET_C48_EXACT_NONWINNER.zip) · [standalone mathematical handoff](sandbox:/mnt/data/AQ32_ALL_OUTLET_C48_EXACT_NONWINNER/AQ32_ALL_OUTLET_C48_complete_handoff.md)

```text
archive SHA-256  7492e86c39a0c6d65426ef010116105c2a4644a6fcd55a24dcaa59c6cfdcc84f
clean-room marker INDEPENDENT_AQ32_ALL_OUTLET_C48_EXACT_NONWINNER_VERIFICATION_PASS
clean-extract marker ALL_AQ32_ALL_OUTLET_C48_VERIFIERS_PASS
```

## Exact deterministic construction

Start with all `25,837` exact candidate rows from `AQ32_OUTLET_candidate_rows_exact.npz`, denominator `2^118`, and apply

```text
A=2^-32 [[1232442050,-2997712012,-13328199580],
         [-2997712012,9338404416,25704283391],
         [-13328199580,25704283391,197566781565]].
```

Append six rows whose numerators over `2^80` are

```text
N0=(-4259019103457880152473600, 9578814026309659451719680, 56252804853344434416254976)
N1=(-2581141375439507963248640, 4316586271334754406105088, 42252170613670782502436864)
N2=(2614496641140728956715008,-4388307471526023089094656,-42713437335124168258093056)
N3=(4229241339885126974177280,-9510963896537677029179392,-55871794597818854969180160)
C0=(-350983448002924147325796352,82596882425099634071306240,372852542225659835411595264)
C1=(25469017317928474293305344,4684689888848013707706368,37241651221771548926935040).
```

The common final denominator is `D=2^150=1427247692705959881058285969449495136382746624`. The full supplied/active ledger is

```text
parent supplied 25837
inserted              6
total supplied    25843
active/extreme         9
inactive           25834
active supplied indices = 15642,15643,15650,15966,25838,25839,25840,25841,25842.
```

The archive contains the complete `25,843`-row CSV, canonical NPZ, expanded active Q coordinates, expanded P data, and `generate_AQ32_ALL_OUTLET_C48_exact.py`. The generator independently rebuilds the complete supplied hull rather than trusting the selected nine-row subhull.

## Actual exact incidence

```text
Q: (V,E,F)=(9,21,14)
P: (V,E,F)=(14,21,9)
C=V+E+F-2=42.
```

Every Q maximal face is triangular; there is no hidden coplanar diagonal. Q maximal-face cycles are

```text
0:(1,0,7) 1:(1,8,0) 2:(0,8,7) 3:(1,7,4) 4:(1,4,8)
5:(2,7,5) 6:(2,5,8) 7:(2,6,7) 8:(2,8,6) 9:(3,4,7)
10:(3,8,4) 11:(3,7,6) 12:(3,6,8) 13:(5,7,8).
```

The complete Q true-edge set is

```text
(0,1),(0,7),(0,8),(1,4),(1,7),(1,8),(2,5),(2,6),(2,7),(2,8),
(3,4),(3,6),(3,7),(3,8),(4,7),(4,8),(5,7),(5,8),(6,7),(6,8),(7,8).
```

P vertices are indexed by Q faces. Its nine maximal-face cycles are

```text
0:(0,1,2)
1:(3,4,1,0)
2:(5,6,8,7)
3:(11,12,10,9)
4:(9,10,4,3)
5:(13,6,5)
6:(7,8,12,11)
7:(0,2,13,5,7,11,9,3)
8:(4,10,12,8,6,13,2,1).
```

All `25,834×14=361,676` inactive-row/maximal-face incidences were checked exactly. The closest inactive supplied row is source `17405` against face `10=(3,8,4)`, with positive exact slack numerator

```text
11151869360431677703416732089759359823907075343455043720773519884447423561272351536227072104338373432296023098929355342487252807712768.
```

Its Euclidean boundary distance is `3.999294277631378e-6`; the minimum active/nonincident distance is `9.479869903625081e-6`. Hence every listed row is extreme and every omitted supplied row is strictly interior.

## Directed own-centre certificate

The unique Santaló root lies in the coordinatewise radius-`1e-80` box around

```text
(-67.5534681645233231074792815521763185322694226308153960658308457162221887386963870170962900205984314959,
 16.3622119277250601407139185479595731631670279229517454315837501531028777975434256549046037004560918738,
 74.5120890905196160841581681224801307394326853278304548326520098683025779671543705892562616826600326468).
```

At the midpoint:

```text
polar volume = 0.000371088638345222901271230256744787148214988209998201612534852969502199299947678102...
||M||/V      = 1.7156492421989464e-101
||F||        = 2.5466317646624823e-104
lambda_min(DF) >= 2.55881368982767125e-9
root-ball radius <= 9.9523922932974092e-96.
```

Every projective face distance stays positive on the box:

```text
[0.9850621608482215383, 91.880211665792450001].
```

Directed interval evaluation contains zero in all three moment components, and strict convexity/positive-definite Santaló Jacobian proves uniqueness. Thus `P=(Q-s(Q))°` has **exact ordinary-volume first moments zero**; the mesh-centroid residual is irrelevant rounding, not the centring proof.

## Exhaustive full-cone mechanics

All 14 maximal faces, all nine full vertex tangent cones, and all four components of all 21 true-edge normal cones were audited over the complete root box. The exact Q features are

```text
stable faces:     face 9=(3,4,7), margin 4.831768715927734
                  face 13=(5,7,8), margin 18.06794...
unstable vertices:6=N3, margin 47.040687504217715
                  7=C0, margin 326.09799...
saddle true edges:(2,7), margin 2.4868543420712297
                  (7,8), margin 70.37963...
```

Global decisive minima are

```text
positive: faces 4.831768715927734; vertices 47.040687504217715; edges 2.4868543420712297
excluded: faces 1.2473815576779577; vertices 24.490209972646845; edges 1.254290553599379.
```

Strict polarity gives the rigorous own-centred P class `(2,2,2)`. A separate direct P midpoint reconstruction gives P stable faces `6,7`, unstable vertices `9,13`, and saddles `(5,7),(2,13)` as an independent sign/incidence cross-check.

The designated surviving target lineage is Q stable face `9=(old14635,N1,C0)` with Q unstable vertex `6=N3` (dually P unstable vertex `9` and stable face `6`). **The literal parent target incidences were not preserved.** This is an explicit failure against the strongest wording of the assignment; the endpoint is returned because it is the strongest fully materialized all-outlet event obtained, not because literal-feature preservation was achieved.

## Exact nonannular all-outlet transition complex

The four relay rows represent all combinations of the two parent stable faces and two parent saddles:

```text
N0: S5293/H(13283,14192)   N1: S5293/H(14645,15596)
N2: S15955/H(13283,14192)  N3: S15955/H(14645,15596).
```

Each lies strictly beyond its three assigned parent planes. Their exact affine rank is three; a nonzero determinant numerator is

```text
-101866397078676187815719473635008708127374290889929627484396881005355729832942302934646658297169255101847893139115020369203001447940096.
```

`N0` is inactive at the endpoint, but active rows `N1/C1` cross its stable plane and `N2/C0` cross both of its saddle planes; the other three channel triples retain active dedicated relays. The active new induced graph is

```text
N1-C0,N1-C1,N2-C0,N2-C1,N3-C0,N3-C1,C0-C1 = K5 minus N1-N2.
```

It is a triangular bipyramid with two genuine positive-volume cells

```text
T_A=[N1,N3,C0,C1], |V|=11362.280482921484
T_B=[N2,N3,C0,C1], |V|=11316.269324776917,
```

sharing internal triangle `[N3,C0,C1]` and having opposite oriented determinants. This is a literal finite-thickness three-dimensional shared event, not a surface sheet or two disconnected caps.

Relative to the parent, every vertex of old stable faces `5293,15955` is inactive; old U rows `14432,14437` survive as rows but are no longer unstable; old saddle edges `(13283,14192)` and `(14645,15596)` are absent. The complete parent six-feature label set is therefore destroyed. The failure is transport to the compact C0 star.

## Rigorous terminal obstruction

C0 has eight incident faces `0,2,3,5,7,9,11,13`. Throughout the root box,

```text
C0-s = α2 n2 + α5 n5 + α11 n11
```

with all three exact coefficient intervals strictly positive (midpoints approximately `1.16644e-90,2.47576e-90,4.12005e-91`). Any single new point `p` seeing the complete C0 star satisfies every selected normal inequality and hence

```text
(C0-s)·(p-C0)>0,
||p-s||²=||C0-s||²+2(C0-s)·(p-C0)+||p-C0||²>||C0-s||².
```

Therefore a one-apex complete-star replacement necessarily creates a point farther from the centre than C0 and cannot preserve N3 as unique unstable feature inside this centring chamber.

Independently, throughout the root box

```text
||C0-s||-||N3-s|| > 185.0036.
```

Since each radius is 1-Lipschitz in the centre, reversal requires centre displacement greater than `92.5018`. This is an exact obstruction, not a failed numerical optimizer.

The compelled local successor must split C0’s octagonal link among at least two new extreme vertices so that no single vertex sees all eight incident planes. The smallest supported topology is a **higher-valence three-cell/four-page terminal**: two independent star-splitting vertices, a third shared cross-gap/return cell, one independent antibirth mode, and three dependent Santaló coordinates. Deleting C0 from the complete supplied lattice numerically reactivates about 3,199 rows, so that successor must rebuild the whole `25,843`-row hull rather than operate only on the reduced nine-row model. The 3,199 count is discovery evidence, not an exact theorem.

## Open perturbation box

All coordinates of all supplied rows may vary independently by `2^-600`. The denominator ledger is

```text
minimum supplied nonincident oriented determinant 0.003835744088635056
minimum true-edge length                          1.8819206644539597
minimum face cross-normal norm                  107.68874048060017
minimum full edge-cone determinant               16.719556764101647.
```

The topology-change bound is `3.312e-174`, giving preservation ratio `>1.15e171`; the root shift is `<1.64e-157<1e-80`; the mechanical-score change is `<2.41e-141` versus decisive minimum `1.2473815576779577`. The incidence lattice, active selector, own-centre box, and `(2,2,2)` class are therefore open, not a wall-point artefact.

## Searches and falsification attempts

Numerical discovery searches—not promoted as exclusions—tested 25,000 valid two-vertex C0 splits, 18,000 valid three-vertex splits, all 376 full-dimensional subhulls of the final nine rows, and 4,906 reduced two-plane relay states. None produced `(1,1,0)`, `(2,1,1)`, or `(1,2,1)`; most remained `(2,2,2)`. These searches agree with, but do not extend, the exact one-apex theorem. Other higher-valence cells and global reconstructions remain unresolved.

## Verification and meshes

From a clean extraction run `./[internal-source-reference].sh`. It regenerates all 25,843 rows, compares the regenerated exact endpoint with the canonical NPZ, runs a verifier that imports neither the generator nor its topology decisions, checks all 361,676 inactive incidences, recomputes Q/P incidence and the Santaló residual, audits every full cone, verifies the two cells and terminal obstruction, checks the perturbation inequalities, and validates SHA-256 bindings and meshes. A clean extraction returned `ALL_AQ32_ALL_OUTLET_C48_VERIFIERS_PASS`.

```text
Q mesh: 9 vertices, 14 triangles, 21 edges, signed volume 24339.340323544035
P mesh: 14 vertices, 24 triangles, 36 edges, signed volume 0.00037108863834522287
```

Every mesh edge has incidence exactly two.

## Final research judgment

`AQ32-ALL-OUTLET-C48` is a rigorous exact finite all-outlet **NONWINNER**. It advances the supplied frontier by replacing every old outlet channel in one shared nonannular three-dimensional complex, exactly re-isolating the true centre, and proving the complete resulting lattice and mechanics. It also establishes a sharp local obstruction: a single terminal apex cannot eliminate C0 without becoming an even farther source. The next topology must be a star-splitting higher-valence three-cell/four-page terminal with at least two new extreme vertices, a shared return/antibirth branch, and three dependent moment controls, or else a genuinely global reconstruction whose centring point moves by more than `92.5018`.
