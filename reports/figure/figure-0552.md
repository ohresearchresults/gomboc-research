# figure-0552

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Finite mass-balanced replacement: a one-cut closure theorem, a retained-material test, and recoverable experiments

## Status and evidence boundary

**No newly verified own110 JOINT75 successor is established by this continuation.** The substantive result is an exact finite-mass theorem: every interior prescribed centre of a convex body is the homogeneous centroid of a uniquely determined proper one-halfspace truncation, unless it is already the body's centroid. That truncation also maximizes retained volume among all measurable uniform-density subsets with the prescribed centroid. Applied to the six-point JOINT75 bridge, this removes a specific mass-existence obstacle, but not the edge-budget or equilibrium obstacles.

The authoritative entrance remains `figure-0549`, SHA-256 `f996fa67a06c542cbe559aadce39ce5f7b2f06b81a609a4a55dd3f03d9291605`. Its literal JOINT75 geometry is V75/E219/F146, own222, additional weak000, with one P bar of relative depth 0.10155678447201545 and one Q bar of depth 0.06771400169970322. The six bridge points and all75 parent rows are reproduced in the standalone source below. No WIDE-ray exclusion is transferred to this body.

There is a material execution limitation. The directly available consecutive journal transcript reaches character296742 of384614; it includes the parent narrative, all75 coordinates, the six bridge points, and the recovery instructions. The remaining87872 characters include the encoded source capsule. Earlier working notes report complete recovery, but the capsule-tail reads, decoded35-file reads, and subsequent computational returns are not inspectable in this continuation. I therefore do **not** claim a newly observed full-pack replay, numerical endpoint census, interval certificate, byte receipt, or successful optimization. In particular, numerical counts and hashes appearing only in those uninspectable working notes are not promoted here.

The proofs below are self-contained. The box control is proved directly. The supplied program is a fresh, complete exact reconstruction/auditing unit with literal inputs; **its execution is not claimed to have been observed**. It is not a reconstruction of an inaccessible optimizer trajectory.

## 1. A finite one-cut theorem with existence, uniqueness, and a volume optimum

### Statement

Let O be a compact, full-dimensional convex body in R³, and let c be any point of int(O). There exists a finite vector q such that

`L(q) = O ∩ {x : q·(x−c) ≤ 1}`

has positive volume and homogeneous-volume centroid exactly c.

Moreover:

* L(q) maximizes volume among **all measurable subsets** of O with centroid c and uniform density one. Consequently it is also optimal among convex subsets.
* The maximizing subset is unique up to a set of volume zero. Among full-dimensional closed convex subsets it is geometrically unique.
* When c differs from the centroid of O, the cut is proper and q is unique. Thus **every one-halfspace truncation of O having centroid c is this same maximizing truncation**.
* When c already equals the centroid of O, the maximizing body is O. Inactive cutting parameters need not be unique; no proper halfspace truncation can have that same centroid.

This is an existence result for a physical uniform solid, not for adjustable point masses. It supplies the missing existence step in the one-cut potential argument. It says nothing by itself about E, the retained route points, S/U/H, or additional weak equilibria.

### Proof

Translate c to zero and write X=O−c. Define

`Φ(q) = ∫_X max(0, 1−q·x) dx`.

The function is convex. It is continuously differentiable, with

`∇Φ(q) = −∫_{X∩{q·x<1}} x dx`.

The separating plane has three-dimensional measure zero. At q=0 the integrand is positive throughout X, so the same derivative formula applies.

Existence requires more than convexity. Choose r>0 with B(0,r)⊂X. Then

`Φ(q) ≥ ∫_{B(0,r)} max(0,−q·x) dx = (πr⁴/4)‖q‖`.

The last equality follows by integrating −z over a hemisphere after rotating q to the z direction. Therefore Φ is coercive and attains a finite minimum q*. At a minimizer, ∇Φ(q*)=0. The selected region contains a neighborhood of zero, and hence has positive volume. Its first moment is zero, proving that its actual homogeneous centroid is c.

For any measurable uniform subset Y⊂X with positive volume and centroid zero,

`vol(Y) = ∫_Y (1−q*·x) dx ≤ ∫_X max(0,1−q*·x) dx = Φ(q*)`.

For the selected region X∩{q*·x≤1}, its zero first moment gives Φ(q*)=vol(L(q*)). This proves global volume optimality without assuming that the competing subset is convex.

Equality requires including almost every point where 1−q*·x>0 and excluding almost every point where it is negative. The zero set is a plane and has zero volume. This proves uniqueness of the maximizing subset up to null sets.

