# figure-0090

AI research report · 2026-08-26 UTC

---

# Complete handoff — volume-moving bifurcated continuation from endpoint F

## Verdict

The journal records endpoint F as exact own-centroid `(2,2,2)`, with the old cap component `K={8,11,12}` forcing a second maximum in its fixed sign cell and requiring a volume-moving bifurcated escape.

**No homogeneous convex polyhedral Gömböc was found; no `(1,1,0)` claim is made.** The requested old obstruction was genuinely destroyed. A connected asymmetric two-rail replacement shifts the uniform-volume centroid toward the old cap, makes all three old K vertices strictly interior, removes the old stable quad `(6,7,2,1)`, neutralizes and then deletes `(0,1)`, and removes `(7,10)`. The strongest exact endpoint **G** is a robust rational 19-vertex body of class `(2,2,2)`.

## What changed

G is not inside F's closed sign cell. Old F vertices `[1,6,7,8,10,11,12]` are deleted; F9 is strictly inactive; retained F rows are `[0,2,3,4,5]`. Therefore every member of old `K={8,11,12}`, the old quad, and both old saddle neighborhoods are absent from G's actual V-representation.

The first post-cap exact stage already makes K strictly interior:

- F8: raw=404776300793265699545236757963449108580669713127089515718667943431244764879250759/1953125000000000000000000000000000000000000000000000000000000000000000000000000000000, normalized≈1.644394724417298782E-4
- F11: raw=400023051323018669415235475892391508506124318524561726038717981/3125000000000000000000000000000000000000000000000000000000000000000, normalized≈1.015677971313658707E-4
- F12: raw=4952032998036739051147829003723707242779437360641306811860922623/62500000000000000000000000000000000000000000000000000000000000000000, normalized≈6.286726243261904522E-5

The exact certificate is source_K_deactivation_certificate.json.

## Exact topology/moment path

Every accepted stage is reconstructed from its rational coordinates, has exact centered first moments `(0,0,0)`, and is exhaustively audited at its own uniform-volume centroid:

```text
00_source_F: VEF=(13, 31, 20), C=('-0.081803536799276461', '0.00013165313870133101', '0.0059102608959475953'), extraS=['F6', 'F7', 'F2', 'F1'], extraU=F8, H=[['F0', 'F1'], ['F7', 'F10']], inactive=7.487687842709326042854244E-7
01_rail_pairs_1: VEF=(9, 21, 14), C=('-0.94984478404150163', '0.014744632584386705', '0.028186967553411185'), extraS=['G5', 'F2', 'G6'], extraU=G5, H=[['F2', 'G5'], ['F5', 'G6']], inactive=5.848800073713597424858065E-6
02_rail_pairs_2: VEF=(11, 27, 18), C=('-0.95455308052764576', '0.016284893684713', '0.02865779586653118'), extraS=['G7', 'F2', 'G8'], extraU=G5, H=[['F2', 'G7'], ['F5', 'G8']], inactive=5.848800073713597424858065E-6
03_rail_pairs_3: VEF=(13, 33, 22), C=('-0.91412001444135926', '0.017594640970937516', '0.02765048477743683'), extraS=['G9', 'F2', 'G10'], extraU=G5, H=[['F2', 'G9'], ['F5', 'G10']], inactive=5.848800073713597424858065E-6
04_rail_pairs_4: VEF=(15, 39, 26), C=('-0.83281070851218153', '0.018686031171870877', '0.025335115390126537'), extraS=['G11', 'G12', 'G10'], extraU=G5, H=[['G9', 'G11'], ['G10', 'G12']], inactive=4.636081485435430169484856E-6
05_rail_pairs_5: VEF=(17, 45, 30), C=('-0.72402989982447141', '0.019520994574451615', '0.022091878863047958'), extraS=['G13', 'G10', 'G8'], extraU=G5, H=[['G9', 'G11'], ['G10', 'G12']], inactive=2.805949238552601458593782E-6
06_rail_pairs_6: VEF=(19, 51, 34), C=('-0.61152198886724984', '0.020047971676783041', '0.018627545397587233'), extraS=['G13', 'G15', 'G6'], extraU=G5, H=[['G9', 'G11'], ['G10', 'G12']], inactive=2.805949238552601458593782E-6
07_rail_pairs_7: VEF=(21, 57, 38), C=('-0.51472364598813636', '0.020245772797703947', '0.015618044882862819'), extraS=['G15', 'G8', 'G6'], extraU=G5, H=[['G10', 'G12'], ['G11', 'G13']], inactive=2.805949238552601458593782E-6
08_delete_F1: VEF=(20, 54, 36), C=('-0.51674417374417247', '0.020325788481222358', '0.015945048798812755'), extraS=['G15', 'G8', 'G6'], extraU=G5, H=[['G9', 'G11'], ['G10', 'G12']], inactive=2.805949238552601458593782E-6
09_delete_F7_final: VEF=(19, 51, 34), C=('-0.50891289885676427', '0.020550962468919538', '0.014549422490392844'), extraS=['G15', 'G8', 'G6'], extraU=G5, H=[['G10', 'G12'], ['G11', 'G13']], inactive=2.805949238552601458593782E-6
```

