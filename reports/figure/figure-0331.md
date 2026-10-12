# figure-0331

AI research report · 2026-09-06 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Vivid Lynx 76 — exact vertex-loss construction and support-event mass correction

## 1. Determination

**No smaller Gömböc is promoted in this continuation.** I do not have a fresh readable acceptance report together with the literal output table for a reduced endpoint. Consequently, I make neither a new C<1000 claim nor a claim that an unpreserved numerical checkpoint is a verified successor.

The last fully identified winner used here is the lead's **STRICT323**, with `(V,E,F,C)=(323,962,641,1924)` and strict ordinary-volume-centred class `(1,1,0)`. It is distinct from the immutable method parent's recovered FUS-SUB4001. The journal supplies every STRICT323 coordinate and integration triangle in its NG01 capsule, together with its exact mass sums. 

This handoff supplies two exact constructive results rather than an unsupported smaller-winner report:

1. **A rational six-control, C2-symmetric neighbour-translation construction that guarantees disappearance of a selected vertex and its mate at its endpoint.** Under explicit affine x-range guards, the stable quadrilateral and unstable apex remain strict equilibria at the body's actual volume centroid throughout. Every admissible endpoint has at most 321 extreme vertices and true-edge budget at most 1912. Additional equilibria may occur; no endpoint is called a Gömböc without the exhaustive census.
2. **An exact correction for ordinary-volume and first-moment formulas across a quadrilateral support flip.** It identifies a first-order centroid derivative change which ordinary smaller-step backtracking does not remove. A complete five-vertex rational fixture demonstrates the change explicitly.

For the neighbour-translation family, all velocities lie in a two-dimensional linear space. On every actual hull cell, support events have degree at most two, volume degree at most two, first moments degree at most three, vertex mechanics degree at most four, and face-side/full-edge-cone mechanics degree at most six after clearing the positive centroid denominator. This gives a bounded-degree exact continuation problem on the actual 323-point input.

## 2. Source identity and validation requirements

The immutable **method parent** is

```text
figure-0316
SHA-256 d552b87dce37c082460f4c327103cb2e9c59c80178bdd2908e73e0801cfe7c51.
```

It is not the coordinate definition of STRICT323. In particular, its 4001-point deletion mask, fusion coordinates and recovered-pass provenance do not transfer to the new input. The journal explicitly preserves this distinction. 

The separate geometric input is the capsule under the exact journal heading

```text
### STRICT323 — exact winner110,C1924
```

Its defining checks are:

```text
NG01 header: D=100000000000000, h=161, a=1, t=642
Decompressed stream SHA-256:
6ecdf84ca0c79201e5c66d14562a510252b0e5dc8962f31a18c0449ba7116adb

W = sum det(I_i,I_j,I_k)
  = 866130105633472884658718756283071557322276871251756

M = sum det(I_i,I_j,I_k)*(I_i+I_j+I_k)
  = (-4648652936059315079947769330829326900864550057143760,0,0)

C0 = 216532526408368221164679689070767889330569217812939
B0 = (-290540808503707192496735583176832931304034378571485,0,0).
```

The raw body is `conv(I/D)`. Its exact centred version is

\[
\operatorname{conv}\left\{\frac{C_0I_i-B_0}{C_0D}\right\},
\qquad \operatorname{Vol}=\frac{W}{6D^3}.
\]

These are source-validation targets, not newly inferred values. The source stable cycle is `[0,2,3,1]`, and the source apex is 322. The new code below requires the stream hash and mass sums before constructing a candidate. It does not retrieve an old scratch archive or reconstruct coordinates from a checksum alone.

## 3. Guaranteed genuine vertex loss by moving neighbours

Let P be a convex polyhedron invariant under

\[
R(x,y,z)=(x,-y,-z).
\]

Choose a noncritical vertex v and three distinct neighbours a,b,c. Choose exact rational positive weights

\[
\alpha,\beta,\gamma>0,\qquad \alpha+\beta+\gamma=1,
\]

and put

\[
p=\alpha a+\beta b+\gamma c,\qquad d=v-p.
\]

Require a,b,c to be noncollinear. Also require the two control triples `{a,b,c}` and `{Ra,Rb,Rc}` to be disjoint and not to contain either v or Rv.

