# figure-0264

AI research report · 2026-09-03 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Calm Maple 15 — exact two-page/two-return successor `AQ32-G44-TP2R2-R139`

## Literal verdict

**No homogeneous convex polyhedral Gömböc was obtained.** The strongest completed successor is the exact rational, full-supplied-hull body

```text
AQ32-G44-TP2R2-R139
```

with strict own-centred class

```text
(S,U,H)=(2,1,1),
```

not `(1,1,0)`. It is a rigorous finite **NONWINNER**, not a wall point or an auxiliary-centre near-solution. The run’s acceptance gate requires an explicit uniform-density body at its own exact centroid with strict `(1,1,0)`, complete H/V/E data, exhaustive margins, independent verification, and matching meshes.

The requested first nonrepeating topology was nevertheless realized on the actual complete hull. Four new supports move simultaneously from exact parent carriers. The parent stable triangle `[25944,26061,26057]`, saddle edge `[25956,25976]`, and all thirteen faces of their certified connecting disk disappear. The final body contains two extreme pages and two communicating transverse returns in a connected positive-volume terminal. The protected stable 17-gon and unique unstable `N3=25840` survive. A replacement stable triangle `[26042,26057,26064]` and replacement saddle `[25975,26063]` are born, and an exact three-arc theorem proves `S>=2` throughout the endpoint cell.

## Reusable artifacts

- Complete exact archive (`AQ32_G44_TP2R2_R139_EXACT_NONWINNER.zip`)
- Complete expanded handoff (`AQ32_G44_TP2R2_R139_complete_handoff.md`)
- Finite exact source specification (`AQ32_G44_TP2R2_R139_source_spec.json`)
- Deterministic generator (`generate_AQ32_G44_TP2R2_R139_exact.py`)
- Independent endpoint verifier (`verify_AQ32_G44_TP2R2_R139_independent.py`)
- Independent common-homotopy verifier (`verify_AQ32_G44_TP2R2_R139_homotopy.py`)
- Exact endpoint certificate (`AQ32_G44_TP2R2_R139_certificate.json`)
- Complete 26,067-row exact table (`AQ32_G44_TP2R2_R139_all_supplied_Q_rows_exact.csv.gz`)
- Exact homotopy atlas (`AQ32_G44_TP2R2_R139_exact_common_homotopy_atlas.json`)
- Terminal-complex certificate (`AQ32_G44_TP2R2_R139_terminal_complex.json`)
- Residual obstruction certificate (`AQ32_G44_TP2R2_R139_dual_component_obstruction.json`)
- Q OBJ (`AQ32_G44_TP2R2_R139_Q.obj`) · Q STL (`AQ32_G44_TP2R2_R139_Q.stl`) · display preview (`AQ32_G44_TP2R2_R139_Q_preview.png`)
- P OBJ (`AQ32_G44_TP2R2_R139_P.obj`) · P STL (`AQ32_G44_TP2R2_R139_P.stl`)
- Archive SHA-256 sidecar (`AQ32_G44_TP2R2_R139_EXACT_NONWINNER.zip.sha256`)

```text
archive SHA-256 = 1e1d494e3e582b3c92af4ce29e13dc2192867c49fa67f4e85ba329e8e77fe5b8
```

The archive contains a manifest-bound copy of the complete authoritative parent construction and verifier. A clean extraction passed `SHA256SUMS`, deterministic regeneration reproduced the full table, and the final combined run returned all four success markers with exit status zero.

## Parent authority and exact generator

The immutable parent is `figure-0258`, SHA-256

```text
7fb3d35136c48889194c34afe5e2945fdafd72a7467696b084a1b906ecb7d26c.
```

It supplies all `26,063` rational rows of `AQ32-G44-CAP2R119-R136`, its `(136,388,254)` Q lattice, exact ordinary centroid zero, the protected stable 17-gon, unique unstable `25840`, stable carrier `[25944,26061,26057]`, saddle `[25956,25976]`, and disk faces

```text
29,30,31,32,33,34,60,73,74,75,77,94,244.
```

Reconstruct those rows exactly from the copied parent source specification and translate by the parent’s exact ordinary centroid. In that parent-centred frame insert the two page supports

