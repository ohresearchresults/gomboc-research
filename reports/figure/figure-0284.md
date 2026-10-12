# figure-0284

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Vivid Quartz 58 — exact `E29-HX2` determination

## Literal verdict

**EXACT MATERIALIZED NONWINNER.** No finite homogeneous convex polyhedron with strict own-centroid `(S,U,H)=(1,1,0)` was obtained. The run’s completion gate requires exact own-volume centring, finite V/H/E data, exhaustive strict face/vertex/full-edge-cone mechanics, an independent verifier, and matching OBJ/STL.

The immutable source is `figure-0282`, SHA-256 `656038ebc281b3ef2277b7bac63a97fc14d8ba2f83baaebf974970fc03829c63`. It supplies exact `E27AB2`, `(V,E,F)=(27,75,50)`, strict `(3,2,3)`, with stable faces `[8,A,B]`, `[8,RA,A]`, `[8,RB,O1]`, unstable vertices `8,RB`, and saddles `(8,A),(8,B),(10,RA)`; the journal identifies the six-face `E29-HX2` disk as its first nonrepeating successor.

The literal six-triangle disk is geometrically realizable, but it leaves both `(8,A)` and `(8,B)` stars unchanged, has `RB→RD>0`, and is `(3,3,4)`. A stronger 29-vertex topology changes both stars through two communicating finite-thickness pages and achieves a strict negative chain `RB→RD→RC→RA`; the extra unstable equilibrium transfers to `RA`. The promoted exact endpoint `E29HX2S` is `(29,81,54)`, strict `(2,2,2)`, and has a certified all-coordinate chamber with `U≥2`.

No CAD or global exclusion of either 29-vertex realization space is claimed.

## Immutable package

- Exact archive (`Vivid_Quartz_58_E29_HX2_exact_NONWINNER.zip`), SHA-256 `da4cfde285ea8ab90dd30c330385cbe8154f4c24211ff0c34e77e7aa04deae81`.
- SHA file (`Vivid_Quartz_58_E29_HX2_exact_NONWINNER.zip.sha256`), full 604-line report (`RESULT.md`), one-command replay (`[internal-source-reference].sh`), clean transcript (`CLEAN_VERIFICATION_TRANSCRIPT.txt`), and 49-entry manifest (`SHA256SUMS`).
- The replay ends `VIVID_QUARTZ_58_E29_HX2_FULL_REPLAY_PASS`; the ZIP passes a complete compressed-data test.

## 1. Literal requested cell `E29HX2L`

Keep every `E27AB2` coordinate fixed at denominator `2^20` and add

```text
RC=(21088,54869,-1324896)/2^20
RD=(19334,114290,-1739769)/2^20.
```

Replace

```text
[A,RA,RB] [Z1,RB,RA]
```

by

```text
[A,RA,RC] [RA,Z1,RC] [Z1,RD,RC]
[Z1,RB,RD] [RB,A,RD] [A,RC,RD].
```

Both disks have boundary `A-RA-Z1-RB-A` and Euler characteristic one. The target has true edge `(RC,RD)` and no edge `(RA,RB)`. The central tetrahedron `[A,Z1,RC,RD]` has exact positive volume

```text
4179244025449/1152921504606846976,
```

and the total added volume is `49464696454903/3458764513820540928`.

Exact mass:

```text
V  = 4519645748473025/3458764513820540928
Mx = 255124209876576797627/14507109835375550096474112
My = 1010947661607833346819/9671406556917033397649408
Mz = -15548683811556942834293/9671406556917033397649408
c  = (255124209876576797627/18956768241403402649600,
      3032842984823500040457/37913536482806805299200,
     -46646051434670828502879/37913536482806805299200).
```

The exact Fraction identities are `M=Vc`; centred first moments vanish. All 29 points are active, and the actual body is `(29,81,54)`, strict

```text
stable   [8,A,B], [8,A,RA], [8,RB,O1]
unstable 8, RB, RA
saddles  (8,A), (8,B), (10,RA), (Z1,RA).
```

The denominator-cleared arrow `RB→RD=36470535957682074821696127264>0`; therefore the literal incidence is not the requested anti-carrier cell. Minimum normalized mechanics separation is `0.0018173110752397563`; normalized nonincidence is `7.403587124119378e-7`.

Evidence: exact report (`E29HX2L_exact_report.json`), H rows (`E29HX2L_H_representation.json`), audit (`E29HX2L_audit.md`), patch (`E27AB2_to_E29HX2L_patch.json`).

