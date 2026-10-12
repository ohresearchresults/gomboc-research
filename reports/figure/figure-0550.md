# figure-0550

AI research report · 2026-09-25 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Finite projective mass repair: an exact rational centering parametrization

## Status and evidence boundary

**No newly audited own110 body is reported.** The accepted computational entrance remains the literal `REFERENCE_BRIDGE79_G8` from `figure-0549`, SHA256 `f996fa67a06c542cbe559aadce39ce5f7b2f06b81a609a4a55dd3f03d9291605`.

The constructive advance below is algebraic: **when the nominated interior point is allowed to vary, the projective centering equation can be eliminated exactly, over the rationals, rather than solved approximately inside every search evaluation.** This gives a complete parametrization of the same centered projective family, with an explicit affine coupling. It does not assert that centering preserves either equilibrium landscape.

There is also an explicit rational a posteriori bound for the error in a fixed-nominee centering solve. Its derivation does not depend on an optimizer's stopping flag.

### Reading and execution limitation

The available inspected reading record reaches lines1–1730 of the current1931-line journal. The remaining lines1731–1931 and the complete348-line numerical-methods attachment were requested, but their tool returns were not available for inspection in this continuation. Thus **the required complete-pack reading is unfinished**. Commands to extract the parent capsule were also issued without inspectable receipts. I do not claim a completed recovery, a numerical screen, an exact endpoint audit, or a newly observed output hash.

The journal and numerical-methods attachment were identified in the resumed runtime inventory as:

```text
research-journal(20260925-183717).md
412240 bytes
1c527c62448c599e45196425af443d663309e8f7ac20ec77dfe7fb6729deb231

JOINT75_numeric_orbit_complete_methods.md
21196 bytes
8a7d43cbd50089a5bff60236b73992c54f87d60501e834fd083d87bfbec2a925
```

The parent geometry and scientific baseline used here come from its previously inspected literal prose. In particular, the bridge's own15/32/45, P31/Q14 and reference-U1 statements are **parent results, not fresh verification**. The patch below does not use or silently modify the unread numerical toolkit.

## 1. Eliminate centering by pulling back the actual centroid

Let L be a rational, full-dimensional convex polyhedron containing0 in its interior. In this application, take the literal bridge and translate it by the old primary centroid. Let

```text
D = {c : 1+c·x > 0 for every x in L},
T_c(x) = x/(1+c·x),
Y_c = T_c(L).
```

Choose **any rational c in D**. Integrate the actual uniformly filled body Y_c, obtaining its exact rational volume V(c) and centroid g(c). Define

```text
d = 1-c·g,
q = g/d,
b = d c,
B = I-g c^T,
C = d B.
```

Then the following identities hold exactly:

```text
d > 0,
q is in the interior of L,
det(B) = d,
det(C) = d^4 > 0,

T_c(x)-g = C T_b(x-q),

centroid(T_b(L-q)) = 0,
Volume(T_b(L-q)) = V(c)/d^4.
```

All these quantities are rational when L and c are rational. Thus **a rational projective parameter produces an exactly centered rational member of the nominated-point family**, without requiring the solution of an algebraic centering equation at a preassigned q.

This is not a reference-centre substitution. The centroid g is obtained by actual filled-volume integration; the new nominee q is its projective preimage. Translating Y_c by its actual centroid changes coordinates, not material density. The identity then identifies the exactly centered canonical member `T_b(L-q)`.

### Proof

The inverse map on Y_c is

```text
T_c^{-1}(y) = y/(1-c·y).
```

The inverse-chart denominator is positive throughout Y_c. Since it is affine in y and g is an interior point of Y_c, `d=1-c·g>0`. Therefore `q=T_c^{-1}(g)` lies in the interior of L.

For x in L,

```text
1+b·(x-q) = d(1+c·x).
```

Moreover `Bq=g`, so

```text
T_c(x)-g
 = [Bx-g]/(1+c·x)
 = B(x-q)/(1+c·x)
 = dB T_b(x-q).
```