```text
26063 = (8319898322512,-30385220475141,-690384794161)/10^12
26064 = (3799019387601, -7786196403518,-609934654598)/10^12.
```

Rebuild the exact hull, compute its exact tetrahedral ordinary centroid, and subtract it from every supplied row. In this exactly recentered two-page frame insert the transverse returns

```text
26065 = midpoint(25944,25945) + 2^-120*( 7,-11, 13)
26066 = midpoint(25944,25978) + 2^-120*(-5, 17,-19).
```

Rebuild the complete hull again, compute the exact volume and three first moments, and subtract the resulting exact centroid from all `26,067` rows. This finite recipe, together with the literal parent specification and the four rows above, deterministically produces every final rational coordinate. The final common denominator and every numerator are expanded in the source specification and complete row table; the generator independently reproduces them without importing saved endpoint incidence.

## Full supplied hull and irredundant incidence

```text
supplied rows       26,067
active/extreme         139
strictly inactive   25,928
Q (V,E,F)       (139,397,260)
P=Q^circ         (260,397,139)
Euler Q/P               2 / 2
complexity               794.
```

All four inserted rows `26063–26066` are exact extreme vertices. Parent row `25976` becomes strictly inactive. The actual endpoint contains no parent target face and no parent saddle edge.

The archive expands all active Q coordinates, all 260 maximal Q face cycles and primitive supporting planes, all 397 true Q edges, all 260 exact P vertices, all 139 maximal P faces, and all 397 true P edges. Mesh-only triangulation diagonals are recorded separately and never classified as true edges.

## Exact own centroid and Santaló identity

The exact Q volume is

```text
42612108429589978254280322958240040656743404133481224577697789835139635898383775689259091744850543867114549139998193554836554892309617907 /
24567402588368654580057483447542780451803749054464768639153435307695698977226752000000000000000000000000000000000000000000000000000000
```

or approximately `1734.4979094275322`. Direct exact tetrahedral summation gives

```text
ordinary first moments = (0,0,0)
ordinary centroid      = (0,0,0).
```

All mechanics is therefore evaluated at the body’s own uniform-volume centroid. Since `P=Q^circ` and `(P-0)^circ=Q` has centroid zero, the origin is exactly the Santaló point of P; strict convexity of polar volume gives uniqueness. The independent verifier rediscovers the complete Q hull before recomputing these exact moments.

## Exact simultaneous four-support event

All four inserted supports follow one exact rational homotopy from their parent carriers/anchors. Seven carrier-plane outward derivatives are exact-positive. Every one of the thirteen parent disk faces has an exact visibility threshold on the same four-support path.

The parent disk cycles are

```text
29  [25944,25945,25950]
30  [25944,25950,25978]
31  [25944,25951,25945]
32  [25944,25978,26061]
33  [25944,26057,25951]
34  [25944,26061,26057]
60  [25950,25967,25978]
73  [25956,25976,25977]
74  [25956,25977,25993]
75  [25956,25993,25967]
77  [25956,26062,25976]
94  [25967,25993,25978]
244 [26042,26057,26061].
```

At the first certified postcarrier sample, stable `[25944,26061,26057]` and saddle `[25956,25976]` are already absent together. The last target is face 244, covered by page `26064` at the exactly isolated threshold

```text
17319661390170597674664379119329139916558985637443041749034808154885215081119653065326105266100757596672 /
17323210971095783496925550366554228993935200352203501108682765732232180990432243675078129175681860616521.
```

Exact safe samples give

```text
first postcarrier cell: Q f-vector (140,400,262)
post-full-disk cell:    Q f-vector (139,397,260).
```

The independent homotopy verifier reconstructs the parent and all four paths, checks all seven carrier derivatives and all thirteen exact thresholds, and separately rebuilds both safe-sample hulls. Thus the deletion is an actual full-row event, not a compact active surrogate.

## Connected positive-volume two-page terminal

The exact boundary comparison gives

```text
removed disk: faces=31, vertices=31, edges=61, Euler=1
added disk:   faces=37, vertices=34, edges=70, Euler=1
common boundary: one cycle of 29 true edges.
```