## 2. Stronger same-size, star-changing connected cell

### `RC` page

```text
remove [8,RA,A] [A,RA,RB] [Z1,RB,RA]
add    [RC,A,8] [RC,8,RA] [RC,RB,A] [Z1,RB,RC] [Z1,RC,RA]
```

Exact positive volume increment:

```text
432035497620961/6917529027641081856.
```

### `RD` page

```text
remove [B,RB,8] [B,A,RB] [RC,RB,A]
add    [RD,8,B] [RD,RB,8] [RD,B,A] [RD,A,RC] [RD,RC,RB]
```

This page contains the first page’s face `[A,RB,RC]`, so the two operations communicate through a genuine 3-dimensional cell. Its exact positive increment is

```text
109799024003/6917529027641081856,
```

and final tetrahedron `[A,Z1,RC,RD]` has volume `89900487929333/2305843009213693952`. Edge `(RA,RB)` is deleted, `(RC,RD)` is created, and the stars of `(8,A)` and `(8,B)` both change.

At the exact lineage anchor

```text
RC=(41187,66119,-1330681)/2^20
RD=(-8,218662,-2537436)/2^20
```

the class is `(3,2,3)`:

```text
stable   [8,A,B], [8,RB,O1], [8,RA,RC]
unstable 8, RD
saddles  (8,A), (8,RD), (Z1,RA).
```

The desired arrow `RB→RD<0` is achieved, but `RD` is born unstable at activation.

Connected-patch certificate (`E27AB2_to_E29HX2A_connected_two_stage_patch.json`) · anchor report (`E29HX2A_exact_report.json`).

## 3. Complete exact declared-path chronology

Use

```text
RC(t)=RA+t(RC*-RA), RC*=(41187,66119,-1330681)/2^20,
RD(t)=RB+t(RD*-RB), RD*=(-8,218662,-2537436)/2^20,
0<t≤1.
```

The point coincides with the old vertex at `t=0`. Stage 1 expands 1,300 actual support predicates and 624 mechanics primitives; stage 2 expands 1,404 support predicates and 648 mechanics primitives. Exact Sturm isolation gives zero open support roots in both stages, so there are no unlisted hull changes.

All mechanics event groups, in exact order, are:

```text
stage 1
1  20324282/348745987 <t< 19241835/330172192 : RA→Z1 / H(Z1,RA), (3,2,3)->(3,3,4)
2  73656691/198484834 <t< 46905255/126396959 : RC→RA / H(RA,RC), no count change
3  96512173/186797540 <t< 52718321/102035343 : S[Z1,RC,RA] component 2 / H(Z1,RC), no count change
4  49857384/96451451 <t< 85834907/166051659 : S[Z1,RB,RC] component 1 / H(Z1,RC), no count change
5  74178824/108162733 <t< 109924085/160284146 : S[Z1,RB,RC] component 0 / H(RB,RC), no count change
6  120093724/159234489 <t< 133747325/177338051 : S[RC,8,RA] component 2 / H(8,RC), (3,3,4)->(4,3,5)
7  220612889/261347103 <t< 224794617/266300950 : S[RC,A,8] component 1 / H(8,RC), (4,3,5)->(3,3,4)
8  231392398/252923105 <t< 272185377/297511808 : RA→10 / H(10,RA), (3,3,4)->(3,2,3)
9  160076342/174542879 <t< 169994809/185357705 : RA→8 / H(8,RA), no count change
10 218510573/236712328 <t< 171626723/185923091 : S[RC,RB,A] component 2 / H(RB,RC), no count change
11 182875069/188430153 <t< 148127389/152626964 : A→RC / H(A,RC), no count change

stage 2
1  55270391/89937990 <t< 89580237/145768219 : S[RD,B,A] component 0 / H(A,B), no count change
2  89574703/145757075 <t< 118123945/192212758 : S[RD,B,A] component 1 / H(A,RD), no count change
3  88273792/98029315 <t< 156715051/174034317 : S[RD,8,B] component 2 / H(8,RD), (3,2,3)->(4,2,4)
4  250987259/278699441 <t< 81427704/90418357 : S[RD,8,B] component 0 / H(8,B), (4,2,4)->(3,2,3).
```

There are 12 stage-1 and 5 stage-2 strict cells; every cell has exact incidence, mass, and complete mechanics, and none is `(1,1,0)`.

