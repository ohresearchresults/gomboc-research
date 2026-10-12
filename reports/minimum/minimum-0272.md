# minimum-0272

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NONPARALLEL_PROJECTIVE_COMPACTIFICATIONS_AND_RATIONAL_CONTROL_FRAMES_V1

## Outcome and verification boundary

**I do not certify a new complete nonparallel S1/U1-exclusion domain from this attempt.** The proposed large three-chart cover did not reach a final verification state that I can substantiate in this handoff. Its purported final certificates, completion counts, and source-only replay pins must not be treated as accepted successors to the previous root-conditioned result.

The durable results are narrower:

1. Exact positive-projective coordinates, actual-refill moments, and two full-dimensional axial compactifications for a genuinely nonparallel heptagon–triangle family. The two endpoint bodies are identified explicitly, including their actual centroid heights and which labels cease to be true vertices.
2. A bounded rational-frame lemma giving a deterministic **actual, same-inverse, strict (S,U,H)=(2,2,2), weak-free metric ray** on every rational E17 body. A library of 2,187 explicitly specified integer frames suffices. The complete recovery program below applies it to three substantial nonparallel images of the literal W body and reconstructs every centroid, pole, metric, inverse, primitive, equilibrium label, and whole-ray sign certificate.
3. Two corrections to the unfinished working notes. One recorded inverse entry was wrong, and one recorded all-ray unstable-root census is incompatible with a strictly positive leading coefficient of the true arrow 1→2. These are corrections to the unfinished working notes, **not amendments to any immutable parent**.

The metric rays are nonattaining controls. They are not U1, S1, or 110 constructions, and they do not exclude other metrics on those shapes. No canonical incidence count or global complexity bound changes.

## 1. Input authority

The retained reading record reaches EOF, line 4799, of the supplied 489,022-byte journal, SHA-256 `bdcea1d91a7f45424b6a84ef385b83f9be6a08816fdb974cfd5206053dc8e490`, and includes all four required literal parents:

| Immutable parent | SHA-256 |
|---|---|
| `minimum-0269` | `8b4cb712a53d69060ede95fbed7a083b623f87f5d5f4a8aef994b80d7f117684` |
| `minimum-0225` | `c772d9b01329dcd809a288ef999d910676c13c3334cff8c96e7d59a51b887bdd` |
| `minimum-0271` | `78c5ee7f94706f5d44ca425624faab7a07c6d99a3b0fee6ba7cb32938ba2b290` |
| `minimum-0268` | `c199a4de7b66fb757fbc3f1b2beeb903f7002fe567611824a9f0626b32aa2fc5` |

The previous two-foot-cell result remains unchanged. The completed parallel five-parameter theorem is not transported through a non-affine projective refill. Likewise, the new actual-covariance condition ceiling is a joint S1/U1 necessary condition; it is not imposed on the unconditional control rays below.

No additional mathematical source is needed for the constructions and proofs in this handoff. The missing item is **completed execution evidence for the large attempted exclusion**, not an unprovided geometric input.

## 2. Literal geometry and actual projective moments

Use the following source vertices, with the original labels:

```
0=(17/80,0,0)
1=(629/800,0,0)
2=(187/250,51/500,0)
3=(51/100,17/50,0)
4=(0,221/800,0)
5=(0,17/80,0)
6=(17/320,17/320,0)
7=(0,0,1)
8=(3/20,0,1)
9=(0,3/20,1).
```

These are the literal W source at `(x,r,p,q,lambda)=(1/10,9/10,3/25,3/5,3/20)`, not a replacement incidence realization. Its outward maximal facet cycles are

```
(6,5,4,3,2,1,0)
(8,7,0,1)
(7,6,0)
(1,2,8)
(9,8,2,3)
(9,3,4)
(4,5,7,9)
(6,7,5)
(7,8,9).
```

Only consecutive pairs in these cycles are mechanical edges. The positive tetrahedral fan, all with apex 7, is

```
(7,6,5,4), (7,6,4,3), (7,6,3,2),
(7,6,2,1), (7,6,1,0), (7,1,2,8),
(7,9,8,2), (7,9,2,3), (7,9,3,4).
```

The original geometry and actual-moment convention agree with the supplied parent.

Write the raw source vertices as Y_i. For p=(h,k,l), define

