# figure-0491

Historical AI scientific report · saved 2026-09-22 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Clear Willow 56 — an actual-mass descent cone for the complete C186 polar bar

## Outcome and verification status

No strict110/additionalweak000 construction is verified in this handoff.

The durable advance is a **mass-coupled, three-dimensional local descent theorem for the unique unwanted polar persistence bar of C186_OBLIQUE_APEX_U1_211**. Insert a point just beyond the two nonstable facets incident to physical edge 14–15. Every strictly outward direction in this two-facet visibility cone decreases the bar to first order, while a sufficiently small insertion preserves strict211 and additionalweak000 at the new actual uniform-volume centroid. The deformation lowers the polar birth and raises its death simultaneously. It does not merely open one primitive arrow.

This releases the planar-base restriction. The resulting local hull has V34/E96/F64, C192. A deterministic, entirely rational constructor and exhaustive auditor are supplied below. They select a finite strict211 witness with a strictly smaller complete polar bar by dyadic search. **The constructor's finite δ, output byte counts, and SHA-256 receipts have not been observed in the restored executor context. No computed C192 endpoint is entered as an independently replayed successor here.** The proved descent cone and complete recovery source are the deliverables.

Submitted numerical work included reciprocal metric descent, actual-mass free-vertex descent, positive-chord U repair, and polar-forest reconstruction. The returned checkpoint and audit payloads from those submissions are unavailable in the retained context. No optimum, census, or exclusion is inferred from those missing outputs.

## Source authority and context limitation

The exact parent is `figure-0487`, SHA-256 `5899754f372a6a6c9505e188fb34f224c3c3c828a0077ce3556c5cb4341cf428`. Its literal C186 rows, parameters, maximal-facet convention, and strict211 census are the authority used here. The parent has S facets 15 and 31, U vertex 31, H edge 15–16, and a single Q bar with peak31, elder15, and death true edge15–46. The two appearances of index31 refer to different objects: physical vertex T and polar vertex corresponding to physical facet31. 

The retained context contains the journal and literal parent narrative and records the earlier complete reading of the Python source units. It does not contain readable returned bodies for the six decoded JSON units `OBLIQUE_APEX_BEST_15.json`, `GATE_BEST_7_7.json`, `EXPECTED.json`, `GATE_ROWS.json`, `C186_INPUT.json`, and `NUMERICAL_RECEIPTS.json`. Their read commands were submitted, but I do not certify their full returned contents as read in this restored context. None is a hidden dependency of the theorem or recovery unit below: all required C186 data are repeated literally.

There is also an arithmetic correction to the branch summary: E93 leaves **156**, not 152, edge slots under E≤249. The C192 stellation described here leaves 153. The literal incidence E93, rather than the summary's headroom number, is authoritative. 

## 1. Exact parent and the selected geometric patch

Let the parent's physical vertices be P0,…,P32, already at their actual homogeneous centroid zero. T=P31 and D=P32. The top facets are `(31,i,i+1)` and the bottom facets `(32,i+1,i)`, with base indices modulo31.

Choose the physical edge

`e = {14,15}`, with positive orientation `P15 → P14`,

and let

`m = (P14+P15)/2`.

Its two incident facets are

`fT = 14 = (T,P14,P15)`,

`fD = 45 = (D,P15,P14)`.

Both are nonstable. Neither is one of the stable carriers15/31, and neither is a carrier of H edge15–16, whose owners are facets15 and46. Thus the stable peak, elder, and saddle carriers can all remain geometrically unchanged while the actual mass moves.

Write the outward, unnormalized plane equations of fT and fD as

`nT·x = hT`, `nD·x = hD`,

where normals are the oriented cross products of the corresponding triangle edges. Because the parent is own-centred and the origin is interior, hT,hD>0.

For a direction u satisfying

`wT = nT·u > 0`, `wD = nD·u > 0`,

insert

`x(t) = m + t u`, with t>0 sufficiently small.

The inserted point sees exactly fT and fD. The complete new maximal hull consists of all old facets except14 and45, together with

`(T,14,x)`, `(T,x,15)`, `(D,15,x)`, `(D,x,14)`.

