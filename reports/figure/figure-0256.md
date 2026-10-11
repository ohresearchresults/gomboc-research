# figure-0256

Historical AI scientific report · saved 2026-09-03 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

The durable journal’s acceptance gate requires a finite uniform-density body evaluated at its own exact ordinary-volume centroid, strict `(S,U,H)=(1,1,0)`, complete H/V/true-edge mechanics, independent verification, and matching OBJ/STL; auxiliary-centre, wall, near-solution, and unexpanded theorem objects do not qualify. :contentReference[oaicite:0]{index=0}

The accepted source is the exact ninth four-support cage: 30 supplied dyadic points, 8 active vertices, `(V,E,F)=(8,18,12)`, strict own-centred `(2,2,2)`, with packet stable `[L,S,R]`, unstable `R`, saddles `[C,L]`,`[R,T]`, and unique nonprotected forcing edge `[0,R]`. The journal identifies a closed five-support/equivalent linked cell changing that entire star as the first nonserial successor. :contentReference[oaicite:1]{index=1}

# Calm Quartz 90 — exact wall-242 tenth five-support carrier cage

## Disposition

**EXACT DELIMITED NONWINNER.** No strict own-centred `(1,1,0)` polyhedron occurs in the exact open chamber constructed here.

A literal closed five-support cage was realized. New supports `U=40021`, `V=40022`, `W=40023`, `X=40024`, `Y=40025` become extreme; old packet rows `L,Q,R,S,T` become strictly interior. The target is an explicit uniform-density rational polyhedron with

```text
35 supplied dyadic points
8 active vertices; 27 strictly inactive rows
(V,E,F,C)=(8,18,12,36)
(S,U,H)=(2,2,2)
independent physical-coordinate radius 2^-18.
```

The ninth-cage packet is genuinely removed: `[0,R]`, `[L,S,R]`, unstable `R`, and saddles `[C,L]`,`[R,T]` are absent. Protected stable `[0,H,C]` and protected unstable `C` remain strict. The replacement packet is

```text
extra stable    [V,W,Y]
extra unstable  V
saddles         [0,Y], [V,X]
forcing edge    [0,V].
```

## Exact finite generator

All coordinates are integer triples divided by `2^24=16777216`.

```text
ACTIVE
0     (  2382238, -6308946,  46171779)
C     (-19656014,-12570508, -84150451)
H     ( -1678613, 11935619, -25478204)
U     (  1685191, 13276133, -46374948)
V     ( 26879404, 19386271,  78110174)
W     (  7850649,  8482803, -17883331)
X     (  5859178, 13722868, -45025776)
Y     (-13940954,-19057608, -61197427)

STRICTLY INACTIVE
1258  (       1,        5,      -10)
1371  (       0,        0,        0)
1975  (       0,        0,        0)
2152  (       0,       -4,       -3)
2369  (       0,        0,        0)
2515  (       2,       -5,       13)
2732  (       0,        0,        0)
3290  (       0,       -5,        8)
3296  (       2,       -1,        2)
A     (       0,       -4,       13)
B     (       0,        0,        0)
D     (      -1,        2,      -21)
E     (      -3,        1,      -25)
F     (      -2,        4,      -20)
G     (       0,        0,        0)
I     (       0,        0,        0)
J     (       0,        0,        0)
K     (       0,        0,        0)
L     (   -3451,   -25547,     2954)
M     (       1,        1,        1)
N     (       6,        1,       21)
O     (       6,        7,       13)
P     (      -4,       -8,      -28)
Q     (    4518,     9611,   -70938)
R     (   12012,    12920,    49488)
S     (    1411,     -851,   -71555)
T     (    2708,    19388,   -40745)
```

The exact minimum inactive oriented slack is

```text
2837069215635145548039/2361183241434822606848>0
```

(`≈1.2015455496419418`), attained by row `S` against face `[V,W,X]`.

## Exact ordinary volume and centroid

