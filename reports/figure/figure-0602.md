# figure-0602

Historical AI scientific report · saved 2026-09-28 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Keen Harbor 93 — an edge-efficient stable platform with exact finite tracking of its own-centroid foot

## 1. Status and evidence boundary

**No new own110/additionalweak000 construction is established in this continuation.** The last accepted computational frontier remains the KH123 parent: CYCLE2_FINAL_G10 is150/225/77, own121, P≈0.18259028347271145, Q[]; CYCLE3_LIMIT_G10 is166/249/85, own121, P≈0.16532516199378647, Q[].

The new result here is analytical and constructive. A three-vertex platform can replace CYCLE2's19-sided stable facet by a triangle entirely below the surviving P death, at **22 additional true edges rather than25**. This gives, for sufficiently small positive rational parameters, a family with **V153/E247/F96, own121/additionalweak000**. More importantly, the platform has an explicit rational tangential motion that keeps its marked interior point **exactly equal to the projection of the actual new uniform-volume centroid at finite amplitude**. This is not a frozen-centre construction, a first-order rank argument, or a claim that other stable equilibria cannot appear.

A second result sharply limits what such low additions can accomplish: the parent's two-block certificate extends to certain genuine outer hulls with changed facets and new edges. When all added points remain below the old P-death radius and the actual centroid stays in an explicitly defined smaller cube, both old radial basins still contain unstable equilibria. Thus low-carrier installation alone cannot complete P; the subsequent construction must leave that radius/mass envelope or remove old material.

A seven-vertex rational control below instantiates the finite mass-tracking formula. Its derived class is648, not110. It demonstrates both the exact foot tracking and the danger of assuming that tracking one stable facet prevents births elsewhere.

### Reading and runtime limitation

The current assignment names `research-journal(20260928-174745).md`,399752 bytes, SHA-256 `3574528de559979661496105113fa074699d06122472c322d007c7726d42e747`. The retained completed reading from the preceding attempt reaches native line1390. Requests for1391–1590 and1591–EOF were made, but their returned text is not inspectable in this continuation. I therefore do **not** claim a newly completed EOF read or a fresh hash verification. The previously visible complete KH123 handoff and the current assignment supply the parent facts used below.

Runtime probes and proposed scan calls also did not provide inspectable terminal output here. Consequently, **no new scan, extracted coordinate array, endpoint audit, or numerical trajectory is counted as an executed result**. This does not establish that the mounted files are lost. In particular, the existing KH123 exact results are not invalidated by this execution boundary.

The controlling parent remains `figure-0601`, SHA-256 `ba133c3f50e7ba2c881a6dad284f404afd2be90c3a32ad166517aeb33b621f9f`. The complete77-row CYCLE2 input was not recovered into inspectable literal text during this continuation. Its previously reported input identity is2723 bytes, SHA-256 `15bd743f76a69e8bec0c7b348adff53a33d62742729cadf9aba5e6f796b5bf48`. **That hash is not supplied as a substitute for the coordinates.** Accordingly, no new instantiated KH123 successor is claimed to have a closed inline recovery capsule here. The mathematical construction and the independent seven-point arithmetic control are completely specified below.

## 2. A three-point platform with the minimum edge cost in its retained-boundary class

Let K be a rational convex3-polytope with own uniform centroid g. Let F be its unique strictly stable maximal facet, with m vertices, and assume no additional weak equilibria. Write its outward plane as

`N·x=h_raw`,

and define

`h=h_raw−N·g>0`,

`d=N/(N·N)`,

`f=g+h d`.

Thus f is the actual stable foot. All following tangential vectors are perpendicular to N.

Choose a triangle T strictly inside F, containing f strictly, such that its three outward edge-normal directions are three outward edge-normal directions of F. For a19-gon such a choice exists. One way to see this is to choose an edge-normal direction whose opposite is not another edge-normal direction, then use the two consecutive directions straddling its opposite. The three positively span the tangent plane. An odd number of distinct outward edge directions guarantees the required unmatched direction.

For a positive lift β, initially consider the three new points

`w_i=b_i+βd`,  i=0,1,2,

where b_i are the vertices of T. Require each w_i to satisfy every old support other than F strictly. Then

