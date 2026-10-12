# figure-0282

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Vivid Quartz 58 — full-coordinate `E25D` frontier and connected two-support successor

## Literal disposition

**EXACT MATERIALIZED NONWINNER.** I did not obtain a homogeneous convex polyhedral Gömböc. The exact finite successor constructed here is `E27AB2`, with `(V,E,F)=(27,75,50)` and strict own-centred `(S,U,H)=(3,2,3)`.

The important structural advance is genuine. Starting from an exact full-dimensional realization `E25S` of the same 25-vertex graph as authoritative `E25D`, the construction makes both inherited extra unstable vertices `A` and `B` non-unstable, removes both inherited extra stable faces `[10,Z2,A]` and `[R,Z1,Q3]`, removes inherited saddles `[10,Z2]` and `[A,B]`, and then activates two interacting extreme supports `RA,RB` in one connected positive-volume disk. The packet nevertheless transfers: `RB` becomes the additional unstable vertex, new stable faces `[8,RA,A]` and `[8,RB,O1]` become strict, and saddles `[8,A]`, `[8,B]`, `[10,RA]` remain.

The complete continuous realization space of the `E25D` graph is **not** globally excluded. The work covers unrestricted full-coordinate numerical discovery with actual-hull recomputation, exactifies a new same-graph open cell, and proves complete exact endpoint, path, and local-chamber theorems. It does not constitute CAD, quantifier elimination, or a proof over every real realization.

## Immutable artifacts

- [Complete exact archive](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER.zip)
- [Archive SHA-256 file](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER.zip.sha256)
- [Full determination](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/RESULT.md)
- [One-command replay](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/[internal-source-reference].sh)
- [Clean replay transcript](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/CLEAN_VERIFICATION_TRANSCRIPT.txt)
- [Verification record](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/VERIFICATION_RECORD.json)
- [Checksummed manifest](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/SHA256SUMS)

The final replay terminates with `VIVID_QUARTZ_58_E25D_FRONTIER_FULL_REPLAY_PASS`, and the ZIP passes a complete compressed-data integrity test.

## 1. Authoritative source and lineage

The sole source authority is immutable parent `figure-0265`, SHA-256

```text
c22e86c375499e8a84f828b5669b43a13b7bcb698a4d39716a3714eaff92bc78.
```

The retired corrupted `(3,4,5)` alias is not used. The durable journal identifies the valid parent, its exact `E26DO2`, the carrier-breaking `E26F19`, and the 25-vertex `E25D` frontier. :contentReference[oaicite:0]{index=0} The immutable parent payload states that deleting `P2` from `E26F19` yields exact `E25D`, `(25,69,46)`, strict `(3,3,4)`, with stable faces `[8,A,B]`, `[10,Z2,A]`, `[R,Z1,Q3]`, unstable vertices `8,A,B`, and saddles `[8,A]`, `[8,B]`, `[10,Z2]`, `[A,B]`. :contentReference[oaicite:1]{index=1} Parent identity and package lineage are preserved separately from all new artifacts. :contentReference[oaicite:2]{index=2}

The authoritative `E25D` label set is

```text
8,10,11,A,B,C,F,L,P,T,W,X,Y,U,V,G,H,K,J,R,S,O1,Z1,Q3,Z2.
```

The label map into `E25S` is the identity on all 25 labels. No relabelling or alias substitution occurs.

Exact source mass data are

```text
V = 8084284506738335804997/2305843009213693952

c_x = 103421218126044157440483141275/25430960132812971615181602816
c_y = 13106154311558412721146150389/3178870016601621451897700352
c_z = -506818269917057987428517683309/9247621866477444223702401024.
```

The exact first moments are `M_j=V c_j`; after translation by `c`, all three centred moments are zero. The complete imported V table, 46 maximal faces, 69 true edges, irredundant H rows, full-cone mechanics, and the original `2^-22` chamber are preserved in:

- [E25D exact specification](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/source_E25D/E25D_spec.json)
- [E25D exact report](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/source_E25D/E25D_exact_report.json)
- [E25D H representation](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/source_E25D/E25D_H_representation.json)
- [E25D exhaustive audit](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/source_E25D/E25D_audit.md)

## 2. Exact reconstruction conventions

