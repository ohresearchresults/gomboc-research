# minimum-0141

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# BALANCED_TRIANGULAR_RECIPROCAL_CIRCUITS_V1

## Determination

**There is a universally impossible, inclusion-minimal system of four nonnegative actual escape arrows, on four DISTINCT true physical edges, which NO single nonnegative primal/polar aggregate pair can certify.** The configuration consists of a two-step primal chain around a triangular facet and a two-step polar chain around its initial simple vertex. This holds throughout the complete balanced realization domain, for every common reciprocal SPD metric, including mechanical equality walls and additional weak equilibria. Both two-source aggregates have inertia (+,−,−) when their weights are positive; the failure is not the already-known common-source rank-two limitation.

The missing mechanism is an exact identity whose multipliers depend on the SAME primal metric and inverse metric. It is a sum of nonnegative products under the four purported escapes, with a strictly positive edge-length product. I also obtain a sharp signed-root version: its only closed-boundary exception is a genuine vertex–facet resting point. A separate explicit inverse-convexification example shows that even ALL valid linear constraints on the inverse image of the primal chain cannot recover this signed-root obstruction.

**Executed actual controls:** four metrics on the parent's exact balanced shape each realize three of the four positive arrows strictly, and each body is own-centroid222/weak000. Seven further controls preserve the scalar-aggregation false positive, the inverse-convexification failure, the signed-root minimality witnesses, and the genuine VF boundary. All eleven have actual10/17/9; none is110. The complete standalone readable source below reproduces every exact object. Normal and fresh source-only build/check both passed byte for byte.

The inherited triangle-root-leaf exclusion is not being renamed as a new ledger closure. The new results are the sharp local identity, root-free four-arrow formulation, universal minimality, source-location obstruction to cofactor certificates, and actual—not merely formal—failure of all scalar aggregation weights. No full balanced-domain exclusion, new selected-tree count, or improvement of34≤C_min≤622 is claimed.

## 1. Sources and complete domain

I read the entire2036-line journal update, including common memory, branch memory and the literal parent `minimum-0136`, declared SHA-256 `b6789e45d05a9964faba66158c9a89ff82ba2f753f2296e0ef2bb3b90ebb213a`, and both newly supplied coordinator materials through EOF. The mounted update is348676 bytes, SHA-256 `558463a689ed4be3e3c06fdaf2d1acc3009ce99a0f6c4b0f64530476ca88fd85`. The new proof is11874 bytes, SHA-256 `591d67555c7a3a78bc62c3d9c5d347223f34b9341721cb9fa7a19aeecaeed0fb`; its complete7695-byte source matches `3c85287035cbd3d0d06f3307fbdb43e761db77a88469fc1881465f5b614bfc45`. No source conflict or missing dependency is required here. The new source is independent of the older repaired wrappers.

The coordinator's alternative is used with its precise scope: for one symmetric A of inertia (+,−,−) and nonzero B, either B≤c adj(A) for c≥0, excluding the joint weak scalar pair, or ONE SPD M makes A:M and B:M⁻¹ both strictly positive. It is not a completeness theorem for several inequalities.

The balanced domain uses eight positive cuts `((sx,sy),(wx,wy),(nx,ny),(ex,ey))`, with `sx+ex,wx+nx,sy+wy,ny+ey<2`, and a>0. Its raw vertices are

```text
P0=(-1+sx,-1,0)       P1=(-1,-1+sy,0)
P2=(-1,1-wy,0)        P3=(-1+wx,1,0)
P4=(1-nx,1,0)         P5=(1,1-ny,0)
P6=(1,-1+ey,0)        P7=(1-ex,-1,0)
P8=(-a,0,1)           P9=(a,0,1).
```

Set `Y_i=P_i/(1+u P_ix+v P_iy)`, with all ten denominators strictly positive; u,v are real. Refill uniformly, compute its actual volume centroid g, and put X_i=Y_i−g. The true maximal facets are

```text
F0=(0,1,2,3,4,5,6,7)
F1=(0,8,1) F2=(1,8,2) F3=(2,8,3) F4=(3,8,9,4)
F5=(4,9,5) F6=(5,9,6) F7=(6,9,7) F8=(7,9,8,0).
```

Their cycles give17 true edges. This is the accepted whole balanced normal form, not an equal-angle or small-cut restriction.

Throughout, `M>0`, `N=M⁻¹`, and actual poles satisfy `q_f·X_i≤1`. Polar mass is NEVER refilled or independently recentered. The theorems below in fact require only an actual interior reference; applying them at the true uniform centroid is therefore valid. All geometric collapse boundaries remain outside the stated strict face stratum; mechanical zero-arrow walls are included explicitly.

## 2. The mixed reciprocal identity at a true triangle

Let F=conv{x,y,z} be ANY actual triangular maximal facet, with normalized pole q. Let r be its neighboring pole across edge xz and p its neighboring pole across xy. Define the genuine positive slacks

`δ_y=1−r·y>0`, `δ_z=1−p·z>0`.

Write

```text
a = xᵀM(y−x),                 b = yᵀM(z−y),
E_y = qᵀN(r−q),               E_z = qᵀN(p−q),
ℓ = (y−x)ᵀM(y−x)>0,          s = qᵀNq>0,
χ = s(xᵀMx)−1 ≥0.
```

The last inequality is the common-metric Cauchy inequality, using q·x=1. The exact identity is

**(T)** `χ+s a−(a+ℓ)E_y/δ_y−(a+ℓ+b)E_z/δ_z=0`.

**Proof.** The actual perpendicular foot f=Nq/s lies in aff(F), whether or not it lies inside F. Write its unique affine coordinates as f=λ_x x+λ_y y+λ_z z, with sum1. True incidence gives

`λ_y=−E_y/(sδ_y)`, `λ_z=−E_z/(sδ_z)`.

The tangent vectors x−f,y−f,z−f have weighted sum0. Pairing that identity with y−f and eliminating λ_x gives

`0=(xᵀMy−1/s)+λ_y(yᵀMy−xᵀMy)+λ_z(yᵀMz−xᵀMy)`.

