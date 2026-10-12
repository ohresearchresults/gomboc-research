# figure-0121

AI research report · 2026-08-27 UTC

---

# Literal verdict

**NO — I did not obtain a strict own-centroid `(S,U,H)=(1,1,0)` polyhedron.**

The strongest completed construction is nevertheless a literal finite, exact, genuinely fan-changing Minkowski sum. It is an own-centred strict `(2,2,2)` body with a new 49-face common normal fan, rather than the nine-face same-fan P9 fallback. One extra stable face, one extra unstable vertex, and two saddle edges survive with substantial positive margins. This is therefore an open Euler-neutral obstruction, not a numerical wall or an incidence-tolerance artefact.

The exact mathematical state and mixed-polynomial computation were completed. Packaging remains incomplete in three respects: the new endpoint was not exported to final human-readable H/V CSV tables, the edge portion of the nonzero interval perturbation audit did not finish, and I did not complete a clean-room verifier or OBJ/STL for the new endpoint. Those omissions mean this handoff does **not** satisfy the assignment’s full artifact contract, although the exact construction and exhaustive pointwise audit are preserved in the files below.

## What changed relative to the supplied journal

The inherited decomposition used four asymmetric rational summands `B,C1,C2,C3` with one common nine-ray normal fan. It had an isolated positive moment root `(1,1,1)` but could not change topology anywhere in the positive parameter orthant. The new work introduced a fourth full-dimensional asymmetric summand `D` whose fan genuinely refines P9’s fan.

The final exact fan data are:

- P9 fan: `(V,E,F)=(14,21,9)`;
- `D` fan: `(V,E,F)=(10,15,7)`;
- common refinement for every `lambda>0`: `(V,E,F)=(55,102,49)`;
- final mechanical complexity: `C=55+102+49-2=204`.

Thus the topology jump at `lambda=0` is real: the nine maximal faces of the seed become 49 maximal faces, and the 21 true edges become 102 true edges. Every common-fan vertex was reconstructed exactly as a sum of a P9-fan vertex and a `D`-fan vertex, and every new normal ray was reconstructed as an exact intersection of a P9 edge-normal plane with a `D` edge-normal plane.

## Exact fan-changing summand

The selected `D` is the exact dyadic H-polytope obtained by rounding the seven active maximal planes of the strongest communicating-patch search state to denominator `2^32`, followed by exact triple-intersection reconstruction. Its seven source-plane labels are

```text
n14, r16, n23, n17, n10, n24, r24.
```

Exact rational reconstruction proves that `D` is full-dimensional and irredundant, with ten vertices, fifteen true edges, and seven maximal faces. All ten vertices are simple. Its graph and exact metric data are asymmetric; it has no nontrivial graph-and-distance automorphism.

The exact H planes, V vertices, common-refinement faces, cycles, true edges, source-pair decomposition, and full equilibrium ledger are serialized in [state.pkl](sandbox:/mnt/data/minkowski_fanchange_slot9/state.pkl). The deterministic exact reconstruction is in [build_state.py](sandbox:/mnt/data/minkowski_fanchange_slot9/build_state.py).

This is less convenient than the requested CSV certificate, but it is not a floating-point search checkpoint: every stored coordinate, support, normal, incidence equality, inactive inequality, centroid quantity, and equilibrium primitive is a Python `Fraction`.

## Traversed fan cells and circuits

The fan-design homotopy contains 37 exact circuit walls and 38 exact open cells. The strongest design came from open cell 15, whose exact parameter interval is

```text
925959855/4294967296 < s < 232323715/1073741824,
```

with exact dyadic sample

```text
s = 1855254715/8589934592.
```

The complete wall ordering, exact circuit row sets, determinant polynomials, isolating dyadic intervals, removed facets, added facets, and left/right mechanics are in [topology_path exact atlas](sandbox:/mnt/data/p9_threebranch_library/topology_path(2).json). All 38 fixed-support cells were searched. Additional searches included random full-dimensional tetrahedral correctors, generic H-polytopes, transformed correctors, dynamic support insertion, and local coupled optimization. None produced `(1,1,0)` or a strict `(2,1,1)` endpoint.