`d_i=1+h*Y_ix+k*Y_iy+l*Y_iz`, and `Z_i=Y_i/d_i`.

Whenever all d_i are positive, this is an actual convex projective image with the same true maximal facets and edges. It is **uniformly refilled**. Let

`w_T=det(Y_b-Y_a,Y_c-Y_a,Y_d-Y_a)>0`

for a source fan tetrahedron T=(a,b,c,d). Its image has six-volume

`w_T(p)=w_T/(d_a*d_b*d_c*d_d)`.

Therefore the actual new moments are

```
D(p) = sum_T w_T(p)                         = 6 Vol(P_p)
J(p) = sum_T w_T(p) sum_{i in T} Z_i         = 24 integral_{P_p} z dz
g(p) = J(p)/(4 D(p)).
```

The tetrahedral formula follows by taking the determinant of the homogeneous projective map and dividing the four homogeneous vertex columns by their positive denominators. It does not push forward the old uniform mass without its Jacobian. The recovery program also checks the moments by an independent oriented-boundary integration.

The basal plane remains `Z_z=0`; the other end plane is

`h Z_x+k Z_y+(1+l)Z_z=1`.

Thus the two ends are genuinely nonparallel whenever `(h,k) != (0,0)`. This is not an affine disguise of a parallel-end realization: the unique heptagonal facet determines the three vertices outside it, and those three determine the triangular end. An affine isomorphism preserves parallelism of that distinguished pair.

## 3. Exact axial compactifications

Fix h,k>0. Positivity of all denominators is then equivalent to `l>-1`, because vertex 7 has denominator `1+l`, the other two top denominators add positive terms, and every basal denominator is positive.

### Upper axial end

For l≥1, put `t=1/(1+l)`, so `0<t≤1/2`, and apply the affine height normalization `diag(1,1,1/t)` after the actual refill. In these coordinates,

```
i<7:  Z_i=(Y_ix,Y_iy,0)/(1+h Y_ix+k Y_iy)
i>=7: Z_i=(t Y_ix,t Y_iy,1)/(1+t(h Y_ix+k Y_iy)).
```

If a fan tetrahedron contains m top labels, its normalized six-volume is

`w_T * t^(m-1) / product_{i in T} dbar_i`,

where dbar is the displayed denominator. There is no negative power of t because every fan tetrahedron contains vertex 7.

At t=0, labels 7,8,9 coincide at `(0,0,1)`. The basal heptagon remains a genuine positively projective image of the source heptagon. The actual limit is a **heptagonal pyramid with f-vector (8,14,8)**. Only the five fan tetrahedra with one top label retain positive volume. Every surviving tetrahedron has centroid height 1/4, so the actual limit centroid satisfies `g_z=1/4`.

This is a full-dimensional indexed limit, not a genuine 10/17/9 body at t=0.

### Lower axial end

For `-1<l≤-1/2`, put `a=1+l`, so `0<a≤1/2`, and apply `diag(1,1,a)`. The normalized vertices are

```
i<7: Z_i=(Y_ix,Y_iy,0)/(1+h Y_ix+k Y_iy)
Z7=(0,0,1)
Z8=((3/20)/(a+3h/20),0,a/(a+3h/20))
Z9=(0,(3/20)/(a+3k/20),a/(a+3k/20)).
```

The factor a from the affine Jacobian cancels the denominator of vertex 7. Consequently each normalized fan weight is exactly

`w_T / product_{i in T, i!=7} dbar_i`.

At a=0, vertices 8 and 9 become `(1/h,0,0)` and `(0,1/k,0)`. The true basal hull has the five vertices with old labels

`0,8,9,5,6`,

in cyclic order, and vertex 7 is its apex. Hence the limit has **f-vector (6,10,6)**, not ten true vertices. Again its actual centroid height is 1/4.

To see the five-vertex basal hull directly, put c=17/80. The mapped source basal polygon lies inside the triangle

`x>=0, y>=0, h*x+k*y<=1`

and satisfies the two lower-corner inequalities

```
(1+c*h)x+(3+c*k)y >= c
(3+c*h)x+(1+c*k)y >= c.
```

Intersecting these five halfspaces gives precisely the pentagon with vertices 0,8,9,5,6. It contains the whole mapped basal heptagon, and all five of its vertices occur in the limiting labelled set. This proves the hull identity without assigning masses to the disappearing labels.

