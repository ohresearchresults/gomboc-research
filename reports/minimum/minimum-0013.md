# minimum-0013

Historical AI scientific report · saved 2026-09-07 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# DEG6_ROOF_MAXIMUM_OBSTRUCTION_V1

## Determination and scope

**No additional whole combinatorial type or complete joint-root class is closed, and no C30 attainer is asserted.** The accepted bracket remains **30 ≤ C_min ≤ 1374**. The new result is an exact, unrestricted-domain obstruction for all three degree-six types: an apex-root realization must have a strict interleaving of the maximum squared radii on its two caps and their common ridge. An explicit positive quadratic identity proves the obstruction. In the surviving interleaving sectors it additionally forces a true escape edge, a strictly negative *nonedge* comparison, and a strict inequality involving the two **actual pyramid volumes**.

This is a proved exclusion of complete norm-order sectors in the joint realization/physical-metric space, not a sampled shape box, a whole-type exclusion, or a claim that the same shape is excluded for every metric regardless of its norm order. The parent's necessary-and-sufficient physical systems remain authoritative; their three degree-six members have fourteen real variables and no incidence equations. :contentReference[oaicite:0]{index=0}

## 1. Authority reconciliation and exact three-type input

The parent is `minimum-0012`, immutable SHA-256 `f09c802ac38060cd54f4546a2fba39ef7fa4d9bde606e7cd101c934a3ca5b80b`. I reconstructed its pinned `first_frontier.json`: **27,025 bytes**, SHA-256 `613ce3d88285e2c8faf2f41e08ee705ce279ec11430c6efbaf35b60273da925f`. The final literal facet arrays in the source below agree with that checkpoint.

**Label correction:** a provisional working catalogue had different vertex/facet labels and used `46388460` for the five-plus-five member. That identifier is not the corresponding identifier in the pinned parent checkpoint. I discarded those provisional labels and reran all reported checks using the actual parent arrays. The authoritative third identifier here is **51318223**. In particular, do not transfer a root or facet number from another catalogue merely because a graph index or type description agrees. This is a correction to my working aliases, not a claim that the immutable parent's mathematics changed.

Here `A` is the unique degree-six vertex; `F,G` are the only maximal facets not incident with `A`; `R` is their common ridge; and `I_F,I_G` are the private vertices of the two caps. Indices are zero-based and use **only the pinned parent's labels**.

| Parent map | A | F,G | R | I_F | I_G |
|---|---:|---|---|---|---|
| 5675263 | 7 | 0,7 | 1,6 | 0,2,3,4,5 | 8 |
| 14858559 | 6 | 0,3 | 0,2 | 1,3,4,5 | 7,8 |
| 51318223 | 8 | 0,1 | 0,2 | 1,3,4 | 5,6,7 |

The cap sizes are respectively **7+3, 6+4, 5+5**. The first member overlaps the heptagonal-facet investigation; the present argument uses a different, apex-root mass/maximum obstruction. Every private cap vertex is simple and adjacent to `A`. The two ridge vertices are simple and are precisely the two vertices not adjacent to `A`.

In every strict realization,

`P = conv(A,F) ∪ conv(A,G)`,

with disjoint interiors and intersection `conv(A,R)`, a triangle. Indeed, every generic ray from `A` through the solid exits through one of its two nonincident facets. These two pyramids therefore give the actual volume decomposition; no artificial weights or flat surrogate are introduced. A fan triangulation of each cap gives exactly six positive-volume tetrahedra in total.

## 2. An actual-moment positive certificate

Use coordinates centred at the **ordinary uniform-volume centroid**, and let `<x,y> = xᵀMy` for an arbitrary symmetric positive-definite physical metric `M`. Write `||x||²=<x,x>`.

The following identity is valid more generally for any vertex `a` of a convex three-polytope. For every facet not containing `a`, choose any vertex maximizing `||x||²` on that facet, including every possible tie choice, and fan-triangulate that facet from the chosen vertex. Denote the resulting triangles by `(b_t,u_t,v_t)`, with outward orientation, and put

