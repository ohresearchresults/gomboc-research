# figure-0291

AI research report · 2026-09-04 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

## Downloadable artifacts

- [Complete exact archive](sandbox:/mnt/data/Vivid_Quartz_58_E30_BELT2_WP2_exact_NONWINNER_FINAL.zip)
- [Archive SHA-256](sandbox:/mnt/data/Vivid_Quartz_58_E30_BELT2_WP2_exact_NONWINNER_FINAL.zip.sha256): `31e9a244448ef4a3fa78e4b2804ac25b9e754aa490252769b597156ceed12b36`
- [Full Markdown determination](sandbox:/mnt/data/Vivid_Quartz_58_E30_BELT2_WP2_exact_NONWINNER_FINAL/RESULT.md)
- [One-command verifier](sandbox:/mnt/data/Vivid_Quartz_58_E30_BELT2_WP2_exact_NONWINNER_FINAL/[internal-source-reference].sh)
- [Clean replay transcript](sandbox:/mnt/data/Vivid_Quartz_58_E30_BELT2_WP2_exact_NONWINNER_FINAL/CLEAN_VERIFICATION_TRANSCRIPT.txt)
- [Verification record](sandbox:/mnt/data/Vivid_Quartz_58_E30_BELT2_WP2_exact_NONWINNER_FINAL/VERIFICATION_RECORD.json)
- [SHA256 manifest](sandbox:/mnt/data/Vivid_Quartz_58_E30_BELT2_WP2_exact_NONWINNER_FINAL/SHA256SUMS)

# Vivid Quartz 58 — exact `E30-BELT2` whole-packet realization and same-size successor

## Literal disposition

**EXACT MATERIALIZED NONWINNER.** No finite uniform-density convex polyhedron with strict own-centroid `(S,U,H)=(1,1,0)` was obtained.

The immutable source is parent `figure-0284`, SHA-256 `08ba13384239488671ad1417e813e986ba38d6f3dc54fbbd18c324cbb845510c`. Its exact endpoint `E29HX2S` has `(29,81,54)`, strict `(2,2,2)`, and the first whole-packet frontier `E30-BELT2` was specified as a 20-triangle connected disk with true shared edge `(RE,RF)` and inactive predecessor vertex `RA`. The journal records both the exact parent and the fact that fixed-metric LP failure was only a search failure, not nonrealizability. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

This handoff resolves that frontier positively at the incidence level:

1. **`E30BELT2R` realizes the literal requested sphere exactly.** It is a dyadic `(30,84,56)` body; `RA` is absent, `RE,RF` are genuine extreme vertices, `(RE,RF)` is a true edge, all 20 requested disk triangles are actual irredundant facets, and the target disk is a finite positive-volume connected cell. Its strict own-centred class is `(2,2,2)`.
2. **`E30WP2R` is a stronger same-size whole-packet successor.** It deletes every unwanted `E30BELT2R` equilibrium label and replaces the 21-face packet disk by a new positive-volume `RG,RH` disk. It remains `(2,2,2)`. On its exact all-coordinate `2^-40` chamber, vertices `8` and `B` are independently forced unstable, so `U>=2`.

Thus the literal sphere is **not geometrically impossible**. It is an exact nonwinner, and a second exact same-size topology also relays rather than annihilates the Euler-neutral packet.

## Reproducible artifact

- Complete archive: `Vivid_Quartz_58_E30_BELT2_WP2_exact_NONWINNER_FINAL.zip`.
- Run `bash [internal-source-reference].sh` from a clean extraction.
- Exact reports, complete H tables, exhaustive mechanics ledgers, perturbation boxes, independent verifiers, and watertight OBJ/STL are included for both promoted endpoints.

## 1. Source reconstruction and label map

The source exact-report SHA-256 is `83a43ab18ef947acd6a324d371c00fc195a4178c41bfb9bc7681f60a75f4b359`. The label map is identity on

