# figure-0055

Historical AI scientific report · saved 2026-08-24 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Continued Conway-polar investigation

## Verdict

No own-centroid strict `(S,U,H)=(1,1,0)` polyhedron was obtained. I therefore make no discovery claim and emit no winner OBJ/STL. The acceptance gate still requires a materialized uniform-density body evaluated at its own volume centroid, with one stable maximal face, one unstable vertex, zero saddle edges, and an exact or directed-rounding certificate. :contentReference[oaicite:0]{index=0}

This continuation did produce a new, fully materialized post-wall member of the Conway branch, crossed another genuine facet-lattice transition, extended the connected dual-edge replacement chain, and found a consequential tolerance defect in the exploratory verifier. The defect invalidates several earlier ultra-small-margin low-facet numerical claims, but it does not affect the new robust 60-facet candidate because its raw combinatorial and mechanical margins are over an order of magnitude larger than the problematic threshold.

## 1. Reference reconstruction remains confirmed

The independently reconstructed Conway polar uses the four angles `(66.173,44.519,29.875,19.716)` degrees, ring-radius multiplier `sec(pi/5)`, axial lift `sin(alpha_1)^2 tan(pi/5)^2`, translation of the 21-point mean to zero, and polarization. It has

`(V,F,E)=(21,21,40)`,

strict origin-relative `(S,U,H)=(1,1,0)`, and uniform-volume centroid

`(approximately 0, approximately 0, -1.6516612978833731)`.

Its own-centroid class is `(16,21,35)`. This agrees with the journal’s independent reconstruction. :contentReference[oaicite:1]{index=1}

The reusable reconstruction and exhaustive H-polytope implementation is [gomboc_core.py](sandbox:/mnt/data/gomboc_core.py).

## 2. Strongest new materialized strict-reference candidate

The strongest robust post-wall object from this continuation is [poly60_edge5256_robust.npz](sandbox:/mnt/data/poly60_edge5256_robust.npz).

Its complete binary64 H-representation is stored as the `60 x 3` array `A`, with support vector

`b=(1,...,1)`,

so the body is exactly the floating representation

`P60={x in R^3 : A[i] dot x <= 1, i=0,...,59}`.

The NPZ therefore contains every normal ray, support, and coordinate needed to reconstruct the body; no unavailable inherited mesh is involved. Extraction is simply:

```python
import numpy as np
z = np.load('/mnt/data/poly60_edge5256_robust.npz')
A = z['A']
b = np.ones(len(A))
```

The complete ConvexHull/polar audit gives:

| quantity | value |
|---|---:|
| vertices | `116` |
| maximal faces | `60` |
| true edges | `174` |
| Euler check | `116-174+60=2` |
| complexity `V+E+F-2` | `348` |
| origin-relative class | `(1,1,0)` |
| origin-relative all-feature hard margin | `6.658838754208282e-5` |
| minimum vertex separation | `0.005649131587838903` |
| minimum raw inactive slack | at least `6.658838754208282e-5` |
| uniform-volume centroid | `(-0.03255073,-0.00721539,-0.27107678)` |
| centroid norm | `0.2731194457347848` |
| own-centroid class | `(15,21,34)` |
| own-centroid hard defect | `-0.14382971895683686` |

Thus `P60` is a robust mechanically homogeneous body relative to the distinguished origin, but not relative to its own mass centroid. It is not the requested Gömböc.

The construction audit and selected patch parameters are recorded in [select_edge5256_robust.log](sandbox:/mnt/data/select_edge5256_robust.log). The complete row matrix and metadata are in the NPZ rather than merely in the log.

## 3. Exact wall and topology sequence crossed

The continuation started from [poly57_flipdel25_t012.npz](sandbox:/mnt/data/poly57_flipdel25_t012.npz), a 57-facet strict-reference body with centroid norm `0.27395108733`. This object already incorporated the earlier controlled transition in which the patch on dual edge `(25,53)` made old row 25 non-extreme; deleting row 25 at interpolation parameter `t=0.012` preserved strict `(1,1,0)`.

### Transition A: edge `(48,52)`

The next fixed-cell centroid descent encountered a simultaneous stable-face/saddle wall involving faces 48 and 52. I inserted a new vertex into that edge of the polar hull using