```
d_t = det(b_t-a,u_t-a,v_t-a) > 0,
D   = Σ_t d_t,
B   = Σ_t d_t b_t,
Y_t = u_t+v_t,
Y   = Σ_t d_t Y_t,
E   = Σ_t d_t <b_t,a-b_t>.
```

The cone tetrahedra are a genuine decomposition of the solid. In the chosen affine coordinates, `D=6 Vol(P)`. Their ordinary first moments give exactly

`D a+B+Y=0`.

Define

```
Q0 = ||D a-B||²,
Q1 = D Σ_t d_t ||u_t-v_t||²,
Q2 = Σ_{t<s} d_t d_s ||Y_t-Y_s||²,
Q3 = 2D Σ_t d_t [2||b_t||²-||u_t||²-||v_t||²].
```

Then the exact certificate is

**`4D E+Q0+Q1+Q2+Q3=0`.**

All four `Q` terms are nonnegative. Moreover **`Q1>0`**: every tetrahedron has positive volume, its triangle has distinct vertices, and `M` is positive definite. Consequently

**`E<0`.**

For completeness, the algebra is not inferred from the controls. The weighted variance identity gives

`Q2 = D Σ_t d_t ||Y_t||²-||Y||²`.

It follows that

`Q1+Q2+Q3 = 4D Σ_t d_t ||b_t||²-||Y||²`,

and therefore

`4D E+Q0+Q1+Q2+Q3 = ||D a+B||²-||Y||² = 0`.

The last equality uses the actual first moment. The nonnegativity of `Q3` uses only that `b_t` is a maximum on its actual facet. This is a parameterized algebraic certificate over the entire physical domain. It does not require a lower bound on a determinant, an equilibrium margin, or an eigenvalue beyond strict positivity.

A useful general consequence is that, for every simultaneous choice of facet maxima, at least one chosen maximum has `<b,a-b><0`. Under a unique-unstable-root hypothesis at `a`, that maximum cannot be a **simple neighbor of a**: its two facet edges have negative scores, and its only remaining edge would have to escape to `a`. The specialized two-cap consequences below exploit this fact completely at the degree-six root.

## 3. Strict interleaving for the degree-six unstable root

Let `a` be the centred vector of `A`, and define

```
J   = max(||r||² : r is one of the two ridge vertices),
H_F = max(||v||² : v is private to F),
H_G = max(||v||² : v is private to G).
```

**Theorem.** If the only unstable vertex is `A`, then

**`(H_F-J)(H_G-J)<0`.**

Thus, after naming the caps `L` and `H`, every possible apex-root attainer must satisfy

**`max_private(L) < max_ridge < max_private(H)`.**

Here all maxima are of squared physical radii. Ties *within* any of these three groups remain allowed.

**Proof.** For distinct vertices `x,y` with `||y||²≤||x||²`,

`<x,y-x> = [||y||²-||x||²-||y-x||²]/2 < 0`.

If `J≥H_F` and `J≥H_G`, choose a ridge maximum `r`. All three genuine neighbors of `r` are roof vertices with radius at most that of `r`. Thus every incident score at `r` is strictly negative, making `r` a second unstable vertex.

If `H_F≥J` and `H_G≥J`, choose a private maximum on each cap. Each is a cap maximum, even when equality with the ridge occurs. Its two cap-edge scores are strictly negative. Since it is simple and its third neighbor is `A`, the unique-root conditions require a positive escape to `A`. Every tetrahedron in the two selected fans therefore contributes positively to `E`, contradicting `E<0`.

Every failure of strict interleaving belongs to one of these two cases, including all equality boundaries. This proves the theorem. In fact this exclusion survives the weaker assumption that every nonroot has an incident nonnegative escape: the second case would give `E≥0`, still a contradiction. The stronger forced-positive conclusions below use the strict target's actual root conditions.

**Proved UNSAT scope:** for each of the three full realization types, the conjunction of its physical domain, unstable root `A`, and `(H_F-J)(H_G-J)≥0` is impossible, for **every** SPD metric and **every** stable-root choice. This is a complete exclusion of those norm-order sectors, not a complete exclusion of the apex-root class.

## 4. What is forced in every remaining apex-root sector