The activation obstruction is explicit:

```text
RB→RD = t(10684872422803939 t²
           -83201998448356962015 t
           -14579595677510575479331662) < 0,
RD→RB = t(10684872422803939 t²
           +1243808836562875774225 t
           +4859865225836858493110554) > 0
```

for all `0<t≤1`. Thus the intended escape is present as soon as the new cell exists, but the replacement unstable vertex is also present immediately: death-before-birth fails exactly.

Full chronology with every exact cell (`E27AB2_to_E29HX2A_exact_chronology.json`) · escape-polynomial certificate (`E29HX2A_stage2_escape_polynomials.json`).

## 4. Promoted robust endpoint `E29HX2S`

This is a separate exact realization of the same labeled star-changing graph. No unproved coordinate homotopy from the lineage anchor is claimed.

### Complete V data

All 29 supplied points are active. With `D=65536`:

```text
8=(0,0,0)
10=(29670,-47959,-6443)
11=(15090,-24411,-3275)
A=(49871,-79888,-11079)
B=(35325,-52565,-9656)
C=(23566,-38183,-5201)
F=(21126,-34246,-4694)
L=(22320,-36127,-4855)
P=(15586,-25235,-3384)
T=(17503,-28351,-3805)
W=(19105,-30955,-4298)
X=(19768,-32034,-4315)
Y=(14812,-24007,-3331)
U=(13331,-21614,-2930)
V=(12331,-19994,-2748)
G=(27880,-45044,-6344)
H=(29786,-48230,-6583)
K=(30749,-49740,-6917)
J=(32022,-51730,-7255)
R=(37419,-60364,-8505)
S=(21354,-34582,-4823)
O1=(44314,-71130,-10263)
Z1=(51084,-82464,-11341)
Q3=(34901,-56485,-7750)
Z2=(47589,-76858,-10418)
RB=(35367,-52562,-9725)
RA=(52231,-84282,-11385)
RC=(52350,-84180,-11513)
RD=(35380,-52539,-9725)
```

The uncentred coordinates are these numerators divided by 65,536; the physical body is their convex hull translated by `-c`.

### Exact volume, moments, centroid

```text
V  = 141012326203/1688849860263936
Mx = 9442316934324439/221360928884514619392
My = -9941173153704349/147573952589676412928
Mz = -4463335902704429/442721857769029238784
cx = 9442316934324439/18482767620079616
cy = -29823519461113047/36965535240159232
cz = -4463335902704429/36965535240159232.
```

Direct rational identities prove `M_j=Vc_j`, hence centred first moments `(0,0,0)`.

### All 54 actual maximal faces

```text
[10,8,11] [10,RA,8] [11,8,P] [B,8,A] [A,8,RC] [B,RD,8]
[T,P,8] [T,8,X] [U,X,8] [V,8,Y] [Y,8,S] [V,U,8] [S,8,G]
[G,8,O1] [RB,O1,8] [RB,8,RD] [RA,RC,8] [10,11,P] [T,L,10]
[10,L,X] [T,10,P] [10,X,H] [10,H,Z2] [10,Z2,RA] [B,A,RD]
[A,RC,RD] [C,X,F] [C,F,H] [C,H,X] [W,F,Y] [W,S,F] [U,F,X]
[V,Y,F] [V,F,U] [F,Q3,H] [S,Q3,F] [T,X,L] [W,Y,S] [K,G,J]
[S,G,K] [R,J,G] [R,G,O1] [Z2,H,Q3] [R,K,J] [R,Q3,K] [S,K,Q3]
[R,O1,Z1] [R,Z1,Q3] [Z1,O1,RB] [Z2,Q3,Z1] [Z2,Z1,RA]
[Z1,RB,RC] [Z1,RC,RA] [RB,RD,RC].
```

### All 81 true edges