Define a one-parameter point configuration by translating the first triple by `s d`, translating its reflected triple by `s R d`, and leaving all other points fixed. Define the actual body at every parameter by its convex hull:

\[
P(s)=\operatorname{conv}\{p_i(s)\},\qquad 0\leq s\leq1.
\]

Then, exactly at s=1,

\[
v=\alpha(a+d)+\beta(b+d)+\gamma(c+d).
\]

Thus v lies in the relative interior of a nondegenerate triangle of other supplied points. **It is not an extreme point of P(1).** The same holds for Rv. This is a literal convex-combination certificate, not a numerical normal-rank estimate or a union of separately visible facets.

If v remains on the boundary at the event, every supporting functional at v must be constant on that entire triangle. Its normal cone therefore has dimension at most one. If the triangle lies inside the new body, v is an interior point instead. Either case eliminates v as a true vertex. The complete hull must still be rebuilt to detect other simultaneous losses and to remove collinear boundary segments.

This operation releases the selected neighbours' y and z coordinates. It does not pretend that a generic fixed-yz point can disappear into an edge without the required projected collinearity.

### Deterministic rational weights

For each neighbour triple, project v orthogonally onto its affine plane using the exact 2×2 Gram system. Retain triples whose projection has three strictly positive barycentric coordinates. Among admissible triples, choose the smallest exact squared displacement `|d|²`, with lexicographic tie-breaking.

This is a complete selector, not an optimizer-dependent missing parameter. It is intentionally restricted to triangular relative-interior loss. A two-neighbour version would give edge-relative loss, but its normal cone and post-event boundary require a different rank-two check.

### Protecting the critical features at the actual centroid

Keep every stable-quadrilateral vertex and the apex fixed. Let their raw x coordinates be `x_S<x_U`. Impose on every translated control the strict endpoint guard

\[
x_S<x_i(1)<x_U.
\]

The source satisfies the same strict inequalities for its noncritical points. Since each control's x coordinate is affine, these guards hold for all s in `[0,1]`.

Therefore the original quadrilateral remains the complete supporting facet in `x=x_S`, and the original apex remains the unique maximizer of x. The filled body remains C2-symmetric, so its actual volume centroid has the form `(g_x(s),0,0)`.

The perpendicular foot on the stable plane is `(x_S,0,0)`, strictly inside the unchanged centrally symmetric quadrilateral. Hence this facet is a **strict stable equilibrium at the actual centroid for the whole interval**.

The apex A remains strictly unstable, because for every other point q,

\[
(A-g)\cdot(q-A)=(x_U-g_x)(q_x-x_U)<0.
\]

The centroid is interior, so the first factor is positive. Thus loss of either protected equilibrium is not the failure mode of this family. Any failure to be a Gömböc consists of additional equilibria elsewhere, which must be enumerated explicitly.

Require additionally that four untouched source points form a nonzero-volume tetrahedron. That fixed tetrahedron remains inside P(s), proving full dimensionality and positive volume throughout. The code tests this condition rather than assuming it.

### Exact endpoint edge-budget bound

At least v and Rv disappear, so `V(P(1))<=321`. The protected maximal quadrilateral persists. Euler's formula and face-degree counting give

\[
E\leq3V-7,
\qquad 2E\leq6V-14\leq1912.
\]

This is a bound on the **true-edge budget of every admissible constructed endpoint**, not a Gömböc-complexity record. The equilibrium class remains an open acceptance test.

## 4. Mass and mechanics on the actual support cells

All velocities in this construction belong to

\[
\operatorname{span}\{d,Rd\},
\]

a space of dimension at most two. Consequently every determinant of three velocity differences vanishes.

On a fixed actual outward triangulation T, define

\[
W(s)=\sum_{(i,j,k)\in T}\det(p_i(s),p_j(s),p_k(s)),
\]

\[
M(s)=\sum_{(i,j,k)\in T}\det(p_i(s),p_j(s),p_k(s))
\bigl(p_i(s)+p_j(s)+p_k(s)\bigr).
\]

Then

\[
\deg W\leq2,\qquad \deg M\leq3,
\qquad V=W/6,\qquad g=M/(4W).
\]

