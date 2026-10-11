# figure-0116

Historical AI scientific report · saved 2026-08-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Fourier-balanced ring continuation — terminal handoff

## Verdict

**No finite homogeneous polyhedral Gömböc was obtained in the continuation.** The acceptance gate remains an exact own-volume-centroid class `(S,U,H)=(1,1,0)` with a finite H/V representation, complete maximal-face and true-edge lattice, positive full-normal-cone margins, independent verification, and matching OBJ/STL. :contentReference[oaicite:0]{index=0}

The continuation did not supersede the previously delivered exact 16-vertex balanced-ring fallback. It did, however, identify a stronger mechanically correct ring seed and quantify why its fixed topology cannot supply the necessary mass transport before crossing real equilibrium walls.

## 1. What changed relative to the previous handoff

The previous result established two facts:

1. Sampling the Sloan fourth-root radial law does not inherit finite Fourier cancellation merely because `R^4` has azimuthal modes zero and one. Actual tetrahedral moment terms contain mixed factors such as `R_a^2R_bR_c`, with unbounded Fourier support.
2. Five-point cancellation is exact when the **vertex coordinates themselves** have Laurent degree at most one, because `det(a,b,c)` then has degree at most three and `det(a,b,c)(a+b+c)` degree at most four.

That addressed the moment half of the journal’s proposed ring architecture. :contentReference[oaicite:1]{index=1} The present continuation attacked the mechanical half by starting from the reconstructed Conway four-pentagonal-ring geometry, which is already strict `(1,1,0)` relative to a known axial mechanical centre.

The principal new conclusion is:

> **The Conway cyclic ring body has full rank-three centroid actuation, but its fixed mechanical chamber is left after roughly one percent of the linearized displacement required to move its uniform-volume centroid into that chamber. A topology-changing complete cyclic-orbit event is mandatory.**

## 2. Reconstructed Conway cyclic-ring seed

The deterministic reconstruction uses the published meridian angles

```text
66.173°, 44.519°, 29.875°, 19.716°
```

with

```text
r_i = product_{j≤i} cos(alpha_j)
theta_i = sum_{j≤i} alpha_j
x_i = r_i sin(theta_i)
z_i = r_i cos(theta_i)
rho_i = x_i / cos(pi/5)
h = sin(alpha_1)^2 tan(pi/5)^2.
```

After reversing the rings to bottom-to-top order and applying an axial similarity gauge, its ring data are approximately

```text
ring 0: radius 0.1179162768568565   z = -1
ring 1: radius 0.2358260737067870   z = -0.965813131663354
ring 2: radius 0.4005553479886099   z = -0.856216312353991
ring 3: radius 0.5493295544724199   z = -0.537555981364411
apex:                                    z = 1
```

The actual hull has

```text
(V,E,F,C) = (21,40,21,80).
```

At its arithmetic vertex centre it has the strict class

```text
(S,U,H) = (1,1,0),
```

with the bottom pentagon as the unique stable maximal face, the axial apex as the unique unstable vertex, and no saddle true edge. The closest normalized exclusions are approximately

```text
nonstable-face exclusion     0.0031093805
nonunstable-vertex exclusion 0.0086791121
nonsaddle-edge exclusion     0.0092164041
inactive convexity gap       0.0170629715.
```

This is therefore a genuinely open cyclic-ring mechanical seed, not a graph surrogate or wall point.

Its axial centres differ substantially:

```text
arithmetic mechanical centre z ≈ -0.752282244
uniform-volume centroid      z ≈ -0.351909225383516.
```

At its own volume centroid the class is

```text
(S,U,H) = (6,21,25).
```

The reconstructed seed is numerical rather than an exact algebraic object because it evaluates trigonometric functions at the published terminating-decimal degree angles. It is used only as a discovery and obstruction seed, not as an admissible exact endpoint.

## 3. Complete axial mechanical-centre interval

