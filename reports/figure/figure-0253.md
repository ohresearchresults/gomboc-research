# figure-0253

Historical AI scientific report · saved 2026-09-03 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

The durable journal fixes the acceptance gate at a finite uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid, with strict `(S,U,H)=(1,1,0)`, complete H/V/true-edge mechanics, independent verification, and matching OBJ/STL; auxiliary-centre, wall, near-solution, and unexpanded theorem objects do not qualify. :contentReference[oaicite:0]{index=0}

The accepted source is the exact eighth three-support cage: 26 supplied dyadic points, 11 active vertices, `(V,E,F,C)=(11,27,18,54)`, strict own-centred `(2,2,2)`, with packet stable `[N,O,P]`, unstable `0`, saddles `[H,O]`,`[L,P]`, and unique nonprotected forcing edge `[0,N]`. The journal identifies a closed four-support/equivalent linked cell changing that whole star as the first nonserial successor. :contentReference[oaicite:1]{index=1}

# Calm Quartz 90 — exact ninth four-support carrier cage

## Disposition

**EXACT DELIMITED NONWINNER.** No strict own-centred `(1,1,0)` polyhedron was obtained.

A literal closed four-support cage was realized. New extreme supports `Q=40017`, `R=40018`, `S=40019`, `T=40020` form one communicating full-star volume; old rows `N,O,P` and every other nonprotected source row become strictly inactive. The target is

```text
30 supplied dyadic points
8 active vertices; 22 strictly inactive rows
(V,E,F,C)=(8,18,12,36)
(S,U,H)=(2,2,2)
independent physical-coordinate radius 2^-17
```

The complete eighth-cage packet is genuinely removed: edge `[0,N]`, stable `[N,O,P]`, saddles `[H,O]`,`[L,P]`, and the extra instability of `0` do not survive. Protected stable `[0,H,C]` and protected unstable `C` remain strict. The replacement packet is stable `[L,S,R]`, unstable `R`, saddles `[C,L]`,`[R,T]`, and unique nonprotected adverse edge `[0,R]`.

## Exact finite generator

All coordinates are integer triples divided by `2^24=16777216`.

```text
active
0     (  2382238, -6308946,  46171779)
C     (-19656014,-12570508, -84150451)
H     ( -1678613, 11935619, -25478204)
L     ( -3451066,-25547268,   2954098)
Q     (  4517835,  9610913, -70938052)
R     ( 12012053, 12919901,  49488350)
S     (  1411285,  -850817, -71554700)
T     (  2708267, 19388382, -40745046)

inactive
1258  (      772,     4592,    -10180)
1371  (       52,       54,       301)
1975  (      223,      -94,        63)
2152  (      249,    -3551,     -2893)
2369  (       66,       37,       302)
2515  (     2455,    -4560,     13102)
2732  (       45,       23,       299)
3290  (      323,    -5235,      8021)
3296  (     1893,     -743,      1777)
A     (     -171,    -4384,     12619)
B     (        0,        0,         0)
D     (    -1305,     1666,    -20612)
E     (    -3106,     1005,    -25032)
F     (    -2418,     3728,    -20281)
G     (       21,     -123,       132)
I     (       18,      116,       -34)
J     (       -4,      -57,        48)
K     (      100,       88,       404)
M     (      935,      981,      1456)
N     (     6085,      891,     20745)
O     (     6075,     6861,     12802)
P     (    -3764,    -8166,    -27702)
```

The exact minimum inactive oriented slack is

```text
251385923098236986603/295147905179352825856 > 0,
```

attained by `F` against face `[0,R,H]`. Minimum Euclidean inactive separation is `0.12488764503184085`.

## Exact volume and own centroid

```text
Vol = 40077758475635013290147/7083549724304467820544

c = (
-497292074325015391946906537579/5379145685932474841053335126016,
-475186011221744702005190433279/5379145685932474841053335126016,
-8144710585065559415963036112611/5379145685932474841053335126016
)
≈(-0.09244815131620847,-0.08833856507445963,-1.5141271608176705).
```

