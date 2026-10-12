# figure-0098

AI research report · 2026-08-27 UTC

---

# Complete research handoff — exact cross-rail frontier, not a claimed winner

## Verdict

I did **not** obtain a finite homogeneous convex polyhedral Gömböc. The strongest fully materialized exact endpoint is an exact rational **(S,U,H)=(2,1,1)** polyhedron with one target stable face, one residual stable face, the unique target unstable vertex, and one residual saddle edge. It is therefore a strict frontier improvement over the journal's transferred endpoint G, whose defect was `(2,2,2)` with the extra unstable rail `{5,6}`. The source journal gives F's reconstructible coordinates and stated audit at lines 1086–1106, and describes G and the missing cross-rail operation at lines 912–920. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

The endpoint here eliminates the transferred extra unstable rail completely: **U=1** and the sole unstable vertex is the preserved target. The old cap `{8,11,12}`, all obsolete F rows, and five obsolete rail rows are strictly interior. A connected two-vertex cross-rail zipper cuts the earlier closure stable face and replaces its two saddle stars in one synchronized common-face event. The remaining obstruction is one stable/saddle pair at opposite ends of the annular closure.

## What was actually tried

1. Reconstructed F from the journal decimals with exact rational arithmetic. The literal rounded rows split the two intended quads, so I applied the minimum-norm rational incidence repair: vertex 7 was projected onto `aff(1,2,6)` and vertex 10 onto `aff(1,6,9)`. The displacement norms are `1.3646940283336739e-18` and `1.2997815791567355e-18`.
2. Recomputed exact maximal faces, true edges, volume, centroid, and every full face/vertex/edge equilibrium test. This recovers `(V,E,F,C)=(13,31,20,62)` and `(S,U,H)=(2,2,2)` exactly.
3. Built an independent 34-point two-branch annular volume mover from F, then inserted two cross-rail zipper vertices. The pre-zipper U1 cell is `(V,E,F)=(37,105,70)` and `(S,U,H)=(3,1,2)`: the target unstable is already unique.
4. Synchronized both zipper vertices through the same U1 face. This cuts that stable face and replaces its two saddle stars, producing the exact final `(2,1,1)` cell.
5. Tried one-point and multi-point continuations: random q3 insertions, local qA/qB optimization, fixed-cell depth optimization, dual-path face stacking, and full-path visibility linear programs. None produced a strict `(1,1,0)` endpoint. The best numerically less-negative local q2 cell had hard score about `-1.17e-3`, but its inactive gap collapsed to `2.84e-8`; the robust exact endpoint below was retained instead.

## Exact reconstruction of F

The exact-repaired F has:

- exact volume approximately `0.00054077374562179915`;
- exact own centroid approximately `[-0.08180353679927678, 0.0001316531387013302, 0.005910260895947606]`;
- stable faces `[[2, 0, 3], [6, 7, 2, 1]]`;
- unstable vertices `[5, 8]`;
- saddle edges `[[0, 1], [7, 10]]`;
- normalized strict nonincidence separation `7.4876878442155833e-07`.

The complete exact repaired coordinates, projection deltas, exact H-representation, face cycles, edges, volume and centroid are in [`endpoint_F_exact.json`](sandbox:/mnt/data/gomboc_crossrail_package/endpoint_F_exact.json). The exact F meshes are [`endpoint_F.obj`](sandbox:/mnt/data/gomboc_crossrail_package/endpoint_F.obj) and [`endpoint_F.stl`](sandbox:/mnt/data/gomboc_crossrail_package/endpoint_F.stl).

## Exact final V-data

Every token below is an exact terminating-decimal rational. Vertices 0,1,2,3 are exactly F0,F2,F3,F5; 3 is the target unstable vertex. Vertices 4–18 and 19–32 are the two rails; 33–34 are the connected zipper.

