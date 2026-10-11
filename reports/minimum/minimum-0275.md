# minimum-0275

Historical AI scientific report · saved 2026-09-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# C610: global physical centroid completion and an exact algebraic control

## 1. Attainment status and provenance

**No smaller attaining own110physicalweak000 body is claimed. The canonical C622 attaining checkpoint is unchanged.** The constructive result here is a global theorem that eliminates the actual-centroid constraint by changing one genuine facet plane. It is stronger than local invertibility of a facet actuator: the completed body exists globally on a precise domain, is unique, and is the unique maximum-volume uniformly filled centred subset of its released-facet kernel. I also give a completely specified algebraic polytope that tests this mechanism with its actual volume, first and second moments, maximal facets, true edges, and physical equilibrium census.

The supplied journal was read through EOF: 393202 bytes, SHA-256 `1f16eb17bab789f3c439b75bc8ff4e40f4c7e4525f9c19d384310f3ec5ca2c22`. The literal parent used was `minimum-0186`, SHA-256 `bf2aa3420122c0e1766c5d29ea403630c07361451168a92fdedca055775d9f57`. Its recovery wrapper was extracted and decoded: 72821 bytes, SHA-256 `022dc1ef9b7b7335033aa7518ccd6be2f308670ceccae3c2a2e8430d73470ada`; the decoded 52-source map had 221314 bytes and SHA-256 `361820340e4f2304f73dbcea4819902377b55f06a9bad1c3f2644e0f6675611b`. No older canonical C622 coordinate file was needed. I do not claim a fresh replay of all twelve parent checkpoints.

The parent-specific discussion below uses the protected omit610 labels, not canonical C622 labels. In particular, the genuine outgoing edge considered is `153 -> w1`, not the internal `153 -> 151`. The actual saddle edge is `w2 -- v165`; facet 99 and old vertices 157 and 163 are not reintroduced.

I explored direct whole-plane motions of 41, 68, 83 and 135, and a whole-S3 hinge, using fresh hull integration rather than independent integration-triangle actuation. Those explorations supplied no newly certified attaining endpoint. No exclusion is inferred from them, and no floating endpoint is promoted to an exact successor. The exact deliverables are the theorem, its concrete omit610 application, the algebraic control, and the reusable exact-audit acceleration described below.

## 2. Global, unique, volume-maximal actual-centroid completion

### Statement

Translate the desired physical centre to the origin. Let K be a full-dimensional closed convex polyhedron with 0 in its interior. Assume that at least one halfspace of the form

`q·x <= 1`

makes K bounded. For bounded K this assumption is automatic. Define

`D = {q : P(q) = K intersect {q·x <= 1} is bounded}`

and the actual-volume potential

`Phi(q) = integral over K of max(1 - q·x, 0) dx`.

Then:

1. There exists a bounded, full-dimensional completed body P* with actual uniform centroid 0.
2. P* is unique among halfspace completions with centroid 0. Its normal q* is also unique unless the completion is redundant and P* = K, with K itself bounded and centred.
3. More strongly, P* is the unique maximum-volume bounded measurable subset of K having uniform centroid 0, up to sets of volume zero.
4. An active completion q* is the unique minimizer of the convex function Phi. It satisfies the actual first-moment equation `J(q*) = integral over P(q*) of x dx = 0`.

This is a theorem about one genuine uniformly filled body. It neither changes density nor independently centres a polar body. It does not assert anything about the number of equilibria of the completed body.

### Actual derivatives

Write V(q) for the volume, J(q) for the first moment, and g(q) = J(q)/V(q). For the actual cutting facet

`F(q) = K intersect {q·x = 1}`,

let A be its area, C its uniform area centroid, T its uniform area second-moment matrix, and `w = A/||q||`. In an ordinary incidence chamber,

`gradient Phi = -J`,

`Hessian Phi = w T`,

`dV = -w C^T dq`,

`dJ = -w T dq`,

`Dg = -(w/V)(T - g C^T)`.

