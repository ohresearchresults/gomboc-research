# figure-0561

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Three-corner replacement at the detached-stable interface: exact finite mass freedom, not an observed successor

## Status and reading limitation

**No newly verified body and no own110 result are reported from this continuation. FINAL76_G6 remains the accepted entrance.**

The current tool calls did not return inspectable results. This affected Files reads, container commands, Python output, and a separate output-visibility probe. The current journal text available for inspection in the resumed context was **lines1–80 of2443**. The remaining lines81–2443 were requested, but their contents were not available for inspection. Consequently, **the required complete reading of the new journal is unfinished**. I have not silently treated a requested read as a completed read or a submitted computation as an observed result.

The affected attachment is `research-journal(20260926-034355).md`, declared461406 bytes, SHA256 `e77e4a6746b2f3669119c1d6a6052dffe1183ef39a04ce490f7ee13b8128a0b2`. These are supplied manifest values, not a fresh verification receipt. The unchanged literal parent answer remains available in this conversation: `figure-0558`, SHA256 `591c9bf0e892e454c2566a0257b301f874eb9874eaad8f4e9ae7f177e71cf156`.

The advance below is therefore an **analytic adaptation of the shared independent-star mass identity to this nonsimplicial, detached-stable entrance**, with a complete pending-execution patch. Its important feature is a proved finite edge budget for opening three movable corner tips. It is not a new general mass theorem, an observed decrease of FINAL76's barcode, or an accepted replacement for the parent.

## 1. Open three corner tips instead of adding another interface collar

FINAL76_G6 is simple: V148/E222/F76 and3V=2E. Its junior root is the vertex at the intersection of **input support rows12,20,47**. Its elder root uses rows5,23,48. The stable support is row6, and the current saddle owners are rows21,60. These are input-halfspace labels, not canonical vertex or facet numbers.

Choose the junior vertex u0 and two noncritical bulk vertices u1,u2. Require their incident-facet sets to be pairwise disjoint. The bulk vertices are also required to avoid the current stable, saddle and root support block `[5,6,12,20,21,23,47,48,60]`.

Each selected simple vertex ui has exactly three neighbours ai,bi,ci. Put

`Ci=conv(ui,ai,bi,ci)`.

The opposite triangle is a supporting face after ui is removed. To see this directly, use the three edge rays from ui as coordinates. Every point of the polyhedron has nonnegative coordinates in this tangent cone. A different extreme vertex whose coordinate sum were less than1 would lie inside Ci and could not be extreme. Equality can occur at the three neighbours, but no other extreme vertex can lie in their triangle. Thus all other vertices are strictly behind the opposite triangle.

The three corner tetrahedra have disjoint interiors. In particular, every vertex of one is an old vertex other than the tip of another and lies behind that other corner's opposite plane.

Replace ui by a point pi strictly inside Ci but strictly above its opposite triangle. All unselected vertices remain fixed. The old facets incident to ui are truncated at that corner; at most three new triangular facets join pi to the edges of its opposite triangle.

### Exact combinatorial budget

All148 marked points remain extreme. Per selected corner, at most three maximal facets and three true edges are added. Triangular old facets can disappear, reducing that cost. Therefore throughout this three-corner architecture,

```text
V = 148,
F <= 76+9 = 85,
E <= 222+9 = 231,
C <= 462.
```

This leaves **at least18 true edges** below249. It opens genuine independent primal tip freedom without rounding the other145 vertices or triangulating their polygonal facets. In particular, it does not incur the cost of a41-edge third collar.

The three original selected points disappear from the new body. The old junior-root point is therefore removed physically, even when its replacement tip remains the current junior equilibrium under the same row label.

The unchanged stable hexagon is protected geometrically by the selection rule. Its mechanical stability is **not** inferred from that fact: the preparation changes mass, and its actual new centroid must first be integrated and audited.

## 2. An exact finite own-mass family after the corner preparation

Let

`ci=(ai+bi+ci)/3`

where the repeated symbol on the right denotes the third neighbour; equivalently, use the neighbour-triangle barycentre. For a rational0<epsilon<1 choose the prepared tips

`pi=(1-epsilon)ui+epsilon*(ai+bi+ci)/3`.

Integrate the prepared body's actual volume and centroid g. Let ni be a nonzero normal to the fixed opposite triangle, and let taui>0 be the volume of the retained tip tetrahedron `conv(pi,ai,bi,ci)`.

