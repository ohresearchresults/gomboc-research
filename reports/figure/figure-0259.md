# figure-0259

AI research report · 2026-09-03 UTC

---

# Calm Raven 06 — exact coupled D–E–F physical co-surgery determination

## Artifacts and replay

- [Exact replay bundle](sandbox:/mnt/data/Calm_Raven_06_coupledDF5_exact_NONWINNER.zip)
- [Archive SHA-256](sandbox:/mnt/data/Calm_Raven_06_coupledDF5_exact_NONWINNER.zip.sha256)
- [Full report](sandbox:/mnt/data/Calm_Raven_06_coupledDF5_exact_NONWINNER/RESULT.md)
- [Master exact certificate](sandbox:/mnt/data/Calm_Raven_06_coupledDF5_exact_NONWINNER/coupledDF5_master_certificate.json)
- [Independent clean-room receipt](sandbox:/mnt/data/Calm_Raven_06_coupledDF5_exact_NONWINNER/independent_coupledDF5_verification.json)
- [Independent full-GMP receipt](sandbox:/mnt/data/Calm_Raven_06_coupledDF5_exact_NONWINNER/independent_coupledDF5_full_gmp_verification.json)
- [Watertight OBJ](sandbox:/mnt/data/Calm_Raven_06_coupledDF5_exact_NONWINNER/endpoint/endpoint_centered.obj) and [STL](sandbox:/mnt/data/Calm_Raven_06_coupledDF5_exact_NONWINNER/endpoint/endpoint_centered.stl)
- [Pristine replay transcript](sandbox:/mnt/data/coupledDF5_pristine_replay.log)

Archive SHA-256: `be9bb0a6d02bdd632b59f7199eb7516f12e3014b22be3031d6042b6e4d319f7`.

A pristine extraction checked all 117 immutable manifest entries and ended with:

```text
INDEPENDENT_EXACT_COUPLED_D_E_F_FAST_PASS
INDEPENDENT_EXACT_COUPLED_D_E_F_PASS
INDEPENDENT_RELEASE_SUMMARY_PASS
MANIFEST_PASS 117
ALL_EXACT_COUPLED_D_E_F_VERIFIERS_PASS
```

The governing acceptance gate is a finite uniform-density convex polyhedron evaluated at its own exact ordinary-volume centroid, strict `(S,U,H)=(1,1,0)`, with expanded exact H/V data, exhaustive maximal-face/vertex/true-edge mechanics, independent verification, and matching OBJ/STL. :contentReference[oaicite:0]{index=0} The accepted physical-E8 result had already isolated paired physical edge surgery as the first nonrepeating route beyond mechanically silent secondary lifts. :contentReference[oaicite:1]{index=1}

## Literal disposition

**EXACT NONWINNER.** A genuinely coupled physical co-surgery was materialized: the exact `closededge21` summand `D` is changed by a nonsingular affine map, the exact `E10` corrector is retained, and an independent five-vertex corrector summand `F5` is added. All four unwanted equilibria of the accepted E10 source become strictly noncritical. The actual common fan changes from `(V,E,F)=(124,246,124)` to `(168,337,171)`.

At the exact positive moment root `(t1,t2,t3)=(1,1,1)`, the promoted homogeneous body has exact ordinary centroid zero and strict class `(S,U,H)=(2,2,2)`. It is therefore not the requested Gömböc.

The new result is nevertheless structurally stronger than a serial relay: the co-surgery breaks one spoke of the former all-positive unstable forcing component and creates an exact nonforcing cross-summand exit `70→69→71`. The remaining three spokes still force a second maximum in the certified cell.

## 1. Exact finite Minkowski family

```text
P(t1,t2,t3)=B+t1*C1+t2*C2+t3*C3
             +(10677075263/4294967296)*D' + E10 + F5.
```

`C1,C2,C3` are retained solely as dependent rank-three controls for the three ordinary first moments.

The exact summand f-vectors are:

```text
D'       = (16,25,11)
E10      = (10,24,16)
F5       = (5,9,6)
E10+F5   = (22,51,31)
```

### Physical D co-surgery

`D'` is obtained from the exact source D by

```text
D' = A*(D-Dmean)+Dmean,

A =
[ 4233522741/4294967296   -238111237/2147483648    137247037/4294967296 ]
[  152888333/2147483648   4731087449/4294967296    -10913823/536870912  ]
[ -352969041/4294967296    280001789/4294967296   4512150817/4294967296 ].
```

