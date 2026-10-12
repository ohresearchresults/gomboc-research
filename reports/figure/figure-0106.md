# figure-0106

AI research report · 2026-08-27 UTC

---

# Rapid Maple 23 — complete finite handoff

## Verdict

No 34–42-input own-centroid Gömböc was found. The strongest fully materialized endpoint is the exact 42-input rational body **M42-SLP**, but its exhaustive own-centroid class is strictly `(S,U,H)=(2,2,2)`, so I do **not** report it as a Gömböc. It does complete the requested macroscopic step: all inherited rows `17–24` become interior, the old stable triangle `(18,20,22)` and saddle `(23,24)` disappear from the rebuilt lattice, twelve new macroscopic rows carry body-scale volume and actuate all three first moments, and the defect transfers to one extra stable face, one extra unstable vertex, and two saddle edges. The exact seed and assigned corridor target are in the journal. The prior exclusion of shallow/local continuation is also preserved.

## Exact generator and inputs

Interpret every displayed coordinate as a literal terminating rational; equivalently scale every coordinate to the common denominator `10^17`. Enumerate all `C(42,3)=11480` triples with integer determinants, keep exact supporting planes, merge coplanar triples, order each maximal face by exact orientation, derive true edges from face cycles, integrate exact tetrahedral volume/moments, translate by the exact centroid, and classify every maximal face, active vertex, and true edge using exact face-foot, adjacent-support, and two-normal-cone primitives. This deterministic procedure is implemented in the linked exact verifier.

```text
00 (0.4756161830,-0.9337688508,0) A
01 (0.6842891459,-0.8989783949,0) A
02 (1.0481552627,-0.6112355097,0) A
03 (1.2755777124,-0.2202413337,0) A
04 (1.3637437814,0.2488334051,0) A
05 (1.2849044523,0.7410523649,0) A
06 (1.0170965409,1.1986517418,0) A
07 (0.6191297824,1.5351441689,0) A
08 (-0.0063866144,1.8754809932,0) A
09 (-0.6985041963,1.4979807161,0) A
10 (-1.0140947488,1.2174063967,0) A
11 (-1.2856529747,0.7456238685,0) A
12 (-1.3710870158,0.2483772792,0) A
13 (-1.2758033499,-0.2249267384,0) A
14 (-1.0483750550,-0.6045635047,0) A
15 (-0.7325841547,-0.8739513553,0) A
16 (-0.4260837488,-1.0043250072,0) A
17 (0.1254053900,-0.9818636314,-0.0822563738) I
18 (0.2262423217,-0.9527871690,-0.0822563738) I
19 (-0.2648479934,-1.0370197767,-0.0822563738) I
20 (-0.0130716858,-1.0014270294,-0.0825191734) I
21 (0.1242088087,-0.9820279589,-0.0825374227) I
22 (-0.0032138147,1.7794928099,-0.0028122892) I
23 (0.5616363774,-0.9211696869,-0.0136515101) I
24 (0.0522771486,-0.9956615507,-0.0809455855) I
25 (0.68636031882206316,-2.25682491321557377,-0.32997462781910897) I
26 (0.64097998343375240,-2.24385705208491970,-0.29112651499906500) I
27 (0.54740069358060317,-2.25548791947495220,-0.21148918096910521) I
28 (0.47448352070582772,-2.30164283051349994,-0.13899777034422278) A
29 (0.43901616620769562,-2.35446680093937122,-0.16379215365015806) A
30 (0.35502867444871983,-2.47740947901762931,-0.31458157054297048) A
31 (0.41450080640930032,-2.55678127710322700,-0.32804322948065862) A
32 (0.56492354041949477,-2.63143168195597532,-0.26237278876453612) A
33 (0.54243310689593016,-2.72368934280812347,-0.47641927501385978) A
34 (0.81596213832586661,-2.71073595634052911,-0.45812426040272303) A
35 (0.81621526036619740,-2.71069195273158137,-0.45795322379194470) A
36 (0.93877668608879794,-2.65347061773248383,-0.40411188999098618) A
37 (0.99240612223286262,-2.58938705699760430,-0.39921689104894637) A
38 (1.00118976812483118,-2.52223909154027170,-0.38998165682618718) A
39 (0.97731251839225231,-2.44121370603035714,-0.43423238004702647) I
40 (0.97376535754317561,-2.35959607564505447,-0.46389337454357249) A
41 (0.97071418197874793,-2.29729289531846392,-0.39082152115224439) I
```

`A` means extreme at the final endpoint; `I` means strictly interior. Active rows are `[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,29,30,31,32,33,34,35,36,37,38,40]`; inactive rows are `[17,18,19,20,21,22,23,24,25,26,27,39,41]`.

## Exact mass data

