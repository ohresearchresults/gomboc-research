# figure-0326

AI research report · 2026-09-06 UTC

---

# Steady Comet 43 — low-facet physical support architecture

## 1. Status and authority

**No new strict (1,1,0) successor is promoted by this handoff. The E<500 target remains unmet in this copy.** The accepted parent remains `STRICT262_DIRECT_REPAIR_EXACT`, with `(V,E,F)=(262,754,494)`, stable triangle `[1,4,3]`, unstable vertex `261`, and no saddles. Its NX02 payload has length 8320 and SHA-256 `88b81fc57bd68aaf6fce037bac50bca86460a9c57bf99dad6d13fc1750d1f2df`. I am retaining the journal's acceptance status, not claiming another completed replay of that parent. 

The contributions here are narrower and self-contained:

* An implementation-ready, ordinary-volume-centroid-closing chart for joint support-normal geometry. It does not require extra moment-control facets, preserves incidence during its centering step, and has an everywhere nonsingular three-dimensional centroid Jacobian.
* An explicit rational physical example proving that deleting one supporting plane can increase true E even while decreasing F. Its final body has `(V,E,F)=(14,25,13)`, exact own-centroid class **(5,9,12)**, and no degenerate equilibria. This is a negative control, not a Gömböc or a near-winner.
* Complete coordinates, supporting planes, maximal facets, true edges, ordinary moments, an exhaustive exact mechanical sign ledger, and runnable verification source for that negative control.

I attempted an executable verification, but did not obtain an inspectable completed interpreter report. Consequently, I do **not** report an observed machine PASS or invent literal hashes for the new source/data. The exact algebraic checks below are the evidence for the fixture; the supplied program is the recovery and fresh-replay capsule. Its two programmatic audits must not be marked executed merely because they are supplied here.

## 2. The useful architectural change: budget supporting planes, not monotone edge loss

For every bounded full-dimensional convex 3-polyhedron—not only a simple one—

`E <= 3F - 6`.

Indeed, `2E >= 3V` and `V-E+F=2`. More precisely,

`3F - 6 - E = sum over physical vertices v of (degree(v)-3)`.

Thus a construction with at most **168 irredundant physical support planes automatically has E<=498**, regardless of nonsimple vertices. Simplicity is not an additional acceptance requirement.

This changes the appropriate search policy. A support-deletion branch need not decrease E at every step. It can lose nonsimple incidence savings, temporarily gain true edges, and still be progressing toward the support-count budget. Requiring an immediate E decrease after every deleted pole can reject legitimate low-F continuations.

There is a precise bookkeeping consequence for the parent. Taking its polar about the supplied origin produces a physical body with `(V,E,F)=(494,754,262)`. This statement concerns geometry and polarity only; it does not assert the polar's own-centroid mechanics. Its incidence deficit is

`3*262 - 6 - 754 = 26`,

corresponding to the parent's 26 quadrilateral facets. A generic movement of those 262 poles can resolve all these incidences and yield `(520,780,262)`. That increase is not automatically a bad low-F move. At a final support count of 168, the generic ceiling is already 498.

The low-F route can therefore deliberately abandon the inherited quadrilateral locks. Its difficult condition is mechanics after actual mass closure, not preservation of those 26 edge savings.

## 3. A physical mass-closing support chart

### 3.1 A common pole translation is a projective deformation of the physical body

Let

`P(q) = {x : q_i dot x <= 1 for every i}`

be bounded and full-dimensional, with the origin in its interior. For a vector `a` satisfying

`1 + a dot x > 0 throughout P`,

define

`T_a(x) = x / (1 + a dot x)`.

Direct substitution gives

`T_a(P(q)) = P(q+a)`.

The same vector `a` is added to every pole. This is **not** a physical translation and is **not** a choice of mechanical reference point. It changes the physical body projectively. Within the positive-denominator domain it preserves the complete face lattice, including all nonsimple incidences.

Its Jacobian determinant in dimension three is

`det DT_a(x) = (1+a dot x)^(-4)`.

Consequently, writing integrals over the original physical body,

`V(a) = integral (1+a dot x)^(-4) dx`,

