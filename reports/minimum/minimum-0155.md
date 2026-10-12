# minimum-0155

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# ONE_ZERO_ENDPOINT_PRESERVING_OVERSHOOT_ERASURE_V1

## 1. Main findings

The genuine height-overshoot complement admits an endpoint-preserving, actual-body reduction that does not assume CH, parallel section boundaries, axis intercepts, or a prescribed volume profile.

Let P be a canonical one-zero body, with a=1, 0<b<1, c=0, d>=0. For ANY H>=max(1,d), put Q=P intersect {ell<=H}. If P has positive volume above H, then

    T(P)<max(T(Q),2).

More precisely, the explicit coupled bound in Section 4 retains the removed cap's own volume and ell-first moment. In particular,

    T(P)>=2  implies  T(Q)>T(P).

Therefore, for 0<d<=1, every possible high-trace violation can be clipped to max ell=ell(A)=1 with strict trace improvement. This operation preserves genuine maximal ABC and ABD whenever the input has them. It is not an equilibrium-preserving operation, and it need not preserve the vertex count.

Two whole-class value consequences are proved:

* If the actual clipped body Q at H=1 belongs to the parent's closed CH or NF class, then T(P)<203/100, with no restriction on the geometry or height of the actual convex cap above it.
* For arbitrary geometry, including proper33, if the cap above H>=max(1,d) has volume at least one twelfth of the retained body's volume, then

      T(P)<132/65<51/25,
      51/25-132/65=3/325.

  A sharper parameter-dependent inequality and a larger closed polynomial sector are given below.

The unconditional strengthening T(P)<=T(Q) is false. A new exact proper33 body with a genuine triangular root has T(P)=231751233675/324704481079, while its endpoint-preserving height clip has the smaller trace 872387245448215146/1222566702767563343. Both traces are below 1. This does not contradict the proved high-trace reduction.

Twelve exact actual bodies are retained: two NF cores, their non-CH caps, their proper resolutions and proper height clips, the unconditional-deletion counterexample and its clip, and a d>1 control and its correctly placed clip. Every body's uniform centroid, maximal facets, true edges and complete edge primitives were recomputed. None is 110 or an E17 attainer.

The parent explicitly left maxell>A and missing-axis geometry outside its completed NF/CH theorem; the new reduction addresses that complement rather than reopening arbitrary-U NF.

## 2. Source authority and evidence status

The entire new journal, including the complete literal required parent, was read through EOF. Unchanged earlier evidence was retained. The supplied NF source, report and receipt were also accessible; no archive object was inferred from an identifier or a historical path.

New journal:

    research-journal(20260921-090356).md
    294677 bytes
    SHA256 6cf10511934ee2dfcd2cba6af26d08761f5b42e711f8c87eb9867d32efa21606

Required parent:

    minimum-0153
    SHA256 377e6ad8854d4bde291d42a305453375447abb5c20136e2af074ded04d492714

The identity was authenticated: extract the parent from its title through EOF, retain one final LF, and compactly serialize the version-2 envelope with ensure_ascii=False and separators=(',',':'). This produces 37703 bytes and exactly the required SHA-256. The embedded 16768-byte nf_full_certificate.py also matches the supplied source. No parent identity or mathematical-scope conflict was found.

The continuous cap theorem below has an elementary analytic proof. The new exact controls were executed normally and then from the sole new source file in a clean directory, producing byte-identical reports and receipts. This is not a proof-assistant formalization. The already accepted NF polynomial certificate was not rerun or re-solved in this continuation.

## 3. Coordinates, marks and the one-point volume identity

Use the original physical coordinates

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    T0=conv(A,B,C,D) subset P subset {x,y>=0},
    alpha=1-b, h=1+b, q=h+d,
    ell=1+(d-1)x-y-alpha z >=0,
    n=h x+q y.

All bodies are compact, convex and full-dimensional. The root is required to be a genuine two-dimensional face when asserting the original root-facet problem; the analytic inequality itself does not need that additional condition.

The physical uniform moments are

    V=int_P 1, X=int_P x, Y=int_P y, Z=int_P z,
    E=int_P ell, N=int_P n, T=N/(6VE),
    g_P=(X,Y,Z)/V.

In level coordinates (x,y,w), w=ell,

    z=[1+(d-1)x-y-w]/alpha,
    A=(0,0,1), B=(0,0,b), C=(0,1,0), D=(1,0,d).

The inverse coordinate map has constant absolute Jacobian 1/alpha. No section is assigned a new density or an independently chosen centroid.

For every r=(x,y,z) with x,y>=0, the exact physical volume of the one-point tetrahedral extension is

    6 Vol(conv(T0,r))
      =1+(-z)_+ +(x+y+z-1)_+.                         (3.1)

Indeed only the faces z=0 and x+y+z=1 can be visible from r. Their actual exterior pyramids have disjoint interiors and the displayed volumes. The coordinate faces cannot be visible because x,y>=0. The formula includes coplanar and interior-point cases.

Consequently, if r belongs to a body Q containing T0 and t=6 Vol(Q), then

    x+y<=t, z>=1-t.                                   (3.2)

These two restrictions come from one actual volume, not two unrelated fitted constraints.

