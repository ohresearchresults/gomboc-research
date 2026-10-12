# figure-0057

AI research report · 2026-08-25 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Simultaneous multi-vertex replacement of the Conway polar chain

## Verdict

No own-centroid strict `(S,U,H)=(1,1,0)` polyhedron was found. The run therefore does not meet the materialized-object acceptance gate. The materialized endpoint that preserves the mechanically distinguished origin is still `(15,21,34)` at its own uniform-volume centroid. The two endpoints with the largest moment displacement are post-wall `(3,1,2)` and `(2,1,1)` bodies, not Gömböcs. No rationalization or winner claim is warranted.

The run nevertheless completed the requested simultaneous replacement experiment: the entire old active chain was removed at once; five polar rows were introduced with independent radial/transverse search freedom; obsolete old rows were permitted to become redundant and were deleted; every accepted topology was rebuilt by exhaustive H-plane triple enumeration; and all maximal faces, vertices, and true edges were audited at both the distinguished origin and the recomputed own volume centroid.

## Incidence discipline and independent verification

All reported bodies have support vector `b=(1,...,1)` and are supplied as `P={x: A x <= 1}`. The primary verifier, `independent_h_verifier.py`, does not infer the primal face lattice from a loose coplanarity grouping. It:

1. enumerates every nonsingular row triple;
2. solves the corresponding plane intersection;
3. tests every half-space;
4. merges only binary-roundoff duplicate vertices;
5. requires exactly three active rows at every vertex;
6. reconstructs every maximal face cycle and every true edge;
7. integrates volume and first moments over the actual face cycles; and
8. classifies every face, vertex, and edge by a complete support test.

Its equality threshold is `2e-10`. Every reported inactive slack exceeds that threshold by at least a factor of about 3,700, and the robust strict body exceeds it by more than `1.2e6`. A second Q-hull/polar implementation (`polar_fast2.py`) independently matches counts, centroid, and equilibrium classes. Finally, `mp_verify_multibulge.py` recomputes all stored active triples, slacks, volume, centroid, and feature signs at 80 decimal digits using the binary64 row coordinates as exact decimal inputs.

## Baseline P60 independently re-audited

The inherited body `P60` was the journal frontier: a robust origin-relative body whose next prescribed operation was this simultaneous chain replacement.

It re-audits as:

| quantity | value |
|---|---:|
| `(V,F,E,C)` | `(116,60,174,348)` |
| volume | `4.579397089857729288...` |
| centroid | `(-0.03255072541373214, -0.007215389256653851, -0.27107677892322448)` |
| centroid norm | `0.27311944573478459` |
| origin class | `(1,1,0)` |
| origin hard margin | `6.658838754205574e-5` |
| own-centroid class | `(15,21,34)` |
| minimum raw inactive slack | `6.891648988980074e-5` |
| minimum vertex separation | `0.005649131587838903` |

The complete reconstructed baseline is included in the handoff rather than assumed from the earlier audit.

## Construction used for the simultaneous replacement

Let `B` be the 59-row body `poly59_edge4857_robust.npz`, and let

`D=(poly59_path_t018.A-B)/0.018`.

The old global descent family is `A_old(t)=B+tD`. At one chosen `t`, rows

`[48,57,58,52,56]`

are removed simultaneously. Relative to P60 this deletes rows

`[48,52,56,57,58,59]`,

because P60 row 59 was the last serial edge patch. Five new polar vertices are then inserted. During search, each new vertex has a local orthonormal frame with one independent radial and two independent transverse coordinates, for 15 free controls. The reusable parameterization is `multibulge_search.py`.

## Result A — strongest robust strict-reference five-vertex body

The best robust endpoint that still preserves the open origin chamber is `conway_5rail_strict_t0256`, at `t=0.0256`. Its five new polar rows are:

```text
(-0.40527608894319744,  1.2335930828739980, 0.18464252214100976)
(-0.39627057390743436,  1.2305024175234116, 0.23238954912498816)
(-0.38669237966542797,  1.2257068945888303, 0.27995728150814810)
(-0.37655301510994726,  1.2192080896672508, 0.32727963773960190)
(-0.36586479644874936,  1.2110099302695998, 0.37429067933305693)
```

They lie at equal angular increments and equal logarithmic radial increments between old rows 53 and 41. All 59 input rows are actual maximal faces; none is redundant.

### Complete audit

