# figure-0556

Historical AI scientific report · saved 2026-09-26 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# RA44 — a finite mass-neutral edge split with separated equilibrium cancellations

## Result and execution boundary

**No new own110 body or computationally audited T37/T43 successor is established here.** The new result is an analytic finite-replacement mechanism: two adjacent moving apices can be coupled through a common planar base so that the actual volume and first moment remain exactly constant through a change of maximal hull. An explicit rational example cancels one stable–saddle pair without creating an unstable equilibrium. A second, distinct parameter value creates an unstable–saddle pair; changing the base proportions separates these events and opens a nondegenerate cancellation interval.

This is a replacement-cell construction, **not yet a valid graft into T37 or T43**. Its global use still requires accounting for the moving interfaces with the rest of the body. The example demonstrates that a finite, uniformly filled replacement need not pay for a stable cancellation by creating an unstable equilibrium at the same parameter.

There is an execution limitation. The accessible tool context contains only the beginning of the newly supplied journal, through its rendered line28. Subsequent file/container calls did not expose inspectable returned contents. I therefore cannot credit a complete reading of the373385-byte update, its hash verification, or a new RA43 replay. The literal RA43 answer already visible in this chat remains the geometry authority: `figure-0554`, declared SHA-256 `75f535724577c7ccca10bff31683fac02ec7a7fc1793b92ba46afb01c671b1b0`. The verifier below was submitted for execution, but no returned success marker, report bytes, or hash was inspectable. **Its computational receipt is unobserved.** The mathematical statements below are supported by the explicit derivations and literal data, not by an alleged numerical run.

## 1. Finite coupled-apex replacement with exact mass closure

Let T be a convex polygon of area A in the plane z=0, with area centroid f. Let

```text
a = (r,h),       b = (s,−k),       h,k>0,
q = (k r+h s)/(h+k).
```

The union of the two filled pyramids conv(T,a) and conv(T,b) is convex exactly when q belongs to T. Their joining segment crosses the base at q. When q is in the relative interior of T, the union is the ordinary bipyramid over T.

For a horizontal vector d, replace the apices by

```text
a(d) = a+d,
b(d) = b−(h/k)d.
```

The two pyramid volumes remain Ah/3 and Ak/3. Their first moments change by

```text
Delta M = (Ah/12)d + (Ak/12)(−h d/k) = 0.
```

Thus the **actual uniform volume and actual first moment are unchanged for a finite displacement**, not merely to first order. The new joining point is

```text
q(d) = q + ((k−h)/k)d.
```

Consequently, the full finite convexity region is the explicit polygon

```text
{d in the base plane : q+((k−h)/k)d belongs to T}.
```

No independent-star assumption, inherited rank calculation, or small-step approximation is involved. The two moving vertices may be adjacent in the entrance hull.

For h≠k and d≠0, this is not a single affine deformation fixing T. An affine map fixing a nondegenerate base polygon pointwise and preserving both heights must move the apices in the ratio h:−k. The moment-balanced displacement uses the different ratio 1:−h/k. These agree only when h=k or d=0.

A useful contact occurs when q is a base vertex E. Then E can be redundant in the entrance hull. Moving q(d) into the interior makes E an extreme vertex, changes the supporting triangles, and changes the actual edge complex while preserving mass. For a triangular base, the entrance can be a tetrahedron and the successor a five-vertex triangular bipyramid: **one new vertex, three net new edges, and two net new maximal facets**.

The convexity criterion follows directly from the common-base decomposition. If q(d) is outside T, the segment between the apices passes outside the union at z=0. If q(d) lies in T, every segment joining the upper and lower pyramids crosses the base in T; equivalently, every upper and lower side plane supports the other apex on its inner side. The union is then exactly its convex hull, so the pyramid volume and moment sums are the physical body’s mass data.

## 2. A literal rational family with a genuine cancellation interval

Set beta=3/4 and define

```text
A = (−1,0,0)
B = ( 1,0,0)
E = ( 0,−3/4,0)
C(t) = (0,−3/4−t, 2)
D(t) = (0,−3/4+2t,−1).

K(t) = conv(A,B,E,C(t),D(t)),       0≤t<3/4.
```

At t=0, E lies on the segment C(0)D(0) and is not an extreme vertex. The actual maximal hull is the tetrahedron conv(A,B,C(0),D(0)). For every 0<t<3/4, the segment C(t)D(t) crosses the base triangle ABE at

```text
(0,−3/4+t,0),
```

