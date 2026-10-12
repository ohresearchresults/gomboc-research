# minimum-0006

AI research report · 2026-09-07 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NOVA24_V9_DISTINCT_TRIPLE_V1

## Result

**Every full-dimensional homogeneous convex three-polytope with exactly one nondegenerate unstable vertex has at least nine true vertices.** More quantitatively, let an interior reference point o make such a polytope mono-unstable, let g be its actual uniform-volume centroid, and let R be its largest vertex distance from o. If the polytope has at most eight vertices, then

**|g−o| > R/7168.**

The proof below is universal over geometry, face lattice, symmetry, and radius ratio. It uses a new second-apex moment inequality and 17 small rational certificate tables. These tables generate 595 positive-definite 8×8 matrices, all freshly checked by exact fraction-free principal determinants and a separate rational LDLᵀ calculation. The exact check certifies the stronger common bound Q_T ≻ I/128, not floating-point eigenvalue positivity.

The underlying statement is stronger than an actual-centroid exclusion. For a finite set X, write Σ₃(X) for the convex hull of sums of three distinct members. No set of four through eight distinct nonzero Euclidean vectors admitting an escape tree can satisfy **−conv(X) ⊆ Σ₃(X)**. A new exact nine-vector rank-two example satisfies all these conditions, with strict escape and relative-interior containment. Thus nine is sharp for this dimension-independent relaxation. The sharpness example has zero three-dimensional volume and is not a homogeneous polyhedron.

Combining the new V≥9 theorem with the named Atlas13 parent's F≥8 theorem gives **E≥15 and C=2E≥30** for strict homogeneous polyhedral Gömböcs. The previous E14,V8,F8 boundary is therefore excluded. Taking the journal's accepted C1374 upper witness as inherited evidence gives **30≤C_min≤1374**, not an exact minimum. No new homogeneous upper witness, F≥9 theorem, or C30 realization is claimed.

## Dependencies and scope

The exact conceptual parents are `minimum-0001`, SHA-256 `9cc634b1d007b03568764c4b4703096fe7216e39fbe9e0f5ea78b1ca4326a4f8`, and `minimum-0003`, SHA-256 `520200e9b9541f54133e00931fc6ce2021fa752d2e8bb06df574ed1248720893`. The former supplies the four-deep-node lemma and actual-volume cone identity; both are reproduced below. The latter supplies the separately established facet lower bound, not a polar-centroid identification. Their literal statements support these distinct uses.

The parent V8 result's former C24 corollary was already superseded by the joint C28 bound; that historical difference is not a conflicting geometry definition. The current handoff advances C28 to C30 through the vertex side. The inherited upper witness was not reaudited here.

Every centroid g below is the ordinary centroid of the uniformly filled original solid. No polar centroid, Santaló point, equal-vertex-mass centroid, prescribed ray set, or affine normalization enters the proof. Scaling the largest radius to one is only a Euclidean similarity. Nonsimplicial facets and nonsimple vertices are included.

## 1. Escape trees and the distinct-triple condition

Translate the reference o to zero. If a vertex v is not strictly unstable, some incident edge to p has nonnegative outgoing derivative:

    D(v,p) = v·p−|v|² ≥ 0.

The incident edge directions generate the tangent cone, so checking these edges suffices. For distinct endpoints,

    |p|²−|v|² = 2D(v,p)+|p−v|² > 0.

Choose one such parent at every nonroot vertex. The resulting arrows cannot cycle and reach the unique unstable vertex u, which is also the unique largest-radius vertex. Weak shadow inequalities suffice throughout this proof. In particular,

    v ∈ B(p/2,|p|/2).

For any actual vertex a, triangulate every maximal facet not containing a, using its actual vertices, and cone those triangles from a. These positive-volume tetrahedra partition the solid up to their boundaries. With their actual normalized volume weights λ_T,

    4g = a + Σ_T λ_T Σ_(v∈T) v,
    λ_T>0,   Σ_T λ_T=1,   |T|=3,   a∉T.                  (1)

Triangulation diagonals are not additional true edges. Equation (1) is an actual-volume identity, not an independently chosen point-mass model.

At g=0 it implies, for every a∈X,

    −a ∈ Σ₃(X\{a}).                                      (2)

Condition (2) is equivalent to −conv(X)⊆Σ₃(X). One direction is immediate. For the converse, sort the projections in an arbitrary direction as x₁≤⋯≤x_N. Global containment gives x₁+x_(N−2)+x_(N−1)+x_N≥0. For a point outside the top three, replacing x₁ by its projection preserves this inequality. For a point in the top three, its projection plus the three largest remaining projections is the sum of the top four, again at least that same nonnegative expression. Separation in every direction proves (2).

The proof will use only (2), in fact only the root-apex condition and, in four tree types, the condition at the second node. Therefore failure of the actual-volume problem is established by a necessary relaxation, not inferred from non-discovery.

## 2. Two elementary rooted-tree bounds

A node is deep relative to a root when its tree distance from that root is at least two.

### 2.1 Individual depth bound

For a descending path from root a to a node v at depth d, let consecutive ray angles be α_i. Shadow inequalities give |v_i|/|v_(i−1)|≤cos α_i. When a·v<0, append the final angle from v to −a. The d+1 angles have sum at least π. Concavity of log cos gives

    −a·v/|a|² ≤ b_d = cos(π/(d+1))^(d+1),  d≥2.

At depths zero and one the projection is nonnegative. The needed bounds are

    b₂=1/8, b₃=1/4,
    b₄=(11+5√5)/64 <89/256,
    b₅=27/64.                                           (3)

The strict rational bound uses √5<9/4. More generally a positive projection in direction w of a node at depth at most m−1 is at most |a|cos(angle(a,w)/m)^m. This follows by appending the final projection angle and padding with zero angles.

### 2.2 Four-deep-node lemma

For a rooted tree with at most four deep nodes and root a, every three distinct nodes satisfy

    a·(x+y+z)>−(15/16)|a|².                              (4)

