# Reconstructed supporting shell and exact rank-five obstruction

## Result

The lost supporting-shell track is reconstructed from the authoritative fifth-cell lattice.  The reconstruction is exact:

- project rows `231..246` orthogonally onto
  `100 x + 20 y - 6 z = 3700`;
- replace row `228` by the rational actuator endpoint `(-19,-35,-12)`;
- rebuild the actual convex hull and its ordinary-volume centroid.

`rank5_exact_reconstruction.py` uses Qhull only to propose maximal-face cycles.  It then checks every supporting-plane sign, exact coplanar set, true-edge incidence, oriented face-fan mass, centroid, and every S/U/H component with `Fraction` arithmetic.

The exact endpoint is

```text
(V,E,F) = (61,150,91)
(S,U,H) = (3,4,5)
```

Its equilibria are exactly:

```text
stable:
  [228,254,255]
  [228,264,246]
  [0,1,...,16]                 protected base

unstable:
  8                            protected
  228, 231, 246

saddle:
  (8,246)
  (228,254), (228,255)
  (231,247)
  (236,237)
```

Thus the finite row-228 actuator really restores the intended base and `U8`, but it does so only after producing the stated five-feature shell/star band.

## Explicit five-control template

The exact first-jet audit fixes the actual cell above and uses five rational controls:

```text
r228: row 228 along q* - q_original
r229: row 229 along (41,-16,2)
r254: row 254 along (-18,-36,-9)
r255: row 255 along (-18,-36,-9)
t231: row 231 along (-24,132,40)
```

The last direction is exactly tangent to the shell plane.

`rank5_exact_jacobian.py` forward-differentiates the oriented volume, ordinary centroid, face-foot numerators, vertex supports and saddle components with Fraction-valued jets.  The five designated face/vertex cancellation gradients have exact rank five.

Adding the selected sixth `H(8,246)` wall produces:

```text
rank(gradient rows)             = 5
rank([gradient | wall value])   = 6
```

The JSON contains a primitive exact left-null vector `lambda` satisfying

```text
lambda^T gradient = 0
lambda^T wall_value != 0.
```

Therefore no increment in this explicit five-control first jet places all six selected walls at one common event.

There is also a genuine inequality-form Farkas certificate in the explicit trust box `|control_k| <= 10`.  A necessary six-inequality subsystem uses the second stable face, `U228`, the branch killing `U246` through row `231`, protected `U8`, and two box sides.  The stored primitive multipliers are all strictly positive and satisfy exactly

```text
lambda^T A = 0
lambda^T b < 0.
```

Hence that complete linearized target branch is infeasible in the stated box.  It requires at least a sixth independent control or a different witness branch.

This is a local theorem for the explicitly listed actual cell, controls and witness choices.  It is not a global nonexistence statement; in particular the alternative `H(8,246)` cancellation through `1-t` remains a distinct branch.

## Actual-hull searches

Every numerical proposer rebuilds the hull and own centroid on every evaluation.  The free searches over four, six and eight local rows found no strict target.  The best completed search currently has hard margin about `-0.32446`, with protected base and `U8` still positive; the residual again transfers to a new local star.  The rational integral-star search also found no target.

The search JSON files are retained as finite falsification, not as proof.

## Reproduction

From the project root:

```bash
python tracks/piecewise_transfer/verify_rank5.py
```

Expected final line:

```text
ALL_EXACT_RANK5_SHELL_AND_FARKAS_VERIFIERS_PASS
```
