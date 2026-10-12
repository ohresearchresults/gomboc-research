# figure-0239

AI research report · 2026-09-03 UTC

---

# Calm Raven 06 — exact E5/E6 Radon-corrector determination

## Outcome and artifacts

**EXACT NONWINNER.** I replaced the tetrahedral second corrector first by an exact five-vertex triangular bipyramid `E5`, then—because its unique Radon wall still relayed the Euler-neutral packet—by an exact six-vertex 4-regular skew triangular antiprism `E6` with two coupled Radon flips. The strongest promoted homogeneous body is exactly ordinary-own-centred but remains strict `(S,U,H)=(2,2,2)`, not `(1,1,0)`.

- [Complete 22 MB replay bundle](sandbox:/mnt/data/Calm_Raven_06_radonE6_exact_NONWINNER.zip)
- [Archive SHA-256 receipt](sandbox:/mnt/data/Calm_Raven_06_radonE6_exact_NONWINNER.zip.sha256)
- [Full report](sandbox:/mnt/data/Calm_Raven_06_radonE6_exact_NONWINNER/RESULT.md)
- [Master exact certificate](sandbox:/mnt/data/Calm_Raven_06_radonE6_exact_NONWINNER/radonE6_master_certificate.json)
- [Independent clean-room receipt](sandbox:/mnt/data/Calm_Raven_06_radonE6_exact_NONWINNER/independent_radonE6_verification.json)
- [Final OBJ](sandbox:/mnt/data/Calm_Raven_06_radonE6_exact_NONWINNER/endpointE6/endpoint_centered.obj) and [STL](sandbox:/mnt/data/Calm_Raven_06_radonE6_exact_NONWINNER/endpointE6/endpoint_centered.stl)

Archive SHA-256: `c32c054eee8bad8300d02613352394bf46eeaf392afed731812d3777348a8a07`. A pristine extraction checked all 137 manifest entries and ended with `INDEPENDENT_EXACT_RADON_E6_PASS`, `INDEPENDENT_RELEASE_SUMMARY_PASS`, and `ALL_EXACT_RADON_E6_VERIFIERS_PASS`.

The governing acceptance gate requires a finite uniform-density body at its own exact ordinary-volume centroid, strict `(1,1,0)`, complete actual H/V/E incidence, exhaustive positive-margin face/vertex/full-edge-cone verification, independent replay, and matching OBJ/STL. :contentReference[oaicite:0]{index=0} The journal specifically identified E5 and then E6 as the first nonrepeating correctors beyond tetrahedral `E4`. :contentReference[oaicite:1]{index=1}

## Exact finite family

```text
P(t1,t2,t3)=B+t1*C1+t2*C2+t3*C3
             +(10677075263/4294967296)*D+E.
```

`D` is the exact `closededge21` summand `(V,E,F)=(16,25,11)`. Complete exact B/C/D rows and vertices are in `summands_H.csv`, `summands_V.csv`, and `endpointE6/D_H.csv`, `D_V.csv`, `D_edges.csv`, `D_faces.csv`. `C1,C2,C3` are used only as dependent full-rank controls for the three ordinary first moments.

## E5: exact triangular bipyramid and unique Radon circuit

Exact vertices:

```text
e0=(0,0,0)
e1=(10738565,-203062521,-581510341)/16777216
e2=(550762868,233248965,-3124960269)/16777216
e3=(621327126,276007399,1336302632)/16777216
e4=(-866210977,-2537310561,968453492)/16777216
```

Its exact f-vector is `(5,9,6)`. The nine true edges are

```text
01,02,03,04,12,14,23,24,34.
```

The six irredundant supporting rows, with facet cycles, are:

```text
E0=(-1,464486370289499859/1753591995349885094,-146321252168846118/876795997674942547; 57023807541835611287277827/29420391681856017797218304), cycle 1-2-4
E1=(-1,164436946613298059/557376312368928211,-67714019697325994/557376312368928211;0), cycle 0-1-4
E2=(-1,286716714209744003/770198995423025214,-38114685207035151/256732998474341738;0), cycle 2-1-0
E3=(-1,439811608320353864/914478777561270965,1337419239888558863/3657915110245083860;0), cycle 3-0-4
E4=(-1174203361665806211/2677608452918225470,1,-3545358798267871/1338804226459112735;0), cycle 3-2-0
E5=(1,-6610341551117778683/12535222390490355200,-67457447282931489/6267611195245177600;5783683394924213295329921587/210306133653293035107123200), cycle 2-3-4
```

The unique affine circuit is

```text
4228306068108476699555538246*e0
-5783683394924213295329921587*e1
+1174240893225788190326487759*e2
-171071422625506833861833481*e3
+552207856215455239309729063*e4=0,
```

with coefficient sum zero, positive part `{0,2,4}` and negative part `{1,3}`. Exact regular triangulations are

```text
{0124,0234}  <->  {0123,0134,1234},
```

a genuine full-dimensional `2↔3` event. Each tetrahedron extends with one fixed P9-side vertex and one fixed scaled-D vertex to an exact lower 5-simplex in the three-colour Cayley embedding; every unselected Cayley point has positive exact lift slack and every translated mixed cell has positive exact volume.