All these quantities belong to the actual maximal facet. Triangulations may integrate them, but their triangles are not separate actuators.

The matrix T is positive definite. Indeed, if `u^T T u = 0`, the linear function `u·x` vanishes on a two-dimensional facet with relative interior. Its affine hull is `q·x = 1`, which does not pass through 0. A linear functional vanishing throughout that affine plane must be zero. Thus u = 0.

The identity `T q = C` gives the useful determinant formula

`det(Dg) = -(w/V)^3 det(T) (1 - q·g) < 0`.

At a centred completion this simplifies to

`Dg = -(w/V) T`.

Consequently the actual centroid equation has a nonsingular, symmetric negative-definite plane derivative at every active centred completion.

### Existence, including unbounded released-facet kernels

Convexity of Phi follows directly from convexity of the positive part of an affine function.

For coercivity at infinity, choose a ball about 0 contained in K. A fixed positive-volume portion of that ball lies a fixed negative distance along the direction q/||q||. Its contribution to Phi grows linearly in ||q||. Therefore Phi tends to infinity as ||q|| tends to infinity.

When K is unbounded, its recession cone is pointed under the stated one-halfspace boundedness assumption. D consists of normals strictly positive on its nonzero recession directions. If a bounded sequence q_n approaches the boundary of D, some unit recession direction d has `q_n·d -> 0+`. A small disk transverse to d, extruded along d, lies in K. On an initial cylinder of length proportional to `1/(q_n·d)`, the integrand remains bounded below by a positive constant. Hence `Phi(q_n) -> infinity`.

Thus sublevel sets are compact inside D and a minimizer exists. Differentiating the actual integral gives `gradient Phi = -J`, so the minimizer has actual centroid 0. The completion contains a neighbourhood of 0, since its offset is 1; it therefore has positive volume and is genuinely three-dimensional.

### Uniqueness without a fixed incidence assumption

Suppose two completions P1 and P2 have first moment zero. On `P1 minus P2`,

`(q1 - q2)·x < 0`,

and on `P2 minus P1` the same expression is positive. But

`(q1 - q2)·(J(P1) - J(P2)) = 0`.

Writing this difference as integrals over the two set differences is strictly negative unless their symmetric difference has volume zero. Thus P1 and P2 coincide. If the cutting plane is active, its normalized equation is unique. The only normal nonuniqueness is the explicitly stated redundant-cut case.

This argument survives facet mergers and incidence changes. It does not retain any forest or root label.

### Maximum-volume property and an exact loss identity

Let A be any bounded measurable subset of K with uniform centroid 0. At the completed normal q*,

`Vol(A) = integral over A of (1 - q*·x) dx`

`       <= integral over K of max(1 - q*·x, 0) dx`

`       = Phi(q*) = Vol(P*)`.

More precisely,

`Vol(P*) - Vol(A) = integral over the symmetric difference of P* and A of |1 - q*·x| dx`.

Therefore the centre-restoring halfspace is not merely some physical correction: it retains the greatest possible volume among all uniformly filled centred subsets of the kernel. Equality forces A = P* up to volume zero.

### Exact certification rather than a small centre residual

For rational kernel data, inside a fixed incidence chamber the vertices and actual first moments are rational functions of q. Clearing denominators produces polynomial equations for `J(q) = 0`. The nonsingular derivative makes the desired solution an isolated algebraic solution.

A practical exact certificate is an interval-Newton box. Let B be a rational box of radius delta about a rational q0, let A0 be an invertible rational approximate inverse of the actual Hessian, and suppose exact interval bounds give

`rho = sup over B of ||I - A0 Hessian Phi(q)||_infinity < 1`,

`||A0 gradient Phi(q0)||_infinity < (1 - rho) delta`.

Then `q -> q - A0 gradient Phi(q)` is a contraction mapping B into itself. Its unique fixed point is the actual centred completion; global uniqueness identifies it with q*. This supplies an exact algebraic normal, not a rational normal with an unaccounted residual.