Its exact determinant is

```text
11420179109265085368468904289/9903520314283042199192993792 > 0
```

with decimal locator `1.1531434022298808`. This is a nonsingular physical deformation, not a regular-subdivision lift. The complete 21 supplied D rows remain represented; active supplied rows are `[0,1,4,5,7,8,11,15,17,18,19,20]`. The actual transformed D lattice remains `(16,25,11)`. Every source active-set incidence is preserved, including protected `D045` and `D048`.

Expanded data are in:

```text
endpoint/D_H_supplied.csv
endpoint/D_V_supplied_incidence.csv
endpoint/D_H.csv
endpoint/D_V.csv
endpoint/D_edges.csv
endpoint/D_faces.csv
```

### Exact independent F5 corrector

```text
f0 active(0;1;2;3) = (0/1, 0/1, 0/1)
f1 active(2;3;4;5) = (-16480109673/2147483648,
                        21098466555/67108864,
                       -680380039461/4294967296)
f2 active(0;2;4)   = (102426236345/4294967296,
                      -212972557057/2147483648,
                     -1771704341045/4294967296)
f3 active(0;1;4;5) = (37581314777/536870912,
                       -55664404611/1073741824,
                       207795960623/536870912)
f4 active(1;3;5)   = (145263459597/2147483648,
                      -190663453659/4294967296,
                      1644262553149/4294967296)
```

Its six exact irredundant supporting rows are:

```text
F0 = (-1/1,
      -175733473413794435129800/275640215610977985624539,
       26313659359796845138361/275640215610977985624539;
       h=0/1), cycle 0;2;3

F1 = (-1/1,
      -2846456650336669369822/12288705027660329630925,
       613747147848151721816/4096235009220109876975;
       h=0/1), cycle 0;3;4

F2 = (-1/1,
      -42694843474452134422205/894046739927274409350318,
      -20711182168289011300826/447023369963637204675159;
       h=0/1), cycle 1;2;0

F3 = (-1/1,
       47824487443830485097960/696842391643972188930227,
       128671576658136144446622/696842391643972188930227;
       h=0/1), cycle 1;0;4

F4 = (1/1,
      681253816161536834964703/5877907459242366950578106,
      -27115546735656966467656/419850532803026210755579;
      h=246111362557020429855216275510427927/
        6311355076590104747591053390905344), cycle 1;3;2

F5 = (1/1,
      153712801624804617448/404135808921096567699,
      1750138040385987932346/15491872675308701761795;
      h=781880203469783771911896245045653/
        8317135811780862596390888407040), cycle 1;4;3
```

Its nine true edges are:

```text
01[F2,F3]
02[F0,F2]
03[F0,F1]
04[F1,F3]
12[F2,F4]
13[F4,F5]
14[F3,F5]
23[F0,F4]
34[F1,F5]
```

Exact exhaustive H reconstruction gives `F5:(V,E,F)=(5,9,6)` and Euler two.

## 2. Actual common-fan transition

| object | exact `(V,E,F)` |
|---|---:|
| accepted E10 source | `(124,246,124)` |
| coupled D′+E10+F5 endpoint | `(168,337,171)` |

The exact H/V/E symmetric differences are nonempty. After projecting away the new F label, the source has 124 P9–D–E common vertices and the target has 123; four projected vertices are removed and three are inserted. Thus the result changes the physical common normal fan rather than polishing a fixed lattice.

The final lattice satisfies

```text
168-337+171=2,
C=168+337+171-2=674.
```

The minimum exact nonincident slack is

```text
130980129111214390767411582325623401948894767693172030238453832119186741761322157010339369039510227141934885502982881035051052733350923092515419529928707101741833625932257062513
/
90654983519680671408884831540514755227680281754461382147107523552028359201187835358502701415275714609040418552262033572462477645641674391968861732541046633219212307885298544810131456
```

with decimal locator `1.4448199539165915e-06`.

The complete transition atlas is `DF5_common_fan_transition_atlas.json`.

## 3. Positive-volume full-dimensional mixed cells

Two exact certificates isolate the coupled geometry.

### D–E–F mixed cell

At final common vertex 93, the pure D, E and F true-edge directions have exact determinant

```text
-172204991968006479433483345749894211517448704818969047621375575949517100562825605693297154202718044850715014314726751
/
180611393598329504412066355460948412279208017461737510120189031397092825269088695278270778051049523548138766336
```

