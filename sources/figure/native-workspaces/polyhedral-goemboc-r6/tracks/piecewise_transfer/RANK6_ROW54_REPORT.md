# Rail-valid row-54 rank-5/6 cancellation report

## Scope

This track analyzes the audited cells `row54_endpoint_rebuilt` and
`row54_far_rebuilt`.  Both have fresh f-vector `(61,162,103)`, class `(2,2,2)`,
all 61 rows active, and all 37 forced rail edges present.  Their requested hard
margins are respectively `0.0591924051` and `0.0517894969`.

The desired strict class is `(1,1,0)`: only the enlarged base is stable, only
row 8 is unstable, and there are no saddle edges.  Four present defects are
therefore cancelled: the non-base stable face near row 246, `U54`, `H(6,7)`,
and `H(9,10)`.  A fifth wall is the tightest protected nonstable face in the
fixed cell.

## Selected walls

| Cell | Extra stable death | Vertex death | Saddle deaths | Fifth protected wall |
|---|---|---|---|---|
| endpoint | `S[245,8,246]`, component `245→8` | `U54→1` | `H67:t`, `H910:1-t` | `S-[247,228,258]`, component `247→228` |
| far | `S[7,8,246]`, component `8→246` | `U54→1` | `H67:t`, `H910:1-t` | `S-[246,8,264]`, component `246→8` |

The numerical scan uses the eight projective/trace-free-metric coordinates.
Raw QR gives sparse rank witnesses `[0,4,7,1,6]` for endpoint and
`[0,4,1,7,6]` for far.  The nonlinear five-control solve uses the five right
singular row-space directions, avoiding an arbitrary sparse subchart with no
finite root.

## Numerical events and blockers

Endpoint has a genuine common five-wall root:

* chart coordinates
  `(-0.104798506,-0.135429194,-0.023171945,1.118788879,-0.178731008)`;
* maximum wall residual `5.53e-14`;
* minimum projective denominator `0.808748`;
* fresh f-vector and maximal-face cell remain exactly `(61,162,103)` and the
  supplied fixed face set.

That root is not guarded.  The first extra event occurs at path fraction
`0.617084`: `S-[7,8,245]` and `H-(8,245)` cross together.  Later paired births
are `U10/H(10,11)` at `0.8843`, `U6/H(5,6)` at `0.9763`, and
`U1/H(1,54)` near `0.9904`.

Far has no accepted numerical common five-wall root in the same projective
family: the best run retains maximum residual `3.588e-6`, and the direct path
to that minimizer hits an unrelated fixed-ledger saddle singularity at
fraction `0.73333`.  Its earliest additional crossing is
`H-(8,246):beta1` at fraction about `0.03667`.

For the selected sixth walls the numerical `6x5` systems have rank five and
left-null residual below `1e-12`.  The affine incompatibilities are
`0.00353891` (endpoint) and `0.00376498` (far).  Large local responses on rail
rows do not yield an event: for example endpoint `row247:z` has response
`53.73`, but loses the rails and stalls at residual `1.68e-4`.

One rail-safe remote column, endpoint `row11:base_v`, does solve the six scalar
equations: its maximum residual is `4.39e-13`, minimum projective denominator
is `0.7771`, and all 37 forced rails survive.  It is **not** an event in the
explicit source cell.  The one-sided fresh hull changes from `(61,162,103)` to
`(61,177,118)`, the fixed maximal-face set fails, and the fresh class remains
`(2,2,2)`.  Thus the artifacts distinguish three statements:

1. an exact local five-control affine obstruction;
2. an algebraic six-scalar shared root after adding `row11:base_v`;
3. no accepted six-wall shared event in the original fixed rail cell.

The separate intrinsic-actuator audit rules out a tangent-convention artifact.
It moves rows `11`, `54`, or `1` within the source base plane *before* the
projective map, so base coplanarity is preserved identically.  The best two
floors are `2.02152e-5` (`row54:base_u`) and `2.02155e-5`
(`row54:base_v`); row 1 is similar and row 11 stalls at `2.278e-3`.  Every
tested intrinsic endpoint keeps 37/37 rails but loses the fixed cell (typically
f-vector `(60,160,102)`).  None is an accepted fixed-cell event.

## Exact rational theorem

`rank6_row54_exact_affine.py` reads every finite CSV decimal as a `Fraction`
and uses the supplied fixed maximal-face cycles, oriented-volume centroid, and
explicit zero-equivalent rational wall functions.  Its five controls are the
sparse QR projective generators listed above.  The sixth actuator moves row 54
along the exact base-plane tangent

`n_base × (q1-q0)`.

For both cells it proves exactly:

| Exact statement | endpoint | far |
|---|---:|---:|
| `rank(G5)` | 5 | 5 |
| `rank(G6)` for six walls and five controls | 5 | 5 |
| `rank([G6|f])` | 6 | 6 |
| `rank(G6 + row54 tangent column)` | 6 | 6 |
| `log10(abs(lambda^T f))` | 759.679 | 816.841 |
| `log10(abs(lambda^T actuator))` | 758.952 | 815.414 |
| `log10(abs(det G6x6))` | 2.32738 | 3.82957 |
| exact inequality-Farkas trust radius | `1/5` | `1/100` |
| `log10(abs(mu^T b))`, with `mu>0` and negative sign | 440.481 | 164.150 |

The exact primitive integer vector `lambda` satisfies `lambda^T G6 = 0` and
`lambda^T f != 0`, so no increment in the explicit five-control first jet
solves all six affine wall equations.  The row-54 base tangent has nonzero
`lambda` response and makes the six-control gradient nonsingular.  This is an
exact rank lift only.  The endpoint algebraic root found with a different
actuator (`row11:base_v`) lies outside the fixed cell, so it does not strengthen
the exact theorem into a fixed-cell existence result.

The exact file also contains genuine inequality-form Farkas certificates, not
only affine equalities.  For endpoint, the positive dual support uses the
necessary rows `U54<=0`, `H67<=0`, the first crossed guard, and three sides of
the box `abs(control)<=1/5`.  For far it uses `U54<=0` and five sides of the
box `abs(control)<=1/100`.  In each case the recorded primitive multiplier is
strictly positive, annihilates `A` exactly, and has `mu^T b<0`; hence even that
necessary linearized subset is infeasible throughout the stated trust box.

## Reproduction

```bash
python tracks/piecewise_transfer/rank6_row54_rail_scan.py
python tracks/piecewise_transfer/rank6_row54_intrinsic_actuator.py
python tracks/piecewise_transfer/rank6_row54_exact_affine.py
python tracks/piecewise_transfer/verify_rank6_row54.py
```

The full numerical scan is intentionally slower because each proposed event
is rebuilt with Qhull and audited against the 37 forced rails.  The exact
certificate and verifier are fast and deterministic.  The intrinsic audit is
also nonlinear and therefore slower.
