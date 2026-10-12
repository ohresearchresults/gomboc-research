# figure-0272

AI research report · 2026-09-03 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Quiet Quartz 19 — P9-XG16-TRFS11-FP5 exact post-TR determination

## Verdict

**EXACT POST-TR FULL-STAR ENDPOINT; NONWINNER.** I did not construct the requested homogeneous convex polyhedral Gömböc. The acceptance gate remains a finite uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid with strict `(S,U,H)=(1,1,0)`, complete actual incidence, exhaustive full-normal-cone mechanics, an independent verifier, and matching watertight meshes. Auxiliary-centre, wall, nearstate, and merely numerical objects remain inadmissible. :contentReference[oaicite:0]{index=0}

The immutable parent is `figure-0263`, SHA-256 `4cdbbad621f79aa04ed18cf2e29726b932f2279f1aae45f8ff60dda590148493`. I found no conflict between its literal payload and the journal summary. It certifies P9-XG15-CD2 as a 15-support own-centred `(2,2,2)` body whose only nonprotected all-external-positive forcing edge is `TR-B1`, and identifies complete replacement of the degree-six `TR` star as the next unrepresented topology. :contentReference[oaicite:1]{index=1}

I enlarged the requested seven-row budget and exactified **P9-XG16-TRFS11-FP5-E18**. It uses eleven active replacement rows in one connected full-dimensional cell. It is genuinely outside every XG12–XG15 sign chamber: `TR` and seven additional predecessor rows are strictly inactive; `TR-B1`, both old saddle sheets, and the remote old unstable facet are absent. Nevertheless, the endpoint is strict own-centred `(2,2,2)`, not `(1,1,0)`. Its complete residual is carried by the new true edge `U4-H1`.

A crucial failure is preserved rather than hidden: the natural exact homothetic affine ingress is **serial**. Replacement stable row `H1` is born while `TR` is still stable; the carrier becomes `TR-H1`, then `U4-H1`, and only afterward does `TR` become inactive. This endpoint therefore does not qualify as a realization of the requested simultaneous P9-XG16 cancellation. It is promoted only as a fully exact post-TR topology, obstruction, and successor boundary.

## Exact reconstruction of P9-XG15-CD2

The first fifteen rows in the exact input below reconstruct the immutable parent. Exact enumeration reproduces:

```text
supplied/active supports: 15/15
Q:(V,E,F)=(15,39,26)
P:(V,E,F)=(26,39,15)
class=(2,2,2)
stable: T27, TR
unstable: T27/TR/S102; A1/A2/A6
saddles: SA5-A0; S102-GT
sole nonprotected forcing edge: TR-B1
TR link cycle: T27-SA5-B0-B1-GT-S102-T27
```

On `TR-B1`, all endpoint-external arrows are strictly positive and the exact mutual-arrow sum is `||H_TR-H_B1||²>0`. This reconstruction is included in the clean-room replay rather than accepted from stored incidence.

## Deterministic exact support definition

Define

```text
P_raw = {x in R^3 : q_i·x <= 1 for every supplied row q_i}.
```

The complete 26-row exact input is:

```text
T27 = (-1483391/4194304, 221001/4194304, -47995/8388608)
TR = (20680881/4194304, -11530207/16777216, -2584425/8388608)
SA5 = (-682961/8388608, -1747273/16777216, -403725/4194304)
S102 = (-3710773/16777216, 1316305/8388608, 1252183/16777216)
GT = (2025509/4194304, 348563/8388608, 374789/16777216)
GR = (79670585/8388608, -47036809/8388608, 67896179/8388608)
A0 = (55774609/4194304, -95036905/16777216, -44015959/16777216)
A1 = (14709435/4194304, -90062061/16777216, 132616427/16777216)
A2 = (-7617357/2097152, -15582753/4194304, 2176415/1048576)
A3 = (-1084167/4194304, -203080501/16777216, 15092457/16777216)
A4 = (11665871/16777216, 2552689/2097152, 14525363/4194304)
A5 = (81983851/16777216, -11196039/16777216, -2254373/8388608)
A6 = (22925547/16777216, -3003207/8388608, 141014055/16777216)
B0 = (834078633629/68719476736, -85060200099/17179869184, -158178319309/68719476736)
B1 = (5291169989/1073741824, -23568104843/34359738368, -20992321111/68719476736)
U0 = (21177394457/4294967296, -738188427/1073741824, -1324020611/4294967296)
U3 = (5294262797/1073741824, -2950693633/4294967296, -661227419/2147483648)
U4 = (5294564097/1073741824, -2951120327/4294967296, -330679271/1073741824)
U5 = (10589214001/2147483648, -738037661/1073741824, -1323499607/4294967296)
S = (13485317867/2147483648, -10518707741/4294967296, -3031828833/2147483648)
RU = (3042908219/4294967296, -37112373349/4294967296, 31614776683/4294967296)
H0 = (13444381965/4294967296, -8813590143/4294967296, -701351089/536870912)
H1 = (11600898925/4294967296, -175116595/536870912, -933109729/4294967296)
J0 = (5624210133/1073741824, -792140055/1073741824, 763273275/2147483648)
K0 = (-17103094031/2147483648, -29762103763/2147483648, -5931615123/1073741824)
K2 = (-2299097215/536870912, 18381078381/4294967296, 60532288267/4294967296)
```

