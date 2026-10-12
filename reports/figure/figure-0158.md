# figure-0158

AI research report · 2026-08-29 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Literal verdict

**NONWINNER.** No strict own-centroid `(S,U,H)=(1,1,0)` polyhedron was obtained. The compact apex-side replacement is nevertheless fully materialized. Its strongest exact post-event body `E10` is dyadic, own-centred, open, and strict `(2,2,2)`. The journal had accepted `G27` and identified this complete apex-side shared-cell replacement as the correct compact successor; the global winner gate remained unmet. 

## 1. Exact source `G27`

Use common denominator `D=2^44=17592186044416`. Uncentred integer numerators are:

```text
1: (-7715758938572,2889556079942,-17779918034961)
2: (-8262479746679,1678647340512,-17660251163923)
3: (-19718591797520,-41379697761669,-17592525598195)
4: (-19707343224389,-41384307037227,-17592329907461)
5: (28735822451870,65017701265160,16682797993973)
6: (3600087730963,23172133013753,-11017132169953)
7: (27967861505375,64205100806705,32167696120114)
8: (-5658133234447,-11830031585001,-22901357099805)
9: (-24778822577834,-27890508662314,-3487947517004)
10: (-17333854524801,-42073399768973,-17068563828311)
11: (7425371686672,6793144760174,-22628800214142)
12: (4728022774716,39660727728711,500165975828058)
```

Exact volume:
`126985493881363575031115070067221091983997/4083388403051261561560495289181218537472`.

Exact first moments:
`Mx=-26710297389305229588633875798394225667591207517553887/23945242826029513411849172299223580994042798784118784`;
`My=21254501471744223791770624627479625117499281210633453513/1149371655649416643768760270362731887714054341637701632`;
`Mz=464496956870470259327279458352642485368709915665052200839/2298743311298833287537520540725463775428108683275403264`.

Exact ordinary-volume centroid:
`C=(-80130892167915688765901627395182677002773622552661661/2233952433302997641806976648607592905411276269003210752, 924108759641053208337853244673027179021707878723193631/1554053866645563576909201146857455934199148708871798784, 464496956870470259327279458352642485368709915665052200839/71486477865695924537823252755442972973160840608102744064)`.
The exact verifier proves `M=VC`, hence centred moments `(0,0,0)`. The actual lattice is `(V,E,F)=(12,30,20)` with maximal faces

`[2,1,8] [9,1,2] [6,11,1] [12,6,1] [1,11,8] [12,1,9] [2,8,3] [2,3,9] [8,4,3] [3,4,12] [12,9,3] [8,10,4] [4,10,12] [5,11,6] [12,5,6] [11,5,7] [12,7,5] [11,7,12] [8,11,10] [10,11,12]`

and true edges

`(1,2) (1,6) (1,8) (1,9) (1,11) (1,12) (2,3) (2,8) (2,9) (3,4) (3,8) (3,9) (3,12) (4,8) (4,10) (4,12) (5,6) (5,7) (5,11) (5,12) (6,11) (6,12) (7,11) (7,12) (8,10) (8,11) (9,12) (10,11) (10,12) (11,12)`.

Its class is `(2,2,2)`: stable `[12,6,1]`,`[10,11,12]`; unstable `3,12`; saddles `(3,12),(5,12)`. Minimum exact integer nonincident support slack is `52336883239874621198990664959533313`.

## 2. Connected complete-star replacement

The common boundary is the six-cycle `[1,2,8,4,12,11]`. The untouched outside faces are

`[1,2,8] [1,8,11] [4,8,10] [4,10,12] [8,10,11] [10,11,12]`.

The removed connected disk is

`[9,1,2] [6,11,1] [12,6,1] [12,1,9] [2,8,3] [2,3,9] [8,4,3] [3,4,12] [12,9,3] [5,11,6] [12,5,6] [11,5,7] [12,7,5] [11,7,12]`.

It has `(V,E,F)=(11,24,14)` as a disk, six boundary vertices and five internal vertices `(3,5,6,7,9)`. The added disk is