The matrix determinant lemma gives `det(B)=1-c·g=d`, hence `det(C)=d^4`. Centroids and filled volumes transform covariantly under this nonsingular affine map. Since `Y_c-g` has actual centroid0, the canonical body has actual centroid0 as well.

### What this changes computationally

A nested search in `(q,b,A)` with three centering equations can instead search in:

```text
c: three positive-chart projective parameters,
A: the chosen affine shape parameters,
P(c,A) = A [T_c(L)-g(c)].
```

For rational c and rational nonsingular A, P is rational and **exactly own-centred** after rational integration. Its corresponding nominee, canonical centering parameter and affine coupling are recovered by the formulas above.

This does not add three new physical degrees of freedom. It removes a nonlinear constraint and an inner numerical solve from a family that already permits the nominee to move. The physical affine factor in the nominated-point representation is `A C`, so the associated polar transformation must use its inverse transpose.

For a prescribed q, the supplied uniqueness theorem still applies: there is one centering b. The rational parametrization instead lets q vary exactly, as the assignment permits.

## 2. The parametrization covers the full nominee family

Write Σ(c) for the covariance matrix of the actual uniformly filled Y_c. The supplied derivative identity is

```text
Dg(c) = -5Σ(c)-g(c)g(c)^T.
```

Differentiating `q=g/d`, with `d=1-c·g`, gives the cancellation

```text
Dq(c) = -(5/d) (I+q c^T) Σ(c).
```

Consequently

```text
det Dq(c) = -125 det(Σ(c))/d^4 < 0.
```

This is a nonsingular map everywhere in the positive chart. It is globally one-to-one and onto the interior of L: given an interior q, take its unique centered parameter b; then

```text
c = b/(1-b·q).
```

The denominator is positive because0 is an interior point of L and the canonical positive chart contains `-q`. Conversely, the pullback construction recovers that same q and b. Thus the proposed elimination does not omit a disconnected set of nominated centres.

There is also a useful weighted-integral identity:

```text
q(c) = [∫_L x(1+c·x)^(-5) dx] / [∫_L (1+c·x)^(-5) dx].
```

This is a formula for a coordinate parameter, not a proposal to replace uniform density by a weight. The final material body remains uniformly filled.

Along any ray `c=t u`,

```text
d/dt [u·q(tu)] = -5 u^T Σ(tu)u / d(tu)^2 < 0.
```

The strict monotonicity can organize one-dimensional nominee sweeps. It is not an equilibrium-monotonicity theorem.

## 3. Finite positive-chart directions with no edge cost

Let the actual supports of L be `u_i·x<=1`, where every u_i is rational. For any actual support row and any rational `0<=t<1`, choose

```text
c = -t u_i.
```

Then, on the whole body,

```text
1+c·x = 1-t u_i·x >= 1-t > 0.
```

These are finite directions, with an exact chart margin, not tiny local perturbations. Convex combinations of the u_i give additional directions with the same guarantee. Since `D=-int(L*)`, these constructions are naturally organized by the actual polar geometry.

Positive-chart projective maps and nonsingular affine maps preserve the entire face lattice. Therefore, for the literal bridge, every such exact projective/affine descendant retains **V79/E231/F154 and C462**, before any optional material modification. Independent vertex rounding is unnecessary and should be avoided: round the three projective parameters and the affine matrix, then reconstruct the rational image exactly.

No implication for own S/U/H follows from this incidence statement. In particular, the old reference-U1 construction is not protected by the centering identity.

## 4. How both equilibrium landscapes must be tested

For a fixed nominee q, put `v_i=x_i-q`, `d_i=1+b·v_i`, and let `G=A^T A` be the primal affine metric. The vertex escape from i toward j has the sign of

```text
E_ij(b,G)
 = d_i v_i^T G v_j - d_j v_i^T G v_i
 = v_i^T G(v_j-v_i)
   + b·[(v_i^T G v_j)v_i-(v_i^T G v_i)v_j].
```

