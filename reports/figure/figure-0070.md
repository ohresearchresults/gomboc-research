# figure-0070

AI research report · 2026-08-26 UTC

---

# Bilateral P2 handoff — no certified winner

## Outcome

I did **not** find a certified own-centroid `(1,1,0)` polyhedron. The target 17-gonal base and unstable vertex 8 survive every retained checkpoint, but every connected bilateral continuation either remains in `(2,1,1)`, enters a genuine `(3,1,2)`/`(4,1,3)` transfer cell, or approaches a numerically degenerate support circuit without opening a target chamber. This respects the journal's requirement that any accepted object be checked with the body's true uniform-volume centroid and complete feature cones, rather than an origin surrogate.

The starting C104 body and its residual witnesses were independently reproduced from the journal's 26 rows. The new work goes beyond the journal's rejected one-sided rail by splitting the central link, adding controls on both incident saddle strips and both top/bottom sides, then performing connected polar support cuts and two-sided dual caps. The journal correctly anticipated that a stable-only rail merely splits the pair.

## Reusable artifact

The complete bundle is p2_bilateral_patch_bundle.zip, SHA-256 `621d86ae900665a0333a222716f974227965537db0426009205dbf3a0f707192`. It includes all coordinates, strict audits, maximal-face cycles, true edges, OBJ/STL meshes, the complete topology path, polar rows, deterministic R160 generator, and a standalone verifier.

Key files:

- R160 coordinates (`R160_bilateral_cut_centered.csv`), audit (`R160_bilateral_cut_centered.audit.json`), combinatorics (`R160_bilateral_cut_centered.combinatorics.txt`), OBJ (`R160_bilateral_cut_centered.obj`), STL (`R160_bilateral_cut_centered.stl`)
- standalone verifier (`independent_verify.py`), deterministic generator (`R160_generator.py`), cut parameters (`R160_cut_parameters.json`)
- complete topology path (`TOPOLOGY_PATH.md`), machine-readable path (`topology_path.json`), continuation samples (`cut_continuation.json`), Jacobian (`cut_jacobian.json`)
- D198 multi-rail wall coordinates (`D198_multirail_wall_centered.csv`), strict audit (`D198_multirail_wall_centered.audit.json`), polar support rows (`D198_polar_support_rows.csv`)

## Strongest robust open bilateral body: R160

`R160_bilateral_cut_centered.csv` is the strongest checkpoint with a genuine incidence reserve. It is the R122 connected bilateral V-patch intersected with two simultaneously parameterized polar cuts; the first new support is extreme and the second is redundant, a fact recorded rather than hidden.

- strict realized hull: `(V,E,F,C)=(45,80,37,160)`
- true uniform volume: `0.022044439064009366`
- integrated own centroid after recentering: `(-7.39899896895e-17,-4.45717042725e-18,3.80936777491e-19)`
- independent maximal-face-fan centroid difference: `2.75846992524e-14`
- centered first-moment norm: `1.63404619137e-18`
- triangle-fan/face-fan volume difference: `1.09287578987e-15`
- class: `(S,U,H)=(2,1,1)`
- target base `[0..16]`: margin `+0.9784897533317164`
- unique unstable vertex `8`: margin `+0.38759568582257375`
- extra stable triangle `[8,17,31]`: margin `+1.9248721008547856e-7`
- opposite top face `[17,25,31]`: margin `-2.1312471675079704e-8`
- saddle edge `[19,20]`: margin/coefficient `+2.6902466726732254e-7`, `t=0.9237805205946193`, coefficients `[1.0118772596223768,2.6902466726732254e-7]`
- opposite lower face `[18,19,20]`: margin `-6.358802746057471e-8`
- competing edge `[18,20]`: margin `-1.1644072901916375e-5`
- closest unwanted vertex: margin `-3.551437837498937e-4`
- minimum inactive support slack: `9.873017514649973e-9`
- maximum incident-plane residual: `7.605027718682322e-15`

The support slack is about 9,873 times the verifier's `1e-12` adjacent-plane tolerance, so R160 is a real open `(2,1,1)` cell. It is not a near-merged false target. The journal's warning that a `2e-7*scale` incidence threshold can corrupt maximal faces is directly relevant here.

## Strongest fully explicit multi-rail wall: D198, rejected as a certificate

The last construction adds active caps on both sides of the lower saddle dual edge, an active top cap, and a second cap on the transferred top edge. At strict adjacent-plane tolerance `1e-12`, its actual topology is `(V,E,F,C)=(58,99,43,198)`, not C196:

- volume `0.022044439064010792`
- centered first-moment norm `1.73237552923e-18`
- class `(2,1,1)`
- base margin `+0.9784897533317002`; vertex 8 margin `+0.38759568582260695`
- extra stable pentagon `[8,17,33,36,41]`: `+1.3443865220939405e-9`
- three closest opposite faces: `[36,41,42] -7.788412470162788e-11`, `[34,36,40,42,43,44] -1.3156916859221238e-9`, `[33,34,36] -2.768745951010586e-8`
- saddle `[22,23]`: `+1.1946635736074436e-7`, `t=0.9848368346736599`, coefficients `[1.0118773396091612,1.1946635736074436e-7]`
- lower opposite face `[18,19,22,23]`: `-5.4322254069114305e-8`; competing edge `[18,23] -9.947332063368332e-6`
- minimum inactive support slack only `1.9539925233402755e-14`, versus incident residual `9.547918011776346e-15`

Thus D198 is the closest materialized bilateral wall but has no perturbation certificate. At plane tolerance `2e-10` one inactive incidence is falsely merged, yielding the misleading `(58,98,42,C196)` count. The strict C198 reconstruction is included to make that failure reproducible.

## Complete topology path and actual classes

All rows were independently rebuilt at `1e-12` using the integrated centroid. `extra S` and `H` list the largest positive non-target stable and saddle margins.

|stage|V,E,F,C|class `(S,U,H)`|extra S|H|inactive slack|
|---|---:|---:|---:|---:|---:|
|S0|24,52,30,104|(2,1,1)|7.75297e-06|7.75298e-06|1.54381e-08|
|S1|26,58,34,116|(2,1,1)|3.63103e-06|4.81519e-06|1.54381e-08|
|S2|28,64,38,128|(2,2,2)|3.63104e-06|4.00031e-07|1.19143e-08|
|S3|27,61,36,122|(2,1,1)|1.32586e-07|1.32571e-07|8.9014e-12|
|S4|27,61,36,122|(2,1,1)|1.78744e-06|4.11286e-06|1.54381e-08|
|S5|30,70,42,140|(2,1,1)|3.26905e-07|4.60402e-07|1.67002e-11|
|S6|30,70,42,140|(3,1,2)|2.11697e-07|2.12171e-07|9.37106e-11|
|S7|28,64,38,128|(2,2,2)|2.24275e-10|2.22243e-10|4.93488e-12|
|R122|27,61,36,122|(2,1,1)|3.11033e-07|3.98172e-07|9.87301e-09|
|R160|45,80,37,160|(2,1,1)|1.92487e-07|2.69025e-07|9.87302e-09|
|T160|45,80,37,160|(3,1,2)|1.76979e-07|1.83151e-07|9.87302e-09|
|D186|55,93,40,186|(2,1,1)|3.06392e-08|1.44981e-07|1.29626e-12|
|D198|58,99,43,198|(2,1,1)|1.34439e-09|1.19466e-07|1.95399e-14|

The stages are: C104 seed; stable-side rail; initial two-sided saddle split; balanced bilateral wall; central vertex/star split; full top/bottom V-patch; open transfer cell; four-feature wall; robust R122 subset; robust R160 support-cut continuation; T160 transfer cell; D186 first dual caps; D198 second top rail plus reoptimized lower cap. Each coordinate file and every witness/opposite wall is in `topology_path.json`.

For R122, the realized connected face path from saddle to stable is

`[19,22,24] -> [19,20,22] -> [11,19,20] -> [10,11,19] -> [10,19,21] -> [19,21,23] -> [21,23,26] -> [23,25,26] -> [21,25,26]`.

The opposite branch to the base is

`[20,22,24] -> [17,20,24] -> [16,17,20] -> [0,16,17] -> base`.

This is a connected replacement of the central link and both saddle-side strips, not an isolated cap.

## Why the pair transfers instead of cancelling

The cut continuation `x(s)=x_open+s(x_transfer-x_open)` gives a reproducible sequence. The IDs in this paragraph are the continuation's native HalfspaceIntersection ordering used in `cut_continuation.json`; at T160 they map to relabeled lower face `[18,19,20]` and saddles `[18,20]`, `[19,20]`. It remains `(2,1,1)` through `s=0.975`. By `s=0.99`, native face `[9,10,11]` has become stable while the old saddle `[10,11]` remains and a new saddle `[9,11]` is born, so the open cell is `(3,1,2)`. By `s=1.08`, the top opposite face also crosses and edge `[8,23]` becomes a saddle, giving `(4,1,3)`. At larger `s` the identifiers change again; at `s=2.6` the class returns to `(2,1,1)`, but the surviving stable and saddle are native `[8,16,23]` and `[9,13]`, not cancellations of the originals.

At T160, tracking `[top stable, lower face, saddle 1, saddle 2]` against `[theta1,phi1,t1,theta2,phi2,t2]` gives

`values = [1.76978959363e-7, 1.00018497936e-9, 1.83151252187e-7, 1.83151259607e-7]`

and central-difference Jacobian