```text
(8,10) (8,11) (8,A) (8,B) (8,P) (8,T) (8,X) (8,Y) (8,U) (8,V)
(8,G) (8,S) (8,O1) (8,RB) (8,RA) (8,RC) (8,RD)
(10,11) (10,L) (10,P) (10,T) (10,X) (10,H) (10,Z2) (10,RA) (11,P)
(A,B) (A,RC) (A,RD) (B,RD) (C,F) (C,X) (C,H)
(F,W) (F,X) (F,Y) (F,U) (F,V) (F,H) (F,S) (F,Q3)
(L,T) (L,X) (P,T) (T,X) (W,Y) (W,S) (X,U) (X,H) (Y,V) (Y,S)
(U,V) (G,K) (G,J) (G,R) (G,S) (G,O1) (H,Q3) (H,Z2)
(K,J) (K,R) (K,S) (K,Q3) (J,R) (R,O1) (R,Z1) (R,Q3) (S,Q3)
(O1,Z1) (O1,RB) (Z1,Q3) (Z1,Z2) (Z1,RB) (Z1,RA) (Z1,RC)
(Q3,Z2) (Z2,RA) (RB,RC) (RB,RD) (RA,RC) (RC,RD).
```

Thus `(V,E,F)=(29,81,54)`, each true edge has two incident faces, and Euler is two.

### Deterministic exact H representation

For every oriented face `(i,j,k)`, let

```text
n=primitive((Q_j-Q_i)×(Q_k-Q_i)), h=n·Q_i.
```

Then the uncentred row is `n·p≤h/65536`, and the centred row is

```text
n·x≤h/65536-n·c.
```

The V table and oriented face list above therefore regenerate all exact H rows without hidden data. The expanded 54-row H table and every nonincident slack (`E29HX2S_H_representation.json`) are supplied. Every row is irredundant. Minimum primitive-integer nonincident slack is `96401`; Euclidean separation is `3.1722305851075076e-5`; circumradius-normalized separation is `3.295687931356116e-5`.

## 5. Exhaustive own-centroid mechanics

The exact class is

```text
stable   [8,A,B], [8,RB,O1]
unstable 8, RA
saddles  (8,RD), (10,RA)
class    (2,2,2).
```

Positive normalized component vectors are

```text
S[8,A,B]   = (0.21981488407629934, 0.2633303265674424, 0.5168547893562583)
S[8,RB,O1] = (0.17128358307349373, 0.6172185856458381, 0.21149783128066815)
U8 minimum = 0.999257981532728
U_RA       = (0.999670226833855,0.9996381368258305,0.996949007470422,
              0.9996723795070566,0.0709972713670833)
H(8,RD)    = (0.9836294038867651,0.016370596113234877,
              1.1231411354553593,1.4437957982857927)
H(10,RA)   = (0.14667606223171065,0.8533239377682894,
              0.3277107304835722,0.9806036553300208).
```

Every other face, vertex, and true edge has an exact negative component witness. The minimum absolute signed normalized separation across the full 54-face, 29-vertex, and 81-edge ledger is `0.016370596113234877`. Face tests use all projection barycentrics; vertex tests use every actual-neighbour arrow `-x_i·(x_j-x_i)`; edge tests use `t`, `1-t`, and both coefficients of the foot in the cone generated by the two incident outward normals. Exact complete report (`E29HX2S_exact_report.json`) and human-readable exhaustive audit (`E29HX2S_audit.md`) contain every exact component.

## 6. Exact escape and residual forcing theorem

```text
RB→RD = -17880350366730807/2422573317499075428352 < 0
RD→RC = -14031559942680197149/2422573317499075428352 < 0
RC→RA = -147985411260167/1305265796066312192 < 0.
```

So `RB,RD,RC` are non-unstable along `RB→RD→RC→RA`. The chain terminates at `RA`. Every arrow at `8` and every arrow at `RA` is strictly positive at the endpoint and throughout the certified box. Their true-edge identity is

```text
u(8→RA)+u(RA→8)=|RA-8|²=4980575555/2147483648>0.
```

Therefore `8` and `RA` remain unstable on the complete certified chamber, including mechanics walls: `U≥2`. This is a local theorem, not a global graph theorem. Exact arrow and forcing ledger (`E29HX2S_residual_forcing_certificate.json`).

## 7. Open chamber, moment controls, and independent replay

Exact outward Fraction interval arithmetic permits every one of the 87 uncentred coordinate entries to vary independently by

```text
ε=1/70368744177664=2^-46.
```

For every box member the verifier reconstructs the same `(29,81,54)` incidence, recomputes volume and all three moments, substitutes the dependent own centroid, preserves all active signs, and preserves an exact negative witness for every inactive feature. The minimum exact support-interval lower bound is

```text
111142540853976340861843/40564819207303340847894502572032.
```

A three-dimensional physical family remains after moment elimination. Lift to denominator `2^51` and vary

```text
RC.x += a/2^51,
RD.y += b/2^51,
RA.z += c/2^51,
(a,b,c)∈[-1,1]^3.
```