`x=(1-s)p+s q+rho |q-p| normalize(lambda n_1+(1-lambda)n_2)`,

where `p,q` are the edge endpoints and `n_1,n_2` are the outward normals of its two incident polar facets. The result is [poly58_edge4852_robust.npz](sandbox:/mnt/data/poly58_edge4852_robust.npz).

A subsequent centroid descent met its first wall at approximately `t=0.00275`. Immediately across it, face 48 became an additional stable face and the P-edge with endpoints `[108,111]`, incident to faces `[48,57]`, became a saddle. The complete wall trace is [inspect_poly58_4852_wall.log](sandbox:/mnt/data/inspect_poly58_4852_wall.log).

### Transition B: edge `(48,57)`

The entire newly exposed dual edge `(48,57)` was then refined, producing [poly59_edge4857_robust.npz](sandbox:/mnt/data/poly59_edge4857_robust.npz). This opened a substantially longer strict segment: interpolation toward the new centroid-descent state remained `(1,1,0)` through `t=0.021`.

At `t=0.022`, the complete audit was

`(S,U,H)=(2,1,1)`,

with extra face 52 score `+8.02104948e-6` and saddle edge incident to faces `[52,56]` score `+7.50515559e-6`. The trace is [inspect_poly59_wall.log](sandbox:/mnt/data/inspect_poly59_wall.log).

I retained the open point `t=0.018`, materialized as [poly59_path_t018.npz](sandbox:/mnt/data/poly59_path_t018.npz). Its centroid was approximately

`(-0.03255081,-0.00721528,-0.27107671)`,

with norm `0.27311938` and origin-relative hard margin `4.4754318e-5`.

### Transition C: edge `(52,56)`

Finally, I inserted a connected outward polar vertex on edge `(52,56)`, giving `P60`. This restored and enlarged the origin-relative hard margin to `6.658838754208282e-5` while retaining the improved centroid position.

The complete materialized chain is therefore

`P57 -> patch(48,52) -> P58 -> patch(48,57) -> P59 -> descent(t=0.018) -> patch(52,56) -> P60`.

Every arrow is represented by an explicit NPZ row matrix; every patch is connected to the preceding polar hull rather than being a disjoint moment actuator.

## 4. Quantitative assessment of the connected-edge strategy

The successful segment from `P59` to its `t=0.018` state reduced the centroid norm by approximately

`0.27395152-0.27311938 = 8.3214e-4`.

A simple polar-edge insertion in a generic simplicial cell changes the complexity by approximately six: two new primal vertices, three new edges, and one new face. Starting from complexity 348, only about 108 such insertions fit below complexity 1000. At the observed displacement rate, 108 further local stages would correct only about `0.09`, far short of the remaining centroid norm `0.2731`.

Consequently, indefinite one-edge-at-a-time refinement is quantitatively inadequate even though it crosses walls correctly. The next continuation should replace the whole active dual chain

`48 -- 57 -- 58 -- 52 -- 56`

by one multi-vertex connected bulge with independent radial and two-dimensional transverse controls. It should optimize at least three to five new polar vertices simultaneously and permit interior members of the old chain to become non-extreme and be deleted. The required average centroid displacement per topology stage must improve by at least a factor of three to four to remain compatible with `C<1000`, and by much more if a robust exactification radius is desired.

## 5. Important verifier defect discovered

The exploratory routine `gomboc_core.maximal_faces` used the equality test

`abs(A[i] dot v-b[i]) <= 2e-7 * scale`.

For the low-facet ring candidates, bottom-row scales were near ten, so raw inactive slacks between approximately `4e-7` and `9e-7` were incorrectly treated as exact incidences. This changed maximal-face cycles and therefore changed the integrated volume centroid even though the vertex set was identical.

A concrete reproduction uses [own_topsamp_sbplx.npz](sandbox:/mnt/data/own_topsamp_sbplx.npz). The fixed-lattice calculation on its actual active triples gives

`volume = 8.002450825746653`,

`centroid = (-0.00461994205, 0.00006336447, 0.336341017)`.

The loose dynamic face grouping instead gives

`volume = 7.911969875549375`,

`centroid = (-0.00354550963,-0.00030931827,0.341747783)`.

