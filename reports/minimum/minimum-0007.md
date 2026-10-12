# minimum-0007

AI research report · 2026-09-07 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NOVA24_RANK3_AND_PROJECTION_MASS_V1

## Determination

**Rank three is not the missing obstruction.** The literal nine-point planar control from `NOVA24_V9_DISTINCT_TRIPLE_V1` admits an exact rational three-dimensional lift with all nine points extreme, all eight prescribed escape arrows on genuine edges, exactly one unstable vertex at the unchanged origin, and strict three-dimensional, apex-excluded distinct-triple containment at every vertex. Even strictly positive weights on all 56 triples per apex are feasible. Thus nine is sharp for that relaxation even after requiring a full-dimensional convex hull and actual escape edges.

**Actual homogeneous volume nevertheless excludes every lift of that exact planar control—and an open neighborhood of its projected coordinates.** I prove a universal projection/chord-concavity inequality and certify these consequences in the original Euclidean coordinates:

1. Any full-dimensional convex body whose orthogonal projection is the parent's exact nine-gon has ordinary volume centroid satisfying `g_x+g_y > 8275/1270748 > 1/160`.
2. Allow each of the eighteen projected coordinates to vary independently by at most `1/100`, and allow all nine heights to be arbitrary real numbers. Every positive-volume convex hull in this entire domain satisfies `g_x+g_y > 7/6625 > 1/1000`. No height bound, fixed graph, simpliciality assumption, prescribed escape assignment, or positive equilibrium-margin cutoff is used in this exclusion.

The new lifted control is not homogeneous mono-unstable: its exact reference census is `(S,U,H)=(2,1,1)`, whereas its own-centroid census is `(2,9,9)`. Moreover, its actual boundary incidence already rules out zero moment with arbitrary nonnegative root-cone weights. Consequently it establishes the insufficiency of rank, convexity, genuine escape edges, and unrestricted triple identities; it does **not** establish that true-volume coupling remains indispensable after imposing every actual-facet/apex constraint.

**The universal homogeneous lower bound remains V≥9, not V≥10.** The inherited joint bracket remains `30≤C_min≤1374`, and the first joint boundary `V9,E15,F8` is not closed here. The new auxiliary hull has `V9,E21,F14`, not the joint boundary. The V≥9 theorem and its stated boundary are inherited from the literal parent; the facet-side F≥8 implication is its separate, correctly centered polar-inclusion result. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## 1. Source authority and exact parent preservation

I read all three named immutable parent payloads through their ends. Their identities are:


[Encoded source block omitted; the code in this passage is incomplete.]


All three declared hashes were reproduced from their serialized version-2 JSON envelopes. No conflicting geometric identity was found. I also extracted and replayed the literal NOVA24 recovery source: 19,433 bytes, SHA-256 `4c15c82965977605609acbbce07ec9322d1f9491792f34c5a2c1310f992171fe`. Its 595 shifted positive-definite matrices and complete 5,040-tree/115-orbit coverage passed, reproducing its 5,705-byte table hash `34f501da2c4cabec97a55ca8311381a78eee0603c9c46c7c375a3f3dbf859af6`. The parent supplies those certificates and the complete replay program. :contentReference[oaicite:2]{index=2}

Most importantly, the new standalone recovery program regenerates the exact **627-byte** original planar-control JSON, with SHA-256

```text
fc768d2c1916da5e3fc91b521b2a74720bb5c99dfa1b078e944ceeb39359b73b
```

before checking any successor. Its original two coordinates, labels, root, parent array, reference origin, sum polygon, and per-apex guards are unchanged. The parent states that control and its rank-two limitation explicitly. :contentReference[oaicite:3]{index=3}

## 2. Exact full-dimensional sharpness control

### 2.1 Literal coordinates and complete boundary

Use the ordinary Euclidean metric and reference `o=(0,0,0)`. Divide each integer row below by `D=1000`:

```text
label       x       y     z
0        1000       0     3
1         517     499     2
2         151     591     1
3        -153     496    -6
4        -331     295    -9
5        -376      79     8
6        -344     -71    -7
7        -256    -189     0
8         445    -496     2
parents = [-1,0,1,2,3,4,5,6,0]
```

Exhausting all supporting triples gives the following complete outward maximal-facet list, in the numbering used by the recovery code:

```text
F0  (0,3,1)    F1  (0,1,5)    F2  (0,4,3)    F3  (0,6,4)
F4  (0,5,8)    F5  (0,8,6)    F6  (1,3,2)    F7  (1,2,5)
F8  (2,3,5)    F9  (3,4,5)    F10 (4,6,5)    F11 (5,6,7)
F12 (5,7,8)    F13 (6,8,7)
```

The complete true-edge list is:

```text
(0,1) (0,3) (0,4) (0,5) (0,6) (0,8)
(1,2) (1,3) (1,5) (2,3) (2,5)
(3,4) (3,5) (4,5) (4,6)
(5,6) (5,7) (5,8) (6,7) (6,8) (7,8)
```

All fourteen supporting planes have positive support constants at the origin and exactly their three displayed contacts. All other supporting inequalities are strict. The minimum raw integer nonincidence guard is `221401`; this is an unnormalized determinant guard, not a Euclidean distance. Every edge has exactly two opposite oriented uses. A rank certificate is

`det(I1−I0,I2−I0,I3−I0)=−832543≠0`.

For the eight parent arrows, the integer guards `I_i·(I_parent−I_i)` are

```text
[712,895,566,350,8,253,226,961].
```

Thus the smallest physical escape is `1/125000>0`, and every arrow is a true edge. Vertex 0 has strictly negative outgoing derivative toward every other vertex. These checks establish a genuine origin-interior three-polytope with reference-relative U1, not free vectors masquerading as a boundary.

### 2.2 Strict distinct-triple containment at all nine apices

For each apex a, the recovery capsule lists four triples excluding a. Their four vector sums are affinely independent and have strictly positive barycentric coefficients expressing `−v_a`. This proves interior containment in three dimensions, not relative interior in a plane.

For example, at apex 0 the four triples are

```text
(1,5,6), (4,5,6), (4,6,7), (5,6,7),
```

with corresponding coefficients

```text
336/1522333,
2141851/6089332,
299021/6089332,
911779/1522333.
```

They are positive, sum to one, and their weighted triple sum is exactly `−v0`. The complete four-triple specifications for all nine apices are literal inputs in the code below; their exact coefficients are regenerated by four-by-four rational elimination.

A stronger finite check puts weight `1/10^12` on each of the other 52 triples for each apex and resolves the four selected coefficients to correct both total weight and all three coordinates. Every resulting one of the 56 weights is strictly positive. The code verifies all nine identities exactly.

These are **independently chosen apex-specific weights on unrestricted triples**. They are not asserted to be boundary triangles, a common affine incidence family, or actual solid-volume weights. The actual homogeneous cone identity requires actual facets and their actual tetrahedral volumes; that distinction is the parent's premise as well. :contentReference[oaicite:4]{index=4}

### 2.3 Actual volume and full equilibrium audit

Direct determinant integration gives

```text
Vol(K) = 17243627/3000000000,
g(K) = (14155590489,12368382246,60508997)/137949016000.
```

Numerically, the centroid is approximately `(0.1026146535833,0.0896590827875,0.0004386330454)`, decisively different from the mechanical reference. The verifier independently recomputes this same centroid by positive-volume reconing from **each of the nine actual vertices**.

The exact feature censuses, with no degenerate equilibrium detected, are:

```text
At o=0:
S = [F3,F4]
U = [0]
H = [(7,8)]

At the actual ordinary-volume centroid:
S = [F1,F3]
U = [0,1,2,3,4,5,6,7,8]
H = [(0,1),(0,8),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8)]
```

Every true edge is tested using its endpoint projection parameters and both incident-normal coefficients. No triangulation diagonal is counted as an edge.

### 2.4 A continuous rank-three family approaching the exact parent

Replace every third coordinate by `t z_i`, where `0<t≤1`. Convexity, the complete face lattice, origin-interiority, and the strict triple containments are preserved by the invertible map `diag(1,1,t)`.

I do **not** invoke affine invariance of equilibrium. Instead, each prescribed escape and each root support guard is affine in `t²`, and is strictly positive at both algebraic endpoints `t=0` and `t=1`; the former is checked against the unchanged planar parent. Therefore every member has reference-relative U1 in the same Euclidean metric.

The actual centroid is `(g_x,g_y,t g_z)`. All own-centroid vertex support guards are also affine in `t²`. Their t=1 values are positive in the complete audit. Their minimum at the algebraic endpoint t=0, in raw integer-coordinate units, is

`45650166095/34487254>0`.

Consequently **every** member with `0<t≤1` has U9 at its own volume centroid. At t=0 this is only an endpoint check of the polynomial guards; no three-dimensional volume centroid is attributed to the collapsed planar body.

This supplies arbitrarily thin, genuinely rank-three, genuine-hull controls converging to the literal parent's nine points. No positive thickness requirement alone can repair the distinct-triple relaxation.

## 3. The realized boundary already blocks arbitrary root-cone weights

For the particular lifted hull, take `n=(1,1,40)`. The eight actual facets not containing vertex 0 give, in their displayed order,

```text
1000 n·(v0 + sum of the three facet vertices)
    = [3101,3021,2028,850,52,3,727,9].
```

All are strictly positive. Hence no convex combination of the **actual** root-cone tetrahedral vertex sums can vanish—even when their weights are allowed to be arbitrary nonnegative numbers. The minimum physical separator guard is `3/1000`.

