# minimum-0170

Historical AI scientific report · saved 2026-09-22 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# HORIZON_AWARE_FOUR_CORNER_ROOT_REDUCTION_V1

## Determination

The inverse-horizon obstruction can be removed by an actual geometric reduction on the **whole bounded positive-octant root-only class**, including `max(c,d)>=a`. The replacement needs at most **four original missing cones**, rather than the parent's three. Consequently every body in the assignment has an actual dominating successor with **at most eight root vertices and twelve total vertices**.

The successor preserves the root plane, all four endpoint values, root area, original volume `V`, original integral `E=integral ell`, the **entire original ell-marginal**, and the actual maximum of `x+y+z`. It does not decrease `N`, hence does not decrease `T=N/(6VE)`. More strongly, it does not decrease `integral n psi(ell)` for any bounded nonnegative measurable `psi`.

This is a whole-sector reduction, **not a proof of `T<51/25` on the resulting finite domain**. No endpoint-stationarity assumption is used. No actual counterexample to `T<51/25` was found or is asserted. The old three-corner value certificate cannot simply be evaluated at the new endpoint values.

## 1. Input authority and a byte-identity limitation

I read the supplied journal through all 1,775 lines, including the literal parent, and decoded and read the parent's complete 28,298-byte source through EOF. The starting theorem is the literal `minimum-0164`, declared SHA-256 `24b1e77ad400149d28a7ab046bbf9f750c5360fde51ae076aeab5565d3a18d84`. Its small-endpoint theorem and its explicit exclusion of the high-endpoint horizon case are the starting point, not conclusions extended by analogy. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

There is a serialization identity limitation: the scientific-parent suffix actually present in this journal, from its title through EOF, is 45,680 UTF-8 bytes with SHA-256 `39e2c5e55f64034039ae4d23545887b248ce6f898fe465a46115352107b57257`, whereas the journal describes a 46,500-byte immutable publication. I cannot authenticate that separate publication envelope from these bytes. I saw no truncation marker or incomplete code block and do not infer what any envelope difference contained. Crucially, the embedded source decodes and authenticates exactly to 28,298 bytes, SHA-256 `8c39f3c5fcc647d89794aa13a81c9c8f475ddedf323a56fb65c001f9e36f8cb9`, matching the parent's source pin. The parent certificate was not rerun. No mathematical conflict between its supplied proof and the journal summary was found.

The new proof below rederives the needed planar lemma and has no dependency on inaccessible older source IDs or an external theorem. The new computational capsule has no parent import.

## 2. The theorem and actual-body conventions

Normalize `a=1`; this scales both `ell` and `n` equally and leaves `T` unchanged. Put

```text
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
T0=conv(A,B,C,D),
0<b<1, c>0, d>0, alpha=1-b,
ell=1+(d-1)x+(c-1)y+(b-1)z,
n=(1+b+c)x+(1+b+d)y.
```

Let `F` be any compact convex positive-area subset of `{ell=0,x>0,y>0,z>=0}`, and let `P=conv(T0,F)`. Define all integrals with the original uniform volume measure:

```text
V=integral_P 1, J=integral_P (x,y,z),
E=integral_P ell, N=integral_P n, g=J/V,
H=max_F(x+y+z), T=N/(6VE).
```

**Theorem.** There is a convex polygon `F*` in the same root plane, with at most eight vertices, such that `P*=conv(T0,F*)` satisfies

```text
V*=V, E*=E, area(F*)=area(F), max_F*(x+y+z)=H,
integral_P* psi(ell)=integral_P psi(ell),
integral_P* n psi(ell)>=integral_P n psi(ell)
```

for every bounded nonnegative measurable `psi`. In particular `T(P*)>=T(P)`. Both coordinate support faces remain the genuine maximal triangles `ABC` and `ABD`. The actual centroid is always recomputed as `J*/V`; it is generally different from `g`.

The construction is rational and finite for rational polygonal input. The same geometric statement extends to marked closure with `x,y>=0`, but there the coordinate faces may be enlarged polygons: they must not be called genuine maximal triangles. The main theorem above does not use that weaker closure.

## 3. A finite containing quadrilateral across the horizon

Use the parent's projectivity only for sets:

```text
phi=(1-x-y-z)/2+d x+c y+b z,
(x',y',z')=(d x,c y,b z)/phi.
```

It fixes all four canonical points. It is positive on `T0` and on `F`, hence on `P`. On the root,

```text
x'+y'+z'=2,
L=-2+x'/d+y'/c+z'/b=1/phi>0,
(x,y,z)=(x'/(dL),y'/(cL),z'/(bL)).
```

Let `F'` be the image root and set

```text
xi=min_F' x'>0, eta=min_F' y'>0, zeta=min_F' z'>=0,
r=2-xi-eta-zeta>0,
R'={x'>=xi,y'>=eta,z'>=zeta,x'+y'+z'=2},
delta=min_F' L>0,
K'=R' intersect {L>=delta}.
```

