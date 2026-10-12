# figure-0073

AI research report · 2026-08-26 UTC

---

# Skew-prismatoid/generalized-antiprism direction — complete handoff

## Determination

**No strict homogeneous polyhedral Gömböc was found.** I kept the journal’s acceptance gate: the body’s own exact uniform-volume centroid, actual maximal faces and true edges, exhaustive full-cone equilibrium classification, strict raw incidence, and a finite expanded object. :contentReference[oaicite:0]{index=0}

The journal had proposed this family but recorded that the previous skew-prismatoid launches failed before doing mathematical work. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2} This continuation actually searched it and produced an exact, independently reconstructible fallback plus a sharply localized rejected cancellation wall.

The strongest **open, exact, fully materialized own-centroid** body is a nonhomothetic two-cap skew prismatoid with `(V,E,F,C)=(20,40,22,80)` and strict class `(S,U,H)=(2,1,1)`. It is not a Gömböc. Its sole unwanted block is one stable face paired with one saddle edge.

## Search performed

The archived counter contains **67,994** complete shape/equilibrium evaluations, excluding uncounted diagnostics. I searched two independently translated/rotated/scaled asymmetric cap polygons with unequal vertex counts; one-, two-, and three-rail additions; deep and above-cap apex additions; fixed-cell full-coordinate optimization; determinant-one metric moves; exact one-face moment closures; and real circuit crossings with vertex deactivation. Generic `(m,n,r)=(4,5,2),(5,7,2),(8,3,2),(5,5,3)` searches ended at `(3,3,4),(2,2,2),(5,3,6),(4,2,4)` respectively. These are empirical outcomes, not a theorem excluding the whole architecture.

## Exact rational fallback

`P=conv(A∪B)`, with 17 vertices in `z=0` and an asymmetric triangle in the parallel plane `z=-0.09833908401260175`. Each decimal below is literal, hence an exact rational with denominator a power of ten.

### Complete V-representation
```text
00 (0.372333917289, -1.005665362556136, 0.0)
01 (0.689483660656, -0.894437806138, 0.0)
02 (1.053323, -0.607976, 0.0)
03 (1.27881, -0.225176, 0.0)
04 (1.366003, 0.241176, 0.0)
05 (1.282433, 0.740573, 0.0)
06 (1.011618999445274, 1.195088491479161, 0.0)
07 (0.562050908658201, 1.5888114583459, 0.0)
08 (-0.006320764093524, 1.830193641967598, 0.0)
09 (-0.575498646057959, 1.588778264086922, 0.0)
10 (-1.007169675893245, 1.210669575104478, 0.0)
11 (-1.282433, 0.740573, 0.0)
12 (-1.365243, 0.241176, 0.0)
13 (-1.27881, -0.225176, 0.0)
14 (-1.053323, -0.607976, 0.0)
15 (-0.738646665159, -0.876603364118, 0.0)
16 (-0.414887042084, -1.000003075674, 0.0)
17 (0.10119984230859137, -0.9943773701016063, -0.09833908401260175)
18 (0.20843076357876725, -0.9510423673722775, -0.09833908401260175)
19 (-0.23870741432314818, -1.0268755433313645, -0.09833908401260175)
```

### Exact mass certificate

Fan-triangulate every oriented maximal face and join its 36 boundary triangles to the coordinate origin. For each oriented triangle `(a,b,c)`, put `D=det(a,b,c)`. The standalone verifier evaluates exactly

`6V=ΣD`,  `centroid=[ΣD(a+b+c)]/[4ΣD]`.

- `6V=1284264598897223875860702210276520230780801814737/1000000000000000000000000000000000000000000000000`
- `V=428088199632407958620234070092173410260267271579/2000000000000000000000000000000000000000000000000` (`≈0.21404409981620398`)
- `c_x=-2173194093337544785825578568202468188890582730297/435318473759172103792717450472158800000000000000000` (`≈-0.00499219358776812275839058813430`)
- `c_y=-2335704599543286344069555002244415041628619215499/65297771063875815568907617570823820000000000000000` (`≈-0.0357700509755293969386216144416`)
- `c_z=-14730986250148071388124118832404572360032283821/544148092198965129740896813090198500000000000000` (`≈-0.0270716491729640342065653845145`)

Translating every vertex by `-c` gives an exact centroid-zero representation if desired.