`M(a) = integral x (1+a dot x)^(-5) dx`,

`J(a) = integral x x^T (1+a dot x)^(-6) dx`.

These are respectively the ordinary volume, first moment, and uncentered second-moment matrix of the **transformed physical solid**, expressed in its new coordinates. In particular,

`gradient V(a) = -4 M(a)`,

`Hessian V(a) = 20 J(a)`.

Since a full-dimensional solid has positive-definite second moment about every nonzero direction, V is strictly convex on its admissible domain. V diverges at the boundary of that domain. One way to see divergence is to integrate over an interior tetrahedron with one vertex at a limiting zero-denominator contact: the resulting integral grows at least proportionally to the reciprocal of the minimum denominator.

It follows that there is a **unique** admissible common pole translation for which the transformed physical solid has ordinary centroid zero. This supplies a mass-closing chart without introducing additional supporting planes.

### 3.2 The centroid Jacobian is explicit and nonsingular

Let `c=M/V` and let `Sigma=J/V-c c^T` be the physical covariance matrix. Differentiation gives

`dc/da = -5 Sigma - c c^T`.

This matrix is negative definite for every bounded full-dimensional physical body. At a centered endpoint,

`dc/da = -5 Sigma`.

Thus this three-coordinate mass-closing block has no exact rank deficiency before geometric degeneration. Poor conditioning is possible; absence of three independent centroid directions is not.

A Newton direction for the centroid equation is

`d = (5 Sigma + c c^T)^(-1) c`.

A finite step adds `tau*d` to every pole and maps every physical vertex by

`x_new = x / (1 + tau*d dot x)`.

Choose tau by checking positive denominators and decreasing actual V. Because

`gradient V dot d = -4 V * c^T (5 Sigma+c c^T)^(-1) c < 0`

away from the centered point, ordinary backtracking has a descent direction. The source below includes an exact-rational finite-step implementation; it does not require finite-difference centroid derivatives.

### 3.3 Coupling this closure to arbitrary support-normal movement

Suppose a support-normal update, before centering compensation, induces an ordinary-centroid differential `dc_free`. At an already centered endpoint the common pole correction is

`da = (5 Sigma)^(-1) dc_free`.

Its additional physical vertex differential is

`dx_projective = -x * (x dot da)`.

For a simple physical vertex with active support-row matrix A, the uncorrected differential is obtained directly from

`A x = (1,1,1)^T`,

`dx_free = -A^(-1) (dA) x`.

This provides a direct analytic pullback into mass-closed normal coordinates. Nonsimple vertices require compatible differentials or an actual finite fan change; one must not differentiate through an arbitrarily chosen active triple and pretend the remaining incidences survive.

At a finite joint-normal endpoint, rebuild the actual body first. Then perform the common-pole centering correction and audit mechanics on that physical endpoint. The centering step preserves the rebuilt incidence, but the preceding independent normal movement need not.

### 3.4 A useful scoped obstruction

If P is already centered, the unique mass-closing common pole translation is `a=0`. Therefore **common pole translation alone cannot generate a nontrivial family of exactly centered descendants of an already centered body**. It is a closure coordinate for other geometry changes, not an independent centered search direction.

This is a scoped obstruction to a particular proposed control family. It is not an obstruction to joint-normal deformation or to a low-F Gömböc.

### 3.5 Boundedness can also be built into this chart

Start instead with any full-dimensional pole polytope `Q=conv{q_i}`. Its arithmetic vertex average lies in its interior when all actual vertices receive positive weights. Translate Q by the negative of that average to initialize an interior polar origin, and then apply the unique physical mass-closing normalization above.

The average is being used **only to initialize an interior point of the pole polytope**. It is not substituted for the physical body's mass centroid.

This matters after pole deletion. A deleted-pole hull can be full-dimensional even when the old polar origin has left its interior. Such a child need not be discarded as intrinsically unbounded: recentering the pole hull before taking its physical polar defines a different, bounded physical continuation. Its mechanics must then be recomputed.

### 3.6 Exact acceptance does not require a rational projective-centering root

The limiting common translation need not be rational. That is not an obstacle to finite rational acceptance.

