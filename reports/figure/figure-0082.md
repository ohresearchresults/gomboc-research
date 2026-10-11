# figure-0082

Historical AI scientific report · saved 2026-08-26 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Skew-prismatoid whole-basin continuation — complete handoff

## Determination

**No strict homogeneous convex polyhedral Gömböc was obtained.** I retained the run’s non-negotiable gate: the uniform-volume centroid of the body itself, one stable maximal face, one unstable vertex, no saddle true edge, complete incidence/cone reconstruction, positive raw separation, and a finite expanded mesh. :contentReference[oaicite:0]{index=0}

The supplied journal ended with the exact 20-vertex `(2,1,1)` prismatoid and a rejected four-circuit 22-vertex wall, and explicitly isolated a 24–26-input bifurcated Y-strip as the smallest untried continuation. :contentReference[oaicite:1]{index=1} This continuation actually crosses that frontier. The strongest result is an exact 25-input Y-strip hull with one obsolete row deactivated, `(V,E,F,C)=(24,52,30,104)`, and a wide strict own-centroid class `(S,U,H)=(2,1,1)`. It eliminates the old unwanted witnesses but transfers their Morse pair to a new stable triangle and a new lower-fork edge. It is a robust nonwinner, not a wall point.

Relative to the journal, the material advances are:

- a completely exact post-Y body with a genuine row deactivation and a `1/2,000,000` outward coordinate box;
- independent Qhull, mass, full-cone, OBJ, and STL reconstruction;
- an exact four-inequality Farkas obstruction for the natural simultaneous edge-breaker branch;
- a low-degree one-apex centroid-closure reduction to a scalar quartic and an enumeration of 1,435 visibility cells / 1,743,536 root candidates;
- a quantitative demonstration that mechanically invisible mass transport is macroscopic rather than a small local repair.

## Search and real topology changes

I searched connected stable-side/lower-side Y strips, four simultaneous edge-star breakers, full-strip and double-Y variants, row deletion/deactivation, fixed-cell coordinate optimization, determinant-one metrics, direct own-centroid optimization, exact single-face pyramid closure, arbitrary multi-face one-apex closure, and mechanically invisible moment corridors. Rebuilt hulls entered strict `(2,1,1)`, `(2,2,2)`, `(3,1,2)`, and `(4,1,3)` cells. The strongest rational endpoint uses five connected input rows `20–24`; old lower-cap row `17` is strictly interior. The original stable triangle `(19,8,18)` is absent, and original saddle edge `(0,19)` survives only as a strict nonsaddle. The residual Euler-balanced pair has migrated to face `F21=(18,20,22)` and edge `E51=(23,24)`.

## Complete exact V-representation

Every decimal below is literal, hence an exact rational. Row 17 is an input control point but is strictly deactivated; the other 24 rows are the actual hull vertices.

```text
00 (0.4756161830, -0.9337688508, 0)
01 (0.6842891459, -0.8989783949, 0)
02 (1.0481552627, -0.6112355097, 0)
03 (1.2755777124, -0.2202413337, 0)
04 (1.3637437814, 0.2488334051, 0)
05 (1.2849044523, 0.7410523649, 0)
06 (1.0170965409, 1.1986517418, 0)
07 (0.6191297824, 1.5351441689, 0)
08 (-0.0063866144, 1.8754809932, 0)
09 (-0.6985041963, 1.4979807161, 0)
10 (-1.0140947488, 1.2174063967, 0)
11 (-1.2856529747, 0.7456238685, 0)
12 (-1.3710870158, 0.2483772792, 0)
13 (-1.2758033499, -0.2249267384, 0)
14 (-1.0483750550, -0.6045635047, 0)
15 (-0.7325841547, -0.8739513553, 0)
16 (-0.4260837488, -1.0043250072, 0)
17 (0.1254053900, -0.9818636314, -0.0822563738)  [strictly interior/deactivated]
18 (0.2262423217, -0.9527871690, -0.0822563738)
19 (-0.2648479934, -1.0370197767, -0.0822563738)
20 (-0.0130716858, -1.0014270294, -0.0825191734)
21 (0.1242088087, -0.9820279589, -0.0825374227)
22 (-0.0032138147, 1.7794928099, -0.0028122892)
23 (0.5616363774, -0.9211696869, -0.0136515101)
24 (0.0522771486, -0.9956615507, -0.0809455855)
```

Active input IDs: `0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24`.

## Exact uniform-volume centroid certificate

Fan-triangulate each oriented maximal polygon and join every boundary triangle `(a,b,c)` to the coordinate origin. With `D=det(a,b,c)`, the verifier computes

