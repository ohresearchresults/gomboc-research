# minimum-0001

Historical AI scientific report · saved 2026-09-07 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Universal centroid obstruction: an independent V ≥ 8 proof

## Result and status

I obtain a universal lower bound, together with a quantitative version:

**Centroid-separation theorem.** Let K be a full-dimensional convex 3-polytope with at most seven true vertices. Suppose an interior reference point o has exactly one nondegenerate unstable vertex. Let g be the ordinary uniform-volume centroid and R = max{|v−o| : v is a vertex}. Then

**|g−o| > R/196.**

Consequently, every homogeneous mono-unstable convex 3-polytope has **V ≥ 8**. In particular, every strict homogeneous polyhedral Gömböc has **V ≥ 8, E ≥ 12, F ≥ 6 and C = 2E ≥ 24**. The proof permits nonsimplicial faces, nonsimple vertices and weak shadow inequalities. It does not assume monostability, symmetry, prescribed rays, a graph type, or a radius ratio.

Two additional reductions are proved below. First, the unique unstable vertex of a homogeneous mono-unstable polytope leaves at least **five other vertices outside its closed diameter ball**. Second, a strict homogeneous polyhedral Gömböc necessarily satisfies **R/r ≤ 27**, where r and R are its actual centroidal inradius and circumradius. The latter is a derived bound, not an extra hypothesis.

This independently establishes the V ≥ 8 statement that the journal had left pending recovery of its old certificate collection; it does not recover or validate that collection. The latest journal explicitly distinguished that pending claim from the externally established V ≥ 7 baseline. :contentReference[oaicite:0]{index=0} The primary paper by Bozóki–Domokos–Papp–Regős proves V ≥ 7 and explains that its root-direction necessary systems leave some seven-vertex cases unresolved. :contentReference[oaicite:1]{index=1}

The exact global minimum is not determined here. The journal-accepted upper witness remains FUSION258_PN03_C1374, with (V,E,F) = (258,687,431); its full audits were not rerun in this assignment. Thus this handoff alone gives **24 ≤ C_min ≤ 1374**, not equality at either endpoint. :contentReference[oaicite:2]{index=2}

## 1. The two necessary structures

Translate o to 0. All norms and dot products until explicitly stated otherwise use this same reference point.

### 1.1 Escape trees

At a vertex v, nondegenerate instability means v·(w−v) < 0 for every adjacent vertex w. If v is not unstable, at least one adjacent vertex p satisfies

    v·p ≥ |v|².                                      (1)

Indeed, the incident edge directions generate the tangent cone: a linear functional that is strictly negative on every incident edge is strictly negative on every other direction into the polytope. The adjacent-shadow criterion is also the starting point of the published approach. :contentReference[oaicite:3]{index=3}

For distinct p and v, (1) implies

    |p|²−|v|² = 2v·(p−v)+|p−v|² ≥ |p−v|² > 0.       (2)

Choose one such parent for every nonunstable vertex. With a unique unstable vertex u, these arrows form a tree directed toward u. Every vertex reaches u, and u is the unique maximum-radius vertex. A child v lies in its parent's closed diameter ball:

    |v−p/2| ≤ |p|/2.                                 (3)

“Children” below refer to this selected tree, not to the physical degree of a polyhedral vertex. In particular, a root with one tree child can still have many true incident edges.

### 1.2 The actual volume-centroid identity

Fix any actual vertex a. Triangulate each maximal face not containing a, using only that face's vertices, and cone each triangle T = (b,c,d) from a. These positive-volume tetrahedra partition K up to their boundaries. Put λ_T = Vol(a,b,c,d)/Vol(K). Then

    λ_T > 0,     Σ_T λ_T = 1,
    4g = a + Σ_T λ_T(b+c+d).                         (4)

This is an identity for uniform solid volume, not for equal vertex masses. Internal face diagonals are integration devices and are not counted as true edges. The published method likewise uses a root-based tetrahedral decomposition; the change here is retaining the vector identity and allowing a separator different from the maximum-radius vertex. :contentReference[oaicite:4]{index=4}