The two compactifications isolate a bounded middle problem from two full-dimensional lower-vertex ends. They do not by themselves quantify an exclusion neighborhood or prove absence of U1 in the middle.

## 4. Bounded rational-frame lemma

### Statement

For every rational full-dimensional convex polytope with V=10, E=17, F=9, at an interior rational origin, one of the following **2,187 integer frames** produces a physical, same-inverse, strictly weak-free (2,2,2) metric ray for all sufficiently large real L:

```
u_r=(1,r,r^2)
v_rs=(-r-s*r^2,1,s)
w_rs=u_r cross v_rs,
1<=r<=81, 1<=s<=27.
```

The metric is

`M(L)=L^2 u_r u_r^T + L w_rs w_rs^T + v_rs v_rs^T`.

The frame selection and a sufficient integer lower bound L0 are computable by exact rational arithmetic. Every frame entry has absolute value less than 2^31. No uniform bound on L0 is claimed.

The lemma needs only an interior origin. In all controls here, that origin is the **actual uniform volume centroid** computed above.

### Choosing the frame

Let A consist of the ten centered primal vertices and the seventeen undirected true edge vectors. Thus |A|=27, and every member is nonzero. Let B consist of the nine actual polar vertices and the seventeen undirected true polar edge vectors, so |B|=26.

For any nonzero a, `a.u_r` is a nonzero polynomial of degree at most two in r. It excludes at most two integer values. A nonzero b can be parallel to u_r for at most one r, since the first coordinate of u_r is 1. Thus at most

`2*27+26=80`

positive integers r are forbidden by the requirements

```
a.u_r != 0 for every a in A,
b not parallel to u_r for every b in B.
```

Some r≤81 works.

For this r, `b.v_rs` is an affine polynomial in s:

`b_y-r*b_x+s*(b_z-r^2*b_x)`.

It is not identically zero, because that would make b parallel to u_r. At most 26 positive integers s are forbidden, so some s≤27 works.

The three axes u,w,v are nonzero and mutually orthogonal. Their exact inverse metric is therefore

```
N(L)=u u^T/(||u||^4 L^2)
    +w w^T/(||w||^4 L)
    +v v^T/||v||^4.
```

This is one physical inverse pair, not independently chosen primal and polar metrics.

### Exact whole-ray bound

Every primal primitive is a quadratic

`q(L)=a2*L^2+a1*L+a0`,

with a2 nonzero by construction. Every polar primitive, after multiplication by the positive factor L^2, has the same form with nonzero leading coefficient.

For all 68 polynomials take

`L0=1+max(1, ceil(2*(abs(a1)+abs(a0))/abs(a2)))`.

For every real L≥L0 the lower-order terms have magnitude less than half the leading term. Hence every primitive has its leading-coefficient sign and is nonzero. Equivalently, after multiplying by that sign and substituting `L=L0+t`, all three coefficients are strictly positive. These are exact whole-ray certificates, not endpoint sampling.

For the primal graph, a positive linear projection that is not the global maximum has a neighbor with larger projection; a negative projection that is not the global minimum has a neighbor with smaller projection. Thus the rank-one leading orientation has exactly two strict unstable vertices. The same argument on the actual polar gives exactly two strict stable facets. The physical inverse relation and the nonzero primitives give a proper equilibrium census; the usual boundary-sphere index identity then gives two strict saddles. The code also checks their actual edge labels directly.

This proves `(S,U,H)=(2,2,2)` with no physical weak contacts for the entire ray. Its condition number tends to infinity. These rays do not challenge the supplied spectral ceiling under joint S1/U1, because they have two stable and two unstable equilibria.

## 5. Three actual nonparallel controls

The recovery unit applies that construction to these literal projectivities:

| p=(h,k,l) | Minimum vertex denominator | Maximum vertex denominator | Tangent of the acute angle between the end planes |
|---|---:|---:|---:|
| `(1,-1,1/2)` | `579/800` | `1429/800` | `2*sqrt(2)/3` |
| `(-1,1,-1/2)` | `171/800` | `1021/800` | `2*sqrt(2)` |
| `(1/2,1,1)` | `691/640` | `43/20` | `sqrt(5)/4` |

All denominators are strictly positive, so all three are genuine uniformly refilled 10/17/9 bodies with the same true cycles. The end-plane angles are substantial in the displayed coordinates; none of these is a microscopic perturbation of a parallel-end body.