The exact boundary tetrahedralization has twelve positive cells. Translating all active vertices by `-c` gives exact ordinary first moments `Mx=My=Mz=0`; no auxiliary mechanical point is used.

## Actual irredundant H/V/E incidence

Maximal faces:

```text
[0,H,C] stable
[0,C,L]
[0,R,H]
[0,L,R]
[C,H,T]
[C,S,L]
[C,Q,S]
[C,T,Q]
[H,R,T]
[L,S,R] stable
[Q,R,S]
[Q,T,R]
```

Physical true edges:

```text
[0,C] [0,H] [0,L] [0,R]
[C,H] [C,L]* [C,Q] [C,S] [C,T]
[H,R] [H,T] [L,R] [L,S]
[Q,R] [Q,S] [Q,T] [R,S] [R,T]*
```

Asterisks mark saddles. Every edge has exactly two incident maximal faces and `8-18+12=2`. Minimum active nonincidence distance is `0.02898552911039006`. Primitive H rows, exact own-centred V rows, maximal-face mechanics, and true-edge incidences are fully materialized.

## Exhaustive equilibrium mechanics

Exactly two faces are stable. Their exact minimum foot barycentrics are

```text
[0,H,C]:
93310859675740770974691038725326499275530447918734103/
371638328074130080174460231037629419235646119455320872
≈0.25107975315486891

[L,S,R]:
1032963909111895766253808110207017168949179221133897/
4640075909068877700566716992857090229000353243970279
≈0.22261789017136580.
```

Every other face has an exact negative Cramer witness; the closest excluded face `[C,S,L]` has decision about `-0.2963828421157214`.

Exactly two vertices are unstable:

```text
C minimum raw outgoing support
401209325832827141527333840061619226269/
90247089068357291822917470929557651456
≈4.445676087446242

R minimum raw outgoing support
210304109722283917912920640505903751871/
90247089068357291822917470929557651456
≈2.330314605083716.
```

Every other active vertex has an exact negative outgoing witness; the closest is `H`, about `-0.35736663512301586`.

Exactly two true edges are saddles. Their normalized four-component tuples `(t,1-t,beta1,beta2)` are

```text
[C,L] (0.6568411119961819,0.34315888800381816,
       0.9888911990822645,1.076221543089925)
[R,T] (0.8210799885370499,0.1789200114629501,
       0.8580175073249580,0.9852035891326747).
```

Every other true edge has an exact negative full-cone component; the closest excluded decision is `-0.16696287041437521` on `[C,Q]`. The exhaustive ledgers contain all 12 face decisions, all 36 directed vertex primitives, and all 72 components of the 18 physical true-edge cones. Hence the exact class is `(2,2,2)`.

## Connected positive-volume four-support surgery

The exact eighth-cage source is augmented only by strict-interior seeds

```text
Q=(1,-2,3)/2^24,
R=(2,1,-1)/2^24,
S=(-2,3,1)/2^24,
T=(3,2,-2)/2^24.
```

Source and target hulls are independently reconstructed. Their common exterior faces are `[0,H,C]` and `[0,C,L]`. Removing those faces leaves dual-connected one-boundary disks with the same quadrilateral boundary `0-H-C-L-0`:

```text
source patch (V,E,F)=(11,26,16), chi=1
target patch (V,E,F)=(8,17,10), chi=1.
```

No bridge face is required. Coning every patch triangle to that side’s own exact centroid gives positive-volume 3-balls. Minimum exact cone volumes are approximately `0.025227086388690666` and `0.23423394664251418`.

Removed true edges:

```text
[0,N] [0,O] [1258,D] [1258,F] [1258,H] [1258,O]
[C,E] [C,F] [C,P] [D,E] [D,F] [D,O] [D,P]
[E,F] [E,P] [F,H] [H,O] [L,N] [L,P]
[N,O] [N,P] [O,P]
```