The old `F0-F1` edge is already strictly nonsaddle at stage 01; F1 is deleted at stage 08 and F7 at stage 09. The centroid-to-old-K-barycenter distance decreases from `2.514549772790089724E+0` to `2.087581386925557137E+0`, with positive exact capward dot product and capward projection `4.270900752306748272E-1`. Volume grows by ratio `3.163795013026745613E+1`. Full exact stage data: topology_path_certificate.json.

# Exact endpoint G

## Finite H/V data

- deterministic exact generator: generate_candidate.py
- all 19 exact rational coordinates and genealogy: candidate.json
- centered rational vertices: vertices_centered.csv
- complete primitive integer H-representation: halfspaces_centered_integer.csv

`(V,E,F,C)=(19,51,34,102)`, Euler characteristic `2`. All 19 vertices and 34 H-rows are irredundant; all faces are triangular.

Exact volume:

```text
6415864798402657636282228748126072962329258449598877487521369/375000000000000000000000000000000000000000000000000000000000000
```

Exact uncentered centroid:

```text
C_x=-6530232706456331785545162262145815193637665922359496363021719344432555221605453343/12831729596805315272564457496252145924658516899197754975042738000000000000000000000
C_y=131852196677635025175811820148821478156906389716245586728612067999525826815277507/6415864798402657636282228748126072962329258449598877487521369000000000000000000000
C_z=93347127593199376044796642727685144143991400969022468066135445030309653024897061/6415864798402657636282228748126072962329258449598877487521369000000000000000000000
```

`C≈(-0.50891289885676427, 0.020550962468919538, 0.014549422490392844)`; exact centered first moments are `(0, 0, 0)`. Primary and independent boundary/tetrahedral integrations agree.

Actual oriented maximal faces:

```text
F00(2, 1, 0) F01(0, 1, 5) F02(3, 2, 0) F03(6, 3, 0) F04(6, 0, 5) F05(4, 1, 2) F06(17, 1, 4) F07(1, 7, 5) F08(1, 9, 7) F09(1, 11, 9) F10(1, 13, 11) F11(13, 1, 15) F12(15, 1, 17) F13(4, 2, 3) F14(18, 4, 3) F15(8, 3, 6) F16(14, 3, 8) F17(14, 16, 3) F18(16, 18, 3) F19(17, 4, 18) F20(5, 7, 6) F21(7, 9, 6) F22(15, 8, 6) F23(9, 11, 6) F24(11, 13, 6) F25(13, 15, 6) F26(14, 8, 10) F27(15, 10, 8) F28(12, 14, 10) F29(15, 12, 10) F30(15, 14, 12) F31(15, 17, 14) F32(17, 16, 14) F33(17, 18, 16)
```