It deletes edge14–15 and adds four edges from x to14,15,T,D. Consequently V increases by1, E by3, and F by2. In the recovery code, the old vertex labels0,…,32 are retained and the new vertex is33.

The resulting combinatorial bipyramid has a generally nonplanar base cycle. It is not covered by either of the previously closed fixed-15-gon height charts.

## 2. Exact actual-mass map over the whole local visibility cell

Let V0 be the parent's volume, and define

`ZT = 3m+T`, `ZD = 3m+D`.

For a general displacement s=x−m within this two-facet visibility cell, put

`A = (nT+nD)/6`,

`L = (ZT nTᵀ + ZD nDᵀ)/24`.

The actual volume and first moment of the inserted hull are exactly

`V(s) = V0 + A·s`,

`M(s) = Ls + (A·s)s/4`,

and its actual centroid is

`c(s) = M(s)/V(s)`.

These are not adjustable-centre equations. They follow by adding the two positive tetrahedra between the inserted point and the visible parent triangles. For a triangle with outward normal n, its added volume is `n·s/6`; its first moment is that volume times the mean of its four vertices.

Along s=tu,

`c′(0) = [wT ZT + wD ZD]/(24 V0)`.

Thus all first-order mass motions generated by the strictly outward insertion cone lie in the positive cone spanned by ZT and ZD. This provides a particularly simple way to couple a geometric modification to its actual mass effect.

## 3. Full-bar derivative, rather than a primitive-arrow derivative

Let

`q = Q31`

be the parent's normalized supporting functional of the unwanted stable facet31. Thus its raw supporting equation is q·x=1.

Let r be the perpendicular foot of the origin on physical edge15–16. Since this is the strict H edge, r is in the edge's relative interior and in the positive cone of its two adjacent facet normals. Put `R=|r|²`.

As long as the two stable roots, their order, and this saddle remain active, the unique polar bar has

`birth β(c) = |q|²/(1−q·c)²`,

`death γ(c) = 1/dist(c,aff(P15,P16))²`.

The second identity is exact chord-min duality. If the physical saddle foot is a positive combination of the two normalized adjacent normals, dividing that foot by its squared norm gives the perpendicular foot on the corresponding polar true edge. Its squared norm is the reciprocal physical saddle radius.

For `ell = log(β/γ)`, differentiation at the parent gives

`ell′(0) = 2 c′(0)·(q − r/R)`.

In particular, if both ZT and ZD satisfy

`q·Z < 0` and `r·Z > 0`,

then every strictly outward insertion direction lowers the birth and raises the death. Therefore it strictly decreases both β/γ and the birth-relative depth `1−γ/β` of the complete bar.

This argument concerns the unique positive true-edge H0 bar. It is independent of which noncritical primitive arrows happen to be zero. Internal tied levels or changes of the packet boundary do not invalidate the birth/death calculation while the stated critical carriers and their pairing persist. The recovery audit nevertheless reconstructs the full tied-level component, cut, and attaining path at its finite witness.

## 4. Exact C186 sign certificate and quantitative descent rate

For the literal C186 input and m=(P14+P15)/2, the useful exact inequalities are

`P15·(P14−P15) > 1/1000`,

`q·ZT < −5/4`, `q·ZD < −5/4`,

`r·ZT > 2/5`, `r·ZD > 1`,

`0 < R < 2/5`.

The source below recomputes all of these with rational arithmetic. They also admit comfortable hand bounds, rather than relying on a near-zero floating sign.

For example, write the parent's base-plane height as z0. It lies between1/10 and103/1000. The positive escape of base vertex0 to T, together with ordinary crossing and the two supporting edges at base vertex0, places T's planar coordinates in `(0.99,1.01)×(−0.01,0.01)`. The first coordinate bound follows because base vertex0 has negative exits to its two planar neighbors and D, so its exit to T must be positive. The crossing point is within0.0011 of the maximal x support, and the two adjacent edge slopes bound its y coordinate. The mass-closed formulas then place p=−3c inside `(-0.42,-0.36)×(-0.075,-0.03)`.

The saddle foot satisfies

`−61/100 < r_x < −59/100`,

`11/100 < r_y < 13/100`,

