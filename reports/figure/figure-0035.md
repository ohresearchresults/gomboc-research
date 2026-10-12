# figure-0035

AI research report · 2026-08-22 UTC

---

# Low-complexity homogeneous polyhedral Gömböc direction

## Outcome

No strict homogeneous polyhedral Gömböc was found in this direction. The fallback deliverable is complete: four exact infinite-family exclusions, a fully exact global certificate for all `V<=6` cases, an exhaustive exact-certificate partition of the seven-vertex shadow systems, a centroid-hardwired seven-vertex continuation family, and a rational verifier covering every face, vertex, and edge.

**Complete artifact:** [low_complexity_gomboc_research_artifact.zip](sandbox:/mnt/data/low_complexity_gomboc_research_artifact.zip)  
ZIP SHA-256: `d211f7de27a7674122ab1b09a651b23faa72db9a2c7f2ab3f63214b03156389f`

Direct entry points:

- [Research report](sandbox:/mnt/data/low_complexity_gomboc/RESEARCH_RESULT.md)
- [Manifest](sandbox:/mnt/data/low_complexity_gomboc/MANIFEST.json)
- [SHA-256 list](sandbox:/mnt/data/low_complexity_gomboc/SHA256SUMS.txt)
- [Exact family-exclusion certificate](sandbox:/mnt/data/low_complexity_gomboc/family_exclusion_certificate.json)
- [Exact `V=5,6` certificate bundle](sandbox:/mnt/data/low_complexity_gomboc/shadow_certificates_5_6.json)
- [Exact `V=7` partition bundle](sandbox:/mnt/data/low_complexity_gomboc/v7_shadow_partition_bundle.json)
- [Exact polyhedron verifier](sandbox:/mnt/data/low_complexity_gomboc/exact_polyhedron_verifier.py)
- [Centroid-hardwired pentagonal-bipyramid builder](sandbox:/mnt/data/low_complexity_gomboc/pentagonal_bipyramid_parametric.py)

## 1. Exact equilibrium predicates

Translate the uniform-volume centroid to the origin and give every maximal face an outward cycle.

For a face `F=(v_0,...,v_{m-1})`, outward normal `n`, and support `H=n·v_i`, let

`Phi(F,i) = n·((v_{i+1}-v_i) × (H n - ||n||^2 v_i))`.

The face is strictly stable exactly when `Phi(F,i)>0` for every edge of its cycle.

A vertex `v` is strictly unstable exactly when

`Psi(v,w) = -v·(w-v)>0`

for every adjacent vertex `w`.

For an edge `[a,b]`, put `e=b-a`, `t_num=-a·e`, `t_den=e·e`, and `q_num=t_den a+t_num e`. If `n_1,n_2` are the two adjacent outward normals, define

`rho_1=(n_1·q_num)(n_2·n_2)-(n_2·q_num)(n_1·n_2)`,

`rho_2=(n_2·q_num)(n_1·n_1)-(n_1·q_num)(n_1·n_2)`.

The edge has a strict saddle exactly when

`t_num>0`, `t_den-t_num>0`, `rho_1>0`, and `rho_2>0`.

`exact_polyhedron_verifier.py` evaluates these signs with `fractions.Fraction`, checks strict convexity, maximal face cycles, two-face edge incidence, Euler topology, exact signed tetrahedral volume and first moment, and `S+U-H=2`. This supplies the complete face/vertex/edge predicate set requested by the assignment.

## 2. Four exact low-complexity exclusion theorems

### Centroidal-axis pyramids

Let an arbitrary strictly convex polygonal base lie in `z=0`, with area centroid `0`, and let the apex be `(0,0,h)`, `h>0`. Its uniform centroid is `(0,0,h/4)`. After centering,

`a=(0,0,3h/4)`, `b_i=(p_i,-h/4)`.

Every apex edge satisfies

`a·(b_i-a)=-3h^2/4<0`,

so the apex is unstable. Choose `k` maximizing `||p_i||^2`. For either cyclic neighbour `j`,

`b_k·(b_j-b_k)=(||p_j||^2-||p_k||^2-||p_j-p_k||^2)/2<0`,

and

`b_k·(a-b_k)=-||p_k||^2-h^2/4<0`.