The theorem does not make the outer equilibrium optimization convex. It also gives no uniform conditioning bound: a thin actuator facet can have a badly conditioned T.

## 3. Concrete application to the real omit610 boundary

First translate the recovered physical parent by its actual uniform centroid g0. For an original inequality `n_i·y <= h_i`, use

`x = y - g0`,

`q_i = n_i / (h_i - n_i·g0)`.

The physical metric for the following local statement is M = I and N = I. No polar recentering is performed.

### A seven-parameter centre-preserving whole-facet chart

The useful actuator is the actual facet 135, which contains the actual saddle edge `w2 -- v165`. Its initial vertices are simple, so its three plane parameters can be used as genuine boundary parameters.

Let p* be the other endpoint, besides w1, of the true edge shared by maximal facets 41 and 83. This incidence definition avoids confusing a sorted output index with a protected raw label. The nonsimple incidence at p* is retained by moving both planes 41 and 83 through p*.

Choose a coordinate k with maximal nonzero absolute component of p*, breaking ties by the smaller index. For each j different from k, define the exact tangent vector

`b_j = e_j - (p*_j/p*_k) e_k`.

Use seven free parameters as follows:

`q41(theta) = q41 + theta0 b_j1 + theta1 b_j2`,

`q68(theta) = q68 + (theta2, theta3, theta4)`,

`q83(theta) = q83 + theta5 b_j1 + theta6 b_j2`.

Hold every other plane except 135 fixed. Form the released-facet kernel from these inequalities, omitting 135. Complete it with the unique plane `q135*(theta)` supplied by the theorem.

Near theta = 0, the initial true incidences persist: the pinned nonsimple incidence is respected, and the remaining affected vertices are simple. The implicit-function theorem applies because the actual facet-135 Hessian is positive definite. This gives a genuine seven-parameter family with exactly the original physical centre. In a sufficiently small neighbourhood it retains the parent census

`(V,E,F) = (173,305,134), C = 610`,

`(S,U,H) = (1,2,1), physical weak = (0,0,0)`.

This local statement is not a cancellation claim. It identifies an actual boundary family, rather than a formal moment family. Globally the unique completion remains defined whenever the kernel satisfies the theorem, but the old incidence must then be discarded whenever an actual support wall is crossed.

### The critical outgoing cut can be actuated without centroid feedback

In this chart the actual parent intersections are

`x153 = intersection(q3, q41, q68)`,

`w1   = intersection(q3, q41, q83)`,

`w2   = intersection(q3, q83, q135*)`,

`v165 = intersection(q3, q103, q135*)`.

Consequently, while these remain actual vertices, the genuine outgoing-cut functional

`D(153 -> w1) = x153^T M (w1 - x153)`

depends explicitly on the free planes 41, 68 and 83, but **not** on the implicit centring normal 135. The centre is fixed by a real boundary change; it is not being held fixed artificially while the body's mass changes.

Meanwhile the completion plane moves the actual saddle edge through w2 and v165. Thus the centroid constraint can be eliminated before optimizing the real outgoing cut and the real saddle geometry. This removes a concrete coupling that made local boundary changes move many otherwise irrelevant equilibrium inequalities through a changing centre.

For a fixed M, the other physical metric is always its actual inverse. Taking M = I throughout is already a legitimate use of this chart. Introducing a larger common metric is an additional outer variable, not an independent polar fit.

### Exact differential formulas for implementation

For each actual moving facet f put `H_f = w_f T_f`. At a centre-preserving point,

`dq135 = -H_135^-1 sum over f in {41,68,83} of H_f dq_f`.

The actual volume derivative is

`dV = sum over f in {41,68,83} of (q135 - q_f)^T H_f dq_f`.

Both formulas use actual whole-facet moments. They avoid differentiating a free centre or introducing independent facet masses.