`1/10 < r_z < 103/1000`.

Also `3m_xy=(-1.257252345,2.05937547)`. These intervals immediately give `r·ZT>2/5` and `r·ZD>1`; the latter uses the exact identity `3z0+zD=−ηa=−0.00028`.

For the stable-facet inequalities, take its planar edge normal

`n0=(0.27801891,0.08659790)`.

Its bottom-cap numerator is `(ηb n0,−gD)`, where `gD>19/50`, and its support h satisfies `0<h<2/25`. Directly,

`n0·(3m_xy+(1,0)) < 11/100`.

Consequently the unnormalized numerator of q·ZD is less than

`(203/500)(11/100) − 4(1/10)(19/50) < −1/10`,

so q·ZD<−5/4. Ordinary crossing gives q·T<q·D=1, hence q·ZT<q·ZD as well.

Substitution into the bar derivative yields the quantitative bound

**`ell′(0) < −(9 wT + 15 wD)/(48 V0) < 0`.**

This is a whole-cone certificate, not a sampled angular search. For every fixed strictly outward u there is an ε(u)>0 for which the resulting own-centred C192 bodies remain strict211/additionalweak000 and their unique polar bar is strictly smaller than the parent's. Uniform ε can also be taken on a compact set of normalized directions staying strictly inside the two inequalities wT,wD>0.

## 5. Why the local census remains strict211/weak000

The physical U argument has explicit true-edge witnesses. The old positive edge P15→P14 is replaced by P15→x and x→P14. At t=0,

`P15·(m−P15) = P15·(P14−P15)/2 > 0`,

and

`m·(P14−m) > 0`.

All other selected positive physical escapes persist. T's exit to the new point is negative at t=0 because m is a convex combination of two vertices toward which T already has strict negative exits. The actual centroid displacement tends to zero, so these strict signs survive for sufficiently small t. There is exactly one physical U and no additional weak-U.

The projections onto the two removed facet planes lie outside their closed triangles: both facets were nonstable and the parent was weak-free. Each new triangle converges to a subtriangle of one of those old triangles. Therefore none of the new facets is stable or additional weak-S for sufficiently small t. The two retained strict stable facets persist.

The new edges toward T and D limit to segments inside the two nonstable parent facets. A new saddle or weak edge equilibrium limiting to one of these segments would require the old facet-plane projection to lie in that facet, which it does not. The two new base-cycle edges limit to subsegments of a strictly increasing-radius edge and cannot carry a saddle. All retained edge tests persist, including the strict H on15–16. Thus the full local census is strict211/additionalweak000, not just a vertex count inferred from Euler.

No claim is made that every new primitive is nonzero. Complete normal-cone tests, not primitive nonvanishing, define the weak audit.

## 6. Consequential continuation: a quartic mass-coupled objective

This direction avoids deleting the entire old 32-vertex polar packet in one operation. It changes mass through a noncritical physical patch while retaining the peak and saddle carriers.

It also reduces the continuation to an explicit algebraic chart. Let d=P16−P15 and let Π be perpendicular projection onto d-perp. With the exact V(s),M(s) above, set

`Rpoly(s)=|V(s) r − Π M(s)|²`,

`Bpoly(s)=V(s)−q·M(s)`.

While the same critical pairing is active,

`β/γ = |q|² Rpoly(s)/Bpoly(s)²`.

Rpoly has degree at most4, and Bpoly has degree at most2. The visibility cell is given by the original facet inequalities. The actual-centred physical arrow numerators are polynomials of degree at most3 after clearing the positive volume denominator.

The useful next step is therefore to continue inside this **labelled three-dimensional point-insertion chart**, minimizing the displayed quartic ratio with actual U guards and full S/H/weak tests, rather than restarting an unconstrained height search. A zero of the formal ratio-minus-one equation is only a boundary candidate; it does not by itself prove cancellation or exclude transfer to another stable root. Primitive sign boundaries that retain a positive escape are not equilibrium boundaries.

The theorem covers the fixed C186 parent, the labelled visible pair14/45, and all sufficiently small strictly outward insertions. It does not exclude the full C186 SPD orbit, decide the entire insertion cell, or establish strict110.

