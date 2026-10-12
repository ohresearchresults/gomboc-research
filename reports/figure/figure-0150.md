# figure-0150

AI research report · 2026-08-29 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Literal verdict

**NONWINNER.** I constructed and exactly certified the requested genuinely two-parameter connected guarded Y-family, including its complete two-dimensional circuit/equilibrium arrangement on the declared exact parameter square. It contains **no open own-centroid `(S,U,H)=(1,1,0)` cell**.

The exact arrangement has three full-dimensional hull topologies and five full-dimensional equilibrium cells. Their classes, in wall order, are

`(3,2,3) -> (3,2,3) -> (3,2,3) -> (4,2,4) -> (3,2,3)`.

The decisive obstruction is stronger than failure of a numerical search: two distinct maximal faces remain strictly stable throughout the entire parameter square by exact tensor-Bernstein certificates, so `S>=2` everywhere off the wall curves. Every wall itself has a zero primitive or incidence margin and therefore cannot supply the positive ambient perturbation box required by the project’s acceptance gate. That gate excludes wall points, auxiliary centres, and near-solutions and requires a fully materialized exact object with complete incidence and all-feature verification.

A separate broader connected-coordinate search produced a stronger exact 12-vertex endpoint `G27` of class `(2,2,2)`. It is fully materialized, independently reconstructed, and watertight, but it is also a literal nonwinner. It is not asserted to lie in the certified affine parameter square.

## 1. What changed relative to the journal

The journal’s one-dimensional continuation had shown that suppressing `V2/E(2,3)` merely transferred the first incoming lower packet to `V4/E(4,10)`. I added two exact affine modes with genuinely distinct guard roles:

- the `s` mode drives `V2/E(2,3)` farther inactive while allowing `V4/E(4,10)` a small outward derivative;
- the `t` mode drives `V4/E(4,10)` farther inactive while allowing `V2/E(2,3)` a small outward derivative;
- both modes simultaneously decrease the governing components of both upper stable–saddle routes and the original lower unstable–saddle route.

The exact atlas reveals a feature missed by coarse grids: after the two circuit flips there is a narrow but genuine open `(4,2,4)` equilibrium cell. It is bounded by two distinct equilibrium walls. The first wall births stable face `[9,10,12]` together with saddle `(10,12)`; the second removes that face and saddle `(9,12)`, leaving `(10,12)` as the transferred saddle. Thus the two lower guards do not create cancellation. They force a further stable–saddle relay.

## 2. Exact starting body

Let `D=2^24=16777216`. The independently reconstructed Conway-compression source has vertices `q_i=Q_i/D` with

```text
0   16777216          0  -16777216
1    5184445   15956081  -16777216
2  -13573053    9861400  -16777216
3  -13573053   -9861400  -16777216
4    5184445  -15956081  -16777216
5   42051094   28817600     417778
6   24543408   26610733  -11452254
7   47848796   58066323   44119118
8  -24046926    6156753  -11843524
9  -15959723  -23586121   23797487
10 -18390945  -24540266  -15149485
11  16396154   -5769132   -6616835
12   -575692    1799886  446447126
```

Its exact uncentred ordinary-volume centroid is

```text
Cx = 8927530278674435758346646647585
     /19580682792453552593699143155712
Cy = 46941148293800050264959085443927
     /78322731169814210374796572622848
Cz = 495967542504696380404904555281339
     /78322731169814210374796572622848
```

or approximately `(0.45593559598009165,0.5993298189771412,6.332357606751124)`. After exact translation by that centroid it has `(V,E,F)=(13,31,20)` and strict class `(3,2,3)`.

The target stable feature is the bottom pentagon `[2,1,0,4,3]`; the target unstable vertex is `12`. The residual block is

- upper A: stable `[12,7,8]`, saddle `(7,12)`;
- upper B: stable `[11,5,12]`, saddle `(9,12)`;
- lower: unstable `10`, saddle `(0,1)`.

The nearest incoming lower walls are `V2/E(2,3)` and `V4/E(4,10)`.

## 3. Complete exact two-parameter guarded Y-family