```text
Vol=27255408762082521813787/7083549724304467820544
   ≈3.8477048687279067

c=(
120627955237556819149704640653/1829079519879004313178465107968,
15210364627095431066434324625/114317469992437769573654069248,
-5343885881081102728270507232313/7316318079516017252713860431872
)
≈(0.06595008796858461,0.13305371985665546,-0.7304064452914828).
```

The boundary tetrahedralization has twelve positive cells. Subtracting this single rational centroid from all active vertices gives exact first moments

```text
Mx=My=Mz=0.
```

No auxiliary mechanical point, point-mass centroid, or Santaló surrogate is used.

## Actual irredundant incidence

Maximal faces:

```text
[0,H,C] stable
[0,C,Y]
[0,V,H]
[0,Y,V]
[C,H,U]
[C,U,X]
[C,X,Y]
[H,V,U]
[U,V,X]
[V,W,X]
[V,Y,W] stable
[W,Y,X]
```

Physical true edges:

```text
[0,C] [0,H] [0,V] [0,Y] saddle
[C,H] [C,U] [C,X] [C,Y]
[H,U] [H,V] [U,V] [U,X]
[V,W] [V,X] saddle [V,Y]
[W,X] [W,Y] [X,Y]
```

Every edge has exactly two incident maximal faces and `8-18+12=2`. Every nonincident supplied row lies strictly behind every support plane. The minimum Euclidean active nonincidence distance is `0.047518830531352287`. No display diagonal is counted as a physical edge.

## Exhaustive own-centroid mechanics

Exactly two faces are stable:

```text
[0,H,C]
  barycentrics ≈(0.29190044659479547,
                  0.5867688267006129,
                  0.12133072670459157)
  exact minimum=
  245318646229370714685311492651895991791741282185363983/
  2021900411316723897703506097513800290816920099168652096

[V,Y,W]
  barycentrics ≈(0.2242530016975632,
                  0.37563872643272006,
                  0.4001082718697167)
  exact minimum=
  313138390712877854630012303861219077973131973628848101/
  1396362092558248613351108897658059603838936852776926280.
```

Every other face has an exact negative Cramer witness. The closest excluded face is `[0,V,H]`, decision

```text
-124570264399877677131058797998350161283908784634715041/
1282221813608225853796584162144158745791797867688263776
≈-0.0971518836115662.
```

Exactly two vertices are unstable:

```text
C: minimum raw outgoing support
45594710699361527657494162476866697981/
7671715546546587306781688916210614272
≈5.943222271827574; normalized minimum≈0.8940844933854609

V: minimum raw outgoing support
1726131922129723097837798474786200463835/
122747448744745396908507022659369828352
≈14.062466794884124; normalized minimum≈0.8677533529749822.
```

Every other vertex has an exact negative outgoing witness. The closest excluded raw decision is `W` at `-0.6114613685226178`; the closest normalized decision is `X` at `-0.45709162919418617`.

Exactly two edges are saddles. Their normalized four-component tuples `(t,1-t,beta1,beta2)` are

```text
[0,Y] (0.5172720967835599,0.48272790321644016,
       1.1642989338039038,0.9312324063157709)

[V,X] (0.7524759483457703,0.24752405165422972,
       1.0783537999756478,0.7740215496491915).
```

Every other true edge has an exact negative component; the closest excluded normalized decision is `-0.29890453102437703` on `[C,X]`. The finite ledgers audit all 12 faces, all 36 directed vertex primitives, and all 72 components of the 18 true-edge cones. Thus the exact class is `(2,2,2)`.

## Connected positive-volume five-support surgery

The ninth-cage source is augmented only by strict-interior seeds

```text
U=(1,-2,3)/2^24,
V=(2,1,-1)/2^24,
W=(-2,3,1)/2^24,
X=(3,2,-2)/2^24,
Y=(-3,-1,2)/2^24.
```

The source and target hulls are independently reconstructed. Their only common exterior face is `[0,H,C]`. Removing it leaves dual-connected disks with common boundary `0-C-H-0`; both have `(V,E,F)=(8,18,11)`, Euler characteristic one, one boundary component, and connected dual graph.