## 7. Self-contained exact recovery unit

Save the following as `C186_mass_basin_descent.py`. It has no external dependencies and uses only exact standard-library arithmetic. The intended runtime is CPython3.13.5; the source does not invoke a numerical optimizer.

Commands:

```text
python -B -S C186_mass_basin_descent.py theory
python -B -S C186_mass_basin_descent.py
```

The first command reconstructs and exhaustively audits the parent and checks the exact descent certificate. The second additionally selects the first qualifying δ=2^(−k), k=8,9,…, in the radial direction u=m. Qualification requires exact visibility, the complete maximal hull, two mass computations, strict211, additionalweak000, the retained critical identities, and a strictly smaller complete polar bar.

Expected successful markers are

```text
C186_PARENT_FULL_RECONSTRUCTION_PASS
C186_OPEN_CONE_MASS_BAR_DESCENT_PASS
C192_STELLATION_211_WEAK000_FULL_AUDIT_PASS
```

The program prints the selected δ, every output's byte count and SHA-256, and its own source digest. **Those receipts are pending replay, not precomputed claims in this handoff.** Its JSON schema differs from the parent's auditor schema, so its reconstructed-parent report is not expected to have the parent's report hash.

```python
from fractions import Fraction as F
from itertools import combinations, count
from collections import defaultdict, deque
from math import lcm
from pathlib import Path
import hashlib
import json
import sys

PARENT_ID = 'figure-0487'
PARENT_SHA = '5899754f372a6a6c9505e188fb34f224c3c3c828a0077ce3556c5cb4341cf428'
ROWS = [
 (100000000,0),(91340210,27801891),(88356684,34856229),
 (82444878,45244784),(68747120,60530146),(57383111,69660774),
 (47094856,75839600),(37355250,80182208),(28037244,83139627),
 (18889672,84994455),(9629493,85859192),(-231057,85661093),
 (-10257768,84269070),(-20542525,81502612),(-33579039,75524138),
 (-50237784,61767560),(-67728196,-26639710),(-62795945,-39574309),
 (-56345784,-50085172),(-48455251,-59186378),(-39338997,-66844875),
 (-29590747,-72759225),(-19130510,-77180323),(-7832556,-80141975),
 (4377650,-81494582),(17143769,-80969795),(29622141,-78494567),
 (42668215,-73748422),(55881542,-66298645),(71482056,-53374754),
 (85294986,-35173466)
]
ZERO = (F(0), F(0), F(0))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(s,a): return tuple(s*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def pack(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):pack(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [pack(v) for v in x]
    return x

def emit(name,obj):
    b=(json.dumps(pack(obj),sort_keys=True,separators=(',',':'))+chr(10)).encode()
    Path(name).write_bytes(b)
    print(name,len(b),hashlib.sha256(b).hexdigest(),flush=True)

def parent():
    Y=[tuple(F(v,100000000) for v in r) for r in ROWS]
    cr=[Y[i][0]*Y[(i+1)%31][1]-Y[i][1]*Y[(i+1)%31][0]
        for i in range(31)]
    area2=sum(cr)
    assert area2>0
    c=tuple(sum((Y[i][j]+Y[(i+1)%31][j])*cr[i]
                for i in range(31))/(3*area2) for j in range(2))
    p=mul(-3,c)
    a=F(1,1000); b=F(1446823,1000000)
    eta=F(7,25); rho=F(24,25); tau=F(444529,25000000)
    v=(rho*(1-tau*tau)/(1+tau*tau),
       rho*2*tau/(1+tau*tau))
    assert dot(v,v)+eta*eta==1
    z0=eta*(b-a)/4
    P=[(x,y,z0) for x,y in Y]
    P.append((*add(p,mul(b,v)),eta*(3*a+b)/4))
    P.append((*sub(p,mul(a,v)),-eta*(a+3*b)/4))
    fs=[(31,i,(i+1)%31) for i in range(31)]
    fs += [(32,(i+1)%31,i) for i in range(31)]
    q=add(p,mul(b-a,v))
    for i in range(31):
        d=sub(Y[(i+1)%31],Y[i])
        assert d[0]*(q[1]-Y[i][1])-d[1]*(q[0]-Y[i][0])>0
    V=area2*eta*(a+b)/6
    assert V==F(108039116315266993463971,
                375000000000000000000000)
    return P,fs,V

def plane(P,f):
    a,b,c=[P[i] for i in f]
    n=cross(sub(b,a),sub(c,a))
    return n,dot(n,a)

def exhaustive_hull(P,fs):
    den=lcm(*(x.denominator for p in P for x in p))
    I=[tuple(int(x*den) for x in p) for p in P]
    assert len(set(I))==len(I)
    found=set()
    for i,j,k in combinations(range(len(I)),3):
        n=cross(sub(I[j],I[i]),sub(I[k],I[i]))
        if not any(n): continue
        h=dot(n,I[i])
        vals=[dot(n,p)-h for p in I]
        if min(vals)<0<max(vals): continue
        assert any(vals)
        found.add(tuple(t for t,z in enumerate(vals) if z==0))
    expected={tuple(sorted(f)) for f in fs}
    assert found==expected
    assert all(len(f)==3 for f in found)

def mass(P,fs):
    o=mul(F(1,len(P)),tuple(sum(p[j] for p in P) for j in range(3)))
    V=F(0); M=ZERO
    VD=[F(0)]*3
    MD=[[F(0)]*3 for _ in range(3)]
    for f in fs:
        a,b,c=[P[i] for i in f]
        dv=det(sub(a,o),sub(b,o),sub(c,o))/6
        assert dv>0
        V+=dv
        M=add(M,mul(dv/4,add(add(o,a),add(b,c))))
        w=mul(F(1,2),cross(sub(b,a),sub(c,a)))
        s=add(add(a,b),c)
        for j in range(3):
            VD[j]+=w[j]*s[j]/3
            for k in range(3):
                MD[j][k]+=w[j]*(s[j]*s[k]+a[j]*a[k]+
                                b[j]*b[k]+c[j]*c[k])/(12*(1+(j==k)))
    assert V>0 and VD==[V]*3 and MD==[list(M)]*3
    return V,M,VD,MD

def chord(a,b):
    d=sub(b,a)
    t=max(F(0),min(F(1),-dot(a,d)/dot(d,d)))
    p=add(a,mul(t,d))
    return dot(p,p)

def landscape(P,E):
    rr=[dot(p,p) for p in P]
    ww=[chord(P[i],P[j]) for i,j in E]
    by=defaultdict(list)
    for k,w in enumerate(ww): by[w].append(k)
    uf=list(range(len(P)))
    peaks=list(range(len(P)))
    members=[{i} for i in range(len(P))]
    bars=[]; ties=[]
    def find(i):
        while uf[i]!=i: i=uf[i]
        return i
    for level in sorted(by,reverse=True):
        es=by[level]
        ca=defaultdict(set)
        for ei in es:
            a,b=[find(i) for i in E[ei]]
            if a!=b:
                ca[a].add(b); ca[b].add(a)
        seen=set(); groups=[]
        for a in sorted(ca):
            if a in seen: continue
            seen.add(a); stack=[a]
            for i in stack:
                for j in sorted(ca[i]):
                    if j not in seen:
                        seen.add(j); stack.append(j)
            groups.append(stack)
        for group in groups:
            elder=max(group,key=lambda g:(rr[peaks[g]],-peaks[g]))
            ep=peaks[elder]
            old_peaks=sorted(peaks[g] for g in group)
            for g in sorted(group,key=lambda g:peaks[g]):
                peak=peaks[g]
                if g==elder or rr[peak]<=level: continue
                comp=members[g].copy()
                cut=[e for e in E if (e[0] in comp)!=(e[1] in comp)]
                at_level=[E[k] for k in es
                          if (E[k][0] in comp)!=(E[k][1] in comp)]
                assert at_level
                adj=[[] for _ in P]
                for (i,j),w in zip(E,ww):
                    if w>=level:
                        adj[i].append(j); adj[j].append(i)
                par={peak:None}; todo=deque([peak])
                while todo and ep not in par:
                    i=todo.popleft()
                    for j in sorted(adj[i]):
                        if j not in par:
                            par[j]=i; todo.append(j)
                assert ep in par
                path=[ep]
                while path[-1]!=peak: path.append(par[path[-1]])
                path.reverse()
                bars.append(dict(peak=peak,elder=ep,birth=rr[peak],
                    death=level,component=sorted(comp),cut=cut,path=path,
                    death_edge=min(at_level),tied_edges=[E[k] for k in es],
                    merging_peaks=old_peaks))
            union=set().union(*(members[g] for g in group))
            for g in group: uf[g]=elder
            members[elder]=union; peaks[elder]=ep
        if len(es)>1:
            ties.append(dict(level=level,edges=[E[k] for k in es]))
    assert len({find(i) for i in range(len(P))})==1
    capacity=[[F(0)]*len(P) for _ in P]
    for i in range(len(P)): capacity[i][i]=rr[i]
    for (i,j),w in zip(E,ww): capacity[i][j]=capacity[j][i]=w
    for k in range(len(P)):
        for i in range(len(P)):
            for j in range(len(P)):
                capacity[i][j]=max(capacity[i][j],
                    min(capacity[i][k],capacity[k][j]))
    checks=0
    for i,j in combinations(range(len(P)),2):
        assert chord(P[i],P[j])<=capacity[i][j]
        checks+=1
    return dict(radii2=rr,edge_levels=ww,bars=bars,tied_levels=ties,
                all_pair_chord_domination_checks=checks)

def audit(raw,fs,full=True):
    N=len(raw)
    if full: exhaustive_hull(raw,fs)
    owners={}; orientations={}
    for fi,f in enumerate(fs):
        for i,j in zip(f,f[1:]+f[:1]):
            e=tuple(sorted((i,j)))
            owners.setdefault(e,[]).append(fi)
            orientations.setdefault(e,[]).append(1 if i<j else -1)
    E=sorted(owners)
    assert all(len(owners[e])==2 and sum(orientations[e])==0 for e in E)
    assert set(i for f in fs for i in f)==set(range(N))
    assert N-len(E)+len(fs)==2
    adj=[[] for _ in raw]
    for i,j in E: adj[i].append(j); adj[j].append(i)
    seen={0}; todo=[0]
    for i in todo:
        for j in adj[i]:
            if j not in seen: seen.add(j); todo.append(j)
    assert len(seen)==N
    V,M,VD,MD=mass(raw,fs)
    c=mul(1/V,M)
    X=[sub(p,c) for p in raw]
    assert sub(M,mul(V,c))==ZERO
    Q=[]; bary=[]; S=[]; wS=[]
    for fi,f in enumerate(fs):
        n,h=plane(X,f)
        assert h>0
        q=mul(1/h,n); Q.append(q)
        assert all(dot(q,x)<=1 for x in X)
        assert all((dot(q,x)==1)==(j in f) for j,x in enumerate(X))
        foot=mul(1/dot(q,q),q)
        a,b,d=[X[i] for i in f]
        u=sub(b,a); v=sub(d,a); z=sub(foot,a)
        A=dot(u,u); B=dot(u,v); C=dot(v,v)
        G=A*C-B*B
        assert G>0
        s=(C*dot(z,u)-B*dot(z,v))/G
        t=(A*dot(z,v)-B*dot(z,u))/G
        bc=(1-s-t,s,t); bary.append(bc)
        if min(bc)>0: S.append(fi)
        elif min(bc)==0: wS.append(fi)
    pd=[[(j,dot(X[i],sub(X[j],X[i]))) for j in sorted(adj[i])]
        for i in range(N)]
    U=[i for i,row in enumerate(pd) if max(v for j,v in row)<0]
    wU=[i for i,row in enumerate(pd) if max(v for j,v in row)==0]
    H=[]; wH=[]; ed=[]
    for i,j in E:
        d=sub(X[j],X[i])
        t=-dot(X[i],d)/dot(d,d)
        foot=add(X[i],mul(t,d))
        f,g=owners[(i,j)]
        a,b=Q[f],Q[g]
        A=dot(a,a); B=dot(a,b); C=dot(b,b)
        G=A*C-B*B
        assert G>0
        lam=(C*dot(foot,a)-B*dot(foot,b))/G
        mu=(A*dot(foot,b)-B*dot(foot,a))/G
        assert add(mul(lam,a),mul(mu,b))==foot
        signs=(t,1-t,lam,mu)
        ed.append((i,j,t,lam,mu))
        if min(signs)>=0:
            if min(signs)>0: H.append((i,j))
            else: wH.append((i,j))
    QE=sorted(tuple(sorted(v)) for v in owners.values())
    assert len(set(QE))==len(E)
    qa=[[] for _ in Q]
    for i,j in QE: qa[i].append(j); qa[j].append(i)
    qd=[[(j,dot(Q[i],sub(Q[j],Q[i]))) for j in sorted(qa[i])]
        for i in range(len(Q))]
    assert S==[i for i,r in enumerate(qd) if max(v for j,v in r)<0]
    assert wS==[i for i,r in enumerate(qd) if max(v for j,v in r)==0]
    weak=[wS,wU,wH]
    if not any(weak): assert len(S)+len(U)-len(H)==2
    result=dict(raw_vertices=raw,centroid=c,vertices=X,volume=V,
        raw_first_moment=M,centred_first_moment=ZERO,faces=fs,edges=E,
        edge_faces=[owners[e] for e in E],polar=Q,polar_edges=QE,
        S=S,U=U,H=H,weak=weak,face_barycentrics=bary,
        physical_arrows=pd,polar_arrows=qd,mixed_edge_tests=ed,
        divergence_volumes=VD,divergence_moments=MD,
        primitive_zero_counts=dict(
            face=sum(v==0 for r in bary for v in r),
            physical_arrow=sum(v==0 for r in pd for j,v in r),
            polar_arrow=sum(v==0 for r in qd for j,v in r),
            edge=sum(v==0 for r in ed for v in (r[2],1-r[2],r[3],r[4]))))
    if full:
        result['P']=landscape(X,E)
        result['Q']=landscape(Q,QE)
        if not any(weak):
            assert len(result['P']['bars'])==len(U)-1
            assert len(result['Q']['bars'])==len(S)-1
    return result

def main():
    raw,fs,V0=parent()
    old=audit(raw,fs,True)
    assert old['centroid']==ZERO and old['volume']==V0
    assert old['S']==[15,31] and old['U']==[31]
    assert old['H']==[(15,16)] and not any(old['weak'])
    assert len(old['Q']['bars'])==1 and not old['P']['bars']
    ob=old['Q']['bars'][0]
    assert ob['peak']==31 and ob['elder']==15
    print('C186_PARENT_FULL_RECONSTRUCTION_PASS',flush=True)
    m=mul(F(1,2),add(raw[14],raw[15]))
    T,D=raw[31],raw[32]
    nT,hT=plane(raw,fs[14]); nD,hD=plane(raw,fs[45])
    assert hT>0 and hD>0 and dot(nT,m)==hT and dot(nD,m)==hD
    assert dot(raw[15],sub(raw[14],raw[15]))>F(1,1000)
    ZT=add(mul(3,m),T); ZD=add(mul(3,m),D)
    q=old['polar'][31]
    edge=sub(raw[16],raw[15])
    tH=-dot(raw[15],edge)/dot(edge,edge)
    assert 0<tH<1
    r=add(raw[15],mul(tH,edge)); R=dot(r,r)
    scalars=[dot(q,ZT),dot(q,ZD),dot(r,ZT),dot(r,ZD)]
    assert scalars[0]<-F(5,4) and scalars[1]<-F(5,4)
    assert scalars[2]>F(2,5) and scalars[3]>1
    assert 0<R<F(2,5)
    assert ob['death']==1/R and ob['birth']==dot(q,q)
    Avec=mul(F(1,6),add(nT,nD))
    L=[[ (ZT[i]*nT[j]+ZD[i]*nD[j])/24 for j in range(3)]
       for i in range(3)]
    A=(hT+hD)/6
    B=mul(F(1,24),add(mul(hT,ZT),mul(hD,ZD)))
    cprime=mul(1/V0,B)
    deriv=2*dot(cprime,sub(q,mul(1/R,r)))
    bound=-(9*hT+15*hD)/(48*V0)
    assert deriv<bound<0
    cert=dict(parent_assignment=PARENT_ID,parent_sha256=PARENT_SHA,
        selected_physical_edge=(14,15),positive_orientation=(15,14),
        visible_facets=(14,45),m=m,nT=nT,nD=nD,hT=hT,hD=hD,
        ZT=ZT,ZD=ZD,q=q,saddle_foot=r,saddle_radius2=R,
        volume0=V0,volume_linear_vector=Avec,moment_linear_matrix=L,
        four_exact_scalar_checks=scalars,radial_centroid_derivative=cprime,
        radial_log_bar_derivative=deriv,radial_derivative_upper_bound=bound,
        old_bar=ob)
    emit('C186_EDGE14_15_DESCENT_CERTIFICATE.json',cert)
    print('C186_OPEN_CONE_MASS_BAR_DESCENT_PASS',flush=True)
    if sys.argv[1:]==['theory']: return
    if sys.argv[1:]: raise SystemExit('Use no argument, or theory')
    kept=[i for i in range(62) if i not in (14,45)]
    mapping={oldi:newi for newi,oldi in enumerate(kept)}
    nf=[fs[i] for i in kept]
    nf += [(31,14,33),(31,33,15),(32,15,33),(32,33,14)]
    expectedS=sorted((mapping[15],mapping[31]))
    oldratio=ob['birth']/ob['death']
    for k in count(8):
        delta=F(1,2**k)
        x=mul(1+delta,m)
        vals=[dot(qi,x)-1 for qi in old['polar']]
        if not all((z>0 if i in (14,45) else z<0)
                   for i,z in enumerate(vals)):
            continue
        points=raw+[x]
        try:
            cand=audit(points,nf,False)
        except (AssertionError,ZeroDivisionError):
            continue
        if cand['S']!=expectedS or cand['U']!=[31]: continue
        if cand['H']!=[(15,16)] or any(cand['weak']): continue
        V=V0+delta*A
        M=add(mul(delta,B),mul(delta*delta*A/4,m))
        assert cand['volume']==V and cand['centroid']==mul(1/V,M)
        c=cand['centroid']
        projected_c=sub(c,mul(dot(c,edge)/dot(edge,edge),edge))
        rnew=sub(r,projected_c)
        ratio=dot(q,q)*dot(rnew,rnew)/(1-dot(q,c))**2
        if ratio>=oldratio: continue
        cand=audit(points,nf,True)
        assert not cand['P']['bars'] and len(cand['Q']['bars'])==1
        nb=cand['Q']['bars'][0]
        assert nb['peak']==mapping[31] and nb['elder']==mapping[15]
        assert nb['birth']/nb['death']==ratio<oldratio
        assert len(points)==34 and len(cand['edges'])==96 and len(nf)==64
        cand.update(name='C192_EDGE14_15_MASS_DESCENT_211',
            parent_assignment=PARENT_ID,parent_sha256=PARENT_SHA,
            dyadic_exponent=k,delta=delta,insertion_direction=m,
            retained_face_map=mapping,old_bar_ratio=oldratio,
            new_bar_ratio=ratio,exact_mass_chart_first_moment=M)
        emit('C192_EDGE14_15_MASS_DESCENT_211.json',cand)
        print('DELTA',str(delta),'EXPONENT',k,flush=True)
        print('C192_STELLATION_211_WEAK000_FULL_AUDIT_PASS',flush=True)
        break
    source=Path(__file__).read_bytes()
    print('SOURCE',len(source),hashlib.sha256(source).hexdigest(),flush=True)

if __name__=='__main__':
    main()
```

## Handoff boundary

The new result is the proved actual-mass descent cone and its exact algebraic continuation chart. The finite constructor is source-complete but awaits an observed replay receipt. The unavailable numerical submissions remain ephemeral and supply no accepted endpoint or exclusion. The next scientifically useful operation is to execute this certificate, record its full C192 packet and mass audit, and then continue the explicit three-dimensional insertion chart through genuine equilibrium boundaries while retaining the full primal escape and polar-basin tests.