`[14,9,12] [14,12,13] [11,13,12] [4,9,14] [4,12,9] [1,14,13] [1,13,11] [2,8,4] [2,4,14] [2,14,1]`.

It has `(V,E,F)=(9,18,10)` as a disk and internal support `(9,13,14)` with true shared edge `(13,14)`. Globally `(12,30,20)->(10,24,16)`. Old labels `3,5,6,7` and their complete stars disappear. Label `11` is retained because preserving target face `[10,11,12]` requires it. The original unwanted stable `[12,6,1]`, unstable `3`, and saddles `(3,12),(5,12)` are absent from the post-event lattice.

## 3. Exact post-event endpoint `E10`

Active labels are `[1,2,4,8,9,10,11,12,13,14]` with the same denominator `D`:

```text
1: (-7715758938572,2889556079942,-17779918034961)
2: (-8262479746679,1678647340512,-17660251163923)
4: (-19707343224389,-41384307037227,-17592329907461)
8: (-5658133234447,-11830031585001,-22901357099805)
9: (-24778822577834,-27890508662314,-3487947517004)
10: (-17333854524801,-42073399768973,-17068563828311)
11: (7425371686672,6793144760174,-22628800214142)
12: (4728022774716,39660727728711,500165975828058)
13: (10760034733605,68069391392350,42437702267733)
14: (-22123888254578,15252741379,1754217266202)
```

Exact volume:
`1681266850734491086730347774173197219339093/32667107224410092492483962313449748299776` `~=51.46665847039511`.

Exact first moments:
`Mx=-13084743467721568266078774833771361473855413627251610057/1149371655649416643768760270362731887714054341637701632`;
`My=97307922671002678684688269731363929366427954638239779935/2298743311298833287537520540725463775428108683275403264`;
`Mz=816657661288454335992266470234363718618523047275588334629/2298743311298833287537520540725463775428108683275403264`.

Exact centroid:
`C=(-13084743467721568266078774833771361473855413627251610057/59154318456861104510651131992312016869945697642926309376, 97307922671002678684688269731363929366427954638239779935/118308636913722209021302263984624033739891395285852618752, 816657661288454335992266470234363718618523047275588334629/118308636913722209021302263984624033739891395285852618752)`.
The verifier proves all three identities `M_j=VC_j`; after translation all moments are exactly zero.

Maximal outward faces:

`[14,9,12] [14,12,13] [11,13,12] [11,10,8] [11,12,10] [4,8,10] [4,9,14] [4,12,9] [4,10,12] [1,11,8] [1,14,13] [1,13,11] [2,8,4] [2,1,8] [2,4,14] [2,14,1]`

True edges:

`(1,2) (1,8) (1,11) (1,13) (1,14) (2,4) (2,8) (2,14) (4,8) (4,9) (4,10) (4,12) (4,14) (8,10) (8,11) (9,12) (9,14) (10,11) (10,12) (11,12) (11,13) (12,13) (12,14) (13,14)`.

For each oriented face `(a,b,c)`, the irredundant H-row is generated exactly by `n=primitive((Q_b-Q_a)x(Q_c-Q_a))`, `h=n·Q_a`, and centred inequality `n·x<=h/D-n·C`. All 16 rows are strict on nonincident vertices. Minimum integer support slack is `9776338830952858060953569106190027892`; minimum Euclidean and circumradius-normalized separations are `0.003130013871669396` and `0.00014503223880626682`.

### Exhaustive face audit

Each line is `face, normalized minimum, status`:

```text
[14,9,12] -0.0154465241174412 -
[14,12,13] +0.024886862112928 S
[11,13,12] -0.00541857395342467 -
[11,10,8] -0.204769773732878 -
[11,12,10] +0.0157721288269942 S
[4,8,10] -0.0644561157121657 -
[4,9,14] -0.243225430644236 -
[4,12,9] -0.043092559967466 -
[4,10,12] -0.00478910821755726 -
[1,11,8] -0.147226108422793 -
[1,14,13] -0.207684914219085 -
[1,13,11] -0.137535634241298 -
[2,8,4] -0.239989987338123 -
[2,1,8] -0.229951025656364 -
[2,4,14] -0.183162765243266 -
[2,14,1] -0.130032251666396 -
```

