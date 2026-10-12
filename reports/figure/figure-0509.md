# figure-0509

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# RH08 — changed-geometry construction handoff

## Outcome

I did not reconstruct or certify a strict110 body. I did obtain two complementary, genuinely changed, nonsymmetric endpoints with **E = 141, C = 282**, at their own uniform volume centroids:

- **RH08_B1_Q2_G3:** V49/E141/F94, strict **(S,U,H) = (2,1,1)**, additional weak **000**. Its physical landscape has no finite positive H0 bar; its same-centre polar has exactly one.
- **RH08_H1_POLISH_G4:** V94/E141/F49, strict **(1,2,1)**, additional weak **000**. Its polar landscape has no finite positive H0 bar; its physical landscape has exactly one.

These use 95 of the entrance’s 203 edges of headroom and leave **108 true edges** below E249. Neither endpoint is a110, and neither is being promoted on the basis of root transport, an isolated edge crossing, or a small surrogate objective.

The principal constructive mechanism is a **nonplanar log-radius bridge followed by unrestricted vertex motion at the actual volume centroid**, followed by complete-bar-aware reconsolidation. A second mechanism constructs a **new uniformly filled H-body from the polar architecture**, releases all support vectors, recomputes its own physical mass, and restores a unique stable face. The second construction is not an illicit recentering of the first body’s diagnostic polar.

### Exact endpoint inventory

All rows below have additional weak census 000. Positive-bar counts exclude the one essential H0 component.

| Object | V/E/F | C | Strict S/U/H | Positive physical/polar bars | r/R, approximately |
|---|---:|---:|---:|---:|---:|
| C92 entrance, independently reindexed | 21/46/27 | 92 | 2/2/2 | 1/1 | 0.0368036928 |
| RH08_B1_Q2_G3 | 49/141/94 | 282 | 2/1/1 | 0/1 | 0.2678601245 |
| RH08_H1_POLISH_G4 | 94/141/49 | 282 | 1/2/1 | 1/0 | 0.2516166358 |
| RH08_B0_Q2_G4 | 55/159/106 | 318 | 2/1/1 | 0/1 | 0.0915964456 |
| RH08_H0_G4 | 100/150/52 | 300 | 1/2/1 | 1/0 | 0.0843620898 |
| RH08_B1_DESC_G3 | 49/141/94 | 282 | 31/1/30 | 0/30 | 0.2671403727 |

The last three constructions are retained deliberately. The planar bridge gives a different, thinner U1 architecture; its H continuation retires support constraints. The DESC body lowers the surviving dominant polar well substantially but creates many additional stable equilibria. It is a useful exact failure control, not a near-a110 certificate.

## Source authority and entrance

I read the entire supplied journal and all three source materials, including their recovery code. No unavailable historical archive item was used as an exact dependency. The entrance was reconstructed as the supplied **G6 COLUMN matrix applied to exact raw G3**, not raw G6. The source explicitly distinguishes the broken orthogonal symmetry of the affine image from the raw reflection construction.

The supplied-file SHA-256 identities were:

| File | SHA-256 |
|---|---|
| D2_V21_E46_THREE_EXACT_CONTROLS.md | f6c71beba0092d91227c851047168f1c7ddd04da7464266254e75404cc3820ad |
| D2_FINITE_REFLECTION_20260923_part1.md | 6b1e3848c40b1dccc00761625bcb9e9c0ad14f4d7d64ae7b6e3d03b85703ebce |
| D2_ENERGY_AND_SYMMETRY_BREAKING_EXACT_CONTROLS.md | e3238a15604499fb7783a6a90b9dedd9200780c9b2946bd6f7f8d1f6f5b2becb |
| research-journal(20260923-092756).md | 06fc5cad672f6aaa3c3059be205681ad857824b3e044745e181105e943b6382e |

The independent generic auditor recovered entrance strict222/weak000 and its supplied actual centroid. Its fresh lexicographic numbering is different from the source auditor’s numbering. The new entrance report is 34,729 bytes, SHA-256 **d15701ea43155e4b948e3c58fbea88bd312c0f85ebbc89d3200a3f32b7e64d0d**; that is a different report format, not a competing source identity.

The capsule’s `freeze.py` contains the complete raw-G3 reflection rows and integer column matrix, so entrance recovery has no external source dependency. The earlier interrupted generic V-auditor work was rebuilt and extended rather than treated as an inaccessible computed successor.