Move the three tips by finite displacements di satisfying

```text
ni·di = 0                         for i=0,1,2,
tau0 d0 + tau1 d1 + tau2 d2 = 0.
```

Every individual retained tetrahedral volume stays constant. Its first moment changes by exactly `taui di/4`, not merely to first order. Hence the whole body's volume and first moment are unchanged for finite motions while the tips remain in their corner charts. Its **actual homogeneous centroid remains g exactly**.

When n1 and n2 are not parallel, any tangent displacement of the junior tip can be compensated. Here is an explicit rational formula. Given d0 with n0·d0=0, put

```text
w = -tau0 d0,
v = n2 - [(n1·n2)/(n1·n1)] n1,
z = [(n2·w)/(v·v)] v,
d1 = z/tau1,
d2 = (w-z)/tau2.
```

Then all six displayed linear constraints hold. An additional free term proportional to `n1 cross n2` can be added to z; the patch below uses coefficient0. The full mass-preserving displacement space has dimension3 under this rank condition.

The patch chooses the bulk pair deterministically, maximizing

`tau1 tau2 |n1 cross n2|²/(|n1|² |n2|²)`

over the permitted pairs. This is a capacity/conditioning heuristic only. Its selected pair and travel capacity have **not** been observed here.

### A precise local barcode descent direction

Write x= p0-g. The exact tangent choice

`d0=-x+[(n0·x)/(n0·n0)]n0`

gives

`d/ds |p0+s d0-g|² at s=0 = -2|d0|²`.

Thus it strictly lowers the junior birth radius unless x is parallel to n0. That exceptional equality is a scoped first-order obstruction to this fixed-volume tip plane, not to other corner preparations or the whole construction problem.

The implementation uses a coarsely rationalized x before projection and then checks the exact inequality x·d0<0. This avoids importing the parent's very large centroid denominator into every new vertex coordinate unnecessarily.

If the prepared body is own121, its junior remains this tip, and its current saddle is unchanged, the death level D of its single P bar is constant on a sufficiently small mechanically unchanged interval. With

`A(s)=|p0+s d0-g|²`,

its relative depth is

`1-D/A(s)`.

Its derivative has the sign of A'(s), so the displayed direction decreases the actual P depth locally. This implication is deliberately conditional on the full mechanics. Lowering one vertex radius alone does not establish a lower full barcode, much less cancellation.

## 3. Exact finite travel and what it does not prove

Express di in the three old edge vectors from ui:

`di = beta_ia(ai-ui)+beta_ib(bi-ui)+beta_ic(ci-ui)`.

The tangent condition is exactly `beta_ia+beta_ib+beta_ic=0`. Along the finite ray, the three base barycentric coefficients are

`epsilon/3+s beta_ij`.

Their strict positivity gives a rational travel interval. The patch uses a dyadic step inside half of that interval and checks the exact decrease of the junior squared radius.

For the entire accepted geometric segment, every proposed facet normal is affine in the segment parameter, and every all-point support slack is a polynomial of degree at most2. The code checks both endpoints and every interior quadratic minimum. This certifies the **actual maximal complex throughout that segment**, rather than checking only the endpoints. Filled volume and first moment are independently evaluated at0,1/2 and1 and agree exactly; the tetrahedral argument proves their identity throughout.

None of this certifies a mechanically invariant interval by itself. The new triangular faces can create stable/saddle defects, and a root can transfer before a substantial radius gain. The code therefore audits both endpoints fully, preserving all positive P/Q bars. Its dyadic backtracking is a bounded search, not an exclusion theorem.

A shallow retained121 endpoint would still leave the main question open. The scientifically relevant subsequent event would be a finite current-root transfer or corner-chart contact with a changed full landscape—not a claim that a small endpoint step completes the cancellation.

## 4. Pending-execution recovery patch

The patch below takes the **unchanged complete parent decoder** already supplied in this conversation. It reads the decoder's literal DATA without executing it, verifies the306027-byte decoded dictionary, and locates the exact FINAL76_G6 input by its complete hash. There is no approximate seed fallback.

Required unchanged identities:

```text
Parent result:
figure-0558
591c9bf0e892e454c2566a0257b301f874eb9874eaad8f4e9ae7f177e71cf156

RECOVER_INTERFACE60.py decoded dictionary:
306027 bytes,97 units
bab9e272fd592d81b9f26bf3290e7347e012a7a96c04615da3452d190951badb

FINAL76_G6.json:
2170 bytes
999919df48ea5fef75728a09403d9b59f2993ccfdc5c8f94679a69fd694040ae
```