with decimal locator `-953455.8619872098`. Its absolute determinant gives a positive local mixed parallelotope volume. Because the three directions are linearly independent, no nonzero supporting normal is orthogonal to all of them; the mixed cell is full-dimensional and nonboundary.

### Local P9–D–F cell at the replacement maximum

At extra unstable vertex 70, pure P9, D and F edge directions have exact determinant

```text
-651126881685990723486730304948175717131141395874295679399347454320397774353890249319372784514615427274995540683255733249318132156865741888192546280787882883694452555412188313163491605576592275338499775079848063
/
16545010097245553755183895545026482223317438989622513975785950409773762128651126847477719515503847020178847409994273341775291832994844569881515697778577057713182989125515673887504732063454593874836229678170112
```

with decimal locator `-39.3548796802724`. The corresponding tetrahedral volume is positive, with decimal locator `6.559146613378734`. Six of the eight local cube corners are actual common vertices. This physical cell contains the F-mediated nonforcing exit described below.

Certificates:

```text
positive_volume_D_E_F_mixed_cell_certificate.json
DF5_positive_volume_mixed_cell_certificate.json
```

## 4. Exact ordinary volume and moment closure

The final mixed system has exactly 20 nonzero volume coefficients and 35 coefficients in each first-moment component. The independent full-GMP replay freshly recompiles the coefficient engine and matches all 125 coefficients exactly.

The ordinary first-moment equations have the exact positive root

```text
(t1,t2,t3)=(1,1,1),
```

isolated in

```text
[1-2^-18,1+2^-18]^3
```

because the certified rational radius is `1/262144`.

The exact moment-control Jacobian determinant is nonzero; its decimal locator is `3.703508414559418e21`.

Exact tetrahedral integration gives:

```text
volume  = 230143217.24297464…
Mx      = 0/1
My      = 0/1
Mz      = 0/1
centroid= (0/1,0/1,0/1).
```

The complete reduced volume fraction, all mixed coefficients, exact Jacobian, inverse preconditioner and Krawczyk inclusion are in:

```text
endpoint/exact_certificate.json
endpoint/root_certificate.json
endpoint/mixed_volume_first_moments.csv
```

## 5. Exhaustive own-centroid mechanics

Every one of the 171 maximal faces, 168 vertices, 337 true edges and 1,348 four-component edge-cone primitives is exact and nonzero.

| type | id | exact lineage | normalized margin |
|---|---:|---|---:|
| intended stable | 35 | `P9edge(15;27)|Dvertex(0;4;5)|Eedge(0;2)|Fvertex(2;3;4;5)` | `0.0021345658285859765` |
| extra stable | 150 | `P9vertex(9;13;26)|Dvertex(18;19;20)|Eface(9)|Fvertex(0;1;4;5)` | `0.004891712521478506` |
| extra unstable | 70 | `P9[9;100;103]|D[1;7;11]|E[0;2;7;9;10;12]|F[0;1;4;5]` | `0.00028634831402465184` |
| intended unstable | 107 | `P9[15;26;27]|D[0;4;8;17;18;20]|E[3;7;8;9;11;13;15]|F[0;2;4]` | `0.4167327237216256` |
| saddle | 5 | `P9edge(13;26)|Dedge(4;5)|Evertex(2;6;12;14)|Fvertex(2;3;4;5) || P9face(26)|Dvertex(0;4;5)|Evertex(2;6;12;14)|Fvertex(2;3;4;5)` | `0.0017980195157336607` |
| saddle | 277 | `P9vertex(15;26;27)|Dedge(1;15)|Eedge(0;7)|Fvertex(0;2;4) || P9vertex(15;26;27)|Dedge(1;20)|Eedge(0;7)|Fvertex(0;2;4)` | `0.0018735057552714323` |

Hence the exact own-centroid class is

```text
(S,U,H)=(2,2,2).
```

All remaining 165 faces, 166 vertices and 335 true edges have at least one strict negative exclusion component.

## 6. Exact genealogy of the E10 packet

The E10 source packet was:

```text
S114
U50
H134
H199.
```

`DF5_carrier_genealogy_certificate.json` proves:

- all four exact source critical identity strings are absent from the target critical set;
- all tracked geometric descendants are strictly noncritical and have explicit exact negative witnesses;
- intended stable E10 id 27 survives as target stable id 35 with protected D045;
- intended unstable E10 id 70 survives as target unstable id 107 with protected D048.

