# Exact C5--C17 continuation and Gordan-support break

## Result

The normalized physical path

\[
q_{255}(t)=q_{255}(0)+t(-1/2,-1,-1/4)
\]

continues from the certified C4-far point `t=-1/10` through thirteen ordered
exact support circuits, C5 through C17.  Every open chamber, wall, hull, mass,
centroid and mechanics ledger is rebuilt from the 119 exact rows.  Throughout
the passage all 61 rows remain active, the protected base remains stable, U8
remains unstable, and all 37 forced rails remain present.

C17 is the decisive circuit `{228,254,255,256}`.  Its exact rational root is
approximately `-0.537902645984612`; the wall has f-vector `(61,149,90)`.  The
far rational point `t=-11/20` is again `(61,150,91)`, mechanics class `(2,5,5)`.
The flip removes edge `(228,255)` and adds `(254,256)`.  Consequently the old
killed face `S[228,254,255]` and killed edge `H(228,255)` are both absent from
the new hull.

This is exactly the required escape from the fixed-cell Gordan obstruction.
At `t=-1/10` the positive exact circuit has the named seven-row support

```text
S[228,264,246], U228, U231, U246, H(8,246), H(228,254), no-rebirth S[228,254,255].
```

Immediately before C17 a guard-dependent Gordan circuit still exists.  After
C17 both possible no-rebirth carriers are no longer mechanical constraints.
The eight residual death gradients have exact rank six and admit the explicit
strict direction, in controls `[r228,r229,r254,r255,t231,t246]`,

```text
[-107/1000, 83/2000, -1, 1, 153/1000, -267/1000].
```

All eight exact directional derivatives are strictly negative.

## Ordered support passage

The exact JSON ledger contains every rational root and its rational isolating
bracket.  The decimal locators and flips are:

| Event | Decimal root | Removed edge | Added edge |
|---|---:|---:|---:|
| C5 | -0.131705008518342 | `(69,253)` | `(252,255)` |
| C6 | -0.169907064091626 | `(54,258)` | `(255,259)` |
| C7 | -0.263888005595115 | `(54,259)` | `(255,260)` |
| C8 | -0.275761918857556 | `(54,260)` | `(72,255)` |
| C9 | -0.282675775406124 | `(69,252)` | `(251,255)` |
| C10 | -0.372219818627720 | `(72,260)` | `(255,261)` |
| C11 | -0.395452229229348 | `(72,261)` | `(73,255)` |
| C12 | -0.420290016340423 | `(73,261)` | `(14,255)` |
| C13 | -0.440906625095795 | `(14,261)` | `(13,255)` |
| C14 | -0.499789182013878 | `(13,261)` | `(255,262)` |
| C15 | -0.501431861490774 | `(69,251)` | `(250,255)` |
| C16 | -0.520972458562379 | `(13,262)` | `(12,255)` |
| C17 | -0.537902645984612 | `(228,255)` | `(254,256)` |

For every chamber, all 10,529 strict support inequalities recover the two
adjacent exact circuit roots as the literal chamber endpoints.  Exact Sturm
audits of the base face components and U8 vertex supports exclude any hidden
mechanics zero throughout every chamber.  Each wall is also rebuilt exactly.

## Material residual descent

From `t=-11/20`, take the exact control step `1/125` in the displayed strict
direction.  The endpoint stays `(61,150,91)`, class `(2,5,5)`, and all eight
residual feature values decrease strictly.

The whole segment, not merely its endpoints, is certified.  For every old
maximal face and every outside row, its oriented support determinant is an
exact cubic in the segment parameter.  All four exact Bernstein coefficients
are strictly inward for all 10,529 inequalities.  Exact planarity identities
hold for every face vertex.  Separate rational-function Sturm audits prove the
base and U8 mechanics guards remain strictly positive over the complete
segment.

## Verification

Run:

```bash
python tracks/piecewise_transfer/verify_rank5_circuit_escape_continuation.py
```

Expected marker:

```text
VERIFIED_EXACT_RANK5_C5_TO_GORDAN_BREAK
```

The verifier regenerates the package, checks every exact determinant root and
bracket, chamber endpoint, wall and material cell, the initial Gordan
stationarity, C17 combinatorics, rank-six strict direction, complete segment
certificates, exact coordinate files and SHA-256 manifest.