For every promoted endpoint, uncentred vertices are `p_i=Q_i/D`, where the integer numerators `Q_i` and common denominator `D` are displayed below. The physical body is

```text
P = conv{Q_i/D-c},
```

where `c` is its exact ordinary-volume centroid.

For an outward-oriented triangular boundary face `(i,j,k)`, define

```text
w_f = det(Q_i,Q_j,Q_k),
V   = sum_f w_f/(6D^3),
M   = sum_f w_f(Q_i+Q_j+Q_k)/(24D^4),
c   = M/V.
```

The exact verifiers prove `M=Vc`, so the translated first moments vanish identically.

The deterministic H row is

```text
n = primitive((Q_j-Q_i) x (Q_k-Q_i)),
h = n·Q_i,
n·x <= h/D-n·c.
```

Every nonincident point is tested with exact rational slack. Strict support of all nonincident vertices proves boundedness, convexity, maximal-face irredundancy, and the actual incidence lattice.

Mechanics are evaluated only at the own centroid:

- A maximal face is stable exactly when the orthogonal projection of the origin has all positive polygon or triangle barycentric components.
- A vertex `i` is unstable exactly when `-x_i·(x_j-x_i)>0` for every actual neighbour `j`.
- For true edge `(u,v)`, let `d=x_v-x_u`, `t=-x_u·d/||d||²`, and let the edge-foot vector be expressed in the cone of the two incident outward normals. The edge is a saddle exactly when `t`, `1-t`, and both normal-cone coefficients are strictly positive. The exact implementation clears the Gram determinant and records all four signs.

Thus the supplied coordinates and oriented faces deterministically regenerate every H row, moment, true edge, and equilibrium component.

## 3. Exact same-graph realization `E25S`

`E25S` is a new full-dimensional exact cell of the **same complete graph** as `E25D`. It was found by allowing all vertex coordinates to move, rebuilding the actual hull, and recomputing the ordinary-volume centroid. No exact coordinate homotopy from the parent point to `E25S` is claimed.

### 3.1 V representation

Use

```text
D = 2^20 = 1048576.
```

The uncentred integer numerators are

```text
8   = (0,0,0)
10  = (2786,22819,-735018)
11  = (1413,11626,-374189)
A   = (51627,75998,-1314640)
B   = (0,218637,-2537126)
C   = (2089,20362,-604914)
F   = (1823,19271,-551634)
L   = (2059,17663,-557902)
P   = (1454,12057,-387114)
T   = (1615,13785,-437081)
W   = (1616,18483,-508232)
X   = (1776,16384,-501174)
Y   = (1254,14206,-392996)
U   = (1165,11740,-344329)
V   = (1061,11304,-322541)
G   = (2191,34253,-805424)
H   = (2669,25431,-761500)
K   = (2516,34022,-855250)
J   = (2581,37151,-905442)
R   = (3035,43176,-1055217)
S   = (1772,21971,-579632)
O1  = (3242,69197,-1407259)
Z1  = (4674,50873,-1367156)
Q3  = (3004,33562,-925756)
Z2  = (4537,40186,-1209587).
```

All 25 supplied points are active.

### 3.2 Exact volume, moments, and centroid

```text
V = 8819901870710275/6917529027641081856

M_x = 494611993692210360983/29014219670751100192948224
M_y = 989295682375959540875/9671406556917033397649408
M_z = -1892013228435820589629/1208925819614629174706176

c_x = 494611993692210360983/36993349695927589273600
c_y = 118715481885115144905/1479733987837103570944
c_z = -5676039685307461768887/4624168711990948659200.
```

Direct Fraction identities prove `M_j=V c_j` for all three coordinates.

### 3.3 All maximal faces

```text
[8,11,10] [8,10,A] [8,P,11] [8,A,B] [8,B,O1]
[8,T,P] [8,X,T] [8,U,X] [8,Y,V] [8,S,Y]
[8,V,U] [8,G,S] [8,O1,G]
[10,11,P] [10,Z2,A] [10,T,L] [10,L,X] [10,P,T]
[10,X,H] [10,H,Z2]
[A,Z1,B] [A,Z2,Z1] [B,Z1,O1]
[C,X,F] [C,F,H] [C,H,X]
[F,Y,W] [F,W,S] [F,X,U] [F,V,Y] [F,U,V]
[F,Q3,H] [F,S,Q3] [L,T,X] [W,Y,S]
[G,J,K] [G,K,S] [G,R,J] [G,O1,R]
[H,Q3,Z2]
[K,J,R] [K,R,Q3] [K,Q3,S]
[R,O1,Z1] [R,Z1,Q3] [Z1,Z2,Q3].
```