`K_β=conv(K,w_0,w_1,w_2)`

is exactly K together with the prismoid `conv(F,T+βd)`, meeting along F. This is one actual added region, not a sum of potentially overlapping caps.

### Exact maximal-face count

The three selected parallel edge pairs produce three quadrilateral lateral facets. Each of the other m−3 old F-edges produces a triangular lateral facet. There are no additional lateral facets, because every top-triangle edge direction already occurs in the base polygon's normal fan.

Every old vertex and every old edge survives. The old facet F is replaced by the m lateral facets and the top triangle. Consequently,

`ΔV=3`,

`ΔF=m`,

`ΔE=m+3`.

For CYCLE2, m=19, so the resulting counts are

**V153/E247/F96.**

These are maximal facets and true edges; the three quadrilaterals must not be triangulated when reporting E.

### Optimality of this edge cost — and its scope

Within the class that retains every old vertex and old edge, adds exactly three vertices forming a top triangular facet, and replaces only F, at least m lateral facets are necessary. A non-base plane intersects the old F-plane in a line and therefore cannot contain two distinct noncollinear edges of the strictly convex base polygon. Euler then gives

`ΔE=ΔV+ΔF≥3+m`.

The parallel-edge construction attains this bound. This is **not** minimum complexity among arbitrary replacements: retiring old vertices, changing other facets, using a different top boundary, or changing the original body escapes the statement.

The generic three-point platform has m+3 lateral facets and costs m+6 edges. The three exact parallelisms save three genuine edges. In particular, a straightforward three-stage stellar installation on the19-gon would cost25 edges and reach E250; this platform costs22 and reaches E247.

## 3. Installing an entire stable triangle below the current P death

Let D be the squared radius of the surviving strict saddle of the parent, measured from g. Since F is the unique stable facet,

`|f−g|²<D`.

Choose a rational L strictly between these values. Shrink the chosen parallel-edge triangle about f until every b_i satisfies

`|b_i−g|²<L`.

The whole triangle then lies inside that squared-radius sublevel by convexity of squared norm.

This shrink can be made entirely rational. For example, normalize every tangential outward base-edge inequality to

`u_j·(x−f)≤1`.

For the selected three indices, form the bounded triangle

`T_0={t:N·t=0, u_j·t≤1 for the three selected j}`.

Its vertices t_i are obtained by rational3×3 solves. Let

`M=max_i |t_i|²`,

`δ=L−|f−g|²>0`.

Any positive rational η satisfying

`η≤1/2`,

`η≤δ/[2(M+1)]`,

`η≤1/[2(1+max_i|u_j·t_i|)]` for every base edge j

gives `b_i=f+ηt_i` strictly inside F and below L.

For all sufficiently small positive β, including the centroid-tracking motion in the next section, the final top triangle remains wholly below the **new actual** saddle death. The complete own121 census persists on a sufficiently small positive interval:

* The old U vertices are not on F in CYCLE2. Their local supporting stars are unchanged, and their strict guards persist under the actual centroid displacement.
* Every new top vertex has a positive chord to an old point of F at β=0, because it is an interior point different from f. That strict exclusion persists for small positive β.
* The new top facet is strictly stable. Every lateral facet has its limiting projection at f, which lies outside that lateral polygon. Thus the lateral facets are nonstable for sufficiently small β.
* On every newly introduced edge, the limiting normal cone collapses to the old facet normal. Since f is not on any such edge, the radial direction cannot create a closed edge equilibrium there for sufficiently small β. Old edge classes persist.

Thus the small family is own121, not merely reference121, with one positive P and Q empty. This is an existence-and-construction theorem for a rational family. **No particular β or new CYCLE2 coordinate array was audited in this continuation.**

F96 also changes the available parameterization. E247 does not permit arbitrary release of96 support normals under the F85 bound. The parallelisms and inherited incidence are material features of this construction, not optional metadata.

## 4. Exact finite mass response of the platform

Work temporarily in coordinates centred at the old g. Then F lies in `N·x=h` and f=hd.

For the fixed tangential triangle T, let C_β be the added prismoid. Its exact volume and first moment have the form