Now `yᵀMy−xᵀMy=a+ℓ` and `yᵀMz−xᵀMy=a+ℓ+b`. Substitution proves (T). The same N appears in the foot, the pole escapes and χ; replacing it by an independent matrix destroys this identity.

### Sharp closed-boundary statement

If a,b≥0 and E_y,E_z≤0, all four terms of (T) are nonnegative. Since ℓ>0, equality forces

`a=χ=E_y=E_z=0`, and `Nq=s x`.

Conversely Nq=sx makes a=E_y=E_z=0; the remaining condition is b≥0. Thus the closed four-inequality system is feasible **exactly at the foot f=x, with b≥0**. This is a genuine physical VF point: Mx is a positive multiple of q, so the radial supporting plane at x exposes the entire actual facet F. It is not a harmless zero primitive. Accordingly the signed system excludes properweak000, but must NOT be declared a weak-boundary exclusion.

A useful quantitative consequence under a,b≥0 is

`max(E_y/δ_y,E_z/δ_z) ≥ (χ+s a)/(2(a+ℓ)+b)`.

In particular, except at that VF configuration, one of these TWO specified outgoing pole escapes is strictly positive. Irrespective of the VF exception, at least one of p,r has squared N-norm strictly larger than q: otherwise both E_y,E_z would be strictly negative by the edge norm identity. This is a strict necessary pole-rank condition, not a hypothesis that F is the stable root.

The dual identity is equally valid on every actual triangular polar facet, using N and M in reversed roles at the SAME origin. The balanced complex supplies36 oriented primal instances from its six triangles and48 polar instances from its eight simple basal vertices:84 generated identities. These are local instances, not registry units.

## 3. Four DISTINCT true positive arrows: a universal obstruction

Assume in addition that x is simple. Then p and r are adjacent actual polar vertices: their common physical edge is the third edge at x, outside F. Consider

`x→y→z` and `p→r→q`.

Their physical edges are xy, yz, the third edge at x, and xz: four distinct TRUE edges. Put

```text
c=pᵀN(r−p),                 d=rᵀN(q−r),
m=||r−q||²_N,               n=||p−r||²_N,               o=||p−q||²_N.
```

All m,n,o are strictly positive. Exact norm telescoping gives

`−E_y=d+m`,
`−E_z=c+d+(m+n+o)/2`.

Therefore (T) becomes the **mixed product certificate**

**(P)** `0=χ+s a+(a+ℓ)(d+m)/δ_y+(a+ℓ+b)[c+d+(m+n+o)/2]/δ_z`.

If a,b,c,d≥0, its right side is at least `ℓm/δ_y>0`, a contradiction. This excludes the FULL weak four-arrow system for every actual realization and every common SPD metric. Additional physical weak points elsewhere cannot change the contradiction. No root, height-ratio, covariance, conditioning or centroid-location restriction is used.

A longer-path variant is immediate: if the two actual polar poles p,r both have genuine weak escape paths ending at q, their norms are strictly smaller than q's, contradicting the pole-rank conclusion in Section2. Paths may be broken into any actual incident edges; a full cyclic star is not assumed.

There are24 oriented instances of (P) from primal triangular facets with basal initial vertex, and24 polarity-reversed instances:48 generated configurations. The source checks that all four edges in EACH instance are distinct actual physical edges. In an already selected complementary pair, the familiar triangular root-leaf argument overlaps this exclusion. I have NOT claimed48 new selected-tree closures. The root-free available-arrow implication and its exact nonconstant-multiplier certificate are what can be reused beyond that overlap.

## 4. Why EVERY scalar aggregation weight misses this actual obstruction

Let `A=α sym(x,y−x)+β sym(y,z−y)` with α,β>0, and let B be ANY positive weighted aggregate of the two actual polar-chain arrows. Put X=[x,y,z]. Since F is a true facet and the reference is interior, X is invertible. In that basis,

```text
A=X H Xᵀ,
H=((-α,α/2,0),(α/2,−β,β/2),(0,β/2,0)),
det H=αβ²/4,
[e1ᵀ adj(H)e1]=−β²/4.
```

Thus A has inertia (+,−,−), and

`xᵀadj(A)x=−det(X)² β²/4<0`.

All three actual polar-chain vertices p,r,q are incident to x, so x·p=x·r=x·q=1. Consequently

`xᵀ B x=0`

for EVERY choice of polar aggregation weights. The polar triangle is nondegenerate, so positive weights likewise give B inertia (+,−,−). Hence `B≤c adj(A)` is impossible for c>0 by evaluation at x, and impossible for c=0 because B has a positive eigenvalue. The supplied scalar alternative proves that one SPD M makes BOTH aggregates strictly positive. Allowing one weight to vanish does not help: the resulting individually feasible rank-two arrow is covered by the general scalar alternative.

This is an actual, disjoint-edge, two-source/two-source counterexample to a proposed completeness of single aggregate certificates. It is not the coordinator's formal traceless-matrix countercontrol and not an independently chosen polar.

**Source-location necessary condition.** More generally, any nontrivial cofactor comparison for a two-step primal chain starting at x, with an individually feasible B, requires `xᵀBx<0`. In actual pairings this is

`Σ μ_fh (x·q_f)[x·q_h−x·q_f]<0`.

An aggregate whose arrows stay entirely inside the actual pole fan incident to x has value0 and cannot work. Thus increasing its weights or its number of within-fan arrows alone cannot repair this obstruction. A larger primal aggregate, a polar aggregate leaving that fan, or genuinely simultaneous mixed constraints are different possibilities and are NOT excluded by this theorem.

## 5. Minimality is universal, with constructive common metrics

Normalize the true triangle by X so its vertices are e1,e2,e3. The actual poles become

```text
q=(1,1,1), r=(1,1−δ_y,1), p=(1,1,1−δ_z).
```

The four inequalities are the two primal chains and the two polar chains in Section3. EVERY proper subsystem is strictly feasible for every δ_y,δ_z>0.

Here is the complete reusable construction underlying the source. Given primal matrices A_i and polar matrices B_j, choose rational v,w with v·w=0, every wᵀA_iw>0 and every vᵀB_jv>0. Put

