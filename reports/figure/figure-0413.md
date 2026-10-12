# figure-0413

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Bright Harbor 81 — globally mass-centered multiple-cut family

Branch: `[internal-source-reference]`.

**No new own110 construction is accepted in this handoff.** The literal parent `figure-0410`, SHA-256 `2b99c50593d761647578973300a0ff02de4f3f4182ccab3d4677b962346457f0`, remains the authority for the C224 own222 entrance.

There are two substantive results here: a globally defined physical mass-closure parameterization whose entire 21-cut family satisfies **E≤309**, and an analytically certified pair of small rational polyhedra showing that an arbitrarily small local escape-defect objective need not indicate progress toward either monostability or mono-instability.

**Evidence limitation.** The interrupted numerical scratch, its complete execution receipts, and the complete continuation-journal text are not retained sufficiently in my current context to support new numerical census or completed-run claims. I am not asserting a complete current-journal read. In particular, I do not promote the exploratory affine, multi-cut, or merge-energy outputs to exact successors. The results below depend on the available literal parent and explicit derivations, not on those unverified outputs. The complete source below is supplied as a replay and verification unit; its terminal markers are expected outputs, not claimed observed executions.

## 1. A global physical mass-closure theorem

Let K be a full-dimensional convex polytope with 0 in its interior, and suppose its uniform-volume first moment M(K) is nonzero. Fix any finite collection of offset vectors v₁,…,vₘ. Duplicate offsets may be removed.

Define

`K(q;v) = K ∩ ⋂ᵢ {x : (q+vᵢ)·x ≤ 1}`.

These are changes to the filled shape. The reference origin is fixed; there is no freely assigned center and no density change.

**Theorem. For every finite choice of the offsets, there is exactly one q such that the actual uniform-volume centroid of K(q;v) is 0.**

This extends the parent's one-cut uniqueness statement to arbitrary numbers, orientations and relative positions of cuts. The cuts need not form one connected cap. They may trim opposite sides, remove the original stable face or unstable pole, and change the active contact complex.

### Existence

Write

`ψ_v(x) = maxᵢ vᵢ·x`

and consider the convex function

`Φ_v(q) = ∫_K max(0, 1 − q·x − ψ_v(x)) dx`.

For each x the integrand is the maximum of zero and an affine function of q. Differentiation under the integral gives

`∇Φ_v(q) = −∫_{K(q;v)} x dx = −M(K(q;v))`.

The switching sets have zero three-dimensional volume, so they do not contribute an extra boundary term to this first derivative.

The function is coercive. Choose a ball B(0,r) contained in K. For q=t e, with |e|=1, restrict the integral to the portion of that ball where e·x≤−r/2. This portion has a positive volume independent of e. Throughout it,

`1 − q·x − ψ_v(x) ≥ 1 + tr/2 − r maxᵢ|vᵢ|`.

Consequently Φ_v(q) tends to infinity as |q| tends to infinity. It therefore has a minimizer, and the gradient equation at that minimizer is exactly M=0. Every K(q;v) contains a neighborhood of 0 and is contained in the bounded set K, so this is a genuine positive-volume, uniformly filled convex body.

### Uniqueness

On a fixed active-complex region, let Fᵢ be the facet belonging to the new plane `(q+vᵢ)·x=1`. Its contribution is

`Hᵢ = ∫_{Fᵢ} xxᵀ / |q+vᵢ| dA`,

and

`−D_q M = D²Φ_v = H = Σᵢ Hᵢ`.

A positive-area facet in an affine plane not through 0 gives a positive-definite Hᵢ: a nonzero homogeneous linear form cannot vanish on the entire affine plane, so its squared integral over the facet is positive.

At a zero-moment solution there must be at least one genuine new facet cutting the interior of K. Otherwise the body would still be K, contradicting M(K)≠0. A positive-area patch of such a facet supplies strict convexity in every parameter direction near the minimizer. This argument also applies when other parts of the complex are undergoing a contact change. Two different minimizers would force Φ_v to be constant along the segment joining them, contradicting this local strict convexity. Hence the minimizer is unique.

The assumption M(K)≠0 matters. A previously centered K with every added inequality inactive can have an open set of parameters describing the same centered body.

## 2. The entire 21-cut G6/G8 family is below the edge target

