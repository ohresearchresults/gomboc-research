# minimum-0205

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# DEGREE7_TWO_CAP_FOLDED_ROOF_AND_GLOBAL_GLuing_COUNTERCONTROL_V1

## 1. Result and limits

The strongest completed result here is a **global, actually homogeneous countercontrol to two natural pyramid-gluing arguments**, together with an exact common-centroid reduction for the whole two-cap sector.

For the rational degree-seven body specified below, there is one reciprocal metric family, valid for every real **L >= 2^41**, with

**strict (S,U,H)=(2,2,2), physical weak000, all68 true-edge primitives nonzero.**

Its ONLY stable facets are the two caps. Its unstable vertices are3 and9; the degree-seven apex0 is NOT unstable. The saddle edges are the genuine edges03 and89. Thus the pyramid theorem guaranteeing a lateral stable facet at a pyramid's own centroid does not imply that a glued two-cap body has a stable true lateral facet.

There is a second, quantitative failure of gluing: if cbar is the ACTUAL volume-weighted mean of the two cap centroids, then the convex hull Kcap of the nine nonapical vertices does NOT satisfy `(3cbar-Kcap)/2 subset Kcap`. An explicit point violates a true cap by more than29/100, even though its projection lies strictly inside the appropriate planar convex body.

The general reduction explains this failure. Every genuine two-cap body can be represented by a convex projected nonagon K and a folded affine roof

`H(u)=(u,1-beta|u1|)`.

Its actual volume and all homogeneous moments are integrals over ONE uniform area measure on K. The crease term, not independently selectable pyramid masses, controls the failure of the lifted reflection.

These countercontrols persist in an open actual-realization neighborhood. They are therefore not isolated formal Gram examples or merely local pole-arrow examples.

**No all-SPD exclusion of an entire degree-seven type is established in this handoff. No complete-U1 or110 witness is established.** The construction is of cap type(4,7); the folded-roof theorem applies to all three two-cap types. The interval34<=C_min<=622 and every canonical count remain unchanged.

I also explored an all-SPD stress-cover route on a fixed positive-projective pencil. I do not submit that exploration as an exclusion theorem: a complete, author-confirmed row certificate is not part of this handoff. In particular, no inferred rooted-tree closure count is used below.

## 2. Starting evidence and verification status

The mathematical starting points are the supplied complete units:

- [internal-source-reference], DEGREE7_TWO_CAP_CLASSIFICATION_AND_EXACT_POLAR_COMPLETION_V1;
- [internal-source-reference], the autonomous degree7_twocap source.

Their classification, exact two-cap chart and arbitrary-heptagonal-face completion are accepted premises, not results rediscovered here. The shared journal and supplied units were read in the preceding unfinished attempt and retained for this continuation. No research connector or unselected archival result is needed. The distinction between the two separately centred pyramids and the one actual centroid of their union is maintained throughout. 

The result below is given as a complete analytical construction and proof, with a small standalone rational verifier. **I do not attach a confirmed execution receipt for that verifier in this resumed attempt, and I do not claim unobserved byte counts or SHA-256 output pins.** The script prints its source/report hashes when executed. Its exact inputs, actual mass formulas, true incidence and expected mathematical checks are fully embedded; no numerical search output or hidden certificate array is necessary.

## 3. General folded-roof moment theorem

### Statement

Let P be any genuine convex two-cap body in the supplied degree-seven sector. Put its common apex at raw A=0. Let the two normalized cap equations be ell_plus=1 and ell_minus=1, and choose w in the relative interior of their true seam edge.

The point w is strictly inside the seven-ray lateral cone and satisfies both cap equations=1. Use w as a vertical coordinate direction. A linear shear removes the common cap slope, and a transverse coordinate aligns their difference with u1. In these fixed linear coordinates the union of the two caps is

`H(u)=(u,h(u)), h(u)=1-beta|u1|, beta>0`.

Let K be the projection of P along w. Then K is a genuine convex nonagon containing0 in its interior. Seven projected vertices are the ray endpoints; two are the seam endpoints. Its two portions K_plus and K_minus are cut by u1=0.

For every homogeneous polynomial phi of degree d about A,

**`integral_P phi(Y)dY = (1/(d+3)) integral_K phi(H(u))du`.**

