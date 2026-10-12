# figure-0277

AI research report · 2026-09-03 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Quiet Quartz 19 — P9-XG17-U4H1-THETA3-DC2 exact determination

## Verdict

**EXACT FINITE POST-XG16 NONWINNER.** No homogeneous convex polyhedral Gömböc was obtained. I materialized a finite exact dyadic endpoint, `P9-XG17-U4H1-THETA3-DC2-E18`, genuinely outside the P9-XG16 incidence chamber and outside its one-page carrier flip. It deletes the XG16 carrier, both incident facets, the old extra stable face, old remote unstable facet, and both old saddles, while realizing one connected full-dimensional three-route/three-page cell. Its own-centred strict class is `(S,U,H)=(2,2,2)`, not `(1,1,0)`.

The immutable parent is `figure-0272`, SHA-256 `6592b23232f7ce2025b03d4310c0e64d722abe416ee28f0c5afa4bc5f7921837`; the journal records the exact XG16 census and the XG17 theta successor. :contentReference[oaicite:0]{index=0} No conflict was found between the literal payload, archived parent input, and journal summary.

The endpoint's surviving obstruction is a new **degree-seven full row-star sink `P0`**, not the old `U4-H1` edge or its `U3-H1` one-page transfer. Three changed edges incident to `P0` have all endpoint-external arrows positive: `P0-T`, `P0-E0`, `P0-E3`. The exact inequality `||H_P0||²-||H_T27||²>0` also excludes any finite strict-negative-arrow path from fixed `P0` to fixed protected sink `T27`. A successor must move or deactivate `P0`.

## Exact immutable-parent reconstruction

For rows `q_i`, define `P_raw={x in R^3:q_i·x<=1 for every i}`. The exact parent rows are:

```text
T27=(-1483391/4194304, 221001/4194304, -47995/8388608)
TR=(20680881/4194304, -11530207/16777216, -2584425/8388608)
SA5=(-682961/8388608, -1747273/16777216, -403725/4194304)
S102=(-3710773/16777216, 1316305/8388608, 1252183/16777216)
GT=(2025509/4194304, 348563/8388608, 374789/16777216)
GR=(79670585/8388608, -47036809/8388608, 67896179/8388608)
A0=(55774609/4194304, -95036905/16777216, -44015959/16777216)
A1=(14709435/4194304, -90062061/16777216, 132616427/16777216)
A2=(-7617357/2097152, -15582753/4194304, 2176415/1048576)
A3=(-1084167/4194304, -203080501/16777216, 15092457/16777216)
A4=(11665871/16777216, 2552689/2097152, 14525363/4194304)
A5=(81983851/16777216, -11196039/16777216, -2254373/8388608)
A6=(22925547/16777216, -3003207/8388608, 141014055/16777216)
B0=(834078633629/68719476736, -85060200099/17179869184, -158178319309/68719476736)
B1=(5291169989/1073741824, -23568104843/34359738368, -20992321111/68719476736)
U0=(21177394457/4294967296, -738188427/1073741824, -1324020611/4294967296)
U3=(5294262797/1073741824, -2950693633/4294967296, -661227419/2147483648)
U4=(5294564097/1073741824, -2951120327/4294967296, -330679271/1073741824)
U5=(10589214001/2147483648, -738037661/1073741824, -1323499607/4294967296)
S=(13485317867/2147483648, -10518707741/4294967296, -3031828833/2147483648)
RU=(3042908219/4294967296, -37112373349/4294967296, 31614776683/4294967296)
H0=(13444381965/4294967296, -8813590143/4294967296, -701351089/536870912)
H1=(11600898925/4294967296, -175116595/536870912, -933109729/4294967296)
J0=(5624210133/1073741824, -792140055/1073741824, 763273275/2147483648)
K0=(-17103094031/2147483648, -29762103763/2147483648, -5931615123/1073741824)
K2=(-2299097215/536870912, 18381078381/4294967296, 60532288267/4294967296)
```

