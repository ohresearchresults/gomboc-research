# figure-0126

AI research report · 2026-08-27 UTC

---

# Literal verdict

**NO WINNER.** I constructed and certified a genuine exact shared multiwall deformation of the seven-face summand `D`, rebuilt the common normal fan on both sides, and solved the three ordinary moment equations strictly inside the immediate post-circuit cell. The strongest exact endpoint is nevertheless strict own-centroid

```text
(S,U,H) = (2,2,2),
```

not `(1,1,0)`. The selected unwanted stable face, unwanted unstable cone, and both saddle cones all participate in one exact simultaneous fan event, but the Euler-neutral four-feature block **transfers rather than cancels or multiplies**.

The run's acceptance gate requires a finite exact own-centroid `(1,1,0)` polyhedron, complete maximal-face/vertex/true-edge audit, independent verification, and matching OBJ/STL; near-solutions and wall points do not qualify. :contentReference[oaicite:0]{index=0} This result therefore remains a rigorous nonwinner.

## What changed relative to the supplied journal

The predecessor had a fixed seven-face summand and a 49-face common fan. Scaling that fixed `D` could not cross another circuit. I replaced that one-dimensional scaling-only continuation by an exact affine shape family

```text
R_i(s) = (1-s) R_i(old) + s R_i(star),
h_i(s) = (1-s) h_i(old) + s h_i(star),
```

while retaining `C1,C2,C3` as the three dependent full-rank ordinary-moment controls. The exact old and star H data for all seven rows are in [D_parameterization.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/D_parameterization.csv); exact pre-, wall-, and post-cell H/V tables are also materialized.

The shared wall is at the exact value `s=1`. One star ray is

```text
n17* = (
  3631087503/4294967296,
 -2157953435/4294967296,
  -777936111/4294967296
).
```

The other four moved rays are defined exactly by

```text
n10* = (A13  - aS n17*) / bS,
n23* = (A26  - b1 n17*) / a1,
r24* = (A9   - aU n23*) / bU,
n24* = (A100 - a2 n17*) / b2,
```

where

```text
aS = 46209696273/4294967296    bS = 194991/4294967296
a1 = 21376613991/4294967296    b1 = 12113/268435456
aU = 190429/4294967296         bU = 36350435007/4294967296
a2 = 37595828527/4294967296    b2 = 2615052993/536870912.
```

All coefficients are strictly positive. The exact star supports, in row order `n14,r16,n23,n17,n10,n24,r24`, are

```text
2298871293/4294967296,
174470261/2147483648,
143976751/2147483648,
202890453/4294967296,
1004515591/4294967296,
8152155/536870912,
548170411/4294967296.
```

Consequently the four selected active cone relations hold simultaneously and exactly:

```text
A13  = aS n17 + bS n10       unwanted stable-face wall
A26  = a1 n23 + b1 n17       first saddle-cone wall
A9   = aU n23 + bU r24       unwanted unstable-cone wall
A100 = a2 n17 + b2 n24       second saddle-cone wall.
```

The independent verifier recomputes these identities from [p9_normals.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/p9_normals.csv) and [event_parameters.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/event_parameters.csv).

## Exact ordered common-fan atlas

The accepted local atlas uses exact dyadic interior samples

```text
s_pre  = 1 - 2^-23 = 8388607/8388608,
s_wall = 1,
s_post = 1 + 2^-23 = 8388609/8388608.
```

The actual rebuilt cells are:

| order | stratum | `D` `(V,E,F)` | common sum `(V,E,F)` | own-centroid class |
|---:|---|---:|---:|---:|
| 0 | strict pre-cell | `(10,15,7)` | `(57,106,51)` | `(2,2,2)` |
| 1 | shared wall | `(10,15,7)` | `(51,90,41)` | wall stratum |
| 2 | strict post-cell | `(10,15,7)` | `(56,104,50)` | `(2,2,2)` |

Thus the direct pre-to-post change is `Δ(V,E,F)=(-1,-2,-1)`, but the wall itself has a larger transient collapse. There is one chronological event level containing four simultaneous active-cone circuits, rather than four serial walls. The complete exact event ledger is [common_fan_event.json](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/common_fan_event.json).

Exact cell tables:

- Pre: [D H](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/D_pre_H.csv), [D V](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/D_pre_V.csv), [common H](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/common_pre_H.csv), [common V](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/common_pre_V.csv), [true edges](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/common_pre_edges.csv).
- Wall: [D H](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/D_wall_H.csv), [D V](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/D_wall_V.csv), [common H](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/common_wall_H.csv), [common V](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/common_wall_V.csv), [true edges](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/common_wall_edges.csv).
- Post: [D H](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/D_post_H.csv), [D V](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/D_post_V.csv), [common H](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/common_post_H.csv), [common V](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/common_post_V.csv), [true edges](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/common_post_edges.csv).

The common fan was rebuilt exactly from inherited P9 rays, active `D` rays, and all intersections of P9 and `D` edge-cone walls. A candidate ray was retained only when its Minkowski support face had affine dimension two. Vertices were then accepted only when their active common normals had rank three; maximal cycles and true edges were reconstructed from exact face intersections.

## Exact post-cell moment system

Only after the post-cell common fan was rebuilt did I form the actual mixed polynomials for

```text
P(t1,t2,t3) = B + t1 C1 + t2 C2 + t3 C3 + lambda D_post.
```

Every final vertex is affine in `(t1,t2,t3)`. For the exact oriented surface triangulation,

```text
V(t) = Σ_T det(v_a(t),v_b(t),v_c(t))/6,
M(t) = Σ_T det(v_a(t),v_b(t),v_c(t))
       (v_a(t)+v_b(t)+v_c(t))/24.
```

This gives a cubic volume polynomial and three quartic first-moment polynomials. All ordinary monomial coefficients are in [mixed_coefficients.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/mixed_coefficients.csv); the exact root, volume, Jacobian, and determinant are in [moment_certificate.json](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/moment_certificate.json). The exact affine vertex coefficients used for deterministic recomputation are in [affine_vertices.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/affine_vertices.csv).

The isolated positive solution is

```text
t1     = 8295156883/4294967296        ≈ 1.9313667162787169
t2     = 741/2147483648                ≈ 3.450550138950348e-7
t3     = 338383657229/4294967296       ≈ 78.78608471457846
lambda = 10677075263/4294967296        ≈ 2.4859503058250993.
```

At this point all three ordinary first moments vanish **exactly**. The exact Jacobian determinant is nonzero; its decimal value is approximately

```text
0.15941702277476746.
```

An exact rational Krawczyk calculation proves uniqueness in

```text
|t_i-t_i*| <= 2^-40 = 1/1099511627776,
```

with contraction approximately `6.48615343134394e-12`. Since `t2*` is about `3.45e-7`, this box remains strictly in the positive orthant and inside the actual post-circuit fan.

## Final exact summand and sum

The final translated `D_post` has

```text
(V,E,F) = (10,15,7),
minimum inactive H/V gap ≈ 0.004999994354004745.
```

Its exact H/V data are [D_final_H.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/D_final_H.csv) and [D_final_V.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/D_final_V.csv). The inherited exact summands are [B,C1,C2,C3 H](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/B_C1_C2_C3_H.csv) and [B,C1,C2,C3 V](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/B_C1_C2_C3_V.csv).

The final sum has

```text
(V,E,F) = (56,104,50),
complexity = 208,
volume ≈ 788.3507506392091,
ordinary first moment = (0,0,0),
ordinary centroid = (0,0,0),
minimum inactive H/V gap ≈ 1.492804534398596e-8.
```

Human-readable exact data are [final_H.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/final_H.csv), [final_V.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/final_V.csv), and [final_edges.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/final_edges.csv).

## Exhaustive own-centroid mechanics

The exact pointwise class is

```text
(S,U,H) = (2,2,2).
```

Protected intended features survive:

- stable face lineage `P9:27`, raw minimum `≈17.307892668788117`;
- unstable source incidence `(15,26,27)`, raw minimum `≈3.7298871157079323`.

The surviving unwanted block is:

- extra stable `P9edge(13,15)|Dedge(n17,n10)`, raw minimum `≈19.158843390437447`;
- extra unstable source incidence `(9,32,103)` with `D` active rows `(r16,n23,r24)`, raw minimum `≈1.3824517743974605`;
- saddle edge whose incident cones are `P9:26` and `P9:13`, raw minimum `≈15.450236881042198`;
- saddle edge whose incident cones are `P9edge(27,100)|Dedge(n14,n24)` and `P9edge(27,100)|Dedge(n17,n24)`, raw minimum `≈81.14225866999332`.

Closest excluded-feature margins are strictly negative:

```text
max excluded face minimum   ≈ -1.4412299059308242
max excluded vertex minimum ≈ -0.3557198979420428
max excluded edge minimum   ≈ -7.061263318088912e-5.
```