`V(C_β)=βv`,

`M(C_β)=βm_1+β²m_2`.

These are finite identities. They follow either from its cross-sections or from the oriented boundary determinants: all moving vertices have the same velocity d, so determinants have degree at most one in β, and first moments have degree at most two.

Put

`c=m_1/v`,

`κ=(N·m_2)/v`.

Then

`N·c=h`,

`m_2=κv d`.

The constants are rational and can be computed without differentiation. If exact prismoid integrals at heights1 and2 are M(1),M(2), then

`m_2=[M(2)−2M(1)]/2`,

`m_1=2M(1)−M(2)/2`.

Let A be the base area, B the mixed area of the two planar polygons, and C the top area. Their common irrational Euclidean area factor cancels in

`κ=(A+2B+3C)/[4(A+B+C)]`.

Because the top triangle is strictly inside the base polygon,

`1/4<κ<1/2`.

The original body's volume is V_0. Without a tangential correction, its new actual centroid is

`g_β−g = a(c+κβd)`,

where

`a=βv/(V_0+βv)`.

In particular, the normal displacement is

`N·(g_β−g)=a(h+κβ)>0`.

The old centroid is therefore not retained by this outward addition. No density adjustment or reference-origin substitution is involved.

## 5. Finite tangential motion that tracks the actual stable foot exactly

Translate the top triangle tangentially by t while keeping its shape and orientation. At cross-section parameter τ, this translates the section by τt without changing its area. Therefore v and κ do not change, and the exact first-moment coefficient changes by

`m_1(t)=m_1+κv t`.

Write

`c_T=c−hd`.

The new own centroid has tangential component

`(g_β−g)_T=a(c_T+κt)`.

To make the marked point f+t on the translated triangle track this tangential component, solve

`t=a(c_T+κt)`.

The finite solution is

**`t(β)=βv c_T/[V_0+(1−κ)βv]`.**

The denominator is positive for every β>0. With the actual three new material points

**`w_i(β)=b_i+t(β)+βd`,**

the actual uniform centroid is exactly

`g_β=g+t(β)+a(h+κβ)d`.

Its orthogonal projection onto the new top plane is exactly

**`f_β=f+t(β)+βd`.**

This point is the same marked strict interior point of the translated top triangle. Hence the top remains strictly stable for **every finite β for which the stated prismoid/visibility geometry is valid**. This is an instantiated boundary motion formula, not a claim that a mass Jacobian has rank three.

The entire construction is rational for rational input and rational β.

### Exact finite visibility conditions

For another old support `n_j·x≤h_j`, put

`A_ji=h_j−n_j·b_i>0`,

`B=(1−κ)v`.

The condition that w_i(β) remain strictly inside that support is exactly

`−V_0 A_ji + β[−B A_ji+V_0(n_j·d)+v(n_j·c_T)] + B(n_j·d)β² < 0`.

Thus the whole retained-facet interval is controlled by finitely many explicit quadratic inequalities. No numerical retraction or old-fan volume extrapolation is needed inside it. Once one of these inequalities fails, the actual hull must be rebuilt; the prismoid chart must not be extended past contact by assertion.

### What the exact foot tracking does not protect

It does not protect other old facets from becoming stable, exclude stable lateral facets at large β, or cancel U.

A useful sufficient lateral-facet test is also explicit. For a tangential outward base-edge normal u, let b>0 be the top triangle's support relative to its marked point, let ℓ>0 be the base support relative to f, and put

`α=[ℓ−u·t−b]/β`.

The lateral plane has normal `u+αN`. Let

`H=h+β−a(h+κβ)`

be the top plane's own-centred unnormalized height. Its orthogonal foot lies strictly above the top plane whenever

`α b |N|²−H|u|²>0`.

Equivalently, its own-centred polar normal has a positive chord to the top normal. This is sufficient to exclude that lateral S, not necessary. The small-β family satisfies it, but finite thickening can cross it even though the top foot remains exactly tracked.

## 6. A whole-basin obstruction that survives some new facets and edges