Exact triple enumeration reconstructs 26 supplied/18 active supports, `Q:(V,E,F)=(18,48,32)`, primal `P:(32,48,18)`, strict `(2,2,2)`, stable `T27,H1`, unstable `T27/S102/H1` and `GR/RU/K2`, saddles `S102-H1`,`H0-K0`, and sole nonprotected all-external-positive edge `U4-H1` with link `U3,U5`. Parent input SHA-256 is `efb950648e93336f71314b068273f6376dd9c328ef3fa725f2e633ea1e5e9f74`; archived parent package SHA-256 is `0a1c1ee55fa7387f0d67dfc89d0b479374f35c70cd7d19ee30f823b41bd5fe46`.

## Exact endpoint generator

The complete 38 supplied rows are:

```text
T27=(-352211/1048576, 42965/1048576, 19657/1048576)
TR=(79/1048576, -11/1048576, -5/1048576)
SA5=(-1/1048576, -2/1048576, -2/1048576)
S102=(-177512/1048576, 165423/1048576, 111393/1048576)
GT=(8/1048576, 1/1048576, 0/1048576)
GR=(10153363/1048576, -5827792/1048576, 8756880/1048576)
A0=(13946484/1048576, -5847349/1048576, -2981157/1048576)
A1=(56/1048576, -86/1048576, 126/1048576)
A2=(-58/1048576, -59/1048576, 33/1048576)
A3=(-4/1048576, -194/1048576, 14/1048576)
A4=(776045/1048576, 1277299/1048576, 3605247/1048576)
A5=(78/1048576, -11/1048576, -4/1048576)
A6=(22/1048576, -6/1048576, 134/1048576)
B0=(12679527/1048576, -4997074/1048576, -2570192/1048576)
B1=(79/1048576, -11/1048576, -5/1048576)
U0=(79/1048576, -11/1048576, -5/1048576)
U3=(79/1048576, -11/1048576, -5/1048576)
U4=(79/1048576, -11/1048576, -5/1048576)
U5=(79/1048576, -11/1048576, -5/1048576)
S=(100/1048576, -39/1048576, -23/1048576)
RU=(11/1048576, -138/1048576, 118/1048576)
H0=(50/1048576, -33/1048576, -21/1048576)
H1=(43/1048576, -5/1048576, -3/1048576)
J0=(84/1048576, -12/1048576, 6/1048576)
K0=(-127/1048576, -222/1048576, -88/1048576)
K2=(-69/1048576, 68/1048576, 226/1048576)
T=(2410248/1048576, -289979/1048576, -219426/1048576)
P0=(5721252/1048576, -707228/1048576, -498158/1048576)
C0=(4797717/1048576, -3312239/1048576, -1614220/1048576)
C1=(-9578340/1048576, -12263300/1048576, -4009947/1048576)
C2=(-4671912/1048576, 5868723/1048576, 16853633/1048576)
R=(1735819/1048576, -9841726/1048576, 8228001/1048576)
E0=(6099958/1048576, -864221/1048576, -576473/1048576)
E1=(4350829/1048576, -428749/1048576, -290987/1048576)
E2=(1133101/1048576, 3131962/1048576, 9549327/1048576)
E3=(7420232/1048576, -2732648/1048576, -1434617/1048576)
E4=(-871502/1048576, -10522006/1048576, -3992926/1048576)
E5=(-5959640/1048576, -18152844/1048576, 1847663/1048576)
```

Enumerate all `C(38,3)=8436` triples. Solve `[q_i;q_j;q_k]x=(1,1,1)^T` exactly and retain `x` iff every supplied row satisfies `q_l·x<=1`. Exactly 32 feasible simple vertices remain; 500 triples are singular and 7904 nonsingular triples are rejected. Orient the cycles below outward, sum signed tetrahedra `conv(0,a,b,c)`, let exact volume be `V`, exact raw first moments be `M`, and put `c=M/V`. The delivered homogeneous body is

```text
P=P_raw-c,
H_i=q_i/(1-q_i·c),
p_ijk=x_ijk-c.
```

This is a deterministic exact rational H/V reconstruction recipe; no tolerance determines incidence or mechanics.

Supplied/active is `38/18`. The irredundant active set is

```text
T27,S102,GR,A0,A4,B0,T,P0,C0,C1,C2,R,E0,E1,E2,E3,E4,E5
```

