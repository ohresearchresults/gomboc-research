# figure-0544

Historical AI scientific report · saved 2026-09-25 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# W54 — finite multi-vertex block release; execution and complete-pack reading unverified

## Status and exact limitation

**No newly verified body, no observed cancellation, and no own110 claim are reported from this continuation. The last accepted entrance remains the literal FOURFREE_D100000 / TWOPOINT_G5_REDUCED_SAME_BODY.**

The read and execution calls made during this continuation did not provide inspectable result messages. This affected container, Python and Files calls, including attempts to read the new journal. Consequently I cannot certify that I read the complete newly supplied `research-journal.md`, recovered its complete source inventory, or executed the code below. I do not interpret this as evidence that the attachment or its source capsule is absent.

The affected attachment is `/mnt/data/research-journal(20260925-084455).md`, declared as 305354 bytes with SHA256 `6849909fef39b88812e148fc065a5f70b629114841bc04ba507e0c69392acb41`. Those are the supplied manifest values, not independently observed receipts from this continuation. The required literal parent is `figure-0542`, declared SHA256 `d8bc615c9cfaacf83c9a22bb08ffeda7dcf17a619428ef6c61f82a3a0c7a9ef7`.

The exact parent coordinates, matrix, mass, material carriers and remaining Q depth used below were already present in the visible parent excerpt. They are repeated completely in the source. I do not substitute that excerpt for the required complete-pack reading. No conflict with an unread portion of the journal has been ruled out.

The useful advance is an algebraically proved finite material parameterization that releases **adjacent groups of original host vertices**, rather than only independent single-vertex stars or a globally affine host. The supplied implementation is complete and independent of an originating sandbox, but its preparation, selected block system, chart bounds and endpoint audits are **unobserved executions**. It must not be entered as an accepted computational successor.

## 1. A finite material freedom beyond independent single-vertex stars

Let an actual simplicial convex boundary have outward-oriented triangles. Partition selected vertices into disjoint blocks B_1,...,B_k, with the condition that no actual triangle contains vertices from two different blocks. Vertices within one block may be adjacent and may form a whole stable triangle, a saddle edge, or a larger critical patch. Translate every vertex in B_i by the same finite vector d_i; unselected vertices stay fixed.

For a triangle f=(a,b,c) touched by block i, let e_a,e_b,e_c be its three zero-or-one block-membership indicators, and put

```
m_f = e_a + e_b + e_c,
l_f = e_a (b × c) + e_b (c × a) + e_c (a × b),
s_f = a+b+c,
w_f = det(a,b,c).
```

Define, with sums over the oriented boundary triangles,

```
A_i = Σ l_f,
C_i = Σ m_f l_f,
J_i = Σ [s_f l_f^T + m_f w_f I].
```

Use W=6 Volume and T=24 times the first moment. The exact finite changes of a translated block are

```
ΔW_i = A_i · d_i,
ΔT_i = J_i d_i + (C_i · d_i) d_i.
```

### Proof

In the determinant of the translated triangle, every term of degree at least two contains the same displacement vector in two columns and vanishes. Therefore its determinant is exactly `w_f+l_f·d_i`. Its vertex sum is exactly `s_f+m_f d_i`. Multiplying gives the stated constant, linear and quadratic first-moment terms. Because no triangle touches two blocks, there are no cross-block products. Summation proves the identities.

Consequently the rational **linear** constraints

```
C_i · d_i = 0                    for each block i,
Σ A_i · d_i = 0,
Σ J_i d_i = 0
```

preserve both actual volume and first moment for finite motions, while the deformed boundary remains the actual convex boundary. There are at most k+4 equations in 3k unknown coordinates, so the nullspace has dimension at least **2k−4**. This dimension count does not establish that every desired critical block has a nonzero projection; the implementation explicitly checks that condition.

For a singleton block, C_i=A_i. Thus the older independent-star construction is a special case, and the total-volume equation is then redundant. For a block containing adjacent vertices, replacing C_i by A_i without justification would generally be wrong. The extra weighted vector C_i is the important distinction.