`6V = ΣD`,  `c = [ΣD(a+b+c)]/[4ΣD]`.

- `6V = 541098968002548333845929162899/500000000000000000000000000000`
- `V = 180366322667516111281976387633/1000000000000000000000000000000` = `0.180366322667516111281976387633`
- `c_x = -358231681941909112458348741706599671399/43287917440203866707674333031920000000000` = `-0.00827555824178318340567943044057179209`
- `c_y = -412411849401330096266713909675026988947/14429305813401288902558111010640000000000` = `-0.0285815447211812891356685184703167393`
- `c_z = -197522805610048283396840117288084103259/8657583488040773341534866606384000000000` = `-0.0228150044273783894267660020383794148`
- Boundary fan: 44 oriented triangles. After translating by this exact centroid, all three first moments are identically zero in `Fraction` arithmetic.

## Complete maximal-face cycles

```text
F00 (1,21,18)
F01 (11,19,12)
F02 (10,19,11)
F03 (8,19,9)
F04 (9,19,10)
F05 (0,16,19)
F06 (4,18,5)
F07 (5,18,6)
F08 (1,18,2)
F09 (7,18,8)
F10 (6,18,7)
F11 (18,21,20)
F12 (12,19,13)
F13 (13,19,14)
F14 (15,19,16)
F15 (14,19,15)
F16 (0,23,1)
F17 (1,23,21)
F18 (3,18,4)
F19 (2,18,3)
F20 (8,18,22)
F21 (18,20,22)
F22 (8,22,19)
F23 (19,22,20)
F24 (21,23,24)
F25 (0,24,23)
F26 (0,19,24)
F27 (20,21,24)
F28 (19,20,24)
F29 (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
```

`F29` is one 17-gonal maximal face; its fan diagonals are not true edges.

## Complete true-edge incidence

```text
E00 (0,1):F16,F29
E01 (0,16):F05,F29
E02 (0,19):F05,F26
E03 (0,23):F16,F25
E04 (0,24):F25,F26
E05 (1,2):F08,F29
E06 (1,18):F00,F08
E07 (1,21):F00,F17
E08 (1,23):F16,F17
E09 (2,3):F19,F29
E10 (2,18):F08,F19
E11 (3,4):F18,F29
E12 (3,18):F18,F19
E13 (4,5):F06,F29
E14 (4,18):F06,F18
E15 (5,6):F07,F29
E16 (5,18):F06,F07
E17 (6,7):F10,F29
E18 (6,18):F07,F10
E19 (7,8):F09,F29
E20 (7,18):F09,F10
E21 (8,9):F03,F29
E22 (8,18):F09,F20
E23 (8,19):F03,F22
E24 (8,22):F20,F22
E25 (9,10):F04,F29
E26 (9,19):F03,F04
E27 (10,11):F02,F29
E28 (10,19):F02,F04
E29 (11,12):F01,F29
E30 (11,19):F01,F02
E31 (12,13):F12,F29
E32 (12,19):F01,F12
E33 (13,14):F13,F29
E34 (13,19):F12,F13
E35 (14,15):F15,F29
E36 (14,19):F13,F15
E37 (15,16):F14,F29
E38 (15,19):F14,F15
E39 (16,19):F05,F14
E40 (18,20):F11,F21
E41 (18,21):F00,F11
E42 (18,22):F20,F21
E43 (19,20):F23,F28
E44 (19,22):F22,F23
E45 (19,24):F26,F28
E46 (20,21):F11,F27
E47 (20,22):F21,F23
E48 (20,24):F27,F28
E49 (21,23):F17,F24
E50 (21,24):F24,F27
E51 (23,24):F24,F25
```

Euler check: `24-52+30=2`; mechanical complexity `C=24+52+30-2=104`.

## Exhaustive equilibrium audit at the exact own centroid

The tests are complete feature-cone tests, not incident-facet proxies:

- For a maximal face, the perpendicular foot of the exact centroid must lie strictly inside every boundary halfplane of the entire maximal polygon.
- For a vertex `v`, instability requires `-(v-c)·(w-v)>0` for every true neighbor `w`.
- For a true edge `AB`, let `e=B-A`, `t=((c-A)·e)/(e·e)`, and `r=A+te-c`. It is a saddle exactly when `0<t<1` and `-r·(x-A)>0` for every other input row `x`; this audits the full edge normal cone, including the deactivated row.

Classification by complete complement:

- **Stable faces:** `F21=(18,20,22)` and target `F29=(0,1,...,16)`. Every other maximal face is strictly nonstable.
- **Unstable vertices:** only target `V08`. Every other actual vertex is strictly nonunstable.
- **Saddle edges:** only `E51=(23,24)`. Every other true edge is strictly nonsaddle.

Margins: residual stable `+0.000408155768513745155450078436791541194`; residual saddle `+0.000408155779985053478591083632084804162`; target cap `+0.321416685729271509514603674709400035`; target vertex `+0.477021765029202359590862694766674277`. The minimum positive equilibrium margin is `+0.000408155768513745155450078436791541194`. The closest excluded feature is nonstable `F23=(19,22,20)` at `-0.000404161146747622623000596526363790967`. The closest nonsaddle edge is `E04=(0,24)` at `-0.000434187809104134885906934970858373388`; the closest nonunstable vertex is `V15` at `-0.00215870776296948049769589956343807094`.

The minimum normalized inactive support separation is `0.0000077280310542952453258651604190793867939554040573876150093906997761290300752944758724879154691801342728102762396` (Euclidean `0.000022605288894329388727762091060400858887286475610862527681949653468003338920906457331289135695248804336433494271`), attained by deactivated row 17 against `F24`. Its exact unnormalized support numerator is `6736909752244404365117/50000000000000000000000000000`. Thus the deactivation and all maximal-plane incidences are raw-separated, not tolerance merges.

The exact sign/numerator for every boundary test, every vertex tangent ray, and every edge-versus-input support test is recorded in `verification.json`; `faces.csv`, `vertices_audit.csv`, and `edges.csv` expose the complete tables.

## Open perturbation box

The outward interval audit passes for `ρ=1/2000000=5×10^-7`. Every `x,y` coordinate varies independently by `±ρ`; rows 0–16 retain `z=0`; every `x,y,z` coordinate of rows 17–24 varies independently by `±ρ`. Throughout this box, the same 30 maximal faces, 52 true edges, strict deactivation of row 17, and full `(2,1,1)` classification persist. This certifies an open nonwinner chamber.

## Independent reconstruction

A separately implemented SciPy/Qhull checker enumerates all supporting triples, reconstructs the same 24 active rows, 30 maximal face sets and 52 edges, performs its own oriented mass integration, and independently recovers volume `0.18036632266751607`, centroid `(-0.008275558241783238,-0.028581544721181323,-0.022815004427378396)`, `(2,1,1)`, minimum positive margin `0.0004081557685137266`, closest negative `-0.0004041611467476039`, and inactive separation `7.728031054322968e-6`.

Trimesh independently loads both exports as watertight, consistently wound Euler-2 meshes with 24 welded vertices and 44 triangles. The OBJ volume/centroid match the exact certificate to floating precision; the binary STL differs only by its mandated float32 storage.

## Exact new branch obstruction

On the separate exact 26-vertex post-Y body used to probe the four circuit breakers, the natural branch choosing support vertex 24 for edge `(19,22)`, support vertex 25 for `(19,24)`, support vertex 24 for `(19,25)`, and support vertex 12 for `(20,23)` is impossible for **every** center. Exact nonnegative multipliers combine the four affine inequalities to coefficient vector `(0,0,0)` and constant

```text
-651581013102860231181839193872643418670192916766579629961887563188644476400845416646185767588927963550298852454889043652265395954649334719493867632942860474503063078709743836501098098904312184660769391544369895343617609913872326591067454441077/1422498835809531605717793119640012085519682899062715447631411307942971765898568804806510791721556038103385767333932148716073508281681992261584316004880776881280123794096680500000000000000000000000000000000000000000000000000000000000000000000000000000
```

which is `-4.580538111527179e-07` and strictly negative. Therefore those four desired halfspaces have empty intersection. The standalone verifier recomputes the rational combination. This closes that precise witness branch, not all possible witness choices or all larger topologies.

## One-apex hard-centroid reduction

For a fixed visibility cell of one arbitrary added apex `a`, every visible boundary-tetrahedron volume is affine in `a`. Writing the exact centroid equation relative to a selected strict mechanical center `q` gives

`a(g·a+h) + C a + d + 4(M₀−V₀q) = 0`.

With `λ=g·a+h`, this becomes `(λI+C)a+d₀=0`; eliminating `a` leaves the scalar quartic

`(λ−h)det(λI+C) + gᵀ adj(λI+C)d₀ = 0`.