```text
8, 10, 11, A, B, C, F, L, P, T, W, X, Y, U, V, G, H, K, J, R, S, O1, Z1, Q3, Z2, RB, RA, RC, RD
```

and the surgery removes only `RA`, while inserting `RE,RF`.

The source has denominator `65536` and uncentred numerators

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

with

```text
V = 141012326203/1688849860263936
M = (9442316934324439/221360928884514619392, -9941173153704349/147573952589676412928, -4463335902704429/442721857769029238784)
c = (9442316934324439/18482767620079616, -29823519461113047/36965535240159232, -4463335902704429/36965535240159232)
class = (2, 2, 2)
stable = [['B', '8', 'A'], ['RB', 'O1', '8']]
unstable = ['8', 'RA']
saddles = [['8', 'RD'], ['10', 'RA']].
```

The package contains its complete original 54-face/81-edge H/V/E and mechanics data unchanged.

## 2. Exact connected `E29HX2S -> E30BELT2R` architecture

The source disk is

```text
[RB,O1,8] [RB,8,RD] [B,RD,8] [10,RA,8]
[10,Z2,RA] [Z2,Z1,RA] [Z1,RC,RA] [RA,RC,8]
[10,8,11] [11,8,P] [T,P,8] [T,8,X]
[U,X,8] [V,U,8] [V,8,Y] [Y,8,S]
[S,8,G] [G,8,O1]
```

and the target disk is

```text
[RE,8,B] [RE,B,RD] [RE,RD,RB] [RE,RB,O1]
[RF,O1,G] [RF,G,S] [RF,S,Y] [RF,Y,V]
[RF,V,U] [RF,U,X] [RF,X,T] [RF,T,P]
[RF,P,11] [RF,11,10] [RF,10,Z2] [RF,Z2,Z1]
[RF,Z1,RC] [RF,RC,8] [8,RE,RF] [O1,RF,RE]
```

Both have Euler characteristic one and the same boundary

```text
8-B-RD-RB-O1-G-S-Y-V-U-X-T-P-11-10-Z2-Z1-RC.
```

The source and target disk f-vectors are

```text
(19,36,18)
(20,39,20).
```

The target has true shared edge `(RE,RF)`. Every target face cones to the exact target centroid with strictly positive tetrahedral volume; the exact total is

```text
26634180516697632411058032693217/3207964247232043742697337279735660544 > 0.
```

The central tetrahedron `(8,O1,RE,RF)` has exact volume

```text
205752076465781/147573952589676412928 > 0.
```

This proves a literal finite-thickness connected target cell. Source and target use independently moved old coordinates; no unproved straight coordinate homotopy is claimed.

## 3. Literal `E30BELT2R`

### 3.1 Complete V data

All 30 supplied vertices are active. Use denominator

```text
D=4194304=2^22.
```

The exact uncentred integer numerators are

```text
8=(0,0,0)
10=(81935,-2050217,5354)
11=(73371,-1770333,5967)
A=(79172,-2342757,1994)
B=(-35966,-2067043,-5875)
C=(48517,-2139423,3350)
F=(42117,-2130524,3070)
L=(67748,-1966361,5082)
P=(67759,-1808684,5653)
T=(62136,-1855891,5257)
W=(25463,-2058302,2415)
X=(51805,-1933271,4502)
Y=(19863,-1933403,2650)
U=(42025,-1900101,4086)
V=(31707,-1896211,3505)
G=(-13220,-2100807,-297)
H=(52259,-2212365,3186)
K=(31687,-2234394,1924)
J=(32812,-2257889,1853)
R=(34743,-2270584,1904)
S=(4954,-2029247,1334)
O1=(-39831,-2253108,-3184)
Z1=(98696,-2369912,4290)
Q3=(41442,-2242637,2481)
Z2=(91999,-2260188,4810)
RB=(-56163,-2325232,-6812)
RC=(98364,-2387705,3402)
RD=(-39138,-2285757,-6290)
RE=(-86569,-1631446,-8165)
RF=(51226,-169919,10010)
```