Choose **any** ridge maximum `r` and **any** private maximum `p` on the high cap. The low cap is maximized by `r`; the high cap is maximized by `p`.

The genuine edge **`p→A` must have positive escape**. At `r`, both edges belonging to the low cap have negative scores. Its unique remaining neighbor `h` is private to the high cap, so the genuine edge **`r→h` must have positive escape**.

All forced ridge exits, in the pinned labels, are:

| Map | Low cap | High cap | Ridge maximum → forced high neighbor |
|---|---:|---:|---|
| 5675263 | 0 | 7 | 1→8 or 6→8 |
| 5675263 | 7 | 0 | 1→4 or 6→0 |
| 14858559 | 0 | 3 | 0→7 or 2→8 |
| 14858559 | 3 | 0 | 0→5 or 2→1 |
| 51318223 | 0 | 1 | 0→7 or 2→5 |
| 51318223 | 1 | 0 | 0→1 or 2→3 |

The word “or” enumerates the possible selected ridge maxima; if both ridge vertices tie for the maximum, **both corresponding conclusions hold**.

Let `D_L,D_H>0` be six times the actual volumes of `conv(A,L)` and `conv(A,H)` in the affine chart, and put

```
e_r = <r,a-r>,
e_p = <p,a-p> > 0.
```

The six-tetrahedron certificate gives the additional strict mass condition

**`D_L e_r+D_H e_p<0`.**

In particular,

**`e_r<0`.**

This is a **nonedge comparison**: the ridge vertex is not adjacent to `A`. It must not be installed as a true mechanical edge or substituted for any of the four actual edge components.

Writing `λ=D_L/(D_L+D_H)`, the actual volume fraction satisfies

**`λ > e_p/(e_p-e_r)`.**

There is also the exact quantitative gap

`λ e_r+(1-λ)e_p = -(Q0+Q1+Q2+Q3)/(4D²) < 0`.

Thus the surviving case needs not only the two forced true escapes, but also a ridge maximum outside the root's escape ball and enough **actual low-cap pyramid mass** to outweigh the high-cap positive escape. The volume fraction is computed from the moving solid; it is not an independently selectable parameter.

## 5. Denominators, metric, incidence, boundaries, and roots

The proof is coordinate-free and uses actual volume. It makes no assumption about the sign of the parent's common Cramer denominator `Delta`. To add the cuts directly to the parent's polynomial system, use its centred numerators `Z_i` and positive denominator `K`:

```
p_i = Z_i/K,
N_i = Z_iᵀ M Z_i,
e_i^Z = Z_iᵀ M(Z_A-Z_i),
d_t^Z = det(Z_b-Z_A,Z_u-Z_A,Z_v-Z_A).
```

Select maxima using the `N_i`; the common divisor `K²` is positive. Use outward cap fans, so every `d_t^Z>0`, and define `D_L^Z,D_H^Z` by their corresponding sums. The added polynomial comparison is

**`D_L^Z e_r^Z+D_H^Z e_p^Z<0`.**

Its sign is exactly the physical sign: coordinate denominators contribute positive powers of `K`, and the physical affine Jacobian is a common positive volume factor. The inherited identity `K=4 Delta⁴ W_raw>0` explicitly covers either sign of `Delta` and arbitrarily small nonzero Cramer denominators. :contentReference[oaicite:1]{index=1}

Positive definiteness is unrestricted. The strictness comes from `Q1>0` for every SPD `M`, not from a selected diagonal metric or a conditioning bound. Singular metrics are outside the physical domain; arbitrarily ill-conditioned positive-definite metrics are included.

The proof assumes the listed objects are genuine vertices and maximal facets of a strict convex realization. All parent support, nonincidence, polygon, and chart guards must remain. Fan diagonals are used only for integration, never as escape edges. Coplanarities that define the maximal facets are preserved exactly; a collapsed tetrahedron or changed maximal incidence is not silently counted as a member of the strict type.

No norm-order tie has been thrown away. Equality between a private maximum and the ridge maximum is excluded by the proof itself. Equal maxima within a ridge or private set are covered by all choices, and require no generic perturbation.