When c is not the centroid of O, a minimizing cut must remove positive volume. Its plane crosses the interior of O, so the new planar boundary contains a relatively open two-dimensional patch. Two normalized halfspaces giving the same selected convex body must have the same plane on that patch and the same retained side. Since the relative offset is normalized to1, their vectors q agree.

Finally, any proper halfspace cut having centroid c can be normalized into the displayed form: c is strictly inside the selected full-dimensional body, so its signed distance from the cutting plane is positive. Its zero relative moment makes it a stationary point of Φ, hence a global minimizer. Therefore there is no second, lower-volume one-cut solution with the same prescribed centre. ∎

At an active cut the derivative has the useful positive-definite form

`D²Φ(q) = (1/‖q‖) ∫_{X∩{q·x=1}} xxᵀ dA`.

For nonzero a, the affine cutting plane does not pass through zero, and a·x cannot vanish on its entire open section unless a=0. Thus the displayed quadratic form is positive definite. This supports a local interval-Newton certificate after a numerical nomination, but no such JOINT75 certificate is credited in this result.

### Consequence for the actual JOINT75 bridge

Let K be the literal75-point parent, let c₀ be its own centroid, and let

`O = conv(K ∪ {the six literal bridge points})`.

Because K⊂O and g(K)=c₀, K is a feasible competitor in the theorem. The unique centroid-restoring one-cut body L* therefore satisfies

`vol(K) ≤ vol(L*) ≤ vol(O)`.

The parent reports bridge growth of approximately38.0168253325%. Hence the theorem permits restoring c₀ by one physical cut while deleting no more than

`(vol(O)−vol(K))/vol(O)`,

approximately27.55% of the bridge body's volume. This is a rigorous bound expressed by exact volumes; the decimal is only a rendering of the parent's reported growth.

The conclusion is **not** that L* retains K, the elder vertex, or the six bridge points. The optimizer may replace old material as well as remove added material. That distinction is precisely useful here: keeping the complete old body and adding a reference-centre chain is not the only available physical construction.

There is also a useful restriction. Once O and c₀ are fixed, there is no alternative proper one-cut body at c₀ obtained merely by choosing a different orientation or offset. If the unique cut has the wrong true E or the wrong equilibrium landscape, the next construction must change the outer body, use additional cuts or replacements, or allow a different own centroid. The original problem does not require c₀, so the last option remains legitimate.

## 2. Exact finite dual bounds, including mandatory route material

The theorem gives a rational certificate even when the exact minimizing q is unknown.

For any rational trial q, set Cq=O∩{q·(x−c)≤1}. If Vq and Mq are its exact volume and raw first moment, then

`Φ_O(q) = Vq − q·(Mq−cVq)`.

Every centred subset L⊂O satisfies

`vol(L) ≤ Φ_O(q)`.

This is an exact upper bound for **every trial q**, not merely for an optimizer. A small centroid residual is not silently substituted for zero. For the JOINT75 bridge the exact invariant

`Φ_O(q) ≥ vol(K)`

must hold for every q, because the old parent K is feasible. It is a useful audit against false numerical optimality or incorrectly integrated moments.

### Mandatory core

Let W⊂O be material that must remain. For example, with the parent's current P component

`J = [22,26,30,34,37,41,44,48,49,50,52,54,55,58,59,62,64,68,70]`,

one natural replacement core is

`W = conv({P_i : i∉J} ∪ {the six bridge points})`.

Every convex modification that retains those points and remains inside O must contain W. This includes arbitrary new vertices and arbitrary repositioning of the nineteen discarded points inside O; it is not limited to a fixed triangulation.

For f_q(x)=1−q·(x−c), any uniform centred K′ with W⊂K′⊂O obeys

`vol(K′) ≤ Ψ_W(q)`

where

`Ψ_W(q) = V_W − q·(M_W−cV_W) + Φ_O(q) − Φ_W(q)`.

Indeed, integrate f_q over mandatory W, and bound its integral on optional material O∖W by the positive part. Therefore either of the following exact rational inequalities is a sufficient obstruction:

`Φ_O(q) < V_W`, or the potentially stronger `Ψ_W(q) < V_W`.

Such an inequality would exclude centring at c for the **specified retained-material envelope**, even allowing nonconvex measurable optional material. It would not exclude deleting further old material, moving the route, leaving O, changing the metric, or seeking an own110 body at a different centroid.

No evaluated JOINT75 inequality of this kind is claimed here. The supplied program reconstructs W and evaluates both bounds at an explicit rational trial.

