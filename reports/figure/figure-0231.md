# figure-0231

AI research report · 2026-09-02 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Calm Quartz 90 — exact wall-242 fourth-support/full-star determination

The durable acceptance gate requires a finite uniform-density body at its own exact ordinary-volume centroid, strict `(S,U,H)=(1,1,0)`, a complete finite H/V/edge audit, an independent exact or directed verifier, and matching OBJ/STL; wall points, auxiliary-centre mechanics, and near-solutions do not qualify.

The supplied frontier says the third-support event genuinely deleted its predecessor packet but left a new forcing component on `[1975,2732]`, together with stable limiting edge `[2152,3290]` and the new saddle routes. It specifically calls for a fourth support in the same multi-cell event and for external-arrow anti-carrier constraints before moment closure.

## Literal disposition

**EXACT DELIMITED NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained in this topology.

The prescribed fourth support was nevertheless realized as a literal exact finite full-hull event. New extreme support `I=40009` participates in one dual-connected, same-boundary, positive-volume full-star replacement. The exact target has

```text
19 supplied dyadic points,
18 active vertices,
(V,E,F,C)=(18,48,32,96),
(S,U,H)=(2,2,2).
```

It preserves intended stable face `[0,1371,C]` and intended unstable vertex `C`. Every equilibrium feature named in the predecessor packet is deleted or loses its equilibrium status, but a new Euler-neutral packet appears:

```text
extra stable    [1258,2152,3296]
extra unstable  2369
saddles         [1975,I], [3290,C].
```

This is an open exact nonwinner, not a wall point or numerical near-solution. It does not supersede the global M42 `(2,1,1)` benchmark.

## What was tried and what changed

I reconstructed the exact third-support source, enumerated 20 combinatorial fourth-support continuations, realized five strict convex full hulls, and used 2,048,000 determinant-one metric samples only for discovery. No numerical winner appeared; those samples are not part of the exclusion theorem.

The selected topology has one connected eight-edge `I` star. It was exactified at denominator `2^24`, its actual convex hull and own volume centroid were independently reconstructed, every face, vertex, and true-edge cone was audited, all target-patch external-arrow patterns were classified, and an exact same-boundary patch certificate was built. The promoted conclusion relies only on the exact dyadic endpoint and its directed interval box.

## Exact dyadic generator

All supplied coordinates have denominator `2^24=16777216`; `A=40001`, `B=40002`, `C=40003`, `D=40004`, `E=40005`, `F=40006`, `G=40007`, `H=40008`, `I=40009`.

```text
0     (     2382238,     -6308946,     46171779) / 16777216
1258  (     1620887,      4967418,    -20558338) / 16777216
1371  (    10559225,     10966823,     61698050) / 16777216
1975  (    10274573,     12571703,     48854565) / 16777216
2152  (      510389,     -7271935,     -5924598) / 16777216
2369  (    13553807,      7635734,     61913618) / 16777216
2515  (     5028442,     -9339607,     26833667) / 16777216
2732  (     9156226,      4616735,     61197940) / 16777216
3290  (      661958,    -10721838,     16427750) / 16777216
3296  (     3876214,     -1521484,      3638813) / 16777216
A     (     -351024,     -8978438,     25844631) / 16777216
B     (           0,            0,            0) / 16777216  inactive
C     (   -19656014,    -12570508,    -84150451) / 16777216
D     (    -2672244,      3411514,    -42213909) / 16777216
E     (    -6361824,      2058745,    -51264980) / 16777216
F     (    -4952003,      7634514,    -41535864) / 16777216
G     (     6883860,      6757049,     11795903) / 16777216
H     (    -1678613,     11935619,    -25478204) / 16777216
I     (     2490487,     15844729,     -4710098) / 16777216
```

`B=(0,0,0)` is strictly interior. Its exact minimum oriented support slack is

```text
153156717762127176455/1180591620717411303424 > 0.
```

Every other supplied point is active. The integer table in `data/generator_exact.json` is authoritative.