Volumes here are in the displayed linear coordinate frame. A fixed coordinate Jacobian restores physical volume and cancels from all normalized moments. In particular,

```
Vol(P)=Area(K)/3,
g=(3/4) E_K H,
E_P[YY^T]=(3/5) E_K[HH^T],
Sigma_P=(3/5)E_K[HH^T]-(9/16)(E_K H)(E_K H)^T.
```

The actual volume fractions of the two pyramids are exactly

`Area(K_plus)/Area(K)` and `Area(K_minus)/Area(K)`.

Their actual cap area centroids are the respective uniform-area means of H on these two regions.

### Proof

Every projection fibre has its upper endpoint on one of the caps. Thus K is also the projection of the cap union. The ray from A through any nonzero point of P has a unique terminal cap point, so, except for measure-zero boundaries, P is parametrized uniquely by

`Y=t H(u), u in K, 0<t<1`.

On either affine cap piece the Jacobian is

`t^2 [h(u)-u.grad h(u)]=t^2`,

because the cap plane has intercept1. Homogeneity contributes t^d; integrating t from0 to1 proves the formula.

The projected ray endpoints remain strict vertices away from the crease. At either seam endpoint, the two cap slopes produce distinct projected edge slopes: the common lateral plane contains A and that endpoint, and its coefficient along w is nonzero. Hence the seam endpoint is also a genuine projected corner. The interior point tw,0<t<1, projects to0, proving0 is interior to K.

The two-cap centroid identity now follows from one area measure rather than two independent assignments of cap masses. The second-moment formula retains the same coupling.

### Explicit crease moments

Writing m=E_K u, a=E_K|u1|, the lifted mean is

`E_K H=(m,1-beta a)`.

The mixed second moment is

`E_K[u h(u)]=m-beta E_K[u|u1|]`,

and

`E_K[h(u)^2]=1-2beta a+beta^2 E_K[u1^2]`.

These quantities belong to the SAME actual projected nonagon. Replacing them by independently chosen moments of two pyramids loses the essential coupling.

Not every abstract nonagon with a crease is automatically an E17 realization. At each seam endpoint the lifted neighboring edges must lie in one true lateral quadrilateral plane through A. This compatibility remains part of the actual shape problem.

## 4. Why planar reflection does not lift

Let

`mH=E_K H`, `c=E_K u`, `a=E_K|u1|`.

For a cap point H(u), form the proposed three-dimensional half-reflection

`r=(3mH-H(u))/2`, with projection `u'=(3c-u)/2`.

Its height above the actual cap roof at u' is exactly

**`r_z-h(u')=(beta/2)[2|u'_1|+|u1|-3a]`.**

Therefore a positive right-hand side puts r outside the true caps even when u' belongs to K. A planar centroid/reflection argument does not by itself lift through the crease. Conversely, a nonpositive right-hand side is not asserted sufficient for membership in the convex hull of the cap vertices: its lower hull must also be respected.

Section8 supplies a true homogeneous E17 example with a strictly positive defect and an interior projected point.

## 5. Complete literal actual body

Use the cone over the seven section points

`b_j=(j+3/2,j^2,1), j=-3,-2,-1,0,1,2,3`,

and cut it by

`z-x/2<=1`, `z+x/2<=1`.

The complete raw vertices are

```
Y0=(0,0,0)
Y1=(-6/7,36/7,4/7)
Y2=(-2/5,16/5,4/5)
Y3=(2/5,4/5,4/5)
Y4=(6/7,0,4/7)
Y5=(10/9,4/9,4/9)
Y6=(14/11,16/11,4/11)
Y7=(18/13,36/13,4/13)
Y8=(0,5/2,1)
Y9=(0,9,1).
```

The seven raw lateral support normals, each with right-hand side0, are

```
n0=(-5,-1,3/2)
n1=(-3,-1,5/2)
n2=(-1,-1,3/2)
n3=(1,-1,-3/2)
n4=(3,-1,-13/2)
n5=(5,-1,-27/2)
n6=(0,1,-9).
```

The two caps have

`n7=(-1/2,0,1), n8=(1/2,0,1)`, both with right-hand side1.

The full outward maximal-facet cycles are