and the strict inactive set is

```text
TR,SA5,GT,A1,A2,A3,A5,A6,B1,U0,U3,U4,U5,S,RU,H0,H1,J0,K0,K2
```

The exact origin-in-Q witness uses rows `T27,S102,GR,T` with positive weights

```text
4418955507776154777/5183537207357209051
123982344869472539/5183537207357209051
4443919386052849/5183537207357209051
636155435325528886/5183537207357209051
```

summing to one with exact weighted row sum zero. The exact minimum nonincidence is `53211303912971/2951877270045811>0`; exact minimum inactive-row slack is `89067896508315369/89117732996548072>0`.

## Complete actual incidence

`Q:(V,E,F)=(18,48,32)` and primal `P:(32,48,18)`, complexity 96.

All 32 Q facets / exact primal vertices (each vertex is the exact three-row solve):

```text
00 T27/S102/T
01 T27/S102/C2
02 T27/T/C0
03 T27/C0/E4
04 T27/C1/C2
05 T27/C1/E4
06 S102/A4/C2
07 S102/A4/E1
08 S102/T/E1
09 GR/A0/E2
10 GR/A0/E5
11 GR/C2/R
12 GR/C2/E2
13 GR/R/E5
14 A0/B0/E0
15 A0/B0/E2
16 A0/P0/E0
17 A0/P0/E3
18 A0/C0/E3
19 A0/C0/E4
20 A0/E4/E5
21 A4/C2/E2
22 A4/E1/E2
23 B0/E0/E2
24 T/P0/C0
25 T/P0/E1
26 P0/C0/E3
27 P0/E0/E2
28 P0/E1/E2
29 C1/C2/E5
30 C1/E4/E5
31 C2/R/E5
```

All 48 true Q edges / dual primal true edges:

```text
T27-S102 T27-T T27-C0 T27-C1 T27-C2 T27-E4 S102-A4 S102-T S102-C2 S102-E1 GR-A0 GR-C2 GR-R GR-E2 GR-E5 A0-B0 A0-P0 A0-C0 A0-E0 A0-E2 A0-E3 A0-E4 A0-E5 A4-C2 A4-E1 A4-E2 B0-E0 B0-E2 T-P0 T-C0 T-E1 P0-C0 P0-E0 P0-E1 P0-E2 P0-E3 C0-E3 C0-E4 C1-C2 C1-E4 C1-E5 C2-R C2-E2 C2-E5 R-E5 E0-E2 E1-E2 E4-E5
```

All 18 maximal primal-face cycles:

```text
T27: 0 2 3 5 4 1
S102: 0 1 6 7 8
GR: 9 12 11 13 10
A0: 9 10 20 19 18 17 16 14 15
A4: 6 21 22 7
B0: 14 23 15
T: 0 8 25 24 2
P0: 16 17 26 24 25 28 27
C0: 2 24 26 18 19 3
C1: 4 5 30 29
C2: 1 4 29 31 11 12 21 6
R: 11 31 13
E0: 14 16 27 23
E1: 7 22 28 25 8
E2: 9 15 23 27 28 22 21 12
E3: 17 18 26
E4: 3 19 20 30 5
E5: 10 13 31 29 30 20
```

Both Euler identities equal two.

## Exact mass, centroid, and first moments

The exact ordinary volume is

```text
728653169078278981512077881700828340064389732088576861600770418351256334936540194978355950786796603500017692906018120681755773575992736863109225303979306090340159553384381403325131800973518207549972895130547711356806782722866516598895123293531475796947013779247944498243708749814138613307123603043150219759403953302845044392269326446410017788287080237119752977043864426673908452222439883746878784928370065402668884660005456622468974666562261922191796485234725613535972875432616602151895341052422105231725284301222721760820555317907935063184039947655929095065643778048/334691460209353272797861531827677601665930024432380442223672992122579127026501489974765703611746518249835244753543202897334640333691768446001468160633812318244551340683172410915633735267526565590587051788471961229091637355928897017470999764670608997417746853228329689948963099950129254335980590579805434561780171998630747450680001108284239630855806207115358057789743804675190968035416203814457149909045635143369619003031119322708385349794293497256934315714363831123116947568639076704504152107998642852110306823130018808095462573616755081603210914430449839116441075
```