The construction gives a rational frame and an exact integer L0 for each. The report generated by the code contains the actual centroid, all poles, the selected frame, M(L0), its exact inverse, all 68 polynomial certificates, and the complete labelled census. The theorem proves the counts (2,2,2) and weak-freedom, but does **not** assert a preferred root label before the exact frame selection is performed.

### Correction to the unfinished notes

The unfinished notes also used the different fixed frame

```
F=((1,2,-1),(7,-4,-1),(1,1,3)).
```

Its inverse is

```
(( 1/6,  7/66, 1/11),
 ( 1/3, -2/33, 1/11),
 (-1/6, -1/66, 3/11)).
```

The previously recorded entry 13/66 in position (0,0) is wrong.

The same notes recorded vertex 1 as an unstable root throughout a large-L ray with leading axis u=(1,2,-1) on the first projectivity above. That all-ray claim is also wrong. The exact projected values are

`u.Z1=629/1429`, and `u.Z2=476/823`.

Every tetrahedron in the actual positive fan has its u-centroid below 1/3. Indeed, the largest possible sum of its three non-apex projections occurs at labels 6,4,3 and is

`51/320+442/579+119/117 < 1/6+4/5+49/48 < 2`,

while `u.Z7=-2/3`. The actual uniformly weighted centroid therefore satisfies `u.g<1/3`. Consequently the leading coefficient of the true primitive 1→2 is strictly greater than

`(629/1429-1/3)*(476/823-629/1429)>0`.

Vertex 1 cannot remain unstable along that ray as L tends to infinity. This correction uses the actual refilled volume geometry; it is not inferred from a freely assigned center. No all-ray census from those unfinished notes is carried forward. None of the four immutable parents is altered by this correction.

## 6. Attempted exclusion domain and remaining gap

The intended large computation targeted

```
0<=h,k<=2, l>=-1/2,
```

together with

```
1<=h,k<=2, -1<l<=-1/2.
```

In particular, it would cover the entire admissible axial interval l>-1 for every h,k in [1,2]. It was organized into a bounded direct chart, an upper chart with t in [0,1/2], and a lower chart with a in [0,1/2]. The proposed mechanism was a complete ordinary-primal stress cover of all 48,790 true rooted trees, using actual fan moments, rational within-cell coordinate changes, and rigorously outward-rounded quadratic Taylor models. That is stronger than a joint exclusion if completed, but it would not be a new root-only separator.

**The final contents and successful completion status of `nonparallel_certificate.json`, `nonparallel_tail_certificate.json`, and `nonparallel_low_certificate.json` are not substantiated in this handoff.** Their locator intermediates are ephemeral here. I give no completed coverage count, positive regional margin, certificate hash, or cold-replay claim for them. A failed or unfinished box search is not a physical survivor, and a partial library is not an exclusion.

The complete source below is authoritative for the analytic chart data and rational control construction only. It is not a replacement name for an unverified large regional certificate.

## 7. Complete recovery unit

Save the following as `nonparallel_rational_controls.py` and run, with assertions enabled:

```
python -B -S nonparallel_rational_controls.py
```

It uses CPython 3.13.5, standard library only; it is also written for Python >=3.10. There is no optimizer, randomness, external source, saved certificate, or hidden geometry input.

Expected terminal marker:

```
NONPARALLEL_CHART_AND_RATIONAL_222_RECOVERY_PASS
```

**Execution status:** this final consolidated recovery unit has not been observed running in the resumed record. The marker is a verification target, not an observed pass. Source and report byte/hash pins remain unassigned; the program prints them when executed. The analytic proofs and complete literal recovery source, rather than an unobserved hash, are the durable handoff.