For a fixed `C5`-symmetric body, every face, vertex, and edge equilibrium primitive is affine in an axial reference coordinate `c`:

- face projection barycentrics are affine because the perpendicular foot is `c e_z + (h-n_z c)n`;
- vertex primitives `(v-c e_z)·(v-w)` are affine;
- edge projection parameter and both incident-normal coefficients are affine.

The continuation therefore constructed the open equilibrium interval of every actual maximal face, vertex, and true edge, intersected the target bottom-face and apex intervals, and subtracted every unwanted equilibrium interval.

For the reconstructed Conway body, the complete axial set on which the actual class is exactly `(1,1,0)` is

```text
c_z < -0.7338174268495291.
```

The arithmetic centre lies inside this chamber, whereas the volume centroid lies above its boundary by

```text
0.38190820146601345.
```

This is a sharper obstruction than merely reporting the centroid displacement: it gives the exact first mechanical wall in the reconstructed fixed geometry. The interval calculation is algebraically exact conditional on the floating reconstructed coordinates and face lattice; it has not been promoted to a directed algebraic certificate for the trigonometric seed.

## 4. Full-rank moment Jacobian but early circuit walls

The affine cyclic-ring parameterization allows independent degree-one bases for the rings while retaining the fixed Conway incidence lattice. The normalized centroid-discrepancy Jacobian at the seed has singular values

```text
0.25015229
0.24795056
0.15786667.
```

Thus the three volume moments have full differential rank. There is no local moment-rank obstruction.

The minimum-norm Newton direction cancels the linearized centroid discrepancy, but the first actual mechanics/topology primitives reach zero at only approximately

```text
1.11177%   edge/full-normal-cone wall
1.13568%   edge/full-normal-cone wall
1.16709%   edge/full-normal-cone wall
1.18273%   maximal-face exclusion wall
1.20797%   maximal-face exclusion wall
```

of the required Newton step. Direct line evaluation confirms that the body exits the strict mechanical chamber while the centroid discrepancy remains about `0.19` in diameter-normalized units.

This quantifies the obstruction:

```text
moment rank                    available
required displacement          macroscopic
fixed-cell safe displacement   about two orders smaller
```

## 5. Fixed-topology nonlinear searches

Three independent fixed-topology approaches were run:

### Differentiable full-feature continuation

An affine degree-one parameterization of the upper rings, an elliptic bottom ring, and a free apex projection reduced the normalized centroid discrepancy from

```text
0.1998394835  to about 0.18265018
```

before reaching a mechanical wall. The own-centroid target score remained approximately `-0.16962`.

### Fixed separator-branch continuation

One negative exclusion primitive was selected for every non-target maximal face, vertex, and true edge, while all target primitives and convexity inequalities were retained. Four runs converged to a best discrepancy of approximately

```text
0.1744610165
```

with the weakest retained branch constraint about `2.52×10^-5`. No moment root occurred inside the branch.

### Global CMA search in the fixed Conway lattice

Eight completed global runs retained reference-relative `(1,1,0)`. The strongest state reduced the discrepancy to

```text
0.1718432980
```

only by shrinking the reference mechanical margin to approximately

```text
9.60×10^-8.
```

Its own-centroid class remained far from the target. This is strong computational evidence that the fixed Conway face lattice cannot close the mass discrepancy, but it is not a global exact impossibility theorem.

## 6. Targeted fifth-ring collar experiment

The next topology was a fifth complete pentagonal ring inserted into the low part of the Conway stack. Physical `C5` symmetry was retained so the transverse first moments remained zero structurally and every circuit change occurred in a complete fivefold orbit.

The coarse search varied:

- the insertion interval among the lower three ring gaps;
- collar radius over a broad log range;
- collar latitude;
- all original radii and internal heights by moderate perturbations;
- independent cyclic ring offsets.

A total of `12,672` completed full-hull samples were audited before termination. The best observed full-active state had

```text
(V,E,F) = (26,70,46)
(S,U,H) = (16,11,25)
full-feature score = -0.1127403711.
```