### 3.4 Every true edge

```text
(8,10) (8,11) (8,A) (8,B) (8,G) (8,O1) (8,P)
(8,S) (8,T) (8,U) (8,V) (8,X) (8,Y)

(10,11) (10,A) (10,H) (10,L) (10,P) (10,T) (10,X) (10,Z2)
(11,P)

(A,B) (A,Z1) (A,Z2)
(B,O1) (B,Z1)

(C,F) (C,H) (C,X)

(F,H) (F,Q3) (F,S) (F,U) (F,V) (F,W) (F,X) (F,Y)

(L,T) (L,X) (P,T) (T,X)
(W,S) (W,Y)
(X,H) (X,U)
(Y,S) (Y,V)
(U,V)

(G,J) (G,K) (G,O1) (G,R) (G,S)
(H,Q3) (H,Z2)
(K,J) (K,Q3) (K,R) (K,S)
(J,R)
(R,O1) (R,Q3) (R,Z1)
(S,Q3)
(O1,Z1)
(Z1,Q3) (Z1,Z2)
(Q3,Z2).
```

Hence `(V,E,F)=(25,69,46)` and `25-69+46=2`.

### 3.5 Exhaustive mechanics

```text
stable faces      [8,A,B], [8,B,O1], [A,Z2,Z1]
unstable vertices 8, B
saddle edges      (8,A), (8,B), (Z1,Z2)
class             (3,2,3).
```

Relative to parent `E25D`:

- `A` is no longer unstable.
- Source extra stable faces `[10,Z2,A]` and `[R,Z1,Q3]` are inactive.
- Source saddles `[10,Z2]` and `[A,B]` are inactive.
- Replacement stable faces `[8,B,O1]`, `[A,Z2,Z1]` and saddle `[Z1,Z2]` are born.
- `B` remains the additional unstable vertex, while `[8,A]` and `[8,B]` remain saddles.

The smallest absolute normalized face, vertex, or edge component is

```text
0.007707777886926225.
```

The minimum circumradius-normalized nonincidence separation is

```text
1.1704272469614726e-06.
```

Exact outward interval arithmetic permits all 75 uncentred coordinate entries to vary independently by

```text
2^-31
```

while recomputing the dependent centroid and preserving the complete graph and strict `(3,2,3)` classification.

All arrows at `8` and `B` remain positive in this box. In particular,

```text
u(8->B)+u(B->8)=|B-8|²
              =6484810477645/1099511627776 > 0.
```

Thus `8` and `B` are independently strict unstable vertices throughout the certified chamber, so `U>=2` there.

Evidence:

- [E25S exact report](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E25S/E25S_exact_report.json)
- [E25S H representation](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E25S/E25S_H_representation.json)
- [E25S exhaustive audit](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E25S/E25S_audit.md)
- [E25S perturbation certificate](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E25S/E25S_perturbation_certificate.json)
- [E25S independent report](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E25S/E25S_independent_verification.json)
- [E25S independent verifier](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E25S/verify_E25S_independent.py)
- [E25S OBJ](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E25S/E25S_centered.obj)
- [E25S STL](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E25S/E25S_centered.stl)

## 4. Connected two-support replacement `E25S -> E27AB2`

The exact construction inserts supports `RA,RB` into one connected disk containing both inherited `A/B` carrier stars.

The common outer boundary is

```text
8-10-Z2-Z1-O1-8.
```

The source disk is

```text
[8,A,B]
[8,10,A] [8,B,O1]
[10,Z2,A]
[A,Z1,B] [A,Z2,Z1]
[B,Z1,O1].
```

Its disk f-vector is `(7,13,7)`.

The target disk is

```text
[8,A,B]
[8,10,RA] [8,RA,A]
[8,B,RB] [8,RB,O1]
[10,Z2,RA]
[A,RB,B] [A,RA,RB]
[O1,RB,Z1]
[Z1,RB,RA] [Z1,RA,Z2].
```