Thus all mass-closing apex roots in a fixed visibility cell can be enumerated rather than merely optimized. The run generated 1,435 self-consistent visibility patterns, sampled 400 distinct strict `(1,1,0)` center chambers of the original exact P20 geometry, solved 1,743,536 nonsingular quartic-root candidates, and found 300 apex roots that both matched their visibility pattern and closed the selected center to numerical residual around `10^-10` or better. None had target mechanics; the best resulting bodies were robust `(2,2,2)` with hard score about `-0.25785`. This is essentially complete over the enumerated cells for those sampled centers, but is not a continuum exclusion over every possible center.

A separate exact single-face pyramid closure sampled 14,405 strict target centers from ten million center proposals and produced no physically interior closure root for any maximal face. Direct one-apex own-centroid optimization instead converged to coplanar `(3,1,2)` transfer walls with inactive separations around `10^-11`–`10^-12`.

## Quantified moment-transport obstruction

The fixed 26-vertex geometry does possess an auxiliary strict `(1,1,0)` chamber, but its center is about one body unit from the own centroid, so it cannot be accepted. Starting from a strict auxiliary-center P20 chamber, a connected mechanically invisible cap sequence retained reference-relative `(1,1,0)` while moving the own centroid. After the first added row the center distance was `0.9223241418424595`; after nine additions it was still `0.8447541907635419`, with reference-mechanical gate `3.612616018533896e-5`. The observed local actuation is therefore far too weak to close the mass in a 24–30-input budget. A macroscopic connected volume corridor is required.

## What remains uncertain

The negative determination is empirical outside the exact certificates stated above. It does not exclude every skew prismatoid, every larger connected rail, or every witness branch. In particular, the one-apex enumeration samples the continuum of target centers, and the exact four-inequality certificate closes only one natural edge-witness branch. No claim of a global nonexistence theorem is made.

## Smallest genuinely unsearched whole-basin continuation

The next finite family should be a **34–42-input connected moment-corridor/double-Y**, not another local cap or serial rail:

1. Allocate roughly 12–18 new extreme rows to a mechanically descending corridor with enough macroscopic volume to move all three first moments, rather than adding shallow local tetrahedra.
2. Allocate 6–8 coupled rows to replace the entire residual stable star around `(18,20,22)` and the entire saddle star around `(23,24)` simultaneously; branch before either pair transfers.
3. Enumerate all immediate circuit cells, and in each cell eliminate the three tetrahedral first-moment equations as hard constraints before mechanical scoring.
4. Permit rows 17–25 and obsolete corridor rows to become interior, but require every claimed retained/new row to be extreme and enforce normalized inactive separation `>10^-6` (preferably `>10^-5`).
5. Exactify only a chamber whose target and excluded-feature margins are both `>10^-6`.

This is sharply delimited: a single arbitrary apex, one-face closure, determinant-one metrics, serial caps, four local edge breakers, and the 24–30-input local Y budget have all either transferred the pair, converged to incidence walls, or been exactly obstructed in the tested branch.

## Reproducible artifacts

- [Complete archive](sandbox:/mnt/data/skew_prismatoid_y_strip_result.zip), SHA-256 `034a76427b742740ea23d4ebfef683fa9aa8a087c1e7d9515223126795c0de49`.
- [README](sandbox:/mnt/data/skew_prismatoid_y_strip_result/README.md), SHA-256 `6194491773d9ac980abe1d90e74b4365888fe83e2c5bd9b090b19094b9698541`.
- [Exact Fraction/interval verifier](sandbox:/mnt/data/skew_prismatoid_y_strip_result/verify_fraction.py), SHA-256 `d7cd4cf1a1001f8e66b44abf8f237fec8ae8460719947803270f0b34e956fc72`.
- [Complete exact audit](sandbox:/mnt/data/skew_prismatoid_y_strip_result/verification.json), SHA-256 `788e1fce4f9b5ef348eee82982984ce103e6884d6772eeb2d7515290e9d941f3`.
- [Independent all-triples/SciPy verifier](sandbox:/mnt/data/skew_prismatoid_y_strip_result/independent_scipy.py), SHA-256 `85e478e956ba918f30c009ad68a9e75973d9fc13395e34b18d504f5527ac1461`.
- [OBJ](sandbox:/mnt/data/skew_prismatoid_y_strip_result/body.obj), SHA-256 `3a1a2ac8fd17533c7a05d9dd7e2083c26df2c0924791630d2521e04d28fabd21`; [binary STL](sandbox:/mnt/data/skew_prismatoid_y_strip_result/body.stl), SHA-256 `8ddebeb332edd7e419a469afadefc713f2de1dca6dfe5123edda5196a87dff1f`.
- `RUN_ALL.sh` reruns the exact audit, two independent reconstructions, mesh checks, and the standalone Farkas certificate verifier.
