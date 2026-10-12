# figure-0619

AI research report · 2026-09-29 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Vivid Comet 47 — exact Q consolidation, certified pair deaths, and detached facet fusion

Branch: `[internal-source-reference]`.
Parent: `figure-0617`, SHA-256 `d9a82a95edfca7994e63592a49a9c42dd4113255ce843f8920fdaf699e717f36`.

## Result and acceptance boundary

**No homogeneous own strict110/additionalweak000 body was obtained.** This continuation nevertheless removes the fragmentation that blocked the previous escaped geometry: the exact FLOW_C body, own(32,1,31), is replaced by **VC47B_CONSOLIDATED_G10, V58/E168/F112, own(2,1,1), additionalweak000, P empty and exactly one positive Q**. The number of positive Q bars falls from31 to1. This is a net endpoint reduction of30 subsidiary pairs; **29 distinct individual S/H deaths are certified along an entire actual-mass path**, not inferred from a persistence threshold.

The second main result is an exact **class-preserving finite fusion into a detached ten-gon**. Starting from a simpler, more robust own211 companion, a rational parallel-coordinate path ends at **VC47B_PIVOT_G4_STAGE7, V58/E161/F105, own211/weak000**, still with both stable carriers avoiding the unique U. The whole path is certified, including one exact diagonal-change wall and the final cofacial fusion. Seven true edges are saved. This is not another S/H cancellation: its single principal Q remains positive.

A separate finite deletion-and-repair sequence gives **VC47B_PRUNED43_G8, V43/E123/F82, own211/weak000**, with both stable triangles detached from U. It is a useful budget alternative with42 generic point slots, but a substantially deeper principal Q. None of these tradeoffs is promoted to110 or an unconditional record improvement.

## Source authority, reading, and scope

The complete supplied journal was read consecutively through EOF,2,786 lines. Its mounted bytes are454,527 and SHA-256 `3cbe5ae02ac35b27b739df12a68e8a4a9c7b9db44fc0c53f23a1d4df556326ad`. The embedded parent's compact UTF-8 version2 JSON reconstructs68,733 bytes and its required SHA-256 above. Its point arrays, not historical aliases, are the source authority. The previous fixed two-anchor corridor was not reused as a proposed mass repair; the present work starts from the genuinely escaped FLOW_C geometry. The parent distinguishes that geometry and its complete nonwinning census explicitly. fileciteturn17file0L366-L385

Two source-precision issues are retained rather than silently reconciled. The journal calls the previous escaped bodies “primitive000”; the literal parent explicitly enumerates additional weak equilibria and global directed primal/polar chord equalities. Here I report those actual checks, not an unspecified stronger primitive census. Also, the literal parent `corridor47.py` is6,837 bytes/SHA `3cadf6a06219fb30f53cf08fad459b4ef57b9bfb289d61347e99f7c1d9b7c3a7`, whereas the advertised ZIP version is6,836 bytes/SHA `5d5187a462c9b8bab978772b284ba6180ea4a187d619c7b6db4e288071e2130e`. Only a descriptive docstring line break differs; the computational code is identical. The dependency extractor authenticates either recorded version. The literal source is used here.

All exact results below use the inherited Fraction engine's exhaustive supporting-triple hull reconstruction, exact maximal facets and true edges, connected oriented boundary checks, global uniform volume/first moments, direct strict/additional-weak S/U/H tests, and every strictly positive P/Q bar. Centered positive tetrahedra reproduce the volume and zero first moments. The divergence-form first-moment formula is also checked. This is one inherited equilibrium engine plus new exact polynomial and mass certificates, **not two independently developed physics verifiers**.

## 1. Genuine consolidation of the subsidiary landscape

Before unconstrained motion, FLOW_C's72 submitted rows were compacted to its58 actual extreme vertices. The exact map is embedded in `data47b.py` and checked against the parent hull. Old submitted root12 becomes compact root10. The58-point bound remains valid throughout the numerical point deformation; no92-row or72-row budget was silently substituted for it.

The numerical consolidation minimizes squared point displacement, rebuilding the hull and actual homogeneous centroid at each evaluation. It permits the current farthest polar vertex and the largest-Q root, while requiring every other current facet to have a negative **direct facet-foot guard**. For outward triangle normal n, centered points p_i and edge i--j, the guarded quantity is `n.cross(p_i,p_j)/(|n|*|p_j-p_i|)`. This avoids dividing by a tiny difference of neighboring polar vertices. Primal nonroots retain positive normalized global chords at the actual centroid. The allowed roots, witnesses, facets and material positions can change.

