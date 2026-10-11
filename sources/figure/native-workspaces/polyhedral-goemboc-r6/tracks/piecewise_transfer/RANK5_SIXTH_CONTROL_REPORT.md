# Sixth support-valid control on the reconstructed rank-five shell

## Verdict

There is a genuine sixth mechanical control in the strict reconstructed
supporting-shell cell:

```text
t246: move row 246 along (-7, 8, -90).
```

It is exactly tangent to the shell plane because

\[
(100,20,-6)\cdot(-7,8,-90)=0.
\]

This is not a formal rank lift.  At each of the two one-sided parameters
`t246 = +/-1/900`, the maximum physical coordinate displacement is exactly
`1/10`.  Fresh actual-hull reconstruction followed by exact support-plane,
centroid, mechanics and incidence checks gives, on both sides,

```text
(V,E,F) = (61,150,91)
(S,U,H) = (3,4,5)
base stable = true
U8 unstable = true
forced rails = 37/37
```

Adding this control makes the six selected cancellation gradients exactly
rank six.  Nevertheless it does not produce a guarded physical event.  The
unique affine six-wall root has maximum coordinate displacement
`58.625008239368796`, more than 586 times the physical trust radius.  A fresh
hull at that root is proposed numerically and then has every support plane,
ordinary centroid and mechanical sign rebuilt exactly.  It has
`(V,E,F)=(24,65,43)`, loses the base and U8, and retains only 20 of the 37
forced rails.

More decisively, the six necessary death inequalities themselves have a
literal rational Farkas obstruction in

\[
\|D c\|_\infty\le\frac1{10}.
\]

After exact stationarity repair using only already-present physical trust
rows, the certificate satisfies

\[
y\ge0,\qquad A^T y=0,\qquad
b^T y=-0.17565499476121785\ldots<0.
\]

Thus this explicit rank-six chart contains no guarded shared event for the
named branch inside the physical trust box.

## Six-control chart

The first five directions are the reconstructed exact chart:

```text
r228: row 228 along q* - q_original
r229: row 229 along ( 41,-16,  2)
r254: row 254 along (-18,-36, -9)
r255: row 255 along (-18,-36, -9)
t231: row 231 along (-24,132, 40)
```

The added `t246` direction is primitive integral and shell tangent.  Both
`t231` and `t246` therefore preserve the intentional 16-gon support plane to
first order and at every finite parameter in their affine family.

The selected positive walls at the seed are:

1. `S[228,254,255]` through edge component `(255,228)`;
2. `S[228,264,246]` through edge component `(246,228)`;
3. `U228` through neighbour `254`;
4. `U231` through neighbour `229`;
5. `U246` through neighbour `231`;
6. `H(8,246)` through component `t`.

Forward differentiation includes the ordinary-volume centroid motion.  The
resulting 6-by-6 Fraction matrix has nonzero exact determinant (its absolute
decimal logarithm is about `23.186`), hence exact rank six.

## Formal root versus actual hull

Solving the six affine wall equations exactly gives the parameter vector

```text
(2.104368977457225,
 0.1447202933182941,
 1.6268075184825934,
 1.6284724510935777,
 0.2484745346007662,
 0.2731448962527770).
```

The values above are only readable decimals; the JSON stores every parameter
and moved coordinate as a rational number.  Row 228 and the two star rows must
move by roughly 59 physical coordinate units.  Rebuilding the hull rather
than evaluating the frozen cell, then exactifying all proposed support planes
and recomputing its centroid and mechanics with Fractions, gives:

```text
(V,E,F) = (24,65,43)
(S,U,H) = (3,5,6)
base face present = false
U8 unstable = false
forced rails = 20/37
```

Therefore the formal rank-six root is not an actual-cell event.

## Exact physical-trust blocker

For the six death jets, write the necessary system as

\[
v_i+g_i c\le0\quad(i=1,\dots,6),
\qquad |Dc|\le\frac1{10}.
\]

Here `D` is the literal 18-by-6 map from control parameters to the Cartesian
coordinates of rows 228, 229, 254, 255, 231 and 246.  A row-scaled
revised-simplex solve locates a sparse nonnegative dual support.  It is not
used as proof.  The exactifier then:

1. rebuilds the supported wall gradients and physical rows as Fractions;
2. converts each positive locator weight to its exact finite-decimal rational;
3. cancels all six stationarity residuals exactly with signed physical trust
   rows, not with an auxiliary coefficient box;
4. evaluates the repaired rational right-hand side.

The repaired RHS remains `-0.17565499476121785...`, so this necessary
subsystem is exactly infeasible.  Adding base, U8, rail or other support guards
cannot restore feasibility.

This is a local first-order theorem for the explicit six controls, named wall
branch and physical radius `1/10`.  It is not a global obstruction to other
sixth controls or other wall-component branches.

## Artifacts

- `rank5_sixth_control.py`: exact jets, two-sided actual-hull probes, affine
  root audit and exact physical-trust Farkas construction.
- `rank5_sixth_control.json`: materialized determinant, rational root, fresh
  hull/rail audits and exact certificate.
- `verify_rank5_sixth_control.py`: clean regeneration and literal assertions.

Run from the project root:

```bash
python tracks/piecewise_transfer/verify_rank5_sixth_control.py
```

Expected final line:

```text
ALL_EXACT_RANK5_SIXTH_SUPPORT_CONTROL_VERIFIERS_PASS
```