```
F0=(0,2,1)        F1=(0,3,8,2)       F2=(0,4,3)
F3=(0,5,4)        F4=(0,6,5)         F5=(0,7,6)
F6=(0,1,9,7)      F7=(1,2,8,9)       F8=(3,4,5,6,7,9,8).
```

Their seventeen TRUE edges are

```
01,02,03,04,05,06,07,12,19,28,34,38,45,56,67,79,89.
```

The degree sequence is7 followed by nine3s. The cap sizes are4 and7. The triangle089 is the internal interface, NOT a maximal facet of P. In particular08 and09 are not physical edges of the union.

All support equalities and nonincident strict inequalities follow directly from these rational inputs. Exhausting supporting triples gives exactly these nine maximal facets; the verifier includes that independent hull check. The full same-origin polar facet lattice is likewise checked against the ten primal vertex stars.

### Actual uniform centroid

The two pyramid six-volumes are

`D_minus=211/35`, `D_plus=617917/45045`.

Thus

`Vol(P)=444737/135135`.

The genuine volume centroid is

```
g=(908514460/4006635633,
   101062842791/32053085064,
   22793234341/40066356330).
```

These values can be recovered from the seven positive tetrahedra obtained by triangulating the two cap polygons and coning them to0. Explicitly, for each oriented cap triangle t=(i,j,k), put D_t=det(Yi,Yj,Yk); then

`6V=sum D_t`, `g=sum D_t(Yi+Yj+Yk)/(4 sum D_t)`.

A second apex fan is included in the verifier. No chosen vertex masses are used.

For mechanics set Xi=Yi-g ONCE. The actual poles are

`q_i=n_i/(h_i-n_i.g)`, where h_i=0 for i<=6 and h_7=h_8=1.

The polar is not independently centred.

The exact centroid satisfies the convenient strict rational box

```
226/1000 < gx < 227/1000,
3152/1000 < gy < 3154/1000,
568/1000 < gz < 570/1000.
```

## 6. A reciprocal family with complete global mechanics

Let

```
u=(12,-18,-1),
v=(-109,-71,-30),
w=(1,1,-6).
```

These vectors are pairwise orthogonal, with squared norms469,17822,38. Define

```
N_L=L^2 uu^T+L vv^T+ww^T,
M_L=uu^T/(469^2 L^2)+vv^T/(17822^2 L)+ww^T/38^2.
```

Then M_L,N_L are SPD and EXACT inverses for every L>0.

### Primal signs

The raw w-projections, in vertex order0 through9, are

`(0,6/7,-2,-18/5,-18/7,-10/9,6/11,30/13,-7/2,3)`.

The actual centroid box gives

`-42/1000 < w.g < -27/1000`.

Consequently every centred projection is nonzero. The positive projected vertices are0,1,6,7,9; the negative ones are2,3,4,5,8. The unique minimum is vertex3 and the unique maximum is vertex9.

The following eight TRUE escapes account for every nonroot vertex:

```
0->7, 1->9, 2->8, 4->3,
5->4, 6->7, 7->9, 8->3.
```

They are positive in the leading w-direction. Every outgoing arrow at3 and9 is negative in that direction.

More quantitatively, write

`L^2 D^primal_ij=a0+a1 L+a2 L^2`.

All raw vertex norms are<10 and the actual centroid norm is<4, so centred norms are<14 and edge lengths<20. The smallest absolute centred w-projection exceeds27/1000, and the smallest true-edge w-projection difference is1/10. Hence

`|a2|>1/1000000`, `|a1|<1`, `|a0|<1`.

These bounds make every primal sign equal to its leading sign for L>=2^41.

### Polar signs

Put p_i=q_i.u. The nine unnormalized numerators n_i.u are

`(-87/2,-41/2,9/2,63/2,121/2,183/2,-9,-7,5)`.

Substitution of the rational centroid box gives the strict total order

**`p7 < p0 < p1 < p6 < 0 < p2 < p3 < p5 < p4 < p8`.**

This order is obtained by cross-multiplying the positive actual support heights. For the eight neighboring comparisons in this displayed order, the conservative lower bound on the cross-multiplied numerator is at least121/400. The smallest case is