Here is the full finite algebra behind the only two exceptional joint cases. Number six nodes 0,…,5 and select 3,4,5. The chain has parents (−1,0,1,2,3,4); the fork has parents (−1,0,1,2,3,3). Their respective matrices are

```text
chain:
 75 -64    0   40   40  40
-64 128 -104    0    0   0
  0 -104 208 -176    0   0
 40   0 -176  352 -168   0
 40   0    0 -168  336 -96
 40   0    0    0  -96 192

fork:
 75 -64    0   40  40  40
-64 128 -104    0   0   0
  0 -104 208 -184   0   0
 40   0 -184  368 -88 -88
 40   0    0  -88 176   0
 40   0    0  -88   0 176
```

Their leading principal determinants are

    chain: 75,5504,333632,15370240,434778112,56623104;
    fork:  75,5504,333632,9116672,817229824,5266866176.

All are positive. For each Euclidean coordinate k, let X_k be the six coordinate entries. With D_i=v_i·v_(p_i)−|v_i|², the corresponding positive weights are

    chain: (8/5,13/5,22/5,21/5,12/5);
    fork:  (8/5,13/5,23/5,11/5,11/5).

Direct expansion gives

    (1/80)Σ_k X_kᵀ M X_k
      = (15/16)|v₀|²+v₀·(v₃+v₄+v₅)−Σ_i weight_i D_i.

Positive definiteness proves (4) in both cases.

For completeness, at most four deep nodes implies height at most five. At height five all four deep nodes lie on the same chain, and only the selected depth pattern (3,4,5) needs its joint certificate; every other triple is bounded by b₂+b₄+b₅<229/256<15/16. At height at most four, three distinct depth-four nodes would require at least five deep nodes. The only exceptional pattern (3,4,4) must share the selected depth-three parent, giving the fork. All other triples are bounded by b₄+2b₃<217/256, 2b₄+b₂<210/256, or 3b₃=3/4. This proves the lemma for every tree, in every Euclidean dimension.

### 2.3 New two-node bound

In a rooted tree of at most six nodes, root a, any two distinct nodes satisfy

    a·(x+y)>−(197/256)|a|².                              (5)

At height five the entire tree is a chain, so the two largest possible depths are four and five: b₄+b₅<197/256. At smaller height, 2b₄<178/256 suffices. Including the root or a depth-one node only improves the bound.

## 3. The new second-apex moment inequality

Consider an eight-node escape tree beginning with two unbranched links:

    v₀ ← v₁ ← v₂,

so all remaining nodes belong to the six-node subtree rooted at b=v₂. Put r=|b|. That subtree has at most four deep nodes, and b·v₁≥r².

Apply (1) with apex b and take its dot product with b. For any triple T excluding b:

- If T contains neither v₀ nor v₁, (4) gives b·(b+Σ_T v)>r²/16.
- If T contains v₁ but not v₀, (5) and b·v₁≥r² give an even stronger positive bound.
- If T contains v₀, (5) gives

    b·(b+Σ_T v)>b·v₀+(59/256)r².                        (6)

For the last statement, the other two entries can include v₁; its positive projection again only improves the bound.

At actual centroid zero the mean in (1) is zero, so some triple has nonpositive projection. It must contain v₀. Equation (6) therefore forces

    H := −v₀·v₂−(59/256)|v₂|² > 0.                      (7)

This is the additional moment information that closes the hard trees. It does not follow from the shadows alone. Its derivation changes the apex of the actual-volume cone identity, rather than silently assigning new weights to the root decomposition.

## 4. Complete eight-node tree reduction

All rooted trees admit a labeling with p_i<i. There are exactly 7!=5040 such parent arrays on eight nodes. Sorting recursive parenthesis encodings produces 115 rooted isomorphism types. The recovery program exhausts all 5040 arrays and verifies the following disjoint reduction; no polyhedral graph or simplicial assumption is involved.

| Exclusion | Rooted types | Increasing-labeled arrays |
|---|---:|---:|
| Root has at least three children: (4) at the root | 30 | 2556 |
| Root has one child, that child has at least two children: (4) at the first child | 28 | 600 |
| Remaining one-child trees of height at most four | 7 | 52 |
| Two-child trees of height at most four, except the broom below | 30 | 1638 |
| Height-four broom | 1 | 7 |
| Two elementary long-tree cases | 2 | 56 |
| New rational-matrix cases 0–16 | 17 | 131 |
| **Total** | **115** | **5040** |

The first row has at most four deep nodes. In the second row, the subtree rooted at the first child a has at most four deep nodes; a·v₀≥|a|² and (4), tested in the original root decomposition, force a positive centroid projection. In the third row that subtree has height at most three, so 3b₃=3/4 is enough. In the fourth row at most two nodes have depth four, so every triple's negative-root projection is below 2b₄+b₃<242/256<1.

### 4.1 The height-four broom

The only remaining short tree has parents

    (−1,0,1,2,3,3,3,0).

Normalize |v₀|=1, put a=v₁, t=|a| and c=v₀·a/t≥t, and let z=v₇ be the other root child. The six-node tail rooted at a has height three; z lies in B(v₀/2,1/2).

For a root-cone triple not containing z,

    a·(v₀+Σ_T v) ≥ t²/4.

For a triple containing z and two tail nodes, the diameter ball and (3) give

    a·(v₀+z+x+y)
      ≥ t(3c/2−1/2−t/2) ≥ t(t−1/2).                    (8)

Thus t>9/16 makes every root-cone tetrahedron's projection exceed t/16.

For t≤9/16, use direction −v₀. The positive projection of each tail node is at most

    f(t)=t cos⁴((π−arccos t)/4)
        =(t/4)(1+√((1−t)/2))².

This function increases on 0<t≤9/16: with q=√((1−t)/2), its derivative has the sign of 2q+4q²−1>0. Using √(7/32)<15/32,

    f(t)≤f(9/16)<19881/65536,
    3f(t)<59643/65536<1.

The other root child has nonnegative v₀-projection. Hence every root-cone triple again has strictly positive total v₀-projection. This excludes the broom without a matrix table and also gives the quantitative reserves used below.