[-7.53381401564e-05, -0.000120325696534, -2.38988762229e-05, 0, 0, 0]
[-2.30469608281e-06, -2.38233128303e-06, -2.67456116121e-06, 0, 0, 0]
[-0.00042203045895, -0.000436247166503, -0.000489756082925, 0, 0, 0]
[3.06311376509e-06, 3.16739348214e-06, 3.55486645102e-06, 0, 0, 0]

The second cut is locally redundant, hence three zero columns. More importantly, the two lower saddle rows respond with opposite signs to the active coordinates, while the lower-face row is almost flat. A direction that suppresses one active saddle moves the equilibrium onto the adjacent edge/face before both can become negative. The top caps show the same phenomenon: each cap makes the old stable support noncritical only by making a nearly coplanar new support critical, collapsing inactive separation from `9.87e-9` to `1.30e-12` and then `1.95e-14`. Geometrically, the patch builds two serial transfer rails; it never opens a bridge in which the maximum and saddle meet and annihilate.

## Complete R160 finite reconstruction

The following 17-digit coordinates are already translated to their true uniform centroid. Rows `0..16` are the stable base and row `8` is the unique unstable vertex.

### Coordinates

```text
0: (0.37285714119637836,-0.98119693421499332,0.0027922684597812735)
1: (0.69000688456337844,-0.86996937779685324,0.0027922684597812735)
2: (1.0538462239073882,-0.58350757165885325,0.0027922684597812735)
3: (1.2793332239073782,-0.20070757165885328,0.0027922684597812735)
4: (1.3665262239073883,0.26564442834114671,0.0027922684597812735)
5: (1.2829562239073884,0.76504142834114675,0.0027922684597812735)
6: (1.0121422233526582,1.2195569198203067,0.0027922684597812735)
7: (0.56257413256557842,1.6132798866870466,0.0027922684597812735)
8: (-0.0057975401861416137,1.8546620703087466,0.0027922684597812735)
9: (-0.57497542215058162,1.6132466924280666,0.0027922684597812735)
10: (-1.0066464519858518,1.2351380034456265,0.0027922684597812735)
11: (-1.2819097760926217,0.76504142834114675,0.0027922684597812735)
12: (-1.3647197760926217,0.26564442834114671,0.0027922684597812735)
13: (-1.2782867760926118,-0.20070757165885328,0.0027922684597812735)
14: (-1.0527997760926218,-0.58350757165885325,0.0027922684597812735)
15: (-0.73812344125162155,-0.85213493577685329,0.0027922684597812735)
16: (-0.4143638181766216,-0.97553464733285322,0.0027922684597812735)
17: (-0.15994669345197163,1.0483956829545067,-0.00054578409369872662)
18: (-0.13463771777962164,-1.0075187037686033,-0.0072766726349587259)
19: (-0.068579969343051606,-1.0099898559888534,-0.0076134805860187263)
20: (-0.035331051612621608,-1.0112336845777934,-0.0077802886403287265)
21: (-0.026383556471481617,-1.0113790227830133,-0.0079890773734587264)
22: (-0.024968210079011614,-1.0114737772840734,-0.0079608682726287263)
23: (-0.022633393616461616,-1.0116275975349434,-0.0079146589539787274)
24: (-0.022385571216971614,-1.0116438561638035,-0.0079097631116087277)
25: (-0.019440367902841614,0.0078489440653467159,-0.0043245453020687259)
26: (-0.0089781657417516147,-1.0122241951582633,-0.0058070358875787261)
27: (-0.0010537754317016142,-1.0079857959514333,-0.0081495191424287277)
28: (9.1495641638385819e-05,-1.0078494115259533,-0.0081545459984387267)
29: (0.00067652277176838578,-1.0124155465470834,-0.007551074160308726)
30: (0.0017605036262583859,-1.0076708016045335,-0.0081592382732987266)
31: (0.0023795648758883859,-0.015536865179373284,-0.0043811438821787264)
32: (0.0037352183557083857,-1.0075221745570935,-0.0081565934564687276)
33: (0.0040151550121983858,-1.0075015567807033,-0.008156159477998727)
34: (0.0041214910801783862,-1.0074938969697134,-0.0081559721413087278)
35: (0.005207764051198386,-1.0074176210656633,-0.0081538005212587264)
36: (0.0064521672653483856,-1.0073425851834734,-0.0081496990923787278)
37: (0.0078790805740483853,-1.0072732539557634,-0.0081428116555687276)
38: (0.0097483105437283848,-1.0072134319063735,-0.0081297365285187273)
39: (0.12555329035840837,-1.0126832018039633,-0.0061201157659887262)
40: (0.24349465818707838,-1.0013261088034833,-0.0062863927698187261)
41: (0.24824653380262837,-1.0012916659948135,-0.0062377753966287265)
42: (0.25092774157191838,-1.0089873907031834,-0.0052017388199787264)
43: (0.25503887334705838,-1.0015696144904234,-0.0061255091689587258)
44: (0.26322541791374837,-1.0036171010550334,-0.0057663253054987262)
```