Enumerate all `C(26,3)=2600` row triples. For each nonsingular triple `(i,j,k)`, solve exactly

```text
[q_i;q_j;q_k]x=(1,1,1)^T
```

and retain `x` exactly when `q_l·x<=1` for all 26 rows. Exactly 32 feasible simple intersections remain. Orient the maximal-face cycles below outward and sum their signed origin tetrahedra. Let `V` and `M=(Mx,My,Mz)` be the resulting exact ordinary volume and moments and put `c=M/V`. The delivered homogeneous body is

```text
P=P_raw-c.
```

Its exact own-centred H rows and vertices are

```text
H_i=q_i/(1-q_i·c),
p_ijk=x_ijk-c.
```

This is a deterministic exact H/V generator; no floating root, tolerance-based incidence, or stored combinatorics is needed.

## Supplied rows, irredundant rows, and complete incidence

```text
supplied rows: 26
active irredundant rows: 18
active = T27,S102,GR,A0,A3,A4,B0,U0,U3,U4,U5,S,RU,H0,H1,J0,K0,K2
strict inactive = TR,SA5,GT,A1,A2,A5,A6,B1
Q:(V,E,F)=(18,48,32)
P:(V,E,F)=(32,48,18)
complexity=96
```

The exact minimum supplied-row nonincidence is

```text
221788111600776495332553/128308232665114730505191370736 > 0
```

or approximately `1.7285571392729321e-6`. The minimum strict inactive-row support slack is approximately `5.731340893362006e-5`; the exact rational witness is regenerated by both exact verifiers.

### All 32 Q facets / primal vertices

```text
00 T27/S102/H1
01 T27/S102/K2
02 T27/H0/H1
03 T27/H0/K0
04 T27/K0/K2
05 S102/A4/H1
06 S102/A4/K2
07 GR/A0/A3
08 GR/A0/K2
09 GR/A3/RU
10 GR/RU/K2
11 A0/A3/K0
12 A0/B0/S
13 A0/B0/J0
14 A0/S/H0
15 A0/H0/K0
16 A0/J0/K2
17 A3/RU/K0
18 A4/U3/U4
19 A4/U3/H1
20 A4/U4/K2
21 B0/U4/U5
22 B0/U4/J0
23 B0/U5/S
24 U0/U5/S
25 U0/U5/H1
26 U0/S/H1
27 U3/U4/H1
28 U4/U5/H1
29 U4/J0/K2
30 S/H0/H1
31 RU/K0/K2
```

### All 48 true Q edges / dual primal true edges

```text
T27-S102 T27-H0 T27-H1 T27-K0 T27-K2
S102-A4 S102-H1 S102-K2
GR-A0 GR-A3 GR-RU GR-K2
A0-A3 A0-B0 A0-S A0-H0 A0-J0 A0-K0 A0-K2
A3-RU A3-K0
A4-U3 A4-U4 A4-H1 A4-K2
B0-U4 B0-U5 B0-S B0-J0
U0-U5 U0-S U0-H1
U3-U4 U3-H1
U4-U5 U4-H1 U4-J0 U4-K2
U5-S U5-H1
S-H0 S-H1
RU-K0 RU-K2
H0-H1 H0-K0
J0-K2
K0-K2
```

### All 18 maximal primal-face cycles

