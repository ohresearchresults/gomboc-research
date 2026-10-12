# minimum-0156

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# NEGATIVE_ANCHOR_SIMPLICIAL_ESCAPE_V1

## Result and exact scope

**A genuine third or fourth negative anchor cannot occur at an all-positive-endpoint joint maximum whose unprotected maximal facets are all triangles.** Root and coordinate polygons, arbitrary positive-support auxiliary vertices, and redundant canonical marks are allowed. In particular, root-only assumptions and the unsupported assertion that every free facet meets A or B are unnecessary.

More precisely, let `P` be a bounded full-dimensional convex polytope in the full marked-body/support-function class, and suppose it is a joint Hausdorff local maximum of the original uniformly filled trace. Assume

```
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
T0=conv(A,B,C,D) subset P subset {x>=0,y>=0,ell>=0},
ell=a+(d-a)x+(c-a)y+(b-a)z,
a>b>0, c>0, d>0,
F=P intersect {ell=0} has positive area.
```

Call only the maximal facets in `x=0`, `y=0`, and `ell=0` protected. If every other **maximal facet**, not every integration triangle, is triangular, then

```
G(C)>0 and G(D)>0.
```

Consequently, a joint maximum in the requested complement `G(C)<0 or G(D)<0` must have a **genuine nonsimplicial unprotected facet**. By the accepted one-canonical rigidity theorem and the fact that AB already belongs to both coordinate facets, such a polygon contains at least two canonical marks and necessarily involves C or D. This is an actual-body restriction on the remaining reaction geometry, not an exclusion of arbitrary moment data.

The proof also gives an actual improving-variation alternative for the entire excluded class: an auxiliary shave, a canonical re-marking followed by affine normalization, a single supporting-plane variation, or a particular outward D-stretch (with the symmetric C-stretch when the labels are exchanged). The final stretch is essential: its body-shape contribution has zero first derivative, but its **actual canonical-mark contribution is strictly positive**.

**Not proved:** the whole negative-anchor complement has trace below `51/25`. The surviving nonsimplicial reaction strata remain open. No `T>=51/25` body is constructed, no global finite-ascent termination is claimed, and the accepted complexity interval remains `34<=C_min<=622`.

## Input closure and evidence level

All four supplied files were read through EOF. Their actual UTF-8 identities are:

- Stationarity/rigidity proof: 14,798 bytes, SHA-256 `8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9`.
- Root-duality/joint-variation proof: 18,784 bytes, SHA-256 `73eb04d63deeab693d29533819d3b95c4e1af3cc01d756987381aaa2bb4c2ed8`.
- Root-fan/Berwald proof and discovery source: 20,592 bytes, SHA-256 `b1d05ed4c84512cf48852d5383ffcc3ff2a066c1b7f6b5777fe62d372c0cb559`.
- Entire supplied journal, including common and branch memory: 250,531 bytes, SHA-256 `4b2b9b995ab78262a74f323aebb3516076ac03357db29bdfa15730865d6aabbe`. This is the whole-file hash, not the embedded common-memory hash.

The later attainment and <=16-vertex localization are retained as the accepted notebook status; the older source's historical lack-of-attainment statement is not treated as current. The full localization proof and the separate old audit sources `[internal-source-reference]` and `[internal-source-reference]` are not attached and were not replayed. None is an exact computational dependency of the new result. The theorem below is conditional on a genuine polyhedral joint maximum and does not need to reconstruct localization.

Evidence levels: the new structural result is an analytic proof given below, using the supplied accepted variation lemmas; the new numerical object is an exactly integrated rational body with an exactly verified improving competitor. The executable verifies its stated algebra and actual-body arithmetic, not the entire geometric proof in a proof assistant.

## 1. Start with the actual joint problem

Write

```
s=a+b, alpha=a-b>0,
n=(s+c)x+(s+d)y,
V=int_P 1, E=int_P ell, N=int_P n,
g=(u,v,z)=V^(-1) int_P (x,y,z),
r=N/V, q=N/E, T=N/(6VE),
G=n-r-q ell.
```

All these integrals use the same uniformly filled body. In particular

