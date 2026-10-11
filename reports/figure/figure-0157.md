# figure-0157

Historical AI scientific report · saved 2026-08-29 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Steady Willow 49 — exact trace-one SPD continuation through walls 19672 and 4421

## Literal disposition

**No homogeneous convex polyhedral Gömböc was found.** In particular, no open trace-one SPD metric box was isolated whose unchanged Santaló-centred 4,324-row lattice has strict own-centroid class `(S,U,H)=(1,1,0)`. The entire bounded five-dimensional SPD core is not covered, so no global fixed-lattice nonexistence theorem is claimed.

The run's acceptance gate remains a finite uniform-density convex polyhedron evaluated at its own exact volume centroid, with exactly one stable maximal face, one unstable vertex, no saddle edge, a positive perturbation margin, independently reconstructible H/V and incidence data, a complete full-cone audit, and matching OBJ/STL. :contentReference[oaicite:0]{index=0} The supplied journal identified walls `19672 (3267→3302)` and `4421 (760→725)` as the first useful continuations after the three previous exact S–H exits. :contentReference[oaicite:1]{index=1}

This continuation resolves both targets by exact actual chamber paths. It adds:

- `17` full-dimensional all-wall boxes, each of independent-coordinate radius `2^-100`;
- `15` exact one-wall corridors, one for every actual intervening wall group;
- `51` exact trace-one corridor-cover boxes proving that every centre segment remains in the prior unresolved compact-core remainder;
- two new full-dimensional relative-condition cells proving `S>=2`;
- two pairwise-disjoint exact inner boxes of radius `2^-17`, removing exact five-coordinate volume

```text
2^-79 = 1/604462909807314587353088
      ≈ 1.6543612251060553e-24
```

from the prior unresolved remainder.

Both target crossings are genuine S–H cancellations, but each leaves an already stable adjacent row. Their far sides are strict `(2,2,2)`, not `(1,1,0)`.

## 1. Exact body, own-centroid invariance, and normalized domain

The immutable source generator is

```text
q_i = Qint_i / 2^48,  i=0,...,4323.
```

The globally unique Santaló point `a_*` is isolated in the previously certified dyadic box

```text
a_* ∈ a_c + [-2^-90,2^-90]^3.
```

For

```text
P_* = (conv{q_i}-a_*)^circ,
```

the uniform-volume centroid is exactly zero. Every invertible linear image `A P_*` remains exactly own-centred because

```text
∫_(A P_*) y dy = det(A) A ∫_(P_*) x dx = 0.
```

The independently rebuilt irredundant lattice is unchanged:

```text
maximal faces / H rows = 4,324
vertices               = 8,644
true edges              = 12,966
Euler                    = 2.
```

Modulo rotation and positive scale, write the trace-one inverse metric as

```text
K = [[k00,k01,k02],
     [k01,k11,k12],
     [k02,k12,1-k00-k11]] ∈ SPD(3).
```

With ordered eigenvalues `lambda1>=lambda2>=lambda3>0`, every claimed box is certified throughout

```text
17179/16384 < lambda1/lambda3 < 2048/19,
lambda2/lambda1 > 1/32,
lambda3/lambda2 > 19/64,
lambda3 > 19/4115,
trace(K)=1,
```

and above its exact direction-dependent stable and unstable collar thresholds. Each box is also proved outside all `285` previously certified relative cells or balls:

```text
23 parent-tube balls
256 Sharp Quartz 52 cells
3 SW49 cells R0/R1/R2
3 previous first-exit renewed cells.
```

The proofs use exact Sturm eigenvalue isolation, rational Weyl bounds, projective eigendirection leaf enclosures, Sylvester positivity, and one generalized-Rayleigh witness pair per previous cell.

## 2. Complete mechanical wall basis

The clean-room verifier reconstructs the actual face and primal graphs from the exact active triples. It checks

```text
25,932 directed face walls,
25,932 directed vertex walls,
12,966 actual true-edge four-component cones.
```

For adjacent support rows `i,j` and adjacent primal vertices `f,g`, the exact walls are

```text
S_ij(K) = (q_i-a_*)^T K(q_i-q_j),

W_fg(K) = d_g y_f^T adj(K)y_f
          - d_f y_f^T adj(K)y_g,

d_f = 1-a_*^T y_f > 0.
```

An actual true edge with incident faces `(i,j)` and endpoints `(f,g)` is a strict saddle exactly when all four actual components are positive:

```text
S_ij>0, S_ji>0, W_fg>0, W_gf>0.
```

Every all-wall box evaluates all `51,864` directed walls over both the metric box and the complete isolated Santaló box. Stable faces, unstable vertices and saddles are then rebuilt from complete actual cones; no representative-feature inference is used.

