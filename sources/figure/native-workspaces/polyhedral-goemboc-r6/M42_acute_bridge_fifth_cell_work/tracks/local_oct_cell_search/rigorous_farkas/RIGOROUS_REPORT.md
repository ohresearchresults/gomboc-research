# Rigorous first-order certificates

## Result

The three previous numerical Farkas observations now have reproducible
rigorous replacements:

| System | Arithmetic | Support | Certified conclusion |
|---|---|---:|---|
| row54 shared 3D | exact rational AD | 4 rows | `A^T y = 0` exactly, `y>0`, `b.y = -87.0567876011...` |
| row54 full 13D | exact rational AD | 14 rows | `A^T y = 0` exactly, `y>0`, `b.y = -3.9185958887276e-5` |
| core beta vs anti-edges | directed rational interval AD | 19 rows | Krawczyk inclusion proves exact positive dual; `b.y` is strictly negative on its entire enclosure |

All three independent verifier programs return `PASS`.

These are rigorous statements only about explicitly defined fixed-sign,
fixed-cell affine first-order models.  They are not actual-cell LP roots,
nonlinear continuation obstructions, or global nonexistence theorems.

## Frozen geometry

The certificate directory contains immutable copies of both relevant row54
realizations:

- `fixed_cell.csv` and `fixed_cell_faces.json`: the row54 far carrier at which
  the first-order Jacobian is taken;
- `actual_endpoint.csv` and `actual_endpoint_faces.json`: the nonlinear
  shared-3D endpoint from the preceding search.

SHA-256 hashes of all four files are embedded in
`row54_shared_exact.json` and rechecked by
`verify_exact_shared_certificate.py`.

The literal frozen hashes are:

```text
611e8e57e2d8986f410894f67f20ffd1c07dc378a49218f5576cf350676ab004  fixed_cell.csv
eae845207e0c293b5f15b35f651428caceea119bd3c33641715ea44197ce1e38  fixed_cell_faces.json
be25a005b5356102e474bdc6646fa3efe45df27e44b010c9da81e7acee8c53c2  actual_endpoint.csv
0a587670fdc836f486177475066951475384cd3030298fabb87e13bdc0542034  actual_endpoint_faces.json
3619a51daacb422b3908fa2f0a4a4343fe03fd99ea12e362bf8fb53535ee385d  input_rows_common_lattice.csv
0626ebce5e9a8f7d5fc4b75de5171d1c752b1808934f19721e771e4e5d74bed0  face_cycles.json
```

The last two hashes identify the exact common-lattice core source and its face
lattice.  They are embedded in the interval core certificate and rechecked by
its verifier.

Fresh-hull reconstruction verifies:

| Cell | f-vector | Class | Features | Forced rails |
|---|---|---|---|---|
| fixed cell | `(61,162,103)` | `(2,2,2)` | `S[7,8,246]`, `U8,U54`, `H67,H910` | all present |
| actual endpoint | `(61,162,103)` | `(2,2,2)` | `S[245,8,246]`, `U8,U1`, `H67,H910` | all present |

Thus the frozen endpoint/faces record the actual transfer found by the
nonlinear search, while the LP certificate is explicitly rooted at the frozen
fixed cell.

## Exact primitive model

The normalized mechanics contain square roots and, in nearly parallel edge
stars, severe cancellation.  The row54 exact systems therefore use selected
sign-equivalent primitive functions evaluated by forward AD over
`fractions.Fraction`:

- topology: `n.(p_face-p_row)` with the exact oriented raw face normal;
- vertex: `-(p_i-C).(p_j-p_i)`;
- edge `t`: `-(p_i-C).d`;
- edge `1-t`: `|d|^2+(p_i-C).d`;
- beta1: `q_num.(n2 x (n1 x n2))`;
- beta2: `q_num.((n1 x n2) x n1)`;
- stable foot: the oriented raw foot-in-polygon numerator multiplied by
  positive `|n|^2`.

Decimal strings in `fixed_cell.csv` are interpreted as exact rationals.  The
13-dimensional chart is also rational: `q246` has three standard coordinate
directions; rows `54,6,7,9,10` use the exact in-base directions `p1-p0` and
`p2-p0`.