Freeze a numerical support configuration as rational rows, reconstruct its actual rational physical vertices, and compute its exact ordinary centroid c. Then translate the physical body by `-c`. Its normalized centered support rows are exactly

`q_i' = q_i / (1 - q_i dot c)`.

All denominators are positive for the genuine ordinary centroid of a bounded full-dimensional body. This final ordinary translation changes coordinates, not own-centroid mechanics or incidence. The exact feature audit—not an assumed closeness to a numerical centering root—decides acceptance.

## 4. Exact finite negative control: one fewer physical support, one more true edge

### 4.1 Construction and complete centered coordinates

Take the zonotope

`Q0 = [-g1,g1] + [-g2,g2] + [-g3,g3] + [-g4,g4]`,

where

`g1=(1,0,0), g2=(0,1,0), g3=(0,0,1), g4=(1,1,-2)`.

It has 14 vertices, 24 true edges, and 12 quadrilateral facets. Let

`v=(2,2,-1)`

and delete that vertex:

`Q1 = conv(vertices(Q0) excluding v)`.

The four neighbors of v are

`a=(0,2,-1), b=(2,0,-1), d=(0,0,3), k=(2,2,-3)`.

They are not coplanar. The new cap consists of triangles `[a,k,d]` and `[b,k,d]`, with supporting planes

`x+2y+z=3`,

`2x+y+z=3`.

The old four incident quadrilaterals survive as triangles. Four old edges disappear and five new edges appear. Hence

`(V,E,F)(Q0)=(14,24,12)`,

`(V,E,F)(Q1)=(13,25,14)`.

Both contain the origin strictly. For Q1, a particularly short boundedness certificate is that the sum of its 13 vertices is `-v`, while

`a+b+d/3 = v`.

Assign weight 1 to every Q1 vertex, add weight 1 to a and b, and add weight 1/3 to d. All weights are positive, their weighted vector sum is zero, and the rows span three dimensions.

Now take the physical polars `P0=Q0 polar`, `P1=Q1 polar`. They have

`(V,E,F)(P0)=(12,24,14)`,

`(V,E,F)(P1)=(14,25,13)`.

Thus **removing one physical supporting plane increases true E from 24 to 25**.

The final own-centroid-centered P1 has common denominator **2760** and the following complete integer vertex numerators. These coordinates alone define the negative control; no parent archive is needed.

```text
index       X       Y       Z
 0        1303     -77     -48
 1         -77    1303     -48
 2         -77     -77     872
 3        1763     -77     872
 4         -77    1763     872
 5        1303   -1457     -48
 6       -1457     -77     -48
 7         -77   -1457     -48
 8         -77     -77    -968
 9       -1917     -77    -968
10         -77   -1917    -968
11       -1457    1303     -48
12         843    1763     872
13        1763     843     872
```

### 4.2 Complete maximal supporting facets

For the centered coordinates `y=I/2760`, each following row means

`q dot y <= h/2760`.

The listed cycles are outward-oriented maximal facets.

```text
face   q                 h       outward cycle
 0    ( 2, 2,-3)       2596      [0,8,1,12,13]
 1    ( 2, 0,-1)       2654      [0,13,3,5]
 2    ( 2, 0,-3)       2750      [0,5,10,8]
 3    ( 0, 2,-1)       2654      [1,11,4,12]
 4    ( 0, 2,-3)       2750      [1,8,9,11]
 5    ( 0, 0, 3)       2616      [2,3,13,12,4]
 6    (-2,-2, 1)       3020      [6,9,10,7]
 7    (-2,-2, 3)       2924      [6,7,2]
 8    (-2, 0, 1)       2866      [6,11,9]
 9    (-2, 0, 3)       2770      [6,2,4,11]
10    ( 0,-2, 1)       2866      [7,10,5]
11    ( 0,-2, 3)       2770      [7,5,3,2]
12    ( 0, 0,-3)       2904      [8,10,9]
```

There are four triangular, seven quadrilateral, and two pentagonal maximal facets. The sum of their boundary lengths is 50, giving exactly 25 true edges—not the edge count of a display triangulation.

### 4.3 Complete true-edge incidence

