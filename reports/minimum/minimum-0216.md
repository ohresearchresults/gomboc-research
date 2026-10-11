# minimum-0216

Historical AI scientific report · saved 2026-09-24 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# PYRAMID_HEPTAGON_ALL_ROOT_AREA_FAN_CAP_V1

## 1. Answer and scientific scope

**No: the constrained octagon in the assignment cannot have a sole strict radial maximum.** For every genuine convex heptagon B, its actual uniform area centroid c_B, and a=−3c_B, whenever Q=conv(a,B) has eight distinct true corners, Q has at least TWO strict radial-maximum corners under every positive-definite planar metric. Every possible root is covered, including a base root. Selected weak-arrow equalities are allowed.

The missing connection is not a sharper angular estimate. Actual base area supplies **eight simultaneous own-vertex-excluded coefficient rows, each of total mass3 and with EVERY coefficient at most1**. The notebook already contains a dimension-free eight-vector obstruction with the weaker cap7/6. Applying that accepted algebraic theorem to these actual area rows closes the constrained heptagon completely. This is a new transfer of accepted working mathematics, not an independent re-proof of that finite vector theorem. :contentReference[oaicite:0]{index=0}

The transfer also extends the supplied PSD/refinement and collar theorem from at most seven to **at most eight actual true vertices**. Consequently the finite heptagonal-cap horizon c_H=(2/7,0,−1) of the direct projective parent has an all-root/all-SPD U2 collar. Its width is not evaluated. The positive-projective interior, unbounded parameter directions and joint epsilon→0 remain separate questions.

No110 attainer, C34 exclusion, canonical incidence subtraction or changed global bound is claimed.

## 2. Authority and the exact inherited premise

The entire newly supplied journal, including the complete literal parent and its encoded source capsule, and the complete coordinator material were read through EOF. The direct parent is

```text
minimum-0215
SHA256 7e379625c02a74dacfba1f6db9e4e291a8c3e8eecc0e39c90cfd01b879c33242
POSITIVE_PROJECTIVE_TWO_CAP_AXIAL_ORBIT_AND_FINITE_HORIZONS_V1.
```

The new coordinator material is `[internal-source-reference]`, `SEVEN_SHADOW_PSD_REFINEMENT_AND_HORIZON_REDUCTION_V1`. It identifies precisely the actual eight-vertex pyramid core and the relation a+3c_B=0. :contentReference[oaicite:1]{index=1} Neither the mother's2023 stresses nor the earlier endpoint6 certificate was replayed or modified.

The additional **accepted shared premise**, stated explicitly in the supplied notebook, is the following finite-vector theorem:

> For at most eight distinct nonzero vectors v_i in a Euclidean space, a weak rooted escape tree cannot coexist with, for every i, a representation
>
> −v_i = sum_(j≠i) C_ij v_j,
> 0≤C_ij≤7/6, sum_(j≠i) C_ij=3.
>
> The statement is dimension-free, in particular it does not require rank3. All selected tree inequalities v_i·(v_parent−v_i)≥0 are weak.

Its recorded authority is

```text
minimum-0024
SHA256 b578a01ead261c6f7745122c22f4bb4767884e46ac46e1531b4e749a19332f95
NOVA24_F9_SYNTHESIS_AND_RECIPROCAL_ACTUAL_TRACE_V1.
```

The supplied notebook describes its complete115 rooted-type/5040-array coverage and1890 shifted-PD identities, and separately notes the primal cap1 consequence. :contentReference[oaicite:2]{index=2} I use that recorded theorem as an accepted premise. Its original finite certificate is not newly attached, reread or independently replayed here. In particular I do NOT substitute the physical conclusion F≥9 for the vector theorem, assume a uniform centroid of the polar, or require the physical Lambda identities. All new geometric steps below are proved explicitly; the new executable has no dependency on the old verifier.

## 3. Exact actual-area mechanism