Its disk f-vector is `(9,19,11)`. Both disks have Euler characteristic one and exactly the same boundary-edge set. The target has true shared edge `(RA,RB)`.

The source-minus-target shell is a closed oriented two-sphere, and the exact signed added volume is

```text
120460233325969/6917529027641081856 > 0.
```

The interior tetrahedron with vertices `A,Z1,RA,RB` has exact positive volume

```text
522918716317/3458764513820540928 > 0.
```

Thus the operation is a genuine finite-thickness communicating two-support cell, not a coincident subdivision or a serial surface relay.

[Exact incidence and positive-volume certificate](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E25S_to_E27AB2_connected_patch.json)

## 5. Exact activation path and circuit chronology

Keep all 25 old vertices fixed. At `t=0`, put

```text
RA(0)=(8+10+A)/3,
RB(0)=(8+B+O1)/3.
```

These points lie in source faces and are inactive. Define

```text
RA(t)=RA(0)+t(RA(1)-RA(0)),
RB(t)=RB(0)+t(RB(1)-RB(0)),
0<=t<=1,
```

where `RA(1),RB(1)` are the endpoint coordinates below.

For every exact `t>0`, both supports are extreme. At `t=0+` the two source triangles undergo simultaneous stellar activation:

```text
[8,10,A] -> [8,10,RA] [8,RA,A] [10,A,RA]
[8,B,O1] -> [8,B,RB] [8,RB,O1] [B,O1,RB].
```

The first strict cell immediately to the right of `t=0` already has

```text
class       (2,3,3)
stable      [8,A,B], [A,Z2,Z1]
unstable    8, B, RB
saddles     (8,A), (8,B), (Z1,Z2).
```

Therefore replacement unstable `RB` is born before source unstable `B` dies. Death-before-birth already fails at the activation event.

The path then crosses exactly five actual hull circuits:

1. At

```text
t1=13076107129159/43029786254971
  ≈0.3038850123883287,
```

circuit `[10,A,RA,Z2]` replaces diagonal `(10,A)` by `(Z2,RA)`.

2. At

```text
t2=88300441598063/114322650974777
  ≈0.7723792340814833,
```

circuit `[A,Z2,RA,Z1]` replaces `(A,Z2)` by `(Z1,RA)`.

3. At

```text
t3=33448198981003/34010465056957
  ≈0.9834678509978508,
```

circuit `[B,O1,RB,Z1]` replaces `(B,O1)` by `(Z1,RB)`.

4. At

```text
t4=1132788604240337/1133182671960671
  ≈0.9996522469588666,
```

circuit `[B,Z1,A,RB]` replaces `(B,Z1)` by `(A,RB)`.

5. At the positive root

```text
t5 = 9710631298594751/47204146364587700
   + 3*sqrt(156097227829495010160211609742689)
     /47204146364587700
   ≈0.9997489159171192,
```

of

```text
23602073182293850 t²
-9710631298594751 t
-13882029346805393=0,
```

circuit `[A,Z1,RA,RB]` replaces `(A,Z1)` by `(RA,RB)`. An exact isolator is

```text
938753431779910/938989197021279
< t5 <
1747324335593629/1747763171106539.
```

Every actual nonincidence predicate, all face components, all actual-neighbour vertex arrows, and all four components of every true-edge cone were expanded on each of the six open incidence regions. This gives

```text
3600 exact mechanics polynomials,
58 distinct mechanics-root groups,
64 strict mechanics cells,
0 winner cells.
```

The exact class distribution is

```text
(1,2,1):  4 cells
(2,2,2):  6 cells
(2,3,3): 14 cells
(3,2,3):  9 cells
(3,3,4): 14 cells
(4,2,4):  9 cells
(4,3,5):  8 cells.
```

Every cell satisfies `S+U-H=2`; none is `(1,1,0)`. Each root record stores its primitive exact polynomial and a rational isolating interval, and every cell stores its actual maximal faces, true edges, exact mass data, and complete equilibrium labels.

- [Complete exact event atlas](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E25S_to_E27AB2_exact_event_atlas.json)
- [Condensed chronology](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E25S_to_E27AB2_chronology_summary.json)
- [Independent atlas verifier](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/verify_event_atlas.py)

## 6. Exact endpoint `E27AB2`

### 6.1 V representation