The selected consolidation run used200 SLSQP iterations as its cap, coordinate bound0.1, facet exclusion target1e-5, and primal target1e-6. It stopped at159 iterations with “Positive directional derivative for linesearch,” not solver success. A stored class-first checkpoint was rationalized and tested by the full exact engine. Its exact class, not the solver's exit code or its final infeasible trial, supplies the finding.

**CONSOLIDATED_G10** has:

```
V/E/F = 58/168/112
own strict S/U/H = 2/1/1
additional weak = 0/0/0
S material cycles = (2,37,9), (22,38,26)
U = compact10
H = compact28--42
P = []
Q = [0.28174488223881283...]  (exact fraction in the replay)
```

The maximum point displacement from exact FLOW_C is about0.000767679. Eleven old triangular support sets disappear and eleven appear; these are endpoint face-set differences, not a certified number of independent flips. The own centroid changes by approximately `(-0.00001690507829,+0.00007545319775,+0.00006104302109)`.

The remaining principal Q **increases** from approximately0.2801239199 to0.2817448822; even total Q depth increases from approximately0.2801365161. Thus this is a class/landscape consolidation, not an improvement of every scalar loss. At the new own centroid there is no subsidiary positive bar in addition to the one principal bar; the count reduction is not obtained by hiding values below a tolerance.

### An entire exact path with29 distinct actual pair deaths

Let A be the exact compact FLOW_C_G10 points and B the exact CONSOLIDATED_G10 points. On

```
X(t)=(1-t)A+tB,   1/10 <= t <= 1,
t=1/10+9s/10,     0 <= s <= 1,
```

the actual boundary has the same112 strict triangular facets throughout. The whole path has exactly one strict U, compact10, and no weak U. Two stable triangles persist;29 other facets each undergo exactly one simple stable-to-nonstable crossing, at disjoint exact root intervals. No other facet has a possible weak-stable event.

The certificate uses integer-coordinate polynomial X(s), actual tetrahedral volume polynomial W of degree3 and first-moment numerator M of degree4. The true centroid is `M/(4WD)` for coordinate denominator D. Cleared primal signs are

```
4W * x_i.(x_j-x_i) - M.(x_j-x_i),
```

and cleared facet-foot signs are

```
4W * n.cross(x_i,x_j) - n.cross(M,x_j-x_i).
```

The latter have degree at most7. All6,160 nonincident hull guards, center-interiority conditions, one positive primal witness per nonroot, all strict root guards, stable guards, exclusion guards and death-guard derivatives are checked over their entire intervals. There are6,561 polynomial tests and6,561 Bernstein nodes, with **zero subdivision** needed. Each dying guard is strictly decreasing;48 exact rational bisections isolate its unique root, and all29 isolating intervals are disjoint.

The first death is at original t approximately0.340086764181082 and the last at0.991559989982871. The report contains every dying facet, edge, complete integer polynomial and rational interval. One exact rational sample in each of the30 event-free intervals receives the full own-centroid census and all positive bars.

Before the first event the path is strict(31,1,30). After j deaths it is strict(31-j,1,30-j), additionalweak000. At the jth event, the crossing face and its edge contribute additionalweak(1,0,1); the other carriers remain strict. A weak edge would require either a weak vertex at an endpoint or a weak incident facet when a normal-cone coefficient vanishes, so the enumerated S/U sign conditions also exclude unlisted weak-edge events. Consequently these are actual S/H deaths, not only polar-root bookkeeping.

**Boundary:** the earlier interval0<=t<1/10 is not certified by this path proof. The net endpoint reduction is30 Q bars;29 individual deaths are proved on the stated later interval. No30-event weak-free homotopy or complete earlier bifurcation sequence is claimed.

### Shape and mass are both essential

The exact cross-centre controls are:

| Surface and reference center | Strict S/U/H | Additional weak | Positive P / Q |
|---|---:|---:|---:|
| Old FLOW_C surface at the new consolidated centroid | 30/34/62 | 0/0/0 | 33 / 29 |
| New consolidated surface at the old FLOW_C centroid | 17/9/24 | 0/0/0 | 8 / 16 |
| New consolidated surface at its own centroid | 2/1/1 | 0/0/0 | 0 / 1 |

The improvement is not obtained by relocating the reference point on a frozen surface, or by moving points while substituting the old mass center. The actual finite changes must be evaluated together.

## 2. Simpler arithmetic and a detached ten-gon