```text
(0,5) (0,8) (0,13)
(1,8) (1,11) (1,12)
(2,3) (2,4) (2,6) (2,7)
(3,5) (3,13)
(4,11) (4,12)
(5,7) (5,10)
(6,7) (6,9) (6,11)
(7,10)
(8,9) (8,10)
(9,10) (9,11)
(12,13)
```

### 4.4 Ordinary solid moments: two analytic checks

For moment calculation, use the uncentered vertices p given in the source below. They satisfy `q_i dot p<=1`. P0 is centrally symmetric, so its ordinary first moment is zero. Direct outward-tetrahedron integration gives

`V(P0) = 2*(3/72 + 2/81 + 3*7/216) = 53/162`.

The physical region added by deleting the support is the convex hull of the old quadrilateral face and the two new vertices. Its volume and first moment are

`Delta V = 1/36`,

`Delta M = (77/7776, 77/7776, 1/162)`.

Therefore

`V(P1) = 115/324`,

`M(P1) = (77/7776, 77/7776, 1/162)`,

`c(P1) = (77/2760, 77/2760, 2/115)`.

The centered integer coordinates above are exactly `2760*p-(77,77,48)`. Their ordinary first moment is `(0,0,0)`.

For an independent analytic integration of the added region, set

`u=x+y`, `v=x-y`,

`u=(1+z)/2+s/3`.

The region is described by

`0<=z<=1/3`,

`0<=s<=3z`,

`abs(v)<=(1+z)/2-s/3`.

The absolute Jacobian from `(s,z,v)` to `(x,y,z)` is 1/6. Integration first in v gives width `1+z-2s/3`. Hence

`Delta V = (1/6)*integral[z=0..1/3] integral[s=0..3z] (1+z-2s/3) ds dz = 1/36`,

`Delta M_z = 1/162`.

The v symmetry gives `Delta M_x=Delta M_y`. Since the slice-average x equals `(1+z)/4+s/6`, its integral gives `77/7776`. This check does not use the boundary triangulation.

### 4.5 Exhaustive exact mechanics: strict (5,9,12), not (1,1,0)

The stable maximal faces are

`S = [0,5,7,9,11]`.

The unstable vertices are

`U = [2,3,4,5,9,10,11,12,13]`.

The saddle edges are

```text
(2,3) (2,4) (2,6) (2,7)
(3,5) (3,13)
(4,11) (4,12)
(5,10)
(9,10) (9,11)
(12,13)
```

There are no degenerate equilibria and no zero-valued true-edge endpoint/cone primitives.

Here is a compact exact face certificate. Put `C=(77,77,48)`, `D=2760`, and define

`L_ij = norm(q_i)^2 * (D-q_j dot C) - (q_i dot q_j)*(D-q_i dot C)`.

A face i is strictly stable exactly when every `L_ij>0` for `j!=i`. The minimum values for the five stable rows are

```text
face 0: 13002
face 5:  1386
face 7:  9078
face 9:  2002
face11:  2002
```

For every other face, the following single negative value is an exclusion witness:

```text
i -> j     L_ij
1 -> 0     -5598
2 -> 0     -2002
3 -> 0     -5598
4 -> 0     -2002
6 -> 7     -6904
8 -> 9     -6212
10 -> 11   -6212
12 -> 0    -2772
```

For completeness, the following edge ledger covers all 25 edges using the exact x/y interchange symmetry. Write `a=77/2760`, `b=2/115`. For an oriented representative edge, t is the orthogonal-foot parameter. The columns A and B are the two Gram-cone coefficient numerators multiplied by 2760; their omitted denominators are positive. A saddle requires `0<t<1`, `A>0`, and `B>0` simultaneously.

```text
edge      mult   t                            A       B       saddle
(6,7)       1    1/2                         19176   -6904       no
(6,9)       2   -(3+6a+12b)/5                   770   10694       no
(0,5)       2   -2a                          15252   -4828       no
(6,11)      2    2a                          17868   -6212       no
(0,8)       2   (9-18a-12b)/13                -2002   13002       no
(6,2)       2   (9+18a+12b)/13                 2002    9078       yes
(9,10)      1    1/2                         35892   35196       yes
(3,5)       2   (4-12a-6b)/7                  42812   21812       yes
(9,11)      2   (4+12a+6b)/7                  45508   22348       yes
(3,2)       2    1-3a/2                       9078    1386       yes
(9,8)       2    1+3a/2                      13002   -1386       no
(1,12)      2    2a-1/3+4b/3                 26946   -5598       no
(4,12)      2    3a                          31734   21042       yes
(12,13)     1    1/2                         46908   67836       yes
```