## Construction and finite experiments

### 1. Free geometry, not fixed affine transport

There were **21 completed optimizer runs**, with 10,762 reported accepted iterations and 17,383 reported function evaluations in total. `EXPERIMENTS.json` records every run’s parameters, dependency, observed termination, root counts, energies, and checkpoint receipt. All non-parent checkpoint inputs needed by these runs are included in the capsule. Numerical code, complete helpers, and replay commands are included.

The initial direct free-21-vertex joint descent greatly reduced both logarithmic persistence energies but proliferated roots: its retained floating scout had 12 physical and 13 polar roots. Asymmetric reconsolidation experiments also produced many small wells. These observations are finite numerical failures, not exclusions of changed geometry.

### 2. A prescribed escape forest with a three-dimensional bridge

The successful bridge uses 48 segments and 47 inserted nomination points. It joins the younger physical maximum to the elder maximum in the parent’s centroid frame. With endpoint unit directions a,b, angle theta, an orthonormal transverse pair e,f, and t=k/48, the nomination is:

```text
d(t) = normalize(cos(theta*t)*a
       + sin(theta*t)*(cos(2*pi*twist*t)*e + sin(2*pi*twist*t)*f))
r(t) = exp((1-t)*log(r0) + t*log(r1) + boost*sin(pi*t)^2)
p(t) = old_actual_centroid + r(t)*d(t)
```

The three finite seeds used twists 0,+1,-1 and boosts 0,0.05,0.05. This old centre is used only to nominate points. Every subsequent objective evaluation recomputes the new convex hull, uniform volume, first moment, physical centroid, physical landscape and same-centre polar landscape.

Each original non-root point receives a positive escape arrow selected from the parent; the retired root is connected along the inserted chain to the elder. All 68 nomination coordinates are then free. The forest is a soft numerical constraint during optimization, not an assumed certificate. Exact positive true-edge forests are constructed independently at promotion.

The +1 bridge reached numerical U1 in 188 iterations. After excess-polar-bar descent and 84 iterations of sign-aware reconsolidation, its independently rounded G3 hull had 49 actual vertices: the two original root nominations and all 47 bridge nominations. The other 19 nomination points are redundant in the final convex hull. Its geometry is not an affine image of the entrance: the f-vector changes from 21/46/27 to 49/141/94.

The reconsolidation correction that mattered was to exempt the global polar root and the peak of the largest complete polar bar, rather than blindly exempting the two largest-radius polar vertices. The latter need not represent two different basins. `polish.py` contains the complete implementation.

### 3. New physical H-bodies and unique stability

For the second architecture, the centred support-vector representation suggested by the first construction is used to nominate a **new physical intersection of halfspaces**. All support vectors are released. Its physical volume centroid is recomputed; its diagnostic polar is then formed about that new actual centre.

The initial own-filled polar of the twisted endpoint had, numerically, two physical roots and 38 polar roots. After free-H optimization and a 32-iteration sign polish, the G4 reconstruction became strict121/weak000 with 49 maximal faces and 141 true edges.

This H representation is important. Independently rounding its 94 physical vertices can destroy coplanar maximal faces and change both mass and edge count. The promoted object is the exact intersection of the 49 supplied rational halfspaces, not a triangulated or independently rounded V approximation.

## Principal exact construction: P49

The following is the complete list of actual vertices of RH08_B1_Q2_G3, in the auditor’s lexicographic order. Divide every row by 1000 and take the convex hull. The capsule retains all 68 original nomination points for provenance and numerical continuation; the 49-row list below defines exactly the same body. Its smaller input representation consequently has different input-file bytes from the quoted full-nomination receipt.