### Exhaustive vertex audit

```text
1 -0.146697682184909 -
2 -0.159303440658457 -
4 +0.0749267544354441 U
8 -0.00284422925087448 -
9 -0.290927143379719 -
10 -0.0682725175625142 -
11 -0.00395296812512303 -
12 +0.99112782578146 U
13 -0.0532080894652955 -
14 -0.225441539563709 -
```

### Exhaustive true-edge four-component audit

Each tuple is `(t,1-t,alpha/R,beta/R)` for the two incident unit outward normals:

```text
[1,2] (+0.3070086504,+0.6929913496,+0.9452140206,-0.6968371241) min=-0.6968371241 -
[1,8] (-3.542931217,+4.542931217,+0.65551767,-0.3437345378) min=-3.542931217 -
[1,11] (-2.134027711,+3.134027711,+0.5891999547,-0.3028336472) min=-2.134027711 -
[1,13] (+1.120824968,-0.1208249678,-0.363259245,+0.5482659087) min=-0.363259245 -
[1,14] (+4.403892018,-3.403892018,-0.410597442,+0.5848929364) min=-3.403892018 -
[2,4] (-0.2978676749,+1.297867675,+1.176125651,-0.9307036351) min=-0.9307036351 -
[2,8] (-4.108288467,+5.108288467,-2.752485677,+3.034895829) min=-4.108288467 -
[2,14] (+4.579341129,-3.579341129,+1.274326185,-1.073349805) min=-3.579341129 -
[4,8] (+1.032573398,-0.03257339835,+0.3339314948,+0.07980927822) min=-0.03257339835 -
[4,9] (+6.476831795,-5.476831795,+0.2429234438,-0.09211609642) min=-5.476831795 -
[4,10] (+11.2600071,-10.2600071,+0.3788734723,+0.08167361929) min=-10.2600071 -
[4,12] (+0.2793775976,+0.7206224024,-0.006830256071,+0.09657067532) min=-0.006830256071 -
[4,14] (+2.370426391,-1.370426391,-1.681513317,+1.877156398) min=-1.681513317 -
[8,10] (+0.02384344753,+0.9761565525,-0.1549617005,+0.5219553266) min=-0.1549617005 -
[8,11] (+1.065936893,-0.06593689303,+0.2211806548,+0.2296989282) min=-0.06593689303 -
[9,12] (+0.2562538571,+0.7437461429,-0.08133807752,+0.1310098201) min=-0.08133807752 -
[9,14] (+2.326938764,-1.326938764,-0.4644325231,+0.5801235097) min=-1.326938764 -
[10,11] (+0.767105423,+0.232894577,+0.4692886575,-0.2535901197) min=-0.2535901197 -
[10,12] (+0.2786936627,+0.7213063373,+0.009596060035,+0.09025008371) min=+0.009596060035 H
[11,12] (+0.2755030115,+0.7244969885,+0.04029808408,-0.01384455778) min=-0.01384455778 -
[11,13] (+1.22586371,-0.2258637101,+0.1437031708,+0.2731527928) min=-0.2258637101 -
[12,13] (+0.8204479676,+0.1795520324,+0.3515320204,+0.3541595024) min=+0.1795520324 H
[12,14] (+0.7578334563,+0.2421665437,+0.07113748421,-0.0441528892) min=-0.0441528892 -
[13,14] (+0.1242712184,+0.8757287816,-0.4195868094,+0.5087724997) min=-0.4195868094 -
```

Therefore `E10` has strict `(S,U,H)=(2,2,2)`: stable `[14,12,13]`,`[11,12,10]`; unstable `4,12`; saddles `(10,12),(12,13)`. The smallest signed normalized feature separation is `0.002844229250874478`. The intended stable and unstable features survive with margins `+0.0157721288269942` and `+0.99112782578146`.

## 4. Exact synchronized multiwall atlas

Hold `E10` fixed and reinsert old labels as shallow caps:

`3->[14,9,12]`, `5->[11,13,12]`, `6->[1,13,11]`, `7->[14,12,13]`.

For each old label `k`, define `p_k(s)=b_k-s d_k`, `-1<=s<=1`, where