Source patch:

```text
[0,C,L] [0,H,R] [0,L,R] [C,H,T] [C,L,S]
[C,Q,S] [C,Q,T] [H,R,T] [L,R,S] [Q,R,S] [Q,R,T]
```

Target patch:

```text
[0,C,Y] [0,H,V] [0,V,Y] [C,H,U] [C,U,X]
[C,X,Y] [H,U,V] [U,V,X] [V,W,X] [V,W,Y] [W,X,Y]
```

Coning each patch triangle to that side’s exact own centroid gives a positive-volume 3-ball. The minimum source and target cone volumes are

```text
531978638371340508407624018434202696246771033/
2271142360006603575132180239938364254395039744
≈0.23423394664251418

1761109457112849415982497395612061378099450957/
12356162766237134333638527340038852204866568192
≈0.14252883281248377.
```

Removed true edges:

```text
[0,L] [0,R] [C,L] [C,Q] [C,S] [C,T]
[H,R] [H,T] [L,R] [L,S]
[Q,R] [Q,S] [Q,T] [R,S] [R,T]
```

Inserted true edges:

```text
[0,V] [0,Y] [C,U] [C,X] [C,Y]
[H,U] [H,V] [U,V] [U,X]
[V,W] [V,X] [V,Y] [W,X] [W,Y] [X,Y]
```

Inherited edges with changed incident stars are `[0,C]`, `[0,H]`, `[C,H]`. This is an actual full-hull, finite-thickness, same-boundary surgery, not frozen-fan or display-mesh bookkeeping.

## Complete external-arrow census and residual theorem

Every target edge, all 15 inserted edges, and all three inherited star-changed edges were audited over all external directed supports. The all-external-positive changed edges are

```text
[0,V], [C,U], [C,Y].
```

The latter two lie in the protected unstable-`C` star. Every other nonprotected changed edge has an explicit negative witness; its smallest box-wide magnitude is

```text
57891415088852115788293202860444356195082067546773982027980660362705305286250914945638058774701089024883/
276139199654116038797419500915787239715414684586415103043504289223000820803048074431320987458070615425024
≈0.20964576981958818.
```

Thus `[0,V]` is the unique nonprotected adverse changed edge.

It is incident to `[0,V,H]` and `[0,Y,V]`. Every external endpoint arrow is positive, with exact minimum

```text
1895768920472102707933813052134813826587/
122747448744745396908507022659369828352
≈15.444466991850673.
```

Its mutual arrows are

```text
sigma(0→V)=
-731673026720429305317934270253497339195/
122747448744745396908507022659369828352

sigma(V→0)=
1726131922129723097837798474786200463835/
122747448744745396908507022659369828352
```

and satisfy

```text
sigma(0→V)+sigma(V→0)=||V-0||²
=1140208196942335/140737488355328>0.
```

If neither endpoint were unstable, both mutual arrows would have to be nonpositive, contradicting the identity. Therefore one endpoint is unstable in addition to strict unstable `C`; here it is `V`. This proves `U≥2` throughout the certified chamber.

## Exact connector chronology

The canonical connector is the affine chord in all 35 uncentred supplied rows. The actual hull and ordinary centroid are recomputed in every certified active cell. Thirty-four activation, deactivation, circuit, vertex, and edge-cone polynomials have exact integer coefficients, pairwise-disjoint rational isolating intervals, one simple root each, and 68 independently replayed side ledgers.

The decisive total order is:

```text
0.052647106229409  replacement unstable 0 birth
0.163597747975187  source unstable R death
0.239556095505796  stable LSR→LSV transfer
0.264641476647683  carrier [0,V] topological birth
0.372914992334371  bridge saddle [T,V] birth
0.374841497181356  source saddle [R,T] death
0.417477391993180  bridge saddle [H,V] birth
0.443015324461941  bridge saddle [T,V] death
0.506738953289485  replacement unstable V birth
0.566571602045567  bridge saddle [0,C] birth
0.574964140166966  R deactivation / source [0,R] death
0.581532104740723  replacement saddle [V,X] birth
0.603562619103105  bridge saddle [L,Y] birth
0.604618562741102  source saddle [C,L] death
0.607595221616783  unstable 0 death
0.611973530912751  replacement saddle [0,Y] birth
0.617876328414863  bridge saddle [L,Y] death
0.656435252572605  bridge saddle [0,C] death
0.681091999813382  stable LSV→SVY transfer
0.683836875353869  stable SVY→VWY transfer
0.745646292457116  bridge saddle [H,V] death.
```

The certificate also includes all activation/deactivation and mechanically neutral circuit events needed to make 34 roots total. In particular:

```text
unstable 0 birth < source unstable R death;
carrier [0,V] birth < source carrier [0,R] death;
[T,V] saddle birth < [R,T] death;
[H,V] saddle birth < [T,V] death;
unstable V birth < unstable 0 death;
[L,Y] saddle birth < [C,L] death;
[0,Y] saddle birth < [L,Y] death;
[V,X] saddle birth < [H,V] death;
the extra stable component transfers LSR→LSV→SVY→VWY with no gap.
```

Hence the exact connector contains no strict `(1,1,0)` interval. This is a complete deterministic chronology for this chord, not a global atlas of all paths between the endpoint hulls.

## Positive independent-coordinate chamber

All 105 uncentred supplied coordinates vary independently by

```text
|delta r_ij|≤2^-18=1/262144.
```

Directed interval arithmetic recomputes volume, all moments, the dependent common centroid, inactivity, incidence, all face and vertex decisions, all 72 true-edge cone components, every anti-carrier witness, and the `[0,V]` forcing identity. It preserves 8 active vertices, 18 true edges, 12 faces, 27 inactive rows, and strict `(2,2,2)`.

Exact volume interval:

```text
[9084672069243668961449/2361183241434822606848,
 9085600439273144506729/2361183241434822606848].
```

Box-wide lower clearances are approximately

```text
topology oriented determinant  0.16636732887402428
inactive rows                   1.1972161450263115
chosen face decisions           0.6042072034582131
chosen vertex decisions         0.6111585360547133
chosen edge-cone decisions      0.38789455278031915
forcing external arrows         15.443191698783993
anti-carrier witnesses          0.20964576981958818.
```

## Independent verification and falsification

A fresh extraction independently reran deterministic exact generation, exact 34-root chronology construction, independent Sturm/side-ledger chronology replay, directed own-centroid interval verification, primary Fraction reconstruction, a standard-library-only clean-room reconstruction, and exact-table-to-OBJ/STL verification. Terminal markers are

```text
DETERMINISTIC_EXACT_TENTH_CAGE_GENERATOR_PASS
EXACT_TENTH_CAGE_CHRONOLOGY_BUILD_PASS
OWN_CENTROID_INTERVAL_TENTH_CAGE_CERTIFICATE_PASS
INDEPENDENT_EXACT_TENTH_CAGE_CHRONOLOGY_PASS
PRIMARY_EXACT_TENTH_CAGE_NONWINNER_PASS
INDEPENDENT_CLEAN_ROOM_TENTH_CAGE_NONWINNER_PASS
WATERTIGHT_TENTH_CAGE_ENDPOINT_MESH_PASS
ALL_CALM_QUARTZ_90_WALL242_TENTH_CAGE_VERIFIERS_PASS
CALM_QUARTZ_90_WALL242_TENTH_CAGE_PACKAGE_PASS.
```

OBJ and STL agree on 8 vertices, 12 outward facets, 18 edge classes, Euler characteristic two, and edge multiplicity two.

Discovery-only work—never used as proof—completed 422/422 rooted topology/flag metric systems, 570,308 general five-support trials, and 127,843 robust five-support trials. No numerical winner appeared. These finite searches do not exclude other five-support placements.