Define

`P_i(s,t)=Q_i/2^24+s u_i/2^18+t v_i/2^18`,

on the exact square

`R={(s,t): 0<=s<=1/10, 0<=t<=1/10}`.

The two integer mode tables are:

| i | ux | uy | uz | vx | vy | vz |
|---:|---:|---:|---:|---:|---:|---:|
|0|37461|-62566|0|44235|-57797|0|
|1|-69215|-38269|0|-60387|-31169|0|
|2|37467|101144|0|-21179|153732|0|
|3|-235050|-36291|0|-229735|-63707|0|
|4|-39616|-36053|0|-100445|-2093|0|
|5|-147971|115071|-99605|-156601|112865|-102624|
|6|-53800|197180|38108|-52528|190593|34773|
|7|-286498|-564284|1245737|-276106|-581668|1224588|
|8|456347|35540|-82966|478550|33508|-82547|
|9|-2254|25483|-5701|17056|23807|-7992|
|10|37599|-83788|25325|77653|-110692|22691|
|11|49198|82744|-16066|67036|94157|-18891|
|12|213244|264981|-47959|221471|241296|-45246|

All thirteen vertices move, and their support is the complete connected true-edge graph of the source body. The lower branch is connected to both upper branches through actual edge routes, not through disconnected caps.

### First-order guard separation

For the governing exact primitive `p`, the table gives `(partial_s p)/p` and `(partial_t p)/p` at `(0,0)`. Active residuals have `p>0`; incoming guarded witnesses have `p<0`.

| primitive | s logarithmic derivative | t logarithmic derivative |
|---|---:|---:|
| upper-A face | -3.849404 | -4.011495 |
| upper-A saddle | -2.540655 | -2.610438 |
| upper-B face | -3.397154 | -3.586329 |
| upper-B saddle | -10.379847 | -13.048902 |
| lower `U10` | -2.261226 | -2.382911 |
| lower `H(0,1)` | -1.676467 | -1.583248 |
| `V2` and `E(2,3)` | +34.580216 | -4.773486 |
| `V4` and `E(4,10)` | -1.682255 | +0.691713 |

Because the last four primitives start negative, the signs mean that the `s` mode makes `V2/E(2,3)` more negative but makes `V4/E(4,10)` less negative, while the `t` mode does the converse. Exact rational derivatives, not only these decimals, are stored in the atlas.

## 4. Exact ordinary-volume centring in every cell

For every actual oriented boundary triangle `(a,b,c)`, the verifier uses

```text
V = sum det(p_a,p_b,p_c)/6
M = sum det(p_a,p_b,p_c)(p_a+p_b+p_c)/24
C = M/V.
```

All arithmetic is rational in `(s,t)`. In each actual hull topology the volume and three first moments are expanded exactly. Mechanics is then evaluated at the translated points `x_i=p_i-C`.

To avoid division in every sign test, the exact implementation writes

`Y_i=4 V6 p_i-N`,

where `V6=6V` and `N=24M`. Face projection components, every incident vertex support, and all four components of every true-edge cone are polynomial signs in `(s,t)`.

For a true edge `uv`, with `d=p_v-p_u`, incident outward normals `n1,n2`, and

`Z=||d||^2 Y_u-(Y_u·d)d`,

the four exact components are proportional to

```text
-Y_u·d,
 Y_v·d,
(Z·n1)||n2||^2-(Z·n2)(n1·n2),
(Z·n2)||n1||^2-(Z·n1)(n1·n2).
```

Thus the audit is the complete four-component mixed normal-cone test, not an endpoint or one-normal surrogate.

Each topology has 198 strict nonincident support tests and 64 actual features: 20 maximal faces, 13 vertices, and 31 true edges. The equilibrium proof checks 248 primitive face/vertex/edge components per topology.

## 5. Exact two-dimensional circuit arrangement

Only two hull circuits occur in the square. With the primitive orientations used by the verifier,

