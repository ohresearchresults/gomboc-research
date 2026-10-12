# figure-0118

AI research report · 2026-08-27 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Determination

No strict finite homogeneous polyhedral Gömböc was found. The required gate remains an explicit uniform-density polyhedron evaluated at its own exact volume centroid with exhaustive strict `(S,U,H)=(1,1,0)` mechanics; auxiliary centres, wall points and near-solutions do not qualify.

This continuation nevertheless advances the M42 branch in three concrete ways:

1. the exact-decimal M42-SLP seed was independently reconstructed from scratch;
2. the strongest genuinely separated transverse endpoint was exactified, fully audited, given a nonzero perturbation box, and exported as OBJ/STL;
3. an exact nonlocal obstruction was isolated at its terminal relay.

The complete detailed handoff, including all 50 coordinates, all maximal-face cycles, all 67 true edges, exact primitive ledgers and continuation details, is here (`m42_research_handoff.md`).

# Exact M42 seed reconstruction

The 42 journal coordinates were interpreted literally as terminating rationals. The exact reconstruction agrees with the recorded active set and frontier.

```text
active =
0..16,28,29,30,31,32,33,34,35,36,37,38,40

(V,E,F,C) = (29,67,40,134)
(S,U,H)   = (2,2,2)

stable:   base 17-gon; [8,40,9]
unstable: 8; 34
saddles:  (4,38); (14,31)
```

Exact seed volume:

```text
3702056925588554198256875532832399692295961450120267
----------------------------------------------------------------
3000000000000000000000000000000000000000000000000000
```

Exact seed centroid:

```text
cx = 14911266126291970291218680442585381020198308201234179308779688950021
     --------------------------------------------------------------------
     59232910809416867172110008525318395076735383201924272000000000000000

cy = -2045306624660345859124144547294383219632032062525015902581007338352599
      ----------------------------------------------------------------------
      2961645540470843358605500426265919753836769160096213600000000000000000

cz = -38310443446861378024830098365774161988650901966632689638735566273861
      ---------------------------------------------------------------------
      269240503679167578055045493296901795803342650917837600000000000000000
```

# Strongest separated transverse endpoint

Rows `42..49` are exact terminating decimals:

```text
42  1.4413773170767861   -2.3885487606201994  -0.664644168696922
43  1.4354787177148578   -2.2408739938957853  -0.65287380732010425
44  1.1504735833328155   -2.6330084933899305  -0.32135610472941745
45  1.2031026053597558   -2.6380616829676433  -0.54403867232415315
46  0.88969515961261558  -2.8384029574151231  -0.4813648208639279
47  0.88192610227077528  -2.8384405289831762  -0.49399081059222788
48  0.24720669443545343  -2.4976437914114418  -0.24637138684718804
49  0.10687557689536829  -2.5644272493217430  -0.30045001439239361
```

All eight are actual hull vertices. The active set is

```text
0..16,28,29,32,33,42,43,44,45,46,47,48,49.
```

Seed-active rows `30,31,34,35,36,37,38,40` deactivate together. Thus every specifically permitted row `31,34,35,38,40` deactivates, although rows `30,36,37` also become interior.

The bridge is genuinely volumetric: rows `(43,44,47,49)` have exact nonzero oriented tetrahedral determinant

```text
-7608925533288053680716140477682551240582625521161
----------------------------------------------------------------
 50000000000000000000000000000000000000000000000000
```

with absolute tetrahedron volume `0.02536308511096018`.

Endpoint data:

```text
(V,E,F,C) = (29,67,40,134)
(S,U,H)   = (4,3,5)
hard score = -0.01590428894647683
minimum bridge-row distance = |p46-p47| = 0.014824819736599338
minimum inactive-point separation = 0.0028122892 at row 22
```

Exact volume:

```text
5661643073467287735837781974727673003334693328719811
----------------------------------------------------------------
3000000000000000000000000000000000000000000000000000
```

Exact own centroid:

```text
cx = 92557282910038200285130860484681571326828880978680968076486474486821
     -------------------------------------------------------------------------
     226465722938691509433511278989106920133387733148792440000000000000000

cy = -450411283192247756835748726576119544123864445599835972749701955519197
      -------------------------------------------------------------------------
      566164307346728773583778197472767300333469332871981100000000000000000

cz = -447336447640754750983307294864285010406855211424213032369270415872883
      --------------------------------------------------------------------------
      2264657229386915094335112789891069201333877331487924400000000000000000
```

Numerically, `c=(0.4087032761911399,-0.7955487079414353,-0.19752942822250283)`.

The exhaustive exact audit gives:

```text
stable:
  base 17-gon              0.14301877436721136
  [4,42,43]                0.004616197762473264
  [10,43,11]               0.015077545808680894
  [14,13,49]               0.014539739281903032

unstable:
  8                         0.9145705570369166
  46                        0.005153353305009138
  47                        0.009671466431590206

saddles:
  (4,42)                    0.008103119887220182
  (4,43)                    0.011495741206234644
  (13,49)                   0.01569376641410315
  (14,49)                   0.01590428894647683
  (46,47)                   0.005153353305009138
```

Every other maximal face, actual vertex and true edge/full normal cone is strictly excluded. The closest excluded face, vertex and edge margins are respectively `-0.00550506256`, `-0.1174875433`, and `-0.1034477810`; this is an open nonwinner, not tolerance dust.

# Hard moment elimination

The exact verifier triangulates the outward maximal faces and forms