Every t differs from both 0 and 1, and every displayed cone numerator is nonzero. The vertex census follows independently from the signs of the radial derivatives along all incident edges. Vertices 0 and 1 have strict escape along the `(0,5)` symmetry pair; vertices 6 and 7 escape along the `(6,9)` pair; vertex 8 escapes toward 9 or 10. All nine remaining vertices have strictly negative outward radial derivatives along every incident edge. Thus no vertex is a degenerate equilibrium.

This finite branch is a failure for the requested mechanics, but a complete negative control for physical centroid handling, maximal-facet counting, full edge cones, and nonmonotone edge complexity under support deletion.

## 5. Complete executable recovery and audit capsule

Save the following complete source as `sc43_exact_fixture.py`. Requirement: CPython 3.11 or later, standard library only. No journal, optimizer, downloaded archive, numerical hull package, or omitted helper is needed for this fixture.

Run:

```sh
python sc43_exact_fixture.py > sc43_exact_fixture_report.json
```

The canonical data hash is SHA-256 of the UTF-8 compact sorted-key JSON containing the exact raw vertices as Fraction strings, the integer support normals, and the complete facet cycles. The program prints that digest and the source-file digest. **Literal fresh digest values and a machine replay transcript remain unconfirmed in this handoff.** The printed source digest identifies the exact saved source, including its line endings.

The audits use two different geometry/mass/mechanics routes. The first checks the explicit oriented maximal-face complex, uses boundary-fan tetrahedra, polygon-foot inequalities, local vertex links, and edge Gram cones. The second reconstructs every feasible H-plane triple and the edge incidence from facet-contact intersections, integrates from a strictly interior anchor through facet centers, and uses global all-point support tests for every feature. Shared vector arithmetic is not counted as an independent geometric test.

