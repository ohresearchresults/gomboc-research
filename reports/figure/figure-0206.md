# figure-0206

Historical AI scientific report · saved 2026-09-02 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Calm Raven 06 — exact post-CU10 bridge-pair determination

## Outcome

I advanced the accepted seven-facet `3×3×3` circuit star through the first topology that had not been classified. The requested single eighth-plane hexagonal cut is **exactly infeasible**. I then materialized an exact adjacent two-facet/ninth-plane bridge, rebuilt the actual common fan through all of its intervening cells and walls, solved the ordinary volume moments, audited every full normal cone, certified independent bridge-shape controls after centring, reconstructed the object independently, and exported matching watertight meshes.

The promoted endpoint is a rigorous **nonwinner**: its own-centroid class is `(S,U,H)=(2,2,2)`, not `(1,1,0)`. No homogeneous convex polyhedral Gömböc is claimed.

The complete 86 MiB replay bundle is [Calm Raven 06 exact bridge-pair bundle](sandbox:/mnt/data/Calm_Raven_06_bridgepair9_exact_NONWINNER.zip). ZIP SHA-256: `e265db113e9da2f0fb33bf94336ff7d0f93ea5686f31c98a6ef7caeb1286856c`. A fresh extraction passed all 858 manifest hashes and ended with `INDEPENDENT_EXACT_BRIDGEPAIR9_PASS`.

## What changed relative to the supplied journal

The journal ended after the complete seven-plane star and minimal triangular bridge, with the cyclic target `01→15→25→24→04→05` still unresolved. This work adds four durable determinations:

1. an exact impossibility proof for realizing precisely those six strict edge cuts with one supporting plane while preserving the named lineage;
2. an exact nine-plane summand whose two adjacent bridge facets jointly cross all six target old edges and preserve `045`;
3. the complete five-open-cell/four-wall actual common-fan atlas, with exact moment roots and H/V/E data in every promoted cell;
4. a six-dimensional independent bridge-shape box after exact centring, with `C1,C2,C3` used only as dependent rank-three moment controls.

## 1. Exact infeasibility of the one-plane cyclic cut

The accepted seven-wall summand has vertices

`0136, 015, 034, 045, 1256, 2346, 245`

and true edges

`01,03,04,05,15,16,24,25,26,34,36,45`.

Let `T={01,15,25,24,04,05}` be the demanded crossed-edge set. A plane avoiding old vertices partitions the old vertices into positive and negative sides, so its crossed edges are exactly a graph coboundary. Every coboundary meets every graph cycle evenly. The exact old-wall cycle

`045→015→0136→2346→245→045`

has edge sequence `05,01,36,24,45`, and `T` meets it in `{05,01,24}`, of cardinality three. Therefore `T` is not a plane cut. The certificate exhaustively enumerates all `2^(7-1)-1=63` nontrivial vertex bipartitions modulo complement: zero produce `T`; the minimum symmetric difference is one.

There is also a direct convex-section obstruction to the literal proposed six vertices. The consecutive old-facet carriers forced by `017,157,257,247,047,057` are

`1,5,2,4,0,0`.

The last two section sides would both lie on old facet 0; equivalently `017,057,047` all lie on the same line `H0∩H7`. Three such points cannot all be extreme vertices of one convex planar facet. Passing through an old vertex only creates a degenerate section and does not realize the six named strict lineages. The protected intended vertex `045` is an old wall vertex and remains untouched by the certificate.

Primary certificate: `single_plane_infeasibility_certificate.json`, SHA-256 `b86276a28a2cfdc2e8eb903629f855a5db822ddf1115a210012cc0f21226756f`.

## 2. Exact two-facet/ninth-plane successor

The final summand is the bounded intersection `D={x:n_i·x≤h_i, i=0,…,8}` with these exact rows:

```text
0 D0: (-13153/32768, -27937/65536, -53127/65536; h=1516059357/2147483648)
1 D1: (-1361/65536, -10805/32768, 61855/65536; h=-61753030599584781385807608441346358116846527699/310810949179262687143965090288773323565704413184)
2 D2: (9313/16384, 4455/8192, 10115/16384; h=-352797091482846540514804485565826624474423927/19425684323703917946497818143048332722856525824)
3 D3: (10039/16384, -4513/8192, -18567/32768; h=3702610017626632720309376484242546264871389323/2428210540462989743312227267881041590357065728)
4 D4: (26213/65536, 13729/16384, 24333/65536; h=-96737211/1073741824)
5 D5: (-19289/65536, 7561/32768, 15195/16384; h=-242832957/268435456)
6 D6: (56045/65536, -16661/32768, -6603/65536; h=90301/65536)
7 bridge7: (-12225/65536, -2399/32768, 64207/65536; h=-2295307548643407433816811540070135540036341203095945005507575/3916822130433258859832783870198263388589283412013047353442304)
8 bridge8: (16291/16384, -5945/65536, 3645/65536; h=214505787219754136715603574458414145391198136777824126622566059565244263873/237881794492947352987653140187185697870657453663791039663324963028160479232)
```