```
G(g)=-r,
G(A)=-r-qa<0,
G(B)=-r-qb<0,
G(B)-G(A)=q alpha>0,
partial_z G=q alpha>0.
```

The supplied fixed-support local-maximum theorem gives `G(v)>0` at every auxiliary true vertex and `P intersect {x=y=0}=AB`. It also gives the whole-facet inequality and one-canonical triangle rigidity. These statements allow arbitrary face-lattice changes and are not fixed-realization-stratum conditions.

The exact comparison underlying the shaves is

```
T(P')>T(P)
iff Delta int G > N Delta V Delta E/(VE).
```

Thus a sufficiently small cap at a negative-G auxiliary vertex improves the trace. At a zero-G auxiliary vertex the supplied thin-edge cap gives a strictly negative limiting average of G and also improves it; ordinary homothetic shaving alone is not substituted for that strictness argument.

Root stationarity is legitimate here precisely because **all four endpoint values are positive**. With `t=6V`, `p=u+v`, `m=3p/t`, `w=(v/(3p),u/(3p),1/3)`, and `k=|grad ell|`, the actual identity is

```
int_F G h/k = 6V^2 [T h(g)-m h(w)]
```

for every affine h. The corresponding G-weighted root centroid is the actual point `R_T` in the relative interior of F. The proof below does not replace this root by independent weights or an auxiliary fan. It uses the actual positive-area root and the fact that no canonical mark lies on it. No two-sided root assertion is made at a zero-endpoint boundary.

## 2. Canonical re-marking gives a useful geometric lemma

### 2.1 Exact C and D mark derivatives

Hold the physical body and physical ell fixed. Choose a new C-mark `C'=(0,y',z')` in its x=0 face and use the affine normalization

```
(x,y,z) -> (x,y/y',z-z'y/y').
```

Its normalized trace, expressed in the old physical integrals `X=int_P x` and `Y=int_P y`, is

```
T_C' = [y'(s+ell(C'))X+(s+d)Y]/(6VE).
```

For `C_epsilon=C+epsilon(0,dy,dz)`, the numerator derivative is

```
X[(b+2c)dy-alpha dz].
```

Therefore a joint maximum satisfies, on the **entire actual coordinate face**,

```
L_C(y,z):=(b+2c)(y-1)-alpha z <= 0.             (C-mark)
```

Similarly, on y=0,

```
L_D(x,z):=(b+2d)(x-1)-alpha z <= 0.             (D-mark)
```

These are actual mark variations, including the affine-volume normalization. They agree with the supplied canonical support tests.

### 2.2 Negative C forces the lower coordinate edge AC

Assume `G(C)<=0`. If an auxiliary vertex `v=(0,y,z)` of the x=0 face had `z<0`, then:

- For `0<=y<=1`, affinity gives `G(v)=(1-y)G(A)+yG(C)+q alpha z<0`, contradicting auxiliary positivity.
- For `y>1`, `L_C(v)>0`, contradicting the genuine C-mark variation.

Hence the entire x=0 face lies in `z>=0`. On its line z=0, the C-mark inequality gives `y<=1`. Because A and C are retained, its intersection with z=0 is **exactly AC**. Thus C is a true vertex and AC is a true edge. Symmetrically, `G(D)<=0` forces D to be a true vertex and AD to be a true edge.

This also gives a direct improving-variation dichotomy, without assuming stationarity in advance: a lower-coordinate protrusion at a nonpositive-G canonical corner yields either a negative-G auxiliary shave or an explicitly improving re-marking.

### 2.3 Redundant opposite marks must not be silently treated as vertices

If D is not a true vertex, it cannot belong to an unprotected facet containing A or B. Indeed, that facet's intersection with y=0 is a true edge containing D and A or B. D lies in the edge's relative interior. Since `L_D<=0` and `L_D(D)=0`, L_D must vanish on this edge. But

```
L_D(A)=-(b+2d)<0,  L_D(B)=-(a+2d)<0,
```

a contradiction. The symmetric assertion holds for a redundant C.

This lemma will be used explicitly below. A triangle containing C and a redundant D is still a **two-mark reaction facet**, not an ordinary one-mark triangle.

## 3. The exact triangular reactions