The physical body is `conv{Q_i/D-c}`.

### 3.2 Exact ordinary mass closure

```text
V = 2717251411019381/221360928884514619392
Mx = 100510223715439754007/2475880078570760549798248448
My = -15283574484250604347723/3713820117856140824697372672
Mz = 20778579737165701537/7427640235712281649394745344
cx = 301530671146319262021/91175827697953870446592
cy = -15283574484250604347723/45587913848976935223296
cz = 20778579737165701537/91175827697953870446592.
```

Direct exact identities give `M_j=V c_j`; after translation, all three first moments are exactly zero.

### 3.3 Every actual maximal face

```text
[B,8,A] [RC,A,8] [B,RE,8] [RC,8,RF]
[8,RE,RF] [P,10,11] [11,10,RF] [L,10,T]
[L,X,10] [P,T,10] [X,H,10] [H,Z2,10]
[Z2,RF,10] [P,11,RF] [RD,B,A] [RD,A,RC]
[RD,RE,B] [F,C,X] [F,H,C] [C,H,X]
[W,F,Y] [W,S,F] [F,X,U] [F,V,Y]
[F,U,V] [F,Q3,H] [F,S,Q3] [L,T,X]
[P,RF,T] [X,T,RF] [W,Y,S] [X,RF,U]
[V,RF,Y] [Y,RF,S] [V,U,RF] [K,G,J]
[K,S,G] [J,G,R] [G,O1,R] [G,S,RF]
[G,RF,O1] [Q3,Z2,H] [K,J,R] [K,R,Q3]
[K,Q3,S] [R,O1,Z1] [Q3,R,Z1] [RB,Z1,O1]
[RB,O1,RE] [O1,RF,RE] [Q3,Z1,Z2] [Z2,Z1,RF]
[RB,RC,Z1] [RC,RF,Z1] [RD,RC,RB] [RD,RB,RE]
```

### 3.4 Every true edge

```text
(8,A) (8,B) (8,RC) (8,RE) (8,RF) (10,11) (10,L)
(10,P) (10,T) (10,X) (10,H) (10,Z2) (10,RF) (11,P)
(11,RF) (A,B) (A,RC) (A,RD) (B,RD) (B,RE) (C,F)
(C,X) (C,H) (F,W) (F,X) (F,Y) (F,U) (F,V)
(F,H) (F,S) (F,Q3) (L,T) (L,X) (P,T) (P,RF)
(T,X) (T,RF) (W,Y) (W,S) (X,U) (X,H) (X,RF)
(Y,V) (Y,S) (Y,RF) (U,V) (U,RF) (V,RF) (G,K)
(G,J) (G,R) (G,S) (G,O1) (G,RF) (H,Q3) (H,Z2)
(K,J) (K,R) (K,S) (K,Q3) (J,R) (R,O1) (R,Z1)
(R,Q3) (S,Q3) (S,RF) (O1,Z1) (O1,RB) (O1,RE) (O1,RF)
(Z1,Q3) (Z1,Z2) (Z1,RB) (Z1,RC) (Z1,RF) (Q3,Z2) (Z2,RF)
(RB,RC) (RB,RD) (RB,RE) (RC,RD) (RC,RF) (RD,RE) (RE,RF)
```

Hence `(V,E,F)=(30,84,56)`, all edges have two incident facets, and Euler is two.

For any oriented face `(i,j,k)`, let

```text
n=primitive((Q_j-Q_i)×(Q_k-Q_i)), h=n·Q_i.
```

Then the exact uncentred and centred H rows are

```text
n·p<=h/D,
n·x<=h/D-n·c.
```

The displayed V table and oriented face list therefore regenerate the complete irredundant H representation. The expanded file stores every primitive normal, right side, and nonincident slack. The minimum integer nonincidence slack is `153181137`; normalized separation is `5.781498067099226e-07`.