## 3. Exact actual path to wall 19672

The first branch begins at an exact open remainder box outside all prior exclusions and promotes every subsequent wall group needed to make `19672` an actual chamber facet:

```text
F16340
V22987
F8096
V17835
V6682
V6683
F19672.
```

Thus the path consists of eight exact open cells and seven exact adjacent corridors. The first seven cells all have

```text
(S,U,H)=(3,2,3),
stable rows        1007,3267,3302,
unstable vertices  1047,6643,
saddle edges       5431,7691,9836.
```

The six wall crossings before the target are mechanically count-neutral. The final target corridor crosses only face wall

```text
19672: 3267 -> 3302,
actual true edge 9836,
edge endpoints 7087,8292.
```

Its exact common root enclosure over the full Santaló box is

```text
[14344720775535182114818847141743965909237597
 /22300745198530623141535718272648361505980416,

 3586180193883795528704757544938828580769135
 /5575186299632655785383929568162090376495104]
```

with width approximately `8.21e-24` and midpoint approximately `0.643239526205624` in the normalized corridor parameter.

Across this wall:

```text
(3,2,3) -> (2,2,2),
removed stable row 3267,
removed saddle edge 9836,
retained stable row 3302,
unstable set unchanged.
```

The result is forced by the exact identity

```text
S_3267,3302 + S_3302,3267
  = (q_3267-q_3302)^T K(q_3267-q_3302) > 0.
```

At the first exact remainder box on this branch, the reverse wall `19673 (3302→3267)` is already positive and row `3302` is already stable. Therefore crossing `19672` can remove row `3267` and its saddle, but it cannot reduce the stable count below two.

### Exact post-19672 endpoint

The far-side metric centre is

```text
K_A = 2^-80 *
[[622856923233914810531840,
  277389809737602057633792,
  495915089495258604503040],

 [277389809737602057633792,
  170260157976430858207232,
  228688748160524985827328],

 [495915089495258604503040,
  228688748160524985827328,
  415808738404283505967104]].
```

The full trace-one independent-coordinate box

```text
|Delta(K00,K11,K01,K02,K12)| <= 2^-100,
K22=1-K00-K11
```

is strict SPD and has exhaustive class

```text
(S,U,H)=(2,2,2),
stable rows        1007,3302,
unstable vertices  1047,6643,
saddle edges       5431,7691.
```

Its minimum certified absolute directed-wall separation is approximately

```text
1.5092757504399995e-11.
```

## 4. Exact actual path to wall 4421

The second branch likewise starts at an exact open remainder box and promotes every actual intervening wall group:

```text
V5001
V4861
V20955
F8087
F12319
V3623
F3289
F4421.
```

The first eight cells have

```text
(S,U,H)=(3,2,3),
stable rows        725,760,3547,
unstable vertices  478,1430,
saddle edges       2210,6370,6424.
```

The first seven crossings are count-neutral. The final exact corridor crosses only

```text
4421: 760 -> 725,
actual true edge 2210,
edge endpoints 2882,4748.
```

The common exact root enclosure is

```text
[33954831248284483424242299345559298553181199
 /44601490397061246283071436545296723011960832,

 8488707812071120856060650935266420265065337
 /11150372599265311570767859136324180752990208]
```

with width approximately `6.82e-24` and midpoint approximately `0.761293646154070`.

The target transition is

```text
(3,2,3) -> (2,2,2),
removed stable row 760,
removed saddle edge 2210,
retained stable row 725,
unstable set unchanged.
```

Again,

```text
S_760,725 + S_725,760
  = (q_760-q_725)^T K(q_760-q_725) > 0.
```

The reverse wall `4420 (725→760)` is already positive in the first exact remainder box, so row `725` is stable before `4421` is crossed.

### Exact post-4421 endpoint

```text
K_B = 2^-80 *
[[794956800190478276362240,
  291306837402833028907008,
  410232098007293813063680],

 [291306837402833028907008,
  161556308243797868806144,
  135423853547030170304512],

 [410232098007293813063680,
  135423853547030170304512,
  252412711180353029537792]].
```

Its radius-`2^-100` trace-one box is strict

```text
(S,U,H)=(2,2,2),
stable rows        725,3547,
unstable vertices  478,1430,
saddle edges       6370,6424,
```

with minimum certified wall separation approximately `1.5515602345862315e-10`.

## 5. Exact chamber adjacency and remainder confinement

The complete atlas has class histogram

```text
15 boxes: (3,2,3)
 2 boxes: (2,2,2)
 0 boxes: (1,1,0).
```