### Complete maximal-face cycles
```text
F00 (19,8,18)
F01 (11,19,12)
F02 (10,19,11)
F03 (8,19,9)
F04 (9,19,10)
F05 (0,19,17)
F06 (19,18,17)
F07 (12,19,13)
F08 (0,16,19)
F09 (15,19,16)
F10 (18,5,4)
F11 (18,6,5)
F12 (18,8,7)
F13 (18,7,6)
F14 (18,4,3)
F15 (18,3,2)
F16 (18,2,1)
F17 (17,1,0)
F18 (1,17,18)
F19 (14,19,15)
F20 (13,19,14)
F21 (7,8,9,10,11,12,13,14,15,16,0,1,2,3,4,5,6)
```

### Complete true-edge incidence
```text
E00 (0,1):F17,F21
E01 (0,16):F08,F21
E02 (0,17):F05,F17
E03 (0,19):F05,F08
E04 (1,2):F16,F21
E05 (1,17):F17,F18
E06 (1,18):F16,F18
E07 (2,3):F15,F21
E08 (2,18):F15,F16
E09 (3,4):F14,F21
E10 (3,18):F14,F15
E11 (4,5):F10,F21
E12 (4,18):F10,F14
E13 (5,6):F11,F21
E14 (5,18):F10,F11
E15 (6,7):F13,F21
E16 (6,18):F11,F13
E17 (7,8):F12,F21
E18 (7,18):F12,F13
E19 (8,9):F03,F21
E20 (8,18):F00,F12
E21 (8,19):F00,F03
E22 (9,10):F04,F21
E23 (9,19):F03,F04
E24 (10,11):F02,F21
E25 (10,19):F02,F04
E26 (11,12):F01,F21
E27 (11,19):F01,F02
E28 (12,13):F07,F21
E29 (12,19):F01,F07
E30 (13,14):F20,F21
E31 (13,19):F07,F20
E32 (14,15):F19,F21
E33 (14,19):F19,F20
E34 (15,16):F09,F21
E35 (15,19):F09,F19
E36 (16,19):F08,F09
E37 (17,18):F06,F18
E38 (17,19):F05,F06
E39 (18,19):F00,F06
```

The independent exact reconstruction enumerates all `C(20,3)=1140` triples, recovers exactly these 22 maximal supporting planes, then exactly these 40 true edges from intersections of maximal faces. The 17-gon is one maximal face; triangulation diagonals are not counted as edges.

## Exhaustive equilibrium classification at the exact own centroid

Tests used: (i) a face is stable exactly when the perpendicular foot of `c` lies strictly inside its entire maximal polygon; (ii) a vertex `v_i` is unstable exactly when `-(v_i-c)·(v_j-v_i)>0` for every true neighbor; (iii) an edge is saddle exactly when its perpendicular projection parameter is in `(0,1)` and the radial-normal plane through the edge strictly supports **all** other vertices. Thus the edge test is the complete normal cone, not an incident-facet proxy. Every predicate numerator is stored as an exact `Fraction` in the verification transcript.

- Faces: `F00` and `F21` are stable; every other maximal face is nonstable. Stable margins are `+0.142450017072598761…` and `+0.967156279665658861…`; closest negative face is `F12` at `-0.141599667466586182…`.
- Vertices: only `V08` is unstable; every other vertex is nonunstable. Its margin is `+0.389779192491295887…`; closest negative vertex is `V05` at `-0.00528845788919712559…`.
- Edges: only `E03=(0,19)` is saddle; every other true edge is nonsaddle. It has projection `t=0.554515921708100400…` and full-cone margin `+0.00667567205879121919…`; closest negative edge is `E35=(15,19)` at `-0.00740977006902806285…`.
- Therefore `(S,U,H)=(2,1,1)`, with target stable cap `F21`, target maximum `V08`, and the live unwanted pair `F00=(19,8,18)` / `E03=(0,19)`.
- Minimum positive equilibrium margin over all four equilibria: `0.00667567205879121919247493902503`. Closest negative nonequilibrium margin over every remaining feature: `-0.00528845788919712559314321167220`.
- Minimum inactive Euclidean face/vertex separation: `0.0008771756923311681591810987737206122933249146222792462416772232183896285137372415515919572320482270150`, attained by `F00` versus `V17`. Exact raw numerator `138228770328195595313080546122642634214381949/125000000000000000000000000000000000000000000000`; corresponding normal square `254286713701827812740674260940736855428194320829444580262628277397/160000000000000000000000000000000000000000000000000000000000000000`.

This class is open. A directed outward interval audit passes for architecture-preserving radius `ρ=1/5000`: every `x,y` coordinate varies independently by `±ρ`, the upper plane remains `z=0`, and the three lower vertices share one lower-plane `z` varying by `±ρ`. Throughout the box the complete incidence and all equilibrium/non-equilibrium witnesses retain sign. This is a robustness radius for `(2,1,1)`, not for a Gömböc.