The y and z moment polynomials vanish exactly by symmetry. No density change, vertex-mass average or freely chosen mechanical centre is involved.

Every four-point support determinant also has degree at most two. Thus the first support event along any such fixed rational direction is rational or quadratic algebraic. One must include all current facet–point support tests and triangle rank tests, not merely the selected cavity's four points.

For a true edge i–j, an exact directed vertex predicate after multiplication by positive `4W` is

\[
A_{ij}=4W\,p_i\cdot(p_j-p_i)-M\cdot(p_j-p_i),
\]

of degree at most four.

For an outward face normal N_f and oriented boundary edge i→j, a face-side predicate is

\[
B_{fij}=N_f\cdot\left[
4W(p_i\times p_j)-(p_i-p_j)\times M
\right],
\]

of degree at most six. This is the sign of the actual-centroid face-side expression after a positive denominator is cleared.

For the two maximal faces incident to a true edge, with opposite edge orientations, the full saddle conditions are

```text
A_ij<0, A_ji<0, B_fij>0, B_gji>0.
```

All four conditions are required. Weak nonnegativity of the corresponding four signed tests, with at least one zero, detects a boundary equilibrium. At a rank-loss parameter, first remove redundant points, collinear boundary pieces and coplanar triangulation diagonals; a vanished artificial diagonal is not a mechanical degeneracy.

This yields a finite exact continuation procedure: isolate the degree-two support events, rebuild the actual hull at each event and on each side, reintegrate W and M on each actual cell, and isolate or certify the degree-at-most-six mechanical predicates. The construction does not assert that every cell has class `(1,1,0)`.

## 5. Exact mass correction at a quadrilateral flip

This is important when a solver reaches a flat support circuit and then keeps shortening its step without entering the next chart.

Let a,b,c,d have the cyclic order of a supporting quadrilateral at the wall. The two oriented patches are

```text
T_ac = (a,b,c), (a,c,d)
T_bd = (a,b,d), (b,c,d).
```

Set

\[
\Delta=\det(b-a,c-a,d-a),\qquad S=a+b+c+d.
\]

Direct determinant expansion gives the exact identities

\[
W_{bd}-W_{ac}=\Delta,
\qquad M_{bd}-M_{ac}=\Delta S.
\]

Here W is the six-volume numerator and M the 24-first-moment numerator. Therefore, when these patches are the two actual hull branches,

\[
V_{bd}-V_{ac}=\Delta/6,
\qquad \mathcal M_{bd}-\mathcal M_{ac}=\Delta S/24.
\]

The algebraic identities hold for the patches themselves. To apply them to the body, certify that the cavity boundary is unchanged and that the selected branch is globally supporting. A determinant sign alone is not a complete hull certificate.

At a wall with `Delta=0`, positions and moments agree, but derivatives need not. The difference between the two one-sided centroid derivatives is

\[
\boxed{
\dot g_{bd}-\dot g_{ac}
=\frac{\dot\Delta}{24V}\bigl(S-4g\bigr).
}
\]

This is a **first-order** difference. Decreasing the step length does not turn the wrong branch's centroid derivative into the right one.

When the outward branch is selected by the sign of Delta, its mass correction contains a positive-part term `max(0,Delta)`. In a first-order feasibility model at the wall this becomes `max(0,ell(delta_p))`, where ell is the exact linearized circuit determinant. Merely imposing epigraph inequalities does not enforce equality to that maximum, because its coefficient in the moment equation can have either sign. Use the two actual sign branches, a valid complementarity formulation, or an exact event crossing and rechart.

For several disjoint cavities, the patch corrections add. Overlapping circuits do not justify independent sign choices without a compatible complete triangulation.

### Complete rational fixture

Take

```text
O=(1/2,1/2,0)
a=(0,0,1)
b=(1,0,1)
c=(1,1,1)
d=(0,1,1+s),     -1/2<=s<=1/2.
```

The four lateral triangles are `(b,a,O)`, `(c,b,O)`, `(d,c,O)`, `(a,d,O)`. For negative s, the actual roof is T_ac; for positive s it is T_bd. At zero the roof is one maximal quadrilateral. The supporting inequalities verify these branches over their whole respective intervals.