All nine rows are irredundant. Its exact lattice is `(V,E,F)=(13,20,9)`, with vertex active sets

`0136, 017, 038, 045, 048, 057, 168, 178, 245, 248, 258, 368, 578`.

The exact rational coordinates of all 13 vertices, all 20 edges, and all nine oriented facet cycles are embedded both in `bridgepair9_master_certificate.json` and in `bridgepair9_run/atlas/cell04/D_V.csv`, `D_edges.csv`, and `D_faces.csv`. Their SHA-256 values are respectively `25f4cf32226f308d016d9767b336b46f5063ead160eee5d8e7b4e60fb9f19997`, `6c1f99d8afd2b08a4c513c3befdb0846e6c1c331b2be2d0d805508d7a348f6d6`, and `81801c51fa52f4d579c407f3c69693039a981149186b30029d6162e1e44e4785`; the exact H rows hash to `e88211763bddc100057bad3586b6fbca9fc9c2437525f48cc3e56aaa495e4250`.

The two bridge pages are literal:

- facet 7 is the quadrilateral `017–057–578–178`;
- facet 8 is the octagon `038–048–248–258–578–178–168–368`;
- their shared true edge is `178–578`.

Plane 7 cuts old edges `{01,05,15}`. Plane 8 cuts the pre-plane-8 edges `{03,04,16,17,24,25,36,57}`. Thus the demanded old chain is distributed exactly as

`plane 7: {01,15,05}` and `plane 8: {25,24,04}`,

while `{03,16,36}` close the second page and `{17,57}` are its shared-page cuts. The first page creates `017,157,057`; the second page then removes the connected pre-plane-8 set `2346,1256,157,034`. The protected vertex `045` survives. This is an actual quadrilateral–octagonal two-page triangular-prismatic/octahedral-type `2↔3/3↔2` successor, not a proposed combinatorial template.

## 3. Complete actual common-fan arrangement

The only varied path coordinate in the atlas is the exact support `h_8`. It crosses the old/pre-bridge vertices in the strict order

`2346 → 1256 → 157 → 034`.

Every crossing changes the reconstructed common refinement. Each open cell below has complete exact `D_H/D_V/D_edges/D_faces`, `common_H_affine/common_V_affine/common_edges`, mixed-volume and first-moment polynomials, exact centred H/V data, exhaustive mechanics, and its own root certificate.

| Cell | exact `h_8` | removed pre-bridge vertices | `D (V,E,F)` | common `(V,E,F)` | class | inactive slack | root-certificate SHA-256 |
|---:|---|---|---|---|---|---:|---|
| 0 | `1665120553913999325965394052258557051702426231629/1243243796717050748575860361155093294262817652736` | none | `(9, 15, 8)` | `(47, 88, 43)` | `(2, 2, 2)` | `0.00126427650782` | `a259c8601c7f2735683168b1a0667ab308d1be2acdaa7c8bbb5b1775c203c60f` |
| 1 | `1521645064268864532894983020632487120145186594129/1243243796717050748575860361155093294262817652736` | 2346 | `(12, 19, 9)` | `(58, 108, 52)` | `(2, 2, 2)` | `0.00126427650782` | `b5f83ee2c9ef1f1080243069f3dafa5bf0fbfb1304e51de4880fe6373d42216a` |
| 2 | `36238463579171687906466101622612816723757814760090610657350023/31334577043466070878662270961586107108714267296104378827538432` | 2346,1256 | `(13, 20, 9)` | `(61, 113, 54)` | `(2, 2, 2)` | `0.00063213825391` | `5cd2df80d1946a365cbd28a1a2b2dd22cae98debd94308cbb87196d149e8e186` |
| 3 | `828357514092238066645022701878122077937486275681109360741734637609524169279/749303449393523580359005452065036257166180620097537177889493793369946587136` | 2346,1256,157 | `(13, 20, 9)` | `(63, 117, 56)` | `(2, 2, 2)` | `0.000232666217492` | `0e8bb42239070e9521627039062be7e7867d5bdf72f706e18a3d28d17b0611c5` |
| 4 | `214505787219754136715603574458414145391198136777824126622566059565244263873/237881794492947352987653140187185697870657453663791039663324963028160479232` | 2346,1256,157,034 | `(13, 20, 9)` | `(65, 121, 58)` | `(2, 2, 2)` | `0.000304990218115` | `b67f4fce63d2478769b7794e3395f6d830c640383372bb51672a7824ca434b10` |