Use the same denominator

```text
D=2^20=1048576.
```

The 25 inherited numerators are exactly those of `E25S`, and

```text
RB=(-22,218603,-2537130)
RA=(5240,40339,-1292513).
```

All 27 supplied vertices are active.

### 6.2 Exact volume, moments, and centroid

```text
V = 2235090526009061/1729382256910270464

M_x = 2615586443686642921/151115727451828646838272
M_y = 2992450637507899282165/29014219670751100192948224
M_z = -45994986499737517648421/29014219670751100192948224

c_x = 7846759331059928763/585915570850119286784
c_y = 2992450637507899282165/37498596534407634354176
c_z = -45994986499737517648421/37498596534407634354176.
```

Again, `M_j=V c_j` exactly and the translated first moments vanish.

### 6.3 All maximal faces

```text
[8,11,10] [8,10,RA] [8,P,11] [8,A,B] [8,RA,A]
[8,B,RB] [8,T,P] [8,X,T] [8,U,X] [8,Y,V]
[8,S,Y] [8,V,U] [8,G,S] [8,O1,G] [8,RB,O1]

[10,11,P] [10,T,L] [10,L,X] [10,P,T] [10,X,H]
[10,H,Z2] [10,Z2,RA]

[A,RB,B] [A,RA,RB]

[C,X,F] [C,F,H] [C,H,X]

[F,Y,W] [F,W,S] [F,X,U] [F,V,Y] [F,U,V]
[F,Q3,H] [F,S,Q3]

[L,T,X] [W,Y,S]

[G,J,K] [G,K,S] [G,R,J] [G,O1,R]
[H,Q3,Z2]
[K,J,R] [K,R,Q3] [K,Q3,S]
[R,O1,Z1] [R,Z1,Q3]
[O1,RB,Z1]
[Z1,Z2,Q3] [Z1,RA,Z2] [Z1,RB,RA].
```

### 6.4 Every true edge

```text
(8,10) (8,11) (8,A) (8,B) (8,G) (8,O1) (8,P)
(8,RA) (8,RB) (8,S) (8,T) (8,U) (8,V) (8,X) (8,Y)

(10,11) (10,H) (10,L) (10,P) (10,RA) (10,T) (10,X) (10,Z2)
(11,P)

(A,B) (A,RA) (A,RB)
(B,RB)

(C,F) (C,H) (C,X)

(F,H) (F,Q3) (F,S) (F,U) (F,V) (F,W) (F,X) (F,Y)

(L,T) (L,X) (P,T) (T,X)
(W,S) (W,Y)
(X,H) (X,U)
(Y,S) (Y,V)
(U,V)

(G,J) (G,K) (G,O1) (G,R) (G,S)
(H,Q3) (H,Z2)
(K,J) (K,Q3) (K,R) (K,S)
(J,R)
(R,O1) (R,Q3) (R,Z1)
(S,Q3)
(O1,RB) (O1,Z1)
(Z1,Q3) (Z1,RA) (Z1,RB) (Z1,Z2)
(Q3,Z2)
(Z2,RA)
(RA,RB).
```

Therefore `(V,E,F)=(27,75,50)` and `27-75+50=2`.

### 6.5 Exhaustive mechanics

```text
stable faces      [8,A,B], [8,RA,A], [8,RB,O1]
unstable vertices 8, RB
saddle edges      (8,A), (8,B), (10,RA)
class             (3,2,3).
```

Both inherited extra unstable vertices have been eliminated:

```text
A is non-unstable,
B is non-unstable.
```

The original extra stable faces `[10,Z2,A]` and `[R,Z1,Q3]` are inactive. Original saddles `(10,Z2)` and `(A,B)` are inactive. The remaining packet is genuinely new rather than a relabelling of those features.

Useful positive normalized margins are

```text
S[8,RA,A]   >= 0.0132292046245516
S[8,RB,O1]  >= 0.0152663989852823
U(RB)       >= 0.0138382635607145
H(8,A)      >= 0.0190547144478046
H(8,B)      >= 0.0117808414055588
H(10,RA)    >= 0.0088720322360365.
```

The minimum absolute signed normalized component over **every** active and inactive face, vertex, and true edge is

```text
0.00023225272903076857.
```

The minimum circumradius-normalized nonincidence separation is