Two further class-first margin stages target1e-4 and1e-3 in both the primal and facet-foot constraints, with bounds0.2/0.5 and iteration caps200/350. They stop at163/167 iterations with the same non-success SLSQP status. Their selected exact freezes nevertheless remain own211. They deliberately exchange a slightly deeper main Q for stronger sufficient fixed-surface center buffers and simpler arithmetic.

**BUFFER_G4** is58/168/112, own211/weak000, Q approximately0.2887050335. Its literal coordinates have at most15 numerator bits and14 denominator bits; its actual centroid denominator has61 bits. In particular, its centroid is not rounded to zero:

```
V = 2775843712561 / 300000000000
c = (173348991486622797,
     -138652517065707771,
     -806066199977119242) / 2220674970048800000.
```

Its two stable triangles `(22,38,26)` and `(32,37,56)` both avoid U10. The sufficient open fixed-surface S2/U1 center-cube radius is approximately0.0004779089935, compared with7.0860538744e-7 for CONSOLIDATED_G10. These are particular inner certificates, not largest center regions or finite physical mass-controller capacities.

### Exact finite fusion recipe

Starting from the complete BUFFER_G4 integer array in the capsule, retain every x and z coordinate and all y coordinates except the ten indices

```
[0,1,2,3,4,9,32,37,56,57].
```

For those ten points impose exactly

```
-523027*x -745798*y -412587*z = 895914,
y = (895914 +523027*x +412587*z)/(-745798).
```

The resulting exact body is **VC47B_PIVOT_G4_STAGE7**. “G4” refers to the base array only: the changed y coordinates are rational fractions, not all multiples of10^-4.

```
V/E/F = 58/161/105
own strict = 2/1/1; additionalweak = 0/0/0
U10 is exactly unchanged and is not in either stable facet
S cycles = (0,2,4,32,37,56,57,3,1,9), (22,38,26)
H = 28--42
P = []
Q = [0.28859413274866513...]
V = 20704254195651905453 / 2237394000000000000
```

Its point numerator/denominator maxima are33/33 bits; actual centroid denominator99 bits. The sufficient open S2/U1 center-cube radius is0.0004488551580. Volume increases by approximately0.00092397863149 relative to BUFFER_G4. The centroid changes nontrivially; no exact mass preservation is claimed.

Seven separately audited nested projection stages produce polygons of4 through10 vertices. All are strict211/weak000, with one positive Q. Their edge counts are167,166,165,164,163,162,161. They are exact endpoint constructions, not merely merged facet labels in a floating hull.

### Entire class-preserving fusion path, including its fan change

The direct interpolation from BUFFER_G4 to the final rational projection moves all affected points parallel to the y axis. Every supporting-tetrahedron determinant is therefore affine. There is exactly one interior diagonal wall at

```
tau = 40534867098 / 6388900792319
    = approximately 0.0063445760727311165.
```

Across it the two triangular sets

```
(3,56,10), (10,56,57)
```

are replaced by

```
(3,57,10), (3,56,57).
```

At the wall the actual maximal boundary is58/167/111; before and after it, away from the final fusion, it is58/168/112. At t=1 the final ten-gon gives58/161/105. Treating all original triangles as supports beyond the wall would be incorrect; the proof uses both actual fan cells.

On each closed fan interval,6,615 exact tests certify the support signs, positive triangle areas, actual volume/interiority, strict U10, a positive primal forest, two stable triangles and negative witnesses for all other triangles. Boundary support zeros are allowed only at the certified fan/fusion endpoints. The volume polynomial has degree at most1 and the first-moment numerator degree at most2. The homogeneous mass formulas also agree with the divergence first-moment formula. The true maximal hulls at t=0,tau,1 receive separate full exact censuses.

The **entire path is own strict211/additionalweak000**, including the diagonal wall and the cofacial endpoint. It preserves both stable carriers' detachment from U. This is a finite class-preserving edge-saving mechanism, not a proof that arbitrary face clusters can be fused or that the remaining Q will disappear.

### Other fusion geometries retained

The earlier FUSED10_G6/G8 bodies also save seven edges but put U10 on the stable ten-gon. They remain valid own211 nonwinners, but do not retain the same useful detachment. DETACHED10_G6 is a separately rounded free-normal fusion with58/161/105, Q approximately0.2885905957. RETIREDFUSED_G6 has57/158/103: original compact point26 becomes nonextreme, and the current junior stable triangle changes to `(22,38,34)` while Q deepens to approximately0.3111930565. These are different exact bodies, not aliases of the simpler pivot recipe.