In every open cell the exact positive moment root is `(t1,t2,t3)=(1,1,1)`. The exact rational Krawczyk box radius is `1/1048576=2^-20`, and each mixed-moment Jacobian determinant is nonzero. Their determinant decimals, only as readable locators for the exact fractions, are `-3.1039802898e9`, `-3.0140328022e9`, `-3.0079742274e9`, `-3.0677213432e9`, and `-3.8392731589e9`.

The exact wall lattices are also materialized:

| Wall | crossed vertex | exact `h_8` | `D (V,E,F)` | common `(V,E,F)` | common-H SHA | common-V SHA | common-E SHA |
|---:|---|---|---|---|---|---|---|
| 1 | `2346` | `1593382809091431929430188536445522085923806412879/1243243796717050748575860361155093294262817652736` | `(9, 15, 8)` | `(47, 88, 43)` | `4aa44dcce9ccbcc1b6e5925599c4198185c70cdc3b4979282382dd23b0d72cd6` | `eb8dfbafe3fc4bea229370fbfed1c0b3098a0d8cf704d176711b2ea1e365461e` | `30fd26d90a637217630f378e7621788ef08b24e2ca0d5ccee1a9a47194c85752` |
| 2 | `1256` | `1449907319446297136359777504819452154366566775379/1243243796717050748575860361155093294262817652736` | `(11, 18, 9)` | `(55, 103, 50)` | `79b41aa96f6f5ff5fafc619c1cbf6fca0536f28f1d0032abd1b85be360b5a804` | `cd8491afa859de0f99b460c122cebab4727571ca4513261c44763b9e38862931` | `7b4e8330f3c560fccde94d8193ddff533534d4e62a1cf0239c1a3060e2fc5c5c` |
| 3 | `157` | `8983406473777879975173647600857234210021496837520241484782087/7833644260866517719665567740396526777178566824026094706884608` | `(12, 19, 9)` | `(60, 112, 54)` | `8d13ff00544913806053a427327398498ebb978d3f6d13e72b5c699c7a44a007` | `6fd34e41324fd5f9a1c5d22424d4e0d8d3ef0638e61887638cb705ec346a0574` | `7f6b22f9baf572546fb2b7d37b9a5daa7d54313ae8f21313f240aaed51520e1c` |
| 4 | `034` | `31639347694459951217793165646747347135281054738677251906637067/29729677347326389323222470867155392576317331743037602060566528` | `(12, 19, 9)` | `(62, 116, 56)` | `d5d1e3351eccf091946c7e86d0135cdb604e769e9d0412f11b93a0ac8380dad6` | `9d6ca321c296d92784fd1ca51d56776beab3e84af6f6a3e4c0c522639028c88b` | `9062ebc4ce1171dda40315257315728751746c7ecff01d17ef15bde92ec20b08` |

The atlas file is `bridgepair9_run/common_fan_transition_atlas.json`, SHA-256 `4ea063ab6397f85de0d3625a9665752c7af2396bca2e7bc20ff528cecd22aa90`. It includes the exact symmetric differences of every adjacent H/V/E set, so the assertion that all four transitions change the actual common fan is independently replayable rather than inferred from the summand alone.

## 4. Final exact centred polyhedron

For cell 4, the Minkowski sum

`P = B + t1 C1 + t2 C2 + t3 C3 + D`

at `(t1,t2,t3)=(1,1,1)` has exact common-refinement lattice

`(V,E,F)=(65,121,58)`, Euler `65-121+58=2`, mechanical complexity `65+121+58-2=242`.

Its exact ordinary volume is