Every side of `R'` contains a point of `F'`. Therefore **at most one vertex of `R'` can have `L<delta`**: two such vertices would have a common side entirely below `delta`, contradicting that side's root contact. It follows that `K'` is a triangle or quadrilateral, contains `F'`, and lies entirely in the positive inverse chart.

Writing

```text
Lbase=-2+xi/d+eta/c+zeta/b,
L_D=Lbase+r/d, L_C=Lbase+r/c, L_B=Lbase+r/b,
```

also shows that any corner on or beyond the inverse horizon is attached to the **unique largest** of `b,c,d`. A tied pair of horizon-bad corners is impossible. In the assigned high-endpoint sector that anchor is `C` or `D`, never `B`.

This gives the precise old applicability boundary: the uncut minima triangle has a finite positive inverse exactly when `min(L_B,L_C,L_D)>0`. Positivity merely on `F'` does not imply it. The parent explicitly identified this obstruction. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

### The new cut is an actual height cap, not an artificial density truncation

On the root,

```text
L=2/(x+y+z-1),
delta=2/(H-1).
```

Thus `L>=delta` is exactly the original condition `x+y+z<=H`. Let `K` be the inverse of `K'`. It is a genuinely bounded original root polygon, contained in the original octant simplex `{x,y,z>=0,x+y+z<=H}`.

Moreover, for any root point `p`, the only visible facet of `T0` is `BCD`, so

```text
6 Vol(conv(T0,p))=x(p)+y(p)+z(p).
```

Since a positive-area root has another point outside this five-point hull, `1<H<6V`. Consequently

```text
delta>2/(6V-1).
```

In conjunction with the previously accepted actual high-trace necessity `6V<45/7`, this gives `delta>7/19` for any `T>=51/25` candidate. That last numerical corollary uses the inherited volume cap; the reduction itself does not need it. :contentReference[oaicite:4]{index=4}

## 4. Why the difference is four actual cones

In root-plane `x',y'` coordinates, the canonical triangle at level `x'+y'+z'=1` is `Delta=conv((0,0),(1,0),(0,1))`. Its support vertices are respectively `B,D,C`.

For `0<=lambda<=1`, the sections of the two transformed bodies at level `1+lambda` are exactly

```text
(1-lambda)Delta+lambda K',
(1-lambda)Delta+lambda F'.
```

Below level one both bodies have the same canonical tetrahedral sections. This follows because every point of `K'/2` and `F'/2` lies in `Delta`; an `A`-to-root segment enters the upper region through the canonical triangle.

The three original side normals of `R'` are the three edge normals of `Delta`. The extra side normal `-grad L` lies in the normal cone of the uniquely clipped canonical corner. Thus each nonzero missing corner of `K'\F'` has its complete boundary-normal interval inside one canonical vertex normal cone. On that interval Minkowski addition translates the boundary chain by one fixed vertex `v_i` of `Delta`.

Choose the nearest root-side contact to each containing corner on its two adjacent sides. The allowed corner triangles have disjoint interiors, and their union contains `K'\F'`. Following each convex boundary chain in cyclic order gives, at every `lambda`, disjoint translated differences

```text
[(1-lambda)Delta+lambda K'] \ [(1-lambda)Delta+lambda F']
 = disjoint union_i ((1-lambda)v_i+lambda S_i'),
```

up to boundaries. Equivalently, before any integration,

```text
conv(T0,K) \ P = disjoint union_i cone(a_i,S_i),
```

where `S_i` is the original inverse missing region, `a_i` is `B`, `C`, or `D`, and there are at most four terms. For a clipped `C` corner the four anchors are, cyclically, `B,D,C,C`; reflection gives the `D` version. A cone over a nonconvex missing region means its union of segments from the anchor, not its convex hull.

This is the parent's translated-chain argument with one additional supporting normal inserted **inside a single canonical vertex cone**. No fifth anchor, signed mass, or projective refill is introduced. The parent's original three-cone argument and original density formulas are the relevant source, rather than its endpoint-specific polynomial certificate. :contentReference[oaicite:5]{index=5}

There is one important degeneration. If `delta` equals the second-smallest vertex value of `L`, an old side of `R'` can shrink to a point in `K'`. Its required root contact forces that merged corner itself to belong to `F'`. Its missing region is zero. Omit that term; the other nonzero corner normal cones still have single canonical anchors. Thus no uncovered equality wall is hidden in the quadrilateral description.

## 5. Original-area corner replacement

Here is the needed planar lemma, including its selection rule. It is the literal parent's elementary lemma, applied **after inversion in actual affine root coordinates**. :contentReference[oaicite:6]{index=6}

For a normalized missing corner