```python
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict, Counter
from pathlib import Path
import hashlib
import json


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(s, a):
    return tuple(s * x for x in a)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0])


def det(a, b, c):
    return dot(a, cross(b, c))


ZERO = (F(0),) * 3


def solid_moments(points, faces):
    # Origin must be strictly interior; faces must be outward oriented.
    volume = F(0)
    moment = ZERO
    second = [[F(0) for j in range(3)] for i in range(3)]
    for cycle in faces:
        for k in range(1, len(cycle) - 1):
            a, b, c = [points[i] for i in
                       (cycle[0], cycle[k], cycle[k+1])]
            d = det(a, b, c)
            assert d > 0
            s = add(add(a, b), c)
            volume += d / 6
            moment = add(moment, mul(d / 24, s))
            for i in range(3):
                for j in range(3):
                    second[i][j] += d / 120 * (
                        s[i]*s[j] + a[i]*a[j]
                        + b[i]*b[j] + c[i]*c[j])
    return volume, moment, second


def projective_mass_step(points, faces):
    # One exact-rational Newton/backtracking step.
    # Add the returned delta to EVERY normalized support row.
    volume, moment, second = solid_moments(points, faces)
    c = mul(1 / volume, moment)
    if c == ZERO:
        return list(points), ZERO
    h = [tuple(5 * second[i][j] / volume - 4 * c[i]*c[j]
               for j in range(3)) for i in range(3)]
    denominator = det(*h)
    assert denominator > 0
    numerator = add(add(mul(c[0], cross(h[1], h[2])),
                        mul(c[1], cross(h[2], h[0]))),
                    mul(c[2], cross(h[0], h[1])))
    direction = mul(1 / denominator, numerator)
    descent = dot(c, direction)
    assert descent > 0
    tau = F(1)
    for attempt in range(100):
        denominators = [1 + tau * dot(direction, p)
                        for p in points]
        if min(denominators) > 0:
            trial = [mul(1 / d, p)
                     for p, d in zip(points, denominators)]
            trial_volume = solid_moments(trial, faces)[0]
            if trial_volume <= volume - volume*tau*descent:
                return trial, mul(tau, direction)
        tau /= 2
    raise ArithmeticError('No accepted projective step in 100 halvings')


P = [(F(1,2), 0, 0),
     (0, F(1,2), 0),
     (0, 0, F(1,3)),
     (F(2,3), 0, F(1,3)),
     (0, F(2,3), F(1,3)),
     (F(1,2), -F(1,2), 0)]
P += [mul(-1, p) for p in P[:6]]
P += [(F(1,3), F(2,3), F(1,3)),
      (F(2,3), F(1,3), F(1,3))]
P = [tuple(F(x) for x in p) for p in P]

Q = [(2,2,-3), (2,0,-1), (2,0,-3),
     (0,2,-1), (0,2,-3), (0,0,3),
     (-2,-2,1), (-2,-2,3), (-2,0,1),
     (-2,0,3), (0,-2,1), (0,-2,3), (0,0,-3)]

FAC = [[0,8,1,12,13], [0,13,3,5], [0,5,10,8],
       [1,11,4,12], [1,8,9,11], [2,3,13,12,4],
       [6,9,10,7], [6,7,2], [6,11,9], [6,2,4,11],
       [7,10,5], [7,5,3,2], [8,10,9]]

# Audit A: exact supports, complete contacts and convex facet boundaries.
ED = defaultdict(list)
oriented_edges = Counter()
for f, (q, cycle) in enumerate(zip(Q, FAC)):
    assert set(cycle) == {i for i, p in enumerate(P) if dot(q, p) == 1}
    assert all(dot(q, p) <= 1 for p in P)
    for i, j in zip(cycle, cycle[1:] + cycle[:1]):
        inward = cross(q, sub(P[j], P[i]))
        assert all(dot(inward, sub(P[k], P[i])) > 0
                   for k in cycle if k not in (i, j))
        ED[tuple(sorted((i, j)))].append(f)
        oriented_edges[(i, j)] += 1

assert all(len(fs) == 2 for fs in ED.values())
assert all(oriented_edges[(i,j)] == oriented_edges[(j,i)] == 1
           for i, j in ED)
assert (len(P), len(ED), len(FAC)) == (14, 25, 13)
assert len(P) - len(ED) + len(FAC) == 2

# Connected cyclic vertex links and rank-three incident normals.
for vertex in range(len(P)):
    link = defaultdict(set)
    incident = []
    for f, cycle in enumerate(FAC):
        if vertex in cycle:
            incident.append(Q[f])
            k = cycle.index(vertex)
            a, b = cycle[k-1], cycle[(k+1) % len(cycle)]
            link[a].add(b)
            link[b].add(a)
    assert link and all(len(nbr) == 2 for nbr in link.values())
    seen = set()
    stack = [next(iter(link))]
    while stack:
        a = stack.pop()
        if a not in seen:
            seen.add(a)
            stack.extend(link[a] - seen)
    assert seen == set(link)
    assert any(det(*triple) != 0 for triple in combinations(incident, 3))

V, M, J = solid_moments(P, FAC)
assert V == F(115, 324)
assert M == (F(77,7776), F(77,7776), F(1,162))
c = mul(1 / V, M)
assert c == (F(77,2760), F(77,2760), F(2,115))
centered = [sub(p, c) for p in P]
VC, MC, JC = solid_moments(centered, FAC)
assert VC == V and MC == ZERO
assert all(dot(q, c) < 1 for q in Q)

# Audit B: exhaustive exact H-vertex reconstruction from all plane triples.
VV = set()
for a, b, d in combinations(Q, 3):
    determinant = det(a, b, d)
    if determinant:
        numerator = add(add(cross(b,d), cross(d,a)), cross(a,b))
        p = mul(F(1, determinant), numerator)
        if all(dot(q, p) <= 1 for q in Q):
            VV.add(p)
assert VV == set(P)

# Strictly positive pole weights prove boundedness independently.
weights = [F(1)
           + F(q in ((0,2,-1), (2,0,-1)))
           + F(1,3)*F(q == (0,0,3)) for q in Q]
assert all(w > 0 for w in weights)
assert tuple(sum(w*q[k] for w,q in zip(weights,Q))
             for k in range(3)) == ZERO
assert any(det(*triple) != 0 for triple in combinations(Q, 3))

# Independent true-edge reconstruction from maximal contact intersections.
contacts = [{i for i,p in enumerate(P) if dot(q,p) == 1} for q in Q]
EB = {}
for f, g in combinations(range(len(Q)), 2):
    common = contacts[f] & contacts[g]
    if len(common) == 2:
        edge = tuple(sorted(common))
        assert edge not in EB
        EB[edge] = (f, g)
assert set(EB) == set(ED)

# Independent mass integration: interior anchor and facet-centre fans.
anchor = mul(F(1,len(P)),
             tuple(sum(p[k] for p in P) for k in range(3)))
assert all(dot(q, anchor) < 1 for q in Q)
VB = F(0)
MB = ZERO
for cycle in FAC:
    fc = mul(F(1,len(cycle)),
             tuple(sum(P[i][k] for i in cycle) for k in range(3)))
    for i, j in zip(cycle, cycle[1:] + cycle[:1]):
        d = det(sub(fc,anchor), sub(P[i],anchor), sub(P[j],anchor))
        assert d > 0
        VB += d / 6
        MB = add(MB, mul(d / 24, add(add(anchor,fc), add(P[i],P[j]))))
assert (VB, MB) == (V, M)

S = []
U = []
H = []
degenerate = []
zero_edge_primitives = 0

# Face audit: polygon inequalities versus all other H-supports.
for f, (q, cycle) in enumerate(zip(Q, FAC)):
    foot = add(c, mul((1-dot(q,c))/dot(q,q), q))
    local = [dot(cross(q,sub(P[j],P[i])), sub(foot,P[i]))
             for i,j in zip(cycle, cycle[1:] + cycle[:1])]
    global_test = [1-dot(r,foot) for j,r in enumerate(Q) if j != f]
    assert (min(local) > 0) == (min(global_test) > 0)
    assert (min(local) >= 0) == (min(global_test) >= 0)
    if min(local) > 0:
        S.append(f)
    elif min(local) == 0:
        degenerate.append(('F', f))

# Vertex audit: incident-edge derivatives versus every other vertex.
for i, p in enumerate(P):
    neighbors = {b if i == a else a for a,b in ED if i in (a,b)}
    local = [dot(sub(p,c), sub(P[j],p)) for j in neighbors]
    global_test = [dot(sub(p,c), sub(y,p))
                   for j,y in enumerate(P) if j != i]
    assert (max(local) < 0) == (max(global_test) < 0)
    assert (max(local) <= 0) == (max(global_test) <= 0)
    if max(local) < 0:
        U.append(i)
    elif max(local) == 0:
        degenerate.append(('V', i))

# Edge audit: full Gram cone versus the global support of the line foot.
for (i,j), (f,g) in EB.items():
    edge = sub(P[j], P[i])
    length2 = dot(edge, edge)
    t = dot(sub(c,P[i]), edge) / length2
    foot = add(P[i], mul(t,edge))
    radial = sub(foot,c)
    n, m = Q[f], Q[g]
    aa, ab, bb = dot(n,n), dot(n,m), dot(m,m)
    gram_det = aa*bb - ab*ab
    assert gram_det > 0
    alpha_num = bb*(1-dot(n,c)) - ab*(1-dot(m,c))
    beta_num = aa*(1-dot(m,c)) - ab*(1-dot(n,c))
    strict = 0 < t < 1 and alpha_num > 0 and beta_num > 0
    closed = 0 <= t <= 1 and alpha_num >= 0 and beta_num >= 0
    global_test = [dot(radial, sub(y,foot))
                   for k,y in enumerate(P) if k not in (i,j)]
    assert strict == (0 < t < 1 and max(global_test) < 0)
    assert closed == (0 <= t <= 1 and max(global_test) <= 0)
    zero_edge_primitives += sum(z == 0 for z in
                                (t,1-t,alpha_num,beta_num))
    if strict:
        H.append((i,j))
    if closed and not strict:
        degenerate.append(('E',i,j))

expected_H = [(2,3),(2,4),(2,6),(2,7),(3,5),(3,13),
              (4,11),(4,12),(5,10),(9,10),(9,11),(12,13)]
assert S == [0,5,7,9,11]
assert U == [2,3,4,5,9,10,11,12,13]
assert sorted(H) == expected_H
assert not degenerate and zero_edge_primitives == 0
assert len(S) + len(U) - len(H) == 2

canonical = json.dumps(
    {'vertices': [[str(v) for v in p] for p in P],
     'support_normals': Q,
     'face_cycles': FAC},
    sort_keys=True, separators=(',', ':')).encode('utf-8')

report = {
    'VEF': [len(P),len(ED),len(FAC)],
    'SUH': [len(S),len(U),len(H)],
    'volume': str(V),
    'raw_first_moment': list(map(str,M)),
    'raw_centroid': list(map(str,c)),
    'centered_first_moment': list(map(str,MC)),
    'centered_integer_denominator': 2760,
    'centered_integer_vertices': [[int(2760*x) for x in p]
                                  for p in centered],
    'stable_faces': S,
    'unstable_vertices': U,
    'saddle_edges': sorted(H),
    'all_true_edges': sorted(ED),
    'degeneracies': degenerate,
    'zero_edge_primitives': zero_edge_primitives,
    'data_sha256': hashlib.sha256(canonical).hexdigest(),
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
print(json.dumps(report, indent=2))
```