`7h0-(87/2)h7=(53/4)gx+7gy+33gz-87/2 >121/400`,

where here h_i denotes the actual height h_i(raw)-n_i.g. All actual heights lie between3/10 and10. Thus every distinct projected-pole difference exceeds1/1000 and every |p_i| exceeds9/20.

The seven noncap poles have genuine positive leading escapes

`0->7, 1->7, 6->7, 2->8, 3->8, 4->8, 5->8`.

Every outgoing arrow from either cap pole is strictly negative. Therefore the only stable primal facets in the leading metric are F7,F8.

For a true polar arrow write

`D^polar_ij=b0+b1 L+b2 L^2`.

The support normals have norm<15, actual heights>3/10, so pole norms are<50 and pole-edge lengths<100. Consequently

`|b2|>1/10000`, `|b1|<100000000`, `|b0|<200000`.

For L>=2^41>2*10^12 these inequalities fix every polar sign to its leading sign. They also imply that all three coefficients of each appropriately signed polynomial after L=2^41+t are strictly positive. The verifier reconstructs all204 coefficients exactly.

### Full result, including true saddles and weak contacts

The primal and polar leading signs together give

```
S={F7,F8},
U={vertex3,vertex9},
H={edge03,edge89}.
```

Every one of the68 true-edge primitives is nonzero for every L>=2^41. Therefore the family is strict222 with physical weak000 throughout that complete closed unbounded tail.

This proves complete global U and S conditions, not merely instability of one proposed apex. The degree-seven apex0 has a positive true escape0->7 and is not U. The two U roots cannot be combined into a single escape arborescence.

The metric conditioning is unbounded. This is not a hidden use of the candidate conditioning bound, nor is it an all-SPD theorem for this body.

## 7. What happens to the component pyramids

The negative-x component is the genuine quadrilateral pyramid with vertices0,1,2,8,9. Its actual volume is211/210 and its own volume centroid is

`g_minus=(-3277/14770,239319/59080,9439/14770)`.

Its w-projection is exactly `-65/11816`. Thus, in the same asymptotic physical metric, its unique minimum and maximum projected vertices are8 and9. They are strict U for all sufficiently large L. In the union, vertex8 has the new genuine escape8->3, and the U set is instead3,9.

This explicitly identifies a way in which a component's unstable vertex does not remain an unstable vertex of the union. The component is centred at g_minus; the union is centred at g. The same matrix is used, but the two homogeneous mechanics are not being evaluated at a fictitious shared centroid.

The positive component is the heptagonal pyramid over F8. Its actual volume is617917/270270. The actual negative-component volume fraction is

`lambda=271557/889474`.

The source reconstructs both component centroids and cap means and verifies

`g=(3/4)[lambda c_minus+(1-lambda)c_plus]`.

Both component pyramids are subject to their separately centred pyramid theorems. Those theorems do not give a stable true lateral facet of the union: the union's full physical S set is precisely the two caps. The triangular interface is not a facet of the union. Also gx>0, so the union's centroid is outside the negative-x component and cannot serve as an interior reference for both pieces.

No component equilibrium is imported into the union without recalculating its actual arrows.

## 8. An exact common-centroid reflection failure

Let Kcap=conv(Y1,...,Y9), and let

`cbar=lambda c_minus+(1-lambda)c_plus=4g/3`.

Take

`r=(3cbar-Y1)/2=2g-Y1/2`.

For the true positive cap ell_plus=z+x/2,

```
ell_plus(r)-1
 =2gz+gx-15/14
 =1304819373/4451817370
 >29/100.
```

Therefore `(3cbar-Kcap)/2` is NOT contained in Kcap—or even in P. This is a true uniform-volume counterexample to the proposed combined-cap half-reflection property.

The folded-roof frame for this body is

`u=(x,y-23z/4)`, `h(u)=1-|u1|/2`.

Its projected nonagon, in cyclic order1,2,8,3,4,5,6,7,9, is

```
(-6/7,13/7), (-2/5,-7/5), (0,-13/4),
(2/5,-19/5), (6/7,-23/7), (10/9,-19/9),
(14/11,-7/11), (18/13,1), (0,13/4).
```

The projection of r lies strictly inside this actual nonagon. For example, the centroid box puts it inside