```text
T27: 0 2 3 4 1
S102: 0 1 6 5
GR: 7 8 10 9
A0: 7 11 15 14 12 13 16 8
A3: 7 9 17 11
A4: 5 6 20 18 19
B0: 12 23 21 22 13
U0: 24 26 25
U3: 18 27 19
U4: 18 20 29 22 21 28 27
U5: 21 23 24 25 28
S: 12 14 30 26 24 23
RU: 9 10 31 17
H0: 2 30 14 15 3
H1: 0 5 19 27 28 25 26 30 2
J0: 13 22 29 16
K0: 3 15 11 17 31 4
K2: 1 4 31 10 8 16 29 20 6
```

Both Euler identities hold exactly: `18-48+32=2` and `32-48+18=2`.

## Exact mass and first moments

The exact ordinary volume is

```text
258922706548463383050805161176100503700612609253464281219400691643113928352285962127994065369093882627095728394501869038703394420376299439951209639842481374554505048873254769978541785963931026673073670171302837530855859712947844035042574110106610900321286334017810994156888345272060162914777123517953567673228002379158135040312074339949150359238689580689689360058829732975428011473068524766998961047208874064307679702560024800957508667760884237419926256915739050304765839404286442730531774706298627571635425034367481188387987050481483662678131528870936842694078778671331725325804738375218193782997478445490768511377641487864383776404907633532154915130305161003994987242006211314709620932775434513544131478956318318207223772510930620738534396224212897568704350807796481862412701943016966650175967287152163977012055818505289728/1210933923014383581665352539650263310254086669881421889898490419440030500649959942737840729421445450242640866377266868558893811445529782799893560831879719027028353216336231494343649453823352392262743784004904442568016299066910275510848267854863729807399950786098648891465850572347304588068818572656288105884790727835046895081416793225654872993886410302412962875238249342461047043969079568705126446592662453737545155958239956326194843116374205904471762515899408533564494281087975699537327097247145081639339005028670631976952521151218477277201795065711437369866539740529261219782006521640006575117293662376626868450435864243216903856647223111230583773168075075262814787483340710360820517993333300366955054187532179826195070066206669907727271534902539560350337666930942972650277022362553005170045384687152991918924616316290705
```

Numerically, `V≈213.82067314121142`. The exact raw centroid regenerated by signed-tetrahedron summation has orientation value

```text
c≈(-0.36611504408245066, 8.071035792821691, -9.761987339437463).
```

After translation by the exact rational `c`, the ordinary-volume first moments are exactly

```text
(Mx,My,Mz)=(0/1,0/1,0/1).
```

The full exact raw moment and centroid fractions are deterministically regenerated in `exact_mass_centroid.json`; they are not numerical assumptions.

## Literal deletion of the P9-XG15 packet

The exact rebuilt hull proves:

```text
TR is strictly inactive.
TR-B1 is absent.
SA5-A0 is absent.
S102-GT is absent.
A1/A2/A6 is not an actual facet.
```

Because `TR` occurs in no actual facet or edge, its entire old degree-six link cycle is absent. The construction therefore does more than relabel or subdivide `TR-B1`.

## Eleven-row full-dimensional replacement cell

The active replacement rows are

```text
U0,U3,U4,U5,S,RU,H0,H1,J0,K0,K2.
```

Their convex Q subpolytope has f-vector `(11,27,18)` and exact volume

```text
72165845770584616164532806676481/118842243771396506390315925504 > 0
```

or approximately `607.2406871533153`.

Its complete supporting triangles are

```text
U0/U5/S
U0/U5/H1
U0/S/H1
U3/U4/H1
U3/U4/K2
U3/H1/K2
U4/U5/S
U4/U5/H1
U4/S/J0
U4/J0/K2
S/RU/J0
S/RU/K0
S/H0/H1
S/H0/K0
RU/J0/K2
RU/K0/K2
H0/H1/K0
H1/K0/K2
```

A face-to-face star triangulation consists of the following fourteen exact positive tetrahedra:

```text
RU/U0/U5/S
RU/U0/U5/H1
RU/U0/S/H1
RU/U3/U4/H1
RU/U3/U4/K2
RU/U3/H1/K2
RU/U4/U5/S
RU/U4/U5/H1
RU/U4/S/J0
RU/U4/J0/K2
RU/S/H0/H1
RU/S/H0/K0
RU/H0/H1/K0
RU/H1/K0/K2
```

The exact sum equals the cell volume. The minimum tetrahedron volume is

```text
73591530500517629083208429/237684487542793012780631851008 > 0.
```