Both disks are face-connected and have exactly the same boundary. Sequential insertion yields four exact positive-volume stages. The two page vertices are `26063,26064`; the two return vertices are `26065,26066`. Page `26063` has 28 endpoint neighbors, page `26064` has 9, and each return has four neighbors joining both pages. The first two-page volume increment is approximately `0.381291026796657`; the exact return increments are positive (approximately `1.4e-21` and `2.0e-18`). Their literal rational values and all shell cells are in the terminal certificate.

This is a genuine finite-thickness communicating terminal. The returns are deliberately tiny but nonzero and exact; they are not coplanar labels or zero-volume decoration.

## Full inactive and nonincidence separation

All

```text
25,928 x 260 = 6,741,280
```

inactive-row/maximal-face inequalities are represented and exact-positive. The closest inactive row is the deactivated parent row `25976` against face 74, with unit-normal distance

```text
5.855154448554481495830904939326439124057280801008161918822940076235558309585352096164877158624018802e-9.
```

The closest active/nonincident pair is row `25978` against face 29, with exact-positive distance

```text
2.972697721525045233891594265580746615483540957623118701759040944394060534203795793094696221001350776e-18.
```

Additional strict data:

```text
inherited inactive-row lower bound  about 0.35686606957
minimum true-edge length             7.423546049557919e-7
minimum maximal-face normal norm     250079254.90987974.
```

The active/nonincident gap is extremely thin but literal exact-positive. Robustness is therefore certified by the exact common affine family below, not by an unjustified independent-coordinate box.

## Exhaustive full-normal-cone mechanics

Every one of the 260 maximal Q faces, all 139 full vertex tangent cones, and all four components of every one of the 397 true-edge normal cones are audited exactly.

The only positive equilibria are

```text
stable protected 17-gon
[15966,25849,25850,25851,25838,25852,25853,25854,25840,
 25855,25856,25857,25845,25858,25859,25860,25861]
margin 2.51364348...

stable replacement triangle [26042,26057,26064]
margin 0.2078810451...

unique unstable vertex 25840=N3
margin 0.1641081346...

sole saddle edge [25975,26063]
margin 0.0448027698....
```

Global excluded-feature margins are

```text
nonstable face       0.0003011823...
nonunstable vertex   0.0002188307...
nonsaddle true edge  0.0000097937573....
```

Hence the complete own-centred class is strictly `(2,1,1)`.

## Positive noncoincidence family

Apply the exact common affine deformation

```text
A(t)=diag(1+t,1,1),  |t|<=2^-20
```

to all `26,067` rows. It preserves the complete hull incidence and keeps the ordinary centroid exactly zero. After positive-denominator clearing, all 822 selected decisive full-cone signs are linear in `g=(1+t)^2` and remain strict at both rational endpoints. The exact minimum endpoint-to-identity signed ratio is positive and is approximately

```text
0.9981076876232511.
```

Thus the endpoint, target deletion, equilibrium class, and obstruction persist on a nonzero genuine shape interval.

## Exact residual forcing obstruction

The replacement stable face is Q-face index 249:

```text
[26042,26057,26064].
```

Its polar dual vertex is a singleton component with exactly three outgoing true-edge arcs, all exact-positive:

```text
249 -> 65  across [26057,26064], normalized support 0.43046789148323533
249 -> 82  across [26042,26057], normalized support 0.9888609355192184
249 ->250  across [26042,26064], normalized support 0.9981945244306416.
```

The exact rational support numerators and denominators are expanded in `AQ32_G44_TP2R2_R139_dual_component_obstruction.json` and independently recomputed. Positive support on all three incident dual edges makes this polar vertex a strict local radius maximum. Its Q-dual face is therefore stable throughout the complete fixed-incidence/outgoing-sign cell. The protected 17-gon is a distinct stable face, proving

```text
S>=2.
```

This excludes every fixed-cell coordinate or metric polishing that retains the certified adjacency and outgoing signs.

The sole saddle is `[25975,26063]`, with incident faces 115 and 116. The smallest exact connected endpoint disk spanning the replacement stable component to both saddle-side faces is

```text
face indices: 65,82,114,115,116,117,119,123,124,125,126,249,250
(V,E,F)=(15,27,13), Euler=1, one boundary component of 15 edges.
```

That disk is the first genuinely nonrepeating topology beyond the present endpoint.

## Independent verification and watertight meshes