### Own-centred equilibrium bounds over a whole material envelope

The same envelope supports direct equilibrium certificates without pretending that the centre is fixed. For any affine function ℓ and δ=V_O−V_W,

`∫_W ℓ + δ min(0,min_O ℓ) ≤ ∫_{K′} ℓ ≤ ∫_W ℓ + δ max(0,max_O ℓ)`.

All quantities are rational for rational polyhedra; extrema of ℓ occur at vertices.

For a common vertex v and an outer vertex w, take

`ℓ_{v,w}(x) = (v−x)·(w−v)`.

Strictly negative upper bounds for every w≠v prove that v is strict U at the **actual** centroid of every K′ in the envelope. The inequalities cover all directions toward O, hence all directions toward K′.

For a common maximal polygonal facet with outward normal n and an oriented boundary edge a→b, take

`ℓ_{a,b}(x) = (n×(b−a))·(x−a)`.

Strictly positive lower bounds for all its edges prove that the projection of every actual centroid lies in the facet's relative interior, hence that the facet remains strict S.

These are scoped whole-envelope tests. I do not report a specific number of protected JOINT75 U or S witnesses without an inspectable exact execution.

## 3. Edge cost and exact rational mass correction

### The cutting plane can consume the available complexity

For a transverse cut of a convex3-polyhedron, let r be the number of deleted old vertices, f the number of completely deleted old maximal facets, and k the number of crossed true old edges. When the plane contains no old vertex or edge,

`V′=V−r+k`,
`F′=F−f+1`,
`E′=E−r+k−f+1`.

The formula follows from the new vertices on crossed edges, the new cap facet, and Euler's relation. At contacts it must be replaced by a fresh maximal-hull calculation.

For the parent's reference-bridge body with E231, a generic one-cut result stays within E249 exactly when

`k−r−f ≤ 17`.

The one-cut theorem does not impose this inequality. A cap with many boundary vertices also creates a genuine large polygon; independently rounding its vertices can destroy that coplanarity and introduce additional true edges.

### Exact repair after rationalizing a useful material replacement

Suppose a rational replacement is close to a desired moment and has k independent triangular vertex stars. No maximal boundary triangle may contain two selected vertices, and selected stars must not acquire hidden polygon-planarity constraints.

For a star with moving vertex v_i and consistently oriented link pairs (p_j,q_j), define

`a_i = Σ(p_j×q_j)/6`,
`B_i = Σ (p_j+q_j)(p_j×q_j)ᵀ/24`,
`τ_i = a_i·v_i`.

Its signed volume is a_i·v_i and its first moment is

`(a_i·v_i)v_i/4 + B_i v_i`.

Consequently, displacements d_i satisfying each a_i·d_i=0 give the exact finite identities

`ΔV=0`,
`ΔM=Σ(τ_i I/4+B_i)d_i`.

The moment repair is a rational linear system with k+3 constraints in3k coordinates. A full-row-rank current matrix has2k−3 free directions. Rank and a formal solution are not enough: the new maximal hull, all support inequalities, polygon planarity, and the complete own-centred mechanics must still be checked.

For a proposed rational segment, these checks can be made interval-complete. Under the stated independent-star assumptions, cleared support and equilibrium predicates are low-degree polynomials. On[0,1], for a polynomial a(t)=Σ a_j t^j of degree n, the Bernstein coefficients are

`b_k = Σ_{j≤k} a_j binom(k,j)/binom(n,j)`.

Strict positivity of every coefficient certifies positivity throughout the closed segment. For a feature claimed not to be a closed equilibrium, one must certify at least one violated closed constraint throughout the segment; a standalone zero or a small numerical residual is not a certificate.

No selected JOINT75 star pack, rank receipt, displacement, or continuous-census certificate is promoted from the uninspectable computations. The identity is retained as the exact repair mechanism for a future finite replacement, not as a claimed cancellation.

## 4. A fully specified exact mass-control regression

A small control makes the one-cut assertion and equal-level barcode handling testable without any missing source.

Take

`O_box=[−1,3]×[−2,2]×[−3,3]`,
`L_box=O_box∩{x₁≤1}=[−1,1]×[−2,2]×[−3,3]`.

The outer volume is96, first moment(96,0,0), centroid(1,0,0). The cut volume is48, first moment zero, centroid zero. For c=0 and q=(1,0,0), Φ(q)=48 and ∇Φ(q)=0. The theorem proves that L_box is the unique maximum-volume uniform subset of O_box with centroid zero.