## 2. A dimension-independent four-deep-vertices lemma

Consider any finite rooted tree of nonzero vectors, root a, satisfying (1) on every child–parent link. A vertex is called deep when its tree distance from a is at least two.

**Lemma.** If the tree has at most four deep vertices, then for every three distinct vertices x,y,z in the tree,

    a·(x+y+z) > −(15/16)|a|².                        (5)

The number of depth-one children is unrestricted. The lemma is valid in any Euclidean dimension.

### 2.1 Individual depth bounds

Let v have depth d. Along the root-to-v chain, let the successive ray angles be α_i. Equation (1) gives

    |v_i|/|v_(i−1)| ≤ cos α_i,     0 ≤ α_i < π/2.

If a·v < 0, append the angle π−angle(a,v). The sum of the d+1 angles is at least π. Since log cos is concave and decreasing on [0,π/2),

    −a·v/|a|² ≤ b_d := cos(π/(d+1))^(d+1),  d ≥ 2. (6)

For depths zero and one the projection is nonnegative, so set b_0 = b_1 = 0 as upper bounds for its negative part. The only other values required are

    b_2 = 1/8,
    b_3 = 1/4,
    b_4 = (11+5√5)/64 < 89/256,
    b_5 = 27/64.                                    (7)

The rational inequality for b_4 follows from √5 < 9/4. There is no lower bound assumed on any vertex radius.

### 2.2 Two explicit joint inequalities

Separate depth estimates are wasteful when the three selected vertices share ancestors. Two six-vector configurations provide the needed improvement. Number their vertices 0,...,5, with root v_0 = a; in each configuration the selected sum is v_3+v_4+v_5.

For the **chain**, parents are

    p = (−1,0,1,2,3,4).

For the **fork**, parents are

    p = (−1,0,1,2,3,3).

Define these integer matrices, with every row printed in full:

```text
M_chain =
[ 75, -64,    0,   40,   40,  40]
[-64, 128, -104,    0,    0,   0]
[  0,-104,  208, -176,    0,   0]
[ 40,   0, -176,  352, -168,   0]
[ 40,   0,    0, -168,  336, -96]
[ 40,   0,    0,    0,  -96, 192]

M_fork =
[ 75, -64,    0,   40,  40,  40]
[-64, 128, -104,    0,   0,   0]
[  0,-104,  208, -184,   0,   0]
[ 40,   0, -184,  368, -88, -88]
[ 40,   0,    0,  -88, 176,   0]
[ 40,   0,    0,  -88,   0, 176]
```

Their successive leading principal determinants are, respectively,

```text
chain: 75, 5504, 333632, 15370240, 434778112, 56623104
fork:  75, 5504, 333632,  9116672, 817229824, 5266866176
```

All are positive, so both matrices are positive definite by Sylvester's criterion. This is a fully specified rational certificate, not a claim based on numerical eigenvalues.

Write D_i = v_i·v_(p_i)−|v_i|² ≥ 0. The positive weights are

    chain: (8/5,13/5,22/5,21/5,12/5),
    fork:  (8/5,13/5,23/5,11/5,11/5).

For each Euclidean coordinate k, put X_k = (v_0k,...,v_5k). Direct expansion gives, for either matrix and its listed weights,

    (1/80) Σ_k X_kᵀ M X_k
      = (15/16)|a|² + a·(v_3+v_4+v_5) − Σ_i weight_i D_i.

The left side is strictly positive because a ≠ 0. Adding back the nonnegative weighted D_i proves

    a·(v_3+v_4+v_5) > −(15/16)|a|²                 (8)

for both configurations.

### 2.3 Exhaustive structural proof of the lemma

At most four deep vertices implies height at most five.

If the height is five, its ancestor chain already uses all four deep vertices, at depths 2,3,4,5. Every other vertex has depth at most one. A selected triple of depths (3,4,5) is exactly the chain configuration in §2.2. Every other triple has total negative-projection bound at most

    b_2+b_4+b_5 < 229/256 < 15/16.