### 4.2 Two elementary long trees

The two additional arrays are

    (−1,0,1,2,3,4,1,0),
    (−1,0,1,2,3,4,0,6).

For each marked triple, take its full ancestor closure. If that closure has at most four deep nodes, use (4). Otherwise the triple includes the side branch's depth-two node and at most two nodes of the five-edge chain; its negative-root projection is at most b₂+b₄+b₅<229/256. Thus all their root-cone triples have projection greater than |v₀|²/16. The program verifies this finite classification over every triple.

All trees on at most seven nodes are already covered directly by (4): either the root has at least two children, or removing the sole root leaves a subtree of at most six nodes and one uses the first-child separator. This also reproduces the parent's |g−o|>R/196 bound where needed.

## 5. Seventeen affine-multiplier certificates

The source below contains the complete 17 parent arrays p, integer direction vectors C, and integer multiplier tables A. Set D=1000. For any of the 35 triples T⊂{1,…,7}, let s be the indicator of {0}∪T and define

    d=Σ_i (C_i/D)v_i,
    λ_j(T)=(1/D)Σ_(i∈T) A_(j,i),

where A's seven columns correspond to nodes 1,…,7. Its first seven rows multiply D_i=v_i·v_(p_i)−|v_i|² for i=1,…,7. Cases **0,1,2,6** have an eighth row multiplying H from (7); the program verifies that each of those trees really begins with the required two unbranched links. No other case uses H.

Negative individual entries of A are harmless: the relevant triple sums are all strictly positive. Exact verification gives |C|₁≤8000, λ_H≤5443/1000<6, and λ_j(T)>0 in every required case.

Let Q_T be the symmetric matrix of the scalar-coordinate quadratic form

    d·(v₀+Σ_T v)−Σ_(i=1)^7 λ_i(T)D_i−λ_H(T)H.          (9)

Equivalently, for a scalar coordinate vector x=(x₀,…,x₇), its form is

    xᵀQ_Tx=(Σ_i C_i x_i/D)(Σ_i s_i x_i)
             −Σ_i λ_i(x_i x_(p_i)−x_i²)
             −λ_H(−x₀x₂−59x₂²/256).

Summing this formula over Euclidean coordinates gives (9). The H term is omitted in the 13 non-H cases. To reconstruct M_T=512D Q_T with integer arithmetic, initialize

    M_ij=256(C_i s_j+s_i C_j).

Writing ℓ_i=Dλ_i, add 512ℓ_i to diagonal (i,i), and subtract 256ℓ_i at each of (i,p_i),(p_i,i). In an H case additionally add 118ℓ_H at (2,2) and 256ℓ_H at (0,2),(2,0).

**For all 595 matrices, M_T−4000I is positive definite.** Equivalently,

    Q_T ≻ I/128.                                        (10)

The complete source verifies every leading principal determinant exactly, independently reconstructs Q_T from (9), and checks a rational LDLᵀ factorization and the determinant/pivot ratios. It does not use a numerical solver, approximate eigenvalues, cached hulls, or unprinted certificates.

At centroid zero every D_i≥0 and every required H>0. Equations (9)–(10) therefore imply, for every root-cone triple,

    d·(v₀+Σ_T v)>(1/128)Σ_i |v_i|²>0.

Averaging over the actual positive tetrahedral volume weights contradicts 4d·g=0. Together with Section 4, this proves **V≥9** and the abstract distinct-triple obstruction.

## 6. Uniform centroid-separation constant

Here g need not be zero. Normalize R=|v₀|=1 and write ε=|g|. In the 13 certificate cases not using H, (10) and |d|≤8 give

    32ε≥4d·g>1/128,

hence ε>1/4096.

For an H case, suppose ε≤1/7168. Every node other than v₀ and v₁ has norm at most r=|v₂|, while v₀·v₁≥0. The root cone identity gives

    1−3r≤4v₀·g≤4ε,

so r>1/4. Therefore 4v₂·g≤4rε<r²/16. In the decomposition with apex v₂, all triples not containing v₀ have projection greater than r²/16. At least one triple containing v₀ must have projection at most 4v₂·g. Equation (6) yields

    H>−4v₂·g≥−4rε≥−4ε.                                (11)

Average (9) over the root decomposition. By (10), λ_H≤6 and the shadows' nonnegativity,

    4d·g>1/128−24ε.

Since |d|≤8, this forces 56ε>1/128, or ε>1/7168, contradicting the supposition.

The elementary categories have stronger reserves. The four-deep root and the two easy long trees give ε>1/64. The first-child four-deep case combines ε>t/64 with ε≥(1−3t)/4, yielding ε>1/196. The shallow first-child case similarly gives ε≥1/52. The short two-child case gives ε≥7/512. In the height-four broom, t>9/16 gives ε>1/64 by (8); t≤9/16 gives ε>5893/262144. Every one exceeds 1/7168. Rescaling proves the stated **|g−o|>R/7168** theorem. The constant is a certified conservative bound, not an optimized one, and is not a manufacturing-tolerance statement.

## 7. Exact sharpness of the dimension-independent relaxation

Take these nine planar vectors, dividing every row by 1000, with parent array (−1,0,1,2,3,4,5,6,0):

```text
 1000    0
  517  499
  151  591
 -153  496
 -331  295
 -376   79
 -344  -71
 -256 -189
  445 -496
```

All nine are vertices of their convex polygon. All eight parent links are actual polygon edges and strict escapes; the smallest D_i is **9/62500**. The root has strictly negative outgoing derivatives to all other points.

Their distinct-triple sum polygon, still in integer coordinates before division by 1000, has this complete counterclockwise cycle:

```text
-1051  303
 -976 -181
 -155 -756
 1189 -685
 1962    3
 1668 1090
  515 1586
 -333 1382
 -860  870
```

For every edge of this polygon and every reflected input point −v_i, the oriented integer cross-product guard is positive; its minimum is **1959**. Directly checking the stronger apex-excluded sum polygons gives the nine minimum integer guards

    [1959,2847,137765,327572,585078,872187,907037,762843,306739].