```text
S={(u,v):0<=u<=1,0<=v<=f(u)},
f>=0 convex and nonincreasing, f(1)=0, f(0)<=1,
m=integral f, X=integral u f, Y=(1/2)integral f^2,
```

one has

```text
2m^2/3<=X<=m/3,
X+Y<=(m+2m^2)/3,
XY>=2m^3/9.
```

For completeness, write `f` as a nonnegative mixture of hinges `(1-u/t)+`, adding an atom at zero to make total coefficient one. Then `2m=E t` and `6X=E t^2`, proving the first line. For `t<=s`, the hinge product integral is `I(t,s)=t/2-t^2/(6s)`, and

```text
(t^2+s^2)/2+3I(t,s)-(t+s)/2-ts
 =-(1-s)(s-t)^2/(2s)<=0.
```

Averaging proves the second line. For the third, set `A=3X/m`, `h=2m/A`, and `g(u)=h(1-u/A)+`. It has the same zeroth and first axial moments as `f`, and `integral gf>=integral g^2`. Expanding `integral(f-g)^2` yields `integral f^2>=integral g^2=4m^3/(9X)`, as required.

For an affine cost `q0+p u+q v`, if `q>=0`, use the missing triangle with intercepts

```text
A=3X/m, h=2m/A.
```

It preserves `m,X` and lowers `Y`. If `q<0`, choose the less costly of the two actual triangles with intercepts `(2m,1)` and `(1,2m)`. The first two inequalities show that a convex combination of their moment pairs matches `X` and has `Y` at least the original value, so at least one actual endpoint triangle has no larger cost.

For an allowed triangle with intercepts `A0,H0`, the same-axial-moment choice remains `(3X/m,2m/(3X/m))`; the two endpoint choices become `(2m/H0,H0)` and `(A0,2m/A0)`. Every chosen triangle remains inside its allowed triangle. Zero-area corners are simply retained.

Apply this to all nonzero original corners with cost `n`. The replacement triangles are disjoint, and intersecting their retained halfplanes with `K` gives one actual convex `F*`. All old side-contact marks survive. In particular all three projective minima and the new `L=delta` contact survive, proving preservation of `H`. At most two new root vertices occur per corner, hence at most eight in total. Root area remains positive because it is preserved exactly.

For curved roots, either use the same convex-function proof directly or approximate inside the fixed `K` by polygons retaining all side contacts. The intercepts remain in compact allowed intervals; a convergent subsequence preserves the moment identities, positive area and eight-vertex bound. This is not an assertion about an unbounded root or a zero-area root facet.

## 6. Original moments, weighted dominance and the finite continuation domain

Let `gell=|grad ell|`, `h_i=ell(a_i)`, `A_i=area(S_i)`, and `R_i=integral_Si r dA` in physical root-plane area. The actual removed cone has

```text
v_i=h_i A_i/(3 gell),
e_i=h_i v_i/4,
j_i=(v_i/4)a_i+(h_i/(4 gell))R_i,
n_i=(v_i/4)n(a_i)+(h_i/(4 gell))integral_Si n dA.
```

Its original ell-density is

```text
(A_i/gell)(1-w/h_i)^2, 0<=w<=h_i.
```

Each replacement preserves its own `A_i`, including the two separate regions having anchor `C`. Therefore the whole ell-law, not merely its first moments, is preserved. If

```text
Delta_i=integral_Si n dA-integral_Si* n dA>=0,
```

then the change in the body's original `n`-weighted ell-density is exactly

```text
sum_i (Delta_i/gell)(1-w/h_i)^3 1_[0,h_i](w)>=0.
```

This proves the theorem for all `psi` simultaneously. It also explains why the full vector `J` is not preserved.

### An explicit finite model for further value work

Use endpoint parameters `(b,c,d)`, minima `(xi,eta,zeta)` and `delta>0`. Form the triangle `R'` and `K'=R' intersect {L>=delta}`, retaining contact with every marked old side. Equivalently `delta` cannot exceed the second-smallest of the three vertex values of `L`. The generic four-corner stratum has strictly smaller minimum vertex value and strictly larger second vertex value than `delta`.

Invert the at most four vertices to original cyclic vertices `q_i`. With `e_i=q_(i+1)-q_i` and `f_i=q_(i-1)-q_i`, cut corner `i` at fractions `(u_i,v_i)`:

```text
0<=u_i,v_i<=1,
u_i+v_(i+1)<=1,
cut triangle=conv(q_i,q_i+u_i e_i,q_i+v_i f_i).
```

Retain positive root area. At a collapsed marked-side vertex the cut must be zero, as explained above. These are actual nonoverlapping corner cuts, not independently fitted moments. There are at most 15 scalar parameters in the generic model: seven container/endpoint parameters and eight fractions.

For rational evaluation, use root `xy` area. Let