```python
P49 = [
[-5349,-4181,-2657],[-5335,-3957,-3045],[-5320,-4491,-2030],
[-5248,-4771,-1284],[-5195,-2972,-4660],[-5158,-4951,-660],
[-5025,-5087,-3],[-4842,-5189,619],[-4651,-5245,1158],
[-4426,-5283,1653],[-4221,-5231,2196],[-3957,-5132,2779],
[-3628,-4986,3372],[-3287,-4698,4017],[-2832,-4319,4672],
[-2359,-3800,5287],[-1853,-3147,5831],[-1308,-2413,6258],
[-820,-1553,6555],[-345,-646,6698],[75,281,6684],
[441,1216,6513],[716,2140,6187],[738,5871,1706],
[829,5591,2655],[871,5954,744],[903,5158,3543],
[915,3016,5720],[924,5889,-205],[954,5672,-1117],
[1028,4540,4393],[1044,3820,5115],[1286,5295,-1845],
[1310,4849,-2586],[1756,3730,-3551],[1833,4341,-2936],
[2113,3135,-3787],[2489,2597,-3860],[2591,1927,-4061],
[2840,1331,-4039],[2863,689,-4088],[3310,176,-3676],
[3728,-42,-3170],[4064,-3,-2674],[4193,1813,-122],
[4281,-101,-2258],[4486,67,-1781],[4592,1107,-369],
[4626,419,-1256]]
```

Its exact uniform volume is **897008511419/3000000000**. Its exact first moment is:

```text
(-13999398936907/600000000000,
  931594680411589/12000000000000,
  840414194943823/24000000000000)
```

Its actual centroid is:

```text
(-13999398936907/179401702283800,
  931594680411589/3588034045676000,
  840414194943823/7176068091352000)
```

The sufficient common centred multiplier used by this auditor has 53 bits, versus 127 for its entrance reconstruction. This is a low-arithmetic V endpoint, not merely a high-precision floating pin.

The strict unstable vertex is **4**. Stable faces are **4 and 86**, with cycles `[0,3,24]` and `[12,46,13]`. The unique saddle is on true edge **[4,40]**. All additional weak cases are absent.

### Complete remaining polar basin

The physical landscape has an exact positive escape forest to its sole root and **no finite positive H0 bar**. The polar has exactly one finite positive bar, from peak 86 to elder 4:

```text
birth = 147783168253173147098324708612158326402560000/
        981617983285926507364692735715683160786210129
death = 4050747330335648424017903577670976000000/
        80490221080802487894633124197862378961453
relative depth = 1 - death/birth = approximately 0.6657206359138741
```

Its complete strict-superlevel component, true-edge cut, and attaining path are:

```python
component = [36,40,43,45,49,54,55,58,59,60,61,62,63,64,65,66,67,68,69,
             70,71,72,73,75,77,78,79,80,81,82,83,84,85,86,87,88,89,
             90,91,92,93]
cut = [[7,66],[8,67],[9,49],[10,78],[11,92],[13,64],[14,62],[16,89],
       [18,58],[20,45],[21,36],[24,93],[25,70],[25,82],[26,90],[26,91],
       [27,54],[28,43],[28,88],[29,75],[29,87],[31,65],[31,86],[32,36],
       [32,69],[33,55],[33,59],[34,40],[35,63],[39,73],[41,84],[42,81],
       [46,80],[48,85],[50,77],[52,61],[53,72],[56,72],[76,83]]
path = [86,80,65,40,69,60,64,78,84,54,55,59,58,66,61,72,56,22,15,
        6,1,5,8,19,7,12,18,4]
```

The auditor verifies that every cut edge has weight at most the stated death, that the path bottleneck equals that death, and that **every chord crossing the component cut** also has weight at most that death. This is a 41-vertex basin with a 39-edge interface, not a two-vertex obstruction.

## Complementary exact H construction

RH08_H1_POLISH_G4 is the intersection of **all inequalities `dot(row,x) <= 10000`** for the following complete 49-row list:

```python
H49 = [
[-48845,-33348,-49408],[43441,15777,-4588],[47310,7015,-3830],
[47072,3332,-13262],[45351,1696,-19792],[43537,944,-24034],
[41211,-659,-28335],[38131,-801,-32851],[33887,-21,-37851],
[30045,4537,-41357],[28766,10738,-41651],[26752,16933,-41503],
[26104,23846,-39152],[21837,29120,-38872],[18927,35123,-36094],
[17573,40806,-31349],[14096,46283,-26295],[13132,50644,-19240],
[9255,54502,-11959],[10482,56312,-2888],[10170,56887,6412],
[10701,55771,15696],[10866,53115,25114],[12291,48575,34107],
[12523,42681,42435],[11942,35511,49834],[10646,27421,55924],
[8598,18647,60631],[5673,9474,63885],[1975,148,65618],
[-2442,-9063,65797],[-7486,-17837,64431],[-12819,-26026,61577],
[-18340,-33281,57398],[-23600,-39541,52124],[-28527,-44618,46080],
[-32927,-48465,39671],[-36604,-51230,33279],[-39639,-53066,27151],
[-42187,-54153,21346],[-44183,-54774,15861],[-46007,-54867,10507],
[-47625,-54603,4875],[-49153,-53834,-1309],[-50407,-52540,-7817],
[-51326,-50705,-14277],[-51930,-48057,-21523],[-51922,-45214,-27884],
[-51545,-42686,-32683]]
```