Every inequality is placed in good-positive form.  Target rows request
`g_0 + Dg*x >= 10^-6`; guard rows request `g_0 + Dg*x >= 0`.  Equivalently,
the stored system is

```text
A x <= b.
```

For the complete systems each row is multiplied by an exact positive rational
constant selected from its exact coefficient magnitudes.  This changes neither
the inequality nor feasibility.

The Farkas check is elementary: if `y>=0`, `A^T y=0`, and `b^T y<0`, any
hypothetical `A x<=b` would imply

```text
0 = (A^T y).x <= b^T y < 0,
```

a contradiction.

## Exact row54 shared-3D certificate

Four exact target gradients are first computed for deaths of
`S[7,8,246]`, `U54`, `H67`, and `H910`.  Exact rational Gaussian elimination
constructs their four right-inverse actuators.  The shared basis is

```text
S actuator, U54 actuator, H67 actuator + H910 actuator.
```

The selected four inequalities and exact normalized dual weights are:

| Primitive row | `y` |
|---|---:|
| `U54-death` | `0.011862784189759872...` |
| `H67-death` | `0.5935048103734714...` |
| topology `f15`, row `8` | `0.38744448526524966...` |
| anti-edge `263-264:c3` | `0.0071879201715190615...` |

The serialized weights are exact fractions with sum one.  Direct fraction
arithmetic gives every component of `A^T y` equal to the exact integer zero and

```text
b^T y = -87.05678760114169...
```

The magnitude is representation/row-scale dependent; its strict sign is the
certificate.

Artifacts:

- `rational_shared_certificate.py`
- `row54_shared_exact.json`
- `verify_exact_shared_certificate.py`
- `row54_shared_exact_audit.json`

The verifier does not merely reread the stored matrix.  It rebuilds the
rational chart, centroid, normals, primitive values, exact Jacobian, target
right inverse and shared basis, then checks that the rebuilt `A,b` equal the
serialized fractions before checking the dual.

## Exact row54 full-13D certificate

The generator constructs all four targets and all 6,301 guards, for 6,305
exact primitive rows.  Floating-point HiGHS is used only to nominate a sparse
support.  No floating result is used in the proof.  The nominated 14 by 13
matrix is rebuilt over rational numbers; its one-dimensional nullspace is
computed by exact Gaussian elimination.

The 14 strictly positive support rows are:

```text
target:S[7,8,246]-death
target:U54-death
guard:topology:f11:row7
guard:topology:f16:row198
guard:topology:f16:row246
guard:U8:to7
guard:antiface:f4:c0
guard:antiface:f13:c1
guard:antivertex:v1:to54
guard:antivertex:v10:to11
guard:antiedge:8-246:c2
guard:antiedge:246-264:c2
guard:antiedge:262-263:c2
guard:antiedge:263-264:c3
```

Exact fraction arithmetic gives

```text
sum(y) = 1
A^T y = (0,...,0) exactly
b^T y = -0.000039185958887276356...
```

Only `S` and `U54` target rows are needed; the saddle targets can be deleted
and the selected primitive subsystem is still infeasible.

Artifacts:

- `rational_full13_certificate.py`
- `row54_full13_exact.json`
- `verify_exact_full13_certificate.py`
- `row54_full13_exact_audit.json`

The verifier parses each of the 14 names and independently reconstructs that
primitive, its derivative, exact positive row scale, `A`, and `b` before
checking the stored dual.

## Core beta certificate with analytic normalization

### Why raw exactification alone was insufficient

The core reduced system contains beta1 death for `H(229,247)` and 162 fixed
anti-edge witnesses.  Replacing every normalized component by only its raw
sign numerator yields a different affine extrapolation.  That raw rational LP
is feasible: its normalized dual minimum is

```text
+0.005058554967169052.
```