## 4. The actual cap inequality and trace domination

Fix H>=max(1,d). Write

    Q=P intersect {w<=H}, R=P intersect {w>H},
    v=V(Q), e=E(Q), W=V(R), F=E(R),
    t=6v.

Use the closure of R for a polyhedral integration fan; its boundary at w=H has zero volume. Assume W>0. Then F>HW.

For a point r at height H, write s=x+y. The exact affine identity is

    n=(b+d)s+1-H-alpha z.

Apply (3.2) to this same point in Q. Since b+d>=0,

    n(r)<=B_H(t):=(1+d)t+b-H.                          (4.1)

Now let p be ANY point of R, of height w>H. Project from the retained zero endpoint C:

    r=C+(H/w)(p-C).

This is a point of Q at height H, by actual convexity. Since n(C)=q,

    n(p)=q+(w/H)(n(r)-q)
         <=a_H(t) w+q,
    a_H(t)=[(1+d)t-(1+d+H)]/H.                        (4.2)

The coefficient a_H may be negative. No sign assumption on it is made.

Integrating (4.2) over the SAME physical cap gives

    N_R<=a_H F+qW < [B_H(t)/H]F=6v gamma_H F,
    gamma_H=B_H(t)/(Ht)
            =(1+d)/H+(b-H)/(Ht)<2.                    (4.3)

The strict step uses F>HW and q>0. Nonempty cap geometry also forces B_H>0. The bound is valid for arbitrarily changing upper normals, sections missing both axes, and nonpolyhedral convex caps.

Every physical moment is split without substitution:

    V_P=v+W, E_P=e+F, N_P=N_Q+N_R,
    X_P=X_Q+X_R, Y_P=Y_Q+Y_R, Z_P=Z_Q+Z_R,
    Z_R=[W+(d-1)X_R-Y_R-F]/alpha.                      (4.4)

In particular the centroid after clipping is the new g_Q, not the old centroid of P. Combining (4.3) and (4.4) yields the stronger trace inequality

    T(P)< [v/(v+W)] [T(Q)e+gamma_H F]/(e+F).           (4.5)

Thus T(P)<max(T(Q),2). If T(P)>=2, (4.5) forces T(Q)>T(P). If W=0, Q=P and the trace is unchanged.

### A sharper section bound for d<1

When 0<=d<1 and H>=1, every point at height H has

    z=-[H-1+(1-d)x+y]/alpha.

The same one-point volume inequality therefore gives

    (1-d)x+y<=alpha t+b-H.

Since q(1-d)=h-d(b+d)<=h,

    n(r)<= h[alpha t+b-H]/(1-d).

Hence B_H in every cap inequality can be replaced by

    Bhat_H=min((1+d)t+b-H, h[alpha t+b-H]/(1-d)).      (4.6)

The exact source audits this stronger version as well. At H=1 it gives

    gammahat_1 < G(b,d),
    G(b,d)=min(1+d,(1-b^2)/(1-d)),  0<=d<1.

Therefore T(P)<max(T(Q),G(b,d)) in this parameter range. The simpler universal cutoff 2 remains valid at d=1 and in the general H>=max(1,d) theorem.

## 5. Canonical retention, endpoint boundaries and scope of the reduction

The operation is a literal intersection with a closed halfspace. All four marked values are <=H, so T0 remains inside Q. Neither ell nor n is changed. The root P intersect {ell=0} is unchanged, including its area and boundary.

If P has genuine maximal facets ABC and ABD, then

    Q intersect {x=0}=ABC,
    Q intersect {y=0}=ABD.

Containment in the corresponding old facets gives one inclusion; retention of their three marked vertices gives the other. Their common edge AB is unchanged. This remains true when H=1 passes through A, when d=1 puts D on the clipping plane, and when H=d>1 passes through D. No interior variation or free root rotation is required at these boundaries.

Thus, for every fixed 0<b<1 and 0<d<=1, the high-trace proper33 problem reduces to maxell=A. The same statement holds for the broader marked-face problem. For d>1, the theorem removes only w>d; the interval 1<w<=d is not erased because clipping it would delete D.

This is trace domination, not preservation of mechanical equilibria. A clip can introduce a new maximal facet, change true edges, increase the number of vertices, and change strict S/U/H at the body's new centroid. In the exact high-trace controls below, a proper clip changes 4/4/6 to 4/5/7 while preserving ABC and ABD. No transfer to a fixed thirteen-vertex or E17 incidence class is asserted.

There is no uniform positive gap between T(Q) and T(P) for every nonempty cap. The cap can tend to zero. The strict inequalities at a fixed positive cap and the limiting identity at zero cap have been kept distinct.

## 6. An arbitrary-geometry whole-class value sector

A quantitative core-mean bound retains the marked tetrahedron explicitly:

    e<=3Hv/4 -(3H-h-d)/24.                            (6.1)

To prove it, use a genuine volume fan from C, where w(C)=0. Triangulate the true coordinate face y=0 so that the marked triangle ABD is a reserved patch, subdividing surrounding face regions as necessary. Its cone from C is exactly T0, of volume 1/6 and mean w=(h+d)/4. Every other fan tetrahedron has mean w<=3H/4. Summing the actual positive cone volumes gives (6.1). Flat fan cells cause no problem. For compact convex bodies, inscribed polyhedral approximation retaining T0 gives the same closed inequality. Integration nodes used for the reserved patch are not declared mechanical vertices or true edges.