For every adjacent pair, the two full-dimensional wall-sign payloads differ at exactly one directed wall. The exact centre segment is certified by the identity

```text
p(t) = (1-t)p(0) + t p(1) - a t(1-t),
```

where `a` is obtained from `adj(K1-K0)` for vertex walls. Face walls are affine. Endpoint signs plus an exact adverse-curvature bound prove that all `51,863` non-target walls retain strict sign. No corridor required wall-sign subdivision.

The target polynomial has degree at most two and opposite strict endpoint signs, hence exactly one sign-changing root. Directed bisection over the complete Santaló box produces the common rational root intervals above.

To certify that the paths really stay in the unresolved remainder, every corridor has an exact trace-one box cover. Adaptive subdivision produced

```text
15 complete corridor covers,
51 trace-one cover boxes,
maximum subdivision depth 4.
```

Every cover box has exact SPD, compact-core, direction-dependent collar, and `285`-cell nonmembership certificates. Thus every point on every claimed centre corridor lies outside the complete prior certified union; the paths do not silently re-enter R0/R1/R2, the parent tube, an SQ52 cell, or one of the three earlier renewed cells.

## 6. Two new rigorous `S>=2` cells

### Post-19672 cell

Define

```text
B(K_A,155/128)
 = {trace-one K in SPD:
    exists mu>0 with mu K_A <= K <= (155/128) mu K_A}.
```

The two disjoint sink subsets are

```text
{1007,1042}
{3267,3302}.
```

All `20` complete outward directed boundaries satisfy the exact squared relative-condition inequality

```text
(1+kappa)^2 c_lower^2
  - (kappa-1)^2 p_upper q > 0.
```

Therefore every metric in the complete cell has `S>=2`.

The first conservative certificate failure is

```text
wall 19674: 3267 -> 3303,
kappa_* approximately 1.2137407601981414,
```

with exact isolating interval stored in `relative_post_19672.json`. The next failure directly leaving stable row `3302` is

```text
wall 19880: 3302 -> 3303,
kappa_* approximately 1.2250329550174668.
```

Thus the sharp continuation is to exactify `19674` and then test whether `19880` can remove `3302` without a compensating birth.

### Post-4421 cell

```text
B(K_B,181/128),
disjoint sink subsets {3547,3512} and {760,725}.
```

All `19` complete outward boundaries are exact-positive, so `S>=2` throughout. Its first certificate failure is already directed out of an active stable row:

```text
wall 21352: 3547 -> 3582,
kappa_* approximately 1.4188263827766405.
```

The exact root enclosure is stored in `relative_post_4421.json`.

### Positive-volume shrinkage

Each relative cell contains an exact closed trace-one inner box

```text
|Delta(K00,K11,K01,K02,K12)| <= 2^-17.
```

At every one of the `32` vertices of each box, exact rational Sylvester minors prove the two Löwner inequalities. Convexity then includes the whole box in its relative cell. Exact generalized-Rayleigh witnesses keep each box outside every one of the `285` earlier cells. The two boxes are pairwise disjoint in the five independent coordinates and each has volume `2^-80`, so their exact union volume is `2^-79`.

The new unresolved set is exactly

```text
R_new = R_previous
        \ B(K_A,155/128)
        \ B(K_B,181/128).
```

It is not claimed empty.

## 7. Search evidence, separated from certificates

Discovery used local random, hyperplane-targeted and adjacency searches in the exact compact-core coordinates. Across `171,158` valid metrics the minimum sampled stable count was two and no strict sampled winner appeared. This guided the two exact branches only; it is not used as coverage or nonexistence evidence.

## 8. Deterministic transformed object and mesh

The strongest endpoint retained for reconstruction is the post-19672 box `A19672_C07`. Let

```text
A = K_A^(-1/2)
```

be the unique SPD algebraic inverse square root. The transformed exact object is defined by

```text
h_i^A = A^(-T)(q_i-a_*),
v_f^A = A y_f/(1-a_*^T y_f).
```

The actual maximal-face cycles, active triples and true edges are independently rebuilt from the source. The deterministic midpoint export has

```text
H rows / maximal faces   4,324
vertices                  8,644
true polyhedral edges    12,966
boundary triangles       17,284
triangulated edges       25,926
triangle-edge incidence       2
watertight                    yes.
```

The CSV/OBJ/STL coordinates use the dyadic metric centre and midpoint of the isolated Santaló box. The exact own-centred body is specified by the dyadic metric, the isolated algebraic Santaló root, the transformation formulas, and the reconstructed incidence.

## 9. Independent verification

From the extracted directory run

```bash
python verify_all.py
```