For an unprotected triangular facet `H=[U,V,W]`, let lambda_Z be the affine barycentric function of one of its true vertices. If lambda_Z vanishes at **every canonical mark in H**, varying just the supporting plane by this affine normal displacement is feasible with both parameter signs. Consequently

```
int_H G lambda_Z = Area(H)[G(U)+G(V)+G(W)+G(Z)]/12 = 0.   (R)
```

This is the actual triangle area moment. It applies to a whole true facet, never to an arbitrarily selected triangle inside a polygonal facet.

Two cases will be used repeatedly:

```
One canonical vertex X, auxiliaries v,w:
  G(v)=G(w)=-G(X)/3.

Two canonical vertices X,Y, auxiliary v, no other marks:
  G(v)=-(G(X)+G(Y))/2.                           (Pair)
```

In particular, an ordinary X triangle cannot meet an XY triangle along Xv when `G(Y)<=0`: simultaneous stationarity would force `G(Y)=G(v)>0`.

The other reaction used later is just as important. If a two-mark triangle `[C,D,v]` has

```
G(C)=-3L, G(D)=G(v)=L>0,
```

then `int_H G lambda_D=0`. D is a **zero-work canonical reaction** on that triangle. This does not mean D is absent from the marked problem: moving D still changes the trace numerator through its actual mark.

## 4. Proof of the simplicial escape theorem

Assume all unprotected maximal facets are triangles and, for a contradiction, `G(C)<=0`. Set `g_X=G(X)` and, when `g_C<0`, `L=-g_C/3`.

By Section 2, AC is a true edge. Its noncoordinate facet is either `[A,C,D]` or `[A,C,v]` with an auxiliary true vertex v. It cannot be ABC, since that is the coordinate plane. A redundant D on this facet is excluded by Section 2.3.

### 4.1 First handle a genuinely redundant D

Suppose D is not a true vertex. Then the other AC facet is `[A,C,v]`. Since it contains A and C but not D, the pair reaction gives

```
g_v=-(g_A+g_C)/2 > -g_C/3 >= 0.                 (4.1)
```

The strict inequality uses `g_A<0` and `g_C<=0`.

The supporting plane through AC is `z=eta x`, with P on `z>=eta x`. Containment of B fixes this orientation; containment of D gives `eta<=0`. Here `eta<0`, since otherwise the facet would also contain D. Because `v_x>0`, it follows that `v_z<0`.

The other facet on Cv is not protected. It cannot be an ordinary C triangle by (4.1), and it cannot be BCv because its pair reaction would imply `g_A=g_B`. Therefore it must contain the redundant mark D. As it is a true triangle, it has the form `[C,v,w]`, with D in the relative interior of the auxiliary edge vw in y=0.

This is the genuine two-mark triangle exception; no ordinary-C moment equation is imposed on it.

The D-mark support vanishes on the whole edge vw, so

```
z=(b+2d)(x-1)/alpha   on vw.
```

Since `v_z<0` and D is strictly between v and w, `v_x<1<w_x`. Along this line, direct differentiation gives

```
dG/dx = (s+c)+q(s+d)>0.
```

Thus `g_w>g_v>-g_C/3`.

Consider the other facet on Cw. It cannot contain A, since AC already has its two incident facets; it cannot contain D, since C,w,D determine the already used plane Cvw. It is not protected. An ordinary C triangle would require `g_w=-g_C/3`, which has just been excluded. Hence it is BCw.

Now the actual coordinate faces are ABC and the quadrilateral ABwv, with D a redundant point on vw. Together with ACv, Cvw and BCw these form a closed facet-adjacency component: every edge of each listed face already has both incident facets listed. The facet-adjacency graph of a convex three-polytope is connected, so these are all the facets. The only auxiliary vertices are v,w; a root disjoint from all canonical marks cannot then have positive area. Contradiction.

**Therefore D must be a true vertex.**

### 4.2 A triangular AC facet forces the actual base facet ACD

Suppose the other AC facet were `[A,C,v]` rather than ACD. Again `v_x>0`, `v_z<0` and (4.1) holds.

The other facet on Cv must be CDv: an ordinary C triangle contradicts (4.1), BCv would force `g_A=g_B`, and protected facets are impossible on Cv. Comparing the two pair reactions gives