If the height is at most four, three distinct depth-four vertices would require at least five deep vertices: ancestors at depths two and three, plus those three vertices. Therefore at most two selected vertices have depth four.

The only exceptional depth pattern is (3,4,4). The two depth-four vertices must share their depth-three parent: otherwise their depth-three parents and at least one depth-two ancestor already give five deep vertices. The selected depth-three vertex must be that parent, since a different one would again exceed the budget. Their ancestors and the selected triple therefore form exactly the fork configuration.

Every nonexceptional triple has negative-projection bound at most one of

    b_4+2b_3 < 217/256 < 15/16,
    2b_4+b_2 < 210/256 < 15/16,
    3b_3 = 3/4 < 15/16.

Together with (8), these cases prove (5). This proof covers all tree shapes; it does not enumerate or presuppose a polyhedral graph.

## 3. The universal lower bound and the centroid gap

Let N ≤ 7, and choose an escape tree rooted at the unique unstable vertex u. Put R = |u|.

### Case A: u has at least two tree children

There are at most N−1−2 ≤ 4 deep vertices relative to u. Apply (5) to every triangle triple in the tetrahedral identity (4), coned from u:

    4u·g = |u|² + Σ_T λ_T u·(b+c+d)
           > |u|²/16.

Thus

    |g| > R/64.                                     (9)

### Case B: u has exactly one tree child w

Every other vertex belongs to the subtree rooted at w, which has at most six vertices. This subtree has at most four deep vertices: if it is nontrivial, at least one vertex is a depth-one child; if it is trivial the assertion is immediate. Put r_w = |w|. Equation (1) gives w·u ≥ r_w².

Apply (5), now with root w, to every triple in the SAME decomposition coned from u. This is the crucial change of separating direction:

    4w·g = w·u + Σ_T λ_T w·(b+c+d)
           > r_w²/16.

Therefore

    |g| > r_w/64.                                   (10)

All vertices other than u have radius at most r_w, by norm increase toward w. Equation (4) also gives

    |4g−u| ≤ 3r_w,
    |g| ≥ (R−3r_w)/4.                               (11)

Set t = r_w/R. If t ≥ 16/49, (10) yields |g| > R/196. If t < 16/49, (11) gives |g| > R/196. Case A is stronger. This proves the centroid-separation theorem.

Taking g = 0 contradicts both cases, so **N ≥ 8** for a homogeneous mono-unstable polytope. Every true vertex of a full-dimensional convex 3-polytope has degree at least three, hence 2E ≥ 3V. Euler's identity gives F = E−V+2 and C = V+E+F−2 = 2E. Thus **E ≥ 12, F ≥ 6, C ≥ 24**.

### A further universal structural obstruction

For any number of vertices, let

    B_u = {v ≠ u : v·(u−v) ≥ 0}.

These are exactly the other vertices in the closed diameter ball with endpoints 0 and u. Choose u as parent of every member of B_u, and choose escape parents for the remaining vertices. Here a parent may be any vertex satisfying (1), even when the corresponding segment is not a true edge; such links certify the inequality and are not added to the feature count. Strict norm increase still guarantees a rooted tree. If there were at most four vertices outside B_u∪{u}, the four-deep-vertices lemma would give u·g > |u|²/64.

Therefore, when g = 0,

    #{v ≠ u : v·(u−v) < 0} ≥ 5.                    (12)

An eight-vertex homogeneous mono-unstable candidate consequently has only one or two vertices directly shadowed by its unique unstable root. This is a geometry-independent restriction on the complete shadow relation, not a prescribed normal pool or a restriction to a particular realization family.

## 4. A universal centroidal aspect-ratio reduction

This section uses BOTH S = 1 and U = 1, unlike the vertex lower bound.

### 4.1 Centroid asymmetry, proved from actual volume

For any z ∈ K, cone a triangulated boundary from z and use the same tetrahedral centroid formula; zero-volume pieces can be omitted. If the solid centroid is 0, then

    −z/3 = Σ_T λ_T (b+c+d)/3 ∈ K.