```text
V = Σ det(a,b,c)/6
M = Σ det(a,b,c)(a+b+c)/24
c = M/V.
```

Only after this exact own-centroid computation are the face-foot, vertex and edge-normal-cone predicates evaluated on `p_i-c`. In common integer scale, centred points are `X_i=4Tq_i-S`, so all three ordinary moments are dependent exact equations rather than score penalties.

# Transverse incidence

The actual new-new bridge edges are

```text
42-43 42-44 42-45 42-47
44-45 44-46
45-46 45-47
46-47 46-49
47-49
48-49
```

The same connected post-wall hull meets all four sectors:

```text
stable circuit {8,9,33,40}:  8-43,9-43,33-42,33-47,33-49
right saddle sector:         4-42,4-43,4-44
34/35 relay sector:          33-42,33-47,33-49; rows34,35,36 inactive
left saddle sector:          14-49 plus 33-42,33-47,33-49; rows30,31 inactive
```

This is genuine volumetric communicating incidence. I did not isolate an exact one-parameter homotopy in which all four original circuit determinants vanish at one common parameter, so I do not claim a certified single simultaneous bifurcation event.

# Exact first nonlocal obstruction

The true edge `(46,47)` is an external-positive two-vertex component. At the exact own centroid every support from either endpoint to a neighbor outside `{46,47}` is positive:

```text
46->32  1.4472822810706603
46->44  0.9214959840157898
46->45  0.6381890095805376
46->49  1.1633810323811198

47->33  1.1156569057278718
47->42  0.8181799731682832
47->45  0.6351337843423919
47->49  1.1650492001855381
```

Let `d=q47-q46`, with `X_i` the exact common-scale centred integer vectors. Then

```text
A = -X46·d > 0
B =  X47·d > 0
A+B = K|d|^2 > 0.
```

The exact positive integers are recorded in the terminal certificate. The identity is structural: while edge `(46,47)` and the listed external-positive signs persist, at least one endpoint has all positive directed supports and is unstable. Row `8` is independently unstable, so the entire sign cell has `U>=2`.

Therefore merely reversing the mutual 46/47 sign transfers the extra maximum. Escape requires an external-support wall, deletion of `(46,47)`, or deactivation of one or both endpoints.

A second quantitative obstruction follows from a radial witness chain. For total angular turn `Θ` over `m` directed ascent edges, a necessary condition is

```text
(r_target/r_start) cos(Θ/m)^m > 1.
```

From row `46` or `47` to target row `8`, the angle is about `174.3°`; `m=18` fails and the first feasible value is `m=19`. This explains why the eight-row endpoint improves only by collapsing the terminal pair toward a wall.

All `2^8=256` fixed-coordinate bridge-row deletion subhulls were rebuilt and audited; none has `(1,1,0)`.

# Perturbation and mesh certificate

A directed interval verifier certifies the independent box

```text
|δp_ij| <= 10^-7 for every coordinate of rows 42..49,
rows 0..41 fixed.
```

Throughout the box the actual face lattice remains `(29,67,40)` and the recomputed-own-centroid class remains `(4,3,5)`. The worst nonincident support upper bound is `-3.7315246926696224e-5`.

The OBJ and STL both weld to 29 vertices and 54 triangles, are watertight and consistently oriented, and reproduce volume `1.887214357822429` and the certified centre of mass.

# Most useful continuation

The next nonredundant operation is a finite-width, genuinely three-dimensional branched/annular replacement of the complete relay `{46,47}` and both remote stable-saddle stars in one rebuilt cell. It should:

```text
- delete edge (46,47) or deactivate its endpoints;
- provide roughly 19 effective ascent links unless a distributed volume lobe
  shifts the own centroid enough to lower the radial bound;
- span the right star around 4-42-43 and left star around 13-14-49;
- permit obsolete seed and bridge rows to become non-extreme together;
- eliminate three selected coordinates from Mx=My=Mz=0 before scoring;
- rebuild all maximal faces, actual vertices, true edges and all four edge-cone
  components after every circuit crossing.
```

The decisive next test is whether distributed positive/negative volume can shift the centroid enough while its projection remains strictly inside the target 17-gon. Failure of that base-footprint test before the relay supports reverse would strengthen the present fixed-cell obstruction into a broader obstruction for this M42 architecture.

# Artifacts

- Complete exact bundle (`m42_transverse_bundle.zip`)
- Full research handoff with every coordinate, maximal face and true edge (`m42_research_handoff.md`)
- Exact endpoint certificate (`m42_transverse_certificate.json`)
- Exact seed certificate (`m42_seed_certificate.json`)
- Independent exact verifier (`m42_transverse_verifier.py`)
- Directed interval box verifier (`m42_transverse_box_verifier.py`)
- Verification transcript (`verification_transcript.txt`)
- Exact terminal-component certificate (`m42_terminal_pair_certificate.txt`)
- Obstruction/radial-bound report (`m42_obstruction_report.json`)
- Exhaustive 256-subset scan (`bridge_subset_scan.json`)
- OBJ (`m42_transverse.obj`)
- STL (`m42_transverse.stl`)
- Collapsed score-extremal checkpoint (`cma03.npz`)

Bundle SHA-256:

```text
0657c52668abe68fc816209909918ac34a13c60c2c0e6611a06dbe8b3131dd8a
```

# Unresolved uncertainty

No strict `(1,1,0)` body and no exact simultaneous four-circuit homotopy were found. The terminal-component theorem excludes only the current incidence/external-sign cell; it does not exclude a larger nonlocal transverse surgery.