Thus (2) holds strictly in the plane, for every apex. This is a decisive counterexample to extending the dimension-independent tree/Σ₃ obstruction to nine points. It is **rank two**, not a full-dimensional three-polytope, and has no positive ordinary three-dimensional volume. It supplies neither a nine-vertex homogeneous mono-unstable solid nor an equality case for C_min. Any next V≥10 argument must exploit something beyond these dimension-independent escape and distinct-triple constraints.

## 8. Recovery capsule

The complete source below is `nova24_v9_recover.py`, **19433 UTF-8 bytes**, LF-terminated, SHA-256 **`4c15c82965977605609acbbce07ec9322d1f9491792f34c5a2c1310f992171fe`**. Reference environment actually executed: **CPython 3.13.5, standard library only**. The certificate inputs have no dependence on numerical discovery files or the mounted journal.

Run in an empty writable directory, with assertions enabled:

```sh
python -S nova24_v9_recover.py
```

Observed output, including an additional clean-directory replay with byte-identical outputs:

```text
NOVA24_PARENT_FOUR_DEEP_CERTIFICATES_PASS
NOVA24_ALL_595_SHIFTED_PD_AND_IDENTITIES_PASS
NOVA24_ALL_5040_TREES_115_ORBITS_COVERED_PASS
NOVA24_NINE_VECTOR_RANK_TWO_SHARPNESS_PASS
CONTROL_BYTES_SHA256 627 fc768d2c1916da5e3fc91b521b2a74720bb5c99dfa1b078e944ceeb39359b73b
CERTIFICATE_BYTES_SHA256 5705 34f501da2c4cabec97a55ca8311381a78eee0603c9c46c7c375a3f3dbf859af6
AUDIT_BYTES_SHA256 5543 e70bfddddc525a6e5599acf9efab8a49b6dbff398746c7aaf20942b3aed78143
NOVA24_V9_DISTINCT_TRIPLE_AND_CENTROID_GAP_RECOVERY_PASS
```

The generated files are `nova24_v9_certificate.json`, `nova24_v9_audit.json`, and `nova24_nine_vector_control.json`, with the byte counts and hashes above. The audit contains the entire tree-coverage count, each case's exact positivity summary and principal-minor-ledger hash, the parent identities, and the sharpness-control identity. Every matrix, determinant ledger and control polygon is regenerated from the literal inputs below.

The certificate coefficients were discovered numerically and then rounded once to the printed rationals. No numerical optimality, timeout status, or search failure is a premise. The runnable unit reproduces every mathematical assertion used from computation using exact inputs and exact arithmetic; the numerical discovery endpoints are not successor objects.