The argument uses a **necessary U-only consequence**. It neither chooses an independent dual metric nor imposes a homogeneous centroid on the polar. Every unexcluded system must still keep the parent's one `M` and exact inverse, every stable-root choice, all genuine edges, and the complete four-component nonsaddle disjunctions. Those conditions are not replaced by the new comparisons. :contentReference[oaicite:2]{index=2}

## 6. Exact remaining strata and what was not proved

For unstable root `A`, each type is now covered by **twelve labelled maximum-choice strata**: choose the low cap, choose one of the two ridge maxima, and choose a private maximum on the other cap. The count is `2(|I_F|+|I_G|)=12`. These strata may overlap on allowed within-group ties; no nonemptiness is asserted for any individual stratum.

For the stratum `(L,r,p)`, retain all parent constraints and impose:

```
N_r >= N_s                         for both ridge vertices s,
N_r >  N_i                         for every private low-cap vertex i,
N_p >= N_j                         for every private high-cap vertex j,
N_p >  N_r,
P_(p,A) > 0,
P_(r,h) > 0,
e_r^Z < 0,
D_L^Z e_r^Z+D_H^Z e_p^Z < 0.
```

All eight stable-root choices remain represented within this necessary reduction, subject to the inherited certified frontier. **The other eight unstable-root choices are not closed or removed by the interleaving theorem.** The general moment identity remains available for them, but I have not turned it into a complete new root-class exclusion there.

The inherited cone remainder is not replaced or recounted. In particular, the previously reported three closed joint-root orbits belong to that earlier result and are not new achievements here; their catalogue labels should not be transferred without a checked crosswalk. Its 178,131-record frontier and the fact that all 74 types remain are unchanged. :contentReference[oaicite:3]{index=3}

I reconstructed the complete parent, extracted and authenticated the degree-six incidence data, replaced the high-degree whole-system attack by the two-cap geometric decomposition, derived the positive identity, and checked it both symbolically and on three exact actual-mass controls. Exploratory metric searches supplied no promoted result. **There is no CAD/SMT UNSAT verdict, no numerical non-discovery theorem, and no exact SAT attainer in this handoff.** The proved UNSAT statements are precisely the analytic norm-order exclusions in Section 3 and violations of the necessary mixed-sector inequalities in Section 4.

The decisive remaining issue is the mixed sector: a ridge maximum escapes to a high-cap neighbor, a high-cap maximum escapes to the apex, yet the ridge-to-apex nonedge comparison is negative and the actual cap-volume ratio must compensate. A useful next whole-domain attack should combine these forced edges and the volume-ratio inequality with the complete physical system, rather than reopen the already excluded norm orders or replace actual mass by free cap weights.

## 7. Self-contained recovery capsule

Save the following source literally as `degree6_roof_max_v1.py`, UTF-8/LF with its final LF. It includes the complete authoritative facet arrays, all exact control inputs, rational hull/incidence and centroid checking, the reciprocal physical metric, all directed true-edge scores, and the full four-component strict saddle census. It needs no former sandbox file or journal to reconstruct its new output.

Executed environment: **CPython 3.13.5**; standard library for the entire geometric/physical audit. The optional formal polynomial check uses **SymPy 1.14.0**. Assertions must be enabled. No floating-point calculation or optimization is used by this capsule.

Commands:

```
python3 -S degree6_roof_max_v1.py
python3 degree6_roof_max_v1.py --formal
```

Both commands produce identical report bytes. The second additionally verifies the six-tetrahedron scalar polynomial identity with independent indeterminates; the displayed bilinear derivation proves its unrestricted SPD-vector version.

Exact source identity: **11,616 bytes**, SHA-256

`4f8ecf2c2f794cc4d9ace4794f1392b1c1e860f8fa78c935eab21608b70c45fe`.

Exact output `degree6_roof_max_v1_report.json`: **25,829 bytes**, SHA-256

`92d26a38f7380c9327ed4a2b34b906152df249fa32dba2cab4e57571ba375d34`.