Exact integration gives

\[
V(s)=\begin{cases}1/3,&s\leq0,\\(2+s)/6,&s\geq0,\end{cases}
\]

\[
g_x=g_y=1/2,
\qquad
g_z(s)=\begin{cases}3/4+s/8,&s\leq0,\\3/4+s/4,&s\geq0.\end{cases}
\]

Thus the centroid's z derivative changes from `1/8` to `1/4` at the support wall. At `s=-1/2,0,1/2`, the exact `(volume,g_z)` pairs are `(1/3,11/16)`, `(1/3,3/4)`, and `(5/12,7/8)`.

This is a five-vertex fixture, **not a Gömböc**. Its true incidence is `(5,8,5)` at zero and `(5,9,6)` on either strict side. It isolates the mass-chart issue without relying on a large numerical example.

## 6. Complete exact next-execution program

The following program is a proposed exact finite-frontier test, **not a returned acceptance report**. It reads the already supplied journal, validates STRICT323's complete capsule and mass, constructs admissible neighbour-translation endpoints, rebuilds each actual convex hull using integer arithmetic, removes redundant points, and performs a full own-centroid feature census.

It uses no numerical optimizer or Qhull. It imports none of the earlier verification implementations. If it finds a smaller strict `(1,1,0)` endpoint, it writes the complete integer table, actual maximal faces, integration triangles, exact mass data and operation. That output must still receive the requested second independently implemented full audit before promotion.

Save as `rank2_frontier.py` and run:

```sh
python3 -S rank2_frontier.py research-journal\(20260905-155840\).md 12
```

The optional final integer bounds the number of candidate endpoints. An exhausted bound is not an infeasibility theorem.

