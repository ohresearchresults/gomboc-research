# minimum-0022

AI research report · 2026-09-08 UTC

---

# Clear Raven 24 — Entire homogeneous-pyramid class excluded

## 1. Determination

**The octagonal wheel is excluded over its entire real realization space. A stronger all-pyramid theorem holds.**

**Theorem.** Let \(K=\operatorname{conv}(A,B)\subset\mathbb R^3\) be a full-dimensional convex pyramid, where \(B\) is any convex polygon, and evaluate equilibria at the ordinary uniform-volume centroid of \(K\). Then

\[
\boxed{\quad S\ge2\quad\text{or}\quad U\ge2.\quad}
\]

Here \(S,U\) count strict stable maximal faces and strict unstable vertices. The conclusion remains valid when other features have zero primitives or degenerate equilibria. In particular, **no homogeneous convex pyramid with any finite number of base vertices is jointly monostable and mono-unstable**, and none has strict \((S,U,H)=(1,1,0)\).

The decisive stronger implication is

\[
\boxed{B\text{ is not strictly stable}\ \Longrightarrow\ U\ge2.}
\tag{N}
\]

Every such pyramid also has a strict unstable **base vertex** and a strict stable **lateral face**. Consequently, when the base is strictly stable there are already two stable faces; when it is not, (N) supplies two unstable vertices.

This closes **all seven stable-face/unstable-vertex root orbits, covering all 81 labelled choices**, for the nine-vertex/nine-facet/sixteen-edge octagonal wheel. Its remaining continuous frontier is empty. It does **not** close the other C32 graphs, so this result alone does not raise the supplied global bracket \(32\le C_{\min}\le1374\). :contentReference[oaicite:0]{index=0}

## 2. Source boundary and what changed

The current journal supplies the physical centroid-hardwired pyramid gauge and its coupled primal/polar formulas; its final entry expressly stops short of an exclusion. An earlier entry proves the base-unstable/lateral-stable lemma but only removes the distinguished-root cases. Those conclusions are consistent with the present result. The new step is (N), proved by maximizing the physical squared distance on the two halves of the actual planar base. It closes the remaining side-face/base-vertex root placements. No trace-cap or independent-metric relaxation is used. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

No immutable exact predecessor body was assumed. Source identity: `research-journal(20260908-033930).md`, **2,311,954 bytes**, SHA-256 `226dfd2099f017940c7018204051d705ad7ca43ea960b118b76c46735ef11d89`; relevant final anchor `2026-09-08T03:39:03.372Z`. The historical base/lateral lemma is independently reproved below, so the theorem and recovery capsule do not require that file.

## 3. One physical Euclidean frame; exact area and volume centroids

Use only translation and an orthogonal change of coordinates. Put the actual base in \(z=0\), its ordinary **area centroid** at the planar origin, and write

\[
A=(4d,0,h),\qquad d\ge0,\quad h>0,
\qquad c=(d,0,h/4).
\tag{1}
\]

The base polygon, still denoted \(B\subset\mathbb R^2\), is otherwise arbitrary. No affine whitening, bounded aspect ratio, or second metric is imposed.

For completeness, the section at height \(sh\) has area \((1-s)^2\operatorname{Area}(B)\) and planar area centroid \(s(4d,0)\). The identities

\[
\int_0^1(1-s)^2\,ds=\frac13,
\qquad
\int_0^1s(1-s)^2\,ds=\frac1{12}
\]

give exactly the ordinary solid centroid in (1). Thus there are no adjustable mass weights.

Let \(e=(d,0)\), \(p=(x,y)\in B\), and

\[
R(p)^2=|p-e|^2.
\]

After translating by the actual centroid, the base vertex and apex are

\[
v(p)=(x-d,y,-h/4),\qquad a=(3d,0,3h/4).
\]

Their actual Euclidean escape products are

\[
\begin{aligned}
D(v(p)\to a)
 &=3d(x-d)-R(p)^2-\frac{h^2}{4},\\
D(a\to v(p))
 &=3d(x-4d)-\frac{3h^2}{4}.
\end{aligned}
\tag{2}
\]

For two base points, the escape product is simply \((p-e)\cdot(w-p)\). A vertex is strictly unstable when these products are negative toward every other vertex; this is the complete strict normal-cone condition. The base is strictly stable precisely when