(`V≈2177.089217103114`). The exact raw centroid is generated by the signed-tetrahedron formula above and is approximately `(-1.210913452378061, 25.854944374302804, -41.94024688338846)`. Translation by that exact rational centroid gives exact ordinary first moments

```text
(Mx,My,Mz)=(0/1,0/1,0/1).
```

## Literal XG16-packet deletion

The exact active/inactive and incidence audit proves simultaneously:

```text
U4-H1 absent;
U3/U4/H1 absent;
U4/U5/H1 absent;
H1 strict inactive;
GR/RU/K2 absent;
S102-H1 absent;
H0-K0 absent;
U3,U4,U5,H0,H1,K0,K2,RU all strict inactive.
```

Thus the endpoint is not a relabelling, subdivision, or one-page diagonal transfer of the parent.

## Connected full-dimensional theta event

Scale every parent row by `1/64` and every future row by `1/65536` to obtain the exact pre-event. Its active body is exactly similar to XG16 and all new rows are strict interior. All 1216 outer-facet/inner-row tests place complete pre-event Q strictly inside endpoint Q; minimum relative slack is `146673667656231947723/365026234353860902912>0`. Exact positive shell volume is `262157949705975475162458983841929517845/124615124604835863084731911901282304>0`.

Endpoint Q is one convex full-dimensional 3-ball. Coning its complete 32-triangle boundary from exact interior origin gives the complete decomposition:


[Encoded source block omitted; the code in this passage is incomplete.]


Every tetrahedron has positive exact volume; total cell volume is `14552727998474757803909/6917529027641081856>0`, and minimum tetrahedron volume is `4443919386052849/6917529027641081856>0`.

Target `T` and return `R` are nonadjacent. Three internally vertex-disjoint boundary routes are

```text
T-T27-C2-R
T-P0-A0-GR-R
T-C0-E4-E5-R
```

Three positive interior communication pages are `O-T27-C2`, `O-P0-A0`, and `O-C0-E4`, each shared by exactly two positive tetrahedra. This certifies one connected finite-thickness three-page theta event.

## Exhaustive mechanics

At the exact own centroid:

```text
stable faces: T27,P0
unstable vertices: T27/S102/T; GR/C2/R
horizontal saddles: S102-T; C1-E4
class=(2,2,2)
```

Every maximal face is audited by all true-neighbour arrows `H_i·(H_i-H_j)`. Every vertex is solved in its full active normal cone. Every one of the 48 true edges is audited with all four exact strict components `t,1-t,alpha,beta`. Exact-point orientation minima are: stable support `4.1492767351149163e-5`; nonstable exclusion `1.1230891564447115e-5`; unstable coefficient `3.3744243191624914`; nonunstable exclusion `1.5843655286129`; saddle component `10.126464502042648`; nonsaddle exclusion `0.0008495351029617811`. Exact rational numerators are regenerated from the supplied rows.

## Complete changed-edge anti-carrier ledger

For external true neighbour `z`, define exactly `A(u->z)=H_u·(H_u-H_z)`. Relative to exact XG16 there are 42 inserted or inherited-star-changed nonprotected true edges. This is the complete witness census; each displayed decimal is only the orientation of an exact rational value:

```text
A4-S102: S102->T27=-0.1269453023429376<0 (exact rational sign)
S102-T: S102->T27=-0.1269453023429376<0 (exact rational sign)
C2-S102: S102->T27=-0.1269453023429376<0 (exact rational sign)
E1-S102: E1->P0=-0.19748358677346209<0 (exact rational sign)
A0-GR: A0->P0=-0.23860039626683813<0 (exact rational sign)
C2-GR: C2->T27=-0.010940325565119407<0 (exact rational sign)
GR-R: GR->A0=-0.0056283676009255303<0 (exact rational sign)
E2-GR: GR->A0=-0.0056283676009255303<0 (exact rational sign)
E5-GR: GR->A0=-0.0056283676009255303<0 (exact rational sign)
A0-B0: A0->P0=-0.23860039626683813<0 (exact rational sign)
A0-P0: A0->E0=-0.19330971043045966<0 (exact rational sign)
A0-C0: A0->P0=-0.23860039626683813<0 (exact rational sign)
A0-E0: A0->P0=-0.23860039626683813<0 (exact rational sign)
A0-E2: A0->P0=-0.23860039626683813<0 (exact rational sign)
A0-E3: E3->P0=-0.25598965530171758<0 (exact rational sign)
A0-E4: A0->P0=-0.23860039626683813<0 (exact rational sign)
A0-E5: A0->P0=-0.23860039626683813<0 (exact rational sign)
A4-C2: C2->T27=-0.010940325565119407<0 (exact rational sign)
A4-E1: E1->P0=-0.19748358677346209<0 (exact rational sign)
A4-E2: A4->S102=-0.0021637836144638781<0 (exact rational sign)
B0-E0: E0->P0=-0.13147482015613646<0 (exact rational sign)
B0-E2: B0->E0=-0.19853886836252624<0 (exact rational sign)
P0-T: FAIL — all endpoint-external arrows positive
C0-T: C0->P0=-0.1703031887852533<0 (exact rational sign)
E1-T: E1->P0=-0.19748358677346209<0 (exact rational sign)
C0-P0: C0->T=-0.17011410455677917<0 (exact rational sign)
E0-P0: FAIL — all endpoint-external arrows positive
E1-P0: E1->T=-0.19745330475997569<0 (exact rational sign)
E2-P0: E2->A4=-2.9196902587434324e-05<0 (exact rational sign)
E3-P0: FAIL — all endpoint-external arrows positive
C0-E3: E3->P0=-0.25598965530171758<0 (exact rational sign)
C0-E4: C0->P0=-0.1703031887852533<0 (exact rational sign)
C1-C2: C1->T27=-0.046118895925633507<0 (exact rational sign)
C1-E4: C1->T27=-0.046118895925633507<0 (exact rational sign)
C1-E5: C1->T27=-0.046118895925633507<0 (exact rational sign)
C2-R: C2->T27=-0.010940325565119407<0 (exact rational sign)
C2-E2: C2->T27=-0.010940325565119407<0 (exact rational sign)
C2-E5: C2->T27=-0.010940325565119407<0 (exact rational sign)
E5-R: E5->C1=-0.0023800007044126256<0 (exact rational sign)
E0-E2: E0->P0=-0.13147482015613646<0 (exact rational sign)
E1-E2: E1->P0=-0.19748358677346209<0 (exact rational sign)
E4-E5: E4->C0=-0.0026629241588246397<0 (exact rational sign)
```

Exactly 39/42 changed edges have strict negative external witnesses. The only failures are `P0-T`, `P0-E0`, and `P0-E3`; no other changed nonprotected edge is all-external-positive.

## Exact residual forcing component

The P0 link cycle is

```text
T-C0-E3-A0-E0-E2-E1-T.
```

All seven P0 outgoing arrows are positive, with orientation values

```text
P0->A0 0.800662671831751
P0->T 4.1492767351149163e-5
P0->C0 0.9316606707995813
P0->E0 0.15157396850350263
P0->E1 0.2535370449743893
P0->E2 1.1617698964128529
P0->E3 0.7520851303210013.
```

For each of the three external-positive edges, exact pair-sum identity `A(u->v)+A(v->u)=||H_u-H_v||²>0` holds. The exact rational number `||H_P0||²-||H_T27||²`, computed from the exact generator, is positive (orientation `0.04049502351816712`). Since `A(x->y)<0` implies `||H_y||>||H_x||`, no finite strict-negative-arrow path with both endpoints fixed can drain P0 to T27.

The exact residual packet is extra stable `P0`, extra unstable `GR/C2/R`, and saddles `S102-T`,`C1-E4`; its index is `+1+1-2=0`.

## Exact ingress chronology

For exact affine ingress `q(t)=(1-t)q_pre+tq_post`, complete Fraction reconstructions give:

```text
t=0: P=(32, 48, 18), class=(2, 2, 2), H1_active=True, stable=T27,H1, unstable=T27/S102/H1; GR/RU/K2, saddles=S102-H1; H0-K0, carriers=U4-H1
t=3/500: P=(38, 57, 21), class=(2, 2, 2), H1_active=True, stable=T27,H1, unstable=T27/S102/P0; GR/RU/K2, saddles=S102-H1; H0-K0, carriers=U5-H1; H1-P0
t=7/1000: P=(38, 57, 21), class=(2, 2, 2), H1_active=True, stable=T27,P0, unstable=T27/S102/P0; GR/RU/K2, saddles=S102-H1; H0-K0, carriers=H1-P0
t=1/100: P=(36, 54, 20), class=(2, 2, 2), H1_active=False, stable=T27,P0, unstable=T27/S102/P0; GR/RU/K2, saddles=S102-P0; H0-K0, carriers=P0-E0; P0-E1
t=1: P=(32, 48, 18), class=(2, 2, 2), H1_active=False, stable=T27,P0, unstable=T27/S102/T; GR/C2/R, saddles=S102-T; C1-E4, carriers=T-P0; P0-E0; P0-E3
```

At `t=3/500`, H1 is stable and `H1-P0` is true/all-external-positive. At `t=7/1000`, the same edge persists, H1 remains active, but P0 is stable. H1 is inactive by `t=1/100`. Thus this displayed ingress is serial and does not satisfy death-before-birth cancellation. These checkpoints do not exclude every nonlinear connector or an untested tiny interval.

## Controls and positive chamber

Seven named shape controls are `T_z,P0_x,C0_y,C2_z,R_x,E4_y,E5_z`. Projective translation `q_i->q_i/(1-q_i·tau)` translates the primal by `-tau`; the centroid-residual Jacobian in `(tau_x,tau_y,tau_z)` is exactly `-I_3`. The ten-variable block Jacobian is `[[I_7,0],[Dc/du,-I_3]]`, rank 10, determinant `-1`, so seven independent physical controls remain after the three moment equations.

Outward interval arithmetic certifies independent variation of all 54 active raw coordinates by

```text
|delta q_ij|<=2^-39=1/549755813888,
```

with all 60 inactive coordinates fixed and centroid recomputed. The box preserves complete incidence, exact class `(2,2,2)`, all routes/pages, changed-edge census, and P0 forcing theorem. Rigorous lower bounds are: Q orientation `0.00023076719093978004`; P nonincidence `0.018026239856991037`; inactive slack `0.9994407792179073`; surface determinant `2.3977034412856358e-5`; projective denominator `0.3200918313243902`; positive mechanics `4.0657842293418424e-5`; negative-witness separation `1.0395980023079807e-5`; changed-edge negative witness `2.9196770713068154e-5`; P0 star arrow `4.0657842293418424e-5`; P0/T27 radius gap `0.04049353971123864`; cell tetra volume `0.0006424142734069713`. The immediately larger tested `2^-38` box fails closed at the nonsaddle beta component of `T-P0`, so no larger box is claimed.

## Independent verification, meshes, and hashes

`verify_independent.py` imports neither `exact_core.py` nor any generator. It independently enumerates every parent/endpoint triple, reconstructs exact H/V/E and mass/centroid, audits every equilibrium and changed-edge arrow, rebuilds the 32 tetrahedra, routes/pages and chronology, and checks meshes. It terminates `P9_XG17_THETA3_DC2_INDEPENDENT_CLEAN_ROOM_PASS`.

Watertight OBJ/STL have 32 vertices, 60 triangles, 90 undirected mesh edges, Euler characteristic two, and edge multiplicity exactly two.

Source and clean fresh extraction both terminate `ALL QUIET QUARTZ 19 P9-XG17 EXACT NONWINNER CHECKS PASS`. Fresh extraction regenerates a byte-identical deterministic ZIP.