Actual true edges:

```text
(0, 1) (0, 2) (0, 3) (0, 5) (0, 6) (1, 2) (1, 4) (1, 5) (1, 7) (1, 9) (1, 11) (1, 13) (1, 15) (1, 17) (2, 3) (2, 4) (3, 4) (3, 6) (3, 8) (3, 14) (3, 16) (3, 18) (4, 17) (4, 18) (5, 6) (5, 7) (6, 7) (6, 8) (6, 9) (6, 11) (6, 13) (6, 15) (7, 9) (8, 10) (8, 14) (8, 15) (9, 11) (10, 12) (10, 14) (10, 15) (11, 13) (12, 14) (12, 15) (13, 15) (14, 15) (14, 16) (14, 17) (15, 17) (16, 17) (16, 18) (17, 18)
```

## Complete own-centroid equilibrium audit

Positive limiting margin means equilibrium; negative gives a strict witness. These are all 34 face, 19 vertex, and 51 full two-normal-cone edge limiting margins:

```text
FACES
F00=2.513673725954982478818637E-3; F01=-6.288769820470916943110213E-4; F02=-2.026552390599848870582503E-3; F03=-1.874145314441855455971244E-3; F04=-1.779408041581416761454344E-1; F05=-1.124069986504245030216949E-2; F06=-2.695923613765330306282186E-2; F07=-4.978218242405803593984913E-3; F08=-5.267108160396232990596608E-3; F09=-4.785329386281910362376914E-3; F10=-3.667507691268424888730980E-3; F11=-2.362514790323985884177902E-3; F12=-3.354595407046693988339585E-3; F13=-6.543825521238898388588087E-3; F14=-4.133148481856271007147069E-3; F15=-2.784542282434734208806140E-3; F16=-3.222645664957564942379593E-3; F17=-6.555708678469014391619657E-3; F18=-9.375417811502911374140227E-4; F19=-4.126533144084504206537105E-1; F20=-6.819232768019497346255692E-2; F21=-2.646925125445283751591061E-2; F22=5.658773217588578882925562E-4; F23=-1.227381929480294549172819E-2; F24=-4.984989961787191057338404E-3; F25=-4.290820544237899917774787E-4; F26=-7.963622093569550793449187E-3; F27=-1.657736467909092717929406E-3; F28=-7.176971014764489782896682E-3; F29=-5.304594075863498011391371E-3; F30=-1.258641302390858046044368E-2; F31=-3.424548538607739660828740E-2; F32=-2.218530263502472050500864E-2; F33=-5.032628653734852558470420E-2

VERTICES
V00=-8.343530857141302600541211E-1; V01=-9.837612730453078020794658E-1; V02=-9.994596204658491692665094E-1; V03=-9.931170157483479102490779E-1; V04=9.869044171420311810427619E-1; V05=1.468965431734079326896094E-1; V06=-8.033199934190148477478687E-2; V07=-9.988547802699575869495337E-1; V08=-9.988281833897682405573130E-1; V09=-9.956336286623709608655758E-1; V10=-9.954528540301183779305281E-1; V11=-1.025510809617061568424856E-1; V12=-3.874129152310551023639514E-2; V13=-9.952992872344059464064412E-1; V14=-9.954184021963209438133255E-1; V15=-9.985927803534739426409141E-1; V16=-9.986197753516719516827574E-1; V17=-9.988507903166616627242293E-1; V18=-9.966436158651661277496308E-1

TRUE EDGES
E00(0, 1)=-3.230416258619889438659854E-1; E01(0, 2)=-1.770075389037019185329315E+0; E02(0, 3)=-5.101574871503787418156291E-1; E03(0, 5)=-1.043166864264687461331069E+1; E04(0, 6)=-1.130497223954686159266599E+1; E05(1, 2)=-3.832118986999454600458070E+1; E06(1, 4)=-8.603351106148331090338381E+0; E07(1, 5)=-7.114203747565252941604820E-1; E08(1, 7)=-1.021171070948920664001670E+1; E09(1, 9)=-2.949323756246761809279192E+0; E10(1, 11)=-1.408487851091673781290419E+0; E11(1, 13)=-6.995250521214943603883196E-1; E12(1, 15)=-1.095442492463638793618488E+0; E13(1, 17)=-3.660166830745459176811030E+0; E14(2, 3)=-4.897013501149396137392586E+0; E15(2, 4)=-1.303063975626452256991093E+0; E16(3, 4)=-2.128933422733482852300197E+0; E17(3, 6)=-1.915826994067517624169049E+0; E18(3, 8)=-3.616324793810928394210573E+1; E19(3, 14)=-6.213581032266175083552884E+2; E20(3, 16)=-3.021821407380115243710135E+0; E21(3, 18)=-1.863478819017452712147166E-1; E22(4, 17)=-3.143672408319808220792070E+0; E23(4, 18)=-2.399887006040115892187211E+0; E24(5, 6)=-1.186664613576749912143157E+0; E25(5, 7)=-2.009330754565246569394949E+0; E26(6, 7)=-3.332488836950206372486766E+2; E27(6, 8)=-1.996203971545208645935163E+0; E28(6, 9)=-1.113767162363069345010961E+2; E29(6, 11)=-5.296065607644897835232164E+1; E30(6, 13)=-2.458209547132961861372402E+1; E31(6, 15)=-3.105380527821265231353084E+0; E32(7, 9)=-1.009403546055547890634834E+0; E33(8, 10)=-9.962654090696147547835288E-1; E34(8, 14)=-2.118880245603750459346546E+0; E35(8, 15)=-1.059842561974788482903315E+2; E36(9, 11)=-9.567256332091767210624449E-3; E37(10, 12)=3.715352426181918745920569E-3; E38(10, 14)=-7.175752615734277994111234E+0; E39(10, 15)=-1.445607372593949550257056E+2; E40(11, 13)=9.815836875024331346955338E-3; E41(12, 14)=-3.687395534631819450461945E-3; E42(12, 15)=-1.509777788468152938329552E+2; E43(13, 15)=-9.898126795761483532485418E-1; E44(14, 15)=-2.387765610964184726406601E+3; E45(14, 16)=-1.003554024619077683868848E+0; E46(14, 17)=-8.257169662135238717527420E+1; E47(15, 17)=-1.989062596731833654026046E+0; E48(16, 17)=-6.535790214344057525416180E+1; E49(16, 18)=-2.003017652301917811549078E+0; E50(17, 18)=-5.541983623658188138464982E+1
```