```text
C1(s,t) =
 99835032171399151616 s^3
+350674914183267270656 s^2 t
+203647696134114854912 s^2
+404353673505194639360 s t^2
+384354450944541740032 s t
-173467839501481183680 s
+153366113100070076416 t^3
+178112820481456812032 t^2
-155134649685946280004 t
+8285236961889875175
```

is circuit `(2,3,8,10)`, and

```text
C2(s,t) =
 11897596984462446690304 s^3
+35208038509757265870848 s^2 t
+289917969170893557573632 s^2
+34336770936102026870784 s t^2
+671966348617246085263360 s t
-451703172240428650595424 s
+11034001281875129663488 t^3
+383443127732109558530048 t^2
-570563250379837450077408 t
+71040736963398951271953.
```

Exact tensor-Bernstein coefficients prove that both partial derivatives of both polynomials are strictly negative throughout `R`.

The following global exact inequalities order all four atlas walls:

```text
C2 - 2000 C1 > 0,
R - 78727844478351363312119663558656 C2 > 0,
A - (113/1000) R > 0.
```

Here `R` and `A` are the primitive degree-seven equilibrium factors generated deterministically as follows in topology T2:

```text
R = primitive gcd of
    face component (F,[9,10,12],12,10)
    and edge component (E,(10,12),2),

A = primitive gcd of
    face component (F,[9,10,12],9,12)
    and edge component (E,(9,12),2),
```

with both oriented positive at `(s,t)=(1/20,1/10)`. Their complete integer coefficient lists are in the exact atlas and are regenerated from the displayed family by the verifier rather than accepted as input.

Both derivatives of `R` and `A` are likewise interval-certified negative on the complete square. The inequalities imply the strict wall order

`C1, C2, R, A`.

In particular, no fourth circuit sign combination exists: `C1>0` forces `C2>0`; `C2>0` forces `R>0`; and `R>0` forces `A>0`.

### Certified wall locations

The exact atlas gives 60-step dyadic isolators. Decimal locators are:

| wall | first boundary intersection | second boundary intersection |
|---|---:|---:|
| `C1=0` | `s=0.05087698088708011` on `t=0` | `t=0.057372604475788506` on `s=0` |
| `C2=0` | `s=0.04818952606052283` on `t=0.1` | `t=0.05999072183625911` on `s=0.1` |
| `R=0` | `s=0.08812068643363077` on `t=0.1` | `t=0.09061495973478160` on `s=0.1` |
| `A=0` | `s=0.08861440640849198` on `t=0.1` | `t=0.09101668162991390` on `s=0.1` |

The strict derivative and ordering certificates prove that these are four disjoint monotone wall arcs, not aliases created by sampling.

## 6. Actual hull topologies

### T0: `C1>0`

This is the original `(13,31,20)` lattice.

### T1: `C1<0<C2`

Circuit `(2,3,8,10)` flips. The old triangles

`[2,3,10]`, `[8,2,10]`

are replaced by

`[8,2,3]`, `[8,3,10]`.

The f-vector remains `(13,31,20)`.

### T2: `C2<0`

Circuit `(2,7,8,12)` also flips. The old triangles

`[7,2,8]`, `[12,7,8]`

are replaced by

`[12,7,2]`, `[12,2,8]`.

Again the f-vector remains `(13,31,20)`.

For T0, exact support validity consists of 192 globally negative support polynomials, four circuit-proportional tests, and two additional tests proved negative by positive multiples of `C1`. T1 has 194 globally negative tests and four circuit-proportional tests. T2 has 192 globally negative tests, four circuit-proportional tests, and two additional tests proved negative using `-C2`. Thus every hull in every open topology cell is the actual convex hull claimed, with no stale edge or triangulation label.

## 7. Exact equilibrium cell complex

The two topology walls and two equilibrium walls divide the square into exactly five open cells:

| cell | defining inequalities | exact class | decisive change |
|---|---|---:|---|
| T0 | `C1>0` | `(3,2,3)` | source cell |
| T1 | `C1<0`, `C2>0` | `(3,2,3)` | first diagonal flip |
| T2a | `C2<0`, `R>0` | `(3,2,3)` | second diagonal flip; saddle still `(9,12)` |
| T2b | `R<0`, `A>0` | `(4,2,4)` | face `[9,10,12]` and saddle `(10,12)` born while `(9,12)` remains |
| T2c | `A<0` | `(3,2,3)` | face `[9,10,12]` and saddle `(9,12)` disappear; `(10,12)` remains |

Exact rational representatives are respectively

`(0,0)`, `(0,23/400)`, `(1/20,1/10)`, `(221/2500,1/10)`, `(9/100,1/10)`.

At each representative, an exact ordinary-volume integration and complete 64-feature audit reproduces the stated class. The continuous cell proof does not depend on representative sampling: every unresolved feature component is closed either by a globally signed Bernstein expansion, a positive conditional residual such as `q-lambda C1`, an exact circuit factor, or the exact `A/R` factor table.

Two faces are especially decisive. Every oriented projection component of

- bottom face `[0,1,2,3,4]`, and
- upper face `[5,11,12]`

has a strictly positive tensor-Bernstein lower coefficient on the entire closed square. Consequently every open cell has at least two stable maximal faces. This alone proves that the family has no `(1,1,0)` member, independently of what happens to the remaining features.

The narrow T2b cell is a genuine open cell, not a degeneracy. At its representative `(221/2500,1/10)`, the complete class is `(4,2,4)`. The transfer factorization is:

- the governing component of face `[9,10,12]` at edge `(12,10)` and the third cone component of `(10,12)` are `R` times globally negative factors;
- the governing component of the same face at edge `(9,12)` and the third cone component of `(9,12)` are `A` times globally positive factors;
- the remaining face component satisfies `f0-1478811992494359145611264 A>0` globally.

That proves the exact sequence `one saddle -> stable face plus two saddles -> the other saddle`.

Every point on `C1=0` or `C2=0` has a four-point incidence circuit with zero ambient incidence margin. Every point on `R=0` or `A=0` has a zero equilibrium primitive. None can be the required open perturbation-stable endpoint.

## 8. Strongest separately exactified endpoint `G27`

A broader connected-coordinate continuation produced a strict dyadic endpoint with one old input vertex interior. It therefore has twelve actual vertices. Let `D_G=2^44=17592186044416`; the exact vertex numerators, with retained old labels, are:

```text
old 1   -7715758938572    2889556079942   -17779918034961
old 2   -8262479746679    1678647340512   -17660251163923
old 3  -19718591797520  -41379697761669   -17592525598195
old 4  -19707343224389  -41384307037227   -17592329907461
old 5   28735822451870   65017701265160    16682797993973
old 6    3600087730963   23172133013753   -11017132169953
old 7   27967861505375   64205100806705    32167696120114
old 8   -5658133234447  -11830031585001   -22901357099805
old 9  -24778822577834  -27890508662314    -3487947517004
old 10 -17333854524801  -42073399768973   -17068563828311
old 11   7425371686672    6793144760174   -22628800214142
old 12   4728022774716   39660727728711   500165975828058
```

The uncentred points are these triples divided by `D_G`. Translate them by the exact ordinary-volume centroid

```text
Cx = -80130892167915688765901627395182677002773622552661661
     /2233952433302997641806976648607592905411276269003210752
Cy =  924108759641053208337853244673027179021707878723193631
     /1554053866645563576909201146857455934199148708871798784
Cz =  464496956870470259327279458352642485368709915665052200839
     /71486477865695924537823252755442972973160840608102744064
```

approximately `(-0.03586956059285408,0.5946439692182284,6.497689783278125)`.

The exact volume is

`126985493881363575031115070067221091983997 / 4083388403051261561560495289181218537472`

or approximately `31.098068894566882`.

The exact uncentred first moments are

```text
Mx = -26710297389305229588633875798394225667591207517553887
     /23945242826029513411849172299223580994042798784118784
My =  21254501471744223791770624627479625117499281210633453513
     /1149371655649416643768760270362731887714054341637701632
Mz =  464496956870470259327279458352642485368709915665052200839
     /2298743311298833287537520540725463775428108683275403264.
```