```text
m_i=(u_i v_i/2) det_xy(e_i,f_i),
Rxy_i=m_i[q_i+(u_i e_i+v_i f_i)/3].
```

Here `Rxy_i` is the three-coordinate first integral with respect to root `dx dy`. Since `dA/gell=dx dy/alpha`, if `(V_K,E_K,J_K,N_K)` are the original moments of `conv(T0,K)`, then

```text
V*=V_K-sum_i h_i m_i/(3 alpha),
E*=E_K-sum_i h_i^2 m_i/(12 alpha),
J*=J_K-sum_i h_i[m_i a_i+3Rxy_i]/(12 alpha),
N*=N_K-sum_i h_i[m_i n(a_i)+3n(Rxy_i)]/(12 alpha).
```

Compute the container moments by any genuine outward boundary triangulation and a strict interior point `o`:

```text
v_tau=det(p-o,q-o,r-o)/6,
V_K=sum v_tau,
J_K=sum v_tau(o+p+q+r)/4,
E_K=V_K+(d-1)J_Kx+(c-1)J_Ky+(b-1)J_Kz,
N_K=(1+b+c)J_Kx+(1+b+d)J_Ky.
```

Thus the remaining value question is an exact rational actual-body problem. The finite model has no projective-density substitution and no unspecified centroid completion.

## 7. Exact actual controls and a failed shortcut

The compact source below preserves three input/successor pairs and their containers. All inputs have positive-area proper roots. It audits nine records, including one repeated container, with 792 nonzero true-edge primitives and no physical weak packet at the recomputed own centroid under the identity metric.

The simplest exact example has `(b,c,d)=(1/2,2,1/2)`, minima `(1/10,1/10,1/10)` and `delta=1/2`. The three minima-triangle values of `L` are `37/20,37/20,-7/10`: the old containing triangle genuinely crosses the horizon. The original finite container root, cyclically, is

```text
q0=(4/37,1/37,72/37),
q1=(72/37,1/37,4/37),
q2=(18/5,1,2/5),
q3=(2/5,1,18/5).
```

The input root is the hull of these twelve exact points, for `i=0,1,2,3`, `j=0,1,2`, with cyclic indices and `t=j/2`:

```text
q_i+((1-t)^2/5)(q_(i-1)-q_i)+(t^2/5)(q_(i+1)-q_i).
```

The four replacement fraction pairs, in this same corner order, are

```text
(3/20,2/15), (1/10,1/5), (1/5,1/10), (3/20,2/15).
```

Their anchors are `B,D,C,C`. Every original local missing corner has area `1/100`, first moments `(1/2000,1/2000)`, and allowed intercepts `(1/5,1/5)`.

The independently integrated actual data are

```text
V=3953837/1026750,
E=718607/342250,
root_xy_area=402624/171125,
H=5,
N_before=28348169311/1519590000,
N_after=5671112291/303918000,
Delta_N=154003/31658125>0,
T_before=26222056612675/68190118681416,
T_after =26228894345875/68190118681416.
```

The f-vectors `(V_vertices,E_edges,F_facets)` change from `(16,30,16)` to `(12,22,12)`. Both have strict `(S,U,H)=(4,4,6)`, weak zero, but this coincidence does not express a preservation theorem. Their actual centroids differ; both are recovered exactly by the code.

**Filling the horizon-safe container is not a valid dominance reduction.** On this same input,

```text
T(conv(T0,K))=43362067675/114084015576
             <T_before<T_after.
```

The values are approximately `0.380089`, `0.384543`, `0.384644`. This refutes plain container filling, not a proposed inequality with an additional `max(2,...)`, and is not a high-trace counterexample.

The other preserved pair on the same container generates the rounded corners in the projective image before inversion. Its true trace rises approximately `0.3918732895` to `0.3922085250`; its strict counts change `446 -> 457`. The asymmetric pair uses `(b,c,d)=(19/20,21/20,1/100)`, minima `(1/10000,1/100,1/100)`, `delta=1/20`, and image-generated corners. Its trace rises approximately `0.0723222315` to `0.0723670433`, with strict counts `255 -> 266`. Its actual radial height is 41. All exact coordinates, V/E/N/J, maximal facets and primitives for these nonwinning bodies are regenerated, not discarded.

## 8. Scope, failed approaches and the useful continuation

The useful repair is **clip in set geometry, then replace four corners using original affine area and original affine cost**. Applying the old three-corner formulas to a horizon-crossing triangle is invalid. Merely filling the clipped quadrilateral can lower trace, as the exact control shows. Replacing image-area corners instead of original-area corners would not preserve the original ell-law; no such refilling is used here.