```
g_D=g_A<0.
```

Hence AD is also a true edge by Section 2.2.

The other facet on Av cannot now be coordinate: at A the two coordinate faces already have their boundary neighbors B,C and B,D. It cannot contain B, because AB already belongs to both coordinate facets. An ordinary A triangle would force `g_C=-g_A/3>0`. Consequently the other facet is ADv, and its pair reaction gives `g_C=g_D`.

We have obtained

```
g_A=g_C=g_D<0.
```

Because these three marks span z=0, affinity implies

```
G(x,y,z)=g_A+(g_B-g_A)z = g_A+q alpha z.
```

But `v_z<0`, so `g_v<g_A<0`, contradicting auxiliary positivity.

Thus the other AC facet is **the true triangular facet ACD**, and `P subset {z>=0}`. This is not an assumption that ACD is present; it is forced by the full triangular fan and the mark geometry.

### 4.3 Exhaust the fan across CD without discarding the three-mark facet

The other facet on CD cannot be BCD: together with ACD and the coordinate halfspaces it would imply `P=T0`, with no positive-area root. Therefore it is `[C,D,v]`, with v auxiliary and `v_z>0`. Its pair reaction is

```
g_v=-(g_C+g_D)/2>0.                             (4.2)
```

On Dv the other facet is either the coordinate face y=0 or BDv. An ordinary D triangle would give `g_C=-g_D/3=g_v>0`, contrary to `g_C<=0`; ADv is impossible because AD already has its two incident facets.

On Cv the other facet is either x=0, BCv, or an ordinary C triangle. These cases are exhaustive: ACD has already fixed the AC adjacency, and C is not on the root.

If the other Cv facet is coordinate or BCv, the polytope closes on only five vertices. More explicitly, the coordinate faces are respectively triangles ABC, ABD or one of the quadrilaterals ABvC, ABvD. Together with ACD, CDv and the required BCv/BDv triangles, every listed edge has both incident facets accounted for. The facet-adjacency graph is again closed and connected. There is only one auxiliary vertex v, so an all-positive-endpoint root of positive area is impossible.

The only remaining case is that the other Cv facet is ordinary. Then

```
g_C=-3L,  g_v=L,  g_D=L>0.                     (4.3)
```

The actual D-star consists of the coordinate face y=0, the three-mark facet ACD, the triangle CDv, and possibly BDv. Indeed, the edges AD, CD, Dv and, when present, BD already have both incident facets among these, closing the vertex link. If BDv occurs, its pair reaction also gives `g_B=g_C=-3L`.

### 4.4 The genuine improving D-stretch

Set

```
D_epsilon=(1+epsilon,0,0),  epsilon>0,
P_epsilon=conv(P,D_epsilon),
```

keeping the physical support function ell fixed for the moment and marking D_epsilon instead of D. The old D lies on AD_epsilon, so this is a genuine convex enlargement. For sufficiently small epsilon, only CDv and, when present, BDv are visible. The coordinate face y=0 and the three-mark facet ACD stay in their original planes.

By (4.3), the shape derivative on CDv vanishes:

```
int_CDv G lambda_D = Area(CDv)(-3L+L+L+L)/12 = 0.
```

The same holds on BDv when present. The two fixed planes have zero normal displacement. Therefore the entire body-shape contribution to the first variation is zero.

Now perform the required affine normalization `x -> x/(1+epsilon)`. In the pre-normalization physical coordinates, the exact marked numerator is

```
(s+c) X_epsilon
 +(1+epsilon)[s+ell(D_epsilon)] Y_epsilon.
```

Since `ell(D_epsilon)=d+(d-a)epsilon`, its explicit mark derivative at zero is

```
Y[(s+d)+(d-a)] = Y(b+2d)>0.
```

Thus

```
(d/d epsilon) T_marked(P_epsilon) at 0
   = Y(b+2d)/(6VE) > 0.                          (Escape)
```

This is the contradiction. The all-positive endpoints persist for small epsilon. The physical root polygon is retained, and affine normalization preserves its positive area and uniform filling. The argument neither rotates ACD freely through three fixed marks nor discards its reaction: the chosen displacement is tangent to its actual plane.