```text
6900166775912653228219142286804759328030386971230268943081019209746506149923697676968053048130375156488896782883635221440594630770982238732193068591512656285260039089721196141029812294095255493418754287019614090449618694479040757952646566129169356431457231559487480461346399876204489430559713679690573493301185552080656286774935590694215137432225541807915274256651638092731392217769604139228389463863857177816071957385479855480013819484301504947685208439525811444300048021729637176516786837878851474129633323178288004361055715584267737742833135852476711105011740196011491300812707969605880594180354460198242966357019282671867806550815431777144969669730621911497299398959703659739038848909492435865575932721732602633427255338076273633879932972390454074904344568324868921145809310892235388351571822485966514637230779790897821759481929387856981852840371520908257902763407933129022767774378384052872186670010659053890499789311523710573817377803969976068647619114030607179775477918139047678650298376791336246768267477160709618592458881933261455016825465355014546099031/76663339406040083715362699664468783709709349630836463861882991099049028627148429958113565042701211260239243001369934421285751734296455710988540010186467178152324009308583582073696702273918381230872115490616662586493940257522137000306625490449808207892879764664669527622350364329050491121687993423834401028099806560404290291383441346031695581245256593614065617638405330339046377719025016648686811942097924390436929287117723396156575555246152886634933409289823139234368982387552962507944876245421967993820891850514403448344725543522020631762257068637807062493939725413618924628061774015623091518998033368951115876391343240970794270218511652320142699220189819768874049243957569930983029777836067546047409219423668949506416848121442923344757075368736865930979976225357483043875070106912531191544385374295759250379869841945905074824738385971426963894323297587541391119716309310006742271386268200204493552093592095047403863610970709118039525654116756040293316353166140750200745726213929948488482910812340938163970751436389880322322023821349566179118545905490329600
```

and its three exact first moments are `0/1,0/1,0/1`; hence the ordinary uniform-volume centroid is exactly the origin. The exact mixed-moment Jacobian determinant is the nonzero rational in `root_certificate.json` (decimal `-3839273158.862234`). The exact rational root box is `[1±2^-20]^3`; a separate outward-directed binary64/GMP enclosure proves strict Krawczyk inclusion, fixed actual fan, and fixed class on `[1±2^-22]^3`.

The exhaustive own-centroid full-cone mechanics is exactly:

- stable face 4, `P9:15|Dvertex(3;6;8)`, normalized margin `0.001625940251326149`;
- stable face 6, intended `P9:27|Dvertex(0;4;5)`, normalized margin `0.03133518238182069`;
- unstable vertex 31, `P9[9;100;103]|D[0;1;3;6]`, normalized margin `0.007000037990942382`;
- unstable vertex 47, intended `P9[15;26;27]|D[0;4;8]`, normalized margin `0.20057832934254907`;
- saddle true edge 24, `P9edge(13;26)|Dedge(2;4) || P9edge(13;26)|Dedge(4;8)`, normalized cone margin `0.11769583963299723`;
- saddle true edge 91, `P9edge(15;27)|Dedge(0;1) || P9edge(15;27)|Dedge(3;6)`, normalized cone margin `0.17488266528536134`.

Every other one of the 58 maximal faces, 65 vertices, and 121 complete true-edge normal cones is strictly negative. The minimum normalized inactive separation is `0.00030499021811543754`. The exact endpoint certificate hashes to `d656297161c674ba86616e0ade874f56498c736e1b1be86944a295bc5ea5ec63`; the root certificate hashes to `b67f4fce63d2478769b7794e3395f6d830c640383372bb51672a7824ca434b10`.

Mechanically, the two-page bridge does reach and alter the B/C-side carriers: `1256` and `2346` are actually deleted, and the intermediate `157` relay is absorbed. It still does not perform the demanded cancellation. The block reappears as the extra stable `D368`, extra unstable `D0136`, C-side saddle on `D24/D48`, and return saddle on `D01/D36`; the intended stable `D045` and intended unstable `D048` lineages remain. This is why the endpoint is a strict `(2,2,2)` nonwinner rather than a wall or a hidden `(1,1,0)` cell.

## 5. Independent shape controls after centring

I did not count `C1,C2,C3` as free shape variables. The independent physical bridge coordinates are

`bridge7_dnx, bridge7_dny, bridge7_dh, bridge8_dnx, bridge8_dny, bridge8_dh`,

with gauges `bridge7_dnz=bridge8_dnz=0`. Rows 0–6 remain fixed, so the inherited three four-plane circuit equalities remain exact.

Three nested certificates were constructed:

1. **Shape-only fan/mechanics box:** radius `1/1073741824=2^-30` in all six bridge coordinates with `(t1,t2,t3)=(1,1,1)` fixed. The exact D lattice stays `(13,20,9)`, the common lattice stays `(65,121,58)`, and every body at its own interval-enclosed centroid stays `(2,2,2)`.
2. **Shape × dependent-control mechanics box:** shape radius `2^-32`, control radius `2^-30`; the whole nine-dimensional product has the same actual fan and strict own-centroid `(2,2,2)` mechanics. This is a certified superset of the centred implicit graph below.
3. **Parametric moment implicit box:** 120-digit directed decimal interval arithmetic gives shape radius `2^-66` and dependent-control radius `2^-36`. The central Jacobian has exact rank three. For every six-coordinate bridge shape in that box there is exactly one positive `t` in `[1±2^-36]^3` for which all three ordinary first moments vanish.