Rows 11, 13, and 15 acquired false near-coplanar incidences. For example, row 11 had inactive raw slacks `4.1544e-7` and `8.5988e-7`, yet both vertices were included as face vertices by the scaled tolerance.

Therefore the ultra-small-margin conclusions associated with `asym_fast_best`, `postwall_best`, `random_top_best`, and the ring topology sampler must not be used as certified evidence. They remain search hints only. Future audits must either use exact incidence, directed intervals, or an equality tolerance strictly below half the independently measured minimum raw inactive slack.

The defect does not explain away `P60`: its raw inactive slack is at least `6.66e-5`, safely separated from the approximately `2e-6` worst scaled equality threshold. The robust Conway-patch branch therefore remains valid as a floating post-wall candidate.

## 6. Constrained low-facet experiment after repairing the interpretation

I formulated the fixed-cell target as a nonlinear max-min problem with an auxiliary margin `tau`. Its constraints were

* intended face score at least `tau`;
* intended vertex score at least `tau`;
* every other face and vertex score at most `-tau`;
* every true-edge score at most `-tau`;
* every inactive half-space slack and vertex separation strictly positive.

The JAX/SLSQP implementation is [jax_own_slsqp.py](sandbox:/mnt/data/jax_own_slsqp.py). From the simple 16-face ring topology it improved the fixed-cell defect from approximately `-1.084e-5` to `-4.84e-7`, but only while the minimum raw inactive slack fell through zero and the minimum vertex separation collapsed to approximately `3.59e-7`. It then left the feasible cell and failed. The transcript is [slsqp_topsamp.log](sandbox:/mnt/data/slsqp_topsamp.log).

This is another transfer-wall approach, not a solution. Because the starting cell itself has raw slack only `2.73e-7`, it is unsuitable for exactification and should not displace the robust 60-facet branch as the principal artifact.

## 7. Reproducible verification route for P60

Use the following files:

* [poly60_edge5256_robust.npz](sandbox:/mnt/data/poly60_edge5256_robust.npz) — complete H rows and patch metadata;
* [fast_ref.py](sandbox:/mnt/data/fast_ref.py) — independent polar-hull origin-relative face/vertex/true-edge audit;
* [polar_fast2.py](sandbox:/mnt/data/polar_fast2.py) — corrected polar structure, volume centroid, and own-centroid mechanics;
* [gomboc_core.py](sandbox:/mnt/data/gomboc_core.py) — triple-intersection verifier, used only with a tightened active-incidence tolerance for near-wall objects;
* [select_edge_patch_robust_small.py](sandbox:/mnt/data/select_edge_patch_robust_small.py) — deterministic connected-edge patch construction.

A minimal verification driver is:

```python
import sys
import numpy as np
sys.path.insert(0, '/mnt/data')
from fast_ref import refaudit
from polar_fast2 import audit

A = np.load('/mnt/data/poly60_edge5256_robust.npz')['A']
R0 = refaudit(A)
Ro = audit(A)

print(R0['counts'], R0['class'], R0['hard'])
print(Ro['centroid'], Ro['class'], Ro['hard'])
```

Expected summary:

`(116,60,174), (1,1,0), 6.658838754208282e-5`,

followed by centroid approximately `(-0.03255073,-0.00721539,-0.27107678)` and own class `(15,21,34)`.

## 8. What changed relative to the supplied journal

The journal ended with a 21-facet reconstructed Conway polar and the instruction to treat support-cell walls as design opportunities rather than terminal failures. This continuation added:

1. Three connected dual-edge refinements beyond the 57-facet branch.
2. A controlled row-deletion flip followed by the explicit edge sequence `(48,52)`, `(48,57)`, `(52,56)`.
3. A new materialized strict-reference body of complexity 348 with hard margin `6.66e-5` and centroid norm `0.27311945`.
4. A quantitative demonstration that serial single-edge patches cannot close the remaining moment within complexity 1000 at the observed rate.
5. Identification of a scaled-incidence tolerance bug that invalidates the earlier tiny-margin low-facet centroid calculations.
6. A constrained max-min formulation that approaches, but does not cross, the low-facet transfer wall while remaining feasible.

The most useful continuation is now a simultaneous connected multi-vertex replacement of the complete five-row dual chain, not another isolated edge midpoint and not another affine-only search.