No `(1,1,0)` own-centroid chamber appeared. Other sampled cells retained fivefold packets such as `(6,6,10)`, `(6,11,15)`, `(11,11,20)`, and larger orbit-multiplied classes.

This search was deliberately coarse and is **not** an exclusion of the complete five-ring family. It does show that merely inserting a ring and perturbing ordinary radii, heights, and twists does not preserve the Conway mechanical chamber while supplying the required low axial mass.

## 7. Exact fallback remains the smallest fully audited balanced-ring body

The strongest admissible exact object from this direction remains the previously delivered algebraic aligned `C5` three-ring body with one apex:

```text
actual vertices       16
true edges            30
maximal faces         16
complexity             60
equilibrium class  (6,6,10)
```

Its centred tetrahedral identities are exact in

```text
Q(theta),  theta = 2 cos(pi/10),
theta^4 - 5 theta^2 + 5 = 0,
theta in (19/10,2),
```

and give

```text
Mx = My = Mz = 0.
```

The transverse moments vanish separately on each of six complete five-triangle boundary orbits. Its complete grouped maximal-face lattice, all 30 true edges, every face/vertex/full-edge-cone primitive, perturbation box, independent mesh reconstruction, and watertight OBJ/STL remain certified.

The exact family-wide aligned obstruction also remains valid. For an aligned homothetic regular-ring stack with lower radius `rho_0>0`, terminal apex, area density `A(z)=kappa_m rho(z)^2`, volume centroid `c`, and side-edge threshold `T(z)=z+rho rho'`,

```text
integral A(z)(T(z)-c) dz = -kappa_m rho_0^4/4 < 0,
```

while `T(z_A)-c>0` at the apex. Hence an interior upward crossing occurs on some side segment and produces a complete orbit of saddle edges:

```text
H >= m.
```

Thus the exact 16-vertex fallback cannot be continued to a winner inside the aligned homothetic family.

## 8. Precise continuation obstruction

The combined evidence now isolates three nested obstructions:

1. **Direct Sloan sampling obstruction.** The fourth-root radial factors destroy the finite-mode argument in the actual tetrahedral first moments.
2. **Aligned-stack topology obstruction.** Every aligned homothetic cap-to-apex stack has at least one complete saddle orbit.
3. **Conway fixed-lattice mass-transport obstruction.** A mechanically correct cyclic-ring seed exists and has rank-three moment actuation, but its first face/edge walls occur after roughly `1.1%` of the required centroid displacement. Fixed-lattice optimization then converges to those walls rather than a centred chamber.

The unresolved topology problem is therefore not to discover a mechanically correct ring flow from scratch. It is to transport macroscopic lower mass through a **complete orbit-scale circuit replacement** while retaining the already correct Conway source–sink mechanics.

## 9. Most useful next construction

The smallest nonexcluded continuation is a 26-vertex cyclic body obtained from the Conway seed by replacing its lower two-ring transition with a genuine volumetric collar complex rather than inserting one ordinary ring.

The required event should:

1. replace all five copies of the earliest edge-cone wall and all five copies of the adjoining maximal-face wall simultaneously;
2. preserve a single bottom polygonal stable face and the axial apex as the sole unstable vertex;
3. carry enough volume near the lower chamber to move `c_z` downward by approximately `0.382` in the present gauge;
4. keep the actual boundary triangulation partitioned into complete five-triangle orbits, so `Mx=My=0` remains a structural tetrahedral identity;
5. solve the remaining axial first-moment equation as a hard dependent algebraic equation;
6. allow the obsolete tiny bottom-to-first-ring side faces and edges to disappear in the same circuit event.

A promising parameterization is a **two-cell collar** with two counterphased pentagonal layers sharing cross-links, rather than one added ring. The two layers provide independent volume and slope controls: one carries low mass, while the second restores the local monotone edge/face witnesses. Only after a symmetric axial root is found inside an open chamber should affine degree-one ring corrugations be introduced to split any surviving fivefold defect packet.