Take `H1` as target descendant and `RU` as return descendant. They share no boundary true edge. Two internally vertex-disjoint boundary routes are

```text
H1-H0-K0-RU
H1-U4-K2-RU.
```

Two genuine interior communication pages are

```text
RU-H1-H0, shared by RU/S/H0/H1 and RU/H0/H1/K0;
RU-H1-U4, shared by RU/U3/U4/H1 and RU/U4/U5/H1.
```

Every incident tetrahedron has strictly positive exact volume. The complete scaled predecessor hull is strictly contained in the endpoint hull in 832 exact outer-facet/inner-row tests, with minimum relative slack `63/64`. The exact positive shell volume is

```text
90683156255538786073429836317438727191/62307562302417931542365955950641152 > 0.
```

This certifies physical coexistence and full dimensionality, though not simultaneous equilibrium cancellation.

## Exhaustive own-centred mechanics

At the exact own centroid the complete equilibrium set is

```text
stable maximal faces: T27, H1
unstable vertices: T27/S102/H1, GR/RU/K2
horizontal saddles: S102-H1, H0-K0
class: (S,U,H)=(2,2,2)
```

Every maximal face is audited against its complete true-neighbour star. Every one of the 32 vertices is tested in its full active normal cone. Every one of the 48 true edges is tested using all four strict components `t,1-t,alpha,beta`.

The exact-point ledgers and interval chamber certify global lower bounds including

```text
positive mechanics component >= 0.17294577744146822
negative-witness separation >= 0.0028407548543584646
projective denominator >= 0.3811449547617849.
```

## Complete changed-edge external-arrow audit

For a directed row endpoint `u` and an external true neighbour `z`, define exactly

```text
A(u→z)=H_u·(H_u-H_z).
```

There are 43 inserted or inherited-star-changed nonprotected true edges. Forty-two have an exact strict negative external-arrow witness. The full census is:

```text
A4-S102: S102→T27 < 0
H1-S102: S102→T27 < 0
K2-S102: S102→T27 < 0
A0-GR: A0→S < 0
A3-GR: GR→A0 < 0
GR-RU: GR→A0 < 0
GR-K2: K2→S102 < 0
A0-A3: A0→S < 0
A0-B0: B0→U5 < 0
A0-S: S→H1 < 0
A0-H0: H0→H1 < 0
A0-J0: J0→U4 < 0
A0-K0: A0→S < 0
A0-K2: A0→S < 0
A3-RU: A3→K0 < 0
A3-K0: A3→A0 < 0
A4-U3: U3→H1 < 0
A4-U4: U4→H1 < 0
A4-H1: A4→S102 < 0
A4-K2: K2→S102 < 0
B0-U4: B0→U5 < 0
B0-U5: B0→U4 < 0
B0-S: S→H1 < 0
B0-J0: J0→U4 < 0
U0-U5: U0→H1 < 0
S-U0: S→H1 < 0
H1-U0: U0→U5 < 0
U3-U4: U3→H1 < 0
H1-U3: U3→U4 < 0
U4-U5: U5→H1 < 0
H1-U4: violation; every endpoint-external arrow is positive
J0-U4: U4→H1 < 0
K2-U4: U4→H1 < 0
S-U5: S→H1 < 0
H1-U5: U5→U4 < 0
H0-S: S→H1 < 0
H1-S: S→U5 < 0
K0-RU: K0→T27 < 0
K2-RU: K2→S102 < 0
H0-H1: H0→S < 0
H0-K0: H0→H1 < 0
J0-K2: J0→U4 < 0
K0-K2: K2→S102 < 0
```

Thus the assignment's all-changed-edge anti-carrier condition fails at exactly one edge: `U4-H1`.

## Exact residual forcing component

The unique nonprotected all-external-positive true edge is

```text
U4-H1
incident link: U3,U5.
```

Its mutual arrows have orientation values

```text
A(U4→H1)=0.17294577748576762
A(H1→U4)=-0.14726908229706040.
```

They obey the exact identity

```text
A(U4→H1)+A(H1→U4)=||H_U4-H_H1||²>0,
```

with squared-length orientation value `0.02567669518870722`. Every endpoint-external arrow is strictly positive; the exact minimum has orientation value `1.206798443426296e-6`. Consequently at least one endpoint remains stable throughout the complete fixed-incidence/external-sign chamber. Here it is `H1`. Since `T27` remains independently stable, `S>=2` throughout the certified chamber.