In contrast, the free root triple `(4,6,7)` has

`n·(v0+v4+v6+v7)=−416/1000`,

and its coefficient in the strict root containment is `299021/6089332>0`. It is not an actual facet. This precisely identifies the incidence loophole used by the free-triple control. For the t-family the separator is `(1,1,40/t)`, and all eight guards remain unchanged.

This is a complete exclusion of arbitrary actual-root-facet weights for this entire scaled family. It is **not** an exclusion of every realization of its graph, and it does not claim feasibility of the stronger common-affine-incidence relaxation.

## 4. A universal actual-volume projection obstruction

The following theorem is independent of the nine-point fixture and applies to every candidate. It uses vertical chord lengths of the **same uniformly filled solid**, not invented masses.

### 4.1 Sandwich lemma for concave chord lengths

Let K be a compact full-dimensional convex body, P′ its orthogonal projection onto a Euclidean plane, and `f(x)` the length of its fiber perpendicular to that plane. Convexity implies that f is nonnegative and concave. Put `H=max f>0`. Fubini gives

`Vol(K)=∫_(P′) f(x) dx`,

`Vol(K) ℓ(g)=∫_(P′) ℓ(x)f(x) dx`

for every linear functional ℓ in the projection plane.

Choose inner and outer polygons `R⊆P′⊆Q`. Let `s_j(x)≥0` be the inward affine facet slacks of R, let `d_j=max_(y∈Q) s_j(y)>0`, and define

`τ(x)=min_j s_j(x)/d_j`, for x∈R.

**Claim:** `f(x)≥H τ(x)` on R.

Choose p∈P′ with f(p)=H. For x in the interior of R with x≠p, extend the ray from p through x to its last intersection r with R. Then `x=λp+(1−λ)r`, with `0<λ<1`. A facet slack vanishes at r, so `s_j(x)=λs_j(p)≤λd_j`. Therefore `τ(x)≤λ`; concavity and f(r)≥0 give `f(x)≥λH≥τ(x)H`. This argument also works when p lies outside R. For x=p the bound follows from τ≤1; on the boundary τ=0 and it is trivial.

For integer N≥1, define

`R_k={x∈R : ℓ(x)≥0 and N s_j(x)≥k d_j for every j}`, `k=1,…,N`.

Since τ is at least its lower N-step approximation, set

`B_N = ∫_(Q∩{ℓ<0}) ℓ(x) dx + (1/N) Σ_(k=1)^N ∫_(R_k) ℓ(x) dx`.

On the positive side use the chord lower bound; on the negative side use f≤H. Enlarging the latter integration domain from P′ to Q only decreases its negative integral. Thus

`Vol(K) ℓ(g) ≥ H B_N`.

If B_N>0, then `Vol(K)≤H area(Q)` yields

**`ℓ(g)≥B_N/area(Q)>0`.**

Accordingly, a homogeneous centroid-zero candidate must have **B_N≤0 for every such projection, sandwich, functional, and N**. This is a universal structural restriction carrying actual volume information through concavity of the chord-length function.

### 4.2 Exact evaluation for the parent's projection

Let P be the convex hull of the nine literal parent XY points divided by 1000, in their displayed cyclic order. Take `R=Q=P`, `ℓ(x,y)=x+y`, and `N=16`.

For consecutive raw vertices u,v, use

```text
a = u_y−v_y,
b = v_x−u_x,
c = u_x v_y−u_y v_x,
s(x,y) = a x+b y+c,
d = max over the nine raw vertices of s.
```

All clipping and integration are rational. The raw area is `953061`, and the exact raw negative first moment is

`−84923241104143/2389974`.

Physical area is obtained by division by `1000²`, and these raw first moments by `1000³`. The nonempty positive layers k=1,…,7 have respectively `[7,8,8,9,7,7,5]` vertices; layers 8 through 16 are empty. Their physical integrals of ℓ are strictly greater than the respective entries of

```text
[2539,1769,1165,705,364,133,14]/10000.
```

The physical negative-moment magnitude is strictly less than `356/10000`. These exact comparisons yield

`B_16 > 6689/160000 − 356/10000 = 993/160000`.

Therefore every positive-volume convex body with this projection satisfies

**`g_x+g_y > (993/160000)/(953061/1000000) = 8275/1270748 > 1/160`.**

This excludes **all real height assignments**, not merely a finite scan or a fixed upper/lower triangulation. It also excludes convex bodies with additional vertices or nonpolyhedral boundaries if the same projection is retained.

### 4.3 Robust exclusion of an open projected-coordinate domain

The same polygon strictly contains `[-1/5,1/5]²`; the recovery code checks every facet against that square. Let q_i have any third coordinates and satisfy

`|q_ix−I_ix/1000|≤1/100`, `|q_iy−I_iy/1000|≤1/100`.