## Exact scope and next topology

Closed exactly:

- this `U/V/W/X/Y` cage and release of `L/Q/R/S/T`;
- the zero-bridge same-boundary positive-volume replacement;
- deletion of every ninth-cage packet feature;
- every target, inserted, and star-changed external-arrow decision;
- the complete 34-event canonical chronology;
- the full `2^-18` own-centroid chamber;
- the `[0,V]` forcing theorem.

Not closed: every five-support placement/release set, every six-support/linked two-cell topology, every alternative source-target path, or the global existence problem.

The endpoint exposes

```text
[0,V]→[H,Y]   legal forcing-edge escape
[W,Y]→[V,X]   ordinary flip illegal because [V,X] already exists
[0,Y]→[C,V]   legal saddle exchange
[V,X]→[U,W]   legal saddle exchange.
```

The first genuinely unrepresented successor is a **closed six-support carrier cage**, or an equivalent linked two-cell hexahedral/double-octahedral volume, containing the full `[0,V]` star, stable `[V,W,Y]`, and both saddle stars in one communicating positive-volume complex. Release of `0` or `V` is allowed. Before dependent moment closure, it must eliminate every nonprotected all-positive edge, forcing two-edge component, and positive directed cycle.

## Final statement

**NONWINNER, rigorously delimited.** The five-support cage genuinely destroys the ninth-cage packet and changes the complete nonprotected boundary star. The target is an exact own-centred eight-vertex polyhedron with a large strict open coordinate chamber. It fails because inserted edge `[0,V]` is the unique nonprotected all-external-positive forcing carrier, and the connector births the replacement instability and saddle routes before their source predecessors die.

## Artifacts

- [Complete exact archive](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER.zip)
- [Complete handoff](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_COMPLETE_HANDOFF.md)
- [Structured wrapper result](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_COMPLETE_RESULT.json)
- [Clean-extraction receipt](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_clean_verification.json)
- [Fresh clean replay](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_clean_replay_final.txt)
- [Exact generator](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/data/generator_exact.json)
- [Supplied exact V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/data/input_vertices_exact.csv)
- [Own-centred active V-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/data/active_vertices_centered_exact.csv)
- [Primitive irredundant H-data](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/data/tenth_cage8_exact_H_irredundant.csv)
- [Face ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/data/tenth_cage8_exact_faces.csv)
- [Vertex ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/data/tenth_cage8_exact_vertex_primitives.csv)
- [True-edge cone ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/data/tenth_cage8_exact_true_edges_full_cones.csv)
- [External-arrow ledger](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/data/external_arrow_full_ledger.csv)
- [Transition certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/certificates/tenth_cage_shared_global_patch.json)
- [Chronology certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/certificates/source_to_target_death_before_birth_obstruction.json)
- [Arrow certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/certificates/external_arrow_design_certificate.json)
- [Forcing certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/certificates/residual_forced_edge_0_V.json)
- [Perturbation certificate](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/certificates/own_centroid_perturbation_certificate.json)
- [Independent clean-room verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/scripts/verify_independent.py)
- [Independent chronology verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/scripts/verify_chronology.py)
- [Aggregate verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/RUN_ALL_VERIFIERS.sh)
- [Package verifier](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/verify_package.py)
- [Watertight OBJ](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/mesh/body.obj)
- [Watertight STL](sandbox:/mnt/data/Calm_Quartz_90_wall242_tenth_five_support_cage_exact_NONWINNER/mesh/body.stl)

```text
archive SHA-256  481e6f16accce9fa5cde4006144d4a9b01a777f9b38f519d728a3c6e9cfc7174
archive bytes    2103920
manifest entries 49
manifest SHA-256 9a29076b2de0265e3058971e63eb75e85bfb0929f62c877122d17af7dc47a0aa
clean replay SHA-256 571935a27a673edc16e49c8b4927bc8d44d8e634242c37da8fee25aa1e2937ba
clean extraction PASS
```