```python
from fractions import Fraction as Q
from itertools import combinations
from collections import defaultdict
from functools import reduce
from math import gcd, lcm
from pathlib import Path
import base64, hashlib, json, re, sys, zlib

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def plane(P,f):
    a,b,c=(P[i] for i in f)
    N=cross(sub(b,a),sub(c,a))
    return N,dot(N,a)
def primitive(N,h):
    z=reduce(gcd,(*N,h))
    assert z>0
    return tuple(x//z for x in (*N,h))

def decode(journal):
    text=Path(journal).read_text(encoding='utf-8')
    text=text.split('### STRICT323 — exact winner110,C1924',1)[1]
    s=re.search(r'```text\s*(.*?)```',text,re.S).group(1)
    raw=zlib.decompress(base64.b85decode(''.join(s.split())))
    assert hashlib.sha256(raw).hexdigest()==(
        '6ecdf84ca0c79201e5c66d14562a510252b0e5dc8962f31a18c0449ba7116adb')
    assert raw[:4]==b'NG01'
    pos=4
    def uint():
        nonlocal pos
        value=shift=0
        while True:
            b=raw[pos];pos+=1
            value|=(b&127)<<shift
            if b<128:return value
            shift+=7
    D,h,a,t=[uint() for _ in range(4)]
    assert (D,h,a,t)==(10**14,161,1,642)
    def table(n):
        out=[[0,0,0] for _ in range(n)]
        for k in range(3):
            last=0
            for i in range(n):
                q=uint()
                last+=q//2 if q%2==0 else -q//2
                out[i][k]=last
        return out
    H=table(h+a)
    P=sorted(map(tuple,H[:h]+[[x,-y,-z] for x,y,z in H[:h]]+H[h:]))
    T=table(t)
    assert pos==len(raw)
    W,M=integrate(P,T)
    assert W==866130105633472884658718756283071557322276871251756
    assert M==[-4648652936059315079947769330829326900864550057143760,0,0]
    return P,D

def integrate(P,T):
    W=0;M=[0,0,0]
    for f in T:
        a,b,c=(P[i] for i in f)
        w=det(a,b,c);W+=w
        for k in range(3):M[k]+=w*(a[k]+b[k]+c[k])
    return W,M

def seed4(P,ids=None):
    ids=list(range(len(P))) if ids is None else list(ids)
    i=ids[0]
    j=max(ids,key=lambda j:dot(sub(P[j],P[i]),sub(P[j],P[i])))
    e=sub(P[j],P[i])
    k=max(ids,key=lambda k:dot(cross(e,sub(P[k],P[i])),
                              cross(e,sub(P[k],P[i]))))
    N=cross(e,sub(P[k],P[i]))
    l=max(ids,key=lambda l:abs(dot(N,sub(P[l],P[i]))))
    assert dot(N,sub(P[l],P[i]))!=0
    return [i,j,k,l]

def incremental(P):
    seed=seed4(P)
    O=tuple(sum(P[i][k] for i in seed) for k in range(3))
    def orient(f):
        N,h=plane(P,f)
        s=dot(N,O)-4*h
        assert s!=0
        return tuple(f if s<0 else (f[0],f[2],f[1]))
    F=[orient(f) for f in combinations(seed,3)]
    for p in range(len(P)):
        if p in seed:continue
        visible=[]
        for i,f in enumerate(F):
            N,h=plane(P,f)
            if dot(N,P[p])>h:visible.append(i)
        if not visible:continue
        horizon={}
        for i in visible:
            f=F[i]
            for a,b in zip(f,f[1:]+f[:1]):
                if (b,a) in horizon:del horizon[b,a]
                else:horizon[a,b]=1
        gone=set(visible)
        F=[f for i,f in enumerate(F) if i not in gone]
        for a,b in horizon:
            N,h=plane(P,(a,b,p))
            if any(N):F.append(orient((a,b,p)))
    return F

def polygon(P,ids,N):
    drop=max(range(3),key=lambda k:abs(N[k]))
    axes=[k for k in range(3) if k!=drop]
    ids=sorted(ids,key=lambda i:(P[i][axes[0]],P[i][axes[1]]))
    def turn(i,j,k):
        a,b,c=[(P[v][axes[0]],P[v][axes[1]]) for v in (i,j,k)]
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[];hi=[]
    for i in ids:
        while len(lo)>1 and turn(lo[-2],lo[-1],i)<=0:lo.pop()
        lo.append(i)
    for i in reversed(ids):
        while len(hi)>1 and turn(hi[-2],hi[-1],i)<=0:hi.pop()
        hi.append(i)
    f=lo[:-1]+hi[:-1]
    assert len(f)>=3
    if dot(N,cross(sub(P[f[1]],P[f[0]]),sub(P[f[2]],P[f[0]])))<0:
        f.reverse()
    return f

def census(P,D):
    P=sorted(set(map(tuple,P)))
    proposal=incremental(P)
    planes=sorted({primitive(*plane(P,f)) for f in proposal})
    cycles=[]
    for pl in planes:
        N,h=pl[:3],pl[3]
        values=[h-dot(N,p) for p in P]
        assert min(values)>=0
        contacts=[i for i,v in enumerate(values) if v==0]
        f=polygon(P,contacts,N)
        for i,j in zip(f,f[1:]+f[:1]):
            for k in contacts:
                assert dot(N,cross(sub(P[j],P[i]),sub(P[k],P[i])))>=0
            for k in set(f)-{i,j}:
                assert dot(N,cross(sub(P[j],P[i]),sub(P[k],P[i])))>0
        cycles.append(f)
    used=sorted({i for f in cycles for i in f},key=lambda i:P[i])
    index={old:i for i,old in enumerate(used)}
    X=[P[i] for i in used]
    cycles=[[index[i] for i in f] for f in cycles]
    E=defaultdict(list);inc=[[] for _ in X]
    for fi,f in enumerate(cycles):
        for i in f:inc[i].append(fi)
        for i,j in zip(f,f[1:]+f[:1]):
            E[tuple(sorted((i,j)))].append((fi,i,j))
    assert len(X)-len(E)+len(cycles)==2
    for fs in E.values():
        assert len(fs)==2 and fs[0][1:]==fs[1][1:][::-1]
    for fs in inc:
        assert any(det(planes[i][:3],planes[j][:3],planes[k][:3])!=0
                   for i,j,k in combinations(fs,3))
    # Closed links and connectedness on the maximal-face boundary.
    neighbours=[set() for _ in X]
    for i,j in E:neighbours[i].add(j);neighbours[j].add(i)
    seen={0};stack=[0]
    while stack:
        for v in neighbours[stack.pop()]:
            if v not in seen:seen.add(v);stack.append(v)
    assert len(seen)==len(X)
    for v,fs in enumerate(inc):
        link=defaultdict(set)
        for fi in fs:
            f=cycles[fi];k=f.index(v)
            a,b=f[k-1],f[(k+1)%len(f)]
            link[a].add(b);link[b].add(a)
        assert all(len(s)==2 for s in link.values())
        reached={next(iter(link))};todo=list(reached)
        while todo:
            for u in link[todo.pop()]:
                if u not in reached:reached.add(u);todo.append(u)
        assert reached==set(link)
    T=[(f[0],f[j],f[j+1]) for f in cycles for j in range(1,len(f)-1)]
    W,M=integrate(X,T);assert W>0
    A=4*W
    R=[tuple(A*p[k]-M[k] for k in range(3)) for p in X]
    S=[];U=[];H=[];deg=[];sides={};outgoing=[[] for _ in X]
    for fi,(pl,f) in enumerate(zip(planes,cycles)):
        N=pl[:3]
        assert A*pl[3]-dot(N,M)>0
        vals=[]
        for i,j in zip(f,f[1:]+f[:1]):
            z=dot(N,cross(R[i],R[j]));sides[fi,i,j]=z;vals.append(z)
        if min(vals)>0:S.append(fi)
        elif min(vals)==0:deg.append(['face',fi])
    zero=0
    for (i,j),fs in E.items():
        e=sub(X[j],X[i]);p=dot(R[i],e);q=-dot(R[j],e)
        outgoing[i].append(p);outgoing[j].append(q)
        vals=(-p,-q,sides[fs[0]],sides[fs[1]])
        zero+=sum(v==0 for v in vals)
        if min(vals)>0:H.append([i,j])
        elif min(vals)==0:deg.append(['edge',i,j])
    for i,vals in enumerate(outgoing):
        if max(vals)<0:U.append(i)
        elif max(vals)==0:deg.append(['vertex',i])
    cls=[len(S),len(U),len(H)]
    if cls==[1,1,0] and not deg:
        f=S[0];N=planes[f][:3];hh=A*planes[f][3]-dot(N,M);nn=dot(N,N)
        for j,pl in enumerate(planes):
            h=A*pl[3]-dot(pl[:3],M)
            if j!=f:assert h*h*nn>hh*hh*dot(pl[:3],pl[:3])
        r2=dot(R[U[0]],R[U[0]])
        assert all(dot(r,r)<r2 for i,r in enumerate(R) if i!=U[0])
    return dict(I=X,D=D,triangles=T,faces=cycles,edges=sorted(E),
                V=len(X),E=len(E),F=len(cycles),edge_budget_2E=2*len(E),
                W=str(W),M=list(map(str,M)),
                volume=str(Q(W,6*D**3)),
                centroid=[str(Q(m,4*W*D)) for m in M],
                equilibrium_class=cls,stable=[cycles[f] for f in S],
                unstable=U,saddles=H,degenerate=deg,
                zero_true_edge_predicates=zero)

def candidates(P,source):
    lookup={p:i for i,p in enumerate(P)}
    mate=[lookup[(x,-y,-z)] for x,y,z in P]
    critical=set(source['stable'][0])|set(source['unstable'])
    adj=[set() for _ in P]
    for i,j in source['edges']:adj[i].add(j);adj[j].add(i)
    xmin=min(p[0] for p in P);xmax=max(p[0] for p in P)
    answer=[]
    for i in range(len(P)):
        if i>=mate[i] or i in critical:continue
        best=None
        for J in combinations(sorted(adj[i]-critical),3):
            moved=set(J)|{mate[j] for j in J}
            if len(moved)!=6 or i in moved or mate[i] in moved:continue
            a,b,c=[P[j] for j in J]
            u,v,w=sub(b,a),sub(c,a),sub(P[i],a)
            aa,bb,cc=dot(u,u),dot(u,v),dot(v,v)
            den=aa*cc-bb*bb
            if den==0:continue
            beta=Q(dot(w,u)*cc-dot(w,v)*bb,den)
            gamma=Q(dot(w,v)*aa-dot(w,u)*bb,den)
            weights=(1-beta-gamma,beta,gamma)
            if min(weights)<=0:continue
            foot=tuple(sum(weights[k]*P[J[k]][r] for k in range(3))
                       for r in range(3))
            d=sub(P[i],foot)
            if not all(xmin<P[j][0]+d[0]<xmax for j in J):continue
            try:seed4(P,[j for j in range(len(P)) if j not in moved])
            except AssertionError:continue
            key=(dot(d,d),J)
            if best is None or key<best[0]:best=(key,i,J,weights,d,mate[i])
        if best is not None:answer.append(best)
    return sorted(answer,key=lambda q:(q[0],q[1])),mate

def main(journal,limit):
    P,D=decode(journal)
    source=census(P,D)
    assert (source['V'],source['E'],source['F'])==(323,962,641)
    assert source['equilibrium_class']==[1,1,0] and not source['degenerate']
    pool,mate=candidates(P,source)
    out=Path('rank2_frontier_output');out.mkdir(exist_ok=True)
    records=[]
    for number,(_,i,J,weights,d,mi) in enumerate(pool[:limit]):
        L=lcm(*(x.denominator for x in d))
        delta=tuple(int(L*x) for x in d)
        points=[tuple(L*x for x in p) for p in P]
        for j in J:
            points[j]=tuple(points[j][k]+delta[k] for k in range(3))
            x,y,z=points[j];points[mate[j]]=(x,-y,-z)
        for k in range(3):
            assert sum(weights[r]*points[J[r]][k] for r in range(3))==points[i][k]
        report=census(points,D*L)
        assert report['V']<=321 and report['edge_budget_2E']<=1912
        operation=dict(source_stream_sha256=
            '6ecdf84ca0c79201e5c66d14562a510252b0e5dc8962f31a18c0449ba7116adb',
            target=i,mate=mi,neighbours=J,weights=list(map(str,weights)),
            translation_in_source_integer_units=list(map(str,d)),
            endpoint_parameter='1')
        stem=out/('candidate_%03d'%number)
        stem.with_suffix('.json').write_text(json.dumps(
            dict(operation=operation,certificate=report),indent=2))
        summary={k:report[k] for k in
            ('V','E','F','edge_budget_2E','equilibrium_class','degenerate')}
        summary['target_source_index']=i
        records.append(summary)
        print(json.dumps(summary),flush=True)
        if report['equilibrium_class']==[1,1,0] and not report['degenerate']:
            print('CANDIDATE_PASSES_THIS_EXACT_IMPLEMENTATION; SECOND_AUDIT_REQUIRED')
            break
    (out/'summary.json').write_text(json.dumps(records,indent=2))

if __name__=='__main__':
    if len(sys.argv) not in (2,3):
        raise SystemExit('usage: rank2_frontier.py JOURNAL.md [MAX_ENDPOINTS]')
    main(sys.argv[1],int(sys.argv[2]) if len(sys.argv)==3 else 12)
```

## 7. Evidence limitations and continuation

The source-validation constants, the previously accepted STRICT323 class and the distinction from FUS-SUB4001 come from the supplied literal journal. The neighbour-translation vertex-loss result, its critical-feature protection, the degree bounds and the support-flip mass identities are proved above. The five-vertex fixture is specified completely and its mass formulas are explicit.

The candidate-search program is **not evidence that a smaller winner was returned**. No numerical point count, isolated flat determinant or unpreserved earlier report is promoted. No continuous equilibrium-preserving transition has been established for a particular STRICT323 cavity here. There is also no claimed global obstruction to C<1000.

The most useful next finite experiment is the deterministic neighbour-triple scan above on the literal STRICT323 coordinates. Its endpoint has guaranteed genuine vertex loss, guaranteed positive volume and retained strict stable/apex equilibria at the actual centroid. For a promising endpoint, trace the one-parameter family through its exact quadratic support events using the correct branch-specific mass formula. Rebuild the maximal hull at the rank-loss event before evaluating the degree-at-most-six full-cone predicates. This separates three questions that must not be conflated: disappearance of the selected vertices, validity of the new convex boundary, and absence of additional equilibria.