The full clean rerun independently verifies:

- exact source hashes and actual incidence;
- all `17` complete `51,864`-wall / `12,966`-edge-cone boxes;
- all `15` one-wall corridor identities and root isolations;
- all `51` compact-core remainder-cover boxes;
- both new relative-condition cells and all `64` Löwner vertices;
- all prior-cell nonmembership witness blocks;
- deterministic H/V reconstruction and watertight OBJ/STL.

The expected terminal synthesis is

```json
{"verified":true,
 "full_all_wall_boxes":17,
 "exact_one_wall_corridors":15,
 "corridor_domain_cover_boxes":51,
 "renewed_relative_cells":2,
 "new_inner_box_volume":"1/604462909807314587353088",
 "target_walls":[19672,4421],
 "next_certificate_failures":[19674,21352],
 "strongest_endpoint":"A19672_C07"}
```

followed by

```text
PASS
```

## 10. Artifact map

- `GLOBAL_CERTIFICATE.json` — compact exact synthesis.
- `continuation_atlas.json` — complete branch, cell, corridor, lineage and remainder ledger.
- `cell_A19672_C*.json`, `cell_B4421_C*.json` — all 17 exact metric/root boxes and full audits.
- `wall_signs_*.bin` — complete 51,864-wall sign payloads.
- `corridor_*.json` — exact one-wall adjacency certificates.
- `domain_cover_corridor_*.json` — exact prior-remainder covers of every corridor.
- `relative_post_19672.json`, `relative_post_4421.json` — complete new `S>=2` cells.
- `verify_structure_cleanroom.py`, `verify_cell_exact.py`, `verify_corridor_bending.py`, `verify_corridor_domain_cover.py`, `verify_relative_post.py`, `verify_mesh.py` — independent component verifiers.
- `verify_all.py` — full rerun entry point.
- `FULL_VERIFICATION.txt` — completed full rerun transcript.
- `rebuild_strongest_endpoint.py` — deterministic H/V and mesh exporter.
- `strongest_endpoint_H.csv`, `strongest_endpoint_V.csv`, `strongest_endpoint.obj`, `strongest_endpoint.stl` — strongest exact nonwinner realization.

## Most useful continuation

The fixed-lattice metric route remains open globally, but the two named targets are closed as direct routes to a Gömböc. The best next finite branch is:

1. cross `19674 (3267→3303)` as an actual chamber facet outside the new post-19672 cell;
2. promote intervening walls, if any, to reach `19880 (3302→3303)`, the nearest renewed-certificate boundary that directly attacks the surviving stable row `3302`;
3. in parallel, cross `21352 (3547→3582)`, which directly attacks surviving stable row `3547` on the post-4421 branch;
4. exactify every child with the same complete all-wall/full-edge audit and renew an SCC/subset cell whenever two disjoint sinks persist.

No refinement inside the two new relative cells is useful: their complete nonwinner status is already proved.

## Downloadable artifacts

- [Complete self-contained bundle](sandbox:/mnt/data/Steady_Willow_49_19672_4421_atlas.zip)
- [Bundle SHA-256 file](sandbox:/mnt/data/Steady_Willow_49_19672_4421_atlas.zip.sha256)
- [Complete Markdown handoff](sandbox:/mnt/data/Steady_Willow_49_19672_4421_atlas/RESULT.md)
- [Global exact certificate](sandbox:/mnt/data/Steady_Willow_49_19672_4421_atlas/GLOBAL_CERTIFICATE.json)
- [Complete continuation atlas](sandbox:/mnt/data/Steady_Willow_49_19672_4421_atlas/continuation_atlas.json)
- [Unified independent verifier](sandbox:/mnt/data/Steady_Willow_49_19672_4421_atlas/verify_all.py)
- [Completed full verification transcript](sandbox:/mnt/data/Steady_Willow_49_19672_4421_atlas/FULL_VERIFICATION.txt)
- [Strongest endpoint H table](sandbox:/mnt/data/Steady_Willow_49_19672_4421_atlas/strongest_endpoint_H.csv)
- [Strongest endpoint V table](sandbox:/mnt/data/Steady_Willow_49_19672_4421_atlas/strongest_endpoint_V.csv)
- [Watertight OBJ](sandbox:/mnt/data/Steady_Willow_49_19672_4421_atlas/strongest_endpoint.obj)
- [Watertight STL](sandbox:/mnt/data/Steady_Willow_49_19672_4421_atlas/strongest_endpoint.stl)

Final bundle SHA-256:

```text
7f8754fe2565c6996b95f9fe53af5180c0058aac8e0ba6e90c981ffe0087d0b6
```