| quantity | value |
|---|---:|
| `(V,F,E,C)` | `(114,59,171,342)` |
| Euler check | `114-171+59=2` |
| volume, mp80 | `4.5747008746101791381702765812174377` |
| centroid, mp80 | `(-0.03296324084274712745, -0.00745169578209973944, -0.27063237558242618170)` |
| centroid norm | `0.2727342767791999` |
| origin class | `(1,1,0)` |
| origin hard margin, mp80 | `5.00767469323095997e-5` |
| unique stable face | `o0`, score `+0.007292144441075167...` |
| unique unstable vertex | active rows `(o18,o19,o54)`, score `+0.09144862284104124...` |
| saddle edges | none |
| nearest unwanted vertex | score `-5.00767469323095997e-5` |
| nearest unwanted face | score `-7.592999500314029e-5` |
| nearest edge | score `-2.966854556074963e-4` |
| own-centroid class | `(15,21,34)` |
| own-centroid hard defect | `-0.14342844456444956` |
| minimum raw inactive slack | `2.4388778968386553e-4` |
| minimum vertex separation | `0.00525340110339459` |
| minimum active determinant | `4.871884570421094e-4` |
| minimum face area | `0.007264889048663654` |

Relative to P60, the centroid moves by

`(-0.0004125154290150, -0.0002363065254459, +0.0004444033407987)`,

with displacement magnitude `6.50771912775e-4`. The centroid norm falls by `3.85168955585e-4` (`0.1410%`), while complexity falls by six. The first-moment norm falls by `0.00304466046345` (`0.2434%`). This is a genuine, robust, simultaneous post-chain body, but its own-center mechanics remain far from the target.

Complete artifacts:

- `conway_5rail_strict_t0256_H.txt`: all 59 active H rows and supports;
- `conway_5rail_strict_t0256_V.txt`: all 114 vertices and active triples;
- `conway_5rail_strict_t0256_incidence.json`: every maximal-face cycle, true edge, origin score, and own-centroid score;
- matching NPZ, OBJ, STL, and audit JSON.

## Result B — largest moment displacement, a resolved `(3,1,2)` wall state

At the macroscopic old-row descent `t=1`, an independently controlled five-input bulge produced `conway_5bulge_wall_t1`. Its five input rows are:

```text
(-0.39868749099635653, 1.3640382870831698, 0.028685820642204731)
(-0.43081985303133474, 1.3689972779316475, 0.13748450843799886)
(-0.41462098058668528, 1.2598771015276831, 0.069282686080092942)
(-0.43193445971937977, 1.3686107020169720, 0.13784087077936602)
(-0.35808440886296067, 1.2540647424730609, 0.41605036928637867)
```

Rows `o23,o40,o41,o49,o53` and new row `n2` are redundant and are deleted. The active body has:

| quantity | value |
|---|---:|
| `(V,F,E,C)` | `(102,53,153,306)` |
| volume, mp80 | `3.9130266625362827709325831540320582` |
| centroid, mp80 | `(-0.07044315006437726320, -0.04181997071206995831, -0.21816021691881720065)` |
| centroid norm | `0.23303439142627894` |
| origin class | `(3,1,2)` |
| origin defect | `2.928526371275242e-7` |
| own-centroid class | `(14,19,31)` |
| minimum raw inactive slack | `7.422241155827664e-7` |
| minimum vertex separation | `0.000608267522886764` |

The only positive origin features are:

- intended face `o0`: `+0.01252322470688883`;
- faces `n1`: `+6.380355705856e-9` and `n3`: `+2.928526371275e-7`;
- intended vertex `(o18,o19,o54)`: `+0.39290772884928366`;
- edges `(o25,n3)`: `+9.702027569815e-8` and `(n1,n3)`: `+7.61354048463e-9`.

Its centroid norm is `0.0400850543085` below P60, a `14.6767%` improvement; its first-moment norm is `27.0926%` smaller. However, this gain is primarily enabled by the macroscopic global deformation `t=1`, not by a cavity-only five-row actuator. The state is geometrically well resolved—its inactive slack is thousands of times the equality threshold—but mechanically it is on the wrong side of two real feature walls.

## Result C — cleaner post-transfer `(2,1,1)` branch

A nearby materialized endpoint, `conway_5bulge_pair_t1`, has the five input rows:

```text
(-0.39879827890189320, 1.3643245367446784, 0.02870900685969653)
(-0.43051427831714195, 1.3693339279486185, 0.13703771343234258)
(-0.41477740691192927, 1.2599169379770070, 0.06944922261374037)
(-0.43167328487656600, 1.3689294116575660, 0.13742306308544097)
(-0.35827579654613434, 1.2541179660636852, 0.41562421359177640)
```

The same six rows are redundant: `o23,o40,o41,o49,o53,n2`. Its full audit is:

| quantity | value |
|---|---:|
| `(V,F,E,C)` | `(102,53,153,306)` |
| volume, mp80 | `3.9129874187084340038056131063551244` |
| centroid, mp80 | `(-0.07044890899810857381, -0.04182939291092557914, -0.21816089117437122747)` |
| centroid norm | `0.23303845461278755` |
| origin class | `(2,1,1)` |
| extra stable face | `n1`, `+4.217958140174e-7` |
| sole saddle edge | `(o25,n3)`, `+1.008215761053e-7` |
| unique intended unstable vertex | `(o18,o19,o54)`, `+0.39290772884928366` |
| own-centroid class | `(14,19,31)` |
| minimum raw inactive slack | `7.723242309765974e-7` |
| minimum vertex separation | `0.000607289526848092` |

This is the cleanest topology reached: one stable–saddle Morse pair remains. It is not an open target chamber.

A fifth-active-row control (`conway_5bulge_edgepatch_t1`) inserted the formerly redundant fifth row into the surviving local patch. It changed the counts to `(104,54,156)` but left the extra face score unchanged and increased the saddle score to `2.180253247e-7`. Thus failure was not caused merely by having only four active new rows in Result C.

## Wall and topology transitions

### 1. Remote unstable–saddle birth along the robust five-rail path

Continuing the equal-rail family in `t` reaches a simultaneous mechanical wall at

`t_* = 0.03003400926526...`.

Two independently rooted scores agree within `1.6e-14` in `t`:

- unstable vertex active triple `(o11,o12,o16)`;
- saddle edge incident to rows `(o12,o16)`.

At `t_*-1e-7`, their scores are approximately `-1.12344e-9` and `-6.66747e-9`, and the class is `(1,1,0)`. At `t_*+1e-7`, the scores are positive with the same magnitudes and the class is `(1,2,1)`. The wall is remote from the replaced chain. Therefore a five-row cavity operation cannot continue this global descent by repairing only rows `48-57-58-52-56`.

### 2. Local circuit A in the clean pair state

The true Q-edge `(n3,o25)` is incident to Q facets

`(o25,n3,n4)` and `(o25,n3,n1)`,

so its four-row circuit is `{n1,n3,o25,n4}`. The signed distance of `n3` from the plane `(n1,o25,n4)` is

`-1.2637858038586184e-4`.

Moving toward and through that coplanarity never produces `(1,1,0)`: the body remains `(2,1,1)`, the extra stable face remains `n1`, and the positive saddle transfers from `(o25,n3)` to `(o25,n1)` before/through the diagonal change. At 1% beyond the coplanarity, the stable and saddle scores are about `3.45e-5` and `6.49e-6`.

### 3. Local circuit B and row deletion

The edge `(n1,n3)` is incident to `(n0,n1,n3)` and `(o25,n1,n3)`, giving circuit `{n0,n1,n3,o25}`. The signed distance of `n1` from plane `(n0,n3,o25)` is

`+9.486058141135115e-4`.

Along the direct motion toward that circuit, stability transfers from `n1` to `n3`; then `n1` becomes non-extreme and is deleted. The saddle `(o25,n3)` persists. Again the class remains `(2,1,1)`, so the transition is a transfer, not a cancellation.

Complete sampled states are in `conway_multibulge_circuit_crossings.json`.

## Quantitative obstruction exposed by the five-point experiment

For origin-centered face mechanics, if face row `a_i` is nonstable because row `a_j` witnesses it, then

`a_j·a_i > ||a_i||^2`.

Writing `r_i=||a_i||`, `r_j=||a_j||`, and angular separation `theta_ij`, this becomes

`r_j cos(theta_ij) > r_i`.

Hence witness chains must strictly increase radius. If a chain spans total angle `Theta` in `m` links, concavity of `log cos` gives the necessary condition

`r_end cos(Theta/m)^m > r_start`.

For P60 row `o53` to reach the unique stable row `o0`, the measured data are

`r_start=1.3091013485`, `r_end=1.4701869394`, `Theta=83.92737°`,

which requires at least `m=10` links. Five new vertices cannot supply that full radial witness route by themselves.

At the moment-efficient `t=1` pair state, rows `n1` and `n3` already have radii about `1.44194`, leaving only 1.96% radial headroom to `o0` across about `84.5°`. The same necessary bound requires `57` links. This explains the observed behavior: with only five inputs, the extra stable equilibrium can be transferred between nearly equal-radius rows, but it cannot be carried all the way into the unique stable basin.

This is a necessary-bound argument for this witness architecture, not a proof that every conceivable five-row deformation is impossible. It does sharply explain why the materialized circuits transfer rather than cancel.

## Strongest justified continuation

The next connected architecture should not be another serial edge midpoint and should not be confined to the original six-row cavity. It should be a connected, bifurcated polar patch with:

1. a radial-ascent rail of at least 9 intermediate rows from the `o53` side toward `o0`, with radii chosen to satisfy a strict witness inequality at every link;
2. a second branch that reaches and replaces the remote `(o11,o12,o16)/(o12,o16)` unstable–saddle basin before the global descent crosses `t_*`;
3. at least three independently placed transverse/radial moment-control rows, so the full three-component volume moment has a well-conditioned Jacobian;
4. permission to delete `o42,o25` and any obsolete chain rows when they become redundant; and
5. hard constraints on every maximal face, vertex, and true edge, plus raw inactive slack at least `1e-5` during search.

A practical first implementation is a 12–16-row connected Y-shaped replacement. Even if each added polar row costs roughly six units of primal complexity, it remains comfortably below `C=500` from this branch. The optimization should use continuation in the global moment direction but halt before the remote wall, solve the remote branch and ascent rail simultaneously, and only then resume descent. This directly targets the two independently observed obstructions rather than asking one five-row cavity to solve both.

## Reproducibility bundle

Run:

```bash
python verify_conway_multibulge.py
python mp_verify_multibulge.py
```

The first command reconstructs all five bodies by two independent floating implementations and requires exact agreement of `(V,F,E)`, centroid, and origin/own equilibrium classes. The second recomputes the stored binary64 geometry at 80 decimal digits. The supplied log ends with `ALL CHECKS PASSED`.

The ZIP bundle contains the complete H/V data, maximal-face cycles, true-edge lists, all feature scores, construction scripts, wall/circuit records, independent verifiers, and OBJ/STL exports.

## Uncertainty and claim boundary

- The coordinates are binary64, not rational or algebraic.
- The 80-digit check validates the geometry determined by those decimal coordinates; it is not a formal interval proof over an uncertainty box.
- The strict-reference body has comfortable positive separation from all tested numerical tolerances, but no exact coefficient-space perturbation radius was derived because it is not an own-centroid candidate.
- No body in this handoff satisfies the target at its own centroid, so none should be rationalized or presented as a homogeneous polyhedral Gömböc.

## Artifact index

- Complete handoff ZIP (`conway_multibulge_handoff.zip`) — all 57 files, including source seeds, H/V data, full incidence, feature scores, verifiers, logs, OBJ/STL, and SHA-256 manifest.
- ZIP SHA-256 (`conway_multibulge_handoff.zip.sha256`) — `66cae879451bb59662f7794f61c8e45acbf7d89f597fc5ae37ebba8c9d2e55c6`.
- Standalone report (`conway_multibulge_report.md`).
- Robust strict-reference endpoint: NPZ (`conway_5rail_strict_t0256.npz`), H matrix (`conway_5rail_strict_t0256_H.txt`), V matrix (`conway_5rail_strict_t0256_V.txt`), complete incidence and scores (`conway_5rail_strict_t0256_incidence.json`), OBJ (`conway_5rail_strict_t0256.obj`), STL (`conway_5rail_strict_t0256.stl`).
- Moment-efficient wall endpoint: NPZ (`conway_5bulge_wall_t1.npz`), H matrix (`conway_5bulge_wall_t1_H.txt`), complete incidence (`conway_5bulge_wall_t1_incidence.json`), OBJ (`conway_5bulge_wall_t1.obj`), STL (`conway_5bulge_wall_t1.stl`).
- Clean `(2,1,1)` pair endpoint: NPZ (`conway_5bulge_pair_t1.npz`), H matrix (`conway_5bulge_pair_t1_H.txt`), complete incidence (`conway_5bulge_pair_t1_incidence.json`), OBJ (`conway_5bulge_pair_t1.obj`), STL (`conway_5bulge_pair_t1.stl`).
- Verification: independent exhaustive H verifier (`independent_h_verifier.py`), two-route verification driver (`verify_conway_multibulge.py`), verification log (`verify_conway_multibulge.log`), 80-digit verifier (`mp_verify_multibulge.py`), 80-digit audit JSON (`conway_multibulge_mp80.json`).
- Transition evidence: wall roots and witness-chain bounds (`conway_multibulge_walls.json`), sampled circuit crossings (`conway_multibulge_circuit_crossings.json`), 15-DOF reusable search parameterization (`multibulge_search.py`).

## Change relative to the supplied journal

This continuation replaces the prescribed five-row polar chain in one operation rather than adding another serial edge point; materializes a robust 59-face strict-reference body; reaches and resolves the macroscopic post-wall topology down to one stable–saddle pair; identifies a separate remote unstable–saddle wall that the local cavity cannot control; and derives a quantitative radial-witness lower bound showing why five replacement rows transfer the remaining stable equilibrium rather than carrying it to the unique stable basin. The resulting next architecture is a connected 12–16-row bifurcated rail, not another five-row cavity optimization.