### 3.5 Exhaustive own-centroid mechanics

```text
stable   [B,8,A], [G,S,RF]
unstable 8, RC
saddles  (8,RE), (Z1,RF)
class    (2,2,2).
```

All active normalized components are

```text
S[B,8,A]=[0.3164999594268173,0.3625368484509089,0.3209631921222738]
S[G,S,RF]=[0.4151990533543972,0.23371173991638636,0.35108920672921645]
U8 minimum=0.9587521230366705
U(RC) minimum=0.45224673404685534
H(8,RE)=[0.8590166924999528,0.14098330750004717,8.463585817331506,8.493047166267914]
H(Z1,RF)=[0.4386907226269677,0.5613092773730324,0.8977070672027925,1.2434592352727545].
```

Every other face, vertex, and true edge has a stored exact negative witness. The smallest absolute normalized component over the complete 56-face, 30-vertex, 84-edge ledger is `0.14098330750004717`.

Exact outward interval arithmetic permits all 90 coordinate entries to vary independently by `2^-35`, recomputes the dependent ordinary centroid, and preserves the entire incidence and class. Every arrow at `8` and `RC` remains positive. The true-edge identity is

```text
u(8→RC)+u(RC→8)=|RC-8|²=5710822217125/17592186044416>0.
```

Hence `8` and `RC` force `U>=2` throughout that exact chamber.

A three-shape family remains after moment closure: at common denominator `2^40`, vary `RE.x`, `RF.y`, and `RC.z` by one numerator unit each over `[-1,1]^3`. These directions have rank three modulo translation and scale, the unique dependent centroid satisfies `c_j=N_j/(4DV6)`, and the whole cube remains `(2,2,2)`.

## 4. Stronger same-size whole-packet replacement

`E30BELT2R` and `E30WP2R` share 35 exterior faces. Remove the 21-face disk

```text
[RC,A,8] [B,RE,8] [RC,8,RF] [8,RE,RF]
[11,10,RF] [Z2,RF,10] [P,11,RF] [RD,A,RC]
[P,RF,T] [X,T,RF] [X,RF,U] [V,RF,Y]
[Y,RF,S] [V,U,RF] [G,S,RF] [G,RF,O1]
[O1,RF,RE] [Z2,Z1,RF] [RB,RC,Z1] [RC,RF,Z1]
[RD,RC,RB]
```

and insert

```text
[A,RH,8] [RG,B,8] [RG,8,RH] [11,RH,10]
[10,RH,Z2] [11,P,RH] [RD,RH,A] [RE,B,RG]
[P,T,RH] [T,X,RH] [U,RH,X] [Y,RH,V]
[Y,S,RH] [U,V,RH] [S,G,RH] [G,O1,RH]
[O1,RE,RG] [O1,RG,RH] [Z2,RH,Z1] [Z1,RH,RB]
[RB,RH,RD]
```

on common boundary

```text
8-B-RE-O1-G-S-Y-V-U-X-T-P-11-10-Z2-Z1-RB-RD-A.
```

The source-only internal vertices are `RC,RF`; the target-only vertices are `RG,RH`, and `(RG,RH)` is a true shared edge. Both disk complexes have `(V,E,F)=(21,41,21)` and Euler one. All 21 target-face cones are strictly positive, with exact total

```text
322643677889210061896068996877393235536221/290407198962200143038864236045945089818624>0.
```

The two page tetrahedra sharing the internal `RG-RH` structure have exact positive volumes

```text
273458830920505612759148949668305918814851/1452035994811000715194321180229725449093120
6808687607129346940815487888595787544121/726017997405500357597160590114862724546560.
```

The feature genealogy is exact:

```text
source extra stable   [G,S,RF]
source extra unstable RC
source saddles        (8,RE), (Z1,RF)

target extra stable   [RG,8,RH]
target extra unstable B
target saddles        (8,A), (8,B).
```