## Rejected closest cancellation wall

The two-rail continuation reached a materialized 22-vertex hull with `(V,E,F,C)=(22,46,26,92)`, volume `0.17967022821058057`, own centroid `(-0.0106445328143388,-0.0276594516546822,-0.0227430348776385)`, and nominal `(2,1,1)`. It is decisively rejected:

- unwanted stable face `(20,8,18)` `+5.3307833793428345e-11`, neighboring `(19,8,20)` `-4.5127420307487404e-11`;
- unwanted saddle `(0,17)` `+4.878241408305068e-11`, neighboring `(8,20)` `-3.5680609339046535e-10`;
- minimum raw inactive slack `1.3088119477089322e-10`;
- four independent circuit slacks `4.4744127905285e-11`, `5.457576407628696e-11`, `5.705477372835444e-11`, `6.468146383307983e-11`;
- 3,500 perturbations at scales `10^-11…10^-9` found no open target; best hard score `-1.1450594242381669e-11`.

The four circuits are `(019|21)`, `(170|21)`, `(198|18)`, `(208|19)`, where `face|opposite vertex` is shown. Complete wall coordinates and audit are included in the archive (`wall_vertices.csv`, `wall_audit.json`). This is a transfer wall, not a result.

## Topology changes crossed

A first rail changed `(20,40,22)` to `(21,43,24)` and transferred the pair. A second rail changed it to `(22,46,26)` and crossed/approached the four circuits above. Adjacent realized classes included `(2,1,1),(3,1,2),(4,1,3),(2,2,2),(3,2,3)`. Third/fourth and Y-rail moves allowed obsolete vertices to become interior but bifurcated the pair to `(3,1,2)` instead of cancelling it. Fixed-cell polishing, single flips, determinant-one metrics, and exact one-face centroid closures all transferred the block or violated another support inequality.

Diagnostic auxiliary-center searches do contain robust `(1,1,0)` chambers for this geometry, but those centers lie near the minimum-`y` support and far from the uniform centroid, so they were rejected. This is evidence—not a proof—that successful geometry must move both the stable-side and saddle-side strips while transporting volume moments macroscopically.

## Next finite family

Enumerate a **24–26 input-vertex bifurcated Y-strip**: retain the 17 upper and 3 lower cap vertices; add two rails across stable circuit `{8,18,19,20}`, two rails across lower saddle circuits `{0,17,19,21}` and `{0,1,17,21}`, and optionally 0–2 remote mechanically negative moment-control vertices. Permit vertices `17–21` to deactivate. In every circuit cell, solve the three exact tetrahedral volume-moment equations as hard constraints before mechanical scoring. Enumerate all signs of the four known circuits and immediate descendants; require raw inactive slack `>10^-5` and prospective target margin `>10^-6` before rational/interval exactification. Expected complexity remains approximately below `C=120`. This is the smallest finite family that attacks both observed transfer basins simultaneously rather than repeating a one-sided rail.

## Artifacts and independent checks

- [Complete archive](sandbox:/mnt/data/skew_prismatoid_result.zip), SHA-256 `48b01fe872e3e2fd93eab10ad000d847de7893dae370378bf521d6c09c8bfd85`.
- [Exact standalone Fraction/interval verifier](sandbox:/mnt/data/skew_prismatoid_result/verify_fraction.py), SHA-256 `61d1059d0389bd74c958e291303e8e492a9ed5c3cf3bb11a3bcb8bd8e905db79`.
- [Complete predicate transcript](sandbox:/mnt/data/skew_prismatoid_result/verification.json), SHA-256 `52af822adeaab9cb37144aba1a69584846da16077f45b6fe9b0fd3f687b3cd1a`.
- [OBJ](sandbox:/mnt/data/skew_prismatoid_result/body.obj), SHA-256 `2c78b4171c96221da7724d08364724ab101129d31ac77d742d0cc689741f5671`; [STL](sandbox:/mnt/data/skew_prismatoid_result/body.stl), SHA-256 `498976819982bc8e3c64e14dc64c993cd8a6ccb576ca13ddb514a49ff8cd7fe1`.

`python verify_fraction.py` reparses the coordinates as exact rationals, reconstructs incidence, recomputes exact volume/first moments, audits every face/vertex/edge, and runs the interval box. Independent Trimesh loading of both OBJ and STL yields 20 welded vertices, 36 triangles, watertightness, consistent winding, Euler 2, volume `0.21404409981620395`, and matching center of mass.