Let the true vertices of B be b_0,…,b_6 in cyclic order, and let A=Area(B)>0. Fix a base vertex b_i. The five triangles

```text
T_(i,k)=conv(b_i,b_(i+k),b_(i+k+1)), k=1,…,5,
```

with indices modulo7, form a genuine positive-area triangulation of B. Define their actual area fractions

```text
w_(i,k)=Area(T_(i,k))/A>0,  sum_k w_(i,k)=1.
```

The exact uniform area-centroid identity is

```text
3c_B = sum_k w_(i,k)(b_i+b_(i+k)+b_(i+k+1)).       (1)
```

These are the areas of the same B, not selectable barycentric masses. No centroid of Q occurs.

### 3.1. A capped row excluding each base vertex

Since a=−3c_B, equation(1) gives

```text
−b_i = sum_k w_(i,k)(a+b_(i+k)+b_(i+k+1)).        (2)
```

Every summand is a sum of THREE DISTINCT vertices of Q, none equal to b_i. On collecting coefficients, the coefficient of a is1. Every other coefficient is a sum over a subset of the area fractions, hence lies in[0,1], and their total is3. This construction works for every i separately, with all seven triangulations integrating the identical actual body B.

### 3.2. A capped row excluding the apex

Use any one actual triangulation of B, for example the fan from b_0. Its centroid identity gives

```text
−a = 3c_B = sum_T [Area(T)/A](b_i+b_j+b_k).        (3)
```

Again each term uses three distinct OTHER vertices, and each collected coefficient is at most1.

Thus, for V with rows(a,b_0,…,b_6), there is an actual-area-generated matrix C satisfying

```text
C_ii=0,  0≤C_ij≤1,  C1=3·1,  CV=−V.             (4)
```

For the strictly convex heptagon all off-diagonal entries in this construction are positive. We only need nonnegativity. C is an **area-fan coefficient matrix**, not the physical facet-trace matrix Lambda. No claim about C², its spectrum, reciprocal facet centroids or surface flux is used.

Equivalently, every vertex satisfies the stronger-than-reflection condition

```text
−v_i ∈ conv{v_j+v_k+v_l : j,k,l distinct and different from i}.   (5)
```

Ordinary −Q/3 containment permits an arbitrary distribution of three units of coefficient mass, including repeated use of one vertex. Equation(5) permits at most one unit at each other vertex. That distinction resolves the present problem.

### 3.3. An actual solid interpretation, with no transported density

The same rows can be regarded as projected apex-fan rows of the genuine uniform pyramid

```text
P_B=conv({(a,3)} ∪ {(b_i,−1): i=0,…,6}).
```

Its volume is4A/3 and its actual volume centroid is

```text
((a+3c_B)/4, (3−3)/4)=0.
```

A fixed triangulation of the true base together with the seven true lateral triangles suffices for every apex fan. At a base apex, triangles lying in the base plane give zero-volume cells; the positive cells are exactly the area fan in(2). At the pyramid apex they give(3). Integration diagonals have not become mechanical edges. This supplies a common actual-body interpretation of ALL rows, while leaving the planar weak/singular-metric issue to the dimension-free vector theorem rather than an unjustified SPD lift.

## 4. All roots and every weak-arrow wall

Suppose Q had only one strict radial-maximum corner r. At every other true corner v there is an incident outgoing primitive that is nonnegative; otherwise v itself would be strict. Choose one such arrow at every nonroot. Along each chosen nonzero edge,

```text
|w|²−|v|² = 2v·(w−v)+|w−v|²>0.                 (6)
```

Hence there is no directed cycle. Every path ends at r, giving a weak rooted spanning tree on the eight vectors. But(4) supplies all the rows of the accepted cap theorem with cap1<7/6. Contradiction.

A global maximum-radius corner is always strict, including radius ties: for every different w of no greater radius,

```text
v·(w−v) = (|w|²−|v|²−|w−v|²)/2<0.
```