```text
parent result SHA-256 6592b23232f7ce2025b03d4310c0e64d722abe416ee28f0c5afa4bc5f7921837
endpoint input SHA-256 6530d0a648a22b696e519e4245807856a3d13d7c3d1eabcaf2950b7965b557c3
exact ledger SHA-256 362aed175bbbaa4f2798c4a9e130f36f49bd8cbe5f48a04b8662186632d5aa12
independent verifier SHA-256 026a6d4b652e2ef1f33a10457aeb067f77be7eefdd415059f356c251c8555d07
independent report SHA-256 88664ae1d257d70e25dc78cef3af31919374a6ec492391772f037717ba647109
triangulated OBJ SHA-256 7beddd52db70ed33249f993d6c4bd773689718fdb37ec1961965d4a89ba2240c
STL SHA-256 3a70217361c7a3a795d965a2c17bdfbe600d09346200dbd931a9648d5a9b4fdc
manifest SHA-256 3300ba2ed1e41eae1a8917b49876167fd4b5738a45b2cc62696f9b2b1fbadfaa
archive SHA-256 b2f20272088997fc694d44bd6b6182ec6c0bda0d5f4b4311a10847c4653ec35f
verification receipt SHA-256 e6dfb7c7c9670df697874458f6314bc887a73a98b2736b477a2bcdbe314f1b89
```

## First genuinely unrepresented continuation

The next topology is **P9-XG18-P0FS9-RC3**: a complete degree-seven P0-star turnover coupled, before moment closure, to remote `GR/C2/R` unstable sector and both saddle exchanges. It must make P0 inactive; remove `P0-T`,`P0-E0`,`P0-E3`, `GR/C2/R`, `S102-T`, and `C1-E4`; preserve T27 as sole stable and one `T27/S102/target` unstable vertex; provide at least three internally vertex-disjoint target/return routes plus a transverse return page; keep target/return nonadjacent; give every changed nonprotected edge a negative external witness; and retain at least seven controls. The smallest unrepresented compact realization is a three-overlapping-cell prismatic/octahedral complex with at least nine new extreme rows. One-edge subdivisions, one-page flips, fixed-P0 ascent belts, and serial transfers through a new P0 neighbour are already represented and excluded as repetitions.

## Artifacts

- [Complete deterministic package](sandbox:/mnt/data/Quiet_Quartz_19_P9_XG17_THETA3_DC2_exact_nonwinner.zip)
- [Detailed full handoff](sandbox:/mnt/data/quiet_quartz19_p9xg17_theta3_dc2/RESEARCH_HANDOFF.md)
- [Package manifest](sandbox:/mnt/data/quiet_quartz19_p9xg17_theta3_dc2/PACKAGE_MANIFEST.json)
- [Verification receipt](sandbox:/mnt/data/Quiet_Quartz_19_P9_XG17_THETA3_DC2_VERIFICATION_RECEIPT.json)
- [Exact endpoint rows](sandbox:/mnt/data/quiet_quartz19_p9xg17_theta3_dc2/p9_xg17_theta3_dc2_rows_exact.json)
- [Complete exact ledger](sandbox:/mnt/data/quiet_quartz19_p9xg17_theta3_dc2/p9_xg17_theta3_dc2_exact_ledger.json)
- [Independent verifier](sandbox:/mnt/data/quiet_quartz19_p9xg17_theta3_dc2/verify_independent.py)
- [Perturbation certificate](sandbox:/mnt/data/quiet_quartz19_p9xg17_theta3_dc2/perturbation_chamber.json)
- [Watertight OBJ](sandbox:/mnt/data/quiet_quartz19_p9xg17_theta3_dc2/p9_xg17_theta3_dc2_centered_triangulated.obj)
- [Watertight STL](sandbox:/mnt/data/quiet_quartz19_p9xg17_theta3_dc2/p9_xg17_theta3_dc2_centered.stl)
- [P9-XG18 specification](sandbox:/mnt/data/quiet_quartz19_p9xg17_theta3_dc2/P9_XG18_successor_spec.json)

## Final status

**USED exact delimited nonwinner.** XG17 is now materially represented with complete XG16 residual absent and a connected finite-thickness three-page event. It fails by a new P0 full-row-star sink and Euler-neutral `(1,1,2)` residual packet; the exact radius inequality proves fixed-P0 drainage to T27 impossible. Continue with complete P0 turnover P9-XG18-P0FS9-RC3, not another local carrier transfer.