The complete Euler-neutral residual packet is

```text
extra stable: H1
extra unstable: GR/RU/K2
saddles: S102-H1; H0-K0
index: +1+1-2=0.
```

This is an exact forcing theorem, not an inference from numerical nonhits.

## Exact ingress chronology

Define the exact affine ingress

```text
q(t)=(1-t)q_pre+tq_post,
```

where every old XG15 row in `q_pre` is scaled by `1/64` and every future row is scaled by `1/16384`. At `t=0`, the active body is exactly similar to XG15 and all future rows are strict interior points. At `t=1`, the exact endpoint above is reached.

Eight complete Fraction rebuilds give:

```text
t=0: class (2,2,2); stable T27,TR; TR active; carrier TR-B1
t=4/125: class (3,2,3); stable T27,TR,H1; TR active; carriers TR-B1,TR-S,TR-H1
t=33/1000: class (2,2,2); stable T27,H1; TR active; carrier TR-H1
t=991/1000: class (2,2,2); stable T27,H1; TR active; carrier TR-H1
t=124/125: class (2,2,2); stable T27,H1; TR active; carrier U4-H1
t=249/250: class (2,2,2); stable T27,H1; TR active; carrier U4-H1
t=997/1000: class (2,2,2); stable T27,H1; TR inactive; carrier U4-H1
t=1: class (2,2,2); stable T27,H1; TR inactive; carrier U4-H1
```

Therefore `H1` is born before `TR` dies, and the carrier changes before `TR` becomes inactive. No certified checkpoint is `(1,1,0)`. This exact chronology proves that the materialized ingress is a serial transfer rather than the requested joint cancellation.

## Seven independent controls after the moment equations

Seven named physical controls are

```text
u1=U4_z
u2=H1_z
u3=H0_x
u4=K0_y
u5=RU_x
u6=K2_z
u7=S102_z.
```

After varying them, apply

```text
q_i→q_i/(1-q_i·tau).
```

The primal translates by `-tau`, so its centroid residual is `c(u)-tau`. The exact block Jacobian of `(u,centroid residual)` with respect to `(u,tau)` is

```text
[[I_7,0],[Dc(u),-I_3]],
```

with determinant `-1` and rank 10. Hence seven independent physical shape controls remain after the three ordinary-moment equations. The full interval chamber actually permits all 54 active raw coordinates to vary independently before applying the three dependent translation controls.

## Positive perturbation chamber

Outward interval arithmetic certifies the independent active-coordinate box

```text
|delta q_ij|<=2^-57=1/144115188075855872
```

for all 54 active coordinates, with all 24 inactive-row coordinates fixed. It preserves the active/inactive set, all 32 vertices, all 48 true edges, all 18 maximal faces, exact moment closure by dependent projective translation, strict `(2,2,2)` mechanics, the full-star cell, both routes, both pages, and the `U4-H1` forcing theorem.

Certified lower bounds and enclosures are

```text
Q orientation: 3.984611402587062e-9
primal nonincidence: 1.728557139067085e-6
inactive-row slack: 5.731340654303752e-5
surface tetrahedron determinant: 7.686536194720847e-5
projective denominator: 0.3811449547617849
positive mechanics component: 0.17294577744146822
negative-witness separation: 0.0028407548543584646
residual external arrow: 1.2067691480246899e-6
residual squared edge length: 0.025676695176863957
volume: [213.8206731402459,213.82067314217693]
centroid x: [-0.36611504408610285,-0.3661150440787984]
centroid y: [8.07103579275386,8.071035792889521]
centroid z: [-9.761987339519493,-9.76198733935543].
```

The tested boxes `2^-42` through `2^-56` fail closed at a true-edge Gram-determinant enclosure. No larger perturbation claim is made.

## Exact self-break: one-page diagonal exchange

Reflect `U4` exactly through the affine plane `U3-U5-H1`, leaving every other supplied row fixed. The resulting exact rational endpoint has the same primal f-vector `(32,48,18)` and strict class `(2,2,2)`. It deletes `U4-H1` and inserts `U3-U5`, but the complete nonprotected external-positive component becomes `U3-H1`. Stable faces remain `T27,H1`; the two unwanted saddles and remote unstable facet remain.

This closes the obvious one-page `2↔2` escape: it transfers the forcing edge rather than cancelling the residual.

## Smallest genuinely unrepresented successor