The Hessians have an especially convenient exact fan formula. For an outward triangle (a,b,c) of a normalized facet `q·x = 1`, write `d = det(a,b,c)` and `s = a+b+c`. Its contribution to H_f is

`d/24 * (s s^T + a a^T + b b^T + c c^T)`.

No square root or numerical surface-area normalization is needed.

### What this does not establish

I have not exhibited parameters in this family that cancel the last U/H pair. I have not bounded the radius of its initial incidence chamber, nor proved that the completion plane stays mechanically favourable along a path to cancellation. A positive value of the outgoing-cut functional could merely move the extra unstable vertex to w1; it would not by itself establish U = 1.

The parent's all-orientation condition-number barrier remains valid on the unchanged parent geometry. This theorem does not contradict it. It changes the actual boundary and solves the actual-centre equation for that changed body.

## 4. A fully specified exact algebraic control

This is a material nonattainer, included to demonstrate the global completion with a real algebraic boundary and a complete physical census.

Let c be the unique root in

`21/20 < c < 11/10`

of

`p(c) = 2c^4 - 8c^3 - 18c^2 + 27 = 0`.

The endpoint signs are exactly

`p(21/20) = 26001/80000 > 0`,

`p(11/10) = -12499/5000 < 0`.

Moreover `p'(c) = 4c(2c^2 - 6c - 9) < 0` on this interval, so the root is isolated uniquely.

Define

`K = [-1,2]^3`,

`P = K intersect {x+y+z <= c}`,

`M = N = I_3`, with uniform density 1.

The completion normal is `q* = (1,1,1)/c`. The theorem makes P the unique maximum-volume uniformly centred subset of K, not merely the best member of a sampled one-dimensional family.

### Complete vertex data

```text
0 = (-1, -1, -1)
1 = ( 2, -1, -1)
2 = (-1,  2, -1)
3 = (-1, -1,  2)
4 = ( 2, c-1, -1)
5 = ( 2, -1, c-1)
6 = (c-1, 2, -1)
7 = (-1, 2, c-1)
8 = (c-1, -1, 2)
9 = (-1, c-1, 2)
```

### Complete maximal-facet data

The cycles are outward oriented.

```text
facet 0: x = -1       cycle [0,3,9,7,2]
facet 1: y = -1       cycle [0,1,5,8,3]
facet 2: z = -1       cycle [0,2,6,4,1]
facet 3: x =  2       cycle [1,4,5]
facet 4: y =  2       cycle [2,7,6]
facet 5: z =  2       cycle [3,8,9]
facet 6: x+y+z = c    cycle [4,6,7,9,8,5]
```

### Complete true-edge data

```text
[0,1], [0,2], [0,3], [1,4], [1,5],
[2,6], [2,7], [3,8], [3,9], [4,5],
[4,6], [5,8], [6,7], [7,9], [8,9]
```

Thus `(V,E,F) = (10,15,7)` and `C = 30`. There are three pentagonal facets, three triangular facets, and one hexagonal facet. All ten vertices are simple.

### Actual uniform moments

The actual volume is

`V = (-2c^3 + 9c^2 + 27c + 27)/6`.

Each coordinate of the actual first moment is

`integral over P of x_i dx = -p(c)/24 = 0`.

The raw second-moment matrix has a common diagonal entry a and common off-diagonal entry b, where

`a = 27/20 + (27/10)c + (9/5)c^2 - (1/2)c^3`,

`b = 9/80 - (9/10)c - (39/40)c^2 + (1/6)c^3`.

Consequently the actual covariance is `((a-b)I + b 11^T)/V`.

For a direct derivation, put `y_i = x_i+1` and `s = c+3`. The retained region is `0 <= y_i <= 3`, `sum y_i <= s`, with `3 < s < 6`. Subtracting the three disjoint excess-coordinate simplices from the simplex `sum y_i <= s` gives the stated volume and first moment. The same calculation, or the true-facet tetrahedral fan in the verifier, gives the stated second moments.

### Exact physical census