- `(V,E,F,C)=(29,67,40,134)`; Euler check `V-E+F=2`.
- Exact ordinary volume: `3702056925588554198256875532832399692295961450120267/3000000000000000000000000000000000000000000000000000` ≈ `1.234018975196185`.
- Exact input-frame centroid:
  - `c_x=14911266126291970291218680442585381020198308201234179308779688950021/59232910809416867172110008525318395076735383201924272000000000000000` ≈ `0.25173954685882788`
  - `c_y=-2045306624660345859124144547294383219632032062525015902581007338352599/2961645540470843358605500426265919753836769160096213600000000000000000` ≈ `-0.69059804649518675`
  - `c_z=-38310443446861378024830098365774161988650901966632689638735566273861/269240503679167578055045493296901795803342650917837600000000000000000` ≈ `-0.14229078806253043`
- Exact input-frame first moments:
  - `M_x=14911266126291970291218680442585381020198308201234179308779688950021/48000000000000000000000000000000000000000000000000000000000000000000` ≈ `0.31065137763108269`
  - `M_y=-2045306624660345859124144547294383219632032062525015902581007338352599/2400000000000000000000000000000000000000000000000000000000000000000000` ≈ `-0.85221109360847747`
  - `M_z=-140471625971825052757710360674505260625053307210986528675363743004157/800000000000000000000000000000000000000000000000000000000000000000000` ≈ `-0.17558953246478132`
- After translating by this exact centroid, all three ordinary uniform-volume first moments are exactly zero. All mechanics below are evaluated at that own centroid, never at an auxiliary point.

## Rebuilt maximal faces and true edges

```text
F00: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
F01: 0 28 1
F02: 0 16 28
F03: 1 28 2
F04: 2 28 3
F05: 3 37 4
F06: 3 28 37
F07: 4 40 5
F08: 4 37 38
F09: 4 38 40
F10: 5 40 6
F11: 6 40 7
F12: 7 40 8
F13: 8 40 9
F14: 9 33 10
F15: 9 40 33
F16: 10 33 11
F17: 11 33 12
F18: 12 33 13
F19: 13 33 14
F20: 14 29 15
F21: 14 32 29
F22: 14 31 30
F23: 14 30 32
F24: 14 33 31
F25: 15 28 16
F26: 15 29 28
F27: 28 29 32
F28: 28 32 37
F29: 30 31 32
F30: 31 33 32
F31: 32 33 35
F32: 32 35 36
F33: 32 36 37
F34: 33 34 35
F35: 33 40 34
F36: 34 36 35
F37: 34 37 36
F38: 34 40 37
F39: 37 40 38
```

```text
0-1  0-16  0-28  1-2  1-28  2-3  2-28  3-4  3-28  3-37
4-5  4-37  4-38  4-40  5-6  5-40  6-7  6-40  7-8  7-40
8-9  8-40  9-10  9-33  9-40  10-11  10-33  11-12  11-33  12-13
12-33  13-14  13-33  14-15  14-29  14-30  14-31  14-32  14-33  15-16
15-28  15-29  16-28  28-29  28-32  28-37  29-32  30-31  30-32  31-32
31-33  32-33  32-35  32-36  32-37  33-34  33-35  33-40  34-35  34-36
34-37  34-40  35-36  36-37  37-38  37-40  38-40
```

## Exhaustive own-centroid audit

The exact/directed audit enumerates all 40 maximal faces, all 29 active vertices, and all 67 true edges/full normal cones. Its result is:

- stable faces: target `F00=[0,1,…,16]`, margin interval `[0.055511271236745922,0.055511271236745936]`; extra `F13=[8,40,9]`, `[3.6887862045489355e-5,3.6887862045489368e-5]`;
- unstable vertices: target `V8`, `[0.3879732074611550,0.3879732074611552]`; extra `V34`, `[1.4552805736488565e-4,1.4552805736488570e-4]`;
- saddle edges: `E(4,38)`, `[8.406692503362472e-5,8.406692503362475e-5]`; `E(14,31)`, `[5.404729440762594e-5,5.404729440762596e-5]`;
- desired all-feature max–min score interval: `[-1.455280573648857e-4,-1.4552805736488565e-4]`;
- closest excluded features: `V35=-1.6993137794e-8`, `F[4,37,38]=-5.5965216475e-7`, `F[14,31,30]=-1.8051945185e-6`, `E(4,37)=-2.6715817861e-6`, `E(14,30)=-8.5436782926e-6`.

Thus the body is an open strict `(2,2,2)` cell, not a wall hit. The complete directed primitive intervals for every face/vertex/edge are in `skew_corridor_M42_audit.json`; the exact verifier proves their rational signs before interval normalization.

## Inactive separation and perturbation

- minimum inactive Euclidean separation: `[0.0028122891999999991,0.0028122892]`;
- normalized inactive separation: `[0.00060068176359748986,0.00060068176359749008]`;
- structured coordinate box radius `10^-12` preserves the complete lattice and class `(2,2,2)`: rows `0–16` vary independently in `x,y` with `z=0`; rows `17–41` vary independently in all three coordinates;
- directed box bounds include volume `>1.2340189751495778`, support slack `<-1.1668368685753821e-7`, stable primitive `>0.002426349210098781`, unstable primitive `>9.526591733922504e-8`, saddle primitive `>4.02785576766786e-13`, and all excluded-feature witnesses strictly negative.

## Macroscopic moment actuation