The exact verifier proves `M_j=V C_j`; hence all three moments after translation are exactly zero.

### Maximal faces

```text
[2,1,8]       [9,1,2]       [6,11,1]      [12,6,1]
[1,11,8]      [12,1,9]      [2,8,3]       [2,3,9]
[8,4,3]       [3,4,12]      [12,9,3]      [8,10,4]
[4,10,12]     [5,11,6]      [12,5,6]      [11,5,7]
[12,7,5]      [11,7,12]     [8,11,10]     [10,11,12]
```

All twenty faces are triangular. The true edges are

```text
(1,2) (1,6) (1,8) (1,9) (1,11) (1,12)
(2,3) (2,8) (2,9)
(3,4) (3,8) (3,9) (3,12)
(4,8) (4,10) (4,12)
(5,6) (5,7) (5,11) (5,12)
(6,11) (6,12)
(7,11) (7,12)
(8,10) (8,11)
(9,12)
(10,11) (10,12)
(11,12)
```

Thus `(V,E,F)=(12,30,20)`.

An irredundant centred H-representation is generated without hidden numerical choices: for each listed oriented face `(a,b,c)`, set

`n_f=(Q_b-Q_a) cross (Q_c-Q_a)` and `h_f=n_f·Q_a`.

The centred halfspace is

`n_f·x <= h_f/D_G - n_f·C`.

Every nonincident support is strictly negative. The minimum exact integer support slack before division by the common scales is

`209347532959498484795962659838133252`.

### Complete own-centroid equilibrium audit

`G27` has strict class

`(S,U,H)=(2,2,2)`.

The positive features are:

- stable faces `[12,6,1]` and `[10,11,12]`;
- unstable vertices `3` and `12`;
- saddle edges `(3,12)` and `(5,12)`.

Normalized positive margins are:

| feature | margin |
|---|---:|
| extra stable `[12,6,1]` | `+9.026602674266982e-4` |
| target stable `[10,11,12]` | `+1.992689451715934e-2` |
| extra unstable `3` | `+3.339502541949767e-4` |
| target unstable `12` | `+9.898302156877877e-1` |
| saddle `(3,12)` | `+2.7452697229308885e-4` |
| saddle `(5,12)` | `+3.360583222767690e-5` |

The closest excluded features remain strictly negative:

- face `[12,7,5]`: `-3.1224068604333604e-5`;
- vertex `11`: `-2.566498537711454e-5`;
- edge `(7,12)`: `-3.135829845859403e-5`.

### Perturbation and independent mesh certificate

Exact rational interval arithmetic certifies the complete `(12,30,20)` lattice and `(2,2,2)` class when **all 36 vertex coordinates vary independently** by at most

`epsilon=2^-29=1/536870912`.

The corresponding directed volume enclosure is

```text
[126985491604219757863354421606604848497277 /
 4083388403051261561560495289181218537472,
 126985496158507392957178214363945035645565 /
 4083388403051261561560495289181218537472].
```

A separate SciPy/Qhull implementation reconstructs `(12,30,20)` and the same `(2,2,2)` feature set. Trimesh independently reports, for both OBJ and STL:

- 12 vertices, 20 triangles;
- watertight `true`;
- winding-consistent `true`;
- Euler number `2`;
- volume `31.09806889456688`;
- centre of mass within about `5e-16` of the origin.

This endpoint is therefore a rigorous open nonwinner, not a wall artefact.

## 9. Obstruction and next topology

### Exact obstruction inside the certified family

The requested two lower guards work exactly as intended at first order, but the family remains trapped by two global stable witnesses. Neither topology flip removes bottom face `[0,1,2,3,4]` or upper face `[5,11,12]`. The later `R/A` event only relays a saddle through a temporary new stable face. Therefore no refinement of this same two-dimensional affine square can lower `S` to one.

### Broader observed relay

Outside the exact square, numerical continuation that simultaneously guards `V2/E(2,3)` and `V4/E(4,10)` makes `V1/E(1,2)` the next lower incoming packet. Adding a third local guard transfers the first packet again to `V0/E(0,4)`. This broader relay is empirical rather than an exact exclusion, but it identifies the base cycle