So failure of a sole root means at least two strict radial maxima, not merely failure of a prescribed root label. Equation(6) remains strict when a selected arrow is zero. Nothing in this argument assumes generic arrows or perturbs away an equality wall.

For a common planar SPD H, choose an invertible L with H=LᵀL. Actual area centroids obey c_(LB)=Lc_B, and the area fractions in(1) are unchanged because all areas scale by the same determinant. Thus La=−3c_(LB), and the Euclidean argument applies to LQ. The conclusion covers every such H, not just diagonal metrics or metrics close to the identity.

**The constrained-heptagon domain has no remaining root or shape sector.** The eight-vector limit is essential to this particular proof; the general problem with more than seven base corners is not claimed solved.

## 5. An independent elementary statement valid for any base-corner count

The actual area identity also proves a useful fact without the eight-vector premise: **the apex a can never be the sole strict radial maximum**, for any finite convex polygon B with a=−3c_B and a distinct from B's vertices.

Choose a maximum-norm base vertex b and write R=|b|, A0=|a|. From its actual area fan,

```text
(−a−b)/2 ∈ B,
```

so |a+b|²≤4R² and

```text
b·(a−b) ≤ (R²−A0²)/2.                           (7)
```

If R<A0, this is negative. If R>A0, Cauchy gives instead b·(a−b)≤R(A0−R)<0. If R=A0, distinctness of a,b gives b·(a−b)=−|a−b|²/2<0. For every other base point w, maximality of R similarly gives b·(w−b)<0. Thus b is a strict maximum of Q. The equality R=A0 is explicitly included.

This elementary statement handles the apex-root option but is not used to disguise the base-root problem. All base roots are excluded as sole roots by section4's capped-row theorem.

## 6. PSD/refinement strengthening and the heptagonal-horizon consequence

### 6.1. Every actual body with at most eight true vertices

Let K be a full-dimensional uniform convex3-polytope at its actual volume centroid, with at most eight true vertices. Let Z be any finite labelled set contained in K and including all its true vertices; labels may coincide or be nonextreme. For every nonzero PSD M, the complete weak-arrow graph on Z has at least two disjoint nonempty closed sets.

Here is a full reduction to the accepted premises. Write M=LᵀL.

At rank3, an actual positive tetrahedral fan from each true vertex x_i gives

```text
−Lx_i = sum_T w_T(Lx_j+Lx_k+Lx_l),
```

where j,k,l are distinct and different from i, w_T are actual volume fractions and sum_Tw_T=1. Thus the same cap1 condition holds. The projected true vertices are distinct and nonzero. If their complete weak graph had a unique sink, norm growth would yield a rooted weak tree, contrary to the accepted eight-vector theorem. Therefore it has at least two sinks.

At rank2, if LK has at most seven corners, use the supplied complete seven-corner theorem, since actual apex fans also give −K/3⊂K. If LK has eight corners, K has exactly eight true vertices and all project to distinct true corners; their projected actual tetrahedral rows again have cap1, so the eight-vector theorem applies. The complete seven-corner theorem is supplied in the new material, not an unfinished endpoint enumeration. :contentReference[oaicite:3]{index=3}

At rank1 the projected interval has a negative and a positive endpoint, since the actual centroid is interior. Both endpoint fibres are closed.

In each case a strict maximum point y of the projected convex hull has y·(z−y)<0 for every different hull point z: negative incident/tangent-cone directions extend by convexity. All labels projecting to y therefore form a nonempty closed set. Two distinct maxima give two disjoint sets, even with repeated labels. Collapsed internal edges cannot connect either set to a different projection. This proves the claimed refinement conclusion without assigning a physical equilibrium census to a singular matrix.

### 6.2. An all-metric collar for eight-vertex affine-normalized limits

Suppose actual uniform polytopes with a bounded finite number of labels admit invertible affine normalizations under which their labelled vertices converge to a bounded full-dimensional hull K with at most eight true vertices. Then every sufficiently nearby body has U≥2 for every SPD.