Hence −K/3 ⊆ K. For the radial function ρ on S² this implies

    ρ(s)/ρ(−s) ≤ 3, for every s ∈ S².               (13)

This is a statement about the original solid's centroid. It invokes neither the centroid of its polar nor the Santaló point.

### 4.2 Antipodal-path intersection lemma

If γ joins p to −p on S², and η joins q to −q, then η meets γ∪(−γ).

Here is a topological proof adequate for the open-set application below. Approximate γ inside its open neighborhood by a polygonal path in general position, then project it to the real projective plane. The projected closed walk is noncontractible because its lift has antipodal, rather than identical, endpoints. Decompose its finite embedded graph walk into simple cycles. At least one cycle is noncontractible: otherwise the original walk would be trivial in the fundamental group Z/2. The lift of that cycle is an antipodally invariant simple closed curve C contained in γ∪(−γ). By the Jordan curve theorem C separates S² into two disks. The antipodal map swaps them: it reverses the orientation of S² but, as a fixed-point-free map of C, preserves the orientation of C. Consequently q and −q lie in different components unless one already lies on C. Every joining path η must meet C. Polygonal approximation can be chosen disjoint from η if the original compact sets were disjoint, so the conclusion also holds for the original paths.

### 4.3 Two extrema force R/r ≤ A³

More generally, let a positive continuous radial function have a unique local minimum and maximum, and let

    A = max_s ρ(s)/ρ(−s),  r = min ρ,  R = max ρ.

Every nonempty strict sublevel set is connected. Otherwise each of two components would attain a minimum below its boundary level, giving two local minima. The analogous assertion holds for strict superlevel sets. These open subsets of S² are locally path connected, so connectedness supplies paths.

Suppose R > A³r. Choose t with Ar < t < R/A². If p is the minimum direction, both p and −p lie in {ρ < t}; join them by γ there. Equation ρ(−s) ≤ Aρ(s) implies

    γ∪(−γ) ⊂ {ρ < At}.

If q is the maximum direction, both q and −q lie in {ρ > At}, since ρ(−q) ≥ R/A > At. Join them by η inside that superlevel set. This contradicts the antipodal-path lemma. Therefore

    R/r ≤ A³.                                       (14)

For a convex polyhedron at an interior reference, local radial maxima are exactly the nondegenerate unstable vertices. A local radial maximum cannot lie inside an edge or face, because squared distance is strictly convex on any segment there. At a vertex, a zero or positive outgoing derivative likewise rules out a local maximum. Local radial minima lie in facet interiors and are their perpendicular feet; at an edge or vertex the direction toward the interior origin is a combination of boundary tangent directions, one of which must decrease squared distance. Thus a strict (1,1,0) polyhedron supplies the unique local minimum and maximum required above.

Combining (13) and (14) proves **R/r ≤ 27** for every strict homogeneous polyhedral Gömböc. After a similarity one may therefore impose

    B(0,1/27) ⊆ K ⊆ B(0,1).                        (15)

This gives a nondegenerate compact geometric normalization for unrestricted finite-feature searches. It does not give a uniform positive equilibrium margin; equilibrium walls remain possible in limits.

The topological step is essential. Centred ellipsoids with semiaxes (L,2,1), L > 2, have antipodal ratio A = 1 but R/r = L. Thus centroid asymmetry alone does not control the global radius ratio, and (15) must not be applied to arbitrary centred bodies or to an arbitrary one-sided monostatic class.

## 5. An exact counterexample to root-direction-only tetrahedral positivity

A tempting stronger intermediate assertion is false:

> With at most seven vertices and one unstable vertex at an interior reference, every tetrahedron in a root-coned decomposition has positive centroid projection in the direction of the unstable root.

The following exact construction disproves it, with a genuine convex polyhedron rather than a free point sequence.

Start z_0 = 1 in the complex plane and recursively set z_i = (999/1000)a_i z_(i−1), where

    a_1 = a_2 = a_3 = a_4 = (9+6i)/13,
    a_5 = (25+10i)/29,
    a_6 = (4+2i)/5.