```python
#!/usr/bin/env python3
"""Exact nonparallel chart and rational (2,2,2) control recovery.
Python 3.13.5, standard library only. Assertions must remain enabled.
Run: python -B -S nonparallel_rational_controls.py
"""
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

PARENTS = {
    'minimum-0269':
    '8b4cb712a53d69060ede95fbed7a083b623f87f5d5f4a8aef994b80d7f117684',
    'minimum-0225':
    'c772d9b01329dcd809a288ef999d910676c13c3334cff8c96e7d59a51b887bdd',
    'minimum-0271':
    '78c5ee7f94706f5d44ca425624faab7a07c6d99a3b0fee6ba7cb32938ba2b290',
    'minimum-0268':
    'c199a4de7b66fb757fbc3f1b2beeb903f7002fe567611824a9f0626b32aa2fc5'
}
Y = tuple(tuple(map(Q, row)) for row in (
    ('17/80', 0, 0), ('629/800', 0, 0),
    ('187/250', '51/500', 0), ('51/100', '17/50', 0),
    (0, '221/800', 0), (0, '17/80', 0),
    ('17/320', '17/320', 0), (0, 0, 1),
    ('3/20', 0, 1), (0, '3/20', 1)))
FACES = ((6,5,4,3,2,1,0), (8,7,0,1), (7,6,0),
         (1,2,8), (9,8,2,3), (9,3,4),
         (4,5,7,9), (6,7,5), (7,8,9))
FAN = tuple((7, f[0], f[j], f[j+1])
            for f in FACES if 7 not in f
            for j in range(1, len(f)-1))
I = tuple(tuple(Q(i == j) for j in range(3)) for i in range(3))
ZERO = tuple(tuple(Q(0) for _ in range(3)) for _ in range(3))


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def scale(t, a):
    return tuple(t*x for x in a)


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def transpose(A):
    return tuple(zip(*A))


def mv(A, v):
    return tuple(dot(row, v) for row in A)


def mm(A, B):
    return tuple(tuple(dot(row, col) for col in transpose(B))
                 for row in A)


def det(A):
    return dot(A[0], cross(A[1], A[2]))


def inverse(A):
    d = det(A)
    assert d
    cof = (cross(A[1], A[2]), cross(A[2], A[0]),
           cross(A[0], A[1]))
    return tuple(tuple(x/d for x in row) for row in transpose(cof))


def outer(a, b):
    return tuple(tuple(a[i]*b[j] for j in range(3)) for i in range(3))


def matadd(A, B):
    return tuple(add(a, b) for a, b in zip(A, B))


def matscale(t, A):
    return tuple(scale(t, row) for row in A)


def polynomial_matrix(coeff, t):
    out = ZERO
    for k, A in enumerate(coeff):
        out = matadd(out, matscale(t**k, A))
    return out


def principal_minors(A):
    return (tuple(A[i][i] for i in range(3))
            + tuple(A[i][i]*A[j][j]-A[i][j]**2
                    for i, j in combinations(range(3), 2))
            + (det(A),))


def six_volume(z, ids):
    a, b, c, d = (z[i] for i in ids)
    return dot(sub(b, a), cross(sub(c, a), sub(d, a)))


W0 = tuple(six_volume(Y, ids) for ids in FAN)
assert len(FAN) == 9 and min(W0) > 0
EDGE_FACES = {}
for f, face in enumerate(FACES):
    for i, j in zip(face, face[1:] + face[:1]):
        EDGE_FACES.setdefault(tuple(sorted((i, j))), []).append(f)
EDGES = tuple(sorted(EDGE_FACES))
DUAL_EDGES = tuple(sorted(tuple(sorted(fs)) for fs in EDGE_FACES.values()))
assert len(EDGES) == len(set(DUAL_EDGES)) == 17
assert all(len(fs) == 2 for fs in EDGE_FACES.values())


def moments(z):
    weights = tuple(six_volume(z, ids) for ids in FAN)
    assert min(weights) >= 0
    D = sum(weights, Q(0))
    J = (Q(0),)*3
    for ids, w in zip(FAN, weights):
        J = add(J, scale(w, tuple(sum(z[i][j] for i in ids)
                                for j in range(3))))
    db = Q(0)
    jb = (Q(0),)*3
    for face in FACES:
        a = z[face[0]]
        for j in range(1, len(face)-1):
            b, c = z[face[j]], z[face[j+1]]
            d = dot(a, cross(b, c))
            db += d
            jb = add(jb, scale(d, add(add(a, b), c)))
    assert D > 0 and db == D and jb == J
    return D, J, scale(1/(4*D), J), weights


def hull_info(z):
    points = tuple(dict.fromkeys(z))
    supporting = {}
    for i, j, k in combinations(range(len(points)), 3):
        n = cross(sub(points[j], points[i]), sub(points[k], points[i]))
        if not any(n):
            continue
        values = tuple(dot(n, sub(a, points[i])) for a in points)
        if min(values) < 0 < max(values):
            continue
        supporting[frozenset(t for t, v in enumerate(values) if v == 0)] = n
    extreme = []
    for i in range(len(points)):
        normals = [n for f, n in supporting.items() if i in f]
        if any(det(t) != 0 for t in combinations(normals, 3)):
            extreme.append(i)
    facets = sorted({tuple(i for i in sorted(f) if i in extreme)
                     for f in supporting})
    assert all(len(f) >= 3 for f in facets)
    edges = {tuple(sorted(set(a) & set(b)))
             for a, b in combinations(facets, 2)
             if len(set(a) & set(b)) == 2}
    fv = (len(extreme), len(edges), len(facets))
    assert fv[0]-fv[1]+fv[2] == 2
    return {'points': points, 'extreme_indices': extreme,
            'facets': facets, 'edges': sorted(edges), 'fvector': fv}


def direct_body(p):
    p = tuple(map(Q, p))
    den = tuple(1+dot(p, y) for y in Y)
    assert min(den) > 0
    z = tuple(scale(1/d, y) for y, d in zip(Y, den))
    D, J, g, weights = moments(z)
    for ids, w0, w in zip(FAN, W0, weights):
        test = w0
        for i in ids:
            test /= den[i]
        assert w == test > 0
    poles = []
    supports = []
    for face in FACES:
        a, b, c = (z[i] for i in face[:3])
        n = cross(sub(b, a), sub(c, a))
        assert any(n)
        h = dot(n, a)
        slacks = tuple(h-dot(n, y) for y in z)
        assert all(slacks[i] == 0 if i in face else slacks[i] > 0
                   for i in range(10))
        height = h-dot(n, g)
        assert height > 0
        poles.append(scale(1/height, n))
        supports.append((n, h, height, slacks))
    hull = hull_info(z)
    assert hull['fvector'] == (10, 17, 9)
    assert {frozenset(f) for f in hull['facets']} == {frozenset(f) for f in FACES}
    return {'projectivity': p, 'denominators': den, 'z': z,
            'D': D, 'J': J, 'g': g, 'volume': D/6,
            'x': tuple(sub(y, g) for y in z),
            'q': tuple(poles), 'supports': supports, 'hull': hull}


def choose_axes(body):
    x, q = body['x'], body['q']
    primal = list(x) + [sub(x[j], x[i]) for i, j in EDGES]
    polar = list(q) + [sub(q[j], q[i]) for i, j in DUAL_EDGES]
    assert len(primal) == 27 and len(polar) == 26
    assert all(any(a) for a in primal+polar)
    r = None
    for candidate in range(1, 82):
        u = (Q(1), Q(candidate), Q(candidate*candidate))
        if (all(dot(u, a) != 0 for a in primal)
                and all(any(cross(u, b)) for b in polar)):
            r = candidate
            break
    assert r is not None
    s = None
    for candidate in range(1, 28):
        v = (Q(-r-candidate*r*r), Q(1), Q(candidate))
        if all(dot(v, b) != 0 for b in polar):
            s = candidate
            break
    assert s is not None
    w = cross(u, v)
    assert dot(u, v) == dot(u, w) == dot(v, w) == 0
    assert min(dot(a, a) for a in (u, w, v)) > 0
    assert max(abs(t) for a in (u, w, v) for t in a) < 2**31
    return r, s, u, w, v


def primitive(a, M, b):
    return dot(a, mv(M, sub(b, a)))


def ceil_nonnegative(x):
    x = Q(x)
    assert x >= 0
    return (x.numerator+x.denominator-1)//x.denominator


def control_ray(body):
    r, s, u, w, v = choose_axes(body)
    primal_matrices = (outer(v, v), outer(w, w), outer(u, u))
    polar_matrices = tuple(matscale(1/dot(a, a)**2, outer(a, a))
                           for a in (u, w, v))
    rows = []
    for side, vertices, edges, matrices in (
            ('primal', body['x'], EDGES, primal_matrices),
            ('polar', body['q'], DUAL_EDGES, polar_matrices)):
        for edge in edges:
            for i, j in (edge, edge[::-1]):
                co = tuple(primitive(vertices[i], A, vertices[j])
                           for A in matrices)
                assert co[2] != 0
                rows.append({'side': side, 'arrow': (i, j),
                             'coefficients_ascending': co})
    assert len(rows) == 68
    L0 = 1+max([1] + [ceil_nonnegative(
        2*(abs(row['coefficients_ascending'][0])
           + abs(row['coefficients_ascending'][1]))
        / abs(row['coefficients_ascending'][2])) for row in rows])
    M = polynomial_matrix(primal_matrices, Q(L0))
    N = matscale(Q(1, L0*L0), polynomial_matrix(polar_matrices, Q(L0)))
    assert min(principal_minors(M)) > 0
    assert min(principal_minors(N)) > 0
    assert mm(M, N) == I and inverse(M) == N
    primal_values = {}
    polar_values = {}
    for row in rows:
        c0, c1, c2 = row['coefficients_ascending']
        sign = 1 if c2 > 0 else -1
        shifted = (sign*(c0+c1*L0+c2*L0*L0),
                   sign*(c1+2*c2*L0), sign*c2)
        assert min(shifted) > 0
        i, j = row['arrow']
        if row['side'] == 'primal':
            value = primitive(body['x'][i], M, body['x'][j])
            assert value == c0+c1*L0+c2*L0*L0
            primal_values[i, j] = value
        else:
            value = primitive(body['q'][i], N, body['q'][j])
            assert value*L0*L0 == c0+c1*L0+c2*L0*L0
            polar_values[i, j] = value
        assert sign*value > 0
        row.update(sign=sign, shifted_coefficients=shifted,
                   endpoint_value=value,
                   positive_scale='1' if row['side'] == 'primal' else 'L^2')
    U = [i for i in range(10) if all(d < 0 for (a, b), d in primal_values.items() if a == i)]
    stable = [i for i in range(9) if all(d < 0 for (a, b), d in polar_values.items() if a == i)]
    saddles = []
    for edge in EDGES:
        f, g = EDGE_FACES[edge]
        if max(primal_values[edge], primal_values[edge[::-1]],
               polar_values[f, g], polar_values[g, f]) < 0:
            saddles.append(edge)
    assert (len(stable), len(U), len(saddles)) == (2, 2, 2)
    return {'r': r, 's': s, 'axes': (u, w, v), 'L_lower': L0,
            'M_polynomial': primal_matrices,
            'L_squared_N_polynomial': polar_matrices,
            'M_at_lower': M, 'N_at_lower': N, 'all_68_rows': rows,
            'census': {'S': stable, 'U': U, 'H': saddles,
                       'counts': (2, 2, 2), 'zero_primitives': 0,
                       'physical_weak_points': 0,
                       'scope': 'Every real L >= L_lower'}}


def compact_chart(h, k, t, upper):
    h, k, t = map(Q, (h, k, t))
    assert h > 0 and k > 0 and 0 <= t <= Q(1, 2)
    den = []
    z = []
    for i, y in enumerate(Y):
        if i < 7:
            d = 1+h*y[0]+k*y[1]
            raw = (y[0], y[1], Q(0))
        elif upper:
            d = 1+t*(h*y[0]+k*y[1])
            raw = (t*y[0], t*y[1], Q(1))
        elif i == 7:
            d = Q(1)
            raw = (Q(0), Q(0), Q(1))
        else:
            d = t+h*y[0]+k*y[1]
            raw = (y[0], y[1], t)
        assert d > 0
        den.append(d)
        z.append(scale(1/d, raw))
    z = tuple(z)
    D, J, g, weights = moments(z)
    for ids, w0, actual in zip(FAN, W0, weights):
        target = w0
        if upper:
            target *= t**(sum(i >= 7 for i in ids)-1)
            for i in ids:
                target /= den[i]
        else:
            for i in ids:
                if i != 7:
                    target /= den[i]
        assert actual == target
    hull = hull_info(z)
    if t == 0:
        assert g[2] == Q(1, 4)
        assert hull['fvector'] == ((8, 14, 8) if upper else (6, 10, 6))
    else:
        physical = direct_body((h, k, 1/t-1 if upper else t-1))
        physical_z = tuple((a[0], a[1], a[2]*t if upper else a[2]/t) for a in z)
        assert physical['z'] == physical_z
        assert physical['D'] == (t*D if upper else D/t)
        assert physical['g'] == (g[0], g[1], g[2]*t if upper else g[2]/t)
    return {'chart': 'upper' if upper else 'lower',
            'parameters': (h, k, t), 'z': z, 'D': D, 'J': J,
            'g': g, 'hull': hull,
            'endpoint_is_genuine_E17': t > 0}


def correction_check(first_body):
    F = tuple(tuple(map(Q, row)) for row in ((1,2,-1),(7,-4,-1),(1,1,3)))
    corrected = ((Q(1,6),Q(7,66),Q(1,11)),
                 (Q(1,3),-Q(2,33),Q(1,11)),
                 (-Q(1,6),-Q(1,66),Q(3,11)))
    assert inverse(F) == corrected and mm(F, corrected) == I
    u = F[0]
    z = first_body['z']
    assert dot(u, z[1]) == Q(629,1429)
    assert dot(u, z[2]) == Q(476,823)
    tetra_centroids = [sum(dot(u,z[i]) for i in ids)/4 for ids in FAN]
    assert max(tetra_centroids) < Q(1,3)
    assert dot(u, first_body['g']) < Q(1,3)
    leading = dot(u, first_body['x'][1])*dot(u, sub(z[2], z[1]))
    lower = (Q(629,1429)-Q(1,3))*(Q(476,823)-Q(629,1429))
    assert leading > lower > 0
    return {'fixed_frame': F, 'correct_inverse': corrected,
            'actual_centroid_projection': dot(u, first_body['g']),
            'maximum_fan_centroid_projection': max(tetra_centroids),
            'D12_leading_coefficient': leading,
            'strict_lower_bound': lower,
            'scope': 'The unfinished all-ray U={1,7} claim is withdrawn.'}


def encode(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {str(k): encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


def main():
    if not __debug__:
        raise RuntimeError('Assertions must remain enabled')
    source = direct_body((0, 0, 0))
    assert source['volume'] == Q(881291,9600000)
    assert source['g'] == (Q(7368835529,28201312000),
                           Q(3427883561,28201312000),
                           Q(50317,153268))
    parameters = ((Q(1),-Q(1),Q(1,2)),
                  (-Q(1),Q(1),-Q(1,2)),
                  (Q(1,2),Q(1),Q(1)))
    bounds = ((Q(579,800),Q(1429,800)),
              (Q(171,800),Q(1021,800)),
              (Q(691,640),Q(43,20)))
    controls = []
    for p, interval in zip(parameters, bounds):
        body = direct_body(p)
        assert (min(body['denominators']),max(body['denominators'])) == interval
        controls.append({'body': body, 'ray': control_ray(body)})
    charts = [compact_chart(h,k,0,upper)
              for upper in (False,True)
              for h,k in product((Q(1),Q(2)),repeat=2)]
    charts += [compact_chart(1,2,Q(1,4),upper) for upper in (False,True)]
    report = {'object':'NONPARALLEL_CHART_AND_RATIONAL_222_RECOVERY_V1',
              'parents':PARENTS, 'source':source,
              'true_facets':FACES, 'true_edges':EDGES,
              'positive_fan':FAN, 'source_fan_six_volumes':W0,
              'controls':controls, 'compact_chart_checks':charts,
              'working_note_correction':correction_check(controls[0]['body']),
              'scope':'Actual rational nonparallel controls and exact chart identities. No complete projective-domain U1 or S1/U1 exclusion is certified.'}
    raw = (json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    output = Path('nonparallel_rational_controls_report.json')
    output.write_bytes(raw)
    source_bytes = Path(__file__).read_bytes()
    print(Path(__file__).name,len(source_bytes),hashlib.sha256(source_bytes).hexdigest())
    print(output.name,len(raw),hashlib.sha256(raw).hexdigest())
    print('NONPARALLEL_CHART_AND_RATIONAL_222_RECOVERY_PASS')


if __name__ == '__main__':
    main()
```

## 8. Continuation

Continue from the last accepted root-hull/two-cell parent, not from an asserted completion of the large three-chart search. The exact positive-projective fan and compactifications above give a self-contained geometric input for a fresh complete calculation. The remaining mechanical task is a completed, inspectable all-tree certificate on the compact charts, or a genuine complete one-sided survivor that makes the actual root-foot disjunction essential. Neither a partial stress library nor one of the (2,2,2) controls settles that task.