The literal G6 and G8 parents each have 84 maximal facets. Their own-centroid census differs from their origin-reference census, so their uniform-volume first moment is not zero. The theorem applies to each independently.

For m new halfspaces,

`F(K(q;v)) ≤ 84+m`.

Every convex three-polyhedron satisfies `E≤3F−6`: combine Euler's identity with the fact that every vertex has degree at least three. Therefore

`m≤21  ⇒  F≤105  ⇒  E≤309<311`.

**Thus every member of this globally mass-centered 21-cut family already satisfies the requested edge budget, irrespective of contact changes.** Its number of vertices need not remain below 105.

There is a three-dimensional offset gauge: replacing every vᵢ by vᵢ+w replaces the unique q by q−w and leaves the actual planes unchanged. Enforcing `Σᵢvᵢ=0` leaves 60 unconstrained offset coordinates when m=21. Some parameter regions have inactive cuts and therefore lower effective shape dimension.

This family is not a restricted selection of centered multiple cuts. Given any origin-centered body obtained by intersecting K with m halfspaces containing 0, normalize their equations to nᵢ·x≤1, set q to the mean of the nᵢ, and set vᵢ=nᵢ−q. The uniqueness theorem returns precisely that q. Hence the parameterization covers **all origin-centered intersections of the parent with at most m additional halfspaces**.

What remains unsolved is the mechanical census. The theorem does not imply own110, and it does not certify the census of a floating approximation to its minimizer.

## 3. An exact derivative for mass-preserving shape changes

The same calculation supplies an implementation-ready derivative. If the offsets change by δvᵢ while the actual centroid is kept at 0, then, away from a contact change,

`δq = −H⁻¹ Σᵢ Hᵢ δvᵢ`.

Thus the actual new plane normals change by

`δnᵢ = δvᵢ − H⁻¹ Σⱼ Hⱼ δvⱼ`.

This removes the three first-moment directions from a proposed physical shape step. It is not a translation of the test center. The matrices are obtained from ordinary face integrals, and can be evaluated exactly for rational input.

For an outward-oriented facet triangle with vertices a,b,c, let s=a+b+c and let n be the facet normal in the equation n·x=1. Its contribution to Hᵢ is

`[cross(b−a,c−a)·n / (24 n·n)] × [ssᵀ+aaᵀ+bbᵀ+ccᵀ]`.

Contact changes must trigger a fresh maximal-complex reconstruction. The smooth derivative is a local computational aid inside this globally defined finite family, not a restriction to one incidence pattern.

At the exactly centered solution, clipping cannot make a previously nonstable original facet stable: its perpendicular foot is unchanged, and its new polygon is a subset of the old polygon. Consequently there are at most m new stable-facet candidates plus the original unique reference-stable facet. That observation reduces stable-side bookkeeping, but it does not preserve old unstable-vertex witnesses. All actual vertices and edges still require fresh checks.

## 4. Exact low-arithmetic regression bodies for local escape scores

The following construction is independent of numerical optimization and has a complete analytical census.

Choose `0<ε<1/2`. Define

`Pε = { (x,y,z): |x|+ε|y|≤1, |y|+ε|z|≤1, |z|+ε|x|≤1 }`.

Its polar is

`Qε = conv{ (±1,±ε,0), (0,±1,±ε), (±ε,0,±1) }`.

The signs in each displayed pair are independent. Both bodies are centrally symmetric, so their actual uniform-volume centroid is exactly 0.

Let `a=1/(1+ε)` and `b=1−ε`. The complete vertex set of Pε consists of the eight points `(±a,±a,±a)` and the twelve cyclic permutations of `(±1,0,±b)`.

| Body | V/E/F | Actual own strict S/U/H | Weak | C=2E |
|---|---|---|---|---:|
| Pε | 20/30/12 | 12/20/30 | 0/0/0 | 60 |
| Qε | 12/30/20 | 20/12/30 | 0/0/0 | 60 |

Pε has twelve maximal pentagons. Qε has twenty maximal triangles. These are maximal-complex counts, not counts obtained by retaining triangulation diagonals.

### Analytical census and mass certificate

All twelve defining normals of Pε have squared norm `1+ε²`. Their perpendicular feet satisfy every other supporting inequality strictly, so all twelve facets are stable.

