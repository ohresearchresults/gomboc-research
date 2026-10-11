# figure-0199

Historical AI scientific report · saved 2026-09-02 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Vivid Atlas 32 — exact P9 two-row terminal determination

## Literal verdict

**NONWINNER.** I did not obtain a homogeneous polyhedral Gömböc. I did materialize and independently verify the first genuinely two-row, shared-interior terminal topology beyond the recorded P9-XG4 one-row concurrency obstruction, and I isolated the first remaining exact obstruction plus the smallest nonrepeating successor topology.

The run’s acceptance gate is a finite uniform-density convex polyhedron at its own ordinary-volume centroid with strict `(S,U,H)=(1,1,0)`, complete actual H/V/E incidence, exhaustive positive-margin mechanics, an independent verifier, and matching meshes. :contentReference[oaicite:0]{index=0} The inherited exact P9-XG4 endpoint instead has eight active rows, `(V,E,F)=(12,18,8)`, own-centroid `(2,2,2)`, and a proved one-row concurrency obstruction; its compelled successor is a two-row or coupled-old-plane shared terminal spanning the three return stars. :contentReference[oaicite:1]{index=1}

## Source boundary

The durable journal supplied the exact P9-XG4 topology, result hash, wall order, witnesses, and obstruction, but not Steady Willow 02’s worker-local XG4 coordinate bundle. The Library did contain the full exact P9-XG3 parent. I therefore reconstructed the specified XG4 active cell exactly from that parent by taking the canonical terminal point `L=(H+K)/2`, then advanced that exact reduced cell. This is an equivalent exact realization of the recorded active topology and mechanics, not a byte-identical reconstruction of the unavailable private XG4 endpoint. I do not claim to have audited its 32 unavailable inactive supplied rows; the new finite object has nine supplied rows, all nine active and irredundant.

## Exact deterministic construction

Let

```text
d=(8,3,5),  alpha=1/16,
L=(H+K)/2,
M=L+alpha*d,
N=L-alpha*d.
```

The exact raw polar/support rows `q_i·x<=1` are

```text
T27  (-7125242734162057/140737488355328,
       265769074670437/35184372088832,
      -63255401657691/70368744177664)

TR   (-892363419092795/281474976710656,
      -235941426090029/140737488355328,
      -528766574131575/140737488355328)

SU   (-544131479513675/140737488355328,
      -96790958131853/35184372088832,
       118288508214145/140737488355328)

SC1  (-276717838830129/140737488355328,
      -1302539451900877/140737488355328,
      -228646779652985/70368744177664)

SA5  (-1735735365091297/281474976710656,
      -2190132466616797/281474976710656,
      -2075306589585777/281474976710656)

S102 (-1745325229249529/70368744177664,
       5268329269809467/281474976710656,
       1934562100355505/281474976710656)

G    (1595031506620615/70368744177664,
      69636553284589/35184372088832,
      72284311426759/70368744177664)

M    (25797847887987223/281474976710656,
     -2226495112408585/140737488355328,
      1064366297382197/281474976710656)

N    (25516372911276567/281474976710656,
     -2279271670541833/140737488355328,
      888444436938037/281474976710656)
```

Exact strictly positive coefficients recorded in `boundedness.positive_spanning_weights` satisfy `Σ λ_i q_i=0`, so the origin is strictly interior to `conv{q_i}` and the polar is bounded. Every row is an extreme polar vertex and therefore an irredundant primal support.

## Complete actual incidence

The exact row hull is `Q:(V,E,F)=(9,21,14)`. Its polar is

```text
P:(V,E,F)=(14,21,9),   C=42.
```

All `C(9,3)=84` candidate triple intersections were enumerated. The 14 actual P vertices, in IDs `0..13`, have active triples

```text
0  T27/TR/SA5
1  T27/TR/S102
2  T27/SU/SC1
3  T27/SU/S102
4  T27/SC1/SA5
5  TR/SA5/G
6  TR/S102/G
7  SU/SC1/M
8  SU/S102/M
9  SC1/SA5/N
10 SC1/M/N
11 SA5/G/N
12 S102/G/M
13 G/M/N
```

The nine actual maximal-face cycles of P are

```text
T27  0 4 2 3 1
TR   0 1 6 5
SU   2 7 8 3
SC1  2 4 9 10 7
SA5  0 5 11 9 4
S102 1 3 8 12 6
G    5 6 12 13 11
M    7 10 13 12 8
N    9 11 13 10
```

The 21 true polar edges, equivalently the 21 dual primal true edges, are

```text
T27-TR, T27-SU, T27-SC1, T27-SA5, T27-S102,
TR-SA5, TR-S102, TR-G,
SU-SC1, SU-S102, SU-M,
SC1-SA5, SC1-M, SC1-N,
SA5-G, SA5-N,
S102-G, S102-M,
G-M, G-N, M-N.
```