Otherwise take a U1 sequence. After transporting each metric by the affine normalization, normalize its trace to1 and pass to a nonzero PSD limit. There are only finitely many possible labelled rooted trees, so choose a subsequence with one fixed tree. The actual uniform centroids converge with the bounded full-dimensional convex bodies. Its selected arrows converge to weak arrows of the limit. The limiting labels include all true vertices of their hull; section6.1 contradicts this rooted tree. This proves existence of a collar, including arbitrarily ill-conditioned metrics, not a computed numerical width.

### 6.3. What changes for the exact projective mother

The parent's horizon normalizations can now use the eight-vertex rather than five- or seven-vertex limiting threshold. In the notation h_i=1+c·Y_i>0, n=−c*, the relevant complete normalizations are:

```text
Vertex horizon v:
 A_c=I+(h_v−1)v nᵀ;
 other limits=[Y_i−v(n·Y_i)]/[1−n·Y_i].

Facet horizon, maximal-area image triangle i1,i2,i3:
 A_c=diag(h_i1,h_i2,h_i3)[Y_i1 Y_i2 Y_i3]⁻¹.
```

The first limit is a pyramid with degree(v)+1 vertices, so degree≤7 now suffices. In the second, the three chosen facet vertices become e1,e2,e3; all other facet vertices have bounded barycentric coordinates, and all off-facet labels tend to0. A facet with at most seven corners therefore gives a full-dimensional limit with at most eight true vertices. Maximal-triangle ties and arbitrary relative denominator rates are handled by subsequences exactly as in the parent. Edge horizons remain the unrestricted-ratio tetrahedral case. :contentReference[oaicite:4]{index=4}

In particular **c_H=(2/7,0,−1), exposing the heptagonal cap, is no longer an unresolved finite horizon**. It now has an all-root/all-SPD U2 collar for every fixed0<epsilon≤5. No claim is made that the entire neighborhood has one unchanged singular root labelling.

A compact consequence strengthens the parent's denominator statement: for any epsilon0>0 and R<∞, there is a positive delta(epsilon0,R) such that any possible U1 parameter in

```text
epsilon∈[epsilon0,5], |c|≤R, all actual h_i>0
```

has min_i h_i≥delta. The old additional restriction staying a fixed distance from c_H can be dropped. A contrary sequence reaches a finite horizon at some positive epsilon limit, now excluded. This is an existence statement, not an evaluated bound. The mother's original finite-boundary description and former exception are literal in the parent. :contentReference[oaicite:5]{index=5}

The remaining mother-domain questions are the positive interior outside the accepted axial band, unbounded c, and joint epsilon→0. The new collar is not an all-orbit exclusion or a conclusion about S1 under an independently chosen polar metric.

## 7. Exact controls: genuine area centring versus a generic rooted octagon

### 7.1. Three new constrained controls, including a weak wall

Use the genuine counterclockwise heptagon

```text
B0=((0,−1),(0,1),(−1,1),(−2,1/2),(−5/2,0),(−2,−1/2),(−1,−1)).
Area(B0)=15/4,
integral_B0 (x,y)=(-89/24,0),
c_B0=(-89/90,0), a=(89/30,0).
```

For any real h apply the area-preserving shear S_h(x,y)=(x+hy,y) to B0. Its actual centroid and a remain unchanged. Let b_i(h)=S_hb_i and use the Q cyclic labels

```text
q0=a, (q1,…,q7)=(b1(h),b2(h),b3(h),b4(h),b5(h),b6(h),b0(h)).
```

This is a distinct calibration family, not a relabelled member of the projective mother. All eight corners and all supports remain genuine under the shear. The three exact audits give:

|h|Strict radial maxima of Q|Zero boundary primitives|D01|
|---|---|---|---|
|2|0,6|none|−2581/900|
|89/30|1,6|only0→1|0|
|119/30|1,6|none|89/30|