Set v_i = (Re z_i, Im z_i, h_i), with h_1 = −1/100000, h_5 = 1/1000 and all other h_i = 0. Let K_7 = conv{v_0,...,v_6}. This is a complete rational definition, independent of any journal checkpoint.

The exact verifier below exhaustively reconstructs its supporting triples. The true f-vector is (7,15,10), the origin is strictly interior, every chain link i→i−1 is a true edge and a strict escape, and v_0 is the only unstable vertex relative to 0. Its complete outward maximal triangular cycles are

```text
[0,1,5] [0,6,1] [0,5,6] [1,3,2] [1,2,5]
[1,4,3] [1,6,4] [2,3,5] [3,4,5] [4,6,5]
```

The last triangle is an actual nonincident facet. Its tetrahedron coned from v_0 satisfies the exact negative projection

    v_0·(v_0+v_4+v_5+v_6)
      = −14230860327418981631273/103533625000000000000000 < 0.

Nevertheless the first-child separator succeeds for EVERY distinct triple from the six nonroot vertices:

    min v_1·(v_0+v_i+v_j+v_k)
      = 27432678191356305112352299/207067250000000000000000000 > 0.

Its ordinary centroid is approximately (0.0815435709548, 0.2359209670254, 0.0002475), not 0. At that actual centroid its unstable vertices are exactly {0,3,6}. The solid is therefore not a homogeneous mono-unstable example and not a Gömböc. No stable/saddle census is asserted for this control. The counterexample pinpoints why changing the separating vector, while keeping the actual vector centroid identity, is substantive.

## 6. Deterministic recovery and executed checks

The analytic proof requires only the inequalities and two printed matrices above. The following complete program additionally reconstructs both matrix certificates, verifies their exact principal determinants, checks all rooted-tree cases through eight nodes that have at most four deep vertices, generates the rational counterexample, reconstructs its true hull, integrates its centroid in two different cone decompositions, and checks both reference-relative and own-centroid instability statements.

Environment actually used: **CPython 3.13.5, standard library only**. Run with assertions enabled:

```sh
python -S v8_recovery.py
```

It creates `tree_certificates.json` and `chain7_counterexample.json` in the current directory. An optional first argument changes only the counterexample output path. Required observed markers are

```text
EXACT_CHAIN_AND_FORK_PD_PASS
EXACT_TREE_CASES_PASS 3310 166802 28 28
CERTIFICATE_BYTES_SHA256 477 e3c50a5bf3cc1ad305136fa07903d12f1fd99a51e5295be692966ca2cbe9b82f
EXACT_CHAIN7_COUNTEREXAMPLE_PASS 913 6acf0c0a67584e3db8cf68a7d12b6a25a2696473dc70bd4e6799a5d32e17d97b
OWN_CENTROID_UNSTABLE_VERTICES [0, 3, 6]
```

The 3,310 count concerns increasing-labeled rooted trees satisfying the four-deep condition; the 166,802 count concerns all their marked triples. These checks support the short structural proof and are not a claimed enumeration of all geometric polyhedra.

The exact source below, encoded as UTF-8 with LF and a final LF, is **6,688 bytes**, SHA-256 **5426236d34537e6b49fcbd1ecc523a174346db12763fff52075d7656ac3580eb**. The two generated exact-object byte counts and hashes are given in the markers. No compressed stream, hidden helper, solver, former archive, or parent coordinates are required.