The accepted CYCLE2 parent has two nonempty disjoint old vertex blocks with negative outward true-edge guards throughout the closed reference-centre cube of radius1/128 about its own g. A maximum-radius vertex in each block is therefore a strict U of the old body at every centre in that cube, even when the maximizing labels change.

The following extension is useful for the proposed platform and for other outer additions.

### General low-addition lemma

Let c be an interior point at which K has two strict radial maxima u_1,u_2. Let

`L=conv(K,A)`.

If every added point satisfies

`|a−c|<min(|u_1−c|,|u_2−c|)`,

then both u_1 and u_2 remain strict U of L at c. Indeed, their radial normals already strictly support K, and for every added a,

`(u_i−c)·(a−u_i) ≤ |u_i−c||a−c|−|u_i−c|² < 0`.

This allows arbitrary numbers of added points, changes of facets and edges, and retirement of other old vertices. It does not require a retained old witness policy for the added points.

### Quantitative application using the parent's two blocks

Let B be the original junior U squared radius, and D its original P-death squared radius. Choose any rational R with

`R>max_v|v−g|`.

Define

**`ρ=min(1/128,(B−D)/(8R))`.**

Suppose all added points satisfy `|a−g|²≤D`, and the actual homogeneous centroid c of L satisfies `||c−g||∞≤ρ`.

At c, each old block still has a strict radial maximum of K. Its radius is at least the radius of the corresponding old U evaluated at c, hence at least `sqrt(B)−sqrt(3)ρ`. Every added point has radius at most `sqrt(D)+sqrt(3)ρ`. But

`sqrt(B)−sqrt(D)=(B−D)/(sqrt(B)+sqrt(D))>(B−D)/(2R)>2sqrt(3)ρ`.

Therefore every added point is strictly shorter than both block maxima, and the low-addition lemma preserves two strict U in the actual final L.

**Conclusion:** no such outer hull can be own110. This is a finite family statement with actual mass, not a fixed-surface-only statement and not a failed optimizer.

Its scope is essential. It does not exclude added points above the old death radius, greater actual-centroid displacement, removal or motion of old material, or another seed. It also does not equate the old-reference radius condition with being below a newly computed death at a changed centre.

This gives a concrete next requirement. Installing a low stable platform is useful carrier separation, but completing P afterwards must leave at least one of these conditions. Raising a genuine crossing carrier above the old death, moving the own centre beyond the certified envelope, or replacing old material is substantive; merely keeping every new point low is not.

No numerical value for the additional `(B−D)/(8R)` bound is asserted here, because the literal CYCLE2 coordinates and exact B,D were not inspectably recovered in this continuation.

## 7. Fully literal rational control of the finite mass-tracking formula

This is an arithmetic and geometry control, **not a KH123 successor or a new target candidate**.

Start with the tetrahedron

`D=(0,0,−3)`,

`A=(−1,−1,1)`,

`B=(2,−1,1)`,

`C=(−1,2,1)`.

It has uniform volume6 and centroid0. Its stable base lies in z=1 with foot(0,0,1). Take a half-size parallel triangle translated tangentially by(1/8,0,0), and lift by β=1/4.

For this prismoid,

`v=21/8`, `κ=11/28`, `c_T=(11/224,0,0)`.

The finite tracking translation is exactly

`t=(11/2184,0,0)`.

The final body is the convex hull of the four old points and

`a=(−101/273,−1/2,5/4)`,

`b=(617/546,−1/2,5/4)`,

`c=(−101/273,1,5/4)`.

Its exact uniform mass is

`V=213/32`,

`M=(781/23296,0,369/512)`,

`g=(11/2184,0,123/1136)`.

The projection onto the top facet is exactly

`(11/2184,0,5/4)`,

strictly inside that triangle. Thus the tangential tracking effect is nonzero and physically instantiated at finite amplitude.

### Maximal lattice and census

Using vertex order `[D,A,B,C,a,b,c]`, the seven oriented maximal facets are

```text
[0,2,1]
[0,1,3]
[0,3,2]
[4,5,6]
[1,2,5,4]
[3,1,4,6]
[2,3,6,5]
```

The body is **V7/E12/F7**, with three genuine quadrilateral lateral facets.

Direct rational guard evaluation gives:

`strict(S,U,H)=(6,4,8)`,