Inserted true edges:

```text
[0,R] [C,Q] [C,S] [C,T] [H,R] [H,T]
[L,R] [L,S] [Q,R] [Q,S] [Q,T] [R,S] [R,T]
```

Inherited star-changed edges are `[0,H] [0,L] [C,H] [C,L]`. This proves actual finite-thickness full-hull surgery, not frozen-fan or display-diagonal bookkeeping.

## Complete changed-edge arrow census and residual theorem

All 18 target edges, all 13 inserted edges, and all four inherited star-changed edges were audited over every external directed support. The all-external-positive changed edges are `[0,R]`, `[C,Q]`, and `[C,S]`; the latter two lie in the protected unstable-`C` star. Thus `[0,R]` is the unique nonprotected adverse changed edge.

For `[0,R]`, every external endpoint arrow is positive, with exact minimum

```text
969359780328057014524082998583563285009/
90247089068357291822917470929557651456
≈10.741175037721376.
```

The mutual arrows are

```text
sigma(0→R)=-58495480235629565375866894694609702071/
            90247089068357291822917470929557651456
sigma(R→0)=210304109722283917912920640505903751871/
            90247089068357291822917470929557651456
```

and their exact sum is

```text
||R-0||²=473481537081675/281474976710656>0.
```

Therefore both endpoints cannot be nonunstable while all external arrows remain positive. One endpoint is unstable in addition to protected unstable `C`; at the target it is `R`.

## Exact birth/death chronology

The connector is the exact affine chord in all 30 uncentred supplied points; the ordinary centroid is recomputed in every active cell. Fourteen integer primitive/circuit polynomials have rational isolating intervals, Sturm count one, no derivative root inside, and exact before/after mechanics ledgers:

```text
0.020699250577694  [C,L] saddle birth
0.049558696669525  [L,P] saddle death
0.268464079262181  stable [N,O,P]→[N,P,Q]
0.295077004672661  stable [N,P,Q]→[L,N,Q]
0.364490603894661  carrier [0,R] topological birth
0.490357538484552  bridge saddle [H,R] birth
0.492823925892748  source saddle [H,O] death
0.554380761111661  target saddle [R,T] birth
0.583190529298511  bridge saddle [H,R] death
0.587268742966058  source carrier [0,N] death
0.619519313564867  stable [L,N,Q]→[L,Q,R], N deactivates
0.768484070027465  stable [L,Q,R]→[L,S,R]
0.830800089496609  unstable R birth
0.945800822014169  unstable 0 death.
```

Thus replacement saddle `[C,L]` is born before `[L,P]` dies; `[0,R]` exists before `[0,N]` dies; the H/R/T saddle relay is born before each source death; and unstable `R` is born before unstable `0` dies. The stable component transfers continuously through five strict faces. No `(1,1,0)` interval occurs on this exact connector.

## Positive independent-coordinate chamber

Every one of the 90 uncentred supplied coordinates may vary independently by

```text
|delta r_ij|≤2^-17=1/131072.
```

Directed interval arithmetic recomputes physical volume, all moments, the dependent common centroid, all inactivity gaps, complete incidence, every face and vertex sign, all 72 true-edge cone components, every changed-edge witness, and the `[0,R]` forcing identity. The exact volume interval is

```text
[40075396397714668894627/7083549724304467820544,
 40080120559905701500835/7083549724304467820544].
```

Box-wide raw lower clearances are approximately

```text
topology/nonincidence  0.43154606429628695
face decisions         1.0499892828735249
vertex decisions       0.3570955517198198
edge-cone decisions    0.6463551736319452
forcing external       10.738901037724391
anti-carrier witnesses 0.3570955517198198.
```

The whole box preserves `(8,18,12)` and strict `(2,2,2)`.

## Independent replay and scope

The package contains deterministic exact generation, a primary Fraction reconstruction, a standard-library-only clean-room hull/centroid/mechanics verifier, directed own-centroid interval verification, independent SymPy/Sturm reconstruction of all 14 chronology polynomials and 28 side ledgers, and exact-to-OBJ/STL incidence/orientation/watertightness checks. Clean replay ends with