These directions have rank three modulo translation and scale. With exact boundary sums `V6,N_j`,

```text
V=V6/(6D³), M_j=N_j/(24D⁴), c_j=N_j/(4DV6), M_j=Vc_j,
d(M-Vc)/dc=-V I₃, det=-V³<0.
```

Thus the three moments determine a unique dependent centroid. The full cube lies inside the certified chamber, and an independent `5×5×5` grid reconstructs all 125 bodies as `(2,2,2)`.

A separately coded SciPy/Qhull–tetrahedral-moment–full-normal-cone verifier reconstructs all 29 vertices, 54 faces, 81 edges, the exact-label equilibrium set, and watertight winding-consistent Euler-two meshes.

- Perturbation certificate (`E29HX2S_perturbation_certificate.json`)
- Three-control family (`E29HX2S_three_control_family.json`)
- Independent family replay (`E29HX2S_three_control_independent_verification.json`)
- Independent endpoint report (`E29HX2S_independent_verification.json`)
- Centred OBJ (`E29HX2S_centered.obj`)
- Centred STL (`E29HX2S_centered.stl`)

## 8. Search scope and next exact frontier

Discovery moved all old and new coordinates, rebuilt actual hulls, recomputed the uniform-volume centroid, and evaluated complete normal cones. It included SPD/projective metrics, unrestricted full-coordinate smooth-max searches, topology-aware support barriers, and local LP/MILP common-descent tests. No strict own-centred winner was found. These are empirical receipts only; exact claims are restricted to the displayed literal cell, connected two-stage path, robust endpoint, `2^-46` box, and three-control cube.

The first nonserial whole-packet successor is `E30-BELT2`. Remove the 18-face disk

```text
[RB,O1,8] [RB,8,RD] [B,RD,8] [10,RA,8] [10,Z2,RA] [Z2,Z1,RA]
[Z1,RC,RA] [RA,RC,8] [10,8,11] [11,8,P] [T,P,8] [T,8,X]
[U,X,8] [V,U,8] [V,8,Y] [Y,8,S] [S,8,G] [G,8,O1]
```

with boundary

```text
8-B-RD-RB-O1-G-S-Y-V-U-X-T-P-11-10-Z2-Z1-RC
```

and replace it by

```text
[RE,8,B] [RE,B,RD] [RE,RD,RB] [RE,RB,O1]
[RF,O1,G] [RF,G,S] [RF,S,Y] [RF,Y,V] [RF,V,U] [RF,U,X]
[RF,X,T] [RF,T,P] [RF,P,11] [RF,11,10] [RF,10,Z2] [RF,Z2,Z1]
[RF,Z1,RC] [RF,RC,8] [8,RE,RF] [O1,RF,RE].
```

The exact sphere architecture has `(V,E,F)=(30,84,56)`, true shared edge `(RE,RF)`, all edges degree two, connected dual, and preserved `[8,A,B]`; `RA` occurs only in the removed disk and becomes inactive. It contains the whole residual stable/unstable/saddle packet in one event. It is **combinatorially exact but not geometrically realized**. A fixed-coordinate sequential visibility LP was infeasible, which is search failure at that metric, not a nonrealizability proof. Exact topology certificate (`next_open_topology.json`).

## Exact claim boundary

**Proved:** literal E29-HX2 realizability; exact positive-volume connected star-changing refinement; complete 15-event/17-cell declared chronology with zero winners; exact robust `E29HX2S` V/H/E and mass; exhaustive own-centroid mechanics; strict negative carrier chain; local `U≥2`; `2^-46` all-coordinate chamber; rank-three post-moment family; independent reconstruction and meshes; exact E30-BELT2 sphere combinatorics.

**Not proved:** global exclusion of either 29-vertex graph, global minimum vertex count, nonrealizability of E30-BELT2, or any conclusion from numerical near-walls beyond discovery evidence.

## Reusable conclusion

The literal `E29-HX2` disk exists but is structurally insufficient. The smallest stronger same-size topology changes both old carrier stars and gives `RB` its requested strict negative escape, yet exact chronology proves immediate unstable transfer. Robust `E29HX2S` relays the terminal maximum to `RA` and is a completely audited exact own-centred `(29,81,54)` nonwinner of class `(2,2,2)`. The complete real 29-vertex realization spaces remain open; `E30-BELT2` is the first whole-packet topology outside the certified chamber.