### Maximal face cycles

Cycles are outward-oriented and use the coordinate indices above.

```text
F0: [0,16,26]
F1: [42,44,1,0]
F2: [26,39,42,0]
F3: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,0]
F4: [44,43,2,1]
F5: [43,41,3,2]
F6: [41,40,4,3]
F7: [40,38,4]
F8: [38,37,5,4]
F9: [5,37,36,6]
F10: [36,35,7,6]
F11: [7,31,8]
F12: [7,35,34,31]
F13: [8,17,9]
F14: [31,17,8]
F15: [9,17,10]
F16: [28,27,11,10]
F17: [10,17,30,28]
F18: [11,18,12]
F19: [11,27,21,18]
F20: [18,13,12]
F21: [13,18,14]
F22: [14,18,15]
F23: [18,16,15]
F24: [16,18,26]
F25: [17,31,25]
F26: [17,32,30]
F27: [17,25,33,32]
F28: [18,19,20]
F29: [20,26,18]
F30: [18,21,22,19]
F31: [19,22,23,20]
F32: [23,24,20]
F33: [20,24,29,26]
F34: [21,27,28,30,32,33,34,35,36,37,38,40,41,43,44,42,39,29,24,23,22]
F35: [31,34,33,25]
F36: [26,29,39]
```

### True edges

```text
E0: [0,1]
E1: [0,16]
E2: [0,26]
E3: [0,42]
E4: [1,2]
E5: [1,44]
E6: [2,3]
E7: [2,43]
E8: [3,4]
E9: [3,41]
E10: [4,5]
E11: [4,38]
E12: [4,40]
E13: [5,6]
E14: [5,37]
E15: [6,7]
E16: [6,36]
E17: [7,8]
E18: [7,31]
E19: [7,35]
E20: [8,9]
E21: [8,17]
E22: [8,31]
E23: [9,10]
E24: [9,17]
E25: [10,11]
E26: [10,17]
E27: [10,28]
E28: [11,12]
E29: [11,18]
E30: [11,27]
E31: [12,13]
E32: [12,18]
E33: [13,14]
E34: [13,18]
E35: [14,15]
E36: [14,18]
E37: [15,16]
E38: [15,18]
E39: [16,18]
E40: [16,26]
E41: [17,25]
E42: [17,30]
E43: [17,31]
E44: [17,32]
E45: [18,19]
E46: [18,20]
E47: [18,21]
E48: [18,26]
E49: [19,20]
E50: [19,22]
E51: [20,23]
E52: [20,24]
E53: [20,26]
E54: [21,22]
E55: [21,27]
E56: [22,23]
E57: [23,24]
E58: [24,29]
E59: [25,31]
E60: [25,33]
E61: [26,29]
E62: [26,39]
E63: [27,28]
E64: [28,30]
E65: [29,39]
E66: [30,32]
E67: [31,34]
E68: [32,33]
E69: [33,34]
E70: [34,35]
E71: [35,36]
E72: [36,37]
E73: [37,38]
E74: [38,40]
E75: [39,42]
E76: [40,41]
E77: [41,43]
E78: [42,44]
E79: [43,44]
```

These lists reconstruct the OBJ/STL exactly. The full audit JSON also contains every face projection margin, every vertex tangent-cone margin, every edge line parameter and normal-cone coefficient, inactive slacks, and both centroid integrations.

## Independent verification

From the extracted bundle:

```bash
python independent_verify.py R160_bilateral_cut_centered.csv --plane-tol 1e-12 --json check.json
python R160_generator.py --out regenerated.csv
python independent_verify.py regenerated.csv --plane-tol 1e-12
```

`R160_generator.py` reproduces the coordinate set with Hausdorff error `1.12e-16`. `independent_verify.py` imports no search module: it groups only adjacent coplanar Qhull triangles, walks maximal-face boundary cycles, constructs true edges, integrates centroid by both triangulated-facet and maximal-face fans, and tests all complete face/edge/vertex cones.

## Uncertainty and useful continuation

No target perturbation radius exists because no target body was found. R160 is safely inside a non-target chamber; D198 is too incidence-degenerate to support any certificate. The next meaningful experiment is not another serial cap. In the polar, the entire residual dual basin follows the paths `14-13-16-23-19-17` and `14-13-16-23-20-37`. A continuation should allow rows `14,13,16,23,19,20,17,37` to become non-extreme together and replace them with one connected support complex, while explicitly constraining every inserted support to remain extreme and every inactive slack above about `1e-8`. Without that simultaneous deactivation constraint, optimization repeatedly rediscovers the transfer rails documented here.