For fixed q and G this is affine in b. If r_i are the polar vertices of `L-q`, the canonically centered projective polar is exactly `r_i+b`, and the corresponding polar escape has the sign of

```text
(r_i+b)^T G^(-1)(r_j-r_i).
```

This too is affine in b. These formulas give exact candidate witness chambers and explain why the affine metric must be inverse-coupled between P and Q.

However, along an ordinary centering iteration most intermediate b do not make the centroid zero. Their zero-reference escape chambers are not their own-centroid mechanical chambers. One must either finish and certify the prescribed-q solve, or use the pullback gauge and audit the actual centred body `A[T_c(L)-g(c)]` at every retained point.

An isolated zero escape does not establish an extra weak equilibrium. The complete closed conditions, including the edge projection interval and both normal-cone coefficients, remain necessary. Likewise, every strictly positive P or Q bar remains a defect, regardless of its size.

## 5. A rational certificate for a fixed-nominee solve

For completeness, the fixed-nominee Newton mechanism admits an explicit, if potentially conservative, error certificate.

Suppose rational bounds satisfy

```text
r B_unit subset L subset R B_unit,
J = ∫_L xx^T dx,
Bmax = 1+R/r.
```

For every c in the positive chart, `|c|<1/r`, so `1+c·x<=Bmax`. Hence

```text
Hessian V(c) >= 20 J/Bmax^6.
```

Since J is positive definite and

```text
lambda_min(J) >= 4 det(J)/(trace(J))^2,
```

a rational global strong-convexity constant is

```text
mu = 80 det(J)/[(trace J)^2 Bmax^6] > 0.
```

Let c* be the unique exact fixed-nominee centering parameter. Strong monotonicity of the gradient and `grad V=-4Vg` give

```text
|c-c*|_2 <= 4 V(c) |g(c)|_2 / mu
          <= 4 V(c) Σ_j |g_j(c)| / mu.
```

Everything on the last right-hand side is rational for a rational trial c. This separates an exact mathematical enclosure from a numerical centering residual. It also supplies a reproducible stopping certificate without pretending that a rounded Newton parameter has exactly zero centroid.

For a polyhedral L, usable rational bounds are

```text
r = min_i h_i / Σ_j |n_ij|,
R = max_vertex Σ_j |x_j|,
```

using actual positive supports `n_i·x<=h_i`. They need not be sharp.

## 6. Complete additive producing and checking patch

The source below implements the exact pullback gauge, optional rational-grid damped Newton, a finite facet-directed transformation, exact mass and covariance, the residual enclosure, actual incidence checks, and a complete independent strict/closed-weak/P/Q audit.

It is **an unexecuted additive patch**, not a newly accepted successor capsule. Its exact input dependency is the already-supplied literal parent. It locates the primary75-row input by its complete byte hash, then adds the six literal bridge points. It can read either that recovered exact input or the supplied journal containing the parent decoder. It does not require an originating sandbox or an external archive.

The primary input dependency is:

```text
2110 bytes
SHA256 e87efbdd3a99a500a5165fd05160987ad15b7c4a9c658bfbb62e32606b51bb52
```

The journal route additionally checks the decoder and decoded dictionary identities stated in the literal parent:

```text
RECOVER_JOINT62.py:
87533 bytes
5766a233e26c790064869e625c93f679cb6a3fe6d5ae1d48ce41f0f439aa3e50

Decoded dictionary:
203263 bytes,35 units
729ec23615fe3b87fc09dd359ef85b67e862abc66a431c83f9f76b79c1c86dd5
```

The patch's independent auditor is included to make its output inspectable and complete. **A target emitted by this previously unexecuted patch must still be cross-checked with the literal parent's established exact auditor before acceptance.** No guessed parent-auditor function name or uninspected command interface is supplied as though verified.