This completes the C case. Exchanging x with y and C with D proves the D case. The zero case `G(C)=0` cannot reach (4.3), because it would require an auxiliary vertex with G=0, and is already excluded by the preceding alternatives. Hence the theorem gives strict positivity at both C and D.

## 5. What the restriction does and does not eliminate

The genuine negative-anchor complement is now localized to **unprotected polygonal reaction facets**. Nonsimpliciality confined to the root or coordinate patches cannot support it at a joint maximum. This covers arbitrary positive-ell auxiliary vertices and includes the possibility that the opposite canonical mark was initially redundant.

The necessary marked incidence types of a surviving polygon are the five two-mark types `AC, AD, BC, BD, CD` or the two three-mark types `ACD, BCD`. This is a list of necessary reaction types, not a classification of their continuous realizations or a count of independent extrema. No assumption that arbitrary CD facets lie on opposite sides of CD is used.

A two-mark quadrilateral remains a real surviving possibility. A nonsimplicial facet containing three canonical marks remains another. One may not triangulate either polygon, enforce (R) on each integration triangle, and call that a supporting-plane variation. The entire polygon has coupled reactions and only its genuinely admissible plane motions are available. This proof does not independently establish that every surviving two-mark polygon has exactly four vertices. The supplied sources already identify these exceptions; the new conclusion is that the negative-anchor sector **requires** an unprotected nonsimplicial exception rather than merely allowing one.

This is not yet a trace-value theorem on those survivors. In particular, an improving step can leave the simplicial-boundary class while retaining `G(C)<0`; the exact control below does exactly that. There is no deduction that all negative-anchor bodies can be monotonically reduced to `G(C),G(D)>=0`, and no claim that the two-anchor value problem is already closed. The notebook explicitly leaves both value frontiers open.

## 6. Exactly reconstructed actual-body control

The following new rational body is not a moment completion and is not root-only. Use

```
(a,b,c,d)=(1,1/4,1/5,1/1000),
ell=1-(999/1000)x-(4/5)y-(3/4)z,
R(x,y)=(x,y,(4/3)[1-(999/1000)x-(4/5)y]),
e=1/1000, rho=17/20, R_outer=103/100,
U=(11/20,11/20,11/15000),  ell(U)=1/100,
P9=conv(A,B,C,D,
        R(e,rho-e), R(rho-e,e),
        R(R_outer-e,e), R(e,R_outer-e), U).
```

All nine displayed points are true vertices. Its actual f-vector is `(9,20,13)`, with one quadrilateral root and all unprotected facets triangular. Every auxiliary true vertex has G>0, including the positive-ell vertex U, while `G(C)<0<G(D)`.

Exact uniform integrals are

```
V = 53786611/225000000,
E = 20600153897/300000000000,
N = 27891076736297/150000000000000,
T = 2091830755222275000/1108012464198073067
  = 1.8879126569539477... .
```

This is a nonwinning control, not an extremum or a `51/25` counterexample. No equilibrium census is claimed.

A genuine free facet is `[A,C,v]` with

```
v=(1029/1000,1/1000,-28771/750000),
H_old=28771*x+771750*z >= 0.
```

In the normalization `H=z-(v_z/v_x)x`, take `h=x/v_x` and replace H by `H-(1/10000)h`. Equivalently replace just the old primitive halfspace by

```
H_new=14348*x+385875*z >= 0,
```

keeping every other actual facet inequality unchanged. The exact reaction residual is

```
G(A)+G(C)+2G(v)
 = -29405582398763755715649/13850155802475913337500 < 0.
```

The resulting actual halfspace intersection has f-vector `(12,23,13)` and

```
T_child=
28672284310023053839188384410111808630005159943269472813219882851751000000/
15186550721478176139105831823171747896350266027166339417702105635927649453
=1.888005040504171... .
```

The exact gain is positive, approximately `0.0000923835502234477`. The new hull has unprotected polygons, so the control also demonstrates why this ascent is not automatically a reduction confined to a simplicial fan.