## 3. A43-vertex clean alternative

The deletion-and-repair producer starts from the literal stored ROBUST_C numerical checkpoint. At each stage it ranks single deletions by complete numerical P plus subsidiary Q depth, tests the four nominated deletions, and performs actual-mass class restoration with coordinate bound0.15, both exclusion margins1e-5, and at most160 SLSQP iterations. It does not require old root coordinates or old facet labels to remain fixed. Fifteen accepted stages and60 completed candidate solves are recorded; this is not an exact certificate of the whole optimizer trajectory.

The accepted deleted original58-point indices are

```
[8,5,44,26,22,38,14,37,29,40,45,36,28,25,35].
```

All43 remaining rows are genuine extremes in **PRUNED43_G8**. Its current material map is preserved; old compact U10 becomes new compact U8.

```
V/E/F = 43/123/82
own strict = 2/1/1; additionalweak = 0/0/0
S = (9,27,26), (24,39,40), both avoiding U8
H = 19--29
P = []
Q = [0.5718188456349375...]
V = approximately 7.881015754901668
c = approximately (0.052614426632338,
                  -0.018727546389636,
                  -0.343059053275377).
```

The full fractions are emitted by the recovery. Its sufficient open fixed-surface S2/U1 center radius is3.9257208177e-6. The48-vertex stage is separately retained at48/138/92, own211 and Q approximately0.5207641049. These smaller bodies buy budget by worsening the principal defect; they are not presented as uniformly better than the58-point buffered entrance.

**Budget distinctions:** the43 extreme points allow42 additional independently moved/submitted points under N<=85, hence E<=249. Its82 actual facets also permit a different parameterization: releasing those82 normals freely gives only the general E<=240 bound, and three additional arbitrary halfspaces keep F<=85/E<=249. It would be wrong to retain E123 after fully releasing all82 normals. For the58-point pivot body,27 generic extra points are unconditional. Retaining the exact ten-gon as a genuine maximal facet, with all ten corners represented, gives the stronger conditional bound E<=3N-13;29 extra points then give N87/E<=248. Neither budget argument preserves the mechanical class.

## 4. Full exact endpoint ledger and rounding controls

All25 retained endpoint representations below have additionalweak000 and global directed primal/polar chord zero counts0/0. Twenty-three are own211. Every row has **exactly one positive Q**. P is empty except in the two explicitly marked controls. Coordinates, full own volume/first moments/centroid, maximal cycles, true edges, every positive bar with its exact birth/death values, and submitted-to-extreme maps are regenerated without an optimizer.

Names in this table have the prefix `VC47B_`.

| Endpoint | V/E/F | Strict S/U/H | Positive P count | Sole Q depth, approximate |
|---|---:|---:|---:|---:|
| BUFFER_G4 | 58/168/112 | 2/1/1 | 0 | 0.2887050335078117 |
| BUFFER_G5 | 58/168/112 | 2/1/1 | 0 | 0.2886787105929747 |
| BUFFER_G8 | 58/168/112 | 2/1/1 | 0 | 0.2886798148498653 |
| CONSOLIDATED_G10 | 58/168/112 | 2/1/1 | 0 | 0.2817448822388128 |
| CONSOLIDATED_G6 | 58/168/112 | 2/9/9 | 8 | 0.2817451643806437 |
| CONSOLIDATED_G8 | 58/168/112 | 2/1/1 | 0 | 0.2817448771372886 |
| DETACHED10_G6 | 58/161/105 | 2/1/1 | 0 | 0.2885905956921498 |
| FUSED10_G6 | 58/161/105 | 2/1/1 | 0 | 0.2821273989329616 |
| FUSED10_G8 | 58/161/105 | 2/1/1 | 0 | 0.2821273589029747 |
| PIVOT_G4_STAGE1 | 58/167/111 | 2/1/1 | 0 | 0.2886556764366772 |
| PIVOT_G4_STAGE2 | 58/166/110 | 2/1/1 | 0 | 0.2886308322299985 |
| PIVOT_G4_STAGE3 | 58/165/109 | 2/1/1 | 0 | 0.288611175138156 |
| PIVOT_G4_STAGE4 | 58/164/108 | 2/1/1 | 0 | 0.2886075538913095 |
| PIVOT_G4_STAGE5 | 58/163/107 | 2/1/1 | 0 | 0.2886004019417637 |
| PIVOT_G4_STAGE6 | 58/162/106 | 2/1/1 | 0 | 0.2885955760160174 |
| PIVOT_G4_STAGE7 | 58/161/105 | 2/1/1 | 0 | 0.2885941327486651 |
| PRUNED43_G5 | 43/123/82 | 2/14/14 | 13 | 0.5718200655647094 |
| PRUNED43_G6 | 43/123/82 | 2/1/1 | 0 | 0.5718188277090095 |
| PRUNED43_G8 | 43/123/82 | 2/1/1 | 0 | 0.5718188456349375 |
| PRUNED48_G6 | 48/138/92 | 2/1/1 | 0 | 0.520764316566831 |
| PRUNED48_G8 | 48/138/92 | 2/1/1 | 0 | 0.5207641048900904 |
| RETIREDFUSED_G6 | 57/158/103 | 2/1/1 | 0 | 0.3111930564754882 |
| ROBUST_G5 | 58/168/112 | 2/1/1 | 0 | 0.2821230949477523 |
| ROBUST_G6 | 58/168/112 | 2/1/1 | 0 | 0.2821272615646554 |
| ROBUST_G8 | 58/168/112 | 2/1/1 | 0 | 0.2821270906263658 |