Every Pε vertex is unstable. Up to signs and cyclic permutation, the only edge-direction calculations needed are

`A·(B−A) = −(1−ε+ε²)/(1+ε)²`,

`B·(A−B) = −ε(1−ε+ε²)/(1+ε)`,

and

`B·(B′−B) = −2(1−ε)²`,

where A is a vertex of the first type, B is an adjacent vertex of the second type, and B′ is its partner on the remaining edge. All are strictly negative in the specified interval.

For adjacent facet normals n,m, the closest point of their intersection line is

`(n+m)/(1+ε²+n·m)`.

Both normal-cone coefficients are positive. The strict endpoint inequalities above place this point strictly inside the corresponding edge. Hence every one of the thirty edges is a strict saddle. There are no zero primitive predicates and no additional weak equilibria. Polarity, with the same actual center 0 on both centrally symmetric bodies, exchanges stable and unstable features and preserves the strict edge test, giving the stated census of Qε.

The volumes are

`Vol(Pε)=4(2−ε)/(1+ε)`,

`Vol(Qε)=4(1+3ε+ε³)/3`.

For Pε, the projection of any one pentagonal facet onto its coordinate plane has area `(2−ε)/(1+ε)`. The twelve origin-based facet cones give the first formula. The twenty triangular faces of Qε comprise eight triangles of absolute determinant `1+ε³` and twelve of absolute determinant `2ε`, giving the second formula.

### A small score with many strict equilibria

For each vertex n of Qε, its best other vertex for the normalized outgoing-dot test is its near-coincident partner. Therefore

`max_{m≠n} n·(m−n)/|n|² = −2ε²/(1+ε²)`.

Exempting any one root gives total negative-part loss

`22ε²/(1+ε²)`.

This tends to zero while Qε retains **twelve strict unstable vertices**, not one. The failure remains even when the exempted root is chosen by maximum radius: all twelve vertices have the same radius and are strictly unstable.

For `ε=1/10⁶`, the loss is exactly `22/(10¹²+1)`, approximately `2.2×10⁻11`. A rule counting an unstable vertex only when its normalized outgoing margin is below `−10⁻10` reports **zero** unstable vertices here. That is a tolerance error, not a weak equilibrium or a physical construction.

The true edge merge structure also stays far from a one-peak state. The six within-pair edges have minimum squared radius 1. The remaining twenty-four edges have minimum squared radius `(1+ε+ε²)/2`. A maximum-spanning merge calculation therefore has six small finite bars of length ε² and five large bars of length `(1−ε+ε²)/2. The large barriers do not vanish with the local escape loss.

This pair is a compact exact regression test for both the physical and polar sides of a search. It also provides a necessary sanity check: a purported strict census must not omit every maximum-radius vertex.

### Literal arithmetic choice

Use `D=1000000`, `ε=1/D`, and `G=D(D+1)`.

Pε has the eight integer rows `(±D²,±D²,±D²)` and the twelve cyclic permutations of `(±G,0,±(D²−1))`, all divided by G. Its common raw and centered denominator has 40 bits.

Qε has the twelve integer rows `(±D,±1,0)`, `(0,±D,±1)`, `(±1,0,±D)`, all divided by D. Its common raw and centered denominator has 20 bits.

These are fully specified nonwinner bodies, with analytical verification status. They are not proposed as close mechanical successors to C224.

## 5. Complete recovery and verification source

The source below contains the complete literal G6 input, a maximal-face exact hull constructor, exact clipping, two volume-moment decompositions, exhaustive strict/weak feature tests, the two regression generators, the exact merge-bar check, and a bounded rational Newton implementation of the common-tilt controller.

It uses only the Python standard library and targets Python 3.13. The default command does not depend on a numerical optimizer or an external checkpoint:

`python BH81_CONT.py`

Expected analytical replay marker:

`BH81_ANALYTIC_CONTINUATION_REPLAY_PASS`

The optional command

`python BH81_CONT.py --mass-probe`

runs a two-sided trimming probe with offsets `(5,0,0)` and `(−5,0,0)`, a control grid of 10¹⁸, at most 40 Newton iterations, at most 30 dyadic backtracks, and actual centroid tolerance 10⁻14. Its returned rational body is audited at its **actual** centroid. A small residual is not represented as an exact zero-centroid root, and no census for that probe is asserted in this handoff.

The script writes canonical JSON outputs and a byte-count/SHA-256 manifest. I do not supply unobserved output hashes. The literal G6 input is checked against its supplied 1144-byte identity before use.

```python
from fractions import Fraction as F
from itertools import combinations, product
from collections import defaultdict, Counter
from pathlib import Path
import argparse, hashlib, json, math, sys