strictly inside that triangle. Hence K(t) is a genuine triangular bipyramid with maximal facets

```text
ABC, ACE, BCE, ABD, ADE, BDE
```

and true edges

```text
AB, AC, AD, AE, BC, BD, BE, CE, DE.
```

Throughout the entire family, with density one,

```text
volume = 3/4
first moment = (0,−9/32,3/16)
own centroid = (0,−3/8,1/4).
```

The upper and lower pyramid volumes are1/2 and1/4. Their finite moment changes cancel because C moves by (0,−t,0) while D moves by (0,2t,0). The body is not obtained by keeping all old material and adding a cap: distinct members have equal volume and cannot contain one another.

### Full strict and additional closed-weak census

The following is an analytic interval classification, not an inference from sampled endpoints. Counts are ordered S/U/H.

| Parameter | True V/E/F | Strict S/U/H | Additional closed weak S/U/H |
|---|---:|---:|---:|
| t=0 |4/6/4|4/4/6|0/0/0|
| 0<t<1/24 |5/9/6|4/4/6|0/0/0|
| t=1/24 |5/9/6|3/4/5|1/0/1|
| 1/24<t<1/3 |5/9/6|3/4/5|0/0/0|
| t=1/3 |5/9/6|3/4/5|0/1/1|
| 1/3<t<25/48 |5/9/6|3/5/6|0/0/0|
| t=25/48 |5/9/6|3/5/6|2/0/2|
| 25/48<t<3/4 |5/9/6|5/5/8|0/0/0|

Thus the path from t=0 to t=1/8 has one stable–saddle cancellation at t=1/24 and no unstable birth. There is a weak event at the cancellation parameter; **this is not a no-weak-throughout homotopy**. Both selected endpoints have no additional weak equilibria.

The unstable–saddle event at t=1/3 can also be traversed in the cancellation direction: decreasing t from the3/5/6 chamber into the3/4/5 chamber removes E’s instability and the saddle on DE without changing the number of stable equilibria.

### Direct sign proof

Write beta=3/4. Outward normals and raw offsets for the six facets can be chosen as

```text
ABC: n=(0,2,beta+t),        h=0
ACE: n=(−beta,−1,−t/2),    h=beta
BCE: n=( beta,−1,−t/2),    h=beta
ABD: n=(0,1,2t−beta),      h=0
ADE: n=(−beta,−1,−2t),     h=beta
BDE: n=( beta,−1,−2t),     h=beta.
```

All centered supports h−n·c are positive. A,B,C,D are strict unstable throughout 0<t<beta. For E, the only outgoing sign that can vanish in this interval is

```text
(E−c)·(D(t)−E) = 1/4−beta*t.
```

Therefore E becomes unstable exactly after t=1/(4beta)=1/3.

Using q=n/(h−n·c), the closed face conditions reduce to the following strict conditions; all omitted positive factors have positive denominators throughout the stated interval:

```text
ABC: always strict stable
ACE, BCE: always strict stable
ABD: strict stable iff 2*beta^2−1−4*beta*t > 0
ADE, BDE: strict stable iff 4*beta*t−(beta^2+1) > 0.
```

The true-edge saddle tests give a particularly simple complete list:

```text
AC, AD, BC, BD, CE: always strict saddle
AB: strict saddle iff t<1/24
DE: strict saddle iff t>1/3
AE, BE: strict saddle iff t>25/48.
```

At equality the corresponding edge satisfies all closed conditions but not all strict ones. No other endpoint or cone coefficient vanishes. These statements establish the table directly, without relying solely on an Euler count.

### Why changing the base proportions matters

The same construction works with a variable beta. Its stable-loss and unstable-birth thresholds are

```text
t_S = (2*beta^2−1)/(4*beta)
t_U = 1/(4*beta).
```

At beta=1 they coincide: the stable cancellation and unstable creation occur at the same parameter. For

```text
1/2 < beta^2 < 1,
```

they separate, with 0<t_S<t_U. The rational choice beta=3/4 opens the interval (1/24,1/3). This is the substantive geometric control: **base proportions separate two mechanical events while the coupled-apex motion preserves the full physical mass exactly**.

This family is not itself a route to110. A,B,C,D remain strict U throughout its specified interval. That is an explicit limitation of this particular replacement cell, not an exclusion of its use in a different exposed complex or of arbitrary T37/T43 surgery.

## 3. Exact endpoint ledgers

The selected successor is K(1/8), defined by the complete five-point list