There remains a genuine value problem on the finite model. The parent's substitutions `c=e/(1+e), d=f/(1+f)` and its nonnegative-parameter certificates do not cover `c>1` or `d>1`. An unsuccessful search for a simpler value inequality is not an exclusion theorem. No formal moment point or numerical optimization output is used as a body certificate.

The most useful continuation is an exact bound on the four-corner model, separating the repeated-highest-anchor pair from the two other anchors and exploiting the preserved actual radial height. The high-trace volume cap confines both the original root and its containing polygon to `x+y+z<45/7`, with inverse denominator `L>7/19`. Those are actual geometric constraints that should stay coupled to the corner fractions and moments.

The theorem requires positive endpoint values, `a>b`, bounded positive-area root, `z>=0`, and `P=conv(T0,F)`. Zero endpoints, `a=b`, negative-z visibility, unbounded roots and positive-ell auxiliary vertices are not covered by the new argument. Coordinate-facet mergers are distinguished from proper `ABC/ABD`. No unconstrained endpoint reaction, full marked stationarity, E17 incidence identification or mechanical exclusion is assumed. The shared bounds and registries remain unchanged. :contentReference[oaicite:7]{index=7}

## 9. Recovery, verification status and exact pins

Save the following complete source as `horizon_four_corner.py`, UTF-8 with LF and one final LF. It uses CPython 3.13.5 standard library only, assertions enabled, no external inputs, random seeds, tolerances, parent imports or third-party dependencies.

```text
python -S horizon_four_corner.py build horizon_four_corner.json
python -S horizon_four_corner.py check horizon_four_corner.json
```

Normal build/check and fresh-directory source-only build/check were completed. Reports and stdout matched byte-for-byte. The two distinct positive volume fans additionally agree on the actual first vector moment and ell moments through degree six; the infinite ell-law identity is proved analytically above, not inferred from those seven tests. Actual cone subtraction agrees independently with the hull integrations before and after every replacement. The hull checker reconstructs maximal facets before identifying true edges; integration diagonals are not mechanical edges.

```text
horizon_four_corner.py
  12102 bytes
  SHA256 aabb3a9ac7b13d01ccec7816e626d5e4f9408ea204040dcf1346a82864472bad
horizon_four_corner.json
  176068 bytes
  SHA256 c309fdc774596792f58660a7942c60c15c993d4a65e049485e7f08fdf95c501f
build/check stdout
  2128 bytes
  SHA256 a413fbfff1092aa0c6c36a61b88ca2ebf7b25ae8576a061ae957a213793e6b6d
terminal marker:
  HORIZON_FOUR_CORNER_ORIGINAL_DENSITY_EXACT_PASS
```

These are executed exact controls and an analytic geometric proof, not a proof-assistant formalization of the entire continuous theorem or a certificate of the remaining threshold inequality.

Convenience copies: [source](sandbox:/mnt/data/horizon_four_corner.py), [exact audit report](sandbox:/mnt/data/horizon_four_corner.json), [execution receipt](sandbox:/mnt/data/horizon_build.txt). The literal source below is sufficient without these links.

## Complete runnable source