The audit independently rebuilds all supporting facets from triples, retains only true vertices, integrates uniform moments using two distinct interior-apex fans, reconstructs the changed halfspace intersection, and checks that its hull facets are exactly the changed halfspaces. That last equality also verifies boundedness of the claimed intersection. It verifies the original support and all retained marks, positive root area, the strict trace gain, and the symbolic zero-work D reaction. It does not certify local optimality, mechanical equilibrium counts, or general polygonal-facet realizability.

## 7. Complete recovery capsule

There is no parent coordinate file or hidden checkpoint dependency. The exact parent is P9 defined above; all its inputs and the changed plane are embedded in the complete source below.

Runtime actually used: **CPython 3.13.5, SymPy 1.14.0**, assertions enabled. All other imports are from the standard library. There is no random seed, optimization stage, external input, or non-default solver parameter.

Save the code block as `negative_anchor_escape_audit.py`, UTF-8/LF, with its final newline. Run

```
python negative_anchor_escape_audit.py > negative_anchor_escape_audit.out
sha256sum negative_anchor_escape_audit.py negative_anchor_escape_audit.out
```

Expected source: **7,004 bytes**, SHA-256 `481b13aa47cd5c4247207b7813d58383d108ff59c639bc5decd521fa50c7b3e3`.

Expected complete stdout: **5,208 bytes**, SHA-256 `b40e1534ed0a562ffcfcef2de81ba3013e013808fccb93409cb6ca33d9b48c26`.

The source's canonical JSON input stream is **291 bytes**, SHA-256 `5bafa8a29297e2a45b61ae196f17db0ff0db27d05186661389a025bb159f22c7`.

Stdout consists of the complete exact JSON report followed by these markers:

```
NEGATIVE_ANCHOR_ACTUAL_AUXILIARY_CONTROL_PASS
ACTUAL_SINGLE_FACET_TILT_STRICTLY_IMPROVES_TRACE_PASS
PASSIVE_CANONICAL_D_REACTION_ALGEBRA_PASS
NEGATIVE_ANCHOR_SIMPLICIAL_ESCAPE_EXACT_CONTROL_PASS
```

Two executions, including a second run in a fresh directory containing only the source, completed and produced byte-identical stdout.