The controls are actual homogeneous solids with the exact specified physical metric. In all three, `A` is the unique greatest-radius vertex and both private-cap maxima exceed the ridge maximum, but there are additional local unstable vertices. Their exact `(S,U,H)` values are **(7,7,12), (7,7,12), (8,7,13)**. They demonstrate a nonempty excluded geometric/metric sector; they are explicitly **not attainers**. Their ordinary centroids are integrated and subtracted exactly, and both the full boundary integration and the six-tetrahedron pyramid decomposition are checked against the same actual volume.

```python
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib, json, sys

assert __debug__
PARENT = dict(assignment='minimum-0012',
    immutable_sha256='f09c802ac38060cd54f4546a2fba39ef7fa4d9bde606e7cd101c934a3ca5b80b',
    checkpoint_name='first_frontier.json', checkpoint_bytes=27025,
    checkpoint_sha256='613ce3d88285e2c8faf2f41e08ee705ce279ec11430c6efbaf35b60273da925f')
MAPS = {
5675263: ((0,6,1,4,3,2,5),(0,7,8,6),(1,8,7,4),(2,7,5),
          (2,3,7),(3,4,7),(0,5,7),(1,6,8)),
14858559: ((0,5,3,4,1,2),(0,7,6,5),(1,6,8,2),(0,2,8,7),
           (3,6,4),(1,4,6),(3,5,6),(6,7,8)),
51318223: ((0,2,3,4,1),(0,7,6,5,2),(0,1,8,7),(2,5,8,3),
           (3,8,4),(5,6,8),(6,7,8),(1,4,8))}
M = ((F(1),F(1,10),F(1,20)),
     (F(1,10),F(1),F(-1,30)),
     (F(1,20),F(-1,30),F(100)))
EPS = F(1,1000)
THRESHOLDS = {5675263:F(11,6),14858559:F(1),51318223:F(0)}
HEX = ((2,0),(1,2),(-1,2),(-2,0),(-1,-2),(1,-2))

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(t,a): return tuple(t*x for x in a)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def bil(a,b): return dot(a,tuple(dot(row,b) for row in M))
def norm(a): return bil(a,a)
def total(vs):
    vs=list(vs);return tuple(sum(v[k] for v in vs) for k in range(3))
def edges(fs):
    return sorted({tuple(sorted((a,b))) for f in fs for a,b in zip(f,f[1:]+f[:1])})
def adjacency(fs,n):
    out=[set() for _ in range(n)]
    for a,b in edges(fs): out[a].add(b);out[b].add(a)
    return out

def hull_faces(V):
    found={}
    for a,b,c in combinations(range(len(V)),3):
        n=cross(sub(V[b],V[a]),sub(V[c],V[a]))
        if not any(n): continue
        h=dot(n,V[a]); scores=[h-dot(n,v) for v in V]
        if min(scores)<0 and max(scores)>0: continue
        if max(scores)<=0:
            n=scale(-1,n);h=-h;scores=[-x for x in scores]
        contact=tuple(i for i,x in enumerate(scores) if x==0)
        if len(contact)<3 or len(contact)==len(V): continue
        found[contact]=(n,h)
    return found

def orient_and_check(V,fs):
    actual=hull_faces(V)
    assert set(actual)=={tuple(sorted(f)) for f in fs}
    out=[];planes=[]
    for f in fs:
        n,h=actual[tuple(sorted(f))]
        if dot(n,cross(sub(V[f[1]],V[f[0]]),sub(V[f[2]],V[f[0]])))<0:
            f=tuple(reversed(f))
        for a,b in zip(f,f[1:]+f[:1]):
            for c in f:
                if c not in (a,b):
                    assert dot(n,cross(sub(V[b],V[a]),sub(V[c],V[a])))>0
        assert all(dot(n,V[i])==h for i in f)
        assert all(dot(n,V[i])<h for i in range(9) if i not in f)
        out.append(f);planes.append((n,h))
    uses={e:[] for e in edges(out)}
    for f in out:
        for a,b in zip(f,f[1:]+f[:1]): uses[tuple(sorted((a,b)))].append((a,b))
    assert all(len(v)==2 and v[0]==v[1][::-1] for v in uses.values())
    for i in range(9):
        ns=[planes[j][0] for j,f in enumerate(out) if i in f]
        assert any(det(*t)!=0 for t in combinations(ns,3))
    assert (len(V),len(uses),len(out))==(9,15,8)
    return tuple(out),planes

def fan(f,b):
    j=f.index(b);f=f[j:]+f[:j]
    return tuple((b,f[i],f[i+1]) for i in range(1,len(f)-1))
def mass(V,fs):
    ts=tuple(t for f in fs for t in fan(f,f[0]))
    ds=[det(*(V[i] for i in t)) for t in ts]
    D=sum(ds); assert D>0
    g=scale(F(1,4)/D,total(scale(d,total(V[i] for i in t)) for d,t in zip(ds,ts)))
    return D/F(6),g

def raw_control(k):
    rays=[tuple(map(F,(x,y,1))) for x,y in HEX]
    ell=[v[0]+v[1]/3 for v in rays]
    V=[(F(0),)*3]+[scale(min(F(1),(1+EPS*k)/(1+EPS*l)),v) for l,v in zip(ell,rays)]
    for i in range(6):
        j=(i+1)%6
        if (ell[i]-k)*(ell[j]-k)<0:
            t=(k-ell[i])/(ell[j]-ell[i])
            V.append(add(scale(1-t,rays[i]),scale(t,rays[j])))
    assert len(V)==9
    return V

def canonical_control(mask,fs):
    W=raw_control(THRESHOLDS[mask]);hf=hull_faces(W)
    # Two vertices are adjacent precisely when their common facets intersect in that pair.
    we=set()
    for f,g in combinations(hf,2):
        z=set(f)&set(g)
        if len(z)==2: we.add(tuple(sorted(z)))
    wa=[set() for _ in W]
    for a,b in we: wa[a].add(b);wa[b].add(a)
    ca=adjacency(fs,9); order=sorted(range(9),key=lambda i:(-len(ca[i]),i))
    mapping={};used=set();answer=None
    def visit(k):
        nonlocal answer
        if k==9:
            if {tuple(sorted(mapping[v] for v in f)) for f in fs}==set(hf):
                answer=dict(mapping);return True
            return False
        a=order[k]
        for b in range(9):
            if b in used or len(ca[a])!=len(wa[b]): continue
            if any((x in ca[a])!=(y in wa[b]) for x,y in mapping.items()): continue
            mapping[a]=b;used.add(b)
            if visit(k+1):return True
            used.remove(b);del mapping[a]
        return False
    assert visit(0)
    return [W[answer[i]] for i in range(9)]

def describe(mask,fs):
    adj=adjacency(fs,9); a=next(i for i in range(9) if len(adj[i])==6)
    assert sorted(map(len,adj))==[3]*8+[6]
    caps=[i for i,f in enumerate(fs) if a not in f]
    assert len(caps)==2
    ridge=sorted(set(fs[caps[0]])&set(fs[caps[1]]))
    assert len(ridge)==2 and tuple(ridge) in edges(fs)
    assert set(ridge)==set(range(9))-{a}-adj[a]
    priv=[sorted(set(fs[f])-set(ridge)) for f in caps]
    assert set(priv[0])|set(priv[1])==adj[a] and not set(priv[0])&set(priv[1])
    forced=[]
    for low in (0,1):
        high=1-low
        for r in ridge:
            h=sorted(adj[r]&set(priv[high]));assert len(h)==1
            forced.append(dict(low_cap=caps[low],high_cap=caps[high],ridge_max=r,
                               forced_true_escape=[r,h[0]],nonedge_root_comparison=[r,a]))
    return dict(mask=mask,apex=a,caps=caps,ridge=ridge,private=priv,forced=forced,
                faces=fs,edges=edges(fs))

def certificate(V,fs,desc,g):
    P=[sub(v,g) for v in V];a=desc['apex'];A=P[a]
    maxsets=[[i for i in fs[f] if norm(P[i])==max(norm(P[j]) for j in fs[f])]
             for f in desc['caps']]
    rows=[]
    for b0 in maxsets[0]:
        for b1 in maxsets[1]:
            tt=[];ds=[];Bs=[];Us=[];Vs=[];which=[]
            for j,(f,b) in enumerate(zip(desc['caps'],(b0,b1))):
                for t in fan(fs[f],b):
                    d=det(*(sub(P[i],A) for i in t));assert d>0
                    tt.append(t);ds.append(d);Bs.append(P[b]);Us.append(P[t[1]]);Vs.append(P[t[2]]);which.append(j)
            assert len(tt)==6
            D=sum(ds);B=total(scale(d,b) for d,b in zip(ds,Bs))
            Ys=[add(u,v) for u,v in zip(Us,Vs)];Y=total(scale(d,y) for d,y in zip(ds,Ys))
            assert add(add(scale(D,A),B),Y)==(0,0,0)
            E=sum(d*bil(b,sub(A,b)) for d,b in zip(ds,Bs))
            q0=norm(sub(scale(D,A),B))
            q1=D*sum(d*norm(sub(u,v)) for d,u,v in zip(ds,Us,Vs))
            q2=sum(ds[i]*ds[j]*norm(sub(Ys[i],Ys[j])) for i,j in combinations(range(6),2))
            q3=2*D*sum(d*(2*norm(b)-norm(u)-norm(v)) for d,b,u,v in zip(ds,Bs,Us,Vs))
            assert min(q0,q1,q2,q3)>=0 and q1>0 and E<0
            assert 4*D*E+q0+q1+q2+q3==0
            rows.append(dict(maxima=[b0,b1],triangles=tt,determinants=ds,
                cap_determinants=[sum(d for d,jj in zip(ds,which) if jj==j) for j in (0,1)],
                weighted_escape_numerator=E,terms=[4*D*E,q0,q1,q2,q3]))
    return P,rows

def inverse3(A):
    d=det(*A);assert d>0
    cs=[cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1])]
    return tuple(tuple(cs[j][i]/d for j in range(3)) for i in range(3))
def census(P,fs,planes,g):
    N=inverse3(M);Q=[]
    for n,h in planes:
        s=h-dot(n,g);assert s>0
        Q.append(scale(1/s,n))
    def bm(x,y):return dot(x,tuple(dot(row,y) for row in N))
    pe={};de={};pairs=[]
    for i,j in edges(fs):
        pe[i,j]=bil(P[i],sub(P[j],P[i]));pe[j,i]=bil(P[j],sub(P[i],P[j]))
        f,h=[k for k,c in enumerate(fs) if i in c and j in c]
        de[f,h]=bm(Q[f],sub(Q[h],Q[f]));de[h,f]=bm(Q[h],sub(Q[f],Q[h]))
        pairs.append((i,j,f,h))
    U=[i for i in range(9) if all(z<0 for (a,b),z in pe.items() if a==i)]
    S=[i for i in range(8) if all(z<0 for (a,b),z in de.items() if a==i)]
    H=[(i,j) for i,j,f,h in pairs if max(pe[i,j],pe[j,i],de[f,h],de[h,f])<0]
    deg=[(i,j) for i,j,f,h in pairs if max(pe[i,j],pe[j,i],de[f,h],de[h,f])==0]
    assert not deg and all(pe.values()) and all(de.values())
    assert len(S)+len(U)-len(H)==2
    return dict(S=S,U=U,H=H,nonedge_comparisons_are_not_edges=True,
                directed_primal={str(k):v for k,v in pe.items()},
                directed_dual={str(k):v for k,v in de.items()})

def formal_identity():
    import sympy as s
    n=6; a=s.symbols('a');d=s.symbols('d:6');b=s.symbols('b:6');u=s.symbols('u:6');v=s.symbols('v:6')
    D=sum(d);B=sum(d[i]*b[i] for i in range(n));Y=sum(d[i]*(u[i]+v[i]) for i in range(n))
    E=sum(d[i]*b[i]*(a-b[i]) for i in range(n))
    gap=D*sum(d[i]*(u[i]-v[i])**2 for i in range(n))
    var=sum(d[i]*d[j]*(u[i]+v[i]-u[j]-v[j])**2 for i,j in combinations(range(n),2))
    deficit=2*D*sum(d[i]*(2*b[i]**2-u[i]**2-v[i]**2) for i in range(n))
    lhs=4*D*E+(D*a-B)**2+gap+var+deficit
    assert s.expand(lhs-(D*a+B+Y)*(D*a+B-Y))==0
    print('FORMAL_SIX_TETRAHEDRON_MOMENT_IDENTITY_PASS',s.__version__,flush=True)

def main():
    assert sys.argv[1:] in ([],['--formal'])
    assert M[0][0]>0 and M[0][0]*M[1][1]-M[0][1]**2>0 and det(*M)>0
    report=dict(version=1,name='DEG6_ROOF_MAXIMUM_OBSTRUCTION_V1',parent=PARENT,
                metric=M,epsilon=EPS,thresholds=THRESHOLDS,maps=[])
    for mask,fs in MAPS.items():
        desc=describe(mask,fs);V=canonical_control(mask,fs);fs,planes=orient_and_check(V,fs)
        volume,g=mass(V,fs);P,certs=certificate(V,fs,desc,g)
        assert mass(P,fs)==(volume,(0,0,0))
        assert all(sum(c['determinants'])==6*volume for c in certs)
        a=desc['apex'];N=[norm(p) for p in P]
        assert N[a]>max(N[i] for i in range(9) if i!=a)
        private_max=[max(N[i] for i in group) for group in desc['private']]
        ridge_max=max(N[i] for i in desc['ridge'])
        sector=(private_max[0]-ridge_max)*(private_max[1]-ridge_max)
        assert min(private_max)>ridge_max and sector>0
        mech=census(P,fs,planes,g)
        assert a in mech['U'] and len(mech['U'])>=2
        print('CONTROL',mask,'APEX',a,'CAPS',desc['caps'],'PRIVATE_SIZES',list(map(len,desc['private'])),
              'ORDER_PRODUCT_SIGN',(sector>0)-(sector<0),'CENSUS',list(map(len,(mech['S'],mech['U'],mech['H']))),flush=True)
        desc.update(vertices=V,centroid=g,volume=volume,oriented_faces=fs,planes=planes,
                    centered_vertices=P,norm_squared=N,private_max=private_max,ridge_max=ridge_max,
                    order_product=sector,certificates=certs,mechanics=mech)
        report['maps'].append(desc)
    if '--formal' in sys.argv:formal_identity()
    raw=(json.dumps(report,default=str,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
    path=Path('degree6_roof_max_v1_report.json');path.write_bytes(raw);assert path.read_bytes()==raw
    print('REPORT',len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
    data=Path(__file__).read_bytes();print('SOURCE',len(data),hashlib.sha256(data).hexdigest(),flush=True)
    print('THREE_EXACT_ACTUAL_MASS_CONTROLS_PASS',flush=True)
    print('NO_WHOLE_TYPE_OR_JOINT_ROOT_CLASS_CLOSED',flush=True)
if __name__=='__main__':main()
```