The complete raw ledgers are [face_audit.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/face_audit.csv), [vertex_audit.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/vertex_audit.csv), [edge_audit.csv](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/edge_audit.csv), and [equilibrium_audit.json](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/equilibrium_audit.json).

## Full nonzero perturbation box, including every edge

The same exact `2^-40` parameter box preserves the complete class `(2,2,2)` at each member's own ordinary centroid. It certifies all 50 maximal faces, all 56 vertices, every inactive H/V inequality, and all four normal-cone components of all 104 true edges. Directed exact lower clearances are approximately

```text
inactive H/V  1.492744045635693e-8
face          1.4412299058304112
vertex        0.3557198978347184
edge          7.059272400917946e-5.
```

The full exact fractions are in [perturbation_certificate.json](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/perturbation_certificate.json).

## What the shared event actually does

The pre-to-post feature map is exact:

1. **Stable branch:** `P9:13` becomes the mixed face `P9edge(13,15)|Dedge(n17,n10)`.
2. **Unstable branch:** the source incidence `(9,32,103)` remains unstable, while its full common-normal cone loses two mixed generators and gains inherited ray `P9:9`.
3. **First saddle:** the two pre-wall mixed `(13,26)` generators become inherited cones `P9:26` and `P9:13`.
4. **Second saddle:** the `P9:100` incident cone is replaced by the mixed `(27,100;n17,n24)` cone.

Therefore the literal topological outcome is **transfer**, not cancellation and not multiplication. Exploratory optimization inside the new post fan, including variation of the positive Minkowski coefficients and a modest continuation of `s`, found no `(1,1,0)` state; the best sampled hard score remained negative. This numerical search is supporting evidence only, not a global exclusion theorem.

## Independent verification and mesh

The verifier is a clean-room C++17/GMP implementation that reads the human-readable CSV files rather than the pickle. It independently:

- reconstructs the final `D` from all exact H triples;
- proves the complete bounded common H/V lattice using exact facet-polygon certificates and positive spanning of the normals;
- rebuilds every true edge and maximal-face cycle;
- integrates exact volume and first moments;
- expands the mixed polynomials from affine vertices;
- verifies the root and nonsingular Jacobian;
- closes the exact Krawczyk box;
- audits every face, vertex, inactive incidence, and all four components of all 104 edge cones;
- checks OBJ/STL counts and the watertight exact triangulation.

The published ZIP was also extracted into an empty directory, the verifier was recompiled there, and it returned

```text
verified=true class=(2,2,2) fvec=(56,104,50)
box=1/1099511627776 all_edges=104.
```

Artifacts:

- [Complete exact bundle](sandbox:/mnt/data/minkowski_multiwall_slot9/minkowski_multiwall_exact_bundle.zip) — SHA-256 `e65a67251b6312f57b6bb95c56c33b9d671da9fa19168b937b8024734cf0557c`.
- [Certificate](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/certificate.json)
- [README](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/README.md)
- [Independent verifier source](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/verify_independent.cpp)
- [Verification transcript](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/verification.txt)
- [Clean-room ZIP verification](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/cleanroom_verification.txt)
- [SHA-256 manifest](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/manifest.sha256)
- [OBJ](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/endpoint.obj)
- [STL](sandbox:/mnt/data/minkowski_multiwall_slot9/artifact/endpoint.stl)

## Smallest remaining obstruction and continuation

This event removes the predecessor's fixed-49-face limitation and proves that a full-dimensional Minkowski summand can make all four selected critical stars cross one exact shared wall while the three inherited correctors still close mass at an isolated positive root. What it does **not** change enough is the radial ordering inside the extra source/sink system: the unstable source `(9,32,103)` remains positive, and both saddle channels reopen immediately in the post cell.

The smallest nonredundant continuation is therefore a **second independent shape coordinate of `D`**, not another global scale and not another fixed-post-fan coefficient search. It should create a genuinely two-parameter, three-dimensional common-normal-fan chamber in which:

- the `(9,32,103)` unstable source loses its last all-positive outgoing component or deactivates;
- the inherited `P9:13/P9:26` saddle pair disappears in the same cell;
- the `27/100` return saddle disappears rather than replacing one incident cone;
- row `27` and incidence `(15,26,27)` remain protected;
- `C1,C2,C3` remain dependent moment controls, with the actual-cell mixed polynomials rebuilt after every circuit crossing.

The current affine `s` direction, scaling of fixed `D`, and the entire certified immediate post stratum are closed by this exact endpoint. Other fan-changing Minkowski summands remain open; this result is not an impossibility theorem for the broader architecture.