The uniform Krawczyk image is strictly interior to the control box:

```text
K1 = [0.999999999999996251947881813103761043242042498659766351101176927553962077470213279592940480320698255929809484542808491104,
      1.00000000000000374805211818689623892341187588364710780147915113060725245230001299546998144187395224290799633457909650724]
K2 = [0.999999999999988086007295227995175775554226580671491556217710469836073502005536126908633973377042244323922671273456663911,
      1.00000000000001191399270477200482425773466429727714415926677797587345639377184459035315131020651348551996338765455332600]
K3 = [0.999999999987966330953858602859761106232179094722881328674114693885142425076130986078986031299038332664731342720440503260,
      1.00000000001203366904614139714021136635816724151828160431688237375950746289569632783518824747869031786372631743105305692]
```

Thus six independent bridge-shape degrees of freedom remain after exact centring, while `C1,C2,C3` serve only as dependent full-rank moment controls. The three certificate hashes are:

- shape-only: `a2b3e8c89d2361131c70cb6e547da7ead8b9ef4bd944c2833d330ed26d438ab1`;
- shape×control mechanics: `7d354dcf61ceb5a19e3015e7dc4980d9e933aa3e2749f187c240cece4f0d4ebb`;
- parametric implicit root: `cc289f93fd83767f366d91e08be821d49dac2ee057a2377876548ff4104c9e82`.

## 6. Independent reconstruction and meshes

`verify_bridgepair9_cleanroom.py` imports neither `exact_core.py` nor `shared_build_lib.py`. From rational CSV data it independently:

- reconstructs the seven-wall graph and reruns all 63 cut-space partitions;
- reconstructs all five open D lattices and all four exact wall lattices with `Fraction` arithmetic;
- verifies the two bridge facet cycles, their shared edge, all cut-edge sets, irredundancy, and protected `045`;
- recompiles a fresh GMP mixed-volume/first-moment executable and matches all polynomial coefficients;
- solves/checks all five roots, exact centroids, H/V/E incidences, inactive slacks, and every face/vertex/full-edge-cone sign;
- validates the directed t-control, shape, shape×control, and parametric implicit certificates;
- parses and matches the final OBJ and binary STL.

Its immutable result is `bridgepair9_run/independent_verification.json`, SHA-256 `a4d644d5a1ee2d16620bcacc92ef5c6c52a82528de500de85201dc6d9cffd72d`, with terminal marker `INDEPENDENT_EXACT_BRIDGEPAIR9_PASS`.

The matching final meshes contain 65 vertices, 126 outward-oriented triangles, and 189 triangulation edges; every edge has incidence two and `65-189+126=2`. Hashes:

- OBJ: `576817b57f9f37394a30effedd484047c5d6f4e11189a3ab52dbca159b6e7e67`;
- STL: `696ca2a70c56728fb58cc437b00edee993a6b35065b0dee7e9ec003f5a8e19c1`;
- mesh certificate: `15e5c7edc7829bebcedca3645f41c19e442c8ce560eb33f8d86e0b69ef29f4b9`.

The self-contained master certificate embeds the exact nine summand rows, all 13 exact summand vertices, the cell and wall atlases, final exact moments/mechanics, control boxes, and key-file hashes. Its SHA-256 is `eae3889ffd0dd2becaf426a0ccf4b5b48e8e107402929f97f374830326c6cbf1`. The package manifest hashes to `efdf680c8694d7af6d8fb36774ae5566fde84d457ac2c3e4dfb9c4411da5f658`.

## Rigorous scope and next frontier

This run proves the exact infeasibility of the *named* single-plane six-edge cut and gives a complete exact two-page/ninth-plane successor. It does not prove that every possible two-facet or nine-plane bridge is a nonwinner, and the exploratory multicircuit descent is not promoted as an exclusion.

The first genuinely unclassified continuation is now a third adjacent page/tenth plane, or an equivalent finite-thickness three-page higher-valence cell, that clips `D0136`, changes the return `D01/D36` carrier, and joins it to the extra-stable `D368` and C-side `D24/D48` packet before any replacement birth. It must retain at least three independent bridge-shape controls after the three moments are eliminated. The exact cell-4 package supplied here is the correct restart boundary.