```python
"""Exact V>=9 escape-tree/distinct-triple certificate, Python 3.13.5 stdlib.
Run: python -S nova24_v9_recover.py (assertions must be enabled).
All inputs are literal. No journal, solver or former file is needed.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from collections import Counter
import hashlib
import json

assert __debug__
PARENTS = {
    'minimum-0001':
    '9cc634b1d007b03568764c4b4703096fe7216e39fbe9e0f5ea78b1ca4326a4f8',
    'minimum-0003':
    '520200e9b9541f54133e00931fc6ce2021fa752d2e8bb06df574ed1248720893'}
D = 1000
CASES = [
    ([-1, 0, 1, 2, 3, 4, 5, 6], [1000, 1000, 1000, 1000, -1000, -1000, -1000, -1000], [[3490, 1134, 1303, 1479, 1656, 1736, 1786], [11322, 3918, 4336, 4319, 3736, 3819, 3973], [11808, 2812, 5713, 5580, 5097, 4863, 4607], [13608, 4187, 4929, 7059, 5974, 5610, 5644], [12874, 3644, 4768, 3714, 7494, 6961, 5975], [9019, 2639, 3202, 2539, 2236, 7094, 6073], [4310, 994, 1558, 1681, 1653, -78, 6543], [2998, 564, 681, 924, 925, 1100, 1345]]),
    ([-1, 0, 1, 2, 3, 4, 5, 5], [1000, 1000, 1000, 1000, -1000, -1000, -1000, -1000], [[3427, 1090, 1248, 1471, 1565, 1780, 1780], [10808, 3912, 4274, 4301, 3516, 3964, 3964], [11326, 2776, 5620, 5703, 4887, 4837, 4837], [13440, 4240, 4717, 7359, 5792, 5758, 5758], [13082, 3419, 4492, 4243, 7604, 6490, 6490], [4396, 1225, 1438, 1466, 929, 6721, 177], [4396, 1225, 1437, 1466, 929, 176, 6721], [2776, 623, 773, 825, 868, 1220, 1220]]),
    ([-1, 0, 1, 2, 3, 4, 5, 4], [1000, 1000, 1000, 1000, -1000, -1000, -1000, -1000], [[3401, 1272, 1329, 1197, 1437, 1723, 1825], [11209, 4327, 4346, 3217, 3034, 3914, 4274], [11689, 3366, 5763, 4744, 4550, 4722, 5296], [13521, 5274, 5138, 6635, 5480, 5552, 6518], [9402, 3186, 3618, 1400, 5996, 5945, 1976], [4696, 1655, 1740, 759, 420, 6018, 1375], [3474, 1275, 1296, 713, 329, 273, 6552], [2931, 614, 786, 508, 750, 1245, 1149]]),
    ([-1, 0, 1, 2, 3, 4, 5, 3], [1000, 1000, 1000, 1000, 792, -1000, -1000, -1000], [[2035, 1531, 1566, 839, 955, 1388, 1277], [8488, 4470, 2673, 1792, 1486, 1791, 2469], [8919, 9929, 8196, 3545, 2136, 2777, 4232], [5750, 7514, 4946, 5103, 3963, 4408, 1103], [5535, 6128, 5158, -108, 6670, 6069, 155], [2159, 3102, 2606, 15, -225, 7357, 786], [2410, 2008, 1194, 856, -333, 33, 6074]]),
    ([-1, 0, 1, 2, 3, 4, 5, 2], [1000, 1000, 1000, 1000, -318, -1000, -1000, 297], [[2208, 1644, 1179, 1075, 1073, 1457, 898], [7977, 5552, 2824, 2027, 1719, 2128, 1755], [7776, 6689, 7838, 3865, 2362, 3349, 1030], [8256, 8507, 3857, 6369, 3859, 5460, -362], [6350, 6548, 4842, 1862, 5787, 7143, -1308], [2739, 2981, 1791, 1356, -368, 7544, -81], [2494, 1107, 327, 90, 65, -47, 4748]]),
    ([-1, 0, 1, 2, 3, 4, 5, 0], [1000, 1000, 1000, 1000, 624, -1000, -1000, 349], [[2036, 1290, 725, 1017, 1069, 1401, 1573], [7648, 4662, 3131, 2291, 1635, 1830, 2969], [9660, 6163, 6529, 3701, 2904, 2902, 1952], [9334, 8406, 4740, 7365, 3622, 4513, 652], [5367, 6690, 4195, 3708, 4991, 5738, 2703], [1251, 1588, 3025, 3425, -314, 5175, 4411], [360, 344, 336, -131, 87, 131, 2231]]),
    ([-1, 0, 1, 2, 3, 4, 4, 4], [1000, 1000, 1000, 1000, -1000, -1000, -1000, -1000], [[3259, 1306, 1290, 1304, 1625, 1625, 1625], [10692, 4425, 4103, 3242, 3686, 3686, 3686], [11253, 3182, 5680, 5210, 4864, 4864, 4864], [13585, 5563, 4343, 6666, 5918, 5917, 5918], [4241, 1523, 1555, 763, 5531, 806, 806], [4241, 1523, 1555, 764, 806, 5531, 806], [4241, 1523, 1555, 763, 806, 806, 5531], [2766, 752, 717, 578, 1006, 1006, 1006]]),
    ([-1, 0, 1, 2, 3, 4, 4, 3], [1000, 1000, 1000, 1000, 848, -1000, -1000, -1000], [[2040, 1606, 1394, 659, 1209, 1209, 1050], [8362, 4532, 2656, 1650, 1662, 1662, 2317], [8787, 9562, 8301, 2911, 2756, 2756, 3711], [5585, 7936, 4090, 4154, 4676, 4676, 382], [2461, 3426, 2454, 35, 6289, 64, 504], [2461, 3426, 2454, 35, 64, 6289, 504], [2092, 1868, 1048, 377, 120, 120, 5467]]),
    ([-1, 0, 1, 2, 3, 4, 4, 2], [1000, 1000, 1000, 1000, -366, -1000, -1000, 355], [[1975, 1887, 967, 990, 1276, 1276, 720], [6988, 5889, 2364, 1924, 1962, 1962, 1670], [7600, 6969, 7149, 3582, 3041, 3041, 771], [8188, 9454, 2550, 6224, 4914, 4914, -570], [3171, 3052, 1682, 1183, 6254, 287, -352], [3171, 3052, 1682, 1183, 287, 6254, -352], [1207, 1024, 298, 22, 67, 67, 4673]]),
    ([-1, 0, 1, 2, 3, 4, 4, 0], [1000, 1000, 1000, 1000, 865, -1000, -1000, 439], [[2059, 1149, 770, 936, 1217, 1217, 1400], [7527, 4981, 2308, 1828, 1921, 1921, 2457], [9387, 6543, 6098, 3613, 2967, 2967, 1800], [9899, 8234, 2667, 6405, 4668, 4668, -407], [2743, 3020, 1101, 1639, 4965, 799, 1660], [2743, 3020, 1101, 1639, 799, 4965, 1660], [223, 211, 226, -178, 151, 151, 2018]]),
    ([-1, 0, 1, 2, 3, 4, 3, 6], [1000, 1000, 1000, 1000, 22, -1000, 22, -1000], [[1463, 1316, 1113, 731, 1302, 731, 1302], [7354, 4284, 2999, 1530, 1984, 1530, 1984], [6932, 8077, 7122, 2825, 3158, 2825, 3158], [3282, 4120, 1896, 5329, 4747, -223, 284], [1848, 2652, 1805, 618, 6526, -368, 426], [3282, 4120, 1896, -223, 284, 5329, 4747], [1848, 2652, 1805, -368, 426, 618, 6526]]),
    ([-1, 0, 1, 2, 3, 4, 3, 3], [1000, 1000, 1000, 1000, 44, -1000, -419, -419], [[1532, 1428, 825, 735, 1275, 916, 916], [6402, 4305, 2752, 1425, 1954, 1696, 1696], [7426, 8203, 5182, 2692, 3092, 3090, 3090], [4294, 4412, 4082, 4671, 5232, -168, -168], [2768, 2867, 2508, 395, 6061, 100, 100], [1645, 1817, 395, -15, 71, 5181, 335], [1645, 1817, 395, -15, 71, 335, 5181]]),
    ([-1, 0, 1, 2, 3, 4, 3, 2], [1000, 1000, 1000, 1000, -468, -1000, -1000, 471], [[1881, 1628, 979, 934, 1230, 1181, 528], [6278, 5260, 2594, 1726, 1883, 2149, 1489], [8030, 7098, 5335, 2978, 3437, 3527, -36], [6786, 6456, 4441, 5091, 4801, 1318, -1450], [3694, 3567, 2683, 1117, 5690, 839, -1170], [2499, 2318, 547, 467, 697, 4772, 33], [1000, 1310, 595, -61, 31, 315, 4261]]),
    ([-1, 0, 1, 2, 3, 4, 3, 0], [1000, 1000, 1000, 1000, 665, -1000, -1000, 390], [[2100, 1203, 515, 729, 1109, 1313, 1375], [6723, 4547, 2103, 1712, 1653, 2252, 2190], [9912, 6641, 4932, 3132, 3003, 3826, 673], [7638, 5879, 1032, 5239, 3993, 1922, 40], [3325, 2836, 143, 344, 5659, 1282, 1681], [3544, 1183, 878, 420, 378, 4902, 907], [274, 186, 292, -8, 186, 37, 1682]]),
    ([-1, 0, 1, 2, 3, 4, 2, 6], [1000, 1000, 1000, 1000, -1000, -1000, 810, -1000], [[2267, 1419, 653, 986, 1046, 691, 1326], [6927, 4959, 2120, 2040, 1593, 1835, 2252], [6481, 5173, 4352, 3234, 2802, 649, 743], [7910, 7260, 1471, 4411, 4866, 272, 1753], [3830, 3548, 827, 1443, 4855, 26, 1500], [3781, 2823, 776, 762, -73, 3999, 2858], [3318, 2987, 466, 806, -129, 658, 5642]]),
    ([-1, 0, 1, 2, 3, 4, 2, 2], [1000, 1000, 1000, 563, -1000, -1000, 382, 382], [[2032, 943, 746, 867, 1260, 883, 883], [4465, 3864, 2378, 2105, 1863, 1777, 1777], [4717, 4686, 4604, 3170, 3006, 494, 494], [6029, 5588, 3679, 4893, 4484, 496, 496], [2818, 3107, 2142, 2789, 3767, 179, 179], [581, 522, 214, 216, 262, 4289, -42], [581, 522, 214, 216, 262, -42, 4289]]),
    ([-1, 0, 1, 2, 3, 4, 2, 0], [1000, 1000, 1000, 1000, -1000, -1000, 621, 510], [[2419, 1366, 731, 1230, 1147, 738, 1278], [7445, 4794, 2635, 2332, 1655, 2211, 1997], [8174, 5727, 4892, 3888, 3179, 596, -486], [8086, 8703, 3712, 5669, 4261, 862, 107], [3232, 3235, 980, 3198, 2855, 708, 2665], [1275, 702, 97, 490, 159, 4598, 617], [712, 426, 173, 186, 117, 96, 2053]]),
]

def bareiss_minors(M):
    """All leading principal determinants, fraction-free, no pivoting."""
    A = [list(row) for row in M]
    previous, minors = 1, []
    for k in range(len(A)):
        pivot = A[k][k]
        assert pivot > 0
        minors.append(pivot)
        for i in range(k+1, len(A)):
            for j in range(k+1, len(A)):
                numerator = pivot*A[i][j]-A[i][k]*A[k][j]
                assert numerator % previous == 0
                A[i][j] = numerator//previous
        previous = pivot
    return minors

def ldlt_pivots(A):
    """A separate rational LDL^T positive-definiteness check."""
    n = len(A)
    L = [[F(i == j) for j in range(n)] for i in range(n)]
    d = []
    for j in range(n):
        dj = A[j][j]-sum(L[j][k]**2*d[k] for k in range(j))
        assert dj > 0
        d.append(dj)
        for i in range(j+1, n):
            L[i][j] = (A[i][j]-sum(L[i][k]*L[j][k]*d[k]
                                      for k in range(j)))/dj
    return d

def depth(p):
    h = [0]*len(p)
    for i in range(1, len(p)):
        assert 0 <= p[i] < i
        h[i] = h[p[i]]+1
    return h

def tree_key(p, root=0):
    return '('+''.join(sorted(tree_key(p, i) for i in range(1, len(p))
                             if p[i] == root))+')'

def canonical(key):
    p, stack = [], []
    for ch in key:
        if ch == '(':
            p.append(stack[-1] if stack else -1)
            stack.append(len(p)-1)
        else:
            assert ch == ')' and stack
            stack.pop()
    assert not stack
    return p

# The analytic four-deep-node lemma: the only two joint cases.
B = [F(0), F(0), F(1,8), F(1,4), F(89,256), F(27,64), F(1), F(1)]
assert F(5) < F(9,4)**2
assert B[2]+B[4]+B[5] == F(229,256) < F(15,16)
assert B[4]+2*B[3] == F(217,256) < F(15,16)
assert 2*B[4]+B[2] == F(210,256) < F(15,16)
assert B[4]+B[5] == F(197,256)
assert 1-F(197,256) == F(59,256)
old_specs = [
    ([-1,0,1,2,3,4], [128,208,352,336,192],
     [75,5504,333632,15370240,434778112,56623104]),
    ([-1,0,1,2,3,3], [128,208,368,176,176],
     [75,5504,333632,9116672,817229824,5266866176])]
for p, diagonal, expected in old_specs:
    M = [[0]*6 for _ in range(6)]
    M[0][0] = 75
    for i, z in enumerate(diagonal, 1):
        M[i][i] += z
        M[i][p[i]] -= z//2
        M[p[i]][i] -= z//2
    for i in (3,4,5):
        M[0][i] += 40
        M[i][0] += 40
    assert bareiss_minors(M) == expected
    ldlt_pivots([[F(x) for x in row] for row in M])
print('NOVA24_PARENT_FOUR_DEEP_CERTIFICATES_PASS')

# Check the finite case split used in the written four-deep lemma.
nt, ns, chains, forks = 0, 0, 0, 0
for n in range(1,9):
    for tail in product(*(range(i) for i in range(1,n))):
        p = [-1]+list(tail)
        h = depth(p)
        if sum(t >= 2 for t in h) > 4:
            continue
        assert max(h) <= 5
        nt += 1
        for T in combinations(range(n),3):
            ns += 1
            ds = sorted(h[i] for i in T)
            if max(h) == 5 and ds == [3,4,5]:
                i,j,k = sorted(T,key=lambda i:h[i])
                assert p[k] == j and p[j] == i
                chains += 1
            elif max(h) <= 4 and ds == [3,4,4]:
                i,j,k = sorted(T,key=lambda i:h[i])
                assert p[j] == i and p[k] == i
                forks += 1
            else:
                assert sum(B[h[i]] for i in T) < F(15,16)
assert (nt,ns,chains,forks) == (3310,166802,28,28)

# New scalar bounds for the height-four broom and the centroid gap.
assert 2*B[4]+B[3] == F(242,256) < 1
assert F(7,32) < F(15,32)**2
assert F(9,64)*F(47,32)**2 == F(19881,65536)
assert 1-3*F(19881,65536) == F(5893,65536)
assert min(F(1,196),F(1,52),F(7,512),F(5893,262144),F(1,64)) > F(1,7168)
assert F(1,128)/(4*(8+6)) == F(1,7168)
assert F(1,7168) < F(1,256) < F(1,16)

# Verify every marked-triple quadratic identity and strict margin exactly.
case_map = {tuple(p): i for i,(p,c,a) in enumerate(CASES)}
assert len(case_map) == 17
extra_ids = {0,1,2,6}
ledger = []
for case_id,(p,C,A) in enumerate(CASES):
    extra = len(A) == 8
    assert len(A) == 7+int(extra)
    assert extra == (case_id in extra_ids)
    assert len(C) == 8 and all(len(row) == 7 for row in A)
    assert sum(abs(x) for x in C) <= 8*D
    if extra:
        assert p.count(0) == 1 and p.count(1) == 1 and p[2] == 1
    lower_lambda, upper_H, min_ldl = None, 0, None
    minor_digest = hashlib.sha256()
    for T in combinations(range(1,8),3):
        s = [int(i == 0 or i in T) for i in range(8)]
        ell = [sum(row[j-1] for j in T) for row in A]
        assert min(ell) > 0
        lower_lambda = min(ell) if lower_lambda is None else min(lower_lambda,min(ell))
        if extra:
            assert ell[7] <= 6*D
            upper_H = max(upper_H,ell[7])
        # Integer matrix M = 512*D*Q_T.
        M = [[256*(C[i]*s[j]+s[i]*C[j]) for j in range(8)] for i in range(8)]
        for i in range(1,8):
            z = ell[i-1]
            M[i][i] += 512*z
            M[i][p[i]] -= 256*z
            M[p[i]][i] -= 256*z
        if extra:
            z = ell[7]
            M[2][2] += 118*z
            M[0][2] += 256*z
            M[2][0] += 256*z
        # Independently form Q from its rank-two objective and primitives.
        Q = [[F(C[i]*s[j]+s[i]*C[j],2*D) for j in range(8)] for i in range(8)]
        for i in range(1,8):
            lam = F(ell[i-1],D)
            Q[i][i] += lam
            Q[i][p[i]] -= lam/2
            Q[p[i]][i] -= lam/2
        if extra:
            lam = F(ell[7],D)
            Q[2][2] += F(59,256)*lam
            Q[0][2] += lam/2
            Q[2][0] += lam/2
        assert all(Q[i][j] == F(M[i][j],512*D) for i in range(8) for j in range(8))
        # Certify Q_T - I/128 is positive definite, not merely Q_T.
        for i in range(8):
            M[i][i] -= 4*D
            Q[i][i] -= F(1,128)
        minors = bareiss_minors(M)
        pivots = ldlt_pivots(Q)
        previous = 1
        for minor,pivot in zip(minors,pivots):
            assert pivot == F(minor,previous*512*D)
            previous = minor
        mn = min(pivots)
        min_ldl = mn if min_ldl is None else min(min_ldl,mn)
        minor_digest.update((' '.join(map(str,minors))+'\n').encode('ascii'))
    ledger.append({'case':case_id,'min_lambda_integer':lower_lambda,
                   'max_H_lambda_integer':upper_H,'min_LDL_pivot':str(min_ldl),
                   'minor_ledger_sha256':minor_digest.hexdigest()})
print('NOVA24_ALL_595_SHIFTED_PD_AND_IDENTITIES_PASS')

# Complete rooted-tree coverage. This enumerates trees, not polyhedral graphs.
LABEL_COUNTS, ORBIT_COUNTS = Counter(), Counter()
keys = set()
for tail in product(*(range(i) for i in range(1,8))):
    keys.add(tree_key([-1]+list(tail)))
assert len(keys) == 115
broom = [-1,0,1,2,3,3,3,0]
easy_long = {(-1,0,1,2,3,4,1,0),(-1,0,1,2,3,4,0,6)}

def classify(p):
    h = depth(p)
    if p.count(0) >= 3:
        assert sum(t >= 2 for t in h) <= 4
        return 'four_deep_root'
    if p.count(0) == 1 and p.count(1) >= 2:
        assert sum(t >= 3 for t in h) <= 4
        return 'four_deep_first_child'
    if max(h) <= 4:
        if p.count(0) == 1:
            assert max(t-1 for t in h[1:]) <= 3
            return 'shallow_first_child'
        assert p.count(0) == 2
        if h.count(4) < 3:
            assert max(sum(B[h[i]] for i in T)
                       for T in combinations(range(1,8),3)) <= F(242,256)
            return 'shallow_root'
        assert p == broom
        return 'height_four_broom'
    if tuple(p) in easy_long:
        for T in combinations(range(1,8),3):
            ancestors = {0}
            for j in T:
                while j > 0:
                    ancestors.add(j)
                    j = p[j]
            if sum(h[j] >= 2 for j in ancestors) > 4:
                assert sum(B[h[j]] for j in T) <= F(229,256)
        return 'easy_long_root'
    assert tuple(p) in case_map, p
    return 'matrix_case_%02d'%case_map[tuple(p)]

for key in sorted(keys):
    p = canonical(key)
    assert tree_key(p) == key
    ORBIT_COUNTS[classify(p)] += 1
for tail in product(*(range(i) for i in range(1,8))):
    p = canonical(tree_key([-1]+list(tail)))
    LABEL_COUNTS[classify(p)] += 1
assert sum(LABEL_COUNTS.values()) == 5040
assert all(ORBIT_COUNTS['matrix_case_%02d'%i] == 1 for i in range(17))
print('NOVA24_ALL_5040_TREES_115_ORBITS_COVERED_PASS')

# Exact nine-vector sharpness control. Rank TWO; it is not a 3D solid.
I9 = [(1000,0),(517,499),(151,591),(-153,496),(-331,295),
      (-376,79),(-344,-71),(-256,-189),(445,-496)]
P9 = [-1,0,1,2,3,4,5,6,0]

def turn(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def hull2(points):
    pts = sorted(set(points))
    low,high = [],[]
    for v in pts:
        while len(low) > 1 and turn(low[-2],low[-1],v) <= 0:
            low.pop()
        low.append(v)
    for v in reversed(pts):
        while len(high) > 1 and turn(high[-2],high[-1],v) <= 0:
            high.pop()
        high.append(v)
    out = low[:-1]+high[:-1]
    assert len(out) >= 3
    assert all(turn(out[i],out[(i+1)%len(out)],out[(i+2)%len(out)]) > 0
               for i in range(len(out)))
    assert all(turn(out[i],out[(i+1)%len(out)],v) >= 0
               for i in range(len(out)) for v in pts)
    return out

H9 = hull2(I9)
assert len(H9) == 9
assert all(turn(H9[i],H9[(i+1)%9],(0,0)) > 0 for i in range(9))
E9 = [sum(I9[i][k]*(I9[p][k]-I9[i][k]) for k in range(2))
      for i,p in enumerate(P9) if p >= 0]
assert min(E9) == 144 > 0
assert all(sum(I9[0][k]*(v[k]-I9[0][k]) for k in range(2)) < 0 for v in I9[1:])
assert all(any({I9[i],I9[p]} == {H9[j],H9[(j+1)%9]} for j in range(9))
           for i,p in enumerate(P9) if p >= 0)
S9 = hull2([tuple(sum(I9[i][k] for i in T) for k in range(2))
            for T in combinations(range(9),3)])
G9 = [turn(S9[j],S9[(j+1)%len(S9)],(-v[0],-v[1]))
      for j in range(len(S9)) for v in I9]
assert min(G9) == 1959 > 0
root_guards = []
for a in range(9):
    vertices = [i for i in range(9) if i != a]
    S = hull2([tuple(sum(I9[i][k] for i in T) for k in range(2))
               for T in combinations(vertices,3)])
    root_guards.append(min(turn(S[j],S[(j+1)%len(S)],(-I9[a][0],-I9[a][1]))
                           for j in range(len(S))))
assert min(root_guards) > 0
control = {'D':1000,'integer_points_2d':I9,'parents':P9,
           'rank':2,'polygon':H9,'distinct_triple_polygon':S9,
           'minimum_escape':str(F(min(E9),1000000)),
           'minimum_global_integer_guard':min(G9),
           'per_apex_integer_guards':root_guards,
           'scope':'Rank-two relaxation only: no three-dimensional solid volume.'}
cc = (json.dumps(control,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
Path('nova24_nine_vector_control.json').write_bytes(cc)
print('NOVA24_NINE_VECTOR_RANK_TWO_SHARPNESS_PASS')
print('CONTROL_BYTES_SHA256',len(cc),hashlib.sha256(cc).hexdigest())

certificate = {'D':D,'cases':[{'p':p,'c':c,'a':a} for p,c,a in CASES]}
raw = (json.dumps(certificate,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
assert len(raw) == 5705
assert hashlib.sha256(raw).hexdigest() == '34f501da2c4cabec97a55ca8311381a78eee0603c9c46c7c375a3f3dbf859af6'
Path('nova24_v9_certificate.json').write_bytes(raw)
report = {'identity':'NOVA24_V9_DISTINCT_TRIPLE_V1','parents':PARENTS,
          'reference_python':'3.13.5','denominator':D,'matrix_count':595,
          'strict_eigenvalue_lower_bound':'1/128','centroid_gap':'1/7168',
          'four_deep_tree_checks':[nt,ns,chains,forks],
          'labeled_coverage':dict(sorted(LABEL_COUNTS.items())),
          'orbit_coverage':dict(sorted(ORBIT_COUNTS.items())),
          'case_positivity':ledger,'rank_two_control_sha256':hashlib.sha256(cc).hexdigest()}
rr = (json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
Path('nova24_v9_audit.json').write_bytes(rr)
print('CERTIFICATE_BYTES_SHA256',len(raw),hashlib.sha256(raw).hexdigest())
print('AUDIT_BYTES_SHA256',len(rr),hashlib.sha256(rr).hexdigest())
print('NOVA24_V9_DISTINCT_TRIPLE_AND_CENTROID_GAP_RECOVERY_PASS')
```