The code also requires four affinely independent unselected vertices. A nonzero accepted block direction therefore cannot be a single global affine deformation of the marked input: an affine map fixing those four points is the identity.

### Application to the literal hybrid

The first requested critical block is

```
[A31,A30,A4,q,A29,A2,A5,p].
```

It includes both current stable carriers, the entire current saddle edge and the current root. It is deliberately not a single independent star. If that block leaves no compatible movable ballast blocks, the program tries the explicitly listed smaller critical blocks; it does not claim the first block is feasible. Every fallback still moves original host material. There is no constraint preserving the mechanical identity of the old root, either stable face, or the saddle.

The input contains exactly the 33 distinct material rows obtained by removing A3 and adding p and q. Every subsequently rebuilt convex hull therefore has at most 33 vertices and at most 93 true edges. The whole finite experiment remains below the required edge budget, independently of exposure changes. This is a combinatorial budget statement, not an equilibrium assertion.

## 2. Finite domain and contact crossing

For a line `v_j(t)=v_j+t d_j`, every original facet normal is affine in t. This remains true when two or three vertices of a facet belong to one moving block, because their displacement differences are collinear. Every all-point supporting inequality is consequently a polynomial of degree at most two.

The source checks each quadratic on the entire interval from zero to t, including its interior minimum. It therefore brackets the first loss of the original strict maximal-facet chart, rather than merely testing an endpoint. The exact volume and centroid identities apply throughout the certified chart.

The proposed finite experiment then samples both inside and **beyond** that first-contact bracket. Beyond contact it discards the old boundary for physical integration, constructs the actual convex hull from all material points, and reintegrates its own homogeneous centroid. The old mass identity is not assumed there. Thus a contact-crossing sample cannot be accepted at a stale reference centre.

No chart width, selected block system, sampled census, contact transition, or target absence is reported as observed. Even a completed finite screen would not exclude unsampled block motions or establish a continuous equilibrium-preserving path.

## 3. Recovery and verification contract

Save the complete source below as `W54_PATCH_RELEASE.py`. It uses only the Python standard library; the intended reproducibility environment is CPython 3.13.5. The actual runtime version was not inspectably confirmed here.

Preparation and the finite experiment are separate commands:

```sh
python -B -S W54_PATCH_RELEASE.py --prepare-only --blocks 4 --rays 4 --bits 24 --out W54_PREPARED
python -B -S W54_PATCH_RELEASE.py --blocks 4 --rays 4 --bits 24 --out W54_RUN
```

All requested non-default parameters are shown. There is no random seed, floating optimization, numerical hull tolerance, or positive-bar threshold. The exact parent is reconstructed from its complete literal A, p, q and M. Its exact volume, centroid, strict/closed-weak census, material carriers and full remaining Q fraction are asserted before a block system is used.

The standalone auditor reconstructs maximal supporting faces and true edges, integrates positive volume and the own centroid, tests full strict and closed-weak S/U/H conditions, records primitive zeros, and computes every positive P/Q bar with components, cuts, attaining edges and paths. Equal barcode levels are processed simultaneously. It writes the complete material-labelled input and audit for every sampled finite endpoint, together with actual byte counts and SHA256 receipts. No new output hash is invented here.

These are **programmed conditions, not observed terminal receipts**:

```
W54_PARENT_SELF_CHECK_PASS
W54_PATCH_PREPARED
W54_PATCH_ENDPOINT
W54_FINITE_BLOCK_RUN_COMPLETE
```

`W54_EXACT_OWN110_NO_ADDITIONAL_WEAK` is printed only after the full actual-hull audit gives strict110, additionalweak000, no positive P or Q bars, and E<=249. Its occurrence is not claimed.

A `NO_FEASIBLE_PATCH_PACK` result would concern the explicitly requested block count and listed critical blocks, not arbitrary host freedom. An unbracketed chart is reported rather than silently assigned a finite boundary.

## Complete runnable source