## 10. Incomplete obligations

The continuation did **not** complete:

- an exact or interval-isolated five-ring/collar moment root;
- an exact topology-changing Conway successor;
- a new exact H/V object smaller or mechanically better than the 16-vertex fallback;
- a full interval proof excluding the fixed Conway topology;
- a continuation archive combining the new exploratory scripts with a newly certified OBJ/STL.

Accordingly, no new object is claimed as a Gömböc or as an exact candidate.

## 11. Reproducible artifacts

### Previously certified exact fallback

- [Complete exact ring handoff](sandbox:/mnt/data/fourier_ring_complete_handoff.zip)
- [Exact algebraic generator and verifier](sandbox:/mnt/data/fourier_ring_handoff/exact_fourier_candidate.py)
- [Machine-readable exact certificate](sandbox:/mnt/data/fourier_ring_handoff/fourier_ring_certificate.json)
- [Expanded exact H/V/topology data](sandbox:/mnt/data/fourier_ring_handoff/fourier_ring_full_exact_data.json)
- [Watertight OBJ](sandbox:/mnt/data/fourier_ring_handoff/fourier_ring_fallback.obj)
- [Watertight STL](sandbox:/mnt/data/fourier_ring_handoff/fourier_ring_fallback.stl)
- [Original full research bundle](sandbox:/mnt/data/fourier_ring_handoff/fourier_ring_research_bundle.zip)

### New continuation artifacts

- [Deterministic Conway ring reconstruction](sandbox:/mnt/data/fourier_ring_continuation/conway_affine_seed.py)
- [Reconstructed Conway vertices, rings, faces and centres](sandbox:/mnt/data/fourier_ring_continuation/conway_affine_seed.json)
- [Axial mechanical-interval constructor](sandbox:/mnt/data/fourier_ring_continuation/axis_mechanical_intervals.py)
- [Centroid Jacobian and first-wall certificate](sandbox:/mnt/data/fourier_ring_continuation/conway_linear_certificate.json)
- [Linear-analysis driver](sandbox:/mnt/data/fourier_ring_continuation/conway_linear_analysis.py)
- [Fast full-feature fixed-topology evaluator](sandbox:/mnt/data/fourier_ring_continuation/conway_numba.py)
- [Differentiable fixed-topology continuation](sandbox:/mnt/data/fourier_ring_continuation/torch_conway_center.py)
- [Fixed separator-branch continuation](sandbox:/mnt/data/fourier_ring_continuation/torch_conway_branch.py)
- [Global fixed-lattice CMA driver](sandbox:/mnt/data/fourier_ring_continuation/cma_conway_center.py)
- [Strongest fixed-lattice CMA state](sandbox:/mnt/data/fourier_ring_continuation/cma_conway/s5.json)
- [Coarse fifth-collar search driver](sandbox:/mnt/data/fourier_ring_continuation/search_conway_collar_coarse.py)
- [Completed fifth-collar search manifest](sandbox:/mnt/data/fourier_ring_continuation/conway_collar_coarse.json)

## Bottom line

The continuation did not produce the requested finite homogeneous polyhedral Gömböc. The exact 16-vertex `(6,6,10)` body remains the smallest fully audited Fourier-balanced ring artifact. The genuinely new advance is the reduction from a vague ring search to a sharply quantified topology problem: a strict `(1,1,0)` Conway cyclic-ring mechanical chamber exists, the moment Jacobian has full rank, its complete axial chamber ends at `c_z=-0.7338174268495291`, the actual volume centroid is `0.38190820146601345` beyond that boundary, and the first fixed-lattice walls occur after only about `1.1%` of the required Newton displacement. A successful continuation must therefore replace a complete fivefold lower transition orbit with a volumetric two-cell collar while solving the axial moment equation inside the new cell; another ordinary ring insertion or fixed-topology deformation is insufficient.