```text
00 F0               -2.595474164348944957 -0.012566706508073207 0.070947774660818738
01 F2               2.309051967174282183 0.016799621324576530 -0.018953898022694479
02 F3               0.586877772857189228 -0.002921362177360634 -0.031858689597751316
03 F5_target        2.625351592784080701 0.008584879304338922 -0.080028597101769683
04 lower_rail_00    -2.594067180404565 0.015874399931474277 0.15699512112904457
05 lower_rail_01    -2.5713095157161634 0.095392830637436726 0.53393809862817454
06 lower_rail_02    -2.4742827687989175 0.17482318343997216 0.90700156599739679
07 lower_rail_03    -2.3036117133308935 0.25119572525233402 1.2621782769745287
08 lower_rail_04    -2.0626812347458836 0.32153518688285548 1.5855635246810482
09 lower_rail_05    -1.7576213124777884 0.38297103871204913 1.863875656961242
10 lower_rail_06    -1.3971894506408233 0.43284829901326743 2.084974327208851
11 lower_rail_07    -0.99255081075319063 0.46883478099870041 2.2383571426902784
12 lower_rail_08    -0.5569601094981409 0.48902065274964257 2.3156153991247672
13 lower_rail_09    -0.10535315578127813 0.49200630421532698 2.3108303353008166
14 lower_rail_10    0.34614042698361036 0.4769747890744217 2.2208928059313076
15 lower_rail_11    0.7807483573054772 0.44374553244538378 2.0457314292416382
16 lower_rail_12    1.1816528233337817 0.3928065584883883 1.7884370656167639
17 lower_rail_13    1.532613248951963 0.32532317956042855 1.4552748467505936
18 lower_rail_14    1.8185925977201252 0.24312188022467404 1.0555787988332452
19 upper_rail_00    -2.5974079843523641 -0.025584284043348043 -0.038802677087221391
20 upper_rail_01    -2.5875207538901477 -0.10576331078253337 -0.41616278262947703
21 upper_rail_02    -2.5032785367097024 -0.18496435853193197 -0.79236770900491083
22 upper_rail_03    -2.3448278673999567 -0.26022231248815869 -1.1533960716020888
23 upper_rail_04    -2.115077164396153 -0.32859958522932681 -1.4852278050900396
24 upper_rail_05    -1.819699478668825 -0.38729631892991634 -1.7743649036536673
25 upper_rail_06    -1.467032677724577 -0.43375989206566734 -2.0083536565690281
26 upper_rail_07    -1.0678766586643138 -0.46578963577628718 -2.1762890439256117
27 upper_rail_08    -0.63519099196133988 -0.48163267874026044 -2.2692818444262586
28 upper_rail_09    -0.18370023191923535 -0.48006700521996676 -2.2808696120684404
29 upper_rail_10    0.27058215089527371 -0.46046812879949078 -2.2073540074540103
30 upper_rail_11    0.71089679831797437 -0.42285624855515563 -2.0480490021713655
31 upper_rail_12    1.1203309723932828 -0.36792135359890116 -1.8054271638760961
32 upper_rail_13    1.4824405216675705 -0.29702445927700177 -1.4851545018186838
33 zipper_A         -2.5961359902755627 -0.0030694937859964445 0.054106244616680205
34 zipper_B         -1.6675596046415924 0.11415923551861645 0.06403116547620194
```

The exact volume is

`2835096734707123048087090790009001741800470793647430193/4000000000000000000000000000000000000000000000000000000`

and the exact uncentered own centroid is

```text
c[0] = -2237543863930681990546377655892664724088858656447393479397581596722544119/3780128979609497397449454386678668989067294391529906924000000000000000000
c[1] = 225522473804104991320307664915938014719407682104702731681873129553984477/7560257959218994794898908773357337978134588783059813848000000000000000000
c[2] = 23230616958534975700838242837739067524120966024554579229444445291301753/850529020412136914426127237002700522540141238094229057900000000000000000
```

Numerically, `c=[-0.591922623804712, 0.029829997206524204, 0.027313138530274044]` and `V=0.7087741836767808`. Translating every vertex by this exact rational centroid makes all three uniform-volume first moments **identically zero**.

## Active H/V topology

The exact endpoint is simplicial with `(V,E,F,C)=(35,99,66,198)`. The following are the oriented maximal-face cycles:

```text
0:(1,0,2) 1:(15,0,1) 2:(2,0,29) 3:(0,5,4) 4:(0,4,33) 5:(5,0,6) 6:(6,0,7) 7:(7,0,8) 8:(8,0,9) 9:(9,0,10) 10:(10,0,11) 11:(11,0,12) 12:(12,0,13) 13:(13,0,14) 14:(14,0,15) 15:(19,20,0) 16:(33,19,0) 17:(21,0,20) 18:(22,0,21) 19:(23,0,22) 20:(24,0,23) 21:(25,0,24) 22:(26,0,25) 23:(27,0,26) 24:(28,0,27) 25:(29,0,28) 26:(2,30,1) 27:(3,17,1) 28:(1,32,3) 29:(15,1,16) 30:(16,1,17) 31:(31,1,30) 32:(32,1,31) 33:(30,2,29) 34:(17,3,18) 35:(3,34,18) 36:(32,34,3) 37:(4,5,33) 38:(6,34,5) 39:(5,34,33) 40:(7,34,6) 41:(8,34,7) 42:(9,34,8) 43:(10,34,9) 44:(11,34,10) 45:(12,34,11) 46:(13,34,12) 47:(14,34,13) 48:(15,34,14) 49:(16,34,15) 50:(17,34,16) 51:(18,34,17) 52:(33,20,19) 53:(20,34,21) 54:(33,34,20) 55:(21,34,22) 56:(22,34,23) 57:(23,34,24) 58:(24,34,25) 59:(25,34,26) 60:(26,34,27) 61:(27,34,28) 62:(28,34,29) 63:(29,34,30) 64:(30,34,31) 65:(31,34,32)
```

The true edge set is:

```text
0-1 0-2 0-4 0-5 0-6 0-7 0-8 0-9 0-10 0-11 0-12 0-13 0-14 0-15 0-19 0-20 0-21 0-22 0-23 0-24 0-25 0-26 0-27 0-28 0-29 0-33 1-2 1-3 1-15 1-16 1-17 1-30 1-31 1-32 2-29 2-30 3-17 3-18 3-32 3-34 4-5 4-33 5-6 5-33 5-34 6-7 6-34 7-8 7-34 8-9 8-34 9-10 9-34 10-11 10-34 11-12 11-34 12-13 12-34 13-14 13-34 14-15 14-34 15-16 15-34 16-17 16-34 17-18 17-34 18-34 19-20 19-33 20-21 20-33 20-34 21-22 21-34 22-23 22-34 23-24 23-34 24-25 24-34 25-26 25-34 26-27 26-34 27-28 27-34 28-29 28-34 29-30 29-34 30-31 30-34 31-32 31-34 32-34 33-34
```

The complete exact H-data are stored face-by-face as rational outward normals and offsets `n·x <= h` in [`crossrail_endpoint_exact.json`](sandbox:/mnt/data/gomboc_crossrail_package/crossrail_endpoint_exact.json). That file also contains the exact V-data, incidence sphere, centered coordinates, mechanics, perturbation data, and all 49 construction-row statuses.

## Exhaustive own-centroid mechanics audit

- Stable face 0: target cycle `(1,0,2)`.
- Stable face 36: residual cycle `(32,34,3)`.
- Unique unstable vertex: `3`.
- Unique saddle edge: `(4,33)`.
- Euler/Poincaré check: `S+U-H = 2+1-1 = 2`.

Normalized class-preservation margins:

| certificate family | lower margin |
|---|---:|
| stable-face positive primitives | `8.8185550822443399e-05` |
| nonstable-face external witnesses | `7.3664031537789461e-05` |
| target unstable normal-cone margin | `0.36613565941671072` |
| nonunstable-vertex external witnesses | `0.0010474315430362435` |
| saddle positive primitives | `0.0036756020163150379` |
| nonsaddle-edge exclusion witnesses | `7.3664031539610311e-05` |
| active face/nonincident-vertex separation | `3.400551921965981e-06` |

An independent pure-standard-library verifier enumerates **every** supporting triple, reconstructs all maximal faces and true edges, computes the exact centroid and volume, audits every complete normal cone, and then uses exact rational interval arithmetic to certify the same topology and `(2,1,1)` mechanics for every coordinatewise perturbation `|delta x_ij| <= 10^-9`. Its recorded output is:

```text
PASS: V=35 E=99 F=66; exact centroid; S=2 U=1 H=1; interval box eps=1e-9.
Stable cycles: [[1, 0, 2], [32, 34, 3]] unstable: [3] saddle: [(4, 33)]
```

The verifier is [`verify_exact_and_interval.py`](sandbox:/mnt/data/gomboc_crossrail_package/verify_exact_and_interval.py).

## Genuine cross-rail incidence

The zipper edge `(33,34)` is true. Its incident true-edge set is:

```text
0-33 3-34 4-33 5-33 5-34 6-34 7-34 8-34 9-34 10-34 11-34 12-34 13-34 14-34 15-34 16-34 17-34 18-34 19-33 20-33 20-34 21-34 22-34 23-34 24-34 25-34 26-34 27-34 28-34 29-34 30-34 31-34 32-34 33-34
```

Vertex 33 is incident to both rail starts: lower `4,5` and upper `19,20`. Vertex 34 is incident to lower `5..18`, upper `20..32`, target vertex 3, and vertex 33. Thus the two branches are not merely parallel sections: the facial sphere contains genuine cross-branch incidences and a connected annular bridge.

## Exact synchronized circuit evidence

### Zipper emergence

Before the zipper, U1 has stable cycles `(5,22,0)`, `(36,5,18)`, and target `(1,0,2)`; unique unstable 4; saddles `(5,22)` and `(0,22)`. Both zipper rays leave the exact U1 hull through the **same** stable face `(36,5,18)`. With `x_i(s)=c_U+rho_i(s)(q_i-c_U)` and piecewise-affine schedules chosen so `rho_i(1/2)=rho_i*`, both boundary crossings occur at one global parameter value:

- zipper_A: rho=1085109452983665511530429030509349939150891686542574483622921936927370043971718250792175446005585316983/2190867230543504274677646878540481455715939175698491038844632720712528766097917619204672421214460066983 ≈ 0.49528763672021997; barycentric=[0.16526840820865238, 0.7670735250927665, 0.0676580666985812]
- zipper_B: rho=3255328358950996534591287091528049817452675059627723450868765810782110131915154752376526338016755950949/132116132514930747576264237513731043652598566112696692874228563586727903635174430969149488085945162666149 ≈ 0.02463990049499144; barycentric=[0.28577246128706735, 0.5418259316140401, 0.17240160709889255]

All barycentric coordinates are strictly positive, so both crossing points lie in the relative interior of the same triangle. At the event the three old face vertices and both zipper points form one connected five-point coplanarity. The closure stable face and its two saddle stars are replaced, and the post-event cell is the exact `(2,1,1)` endpoint.

### Simultaneous old-cap absorption

For the final hull H with exact centroid c, move each old cap row by `x_i(s)=c+rho_i(s)(F_i-c)`. The three radial boundary hits all occur in the relative interior of the **same** final face `(0,4,33)`. Independent piecewise-affine schedules synchronize them at `s=1/2`:

- F8: rho=176897864835470263443793977101687487937527980999725883953301990960366200068083051055139287879370778559838931/176895573501178725965271614783080976877362477258727920281971626616398678856055802611906259347590783838303979 ≈ 1.0000129530335111; barycentric=[0.8881919114806979, 0.025113974690070855, 0.08669411382923126]
- F11: rho=176897864835470263443793977101687487937527980999725883953301990960366200068083051055139287879370778559838931/176896986083469659261534928123186063652970141548612063629895004026967642252540209729826423942137189001636999 ≈ 1.0000049675917044; barycentric=[0.9396670219864005, 0.011908984352966908, 0.04842399366063261]
- F12: rho=176897864835470263443793977101687487937527980999725883953301990960366200068083051055139287879370778559838931/176896797357627063653051258999872978950117423396465914913179950793268029114660338641571387374701083286882099 ≈ 1.0000060344667576; barycentric=[0.9485209589815276, 0.013205732784186273, 0.038273308234286214]

Thus F8,F11,F12 can be absorbed in one connected six-point coplanarity with face `(0,4,33)`, rather than as three unrelated endpoint deletions. The exact fractions, boundary points, schedules, all 36 added rows, and direct affine witness path are in [`circuit_path_exact.json`](sandbox:/mnt/data/gomboc_crossrail_package/circuit_path_exact.json).

## Inactive construction rows and separation

The full exact construction has 49 rows: F0..F12 and A00..A35. Final active combined labels are `[0, 2, 3, 5, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 47, 48]`. Strictly interior labels are `[1, 4, 6, 7, 8, 9, 10, 11, 12, 28, 29, 44, 45, 46]`. This includes old cap F8,F11,F12 and all obsolete F/rail rows. Every inactive row satisfies every final supporting inequality strictly. The minimum normalized distance to the final boundary is `1.9025835929243958e-06`. [`verify_inactive_rows.py`](sandbox:/mnt/data/gomboc_crossrail_package/verify_inactive_rows.py) performs this audit with exact fractions.