```text
b3=(-1317959001803/1649267441664,122765331331/549755813888,62304030697157/6597069766656)
b5=(22913429194993/52776558133248,38174421293745/17592186044416,173324959293883/17592186044416)
b6=(10469647481705/52776558133248,38876046116233/26388279066624,338164003105/8796093022208)
b7=(-6635830746257/52776558133248,13468171482805/6597069766656,181452631787331/17592186044416)
d3=(-1/4096,295622085640177060337521643/14029549058488452251802611523584,322033445055507961644894875/28059098116976904503605223047168)
d5=(1/4096,-6396171601572686358164567/408184462895507029059120610304,274885731549232212434043277/122455338868652108717736183091200)
d6=(-22963090118849689949280119/170897032811123905680376212992,1/4096,-38115604231668705784288437/170897032811123905680376212992)
d7=(-1/4096,2549550760888367400797783089/22054274959644765394720328966144,261842464958875203855923359/66162824878934296184160986898432)
```

Each `b_k` is the exact face barycentre and each outward `d_k` has `L_infinity` norm `2^-12`. For `s<0` all four old cap vertices are active; for `s>0` all are inactive. Cross-edge `(13,14)` is true on both sides.

All `C(14,4)=1001` affine circuit determinants were expanded exactly. None is identically zero. Exactly seven have a root in `[-1,1]`:

```text
(1,5,6,12): degree 2, unique simple root s=0
(1,6,11,13): degree 1, unique simple root s=0
(3,7,9,13): degree 2, unique simple root s=0
(3,9,12,14): degree 1, unique simple root s=0
(5,7,11,14): degree 2, unique simple root s=0
(5,11,12,13): degree 1, unique simple root s=0
(7,12,13,14): degree 1, unique simple root s=0
```

No other circuit root exists. At `s=0` the four old points lie in face interiors, all seven circuits vanish, and inactive separation is zero; the wall is not an admissible endpoint.

The two exact open cells are:

- `-1<=s<0`: actual `(V,E,F)=(14,36,24)`, class `(2,2,2)`, stable `[11,12,10]`,`[7,14,12]`, unstable `4,12`, saddles `(10,12),(12,13)`. Faces: `[11,10,8] [11,12,10] [4,8,10] [4,9,14] [4,12,9] [4,10,12] [3,9,12] [3,14,9] [3,12,14] [7,12,13] [7,13,14] [7,14,12] [5,13,12] [5,11,13] [5,12,11] [6,13,11] [1,11,8] [1,6,11] [1,14,13] [1,13,6] [2,8,4] [2,1,8] [2,4,14] [2,14,1]`. Edges: `(1,2) (1,6) (1,8) (1,11) (1,13) (1,14) (2,4) (2,8) (2,14) (3,9) (3,12) (3,14) (4,8) (4,9) (4,10) (4,12) (4,14) (5,11) (5,12) (5,13) (6,11) (6,13) (7,12) (7,13) (7,14) (8,10) (8,11) (9,12) (9,14) (10,11) (10,12) (11,12) (11,13) (12,13) (12,14) (13,14)`.
- `0<s<=1`: actual `E10`, `(10,24,16)`, class `(2,2,2)`, stable `[14,12,13]`,`[11,12,10]`, unstable `4,12`, saddles `(10,12),(12,13)`.

For the pre-cell the exact boundary integration gives affine `V6(s)=6V(s)` and quadratic `N_j(s)=24M_j(s)`, with `C_j(s)=N_j(s)/(4V6(s))`; therefore `M_j=VC_j` identically. The verifier enumerates 288 equilibrium-component polynomials and 264 nonincident support polynomials and proves zero internal roots in `(-1,0)`. It also proves 64 old-point support inequalities strictly negative throughout `(0,1]`.

**Rigorous obstruction:** the extra stable equilibrium transfers from daughter face `[7,14,12]` to parent face `[14,12,13]` as the complete old star collapses. Extra unstable `4` and saddles `(10,12),(12,13)` persist. There is no hidden circuit or equilibrium wall in either open cell.