The endpoint verifier imports neither the endpoint generator nor saved topology labels. It reconstructs the authoritative parent from its finite specification, reconstructs all four inserted rows, rediscovers the complete exact hull, recomputes exact moments, every inactive gap, Q/P incidence, every face/vertex/four-component edge cone, the terminal disks, the three-arc theorem, all perturbation signs, deterministic row-table output, and both mesh formats. It returns

```text
INDEPENDENT_AQ32_G44_TP2R2_R139_EXACT_NONWINNER_VERIFICATION_PASS.
```

The separate homotopy verifier returns

```text
INDEPENDENT_AQ32_G44_TP2R2_R139_EXACT_COMMON_HOMOTOPY_PASS.
```

Mesh audits:

```text
Q OBJ/STL: 139 vertices, 274 triangles, 411 mesh edges,
           signed volume 1734.4979094275322, watertight.
P OBJ/STL: 260 vertices, 516 triangles, 774 mesh edges,
           signed volume 0.007347362960967396, watertight.
```

Every mesh edge has triangle incidence exactly two. The Q mesh volume agrees with the exact rational value. The polyhedral true-edge count is 397 for both dual bodies; export-only diagonals are excluded from mechanics.

## Searches used to challenge the result

The following are finite discovery observations, not continuum exclusions:

```text
13-face visibility subset masks                 8,191
nominal strict visibility cells                   127
practical deduplicated geometries                  57
focused two-page A->B trials                    3,000, valid 2,470, winners 0
focused two-page B->A trials                    5,000, valid 4,557, winners 0
best local two-support hard score              -1.0662715648914387e-7
post-page targeted one-support winners            0
six-parameter determinant-one metric searches     4 x 1,200 DE iterations
best target-compatible metric hard score        -0.003440395776136571
metric winners                                    0.
```

A metric trajectory approached a wall but entered replacement class `(3,1,2)`, not a strict target chamber. None of these searches is used as proof; the exact three-arc theorem is the rigorous stopping boundary.

## First nonrepeating continuation

The complete parent 13-face disk and its original pair are gone, so another page attached only to one carrier would repeat the relay. The next admissible move is a connected three-page/second-return, double-octahedral, or stronger positive-volume replacement of the exact endpoint disk

```text
65,82,114,115,116,117,119,123,124,125,126,249,250.
```

It must, in one actual full-supplied-hull event:

1. delete or retopologize stable `[26042,26057,26064]` and saddle `[25975,26063]` jointly;
2. cross at least one of the three certified outgoing stable arcs;
3. preserve the protected stable 17-gon and unique unstable `N3=25840`;
4. suppress every replacement stable, unstable, and saddle birth before both target deaths;
5. give the transverse return macroscopic independent thickness rather than the present ultra-shallow scale; and
6. retain at least four genuine shape variables after the three exact ordinary-moment controls.

## Reproduction

From the unpacked archive:

```bash
python -m pip install -r requirements.txt
./[internal-source-reference].sh
```

Expected terminal markers:

```text
REGENERATE_AQ32_G44_TP2R2_R139_PASS
INDEPENDENT_AQ32_G44_TP2R2_R139_EXACT_NONWINNER_VERIFICATION_PASS
INDEPENDENT_AQ32_G44_TP2R2_R139_EXACT_COMMON_HOMOTOPY_PASS
ALL_AQ32_G44_TP2R2_R139_VERIFIERS_PASS.
```

The final timed clean run exited zero after `1:35.56`, with maximum resident set size `210200` KiB.

## Final research judgment

`AQ32-G44-TP2R2-R139` is the strongest exact finite result completed for this assignment. It advances the authoritative `AQ32-G44-CAP2R119-R136` parent through the demanded multi-support topology on all `26,067` supplied rows, materializes two pages and two communicating returns, deletes the complete certified parent disk and both named carriers, preserves the intended pair, solves all three ordinary moments exactly, and supplies complete incidence, strict mechanics, exact separation, independent endpoint and homotopy verifiers, and watertight meshes. It is not a Gömböc because the Euler-neutral stable–saddle pair is born immediately on `[26042,26057,26064]` and `[25975,26063]`. The exact singleton three-arc theorem—not the finite searches—determines the next topology.