```python
[[-1,0,0],[1,0,0],[0,-3/4,0],[0,-7/8,2],[0,-1/2,-1]]
```

with the fractions understood literally. Its true counts are5/9/6, C18, own3/4/5, additional weak000. This is an analytic replacement-cell control, not a candidate110 construction and not a new low-complexity record for the original problem.

Its strict stable facets are ABC,ACE,BCE. Its strict unstable vertices are A,B,C,D. Its strict saddle edges are AC,AD,BC,BD,CE. At both t=0 and t=1/8, none of the face-side, vertex-outgoing, or edge-foot/cone predicates used by the verifier is zero.

### Every positive P and Q bar

All depths below are exact relative squared-radius depths. Equal birth/death levels are treated simultaneously.

```text
K(0):
P = [6097/9701,1089/3157,1089/3157]
Q = [19321/22525,9/25,1/325]

K(1/8):
P = [2505/4141,25/77,25/77]
Q = [138384/164009,144/401]
```

No positive bar is suppressed. In particular the initial Q bar1/325 is genuinely positive and is the stable–saddle pair eliminated along the finite path.

For K(1/8), the complete positive-bar interfaces are:

| Landscape and peak | Elder | Birth | Death | Death component | Complete cut | Attaining path |
|---|---|---:|---:|---|---|---|
| P, D |C|101/64|409/656|A,B,D|AC,BC,AE,BE,DE|D–A–C|
| P, A |D|77/64|13/16|A|AB,AC,AD,AE|A–D|
| P, B |D|77/64|13/16|B|AB,BC,BD,BE|B–D|
| Q, ACE |ABC|6416/625|656/409|ACE,ADE,BCE,BDE|ABC–ACE,ABC–BCE,ABD–ADE,ABD–BDE|ACE–ABC|
| Q, BCE |ACE|6416/625|4112/625|BCE,BDE|ABC–BCE,ACE–BCE,ABD–BDE,ADE–BDE|BCE–ACE|

For the entrance tetrahedron, the P component dying at its final merger is A,B,D, with cut AC,BC,CD and attaining path D–A–C. The two earlier P deaths are the singleton vertices A and B. Its Q deaths are: BCD into ACD at64/9; ABD into ABC at64/13; and the component ACD,BCD into ABC at1424/901. The standalone verifier reconstructs these complete cuts and paths as well.

As an independent compact check on the successor, its centered primal coordinates are

```text
A=(-8,3,−2)/8
B=( 8,3,−2)/8
E=( 0,−3,−2)/8
C=( 0,−4,14)/8
D=( 0,−1,−10)/8,
```

and its polar facet points, with the same facet labels, are

```text
ABC = (0,64/17,28/17)
ACE = (−48/25,−64/25,−4/25)
BCE = ( 48/25,−64/25,−4/25)
ABD = (0,2,−1)
ADE = (−12/7,−16/7,−4/7)
BDE = ( 12/7,−16/7,−4/7).
```

These data independently determine the two full radial merge problems.

## 4. A scoped rigidity result explains where to seek this freedom in T37/T43

The construction above is a piecewise affine translation of horizontal sections. Its entrance deliberately has a horizontal true edge AB. That alignment is essential to obtaining non-affine section-translation freedom.

**Section-translation rigidity.** Let K be a full-dimensional convex3-polytope and choose a height functional z=n·x such that no true edge of K is horizontal. Suppose a compact convex body L is obtained by translating every section K∩{z=s} within its own plane, without changing the section’s shape. Then those translations are affine in s. Thus L is an affine shear and translation of K, not a new nonlinear material redistribution.

**Proof.** At any interior height, every nondegenerate edge of the section comes from an original facet that persists on both sides of that height. A facet merely touching the height plane could contribute a section edge only by having a horizontal original edge. The persistent section-edge outward normals positively span the transverse plane. For each such normal u, the original sectional support is affine in height on a neighborhood. Convexity of L makes its sectional support concave; therefore u·t(s) is concave for the section translation t. A strictly positive linear combination of these normals is zero, so the corresponding positive sum of concavity gaps is identically zero. Each gap must vanish. Since the normals span the transverse plane, t is affine on that neighborhood. Overlapping neighborhoods give a single affine t throughout the height interval. Compactness supplies the endpoint sections. ∎

For the literal T43 G3 input, the height normal

```text
n=(1,4096,4096^2)
```