For the final fixed exact `D`, the Minkowski scaling parameter has two fan strata:

```text
lambda = 0: original nine-face P9 fan;
lambda > 0: fixed 49-face common refinement fan.
```

The fan is therefore genuinely changed by adding `D`, but after entering the positive `lambda` stratum, scaling this particular summand cannot create another circuit crossing.

## Exact mixed-volume and mixed-first-moment system

The final family is

```text
P(t1,t2,t3) = B + t1 C1 + t2 C2 + t3 C3 + lambda D.
```

Here `lambda` is a fixed positive dyadic design parameter, while `t1,t2,t3` remain the three dependent ordinary-moment controls. A translation of `D`, which leaves its normal fan unchanged, was chosen exactly so that the selected positive dyadic root has zero first moment.

Inside the 49-face common-fan cell,

```text
V(t)   = sum_{|alpha|<=3} v_alpha t^alpha,
M_q(t) = sum_{|alpha|<=4} m_{q,alpha} t^alpha,  q=x,y,z.
```

All coefficients were recovered exactly from the 35 integer simplex evaluations `alpha in N^3`, `|alpha|<=4`, using multivariate forward differences:

```text
Delta^alpha p(0)
  = sum_{beta<=alpha} (-1)^(|alpha|-|beta|)
      binom(alpha,beta) p(beta),

p(t) = sum_alpha Delta^alpha p(0)
       product_j binom(t_j,alpha_j).
```

The Newton-binomial representation was then converted exactly to ordinary monomials. This determines every degree-three volume coefficient and every coefficient of all three degree-four first-moment polynomials without numerical fitting.

The 35 exact geometry evaluations are in [grid_values.json](sandbox:/mnt/data/minkowski_fanchange_slot9/grid_values.json). The complete exact ordinary-monomial polynomials, exact root, exact Jacobian, and exact nonzero Jacobian determinant are in [polynomials.json](sandbox:/mnt/data/minkowski_fanchange_slot9/polynomials.json). The deterministic interpolation implementation is [build_polys.py](sandbox:/mnt/data/minkowski_fanchange_slot9/build_polys.py), and the exact cell evaluator is [evaluate_grid.py](sandbox:/mnt/data/minkowski_fanchange_slot9/evaluate_grid.py).

The positive isolated root is the exact dyadic point stored under `root` in `state.pkl` and `polynomials.json`; numerically it is approximately

```text
t1 = 1.93136672,
t2 = 3.44991315e-7,
t3 = 78.7860847,
lambda = 2.4859503058.
```

At that point all three ordinary first moments vanish exactly. The exact three-by-three moment Jacobian has nonzero determinant. An exact rational interval-Krawczyk computation on

```text
|t_i-t_i*| <= 2^-44
```

has infinity-norm contraction approximately

```text
4.612795995683309e-11 < 1,
```

so the positive moment root is unique in that box. The reproducible interval implementation is [build_interval.py](sandbox:/mnt/data/minkowski_fanchange_slot9/build_interval.py).

## Complete pointwise own-centroid audit

At the exact root, the integrated ordinary centroid is exactly `(0,0,0)`. The complete exact audit covers all 49 maximal faces, all 55 vertices, and the full four-component normal-cone system on all 102 true edges. Triangulation diagonals are not counted as edges.

The resulting strict class is

```text
(S,U,H) = (2,2,2).
```

The intended P9 equilibria remain protected:

- intended stable branch descending from row `27`;
- intended unstable branch descending from incidence `(15,26,27)`.

The surviving unwanted block consists of exactly one additional stable face, one additional unstable vertex, and two saddle edges. The numerical values below are decimal renderings of exact rational primitives stored in `state.pkl`:

| primitive | strict raw margin |
|---|---:|
| intended stable face | `+0.00398560456` |
| unwanted stable face | `+0.00801280542` |
| intended unstable vertex | `+101.407215079` |
| unwanted unstable vertex | `+12.148435451` |
| first saddle | `+0.104616902` |
| second saddle | `+0.00681637` |
| closest excluded face | `-0.00395563057` |
| closest excluded vertex | about `-0.31418` |
| closest excluded nonsaddle edge | about `-0.0065049` |

Every nonincident H/V inequality at the root is strictly separated. The interval audit also completed all common-fan vertex enclosures, centroid enclosure, inactive-incidence inequalities, all 49 face classifications, and all 55 vertex classifications throughout the `2^-44` moment box. The run stopped during the 102-edge interval loop because repeated large-`Fraction` interval allocations became prohibitively slow. Consequently, the pointwise edge audit is exact and exhaustive, but the claimed nonzero perturbation box is **not yet certified for all edges**.

## Strongest obstruction obtained

The first rigorous new obstruction is sharper than the inherited same-fan result:

1. A full-dimensional asymmetric summand can genuinely replace the P9 fan: the exact common refinement expands from `(14,21,9)` to `(55,102,49)`.
2. The three inherited correctors still solve the three ordinary first moments at a unique positive root with a nonsingular exact Jacobian.
3. The intended stable and unstable branches survive with positive margins.
4. Nevertheless, the coupled defect reappears in the new fan as one stable, one unstable, and two saddles, all separated from zero by margins between roughly `6.8e-3` and `1.05e-1` except for the protected stable margin.
5. Once this `D` is fixed, every positive `lambda` lies in the same 49-face common-fan stratum. Scaling `D` or polishing only `t1,t2,t3` cannot cross another incidence circuit.

This does not prove that arbitrary fan-changing Minkowski synthesis is impossible. It proves that the selected seven-face communicating patch changes the fan and closes mass globally, but still realizes the familiar Euler-neutral transfer block in a new location.

## Smallest remaining operation

The next summand should not be another scaled version of this `D`. It must have at least one additional three-dimensional common-normal-fan cell whose entrance circuit is shared by the unwanted stable and unstable stars and both saddle cones. A minimal useful continuation is:

- retain `C1,C2,C3` as dependent moment variables;
- add one or two shape parameters to `D`, not merely a global scale;
- force a simultaneous change of the four surviving critical stars before solving the three moment equations;
- enumerate the resulting common-refinement cells before accepting formal mixed polynomials;
- require the moment root to lie strictly inside a post-circuit cell rather than on its continuation from the current 49-face stratum.

The exact 38-cell circuit atlas and the final 49-face state provide the reusable starting data for that continuation.

## Reproducible files and incompleteness boundary

- [Exact complete geometry and audit state](sandbox:/mnt/data/minkowski_fanchange_slot9/state.pkl)
- [Exact mixed polynomials and Jacobian](sandbox:/mnt/data/minkowski_fanchange_slot9/polynomials.json)
- [Exact 35-point mixed-polynomial evaluations](sandbox:/mnt/data/minkowski_fanchange_slot9/grid_values.json)
- [Exact geometry builder](sandbox:/mnt/data/minkowski_fanchange_slot9/build_state.py)
- [Exact polynomial interpolation](sandbox:/mnt/data/minkowski_fanchange_slot9/build_polys.py)
- [Exact grid evaluator](sandbox:/mnt/data/minkowski_fanchange_slot9/evaluate_grid.py)
- [Partially completed interval verifier](sandbox:/mnt/data/minkowski_fanchange_slot9/build_interval.py)
- [Exact 38-cell/37-circuit design atlas](sandbox:/mnt/data/p9_threebranch_library/topology_path(2).json)
- [Inherited exact same-fan P9 bundle](sandbox:/mnt/data/minkowski_gomboc_slot9/minkowski_common_fan_fallback.zip)

The missing final H/V CSV export, new clean-room verifier, complete edge perturbation box, and new OBJ/STL are real deliverable gaps and should not be inferred from the exact state file. The endpoint is therefore a materialized exact research state and a stronger fan-changing nonwinner, but not a contract-complete artifact bundle and not a homogeneous polyhedral Gömböc.