Every named source-unwanted feature is absent or inactive in the target. The packet is destroyed topologically but replaced mechanically.

## 5. Strongest endpoint `E30WP2R`

### 5.1 Complete V data

All 30 supplied vertices are active. Use denominator `D=4194304=2^22` and uncentred numerators

```text
8=(3749431,16736550,-31333486)
10=(-64436,375195,1704247)
11=(-59661,494141,1719581)
A=(-539323,6222508,-5579516)
B=(-544236,-10301790,-3244717)
C=(-69302,241014,1686719)
F=(-70541,200247,1681244)
L=(-63658,391333,1706296)
P=(-60036,484373,1718320)
T=(-61532,445358,1713277)
W=(-71235,169665,1676753)
X=(-64999,353586,1701375)
Y=(-67263,278134,1691052)
U=(-63524,386583,1705519)
V=(-63979,371440,1703448)
G=(-91074,-468690,1586304)
H=(-72343,169800,1677581)
K=(-89565,-365556,1603513)
J=(-93815,-506633,1583003)
R=(-100746,-684058,1559187)
S=(-75869,31511,1658039)
O1=(-129231,-1821271,1379045)
Z1=(-113451,-706663,1561337)
Q3=(-86031,-191067,1630216)
Z2=(-78471,46875,1661693)
RB=(-218440,-1992987,1292164)
RD=(-407289,-2286551,420196)
RE=(-306481,-4920303,505644)
RG=(31574,-3776561,-104332)
RH=(-54473,623819,1736298)
```

The physical body is `conv{Q_i/D-c}`.

### 5.2 Exact mass

```text
V=68329018233560660535/36893488147419103232
Mx=521629729815566613315412483/1856910058928070412348686336
My=370140151986673134369793573/309485009821345068724781056
Mz=-9905861491901697619672203957/2475880078570760549798248448
cx=521629729815566613315412483/3439112093917156952695111680
cy=370140151986673134369793573/573185348986192825449185280
cz=-3301953830633899206557401319/1528494263963180867864494080.
```

Again `M=Vc` exactly and centred first moments are `(0,0,0)`.

### 5.3 All 56 maximal faces

```text
[A,8,B] [A,RH,8] [RG,B,8] [RG,8,RH]
[11,10,P] [11,RH,10] [L,T,10] [L,10,X]
[P,10,T] [X,10,H] [10,Z2,H] [10,RH,Z2]
[11,P,RH] [RD,A,B] [RD,RH,A] [RE,RD,B]
[RE,B,RG] [C,F,X] [C,H,F] [C,X,H]
[W,Y,F] [W,F,S] [U,X,F] [Y,V,F]
[U,F,V] [F,H,Q3] [F,Q3,S] [L,X,T]
[P,T,RH] [T,X,RH] [W,S,Y] [U,RH,X]
[Y,RH,V] [Y,S,RH] [U,V,RH] [J,G,K]
[K,G,S] [J,R,G] [G,R,O1] [S,G,RH]
[G,O1,RH] [H,Z2,Q3] [J,K,R] [K,Q3,R]
[K,S,Q3] [R,Z1,O1] [Q3,Z1,R] [Z1,RB,O1]
[O1,RB,RE] [O1,RE,RG] [O1,RG,RH] [Z2,Z1,Q3]
[Z2,RH,Z1] [Z1,RH,RB] [RB,RD,RE] [RB,RH,RD]
```

### 5.4 All 84 true edges