```python
# HORIZON_AWARE_FOUR_CORNER_ROOT_REDUCTION_V1
# Exact parent: minimum-0164
# Declared parent SHA256: 24b1e77ad400149d28a7ab046bbf9f750c5360fde51ae076aeab5565d3a18d84
# Standalone CPython standard library. No parent imports, external inputs or RNG.
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib, json, sys
assert __debug__
A=(Q(0),Q(0),Q(0)); B=(Q(0),Q(0),Q(1)); C=(Q(0),Q(1),Q(0)); D=(Q(1),Q(0),Q(0))
CAN=[A,B,C,D]
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),Q(0))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def orient(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def chull(p):
    p=sorted(set(p))
    if len(p)<=1: return p
    def half(pp):
        r=[]
        for x in pp:
            while len(r)>1 and orient(r[-2],r[-1],x)<=0:r.pop()
            r.append(x)
        return r
    return half(p)[:-1]+half(p[::-1])[:-1]
def poly(p):
    ar=Q(0);j=[Q(0),Q(0)]
    if len(p)<3:return ar,tuple(j)
    for x,y in zip(p,p[1:]+p[:1]):
        d=x[0]*y[1]-x[1]*y[0];ar+=d/2
        for k in range(2):j[k]+=d*(x[k]+y[k])/6
    assert ar>=0
    return ar,tuple(j)
def clip(p,f):
    if not p:return []
    r=[]
    for x,y in zip(p,p[1:]+p[:1]):
        fx,fy=f(x),f(y)
        if fx>=0:r.append(x)
        if (fx<0<fy) or (fy<0<fx):r.append(add(x,mul(fx/(fx-fy),sub(y,x))))
    return chull(r)
def intersect(p,r):
    for a,b in zip(r,r[1:]+r[:1]):p=clip(p,lambda x,a=a,b=b:orient(a,b,x))
    return p

def simplex_ell(heights,degree=6):
    h=[Q(1)]+[Q(0)]*degree
    for a in heights:
        for k in range(1,degree+1):h[k]+=a*h[k-1]
    return [h[k]*Q(6,(k+1)*(k+2)*(k+3)) for k in range(degree+1)]

def body(root,b,c,d):
    p=CAN+[tuple(x) for x in root]
    assert len(p)==len(set(p))
    ell=lambda x:1+(d-1)*x[0]+(c-1)*x[1]+(b-1)*x[2]
    nn=lambda x:(1+b+c)*x[0]+(1+b+d)*x[1]
    assert all(min(x)>=0 and ell(x)>=0 for x in p)
    assert all(x[0]>0 and x[1]>0 and ell(x)==0 for x in root)
    ff={}
    for i,j,k in combinations(range(len(p)),3):
        n=cross(sub(p[j],p[i]),sub(p[k],p[i]))
        if not any(n):continue
        h=dot(n,p[i]);ss=[dot(n,x)-h for x in p]
        if min(ss)<0<max(ss):continue
        if max(ss)>0:n=mul(-1,n);h=-h;ss=[-x for x in ss]
        ids=[i for i,v in enumerate(ss) if v==0];drop=max(range(3),key=lambda j:abs(n[j]));axes=[j for j in range(3) if j!=drop]
        pp=[tuple(p[i][j] for j in axes) for i in ids];cy=[ids[pp.index(x)] for x in chull(pp)]
        if dot(cross(sub(p[cy[1]],p[cy[0]]),sub(p[cy[2]],p[cy[0]])),n)<0:cy.reverse()
        j=cy.index(min(cy));cy=tuple(cy[j:]+cy[:j]);ff[tuple(sorted(cy))]=(cy,n,h)
    faces=[ff[k] for k in sorted(ff)];edges={}
    vertices=sorted({i for cy,n,h in faces for i in cy})
    for fi,(cy,n,h) in enumerate(faces):
        for i,j in zip(cy,cy[1:]+cy[:1]):edges.setdefault(tuple(sorted((i,j))),[]).append(fi)
    assert all(len(fs)==2 for fs in edges.values()) and len(vertices)-len(edges)+len(faces)==2
    assert {i for i in vertices if p[i][0]==0}=={0,1,2}
    assert {i for i in vertices if p[i][1]==0}=={0,1,3}
    assert {i for i in vertices if ell(p[i])==0}==set(range(4,len(p)))
    # Two independent positive fans at different strict interior points.
    moments=[]
    for w in ([Q(1)]*len(p),[Q(i+1) for i in range(len(p))]):
        o=tuple(sum(a*x[j] for a,x in zip(w,p))/sum(w) for j in range(3));V=Q(0);J=(Q(0),)*3;M=[Q(0)]*7
        assert all(dot(n,o)<h for cy,n,h in faces)
        for cy,n,h in faces:
            for j in range(1,len(cy)-1):
                x,y,z=[p[i] for i in (cy[0],cy[j],cy[j+1])];v=det(sub(x,o),sub(y,o),sub(z,o))/6
                assert v>0;V+=v;J=add(J,mul(v/4,add(add(o,x),add(y,z))))
                me=simplex_ell([ell(q) for q in (o,x,y,z)])
                M=[a+v*b for a,b in zip(M,me)]
        moments.append((V,J,M))
    assert moments[0]==moments[1];V,J,M=moments[0];g=mul(1/V,J)
    E=V+(d-1)*J[0]+(c-1)*J[1]+(b-1)*J[2];N=nn(J);assert M[0]==V and M[1]==E
    poles=[mul(1/(h-dot(n,g)),n) for cy,n,h in faces];xx=[sub(x,g) for x in p]
    us={i:True for i in vertices};ss=[True]*len(faces);hs=[];weak=[];pack=[]
    for edge,fs in sorted(edges.items()):
        i,j=edge;f,h=fs
        row=(dot(xx[i],sub(xx[j],xx[i])),dot(xx[j],sub(xx[i],xx[j])),dot(poles[f],sub(poles[h],poles[f])),dot(poles[h],sub(poles[f],poles[h])))
        us[i]&=row[0]<0;us[j]&=row[1]<0;ss[f]&=row[2]<0;ss[h]&=row[3]<0
        if max(row)<0:hs.append(edge)
        if max(row)<=0 and 0 in row:weak.append(edge)
        pack.append((edge,fs,row))
    return dict(points=p,facets=[cy for cy,n,h in faces],edges=sorted(edges),V=V,J=J,g=g,E=E,N=N,T=N/(6*V*E),
                ell_moments=M,f_vector=(len(vertices),len(edges),len(faces)),strict=(sum(ss),sum(us.values()),len(hs)),weak=weak,packets=pack)

def run_case(name,b,c,d,mins,level,LENGTH=2,original=False):
    b,c,d=map(Q,(b,c,d));xi,eta,zeta=map(Q,mins)
    L=lambda p:-2+p[0]/d+p[1]/c+(2-p[0]-p[1])/b
    rinv=lambda p:(p[0]/(d*L(p)),p[1]/(c*L(p)),(2-p[0]-p[1])/(b*L(p)))
    forward=lambda p:(d*p[0]/((1-sum(p))/2+d*p[0]+c*p[1]+b*p[2]),c*p[1]/((1-sum(p))/2+d*p[0]+c*p[1]+b*p[2]))
    R=chull([(xi,eta),(2-eta-zeta,eta),(xi,2-xi-zeta)])
    kr=clip(R,lambda p:L(p)-level)
    assert len(kr)==4 and min(map(L,R))<=0 and min(map(L,kr))==level>0
    # Three vertices at each rounded corner; every edge has a retained middle segment.
    fr=[]
    for i,p in enumerate(kr):
        prev,nxt=kr[i-1],kr[(i+1)%4]
        for j in range(LENGTH+1):
            t=Q(j,LENGTH);fr.append(add(p,add(mul((1-t)**2/5,sub(prev,p)),mul(t*t/5,sub(nxt,p)))))
    if original:
        kk=[rinv(x) for x in kr];fr=[]
        for i,p in enumerate(kk):
            for j in range(LENGTH+1):
                t=Q(j,LENGTH)
                r=add(p,add(mul((1-t)**2/5,sub(kk[i-1],p)),mul(t*t/5,sub(kk[(i+1)%4],p))))
                fr.append(forward(r))
    fr=chull(fr);assert len(fr)==4*(LENGTH+1)
    assert min(x[0] for x in fr)==xi and min(x[1] for x in fr)==eta and min(2-sum(x) for x in fr)==zeta
    assert min(map(L,fr))==level
    K3=[rinv(x) for x in kr];F3=[rinv(x) for x in fr]
    K=chull([x[:2] for x in K3]);F=chull([x[:2] for x in F3]);to3=lambda p:(p[0],p[1],(1+(d-1)*p[0]+(c-1)*p[1])/(1-b))
    nn=lambda p:(1+b+c)*p[0]+(1+b+d)*p[1]
    out=K[:];records=[];caps=[]
    for i,p in enumerate(K):
        u=K[(i+1)%len(K)];v=K[i-1];e=sub(u,p);f=sub(v,p);jac=orient(p,u,v);assert jac>0
        # Positive inverse projectivity need not preserve Euclidean edge lengths.
        def lc(x):
            w=sub(x,p);return ((w[0]*f[1]-w[1]*f[0])/jac,(e[0]*w[1]-e[1]*w[0])/jac)
        local=chull([lc(x) for x in F]);aa=[x[0] for x in local if x[1]==0];hh=[x[1] for x in local if x[0]==0]
        aa0=min(aa);hh0=min(hh);assert aa0>0 and hh0>0
        tri=[(Q(0),Q(0)),(aa0,Q(0)),(Q(0),hh0)]
        ma,ja=poly(tri);mi,ji=poly(intersect(local,tri));m=ma-mi;X=ja[0]-ji[0];Y=ja[1]-ji[1]
        assert m>0
        mn=m/(aa0*hh0);xn=X/(aa0*aa0*hh0);yn=Y/(aa0*hh0*hh0)
        assert 2*mn*mn/3<=xn<=mn/3 and xn+yn<=(mn+2*mn*mn)/3 and xn*yn>=2*mn**3/9
        pe,qe=nn(e),nn(f)
        if qe>=0:
            aa=3*X/m;hh=2*m/aa;choice='same axial first moment'
        else:
            aa,hh=min([(2*m/hh0,hh0),(aa0,2*m/aa0)],key=lambda t:(pe*t[0]+qe*t[1],t));choice='endpoint triangle'
        assert 0<aa<=aa0 and 0<hh<=hh0 and aa*hh==2*m
        oldcost=jac*(m*nn(p)+pe*X+qe*Y);newcost=jac*m*(nn(p)+(pe*aa+qe*hh)/3)
        assert newcost<=oldcost
        c1=add(p,mul(aa,e));c2=add(p,mul(hh,f))
        out=clip(out,lambda x,c1=c1,c2=c2:-orient(c1,c2,x))
        # Recover the containing image corner and determine its actual Minkowski anchor.
        ip=forward(to3(p));idx=kr.index(ip);pre=kr[idx-1];nxt=kr[(idx+1)%len(kr)]
        aedge=sub(ip,pre);bedge=sub(nxt,ip);normal=(aedge[1]+bedge[1],-aedge[0]-bedge[0])
        scores=[Q(0),normal[0],normal[1]];anchor_idx=max(range(3),key=lambda i:scores[i]);assert scores.count(max(scores))==1
        anchor=[B,D,C][anchor_idx];height=[b,d,c][anchor_idx];label=['B','D','C'][anchor_idx]
        area=jac*m;rr=(jac*(m*p[0]+X*e[0]+Y*f[0]),jac*(m*p[1]+X*e[1]+Y*f[1]))
        rrz=(area+(d-1)*rr[0]+(c-1)*rr[1])/(1-b);rootj=(rr[0],rr[1],rrz)
        nr=(jac*m*(p[0]+(aa*e[0]+hh*f[0])/3),jac*m*(p[1]+(aa*e[1]+hh*f[1])/3))
        nrz=(area+(d-1)*nr[0]+(c-1)*nr[1])/(1-b);newrootj=(nr[0],nr[1],nrz)
        vol=height*area/(3*(1-b));Ell=height*vol/4
        Jold=add(mul(vol/4,anchor),mul(height/(4*(1-b)),rootj))
        Jnew=add(mul(vol/4,anchor),mul(height/(4*(1-b)),newrootj))
        caps.append((vol,Ell,Jold,Jnew))
        records.append(dict(corner=to3(p),image_corner=ip,anchor=label,height=height,local_area=m,local_first=(X,Y),allowed=(aa0,hh0),replacement=(aa,hh),
                            root_xy_area=area,old_root_n=oldcost,new_root_n=newcost,choice=choice))
    before=body([to3(x) for x in F],b,c,d);after=body([to3(x) for x in out],b,c,d);container=body([to3(x) for x in K],b,c,d)
    assert len(out)<=8 and poly(F)[0]==poly(out)[0]>0
    H=max(sum(x) for x in before['points'][4:])
    assert H==1+2/level==max(sum(x) for x in after['points'][4:])
    assert H<=6*before['V']
    assert all(sum(x)<=H for x in container['points'])
    assert before['V']==after['V'] and before['E']==after['E'] and before['N']<after['N']
    assert container['V']-sum(x[0] for x in caps)==before['V']
    assert container['E']-sum(x[1] for x in caps)==before['E']
    for j in range(3):
        assert container['J'][j]-sum(x[2][j] for x in caps)==before['J'][j]
        assert container['J'][j]-sum(x[3][j] for x in caps)==after['J'][j]
    assert before['ell_moments']==after['ell_moments']
    assert before['T']>container['T']  # Filling the horizon-safe container is not trace dominance.
    return dict(name=name,chain_chart='original' if original else 'image',endpoints=(1,b,c,d),minima=(xi,eta,zeta),horizon_level=level,actual_radial_height=H,minima_triangle=R,L_at_triangle=[L(x) for x in R],image_container=kr,
                input_root_image=fr,replacements=records,root_area_before=poly(F)[0],root_area_after=poly(out)[0],before=before,after=after,container=container)

def clean(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [clean(v) for v in x]
    return x

def main():
    cases=[run_case('simple_original_horizon',Q(1,2),2,Q(1,2),(Q(1,10),)*3,Q(1,2),original=True),
           run_case('symmetric_horizon',Q(1,2),2,Q(1,2),(Q(1,10),)*3,Q(1,2)),
           run_case('near_endpoint_wall',Q(19,20),Q(21,20),Q(1,100),(Q(1,10000),Q(1,100),Q(1,100)),Q(1,20))]
    audited=[r[k] for r in cases for k in ('before','after','container')]
    assert sum(4*len(o['edges']) for o in audited)==792
    assert all(not o['weak'] and all(x!=0 for e,fs,row in o['packets'] for x in row) for o in audited)
    raw=(json.dumps(clean(cases),sort_keys=True,separators=(',',':'))+'\n').encode()
    target=Path(sys.argv[2])
    if sys.argv[1]=='build':target.write_bytes(raw)
    else:assert target.read_bytes()==raw
    for r in cases:
        print(r['name'],'L_TRI',*[str(x) for x in r['L_at_triangle']])
        for key in ('before','after'):
            o=r[key];print(key,'VEF',*o['f_vector'],'SUH',*o['strict'],'WEAK',len(o['weak']),'T',o['T'])
        print('V',r['before']['V'],'E',r['before']['E'],'DELTA_N',r['after']['N']-r['before']['N'])
        print('ANCHORS',','.join(x['anchor'] for x in r['replacements']))
    src=Path(__file__).read_bytes()
    print('SOURCE',len(src),hashlib.sha256(src).hexdigest())
    print('REPORT',len(raw),hashlib.sha256(raw).hexdigest())
    print('HORIZON_FOUR_CORNER_ORIGINAL_DENSITY_EXACT_PASS')
if __name__=='__main__':
    assert len(sys.argv)==3 and sys.argv[1] in ('build','check')
    main()
```