Both bodies have true V/E/F=8/12/6, C24, strict S/U/H=6/8/12 and additional weak000 at their respective own centroids. Every face foot is in the relative interior, every vertex has three strictly negative outgoing radial dots, and every edge projection is interior with both normal-cone coefficients positive. These bodies are regression controls, **not** candidate110 constructions or exceptions to any minimum bound for110.

Every positive relative squared-radius bar is as follows:

```text
O_box, centred at (1,0,0):
P = [9/17,4/17,4/17,4/17,4/17,4/17,4/17]
Q = [1/2,1/2,1/2,4/13,4/13]

L_box, centred at (0,0,0):
P = [9/14,2/7,2/7,1/14,1/14,1/14,1/14]
Q = [4/5,1/5,1/5,1/10,1/10]
```

For L_box all vertex births are14. Four x-edge mergers occur at13, two y-direction mergers at10, and the final z-direction merger at5. Its polar vertices are ±e₁, ±e₂/2, ±e₃/3; their relevant connection levels are1/5 and1/10. This proves the displayed ledger, including its equal-level multiplicities. The outer box follows by using centred half-widths(2,2,3).

## 5. Complete standalone recovery and auditing source

The following source uses only the Python standard library, Python3.10 or newer. It contains all75 parent rows, the six bridge points, the complete current P component, exact maximal-facet reconstruction, true edges, two-origin volume/moment checks, strict and closed-weak S/U/H predicates, and a **simultaneous-level** radial merge implementation. No tiny positive bar is discarded.

The default command audits the two box controls. The JOINT75 command additionally reconstructs the literal parent and reference bridge, audits the bridge at both its own centroid and the old parent centroid, and audits four explicit finite replacement recipes. Their new equilibrium classes are deliberately not asserted in advance.

The trial q below is merely a retained rational experiment input. It is **not claimed to be the exact optimum or an observed successful numerical nomination**. The conical trial is likewise an explicit recipe, not an accepted endpoint. The program computes their actual mass, maximal complexity, and every positive bar.

```sh
python exact_replacement42.py --out box42.json
python exact_replacement42.py --joint75 --out joint75_replacement42.json
```

Conditional terminal markers are `BOX_CENTROID_CUT_EXACT_PASS`, `JOINT75_INPUT_RECONSTRUCTION_PASS`, and `JOINT75_RECIPES_EXACT_AUDIT_FINISHED`. The program prints the generated report's byte count and SHA-256. **These are reconstruction commands and expected markers, not observed execution receipts.** No source or output hash is invented here.