## Exact ordinary volume and own centroid

The uncentred volume is

```text
66863670489079043048831/28334198897217871282176
≈ 2.359822161608542.
```

The exact ordinary-volume centroid is

```text
cx = 13351765998894380385063/1121786242348104746303536234496
cy = -12368866643540236632853/2243572484696209492607072468992
cz = 410151026352539373635977/4487144969392418985214144937984
```

approximately

```text
(1.1902237248824411e-08,
 -5.5130229702451712e-09,
 9.1405789015119744e-08).
```

Subtracting this one rational vector from every active vertex gives exact first moments

```text
Mx=My=Mz=0.
```

No auxiliary mechanical centre is used. The exact tetrahedral contributions are materialized in `data/positive_tetrahedralization.csv`.

## Complete actual maximal faces

The 32 outward irredundant maximal triangular cycles are:

```text
[0,2732,1371]
[0,1371,C]                 stable
[0,2515,2369]
[0,2369,2732]
[0,3290,2515]
[0,A,3290]
[0,C,A]
[1258,3296,2152]           stable
[1258,2152,D]
[1258,G,3296]
[1258,D,I]
[1258,I,G]
[1371,2369,1975]
[1371,1975,I]
[1371,2732,2369]
[1371,I,C]
[1975,2369,I]
[2152,3296,2515]
[2152,2515,C]
[2152,C,D]
[2369,2515,G]
[2369,G,I]
[2515,3290,C]
[2515,3296,G]
[3290,A,C]
[C,E,D]
[C,F,E]
[C,H,F]
[C,I,H]
[D,E,F]
[D,F,H]
[D,H,I]
```

Every active vertex lies on its listed supports and every nonincident supplied point lies strictly behind every support. The minimum Euclidean nonincidence separation is

```text
2.424658958923686e-4.
```

## Complete true-edge incidence

The 48 physical true edges are:

```text
[0,1371] [0,2369] [0,2515] [0,2732] [0,3290] [0,A]
[0,C] [1258,2152] [1258,3296] [1258,D] [1258,G] [1258,I]
[1371,1975] [1371,2369] [1371,2732] [1371,C] [1371,I]
[1975,2369] [1975,I] H
[2152,2515] [2152,3296] [2152,C] [2152,D]
[2369,2515] [2369,2732] [2369,G] [2369,I]
[2515,3290] [2515,3296] [2515,C] [2515,G]
[3290,A] [3290,C] H [3296,G] [A,C]
[C,D] [C,E] [C,F] [C,H] [C,I]
[D,E] [D,F] [D,H] [D,I] [E,F] [F,H] [G,I] [H,I]
```

Every edge has exactly two incident maximal faces and

```text
18-48+32=2.
```

No display-mesh diagonal is counted as a physical edge.

## Exhaustive mechanics at the exact own centroid

Exactly two maximal faces are stable:

```text
[0,1371,C]
  barycentrics ≈ (0.020872145945522197,
                  0.5606863080781870,
                  0.4184415459762908)

[1258,3296,2152]
  barycentrics ≈ (0.14588889646466843,
                  0.7829074043570452,
                  0.07120369917828637).
```

The global positive stable-coordinate minimum is

```text
57263300436523330534085101483689151049347420843431/
2743527214977543223119398588631692961916667347871344
≈ 0.020872145945522197.
```

Every other maximal face has an exact negative Cramer witness. The closest excluded face coordinate is

```text
-6283121672004573703588711627919599236388094554364463/
399550126606276237875205291345818763789336371745169416
≈ -0.015725490379323727.
```

Exactly two vertices are unstable:

```text
2369  minimum raw outgoing support ≈ 0.10124974816857943
C     minimum raw outgoing support ≈ 11.413217728627876.
```

Every other active vertex has an exact nonpositive outgoing witness. The closest excluded raw support is

```text
-1121855468237409469485150722674251969/
37640900187405001038719257939932086272
≈ -0.029804161501238297.
```

Exactly two true edges are saddles. Their normalized four-component full-cone tuples are