`additionalweak=(0,0,0)`.

Stable facet indices are `[0,1,2,3,4,5]`; unstable vertices are `[0,1,2,3]`; saddle edges are

```text
[0,1] [0,2] [0,3] [1,2] [1,3] [4,5] [4,6] [5,6]
```

In particular, two lateral facets have become stable. Exact top-foot tracking did not preserve the parent's stable census. For the AB lateral facet the sufficient exclusion numerator is `1−H=−161/1136<0`, where `H=1297/1136`; its own foot is actually inside the lateral quadrilateral.

These are analytically derived rational values. The executable verifier below is complete, but its terminal output was **not observed** in this continuation. It is not described as a completed runtime audit.

### Every positive bar, as complete exact rational expressions

Set

`x=11/2184`, `z=123/1136`, `H=5/4−z`,

`W=x²+(3+z)²`,

`B_A=(1+x)²+1+(1−z)²`,

`B_B=(2−x)²+1+(1−z)²`,

`B_C=(1+x)²+4+(1−z)²`,

`D_AD=W−[x−4(3+z)]²/18`,

`D_BD=W−[−2x−4(3+z)]²/21`,

`D_CD=W−[x−4(3+z)]²/21`,

`D_AB=1+(1−z)²`,

`D_AC=(1+x)²+(1−z)²`.

The complete positive P list is

```text
1−D_CD/B_C
1−D_BD/B_B
1−D_AC/B_A
```

The complete positive Q list is

```text
1−(3+4x+z)²/(17 D_AD)
1−(961/273+x−688z/273)²/((1+(688/273)²)(H²+9/64))
1−H²/(H²+25/128)
1−(3−2z)²/(5(H²+1/4))
1−(3+z)²/(17 D_AB)
```

These expressions specify exact rational numbers, not toleranced decimals. No other positive P or Q is asserted absent on the basis of a floor.

## 8. Complete standalone control verifier

Save as `platform_control.py` and run `python platform_control.py`. It requires only the Python standard library. It reconstructs the seven literal vertices, checks every supporting triple against the given maximal lattice, integrates positive tetrahedra, evaluates strict and additional-weak S/U/H, computes all positive primal/polar bars, and checks the complete rational expressions above.

Expected, **unobserved here**, terminal marker:

`PLATFORM_FINITE_CONTROL_OWN648_NOT110`

The program prints the actual output byte count and SHA-256. No unobserved output hash is invented.