The disk comparison is between literal `G27` and literal `E10`. The shallow-cap family is an exact local realization of the same synchronous complete-star collapse after preparatory deformation; it is not claimed to be one affine homotopy beginning at the literal `G27` coordinates.

## 5. Perturbation and independent verification

A simultaneous independent perturbation of all 30 active coordinate entries by at most `2^-12=1/4096` preserves the complete `(10,24,16)` lattice and `(2,2,2)` class. Exact volume enclosure:

`[1679775458268598965498488567335338751499093/32667107224410092492483962313449748299776, 560919454477144193677488447462472166650823/10889035741470030830827987437816582766592]`.

A `2^-11` box first fails an inactive-edge certificate; `2^-10` reaches a hull wall. A separately coded SciPy/Qhull audit reconstructs the same lattice and positive features. Trimesh independently reports for both OBJ and STL: 10 vertices, 16 triangles, watertight, winding-consistent, Euler number 2, volume `51.46665847039512`, centre of mass within `4.7e-16` of zero. A separate event checker samples 101 points in each open cell and obtains only the two certified states.

## 6. Smallest genuinely new topology

The exact local branch is exhausted. The smallest unrepresented connected successor removes the complete `E10` residual disk with internal vertices `(4,9,13,14)` and boundary hexagon `[1,2,8,10,12,11]`, preserves outside target face `[10,11,12]`, and fills the disk with two new internal vertices sharing an edge. It would have global `(V,E,F)=(8,18,12)`. This can delete extra S `[14,12,13]`, U4, H(12,13), and replace the second face incident to `(10,12)` in one operation. A 75,000-proposal empirical scan found 12,689 valid all-eight-active target-preserving bodies but no `(1,1,0)`, `(2,1,1)`, or `(1,2,1)` body; this is discovery evidence, not an exclusion.

## 7. Artifacts

- [Portable exact bundle](sandbox:/mnt/data/g27_apex_two_cell_nonwinner.zip)
- [Full immutable handoff](sandbox:/mnt/data/g27_apex_two_cell_result/RESULT.md)
- [Exact source verifier](sandbox:/mnt/data/g27_apex_two_cell_result/verify_G27_start.py)
- [Exact endpoint verifier](sandbox:/mnt/data/g27_apex_two_cell_result/verify_postevent_exact.py)
- [Complete endpoint report](sandbox:/mnt/data/g27_apex_two_cell_result/E10_exact_report.json)
- [Exact H rows](sandbox:/mnt/data/g27_apex_two_cell_result/E10_H_representation.json)
- [Perturbation certificate](sandbox:/mnt/data/g27_apex_two_cell_result/E10_perturbation_certificate.json)
- [Independent endpoint report](sandbox:/mnt/data/g27_apex_two_cell_result/E10_independent_verification.json)
- [Watertight OBJ](sandbox:/mnt/data/g27_apex_two_cell_result/E10_centered.obj)
- [Watertight STL](sandbox:/mnt/data/g27_apex_two_cell_result/E10_centered.stl)
- [Patch complex](sandbox:/mnt/data/g27_apex_two_cell_result/patch_complex.json)
- [Exact event specification](sandbox:/mnt/data/g27_apex_two_cell_result/simultaneous_caps_event_spec.json)
- [Circuit atlas](sandbox:/mnt/data/g27_apex_two_cell_result/event_circuit_atlas.json)
- [Equilibrium atlas](sandbox:/mnt/data/g27_apex_two_cell_result/event_equilibrium_atlas.json)
- [Independent event report](sandbox:/mnt/data/g27_apex_two_cell_result/event_independent_verification.json)

A clean extraction and `./[internal-source-reference].sh` ends with `ALL VERIFIERS PASSED`.

## Reusable conclusion

Literal verdict: **NONWINNER**. `E10` is the strongest exact post-event body: `(10,24,16)`, own-centred `(2,2,2)`, positive `2^-12` perturbation box. The original `G27` residual labels disappear in one connected disk replacement, but the Euler-neutral block transfers to S `[14,12,13]`, U4, H(10,12), H(12,13). The smallest nonduplicative successor is the exact eight-vertex hexagonal-boundary two-internal-edge cell.