```text
7.567244140139231e-07.
```

Exact interval arithmetic permits all 81 uncentred coordinate entries to vary independently by

```text
2^-31
```

while preserving all 50 maximal faces, 75 true edges, exact positive volume, and strict `(3,2,3)` after dependent centroid recomputation.

A separately coded Qhull/tetrahedral-moment/full-normal-cone implementation reconstructs the same actual hull, centroid, and equilibrium labels. Both display meshes are watertight, winding-consistent, and Euler two.

- [E27AB2 exact report](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E27AB2/E27AB2_exact_report.json)
- [E27AB2 H representation](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E27AB2/E27AB2_H_representation.json)
- [E27AB2 exhaustive audit](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E27AB2/E27AB2_audit.md)
- [E27AB2 perturbation certificate](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E27AB2/E27AB2_perturbation_certificate.json)
- [E27AB2 independent report](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E27AB2/E27AB2_independent_verification.json)
- [E27AB2 independent verifier](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E27AB2/verify_E27AB2_independent.py)
- [E27AB2 OBJ](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E27AB2/E27AB2_centered.obj)
- [E27AB2 STL](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E27AB2/E27AB2_centered.stl)

## 7. Exact residual forcing component

Every actual-neighbour arrow at `RB` is strictly positive at the endpoint and remains interval-positive throughout the entire `2^-31` coordinate box. Every actual-neighbour arrow at protected vertex `8` is independently interval-positive in the same box.

The true edge `(8,RB)` satisfies

```text
u(8->RB)+u(RB->8)
 = |RB-8|²
 = 6484815908993/1099511627776
 > 0.
```

Consequently `8` and `RB` are both strict unstable vertices throughout the complete certified chamber, including all internal mechanics walls:

```text
U>=2.
```

This is the precise local obstruction. It is not extrapolated to every realization of the 27-vertex graph.

## 8. Positive-dimensional moment-eliminated family

Lift all endpoint numerators to denominator

```text
D_f=2^33
```

by multiplying them by `8192`. For independent parameters `(a,b,c) in [-1,1]^3`, vary

```text
Q_RA.x += a
Q_RB.y += b
Q_Z1.z += c.
```

The physical amplitudes are at most `2^-33`, strictly within the exact `2^-31` chamber. These three sparse deformation directions have rank three modulo common translation and uniform scale.

For each shape, write the exact boundary sums as `V6(a,b,c)` and `N_j(a,b,c)`. Then

```text
V   = V6/(6D_f^3),
M_j = N_j/(24D_f^4),
c_j = N_j/(4D_f V6).
```

Thus `M_j=Vc_j` identically. Equivalently, for `G(c)=M-Vc`,

```text
dG/dc = -V I_3,
det(dG/dc)=-V^3<0,
```

so the three moment equations have a unique dependent centroid throughout the family. Exact interval containment preserves the complete incidence and `(3,2,3)` classification; an independent `5x5x5` grid reconstructs all 125 members.

- [Exact three-control family](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/E27AB2_three_control_family.json)
- [Independent family verifier](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/verify_family.py)

## 9. Search coverage and uncertainty

The constructive search did not remain in the inherited `2^-22` box or restrict itself to an affine metric orbit. It used unrestricted old-vertex coordinates modulo translation and scale, rebuilt the actual convex hull after accepted changes, integrated the ordinary-volume centroid, and audited full normal cones.

Work performed included:

- the parent’s 112,575-state full-coordinate `E25D` continuation;
- same-graph full-coordinate search that produced exact `E25S`;
- dynamic actual-incidence sequential linearization from `E25S`;
- full nonlinear constrained searches attempting simultaneous non-instability of `A,B` and death of all extra stable/saddle sheets;
- projective and metric recharting with actual-hull checks;
- auxiliary-centre continuation followed by explicit continuation toward the ordinary-volume centroid;
- connected two-support searches that produced `E27AB2`;
- post-endpoint dynamic searches and small exact deletion checks.

One auxiliary-centre construction reached a relative-centre `(2,1,1)` state, but continuation toward the true volume centroid failed at a collapsing support wall near continuation parameter `0.0517`. It is not accepted or promoted.