For `P′=conv{(q_ix,q_iy)}`, the support functions obey

`|h_(P′)(u)−h_P(u)|≤(1/100)||u||_1≤(1/20)h_P(u)`.

Hence

`(19/20)P⊆P′⊆(21/20)P`.

Apply the sandwich lemma with `δ=1/20`, `R=(1−δ)P`, `Q=(1+δ)P`, and `N=256`. In raw coordinates, each original slack `(a,b,c,d)` becomes

```text
inner slack:      a x+b y+(1−δ)c,
maximum on outer: (1+δ)d−2δc.
```

The complete rational clipping computation certifies, in physical units,

```text
positive 256-step integral  > 2113/50000,
negative outer magnitude   < 2057/50000,
outer area                 < 53/50.
```

Consequently

**`g_x+g_y > [(2113−2057)/50000]/(53/50) = 7/6625 > 1/1000`.**

The exact unsimplified certified bound is about `0.001073976225966125`; `7/6625` is a simpler conservative lower bound. These are not optimized constants.

The exclusion covers the entire closed eighteen-coordinate XY box times **all nine real heights**, whenever the hull has positive three-dimensional volume. It permits inactive input points, arbitrary changes of face lattice, nonsimplicial facets, nonsimple vertices, and arbitrarily small positive thickness. No failed optimization status is involved. A zero-volume limit is not a homogeneous three-dimensional solid and is not being assigned a volume centroid by this statement. More generally, the proof excludes every full-dimensional convex body whose projection satisfies the displayed sandwich.

## 5. Remaining frontier and interpretation

The strongest positive finding is a complete rank-three sharpness control, and the strongest negative finding is an actual-volume exclusion uniform over arbitrary heights and a nonzero projected-coordinate neighborhood. They address different relaxations and must not be conflated.

The exploration first sought small integer lifts of the exact parent and then tested increasingly physical moment conditions. Small-height searches and linear-programming experiments were used only to locate and diagnose the explicit control. Their successes or failures are not premises: the single exact recovery unit below reconstructs and verifies every new claimed numerical or algebraic object. The height-search question was replaced by the stronger written chord-concavity theorem, which does not enumerate heights or rely on a numerical solver.

The global nine-vertex problem remains open here. In particular, I have not proved infeasibility for every nine-vertex graph, every escape tree, or every projected shape outside the certified domain. I have not shown that the all-actual-apex facet-containment relaxation is feasible at nine, nor that a common affine incidence family can support U1 there. These are the next distinctions that need exact controls or exclusions.

For a volume-complete continuation, the inherited common operator `LTL+L=4J` plus genuine-edge cross-slack balances is a valid route; the balances, rather than arbitrary triangle weights, restore actual cone volumes. Its compatible Gram coupling keeps all mechanical tests in one physical metric. :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6} The new projection theorem offers an alternative necessary condition that can be tested before those larger systems: use endogenous projection planes and linear directions, and certify B_N>0 over coordinate boxes. Merely adding rank constraints or tuning heights over the inherited nine-gon, even with the stated independent XY perturbations, is now rigorously closed.

No new homogeneous upper witness, V≥10 theorem, F≥9 theorem, minimum-complexity determination, or publication-priority claim is made.

## 6. Complete recovery capsule

Save the source below verbatim as `nova24_rank3_projection_recover.py`, UTF-8 with LF line endings and one final LF. It is **13,543 bytes**, SHA-256

```text
1c56d8ae03ce0c8175e15e3ac3bc89f7eeb0e39478469090e8b230c45856335b
```

Executed environment: **CPython 3.13.5, standard library only**. There is no numerical solver, external graph catalogue, parent file, or downloaded fixture dependency. All non-default choices are literal: D=1000, the nine height numerators, the parent array, all nine four-triple simplex specifications, other-triple weight `1/10^12`, fixed-projection N=16, robust sandwich δ=1/20 and N=256.

Run with assertions enabled in a writable directory:

```sh
python -S nova24_rank3_projection_recover.py
```

The program writes `nova24_rank3_projection_report.json`: **39,187 bytes**, SHA-256

```text
78bc9d0a3bc8f759161b3d8223ec2db7b30bebf85a1f5d96ee038b7ec04e61d9
```

The report contains the complete coordinates, incidence, all edge lists and censuses, exact volume and centroid, all simplex coefficients, the complete positive-weight reconstruction parameters, and every exact layer integral in both projection certificates. Every layer integral is checked two ways: polygon first-moment summation and independent fan-triangle integration. Actual volume is additionally checked by all nine apex decompositions. A clean-directory replay produced a byte-identical report.

Observed terminal output:

```text
PARENT_627_BYTE_CONTROL_IDENTITY_PASS
RANK3_ACTUAL_HULL_TRUE_EDGE_ESCAPE_PASS 9 21 14
ALL_9_APICES_STRICT_RANK3_DISTINCT_TRIPLE_AND_POSITIVE_WEIGHTS_PASS
ACTUAL_ALL_APEX_VOLUME_RECONING_AND_ROOT_FACE_SEPARATOR_PASS
ALL_0_LT_T_LE_1_REFERENCE_U1_OWN_U9_VERTICAL_FAMILY_PASS
EXACT_REFERENCE_CENSUS 2 1 1
EXACT_OWN_CENTROID_CENSUS 2 9 9
ALL_CONVEX_BODIES_WITH_PARENT_PROJECTION_GX_PLUS_GY_GT_1_OVER_160_PASS
ALL_XY_PERTURBATIONS_LE_1_OVER_100_ARBITRARY_HEIGHTS_GAP_GT_1_OVER_1000_PASS
REPORT_BYTES_SHA256 39187 78bc9d0a3bc8f759161b3d8223ec2db7b30bebf85a1f5d96ee038b7ec04e61d9
NOVA24_RANK3_AND_PROJECTION_MASS_RECOVERY_PASS
```

The source performs exact reconstruction and arithmetic certification. The universal quantifiers in the height and coordinate-box exclusions are justified by the written sandwich lemma, not by interpreting a finite calculation as a continuous-domain search.