```python
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import sys

# Both six-variable certificates are dimension-independent.
def determinant(A):
    A = [[Q(x) for x in row] for row in A]
    d = Q(1)
    for k in range(len(A)):
        j = next((j for j in range(k, len(A)) if A[j][k]), None)
        if j is None:
            return Q(0)
        if j != k:
            A[k], A[j] = A[j], A[k]
            d = -d
        pivot = A[k][k]
        d *= pivot
        for i in range(k+1, len(A)):
            r = A[i][k]/pivot
            for j in range(k+1, len(A)):
                A[i][j] -= r*A[k][j]
            A[i][k] = Q(0)
    return d

cert = {'scale': 80, 'c': '15/16'}
specs = [
    ('chain', [-1, 0, 1, 2, 3, 4], [128, 208, 352, 336, 192],
     [75, 5504, 333632, 15370240, 434778112, 56623104]),
    ('fork', [-1, 0, 1, 2, 3, 3], [128, 208, 368, 176, 176],
     [75, 5504, 333632, 9116672, 817229824, 5266866176])]
for name, parents, diag, expected in specs:
    A = [[0]*6 for _ in range(6)]
    A[0][0] = 75
    for i, d in enumerate(diag, 1):
        assert d > 0 and d % 2 == 0
        A[i][i] = d
        A[i][parents[i]] -= d//2
        A[parents[i]][i] -= d//2
    for i in (3, 4, 5):
        A[0][i] += 40
        A[i][0] += 40
    minors = [determinant([row[:k] for row in A[:k]]) for k in range(1, 7)]
    assert minors == expected and all(d > 0 for d in minors)
    cert[name] = {'parents': parents, 'matrix': A, 'minors': expected}
print('EXACT_CHAIN_AND_FORK_PD_PASS')

# Every rooted tree has a labeling in which parents precede children.
c = Q(15, 16)
b = [Q(0), Q(0), Q(1, 8), Q(1, 4), Q(89, 256), Q(27, 64)]
assert Q(5) < Q(9, 4)**2
assert b[4]+2*b[3] == Q(217, 256) < c
assert 2*b[4]+b[2] == Q(210, 256) < c
assert b[2]+b[4]+b[5] == Q(229, 256) < c
assert ((1-c)/4)/(3+1-c) == Q(1, 196)
nt = ns = chains = forks = 0
for n in range(1, 9):
    for p0 in product(*(range(i) for i in range(1, n))):
        if n-1-p0.count(0) > 4:
            continue
        p = [-1]+list(p0)
        depth = [0]*n
        for i in range(1, n):
            depth[i] = depth[p[i]]+1
        h = max(depth)
        assert h <= 5
        nt += 1
        for I in combinations(range(n), 3):
            ns += 1
            D = sorted(depth[i] for i in I)
            if h <= 4 and D == [3, 4, 4]:
                i, j, k = sorted(I, key=lambda v: depth[v])
                assert p[j] == i and p[k] == i
                forks += 1
            elif h == 5 and D == [3, 4, 5]:
                i, j, k = sorted(I, key=lambda v: depth[v])
                assert p[k] == j and p[j] == i
                chains += 1
            else:
                assert h == 5 or depth.count(4) <= 2
                assert sum(b[depth[i]] for i in I) < c
assert (nt, ns, chains, forks) == (3310, 166802, 28, 28)
print('EXACT_TREE_CASES_PASS', nt, ns, chains, forks)
cert_raw = (json.dumps(cert, sort_keys=True, separators=(',', ':'))+'\n').encode('ascii')
Path('tree_certificates.json').write_bytes(cert_raw)
print('CERTIFICATE_BYTES_SHA256', len(cert_raw), hashlib.sha256(cert_raw).hexdigest())

# A new rational seven-vertex, reference-relative U1 counterexample.
def add(a, b):
    return tuple(x+y for x, y in zip(a, b))
def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))
def dot(a, b):
    return sum(x*y for x, y in zip(a, b))
def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def det(a, b, c):
    return dot(a, cross(b, c))
def vsum(*a):
    return tuple(sum(v[k] for v in a) for k in range(3))

v = [(Q(1), Q(0), Q(0))]
factors = [(Q(9, 13), Q(6, 13))]*4 + [(Q(25, 29), Q(10, 29)), (Q(4, 5), Q(2, 5))]
rho = Q(999, 1000)
x, y = Q(1), Q(0)
for a, b in factors:
    x, y = rho*(a*x-b*y), rho*(b*x+a*y)
    v.append((x, y, Q(0)))
v[1] = (v[1][0], v[1][1], -Q(1, 100000))
v[5] = (v[5][0], v[5][1], Q(1, 1000))
assert det(sub(v[1], v[0]), sub(v[2], v[0]), sub(v[5], v[0])) != 0
assert all(dot(v[i], sub(v[i-1], v[i])) > 0 for i in range(1, 7))
assert all(dot(v[0], sub(v[0], v[i])) > 0 for i in range(1, 7))
faces = []
for i, j, k in combinations(range(7), 3):
    normal = cross(sub(v[j], v[i]), sub(v[k], v[i]))
    if normal == (0, 0, 0):
        continue
    height = dot(normal, v[i])
    slack = [height-dot(normal, w) for w in v]
    f = [i, j, k]
    if all(s <= 0 for s in slack):
        slack = [-s for s in slack]
        height = -height
        f = [i, k, j]
    if not all(s >= 0 for s in slack):
        continue
    assert height > 0
    assert all(slack[t] > 0 for t in range(7) if t not in f)
    faces.append(f)
assert set(sum(faces, [])) == set(range(7))
assert [4, 6, 5] in faces
edge_uses = {}
for f in faces:
    for i in range(3):
        a, b = f[i], f[(i+1) % 3]
        edge_uses.setdefault(tuple(sorted((a, b))), []).append((a, b))
assert all(len(a) == 2 and a[0] == a[1][::-1] for a in edge_uses.values())
assert all((i-1, i) in edge_uses for i in range(1, 7))
assert (len(v), len(edge_uses), len(faces)) == (7, 15, 10)
W = Q(0)
M = [Q(0)]*3
Wr = Q(0)
Mr = [Q(0)]*3
for f in faces:
    a, b, c0 = [v[i] for i in f]
    d = det(a, b, c0)
    assert d > 0
    W += d
    s = vsum(a, b, c0)
    for k in range(3):
        M[k] += d*s[k]
    if 0 not in f:
        dr = det(sub(a, v[0]), sub(b, v[0]), sub(c0, v[0]))
        assert dr > 0
        Wr += dr
        sr = vsum(v[0], a, b, c0)
        for k in range(3):
            Mr[k] += dr*sr[k]
g = tuple(t/(4*W) for t in M)
assert Wr == W and tuple(t/(4*Wr) for t in Mr) == g
assert g != (0, 0, 0)
Y = [sub(w, g) for w in v]
own_U = [i for i, a in enumerate(Y)
         if all(dot(a, sub(b, a)) < 0 for j, b in enumerate(Y) if i != j)]
assert own_U == [0, 3, 6]
root_projection = dot(v[0], vsum(v[0], v[4], v[5], v[6]))
child_projection = min(dot(v[1], vsum(v[0], v[i], v[j], v[k]))
                       for i, j, k in combinations(range(1, 7), 3))
assert root_projection < 0 < child_projection
obj = {'vertices': [[str(x) for x in w] for w in v], 'faces': faces,
       'edges': [list(e) for e in sorted(edge_uses)], 'centroid': [str(x) for x in g]}
raw = (json.dumps(obj, sort_keys=True, separators=(',', ':'))+'\n').encode('ascii')
sha = hashlib.sha256(raw).hexdigest()
assert len(raw) == 913
assert sha == '6acf0c0a67584e3db8cf68a7d12b6a25a2696473dc70bd4e6799a5d32e17d97b'
Path(sys.argv[1] if len(sys.argv) > 1 else 'chain7_counterexample.json').write_bytes(raw)
print('EXACT_CHAIN7_COUNTEREXAMPLE_PASS', len(raw), sha)
print('root_projection', root_projection)
print('minimum_child_projection', child_projection)
print('centroid', *g)
print('OWN_CENTROID_UNSTABLE_VERTICES', own_U)
```