Use CPython3.13.5 and the standard library. There is no NumPy/SciPy/Torch dependency or random seed in this patch. Save it as `PROJECTIVE_RATIONAL_GAUGE.py` and run, for example:

```sh
python -B -S PROJECTIVE_RATIONAL_GAUGE.py --journal research-journal.md --facet 0 --t 1/2 --out FACET0_HALF
python -B -S PROJECTIVE_RATIONAL_GAUGE.py --journal research-journal.md --newton 12 --grid 10000000000 --out FIXED_NOMINEE_NEWTON12
python -B -S PROJECTIVE_RATIONAL_GAUGE.py --journal research-journal.md --facet 0 --t 3/4 --matrix 2 0 0 0 1 0 0 0 1/2 --out FACET0_THREEQUARTERS_AFFINE
```

These are explicit finite controls, not an asserted completed screen or a preferred facet chosen by evidence. Every new input, audit, parameter file and source receives its actual byte count and SHA256 when the program runs. No unobserved output hash is asserted here.

### Complete source

```python
# Exact rational centering gauge for the literal R62J reference bridge.
# Standard library only. Execution is unverified in the accompanying handoff.
import argparse, ast, base64, hashlib, itertools, json, lzma, re, sys
from collections import deque
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
PARENT = 'figure-0549'
PARENT_SHA = 'f996fa67a06c542cbe559aadce39ce5f7b2f06b81a609a4a55dd3f03d9291605'
INPUT_SHA = 'e87efbdd3a99a500a5165fd05160987ad15b7c4a9c658bfbb62e32606b51bb52'
JOURNAL_SHA = '1c527c62448c599e45196425af443d663309e8f7ac20ec77dfe7fb6729deb231'
DECODER_SHA = '5766a233e26c790064869e625c93f679cb6a3fe6d5ae1d48ce41f0f439aa3e50'
RAW_SHA = '729ec23615fe3b87fc09dd359ef85b67e862abc66a431c83f9f76b79c1c86dd5'
SIX = [[54523165,-66300276,-55391279],[49842012,-91287749,-32456638],
       [35949856,-110325885,-5024889],[13236236,-120608734,24070669],
       [-16841661,-119820327,51618679],[-51605841,-106402263,74185541]]
GREF = tuple(F(x,301728380651199510841280000000) for x in
    [-53286920506055854442174018051,-42633799180986064597953397917,
     -43819041531080084398689329023])
Z = (F(0),F(0),F(0))
IDENTITY = [[F(int(i==j)) for j in range(3)] for i in range(3)]

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,t): return tuple(t*x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def mv(A,x): return tuple(dot(r,x) for r in A)
def md(A): return det(*A)
def sha(b): return hashlib.sha256(b).hexdigest()

def write(out,name,obj):
    b=(json.dumps(obj,default=str,sort_keys=True,separators=(',',':'))+'\n').encode()
    (out/name).write_bytes(b)
    return dict(file=name,bytes=len(b),sha256=sha(b))

def primary_bytes(args):
    if args.primary:
        b=Path(args.primary).read_bytes()
    else:
        jb=Path(args.journal).read_bytes()
        assert len(jb)==412240 and sha(jb)==JOURNAL_SHA
        candidates=[]
        for text in re.findall(r'```python\n(.*?)\n```',jb.decode(),re.S):
            code=(text+'\n').encode()
            if len(code)==87533 and sha(code)==DECODER_SHA:
                candidates.append(code.decode())
        assert len(candidates)==1, 'EXACT_PARENT_DECODER_NOT_FOUND'
        vals=[]
        for node in ast.parse(candidates[0]).body:
            if isinstance(node,ast.Assign) and any(
                isinstance(t,ast.Name) and t.id=='DATA' for t in node.targets):
                vals.append(ast.literal_eval(node.value))
        assert len(vals)==1
        raw=lzma.decompress(base64.b64decode(vals[0]))
        assert len(raw)==203263 and sha(raw)==RAW_SHA
        files=json.loads(raw)
        assert len(files)==35 and all(isinstance(v,str) for v in files.values())
        found=[v.encode() for v in files.values() if sha(v.encode())==INPUT_SHA]
        assert len(found)==1, 'EXACT_PRIMARY_INPUT_NOT_FOUND'
        b=found[0]
    assert len(b)==2110 and sha(b)==INPUT_SHA
    return b

def primary_rows(b):
    obj=json.loads(b); found=[]
    def walk(x):
        if isinstance(x,list):
            if len(x)==75 and all(isinstance(r,list) and len(r)==3 for r in x):
                try:
                    y=[[F(v) for v in r] for r in x]
                    if all(v.denominator==1 for r in y for v in r):
                        found.append([[int(v) for v in r] for r in y])
                except (ValueError,TypeError,ZeroDivisionError):
                    pass
            for v in x: walk(v)
        elif isinstance(x,dict):
            for v in x.values(): walk(v)
    walk(obj)
    assert len(found)==1, 'UNIQUE_LITERAL_75_BY_3_INTEGER_ARRAY_REQUIRED'
    return found[0]

def hull_integer(I):
    planes={}
    for ia,ib,ic in itertools.combinations(range(len(I)),3):
        a,b,c=I[ia],I[ib],I[ic]
        n=cross(sub(b,a),sub(c,a))
        if n==Z: continue
        h=dot(n,a); pos=neg=False
        for p in I:
            s=dot(n,p)-h
            pos=pos or s>0; neg=neg or s<0
            if pos and neg: break
        if pos and neg or not(pos or neg): continue
        if pos: n=mul(n,-1); h=-h
        row=tuple(int(x) for x in (*n,h))
        k=gcd(*(abs(x) for x in row)); row=tuple(x//k for x in row)
        ids=[j for j,p in enumerate(I) if dot(row[:3],p)==row[3]]
        assert len(ids)==3, 'NONTRIANGULAR_SUPPORT: DO_NOT_TREAT_FAN_DIAGONALS_AS_EDGES'
        planes[row]=ids
    faces=[]; rows=sorted(planes)
    for row in rows:
        f=planes[row][:]
        if dot(cross(sub(I[f[1]],I[f[0]]),sub(I[f[2]],I[f[0]])),row[:3])<0:
            f[1],f[2]=f[2],f[1]
        faces.append(f)
    owners={}
    for j,f in enumerate(faces):
        for a,b in zip(f,f[1:]+f[:1]):
            owners.setdefault(tuple(sorted((a,b))),[]).append(j)
    assert all(len(v)==2 for v in owners.values())
    vertices=sorted({i for f in faces for i in f}); edges=sorted(owners)
    assert len(vertices)-len(edges)+len(faces)==2
    assert (len(vertices),len(edges),len(faces))==(79,231,154)
    return vertices,faces,edges,owners,rows

def moments(P,faces,second=False):
    W=F(0); T=Z; J=[[F(0)]*3 for _ in range(3)]
    for f in faces:
        a,b,c=[P[i] for i in f]
        w=det(a,b,c); s=add(add(a,b),c)
        W+=w; T=add(T,mul(s,w))
        if second:
            for i in range(3):
                for j in range(3):
                    J[i][j]+=w*(s[i]*s[j]+a[i]*a[j]+b[i]*b[j]+c[i]*c[j])/120
    assert W>0
    return W/6,mul(T,F(1,24)),mul(T,1/(4*W)),J

def image(L,c):
    den=[1+dot(c,x) for x in L]
    assert min(den)>0, 'NONPOSITIVE_PROJECTIVE_CHART'
    return [mul(x,1/d) for x,d in zip(L,den)],min(den)

def solve3(A,y):
    d=md(A); assert d>0
    ans=[]
    for j in range(3):
        B=[r[:] for r in A]
        for i in range(3): B[i][j]=y[i]
        ans.append(md(B)/d)
    return tuple(ans)

def newton(L,faces,c,steps,grid):
    history=[]
    for k in range(steps):
        Y,margin=image(L,c); V,M,g,J=moments(Y,faces,True)
        H=[[5*J[i][j]/V-4*g[i]*g[j] for j in range(3)] for i in range(3)]
        rec=dict(iteration=k,c=c,volume=V,centroid=g,denominator_min=margin)
        history.append(rec)
        if g==Z: rec['stop']='EXACT_ZERO'; break
        direction=solve3(H,g); accepted=False
        for j in range(80):
            z=tuple(F(round((c[i]+direction[i]/(2**j))*grid),grid) for i in range(3))
            delta=sub(z,c)
            if dot(g,delta)<=0: continue
            if min(1+dot(z,x) for x in L)<=0: continue
            YY,mm=image(L,z); VV,_,_,_=moments(YY,faces)
            if VV<=V-V*dot(g,delta)/1000:
                rec['step']=delta; rec['backtracks']=j
                c=z; accepted=True; break
        if not accepted:
            rec['stop']='NO_ROUNDED_ARMIJO_DESCENT'; break
    return c,history

def chord(a,b):
    A,B,C=dot(a,a),dot(a,b),dot(b,b)
    if B>=A: return A
    if B>=C: return C
    return (A*C-B*B)/(A+C-2*B)

def bars(P,edges):
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
                comp=members[r]
                cut=[e for e in edges if (e[0] in comp)!=(e[1] in comp)]
                assert cut and max(weights[e] for e in cut)==level
                result.append(dict(peak=r,elder=keep,birth=birth[r],death=level,
                    depth=birth[r]-level,relative_depth=(birth[r]-level)/birth[r],
                    component=sorted(comp),cut=cut,
                    attaining_edge=min(e for e in cut if weights[e]==level),
                    path=path(r,keep,level)))
            for r in group:
                if r!=keep: parent[r]=keep; del members[r]
            members[keep]=merged
    assert len({root(i) for i in nodes})==1
    return result

def audit(P,vertices,faces,edges,owners):
    V,M,g,_=moments(P,faces)
    assert g==Z and M==Z, 'BODY_NOT_EXACTLY_OWN_CENTRED'
    normals=[]; heights=[]
    for f in faces:
        a,b,c=[P[i] for i in f]; n=cross(sub(b,a),sub(c,a)); h=dot(n,a)
        assert h>0
        sl=[h-dot(n,p) for p in P]
        assert min(sl)>=0 and {i for i,s in enumerate(sl) if s==0}==set(f)
        normals.append(n); heights.append(h)
    strict=[[],[],[]]; weak=[[],[],[]]; zero=[[],[],[]]
    for j,f in enumerate(faces):
        vals=[-dot(cross(normals[j],sub(P[b],P[a])),P[a])
              for a,b in zip(f,f[1:]+f[:1])]
        if min(vals)>0: strict[0].append(j)
        if min(vals)>=0: weak[0].append(j)
        if 0 in vals: zero[0].append(j)
    for i in vertices:
        neigh=[b if a==i else a for a,b in edges if i in (a,b)]
        vals=[dot(P[i],sub(P[j],P[i])) for j in neigh]
        if max(vals)<0: strict[1].append(i)
        if max(vals)<=0: weak[1].append(i)
        if 0 in vals: zero[1].append(i)
    for e in edges:
        a,b=e; d=sub(P[b],P[a]); dd=dot(d,d); tn=-dot(P[a],d)
        r=add(mul(P[a],dd),mul(d,tn)); f1,f2=owners[e]
        n1,n2=normals[f1],normals[f2]
        aa,ab,bb=dot(n1,n1),dot(n1,n2),dot(n2,n2)
        assert aa*bb-ab*ab>0
        vals=[tn,dd-tn,bb*dot(r,n1)-ab*dot(r,n2),aa*dot(r,n2)-ab*dot(r,n1)]
        if min(vals)>0: strict[2].append(e)
        if min(vals)>=0: weak[2].append(e)
        if 0 in vals: zero[2].append(e)
    PB=bars({i:P[i] for i in vertices},edges)
    Q={j:mul(n,1/h) for j,(n,h) in enumerate(zip(normals,heights))}
    QE=sorted({tuple(sorted(v)) for v in owners.values()})
    QB=bars(Q,QE)
    counts=list(map(len,strict)); wc=list(map(len,weak)); zc=list(map(len,zero))
    extra=[wc[i]-counts[i] for i in range(3)]
    if zc==[0,0,0]:
        assert counts[0]+counts[1]-counts[2]==2
        assert len(PB)==counts[1]-1 and len(QB)==counts[0]-1
    return dict(points=P,vertices=vertices,faces=faces,edges=edges,
        edge_faces=[[a,b,*owners[(a,b)]] for a,b in edges],
        normals=normals,support_heights=heights,V=len(vertices),E=len(edges),
        F=len(faces),C=2*len(edges),volume=V,first_moment=M,centroid=g,
        S=strict[0],U=strict[1],H=strict[2],strict=counts,weak=wc,
        additional_weak=extra,primitive_zero=zc,closed_weak_ids=weak,
        primitive_zero_ids=zero,P_bars=PB,Q_bars=QB,
        stable_material_faces=[faces[j] for j in strict[0]],
        root_stars={str(i):[j for j,f in enumerate(faces) if i in f] for i in strict[1]})

def lattice(P):
    D=lcm(*(v.denominator for p in P for v in p))
    return dict(denominator=D,points=[[int(v*D) for v in p] for p in P])

def main():
    ap=argparse.ArgumentParser()
    src=ap.add_mutually_exclusive_group(required=True)
    src.add_argument('--journal'); src.add_argument('--primary')
    ap.add_argument('--facet',type=int)
    ap.add_argument('--t',default='1/2')
    ap.add_argument('--c',nargs=3)
    ap.add_argument('--matrix',nargs=9)
    ap.add_argument('--newton',type=int,default=0)
    ap.add_argument('--grid',type=int,default=10000000000)
    ap.add_argument('--out',default='PROJECTIVE_GAUGE')
    args=ap.parse_args()
    assert args.newton>=0 and args.grid>0
    assert not(args.facet is not None and args.c is not None)
    out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    raw=primary_bytes(args); I=[[10*x for x in r] for r in primary_rows(raw)]+SIX
    vertices,faces,edges,owners,rows=hull_integer(I)
    X=[tuple(F(x,100000000) for x in r) for r in I]
    L=[sub(p,GREF) for p in X]
    supports=[(tuple(map(F,r[:3])),F(r[3],100000000)-dot(r[:3],GREF)) for r in rows]
    assert min(h for n,h in supports)>0
    chain=[62,75,76,77,78,79,80,6]
    assert all(dot(L[a],sub(L[b],L[a]))>0 for a,b in zip(chain,chain[1:]))
    reference_u=[]
    for i in vertices:
        js=[b if a==i else a for a,b in edges if i in (a,b)]
        val=max(dot(L[i],sub(L[j],L[i])) for j in js)
        assert val!=0
        if val<0: reference_u.append(i)
    assert reference_u==[6]
    c=tuple(map(F,args.c)) if args.c else Z
    if args.facet is not None:
        assert 0<=args.facet<len(faces)
        t=F(args.t); assert 0<=t<1
        n,h=supports[args.facet]; c=mul(n,-t/h)
    c,history=newton(L,faces,c,args.newton,args.grid)
    Y,margin=image(L,c); V,M,g,J=moments(Y,faces,True)
    d=1-dot(c,g); assert d>0
    q=mul(g,1/d); b=mul(c,d)
    C=[[d*(F(int(i==j))-g[i]*c[j]) for j in range(3)] for i in range(3)]
    assert md(C)==d**4
    Zbody=[mul(sub(x,q),1/(1+dot(b,sub(x,q)))) for x in L]
    centered=[sub(y,g) for y in Y]
    assert all(mv(C,z)==p for z,p in zip(Zbody,centered))
    ZV,ZM,ZG,_=moments(Zbody,faces)
    assert ZV==V/d**4 and ZM==ZG==Z
    A=([list(map(F,args.matrix[i:i+3])) for i in (0,3,6)] if args.matrix else IDENTITY)
    assert md(A)>0
    P=[mv(A,p) for p in centered]
    result=audit(P,vertices,faces,edges,owners)
    assert result['volume']==md(A)*V
    LV,LM,LG,LJ=moments(L,faces,True)
    radius=min(h/sum(abs(v) for v in n) for n,h in supports)
    outer=max(sum(abs(v) for v in p) for p in L)
    tr=sum(LJ[i][i] for i in range(3)); assert md(LJ)>0 and tr>0
    mu=80*md(LJ)/(tr*tr*(1+outer/radius)**6)
    bound=4*V*sum(abs(v) for v in g)/mu
    params=dict(parent=PARENT,parent_sha256=PARENT_SHA,primary_input_sha256=INPUT_SHA,
        original_reference_centroid=GREF,projective_parameter=c,
        denominator_min=margin,image_volume=V,image_centroid=g,d=d,
        pulled_back_nominee_relative=q,pulled_back_nominee_original=add(GREF,q),
        canonical_centering_parameter=b,canonical_to_centered_affine=C,
        physical_affine=A,canonical_volume=ZV,canonical_centroid=ZG,
        fixed_nominee_center_error_bound=bound,strong_convexity_constant=mu,
        inradius_lower=radius,raw_radius_upper=outer,newton_history=history,
        options=vars(args),material_labels=['P%02d'%i for i in range(75)]+
        ['bridge%02d'%i for i in range(6)])
    ir=write(out,'BODY_LATTICE.json',lattice(P))
    pr=write(out,'PARAMETERS.json',params)
    result['input_sha256']=ir['sha256']
    ar=write(out,'FULL_AUDIT.json',result)
    source=Path(__file__).read_bytes()
    receipt=write(out,'MANIFEST.json',dict(input=ir,parameters=pr,audit=ar,
        source_bytes=len(source),source_sha256=sha(source),python=sys.version))
    print('PROJECTIVE_RATIONAL_GAUGE_IDENTITY_PASS',len(vertices),len(edges),len(faces),flush=True)
    print('PROJECTIVE_OWN_CENTRE_AUDIT',result['strict'],result['additional_weak'],
          result['primitive_zero'],len(result['P_bars']),len(result['Q_bars']),receipt,flush=True)
    if (result['strict']==[1,1,0] and result['additional_weak']==[0,0,0]
        and not result['P_bars'] and not result['Q_bars'] and result['E']<=249):
        print('PROJECTIVE_TARGET_REQUIRES_LITERAL_PARENT_AUDITOR_CROSSCHECK',flush=True)

if __name__=='__main__':
    main()
```

## Handoff conclusion

The established result is the rational pullback-centroid identity, its full-family coverage, the covariance Jacobian, and the rational fixed-nominee residual enclosure. These remove a computational obstacle to a finite projective search without changing density, spending edges, or accepting a stale centre.

There is **no observed information here about whether the bridge's P31/Q14 landscape improves under these new parameters**. The baseline's reference-U1 success and its severe own-mass failure must remain separate. Neither the supplied centering theorem nor the new gauge identity resolves that mechanical question.

The most useful continuation is to finish the missing source reading, obtain inspectable execution, and use rational c as the outer projective coordinate with the nominee recovered exactly. Retained endpoints should carry the full generated audits and then pass the literal parent's established auditor. Until then, this is a proved parametrization and a complete pending-execution patch—not an accepted projective descendant, a finite-screen exclusion, or a cancellation claim.