`22/25 < u1 < 221/250`, `-59/50 < u2 < -23/20`,

and all four corners of that rectangle satisfy every projected edge inequality strictly. The source checks the exact reflected point and every true projected edge.

Thus the failure is specifically in lifting the planar geometry through the crease, not in claiming that an exterior projected point was interior. The source verifies the exact folded-roof volume, first moment and second-moment identities as well as the crease-defect formula.

## 9. Robustness, unresolved scope and continuation

All incidence inequalities, the projected-pole ordering, the leading primal signs, and the coefficient bounds used above are strict. Actual volume centroids and support heights depend continuously on the nondegenerate true two-cap chart. Consequently there is an open actual-realization neighborhood of this example, with the same labelled cap type, in which the same qualitative global222 tail and the reflection failure persist. No quantitative radius or coverage of the entire type is asserted.

The completed conclusions are therefore: a universal common-measure folded-roof reduction for genuine two-cap bodies; a robust actual failure of combined-cap half-reflection; and a complete reciprocal metric tail on an explicit homogeneous E17 body having no stable lateral facet and no unstable degree-seven apex.

What remains is the genuinely global question for arbitrary seven-ray/two-cap shapes and arbitrary common metrics. The present counterfamily is not110 and does not disprove a universal degree-seven110 exclusion. It does show that such an exclusion cannot be justified by simply retaining a lateral S or a particular U from the separately centred component pyramids, or by imposing the false half-reflection about their weighted cap mean.

The most useful continuation is to exploit the coupled area moments of the projected nonagon while retaining the two true seam-quadrilateral compatibility conditions and complete primal/dual escape information. Independent component centroids, a planar projection test alone, or a local heptagonal-pole argument discard information needed for that connection.

## 10. Complete standalone reference verifier

Save the following complete source as `two_cap_global.py` and run

```sh
python -B -S two_cap_global.py
```

It uses only the Python standard library and exact Fraction arithmetic. It reconstructs the true primal and polar lattices, two independent actual mass fans, the stated centroid, the reciprocal metric, all68 physical primitives, all204 positive shifted coefficients, the projected nonagon and the failed reflection. It also reconstructs the smaller component at its own centroid.

The expected mathematical markers are

```
TRUE_F_VECTOR 10 17 9
STRICT_S [7, 8]
STRICT_U [3, 9]
STRICT_H [(0, 3), (8, 9)]
ZERO_PRIMITIVES 0
POSITIVE_TAIL_COEFFICIENTS 204
TWO_CAP_FOLDED_ROOF_AND_GLOBAL_COUNTERCONTROL_PASS
```

The source and report hashes are computed by the script rather than supplied as an unobserved execution receipt. The exact analytical construction above does not depend on accepting a numerical solver's output.