```text
[1975,I]
(0.9031555553748887,
 0.09684444462511138,
 2.4382114969700344,
 0.7287862296091725)

[3290,C]
(0.15627314320851543,
 0.8437268567914845,
 0.2364899912080947,
 0.4463259754892148).
```

The global positive saddle-component minimum is

```text
76162786561549829130207252053049809683/
786444559173001035968012480728101222684
≈ 0.09684444462511138.
```

Every other true edge has an exact negative full-cone component. The closest excluded normalized component is

```text
-225058135876627516630426217106157208453179794342875758592/
5428734967450146358248141060930580134932762179853366993925
≈ -0.04145682875035182.
```

Thus the complete strict class is exactly

```text
(S,U,H)=(2,2,2),
S+U-H=2.
```

## Genuine connected fourth-support/full-star event

The predecessor and target hulls were reconstructed independently. Their changed-face sets become dual-connected, one-boundary-component disks after adjoining the minimal five common bridge faces

```text
[1371,1975,2369]
[0,1371,C]
[0,3290,A]
[3290,A,C]
[0,A,C].
```

Their common boundary cycle is

```text
0–1371–2732–2369–G–1258–D–H–C–2152–2515–0.
```

The predecessor-side patch has `(V,E,F)=(14,28,15)` and the target-side patch has `(15,31,17)`. Both have Euler characteristic one, one boundary component, and connected dual graph. Coning every patch triangle to that side's exact own centroid gives a positive-volume 3-ball.

The smallest exact cone volumes are

```text
source
19591177258194791920200869896791397/
116587292086631919656971678718165390458880
≈ 1.6803870222525861e-7

target
13654160107885426725342737964369972897030445/
631509512878534181906817353817955636715978752
≈ 0.021621463856731634.
```

The exact true-edge symmetric difference is

```text
removed:
[0,2152]
[1975,2732]
[2152,3290]
[2369,C]
[C,G]
[D,G]
[G,H]

inserted:
[1258,I]
[1371,I]
[1975,I]
[2369,I]
[2515,3290]
[2515,C]
[C,I]
[D,I]
[G,I]
[H,I].
```

Consequently:

- forced edge `[1975,2732]` is absent;
- the already-existing opposite edge `[1371,2369]` persists with a rebuilt incident star rather than being inserted by an ordinary flip;
- stable face `[2152,3290,C]` is absent;
- vertex `2732` remains active but is no longer unstable;
- saddle `[G,H]` is absent;
- edge `[0,C]` remains physical but its full normal cone is nonsaddle;
- `I` has a connected eight-edge star through `1258,1371,1975,2369,C,D,G,H`.

The bridge enumerator tested exactly 11,353 common-face subsets in increasing cardinality. No valid bridge with fewer than five added common faces exists for these exact changed-face sets. This is not a classification of every possible fourth-support topology.

The theorem-level event is the pair of exact full hulls and their connected same-boundary positive-volume replacement. No scalar one-parameter simultaneous wall chronology is claimed.

## External-arrow design certificate

Every edge inserted by the event has an exact strictly negative external directed support:

```text
inserted edge  witness arrow       exact support
[1258,I]       1258→D
 -115143272825494916238780229057980702651/
 75281800374810002077438515879864172544

[1371,I]       I→H
 -3409775584156411037097896422871688227/
 37640900187405001038719257939932086272

[1975,I]       1975→1371
 -163203910864041074619988046437070019415/
 75281800374810002077438515879864172544

[2369,I]       I→H
 -3409775584156411037097896422871688227/
 37640900187405001038719257939932086272

[2515,3290]    2515→2369
 -220823947293769621429523899673378820479/
 75281800374810002077438515879864172544

[2515,C]       2515→2369
 -220823947293769621429523899673378820479/
 75281800374810002077438515879864172544

[C,I]          I→H
 -3409775584156411037097896422871688227/
 37640900187405001038719257939932086272

[D,I]          D→C
 -235516222676509217013114856075880729521/
 37640900187405001038719257939932086272

[G,I]          G→2369
 -171982968959743231309989556434918039531/
 75281800374810002077438515879864172544

[H,I]          H→C
 -329649897136344655103743785239008229221/
 75281800374810002077438515879864172544.
```