gives distinct heights to all43 vertices. Its x-coordinate span is1812 and its y-coordinate span is1453 in integer input units. Equality of two heights first forces equality of x modulo4096, then y, then z. Therefore every convex section-translation deformation in this explicit direction is just an affine shear. Preserving the original centroid reduces the translations to t(s)=v(s−n·c), with v·n=0.

This theorem does **not** exclude changed section shapes, section rotations, convexification after a nonconvex piecewise shear, or an intentionally edge-aligned height direction. It also does not exclude110 in the resulting affine orbit; that is the coordinator’s separate investigation.

The finite replacement cell escapes this rigidity exactly at an edge-aligned slice. Its upper and lower shear slopes differ, its common-base vertex becomes exposed, and its maximal facets change. For the current T37, the parent’s actual saddle edges [12,35] and[31,36] are concrete edge-aligned entrances to test; no admissible hinge direction on either is claimed to have been computed here.

## 5. What remains for a genuine T37/T43 successor

The new mass identity is useful only when it describes the actual complete moved material. Taking a tetrahedron inside T37 and moving its two tips generally changes its interfaces with the rest of T37. The tetrahedron’s zero moment change does **not** account for overlaps, gaps, or other changed vertex stars. It must not be transplanted as if it were an independent reservoir.

A direct whole-body version is an edge-aligned piecewise shear. For n·v=0, split a rational body K at n·x=h and apply

```text
F_v(x)=x+v*max(0,n·x−h).
```

Each piece has determinant one and heights are unchanged. Before convexification, the union has exactly the old volume, and its first-moment change is exactly

```text
Delta M = v*(n·M_plus−h*V_plus),
```

where V_plus,M_plus are the actual upper-piece volume and moment. A global translation can remove this centroid displacement without changing the mechanics. Convexity, however, is a real constraint—not a consequence of the mass formula.

The image is generated by transformed old vertices and the exact intersections of the slicing plane with crossed true edges. If the convex hull of that image has exactly the old volume, equality certifies that no positive-volume convexification material was added. If it has larger volume, the displayed moment formula is no longer the moment of the convex hull; the whole solid must be re-integrated.

For T37, a slice crossing at most48 old edges gives at most85 candidate vertices and hence an unconditional E≤249 bound before accounting for further hidden points. The critical task is to find an edge-aligned finite jump whose support inequalities allow it to alter the **current** stable carriers and root stars. Generic section translations supply no extra freedom; the exact ridge contact and the changed maximal complex do.

The remaining obstruction in this continuation is therefore concrete: **a globally compatible mobile interface on T37/T43 has not been identified and certified.** The replacement-cell proof closes a finite mass-balance and event-separation mechanism, not that embedding problem or the macroscopic P/Q cancellation.

## 6. Complete standalone recovery and verifier

The following source requires Python3.10 or newer and only the standard library. It contains every input for the two analytic endpoint controls. It enumerates all supporting triples, verifies the complete simplicial maximal hull, counts true edges, computes volume and moment with two different tetrahedral origins, checks strict and closed-weak S/U/H, and generates every positive P/Q bar with complete components, cuts and attaining paths. It batches equal levels and uses no numerical tolerance.

Save it as `edge_split44.py` and run:

```sh
python edge_split44.py
```

Its expected terminal marker is

```text
EDGE_SPLIT_EQUAL_MASS_CENTROID_446_TO_345_PASS
```

It then prints the generated report’s exact byte count and SHA-256. **That marker and those receipts are not reported as observed in this turn.** No sandbox dependency, inaccessible parent file, or optimizer checkpoint is needed to reconstruct the controls. The interval theorem is supplied by the sign proof above, not by the program’s two endpoint checks.