Exact vertex coordinates, centered support rows, face ledgers, and all four cone components for all 21 edges are expanded in the bundle’s CSV/JSON files.

## Genuine two-row shared-interior terminal

The one-row `L` star

```text
SU/SC1/L, SU/S102/L, SC1/SA5/L, SA5/G/L, S102/G/L
```

is replaced by

```text
SU/SC1/M, SU/S102/M,
SC1/SA5/N, SC1/M/N,
SA5/G/N, S102/G/M, G/M/N.
```

`M-N` is a true cross-edge. The two positive-volume radial tetrahedral cells `conv(0,SC1,M,N)` and `conv(0,G,M,N)` share `conv(0,M,N)`. Their connected boundary simultaneously spans the three requested return stars `M/SU/S102`, `N/SA5/SC1`, and `M/G/S102`. This is one common three-dimensional prismatic terminal complex, not another serial page or boundary-spine insertion.

## Exact volume, centroid, and first moments

The exact ordinary volume is the rational `mass.raw_volume` in the exact data file; independently evaluated,

```text
V ≈ 0.0025270722405904577.
```

The exact raw first moments are the three rationals in `mass.raw_first_moment`, numerically

```text
(-9.521847796082168e-6,
 -3.5521194665682756e-6,
 -1.0510004940005398e-5).
```

The exact raw centroid is the three-rational vector in `mass.raw_centroid`, numerically

```text
c=(-0.003767936524781484,
   -0.0014056264041499313,
   -0.004158964975828987).
```

Translation by this exact `c` gives literal first moments `(0,0,0)`. Equivalently, the own-centered H representation is exactly

```text
H_i = q_i/(1-q_i·c).
```

All denominators are positive; the directed perturbation certificate gives the uniform lower bound `0.8161132702647319`.

## Exhaustive full-cone mechanics

At its exact own centroid the body is strictly

```text
(S,U,H)=(2,2,2).
```

The complete positive features are

```text
stable faces:      T27, M
unstable vertices: TR/S102/G, SU/S102/M
saddle true edges: SA5-N, S102-M.
```

Exact category-clearance minima, shown in decimal, are

```text
stable primitive                    24.373401900060898
nonstable-face exclusion            12.414493830586082
unstable full-cone coefficient       0.022567017958335742
nonunstable-vertex exclusion         0.0014633381612485063
saddle full-cone component           0.0007701565648860707
nonsaddle full-cone exclusion        0.0002899554454052931
nonincident support slack            0.02177280804967796
```

No intended combinatorics or triangulation proxy is used: every maximal face, every actual vertex, and the four components `t,1-t,alpha,beta` of every true-edge normal cone are checked.

A coordinatewise independent box

```text
|δq_ij| <= 2^-26
```

preserves all 126 affine four-row signs, all H/V/E incidence, boundedness, positive projective denominators, the exact own-centroid recomputation, every mechanical sign, and class `(2,2,2)`. A separate two-parameter `alpha,beta` box of radius `2^-26` preserves the same cell.

## Three centering controls and two independent topology controls

The three translation/projective-normalization variables are dependent centering controls. Their centroid-residual Jacobian is exactly `-I_3`, determinant `-1`.

After eliminating them, two independent shape controls remain:

```text
alpha: M=L+alpha*d, N=L-alpha*d          shared-edge/diagonal control
beta:  G(beta)=G+beta*(0,1,0)            external-witness/antibirth control.
```

For the exact diagonal primitive

```text
det(M-SC1,N-SC1,G-SC1)
```

and the own-centered antibirth primitive

```text
H_M·(H_M-H_G),
```

the exact `2×2` Jacobian has nonzero determinant. Its decimal evaluation is

```text
[ 9058.562184385446      51.4809486153053  ]
[-1341.5582186592585     35.59346113073926 ]

det = 391490.2707295457.
```

Thus the terminal has two genuine independent topology variables after centering, rather than one variable under a reparameterization.

## First remaining exact obstruction

The true shared edge `M-N` is a forced stable component. Every directed support from either endpoint to every true neighbor outside `{M,N}` is exactly positive. The mutual supports obey

```text
A(M→N)+A(N→M)=||H_M-H_N||^2>0.
```

At the endpoint,

```text
A(M→N)= 24.373401900060898
A(N→M)=-23.892107507058395
||H_M-H_N||^2=0.4812943930025013.
```

Therefore at least one of `M,N` is stable throughout every incidence/external-sign cell covered by the certificate. `T27` is independently stable, hence

```text
S >= 2
```