```python
"""Finite multi-vertex material-block release of the literal two-point hybrid.
Standard library only. Exact acceptance uses the actual convex hull and own COM.
Preparation and execution have not been observed in the accompanying handoff.
"""
import argparse
import hashlib
import itertools
import json
import sys
from collections import deque
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

PARENT = 'figure-0542'
PARENT_SHA = 'd8bc615c9cfaacf83c9a22bb08ffeda7dcf17a619428ef6c61f82a3a0c7a9ef7'
A = [
 [-2678,-1136,975],[-2745,-769,406],[-2212,-627,45],[96,-637,-245],
 [465,1184,-402],[80,119,-1160],[294,781,-935],[157,537,-1075],
 [311,1098,-580],[681,814,-815],[565,-379,-1032],[883,11,-962],
 [947,461,-856],[1007,793,-634],[840,1037,-473],[1206,848,-369],
 [1174,1065,103],[1389,818,-95],[1535,736,189],[1603,668,465],
 [1571,172,-108],[1639,563,721],[1644,425,972],[1609,244,1244],
 [1506,4,1547],[1301,-295,1859],[970,-604,2131],[548,-896,2304],
 [78,-1126,2365],[-418,-1288,2323],[-968,-1386,2170],[-1604,-1391,1853]
]
MI = [[98995,0,0],[971,98386,0],[-1592,3368,102673]]
PI = [-268884,-112219,95168]
QI = [57210,-67277,-92955]
V0 = F(48866057199911217841414872799,6000000000000000000000000000)
G0 = (
 F(-81928373233763022239117,1954629613996036000000000),
 F(-465553112358495819818249,1954629613996036000000000),
 F(6417163112727527836208561,19546296139960360000000000)
)
QDEPTH = F(
 24281893032213769980395324703584279562133073319971703278268479113191423457003553005297094668598356447,
 34267199924538813532793406874303293481012368770159432274442995705318756523380152800223615152162531697
)
Z = (F(0),F(0),F(0))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,t): return tuple(t*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))

def seed():
    raw = [tuple(F(x,1000) for x in a) for i,a in enumerate(A) if i != 3]
    labels = ['A'+str(i) for i in range(32) if i != 3]
    raw += [tuple(F(x,100000) for x in PI),tuple(F(x,100000) for x in QI)]
    labels += ['p','q']
    M = [[F(x,100000) for x in r] for r in MI]
    return [tuple(dot(r,p) for r in M) for p in raw], labels

def strings(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {str(k):strings(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [strings(v) for v in x]
    return x

def save(out,name,obj):
    data = (json.dumps(strings(obj),sort_keys=True,separators=(',',':'))+'\n').encode()
    (out/name).write_bytes(data)
    return dict(file=name,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())

def primitive(row):
    row = list(map(F,row))
    D = lcm(*(x.denominator for x in row))
    z = [int(D*x) for x in row]
    g = gcd(*(abs(x) for x in z))
    assert g
    return tuple(x//g for x in z)

def polygon(P,ids,n):
    drop = max(range(3),key=lambda j:abs(n[j]))
    axes = [j for j in range(3) if j != drop]
    unique = {}
    for i in sorted(ids):
        unique.setdefault((P[i][axes[0]],P[i][axes[1]]),i)
    order = [unique[k] for k in sorted(unique)]
    def orient(i,j,k):
        a,b,c = P[i],P[j],P[k]
        return ((b[axes[0]]-a[axes[0]])*(c[axes[1]]-a[axes[1]])
                -(b[axes[1]]-a[axes[1]])*(c[axes[0]]-a[axes[0]]))
    def half(seq):
        ans = []
        for i in seq:
            while len(ans)>=2 and orient(ans[-2],ans[-1],i)<=0:
                ans.pop()
            ans.append(i)
        return ans
    f = half(order)[:-1]+half(list(reversed(order)))[:-1]
    assert len(f)>=3
    if dot(cross(sub(P[f[1]],P[f[0]]),sub(P[f[2]],P[f[0]])),n)<0:
        f.reverse()
    return f

def hull(P):
    planes = set()
    for ia,ib,ic in itertools.combinations(range(len(P)),3):
        a,b,c = P[ia],P[ib],P[ic]
        n = cross(sub(b,a),sub(c,a))
        if n == Z: continue
        h = dot(n,a)
        s = [h-dot(n,p) for p in P]
        if min(s)<0<max(s): continue
        if min(s)==max(s)==0: continue
        if max(s)<=0:
            n = mul(n,-1)
            h = -h
        planes.add(primitive((*n,h)))
    planes = sorted(planes)
    assert len(planes)>=4
    faces = []
    for row in planes:
        n,h = row[:3],row[3]
        ids = [i for i,p in enumerate(P) if dot(n,p)==h]
        faces.append(polygon(P,ids,n))
    owners = {}
    for fi,f in enumerate(faces):
        for a,b in zip(f,f[1:]+f[:1]):
            owners.setdefault(tuple(sorted((a,b))),[]).append(fi)
    assert all(len(x)==2 for x in owners.values())
    vertices = sorted(set(i for f in faces for i in f))
    edges = sorted(owners)
    assert len(vertices)-len(edges)+len(faces)==2
    return vertices,faces,edges,owners,planes

def mass(P,faces):
    W = F(0)
    T = Z
    for f in faces:
        for j in range(1,len(f)-1):
            a,b,c = [P[i] for i in (f[0],f[j],f[j+1])]
            w = det(a,b,c)
            W += w
            T = add(T,mul(add(add(a,b),c),w))
    assert W>0
    volume = W/6
    moment = mul(T,F(1,24))
    centroid = mul(T,1/(4*W))
    return volume,moment,centroid

def chord(a,b):
    A,B,C = dot(a,a),dot(a,b),dot(b,b)
    if B>=A: return A
    if B>=C: return C
    return (A*C-B*B)/(A+C-2*B)

def barcode(points,edges):
    nodes = sorted(points)
    birth = {i:dot(points[i],points[i]) for i in nodes}
    weights = {e:chord(points[e[0]],points[e[1]]) for e in edges}
    parent = {i:i for i in nodes}
    members = {i:{i} for i in nodes}
    def root(i):
        while parent[i]!=i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def path(a,b,level):
        adj = {i:[] for i in nodes}
        for (u,v),w in weights.items():
            if w>=level:
                adj[u].append(v)
                adj[v].append(u)
        todo = deque([a])
        prev = {a:None}
        while todo and b not in prev:
            u = todo.popleft()
            for v in sorted(adj[u]):
                if v not in prev:
                    prev[v] = u
                    todo.append(v)
        assert b in prev
        ans = [b]
        while ans[-1]!=a: ans.append(prev[ans[-1]])
        return list(reversed(ans))
    bars = []
    batches = {}
    for e,w in weights.items(): batches.setdefault(w,[]).append(e)
    for level in sorted(batches,reverse=True):
        adj = {}
        for a,b in batches[level]:
            a,b = root(a),root(b)
            if a!=b:
                adj.setdefault(a,set()).add(b)
                adj.setdefault(b,set()).add(a)
        unseen = set(adj)
        groups = []
        while unseen:
            r = min(unseen)
            group = {r}
            stack = [r]
            unseen.remove(r)
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if v in unseen:
                        unseen.remove(v)
                        group.add(v)
                        stack.append(v)
            groups.append(sorted(group))
        for group in groups:
            keep = min(group,key=lambda r:(-birth[r],r))
            merged = set().union(*(members[r] for r in group))
            for r in group:
                if r==keep or birth[r]==level: continue
                assert birth[r]>level
                component = members[r]
                cut = [e for e in edges if (e[0] in component)!=(e[1] in component)]
                assert cut and max(weights[e] for e in cut)==level
                attaining = min(e for e in cut if weights[e]==level)
                bars.append(dict(peak=r,elder=keep,birth=birth[r],death=level,
                    depth=birth[r]-level,relative_depth=(birth[r]-level)/birth[r],
                    component=sorted(component),cut=cut,attaining_edge=attaining,
                    path=path(r,keep,level)))
            for r in group:
                if r!=keep:
                    parent[r] = keep
                    del members[r]
            members[keep] = merged
    assert len({root(i) for i in nodes})==1
    return bars

def audit(P,labels):
    vertices,faces,edges,owners,planes = hull(P)
    V,M,g = mass(P,faces)
    X = {i:sub(P[i],g) for i in vertices}
    assert all(row[3]-dot(row[:3],g)>0 for row in planes)
    S,U,H = [],[],[]
    Sw,Uw,Hw = [],[],[]
    Sz,Uz,Hz = [],[],[]
    for fi,f in enumerate(faces):
        n = planes[fi][:3]
        s = [-dot(cross(n,sub(P[b],P[a])),X[a])
             for a,b in zip(f,f[1:]+f[:1])]
        if min(s)>0: S.append(fi)
        if min(s)>=0: Sw.append(fi)
        if 0 in s: Sz.append(fi)
    for i in vertices:
        neigh = [b if a==i else a for a,b in edges if i in (a,b)]
        s = [dot(X[i],sub(P[j],P[i])) for j in neigh]
        if max(s)<0: U.append(i)
        if max(s)<=0: Uw.append(i)
        if 0 in s: Uz.append(i)
    for e in edges:
        a,b = e
        d = sub(P[b],P[a])
        dd = dot(d,d)
        tn = -dot(X[a],d)
        r = add(mul(X[a],dd),mul(d,tn))
        f1,f2 = owners[e]
        n1,n2 = planes[f1][:3],planes[f2][:3]
        aa,ab,bb = dot(n1,n1),dot(n1,n2),dot(n2,n2)
        assert aa*bb-ab*ab>0
        l1 = bb*dot(r,n1)-ab*dot(r,n2)
        l2 = aa*dot(r,n2)-ab*dot(r,n1)
        s = [tn,dd-tn,l1,l2]
        if min(s)>0: H.append(e)
        if min(s)>=0: Hw.append(e)
        if 0 in s: Hz.append(e)
    Pbars = barcode(X,edges)
    dual = {fi:mul(row[:3],1/(row[3]-dot(row[:3],g)))
            for fi,row in enumerate(planes)}
    dualedges = sorted(set(tuple(sorted(x)) for x in owners.values()))
    Qbars = barcode(dual,dualedges)
    strict = [len(S),len(U),len(H)]
    weak = [len(Sw),len(Uw),len(Hw)]
    extra = [weak[i]-strict[i] for i in range(3)]
    zero = [len(Sz),len(Uz),len(Hz)]
    if zero==[0,0,0]:
        assert len(S)+len(U)-len(H)==2
        assert len(Pbars)==len(U)-1 and len(Qbars)==len(S)-1
    return dict(parent=PARENT,parent_sha256=PARENT_SHA,labels=labels,input_points=P,
        vertices=vertices,points=[P[i] for i in vertices],faces=faces,edges=edges,
        supporting_planes=planes,V=len(vertices),E=len(edges),F=len(faces),C=2*len(edges),
        volume=V,first_moment=M,centroid=g,S=S,U=U,H=H,strict=strict,weak=weak,
        additional_weak=extra,primitive_zero=zero,closed_weak_ids=[Sw,Uw,Hw],
        primitive_zero_ids=[Sz,Uz,Hz],P_bars=Pbars,Q_bars=Qbars,
        stable_material_faces=[[labels[i] for i in faces[j]] for j in S],
        unstable_material_vertices=[labels[i] for i in U],
        saddle_material_edges=[[labels[i] for i in e] for e in H],
        root_star=([j for j,f in enumerate(faces) if U[0] in f] if len(U)==1 else None))

def nullspace(R):
    R = [list(map(F,r)) for r in R]
    m,n = len(R),len(R[0])
    piv = []
    r = 0
    for c in range(n):
        k = next((k for k in range(r,m) if R[k][c]),None)
        if k is None: continue
        R[r],R[k] = R[k],R[r]
        s = R[r][c]
        R[r] = [x/s for x in R[r]]
        for k in range(m):
            if k!=r and R[k][c]:
                s = R[k][c]
                R[k] = [a-s*b for a,b in zip(R[k],R[r])]
        piv.append(c)
        r += 1
        if r==m: break
    N = []
    for c in range(n):
        if c in piv: continue
        v = [F(0)]*n
        v[c] = F(1)
        for j,p in enumerate(piv): v[p] = -R[j][c]
        N.append(v)
    return N,piv

def block_system(P,faces,blocks):
    k = len(blocks)
    R = [[F(0)]*(3*k) for _ in range(k+4)]
    parts = []
    assert all(sum(bool(set(f)&set(b)) for b in blocks)<=1 for f in faces)
    for bi,block in enumerate(blocks):
        selected = set(block)
        A,C = Z,Z
        J = [[F(0)]*3 for _ in range(3)]
        for f in faces:
            assert len(f)==3
            a,b,c = [P[j] for j in f]
            e = [int(j in selected) for j in f]
            m = sum(e)
            if not m: continue
            L = add(add(mul(cross(b,c),e[0]),mul(cross(c,a),e[1])),
                    mul(cross(a,b),e[2]))
            s = add(add(a,b),c)
            w = det(a,b,c)
            A = add(A,L)
            C = add(C,mul(L,m))
            for u in range(3):
                for v in range(3):
                    J[u][v] += s[u]*L[v]+(m*w if u==v else 0)
        for v in range(3):
            R[bi][3*bi+v] = C[v]
            R[k][3*bi+v] = A[v]
        for u in range(3):
            for v in range(3): R[k+1+u][3*bi+v] = J[u][v]
        parts.append(dict(block=block,A=A,C=C,J=J))
    N,piv = nullspace(R)
    assert all(all(dot(row,v)==0 for row in R) for v in N)
    return R,N,piv,parts

def choose_blocks(P,labels,faces,edges,k):
    lookup = {s:i for i,s in enumerate(labels)}
    critical = [
      ['A31','A30','A4','q','A29','A2','A5','p'],
      ['A30','q','A29','A2','A5'],
      ['A30','q','A29'],
      ['A2','A5','p'],
      ['A2','A5']
    ]
    edge_set = set(edges)
    def adjacent(a,b): return tuple(sorted((a,b))) in edge_set
    for names in critical:
        block = sorted(lookup[s] for s in names)
        pool = [i for i in range(len(P)) if i not in block
                and all(not adjacent(i,j) for j in block)]
        candidates = []
        center = mul(tuple(sum((P[i][j] for i in block),F(0))
                           for j in range(3)),F(1,len(block)))
        for extra in itertools.combinations(pool,k-1):
            if any(adjacent(a,b) for a,b in itertools.combinations(extra,2)): continue
            reps = [center]+[P[i] for i in extra]
            score = sum((dot(sub(a,b),sub(a,b))
                         for a,b in itertools.combinations(reps,2)),F(0))
            candidates.append((score,extra))
        candidates.sort(key=lambda x:(-x[0],x[1]))
        for score,extra in candidates:
            blocks = [block]+[[i] for i in extra]
            moving = set().union(*(set(b) for b in blocks))
            fixed = [i for i in range(len(P)) if i not in moving]
            tetra = next((t for t in itertools.combinations(fixed,4)
                if det(sub(P[t[1]],P[t[0]]),sub(P[t[2]],P[t[0]]),
                       sub(P[t[3]],P[t[0]]))),None)
            if tetra is None: continue
            R,N,piv,parts = block_system(P,faces,blocks)
            if not N: continue
            movable = all(any(any(v[3*j+c] for c in range(3)) for v in N)
                          for j in range(k))
            if movable:
                return blocks,R,N,piv,parts,list(tetra)
    raise ArithmeticError('NO_FEASIBLE_PATCH_PACK_FOR_LISTED_BLOCKS_AND_REQUESTED_COUNT')

def directions(N,blocks,npoints,wanted):
    q,k = len(N),len(blocks)
    candidates = list(N)
    for s in range(1,k*max(1,q-1)+wanted+3):
        candidates.append([sum((F(s**j)*N[j][i] for j in range(q)),F(0))
                           for i in range(3*k)])
    ans,seen = [],set()
    for v in candidates:
        if any(not any(v[3*j+c] for c in range(3)) for j in range(k)): continue
        size = max(map(abs,v))
        v = tuple(x/size for x in v)
        for sign in (1,-1):
            w = tuple(sign*x for x in v)
            if w in seen: continue
            seen.add(w)
            d = [Z]*npoints
            for j,block in enumerate(blocks):
                for i in block: d[i] = tuple(w[3*j:3*j+3])
            ans.append(d)
            if len(ans)==wanted: return ans
    assert ans
    return ans

def slack_polynomials(P,faces,d):
    rows = []
    for f in faces:
        ia,ib,ic = f
        a,b,c = P[ia],P[ib],P[ic]
        da,db,dc = d[ia],d[ib],d[ic]
        u,v = sub(b,a),sub(c,a)
        du,dv = sub(db,da),sub(dc,da)
        assert cross(du,dv)==Z
        n0 = cross(u,v)
        n1 = add(cross(du,v),cross(u,dv))
        for j in range(len(P)):
            if j in f: continue
            x,dx = sub(a,P[j]),sub(da,d[j])
            row = (dot(n0,x),dot(n1,x)+dot(n0,dx),dot(n1,dx))
            assert row[0]>0
            rows.append(row)
    return rows

def positive_segment(rows,t):
    for a,b,c in rows:
        if a+b*t+c*t*t<=0: return False
        if c>0:
            s = -b/(2*c)
            if 0<s<t and a+b*s+c*s*s<=0: return False
    return True

def chart_bound(rows,bits):
    lo,hi = F(0),F(1)
    for _ in range(64):
        if not positive_segment(rows,hi): break
        lo,hi = hi,2*hi
    else:
        raise ArithmeticError('STRICT_CHART_BOUND_NOT_BRACKETED_WITHIN_2_TO_64')
    for _ in range(bits):
        mid = (lo+hi)/2
        if positive_segment(rows,mid): lo = mid
        else: hi = mid
    while lo==0:
        mid = hi/2
        if positive_segment(rows,mid): lo = mid
        else: hi = mid
    assert positive_segment(rows,lo) and not positive_segment(rows,hi)
    return lo,hi

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out',default='W54_RUN')
    ap.add_argument('--blocks',type=int,default=4)
    ap.add_argument('--rays',type=int,default=4)
    ap.add_argument('--bits',type=int,default=24)
    ap.add_argument('--prepare-only',action='store_true')
    args = ap.parse_args()
    assert 3<=args.blocks<=7 and args.rays>0 and args.bits>=8
    out = Path(args.out)
    out.mkdir(parents=True,exist_ok=True)
    P,labels = seed()
    base = audit(P,labels)
    assert (base['V'],base['E'],base['F'])==(33,93,62)
    assert base['volume']==V0 and base['centroid']==G0
    assert base['strict']==base['weak']==[2,1,1]
    assert base['additional_weak']==base['primitive_zero']==[0,0,0]
    assert not base['P_bars'] and len(base['Q_bars'])==1
    assert base['Q_bars'][0]['relative_depth']==QDEPTH
    assert {frozenset(x) for x in base['stable_material_faces']}=={
        frozenset(['A31','A30','A4']),frozenset(['A30','q','A29'])}
    assert base['unstable_material_vertices']==['p']
    assert {frozenset(x) for x in base['saddle_material_edges']}=={
        frozenset(['A2','A5'])}
    parent_receipt = save(out,'W54_PARENT_AUDIT.json',base)
    print('W54_PARENT_SELF_CHECK_PASS',parent_receipt,flush=True)
    faces,edges = base['faces'],base['edges']
    assert all(len(f)==3 for f in faces)
    blocks,R,N,piv,parts,tetra = choose_blocks(P,labels,faces,edges,args.blocks)
    rays = directions(N,blocks,len(P),args.rays)
    source = Path(__file__).read_bytes()
    parameters = dict(parent=PARENT,parent_sha256=PARENT_SHA,labels=labels,
        input_points=P,parent_faces=faces,parent_edges=edges,blocks=blocks,
        material_blocks=[[labels[i] for i in b] for b in blocks],
        fixed_tetrahedron=tetra,constraints=R,rank=len(piv),nullspace=N,
        block_coefficients=parts,directions=rays,options=vars(args),
        source_bytes=len(source),source_sha256=hashlib.sha256(source).hexdigest())
    receipt = save(out,'W54_PARAMETERS.json',parameters)
    print('W54_PATCH_PREPARED',len(blocks),len(piv),len(N),len(rays),receipt,flush=True)
    if args.prepare_only: return
    records = []
    M0 = base['first_moment']
    for ri,d in enumerate(rays):
        # These are polynomial-identity checks on the oriented original chain,
        # not claims that this chain is a convex boundary at t=-1,1,2.
        for t in (F(-1),F(1),F(2)):
            formal = [add(p,mul(v,t)) for p,v in zip(P,d)]
            vol,mom,com = mass(formal,faces)
            assert vol==V0 and mom==M0 and com==G0
        rows = slack_polynomials(P,faces,d)
        lo,hi = chart_bound(rows,args.bits)
        samples = [('inside_half',lo/2),('inside_contact',lo),
                   ('beyond_5_4',hi*F(5,4)),('beyond_2',hi*2)]
        for phase,t in samples:
            PP = [add(p,mul(v,t)) for p,v in zip(P,d)]
            name = 'W54_R%02d_%s'%(ri,phase)
            inp = dict(name=name,parent=PARENT,parent_sha256=PARENT_SHA,
                       labels=labels,points=PP,ray=ri,t=t,
                       chart_lower=lo,chart_upper=hi,phase=phase)
            ir = save(out,name+'.json',inp)
            result = audit(PP,labels)
            same = {frozenset(f) for f in result['faces']}=={
                    frozenset(f) for f in faces}
            if phase.startswith('inside'):
                assert positive_segment(rows,t) and same
                assert result['volume']==V0
                assert result['first_moment']==M0 and result['centroid']==G0
            result['input_sha256'] = ir['sha256']
            result['same_original_maximal_face_sets'] = same
            result['centroid_change_from_parent'] = sub(result['centroid'],G0)
            ar = save(out,name+'_AUDIT.json',result)
            assert result['V']<=33 and result['E']<=93
            target = (result['strict']==[1,1,0]
                      and result['additional_weak']==[0,0,0]
                      and not result['P_bars'] and not result['Q_bars']
                      and result['E']<=249)
            rec = dict(name=name,input=ir,audit=ar,ray=ri,t=t,phase=phase,
                chart_lower=lo,chart_upper=hi,strict=result['strict'],
                weak=result['weak'],additional_weak=result['additional_weak'],
                primitive_zero=result['primitive_zero'],V=result['V'],E=result['E'],
                F=result['F'],P=len(result['P_bars']),Q=len(result['Q_bars']),target=target)
            records.append(rec)
            print('W54_PATCH_ENDPOINT',strings(rec),flush=True)
            if target:
                print('W54_EXACT_OWN110_NO_ADDITIONAL_WEAK',name,flush=True)
    summary = save(out,'W54_RUN_MANIFEST.json',dict(parent_audit=parent_receipt,
        parameters=receipt,endpoints=records,target_count=sum(r['target'] for r in records)))
    print('W54_FINITE_BLOCK_RUN_COMPLETE',len(records),summary,flush=True)

if __name__=='__main__':
    main()
```

## Handoff boundary

The finite block identities and quadratic support-domain statement are proved above. Their usefulness for this specific host is not established by an observed selected matrix, nonzero critical projection, finite chart, or endpoint. No finite search has been converted into a global obstruction, and no numerical or unexecuted source output has been promoted to an accepted body.

The next useful continuation is first to restore inspectable complete-pack reading, then obtain the exact preparation result. A compatible multi-vertex critical block would give a finite actual-mass host freedom distinct from both a fixed-host two-point search and independent single-star rails. Its beyond-contact samples must be judged only by their regenerated actual-hull audits. Until such evidence is available, **FOURFREE_D100000 remains the durable entrance; this handoff contributes a proved, executable but unverified material-family construction, not a new equilibrium record.**