Put

    s=W/v,
    k=3/4-(3H-h-d)/(4Ht).

Then 0<e/(Hv)<=k<3/4.

The other premise is the accepted individual boundary-trace cap c3<10/9. It applies to each true coordinate facet with the nonnegative weight ell. The marked triangle contributes no more than its containing facet because ell>=0. Thus, even without proper33,

    hX_Q/(6ve)<=c3,
    qY_Q/(6ve)<=c3,
    T(Q)<=2c3<20/9.                                  (6.2)

This uses true whole-facet integrals, not an identification of a marked triangle with a larger facet. The precise inherited boundary theorem and its uniform localization proof are supplied in the journal.

Since 20/9>gamma_H, the right side of (4.5) increases with the core mean e and decreases with F. Using (6.1) and F>=HW gives the actual-body bound

    T(P)< Phi(t,b,d,H,s)
         =[(20/9)k+gamma_H s]/[(1+s)(k+s)].            (6.3)

The sharper gammahat_H from (4.6) can replace gamma_H. Formula (6.3) is a whole-class test using the same body's core and cap volumes. No independent area or section-centroid parameters occur.

A convenient uniform overbound is

    T(P)< [5/3+2s]/[(1+s)(3/4+s)].                    (6.4)

Its right side decreases for s>=0. The exact identity

    (51/25)(1+s)(3/4+s)-(5/3+2s)
      =(612s^2+471s-41)/300

therefore closes the ENTIRE sector

    612s^2+471s-41>=0.

In particular W>=v/12 gives

    T(P)<132/65<51/25,
    51/25-132/65=3/325.

Equivalently, this simple sufficient condition is that at least one thirteenth of the total volume lies above the largest marked endpoint value. It applies to arbitrary actual upper geometry and to proper33. It is not asserted necessary: (6.3) is stronger, and many smaller caps are also excluded by it.

## 7. Whole NF/CH-core extension and proper resolutions

For 0<d<=1 and H=1, suppose the ACTUAL truncation Q belongs to the accepted NF class:

    0<=w<=1, x,y>=0,
    u x+y<=U(w),
    h x+q y+(m/b)w>=m,
    U concave and nonnegative, U(0)=1, u=U(d)>0,
    h/u<=q, 0<=m<=q.

The parent proves T(Q)<203/100 for this whole class. It also proves the same cap for CH through its actual-body domination. These are the inherited value premises, not newly assumed properties of an arbitrary clipped body.

Equation (4.5) immediately gives

    T(P)<203/100

for EVERY actual convex extension above such a core. The cap may have arbitrarily many faces, changing supporting normals, or sections missing both axes. There is no small-overshoot or small-aspect restriction. For example, with U identically 1, an apex (1/4,1/3,L) in level coordinates is beyond only the top plane for every L>1; its convex hull with the NF core supplies genuine missing-axis caps of arbitrarily large height.

For positive-root inputs in this new class, take q0 in the relative interior of the root with positive x,y and define

    P_lambda=conv(T0,lambda P+(1-lambda)q0), 0<lambda<1.

This is one actual body contained in P. Its contracted component has positive x,y, so its coordinate maximal facets are exactly ABC and ABD. The root remains two-dimensional. Since ell(q0)=0,

    V_lambda>=lambda^3 V,
    E_lambda>=lambda^4 E,
    N_lambda<=N,
    T(P_lambda)<=lambda^(-7)T(P).                     (7.1)

Thus all 9993/10000<=lambda<1 satisfy

    T(P_lambda)<20300/9951<51/25,
    51/25-20300/9951=1/248775.

This is a proved proper33 value family outside CH, not a claim that every proper body is such a resolution. An overshoot remains when lambda maxell(P)>1. The exact controls satisfy this strict condition. Properization can increase trace; it is not being treated as monotone.

## 8. Exact physical controls and useful failures

All coordinates in this section are level coordinates unless explicitly called physical. Convert them with z=[1+(d-1)x-y-w]/(1-b). The recovery source computes V,X,Y,Z,E,N and the actual physical centroid independently for every body and every clip.

### 8.1. Two high-trace non-CH caps and their proper resolutions

Set eps=d=1/1000. Use each of the two exact parameter pairs

    (b,rho)=(1/5,4/5), (3/5,31/32),
    h=1+b, q=h+d, m=h rho.

The core Q is exactly

    x,y,w>=0, w<=1,
    x+y<=1, x+y+w<=1+d,
    h x+q y+(m/b)w>=m.

It is an NF body with U(w)=min(1,1+d-w), u=1. Add the off-axis apex

    p=(eps/4,eps/3,1+eps/4), P=conv(Q,p).

The apex satisfies every old halfspace strictly except w<=1. Hence Q is exactly the clip at w=1; the added region is the pyramid over the top triangle with vertices (0,0,1),(eps,0,1),(0,eps,1).

Its exact physical cap volume and level-coordinate centroid are

    W=eps^3/[24(1-b)],
    g_cap_level=(5eps/16,eps/3,1+eps/16).