throughout the entire certified two-row terminal cell. This is the first exact obstruction; local rank, centering rank, and the requested two-row connectivity are not the issue.

I also tested the exact serial subdivision

```text
X=L+2^-6(1,-1,-1).
```

It deletes edge `M-N`, gives `P:(V,E,F)=(16,24,10)`, and remains strict `(2,2,2)`. The connected component `{M,N,X}` has all external endpoint supports positive. Its maximum-radius member is necessarily stable by Cauchy, so this one-row edge subdivision still forces `S>=2`. It enlarges the transferred component rather than killing it.

## What I tried beyond the exact construction

Every numerical experiment rebuilt the actual hull, integrated the true volume centroid, regrouped maximal faces, rebuilt true edges, and audited full cones.

- A broad 15,000-proposal independent two-row scan found no target.
- A local seven-row campaign retained 2,811 target-preserving states: 1,764 were `(2,2,2)`, 432 `(2,3,3)`, 365 `(3,2,3)`, and none was `(1,1,0)`, `(2,1,1)`, or `(1,2,1)`.
- Differential evolution on `M,N,G` reached best score about `-0.22538`, class `(4,2,4)`.
- A fixed-nine-row covariance minimax search reached about `-0.02594` but expanded the critical block.

These searches are discovery evidence only. The exact forced-edge/component theorem is the certified conclusion.

## Minimal successor topology

The smallest nonrepeating successor must do all of the following in one rebuilt full-hull event:

1. delete/deactivate `M-N` and at least one endpoint, or give both possible component radius maxima independent nonpositive external witnesses;
2. replace the extra unstable star `SU/S102/M` and both saddle channels `S102/M` and `SA5/N` in the same volumetric complex;
3. preserve stable `T27` and target unstable vertex `TR/S102/G`;
4. retain the three exact moment/centering equations as dependent controls;
5. provide at least three independent topology controls: shared-spine deletion/diagonal, a separate S-H antibirth/death coordinate, and a separate U-H antibirth/death coordinate.

The smallest evidence-supported realization is a **second-spine/fifth-page terminal**: an octahedral or triangular-prismatic pair of communicating nonsimplicial cells joining the `SC1/G` cross-gap to the `S102/SA5` return sectors. Coupled motion of old planes `G,SC1,SA5,S102` producing the same two-spine interior is equivalent. Another serial edge subdivision, single-row page, or fixed-cell polishing is closed.

## Reproducible artifact

- [Complete exact bundle](sandbox:/mnt/data/P9_XG5_TWO_ROW_EXACT_NONWINNER.zip)
- [Archive SHA-256](sandbox:/mnt/data/P9_XG5_TWO_ROW_EXACT_NONWINNER.zip.sha256)
- [Complete research handoff](sandbox:/mnt/data/P9_XG5_TWO_ROW_EXACT_NONWINNER/RESEARCH_HANDOFF.md)
- [Expanded exact H/V/E, mass, mechanics, controls](sandbox:/mnt/data/P9_XG5_TWO_ROW_EXACT_NONWINNER/p9_xg5_two_row_exact.json)
- [Independent exact verifier](sandbox:/mnt/data/P9_XG5_TWO_ROW_EXACT_NONWINNER/verify_independent.py)
- [Perturbation certificate](sandbox:/mnt/data/P9_XG5_TWO_ROW_EXACT_NONWINNER/perturbation_box_certificate.json)
- [Watertight OBJ](sandbox:/mnt/data/P9_XG5_TWO_ROW_EXACT_NONWINNER/p9_xg5_two_row_centered.obj)
- [Watertight STL](sandbox:/mnt/data/P9_XG5_TWO_ROW_EXACT_NONWINNER/p9_xg5_two_row_centered.stl)

Archive SHA-256:

```text
039d26afe6d7add90cde950374d210509d8713968d6660f5c0ead4fec0d98306
```

A clean extraction followed by `./RUN_ALL.sh` regenerates the endpoint and certificates, verifies all 84 candidate intersections, 14 actual vertices, 9 maximal faces, 21 true edges and 21 full edge cones, checks exact volume/centroid and zero translated first moments, validates both interval boxes, proves the serial-component obstruction, and verifies OBJ/STL watertightness. Terminal output:

```text
ALL P9-XG5-2R VERIFIERS PASS
```

## Unresolved uncertainty

The exact theorem excludes the displayed two-row cell and its certified neighborhood, plus the explicit one-row subdivision successor. It is not a global impossibility theorem for all two-row placements, all coupled old-plane motions, or the proposed two-spine nonsimplicial successor. The missing worker-local XG4 inactive-row bundle also prevents a literal 40-row path audit from the original endpoint; the new nine-row endpoint itself is fully exact, finite, independently reconstructible, and certificate-complete.