```python
"""NOVA24_RANK3_AND_PROJECTION_MASS_V1. CPython 3.13.5, stdlib only.
Run with assertions: python -S nova24_rank3_projection_recover.py
All coordinates, simplex witnesses and integration parameters are literal.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json

assert __debug__
PARENT = 'minimum-0006'
PARENT_SHA = '4480a792dec44a82e252175c8263360cd2cac11c705c881fe30da85b47087f08'
CONTROL_SHA = 'fc768d2c1916da5e3fc91b521b2a74720bb5c99dfa1b078e944ceeb39359b73b'
D = 1000
I = [(1000,0,3),(517,499,2),(151,591,1),(-153,496,-6),
     (-331,295,-9),(-376,79,8),(-344,-71,-7),(-256,-189,0),(445,-496,2)]
p = [-1,0,1,2,3,4,5,6,0]
SIMPLEX = [
 [(1,5,6),(4,5,6),(4,6,7),(5,6,7)],
 [(0,5,7),(5,6,7),(5,7,8),(6,7,8)],
 [(0,5,7),(5,6,7),(5,7,8),(6,7,8)],
 [(0,5,7),(0,7,8),(5,7,8),(6,7,8)],
 [(0,5,7),(0,7,8),(5,7,8),(6,7,8)],
 [(0,4,6),(0,6,7),(0,6,8),(6,7,8)],
 [(0,1,7),(0,4,5),(0,4,7),(0,5,7)],
 [(0,4,5),(0,4,6),(0,5,6),(4,5,6)],
 [(0,4,5),(2,4,5),(4,5,6),(4,5,7)]]

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def triple(t): return tuple(sum(I[i][k] for i in t) for k in range(3))
def encode(obj):
    return (json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
def solve(A,b):
    n=len(b); B=[[F(x) for x in row]+[F(y)] for row,y in zip(A,b)]
    for k in range(n):
        j=next(j for j in range(k,n) if B[j][k])
        B[k],B[j]=B[j],B[k]
        q=B[k][k];B[k]=[x/q for x in B[k]]
        for i in range(n):
            if i!=k:
                q=B[i][k];B[i]=[x-q*y for x,y in zip(B[i],B[k])]
    return [row[-1] for row in B]
def turn(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull2(points):
    P=sorted(set(points));L=[];H=[]
    for v in P:
        while len(L)>1 and turn(L[-2],L[-1],v)<=0: L.pop()
        L.append(v)
    for v in reversed(P):
        while len(H)>1 and turn(H[-2],H[-1],v)<=0: H.pop()
        H.append(v)
    return L[:-1]+H[:-1]

# Reproduce the exact original parent control, not an aliased substitute.
XY=[v[:2] for v in I];H=hull2(XY)
SP=hull2([tuple(sum(XY[i][k] for i in t) for k in range(2))
          for t in combinations(range(9),3)])
escape0=[dot(XY[i],sub(XY[p[i]],XY[i])) for i in range(1,9)]
global_guard=min(turn(SP[j],SP[(j+1)%len(SP)],(-v[0],-v[1]))
                 for j in range(len(SP)) for v in XY)
apex_guards=[]
for a in range(9):
    ss=hull2([tuple(sum(XY[i][k] for i in t) for k in range(2))
              for t in combinations([i for i in range(9) if i!=a],3)])
    apex_guards.append(min(turn(ss[j],ss[(j+1)%len(ss)],(-XY[a][0],-XY[a][1]))
                           for j in range(len(ss))))
control={'D':D,'integer_points_2d':XY,'parents':p,'rank':2,'polygon':H,
         'distinct_triple_polygon':SP,'minimum_escape':str(F(min(escape0),D*D)),
         'minimum_global_integer_guard':global_guard,'per_apex_integer_guards':apex_guards,
         'scope':'Rank-two relaxation only: no three-dimensional solid volume.'}
raw=encode(control)
assert len(raw)==627 and hashlib.sha256(raw).hexdigest()==CONTROL_SHA
print('PARENT_627_BYTE_CONTROL_IDENTITY_PASS')

# Complete supporting-triple reconstruction of the lifted hull.
faces=[];planes=[];inactive=[]
for a,b,c in combinations(range(9),3):
    n=cross(sub(I[b],I[a]),sub(I[c],I[a]))
    if n==(0,0,0): continue
    h=dot(n,I[a]);slack=[h-dot(n,v) for v in I]
    if max(slack)<=0:
        b,c=c,b;n=tuple(-x for x in n);h=-h;slack=[-x for x in slack]
    if min(slack)<0: continue
    assert h>0 and sum(s==0 for s in slack)==3
    faces.append((a,b,c));planes.append((n,h))
    inactive += [s for s in slack if s]
assert set(i for f in faces for i in f)==set(range(9))

def edge_map(fs):
    E={}
    for f,cyc in enumerate(fs):
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):
            E.setdefault(tuple(sorted((a,b))),[]).append((f,a,b))
    assert all(len(v)==2 and v[0][1:]==v[1][1:][::-1] for v in E.values())
    return E
E=edge_map(faces)
assert (len(I),len(E),len(faces))==(9,21,14)
assert all(tuple(sorted((i,p[i]))) in E for i in range(1,9))
assert det(sub(I[1],I[0]),sub(I[2],I[0]),sub(I[3],I[0]))!=0
escape1=[dot(I[i],sub(I[p[i]],I[i])) for i in range(1,9)]
assert escape1==[712,895,566,350,8,253,226,961]
assert min(escape0)>0 and min(escape1)>0
assert all(dot(I[0],sub(I[0],v))>0 for v in I[1:])
assert all(dot(XY[0],sub(XY[0],v))>0 for v in XY[1:])
print('RANK3_ACTUAL_HULL_TRUE_EDGE_ESCAPE_PASS 9 21 14')

# Nine full-dimensional containing tetrahedra in the apex-excluded sum sets.
# Also produce strictly positive weights on ALL 56 distinct triples per apex.
eps=F(1,10**12);sum_cert=[]
for a,ts in enumerate(SIMPLEX):
    assert len(set(ts))==4 and all(len(set(t))==3 and a not in t for t in ts)
    Y=[triple(t) for t in ts]
    A=[[1]*4]+[[v[k] for v in Y] for k in range(3)]
    b=[F(1)]+[-F(x) for x in I[a]]
    lam=solve(A,b)
    assert min(lam)>0
    assert all(sum(A[k][j]*lam[j] for j in range(4))==b[k] for k in range(4))
    all_t=list(combinations([i for i in range(9) if i!=a],3))
    other=[t for t in all_t if t not in ts]
    bb=[b[0]-len(other)*eps]+[b[k+1]-eps*sum(triple(t)[k] for t in other)
                              for k in range(3)]
    ll=solve(A,bb);weights={t:eps for t in other};weights.update(zip(ts,ll))
    assert len(weights)==56 and min(weights.values())>0
    assert sum(weights.values())==1
    assert all(I[a][k]+sum(w*triple(t)[k] for t,w in weights.items())==0 for k in range(3))
    sum_cert.append({'apex':a,'four_triples':ts,'barycentric':list(map(str,lam)),
                     'all56_adjusted_four':list(map(str,ll))})
print('ALL_9_APICES_STRICT_RANK3_DISTINCT_TRIPLE_AND_POSITIVE_WEIGHTS_PASS')

# Actual homogeneous moments, with independent reconing from every vertex.
W=0;M=[0,0,0]
for a,b,c in faces:
    z=det(I[a],I[b],I[c]);assert z>0;W+=z
    for k in range(3): M[k]+=z*(I[a][k]+I[b][k]+I[c][k])
g=tuple(F(x,4*W) for x in M)
assert W==34487254 and M==[14155590489,12368382246,60508997]
for r in range(9):
    w=0;m=[0,0,0]
    for f in faces:
        if r in f: continue
        a,b,c=[I[i] for i in f]
        z=det(sub(a,I[r]),sub(b,I[r]),sub(c,I[r]));assert z>0;w+=z
        for k in range(3):m[k]+=z*(I[r][k]+a[k]+b[k]+c[k])
    assert w==W and tuple(F(x,4*w) for x in m)==g
# Real boundary triangles already rule out zero at the root apex.
separator=(1,1,40)
root_guard=[dot(separator,tuple(I[0][k]+triple(f)[k] for k in range(3)))
            for f in faces if 0 not in f]
assert root_guard==[3101,3021,2028,850,52,3,727,9]
print('ACTUAL_ALL_APEX_VOLUME_RECONING_AND_ROOT_FACE_SEPARATOR_PASS')

def census(center):
    Z=[sub(v,center) for v in I]
    pp=[(n,h-dot(n,center)) for n,h in planes]
    assert all(h>0 for n,h in pp)
    out={'S':[],'U':[],'H':[],'degenerate':[]}
    for f,(n,h) in enumerate(pp):
        foot=tuple(F(h*x,dot(n,n)) for x in n)
        guards=[k-dot(m,foot) for j,(m,k) in enumerate(pp) if j!=f]
        if min(guards)>0:out['S'].append(f)
        elif min(guards)==0:out['degenerate'].append(('F',f))
    for i,a in enumerate(Z):
        q=min(dot(a,sub(a,b)) for j,b in enumerate(Z) if i!=j)
        if q>0:out['U'].append(i)
        elif q==0:out['degenerate'].append(('V',i))
    for (i,j),uses in sorted(E.items()):
        a,b=Z[i],Z[j];e=sub(b,a);L=dot(e,e);T=-dot(a,e)
        z=tuple(L*a[k]+T*e[k] for k in range(3))
        n,m=[pp[u[0]][0] for u in uses];nn,mm,nm=dot(n,n),dot(m,m),dot(n,m)
        assert nn*mm-nm*nm>0
        v1=tuple(mm*n[k]-nm*m[k] for k in range(3))
        v2=tuple(nn*m[k]-nm*n[k] for k in range(3))
        q=min(T,L-T,dot(z,v1),dot(z,v2))
        if q>0:out['H'].append((i,j))
        elif q==0:out['degenerate'].append(('E',i,j))
    assert not out['degenerate'] and len(out['S'])+len(out['U'])-len(out['H'])==2
    return out
ref=census((0,0,0));own=census(g)
assert ref['U']==[0] and own['U']==list(range(9))
Z=[sub(v,g) for v in I]
own_xy_guard=min(dot(Z[i][:2],sub(Z[i][:2],Z[j][:2]))
                 for i in range(9) for j in range(9) if i!=j)
assert own_xy_guard==F(45650166095,34487254)>0
print('ALL_0_LT_T_LE_1_REFERENCE_U1_OWN_U9_VERTICAL_FAMILY_PASS')
print('EXACT_REFERENCE_CENSUS',*[len(ref[k]) for k in ('S','U','H')])
print('EXACT_OWN_CENTROID_CENSUS',*[len(own[k]) for k in ('S','U','H')])

# Universal projection-mass certificate, not a finite height search.
# Physical XY coordinates are the following raw polygon divided by D.
Q=[tuple(F(x) for x in v) for v in XY]
def clip(poly,a,b,c):
    if not poly:return []
    out=[]
    for u,v in zip(poly,poly[1:]+poly[:1]):
        su=a*u[0]+b*u[1]+c;sv=a*v[0]+b*v[1]+c
        if su>=0:out.append(u)
        if (su<0<sv) or (sv<0<su):
            out.append(tuple((su*v[k]-sv*u[k])/(su-sv) for k in range(2)))
    ans=[]
    for x in out:
        if not ans or x!=ans[-1]:ans.append(x)
    if len(ans)>1 and ans[0]==ans[-1]:ans.pop()
    return ans

def integrate(poly):
    if len(poly)<3:return F(0),F(0)
    area=F(0);moment=F(0)
    for u,v in zip(poly,poly[1:]+poly[:1]):
        d=u[0]*v[1]-u[1]*v[0]
        area+=d;moment+=d*(sum(u)+sum(v))
    assert area>=0
    # Independent fan-triangle integration of the same affine function.
    aa=F(0);mm=F(0);u=poly[0]
    for v,w in zip(poly[1:-1],poly[2:]):
        d=turn(u,v,w);assert d>=0
        aa+=d/2;mm+=d*(sum(u)+sum(v)+sum(w))/6
    assert aa==area/2 and mm==moment/6
    return aa,mm

slacks=[]
for u,v in zip(Q,Q[1:]+Q[:1]):
    a=u[1]-v[1];b=v[0]-u[0];c=u[0]*v[1]-u[1]*v[0]
    dd=[a*x+b*y+c for x,y in Q]
    assert min(dd)==0 and max(dd)>0
    slacks.append((a,b,c,max(dd)))
area,_=integrate(Q);_,negative=integrate(clip(Q,-1,-1,0))
assert area==953061 and negative==F(-84923241104143,2389974)
N=16;total=F(0);layers=[]
for k in range(1,N+1):
    R=clip(Q,1,1,0)
    for a,b,c,d in slacks:R=clip(R,N*a,N*b,N*c-k*d)
    aa,mm=integrate(R);assert aa>=0 and mm>=0
    total+=mm
    layers.append({'k':k,'vertices':len(R),'area':str(aa),'moment':str(mm)})
gap=negative+total/N
bound=gap/(D*area)
assert [r['vertices'] for r in layers]==[7,8,8,9,7,7,5]+[0]*9
low=[2539,1769,1165,705,364,133,14]
assert all(F(layers[k]['moment'])>F(low[k],10000)*D**3 for k in range(7))
assert -negative<F(356,10000)*D**3
assert sum(low)==6689 and F(6689,160000)-F(356,10000)==F(993,160000)
simple_bound=F(993,160000)/(area/D**2)
assert bound>simple_bound==F(8275,1270748)>F(1,160)
print('ALL_CONVEX_BODIES_WITH_PARENT_PROJECTION_GX_PLUS_GY_GT_1_OVER_160_PASS')

# Open XY-box exclusion: every coordinate can change by 1/100 physically.
# The projection lies between (19/20)Q and (21/20)Q; heights are arbitrary.
assert all(c>F(D,5)*(abs(a)+abs(b)) for a,b,c,d in slacks)
delta=F(1,20);NN=256
inner=[tuple((1-delta)*x for x in v) for v in Q]
outer=[tuple((1+delta)*x for x in v) for v in Q]
ss=[(a,b,(1-delta)*c,(1+delta)*d-2*delta*c) for a,b,c,d in slacks]
outer_area,_=integrate(outer)
_,outer_negative=integrate(clip(outer,-1,-1,0))
box_total=F(0);box_layers=[]
for k in range(1,NN+1):
    R=clip(inner,1,1,0)
    for a,b,c,d in ss:R=clip(R,NN*a,NN*b,NN*c-k*d)
    aa,mm=integrate(R);assert aa>=0 and mm>=0
    box_total+=mm
    box_layers.append({'k':k,'vertices':len(R),'area':str(aa),'moment':str(mm)})
box_positive=box_total/NN
assert box_positive>F(2113,50000)*D**3
assert -outer_negative<F(2057,50000)*D**3
assert outer_area<F(53,50)*D**2
assert (F(2113,50000)-F(2057,50000))/F(53,50)==F(7,6625)>F(1,1000)
box_bound=(box_positive+outer_negative)/(D*outer_area)
assert box_bound>F(7,6625)
print('ALL_XY_PERTURBATIONS_LE_1_OVER_100_ARBITRARY_HEIGHTS_GAP_GT_1_OVER_1000_PASS')

report={'identity':'NOVA24_RANK3_AND_PROJECTION_MASS_V1',
        'parent':PARENT,'parent_sha256':PARENT_SHA,'parent_control_sha256':CONTROL_SHA,
        'D':D,'integer_lift':I,'escape_parents':p,'facets':faces,'edges':sorted(E),
        'minimum_inactive_integer_guard':min(inactive),
        'integer_escape_guards':escape1,'minimum_physical_escape':str(F(min(escape1),D*D)),
        'volume':str(F(W,6*D**3)),'centroid':list(map(str,(x/D for x in g))),
        'reference_census':ref,'own_centroid_census':own,
        'simplex_certificates':sum_cert,'all56_other_weight':str(eps),
        'root_actual_face_separator':separator,'root_actual_face_integer_guards':root_guard,
        'projection_area_raw':str(area),'projection_negative_moment_raw':str(negative),
        'projection_layers':layers,'projection_gap_raw':str(gap),
        'projection_centroid_linear_bound':str(bound),
        'projection_simple_lower_bound':str(simple_bound),
        'own_xy_minimum_integer_guard':str(own_xy_guard),
        'projection_box':{'XY_radius':'1/100','sandwich_delta':str(delta),'N':NN,
                          'outer_area_raw':str(outer_area),
                          'outer_negative_moment_raw':str(outer_negative),
                          'positive_lower_moment_raw':str(box_positive),
                          'centroid_bound':str(box_bound),'simple_bound':'7/6625',
                          'layers':box_layers},
        'scope':'Rank3 actual reference-U1 hull, not homogeneous U1; universal fixed-projection mass exclusion.'}
raw=encode(report)
Path('nova24_rank3_projection_report.json').write_bytes(raw)
print('REPORT_BYTES_SHA256',len(raw),hashlib.sha256(raw).hexdigest())
print('NOVA24_RANK3_AND_PROJECTION_MASS_RECOVERY_PASS')
```

Supplemental convenience copies: [complete runnable recovery source](sandbox:/mnt/data/nova24_next/nova24_rank3_projection_recover.py) and [exact generated report](sandbox:/mnt/data/nova24_next/nova24_rank3_projection_report.json). The literal source above, not these links, is the durable reconstruction authority.