The full cap moments follow by the displayed affine coordinate map. They are also independently integrated from the actual re-hulled cap. At w=1+eps/8 its actual section has min x=eps/8 and min y=eps/6, so it misses both axes. More generally all its nondegenerate sections strictly above 1 miss both axes. These full bodies are not CH.

For both pairs, form the proper resolution with

    lambda=9999/10000,
    q0=(99/200,99/200,0).

The point q0 is strictly inside the root. The actual maximum height is

    lambda(1+eps/4)=40005999/40000000>1.

The common exact geometric/mechanical counts for the two parameter pairs are:

| Actual body | Vertices / edges / maximal facets | Strict S/U/H | Physical weak points |
|---|---:|---:|---:|
| NF core | 10 / 15 / 7 | 4 / 5 / 7 | 0 |
| Non-CH capped body | 11 / 18 / 9 | 4 / 4 / 6 | 0 |
| Proper capped body | 11 / 25 / 16 | 4 / 4 / 6 | 0 |
| Height clip of proper body | 12 / 27 / 17 | 4 / 5 / 7 | 0 |

The core and nonproper capped body have coordinate maximal facets of sizes 6/6. Both proper bodies have exactly 3/3. All four primitives on every true edge are nonzero in all eight bodies.

For b=1/5, the core and capped traces are respectively approximately 2.022870717749339 and 2.022870715104570. The proper capped trace is exactly

    16150314516751947210960410988691307353600000000000000000
    /7983834681774205747424870641654572594114393569793162621,

approximately 2.0228768706371745. Its height clip has the larger trace approximately 2.0228768715244696.

For b=3/5, the capped trace is approximately 2.003324555494442. Its proper resolution is approximately 2.003333907994092 and its proper height clip is approximately 2.003333909383935. This pair also shows the construction outside the older b<=1/2 low-endpoint sector. Neither parameter pair is a record or a mechanical attainer.

These controls demonstrate both directions that must be distinguished: removing the positive cap improves trace above 2, while properization increases trace here. The new clip changes mechanical counts even though it retains the required two maximal triangles.

### 8.2. Exact failure of unconditional height-deletion monotonicity

Take b=7/20,d=9/10. In ORIGINAL PHYSICAL coordinates the complete seven-point input is

    (0,0,0), (0,0,1), (0,1,0), (1,0,0),
    (1/50,49/50,9/325),
    (1/50,51/50,-11/325),
    (4,4,-177/26).

Its actual maximal coordinate facets are ABC and ABD. Its root is the triangle consisting of C and the next two listed root points. The last vertex has ell=41/40. Its actual f-vector is 7/15/10, strict S/U/H=3/2/3, weak000.

Its exact original moments are

    V=65879/48750,
    X=59206757/39000000,
    Y=158809/104000,
    Z=-248684291/126750000,
    E=4928801/5200000,
    N=54852363/10000000,
    g=(59206757/52703200,2382135/2108128,-248684291/171285400).

The height clip Q=P intersect {ell<=1} is a genuine 11/20/11 proper33 body with the same root, strict 3/2/3 and weak000. Its own moments, not the old centroid, give

    T(P)=231751233675/324704481079,
    T(Q)=872387245448215146/1222566702767563343,
    T(P)-T(Q)
      =1072775985744707886083949/6728354013671282854950465883>0.

Thus an endpoint-preserving height cut can lower trace. Both values are below 1; this defeats only the unconditional strengthening, not the proved high-trace result. It is a different operator and a different control from the older false monotonicity for clipping x+y>1.

### 8.3. Retained d>1 boundary control

Use b=1/3,d=3/2 and the level-coordinate hull of the four canonical marks with

    (1/50,49/50,0), (1/50,51/50,0), (2,3,2).

The correct retained-endpoint clip is H=d=3/2, not H=1. The original is proper 7/15/10 with T=1645548100/2921051729. Its clip is proper 10/19/11 with T=2348722096000/3972028095143. Both have strict 3/2/3 and weak000. The source verifies all cap-restoration identities in this genuinely different endpoint ordering as well.

## 9. Complete deterministic recovery capsule

Save the following complete unit as one_zero_cap.py, UTF-8/LF with one final LF, and run with assertions enabled:

    python -S one_zero_cap.py > one_zero_cap_receipt.txt

Tested environment: CPython 3.13.5, standard library only. There are no external inputs, seeds, numerical hull dependencies or parent-code imports.

Observed normal and clean-directory replay pins:

    one_zero_cap.py: 14361 bytes
    SHA256 171842c7740f6d32efc95f6a451e18ed570951b64f7496966d4b61c608cf10ec
    one_zero_cap.json: 146052 bytes
    SHA256 9f8a8f0178f63d44685d4861ab8d737d63ee056b56250c3f0b05e468df107345
    one_zero_cap_receipt.txt: 1584 bytes
    SHA256 eb9b310d1f6e6bed7c1c4c28f26fec0fe120980a91c4cb0c239759379e2841a5

Expected terminal marker:

    ONE_ZERO_ENDPOINT_PRESERVING_OVERSHOOT_ERASURE_EXACT_PASS