```python
from fractions import Fraction as F
from itertools import combinations, groupby
from collections import deque
from pathlib import Path
import hashlib, json


def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))


def geometry(P):
    P={k:tuple(map(F,v)) for k,v in sorted(P.items())}
    faces={}
    for ids in combinations(P,3):
        a,b,c=(P[i] for i in ids)
        n=cross(sub(b,a),sub(c,a))
        if n==(0,0,0): continue
        h=dot(n,a)
        s=[dot(n,x)-h for x in P.values()]
        if min(s)<0<max(s): continue
        assert min(s)<0 or max(s)>0
        order=list(ids)
        if max(s)>0:
            n=tuple(-x for x in n); h=-h; order=[ids[0],ids[2],ids[1]]
        assert all(dot(n,x)<=h for x in P.values())
        assert sum(dot(n,x)==h for x in P.values())==3
        faces[''.join(ids)]=(order,n,h)
    edges={}
    for name,(ids,n,h) in faces.items():
        for i,j in zip(ids,ids[1:]+ids[:1]):
            edges.setdefault(tuple(sorted((i,j))),[]).append(name)
    assert all(len(v)==2 for v in edges.values())
    assert set(P)==set(i for e in edges for i in e)
    assert len(P)-len(edges)+len(faces)==2
    V=F(0); M=[F(0)]*3
    for ids,n,h in faces.values():
        a,b,c=(P[i] for i in ids)
        w=det(a,b,c)/6; V+=w
        for k in range(3): M[k]+=w*(a[k]+b[k]+c[k])/4
    assert V>0
    centre=tuple(x/V for x in M)
    assert all(dot(n,centre)<h for ids,n,h in faces.values())
    o=tuple(sum(x[k] for x in P.values())/len(P) for k in range(3))
    VV=F(0); MM=[F(0)]*3
    for ids,n,h in faces.values():
        a,b,c=(P[i] for i in ids)
        w=det(sub(a,o),sub(b,o),sub(c,o))/6
        assert w>0; VV+=w
        for k in range(3): MM[k]+=w*(o[k]+a[k]+b[k]+c[k])/4
    assert VV==V and MM==M
    return P,faces,edges,V,tuple(M),centre


def mechanics(P,faces,edges,c):
    strict=[[],[],[]]; weak=[[],[],[]]; zeros=[0,0,0]
    def record(k,name,tests):
        zeros[k]+=sum(t==0 for t in tests)
        if all(t>0 for t in tests): strict[k].append(name)
        elif all(t>=0 for t in tests): weak[k].append(name)
    for name,(ids,n,h) in faces.items():
        record(0,name,[dot(cross(n,sub(P[j],P[i])),sub(c,P[i]))
                      for i,j in zip(ids,ids[1:]+ids[:1])])
    nb={i:set() for i in P}
    for i,j in edges: nb[i].add(j); nb[j].add(i)
    for i in P:
        record(1,i,[-dot(sub(P[i],c),sub(P[j],P[i])) for j in sorted(nb[i])])
    for (i,j),(fi,gi) in edges.items():
        p=sub(P[i],c); d=sub(P[j],P[i]); dd=dot(d,d); t=-dot(p,d)
        R=tuple(dd*p[k]+t*d[k] for k in range(3))
        n=faces[fi][1]; m=faces[gi][1]
        aa=dot(n,n); ab=dot(n,m); bb=dot(m,m)
        assert aa*bb>ab*ab
        record(2,i+j,[t,dd-t,bb*dot(R,n)-ab*dot(R,m),aa*dot(R,m)-ab*dot(R,n)])
    return dict(strict=list(map(len,strict)),additional_weak=list(map(len,weak)),
                primitive_zero=zeros,S=strict[0],U=strict[1],H=strict[2],
                weak_S=weak[0],weak_U=weak[1],weak_H=weak[2])


def gate(u,v):
    a=dot(u,u); b=dot(u,v); c=dot(v,v)
    if b>=a: return a
    if b>=c: return c
    return (a*c-b*b)/(a+c-2*b)


def barcode(P,edges):
    edges=sorted(set(tuple(sorted(e)) for e in edges))
    birth={i:dot(p,p) for i,p in P.items()}
    W={e:gate(P[e[0]],P[e[1]]) for e in edges}
    parent={i:i for i in P}; peak=dict(parent); members={i:{i} for i in P}
    def find(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]; i=parent[i]
        return i
    def path(s,t,level):
        adj={i:[] for i in P}
        for i,j in edges:
            if W[(i,j)]>=level: adj[i].append(j); adj[j].append(i)
        prev={s:None}; todo=deque([s])
        while todo and t not in prev:
            i=todo.popleft()
            for j in sorted(adj[i]):
                if j not in prev: prev[j]=i; todo.append(j)
        assert t in prev
        out=[]
        while t is not None: out.append(t); t=prev[t]
        return out[::-1]
    out=[]
    for level,es in groupby(sorted(edges,key=lambda e:(-W[e],e)),key=lambda e:W[e]):
        adj={}
        for i,j in es:
            a,b=find(i),find(j)
            if a!=b: adj.setdefault(a,set()).add(b); adj.setdefault(b,set()).add(a)
        unseen=set(adj)
        while unseen:
            a=min(unseen); todo=[a]; cc={a}; unseen.remove(a)
            while todo:
                a=todo.pop()
                for b in adj[a]:
                    if b in unseen: unseen.remove(b); cc.add(b); todo.append(b)
            elder=min(cc,key=lambda a:(-birth[peak[a]],peak[a]))
            for a in sorted(cc):
                if a==elder or birth[peak[a]]==level: continue
                assert birth[peak[a]]>level
                comp=members[a]
                cut=[e for e in edges if (e[0] in comp)!=(e[1] in comp)]
                assert cut and max(W[e] for e in cut)==level
                pp=path(peak[a],peak[elder],level)
                assert min(W[tuple(sorted(e))] for e in zip(pp,pp[1:]))==level
                out.append(dict(peak=peak[a],elder=peak[elder],birth=birth[peak[a]],
                    death=level,depth=(birth[peak[a]]-level)/birth[peak[a]],
                    component=sorted(comp),cut=cut,
                    attaining_edge=next(e for e in cut if W[e]==level),attaining_path=pp))
            joined=set().union(*(members[a] for a in cc))
            for a in cc: parent[a]=elder
            members[elder]=joined
    assert len({find(i) for i in P})==1
    return sorted(out,key=lambda r:(-r['depth'],r['peak']))


def body(t):
    t=F(t); b=F(3,4)
    assert 0<=t<b
    P={'A':(-1,0,0),'B':(1,0,0),'C':(0,-b-t,2),'D':(0,-b+2*t,-1)}
    if t: P['E']=(0,-b,0)
    return P


def audit(t):
    P,faces,edges,V,M,c=geometry(body(t))
    r=mechanics(P,faces,edges,c)
    X={i:sub(p,c) for i,p in P.items()}
    Q={i:tuple(v/(h-dot(n,c)) for v in n) for i,(ids,n,h) in faces.items()}
    pb=barcode(X,edges); qb=barcode(Q,edges.values())
    assert V==F(3,4) and M==(0,F(-9,32),F(3,16)) and c==(0,F(-3,8),F(1,4))
    if not any(r['additional_weak']):
        s,u,h=r['strict']; assert s+u-h==2
        assert len(pb)==u-1 and len(qb)==s-1
    r.update(t=t,vertices=P,facets={i:dict(vertices=a,normal=n,height=h)
        for i,(a,n,h) in faces.items()},edges=[dict(vertices=e,facets=f) for e,f in sorted(edges.items())],
        counts=[len(P),len(edges),len(faces)],complexity=2*len(edges),volume=V,moment=M,
        centroid=c,P_bars=pb,Q_bars=qb,metric='Euclidean',density=1)
    return r


def main():
    a=audit(F(0)); b=audit(F(1,8))
    assert a['counts']==[4,6,4] and a['strict']==[4,4,6]
    assert b['counts']==[5,9,6] and b['strict']==[3,4,5]
    assert set(b['S'])=={'ABC','ACE','BCE'} and set(b['U'])=={'A','B','C','D'}
    assert set(b['H'])=={'AC','AD','BC','BD','CE'}
    for r in (a,b):
        assert r['additional_weak']==[0,0,0] and r['primitive_zero']==[0,0,0]
    assert [r['depth'] for r in a['P_bars']]==[F(6097,9701),F(1089,3157),F(1089,3157)]
    assert [r['depth'] for r in a['Q_bars']]==[F(19321,22525),F(9,25),F(1,325)]
    assert [r['depth'] for r in b['P_bars']]==[F(2505,4141),F(25,77),F(25,77)]
    assert [r['depth'] for r in b['Q_bars']]==[F(138384,164009),F(144,401)]
    data=(json.dumps({'tetrahedron':a,'replacement':b},sort_keys=True,separators=(',',':'),default=str)+'\n').encode()
    Path('edge_split44_audit.json').write_bytes(data)
    print('EDGE_SPLIT_EQUAL_MASS_CENTROID_446_TO_345_PASS')
    print('REPORT_BYTES_SHA256',len(data),hashlib.sha256(data).hexdigest())

if __name__=='__main__': main()
```

## Handoff boundary

The durable additions are a finite common-base coupled-apex mass law, an explicit convex cancellation interval with complete strict/closed-weak classification, exact endpoint P/Q ledgers, and a scoped rigidity theorem distinguishing genuine ridge-enabled material redistribution from an affine shear. **No unobserved tool result is promoted to an executed certificate, and no replacement cell is presented as an already embedded T37/T43 successor.** The next construction must resolve the current compact body's supporting-interface compatibility while changing both stable carriers and unstable-root geometry.