Its volume is approximately **0.0405672516522887**, and its actual centroid is approximately **(0.0017613342146528222, -0.0006045353829116593, -0.0004614387685244582)**. The complete exact volume, first moment and centroid are regenerated in its audit report. Its low-arithmetic support representation should not be confused with low-arithmetic mass: the auditor’s sufficient centred multiplier has **13,558 bits**.

The unique stable face is **5**, with cycle `[8,10,20,30,31,32,35,36,37,38,43,45,41]`. Strict unstable vertices are **0 and 82**. The unique saddle is on true edge **[37,38]**. Its polar has no finite positive bar. Its physical landscape has exactly one, from peak 82 to elder 0, with relative depth approximately **0.7322846516811148**, a 41-vertex strict-superlevel component and a 43-edge complete true-edge cut. The report contains the full rational birth/death, cut, attaining path and all-chord certificate.

## Verification scope and preserved failures

`exact.py` is a complete arbitrary-rational V/H auditor. For V input it exhausts supporting triples and constructs exact maximal planar facet hulls, removing redundant nominations and collinear polygon points. For H input it exhausts feasible triple intersections, proves boundedness by the exact polar hull, and retains exactly the supporting inequalities that define maximal facets. It checks global support, convex facet cycles, two-owner true edges, connectivity and Euler incidence.

Uniform volume and first moment are checked with **two tetrahedral origins** and independently by **three coordinate divergence identities**. The resulting actual centroid must give positive centred facet supports and positive centred tetrahedra. Stable feet are tested directly against all other facets and crosschecked against dual-neighbour inequalities. Unstable vertices are tested through true edges and independently against all other vertices. Every true-edge interior foot is tested in its two-normal cone, including coefficient-zero weak cases; endpoint weak vertices are also checked. The identity S+U-H=2 is only a consistency check after direct classification.

Both complete positive H0 landscapes are regenerated with exact chord minima, simultaneous equal-level merges, elder tie-breaking, strict-superlevel components, complete cuts, attaining paths, maximum spanning trees and all-pair chord domination checks. For P49 and the H49 construction, the two landscapes check 1,176 and 4,371 unordered pairs, in the appropriate order. This uses the complete-landscape framework recorded in the notebook, rather than a selected-edge proxy.

Every promoted construction has distinct exact vertex distance-multiset signatures for all its vertices. Any Euclidean self-isometry would have to preserve these signatures, hence fix every vertex and be the identity. Thus nonsymmetry is checked, not inferred from the optimizer’s appearance.

The standard-library Fraction and GMP backends produced byte-identical complete entrance reports. Tetrahedron and cube full-mechanics controls also passed. The large H reports were completed with the included exact GMP adapter; a separate complete Fraction rerun of those large reports was not completed. A second independently implemented full mechanics auditor has not been run on the new bodies. The certificates are endpoint certificates, not a certified continuous deformation or an exhaustive list of path bifurcations.

Important exact nonwinning controls:

- B0’s G3 rounding is strict255/weak000, while its G4 and G5 roundings are strict211/weak000. A floating U1 scout is not by itself a rounding certificate.
- H1_POLISH at G3 is strict222/weak000. Its extra polar bar has relative depth approximately **2.561085330351921e-7**. G4 and G5 are strict121/weak000. The small extra bar is genuinely positive, not an extra weak equilibrium or an ignorable numerical residue.
- B1_DESC at G3, G4 and G5 is strict(31,1,30)/weak000. At G3 its dominant polar bar has relative depth approximately **0.31087219451277714**, but there are **30** positive polar bars. Reducing the dominant well while proliferating other wells did not solve the problem.
- The finite deletion scout tested all 49 single actual-vertex deletions of P49 and accepted none under its recomputed numerical U1/S2 predicate. This is not a proof of deletion minimality, much less an exclusion of deletion followed by geometry compensation. `prune.py` and its exact input and ledger are retained.

## Most useful continuation