Thus `b_k` is a second unstable vertex and every homogeneous right/centroidal-axis pyramid has `U>=2`. This rules out all base sizes, not only a fixed normal fan. The transcript's oblique-pyramid centroid hardwiring is the more general identity `A=(-3C_x,-3C_y,3)` for a base in `z=-1`. :contentReference[oaicite:0]{index=0}

### Centroidal-axis bipyramids

For an arbitrary equatorial polygon of area centroid zero and apices `(0,0,h)` and `(0,0,-k)`, the uniform centroid is `(0,0,(h-k)/4)`. The centered top and bottom edge derivatives are respectively

`-h(3h+k)/4<0`, `-k(h+3k)/4<0`.

Both apices are strictly unstable, hence `U>=2` for every such bipyramid.

### Homothetic right frusta and controlled coaxial caps

For `P=conv(B×{0}, lambda B×{H})`, where `B` has area centroid zero and `lambda,H>0`,

`z_g/H=(1+2 lambda+3 lambda^2)/(4(1+lambda+lambda^2))`.

Every section centroid lies on the common axis. The projections of `g` to both end-face planes are therefore their area centroids, strictly inside both caps, so `S>=2`. The same argument excludes any convex coaxial stack with two noncollapsed parallel end caps and all section centroids on their common perpendicular; collapse of one end reduces to the pyramid theorem.

### Centrally symmetric families

For `P=-P`, the centroid is the symmetry centre and every equilibrium cell is paired with a distinct antipodal equilibrium cell of the same dimension and type. Therefore `S`, `U`, and `H` are even. This excludes centrally symmetric bipyramids, symmetric vertex splits, and symmetric truncated/stacked constructions.

The quantified statements and algebraic identities are machine-readable in `family_exclusion_certificate.json`; `verify_family_theorems.py` checks them symbolically.

## 3. Exact global exclusion for five and six vertices

The published source proves that a unique unstable root induces a rooted shadow tree with inequalities

`(r_i-r_parent(i))·r_i <= 0`,

and that a root-based tetrahedral decomposition of a centroid-zero polyhedron has at least one tetrahedron `T` with

`sum_{k in T} r_{k,1} <= 0`.

It then reduces the problem to finitely many inhomogeneous quadratic systems and certifies infeasibility by positive rational weighted sums whose augmented matrices are positive definite. The paper states the rooted-tree/tetrahedron algorithm, the exact counts `375` for `V=5`, `5568` for `V=6`, and `5943` total, while its official repository provides independently rational-verifiable supplementary material. :contentReference[oaicite:1]{index=1}

This run independently regenerated all `5943` cases and stored an integer weight vector for every one. `certify_shadow.py` reconstructs each augmented integer matrix and proves positive definiteness using fraction-free Bareiss/Sylvester pivots—no floating-point sign is trusted.

| vertices | systems | exact certificates | remainder |
|---:|---:|---:|---:|
| 5 | 375 | 375 | 0 |
| 6 | 5,568 | 5,568 | 0 |
| total | 5,943 | 5,943 | 0 |

Bundle internal SHA-256: `83005fc9fc76f0e6124b2f98deda54d41985d232f98fdd9fd1c8eaf3483bc899`.

Consequently every homogeneous mono-unstable polyhedron, and therefore every homogeneous polyhedral Gömböc, has at least seven vertices.

## 4. Exhaustive seven-vertex shadow partition

The same necessary-condition search was run over every maximal planar graph on seven vertices, every representative unstable-root orbit, every rooted spanning tree, and every root tetrahedron. The simplicial reduction is globally applicable here: the source paper explains that an arbitrarily small perturbation can preserve mono-instability while making the polyhedron simplicial, so maximal planar graphs suffice. :contentReference[oaicite:2]{index=2}

| graph6 | architecture | systems | exact PD exclusions | run remainder | remainder orbits |
|---|---|---:|---:|---:|---:|
| `F~nR_` | stacked simplicial | 23,120 | 22,926 | 194 | 91 |
| `Fv|Xo` | stacked simplicial | 33,649 | 33,289 | 360 | 152 |
| `Fek~w` | stacked simplicial | 32,736 | 32,292 | 444 | 420 |
| `FJn^W` | nonstacked simplicial | 30,276 | 29,820 | 456 | 156 |
| `Fhf~o` | pentagonal bipyramid | 19,855 | 19,595 | 260 | 50 |
| **total** | all five maximal-planar types | **139,636** | **137,922** | **1,714** | **869** |