Thus apex-root and base-root possibilities are genuinely different, and the weak apex-escape wall still has two strict base maxima. Across the three controls47 boundary primitives are nonzero and one is zero. These are planar radial classifications, not physical3D weak-packet counts.

For all three, the actual area-fan matrix is C=(1/30) times

```text
[ 0,30, 2, 5,10,17,18, 8]
[30, 0, 2, 5,10,17,18, 8]
[30, 8, 0, 1, 6,13,16,16]
[30,18, 2, 0, 2, 6,10,22]
[30,24, 5, 1, 0, 1, 5,24]
[30,22,10, 6, 2, 0, 2,18]
[30,16,16,13, 6, 1, 0, 8]
[30, 8,18,17,10, 5, 2, 0].
```

The source regenerates this matrix from the seven complete actual area fans, not from a fitted solution of CV=−V. Each fan's area and first moment independently agree with the polygon shoelace formulas. The natural full-dimensional pyramid lift from section3.3 has actual volume5 and actual centroid0 in each case. No S/U/H census for those lifts is claimed, and none is offered as110.

### 7.2. Preserving the existing unrestricted octagon without misidentifying it

The notebook gives the following earlier rooted octagon, divided by10000:

```text
(10000,0),(5172,4975),(1849,5969),(−1122,5299),
(−3091,3496),(−3780,1265),(−3235,−763),(2462,−4283).
```

Its parent array is(0,0,1,2,3,4,5,0), all selected arrows are strict and0 is the sole strict radial maximum. This is an inherited control, not newly invented coordinates. The same notebook explicitly distinguishes its failed homogeneous lift. :contentReference[oaicite:6]{index=6}

The new exact audit verifies all16 nonzero boundary primitives, strict convexity,0 interior and all64 strict −Q/3 support tests. But with n=(7,5), every distinct triple from the other seven vertices satisfies

```text
n·(q0+qi+qj+qk) ≥2403/1250>0,
```

with the minimum at{5,6,7}. Hence −q0 is not in the capped triple-sum hull in(5). This reproduces the recorded fan-separation obstruction and identifies exactly which stronger necessary condition is absent; it is not a new unrestricted-octagon optimum.

For completeness the source also treats each of the eight vertices in turn as a proposed apex, computes the actual area centroid of the other seven, and verifies that every residual q_i+3c_(Q without q_i) has positive x-component. No choice of the apex repairs this particular polygon. Merely testing −Q/3 or a freely chosen capped mean would miss the actual area condition.

## 8. Status, recovery and remaining boundary

The constrained-heptagon theorem is complete **relative to the explicitly recorded accepted dimension-free capped-vector theorem**. It is not an independent reconstruction of that older theorem's1890 finite certificates. The new proof requires no old coefficient file, projective-grid weight or optimizer. It also explains why an ordinary full-rank U2 theorem alone would have been insufficient at a weak rank2 limit: the necessary input is the rank-independent vector obstruction.

The code below verifies the newly material actual geometry, all area/centroid identities and exact controls. It does not pretend that these finite controls prove the universal theorem. Author build, check and a separate source-only cold build were executed; report and stdout bytes matched. No independently authored verifier or proof-assistant formalization is claimed.

Observed environment: CPython3.13.5. Supported recovery: CPython≥3.11, standard library only, assertions enabled. Save the full source as `pyramid_heptagon_area_fan.py`, UTF-8/LF with its final LF, and run

```text
python -B -S pyramid_heptagon_area_fan.py build > build.out
python -B -S pyramid_heptagon_area_fan.py check > check.out
cmp build.out check.out
```

Exact pins:

```text
pyramid_heptagon_area_fan.py:8941 bytes
SHA256 4a7d0be56bbc98c3d15353187a9e6fdf9121ac6c1f6845c398d84a6b5779d596
pyramid_heptagon_area_fan.json:33314 bytes
SHA256 6a989eb3e866474746d9da2c4314e6d9f7562c862961260c57208df83016cf75
identical build/check stdout:337 bytes
SHA256 9efb489751d514420c609e4906614aee26c0f7727a12912e896d782a4d5f86f6
```