```text
(8,A) (8,B) (8,RG) (8,RH) (10,11) (10,L) (10,P)
(10,T) (10,X) (10,H) (10,Z2) (10,RH) (11,P) (11,RH)
(A,B) (A,RD) (A,RH) (B,RD) (B,RE) (B,RG) (C,F)
(C,X) (C,H) (F,W) (F,X) (F,Y) (F,U) (F,V)
(F,H) (F,S) (F,Q3) (L,T) (L,X) (P,T) (P,RH)
(T,X) (T,RH) (W,Y) (W,S) (X,U) (X,H) (X,RH)
(Y,V) (Y,S) (Y,RH) (U,V) (U,RH) (V,RH) (G,K)
(G,J) (G,R) (G,S) (G,O1) (G,RH) (H,Q3) (H,Z2)
(K,J) (K,R) (K,S) (K,Q3) (J,R) (R,O1) (R,Z1)
(R,Q3) (S,Q3) (S,RH) (O1,Z1) (O1,RB) (O1,RE) (O1,RG)
(O1,RH) (Z1,Q3) (Z1,Z2) (Z1,RB) (Z1,RH) (Q3,Z2) (Z2,RH)
(RB,RD) (RB,RE) (RB,RH) (RD,RE) (RD,RH) (RE,RG) (RG,RH)
```

Thus `(V,E,F)=(30,84,56)` and Euler is two. The same primitive-normal formula regenerates every exact H row. The minimum integer nonincidence slack is `4780228`; normalized nonincidence is `5.4622173315332344e-08`.

### 5.5 Exhaustive mechanics

```text
stable   [A,8,B], [RG,8,RH]
unstable 8, B
saddles  (8,A), (8,B)
class    (2,2,2).
```

Active normalized components:

```text
S[A,8,B]=[0.5128789930034059,0.16731833680070157,0.3198026701958926]
S[RG,8,RH]=[0.5971960900033793,0.2917828286342086,0.11102108136241211]
U8 minimum=0.9794430708109022
U(B) minimum=0.516542884371853
H(8,A)=[0.927099330371175,0.07290066962882506,1.6856335647845329,1.87166009165056]
H(8,B)=[0.6618675035279024,0.33813249647209764,5.391276416888581,5.396724066525178].
```

Every inactive feature has a stored exact negative witness. The global minimum absolute normalized feature separation is `0.06139499006706498`.

### 5.6 Exact residual obstruction

On the full independent-coordinate box

```text
epsilon=2^-40=1/1099511627776,
```

every actual-neighbour arrow at `8` and `B` is interval-positive after recomputing the exact dependent ordinary centroid. The limiting endpoint arrow is

```text
B→RE=159014115147924808888358871310503413/57698726447860428301267670799482880>0.
```

The mutual identity is

```text
u(8→B)+u(B→8)=769243175098925/8796093022208=|B-8|²>0.
```

Therefore both `8` and `B` remain strict unstable vertices throughout the whole certified chamber, including internal mechanics walls: `U>=2`. This is a local exact theorem, not a global exclusion of all realizations of the graph.

A separate three-parameter physical family uses common denominator `2^45` and changes

```text
Q_RG.x+=a,
Q_RH.y+=b,
Q_B.z+=c,
(a,b,c)∈[-1,1]^3.
```

It has shape rank three modulo translation and scale. The exact volume and moment polynomials have multidegrees `(1,1,1)` and `(2,1,1)/(1,2,1)/(1,1,2)`; `d(M-Vc)/dc=-V I_3`, so the centroid is the unique dependent moment solve. The entire cube is contained in the `2^-40` chamber, and an independent 125-member grid reconstructs only `(2,2,2)`.

## 6. Independent replay and meshes

A clean implementation imports neither stored incidence nor exact feature signs. It reconstructs each hull with SciPy/Qhull, orients every actual triangle from an interior point, integrates ordinary volume and first moments directly, rebuilds all actual-neighbour vertex cones and every two-normal edge cone, compares the resulting labels and counts, and reads both OBJ and STL with Trimesh. Both endpoints pass as watertight, winding-consistent Euler-two meshes. The exact verifier separately regenerates every rational mass, H row, face component, vertex arrow, and four-component edge cone from the integer V data.

A clean extraction replay produced:

```text
E30BELT2R exact whole-packet realization EXACT_RECONSTRUCTION_PASS
E30WP2R exact whole-packet successor EXACT_RECONSTRUCTION_PASS
E29HX2S_TO_E30BELT2R_EXACT_CONNECTED_PATCH_PASS
E30_TO_WP2_POSITIVE_VOLUME_PATCH_PASS
E30BELT2R_TO_E30WP2R_FEATURE_GENEALOGY_PASS
E30BELT2R_INTERVAL_BOX_PASS
E30WP2R_INTERVAL_BOX_PASS
E30BELT2R_LOCAL_U_GE_2_FORCING_PASS
E30WP2R_LOCAL_U_GE_2_FORCING_PASS
INDEPENDENT_E30BELT2R_THREE_CONTROL_FAMILY_PASS
INDEPENDENT_E30WP2R_THREE_CONTROL_FAMILY_PASS
INDEPENDENT_E30BELT2R_RECONSTRUCTION_PASS
INDEPENDENT_E30WP2R_RECONSTRUCTION_PASS
E32_RING2_EXACT_SPHERE_PASS
E30_BELT2_WP2_MANIFEST_PASS 53
VIVID_QUARTZ_58_E30_BELT2_WP2_FULL_REPLAY_PASS
```

## 7. Search coverage and claim boundary

Discovery included unrestricted full-coordinate realization, support-space/Tutte-Maxwell seeds, projective and SPD recharting, topology-aware nonlinear searches, and millions of sampled metric/projective bodies. No strict own-centred `(1,1,0)` state was found. Apparent extreme-transform winners resolved under higher precision to cancellation artifacts. These searches are empirical evidence only.

**Proved:** exact convex realization of the literal `E30-BELT2` sphere; exact own mass; complete H/V/E; exhaustive mechanics; positive target-cell volume; `2^-35` open chamber; exact local `U>=2`; a second exact same-size positive-volume whole-packet replacement; complete `E30WP2R` H/V/E/mass/mechanics; `2^-40` open chamber; local `U>=2`; rank-three moment-eliminated families; independent replay and watertight meshes.

**Not proved:** global nonexistence in either 30-vertex realization space, a minimum-vertex theorem, or an exact coordinate homotopy between endpoint tables.

## 8. First genuinely nonrepeating successor

The exact next sphere is `E32-RING2`. In `E30WP2R`, remove

```text
[A,8,B] [A,RH,8] [RG,B,8] [RG,8,RH]
[RD,A,B] [RD,RH,A] [RE,RD,B] [RE,B,RG]
```

and add

```text
[A,8,B] [RI,A,RH] [RI,RH,RG] [RI,RG,RJ]
[RI,RJ,8] [RI,8,A] [RJ,RG,B] [RJ,B,8]
[RD,A,B] [RD,RH,A] [RE,RD,B] [RE,B,RG]
```

on boundary `RG-RH-RD-RE`. New vertices are `RI,RJ`, with true shared edge `(RI,RJ)`. The exact sphere has `(V,E,F)=(32,90,60)`, all edges degree two, connected dual, and preserved `[8,A,B]`.

Its purpose is to remove `[RG,8,RH]`, alter both saddle stars `(8,A),(8,B)`, and give `B` a prospective negative external escape in one connected annular-to-disk event. It is exact combinatorics only: no exact convex endpoint or minimum theorem is claimed.

## Reusable conclusion

The literal `E30-BELT2` sphere is convexly realizable. Its connected two-page cell jointly removes the entire `E29HX2S` packet, but exact own-centroid mechanics immediately produce a new `(2,2,2)` packet. A second same-size whole-packet replacement removes that packet as well and again relays it. `E30WP2R` is the strongest exact endpoint in this handoff: a fully materialized, own-centred, irredundant, independently reconstructed and watertight `(30,84,56)` nonwinner, with local theorem `U>=2` on an all-coordinate `2^-40` chamber.

**Final disposition: exact materialized NONWINNER; the requested topology is realized, and `E32-RING2` is the first explicit nonrepeating incidence frontier.**