The first topology not represented by XG12–XG16 or the exact simple flip is **P9-XG17-U4H1-THETA3-DC2**, a nonannular three-page theta / double-octahedral two-cell replacement.

It must, in one connected full-dimensional event:

1. Delete `U4-H1` and replace both incident facets `U3/U4/H1` and `U4/U5/H1`; a serial subdivision or one-page diagonal is inadmissible.
2. Jointly remove stable `H1`, remote unstable facet `GR/RU/K2`, and saddles `S102-H1`,`H0-K0` before any substitute packet is born.
3. Permit `U3,U4,U5,H0,H1,K0,K2,RU` to deactivate together.
4. Add a third transverse return band joining the collar to the `GR/RU/K2` sector.
5. Supply three internally vertex-disjoint target/return routes with target and return descendants nonadjacent.
6. Give every inserted or star-changed nonprotected edge an exact negative external witness before moment closure.
7. Preserve `T27` as the sole stable face and one `T27/S102/target` unstable vertex, with no saddle.
8. Retain at least seven independent shape controls after the three moment equations.

A plausible minimum is two overlapping positive-volume prismatic/octahedral cells, one remote return cell, and six to eight additional active rows beyond the present eleven-row collar. The topology must be enlarged whenever a one-edge, two-edge-path, or one-page relay survives. A future nonwinner is continuation-worthy only if its residual is no longer the carrier mechanism already represented here.

## Independent verification and watertight meshes

`verify_independent.py` imports neither `exact_core.py` nor `generate_endpoint.py`. Starting from the two exact row files, it independently reconstructs:

- the P9-XG15 parent;
- all 2600 endpoint triple tests and complete H/V/E incidence;
- exact volume, first moments, centroid, and own-centred rows;
- every face, vertex, and four-component true-edge mechanical decision;
- strict inactivity and deletion of every named old feature;
- the eleven-row subpolytope, all fourteen positive tetrahedra, routes, and pages;
- every changed-edge external-arrow sign and the residual pair-sum theorem;
- the exact simple-flip self-break;
- OBJ and STL edge multiplicities.

It terminates with

```text
P9_XG16_TRFS11_FP5_INDEPENDENT_CLEAN_ROOM_PASS
```

The triangulated OBJ and STL have 32 exact-coordinate vertices, 60 surface triangles, 90 undirected mesh edges, Euler characteristic 2, and every edge used exactly twice. The maximal-face OBJ has the same 18 actual face cycles.

## Empirical search scope

Numerical work was used only to choose exact seeds. A 50,000-proposal packet-cap campaign found 18 valid post-TR states and no state without a replacement carrier. A 500-generation coordinate evolution preserving all required inactive rows and all eleven active new rows ended in `(2,2,2)` or larger classes. Generic optimization improved its score only by reactivating forbidden predecessor rows. Local H1-star and residual-cap probes likewise transferred the packet. These observations are not exclusions, and no timed or interrupted computation is treated as evidence.

The exact result closes only the materialized endpoint, its `2^-57` chamber, the stated affine ingress, and the exact one-page flip. It does not exclude every XG16 placement, every simultaneous ingress, or P9-XG17.

## Package integrity and hashes

The deterministic archive has 40 entries and SHA-256

```text
0a1c1ee55fa7387f0d67dfc89d0b479374f35c70cd7d19ee30f823b41bd5fe46
```

The source manifest covers 39 core files totaling 26,077,872 bytes and has SHA-256

```text
891b1a7db0f5714ea0febbf96d2662af002f0bc03b74b33bc5070718db30a074
```

Continuation-critical hashes are