The complete positive P-depth lists for the coarse controls are:

```
CONSOLIDATED_G6, strict(2,9,9):
6.647255173916569e-12, 4.127565570860337e-12,
6.325061914055338e-13, 6.312042592613923e-13,
4.0856475598055253e-13, 2.1569878855621825e-13,
1.618514063415671e-13, 4.896262636986098e-14.

PRUNED43_G5, strict(2,14,14):
5.512693423526528e-10, 3.5735658957026975e-10,
3.2337795135730256e-10, 3.0990887541278414e-10,
2.6188315756821085e-10, 1.0757886237717043e-10,
1.0415275022516194e-10, 7.483448667929529e-11,
3.2337814975941465e-11, 2.1707793030362347e-11,
1.3482994638392855e-11, 4.114190132947774e-12,
2.2590304675383965e-12.
```

Those are display approximations to strictly positive rational values, not zeros. Across the25 endpoint audits there are21 positive P bars and25 positive Q bars. The exact cross-center controls and the path's interval samples have their own complete bar lists, separately identified in their reports; they are not additional homogeneous endpoint records.

## 5. The current remaining basin and useful continuation

For PIVOT_G4_STAGE7, the sole junior is triangle `(22,38,26)`, facet61 in the exact endpoint ordering. Its Q dies across dual77--78, physical saddle28--42. The strict polar component above that death has37 vertices and21 true dual crossing edges; all2,516 global outgoing chords from that component to its complement are strictly negative at the actual centroid. U10 has four incident facets, three belonging to this component. Thus detaching the two stable carriers from U does **not** make the whole stable basin independent of the unstable carrier.

For PRUNED43_G8 the corresponding high component has28 polar vertices,22 true dual crossings and1,512 strictly negative global exits. Its physical saddle19--29 lies between triangles `(19,20,29)` and `(19,29,23)`. U8's six incident facets split three inside and three outside the component. The exact component lists, crossings, material cycles and witness extrema are in `VC47B_CURRENT_Q_BASINS.json`.

These are endpoint diagnostics, not exclusions of changed geometry or mass. The next substantial operation should alter this **single principal basin and its crossing boundary** while using the newly available point/facet budget and actual U1 margins. Repeating the previous tiny-bar shrinkage is unnecessary: there is now a clean one-bar entrance. PIVOT58 offers buffered, detached, partially planar geometry; PRUNED43 offers much more free material budget and a separate82-support chart. Their different Q depths and center buffers should remain explicit when selecting a continuation.

## 6. Complete recovery, commands, and evidence level

The capsule below contains19 complete new files:17 source units, the literal binary64 nomination/checkpoint data needed by their exact freezing procedures, and the exact expected-output manifest. All coordinates needed to reproduce every reported exact endpoint are included. Binary64 checkpoint numbers are finite round-tripping values, converted to exact Fractions **before** ties-to-even grid freezing; no trigonometric or optimization rerun is required. A source-only nomination-to-freeze replay reproduced all50 input/audit hashes for the25 endpoints.

The four unchanged parent dependencies are `exact47.py`, `replay47.py`, `corridor47.py` and `num47.py`. They are already supplied literally in the named parent and are not duplicated here. The included extractor accepts the current complete journal or the literal parent's Markdown, verifies the complete parent hash, and extracts/authenticates those four files. This is a supplied-source dependency, not an on-demand archive request.