sys.set_int_max_str_digits(0)
Z = F(0)
P6 = [
[-662782,-214465,-845973],[-414228,-151742,533649],
[-161896,254607,812156],[365352,256078,682778],
[-4963,148822,-521027],[472559,520988,212704],
[79060,562904,-173068],[201613,126680,-443592],
[329321,453145,628173],[223093,597478,579771],
[-19072,614025,655946],[-249702,561436,698505],
[-441568,542642,645050],[81579,740260,404654],
[-621409,499632,558154],[-759574,464284,346398],
[-876227,418544,281729],[-762901,475717,422075],
[-969023,321126,89302],[-933907,249672,-106357],
[-931297,367490,186346],[-990566,281683,-2502],
[-1004114,233262,-93695],[-1009407,175066,-181963],
[-1003594,111429,-275498],[-985825,56733,-362387],
[-963561,3357,-431336],[-926489,-29260,-514430],
[-874803,-74796,-604952],[-797712,-129095,-709746],
[212288,-80824,-582533],[-530449,-300001,-896862],
[-453991,-363552,-909506],[-263404,-613951,20338],
[-477834,-372599,114345],[-600760,-232410,-880486],
[-364153,-430343,-913823],[217011,-462047,-780335],
[486981,106570,612006],[157779,-569803,63306],
[-149044,-601434,-828255],[-98079,-133974,751134],
[19869,-745421,-660667],[119026,-858571,-341744],
[285028,-657317,-632695],[168908,-413062,260503]]
G6 = dict(grid=1000000, points=P6)
G6_SHA = '63ead46daff5c7c9cd4344699cbe551a7e92b2a2851703aacfa55eb1621b6aa5'

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def encode(x):
    return json.dumps(x,sort_keys=True,separators=(',',':'),
                      default=str).encode()
def rational_points(raw):
    return [tuple(F(x,raw['grid']) for x in row) for row in raw['points']]
def raw_points(points):
    points=sorted(set(points))
    g=math.lcm(*(x.denominator for row in points for x in row))
    return dict(grid=g,points=[[int(x*g) for x in row] for row in points])