Expected terminal output for `--formal`:

```text
CONTROL 5675263 APEX 7 CAPS [0, 7] PRIVATE_SIZES [5, 1] ORDER_PRODUCT_SIGN 1 CENSUS [7, 7, 12]
CONTROL 14858559 APEX 6 CAPS [0, 3] PRIVATE_SIZES [4, 2] ORDER_PRODUCT_SIGN 1 CENSUS [7, 7, 12]
CONTROL 51318223 APEX 8 CAPS [0, 1] PRIVATE_SIZES [3, 3] ORDER_PRODUCT_SIGN 1 CENSUS [8, 7, 13]
FORMAL_SIX_TETRAHEDRON_MOMENT_IDENTITY_PASS 1.14.0
REPORT 25829 92d26a38f7380c9327ed4a2b34b906152df249fa32dba2cab4e57571ba375d34
SOURCE 11616 4f8ecf2c2f794cc4d9ace4794f1392b1c1e860f8fa78c935eab21608b70c45fe
THREE_EXACT_ACTUAL_MASS_CONTROLS_PASS
NO_WHOLE_TYPE_OR_JOINT_ROOT_CLASS_CLOSED
```

Convenience copies, unnecessary for the inline reconstruction: [complete source](sandbox:/mnt/data/degree6_roof_max_v1.py) and [exact generated report](sandbox:/mnt/data/degree6_roof_max_v1_report.json).