```python
"""Exact actual-body control for NEGATIVE_ANCHOR_SIMPLICIAL_ESCAPE_V1.
CPython 3.13.5, SymPy 1.14.0. No data files, optimization, or random input.
Run with assertions enabled: python negative_anchor_escape_audit.py
"""
from itertools import combinations
from math import gcd, lcm
import hashlib
import json
import sympy as S

Q = S.Rational
A, B, C, D = [S.Matrix(p) for p in
              ((0,0,0), (0,0,1), (0,1,0), (1,0,0))]
MARKS = (A, B, C, D)
a, b, c, d = S.S(1), Q(1,4), Q(1,5), Q(1,1000)
ALPHA = S.Matrix((d-a, c-a, b-a))

def ell(p):
    return a + ALPHA.dot(p)

def n(p):
    return (a+b+c)*p[0] + (a+b+d)*p[1]

def primitive(h):
    h = list(map(S.Rational, h))
    den = lcm(*(int(x.q) for x in h))
    nums = [int(x*den) for x in h]
    common = gcd(*nums)
    assert common > 0
    return tuple(x//common for x in nums)

def slack(h, p):
    return S.Matrix(h[:3]).dot(p) + h[3]

def hull(points):
    """Enumerate every supporting triple; retain only genuine vertices."""
    planes = set()
    for i,j,k in combinations(range(len(points)), 3):
        p,u,v = points[i],points[j],points[k]
        normal = (u-p).cross(v-p)
        if normal == S.zeros(3,1):
            continue
        h = list(normal) + [-normal.dot(p)]
        vals = [slack(h, x) for x in points]
        if min(vals) >= 0:
            pass
        elif max(vals) <= 0:
            h = [-x for x in h]
        else:
            continue
        planes.add(primitive(h))
    planes = sorted(planes)
    keep = []
    for p in points:
        active = [h[:3] for h in planes if slack(h,p) == 0]
        if len(active) >= 3 and S.Matrix(active).rank() == 3:
            keep.append(tuple(p))
    pts = [S.Matrix(p) for p in sorted(set(keep))]
    faces = [tuple(i for i,p in enumerate(pts) if slack(h,p) == 0)
             for h in planes]
    assert len(pts) >= 4 and all(len(f) >= 3 for f in faces)
    return pts, planes, faces

def edges_of(f, faces):
    edges = set()
    for other in faces:
        shared = set(f) & set(other)
        if other != f and len(shared) == 2:
            edges.add(tuple(sorted(shared)))
    assert len(edges) == len(f)
    assert all(sum(i in e for e in edges) == 2 for i in f)
    return sorted(edges)

def moments(pts, faces, origin):
    """Positive tetrahedra from one interior point and actual facet fans."""
    V = S.S(0)
    J = S.zeros(3,1)
    for f in faces:
        center = sum((pts[i] for i in f), S.zeros(3,1))/len(f)
        for i,j in edges_of(f,faces):
            p,q = pts[i],pts[j]
            vol = abs(S.det(S.Matrix.hstack(center-origin,
                                             p-origin,q-origin)))/6
            assert vol > 0
            V += vol
            J += vol*(origin+center+p+q)/4
    return V,J

def audit(points):
    pts,hs,fs = hull(points)
    for p in MARKS:
        assert all(slack(h,p) >= 0 for h in hs)
    assert all(p[0] >= 0 and p[1] >= 0 and ell(p) >= 0 for p in pts)
    o = sum(MARKS,S.zeros(3,1))/4
    V,J = moments(pts,fs,o)
    assert (V,J) == moments(pts,fs,S.Matrix([Q(1,5)]*3))
    E = a*V + ALPHA.dot(J)
    N = (a+b+c)*J[0] + (a+b+d)*J[1]
    assert V > 0 and E > 0 and N > 0
    r,q = N/V,N/E
    G = lambda p: n(p)-r-q*ell(p)
    assert G(J/V) == -r
    root = tuple(i for i,p in enumerate(pts) if ell(p) == 0)
    assert root in fs and len(root) >= 3
    edges = set(e for f in fs for e in edges_of(f,fs))
    assert len(pts)-len(edges)+len(fs) == 2
    out = dict(vertices=[[str(x) for x in p] for p in pts],
               planes=[list(h) for h in hs], faces=[list(f) for f in fs],
               f_vector=[len(pts),len(edges),len(fs)], V=str(V),
               J=[str(x) for x in J], centroid=[str(x/V) for x in J],
               E=str(E), N=str(N), r=str(r), q=str(q),
               T=str(N/(6*V*E)), G_marks=[str(G(p)) for p in MARKS])
    return pts,hs,fs,V,E,N,G,out

def intersect(hs):
    vertices = set()
    for ids in combinations(range(len(hs)),3):
        H = S.Matrix([hs[i][:3] for i in ids])
        if H.det() == 0:
            continue
        p = H.inv()*S.Matrix([-hs[i][3] for i in ids])
        if all(slack(h,p) >= 0 for h in hs):
            vertices.add(tuple(p))
    assert len(vertices) >= 4
    return [S.Matrix(v) for v in sorted(vertices)]

# All inputs are rational, including one genuine positive-ell auxiliary vertex.
e,rho,R = Q(1,1000),Q(17,20),Q(103,100)
xy = [(e,rho-e),(rho-e,e),(R-e,e),(e,R-e)]
roots = [S.Matrix((x,y,(a+(d-a)*x+(c-a)*y)/(a-b))) for x,y in xy]
x = y = Q(11,20)
aux = S.Matrix((x,y,(a+(d-a)*x+(c-a)*y-Q(1,100))/(a-b)))
points = list(MARKS) + roots + [aux]
input_bytes = (json.dumps(dict(endpoints=list(map(str,(a,b,c,d))),
                 points=[[str(x) for x in p] for p in points]),
                 sort_keys=True,separators=(',',':'))+'\n').encode()
pts,hs,fs,V,E,N,G,parent = audit(points)
assert len(pts) == 9 and all(any(p == v for v in pts) for p in points)
assert G(C) < 0 < G(D)
assert all(G(v) > 0 for v in roots+[aux])
assert ell(aux) == Q(1,100)
protected = {(1,0,0,0),(0,1,0,0),primitive(list(ALPHA)+[a])}
assert all(len(f) == 3 for h,f in zip(hs,fs) if h not in protected)
assert parent['f_vector'] == [9,20,13]
assert N/(6*V*E) == Q(2091830755222275000,1108012464198073067)

# Genuine one-plane tilt through AC, not independent simplex mass editing.
v = roots[2]
old = primitive([-v[2]/v[0],0,1,0])
assert old in hs
f = fs[hs.index(old)]
assert {tuple(pts[i]) for i in f} == {tuple(A),tuple(C),tuple(v)}
residual = G(A)+G(C)+2*G(v)
assert residual < 0
step = Q(1,10000)
# H=z-(v_z/v_x)x, h=x/v_x; use H-step*h >= 0.
new = primitive([(-v[2]-step)/v[0],0,1,0])
new_hs = list(hs)
new_hs[hs.index(old)] = new
child_vertices = intersect(new_hs)
cp,ch,cf,cV,cE,cN,cG,child = audit(child_vertices)
# This equality proves the intersection is bounded and is this exact hull.
assert set(ch) == set(new_hs)
gap = cN/(6*cV*cE)-N/(6*V*E)
assert gap > 0
first_derivative = -v[0]*residual/(144*V*E)
assert first_derivative > 0

# Symbolic checks for the passive-D reaction used in the analytic proof.
t,aa,bb,dd,L = S.symbols('t aa bb dd L')
mark_gain = (1+t)*(aa+bb+dd+(dd-aa)*t)-(aa+bb+dd)
assert S.diff(mark_gain,t).subs(t,0) == bb+2*dd
assert (-3*L+L+L)+L == 0  # 12*mean_F(G lambda_D)
report = dict(input_bytes=len(input_bytes),
              input_sha256=hashlib.sha256(input_bytes).hexdigest(),
              parent=parent, child=child,
              tilt=dict(old_plane=list(old),new_plane=list(new),
                        step=str(step),residual=str(residual),
                        first_derivative=str(first_derivative),
                        exact_trace_gain=str(gap)),
              status='ACTUAL_UNIFORM_BODY_CONTROL_NOT_A_JOINT_MAXIMUM')
print(json.dumps(report,sort_keys=True,separators=(',',':')))
print('NEGATIVE_ANCHOR_ACTUAL_AUXILIARY_CONTROL_PASS')
print('ACTUAL_SINGLE_FACET_TILT_STRICTLY_IMPROVES_TRACE_PASS')
print('PASSIVE_CANONICAL_D_REACTION_ALGEBRA_PASS')
print('NEGATIVE_ANCHOR_SIMPLICIAL_ESCAPE_EXACT_CONTROL_PASS')
```