Save the following code block as `RECOVER_VC47B.py`, then run:

```sh
python -B -S RECOVER_VC47B.py VC47B_SOURCE
cd VC47B_SOURCE
python -B -S extract_parent47b.py /path/to/research-journal.md
python -B -S regenerate47b.py OUT
```

The exact commands use standard-library Python3.13.5, assertions enabled. No numerical package is imported by the exact recovery. In a fresh directory, the final command reconstructs the25 freezes, audits every actual body, proves both entire paths, checks the center controls and reference-center cubes, writes all compaction/remaining-basin data, and verifies55 exact scientific output identities. That complete fresh-directory replay was executed successfully.

Observed terminal markers:

```
VC47B_LITERAL_NOMINATIONS_ALL25_EXACT_FREEZES_PASS 50
VC47B_29_DISTINCT_OWN_MASS_S_H_DEATHS_U1_PATH_EXACT_PASS_NO_110
VC47B_ENTIRE_TWO_FAN_DETACHED_FUSION_OWN211_PATH_EXACT_PASS_NO_110
VC47B_FIXED_SURFACE_CUBES_AND_CROSS_CENTRE_CONTROLS_EXACT_PASS_NO_110
VC47B_ALL25_ENDPOINTS_BOTH_WHOLE_PATHS_COLD_REPLAY_PASS_NO_110 55
```

`python nominate47b.py` restores the exact stored numerical checkpoints and prints every executed primary producing command, including all nondefault settings. Numerical nomination used NumPy2.3.5, SciPy1.17.0 and PyTorch2.10.0+cpu, float64, one Torch/BLAS/OpenMP thread. Floating optimizer trajectories need not reproduce across environments; the stored checkpoints, exact freezes and polynomial proofs do not rely on that portability.

Principal report identities:

| Exact report | Bytes | SHA-256 |
|---|---:|---|
| VC47B_CONSOLIDATED_G10_EXACT.json | 64259 | 92335a1e275301fe05d75b0b35916e03d685663c70174330398e387c11843a46 |
| VC47B_29_DEATHS_PATH_EXACT.json | 1202599 | 4a492c314182db9eb64006f02ac2eafb6a7b223ab86400ec784c61ec220e9c2d |
| VC47B_BUFFER_G4_EXACT.json | 39284 | dce6be9d2b88cc0c281969fa0af8c212bc2d80d6bd55cd9d74964266e8a8dc8c |
| VC47B_PIVOT_G4_STAGE7_EXACT.json | 44680 | 2e0e2e17f3e3e1e8f4af519dc336c8f2f05f6f69c70178972c08b9e44978b897 |
| VC47B_DETACHED_FUSION_PATH_EXACT.json | 427761 | 40abb6e3426aba4ad21c35dac96a2dbcb719e8e7c9e6df57cd17c35985fe779e |
| VC47B_PRUNED43_G8_EXACT.json | 41544 | a9a1d00405046cb7deed26f53691c85684e78b17ecc7956128d325d8c823c2fd |
| VC47B_CURRENT_Q_BASINS.json | 6375 | 560e7d7a4bb9581d4d6b747cfe098df05ec7c853d7da6fc939ed08b29ec1bfa9 |

Capsule dictionary: **107749 bytes**, SHA-256 `3c7c015455f163d4a99d08201a5f1ead98ba77df1d0451983af9b835b480608d`. Canonical decoder source: **38140 bytes**, SHA-256 `10d4cc3e0d7b3cb6d742209160b2181c7131f1caa3dc398ec3bc85473918e956`. The decoder validates the entire recovered dictionary and writes per-file byte counts/hashes. These are transport checks; the exact replay supplies the scientific checks.


[Encoded source block omitted; the code in this passage is incomplete.]


## Supplement and final boundary

[VC47B supplementary files, exact outputs and research sources](sandbox:/mnt/data/VC47B_RESEARCH_HANDOFF.zip) accompany the inline recovery; the ZIP is not the sole source of any reported exact successor. It also retains unpromoted numerical exploratory files, separated from the25 exact endpoint records. The canonical decoder is also available as [RECOVER_VC47B.py](sandbox:/mnt/data/RECOVER_VC47B.py).

No scheduler or journal operation was performed. No accepted own110 result is changed. The durable new scientific results are the clean actual-U1/one-Q entrance,29 rigorously traced subsidiary pair deaths, the whole class-preserving detached ten-gon fusion path, the simpler buffered rational body, and the43-vertex budget alternative. The remaining principal Q is positive in every retained endpoint.