The positive features are exactly:

```text
stable: F00=(2,1,0), margin [2.513673725954982478818637E-3,2.513673725954982478818637E-3]
        F22=(15,8,6), margin [5.658773217588578882925562E-4,5.658773217588578882925562E-4]
unstable: V4, margin [9.869044171420311810427619E-1,9.869044171420311810427619E-1]
          V5, margin [1.468965431734079326896094E-1,1.468965431734079326896094E-1]
saddles: E37=(10,12), 1-t margin [3.715352426181918745920569E-3,3.715352426181918745920569E-3]
         E40=(11,13), t margin [9.815836875024331346955338E-3,9.815836875024331346955338E-3]
(S,U,H)=(2,2,2), S+U-H=2.
```

Every constituent raw exact primitive—not only each limiter—is materialized in face_primitives.csv, vertex_primitives.csv, and edge_primitives.csv.

## Incidence separation and strict boxes

Minimum inactive unit-normal/diameter separation is `[2.805949238552601458593782E-6,2.805949238552601458593782E-6]` at face 26, vertex 12; exact raw value `9950861017785467299613379637/1000000000000`. All inactive slacks: inactive_incidence.csv.

Two exact open certificates hold:

1. all 57 uncentered coordinate components independently vary by `±1/10000000000` while incidence and every primitive sign remain fixed;
2. all five parameters of `A(t)=I+t0 diag(1,0,-1)+t1 diag(0,1,-1)+t2(E01+E10)+t3(E02+E20)+t4(E12+E21)` independently vary by `±1/10000000000` with `det A>0`, exact transformed moments, unchanged incidence, and unchanged class.