At the exact positive moment root `(1,1,1)`, E5 gives common refinement `(106,205,101)`, volume `3340444.6342578656…`, exact first moment `(0,0,0)`, nonzero moment Jacobian determinant `3.568298536465256e15`, rational Krawczyk radius `2^-22`, and minimum nonincident slack `1.3304141045599097e-6`. Its exhaustive class is `(2,2,2)` with positive features:

- stable 36, intended lineage `P9edge(27;102)|D045|Eedge(1;3)`, margin `0.3443685723061059`;
- stable 51, `P9edge(9;26)|D(18,19,20)|Eedge(4;5)`, margin `0.09412357716110577`;
- unstable 44, `P9[9,100,103]|D[1,7,11]|E[0,1,3,5]`, margin `0.0031065443937455944`;
- intended unstable 61, `P9[15,26,27]|D048|E[0,2,4,5]`, margin `0.2618257562075484`;
- saddles 12 and 151, margins `0.03147929752409854` and `0.2037004795816619`.

The E5 extra maximum has four strictly positive outgoing arrows; the minimum is `0.3094673622771227`. Thus the single Radon circuit deletes the preceding mechanical packet but births another one.

## E6: exact skew triangular antiprism and coupled Radon pair

Exact vertices:

```text
e0=(0,0,0)
e1=(10738565,-203062521,-581510341)/16777216
e2=(550762868,233248965,-3124960269)/16777216
e3=(621327126,276007399,1336302632)/16777216
e4=(-1064915912,-3004110004,837569063)/16777216
e5=(269931130,311500836,-1051037655)/16777216
```

Its exact f-vector is `(6,12,8)` and degree sequence `(4,4,4,4,4,4)`. True edges are

```text
01,03,04,05,12,14,15,23,24,25,34,35.
```

The eight irredundant supporting rows are:

```text
E0=(-1,492383984007943061/1626290843862424220,-80254870107273579/500397182726899760;136902427365295369418901383/109138531065208661690286080), cycle 1-2-4
E1=(-1,610265325298431397/1916999918271939187,-248504340288838412/1916999918271939187;0), cycle 0-1-4
E2=(-1,202843575152536589/551952986612079846,-54929341672654527/367968657741386564;530573031767518691935801/6173489652157314523725824), cycle 5-2-1
E3=(-1,145681107277150255/394567313254373331,-19385989243039690/131522437751457777;0), cycle 5-1-0
E4=(-1,1943454314804583322/4245575363724227665,1572610363948335616/4245575363724227665;0), cycle 3-0-4
E5=(-706353556424609697/1013747884976663690,1,8502923577003319/72410563212618835;0), cycle 3-5-0
E6=(52084897162862259/279841804913816470,1,-1752971054860501/139920902456908235;5245758424953742830406095/234748320343448015077376), cycle 3-2-5
E7=(1,-7487580743262756436/14612141014534695157,-159357939047299482/14612141014534695157;3399670731069062160712611097/122575523011653860071571456), cycle 2-3-4
```

All six five-point subsets are exact circuits. In the exact two-dimensional secondary-fan slice with lift `a` on vertex 0 and lift `b` on vertex 5, the certified chambers are

```text
A=(-50,-36), B=(-50,-50), C=(-37,-50).
```

`A→B` crosses circuit `{0,2,3,4,5}` and performs `2↔3`:

```text
remove {0234,0235}; insert {0245,0345,2345}.
```

`B→C` crosses circuit `{0,1,2,4,5}` and performs `3↔2`:

```text
remove {0124,0125,0245}; insert {0145,1245}.
```

All other circuit signs remain unchanged at each crossing. The flips share chamber B and overlap on `{0,2,4,5}`. Exact lower-cell determinants, positive volumes and strict Cayley lift slacks are in `coupled_radon_E6_certificate.json`. These are exact regular mixed cells; the physical E5 and E6 endpoint fans are separately reconstructed rather than inferred from the lift diagram.

## Final common fan, moments and mechanics

The actual E4→E5 transition removes/inserts `109/105` common vertices, `102/99` maximal faces and `211/204` true edges. E5→E6 removes/inserts `106/108` vertices, `98/101` faces and `203/208` edges. Both transitions have exact nonempty H/V/E symmetric differences.

For E6, a fresh GMP reconstruction yields 20 exact volume coefficients and 35 exact coefficients in each first-moment polynomial. The exact positive root is `(t1,t2,t3)=(1,1,1)`, isolated in `[1±2^-22]^3`; the exact Jacobian determinant is nonzero, with decimal locator `5.971369618953818e15`. Exact tetrahedral integration gives volume `3779910.2852822701…` and first moment and centroid exactly `(0/1,0/1,0/1)`.

The final actual common refinement has `(V,E,F)=(108,210,104)`, Euler two, complexity 420, and minimum exact nonincident slack `1.3304141045599097e-6`. Every maximal face, vertex, true edge, and all `840` four-component edge-cone primitives are strict. The complete positive set is:

| type | id | exact lineage | margin |
|---|---:|---|---:|
| stable | 35 | `P9edge(27;102)|D045|Eedge(1;4)` | `0.4222255259519434` |
| extra stable | 51 | `P9edge(9;26)|D(18,19,20)|Eedge(6;7)` | `0.061510690783569515` |
| extra unstable | 47 | `P9[9,100,103]|D[1,15,20]|E[0,1,4,7]` | `0.0060435408600227935` |
| intended unstable | 63 | `P9[15,26,27]|D048|E[0,2,6,7]` | `0.2621678466644689` |
| saddle | 12 | `P9edge(13;26)|Dedge(4;17)|Evertex(4;5;6;7) || P9edge(13;26)|D048|Eedge(6;7)` | `0.03003052660379185` |
| saddle | 156 | `P9edge(15;27)|Dedge(1;11)|Evertex(0;1;4;7) || P9edge(15;27)|Dedge(7;11)|Evertex(0;1;4;7)` | `0.03664014840918944` |

All E4 critical identities are absent from E5, and all E5 critical identities are absent from E6. Exact descendant ledgers supply negative witnesses for the geometric remnants. The two Radon stages therefore genuinely delete their predecessor mechanical packets, but each births another Euler-neutral packet.

At extra unstable vertex 47 the complete exact outgoing-arrow ledger is strictly positive:

```text
47→30   106.68828338219858
47→46     0.13619178510871097
47→48     3.978094783249529
47→105 16742.980534475184
```

The intended unstable vertex 63 is distinct and independently strict. Hence `U>=2` throughout the certified fixed-incidence/external-sign E6 cell.

## Positive-dimensional centred family

Fix E6 vertices `e0…e4` and vary all three Cartesian coordinates of `e5` independently.

- Shape-only directed radius `2^-40` preserves E6 `(6,12,8)`, common fan `(108,210,104)`, intended D045/D048 lineages, and own-centroid class `(2,2,2)`.
- Shape×control radii `2^-48` and `2^-42` preserve the same fan and mechanics.
- A 150-digit directed parametric Krawczyk theorem uses shape radius `2^-60` and dependent-control radius `2^-42`: every E shape in that three-dimensional box has exactly one positive moment-closing control triple.

Thus three independent physical E-shape coordinates survive centring; `C1,C2,C3` remain dependent moment controls.

## Independent reconstruction and mesh

`verify_radonE6_cleanroom.py` imports neither `exact_core.py`, a generator, the auxiliary builder, nor search code. It reconstructs D/E5/E6 from exact H rows and all feasible triples, rebuilds both common fans, recomputes exact volume and every equilibrium primitive, freshly compiles the GMP moment engine, verifies all Radon/Cayley cells, transition and lineage ledgers, arrow signs, directed boxes, manifest, and OBJ/STL parity.

The final mesh has 108 vertices, 212 outward triangles and 318 triangulation edges; every edge has incidence two and `108-318+212=2`.

Principal hashes:

```text
MANIFEST.sha256                         645cabb244cbe60dd3e452ca16a58d066254cff8f4e25afeec178980eb3b79ec
RESULT.md                               86ed8e125055bc921ee382e22d816023c90cf10421d03fd41b68bcd9ea041883
radonE6_master_certificate.json         4ab2d4af2be7996b9bf8edb42089ed13f072c80eea31957723d2139f12bf9add
independent verification                725d7a6943fcbb1ced1c0fb8598344974a0edd5ec484c94fced6937520c1d5f3
radon_E5_certificate.json               b74f2c182333b3def1e35e2aa9b30a66b969c6fe1939685349159d2631995dcb
coupled_radon_E6_certificate.json       5ef35f68a87332080d8736e13ff0e52390bcd636fb4ec4c3d4a48ebb8eecd301
common-fan atlas                        faa43eecb2902a0fce0a775c0011942e1ba9208e3b3cbabc79504d12999b8161
carrier-transition certificate          2565a0b6f491a23a7257739f61e9746a11d3db08c43eb92e81159f6878b3107c
external-arrow certificate              7407c5799d11510218343ce31e1e97ba043a51811a698612f7180a3f727c5773
endpointE6 exact/root                    84d8f73a… / 5a4c9038…
OBJ/STL                                  83a61804… / 6824bb42…
```

## Exact scope and next topology

The exact theorem covers the displayed E5 and E6 cells and their certified boxes. The numerical searches in `search_provenance` are locator evidence only; they do not exclude all five- or six-vertex correctors.

The obstruction has advanced with secondary-fan dimension: E4 has dimension zero and no internal circuit; E5 has dimension one and one relaying wall; E6 has dimension two and two coupled relaying flips. The first genuinely unclassified corrector is therefore a seven-vertex chiral capped triangular antiprism or pentagonal-bipyramid-type `E7`, whose secondary fan has dimension three. It should realize a closed three-wall Radon chamber rather than a linear two-flip chain, so the extra stable, extra unstable and both saddle death sheets can be phased before any replacement birth. It must preserve D045/D048 and retain at least three shape coordinates after moment elimination. This is an evidence-supported next topology, not a proof of global seven-vertex minimality. The exact M42 `(61,163,104)`, `(2,1,1)` body remains the stronger global benchmark.