```text
P=vvᵀ/(vᵀv), Q=I−P,
epsilon=min_i {wᵀA_iw/[2(1+|A_i:Q|)]},
H=wwᵀ+epsilon Q, Hdag=(H+P)⁻¹−P,
G=T H+P, G⁻¹=T⁻¹Hdag+P.
```

Choose an integer T strictly larger than0 and all `−(A_i:P)/(A_i:H)` and `−(B_j:Hdag)/(B_j:P)`. Then this ONE reciprocal pair satisfies all retained inequalities strictly.

To delete either primal inequality, choose v with `(p·v,r·v,q·v)=(1,2,k)`, k among4,5,6. For retaining y→z use `w=(-(v2+2v3)/v1,1,2)`; for retaining x→y use `w=(1,2,-(v1+2v2)/v3)`. The required denominator can be made nonzero among those choices. Both polar rank-one values are positive.

To delete the first polar inequality p→r, use the physical triangular vectors `(1,0,0),(2,1,0),(R,1,1)`, with integer R>3+2δ_y. Their Gram G has primal values1 and2R−4, and the retained polar value is `δ_y(R−3−2δ_y)>0`.

To delete the second polar inequality r→q, take sufficiently small positive dyadic e and

`v=(1,−2δ_z e,−δ_y e)`, `w=(2(δ_y+δ_z)e,1,2)`.

Then v·w=0, both primal rank-one values are positive, and `vᵀB_1v=(p·v)δ_yδ_z e>0`. The common-metric construction above completes the strict subsystem. Dyadic halving terminates because the displayed strict conditions hold near e=0.

Pull each resulting G back as `M=X⁻ᵀ G X⁻¹`, `N=X G⁻¹ Xᵀ`. This changes only the physical affine metric, not the actual uniform reference. For rational original data all witnesses and recipes are rational. No metric is fitted independently to the polar.

## 6. Actual balanced controls, including the genuine weak boundary

All new controls use the SAME exact11 shape parameters from the accepted fan-blind parent:

```text
(sx,sy,wx,wy,nx,ny,ex,ey,a,u,v)
=(.18,1.38,1.15,.33,.67,.16,.18,1.61,.27,−.21,−.66).
```

These are terminating rationals. The selected triangle is F3 with `(x,y,z)=(X2,X8,X3)`, and `(p,r,q)=(q2,q0,q3)`. The positive four-arrow system is

`2→8→3`, `F2→F0→F3`,

on physical edges `(2,8),(3,8),(1,2),(2,3)`.

The freshly integrated chart volume is

`831029321026158812776613018750000000/178745809468888532386940039010475509`.

The full rational centroid, all vertices/poles and all metric inputs are regenerated by the standalone source from the displayed cuts/projectivity and two actual positive apex fans. It does not transport an old centroid.

The four controls P0–P3 are the universal minimality constructions of Section5. Their deterministic large-metric parameters are respectively T=121, T=24, the rational triangular image with R=11, and T=151 with dyadic e=1/16. Each satisfies precisely three of the four desired positive arrows strictly and violates the omitted arrow strictly. All four are genuine own-centroid222/weak000.

The source also constructs a real scalar-aggregation false positive: one common M has `(a+b)>0` and `(c+d)>0`, although individual a,d are negative. Its scalar-recipe parameters are perturbation1/4, lattice radius2 and T=419. This body is strict323/weak000, not110.

The following table retains all eleven actual controls. Labels refer to the true facets/vertices above; H lists true edges. Every row has zero physical weak points and68 nonzero primitives EXCEPT VF, whose four zeros describe ONE genuine VF point.

| Control | Strict S | Strict U | Strict H | Physical weak |
|---|---|---|---|---|
| R0 |0,3,7|0,5,7|(0,7),(2,3),(2,8),(5,6)|0|
| R1 |0,3,5,6|4,5,7|(2,3),(3,8),(4,5),(5,9),(6,7)|0|
| R2 |0,6|3,7|(0,8),(4,5)|0|
| R3 |0,6|4,7|(1,2),(5,6)|0|
| VF |0,7|4,5,7|(1,2),(4,5),(5,6)|1 VF at2|
| Rbar |0,3,6|2,4,5,7|(1,2),(2,3),(2,8),(4,5),(5,6)|0|
| P0, omit a |3,7|0,5|(0,8),(5,6)|0|
| P1, omit b |3,7|5,8|(5,9),(6,7)|0|
| P2, omit c |2,6|4,7|(5,6),(7,9)|0|
| P3, omit d |0,6|3,7|(4,5),(7,9)|0|
| Scalar sums |0,3,6|4,7|(2,3),(5,6),(7,9)|0|

The VF control uses normalized Gram

`G=((1,1,1),(1,2,3),(1,3,6))`, `G⁻¹1=(1,0,0)`.

Its packets on `(2,3)` and `(2,8)` both have signs `(0,−,−,0)`, edge parameter0 and normal coefficients `(0,1)` in the source's incident-facet order. Both packets are the SAME physical point X2; its radial plane is F3. The strict counts are233 PLUS that weak point. This realizes, rather than merely postulates, the boundary exception of Section2.

The parent's conditioning/product caps are NOT transferred to these changed metrics. No such cap is asserted for the new controls.

## 7. Convexifying the inverse image loses an actual root constraint

This is a SEPARATE limitation for the signed-root system of Section2, not a claim that every simultaneous cofactor relaxation of the positive four-arrow system fails.

In normalized triangular coordinates put

```text
G_B=((1,2,2),(2,5,6),(2,6,9)),
G_A=((1,2,7),(2,5,18),(7,18,66)).
```

Both have determinant1 and both primal chain values strictly positive: (1,1) and(1,13). But

`G_B⁻¹1=(5,−3,1)`, `G_A⁻¹1=(1,7,−2)`.

Their exact convex combination is

```text
Nbar=(4 G_A⁻¹+9 G_B⁻¹)/13
    =((105,−78,22),(−78,113,−34),(22,−34,13))/13,
Nbar*1=(49,1,1)/13>0,
Nbar⁻¹=((313,266,166),(266,881,1854),(166,1854,5781))/1213.
```