This diagnostic is stored in `core_beta_exact.json` with
`certificate_pass=false`.  It is not a contradiction.  Multiplication by a
positive coordinate-dependent normalization preserves signs of the nonlinear
functions, but it does not preserve their affine linearizations away from a
zero wall.  Therefore the old normalized FD certificate could not honestly be
renamed an exact raw-sign certificate.

### Analytic interval replacement

`interval_core_beta_certificate.py` instead implements the original normalized
edge functions analytically:

```text
t, 1-t, beta1/|q|, beta2/|q|
```

with unit incident normals.  All rational operations use exact interval
endpoints.  Square roots are enclosed by integer-square-root lower and upper
bounds on a 90-decimal rational grid.  Forward interval AD therefore encloses
the exact value and all 18 analytic partial derivatives; no finite difference
is used.

The midpoint LP nominates 19 rows.  Let

```text
M = [ A_support^T ]
    [      1^T    ],       c = (0,...,0,1).
```

A rationalized numerical inverse is used only as a Krawczyk preconditioner.
Directed interval arithmetic proves strict inclusion of `K(X)` in the
interior of a positive box `X`.  Hence the exact algebraic matrix has a unique
dual `y` in that box satisfying `A^T y=0` and `sum(y)=1`.  The sharper
`K(X)` enclosure is strictly positive componentwise, and interval evaluation
gives

```text
b^T y in
[-0.009100078605714657, -0.009100078605713246].
```

The upper endpoint is negative, completing the rigorous Farkas contradiction.

The support comprises beta1 death and these 18 anti-edge witnesses:

```text
0-54:c3, 54-258:c3, 69-228:c2, 198-224:c2, 198-246:c2,
224-229:c3, 224-230:c3, 224-231:c3, 224-241:c2,
224-257:c3, 224-258:c2, 228-229:c2, 228-235:c2,
228-247:c3, 228-248:c3, 229-230:c0, 247-248:c0,
257-258:c0.
```

This analytic calculation also exposes why the old finite-difference Jacobian
was not certifiable as written.  For example, the analytic derivative row for
`224-258:c2` has entries as large as `1.06e7`; central-difference maximum error
varies from about `53` at `h=1e-6` to `520` at `h=1e-7` and `4686` at
`h=1e-8`.  The interval certificate replaces, rather than blesses, those FD
entries.

Artifacts:

- `interval_core_beta_certificate.py`
- `core_beta_interval.json`
- `verify_interval_core_beta.py`
- `core_beta_interval_audit.json`

The independent verifier rebuilds all 163 analytic interval rows, selects the
frozen 19 names, repeats the Krawczyk solve, verifies that the serialized
outward-rounded intervals contain the reconstruction, and rechecks positivity
and the strict negative upper bound.

## Reproduction

From `M42_acute_bridge_fifth_cell_work`:

```bash
bash tracks/local_oct_cell_search/rigorous_farkas/RUN_ALL.sh
```

A clean-room regeneration completed with exit code zero.  Its complete
transcript is `CLEAN_ROOM_RUN.log`; the literal final line is:

```text
ALL RIGOROUS FIXED-CELL FIRST-ORDER CERTIFICATES PASS
```

The regenerated shared, full-13D and core audits all report `status: PASS`,
all of their individual checks are true, and the six regenerated source/face
hashes equal the literals above.

The two core interval passes are intentionally slow because both reconstruct
all 163 normalized analytic rows with directed 90-digit rational bounds.
Typical total runtime is several minutes.  The rational row54 certificates and
verifiers complete in seconds.

## Scope

- The row54 exact certificates are exact for the stated rational chart,
  frozen decimal-as-rational coordinates, fixed face lattice, fixed selected
  sign witnesses, primitive definitions and `epsilon=10^-6` affine
  first-order request.
- The core certificate is an interval proof for the exact algebraic normalized
  functions, fixed face lattice and fixed 18 anti-edge witness rows at the
  exact common-lattice endpoint.
- Positive exact row rescaling is used only where stated and preserves each
  affine inequality.
- The actual endpoint/faces are frozen and fresh-audited, but they are not the
  root of these LPs.
- None of the certificates rules out arbitrary nonlinear paths after topology
  changes or motions outside the chosen local coordinate families.