\[
e\in\operatorname{int}B.
\tag{3}
\]

### 3.1 Elementary proof of the required centroid reflection

The ordinary area centroid implies

\[
-\frac12 B\subseteq B.
\tag{4}
\]

Here is a self-contained proof. In any chosen linear direction, rescale the projection interval to \([0,1]\). The lengths \(\ell(t)\) of the parallel sections of a convex polygon form a nonnegative concave piecewise-linear function: the intermediate section contains the Minkowski interpolation of the two sections, which are intervals.

Every such function is a nonnegative linear combination of \(1-t\), \(t\), and the tents

\[
T_r(t)=\min\{(1-r)t,\ r(1-t)\},\qquad 0<r<1.
\]

Indeed, subtract the endpoint chord; the coefficient of each tent is the nonnegative drop in slope at its breakpoint. The centroids of the first two functions are \(1/3,2/3\), while

\[
\int T_r=\frac{r(1-r)}2,
\qquad
\int tT_r=\frac{r(1-r)(1+r)}6.
\]

Thus every section-length centroid lies in \([1/3,2/3]\). If the unscaled support interval about the area centroid is \([-\alpha,\beta]\), this says \(\beta\le2\alpha\) and \(\alpha\le2\beta\). In every direction, \(h_B(-n)\le2h_B(n)\); hence \(-p/2\in B\) for every \(p\in B\), proving (4), including its equality cases.

The subsequent lemmas actually require only (4) and the reference point in (1), not that the base balancing point be its area centroid. This slightly stronger formulation is essential when applying them to the actual polar.

## 4. A base unstable vertex and a lateral stable face always exist

### 4.1 Any farthest base vertex is strictly unstable

Choose a base vertex \(p\) maximizing \(R=|p-e|\), allowing any number of tied maximizers. For every other base vertex \(w\),

\[
(p-e)\cdot(w-p)
 =\frac{|w-e|^2-R^2-|w-p|^2}{2}
 \le-\frac{|w-p|^2}{2}<0.
\tag{5}
\]

It remains to check its actual apex spoke. Put \(u=x-d\). If \(R\ge3d\), Cauchy gives \(u\le R\), and (2) yields

\[
D(v(p)\to a)
\le-R(R-3d)-h^2/4\le-h^2/4<0.
\tag{6}
\]

If \(R\le3d\), the reflected point \(-p/2\in B\) has distance at most \(R\) from \(e\). Therefore

\[
L:=R^2-\left|-\frac{p-e}{2}-\frac{3e}{2}\right|^2
 =\frac34R^2-\frac32du-\frac94d^2\ge0.
\]

The exact identity

\[
-D(v(p)\to a)-\frac{h^2}{4}
 =\frac{(3d-R)(3d+R)}2+2L\ge0
\tag{7}
\]

again gives a strictly negative apex escape. Thus every farthest base vertex is strictly unstable, with apex-spoke margin at least \(h^2/4\). This includes \(d=0\), \(R=3d\), and all norm ties.

### 4.2 The actual polar supplies a strict lateral stable face

Let \(z_i=(u_i,w_i)\) be the actual edge poles of \(B\), so that \(B=\{p:z_i\cdot p\le1\}\). The poles of the **same physical centered pyramid** are

\[
q_B=(0,0,-4/h),
\qquad
q_i=\left(\frac{4u_i}{3},\frac{4w_i}{3},
          \frac{4(1-4du_i)}{3h}\right).
\tag{8}
\]

Direct substitution gives

\[
q_i\cdot v(p)=\frac{4z_i\cdot p-1}{3},
\qquad q_i\cdot a=1,
\qquad q_B\cdot v(p)=1,
\qquad q_B\cdot a=-3.
\]

In particular these are actual side and base poles, not independent vectors. Their convex hull is the actual polar.

Its basal polygon \(Q_s=\operatorname{conv}\{q_i\}\) has the balancing point

\[
b_*=(0,0,4/(3h)),\qquad q_B=-3b_*.
\]

It is an injective affine image \(b_*+L_*B^\circ\), where

\[
L_*(u,w)=\left(4u/3,4w/3,-16du/(3h)\right).
\]