Thus Nbar is in the convex hull of inverses of metrics satisfying BOTH primal arrows strictly, but it makes the actual F3 foot strictly interior: the entire root star is strict. Its actual inverse violates the first primal arrow by−47/1213; the second is973/1213. Rbar in the table is this physical reciprocal body, not an independently filled polar or a purported simultaneous witness.

Every valid affine-linear inequality in N for the inverse image of the two primal constraints must hold at Nbar. Hence **no convex outer approximation in N alone** can exclude its intersection with the strict root-star cone. In particular all cofactor cuts of positive primal aggregations hold: for the coordinator's Hc(t),

`4 adj(Hc(t)):Nbar=−1−40t/13−105t²/13<0` for every t≥0.

There are also explicit one-sided scalarization constructions in the source. For any b,c≥0, b+c>0, some common G keeps BOTH primal arrows positive and `b(G⁻¹1)_2+c(G⁻¹1)_3>0`; for b>0 take triangular image `(1,0,0),(2,1,0),(t+2,t,1)` with `t=ceil(c/b)+2`, giving inverse components t−1 and−1. Conversely any nonzero nonnegative primal aggregation can be made positive while keeping the FULL triangular root star strict: use planar image vertices `(-3e,-e,1),(1,0,1),(2,1,1)` with `e≤min(1/10,beta/(8alpha))` when beta>0. Their primal values are `−3e−10e²` and1, while the perpendicular foot lies strictly inside. The zero-coefficient cases are included in the complete code.

These conclusions do not prevent a solver from keeping the actual reciprocal relation or using mixed products such as (T)/(P). They identify why scalarization or an inverse-only convex relaxation drops essential information.

## 8. Executed evidence, scope, and continuation

All eleven controls use the actual common shape and freshly integrated uniform centroid. The source independently reconstructs every maximal facet by supporting triples, all17 true edges, and the actual polar's maximal faces without recentering it. Each common M,N inverse, all748 primitives, every true edge foot, its two normal-cone coefficients, strict facets/vertices and deduplicated weak points are checked exactly. There are744 nonzero primitives and the four VF zeros. Six controls have rational physical affine maps with fresh physical hull and two-fan mass checks. The other five have exact rational LDL factorizations specifying ordinary Euclidean coordinates with positive square roots; their full mechanics is audited in the equivalent rational common-metric chart. No symbolic physical-mass replay is claimed for those five.

The implementation checks924 instances of (T) and528 instances of (P) across the eleven controls. Universal validity is proved analytically above; these finite audits are calibration and recoverability evidence, not sampled whole-domain positivity. Five rational coefficient pairs also test the two parameterized scalarization formulas; those are algebraic matrix checks, not additional physically audited bodies. There is no floating acceptance test, numerical optimizer dependency, or finite nonfinding promoted into an exclusion.

For future outer-domain work, (P) supplies a genuine mixed common-metric constraint involving nonbasal triangular facets and edges outside the apex ridge. Its pole-rank/path version can be propagated using actual available arrows and global norm ordering. Any cofactor-only continuation must respect the source-location obstruction and distinguish a larger cross-fan aggregate from a reweighting of the impossible within-fan scalar architecture. The full remaining balanced domain, including root locations and patterns not forced into these local configurations, is still unresolved. No110, new minimum bound, or registry delta is asserted.

## 9. Complete standalone readable recovery

Save the following exact source as `triangle_reciprocal.py`, UTF-8/LF with one final LF. It contains EVERY exact input and all helpers; no parent file, archive, third-party package, report download or originating sandbox is needed.

```sh
python -S triangle_reciprocal.py build
python -S triangle_reciprocal.py check
```

Executed environment: CPython3.13.5 standard library, assertions enabled. Both normal build/check and a fresh directory containing ONLY this source passed and regenerated identical reports.

```text
triangle_reciprocal.py 17089 bytes
67de5444f2953c23388bf2780bcf4458a742182a1c2beb569a3bac7f046e3698
triangle_reciprocal.json 9116298 bytes
97d9f8106277800a7d74669718f2979e3d3c70a0bfda03dd386db101f71ee743
```

Expected terminal markers:


[Encoded source block omitted; the code in this passage is incomplete.]