Every listed exclusion is an exact positive-integer-weight positive-definite certificate; all denominators are at most `100000`. `verify_v7_shadow_bundle.py` reconstructs the enumeration, verifies each matrix exactly, proves that certified and surviving keys are disjoint and exhaustive, and recomputes the 869 rooted automorphism orbits.

Bundle internal SHA-256: `d13260088b7a769ffb0d48f4e62b514d3cbb3cd91c8a1e026bf774499e4eb39a`.

This agrees with the source paper's warning that Algorithm 2 resolves only approximately 99% at `V=7`; the positive-definite weighted-sum condition is sufficient, not necessary. :contentReference[oaicite:3]{index=3} The 1,714 systems are therefore an exact search remainder, not claimed feasible.

## 5. Smallest surviving centroid-hardwired family

Because `V<=6` is excluded, the first possible size is seven. The smallest explicit continuation family is a planar-equator oblique pentagonal bipyramid.

Let `p_0,...,p_4` be a strictly convex CCW pentagon in `z=0` containing the origin, with area centroid `C`. Put

`T_0=(u,h)`, `D_0=(-(k/h)u,-k)`, with `h,k>0`.

The apex segment crosses the equator at the origin, and the exact uniform-volume centroid is

`g_xy=3C/4 + (h-k)u/(4h)`, `g_z=(h-k)/4`.

The centered vertices are

`T=(u-g_xy,(3h+k)/4)`,

`D=(-(k/h)u-g_xy,-(h+3k)/4)`,

`B_i=(p_i-g_xy,(k-h)/4)`.

The ten facets are `(T,B_i,B_{i+1})` and `(D,B_{i+1},B_i)`. Strict topology is expressed by

`det(p_{i+1}-p_i,p_{i+2}-p_{i+1})>0`,

`det(p_{i+1}-p_i,-p_i)>0`, `h>0`, `k>0`.

Polygon area and centroid formulas, followed by the `Phi`, `Psi`, and `rho` signs above, give a finite rational semialgebraic `S=1,U=1,H=0` system. A SAT chamber chooses one negative witness for every nontarget face/vertex and at least one violated saddle condition for every edge. `pentagonal_bipyramid_parametric.py` emits exact rational centered coordinates and runs the full verifier; `oblique_bipyramid7_search.py` is the differentiable front end. No strict winner arose in the sampled chambers, so no near-solution is mislabeled as a certificate.

## 6. Reproduction

```bash
unzip low_complexity_gomboc_research_artifact.zip
cd low_complexity_gomboc
sha256sum -c SHA256SUMS.txt
python verify_family_theorems.py
python certify_shadow.py --verify shadow_certificates_5_6.json
for g in 0 1 2 3 4; do python verify_v7_shadow_bundle.py --graph "$g"; done
python pentagonal_bipyramid_parametric.py pentagonal_bipyramid_example_input.json \
  --polyhedron /tmp/pb.json --audit /tmp/pb.audit.json --obj /tmp/pb.obj
python exact_polyhedron_verifier.py right_hexagonal_pyramid.json
python exact_polyhedron_verifier.py right_hexagonal_frustum.json
```

The included pyramid, frustum, and bipyramid rational examples are verifier tests, not Gömböcs. All have exact centroid zero, strict topology, a complete exact equilibrium audit, and `S+U-H=2`.

## 7. Finite continuation target

The unconstrained coordinate search has been reduced to a finite exact task: take the 869 rooted seven-vertex survivor orbits, impose maximal-planar realization inequalities and the exact degree-four uniform-volume centroid equations, add one target stable-face chamber, one target unstable-vertex chamber, and the explicit no-saddle edge disjunctions, then eliminate branches with rational SOS/Positivstellensatz or interval branch-and-bound. Every surviving rational point should be passed through `exact_polyhedron_verifier.py` before acceptance. This continuation uses new normals and combinatorial types and does not reuse the excluded fixed-normal Reshetov or Conway families.