```python
from fractions import Fraction as F
from itertools import combinations, product, groupby
from functools import reduce
from collections import deque
from math import gcd, lcm
from pathlib import Path
import argparse, hashlib, json, sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

D = 10000000
I75 = [
[-11310213,-3802031,232661],[-11269293,-2834032,-2182730],
[-10855182,-2246500,-3911998],[-10128821,-1814868,-5467871],
[-9452382,-6834502,6456555],[-9308206,-1555414,-6662777],
[-8712882,-8006246,8846843],[-8693078,-1373304,-7380329],
[-7797905,-1286403,-8181129],[-6681453,-1307873,-8916622],
[-6352338,2020313,-1146993],[-5892536,2295258,-71116],
[-5592263,2241235,541206],[-5425338,-1474781,-9487378],
[-5280741,2171200,1073969],[-4959361,3312877,-1863739],
[-4453446,1994305,2115702],[-4311479,345947,4048866],
[-4305575,1694912,2608464],[-4237167,1203950,3206121],
[-3820955,4252385,-2139686],[-3661038,4074852,-884602],
[-3623465,-1644023,-10021566],[-3190033,811977,3827673],
[-3155609,4102561,85230],[-3074935,4483432,-2851622],
[-2953571,-1851896,-10161171],[-2718323,668005,3934224],
[-2651732,122199,4295157],[-2302445,4621821,-3324860],
[-2248430,-2037367,-10247983],[-2145336,4388373,461753],
[-1938256,3964861,1093487],[-1561887,3760992,1454978],
[-1502148,-2223378,-10275715],[-1278721,4758931,-3663608],
[-1049751,3727821,1606020],[-740759,-2457388,-10231458],
[-298044,4806779,-3669461],[-159770,3872224,1576892],
[-121991,838112,3483867],[39249,-2666243,-10115526],
[91753,589879,3521150],[725989,729286,3291554],
[822613,-2865673,-9923443],[847151,1601384,2948252],
[1257541,4150503,1429262],[1400720,4852019,-3212547],
[1599055,-3043575,-9655675],[2331916,-2317243,-9420429],
[2351892,-3267823,-9302290],[2947803,5018418,-438633],
[3091632,-3449326,-8871363],[3252567,4572542,973174],
[3518927,-4445832,-8207140],[3801752,-3598386,-8365506],
[3886092,3932529,1241770],[4317265,3420766,1352627],
[4466143,-3720508,-7791824],[4524082,-5334292,-6695320],
[4622668,3053371,1323427],[4905967,2678528,1274548],
[5061533,-3853293,-7158199],[5166891,2298083,1206990],
[5506198,-4926808,-5369878],[5525767,-801605,-6004784],
[5644371,1606910,926729],[6018142,937609,612094],
[6137534,-4326615,-4182924],[6330239,239389,230320],
[6547165,-3582767,-3087182],[6574260,-489010,-228500],
[6738672,-1246564,-776981],[6751376,-2814918,-2197016],
[6805726,-2026966,-1429050]]
A6 = [
[54523165,-66300276,-55391279],
[49842012,-91287749,-32456638],
[35949856,-110325885,-5024889],
[13236236,-120608734,24070669],
[-16841661,-119820327,51618679],
[-51605841,-106402263,74185541]]
J19 = [22,26,30,34,37,41,44,48,49,50,52,54,55,58,59,62,64,68,70]
PARENT_SHA = 'f996fa67a06c542cbe559aadce39ce5f7b2f06b81a609a4a55dd3f03d9291605'

class Degenerate(ValueError):
    pass

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def primitive(a):
    g = reduce(gcd,(abs(x) for x in a),0)
    return tuple(x//g for x in a) if g else None

def polygon(ids,P,n):
    drop = max(range(3),key=lambda k:abs(n[k]))
    u,v = [k for k in range(3) if k != drop]
    ids = sorted(ids,key=lambda i:(P[i][u],P[i][v]))
    def turn(i,j,k):
        return ((P[j][u]-P[i][u])*(P[k][v]-P[i][v])
               -(P[j][v]-P[i][v])*(P[k][u]-P[i][u]))
    def half(seq):
        a=[]
        for i in seq:
            while len(a)>1 and turn(a[-2],a[-1],i)<=0:
                a.pop()
            a.append(i)
        return a
    f=half(ids)[:-1]+half(reversed(ids))[:-1]
    assert len(f)>=3
    if dot(cross(sub(P[f[1]],P[f[0]]),sub(P[f[2]],P[f[0]])),n)<0:
        f.reverse()
    k=f.index(min(f))
    return f[k:]+f[:k]

def mass(P,faces):
    V=F(0); M=[F(0)]*3; area=[F(0)]*3
    triangles=[]
    for f in faces:
        for j in range(1,len(f)-1):
            a,b,c=[P[i] for i in (f[0],f[j],f[j+1])]
            triangles.append((a,b,c))
            w=det(a,b,c)/6
            V+=w
            for k in range(3): M[k]+=w*(a[k]+b[k]+c[k])/4
            nn=cross(sub(b,a),sub(c,a))
            area=[area[k]+nn[k] for k in range(3)]
    assert V>0 and area==[0,0,0]
    o=tuple(sum(p[k] for p in P)/len(P) for k in range(3))
    VV=F(0); MM=[F(0)]*3
    for a,b,c in triangles:
        w=det(sub(a,o),sub(b,o),sub(c,o))/6
        assert w>0
        VV+=w
        for k in range(3): MM[k]+=w*(o[k]+a[k]+b[k]+c[k])/4
    assert VV==V and MM==M
    return V,tuple(M),tuple(x/V for x in M)

def hull(points):
    P=sorted(set(tuple(F(x) for x in p) for p in points))
    if len(P)<4 or not any(det(sub(P[i],P[0]),sub(P[j],P[0]),
                             sub(P[k],P[0]))
                           for i,j,k in combinations(range(1,len(P)),3)):
        raise Degenerate('The input is not full-dimensional')
    HP=[]
    for p in P:
        d=lcm(*(x.denominator for x in p))
        HP.append(tuple(int(x*d) for x in p)+(d,))
    planes=set()
    for inds in combinations(range(len(P)),3):
        rows=[HP[i] for i in inds]
        vv=[]
        for j in range(4):
            a=[tuple(r[k] for k in range(4) if k!=j) for r in rows]
            vv.append((-1 if j%2 else 1)*det(*a))
        if not any(vv[:3]): continue
        a=primitive((vv[0],vv[1],vv[2],-vv[3]))
        pos=neg=False
        for p in HP:
            s=a[0]*p[0]+a[1]*p[1]+a[2]*p[2]-a[3]*p[3]
            pos=pos or s>0; neg=neg or s<0
            if pos and neg: break
        if pos and neg: continue
        if pos: a=tuple(-x for x in a)
        planes.add(a)
    planes=sorted(planes)
    faces=[]
    for a in planes:
        ids=[i for i,p in enumerate(HP)
             if a[0]*p[0]+a[1]*p[1]+a[2]*p[2]==a[3]*p[3]]
        faces.append(polygon(ids,P,a[:3]))
    keep=sorted(set(i for f in faces for i in f))
    remap={i:j for j,i in enumerate(keep)}
    P=[P[i] for i in keep]
    faces=[[remap[i] for i in f] for f in faces]
    owners={}
    for k,f in enumerate(faces):
        for i,j in zip(f,f[1:]+f[:1]):
            owners.setdefault(tuple(sorted((i,j))),[]).append(k)
    edges=sorted(owners)
    assert all(len(owners[e])==2 for e in edges)
    assert len(P)-len(edges)+len(faces)==2
    assert sum(map(len,faces))==2*len(edges)
    V,M,g=mass(P,faces)
    assert all(dot(a[:3],g)<a[3] for a in planes)
    return dict(points=P,planes=planes,faces=faces,edges=edges,
                edge_faces=[owners[e] for e in edges],
                V=len(P),E=len(edges),F=len(faces),C=2*len(edges),
                volume=V,moment=M,centroid=g)

def mechanics(K,c):
    P=K['points']; faces=K['faces']; planes=K['planes']; edges=K['edges']
    nb=[set() for _ in P]
    for i,j in edges: nb[i].add(j); nb[j].add(i)
    strict=[[],[],[]]; weak=[[],[],[]]; zeros=[0,0,0]
    def record(kind,label,z):
        zeros[kind]+=sum(t==0 for t in z)
        if all(t>0 for t in z): strict[kind].append(label)
        elif all(t>=0 for t in z): weak[kind].append(label)
    for fi,f in enumerate(faces):
        n=planes[fi][:3]
        z=[dot(cross(n,sub(P[j],P[i])),sub(c,P[i]))
           for i,j in zip(f,f[1:]+f[:1])]
        record(0,fi,z)
    for i in range(len(P)):
        record(1,i,[-dot(sub(P[i],c),sub(P[j],P[i])) for j in sorted(nb[i])])
    for (i,j),(f,g) in zip(edges,K['edge_faces']):
        p=sub(P[i],c); d=sub(P[j],P[i]); dd=dot(d,d); t=-dot(p,d)
        R=tuple(p[k]*dd+t*d[k] for k in range(3))
        n=planes[f][:3]; m=planes[g][:3]
        aa=dot(n,n); ab=dot(n,m); bb=dot(m,m)
        assert aa*bb-ab*ab>0
        z=[t,dd-t,bb*dot(R,n)-ab*dot(R,m),aa*dot(R,m)-ab*dot(R,n)]
        record(2,[i,j],z)
    return dict(strict=list(map(len,strict)),additional_weak=list(map(len,weak)),
                primitive_zero=zeros,S=strict[0],U=strict[1],H=strict[2],
                weak_S=weak[0],weak_U=weak[1],weak_H=weak[2])

def gate(u,v):
    a=dot(u,u); b=dot(u,v); c=dot(v,v); d=a+c-2*b
    if d==0: return a
    if b>=a: return a
    if b>=c: return c
    return (a*c-b*b)/d

def bars(P,edges):
    edges=sorted(set(tuple(sorted(e)) for e in edges))
    birth=[dot(p,p) for p in P]
    weights={e:gate(P[e[0]],P[e[1]]) for e in edges}
    parent=list(range(len(P))); peak=list(range(len(P)))
    members=[{i} for i in range(len(P))]
    def find(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]; i=parent[i]
        return i
    def path(s,t,level):
        adj=[[] for _ in P]
        for i,j in edges:
            if weights[(i,j)]>=level:
                adj[i].append(j); adj[j].append(i)
        prev={s:None}; todo=deque([s])
        while todo and t not in prev:
            i=todo.popleft()
            for j in sorted(adj[i]):
                if j not in prev: prev[j]=i; todo.append(j)
        assert t in prev
        out=[]; i=t
        while i is not None: out.append(i); i=prev[i]
        return out[::-1]
    out=[]
    ranked=sorted(edges,key=lambda e:(-weights[e],e))
    for level,ee in groupby(ranked,key=lambda e:weights[e]):
        adj={}
        for i,j in ee:
            a,b=find(i),find(j)
            if a!=b:
                adj.setdefault(a,set()).add(b); adj.setdefault(b,set()).add(a)
        unseen=set(adj)
        groups=[]
        while unseen:
            start=min(unseen); cc={start}; todo=[start]; unseen.remove(start)
            while todo:
                a=todo.pop()
                for b in adj[a]:
                    if b in unseen: unseen.remove(b); cc.add(b); todo.append(b)
            groups.append(sorted(cc))
        for cc in groups:
            elder=max(cc,key=lambda a:(birth[peak[a]],-peak[a]))
            for a in cc:
                if a==elder or birth[peak[a]]==level: continue
                assert birth[peak[a]]>level
                comp=members[a]
                cut=[e for e in edges if (e[0] in comp)!=(e[1] in comp)]
                assert cut and max(weights[e] for e in cut)==level
                pp=path(peak[a],peak[elder],level)
                assert min(weights[tuple(sorted(e))] for e in zip(pp,pp[1:]))==level
                out.append(dict(peak=peak[a],elder=peak[elder],birth=birth[peak[a]],
                    death=level,depth=(birth[peak[a]]-level)/birth[peak[a]],
                    component=sorted(comp),cut=cut,
                    attaining_edge=next(e for e in cut if weights[e]==level),
                    attaining_path=pp))
            allmembers=set().union(*(members[a] for a in cc))
            for a in cc: parent[a]=elder
            members[elder]=allmembers
    assert len({find(i) for i in range(len(P))})==1
    return sorted(out,key=lambda b:(-b['depth'],b['peak'],b['elder']))

def audit(points,name,reference=None):
    K=hull(points)
    c=K['centroid'] if reference is None else tuple(map(F,reference))
    assert all(dot(a[:3],c)<a[3] for a in K['planes'])
    K.update(mechanics(K,c))
    P=[sub(p,c) for p in K['points']]
    Q=[tuple(F(n,a[3]-dot(a[:3],c)) for n in a[:3]) for a in K['planes']]
    K['P_bars']=bars(P,K['edges']); K['Q_bars']=bars(Q,K['edge_faces'])
    if not any(K['additional_weak']):
        s,u,h=K['strict']
        assert s+u-h==2
        assert len(K['P_bars'])==u-1 and len(K['Q_bars'])==s-1
    K.update(name=name,equilibrium_center=c,own_centred=c==K['centroid'],density=1)
    return K

def clip_points(K,n,h):
    P=K['points']; s=[dot(n,p)-h for p in P]
    out=[p for p,v in zip(P,s) if v<=0]
    for i,j in K['edges']:
        if s[i]*s[j]<0:
            t=s[i]/(s[i]-s[j])
            out.append(tuple(P[i][k]+t*(P[j][k]-P[i][k]) for k in range(3)))
    return sorted(set(out))

def phi(K,q,c):
    pp=clip_points(K,q,1+dot(q,c))
    try: L=hull(pp)
    except Degenerate: return F(0)
    return L['volume']-dot(q,sub(L['moment'],tuple(x*L['volume'] for x in c)))

def run(joint):
    O=audit(list(product((-1,3),(-2,2),(-3,3))),'O_BOX')
    L=audit(clip_points(O,(F(1),F(0),F(0)),F(1)),'L_BOX')
    assert O['volume']==96 and O['moment']==(96,0,0)
    assert L['volume']==48 and L['moment']==(0,0,0)
    for K in (O,L):
        assert [K[k] for k in ('V','E','F')]==[8,12,6]
        assert K['strict']==[6,8,12] and K['additional_weak']==[0,0,0]
    assert [b['depth'] for b in O['P_bars']]==[F(9,17)]+[F(4,17)]*6
    assert [b['depth'] for b in O['Q_bars']]==[F(1,2)]*3+[F(4,13)]*2
    assert [b['depth'] for b in L['P_bars']]==[F(9,14)]+[F(2,7)]*2+[F(1,14)]*4
    assert [b['depth'] for b in L['Q_bars']]==[F(4,5)]+[F(1,5)]*2+[F(1,10)]*2
    assert phi(O,(F(1),F(0),F(0)),(F(0),)*3)==48
    report=dict(box_outer=O,box_cut=L)
    print('BOX_CENTROID_CUT_EXACT_PASS')
    if not joint: return report
    assert len(I75)==75 and len(A6)==6
    P=[tuple(F(x,D) for x in p) for p in I75]
    A=[tuple(F(x,100000000) for x in p) for p in A6]
    K=audit(P,'JOINT75_LITERAL_PARENT')
    c=tuple(F(x,301728380651199510841280000000) for x in
       (-53286920506055854442174018051,-42633799180986064597953397917,
        -43819041531080084398689329023))
    assert K['volume']==F(942901189534998471379,750000000000000000000)
    assert K['centroid']==c
    assert [K[k] for k in ('V','E','F')]==[75,219,146]
    assert K['strict']==[2,2,2] and K['additional_weak']==[0,0,0]
    print('JOINT75_INPUT_RECONSTRUCTION_PASS')
    O=audit(P+A,'SIX_POINT_BRIDGE_OWN')
    R=audit(P+A,'SIX_POINT_BRIDGE_OLD_CENTRE',reference=c)
    assert [O[k] for k in ('V','E','F')]==[79,231,154]
    assert O['strict']==[15,32,45] and O['additional_weak']==[0,0,0]
    assert R['strict'][1]==1
    core=[p for i,p in enumerate(P) if i not in set(J19)]
    C=audit(core,'CORE56_TRIAL')
    W=audit(core+A,'REPLACEMENT62_TRIAL')
    q=tuple(F(x,10**9) for x in (-52962533,-2728027519,-562522899))
    T=audit(clip_points(O,q,1+dot(q,c)),'CUT_Q_TRIAL')
    po=phi(O,q,c); pw=phi(W,q,c)
    psi=W['volume']-dot(q,sub(W['moment'],tuple(x*W['volume'] for x in c)))+po-pw
    assert po>=K['volume']
    n=tuple(F(x,10**9) for x in (97906953,-980480683,170504715))
    h=dot(n,c)-F(162905599,10**9)
    cp=clip_points(O,n,h)+[A[4]]
    try: cone=audit(cp,'CONE_A4_TRIAL')
    except Degenerate: cone=dict(name='CONE_A4_TRIAL',full_dimensional=False)
    report.update(parent_result_sha256=PARENT_SHA,parent=K,bridge_own=O,
        bridge_old_centre=R,core56=C,replacement62=W,trial_cut=T,trial_cone=cone,
        dual=dict(q=q,target=c,Phi_O=po,Phi_W=pw,Psi_W=psi,
            old_parent_feasible_lower_bound=K['volume'],
            retained_core_excluded_by_Phi=po<W['volume'],
            retained_core_excluded_by_Psi=psi<W['volume'],
            trial_cut_relative_moment=sub(T['moment'],tuple(x*T['volume'] for x in c))))
    print('JOINT75_RECIPES_EXACT_AUDIT_FINISHED')
    return report

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--joint75',action='store_true')
    ap.add_argument('--out',default='replacement42.json')
    args=ap.parse_args()
    result=run(args.joint75)
    text=json.dumps(result,sort_keys=True,separators=(',',':'),default=str)+'\n'
    data=text.encode('utf-8')
    Path(args.out).write_bytes(data)
    print('EXACT_REPORT_BYTES_SHA256',len(data),hashlib.sha256(data).hexdigest())
```