`0-1-2-3-4-0`

as the complete lower return belt.

### Smallest genuinely new successor

The next operation should not be another two-mode tangent or a third isolated guard. It should be a **three-dimensional connected return cell** with these properties:

1. one branch continues to couple the two upper routes through the apex-side star;
2. two lower branches span opposite sectors of the complete base belt and share actual cross-faces, so the incoming `V0/V1/V2/V4` packets cannot circulate around the pentagon independently;
3. the branch must permit at least one obsolete base-adjacent vertex or one of the two globally stable faces to disappear in the same incidence event;
4. all three ordinary moments remain dependent exact equations after each hull rebuild;
5. the first search cell should include the complete stars of edges `(0,1)`, `(1,2)`, `(2,3)`, `(3,4)`, `(4,10)`, and both upper saddles, rather than guarding only their current labels.

A useful alternative seed is exact endpoint `G27`. Its residual block is compact: extra stable `[12,6,1]`, extra unstable `3`, saddles `(3,12)` and `(5,12)`, with nearby inactive face `[12,7,5]`, vertex `11`, and edge `(7,12)`. A nonredundant successor would replace that complete apex-side star in one prismatic or tetrahedral two-cell event, allowing old vertices `3,5,6,7,11` to deactivate together while retaining the exact centroid equations.

## 10. Reproducible artifacts

### Exact guarded-Y atlas

- Exact two-parameter circuit and equilibrium atlas (`guarded_y2d_exact_atlas.json`)
- Deterministic exact atlas builder and verifier (`build_guarded_y2d_certificate.py`)
- Exact guarded-Y family generator (`guarded_y2d_family.py`)
- Exact bivariate Bernstein arithmetic (`bivar_exact.py`)
- Independent Qhull family cross-check (`verify_guarded_y2d_independent.py`)
- Independent family verification report (`guarded_y2d_independent_verification.json`)

The independent checker audits all five rational representatives and a separate `21x21` actual-hull grid. It reproduces the exact representative classes and finds no winner. The exact atlas, rather than that grid, supplies the continuous proof.

### Exact `G27` endpoint

- Complete exact endpoint report (`G27_exact_report.json`)
- Standalone exact Fraction verifier (`verify_G27_exact.py`)
- Exact-verifier output (`G27_exact_verification.json`)
- Independent Qhull and Trimesh verifier (`verify_G27_independent.py`)
- Independent endpoint report (`G27_independent_verification.json`)
- Exact perturbation-box verifier (`verify_G27_perturbation.py`)
- Perturbation certificate (`G27_perturbation_certificate.json`)
- Exact numerator coordinate table (`G27_vertices.csv`)
- Centred watertight OBJ (`G27_centered.obj`)
- Centred watertight STL (`G27_centered.stl`)

No consolidated ZIP was generated in this continuation; the mathematical generators, ledgers, verifiers, reports, and meshes are individually materialized above.

## 11. Scope and unresolved uncertainty

The nonwinner theorem is exact for the displayed guarded-Y family on `[0,1/10]^2`. It does not exclude arbitrary two-parameter patches, a larger continuation of these modes after additional circuit changes, or the proposed three-dimensional lower return cell.

Larger numerical scans of these and related mode planes found no winner, but those scans are not used as exact exclusion evidence. Likewise `G27` is an exact, independently verified endpoint from the broader connected search, but it is not represented as a point of the certified affine square.

The durable new facts are therefore:

- the requested two guard controls have been made genuinely independent;
- the full exact 2D arrangement has been closed;
- it contains three hull cells and five equilibrium cells, with zero winners;
- a previously unresolved narrow `(4,2,4)` transfer cell is real;
- two globally stable faces exactly obstruct the whole square;
- the strongest exact successor endpoint is the open `(2,2,2)` body `G27`;
- the next nonrepeating topology must span the full lower pentagonal return belt or replace the complete compact `G27` apex star, rather than add another isolated guard.