## Volume and moment shift

- F: `V≈0.00054077374562179915`, `c≈[-0.08180353679927678, 0.0001316531387013302, 0.005910260895947606]`.
- U1: `V≈0.068742511575944493`, `c≈[-0.6059375594289373, 0.0012724020018477105, 0.021703874847046858]`.
- Final: `V≈0.7087741836767808`, `c≈[-0.591922623804712, 0.029829997206524204, 0.027313138530274044]`.
- Volume factor final/F: `1310.6667796192828`.
- Cartesian centroid shift: `[-0.5101190870054351, 0.029698344067822874, 0.02140287763432644]`.
- In the target-face orthonormal frame the centroid moves from approximately `(2.51447136,0.0190344419,0.0016231694)` to `(2.00423263,0.00046152123,0.0311704768)`, a shift `(-0.51023873,-0.01857292,+0.02954731)`.

This is a genuine uniform-volume move; it is not an auxiliary-center audit.

## Quantified remaining obstruction

The residual stable face 36 `(32,34,3)` and saddle edge `(4,33)` lie at opposite ends of the annulus. Their two shortest dual paths to the saddle's incident faces have lengths 16 and 15:

```text
P0 = [36, 65, 64, 63, 62, 25, 24, 23, 22, 21, 20, 19, 18, 17, 15, 16, 4]
P1 = [36, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 53, 54, 39, 37]
```

A one-point visibility LP maximized a common margin for seeing every face of each full path while protecting the target face. On P0 the margin remains negative through the target-frame box `[-5,5]^3`; the first sampled positive value is at `B=10`, where the point sees 36 of 66 faces and the resulting mechanics are `(2,4,4)`. On P1 positivity starts at `B=0.2`, but the point already sees 31 faces and returns `(2,2,2)`. This is not a theorem that no larger distributed construction works; it is a quantified obstruction to the missing **single-cone** move. The reproducible LP and table are [`obstruction_lp.py`](sandbox:/mnt/data/gomboc_crossrail_package/obstruction_lp.py) and [`obstruction_results.json`](sandbox:/mnt/data/gomboc_crossrail_package/obstruction_results.json).

The most useful continuation is therefore a **distributed multi-vertex zipper along one of these dual paths**, with at least two independently actuated terminal vertices so that the residual stable primitive and residual saddle primitive cross zero in the same topology-changing event. Adding more parallel rail sections is not indicated; the needed degrees of freedom must alter visibility along the dual path and provide two independent moment directions.

## Reproducible artifacts

- [Complete package ZIP](sandbox:/mnt/data/gomboc_crossrail_package.zip) — SHA-256 `6c9bd271fa8373b7e6d695a92c2e196d3e51f6d3e560abaf1f05ef63ecf7684d`
- [Package README](sandbox:/mnt/data/gomboc_crossrail_package/README.md)
- [Exact endpoint JSON](sandbox:/mnt/data/gomboc_crossrail_package/crossrail_endpoint_exact.json)
- [Exact circuit path JSON](sandbox:/mnt/data/gomboc_crossrail_package/circuit_path_exact.json)
- [Independent exact + interval verifier](sandbox:/mnt/data/gomboc_crossrail_package/verify_exact_and_interval.py)
- [Centered endpoint OBJ](sandbox:/mnt/data/gomboc_crossrail_package/crossrail_endpoint.obj)
- [Centered endpoint STL](sandbox:/mnt/data/gomboc_crossrail_package/crossrail_endpoint.stl)
- [Deterministic mesh rebuilder](sandbox:/mnt/data/gomboc_crossrail_package/rebuild_meshes.py)
- [Verification transcript](sandbox:/mnt/data/gomboc_crossrail_package/VERIFICATION.txt)

## Bottom line

This is not the requested winner, and I do not label it one. It is an exact, independently verified, perturbation-safe cross-rail endpoint that advances the journal frontier from two unstable vertices to one, gives explicit synchronized circuit replacements for the old cap and the pre-zipper saddle stars, closes all ordinary volume moments exactly, and isolates the remaining failure to one stable/saddle pair with a measured dual-path visibility obstruction.