```python
"""TRIANGLE_RECIPROCAL_FOUR_CIRCUIT_V1. Python3.13.5 stdlib, assertions.
Parent minimum-0136, SHA256
b6789e45d05a9964faba66158c9a89ff82ba2f753f2296e0ef2bb3b90ebb213a.
All exact inputs are here. Run python -S triangle_reciprocal.py build|check.
"""
from fractions import Fraction as F
from itertools import combinations,permutations
from pathlib import Path
import hashlib,json,sys
assert __debug__
FAC=((0,1,2,3,4,5,6,7),(0,8,1),(1,8,2),(2,8,3),(3,8,9,4),(4,9,5),(5,9,6),(6,9,7),(7,9,8,0))
ED=tuple(sorted({tuple(sorted((f[j],f[(j+1)%len(f)]))) for f in FAC for j in range(len(f))}))
EF=tuple(tuple(i for i,f in enumerate(FAC) if a in f and b in f) for a,b in ED)
PE=dict(zip(ED,EF));QE={tuple(sorted(fh)):e for e,fh in zip(ED,EF)}
PARAM=tuple(map(F,('.18','1.38','1.15','.33','.67','.16','.18','1.61','.27','-.21','-.66')))
# Rows are physical images of the three normalized triangular-basis vertices.
TS=((( -3,-1,1),(1,0,1),(2,1,1)),
    ((1,0,1),(2,1,1),(-3,-1,1)),
    ((1,0,0),(2,1,0),(2,2,1)),
    ((1,0,0),(2,1,0),(7,4,1)),
    ((0,0,1),(1,0,1),(2,1,1)))
XYZ=(2,8,3); ROOT=3

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(a,c):return tuple(c*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def tr(A):return tuple(zip(*A))
def mv(A,b):return tuple(dot(a,b) for a in A)
def mm(A,B):return tuple(tuple(dot(a,b) for b in tr(B)) for a in A)
def ms(A,c):return tuple(mul(a,c) for a in A)
def ma(A,B):return tuple(add(a,b) for a,b in zip(A,B))
def det(A):return dot(A[0],cross(A[1],A[2]))
def adj(A):return tuple(tuple(A[(j+1)%3][(i+1)%3]*A[(j+2)%3][(i+2)%3]-A[(j+1)%3][(i+2)%3]*A[(j+2)%3][(i+1)%3] for j in range(3)) for i in range(3))
def inv(A):return ms(adj(A),1/det(A))
def eye():return tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
def bil(a,M,b):return dot(a,mv(M,b))
def sg(a):return (a>0)-(a<0)
def sym(a,b):return tuple(tuple((a[i]*b[j]+b[i]*a[j])/2 for j in range(3)) for i in range(3))
def pair(A,B):return sum(A[i][j]*B[i][j] for i in range(3) for j in range(3))
def arrow(V,i,j):return sym(V[i],sub(V[j],V[i]))
def ceil(q):return -((-q.numerator)//q.denominator)
def rat(A):return tuple(tuple(F(x) for x in r) for r in A)
def pd(A):
 assert A==tr(A)
 r=(A[0][0],A[0][0]*A[1][1]-A[0][1]**2,det(A));assert min(r)>0;return r

def mass(Y,root):
 D=F(0);J=(F(0),)*3
 for f in FAC:
  if root in f:continue
  for j in range(1,len(f)-1):
   ids=(root,f[0],f[j],f[j+1]);p=[Y[i] for i in ids]
   d=abs(det(tuple(sub(x,p[0]) for x in p[1:])));assert d>0
   D+=d;J=add(J,mul(tuple(sum(x[k] for x in p) for k in range(3)),d))
 return D/6,mul(J,1/(4*D))

def hull(Y):
 out=set()
 for i,j,k in combinations(range(len(Y)),3):
  n=cross(sub(Y[j],Y[i]),sub(Y[k],Y[i]))
  if n==(0,0,0):continue
  s=tuple(dot(n,sub(x,Y[i])) for x in Y)
  if min(s)>=0 or max(s)<=0:out.add(tuple(i for i,x in enumerate(s) if x==0))
 return out

def geometry():
 sx,sy,wx,wy,nx,ny,ex,ey,a,u,v=PARAM
 assert min(PARAM[:9])>0 and max(sx+ex,wx+nx,sy+wy,ny+ey)<2
 P=((-1+sx,-1,0),(-1,-1+sy,0),(-1,1-wy,0),(-1+wx,1,0),(1-nx,1,0),(1,1-ny,0),(1,-1+ey,0),(1-ex,-1,0),(-a,0,1),(a,0,1))
 h=tuple(1+u*x+v*y for x,y,z in P);assert min(h)>0
 Y=tuple(mul(p,1/f) for p,f in zip(P,h));V,g=mass(Y,8);assert mass(Y,9)==(V,g)
 assert hull(Y)=={tuple(sorted(f)) for f in FAC}
 X=tuple(sub(y,g) for y in Y);assert mass(X,8)==mass(X,9)==(V,(0,0,0))
 Q=[]
 for f in FAC:
  n=cross(sub(X[f[1]],X[f[0]]),sub(X[f[2]],X[f[0]]));q=mul(n,1/dot(n,X[f[0]]))
  assert all(dot(q,x)==1 if i in f else dot(q,x)<1 for i,x in enumerate(X));Q.append(q)
 assert len(ED)==17 and all(len(x)==2 for x in EF)
 assert {tuple(sorted(set(f)&set(h))) for f,h in combinations(FAC,2) if len(set(f)&set(h))==2}==set(ED)
 # Reconstruct the polar's maximal faces independently, without recentering it.
 assert hull(Q)=={tuple(i for i,f in enumerate(FAC) if j in f) for j in range(10)}
 return dict(parameters=PARAM,raw=P,denominators=h,Y=Y,volume=V,centroid=g,X=X,Q=tuple(Q),facets=FAC,edges=ED,edge_facets=EF)

def stencil(V,Q,E,f,xyz,M,N):
 i,j,k=xyz
 a=next(h for h in E[tuple(sorted((i,k)))] if h!=f)
 b=next(h for h in E[tuple(sorted((i,j)))] if h!=f)
 x,y,z=V[i],V[j],V[k];q=Q[f]
 dy=1-dot(Q[a],y);dz=1-dot(Q[b],z);assert dy>0 and dz>0
 D1=bil(x,M,sub(y,x));D2=bil(y,M,sub(z,y))
 Ey=bil(q,N,sub(Q[a],q));Ez=bil(q,N,sub(Q[b],q))
 length=bil(sub(y,x),M,sub(y,x));s=bil(q,N,q);gap=s*bil(x,M,x)-1
 assert gap>=0 and length>0 and s>0
 C=D1+length;identity=gap+s*D1-C*Ey/dy-(C+D2)*Ez/dz
 assert identity==0
 if D1>=0 and D2>=0 and Ey<=0 and Ez<=0:
  assert D1==gap==Ey==Ez==0 and mv(N,q)==mul(x,s)
 return dict(root=f,chain=xyz,opposite_neighbors=(a,b),opposite_slacks=(dy,dz),primitives=(D1,D2,Ey,Ez),length2=length,s=s,cauchy_gap=gap,multiplier=(C,C+D2),identity=identity)

def all_stencils(z,M,N):
 out=[]
 for f,vs in enumerate(FAC):
  if len(vs)==3:
   for xyz in permutations(vs):out.append(('P',stencil(z['X'],z['Q'],PE,f,xyz,M,N)))
 for i in range(10):
  fs=tuple(f for f,vs in enumerate(FAC) if i in vs)
  if len(fs)==3:
   for xyz in permutations(fs):out.append(('Q',stencil(z['Q'],z['X'],QE,i,xyz,N,M)))
 assert len(out)==84
 positives=0
 for side,c in out:
  V,Q,E,M0,N0=(z['X'],z['Q'],PE,M,N) if side=='P' else (z['Q'],z['X'],QE,N,M)
  i,j,k=c['chain'];f=c['root'];h,p=c['opposite_neighbors']
  if sum(i in edge for edge in E)!=3:continue
  other=QE if side=='P' else PE
  assert tuple(sorted((h,p))) in other
  ve=(tuple(sorted((i,j))),tuple(sorted((j,k))),other[tuple(sorted((p,h)))],other[tuple(sorted((h,f)))])
  real=ve if side=='P' else tuple(QE[tuple(sorted(e))] for e in ve)
  assert len(set(real))==4 and all(tuple(sorted(e)) in PE for e in real)
  x,y,zz=V[i],V[j],V[k];q,r,pp=Q[f],Q[h],Q[p]
  a,b=c['primitives'][:2];cc=bil(pp,N0,sub(r,pp));dd=bil(r,N0,sub(q,r))
  m=bil(sub(r,q),N0,sub(r,q));n=bil(sub(pp,r),N0,sub(pp,r));o=bil(sub(pp,q),N0,sub(pp,q))
  dy,dz=c['opposite_slacks'];ell=c['length2']
  terms=(c['cauchy_gap'],c['s']*a,(a+ell)*(dd+m)/dy,(a+ell+b)*(cc+dd+(m+n+o)/2)/dz)
  assert sum(terms)==0 and min(m,n,o)>0 and not all(v>=0 for v in (a,b,cc,dd))
  B=tr((x,y,zz));A1=arrow(V,i,j);A2=arrow(V,j,k)
  assert bil(x,adj(A1),x)==0 and bil(x,adj(A2),x)==-det(B)**2/4
  assert bil(x,adj(ma(A1,A2)),x)==bil(x,adj(A2),x)
  assert dot(x,q)==dot(x,r)==dot(x,pp)==1
  c['positive_disjoint_circuit']=dict(dual_chain=(p,h,f),physical_edges=real,four_values=(a,b,cc,dd),identity_terms=terms)
  positives+=1
 assert positives==48
 return out

def ldl(M):
 # Physical map diag(sqrt(D))*L^T; all listed L,D are rational and D>0.
 L=[[F(i==j) for j in range(3)] for i in range(3)];D=[]
 for j in range(3):
  D.append(M[j][j]-sum(L[j][k]**2*D[k] for k in range(j)));assert D[j]>0
  for i in range(j+1,3):L[i][j]=(M[i][j]-sum(L[i][k]*L[j][k]*D[k] for k in range(j)))/D[j]
 L=tuple(map(tuple,L));DD=tuple(tuple(D[i] if i==j else F(0) for j in range(3)) for i in range(3))
 assert mm(mm(L,DD),tr(L))==M
 return dict(L=L,D=tuple(D),physical_map='diag(sqrt(D))*transpose(L)')

def audit(z,G,T=None):
 basis=tr(tuple(z['X'][i] for i in XYZ));bi=inv(basis)
 M=mm(mm(tr(bi),G),bi);N=mm(mm(basis,inv(G)),tr(basis));pd(M);pd(N);assert mm(M,N)==eye()
 X,Q=z['X'],z['Q'];S=set(range(9));U=set(range(10));H=[];weak={};pack=[];zeros=0
 for (i,j),(f,h) in zip(ED,EF):
  a=bil(X[i],M,sub(X[j],X[i]));b=bil(X[j],M,sub(X[i],X[j]))
  c=bil(Q[f],N,sub(Q[h],Q[f]));d=bil(Q[h],N,sub(Q[f],Q[h]));ds=(a,b,c,d);zeros+=sum(x==0 for x in ds)
  if a>=0:U.discard(i)
  if b>=0:U.discard(j)
  if c>=0:S.discard(f)
  if d>=0:S.discard(h)
  t=a/(a+b);p=add(X[i],mul(sub(X[j],X[i]),t))
  ff=bil(Q[f],N,Q[f]);fh=bil(Q[f],N,Q[h]);hh=bil(Q[h],N,Q[h]);D=ff*hh-fh*fh;assert D>0
  lam=((hh-fh)/D,(ff-fh)/D);assert mv(M,p)==add(mul(Q[f],lam[0]),mul(Q[h],lam[1]))
  assert (max(ds)<=0)==(0<=t<=1 and min(lam)>=0)
  r=dict(edge=(i,j),facets=(f,h),primitives=ds,t=t,foot=p,normal_coefficients=lam)
  if max(ds)<0:H.append((i,j))
  elif max(ds)<=0:
   key=p
   if key not in weak:weak[key]=dict(point=p,packets=[])
   weak[key]['packets'].append(r)
  pack.append(r)
 assert all(bil(X[i],M,sub(y,X[i]))<0 for i in U for j,y in enumerate(X) if j!=i)
 feet={f:mul(mv(N,Q[f]),1/bil(Q[f],N,Q[f])) for f in S}
 assert all(all(dot(q,p)<1 for h,q in enumerate(Q) if h!=f) for f,p in feet.items())
 out=dict(G=G,M=M,N=N,ldl=ldl(M),S=sorted(S),U=sorted(U),H=H,weak=list(weak.values()),zero_primitives=zeros,packets=pack,stable_feet=feet,stencils=all_stencils(z,M,N))
 if T is not None:
  A=mm(tr(T),bi);AI=inv(A);Y=tuple(mv(A,x) for x in X);P=tuple(mv(tr(AI),q) for q in Q)
  assert mm(tr(A),A)==M and mass(Y,8)==mass(Y,9)==(abs(det(A))*z['volume'],(0,0,0))
  assert hull(Y)=={tuple(sorted(f)) for f in FAC}
  assert all(dot(y,w)==bil(x,M,v) for x,y in zip(X,Y) for v,w in zip(X,Y))
  assert all(dot(y,w)==bil(x,N,v) for x,y in zip(Q,P) for v,w in zip(Q,P))
  out.update(physical_map=A,physical_vertices=Y,physical_poles=P,physical_volume=abs(det(A))*z['volume'])
 return out

def aggregate_metric(b,c):
 # For ANY rational b,c>=0, b+c>0: two strict chain arrows AND b*r_y+c*r_z>0.
 assert b>=0 and c>=0 and b+c>0
 if b==0:T=rat(TS[2])
 else:
  q=c/b;t=(q.numerator+q.denominator-1)//q.denominator+2
  T=rat(((1,0,0),(2,1,0),(t+2,t,1)))
 G=mm(T,tr(T));r=mv(inv(G),(1,1,1))
 assert G[0][1]>G[0][0] and G[1][2]>G[1][1] and b*r[1]+c*r[2]>0
 return G

def root_metric(alpha,beta):
 # ANY nonzero nonnegative primal aggregation, with the FULL root star strict.
 assert alpha>=0 and beta>=0 and alpha+beta>0
 if beta==0:T=rat(TS[1])
 else:
  e=F(1,10) if alpha==0 else min(F(1,10),beta/(8*alpha))
  T=(( -3*e,-e,F(1)),(F(1),F(0),F(1)),(F(2),F(1),F(1)))
 G=mm(T,tr(T));r=mv(inv(G),(1,1,1))
 assert min(r)>0 and alpha*(G[0][1]-G[0][0])+beta*(G[1][2]-G[1][1])>0
 return G

def large_metric(v,w,As,Bs):
 # v is a strict common rank-one direction for all Bs; w perpendicular v
 # is strictly positive for all As. This gives ONE reciprocal SPD pair.
 assert dot(v,w)==0 and all(bil(v,B,v)>0 for B in Bs) and all(bil(w,A,w)>0 for A in As)
 P=ms(sym(v,v),1/dot(v,v));Q=ma(eye(),ms(P,-1))
 eps=min(bil(w,A,w)/(2*(1+abs(pair(A,Q)))) for A in As)
 H=ma(sym(w,w),ms(Q,eps));Hd=ma(inv(ma(H,P)),ms(P,-1))
 bounds=[F(0)]+[-pair(A,P)/pair(A,H) for A in As]+[-pair(B,Hd)/pair(B,P) for B in Bs]
 t=F(ceil(max(bounds))+1);G=ma(ms(H,t),P);N=ma(ms(Hd,1/t),P)
 pd(G);assert inv(G)==N
 assert all(pair(A,G)>0 for A in As) and all(pair(B,N)>0 for B in Bs)
 return G,dict(v=v,w=w,epsilon=eps,t=t,P=P,H=H,Hdag=Hd)

def scalar_metric(A,B):
 # For the positive two-chain aggregates used below, e1^T B e1=0,
 # B e1!=0, and e1^T adj(A)e1<0. Constructive scalar-pair alternative.
 e1=(F(1),F(0),F(0));be=mv(B,e1);e=F(1)
 while True:
  v=add(e1,mul(be,e))
  if bil(v,B,v)>0 and bil(v,adj(A),v)<0 and v[0]!=0:break
  e/=2
 b1=(-v[1],v[0],F(0));b2=(-v[2],F(0),v[0]);radius=0
 while True:
  radius+=1;found=False
  for i in range(-radius,radius+1):
   for j in range(-radius,radius+1):
    if max(abs(i),abs(j))!=radius:continue
    w=add(mul(b1,i),mul(b2,j))
    if bil(w,A,w)>0:found=True;break
   if found:break
  if found:break
 G,recipe=large_metric(v,w,(A,),(B,));recipe.update(perturbation=e,lattice_radius=radius)
 return G,recipe

def positive_four(z):
 basis=tr(tuple(z['X'][i] for i in XYZ));bi=inv(basis)
 E=eye();one=(F(1),)*3
 dy=1-dot(z['Q'][0],z['X'][8]);dz=1-dot(z['Q'][2],z['X'][3]);assert dy>0 and dz>0
 q=one;py=(F(1),1-dy,F(1));pz=(F(1),F(1),1-dz)
 A1=arrow(E,0,1);A2=arrow(E,1,2);B1=sym(pz,sub(py,pz));B2=sym(py,sub(q,py))
 # The pole chain is F2 -> F0 -> F3. Its edges are 1--2 and 2--3.
 physical=((2,8),(3,8),(1,2),(2,3));assert len(set(physical))==4 and all(e in ED for e in physical)
 assert tuple(dot(z['Q'][f],z['X'][2]) for f in (2,0,3))==(1,1,1)
 R=mm(tr(basis),tr(tuple(z['Q'][f] for f in (2,0,3))))
 assert R==tr((pz,py,q)) and det(R)!=0
 controls=[];recipes=[]
 # Delete first or second primal inequality; both polar arrows remain strict.
 for missing,A in ((0,A2),(1,A1)):
  for last in (4,5,6):
   v=mv(inv((pz,py,q)),(F(1),F(2),F(last)))
   if (v[0]!=0 if missing==0 else v[2]!=0):break
  if missing==0:w=(-(v[1]+2*v[2])/v[0],F(1),F(2))
  else:w=(F(1),F(2),-(v[0]+2*v[1])/v[2])
  G,recipe=large_metric(v,w,(A,),(B1,B2));controls.append(audit(z,G));recipes.append(recipe)
 # Delete first polar inequality: both primal arrows and py->q are strict.
 r=F(ceil(3+2*dy)+1);T=rat(((1,0,0),(2,1,0),(r,1,1)));G=mm(T,tr(T))
 controls.append(audit(z,G,T));recipes.append(dict(T=T))
 # Delete second polar inequality: a rational rank-one inverse limit for pz->py.
 e=F(1,2)
 while True:
  v=(F(1),-2*dz*e,-dy*e);w=(2*e*(dz+dy),F(1),F(2))
  if 0<w[0]<1 and bil(v,B1,v)>0:break
  e/=2
 G,recipe=large_metric(v,w,(A1,A2),(B1,));recipe['dyadic_e']=e
 controls.append(audit(z,G));recipes.append(recipe)
 for missing,c in enumerate(controls):
  G=c['G'];NN=inv(G);vals=(pair(A1,G),pair(A2,G),pair(B1,NN),pair(B2,NN))
  assert tuple(sg(x) for x in vals)==tuple(-1 if i==missing else 1 for i in range(4))
  c['four_values']=vals
 # Exact coefficient bridge: for all t>0, e1^T adj(Hc(t)) e1=-t^2/4;
 # for all nonnegative polar weights, e1^T B e1=0. The full matrix
 # formulas are recovered, and endpoint certificates have no sampled weights.
 assert B1[0][0]==B2[0][0]==0
 G,recipe=scalar_metric(ma(A1,A2),ma(B1,B2));scalar=audit(z,G)
 scalar['four_values']=tuple(pair(A,G) for A in (A1,A2))+tuple(pair(B,inv(G)) for B in (B1,B2))
 assert sum(scalar['four_values'][:2])>0 and sum(scalar['four_values'][2:])>0
 return dict(slacks=(dy,dz),R=R,primal=(A1,A2),dual=(B1,B2),physical_edges=physical,controls=controls,recipes=recipes,scalar_control=scalar,scalar_recipe=recipe)

def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return list(map(enc,x))
 return x

def main():
 assert sys.argv[1:] in (['build'],['check'])
 z=geometry();ts=tuple(rat(T) for T in TS);gs=[mm(T,tr(T)) for T in ts]
 controls=[audit(z,G,T) for G,T in zip(gs,ts)]
 for i,G in enumerate(gs[:4]):
  r=mv(inv(G),(1,1,1));v=(G[0][1]-G[0][0],G[1][2]-G[1][1],r[1],r[2])
  assert tuple(sg(x) for x in v)==tuple(-1 if j==i else 1 for j in range(4))
 Nbar=ms(ma(ms(inv(gs[3]),4),ms(inv(gs[2]),9)),F(1,13));Gbar=inv(Nbar)
 assert mv(Nbar,(1,1,1))==(F(49,13),F(1,13),F(1,13))
 cofactor=(-Nbar[2][2],2*(Nbar[0][2]+2*Nbar[1][2]+2*Nbar[2][2]),-Nbar[0][0]);assert cofactor==(-F(1),-F(40,13),-F(105,13))
 controls.append(audit(z,Gbar))
 expected=(((0,3,7),(0,5,7),((0,7),(2,3),(2,8),(5,6)),0,0),((0,3,5,6),(4,5,7),((2,3),(3,8),(4,5),(5,9),(6,7)),0,0),((0,6),(3,7),((0,8),(4,5)),0,0),((0,6),(4,7),((1,2),(5,6)),0,0),((0,7),(4,5,7),((1,2),(4,5),(5,6)),1,4),((0,3,6),(2,4,5,7),((1,2),(2,3),(2,8),(4,5),(5,6)),0,0))
 for c,ex in zip(controls,expected):assert (tuple(c['S']),tuple(c['U']),tuple(c['H']),len(c['weak']),c['zero_primitives'])==ex
 w=controls[4]['weak'][0];assert w['point']==z['X'][2] and tuple(p['edge'] for p in w['packets'])==((2,3),(2,8))
 assert all(p['t']==0 and p['normal_coefficients']==(0,1) for p in w['packets'])
 for k,r in enumerate(controls):print('CONTROL',k,'S',r['S'],'U',r['U'],'H',r['H'],'weak',len(r['weak']),'zeros',r['zero_primitives'])
 tests=[]
 for a,b in ((F(0),F(1)),(F(1),F(0)),(F(1),F(1)),(F(7,3),F(2,11)),(F(1,1000),F(1000))):
  tests.append((a,b,aggregate_metric(a,b),root_metric(a,b)))
 pos=positive_four(z)
 pex=(((3,7),(0,5),((0,8),(5,6))),((3,7),(5,8),((5,9),(6,7))),((2,6),(4,7),((5,6),(7,9))),((0,6),(3,7),((4,5),(7,9))))
 for c,ex in zip(pos['controls'],pex):assert (tuple(c['S']),tuple(c['U']),tuple(c['H']))==ex and not c['weak'] and c['zero_primitives']==0
 sc=pos['scalar_control'];assert (sc['S'],sc['U'],sc['H'],len(sc['weak']),sc['zero_primitives'])==([0,3,6],[4,7],[(2,3),(5,6),(7,9)],0,0)
 print('SCALAR','S',sc['S'],'U',sc['U'],'H',sc['H'],'weak',len(sc['weak']),'zeros',sc['zero_primitives'])
 for i,c in enumerate(pos['controls']):print('POSITIVE',i,'S',c['S'],'U',c['U'],'H',c['H'],'weak',len(c['weak']),'zeros',c['zero_primitives'])
 out=dict(name='TRIANGLE_RECIPROCAL_FOUR_CIRCUIT_V1',geometry=z,triangle=(ROOT,XYZ),controls=controls,positive_four=pos,inverse_convex_combination=dict(weights=(F(4,13),F(9,13)),indices=(3,2),Nbar=Nbar,Gbar=Gbar,cofactor_coefficients=cofactor),rational_aggregate_checks=tests)
 raw=(json.dumps(enc(out),sort_keys=True,separators=(',',':'))+'\n').encode();path=Path(__file__).with_suffix('.json')
 if sys.argv[1]=='build':path.write_bytes(raw)
 else:assert path.read_bytes()==raw
 print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
 print('ALL_84_TRUE_PRIMAL_POLAR_TRIANGLE_RECIPROCAL_IDENTITIES_PASS')
 print('ALL_48_DISJOINT_POSITIVE_FOUR_ARROW_IDENTITIES_PASS')
 print('FOUR_STRICT_CONSTRAINTS_EVERY_PROPER_SUBSYSTEM_FEASIBLE_PASS')
 print('INVERSE_CONVEXIFICATION_AND_ALL_SCALAR_AGGREGATES_INSUFFICIENT_PASS')
 print('FOUR_DISJOINT_TRUE_POSITIVE_ARROWS_MINIMAL_RECIPROCAL_OBSTRUCTION_PASS')
 print('TRIANGLE_RECIPROCAL_FOUR_CIRCUIT_RECOVERY_PASS')
if __name__=='__main__':main()
```

Supplemental copies: standalone source (`triangle_reciprocal.py`), complete handoff (`triangular_reciprocal_handoff.md`), and source, full exact report and cold receipt (`triangular_reciprocal_handoff.zip`). The source above is the complete recovery.