```python
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def scale(t, a):
    return tuple(t*x for x in a)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def det(a, b, c):
    return dot(a, cross(b, c))


def mean(points):
    return tuple(sum(p[k] for p in points)/len(points)
                 for k in range(3))


P = [
    (F(0), F(0), F(-3)),
    (F(-1), F(-1), F(1)),
    (F(2), F(-1), F(1)),
    (F(-1), F(2), F(1)),
    (F(-101, 273), F(-1, 2), F(5, 4)),
    (F(617, 546), F(-1, 2), F(5, 4)),
    (F(-101, 273), F(1), F(5, 4)),
]
faces = [
    [0, 2, 1], [0, 1, 3], [0, 3, 2], [4, 5, 6],
    [1, 2, 5, 4], [3, 1, 4, 6], [2, 3, 6, 5],
]
o = mean(P)
normals = []
supports = []
edges = {}
orientations = {}
for fi, face in enumerate(faces):
    a, b, c = [P[i] for i in face[:3]]
    n = cross(sub(b, a), sub(c, a))
    h = dot(n, a)
    assert dot(n, n) > 0 and dot(n, o) < h
    assert all(dot(n, p) <= h for p in P)
    assert {i for i, p in enumerate(P) if dot(n, p) == h} == set(face)
    for k in range(len(face)):
        a, b, c = [P[face[(k+j) % len(face)]] for j in range(3)]
        assert dot(n, cross(sub(b, a), sub(c, b))) > 0
    normals.append(n)
    supports.append(h)
    for i, j in zip(face, face[1:]+face[:1]):
        e = tuple(sorted((i, j)))
        edges.setdefault(e, []).append(fi)
        orientations[e] = orientations.get(e, 0)+(1 if i < j else -1)
assert len(edges) == 12
assert all(len(v) == 2 for v in edges.values())
assert all(v == 0 for v in orientations.values())
assert len(P)-len(edges)+len(faces) == 2

# Exhaust every supporting triple; coplanar triangles are grouped as one facet.
found = set()
for ids in combinations(range(len(P)), 3):
    a, b, c = [P[i] for i in ids]
    n = cross(sub(b, a), sub(c, a))
    if dot(n, n) == 0:
        continue
    values = [dot(n, sub(p, a)) for p in P]
    if max(values) <= 0 or min(values) >= 0:
        found.add(frozenset(i for i, v in enumerate(values) if v == 0))
assert found == {frozenset(face) for face in faces}

# Positive tetrahedral uniform-volume integration.
W = F(0)
T = (F(0), F(0), F(0))
for face in faces:
    a = P[face[0]]
    for k in range(1, len(face)-1):
        b, c = P[face[k]], P[face[k+1]]
        w = det(sub(a, o), sub(b, o), sub(c, o))
        assert w > 0
        W += w
        T = add(T, scale(w, add(add(o, a), add(b, c))))
volume = W/6
g = scale(1/(4*W), T)
moment = scale(volume, g)
assert volume == F(213, 32)
assert g == (F(11, 2184), F(0), F(123, 1136))
assert moment == (F(781, 23296), F(0), F(369, 512))
X = [sub(p, g) for p in P]

S, U, H = [], [], []
weak = [0, 0, 0]
polar = []
for fi, (face, n, h) in enumerate(zip(faces, normals, supports)):
    hc = h-dot(n, g)
    assert hc > 0
    polar.append(scale(1/hc, n))
    foot = add(g, scale(hc/dot(n, n), n))
    guards = [dot(n, cross(sub(P[j], P[i]), sub(foot, P[i])))
              for i, j in zip(face, face[1:]+face[:1])]
    if min(guards) > 0:
        S.append(fi)
    elif min(guards) >= 0:
        weak[0] += 1
neighbours = [set() for _ in P]
for i, j in edges:
    neighbours[i].add(j)
    neighbours[j].add(i)
for i, adjacent in enumerate(neighbours):
    guards = [-dot(X[i], sub(X[j], X[i])) for j in adjacent]
    if min(guards) > 0:
        U.append(i)
    elif min(guards) >= 0:
        weak[1] += 1
for (i, j), (fa, fb) in sorted(edges.items()):
    d = sub(X[j], X[i])
    dd = dot(d, d)
    t = -dot(X[i], d)
    z = add(scale(dd, X[i]), scale(t, d))
    n, q = normals[fa], normals[fb]
    nn, qq, nq = dot(n, n), dot(q, q), dot(n, q)
    assert nn*qq-nq*nq > 0
    alpha = dot(z, n)*qq-dot(z, q)*nq
    beta = dot(z, q)*nn-dot(z, n)*nq
    guards = [t, dd-t, alpha, beta]
    if min(guards) > 0:
        H.append([i, j])
    elif min(guards) >= 0:
        weak[2] += 1
assert S == [0, 1, 2, 3, 4, 5]
assert U == [0, 1, 2, 3]
assert H == [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3],
             [4, 5], [4, 6], [5, 6]]
assert weak == [0, 0, 0]


def bars(points, edge_list):
    radius = [dot(p, p) for p in points]
    events = []
    for i, j in sorted(edge_list):
        d = sub(points[j], points[i])
        dd = dot(d, d)
        assert dd > 0
        t = -dot(points[i], d)/dd
        if t <= 0:
            level = radius[i]
        elif t >= 1:
            level = radius[j]
        else:
            level = radius[i]-dot(points[i], d)**2/dd
        assert level <= min(radius[i], radius[j])
        events.append((level, i, j))
    parent = list(range(len(points)))
    peak = parent[:]

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    out = []
    for level, i, j in sorted(events, key=lambda e: (-e[0], e[1], e[2])):
        a, b = find(i), find(j)
        if a == b:
            continue
        if (radius[peak[a]], peak[a]) < (radius[peak[b]], peak[b]):
            a, b = b, a
        birth = radius[peak[b]]
        assert birth >= level
        if birth > level:
            out.append(dict(root=peak[b], elder=peak[a],
                            birth=birth, death=level,
                            depth=(birth-level)/birth,
                            edge=[i, j]))
        parent[b] = a
    return out


PB = bars(X, edges)
QE = {tuple(sorted(v)) for v in edges.values()}
QB = bars(polar, QE)
x, z = F(11, 2184), F(123, 1136)
height = F(5, 4)-z
ww = x*x+(3+z)**2
ba = (1+x)**2+1+(1-z)**2
bb = (2-x)**2+1+(1-z)**2
bc = (1+x)**2+4+(1-z)**2
dad = ww-(x-4*(3+z))**2/18
dbd = ww-(-2*x-4*(3+z))**2/21
dcd = ww-(x-4*(3+z))**2/21
dab = 1+(1-z)**2
dac = (1+x)**2+(1-z)**2
expected_p = [1-dcd/bc, 1-dbd/bb, 1-dac/ba]
expected_q = [
    1-(3+4*x+z)**2/(17*dad),
    1-(F(961, 273)+x-F(688, 273)*z)**2 /
      ((1+F(688, 273)**2)*(height**2+F(9, 64))),
    1-height**2/(height**2+F(25, 128)),
    1-(3-2*z)**2/(5*(height**2+F(1, 4))),
    1-(3+z)**2/(17*dab),
]
assert min(expected_p+expected_q) > 0
assert sorted(b['depth'] for b in PB) == sorted(expected_p)
assert sorted(b['depth'] for b in QB) == sorted(expected_q)
assert len(PB) == 3 and len(QB) == 5

# The tracked top foot is not the old centroid or a nominated substitute.
top_foot = add(g, (F(0), F(0), F(5, 4)-g[2]))
assert top_foot == (F(11, 2184), F(0), F(5, 4))
result = dict(vertices=P, maximal_facets=faces,
              edges=[list(e) for e in sorted(edges)],
              V=7, E=12, F=7, volume=volume,
              first_moment=moment, centroid=g,
              strict=[len(S), len(U), len(H)], additional_weak=weak,
              stable_facets=S, unstable_vertices=U, saddle_edges=H,
              top_foot=top_foot, P_bars=PB, Q_bars=QB)
data = (json.dumps(result, default=str, sort_keys=True,
                   separators=(',', ':'))+'\n').encode()
Path('PLATFORM_CONTROL_EXACT.json').write_bytes(data)
print(len(data), hashlib.sha256(data).hexdigest())
print('PLATFORM_FINITE_CONTROL_OWN648_NOT110')
```