Supplemental copies: [complete recovery source](sandbox:/mnt/data/v8_recovery.py), [two exact matrix certificates](sandbox:/mnt/data/tree_certificates.json), [exact seven-vertex control](sandbox:/mnt/data/chain7_counterexample.json). These copies are conveniences; the definition and verification source are fully embedded above.

## 7. What was tried, what failed, and the continuation

I first combined the individual angular-depth estimate with the root-coned moment identity. Separate estimates suffice for shallow trees but overestimate negatively projecting clustered descendants. Numerical complex-plane diameter-ball chains identified the five-link last-three-vertex sum as a critical joint case. I replaced the numerical estimate by the two explicit positive-definite certificates, and found that the complete classification depends only on the number of vertices at depth at least two, not on a polyhedral graph.

The six-link control then falsified root-direction positivity on individual tetrahedra. Retaining the full vector moment identity and testing in the first child's direction closes precisely that gap. The numerical exploration is not being used as a global-optimality certificate. For completeness, the complete short exploratory unit that led to the chain case is below; it was run with NumPy 2.3.5 and SciPy 1.17.0 on CPython 3.13.5. Its multistart BFGS outputs are heuristic; the exact proof does not depend on their terminal values.

```python
import numpy as np
from scipy.optimize import minimize
rng=np.random.default_rng(710)
for m in range(3,10):
    def f(t):
        p=np.cumprod((1+np.exp(1j*t))/2)
        return p[-3:].real.sum()
    best=None
    for k in range(20):
        fit=minimize(f, rng.uniform(0,1,m),method='BFGS',options={'gtol':1e-10})
        if best is None or fit.fun<best.fun: best=fit
    print(m,best.fun,best.x, np.cumprod((1+np.exp(1j*best.x))/2))
```