No strict own-centred `(1,1,0)` state was found. These searches are empirical discovery evidence, not a theorem over the full semialgebraic realization space. Exact claims are limited to `E25S`, `E27AB2`, their displayed chambers, and the complete declared connecting path.

[Search ledger](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/search_ledger.json)

## 10. First genuinely nonrepeating successor

The smallest rigorous continuous frontier remains the full real realization space of the 25-vertex `E25D` graph outside the exact `E25D` and `E25S` chambers. No global graph-theoretic obstruction has been proved there.

For a distinct incidence change beyond `E27AB2`, the first explicit nonserial carrier-breaking topology is `E29-HX2`. Replace the two-triangle local disk

```text
[A,RA,RB]
[Z1,RB,RA]
```

with a six-triangle finite-thickness disk using new supports `RC,RD`:

```text
[A,RA,RC]
[RA,Z1,RC]
[Z1,RD,RC]
[Z1,RB,RD]
[RB,A,RD]
[A,RC,RD].
```

The common boundary is

```text
A-RA-Z1-RB-A.
```

The new cell removes true edge `(RA,RB)`, inserts true shared edge `(RC,RD)`, and has all-active global simplicial counts

```text
(V,E,F)=(29,81,54).
```

It is combinatorially verified but not geometrically realized in this handoff. A valid realization must prospectively impose

```text
RB->RD < 0
```

or another strict negative external escape from `RB`, preserve `[8,A,B]` and unstable `8`, and prevent every new internal edge from becoming an all-external-positive carrier. The stars of `(8,A)` and `(8,B)` must change in the same finite event; otherwise the construction merely repeats the exact transfer documented above. Three ordinary-volume moment variables must remain dependent after reserving at least three independent physical shape controls.

[Exact next-topology specification](sandbox:/mnt/data/Vivid_Quartz_58_E25D_full_realization_frontier_NONWINNER/next_open_topology.json)

## 11. Exact claim boundary

### Proved

1. The authoritative parent lineage and exact `E25D` source are reconstructed without using the retired alias.
2. `E25S` is an exact, full-dimensional, same-graph realization outside the inherited local endpoint claim. It makes `A` non-unstable and exactly removes several inherited stable and saddle features.
3. `E25S` has complete V/H/E data, exact own-centroid mass closure, exhaustive full-cone mechanics, an all-coordinate `2^-31` chamber, independent replay, and watertight meshes.
4. `E25S -> E27AB2` is a genuine connected positive-volume two-support event with a common boundary disk and true shared edge `(RA,RB)`.
5. The exact connecting path has one simultaneous activation, five actual circuit flips, 58 mechanics-root groups, and 64 fully audited strict cells; none is `(1,1,0)`.
6. `E27AB2` makes both source carrier vertices `A,B` non-unstable and removes the two original extra stable faces plus saddles `(10,Z2)` and `(A,B)`.
7. `E27AB2` is exact own-centred `(27,75,50)`, strict `(3,2,3)`, with complete V/H/E and mechanics, an all-coordinate `2^-31` chamber, independent replay, and watertight meshes.
8. Protected `8` and replacement `RB` force `U>=2` throughout the certified `E27AB2` chamber.
9. A genuine three-dimensional physical shape family remains after dependent exact elimination of all three moments.

### Not proved

- The full continuous realization space of the `E25D` graph is not globally excluded.
- No CAD, quantifier-elimination, or minimum-vertex theorem is claimed.
- Numerical search failures and the auxiliary-centre near-solution are not nonexistence proofs.
- No exact parent-`E25D` to `E25S` coordinate homotopy is claimed; they are exact realizations of the same labeled graph.
- `E29-HX2` is currently an exact combinatorial design, not a geometric endpoint.

## Reusable conclusion

The inherited `E25D` packet can be altered substantially within its full coordinate freedom. Exact `E25S` already makes `A` non-unstable and kills the original extra stable faces. The connected two-support event then makes **both** `A` and `B` non-unstable and removes the remaining original carrier features. Cancellation still fails because `RB` is born unstable before `B` dies, and the final replacement packet is strict. Exact `E27AB2` is therefore a robust, independently verified, finite-thickness nonwinner with class `(3,2,3)`.

**Final disposition: exact materialized NONWINNER; the complete real `E25D` realization space remains open, and `E29-HX2` is the first explicit nonrepeating topology beyond the certified replacement carrier.**