## 9. Research interpretation and continuation

The useful change was to stop asking only whether a root-coned tetrahedron can have negative root projection. First-child directions eliminate many additional cases, but four eight-node chain/fork architectures survive that route. Applying the *same actual-volume identity at a second apex* forces (7). Affine dependence of the SOS multipliers on the marked triple then makes the complete remaining proof compact: 17 tables, not a separately optimized certificate for every geometry or face lattice.

The new theorem leaves no eight-vertex mono-unstable realization case unresolved in its stated scope. It does not solve the nine-vertex actual-volume problem, determine the global minimum, or improve the facet lower bound to nine. The exact rank-two control shows precisely why another dimension-independent Σ₃ exclusion cannot by itself provide V≥10. The next actual-solid obstruction would need three-dimensional realization/volume information beyond (2), or the joint facet-side mass and equilibrium constraints.

For the Gömböc problem the next possible equality boundary is **E15,V9,F8,C30**. This statement uses the parent's independent F≥8 theorem; it does not apply the new primal moment relaxation to a polar at the wrong centroid. Matching existence remains a separate obligation.

This is a self-contained analytic/computer-assisted proof with executed rational certificates and two distinct positivity algorithms, not a proof-assistant formalization or an external peer review. No claim of publication priority is made.

Convenience copies: complete recovery source (`nova24_v9_recover.py`), literal rational tables (`nova24_v9_certificate.json`), exact audit (`nova24_v9_audit.json`), and rank-two sharpness control (`nova24_nine_vector_control.json`). These copies supplement the full inline recovery capsule; none is its sole source.