Property (4) also holds for \(B^\circ\): for \(z\in B^\circ\) and \(p\in B\), \((-z/2)\cdot p=z\cdot(-p/2)\le1\). Hence

\[
-\frac12(Q_s-b_*)\subseteq Q_s-b_*.
\]

The reference origin equals \((q_B+3b_*)/4\). Consequently the lemma of §4.1 applies to this polar pyramid in its **actual inherited Euclidean metric**, after an orthogonal change of frame. It gives a strict unstable vertex \(q_i\) of its basal polygon.

There is no assumption that \(b_*\) is the polar base's area centroid or that zero is the polar's volume centroid. The reflection condition and quarter-height reference are exactly what the lemma uses.

For this \(q_i\), all other polar vertices satisfy \(q_j\cdot q_i<|q_i|^2\). Thus

\[
f_i=\frac{q_i}{|q_i|^2}
\]

satisfies \(q_i\cdot f_i=1\) and every other primal facet inequality strictly. It is the perpendicular foot in the relative interior of the original **lateral** face. That face is strictly stable.

## 5. New two-half maximum lemma: nonstable base forces two unstable vertices

Assume the base is not strictly stable. By (3), \(e\notin\operatorname{int}B\), so \(d>0\).

If the apex is strictly unstable, §4.1 already supplies a different strict unstable base vertex. Hence \(U\ge2\) in this entire branch.

Otherwise the apex is not strictly unstable. There is an actual base vertex \(p=(x,y)\) with \(D(a\to v(p))\ge0\). Formula (2) gives

\[
x\ge4d+\frac{h^2}{4d}>4d.
\tag{9}
\]

This implication includes an exactly zero apex escape; its final strictness comes from full dimensionality \(h>0\), not from genericity.

Write the intersection with the horizontal axis as

\[
B\cap\{y=0\}=[\ell,r]\times\{0\},\qquad \ell<0<r.
\]

Since \(e\) is not interior, \(r\le d\). Reflecting \((\ell,0)\) using (4) gives \(-\ell/2\le r\). Therefore

\[
-2d\le-2r\le\ell<0<r\le d.
\tag{10}
\]

Every point on this entire axis chord is at distance at most \(3d\) from \(e\).

The vertex in (9) cannot lie on the axis. It satisfies

\[
|p-e|>3d.
\]