The source packet is therefore genuinely destroyed rather than merely renamed. The replacement Euler-neutral packet is `S150/U70/H5/H277` on different P9+D carriers.

## 7. External-arrow ledger and nonforcing cross-summand exit

Extra unstable vertex 70 has four strictly positive outgoing arrows:

```text
70→43 = 72.61456742325441
70→68 = 22.61480534959755
70→69 = 772536.2250378169
70→72 = 0.10205236671545385
```

The spoke classification is:

```text
43: forcing, reverse mutual arrow -71.28700101781345
68: forcing, reverse mutual arrow -22.61170917419025
69: nonforcing, reverse mutual arrow -128874.16173114703
72: forcing, reverse mutual arrow -0.018573636835159356
```

For neighbours 43, 68 and 72, every nonmutual external arrow is positive. The exact mutual-arrow identity therefore gives a U–H–U transfer along each of those three spokes.

The fourth spoke is different:

- edge `70–69` changes only the F component;
- edge `69–71` changes only the D component;
- the exact arrow `69→71` is strictly negative, with decimal locator `-50.12525877043108`.

Thus the coupled D–F surgery supplies the requested negative external arrow from another summand and breaks one spoke of the former fully forcing component. The local route

```text
70 → 69 → 71
```

is an exact physical nonforcing exit. Nevertheless U70 remains strict, the three other spokes remain forcing, and intended U107 is independently strict. Therefore the displayed cell still has `U≥2`.

## 8. Exact death-before-birth chronology

The certified physical ingress is

```text
D(t)=A(t)*(D-Dmean)+Dmean,
A(t)=I+t*(A-I),
F(t)=tF,
E10 fixed,
C controls fixed at 1,
```

with each body rebuilt and evaluated at its exact own ordinary centroid.

| exact t | actual common `(V,E,F)` | class | source `[S,U,H1,H2]` still present |
|---:|---:|---:|---|
| `1/8` | `(169,339,172)` | `(2,2,2)` | `[true,true,true,true]` |
| `1/4` | `(169,339,172)` | `(2,2,2)` | `[false,true,true,true]` |
| `1/2` | `(169,339,172)` | `(2,3,3)` | `[false,true,true,true]` |
| `3/4` | `(168,337,171)` | `(2,2,2)` | `[false,true,false,false]` |
| `7/8` | `(168,337,171)` | `(2,2,2)` | `[false,true,false,false]` |
| `1` | `(168,337,171)` | `(2,2,2)` | `[false,false,false,false]` |

At `t=1/2`, a third unstable vertex and third saddle are already strict while source U and both source saddles remain. All source unwanted carriers are absent only at `t=1`. Replacement birth therefore precedes complete predecessor death on this exact physical ingress.

This is a rigorous theorem for the displayed path, not a continuum exclusion of all nonlinear D–F co-surgeries.

## 9. Positive-dimensional centred chamber

Fix F vertices `f0…f3` and vary all three Cartesian coordinates of `f4` independently.

- Shape-only radius `2^-40` preserves F5, common `(168,337,171)`, protected D045/D048 descendants, and own-centroid `(2,2,2)`.
- Shape×control radii `2^-44` and `2^-42` preserve the same actual fan and mechanics.
- A 150-digit parametric Krawczyk theorem uses F-shape radius `2^-60` and dependent-control radius `2^-44`. For every physical F shape in this three-dimensional box, there is exactly one positive moment-closing control triple.

Therefore three independent physical F-shape coordinates survive ordinary-moment elimination. `C1,C2,C3` remain dependent moment controls and contribute no independent shape dimension.

## 10. Search scope and attempted falsification

The included finite locator batches report:

```text
samples: 9600
valid exact-fan numerical reconstructions: 9311
observed (1,1,0), (2,1,1), or (1,2,1): 0
```

Additional CMA/SLP searches varied D and F jointly and tested tetrahedral, bipyramidal and segment-like fourth correctors. They selected the exactified endpoint above and found no better state. These computations are discovery evidence only; they are not continuum exclusions and do not prove support-count minimality.

## 11. Independent clean-room replay and mesh

`verify_coupledDF5_cleanroom.py` imports neither `exact_core.py`, the endpoint generator, search code, chronology builder nor interval certifiers. It independently:

- reconstructs all 21 supplied D rows and the transformed active D lattice;
- reconstructs E10, F5 and `G=E10+F5` from exact rows and feasible triples;
- rebuilds the complete common H/V/E lattice;
- recomputes exact volume, first moments and every face/vertex/full-edge-cone primitive;
- freshly compiles the GMP mixed-moment engine and matches all coefficients;
- verifies genealogy, actual fan transition, external arrows, both mixed cells, chronology and directed boxes;
- checks the OBJ/STL against the exact incidence data.

The final mesh has:

```text
168 vertices
332 outward triangles
498 triangulation edges
all mesh edges incident to exactly two triangles
168-498+332=2.
```

## 12. Exact scope and next nonrepeating topology

This determination is exact for the displayed affine-D + E10 + F5 common-fan cell, the physical ingress samples, and the certified shape/control boxes. It does not exclude other D–E co-surgeries, other five-vertex F realization components, or nonlinear paths.

The first genuinely nonrepeating successor should exploit the nonforcing route already created rather than add an unrelated serial page. The evidence-supported topology is a **closed physical D–F gate around `70–69–71`**:

- an edge-sharing paired-Radon or triangular-prismatic two-cell must internalize or delete U70 through the F edge;
- the strict negative D exit at vertex 69 must remain available;
- extra stable S150 and saddles H5/H277 must cross before any replacement birth;
- the remaining forcing spokes through 43, 68 and 72 must be deleted, deactivated, or given independent negative external arrows;
- protected D045/D048 descendants must remain strict;
- C1–C3 must remain dependent full-rank moment controls;
- at least three physical shape coordinates must survive centring.

At least two independent D/F incidence coordinates are required in addition to the three dependent moment controls. If the closed D–F gate is unrealizable, the next finite architecture is a fourth corrector summand coupled to the same D–F exit, not another serial refinement of F.

The unrelated exact M42 `(61,163,104)`, strict `(2,1,1)` body remains the stronger run-wide equilibrium-count benchmark.

## Principal immutable hashes

```text
MANIFEST.sha256                                      c379f0b29dee69064514bae630bbd4137ba8b4ae88f859bd467c836e2754e2b2
RESULT.md                                            3562a7885e423d34793ec7ff4b569f6b39d237d60b028c1fedb2842b762a7c0c
coupledDF5_master_certificate.json                   cecd59e83203fea2e82693b3562485fc1d5fe33b0529f043bb5395beb8dce1dc
independent_coupledDF5_verification.json             1fe9601f290f8d65c23cbb01e27ac5ee3d227fd17a69519224e24c41cc5f7d4e
endpoint/exact_certificate.json                      10bdbd4b55369ae982673a3e832911b79ed9eedab0300cd48ed266a1be912e10
endpoint/root_certificate.json                       8a21c75f8ca557479fe0255b81db3eabb84abc558a4122a02d18e9f83dd732ea
DF5_common_fan_transition_atlas.json                 0eeb1e95aa79e8b08d207c342b6c9bc1dc49f9d5016ea5604f1eefa24a2fa83f
positive_volume_D_E_F_mixed_cell_certificate.json    41fc1b76283dcc3f1ab32e8aa0feac2ca79cbbf611e5f73a80e0899241fedabc
DF5_positive_volume_mixed_cell_certificate.json      c5733ebde131226441f5090b282c3fad955a99c4777aee6e52b7438242997e0a
DF5_carrier_genealogy_certificate.json               7ef49d8a75a460a8ed8d81581ebd4049d4d5e2a83cf9aeb88ea8788114070e22
DF5_external_arrow_certificate.json                  6120f38869a2209dadab5faf8c6bd54e3849aa264760681b10a8bbf86af87622
DF5_shape_box_directed.json                          bdbaee40c37e8dab26c802cf1a1c2024ba24224479a5a9c7c5e8e4d815b95c2e
DF5_shape_control_mechanics_box.json                 2881e810352ddf817f507a1809e0a645910f249adbc3fdf3b8a3c91211185107
DF5_shape_moment_implicit_box.json                   a5cc1ec05266318903d3ac7852af870fcad3be3aa3502a7174bf234805b70fe7
endpoint/endpoint_centered.obj                       e1aa5f40e0a5656a09861b036e884b32af1ee9e533d9b206b4af2649d9241b99
endpoint/endpoint_centered.stl                       b7c7821a401ea2f91f89042d88841dd930689c8080ba8fa599b3b1f897a0d047
```