```text
INDEPENDENT_CLEAN_ROOM_NINTH_CAGE_NONWINNER_PASS
WATERTIGHT_NINTH_CAGE_ENDPOINT_MESH_PASS
ALL_CALM_QUARTZ_90_WALL242_NINTH_CAGE_VERIFIERS_PASS
CALM_QUARTZ_90_WALL242_NINTH_CAGE_PACKAGE_PASS.
```

Closed exactly: this `Q/R/S/T` cage; its zero-bridge positive-volume transition; deletion of the full eighth-cage packet; all 17 inserted/star-changed arrow decisions; the 14 decisive chronology events; the full `2^-17` chamber; and the `[0,R]` forcing theorem.

Not closed: every four-support placement/release set, every five-support cage, or the global existence problem.

## First genuinely unrepresented successor

The endpoint exposes legal exchanges

```text
[0,R]→[H,L]
[R,S]→[L,Q]
[C,L]→[0,S]
[R,T]→[H,Q].
```

Serial use would repeat packet transfer. The first nonrepeating successor is a closed five-support carrier cage, or linked two-cell hexahedral/double-octahedral volume, containing the full `[0,R]` star, stable `[L,S,R]`, and both saddle stars in one communicating cell. Release of `0` or `R` is allowed. It must have no nonprotected all-positive edge, two-edge component, or positive directed cycle after dependent moment closure.

## Final statement

**NONWINNER, rigorously delimited.** The four-support cage genuinely destroys the entire eighth-cage packet and reaches the rigorous eight-active-vertex frontier, but inserted edge `[0,R]` is the unique nonprotected forcing carrier. Replacement saddles, carrier, and unstable vertex are all born before their source counterparts die on the exact connector.

## Artifacts

- [Complete exact archive](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER.zip)
- [Full handoff](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_handoff.md)
- [Structured result](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_result.json)
- [Clean verification receipt](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_clean_verification.json)
- [Clean aggregate replay](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_clean_replay.txt)
- [Exact generator](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/data/generator_exact.json)
- [Supplied V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/data/input_vertices_exact.csv)
- [Own-centred active V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/data/active_vertices_centered_exact.csv)
- [Irredundant H-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/data/ninth_cage8_exact_H_irredundant.csv)
- [Face ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/data/ninth_cage8_exact_faces.csv)
- [Directed vertex ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/data/ninth_cage8_exact_vertex_primitives.csv)
- [True-edge full-cone ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/data/ninth_cage8_exact_true_edges_full_cones.csv)
- [External-arrow ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/data/external_arrow_full_ledger.csv)
- [Transition certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/certificates/ninth_cage_shared_global_patch.json)
- [Chronology certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/certificates/source_to_target_death_before_birth_obstruction.json)
- [Arrow certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/certificates/external_arrow_design_certificate.json)
- [Forcing certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/certificates/residual_forced_edge_0_R.json)
- [Perturbation certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/certificates/own_centroid_perturbation_certificate.json)
- [Independent verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/scripts/verify_independent.py)
- [Aggregate verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/RUN_ALL_VERIFIERS.sh)
- [Watertight OBJ](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/mesh/body.obj)
- [Watertight STL](sandbox:/mnt/data/Calm_Quartz_90_wall242_ninth_four_support_cage_exact_NONWINNER/mesh/body.stl)

```text
archive SHA-256  347fc8d83e39a833bd56348636521e064fb7be658db1e7ea81b61658976b7739
archive bytes    2049886
manifest entries 51
manifest SHA-256 a84ac41c5ec0daac09ff430575abc2960f6cf12f969ee7d4222dcaede85bcfd8
clean replay SHA-256 06609a273ad80ef48933c0ee82f43cdcaff72e6dc08c08201ba73d93301bb32d
clean extraction PASS
```