Use **P49/G3** as the low-arithmetic primary entrance, with its full remaining polar cut, rather than reverting to the fixed affine parent. The next geometrically different experiment is cut-aware insertion or redistribution on the surviving polar basin while compensating mass elsewhere and protecting the already exact physical escape forest. All support changes must be followed by a new physical volume/moment calculation and a complete two-landscape audit.

`bridge_budget.py` gives a concrete nomination calculation. At the old actual centre, a short log-radius arc for P49’s remaining polar roots needs 15 segments, or 14 interior nomination points, for positive consecutive radial arrows. For H1’s remaining physical roots it gives 19 segments, or 18 interior points. These are **old-centre nomination calculations only**: no filled successor or E bound has been proved for either insertion. In particular, a three-edges-per-insertion rule must not be transferred to the wrong primal/dual architecture. The actual resulting maximal hull must decide whether the 108-edge reserve suffices.

## Recovery capsule and receipts

The following capsule writes **29 files**, including complete source units, all 21 finite-experiment specifications, every non-parent numerical checkpoint needed as an experiment input, the material nonwinning pins, exact rounders, the complete auditor, and 14 observed report receipts including the entrance. It has no external research-library dependency.

Exact authoring environment: CPython **3.13.5**. Numerical replay: NumPy **2.3.5**, SciPy **1.17.0**, Torch **2.10.0+cpu**, single OMP/BLAS/MKL/Torch threads. There is no random seed to supply. Numerical trajectories may depend on the QHull/platform implementation; the exact pinned rational bodies do not. G3/G4/G5 rounding is exact ties-to-even rounding of the stored binary64 values multiplied by 10^g, not rounding of printed decimal coordinates.

For faster large-H exact arithmetic, `C92_GMP=1` selects the included ctypes adapter for GNU GMP **6.3.0**. Without that environment variable, the entire auditor uses standard-library Fraction.

After saving and running the capsule below as `recover_rh08.py`:

```sh
python recover_rh08.py
cd RH08_recovered
python -B -S freeze.py
python -B -S exact.py C92_PARENT.json
python -B -S exact.py RH08_B1_Q2_G3.json
C92_GMP=1 python -B -S exact.py RH08_H1_POLISH_G4.json
python -B -S checks.py
python -B -S bridge_budget.py
```

The other control inputs generated by `freeze.py` use the same `exact.py` command. `checks.py` validates the reports present in that directory; it does not silently claim that ungenerated reports were checked in that invocation. All 14 listed reports were generated and checked in the research run.

Expected principal markers and receipts:

```text
RH08_CAPSULE_EXTRACT_PASS 28
RH08_FREEZE_CAPSULE_PASS
C92_EXACT_FULL_AUDIT_PASS RH08_B1_Q2_G3 49 141 94 [2, 1, 1] [0, 0, 0]
C92_EXACT_FULL_AUDIT_PASS RH08_H1_POLISH_G4 94 141 49 [1, 2, 1] [0, 0, 0]
RH08_RECEIPTS_AND_SYMMETRY_PASS

RH08_B1_Q2_G3.json:
  3385 bytes
  10879d94d227c49665ddbdcbc7f0f4a8e8be57fadf72ba10429e0c49887477d9
RH08_B1_Q2_G3_audit.json:
  89755 bytes
  f8f470eefe4ff65758fbac34d4b5e7d67194849ff167a2e8c41b619e77c8d0e7
RH08_H1_POLISH_G4.json:
  2615 bytes
  6362a065e0ce0070ee11db33cc9977bf7263b32dbc78bbcd62f69697d739c62a
RH08_H1_POLISH_G4_audit.json:
  3793723 bytes
  a6fc9ff28faf87490be29021533ec2446a69b70ac43ecf6b6b333208792f54c5

Complete capsule archive:
  31684 bytes
  4766281bc5a6fc2649dbb6a72d57196df8982270a79e343525a9865043dbdeb9
```

The final capsule was extracted into a separate directory, its 28 manifest entries were hash-checked, and P49 was reconstructed and fully re-audited there with the quoted receipt. Convenience copies: capsule archive (`RH08_capsule.tar.xz`), bootstrap script (`recover_rh08.py`), and principal G3 input (`RH08_B1_Q2_G3.json`).

### Complete inline capsule


[Encoded source block omitted; the code in this passage is incomplete.]