The source reconstructs every maximal facet and true edge from supporting triples; all six physical moments are checked through three different volume fans. The two NF-core moment sets have an independent exact section integration. Each actual cap is re-hulled and integrated separately, and all V,X,Y,Z,E,N restoration identities are verified. The report retains every edge packet and projected canonical one-point hull, not only rounded traces or a count.

```python
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json

# CPython 3.13.5, standard library only, assertions enabled. No random/external input.
PARENT = 'minimum-0153'
PARENT_SHA256 = '377e6ad8854d4bde291d42a305453375447abb5c20136e2af074ded04d492714'
KEYS = ('V','X','Y','Z','E','N')

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def average(v): return tuple(sum(p[j] for p in v)/len(v) for j in range(3))
def ratrow(row): return tuple(F(x) for x in row)

def solve3(rows,rhs):
    d=det(*rows)
    if not d: return None
    return tuple(det(*(tuple(rhs[i] if k==j else rows[i][k] for k in range(3))
                      for i in range(3)))/d for j in range(3))

def from_halfspaces(H):
    P=set()
    for ids in combinations(range(len(H)),3):
        p=solve3([H[i][0] for i in ids],[H[i][1] for i in ids])
        if p is not None and all(dot(n,p)<=s for n,s in H): P.add(p)
    assert len(P)>=4
    return sorted(P)

def cycle(P,ids,n):
    drop=next(j for j in range(3) if n[j])
    keep=[j for j in range(3) if j!=drop]
    Q=sorted((P[i][keep[0]],P[i][keep[1]],i) for i in ids)
    def turn(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[]
    for p in Q:
        while len(lo)>=2 and turn(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(Q):
        while len(hi)>=2 and turn(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    return tuple(p[2] for p in lo[:-1]+hi[:-1])

def hull(candidates):
    Q=sorted(set(candidates)); raw={}
    for i,j,k in combinations(range(len(Q)),3):
        n=cross(sub(Q[j],Q[i]),sub(Q[k],Q[i]))
        if n==(0,0,0): continue
        s=dot(n,Q[i]); vals=[dot(n,p)-s for p in Q]
        if all(v<=0 for v in vals): pass
        elif all(v>=0 for v in vals): n=mul(-1,n); s=-s; vals=[-v for v in vals]
        else: continue
        ids=tuple(i for i,v in enumerate(vals) if v==0)
        raw[ids]=(n,s)
    extreme=set()
    for ids,(n,s) in raw.items(): extreme.update(cycle(Q,ids,n))
    P=[Q[i] for i in sorted(extreme)]
    index={p:i for i,p in enumerate(P)}; ff={}
    for ids,(n,s) in raw.items():
        face=tuple(sorted(index[Q[i]] for i in cycle(Q,ids,n)))
        ff[face]=(n,s)
    faces=[]; planes=[]
    for ids,(n,s) in sorted(ff.items()):
        f=cycle(P,ids,n)
        faces.append(f); planes.append((n,s))
    edges={}
    for f_id,f in enumerate(faces):
        for i in range(len(f)):
            edge=tuple(sorted((f[i],f[(i+1)%len(f)])))
            edges.setdefault(edge,[]).append(f_id)
    assert all(len(v)==2 for v in edges.values())
    assert len(P)-len(edges)+len(faces)==2
    for p in P:
        active=[n for n,s in planes if dot(n,p)==s]
        assert any(det(*triple)!=0 for triple in combinations(active,3))
    return P,faces,planes,edges

def moments(P,faces,o):
    V=F(0); J=(F(0),)*3
    for f in faces:
        a=P[f[0]]
        for i in range(1,len(f)-1):
            b,c=P[f[i]],P[f[i+1]]
            v=abs(det(sub(a,o),sub(b,o),sub(c,o)))/6
            V+=v
            J=add(J,mul(v/4,add(add(o,a),add(b,c))))
    return V,J

def world(p,b,d):
    x,y,w=p
    return x,y,(1+(d-1)*x-y-w)/(1-b)

def audit(K,b,d,proper):
    P,faces,planes,edges=hull([world(p,b,d) for p in K])
    V,J=moments(P,faces,average(P))
    for o in [P[0],P[-1]]: assert moments(P,faces,o)==(V,J)
    g=mul(1/V,J); X=[sub(p,g) for p in P]
    assert all(s-dot(n,g)>0 for n,s in planes)
    Q=[mul(1/(s-dot(n,g)),n) for n,s in planes]
    E=V+(d-1)*J[0]-J[1]-(1-b)*J[2]
    N=(1+b)*J[0]+(1+b+d)*J[1]
    T=N/(6*V*E)
    ell=lambda p: 1+(d-1)*p[0]-p[1]-(1-b)*p[2]
    assert min(map(ell,P))==0 and max(map(ell,P))>=1
    canonical=[ratrow(r) for r in [(0,0,0),(0,0,1),(0,1,0),(1,0,0)]]
    assert all(all(dot(n,p)<=s for n,s in planes) for p in canonical)
    root=[i for i,p in enumerate(P) if ell(p)==0]
    assert any(set(f)==set(root) for f in faces)
    coord=[]
    for j in [0,1]:
        ids=[i for i,p in enumerate(P) if p[j]==0]
        assert any(set(f)==set(ids) for f in faces)
        coord.append(ids)
    if proper:
        assert {P[i] for i in coord[0]}=={canonical[i] for i in [0,1,2]}
        assert {P[i] for i in coord[1]}=={canonical[i] for i in [0,1,3]}
    pv=[[] for p in P]; pf=[[] for f in faces]; saddles=[]; weak=[]; zero=0; packets=[]
    for edge,(f,h) in sorted(edges.items()):
        i,j=edge
        a=dot(X[i],sub(X[j],X[i])); bb=dot(X[j],sub(X[i],X[j]))
        c=dot(Q[f],sub(Q[h],Q[f])); dd=dot(Q[h],sub(Q[f],Q[h]))
        vals=[a,bb,c,dd]; zero+=sum(v==0 for v in vals)
        packets.append(dict(edge=edge,facets=[f,h],primitives=vals))
        pv[i].append(a); pv[j].append(bb); pf[f].append(c); pf[h].append(dd)
        if all(v<0 for v in vals): saddles.append(edge)
        if all(v<=0 for v in vals) and any(v==0 for v in vals): weak.append(edge)
    S=[i for i,v in enumerate(pf) if all(x<0 for x in v)]
    U=[i for i,v in enumerate(pv) if all(x<0 for x in v)]
    if zero==0: assert len(S)+len(U)-len(saddles)==2
    # Weak edge-packets are reported, not silently equated with physical-point counts.
    return dict(vertices=P,facets=faces,edges=sorted(edges),planes=planes,
                f_vector=[len(P),len(edges),len(faces)],V=V,X=J[0],Y=J[1],Z=J[2],
                E=E,N=N,T=T,centroid=g,root=root,coordinate_faces=coord,
                strict_SUH=[len(S),len(U),len(saddles)],stable=S,unstable=U,
                saddle_edges=saddles,weak_edge_packets=weak,zero_primitives=zero,packets=packets,
                maxell=max(map(ell,P)),proper33=proper)



def anchors(b,d):
    return [ratrow(r) for r in [(0,0,1),(0,0,b),(0,1,0),(1,0,d)]]

def cut(K,H,lower=True):
    P,faces,planes,edges=hull(K)
    out=[p for p in P if (p[2]<=H if lower else p[2]>=H)]
    for i,j in edges:
        p,q=P[i],P[j]
        if (p[2]-H)*(q[2]-H)<0:
            out.append(add(p,mul((H-p[2])/(q[2]-p[2]),sub(q,p))))
    return hull(out)[0]

def section(K,w):
    P,faces,planes,edges=hull(K)
    pts=set(p for p in P if p[2]==w)
    for i,j in edges:
        p,q=P[i],P[j]
        if (p[2]-w)*(q[2]-w)<0:
            pts.add(add(p,mul((w-p[2])/(q[2]-p[2]),sub(q,p))))
    pts=sorted(pts); c=cycle(pts,range(len(pts)),(0,0,1))
    Q=[pts[i] for i in c]
    area=abs(sum(Q[i][0]*Q[(i+1)%len(Q)][1]-Q[i][1]*Q[(i+1)%len(Q)][0]
                 for i in range(len(Q))))/2
    assert area>0
    return dict(vertices=Q,area=area,min_x=min(p[0] for p in Q),min_y=min(p[1] for p in Q))

def mass(K,b,d):
    P,faces,planes,edges=hull([world(p,b,d) for p in K])
    V,J=moments(P,faces,average(P))
    for o in [P[0],P[-1]]: assert moments(P,faces,o)==(V,J)
    X,Y,Z=J;E=V+(d-1)*X-Y-(1-b)*Z;N=(1+b)*X+(1+b+d)*Y
    assert V>0 and E>0
    return dict(V=V,X=X,Y=Y,Z=Z,E=E,N=N,centroid=mul(1/V,J),
                level_vertices=hull(K)[0],physical_vertices=P,facets=faces)

def one_point_volume(r):
    T=[ratrow(p) for p in [(0,0,0),(0,0,1),(0,1,0),(1,0,0)]]
    P,faces,planes,edges=hull(T+[r]);V,J=moments(P,faces,average(P))
    x,y,z=r
    exact=1+max(-z,0)+max(x+y+z-1,0)
    assert 6*V==exact
    return exact

def clipping_receipt(K,b,d,H,proper):
    assert 0<b<1 and d>=0 and H>=max(F(1),d)
    Q=cut(K,H);R=cut(K,H,False)
    ap=audit(K,b,d,proper);aq=audit(Q,b,d,proper);ar=mass(R,b,d)
    for name in KEYS: assert ap[name]==aq[name]+ar[name]
    v,e,W,Fcap=aq['V'],aq['E'],ar['V'],ar['E']
    t=6*v;h=1+b;q=h+d
    BH=(1+d)*t+b-H
    a=((1+d)*t-(1+d+H))/H
    gamma=BH/(H*t)
    assert 0<=gamma<2 and Fcap>H*W
    assert ar['N']<=a*Fcap+q*W<6*v*gamma*Fcap
    bound=v/(v+W)*(aq['T']*e+gamma*Fcap)/(e+Fcap)
    assert ap['T']<bound
    if ap['T']>=2: assert aq['T']>ap['T']
    # The marked ABD patch in the true fan from C gives the stronger core mean bound.
    assert 4*e<=3*H*v-(3*H-h-d)/6
    k=F(3,4)-(3*H-h-d)/(4*H*t);s=W/v
    assert 0<e/(H*v)<=k<F(3,4)
    sector=(F(20,9)*k+gamma*s)/((1+s)*(k+s))
    sharp_B=min(BH,h*((1-b)*t+b-H)/(1-d)) if d<1 else BH
    sharp_gamma=sharp_B/(H*t);sharp_a=(sharp_B-q)/H
    sharp_bound=v/(v+W)*(aq['T']*e+sharp_gamma*Fcap)/(e+Fcap)
    assert 0<sharp_gamma<=gamma and ap['T']<sharp_bound<=bound
    assert ar['N']<=sharp_a*Fcap+q*W<6*v*sharp_gamma*Fcap
    assert aq['T']<F(20,9) and ap['T']<sector
    C=(F(0),F(1),F(0)); projected=[]
    for p in ar['level_vertices']:
        r=add(C,mul(H/p[2],sub(p,C)))
        rr=world(r,b,d)
        assert all(dot(n,rr)<=rhs for n,rhs in aq['planes'])
        point_t=one_point_volume(rr)
        assert point_t<=t and rr[0]+rr[1]<=point_t and rr[2]>=1-point_t
        nr=h*r[0]+q*r[1]
        assert nr<=sharp_B<=BH
        assert h*p[0]+q*p[1]<=a*p[2]+q
        projected.append(dict(point=r,six_hull_volume=point_t,n=nr,bound=BH))
    return dict(P=ap,Q=aq,cap=ar,H=H,gamma=gamma,a=a,cap_volume_ratio=s,
                core_mean_bound=k,trace_bound=bound,mass_sector_bound=sector,
                sharp_section_bound=sharp_B,sharp_gamma=sharp_gamma,sharp_trace_bound=sharp_bound,
                projected_points=projected)

def core_integrals(b,d,m):
    # Exact cubic integration of genuine sections, independent of all boundary fans.
    h=1+b;q=h+d;alpha=1-b;I=[F(0)]*4
    cuts=sorted(set([F(0),b,d,F(1)]))
    for l,r in zip(cuts[:-1],cuts[1:]):
        for j,weight in enumerate([1,3,3,1]):
            w=l+(r-l)*F(j,3);U=min(F(1),1+d-w);t=m*max(1-w/b,0)
            assert t<=h*U
            A=U*U/2-t*t/(2*h*q)
            Ix=U**3/6-t**3/(6*h*h*q)
            Iy=U**3/6-t**3/(6*h*q*q)
            for k,value in enumerate([A,w*A,Ix,Iy]): I[k]+=(r-l)*weight*value/8
    V,E,X,Y=[x/alpha for x in I]
    Z=(V+(d-1)*X-Y-E)/alpha;N=h*X+q*Y
    return dict(V=V,X=X,Y=Y,Z=Z,E=E,N=N)

def nf_cap_family(b,rho):
    d=eps=F(1,1000);h=1+b;q=h+d;m=h*rho
    HH=[((-1,0,0),0),((0,-1,0),0),((0,0,-1),0),((0,0,1),1),
        ((1,1,0),1),((1,1,1),1+d),((-h,-q,-m/b),-m)]
    HH=[(ratrow(n),F(s)) for n,s in HH]
    Q=from_halfspaces(HH);p=(eps/4,eps/3,1+eps/4);K=Q+[p]
    assert dot(HH[3][0],p)>HH[3][1]
    assert all(dot(n,p)<s for i,(n,s) in enumerate(HH) if i!=3)
    assert hull(cut(K,1))[0]==hull(Q)[0]
    out=clipping_receipt(K,b,d,F(1),False)
    assert out['P']['T']>2
    I=core_integrals(b,d,m)
    for k in KEYS: assert out['Q'][k]==I[k]
    # Exact physical pyramid cap, including all first moments of the same mass.
    capV=eps**3/(24*(1-b))
    gc=world((5*eps/16,eps/3,1+eps/16),b,d)
    assert out['cap']['V']==capV and out['cap']['centroid']==gc
    witness=section(K,1+eps/8)
    assert witness['min_x']==eps/8 and witness['min_y']==eps/6
    lam=F(9999,10000);c=(F(99,200),F(99,200),F(0))
    assert all(dot(n,c)<s for i,(n,s) in enumerate(HH) if i!=2)
    KP=anchors(b,d)+[add(mul(lam,v),mul(1-lam,c)) for v in K]
    pp=clipping_receipt(KP,b,d,F(1),True)
    a=pp['P'];old=out['P']
    assert a['maxell']==lam*p[2]>1 and a['T']>2
    assert a['V']>=lam**3*old['V'] and a['E']>=lam**4*old['E'] and a['N']<=old['N']
    assert a['T']<=old['T']/lam**7<F(51,25)
    wp=section(KP,(1+a['maxell'])/2)
    assert wp['min_x']>0 and wp['min_y']>0
    for z in [out['P'],out['Q'],pp['P'],pp['Q']]:
        assert z['zero_primitives']==0 and not z['weak_edge_packets']
    return dict(inputs=dict(b=b,d=d,rho=rho,m=m,eps=eps,cap_apex=p,
                            core_halfspaces=HH,lambda_value=lam,root_center=c),
                prototype=out,proper=pp,missing_axes=witness,proper_missing_axes=wp)

def countercontrols():
    root=[ratrow(r) for r in [(F(1,50),F(49,50),0),(F(1,50),F(51,50),0)]]
    b,d=F(7,20),F(9,10)
    K=anchors(b,d)+root+[ratrow((4,4,F(41,40)))]
    negative=clipping_receipt(K,b,d,F(1),True)
    gap=negative['P']['T']-negative['Q']['T']
    assert gap==F(1072775985744707886083949,6728354013671282854950465883)>0
    assert negative['P']['T']<1
    b2,d2=F(1,3),F(3,2)
    K2=anchors(b2,d2)+root+[ratrow((2,3,2))]
    largeD=clipping_receipt(K2,b2,d2,d2,True)
    for z in [negative['P'],negative['Q'],largeD['P'],largeD['Q']]:
        assert z['proper33'] and z['zero_primitives']==0 and not z['weak_edge_packets']
    return dict(unconditional_deletion=dict(b=b,d=d,level_generators=K,
                    result=negative,trace_increase=gap),
                large_D=dict(b=b2,d=d2,level_generators=K2,result=largeD))

def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    return x

def main():
    assert __debug__
    assert (F(20,9)*F(3,4)+2*F(1,12))/((1+F(1,12))*(F(3,4)+F(1,12)))==F(132,65)
    assert F(51,25)-F(132,65)==F(3,325)>0
    lam0=F(9993,10000)
    assert lam0**7>=F(9951,10000)
    assert F(203,100)/F(9951,10000)==F(20300,9951)<F(51,25)
    report=dict(parent=PARENT,parent_sha256=PARENT_SHA256,
                higher_trace=nf_cap_family(F(1,5),F(4,5)),
                larger_b=nf_cap_family(F(3,5),F(31,32)),
                controls=countercontrols(),volume_sector_bound=F(132,65))
    data=(json.dumps(serial(report),sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('one_zero_cap.json').write_bytes(data)
    for key in ['higher_trace','larger_b']:
        z=report[key]
        for label,a in [('CORE',z['prototype']['Q']),('CAP',z['prototype']['P']),
                        ('PROPER',z['proper']['P']),('PROPER_CLIP',z['proper']['Q'])]:
            print(key,label,*a['f_vector'],'T',a['T'],'SUH',*a['strict_SUH'],'ZERO',a['zero_primitives'])
    for key in ['unconditional_deletion','large_D']:
        z=report['controls'][key]['result']
        for label in ['P','Q']:
            a=z[label];print(key,label,*a['f_vector'],'T',a['T'],'SUH',*a['strict_SUH'],'ZERO',a['zero_primitives'])
    print('ALL_TRUE_CAP_RESTORATIONS_VXYZEN_THREE_FANS_AND_CORE_SECTIONS_PASS')
    print('ALL_CANONICAL_PROJECTIONS_MARKED_TETRAHEDRA_AND_PROPER_FACES_PASS')
    print('REPORT',len(data),hashlib.sha256(data).hexdigest())
    print('ONE_ZERO_ENDPOINT_PRESERVING_OVERSHOOT_ERASURE_EXACT_PASS')

if __name__=='__main__':main()
```