def cycle(points,n):
    points=sorted(set(points))
    if len(points)<3: return ()
    drop=max(range(3),key=lambda i:abs(n[i]))
    axes=[i for i in range(3) if i!=drop]
    def xy(p): return (p[axes[0]],p[axes[1]])
    def turn(a,b,c):
        a,b,c=xy(a),xy(b),xy(c)
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    ordered=sorted(points,key=xy)
    lo=[]
    for p in ordered:
        while len(lo)>1 and turn(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(ordered):
        while len(hi)>1 and turn(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    out=lo[:-1]+hi[:-1]
    if len(out)<3: return ()
    if dot(cross(sub(out[1],out[0]),sub(out[2],out[0])),n)<0:
        out.reverse()
    k=out.index(min(out))
    return tuple(out[k:]+out[:k])

# A face is (outward normal, positive support, cyclic rational vertices).
def hull(points):
    points=sorted(set(points)); raw=raw_points(points)
    ip=[tuple(v) for v in raw['points']]; g=raw['grid']; planes={}
    for i,j,k in combinations(range(len(ip)),3):
        n=cross(sub(ip[j],ip[i]),sub(ip[k],ip[i]))
        if n==(0,0,0): continue
        d=dot(n,ip[i]); vals=[dot(n,p)-d for p in ip]
        if max(vals)<=0 and min(vals)<0: pass
        elif min(vals)>=0 and max(vals)>0:
            n=mul(-1,n); d=-d
        else: continue
        h=math.gcd(*(abs(x) for x in (*n,d)))
        key=tuple(x//h for x in (*n,d))
        planes[key]=None
    faces=[]
    for key in sorted(planes):
        n=tuple(F(x) for x in key[:3]); d=F(key[3],g)
        assert d>0
        poly=cycle([p for p in points if dot(n,p)==d],n)
        assert len(poly)>=3
        faces.append((n,d,poly))
    assert len(faces)>=4
    return faces

def vertices(faces):
    return sorted({p for n,d,poly in faces for p in poly})

def clip(faces,n,d=F(1)):
    n=tuple(map(F,n)); d=F(d); allp=vertices(faces)
    if all(dot(n,p)<=d for p in allp): return faces
    assert any(dot(n,p)<d for p in allp)
    result=[]; cap=set()
    for nn,dd,poly in faces:
        out=[]
        for a,b in zip(poly,poly[1:]+poly[:1]):
            sa=dot(n,a)-d; sb=dot(n,b)-d
            if sa<=0: out.append(a)
            if sa==0: cap.add(a)
            if (sa<0<sb) or (sb<0<sa):
                p=add(a,mul(-sa/(sb-sa),sub(b,a)))
                out.append(p); cap.add(p)
        out=cycle(out,nn)
        if len(out)>=3: result.append((nn,dd,out))
    cap=cycle(cap,n)
    assert len(cap)>=3
    result.append((n,d,cap))
    return result

def integrate(faces,anchor=(Z,Z,Z)):
    V=Z; M=[Z,Z,Z]; count=0
    for n,d,poly in faces:
        for j in range(1,len(poly)-1):
            a,b,c=poly[0],poly[j],poly[j+1]
            w=F(det(sub(a,anchor),sub(b,anchor),sub(c,anchor)),6)
            assert w>0
            V+=w; count+=1
            for k in range(3): M[k]+=w*(anchor[k]+a[k]+b[k]+c[k])/4
    assert V>0
    return V,tuple(M),count

def complex_data(faces):
    p=vertices(faces); lookup={x:i for i,x in enumerate(p)}
    f=[[lookup[x] for x in poly] for n,d,poly in faces]
    edges=defaultdict(list); nbr=defaultdict(set)
    for k,((n,d,poly),row) in enumerate(zip(faces,f)):
        assert all(dot(n,x)<=d for x in p)
        assert set(row)=={i for i,x in enumerate(p) if dot(n,x)==d}
        for i,j in zip(row,row[1:]+row[:1]):
            edges[tuple(sorted((i,j)))].append((k,i,j))
            nbr[i].add(j); nbr[j].add(i)
    for pair,inc in edges.items():
        assert len(inc)==2
        assert inc[0][1:]==tuple(reversed(inc[1][1:]))
    assert len(p)-len(edges)+len(f)==2
    reached={0}; stack=[0]
    while stack:
        i=stack.pop()
        for j in nbr[i]-reached: reached.add(j); stack.append(j)
    assert len(reached)==len(p)
    return p,f,edges,nbr

def census(faces,c):
    p,f,edges,nbr=complex_data(faces); x=[sub(a,c) for a in p]
    strict=[[],[],[]]; weak=[[],[],[]]; zeros=[0,0,0]
    def take(k,label,values):
        zeros[k]+=sum(v==0 for v in values)
        if min(values)>0: strict[k].append(label)
        elif min(values)>=0: weak[k].append(label)
    for k,((n,d,poly),row) in enumerate(zip(faces,f)):
        take(0,k,[-dot(n,cross(sub(x[j],x[i]),x[i]))
                  for i,j in zip(row,row[1:]+row[:1])])
    for i in range(len(p)):
        take(1,i,[-dot(x[i],sub(x[j],x[i])) for j in sorted(nbr[i])])
    for (i,j),inc in sorted(edges.items()):
        e=sub(x[j],x[i]); ee=dot(e,e); t=-dot(x[i],e)
        z=add(mul(ee,x[i]),mul(t,e))
        n,m=faces[inc[0][0]][0],faces[inc[1][0]][0]
        aa,bb,ab=dot(n,n),dot(m,m),dot(n,m)
        zn,zm=dot(z,n),dot(z,m)
        take(2,[i,j],[t,ee-t,zn*bb-zm*ab,zm*aa-zn*ab])
    counts=list(map(len,strict))
    if not any(weak): assert counts[0]+counts[1]-counts[2]==2
    # Independent all-halfspace characterization of strict stable faces.
    stable2=[]
    for i,(n,d,poly) in enumerate(faces):
        foot=add(c,mul((d-dot(n,c))/dot(n,n),n))
        if all(dot(m,foot)<h for j,(m,h,pp) in enumerate(faces) if i!=j):
            stable2.append(i)
    assert stable2==strict[0]
    # Independent all-vertex characterization of strict unstable vertices.
    unstable2=[i for i in range(len(p))
        if all(dot(x[i],sub(x[j],x[i]))<0 for j in range(len(p)) if i!=j)]
    assert unstable2==strict[1]
    return dict(strict=counts,weak=list(map(len,weak)),primitive_zeros=zeros,
                strict_features=strict,weak_features=weak)

def audit(faces):
    p,f,edges,nbr=complex_data(faces)
    V,M,nt=integrate(faces)
    anchor=tuple(sum(x[k] for x in p)/len(p) for k in range(3))
    V2,M2,nt2=integrate(faces,anchor)
    assert (V,M)==(V2,M2)
    c=tuple(x/V for x in M)
    own=census(faces,c)
    return dict(V=len(p),E=len(edges),F=len(f),C=2*len(edges),
        volume=V,centroid=c,own=own,faces=f,points=p,
        face_histogram=dict(Counter(map(len,f))),positive_tetrahedra=nt,
        second_mass_decomposition_equal=True)

def inverse3(h):
    d=det(*h)
    if not d: raise ArithmeticError('singular active-cap mass derivative')
    cols=[cross(h[1],h[2]),cross(h[2],h[0]),cross(h[0],h[1])]
    return [[cols[j][i]/d for j in range(3)] for i in range(3)]

def cap_body(base,q,offsets):
    faces=base
    for v in offsets: faces=clip(faces,add(q,v))
    return faces

def cap_hessian(faces,q,offsets):
    keys={add(q,v) for v in offsets}
    H=[[Z for j in range(3)] for i in range(3)]
    for n,d,poly in faces:
        nn=tuple(t/d for t in n)
        if nn not in keys: continue
        for j in range(1,len(poly)-1):
            a,b,c=poly[0],poly[j],poly[j+1]; s=add(add(a,b),c)
            w=dot(cross(sub(b,a),sub(c,a)),nn)/(24*dot(nn,nn))
            assert w>0
            for k in range(3):
                for l in range(3):
                    H[k][l]+=w*(s[k]*s[l]+a[k]*a[l]+b[k]*b[l]+c[k]*c[l])
    return H

def mass_probe(base,offsets):
    offsets=sorted(set(tuple(map(F,v)) for v in offsets))
    q=tuple(F(x,10**8) for x in [-286112322,-83717249,58027896])
    grid=10**18; tol=F(1,10**14); trace=[]; status='iteration_limit'
    oldkeys={tuple(x/d for x in n) for n,d,poly in base}
    for k in range(40):
        faces=cap_body(base,q,offsets); V,M,nt=integrate(faces)
        c=tuple(x/V for x in M)
        trace.append(dict(iteration=k,q=q,volume=V,centroid=c))
        if max(map(abs,c))<tol:
            status='rational_centroid_residual_target_met'; break
        if oldkeys & {add(q,v) for v in offsets}:
            status='old_new_facet_contact_requires_new_chart'; break
        try: R=inverse3(cap_hessian(faces,q,offsets))
        except ArithmeticError:
            status='singular_active_chart'; break
        step=tuple(dot(row,M) for row in R); score=dot(M,M)
        accepted=False
        for j in range(30):
            qq=tuple(F(round((q[i]+step[i]/(2**j))*grid),grid) for i in range(3))
            if qq==q: continue
            ff=cap_body(base,qq,offsets); vv,mm,nn=integrate(ff)
            if dot(mm,mm)<score:
                q=qq; accepted=True; break
        if not accepted:
            status='rational_line_search_stalled'; break
    faces=cap_body(base,q,offsets)
    return dict(status=status,q=q,offsets=offsets,control_grid=grid,
        exact_zero_centroid_claim=False,trace=trace,
        raw=raw_points(vertices(faces)),audit=audit(faces))

def regression_raw(D):
    G=D*(D+1); p=set(); q=set()
    for s in product([-1,1],repeat=3): p.add(tuple(t*D*D for t in s))
    for s,t in product([-1,1],repeat=2):
        b=(s*G,0,t*(D*D-1))
        for k in range(3): p.add(b[k:]+b[:k])
        b=(s*D,t,0)
        for k in range(3): q.add(b[k:]+b[:k])
    return dict(grid=G,points=sorted(p)),dict(grid=D,points=sorted(q))

def merge_certificate(faces,D):
    p,f,edges,nbr=complex_data(faces); R=F(D*D+1,D*D)
    assert all(dot(x,x)==R for x in p)
    weighted=[]
    for i,j in edges:
        midpoint=mul(F(1,2),add(p[i],p[j]))
        weighted.append((dot(midpoint,midpoint),i,j))
    parent=list(range(len(p)))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]; i=parent[i]
        return i
    bars=[]
    for w,i,j in sorted(weighted,reverse=True):
        a,b=root(i),root(j)
        if a!=b: parent[b]=a; bars.append(R-w)
    expected=Counter({F(1,D*D):6,F(D*D-D+1,2*D*D):5})
    assert Counter(bars)==expected
    loss=F(22,D*D+1)
    assert loss<F(1,10**10)
    return dict(local_root_exempt_loss=loss,
        bars=[dict(length=k,multiplicity=v) for k,v in sorted(expected.items())],
        normalized_merge_loss=sum(bars)/R)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mass-probe',action='store_true')
    args=ap.parse_args(); manifest={}
    def emit(name,obj):
        b=encode(obj); Path(name).write_bytes(b)
        manifest[name]=dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
    raw=encode(G6)
    assert len(raw)==1144 and hashlib.sha256(raw).hexdigest()==G6_SHA
    emit('G6.json',G6)
    base=hull(rational_points(G6)); ba=audit(base)
    assert [ba[k] for k in ['V','E','F']]==[44,126,84]
    assert ba['own']['strict']==[15,25,38] and ba['own']['weak']==[0,0,0]
    assert census(base,(Z,Z,Z))['strict']==[1,1,0]
    emit('G6_SOURCE_AUDIT.json',ba)
    D=1000000; eps=F(1,D); pr,qr=regression_raw(D)
    pf,qf=hull(rational_points(pr)),hull(rational_points(qr))
    pa,qa=audit(pf),audit(qf)
    assert [pa[k] for k in ['V','E','F']]==[20,30,12]
    assert [qa[k] for k in ['V','E','F']]==[12,30,20]
    assert pa['own']['strict']==[12,20,30]
    assert qa['own']['strict']==[20,12,30]
    for r in [pa,qa]:
        assert r['centroid']==(Z,Z,Z)
        assert r['own']['weak']==r['own']['primitive_zeros']==[0,0,0]
    assert pa['volume']==4*(2-eps)/(1+eps)
    assert qa['volume']==F(4,3)*(1+3*eps+eps**3)
    emit('P_E30_EXACT.json',dict(parameter_D=D,raw=pr,audit=pa))
    emit('Q_E30_EXACT.json',dict(parameter_D=D,raw=qr,audit=qa,
                               merge=merge_certificate(qf,D)))
    if args.mass_probe:
        emit('COMMON_TILT_RATIONAL_PROBE.json',
             mass_probe(base,[(5,0,0),(-5,0,0)]))
    Path('MANIFEST.json').write_bytes(encode(manifest))
    print(json.dumps(manifest,sort_keys=True))
    print('BH81_ANALYTIC_CONTINUATION_REPLAY_PASS')

if __name__=='__main__': main()
```

## 6. The next constructive question

The new finite search space is the zero-mean collection of at most 21 offset vectors, with q determined by genuine uniform-volume mass closure. Its edge budget is already controlled globally. The remaining question is whether its actual physical and polar complexes can simultaneously have one strict root each, with every other feature excluded strictly.

A useful next implementation is to apply the mass-preserving derivative to finite offset changes, rebuilding contacts after every accepted step. At the centered solution, the stable side can be tested directly on the original and new plane normals; the original nonstable facets cannot become stable by clipping. The physical unstable side must still be rebuilt in full. The regression pair above should be included before trusting any stopping rule based on small outgoing-dot deficits, a tolerance-filtered census, or an exempted root. A successful endpoint must then be frozen as exact input and independently checked for its maximal geometry, actual mass and exhaustive strict/weak census.

This handoff supplies a globally defined physical mass-realization family below E=311 and exact failure controls. It does **not** supply an own110 member of that family.