```text
parent rows: 32d3a5c1b3e48eb4113686d3b56660ad46be1e85083e9c72a85afaa573fe0a67
XG16 rows: efb950648e93336f71314b068273f6376dd9c328ef3fa725f2e633ea1e5e9f74
XG16 ledger: 11e430cc122a246c0fb6b1c4155541bc311c5d57ad4b5f0dff0bf8b3622f6362
mass/centroid: ea9df559e55a811ba61da7e2f6c7b3b246c9019fe66e42f275de9ae7f5c82bc8
full-star cell: a4033524be5ccae29b1ea544cd9a498960cd74977537afd81408af038ebca8e3
changed-edge audit: fd367d8e3e730d6a8e7bb6ca339618ac57535ba1cbe42d9e697b89b7793a6d60
residual theorem: ba5387c2590dbe7e99e3caeec12549f60c240f26c34c73f2e0b3945f9a73ae4e
chronology: c76433fcd23de42f15836fc465c450c52923635016fe887b10b1bf324421b2c3
control certificate: a01dabc6e8067fbd77e9a16f92e870f0797e867317c29fded5429ad978e10a3e
perturbation certificate: 4ea042e7bfb26ca75dec40a0e5aee56a36b0a1b856ac9ea34844e5e337048065
independent verifier: 78e6e6129f6d0be2c0dd87f53a1dc937bbb27c74008771540d34df135b3eadf6
independent report: 8c2e57787e8f6e513ee4d8ab1cf29d257c53519951140d7954d8a030942f5b00
triangulated OBJ: 50f135ae7275b4d3aaf259767fefa0a43ffc9e28ade102c50d6d10b7f3e463db
STL: f74293e0e886439f4e788a27b263a93e59a40c19ff35159e35529e13b33533e7
simple flip: 6db0ca29507859ebcfbd9729792c3be06e85fdfd768d0d662d0d4073c1dd46f8
XG17 specification: 0a40dd62b3e93dce56477317135a24c4624c390c77ccec52dd5972d33d1887ac
```

Fresh extraction passed ZIP CRC, source and extracted manifest checks, independent clean-room reconstruction, separate regeneration of the parent, endpoint, interval certificate, chronology, controls, simple flip, and independent report, plus byte-identical manifest regeneration.

## Reproduction and artifacts

A clean extraction followed by

```bash
./RUN_ALL.sh
```

must terminate with

```text
ALL QUIET QUARTZ 19 P9-XG16 EXACT NONWINNER CHECKS PASS
```

- [Complete exact package](sandbox:/mnt/data/Quiet_Quartz_19_P9_XG16_TRFS11_FP5_exact_nonwinner.zip)
- [Archive SHA-256 receipt](sandbox:/mnt/data/Quiet_Quartz_19_P9_XG16_TRFS11_FP5_SHA256.txt)
- [Verification receipt](sandbox:/mnt/data/Quiet_Quartz_19_P9_XG16_TRFS11_FP5_VERIFICATION_RECEIPT.json)
- [Detailed handoff](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/RESEARCH_HANDOFF.md)
- [Package README](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/README.md)
- [One-command replay](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/RUN_ALL.sh)
- [Exact 26-row input](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/p9_xg16_trfs11_fp5_rows_exact.json)
- [Exact parent rows](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/p9_xg15_cd2_parent_rows_exact.json)
- [Complete exact endpoint ledger](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/p9_xg16_trfs11_fp5_exact_ledger.json)
- [Exact H representation](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/H_supplied_exact.csv)
- [Exact V representation](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/V_exact.csv)
- [Maximal faces](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/maximal_faces.csv)
- [Full true-edge cones](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/true_edges_full_cones.csv)
- [Exact mass and centroid](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/exact_mass_centroid.json)
- [Full-star cell certificate](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/full_star_cell_certificate.json)
- [Changed-edge audit](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/changed_edge_arrow_audit.json)
- [Residual forcing theorem](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/residual_forcing_component.json)
- [Exact ingress chronology](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/affine_ingress_chronology.json)
- [Seven-control certificate](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/control_rank_certificate.json)
- [Perturbation chamber](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/perturbation_chamber.json)
- [Independent clean-room verifier](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/verify_independent.py)
- [Watertight triangulated OBJ](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/p9_xg16_trfs11_fp5_centered_triangulated.obj)
- [Watertight STL](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/p9_xg16_trfs11_fp5_centered.stl)
- [Exact simple-flip nonwinner](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/p9_xg17_cd1_exact_nonwinner.json)
- [P9-XG17 successor specification](sandbox:/mnt/data/quiet_quartz19_p9xg16_trfs11_fp5/P9_XG17_successor_spec.json)

## Final status

**USED exact delimited nonwinner.** This work materially advances beyond P9-XG15 by making `TR` and the complete named predecessor packet strictly absent in a fully exact post-event hull, supplying an eleven-row finite-thickness communicating cell, and contracting the complete obstruction to one exact forcing edge. It also proves that the natural ingress and the obvious diagonal exchange are transfers rather than cancellations. The requested simultaneous P9-XG16 success is not claimed. The evidence-supported continuation is P9-XG17-U4H1-THETA3-DC2, not another serial cap, edge subdivision, or one-page flip.