The stable facets are exactly `[0,1,2,6]`. Their orthogonal feet lie in their relative interiors. The feet of the three upper coordinate facets violate `x+y+z <= c` because `c < 2`.

Every vertex is strictly unstable. Up to coordinate permutations, the directed true-edge products are drawn from

`-3, -6, -c, -c(c-1), -c^2, -(3-c)^2`,

all strictly negative on the isolating interval.

The twelve saddle edges are exactly

```text
[0,1], [0,2], [0,3], [1,4], [1,5], [2,6],
[2,7], [3,8], [3,9], [4,6], [5,8], [7,9]
```

The three excluded edges are `[4,5]`, `[6,7]`, and `[8,9]`. On each of them the upper-coordinate pole has a strictly positive escape toward the diagonal pole:

`1/(2c) - 1/4 > 0`.

All sixty directed primal/polar true-edge primitives are nonzero. Therefore the complete census is

`strict (S,U,H) = (4,10,12)`,

`physical weak (VE,EF,VF) = (0,0,0)`.

This is not an attaining body. Its C = 30 does not improve an own110 bound.

## 5. Standalone exact recovery and verification capsule for the control

The polynomial, isolating interval, all vertices, all maximal facets, all true edges, metric, and moment formulas above are complete literal recovery data. No parent file or external library is needed for this control.

The following complete verifier uses CPython 3.13.5 and its standard library only. It uses exact rational arithmetic in the quotient by p, with rational interval refinement to certify signs at the specified real root. There is no floating-point input or random seed. Run it as `python -S centroid_completion_control.py`.

The expected terminal marker is `GLOBAL_CENTROID_COMPLETION_ALGEBRAIC_CONTROL_PASS`, with geometry `10 15 7`, strict census `4 10 12`, and sixty nonzero true-edge primitives. The program writes a canonical JSON recovery record and prints its byte count and SHA-256 for archiving. I am supplying an analytical certificate and complete replay source, not claiming an observed fresh byte/hash cold-replay receipt for this new program.