Its reflection \(p'=-p/2\in B\) lies on the opposite side of the axis and satisfies

\[
|p'-e|\ge x/2+d>3d.
\tag{11}
\]

Now maximize \(F(w)=|w-e|^2\) separately on the compact convex polygons

\[
B_+=B\cap\{y\ge0\},\qquad B_-=B\cap\{y\le0\}.
\]

Both maxima exceed \(9d^2\), by (9)–(11). Neither can occur on the cut chord, by (10). A maximum can be chosen at a vertex of each clipped polygon, and an off-axis vertex of a clipped polygon is an actual vertex of \(B\). Denote them by \(v_+,v_-\); they are distinct, lie on opposite sides, and have radii \(R_+,R_->3d\).

Here is the strictness argument, including all nonroot norm ties and neighbors crossing the cut. Fix one maximizer \(v\), and take **any** other point \(w\in B\). Because \(v\) lies strictly off the cut, there exists \(0<\lambda\le1\) such that \(v+\lambda(w-v)\) remains in the same half. Maximality yields

\[
0\ge F(v+\lambda(w-v))-F(v)
 =2\lambda(v-e)\cdot(w-v)+\lambda^2|w-v|^2.
\]

Consequently

\[
(v-e)\cdot(w-v)
\le-\frac{\lambda}{2}|w-v|^2<0.
\tag{12}
\]

Thus every true base-edge direction is strictly descending at \(v\); indeed the inequality holds toward every other base vertex. Its apex direction is also strictly descending:

\[
D((v-e,-h/4)\to a)
\le3dR_v-R_v^2-h^2/4
=-R_v(R_v-3d)-h^2/4<0.
\tag{13}
\]

Both \(v_+,v_-\) are therefore strict unstable vertices of the **full three-dimensional pyramid**. This proves (N).

The proof is a whole-realization geometric alternative to wheel-tree enumeration: the cut has only two sides, and both contain an unavoidable radius maximum outside the entire apex-escape region. No prescribed outgoing tree, cotree, or nonroot radius ordering was imposed.

## 6. Completion, root coverage, and exceptional strata

If the base is strictly stable, §4.2 supplies another strict stable lateral face. Otherwise §5 supplies two strict unstable vertices. The theorem follows.

The same argument also applies to the balanced polar of §4.2. Because its base stability is equivalent to original-apex instability, it gives the useful additional necessary condition

\[
A\text{ not strictly unstable}\ \Longrightarrow\ S\ge2.
\]

Thus a homogeneous mono-unstable pyramid must have a strictly stable base, and a homogeneous monostable pyramid must have a strictly unstable apex. These do not rule out one-sided monostatic pyramids: the primary-source constructions \(P_2\in(2,1)\) and \(P_3\in(3,1)\) remain fully consistent. The source's construction is not being cited as a proof of this new exclusion. :contentReference[oaicite:3]{index=3}

For the octagon, write \(F_i=[p_i,p_{i+1},A]\), cyclically modulo 8. Its full graph automorphism group is \(D_8\): the apex is the unique degree-eight vertex, and the induced rim is an eight-cycle. The seven root representatives are

\[
(F_0,p_0),\ (F_0,p_2),\ (F_0,p_3),\ (F_0,p_4),
(F_0,A),\ (B,p_0),\ (B,A).
\]

The two base-face-root orbits are excluded by §4.2, the lateral-face/apex-root orbit by §4.1, and the four remaining lateral-face/base-vertex orbits by §5. The exact script independently enumerates all 81 pairs and their seven orbits.

**Zero tilt:** \(d=0\) makes the base foot its interior area centroid, so the first branch applies. **Boundary base foot:** \(r=d\) is expressly included in (10). **Zero apex escape:** the weak inequality in (9) still forces \(x>4d\). **Tied norms:** (5) and (12) retain strict negative directional products. **Unbounded tilt, height ratios and anisotropy:** the proof permits every \(d\ge0,h>0\) and every full-dimensional convex planar polygon. It uses no bounded parameter box or fixed positive numerical tolerance.

To connect explicitly to the journal's final gauge \(A=(0,0,3)\), \(p_i=(x_i,y_i,tx_i-1)\), its actual Euclidean base coordinates in (1) are

\[
X_i=\sqrt{1+t^2}\,x_i,\quad Y_i=y_i,
\quad d=\frac{t}{\sqrt{1+t^2}},\quad h=\frac4{\sqrt{1+t^2}}.
\]

This comes from an orthogonal frame after translating the base centroid, not an affine metric substitution. Every finite \(t\ge0\), including arbitrarily large \(t\), is covered. The excluded \(h=0\) limit is not a full-dimensional pyramid; arbitrarily small positive \(h\) is covered by the strict \(h^2/4\) term.

## 7. Exact algebraic recovery and physical audit

The universal proof is the argument above, not a finite negative sample. Its arithmetic has been replayed exactly: 15 symbolic identities, the complete octagonal root-orbit partition, and four rational octagonal physical controls. The controls include the difficult outside-base/nonunstable-apex branch, a boundary base foot, and a right pyramid with all eight base-vertex norms tied.

The source also contains `audit_pyramid(name, B, apex)`, a reusable exact witness extractor for **any rational physical three-dimensional pyramid** with its actual planar base supplied in cyclic order. It recomputes the ordinary area centroid, recomputes the volume centroid by an independent outward-tetrahedron sum, reconstructs all H-triple intersections, checks primal and actual-polar reflection, and selects two strict stable faces or two strict unstable vertices according to the theorem. Its finite execution is not a replacement for the universal convex-geometric proof.

For every true edge \(ij\) with actual incident poles \(q_f,q_g\), it computes

\[
L=|v_j-v_i|^2>0,\qquad
\Delta=|q_f|^2|q_g|^2-(q_f\cdot q_g)^2>0
\]

and all four cone components

\[
\left(-\frac{D_i}{L},-\frac{D_j}{L},
      -\frac{D_g}{\Delta},-\frac{D_f}{\Delta}\right)
=(t,1-t,\beta_f,\beta_g).
\]

Here \(D_i,D_j\) are the two directed primal escape products and \(D_f,D_g\) the two directed dual escape products. The script verifies the actual vector identity for the edge foot and normal combination, and declares a strict saddle only when all four components are positive. There are 16 true edges and 64 components in each control; no polygon triangulation diagonal enters the edge ledger.

The four controls have strict-feature counts respectively `(9,9,16)`, `(2,3,3)`, `(2,2,2)`, `(2,2,2)`. The second control has two irrelevant zero normal coefficients, each accompanied by a negative segment parameter. The fourth has a genuine boundary-foot zero component. Neither is silently discarded or called an attainer.

### Exact identities and reconstruction record

The identifier is `RAVEN24_ALL_PYRAMIDS_NO_110_V1`. All inputs and helpers are contained in the single source below. Executed dependencies: **CPython 3.13.5, SymPy 1.14.0**; geometry, moments, hull and cone calculations use standard-library `Fraction`. Assertions must remain enabled.

Save the code literally as `raven24_pyramid_check.py`, with LF newlines and a final newline. Its identity is:

- Source: **9,977 bytes**, SHA-256 `6c1bdcae2c46b4758cb304adb9b3cf273aa7554500d4fff99b9f65b7c0f05495`.
- Generated `raven24_pyramid_exact_audit.json`: **9,860 bytes**, SHA-256 `1af8f55f7ce8e60256a4bc69c5c507362a94a7243b8f5ed4ddf0f331bf0ce3c3`.

Commands:

```bash
python3 -m pip install sympy==1.14.0
python3 raven24_pyramid_check.py
sha256sum raven24_pyramid_check.py raven24_pyramid_exact_audit.json
```

Expected complete terminal output:

```text
PYRAMID_SYMBOLIC_IDENTITIES_PASS 15
OCTAGONAL_WHEEL_ROOT_ORBITS_PASS 7 81
CONTROL right_all_base_norms_tied S_U_H 9 9 16 BASE_APEX True True
CONTROL outside_base_apex_unstable S_U_H 2 3 3 BASE_APEX False True
CONTROL outside_base_apex_not_unstable S_U_H 2 2 2 BASE_APEX False False
CONTROL boundary_base_foot S_U_H 2 2 2 BASE_APEX False False
REPORT 9860 1af8f55f7ce8e60256a4bc69c5c507362a94a7243b8f5ed4ddf0f331bf0ce3c3
SOURCE 9977 6c1bdcae2c46b4758cb304adb9b3cf273aa7554500d4fff99b9f65b7c0f05495
RAVEN24_PYRAMID_ALGEBRA_AND_PHYSICAL_AUDIT_PASS
```

The terminal marker certifies this algebraic and physical replay, not an unprovided formalization of convex geometry. The concavity, polarity and two-half maximum steps are proved explicitly in §§3–5. No numerical optimization, random seed, unavailable certificate archive, or external predecessor is needed.

### Complete runnable source

```python
#!/usr/bin/env python3
"""Exact algebra/root-orbit replay and four physical octagonal controls.
The universal convex-geometric argument is in the accompanying handoff;
finite controls are regression tests, not a numerical exclusion proof.
Dependencies: CPython 3.13.5; SymPy 1.14.0. Run with assertions enabled.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sympy as s

assert s.__version__ == '1.14.0'
THEOREM = 'RAVEN24_ALL_PYRAMIDS_NO_110_V1'
PARENT = '226dfd2099f017940c7018204051d705ad7ca43ea960b118b76c46735ef11d89'
identities = []
def identity(name, lhs, rhs):
    assert s.cancel(lhs-rhs) == 0, name
    identities.append(name)

R,d,u,h,x,y,k,t,r = s.symbols('R d u h x y k t r')
D = 3*d*u-R**2-h**2/4
L = s.Rational(3,4)*R**2-s.Rational(3,2)*d*u-s.Rational(9,4)*d**2
identity('farthest_R_ge_3d', -D-h**2/4, R*(R-3*d)+3*d*(R-u))
identity('farthest_R_le_3d', -D-h**2/4, (3*d-R)*(3*d+R)/2+2*L)
identity('reflected_point_slack', L,
         R**2-((u/2+3*d/2)**2+(R**2-u**2)/4))
identity('axis_chord_radius_bound', 9*d**2-(x-d)**2, (x+2*d)*(4*d-x))
identity('base_to_apex',
         s.Matrix([x-d,y,-h/4]).dot(s.Matrix([4*d-x,-y,h])),
         3*d*(x-d)-(x-d)**2-y**2-h**2/4)
identity('apex_to_base',
         s.Matrix([3*d,0,3*h/4]).dot(s.Matrix([x-4*d,y,-h])),
         3*d*(x-4*d)-3*h**2/4)
identity('half_edge_strictness',
         (u+t*x)**2+(y+t*k)**2-u**2-y**2,
         2*t*(u*x+y*k)+t**2*(x**2+k**2))
area_tent = s.integrate((1-r)*t,(t,0,r))+s.integrate(r*(1-t),(t,r,1))
moment_tent = s.integrate((1-r)*t**2,(t,0,r))+s.integrate(r*t*(1-t),(t,r,1))
identity('tent_area', area_tent, r*(1-r)/2)
identity('tent_moment', moment_tent, r*(1-r)*(1+r)/6)
identity('tent_lower_centroid', 3*moment_tent-area_tent, r**2*(1-r)/2)
identity('tent_upper_centroid', 2*area_tent-3*moment_tent, r*(1-r)**2/2)
identity('pyramid_slice_volume', s.integrate((1-t)**2,(t,0,1)), s.Rational(1,3))
identity('pyramid_slice_moment', s.integrate(t*(1-t)**2,(t,0,1)), s.Rational(1,12))
Q = s.Matrix([4*u/3,4*k/3,4*(1-4*d*u)/(3*h)])
V = s.Matrix([x-d,y,-h/4]); A = s.Matrix([3*d,0,3*h/4])
identity('physical_side_contact', Q.dot(V), (4*(u*x+k*y)-1)/3)
identity('physical_side_apex_contact', Q.dot(A), 1)
print('PYRAMID_SYMBOLIC_IDENTITIES_PASS',len(identities))

# Complete D8 action on (side/base face, rim/apex vertex). Index 8 is distinguished.
def action(face,vertex,shift,sign):
    vv = 8 if vertex == 8 else (sign*vertex+shift)%8
    ff = 8 if face == 8 else (sign*face+shift-(sign == -1))%8
    return (ff,vv)
root_orbits = {}
for face in range(9):
    for vertex in range(9):
        orb = {action(face,vertex,k,sgn) for k in range(8) for sgn in [-1,1]}
        root_orbits.setdefault(min(orb),orb)
assert sorted(root_orbits) == [(0,0),(0,2),(0,3),(0,4),(0,8),(8,0),(8,8)]
assert sum(map(len,root_orbits.values())) == 81
assert set.union(*root_orbits.values()) == set((i,j) for i in range(9) for j in range(9))
print('OCTAGONAL_WHEEL_ROOT_ORBITS_PASS',len(root_orbits),81)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(t,a): return tuple(t*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det2(a,b): return a[0]*b[1]-a[1]*b[0]
def det3(a,b,c): return dot(a,cross(b,c))
def strings(a): return [str(x) for x in a]

BASE = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

def audit_pyramid(name,B,apex):
    """Any rational strict convex planar base in cyclic order, in physical R^3."""
    B = [tuple(F(x) for x in p) for p in B]; apex = tuple(F(x) for x in apex)
    n = len(B); assert n >= 3
    N = cross(sub(B[1],B[0]),sub(B[2],B[0])); NN = dot(N,N)
    assert NN > 0 and all(dot(N,sub(p,B[0])) == 0 for p in B)
    weights = [dot(N,cross(sub(B[j],B[0]),sub(B[j+1],B[0]))) for j in range(1,n-1)]
    assert min(weights) > 0
    total = sum(weights); b = (F(0),)*3
    for j,w in enumerate(weights,1):
        b = add(b,scale(w,add(add(B[0],B[j]),B[j+1])))
    b = scale(1/(3*total),b)
    g = scale(F(1,4),add(apex,scale(3,b)))
    assert dot(N,sub(apex,B[0])) != 0
    V = [sub(p,g) for p in B]+[sub(apex,g)]
    faces = [(i,(i+1)%n,n) for i in range(n)]+[tuple(range(n))]
    Q = []
    for f,face in enumerate(faces):
        a,c,e = (V[v] for v in face[:3])
        normal = cross(sub(c,a),sub(e,a)); hh = dot(normal,a)
        assert hh != 0
        Q.append(scale(1/hh,normal))
        if hh < 0: faces[f] = tuple(reversed(face))
    edges = sorted({tuple(sorted((face[j],face[(j+1)%len(face)])))
                    for face in faces for j in range(len(face))})
    assert (len(V),len(edges),len(faces)) == (n+1,2*n,n+1)
    volume = F(0); moment = (F(0),)*3; flux = (F(0),)*3
    for f,face in enumerate(faces):
        assert all(dot(Q[f],p) == 1 if j in face else dot(Q[f],p) < 1
                   for j,p in enumerate(V))
        for j in range(1,len(face)-1):
            a,c,e = (V[v] for v in (face[0],face[j],face[j+1]))
            normal = cross(sub(c,a),sub(e,a)); dd = det3(a,c,e)
            assert dd > 0 and dot(normal,Q[f]) > 0
            flux = add(flux,normal); volume += dd/6
            moment = add(moment,scale(dd/24,add(add(a,c),e)))
    assert flux == moment == (0,0,0)
    assert volume == total*abs(dot(N,sub(apex,B[0])))/(6*NN)
    # Positive outward flux and spanning normals prove boundedness; enumerate H vertices.
    H_vertices = set()
    for i,j,k in combinations(range(n+1),3):
        dd = det3(Q[i],Q[j],Q[k])
        if not dd: continue
        p = scale(1/dd,add(add(cross(Q[j],Q[k]),cross(Q[k],Q[i])),cross(Q[i],Q[j])))
        if all(dot(q,p) <= 1 for q in Q): H_vertices.add(p)
    assert H_vertices == set(V)
    # Actual base reflection, then actual polar-base reflection about -Q[n]/3.
    for p in B:
        reflected = sub(scale(F(1,2),sub(scale(3,b),p)),g)
        assert dot(Q[n],reflected) == 1
        assert all(dot(q,reflected) <= 1 for q in Q[:n])
    dual_b = scale(F(-1,3),Q[n])
    assert dot(V[n],dual_b) == 1
    for q in Q[:n]:
        reflected = scale(F(1,2),sub(scale(3,dual_b),q))
        assert dot(V[n],reflected) == 1
        assert all(dot(p,reflected) <= 1 for p in V[:n])
    U = [i for i,p in enumerate(V) if all(dot(p,sub(q,p)) < 0 for j,q in enumerate(V) if j != i)]
    S = [i for i,p in enumerate(Q) if all(dot(p,sub(q,p)) < 0 for j,q in enumerate(Q) if j != i)]
    H = []; edge_ledger = []
    for a,c in edges:
        f,gg = [f for f,face in enumerate(faces) if a in face and c in face]
        e = sub(V[c],V[a]); LL = dot(e,e)
        da,dc = dot(V[a],e),-dot(V[c],e)
        df,dg = dot(Q[f],sub(Q[gg],Q[f])),dot(Q[gg],sub(Q[f],Q[gg]))
        delta = dot(Q[f],Q[f])*dot(Q[gg],Q[gg])-dot(Q[f],Q[gg])**2
        assert LL > 0 and delta > 0
        cone = (-da/LL,-dc/LL,-dg/delta,-df/delta)
        assert cone[0]+cone[1] == 1
        assert add(V[a],scale(cone[0],e)) == add(scale(cone[2],Q[f]),scale(cone[3],Q[gg]))
        if min(cone) > 0: H.append((a,c))
        edge_ledger.append(dict(edge=[a,c],faces=[f,gg],cone=strings(cone)))
    base_stable,apex_unstable = n in S,n in U
    far_base = max(range(n),key=lambda i:dot(V[i],V[i]))
    far_side = max(range(n),key=lambda i:dot(Q[i],Q[i]))
    assert far_base in U and far_side in S
    if base_stable:
        witness_type,witness = 'S',[n,far_side]
    elif apex_unstable:
        witness_type,witness = 'U',[n,far_base]
    else:
        cut_normal = cross(N,sub(apex,b)); assert dot(cut_normal,cut_normal) > 0
        signs = [dot(cut_normal,sub(p,b)) for p in B]
        witness_type = 'U'
        witness = [max((i for i in range(n) if sg*signs[i] > 0),
                       key=lambda i:dot(V[i],V[i])) for sg in [-1,1]]
    assert len(set(witness)) == 2
    assert all(i in (S if witness_type == 'S' else U) for i in witness)
    assert base_stable or len(U) >= 2
    assert apex_unstable or len(S) >= 2
    assert (len(S),len(U)) != (1,1)
    print('CONTROL',name,'S_U_H',len(S),len(U),len(H),'BASE_APEX',base_stable,apex_unstable)
    return dict(name=name,source_base=[strings(p) for p in B],source_apex=strings(apex),
        base_centroid=strings(b),source_centroid=strings(g),centered_volume=str(volume),
        centered_moments=['0','0','0'],vertices=[strings(p) for p in V],
        facet_poles=[strings(q) for q in Q],faces=faces,edges=edge_ledger,
        stable=S,unstable=U,saddles=H,strict_counts=[len(S),len(U),len(H)],
        base_stable=base_stable,apex_unstable=apex_unstable,
        witness_type=witness_type,witness=witness,
        zero_edge_components=sum(x == '0' for e in edge_ledger for x in e['cone']))

def control(name,matrix,d,h,expected_branch):
    B = [tuple(dot(row,p) for row in matrix)+(0,) for p in BASE]
    out = audit_pyramid(name,B,(4*d,0,h))
    assert (out['base_stable'],out['apex_unstable']) == expected_branch
    return out

controls = [
    control('right_all_base_norms_tied',[[1,0],[0,1]],0,4,(True,True)),
    control('outside_base_apex_unstable',[[1,0],[0,1]],3,1,(False,True)),
    control('outside_base_apex_not_unstable',[[3,0],[9,1]],1,1,(False,False)),
    control('boundary_base_foot',[[3,0],[6,1]],1,1,(False,False))]
report = dict(theorem=THEOREM,parent_journal_sha256=PARENT,
    anchor='2026-09-08T03:39:03.372Z',identities=identities,
    root_orbits=[dict(representative=list(a),members=sorted(o)) for a,o in sorted(root_orbits.items())],
    controls=controls,scope='Universal argument is in the handoff; controls are not an exhaustion.')
raw = (json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
Path('raven24_pyramid_exact_audit.json').write_bytes(raw)
print('REPORT',len(raw),hashlib.sha256(raw).hexdigest())
src = Path(__file__).read_bytes()
print('SOURCE',len(src),hashlib.sha256(src).hexdigest())
print('RAVEN24_PYRAMID_ALGEBRA_AND_PHYSICAL_AUDIT_PASS')
```

## 8. Scope and continuation

**Entire resolved family:** every full-dimensional homogeneous convex pyramid, hence the complete C32 octagonal wheel. The proof actually covers any polygon with the reflection property (4) and the quarter-height reference (1); its actual polar stays in that larger balanced-reference class.

**Not resolved by this result:** the other C32 combinatorial types, general nonpyramidal nine-vertex/nine-facet bodies, and any new global minimum. Roofs, bipyramids, prismatoids, or genuine apex-replacement bodies are outside the theorem unless they are actually pyramids. The accepted global bracket remains unchanged by this exclusion alone.

The useful continuation is to remove the wheel and every pure-pyramid search from the live joint-monostatic frontier, retain the other C32 graphs, and reuse the exact witness extractor as a regression test for purported pyramid attainments. A pure-base deformation, tilt, height change, or physical affine deformation cannot evade the theorem while preserving a homogeneous pyramid.

The theorem is a new deduction relative to the supplied journal, with its full proof and exact arithmetic replay supplied here. External peer review, proof-assistant formalization and historical novelty determination have not been performed; no priority claim is made. No homogeneous strict110 construction or mesh is claimed.

Supplementary copies: [complete source](sandbox:/mnt/data/raven24_pyramid_check.py), [complete exact audit](sandbox:/mnt/data/raven24_pyramid_exact_audit.json), [this self-contained handoff](sandbox:/mnt/data/raven24_all_pyramids_handoff.md). The inline proof and source are the recovery authority, not these links.