The program deliberately derives facet indices anew. Its facet IDs are not promised to equal those of the parent's auditor. It retains material vertex coordinates and full face polygons, so correspondence is recoverable without renaming facets by guesswork. For every audited body, actual raw volume and first moment, own centroid, strict and additional closed-weak census, maximal face/edge structure, and every positive P/Q component, cut, birth, death, and attaining path are written to the report.

## 6. Strongest conclusion and continuation

The six-point reference bridge does **not** face an unrestricted impossibility of physical centroid restoration: a finite one-cut restoration to the old centroid always exists, and its retained volume is at least the original parent volume. What remains consequential is whether that unique truncation preserves useful route material and the opposite landscape while respecting E249.

The sharper next physical question is therefore not simply whether mass can be balanced. It is **which route vertices and old carrier material may survive the balancing operation**. The retained-core dual bound provides an exact way to reject an overconstrained choice; it does not require assuming a fixed equilibrium root. The independent-star identity provides an exact rational correction after a promising finite replacement, provided its current geometry really admits those stars.

No uninspectable candidate is a durable successor to JOINT75 in this handoff. The durable additions are the finite one-cut existence/uniqueness/optimality proof, the mandatory-material dual and own-centred envelope tests, the exact box controls, and a complete source-only experiment/audit unit containing the literal JOINT75 input. The joint own110, weak000, E≤249 cancellation remains unestablished by this continuation.