Certificates: coordinate_box_certificate.json, metric_box_certificate.json.

# Proof-level obstruction in G's realized cell

The old K theorem no longer applies. A new exact rail component appears:

```text
R={5,6}, internal true edge (5,6).
```

Every support from 5 or 6 to a true neighbor outside R is strictly positive; the minimum raw support is

```text
111580510377104740299314533309290517316145469689224525431595183108363769097164483026673338498676436807/400991549900166102267639296757879560145578653099929842970085562500000000000000000000000000000000000000
```

At a maximum-radius member `v*` of R, each internal support is also strict positive because

`-x_v*·(x_u-x_v*)=||x_v*||²-x_v*·x_u≥||x_v*||²-||x_v*||||x_u||≥0`,

with equality impossible for distinct endpoints. Hence R always contains an unstable vertex throughout this fixed-incidence/external-positive sign cell. Target V4 is independently unstable, so the cell has `U≥2`. Exact proof: rail_cluster_obstruction_certificate.json.

## Search scope

A ten-parameter, eight-section connected asymmetric profile family was audited at each body's own centroid: 2499 of 2500 random profiles were valid; 909 were strict target-preserving `(2,2,2)`; none was `(1,1,0)`. The class histogram and parameters are in search_summary.json. A complete 192-branch fixed-topology first-order separator screen had best common margin `-0.02243536147322095` and no positive branch. These searches are empirical/first-order evidence only.

## Exact closure and continuation

Exactly closed:

- the ten rational F→G stages and all three moment equations at every stage;
- G's `10^-10` independent-coordinate box;
- G's `10^-10` five-parameter metric box;
- G's complete fixed-incidence/external-positive rail-cluster cell, where `U≥2`.

The smallest nonredundant next architecture is a **cross-rail 2×2 zipper/annular bridge**. It must add cross-branch edges—not more independent rail sections—so each possible maximum in `{5,6}` receives an independent nonpositive external witness or deactivates; simultaneously span saddle neighborhoods `(10,12)` and `(11,13)`, cut stable `(15,8,6)`, allow `{5,6,8,10,11,12,13,15}` to become non-extreme in one coupled circuit event, and solve three exact volume moments through dependent coordinates or safe actuators.

## Reproducibility

- complete bundle ZIP (`F_bifurcated_volume_moving_research_bundle.zip`)
- full standalone report (`F_bifurcated_volume_moving_research_REPORT.md`)
- combined verifier transcript (`RUN_ALL_VERIFIERS.txt`)
- fresh-extraction transcript (`F_bifurcated_volume_moving_research_FRESH_VERIFY.txt`)
- SHA-256 manifest (`SHA256SUMS.txt`)
- ZIP SHA-256 record (`F_bifurcated_volume_moving_research_bundle.zip.sha256`)
- primary exact verifier (`verify_exact.py`)
- independent exact reconstructor (`verify_independent.py`)
- mesh verifier (`verify_mesh.py`)
- OBJ (`body.obj`)
- STL (`body.stl`)

Run `bash RUN_ALL_VERIFIERS.sh` after extraction. Fresh extraction verified all 229 manifest-tracked files before and after rerunning every verifier. ZIP SHA-256:

```text
71120040fc780c4ee1a22219273b63cadfdce51cc5c04d0121b4501a37ebdc27
```