The included `projective_mass_step` is a reusable finite construction operation, not an assertion that applying it to this fixture produces (1,1,0). After calling it, update every support row by its returned delta and repeat the actual mechanical audit. It is deliberately not called automatically in the fixture's fixed-object verification.

## 6. Most useful continuation toward the assigned winner

The next substantive construction should exploit the chart above rather than reproduce this negative control.

Use the 262 parent's exact centered physical vertices as an initial pole set for a physical H-body with 262 support planes. This is its polar as a geometric seed only. Compute that new physical body's ordinary moments and apply the common-pole mass closure. **Its resulting own-centroid equilibrium class is not computed or claimed here.** The initial intended stable support is associated with parent vertex 261, and the initial intended unstable physical vertex with parent face `[1,4,3]`; these are labels to test, not invariants under mass-changing deformation.

Proceed toward an actual pole count of 168 while permitting true E to be nonmonotone. A child that remains full-dimensional in pole space can be given a new interior polar origin and mass-normalized even when deletion invalidates the old origin. Score actual full mechanics and conditioning before penalizing a temporary loss of nonsimple incidence savings.

For joint-normal repair, compute the free physical centroid differential, apply the explicit three-dimensional projective closure, and differentiate the resulting primal and polar escape inequalities. Maintain the distinction between already-positive guards and genuinely negative defects. Require noncoincident, larger-radius escape witnesses where those are used; a negative score tending to zero through witness collapse is not cancellation.

At every finite endpoint: rebuild the true maximal contacts after the independent normal movement; close the physical mass; then enumerate faces, vertices, and full edge cones. The common-pole centering step itself preserves incidence and therefore need not trigger a new combinatorial guess, although its mechanics must be reevaluated.

For any numerical (1,1,0) endpoint with at most 168 actual supports, rationalize the support rows, reconstruct the finite rational H-body, compute its exact ordinary centroid, and translate physically to that centroid. Require two complete independent geometry/mass/feature checks before promotion. No rational limiting projective-centering root is required.

## 7. Boundary of the result

There is no new accepted (1,1,0) object, no executed 168-support optimization result, and no E<500 winner hidden in this handoff. The explicit 13-support endpoint is strict (5,9,12). Its purpose is to make the physical mass, normal-cone, and incidence issues concrete and replayable.

The useful redirection is exact: **F<=168 suffices without simplicity; individual support deletion need not lower E; physical centroid closure has a nonsingular global three-coordinate projective block; and that block must be coupled to other normal changes rather than mistaken for a standalone centered deformation.** None of these statements is a lower bound on Gömböc complexity or evidence that the low-F construction is impossible.