Terminal markers:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


The useful continuation is now the mother's noncompact projective tails or finite-distance positive interior, not another search over this constrained heptagon. No global bound or register is changed. Supplementary copies: [source](sandbox:/mnt/data/pyramid_heptagon_area_fan.py), [full bundle](sandbox:/mnt/data/PYRAMID_HEPTAGON_AREA_FAN_bundle.zip). The complete source follows and requires neither link.

### Complete runnable source

```python
#!/usr/bin/env python3
"""PYRAMID_HEPTAGON_ALL_ROOT_AREA_FAN_CAP_V1.
Exact new geometry and scope controls, not a replay of the accepted cap theorem.
CPython >=3.11, standard library only, assertions enabled.
python -B -S pyramid_heptagon_area_fan.py build|check
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json,sys
assert __debug__ and sys.version_info >= (3,11)
HERE=Path(__file__).resolve().parent
PARENT=('minimum-0215','7e379625c02a74dacfba1f6db9e4e291a8c3e8eecc0e39c90cfd01b879c33242')
CAP_PREMISE=('minimum-0024','b578a01ead261c6f7745122c22f4bb4767884e46ac46e1531b4e749a19332f95')
BASE=((0,-1),(0,1),(-1,1),(-2,F(1,2)),(F(-5,2),0),(-2,F(-1,2)),(-1,-1))
OCTAGON_NUM=((10000,0),(5172,4975),(1849,5969),(-1122,5299),(-3091,3496),(-3780,1265),(-3235,-763),(2462,-4283))

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(t,a):return tuple(t*x for x in a)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def summ(points):
    points=tuple(points)
    return tuple(sum(p[j] for p in points) for j in range(2))
def enc(v):
    if isinstance(v,F):return str(v)
    if isinstance(v,dict):return {str(k):enc(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [enc(x) for x in v]
    return v
def pin(b):return (len(b),hashlib.sha256(b).hexdigest())

def polygon(q,origin=False):
    q=tuple(tuple(map(F,p)) for p in q);n=len(q)
    assert n>=3 and len(set(q))==n
    e=tuple(sub(q[(i+1)%n],q[i]) for i in range(n))
    guards=tuple((i,j,det(e[i],sub(q[j],q[i]))) for i in range(n) for j in range(n) if j not in (i,(i+1)%n))
    assert all(z>0 for i,j,z in guards)
    cross=tuple(det(q[i],q[(i+1)%n]) for i in range(n));twice=sum(cross)
    assert twice>0
    centroid=tuple(sum(cross[i]*(q[i][j]+q[(i+1)%n][j]) for i in range(n))/(3*twice) for j in range(2))
    first=scale(twice/2,centroid)
    if origin:assert min(cross)>0
    return dict(vertices=q,edges=tuple((i,(i+1)%n) for i in range(n)),nonincident_supports=guards,area=twice/2,first_moment=first,centroid=centroid,origin_supports=cross)

def area_fan(B,r):
    n=len(B['vertices']);q=B['vertices'];cells=[];weights=[F(0)]*n
    total=F(0);moment=(F(0),F(0))
    for k in range(1,n-1):
        ids=(r,(r+k)%n,(r+k+1)%n)
        p0,p1,p2=(q[i] for i in ids)
        area=det(sub(p1,p0),sub(p2,p0))/2
        assert area>0
        mean=scale(F(1,3),summ((p0,p1,p2)))
        total+=area;moment=add(moment,scale(area,mean))
        w=area/B['area']
        for i in ids:weights[i]+=w
        cells.append(dict(indices=ids,area=area,area_fraction=w,centroid=mean))
    assert total==B['area'] and moment==B['first_moment']
    assert weights[r]==1 and sum(weights)==3 and all(0<w<=1 for w in weights)
    assert summ(scale(weights[i],q[i]) for i in range(n))==scale(3,B['centroid'])
    return dict(root=r,cells=cells,vertex_inclusion_fractions=tuple(weights))

def capped_matrix(Q):
    q=Q['vertices'];assert len(q)==8
    B=polygon(q[1:]);assert q[0]==scale(-3,B['centroid'])
    fans=tuple(area_fan(B,r) for r in range(7))
    rows=[(F(0),)+fans[0]['vertex_inclusion_fractions']];mixtures=[]
    apex_mix=[]
    for t in fans[0]['cells']:
        ids=tuple(i+1 for i in t['indices']);apex_mix.append((t['area_fraction'],ids))
    mixtures.append(tuple(apex_mix))
    for r,fan in enumerate(fans):
        row=[F(1)]+list(fan['vertex_inclusion_fractions']);row[r+1]=F(0);rows.append(tuple(row));mix=[]
        for t in fan['cells']:
            ids=(0,)+tuple(i+1 for i in t['indices'] if i!=r)
            assert len(ids)==len(set(ids))==3 and r+1 not in ids
            mix.append((t['area_fraction'],ids))
        mixtures.append(tuple(mix))
    rows=tuple(rows)
    for r,row in enumerate(rows):
        assert row[r]==0 and sum(row)==3 and all(0<row[i]<=1 for i in range(8) if i!=r)
        assert summ(scale(row[i],q[i]) for i in range(8))==scale(-1,q[r])
        assert sum(w for w,ids in mixtures[r])==1
        assert summ(scale(w,summ(q[i] for i in ids)) for w,ids in mixtures[r])==scale(-1,q[r])
    return dict(base=B,all_seven_actual_fans=fans,C=rows,root_excluded_triple_mixtures=tuple(mixtures),cap=F(1),row_sum=3)

def radial(Q):
    q=Q['vertices'];n=len(q)
    arrows=tuple((i,j,dot(q[i],sub(q[j],q[i]))) for i in range(n) for j in ((i-1)%n,(i+1)%n))
    roots=tuple(i for i in range(n) if all(z<0 for s,j,z in arrows if s==i))
    complete=tuple((i,j,dot(q[i],sub(q[j],q[i]))) for i in range(n) for j in range(n) if i!=j)
    sinks=tuple(i for i in range(n) if all(z<0 for s,j,z in complete if s==i))
    assert roots==sinks
    return dict(all_boundary_primitives=arrows,strict_radial_maxima=roots,all_distinct_pair_primitives=complete,zero_boundary_primitives=tuple((i,j) for i,j,z in arrows if z==0))

def pyramid_controls():
    raw=tuple(tuple(map(F,b)) for b in BASE);base=polygon(raw)
    assert base['area']==F(15,4) and base['centroid']==(F(-89,90),F(0))
    specs=(('APEX_AND_BASE_MAXIMA',F(2),(0,6),()),('APEX_WEAK_ESCAPE_WALL',F(89,30),(1,6),((0,1),)),('APEX_NOT_MAXIMUM',F(119,30),(1,6),()))
    out=[];previous=None
    for name,h,roots,zeros in specs:
        B=tuple((x+h*y,y) for x,y in raw);p=polygon(B)
        assert p['area']==base['area'] and p['centroid']==base['centroid']
        apex=scale(-3,p['centroid']);q=(apex,)+B[1:]+B[:1]
        Q=polygon(q,True);r=radial(Q);f=capped_matrix(Q)
        assert r['strict_radial_maxima']==roots and r['zero_boundary_primitives']==zeros
        if previous is not None:assert f['C']==previous
        previous=f['C']
        # Exact solid pyramid shape, not an equilibrium census:
        # base (b,-1), apex (a,3), volume=4*area/3, centroid=(a+3c,0)/4.
        solid_volume=4*p['area']/3
        solid_centroid=scale(F(1,4),add(apex,scale(3,p['centroid'])))+(F(0),)
        assert solid_volume==5 and solid_centroid==(0,0,0)
        out.append(dict(name=name,shear=h,apex=apex,Q=Q,radial=r,area_certificate=f,canonical_solid_lift_volume=solid_volume,canonical_solid_lift_centroid=solid_centroid,solid_equilibrium_census_claim=False))
    assert sum(len(p['radial']['zero_boundary_primitives']) for p in out)==1
    print('THREE_TRUE_PYRAMID_CENTROID_SHADOW_CONTROLS_47_NONZERO_ONE_WEAK_PASS')
    print('ALL_EIGHT_ROOT_EXCLUDED_ACTUAL_AREA_FAN_ROWS_CAP_ONE_PASS')
    return out

def unrestricted_control():
    q=tuple(tuple(F(x,10000) for x in p) for p in OCTAGON_NUM)
    Q=polygon(q,True);r=radial(Q)
    assert r['strict_radial_maxima']==(0,) and not r['zero_boundary_primitives']
    parents=(0,0,1,2,3,4,5,0)
    assert all(dot(q[i],sub(q[parents[i]],q[i]))>0 for i in range(1,8))
    margins=tuple((i,j,det(sub(q[(i+1)%8],q[i]),sub(scale(F(-1,3),q[j]),q[i]))) for i in range(8) for j in range(8))
    assert min(z for i,j,z in margins)>0
    direction=(F(7),F(5));triples=tuple((ids,dot(direction,add(q[0],summ(q[j] for j in ids)))) for ids in combinations(range(1,8),3))
    assert len(triples)==35 and min(z for ids,z in triples)==F(2403,1250)>0
    assert tuple(ids for ids,z in triples if z==F(2403,1250))==((5,6,7),)
    candidates=[]
    for i in range(8):
        B=polygon(tuple(q[j] for j in range(8) if j!=i))
        defect=add(q[i],scale(3,B['centroid']))
        assert defect[0]>0
        candidates.append(dict(apex_index=i,base_area=B['area'],base_first_moment=B['first_moment'],base_centroid=B['centroid'],apex_plus_three_base_centroid=defect))
    print('INHERITED_ROOTED_OCTAGON_PASSES_THIRD_BUT_FAILS_CAP_ONE_AND_ALL_APEX_CENTROIDS_PASS')
    return dict(name='INHERITED_UNRESTRICTED_ROOTED_OCTAGON',not_new_vertices=True,Q=Q,radial=r,parents=parents,third_support_margins=margins,root_zero_cap_separator_direction=direction,all_35_root_excluded_triple_tests=triples,separation=F(2403,1250),all_eight_candidate_apex_centroid_tests=candidates)

def main():
    assert sys.argv[1:] in (['build'],['check'])
    controls=pyramid_controls();counter=unrestricted_control()
    out=dict(identity='PYRAMID_HEPTAGON_ALL_ROOT_AREA_FAN_CAP_V1',parent=PARENT,accepted_cap_premise=CAP_PREMISE,material='[internal-source-reference]',source_pin=pin(Path(__file__).read_bytes()),controls=controls,unrestricted_scope_control=counter,scope='The universal proof applies the recorded accepted dimension-free eight-vector cap theorem. This source verifies actual area moments, all-root capped rows, true planar supports and exact scope controls; it does not replay that prior theorem, compute a collar width, or claim a110 attainer.')
    data=(json.dumps(enc(out),sort_keys=True,separators=(',',':'))+'\n').encode()
    p=HERE/'pyramid_heptagon_area_fan.json'
    if sys.argv[1]=='check' or p.exists():assert p.read_bytes()==data
    else:p.write_bytes(data)
    print('PYRAMID_HEPTAGON_AREA_FAN_TRANSFER_EXACT_CONTROLS_PASS',*pin(data))
if __name__=='__main__':main()
```