```python
from fractions import Fraction as R
from itertools import combinations
from pathlib import Path
import hashlib
import json


def poly(t):
    return 2*t**4 - 8*t**3 - 18*t**2 + 27


left, right = R(21,20), R(11,10)
assert poly(left) == R(26001,80000)
assert poly(right) == -R(12499,5000)


class Alg:
    def __init__(self, value=0):
        if isinstance(value, Alg):
            self.a = value.a
        elif isinstance(value, (tuple, list)):
            assert len(value) <= 4
            self.a = tuple(R(z) for z in value) + (R(0),)*(4-len(value))
        else:
            self.a = (R(value), R(0), R(0), R(0))

    def __add__(self, other):
        other = Alg(other)
        return Alg([x+y for x,y in zip(self.a, other.a)])

    __radd__ = __add__

    def __neg__(self):
        return Alg([-x for x in self.a])

    def __sub__(self, other):
        return self + (-Alg(other))

    def __rsub__(self, other):
        return Alg(other) - self

    def __mul__(self, other):
        other = Alg(other)
        w = [R(0)]*7
        for i,x in enumerate(self.a):
            for j,y in enumerate(other.a):
                w[i+j] += x*y
        for k in range(6,3,-1):
            z = w[k]
            w[k] = R(0)
            w[k-1] += 4*z
            w[k-2] += 9*z
            w[k-4] -= R(27,2)*z
        return Alg(w[:4])

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = R(scalar)
        assert scalar
        return Alg([x/scalar for x in self.a])

    def __eq__(self, other):
        return self.a == Alg(other).a


def interval(value):
    lo = hi = R(0)
    for z in reversed(Alg(value).a):
        products = (lo*left, lo*right, hi*left, hi*right)
        lo, hi = min(products)+z, max(products)+z
    return lo, hi


def sign(value):
    global left, right
    value = Alg(value)
    if not any(value.a):
        return 0
    for unused in range(512):
        lo, hi = interval(value)
        if lo > 0:
            return 1
        if hi < 0:
            return -1
        mid = (left+right)/2
        pm = poly(mid)
        if pm == 0:
            v = sum(z*mid**i for i,z in enumerate(value.a))
            return (v > 0) - (v < 0)
        if pm > 0:
            left = mid
        else:
            right = mid
    raise ArithmeticError('Unresolved algebraic sign')


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), Alg())


def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def det(a,b,c):
    return dot(a, cross(b,c))


def enc(a):
    return [str(z) for z in Alg(a).a]


c = Alg([0,1,0,0])
ic = Alg([0,R(2,3),R(8,27),-R(2,27)])
assert c*ic == 1

literal_vertices = [
    (-1,-1,-1), (2,-1,-1), (-1,2,-1), (-1,-1,2),
    (2,c-1,-1), (2,-1,c-1), (c-1,2,-1),
    (-1,2,c-1), (c-1,-1,2), (-1,c-1,2)
]
X = [tuple(Alg(z) for z in row) for row in literal_vertices]
normal_literals = [
    (-1,0,0), (0,-1,0), (0,0,-1),
    (1,0,0), (0,1,0), (0,0,1), (1,1,1)
]
normals = [tuple(Alg(z) for z in row) for row in normal_literals]
heights = [Alg(1),Alg(1),Alg(1),Alg(2),Alg(2),Alg(2),c]
faces = [
    [0,3,9,7,2], [0,1,5,8,3], [0,2,6,4,1],
    [1,4,5], [2,7,6], [3,8,9], [4,6,7,9,8,5]
]
poles = [tuple(Alg(z)/h for z in n)
         for n,h in zip(normal_literals[:6], [1,1,1,2,2,2])]
poles.append((ic,ic,ic))

edge_data = {}
vertex_faces = [[] for unused in X]
for f,cy in enumerate(faces):
    actual = {i for i,x in enumerate(X) if dot(normals[f],x) == heights[f]}
    assert actual == set(cy)
    assert all(sign(heights[f]-dot(normals[f],x)) >= 0 for x in X)
    for i in cy:
        vertex_faces[i].append(f)
    for a,b in zip(cy,cy[1:]+cy[:1]):
        e = sub(X[b],X[a])
        assert all(sign(dot(normals[f],cross(e,sub(X[k],X[a])))) >= 0
                   for k in cy)
        edge_data.setdefault(tuple(sorted((a,b))), []).append((a,b,f))

for fs in vertex_faces:
    assert len(fs) == 3
    assert any(sign(det(normals[i],normals[j],normals[k])) != 0
               for i,j,k in combinations(fs,3))
for items in edge_data.values():
    assert len(items) == 2
    assert items[0][0] == items[1][1]
    assert items[0][1] == items[1][0]

edges = sorted(edge_data)
expected_edges = [
    (0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(2,7),(3,8),
    (3,9),(4,5),(4,6),(5,8),(6,7),(7,9),(8,9)
]
assert edges == expected_edges
assert len(X)-len(edges)+len(faces) == 2

D = Alg()
J24 = [Alg() for unused in range(3)]
T2 = [[Alg() for unused in range(3)] for unused in range(3)]
HH = [[Alg() for unused in range(3)] for unused in range(3)]
for f,cy in enumerate(faces):
    for k in range(1,len(cy)-1):
        t = [X[cy[0]],X[cy[k]],X[cy[k+1]]]
        d = det(*t)
        assert sign(d) > 0
        s = [sum((v[i] for v in t),Alg()) for i in range(3)]
        D += d
        for i in range(3):
            J24[i] += d*s[i]
            for j in range(3):
                B = s[i]*s[j] + sum((v[i]*v[j] for v in t),Alg())
                T2[i][j] += d*B/120
                if f == 6:
                    HH[i][j] += d*B/24

volume = D/6
expected_volume = Alg([R(9,2),R(9,2),R(3,2),-R(1,3)])
a = Alg([R(27,20),R(27,10),R(9,5),-R(1,2)])
b = Alg([R(9,80),-R(9,10),-R(39,40),R(1,6)])
assert volume == expected_volume
assert sign(volume) > 0
assert all(z == 0 for z in J24)
for i in range(3):
    for j in range(3):
        assert T2[i][j] == (a if i == j else b)
assert sign(HH[0][0]) > 0
assert sign(HH[0][0]*HH[1][1]-HH[0][1]*HH[1][0]) > 0
assert sign(det(*HH)) > 0

vertex_signs = [[] for unused in X]
facet_signs = [[] for unused in faces]
saddles = []
for i,j in edges:
    f,g = [row[2] for row in edge_data[(i,j)]]
    values = [
        dot(X[i],sub(X[j],X[i])),
        dot(X[j],sub(X[i],X[j])),
        dot(poles[f],sub(poles[g],poles[f])),
        dot(poles[g],sub(poles[f],poles[g]))
    ]
    ss = [sign(v) for v in values]
    assert all(z != 0 for z in ss)
    vertex_signs[i].append(ss[0])
    vertex_signs[j].append(ss[1])
    facet_signs[f].append(ss[2])
    facet_signs[g].append(ss[3])
    if max(ss) < 0:
        saddles.append([i,j])

stable = [i for i,ss in enumerate(facet_signs) if max(ss) < 0]
unstable = [i for i,ss in enumerate(vertex_signs) if max(ss) < 0]
expected_saddles = [
    [0,1],[0,2],[0,3],[1,4],[1,5],[2,6],
    [2,7],[3,8],[3,9],[4,6],[5,8],[7,9]
]
assert stable == [0,1,2,6]
assert unstable == list(range(10))
assert saddles == expected_saddles
assert 4*len(edges) == 60

identity = [[1,0,0],[0,1,0],[0,0,1]]
report = {
    'name': 'ALGEBRAIC_DIAGONAL_BOX_COMPLETION_10_15_7_V1',
    'polynomial_ascending': [27,0,-18,-8,2],
    'isolating_interval': ['21/20','11/10'],
    'vertices': [[enc(z) for z in row] for row in X],
    'normal_vectors': normal_literals,
    'offsets': [enc(z) for z in heights],
    'poles': [[enc(z) for z in row] for row in poles],
    'faces': faces,
    'edges': edges,
    'M': identity,
    'N': identity,
    'density': 1,
    'volume': enc(volume),
    'first_moment': [enc(z/24) for z in J24],
    'second_moment': [[enc(z) for z in row] for row in T2],
    'completion_hessian': [[enc(z) for z in row] for row in HH],
    'stable': stable,
    'unstable': unstable,
    'saddles': saddles,
    'physical_weak': [0,0,0],
    'nonzero_true_edge_primitives': 60
}
raw = (json.dumps(report,sort_keys=True,separators=(',',':'))+chr(10)).encode('ascii')
Path('centroid_completion_control.json').write_bytes(raw)
print('GEOMETRY',len(X),len(edges),len(faces),'C',2*len(edges))
print('STRICT',len(stable),len(unstable),len(saddles),'PHYSICAL_WEAK',0,0,0)
print('NONZERO_TRUE_EDGE_PRIMITIVES',4*len(edges))
print('BYTES',len(raw),'SHA256',hashlib.sha256(raw).hexdigest())
print('GLOBAL_CENTROID_COMPLETION_ALGEBRAIC_CONTROL_PASS')
```