The exhaustive target-patch ledger covers all 20 internal patch edges. Exactly one has all external arrows positive:

```text
[1371,2369].
```

It is inherited from the common bridge. Thus no geometrically inserted edge becomes the forcing carrier. The precise design lesson is stronger: the anti-carrier test must cover every internal edge whose incident star changes, not only newly inserted edges. The altered inherited edge `[1371,2369]` acquires the unique all-positive carrier role.

## Exact residual forcing component

True edge `[1371,2369]` is incident to

```text
[1371,2369,1975]
[1371,2732,2369].
```

Every external endpoint support is positive. The exact minimum is

```text
15420191234177049990672282802849792193/
37640900187405001038719257939932086272
≈ 0.40966584639059167.
```

The mutual supports are

```text
sigma(1371→2369)
= -1121855468237409469485150722674251969/
  37640900187405001038719257939932086272

sigma(2369→1371)
= 3811131664813390534983922711491589047/
  37640900187405001038719257939932086272.
```

They satisfy the exact energy identity

```text
sigma(1371→2369)+sigma(2369→1371)
= ||p_2369-p_1371||²
= 20110144843269/281474976710656
> 0.
```

If neither endpoint were unstable while every external arrow remained positive, both mutual arrows would have to be nonpositive, contradicting this identity. Therefore one endpoint is unstable in addition to independently strict unstable vertex `C`. Hence

```text
U>=2
```

throughout the certified chamber.

## Positive own-centroid perturbation box

Independent perturbations of all 57 supplied uncentred coordinates by

```text
|delta r_ij| <= 2^-34
              = 1/17179869184
              ≈ 5.820766091346741e-11
```

preserve, after exact outward interval recomputation of physical volume, all three first moments, the dependent common centroid, hull incidence, and mechanics:

```text
19 supplied rows;
B strictly inactive;
18 active vertices;
32 maximal faces;
48 true edges;
strict class (2,2,2);
all 96 directed vertex primitives;
all four components of all 48 true-edge cones;
all ten inserted-edge anti-carrier witnesses;
the [1371,2369] external-positive forcing chamber.
```

Selected box-wide lower clearances are

```text
topology oriented determinant  0.00073133519582574359
inactive B                     0.12972878105093055
face-sign determinant          0.027008342758124537
vertex-sign support            0.029804141488570392
edge determinant-scaled sign   0.00099787934630264337
forced external arrow          0.40966582628913967
inserted anti-carrier arrow     0.090586977000446392.
```

The 57 input coordinates remain independent while the physical centroid is recomputed as a dependent common translation. Thus the result is a genuine positive-radius shape chamber, not a single exact point.

## First genuinely unclassified successor

The target incidence exposes

```text
[1371,2369] -> [1975,2732]
legal forcing-edge escape

[1258,3296] -> [2152,G]
legal death sheet of extra stable [1258,2152,3296]

[3290,C] -> [2515,A]
legal saddle exchange

[1975,I] -> [1371,2369]
ordinary flip illegal because [1371,2369] already exists.
```

The smallest evidence-supported nonrepeating successor is therefore a fifth shared support `J`, or an equivalent changed-diagonal prism/double-octahedral cell with coordinated release or deactivation of at least one of `1371,1975,2369,I`. One connected event must delete the full `[1371,2369]` component, kill the extra stable face and both saddles, preserve the intended pair or explicitly supersede it, and enforce anti-carrier arrows on every inserted or star-changed internal edge before solving the three volume moments.

## Independent verification

The package contains five replay layers:

```text
scripts/verify_exact.py
  primary exact reconstruction

scripts/verify_interval_own_centroid.py
  complete 2^-34 directed interval proof

scripts/verify_independent.py
  standard-library-only clean-room reconstruction importing
  neither construction code nor exact_core.py

scripts/find_minimal_bridge_patch.py
  exact 11,353-subset bridge replay

scripts/verify_mesh.py
  OBJ/STL orientation, incidence, Euler, and watertightness audit.
```

The aggregate replay ends with


[Encoded source block omitted; the code in this passage is incomplete.]


A clean extraction independently checks all 39 manifested files and reruns the complete package verifier. The OBJ contains 18 vertices and 32 outward triangles; its 48 edge classes all have multiplicity two. The STL has the same 32 facets.

## Exact scope

Closed exactly:

- this materialized one-`I` fourth-support/full-star topology;
- its complete `2^-34` own-centroid mechanics chamber;
- every named predecessor-lineage deletion claim;
- all ten inserted-edge anti-carrier signs;
- all 20 target-patch internal-edge external-arrow classifications;
- the external-positive `[1371,2369]` forcing chamber;
- common-face bridge cardinalities below five for the stated changed-face sets.

Not closed:

- every possible placement of a fourth support;
- every alternate old-row release or multi-cell boundary;
- the fifth-support or changed-diagonal successor above;
- the global existence problem.

## Final statement

**NONWINNER, rigorously delimited.** Fourth support `I` genuinely deletes the preceding equilibrium packet in one connected positive-volume full-star replacement. Every newly inserted edge satisfies the requested external-arrow anti-carrier condition. The endpoint nevertheless remains exact open `(2,2,2)` because inherited internal edge `[1371,2369]` becomes the next forcing component. The first mathematically new continuation is a fifth-support or old-row-released changed-diagonal full-star event that also eliminates this inherited carrier.

## Delivered artifacts

- Complete exact NONWINNER archive (`Calm_Quartz_90_wall242_fourth_support_exact_NONWINNER.zip`) — SHA-256 `de7be1923236e57fe6f04b41521d0cd4dee5522998c54237cd871d2f3aab6200`, 627,242 bytes.
- Full Markdown handoff (`Calm_Quartz_90_wall242_fourth_support_handoff.md`)
- Structured result (`Calm_Quartz_90_wall242_fourth_support_result.json`)
- Clean-extraction verification receipt (`Calm_Quartz_90_wall242_fourth_support_clean_verification.json`)
- Clean replay transcript (`Calm_Quartz_90_wall242_fourth_support_clean_replay.txt`)
- Exact 19-row generator (`generator_exact.json`)
- Supplied exact V-data (`input_vertices_exact.csv`)
- Exact own-centred active V-data (`active_vertices_centered_exact.csv`)
- Primitive irredundant H-data (`fourth_support18_exact_H_irredundant.csv`)
- All maximal-face mechanics (`fourth_support18_exact_faces.csv`)
- All 96 directed vertex primitives (`fourth_support18_exact_vertex_primitives.csv`)
- All 48 true edges and full cones (`fourth_support18_exact_true_edges_full_cones.csv`)
- Full external-arrow ledger (`external_arrow_full_ledger.csv`)
- Same-boundary full-star certificate (`fourth_support_shared_terminal_patch.json`)
- External-arrow design certificate (`external_arrow_design_certificate.json`)
- Minimal bridge certificate (`minimal_same_boundary_bridge.json`)
- Own-centroid perturbation certificate (`own_centroid_perturbation_certificate.json`)
- Residual forcing-edge certificate (`residual_forced_edge_1371_2369.json`)
- Next-topology certificate (`first_successor_topology.json`)
- Independent clean-room verifier (`verify_independent.py`)
- Aggregate verifier (`RUN_ALL_VERIFIERS.sh`)
- Package verifier (`verify_package.py`)
- SHA-256 manifest (`SHA256SUMS.txt`) — 39 entries, SHA-256 `749aaeb48902e5a0f40cf7e5389fab55d5bd0630f7657bad98964294414293ac`.
- Watertight OBJ (`body.obj`)
- Watertight STL (`body.stl`)