That unit is 435 bytes with SHA-256 9eb882a9ff361a71bad6b2e0c4af8127e6b17576aee19e6ef84b569fb17f7c4e; [supplemental source](sandbox:/mnt/data/path_probe.py).

### A precise next relaxation, rather than an extrapolated bound

For any direction d, order the true vertex projections as x_1 ≤ ... ≤ x_N. Cone from a vertex attaining x_N and then from one attaining x_1. Equation (4) gives the simultaneous necessary inequalities

    x_N+x_1+x_2+x_3 ≤ 4d·g
                    ≤ x_1+x_(N−2)+x_(N−1)+x_N.       (16)

The three vertices in each sum are distinct. In particular, at the actual centroid these sums bracket zero in EVERY direction, not merely along u. Equivalently, with Σ_3(V) the convex hull of all sums of three distinct vertex vectors,

    4g−K ⊆ Σ_3(V).                                  (17)

To check the equivalence, the right inequality of (16) is exactly the support-function inclusion (17), and the left is the same statement after replacing d by −d. This necessary inclusion is stronger than the repeated-vertex relaxation −K/3 ⊆ K, but still does not encode the actual tetrahedral volume weights or face lattice.

For eight vertices, (12) restricts the root to one or two direct shadows. If an escape tree has only one root child w, the same first-child proof excludes that tree whenever w has two or more children. The remaining trees therefore either have two root children, or start with two unbranched links. Their relevant subtrees can have five deep vertices, beyond the proved four-deep lemma. The existing six-link counterexample shows why simply extending the old projection inequality is unjustified.

The strongest continuation is to combine (16) in several endogenous directions—u, its first successors, and separating directions of the three-vertex-sum hull—with the five-outside-diameter-ball restriction and the actual tetrahedral weights. Directions must remain variables determined by the candidate geometry, not a frozen pool. For the joint S1/U1 problem, (15) supplies a justified compact normalization. A failure of this relaxation would not establish existence, and finite numerical searches over it would not establish infeasibility.

### Evidence boundary

The V ≥ 8 result here is a self-contained analytic argument with two small exact rational positivity certificates. The auxiliary computer checks have actually executed, but this is not a proof-assistant formalization or an external peer review. The R/r ≤ 27 reduction is a separate written argument; no numerical mesh is used to establish it. Priority of these derivations has not been established by the limited literature check.

No V ≥ 9 theorem, stronger universal edge lower bound, matching minimum-complexity realization, or new Gömböc upper witness is claimed. Nothing here treats a polar centroid as the original volume centroid, promotes the seven-vertex reference-relative control to a homogeneous object, or restores any withdrawn fixed-pool or mixed-cone assertion.