The seed volume is `180366322667516111281976387633/1000000000000000000000000000000`; the endpoint adds exact volume `3160957957586005864410946369933399692295961450120267/3000000000000000000000000000000000000000000000000000` ≈ `1.0536526525286687`, increasing total volume by about `6.8417371766×`. Exact first-moment increments are:
- `ΔM_x=14982912462680352113710350190926700954478108201234179308779688950021/48000000000000000000000000000000000000000000000000000000000000000000` ≈ `0.31214400963917399`
- `ΔM_y=-2032934269178305956236143130004132409963622062525015902581007338352599/2400000000000000000000000000000000000000000000000000000000000000000000` ≈ `-0.84705594549096086`
- `ΔM_z=-411538737634972744103289076159111576712209921632959586026091229012471/2400000000000000000000000000000000000000000000000000000000000000000000` ≈ `-0.17147447401457197`
All three components are nonzero. The own centroid moves from approximately `(-0.00827555824,-0.02858154472,-0.02281500443)` to `(0.25173954686,-0.69059804650,-0.14229078806)`. Active new rows `28–38,40` span `y≈-2.30…-2.72`, so this is genuine body-scale transport, not a shallow local cap. Every accepted search state was re-integrated and scored at its own centroid. The topology-changing stage did not symbolically eliminate the moment equations; the exact endpoint does close them identically after exact own-centering, and the complete own-centroid audit rejects it.

## Topology/circuit path

Seventeen rows `25–41` were introduced. The run crossed real deactivation/transfer cells with classes `(3,2,3)`, `(4,2,4)`, `(5,2,5)`, `(2,3,3)`, and `(2,2,2)`. A 29-active-row cell first appeared at iteration 78; fixed-lattice own-centroid sequential linear polishing reached score `-1.45528057367e-4`, where the trust radius collapsed and the linearized max–min optimum remained negative.

Four smallest immediate determinant walls were crossed independently: row 40 through plane `(8,9,33)`; row 38 through `(4,37,40)`; row 31 through `(14,30,33)`; row 35 through `(33,34,36)`. All 16 sign orthants were materialized 20% beyond their walls and fully re-integrated. Ten cells were `(2,2,2)` and six were `(2,3,3)`; none was `(1,1,0)`. Stable equilibrium transfers between `[8,40,9]` and `[8,33,9]`; saddles transfer between `(4,38)/(4,37)` and `(14,31)/(14,30)`; the fourth wall opens the `34/35` unstable relay. This is exhaustive for those four local walls, not a global exclusion of all 42-row designs.

## Independent reconstruction, OBJ/STL, and reproducibility

A separate SciPy-Qhull implementation with an independent interior-reference tetrahedral mass formula and separately coded cone audit reproduces `(29,67,40)`, volume `1.2340189751961848`, centroid `(0.2517395468588277,-0.6905980464951867,-0.1422907880625304)`, and exactly the same `(2,2,2)` feature set. The OBJ has 29 vertices/40 maximal faces; its triangulation and the 54-triangle STL are identical and watertight.

- Complete bundle (`skew_corridor_M42_bundle.zip`) — SHA-256 `7d5f92709664283edc284ad723f203f5a0f6934979f44ed271008466e5e43031`
- Exact rational generator/verifier (`skew_corridor_M42_exact.py`)
- Independent verifier (`skew_corridor_M42_independent.py`)
- 42 exact inputs (`skew_corridor_M42_input.csv`)
- Exact own-centred rational rows (`skew_corridor_M42_centered_rational.csv`)
- Complete all-feature audit (`skew_corridor_M42_audit.json`)
- All 16 immediate circuit cells (`skew_corridor_M42_circuit_cells.json`)
- OBJ (`skew_corridor_M42.obj`)
- STL (`skew_corridor_M42.stl`)
- Independent report (`skew_corridor_M42_independent_report.json`)
- Full checksums (`skew_corridor_M42_FULL_SHA256SUMS.txt`)

Reproduce with `python skew_corridor_M42_exact.py --outdir .`, `python skew_corridor_M42_independent.py`, and `python skew_corridor_M42_circuit_cells.py`.

## Sharp next architecture

The 42-input ceiling has solved the scale problem and removed the inherited pair, but the residual block is split across two distant sectors. A serial cap, one diagonal flip, determinant-one metric, or one-sided Y is redundant. The smallest justified continuation is a 46–50-input transverse communicating bridge: one branch must span stable circuit `(8,9,33,40)` and the `34/35` relay; another must span both saddle quadrilaterals `(4,37,38,40)` and `(14,30,31,33)`; two transverse links must make the branches communicate before transfer; rows `31,34,35,38,40` and possibly anchors `33,37` must be allowed to deactivate together; and three corridor coordinates should be dependent variables of the exact moment map while the four determinant walls are crossed. Require all new rows extreme and normalized inactive separation `>10^-5` before exactification.

That continuation exceeds the assigned 42-input budget. Within the completed finite search, M42-SLP is the strongest reconstructible post-corridor body and a useful exact frontier, but it is definitively not a homogeneous polyhedral Gömböc.