## 10. What changed and the remaining geometric problem

The useful change of viewpoint was to stop trying to replace the upper sections by a parallel band. The actual zero endpoint C projects every high-cap point into the retained body. The volume of that projected point together with the marked tetrahedron controls its mixed moment. Integrating that one geometric bound retains both the actual cap volume and its ell-first moment, including the possibly negative coefficient a_H.

The full maxell>A sector with 0<d<=1 is now removable from the high-trace optimization problem by a proper-preserving clip. This is a reduction, not an unconditional numerical bound for every body in that sector: its retained core may still have genuinely non-CH geometry. The new NF/CH-core extension and the whole cap-volume sector are actual numerical exclusions.

The primary remaining geometry is therefore outside CH already within 0<=ell<=1: sections with several positive upper normals, sections missing an axis near the zero root, or sections extending beyond their outer-axis chord. For d>1 the remaining marked range is 0<=ell<=d, including 1<ell<=d; the theorem cannot delete D to force maxell=A.

A useful continuation should combine a real bounded-height multi-normal core with its marked coordinate-face geometry. The cap inequalities (4.3), (4.6) and the reserved-tetrahedron mean reaction (6.1) can be retained without redoing the NF certificate. Independent section-centroid assignments would lose their proof.

No whole E17 exclusion, universal one-zero 51/25 theorem, sharp trace supremum, equilibrium-preserving regularization, or new attaining complexity follows. The original mechanical interval remains 34..622. The exact nonwinning controls and the failed unconditional deletion are fully reconstructible above.

Convenience copies, not dependencies: runnable source (`one_zero_cap.py`), complete exact report (`one_zero_cap.json`), normal and cold-matched receipt (`one_zero_cap_receipt.txt`).