Save the source as `THREE_TIP_FINAL76.py`. Intended environment: CPython3.13, standard library only. No fresh runtime-version receipt was available here.

```sh
python -B -S THREE_TIP_FINAL76.py RECOVER_INTERFACE60.py --entry-start 4 --entry-count 12 --steps 16 --direction-grid 1000000 --out THREE_TIP_RUN
```

The code records every attempted prepared body and finite endpoint, including nonwinning classes and all positive bars. It creates actual byte/SHA256 receipts when run. **No new output hash or successful terminal marker is asserted in this handoff.** A110 result from this previously unexecuted independent checker would still require the established parent auditor's cross-check before acceptance.

The exact patch is complete below; its dependency is the unchanged, fully supplied parent decoder, not an originating sandbox.

```python
# Pending-execution three-corner physical replacement of literal FINAL76_G6.
# CPython 3.13, standard library only. No numerical tolerance or bar cutoff.
import argparse
import ast
import base64
import hashlib
import itertools
import json
import lzma
import sys
from collections import deque
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
PARENT = 'figure-0558'
PARENT_SHA = '591c9bf0e892e454c2566a0257b301f874eb9874eaad8f4e9ae7f177e71cf156'
DICT_SHA = 'bab9e272fd592d81b9f26bf3290e7347e012a7a96c04615da3452d190951badb'
INPUT_SHA = '999919df48ea5fef75728a09403d9b59f2993ccfdc5c8f94679a69fd694040ae'
Z = (F(0), F(0), F(0))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,t): return tuple(t*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),0)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def digest(b): return hashlib.sha256(b).hexdigest()

def primitive(row):
    row = list(map(F,row))
    D = lcm(*(x.denominator for x in row))
    z = [int(D*x) for x in row]
    k = gcd(*(abs(x) for x in z))
    assert k
    return tuple(x//k for x in z)

def emit(out,name,obj):
    data = (json.dumps(obj,default=str,sort_keys=True,
                       separators=(',',':'))+chr(10)).encode()
    (out/name).write_bytes(data)
    return dict(file=name,bytes=len(data),sha256=digest(data))

def input_normals(decoder):
    tree = ast.parse(Path(decoder).read_text())
    values = []
    for node in tree.body:
        if isinstance(node,ast.Assign) and any(
            isinstance(t,ast.Name) and t.id=='DATA' for t in node.targets):
            values.append(ast.literal_eval(node.value))
    assert len(values)==1
    raw = lzma.decompress(base64.b64decode(''.join(values[0].split()),validate=True))
    assert len(raw)==306027 and digest(raw)==DICT_SHA
    files = json.loads(raw)
    assert len(files)==97
    matches = [v.encode() for v in files.values()
               if isinstance(v,str) and digest(v.encode())==INPUT_SHA]
    assert len(matches)==1 and len(matches[0])==2170
    arrays = []
    def walk(x):
        if isinstance(x,list):
            if len(x)==76 and all(isinstance(r,list) and len(r)==3 for r in x):
                try:
                    a = [[F(v) for v in r] for r in x]
                    if all(v.denominator==1 for r in a for v in r):
                        arrays.append([tuple(int(v) for v in r) for r in a])
                except (ValueError,TypeError,ZeroDivisionError):
                    pass
            for v in x: walk(v)
        elif isinstance(x,dict):
            for v in x.values(): walk(v)
    walk(json.loads(matches[0]))
    assert len(arrays)==1, 'EXACT_76_BY_3_INTEGER_INPUT_NOT_IDENTIFIED'
    return arrays[0],1000000

def polygon(P,ids,n):
    drop = max(range(3),key=lambda j:abs(n[j]))
    a,b = [j for j in range(3) if j!=drop]
    order = sorted(ids,key=lambda i:(P[i][a],P[i][b],i))
    def turn(i,j,k):
        return ((P[j][a]-P[i][a])*(P[k][b]-P[i][b])
               -(P[j][b]-P[i][b])*(P[k][a]-P[i][a]))
    def half(seq):
        result=[]
        for i in seq:
            while len(result)>1 and turn(result[-2],result[-1],i)<=0:
                result.pop()
            result.append(i)
        return result
    f=half(order)[:-1]+half(list(reversed(order)))[:-1]
    assert len(f)>=3 and set(f)==set(ids)
    if dot(cross(sub(P[f[1]],P[f[0]]),sub(P[f[2]],P[f[0]])),n)<0:
        f.reverse()
    return f

def hbody(N,D):
    homogeneous=set()
    for a,b,c in itertools.combinations(N,3):
        denominator=det(a,b,c)
        if not denominator: continue
        numerator=mul(add(add(cross(b,c),cross(c,a)),cross(a,b)),D)
        if denominator<0:
            numerator=mul(numerator,-1); denominator=-denominator
        if any(dot(n,numerator)>D*denominator for n in N): continue
        k=gcd(*(abs(x) for x in (*numerator,denominator)))
        homogeneous.add(tuple(x//k for x in (*numerator,denominator)))
    P=sorted(tuple(F(x,d) for x in (a,b,c)) for a,b,c,d in homogeneous)
    faces=[]
    for n in N:
        ids=[i for i,p in enumerate(P) if dot(n,p)==D]
        assert len(ids)>=3, 'PARENT_SUPPORT_UNEXPECTEDLY_INACTIVE'
        faces.append(polygon(P,ids,n))
    owners,normals,heights=validate(P,faces)
    assert (len(P),len(owners),len(faces))==(148,222,76)
    return P,faces,owners

def validate(P,faces):
    owners={}; normals=[]; heights=[]; planes=set()
    for fi,f in enumerate(faces):
        assert len(f)>=3 and len(set(f))==len(f)
        a,b,c=[P[i] for i in f[:3]]
        n=cross(sub(b,a),sub(c,a)); h=dot(n,a)
        assert n!=Z
        sl=[h-dot(n,p) for p in P]
        assert min(sl)>=0 and {i for i,s in enumerate(sl) if s==0}==set(f)
        key=primitive((*n,h)); assert key not in planes; planes.add(key)
        normals.append(n); heights.append(h)
        for u,v in zip(f,f[1:]+f[:1]):
            owners.setdefault(tuple(sorted((u,v))),[]).append(fi)
    assert all(len(v)==2 for v in owners.values())
    assert set(i for f in faces for i in f)==set(range(len(P)))
    assert len(P)-len(owners)+len(faces)==2
    reached={0}; todo=[0]
    while todo:
        u=todo.pop()
        for e in owners:
            if u in e:
                v=e[0] if e[1]==u else e[1]
                if v not in reached: reached.add(v); todo.append(v)
    assert len(reached)==len(P)
    return owners,normals,heights

def mass(P,faces):
    W=F(0); T=Z
    o=mul(tuple(sum(p[j] for p in P) for j in range(3)),F(1,len(P)))
    V2=F(0); M2=Z
    for f in faces:
        for j in range(1,len(f)-1):
            a,b,c=[P[i] for i in (f[0],f[j],f[j+1])]
            w=det(a,b,c); W+=w
            T=add(T,mul(add(add(a,b),c),w))
            v=det(sub(a,o),sub(b,o),sub(c,o))/6
            assert v>0
            V2+=v
            M2=add(M2,mul(add(add(add(o,a),b),c),v/4))
    V=W/6; M=mul(T,F(1,24)); assert V>0
    assert V==V2 and M==M2
    return V,M,mul(M,1/V)

def chord(a,b):
    A,B,C=dot(a,a),dot(a,b),dot(b,b)
    if B>=A: return A
    if B>=C: return C
    return (A*C-B*B)/(A+C-2*B)

def barcode(P,edges):
    nodes=sorted(P); birth={i:dot(P[i],P[i]) for i in nodes}
    weights={e:chord(P[e[0]],P[e[1]]) for e in edges}
    assert min(weights.values())>0
    parent={i:i for i in nodes}; members={i:{i} for i in nodes}
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]; i=parent[i]
        return i
    def path(a,b,level):
        adj={i:[] for i in nodes}
        for (u,v),w in weights.items():
            if w>=level: adj[u].append(v); adj[v].append(u)
        todo=deque([a]); prev={a:None}
        while todo and b not in prev:
            u=todo.popleft()
            for v in sorted(adj[u]):
                if v not in prev: prev[v]=u; todo.append(v)
        assert b in prev
        p=[b]
        while p[-1]!=a: p.append(prev[p[-1]])
        return list(reversed(p))
    batches={}; result=[]
    for e,w in weights.items(): batches.setdefault(w,[]).append(e)
    for level in sorted(batches,reverse=True):
        adj={}
        for a,b in batches[level]:
            a,b=root(a),root(b)
            if a!=b:
                adj.setdefault(a,set()).add(b); adj.setdefault(b,set()).add(a)
        unseen=set(adj)
        while unseen:
            first=min(unseen); group={first}; stack=[first]; unseen.remove(first)
            while stack:
                for v in adj[stack.pop()]:
                    if v in unseen: unseen.remove(v); group.add(v); stack.append(v)
            keep=min(group,key=lambda r:(-birth[r],r))
            merged=set().union(*(members[r] for r in group))
            for r in sorted(group):
                if r==keep or birth[r]==level: continue
                assert birth[r]>level
                component=members[r]
                cut=[e for e in edges if (e[0] in component)!=(e[1] in component)]
                assert cut and max(weights[e] for e in cut)==level
                result.append(dict(root=r,elder=keep,birth=birth[r],death=level,
                    lifetime=birth[r]-level,relative_depth=(birth[r]-level)/birth[r],
                    component=sorted(component),cut=cut,
                    attaining_edge=min(e for e in cut if weights[e]==level),
                    path=path(r,keep,level)))
            for r in group:
                if r!=keep: parent[r]=keep; del members[r]
            members[keep]=merged
    assert len({root(i) for i in nodes})==1
    return result

def audit(P,faces):
    owners,N,h=validate(P,faces); edges=sorted(owners)
    V,M,g=mass(P,faces); X=[sub(p,g) for p in P]
    assert all(hh-dot(n,g)>0 for n,hh in zip(N,h))
    strict=[[],[],[]]; weak=[[],[],[]]; zero=[[],[],[]]
    for fi,f in enumerate(faces):
        vals=[-dot(cross(N[fi],sub(P[b],P[a])),X[a])
              for a,b in zip(f,f[1:]+f[:1])]
        if min(vals)>0: strict[0].append(fi)
        if min(vals)>=0: weak[0].append(fi)
        if 0 in vals: zero[0].append(fi)
    for i in range(len(P)):
        vals=[dot(X[i],sub(p,P[i])) for j,p in enumerate(P) if j!=i]
        if max(vals)<0: strict[1].append(i)
        if max(vals)<=0: weak[1].append(i)
        if 0 in vals: zero[1].append(i)
    for e in edges:
        a,b=e; d=sub(P[b],P[a]); dd=dot(d,d); tn=-dot(X[a],d)
        r=add(mul(X[a],dd),mul(d,tn)); f1,f2=owners[e]
        n1,n2=N[f1],N[f2]
        aa,ab,bb=dot(n1,n1),dot(n1,n2),dot(n2,n2)
        assert aa*bb-ab*ab>0
        vals=[tn,dd-tn,bb*dot(r,n1)-ab*dot(r,n2),aa*dot(r,n2)-ab*dot(r,n1)]
        if min(vals)>0: strict[2].append(e)
        if min(vals)>=0: weak[2].append(e)
        if 0 in vals: zero[2].append(e)
    PB=barcode(dict(enumerate(X)),edges)
    Q={i:mul(n,1/(h[i]-dot(n,g))) for i,n in enumerate(N)}
    QE=sorted({tuple(sorted(v)) for v in owners.values()})
    QB=barcode(Q,QE)
    counts=list(map(len,strict)); wc=list(map(len,weak)); zc=list(map(len,zero))
    extra=[wc[i]-counts[i] for i in range(3)]
    if zc==[0,0,0]:
        assert counts[0]+counts[1]-counts[2]==2
        assert len(PB)==counts[1]-1 and len(QB)==counts[0]-1
    return dict(points=P,faces=faces,edges=edges,
        edge_faces=[[a,b,*owners[(a,b)]] for a,b in edges],
        supporting_planes=[[*n,hh] for n,hh in zip(N,h)],
        V=len(P),E=len(edges),F=len(faces),C=2*len(edges),
        volume=V,first_moment=M,centroid=g,strict=counts,closed_weak=wc,
        additional_weak=extra,primitive_zero=zc,S=strict[0],U=strict[1],H=strict[2],
        closed_weak_ids=weak,primitive_zero_ids=zero,P=PB,Q=QB,
        stable_faces=[faces[i] for i in strict[0]],
        root_stars={str(i):[j for j,f in enumerate(faces) if i in f] for i in strict[1]})

def corner(P,owners,u):
    neighbours=sorted(b if a==u else a for a,b in owners if u in (a,b))
    assert len(neighbours)==3
    a,b,c=[P[j] for j in neighbours]
    n=primitive(cross(sub(b,a),sub(c,a)))
    tau=abs(det(sub(P[u],a),sub(b,a),sub(c,a)))/6
    assert tau>0
    barycentre=mul(add(add(a,b),c),F(1,3))
    return dict(tip=u,neighbours=neighbours,n=n,tau=tau,barycentre=barycentre)

def choose_corners(P,faces,owners):
    stars=[set(j for j,f in enumerate(faces) if i in f) for i in range(len(P))]
    assert all(len(s)==3 for s in stars)
    junior=next(i for i,s in enumerate(stars) if s=={12,20,47})
    elder=next(i for i,s in enumerate(stars) if s=={5,23,48})
    protected={5,6,12,20,21,23,47,48,60}
    pool=[i for i,s in enumerate(stars) if not(s & protected)]
    data={i:corner(P,owners,i) for i in [junior]+pool}
    options=[]
    for i,j in itertools.combinations(pool,2):
        if stars[i]&stars[j]: continue
        ni,nj=data[i]['n'],data[j]['n']; w=cross(ni,nj)
        if w==Z: continue
        score=data[i]['tau']*data[j]['tau']*dot(w,w)/(dot(ni,ni)*dot(nj,nj))
        options.append((score,i,j))
    assert options, 'NO_PERMITTED_NONPARALLEL_BULK_PAIR'
    _,i,j=min(options,key=lambda z:(-z[0],z[1],z[2]))
    selected=[junior,i,j]
    assert all(not(stars[a]&stars[b]) for a,b in itertools.combinations(selected,2))
    return [data[k] for k in selected],junior,elder,stars

def prepare(P,faces,C,epsilon):
    selected={c['tip'] for c in C}; Q=list(P)
    for c in C:
        u=c['tip']; Q[u]=add(mul(P[u],1-epsilon),mul(c['barycentre'],epsilon))
    ff=[]
    for f in faces:
        g=[i for i in f if i not in selected]
        if len(g)>=3: ff.append(g)
    for c in C:
        u=c['tip']
        for a,b in itertools.combinations(c['neighbours'],2):
            f=[u,a,b]; n=cross(sub(Q[a],Q[u]),sub(Q[b],Q[u]))
            sl=[dot(n,sub(Q[u],p)) for p in Q]
            if max(sl)<=0: f=[u,b,a]
            ff.append(f)
    validate(Q,ff)
    return Q,ff

def solve3(A,y):
    denominator=det(*A); assert denominator
    answer=[]
    for j in range(3):
        B=[list(r) for r in A]
        for i in range(3): B[i][j]=y[i]
        answer.append(det(*B)/denominator)
    return tuple(answer)

def motion(P,Q,C,epsilon,g,grid):
    x=sub(Q[C[0]['tip']],g); n0=C[0]['n']; nn=dot(n0,n0)
    d0=None
    for power in range(12):
        G=grid*10**power
        r=tuple(F(round(t*G),G) for t in x)
        trial=sub(mul(n0,dot(n0,r)/nn),r)
        if dot(x,trial)<0:
            d0=trial; break
    assert d0 is not None, 'NO_CERTIFIED_TANGENT_DESCENT_IN_DIRECTION_GRID_RANGE'
    tau=[(1-epsilon)*c['tau'] for c in C]
    n1,n2=C[1]['n'],C[2]['n']
    v=sub(n2,mul(n1,dot(n1,n2)/dot(n1,n1)))
    assert dot(v,v)>0
    w=mul(d0,-tau[0]); z=mul(v,dot(n2,w)/dot(v,v))
    ds=[d0,mul(z,1/tau[1]),mul(sub(w,z),1/tau[2])]
    assert add(add(mul(ds[0],tau[0]),mul(ds[1],tau[1])),mul(ds[2],tau[2]))==Z
    slopes=[]
    for c,d in zip(C,ds):
        assert dot(c['n'],d)==0
        columns=[sub(P[j],P[c['tip']]) for j in c['neighbours']]
        A=[[columns[j][i] for j in range(3)] for i in range(3)]
        beta=solve3(A,d); assert sum(beta)==0; slopes.append(beta)
    step=F(1,2)
    for k in range(256):
        inside=all(epsilon/3+2*step*b>0 for beta in slopes for b in beta)
        decreasing=2*step*dot(x,d0)+step*step*dot(d0,d0)<0
        if inside and decreasing: break
        step/=2
    else: raise ArithmeticError('DYADIC_TRAVEL_BOUND_NOT_FOUND')
    return ds,tau,slopes,step

def at(Q,C,ds,s):
    R=list(Q)
    for c,d in zip(C,ds): R[c['tip']]=add(Q[c['tip']],mul(d,s))
    return R

def interval_complex(P,Q,faces):
    directions=[sub(q,p) for p,q in zip(P,Q)]; minimum=None
    for f in faces:
        ia,ib,ic=f[:3]
        a,b,c=P[ia],P[ib],P[ic]
        da,db,dc=directions[ia],directions[ib],directions[ic]
        u,v=sub(b,a),sub(c,a); du,dv=sub(db,da),sub(dc,da)
        n0=cross(u,v); n1=add(cross(du,v),cross(u,dv))
        assert cross(du,dv)==Z and dot(n1,da)==0
        h0=dot(n0,a); h1=dot(n0,da)+dot(n1,a)
        for j,(p,d) in enumerate(zip(P,directions)):
            aa=h0-dot(n0,p)
            bb=h1-dot(n0,d)-dot(n1,p)
            cc=-dot(n1,d)
            if j in f:
                assert aa==bb==cc==0; continue
            values=[aa,aa+bb+cc]
            if cc>0:
                t=-bb/(2*cc)
                if 0<t<1: values.append(aa+bb*t+cc*t*t)
            m=min(values); assert m>0
            minimum=m if minimum is None else min(minimum,m)
    return minimum

def safe121(a):
    return (a['strict']==[1,2,1] and a['additional_weak']==[0,0,0]
            and a['primitive_zero']==[0,0,0] and len(a['P'])==1 and not a['Q'])

def target(a):
    return (a['strict']==[1,1,0] and a['additional_weak']==[0,0,0]
            and not a['P'] and not a['Q'] and a['E']<=249)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('decoder')
    ap.add_argument('--entry-start',type=int,default=4)
    ap.add_argument('--entry-count',type=int,default=12)
    ap.add_argument('--steps',type=int,default=16)
    ap.add_argument('--direction-grid',type=int,default=1000000)
    ap.add_argument('--out',default='THREE_TIP_RUN')
    args=ap.parse_args()
    assert args.entry_start>=1 and args.entry_count>0 and args.steps>0 and args.direction_grid>0
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    N,D=input_normals(args.decoder); P,faces,owners=hbody(N,D)
    base=audit(P,faces); assert safe121(base)
    C,junior,elder,stars=choose_corners(P,faces,owners)
    assert set(base['U'])=={junior,elder} and base['S']==[6]
    assert base['P'][0]['root']==junior and base['P'][0]['elder']==elder
    saddle=base['H'][0]
    assert set(owners[tuple(saddle)])=={21,60}
    receipts=[emit(out,'PARENT_AUDIT.json',base)]
    print('THREE_TIP_PARENT_MATCH',base['V'],base['E'],base['F'],flush=True)
    entry=None
    for k in range(args.entry_start,args.entry_start+args.entry_count):
        epsilon=F(1,2**k); Q,ff=prepare(P,faces,C,epsilon); a=audit(Q,ff)
        assert a['V']==148 and a['E']<=231 and a['F']<=85
        name='ENTRY_'+str(k)
        receipts.append(emit(out,name+'_INPUT.json',dict(points=Q,faces=ff,epsilon=epsilon)))
        receipts.append(emit(out,name+'_AUDIT.json',a))
        print('THREE_TIP_ENTRY',k,a['strict'],a['additional_weak'],len(a['P']),len(a['Q']),flush=True)
        if target(a):
            print('THREE_TIP_TARGET_NEEDS_PARENT_AUDITOR',name,flush=True)
            emit(out,'MANIFEST.json',dict(receipts=receipts,status='TARGET_REQUIRES_CROSSCHECK'))
            return
        unchanged=(safe121(a) and set(a['U'])=={junior,elder}
                   and a['P'][0]['root']==junior and a['P'][0]['elder']==elder
                   and a['H']==base['H']
                   and {frozenset(f) for f in a['stable_faces']}=={frozenset(faces[6])})
        if unchanged:
            entry=(epsilon,Q,ff,a); break
    if entry is None:
        emit(out,'MANIFEST.json',dict(receipts=receipts,status='BOUNDED_ENTRY_SEARCH_UNRESOLVED'))
        print('THREE_TIP_NO_SAFE_ENTRY_WITHIN_REQUESTED_LIMIT',flush=True)
        return
    epsilon,Q,ff,a0=entry
    ds,tau,slopes,step=motion(P,Q,C,epsilon,a0['centroid'],args.direction_grid)
    source=Path(__file__).read_bytes()
    parameters=dict(parent=PARENT,parent_sha256=PARENT_SHA,input_sha256=INPUT_SHA,
        source_bytes=len(source),source_sha256=digest(source),options=vars(args),python=sys.version,
        corners=C,selected_support_stars=[sorted(stars[c['tip']]) for c in C],
        epsilon=epsilon,directions=ds,retained_tetra_volumes=tau,barycentric_slopes=slopes,
        initial_step=step,prepared_volume=a0['volume'],prepared_centroid=a0['centroid'])
    receipts.append(emit(out,'PARAMETERS.json',parameters))
    print('THREE_TIP_SAFE_ENTRY',epsilon,[c['tip'] for c in C],flush=True)
    for j in range(args.steps):
        s=step/(2**j); R=at(Q,C,ds,s); a1=audit(R,ff)
        margin=interval_complex(Q,R,ff)
        middle=at(Q,C,ds,s/2)
        vm,mm,gm=mass(middle,ff)
        assert (a1['volume'],a1['first_moment'],a1['centroid'])==(
                a0['volume'],a0['first_moment'],a0['centroid'])
        assert (vm,mm,gm)==(a0['volume'],a0['first_moment'],a0['centroid'])
        before=dot(sub(Q[junior],gm),sub(Q[junior],gm))
        after=dot(sub(R[junior],gm),sub(R[junior],gm)); assert after<before
        name='FINITE_'+str(j)
        receipts.append(emit(out,name+'_INPUT.json',dict(points=R,faces=ff,s=s)))
        receipts.append(emit(out,name+'_AUDIT.json',a1))
        receipts.append(emit(out,name+'_PATH.json',dict(s=s,quadratic_support_minimum=margin,
            volume=vm,first_moment=mm,centroid=gm,junior_radius_squared_before=before,
            junior_radius_squared_after=after,mechanics_between_endpoints='NOT_CERTIFIED')))
        print('THREE_TIP_FINITE_ENDPOINT',j,a1['strict'],a1['additional_weak'],
              len(a1['P']),len(a1['Q']),flush=True)
        if target(a1):
            status='TARGET_REQUIRES_PARENT_CROSSCHECK'
            print('THREE_TIP_TARGET_NEEDS_PARENT_AUDITOR',name,flush=True)
            break
        if safe121(a1) and a1['P'][0]['relative_depth']<a0['P'][0]['relative_depth']:
            status='OWN121_IMPROVES_PREPARED_ENTRY_NOT_AUTOMATICALLY_PARENT'
            print('THREE_TIP_EXACT121_IMPROVEMENT',name,
                  a1['P'][0]['relative_depth']<base['P'][0]['relative_depth'],flush=True)
            break
    else:
        status='BOUNDED_STEP_SEARCH_UNRESOLVED'
    emit(out,'MANIFEST.json',dict(receipts=receipts,status=status))

if __name__=='__main__':
    main()
```

## Handoff boundary and next decision

The proved contribution is the **three-corner opening with E<=231**, together with an explicit rational, finite, exactly volume-and-first-moment-preserving displacement space and a junior-radius descent direction. Its usefulness on the literal FINAL76 geometry has not been established by an inspectable selected bulk pair, preparation census, travel distance, or endpoint audit.

There is no new exact successor to retain, no observed output receipt, and no finite-screen or global exclusion to integrate from this attempt. The unchanged FINAL76/H60 and simple26 controls remain authoritative.

The next useful execution is to restore complete journal reading and inspect the three-corner preparation and first finite path output. The decisive geometric question is whether these opened tips have useful travel before a new critical carrier or corner contact—not whether the algebraic mass identity holds. That identity alone cannot certify cancellation.