```python
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json

Z = F(0)

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))
def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))
def scale(s,a):
    return tuple(s*x for x in a)
def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),Z)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def cross2(a,b):
    return a[0]*b[1]-a[1]*b[0]
def det(a,b,c):
    return dot(a,cross(b,c))
def mv(A,x):
    return tuple(dot(r,x) for r in A)
def trans(A):
    return tuple(zip(*A))
def mm(A,B):
    return tuple(tuple(dot(r,c) for c in trans(B)) for r in A)
def ident():
    return tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
def spd(A):
    p=(A[0][0],A[0][0]*A[1][1]-A[0][1]**2,det(*A))
    assert all(x>0 for x in p)
    return p

def support_sets(Y):
    out=set()
    for i,j,k in combinations(range(len(Y)),3):
        n=cross(sub(Y[j],Y[i]),sub(Y[k],Y[i]))
        if not any(n):
            continue
        vals=[dot(n,sub(y,Y[i])) for y in Y]
        if all(x<=0 for x in vals) or all(x>=0 for x in vals):
            out.add(frozenset(a for a,x in enumerate(vals) if x==0))
    return out

def planes(Y,faces):
    out=[]
    for f in faces:
        n=cross(sub(Y[f[1]],Y[f[0]]),sub(Y[f[2]],Y[f[0]]))
        assert any(n)
        h=dot(n,Y[f[0]])
        for i,y in enumerate(Y):
            assert dot(n,y)==h if i in f else dot(n,y)<h
        out.append((n,h))
    assert support_sets(Y)==set(map(frozenset,faces))
    return out

def moments(Y,faces,apex):
    V=Z
    J=[Z]*3
    T=[[Z]*3 for _ in range(3)]
    cells=[]
    for f in faces:
        for k in range(1,len(f)-1):
            t=(apex,Y[f[0]],Y[f[k]],Y[f[k+1]])
            v=det(sub(t[1],t[0]),sub(t[2],t[0]),sub(t[3],t[0]))/6
            assert v>=0
            if not v:
                continue
            s=tuple(sum(p[a] for p in t) for a in range(3))
            V+=v
            for a in range(3):
                J[a]+=v*s[a]/4
                for b in range(3):
                    T[a][b]+=v*(s[a]*s[b]+sum(p[a]*p[b] for p in t))/20
            cells.append((v,t))
    assert V>0
    return V,tuple(x/V for x in J),tuple(tuple(x/V for x in r) for r in T),cells

def incidence(faces,nv):
    ef={}
    nb=[set() for _ in range(nv)]
    fn=[set() for _ in faces]
    for k,f in enumerate(faces):
        for i,j in zip(f,f[1:]+f[:1]):
            ef.setdefault(tuple(sorted((i,j))),[]).append(k)
            nb[i].add(j)
            nb[j].add(i)
    assert all(len(x)==2 for x in ef.values())
    for a,b in ef.values():
        fn[a].add(b)
        fn[b].add(a)
    return ef,nb,fn

u=tuple(map(F,(12,-18,-1)))
v=tuple(map(F,(-109,-71,-30)))
w=tuple(map(F,(1,1,-6)))
vec=(u,v,w)
norm=(F(469),F(17822),F(38))
assert tuple(dot(x,x) for x in vec)==norm
assert all(dot(vec[i],vec[j])==0 for i in range(3) for j in range(i))
L0=2**41

def metric(L):
    L=F(L)
    N=tuple(tuple(L*L*u[i]*u[j]+L*v[i]*v[j]+w[i]*w[j]
                  for j in range(3)) for i in range(3))
    M=tuple(tuple(u[i]*u[j]/(norm[0]**2*L**2)
                  +v[i]*v[j]/(norm[1]**2*L)
                  +w[i]*w[j]/norm[2]**2
                  for j in range(3)) for i in range(3))
    assert mm(M,N)==ident()
    spd(M)
    spd(N)
    return M,N

def evaluate(Y,faces):
    pp=planes(Y,faces)
    V,g,T,fan=moments(Y,faces,Y[0])
    X=[sub(y,g) for y in Y]
    q=[scale(1/(h-dot(n,g)),n) for n,h in pp]
    assert all(h-dot(n,g)>0 for n,h in pp)
    stars={frozenset(k for k,f in enumerate(faces) if i in f)
           for i in range(len(Y))}
    assert support_sets(q)==stars
    ef,nb,fn=incidence(faces,len(Y))
    M,N=metric(L0)
    primal={}
    dual={}
    polynomial=[]
    shifted=[]
    records=[]
    for (i,j),(a,b) in sorted(ef.items()):
        values=[]
        for s,t in ((i,j),(j,i)):
            e=sub(X[t],X[s])
            c=tuple(dot(X[s],vec[k])*dot(e,vec[k])/norm[k]**2
                    for k in range(3))
            value=dot(X[s],mv(M,e))
            assert value*L0**2==c[0]+L0*c[1]+L0**2*c[2]
            primal[s,t]=value
            polynomial.append(('P',s,t,c))
            values.append(value)
        for s,t in ((a,b),(b,a)):
            e=sub(q[t],q[s])
            c=tuple(dot(q[s],vec[k])*dot(e,vec[k]) for k in (2,1,0))
            value=dot(q[s],mv(N,e))
            assert value==c[0]+L0*c[1]+L0**2*c[2]
            dual[s,t]=value
            polynomial.append(('Q',s,t,c))
            values.append(value)
        records.append((i,j,a,b,tuple(values)))
    for kind,i,j,c in polynomial:
        assert c[2]!=0
        sign=1 if c[2]>0 else -1
        sh=(sign*(c[0]+L0*c[1]+L0**2*c[2]),
            sign*(c[1]+2*L0*c[2]),sign*c[2])
        assert all(x>0 for x in sh)
        shifted.append((kind,i,j,sh))
    U=[i for i in range(len(Y)) if all(primal[i,j]<0 for j in nb[i])]
    S=[i for i in range(len(faces)) if all(dual[i,j]<0 for j in fn[i])]
    saddles=[(i,j) for i,j,a,b,p in records if all(x<0 for x in p)]
    weak_edges=[(i,j) for i,j,a,b,p in records
                if all(x<=0 for x in p) and any(x==0 for x in p)]
    zeros=sum(x==0 for i,j,a,b,p in records for x in p)
    return dict(vertices=Y,faces=faces,planes=pp,volume=V,centroid=g,
                raw_second=T,covariance=tuple(tuple(T[i][j]-g[i]*g[j]
                for j in range(3)) for i in range(3)),fan=fan,
                centred_vertices=X,poles=q,M=M,N=N,
                edges=sorted(ef),S=S,U=U,H=saddles,
                zero_primitives=zeros,weak_edges=weak_edges,
                primitives=records,polynomials=polynomial,
                shifted_coefficients=shifted)

Y=[(Z,Z,Z),
   (F(-6,7),F(36,7),F(4,7)),
   (F(-2,5),F(16,5),F(4,5)),
   (F(2,5),F(4,5),F(4,5)),
   (F(6,7),Z,F(4,7)),
   (F(10,9),F(4,9),F(4,9)),
   (F(14,11),F(16,11),F(4,11)),
   (F(18,13),F(36,13),F(4,13)),
   (Z,F(5,2),F(1)),(Z,F(9),F(1))]
faces=[(0,2,1),(0,3,8,2),(0,4,3),(0,5,4),(0,6,5),
       (0,7,6),(0,1,9,7),(1,2,8,9),(3,4,5,6,7,9,8)]
main=evaluate(Y,faces)
V,g,T=main['volume'],main['centroid'],main['raw_second']
assert V==F(444737,135135)
assert g==(F(908514460,4006635633),F(101062842791,32053085064),
           F(22793234341,40066356330))
assert moments(Y,faces,Y[4])[:3]==(V,g,T)
assert moments(main['centred_vertices'],faces,(Z,Z,Z))[1]==(Z,Z,Z)
assert len(main['edges'])==17 and len(Y)==10 and len(faces)==9
assert sorted(sum(i in e for e in main['edges']) for i in range(10))==[3]*9+[7]
assert main['S']==[7,8] and main['U']==[3,9]
assert main['H']==[(0,3),(8,9)]
assert main['zero_primitives']==0 and not main['weak_edges']
assert len(main['shifted_coefficients'])==68
box=((F(226,1000),F(227,1000)),(F(3152,1000),F(3154,1000)),
     (F(568,1000),F(570,1000)))
assert all(a<x<b for x,(a,b) in zip(g,box))
assert F(-42,1000)<dot(w,g)<F(-27,1000)
order=(7,0,1,6,2,3,5,4,8)
p=[dot(q,u) for q in main['poles']]
assert all(p[i]<p[j] for i,j in zip(order,order[1:]))

# The smaller actual component is centred separately, never at g.
ids=(0,1,2,8,9)
smallY=[Y[i] for i in ids]
smallF=[(0,2,1),(0,3,2),(0,1,4),(0,4,3),(1,2,3,4)]
small=evaluate(smallY,smallF)
assert small['volume']==F(211,210)
assert small['centroid']==(F(-3277,14770),F(239319,59080),F(9439,14770))
assert [ids[i] for i in small['U']]==[8,9]
assert small['S']==[3,4] and small['zero_primitives']==0
assert dot(w,small['centroid'])==F(-65,11816)
assert small['volume']/V==F(271557,889474)

# Actual folded-roof projection and all moments through degree two.
R=((F(1),Z,Z),(Z,F(1),F(-23,4)),(Z,Z,F(1)))
HY=[mv(R,y) for y in Y]
cyc=(1,2,8,3,4,5,6,7,9)
K=[HY[i][:2] for i in cyc]
for i,(a,b) in enumerate(zip(K,K[1:]+K[:1])):
    for j,c in enumerate(K):
        if j not in (i,(i+1)%len(K)):
            assert cross2(sub(b,a),sub(c,a))>0
assert all(h[2]==1-abs(h[0])/2 for h in HY[1:])
area=Z
J=[Z]*3
TT=[[Z]*3 for _ in range(3)]
for i,j in zip(cyc,cyc[1:]+cyc[:1]):
    ar=cross2(HY[i][:2],HY[j][:2])/2
    assert ar>0
    verts=((Z,Z,F(1)),HY[i],HY[j])
    su=tuple(sum(x[k] for x in verts) for k in range(3))
    area+=ar
    for a in range(3):
        J[a]+=ar*su[a]/3
        for b in range(3):
            TT[a][b]+=ar*(su[a]*su[b]+sum(x[a]*x[b] for x in verts))/12
mean=tuple(x/area for x in J)
second=tuple(tuple(x/area for x in row) for row in TT)
assert area/3==V
assert scale(F(3,4),mean)==mv(R,g)
assert tuple(tuple(F(3,5)*x for x in row) for row in second)==mm(mm(R,T),trans(R))
reflected=sub(scale(2,g),scale(F(1,2),Y[1]))
rr=mv(R,reflected)
for a,b in zip(K,K[1:]+K[:1]):
    assert cross2(sub(b,a),sub(rr[:2],a))>0
cap_gap=reflected[2]+reflected[0]/2-1
assert cap_gap==F(1304819373,4451817370)>F(29,100)
meanabs=2*(1-mean[2])
crease=(2*abs(rr[0])+abs(HY[1][0])-3*meanabs)/4
assert crease==rr[2]-(1-abs(rr[0])/2)==cap_gap

# Recover the remaining component moments directly from its actual facets.
plus_ids=(0,3,4,5,6,7,8,9)
plusY=[Y[i] for i in plus_ids]
plusF=[(0,1,6),(0,2,1),(0,3,2),(0,4,3),(0,5,4),
       (0,7,5),(0,6,7),(1,2,3,4,5,7,6)]
planes(plusY,plusF)
Vp,gp,Tp,fanp=moments(plusY,plusF,plusY[0])
assert Vp==F(617917,270270)
assert Vp+small['volume']==V
assert tuple((small['volume']*small['centroid'][i]+Vp*gp[i])/V
             for i in range(3))==g

report=dict(title='DEGREE7_TWO_CAP_FOLDED_ROOF_AND_GLOBAL_COUNTERCONTROL_V1',
            L0=L0,vectors=vec,norm_squares=norm,whole=main,
            smaller_component_indices=ids,smaller_component=small,
            larger_component_indices=plus_ids,
            larger_component=dict(vertices=plusY,faces=plusF,volume=Vp,
                                  centroid=gp,raw_second=Tp,fan=fanp),
            projection=K,projection_area=area,mean_lift=mean,
            second_lift=second,reflected_point=reflected,
            reflected_projection=rr[:2],cap_gap=cap_gap)

def encode(x):
    if isinstance(x,F):
        return str(x)
    if isinstance(x,dict):
        return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [encode(v) for v in x]
    return x

data=(json.dumps(encode(report),sort_keys=True,separators=(',',':'))+'\n').encode()
path=Path('two_cap_global.json')
path.write_bytes(data)
print('TRUE_F_VECTOR',len(Y),len(main['edges']),len(faces))
print('STRICT_S',main['S'])
print('STRICT_U',main['U'])
print('STRICT_H',main['H'])
print('ZERO_PRIMITIVES',main['zero_primitives'])
print('POSITIVE_TAIL_COEFFICIENTS',3*len(main['shifted_coefficients']))
print('TWO_CAP_FOLDED_ROOF_AND_GLOBAL_COUNTERCONTROL_PASS')
print('REPORT',len(data),hashlib.sha256(data).hexdigest())
source=Path(__file__).read_bytes()
print('SOURCE',len(source),hashlib.sha256(source).hexdigest())
```

The durable conclusion is the analytical folded-roof theorem and the explicitly proved rational global counterfamily. A broader all-SPD degree-seven exclusion is not being inferred from this verifier or from unconfirmed stress-cover exploration.