## 6. Retained reusable method: fast candidate location with a complete exact hull certificate

The exhaustive intersection loop in the parent auditor can be expensive for the large rational normals. A floating convex hull of the pole vectors can locate candidate triples, while the existing exact auditor supplies the certificate. Floating geometry is not used to accept a facet, vertex, moment, or equilibrium sign.

The certification argument is important. Every accepted polygon is an actual supporting facet of the convex hull of the accepted exact vertices. Every boundary edge is paired with exactly two such facets, with opposite orientations. Therefore this nonempty collection is closed under adjacency in the facet graph of that convex hull. The facet graph is connected, so no hull facet is omitted. Since every accepted vertex satisfies every input halfspace, the certified convex hull equals the whole halfspace intersection. A missed floating candidate can cause failure, but cannot turn an incomplete list into a certified different body.

The following is the complete wrapper. Its exact dependency is the supplied parent's `check_A.py`, obtained from the verified 52-source capsule, not a canonical C622 file. The local numerical environment was CPython 3.13.5, NumPy 2.3.5 and SciPy 1.17.0. NumPy and SciPy are used only for candidate location.

```python
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import sys
sys.set_int_max_str_digits(0)
import json
import hashlib
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.spatial import ConvexHull
import check_A as A

_EXACT_RUN = A.run


def run(raw):
    q = np.array([[float(Fraction(n,row[3])) for n in row[:3]]
                  for row in raw['H']])
    assert np.isfinite(q).all()
    z = q-q.mean(axis=0)
    unused,s,vh = np.linalg.svd(z,full_matrices=False)
    assert np.all(s > 0)
    locator = ConvexHull((z @ vh.T)/s)
    triples = sorted({tuple(sorted(map(int,t))) for t in locator.simplices})
    old = A.combinations
    A.combinations = lambda values,k: iter(triples)
    try:
        return _EXACT_RUN(raw)
    finally:
        A.combinations = old


if __name__ == '__main__':
    assert len(sys.argv) == 3
    result = run(json.loads(Path(sys.argv[1]).read_text()))
    data = json.dumps(result,sort_keys=True,separators=(',',':')).encode()
    Path(sys.argv[2]).write_bytes(data)
    print('EXACT_CLOSED_HULL_AUDIT_PASS',result['V'],result['E'],result['F'])
    print('BYTES',len(data),'SHA256',hashlib.sha256(data).hexdigest())
```