## 9. Consequence for the actual KH123 continuation

The proposed CYCLE2 stage is not another arbitrary descent of its largest P. It changes the stable boundary from the original19-gon to an entirely low triangle, uses the minimum22-edge cost in the stated retained-boundary class, and has a finite rational mass-coupled motion that prevents the new top foot from leaving that triangle. Its contact boundary is explicitly quadratic rather than an unquantified compensator capacity.

However, the low-addition theorem proves that this installation cannot by itself cancel the whole P basin while remaining in the stated old-radius and own-centre envelope. A subsequent constructive step must genuinely cross that envelope, introduce a high crossing carrier, or replace old material. At finite amplitude the other old and lateral stable guards must also be recomputed; the648 control shows why the tracked top facet alone is insufficient.

For actual computation, CYCLE2 is preferable to CYCLE3 for this particular operation: CYCLE2 yields E247, whereas the analogous operation on CYCLE3's20-gon would add23 edges to E249 and exceed the target. This comparison concerns the mechanism, not a ranking by P alone.

The outstanding input dependency is the complete literal77-row `KH123_CYCLE2_FINAL_G10.txt` and its exact parent lattice/mass, already contained in the retained KH123 bundle but not inspectably exported in this continuation. No new named KH123 endpoint, audited β interval, executed numerical termination, or complete chosen-seed inline recovery is claimed. The new durable content of this handoff is the construction theorem, its exact finite mass/foot formulas, the scoped whole-basin obstruction, and the fully literal rational arithmetic control above.