Convenience copies, not recovery dependencies: complete source (`negative_anchor_escape_audit.py`) and exact report (`negative_anchor_escape_audit.out`).

## 8. Most useful continuation

The next finite-fan analysis should begin with a **genuine unprotected nonsimplicial reaction facet containing C or D**, not with a wholly triangular third-anchor fan. For a two-mark polygon H, keep the complete reaction identity

```
int_H G h = -gamma_C h(C)-gamma_X h(X)
```

for all affine h on H, with its actual area measure and nonnegative reaction coefficients. For a three-mark facet, retain all three reactions. The new proof identifies the precise missing cancellation: in the triangular case the required fan either closes before a root can exist or leaves a canonical D whose boundary reactions do no work against a strictly improving mark stretch. A polygon can transmit a nonzero D-work term and is exactly where that argument can fail.

A promising concrete next target is therefore a fan with one unprotected quadrilateral of type AC, AD, BC, BD or CD and otherwise triangular unprotected facets, with its true coupled area moments and the D-stretch first variation computed before any ordinary-level reduction. The polygon need not contain the negative mark itself: a reaction at the opposite D-star can block the escape. The alternative that this quadrilateral reaction supports an all-positive-endpoint `T>=51/25` extremum is unresolved; so is a general improving variation that removes it. No abstract covariance completion or auxiliary root polygon has been promoted to a uniform body.