This wrapper is single-process; its temporary module-level substitution must not be used concurrently in multiple threads.

For the omit610 input, reconstruct `room612_raw.json` from the supplied parent capsule, then remove raw facet 99. Raw facet 134 is already absent. The exact conversion is:

```python
import json
import sys
from pathlib import Path
sys.set_int_max_str_digits(0)
room = json.loads(Path('room612_raw.json').read_text())
labels = [i for i in range(136) if i != 134]
assert len(room['H']) == len(labels)
omit = {'H':[row for label,row in zip(labels,room['H']) if label != 99]}
Path('omit610_raw.json').write_text(json.dumps(omit,sort_keys=True,separators=(',',':')))
```

Run `python -B fast_A.py omit610_raw.json omit610_A_replayed.json`. The parent geometry pin is `173 305 134`. The original exact auditor still recomputes the actual uniform centre after the omission and performs its complete physical census. This acceleration is not a replacement of maximal facets by a numerical triangulation.

## 7. Verification limits and the next constructive step

The global completion theorem is proved above. The algebraic control is specified by complete literal data, and its full physical census follows from the exact moment identities and strict edge products above. Its verifier is supplied for replay; expected terminal text is not presented as an observed cold-replay receipt. No new numerical own110 endpoint, no smaller attaining complexity, and no whole-family mechanical exclusion is claimed.

The most useful continuation is to search the seven free whole-facet parameters while eliminating plane 135 by the unique convex actual-centroid completion. Target the genuine outgoing cut `153 -> w1` and the actual saddle geometry, not the internal arrow `153 -> 151`. At every incidence event, rebuild the maximal facets and true edges rather than carrying old labels or forests across the event. A promising numerical normal should be replaced by an isolated algebraic solution of the actual first-moment equations, with strict sign bounds for the complete physical census. A cutset escape or root migration is a useful intermediate only; an improvement over C622 requires the persisted endpoint itself to have strict `(S,U,H) = (1,1,0)`, physical weak `(0,0,0)`, and actual `C < 622`.
