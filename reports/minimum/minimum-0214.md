# minimum-0214

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# ENDPOINT6_TWO_ANTIPODES_19_OVER60_V1

## 1. Complete endpoint6 obstruction

**The entire endpoint-root six-step form is impossible under −Q/3⊂Q.** A stronger uniform separation is proved:

> Let Q be a convex planar polygon with seven true corners q0,…,q6 listed counterclockwise, contain 0 strictly in its interior, and satisfy qi·(q(i−1)−qi)≥0 for i=1,…,6. Normalize q0=(1,0). Then the two points −19q0/60 and −19q2/60 cannot both belong to Q.

In fact the proof establishes the stronger support alternative

```text
min_i (qi)x ≤ −19/60  ⇒  −19q2/60 ∉ Q.                 (T)
```

Thus −(19/60)Q is not contained in Q. Since 19/60<1/3 and 0∈Q, containment −Q/3⊂Q would imply the forbidden smaller containment. The gap between these coefficients is exactly 1/60. The constant 19/60 is not claimed optimal.

This is an all-shape theorem. Selected arrows may be weak, all equality walls of the necessary scalar inequalities are included, and no equal-turn, tight-arrow, fixed-radius, uniform-area-centroid or prescribed polygon-family assumption is made. A fixed planar SPD can be absorbed by a linear isometry before the Euclidean normalization, so the corresponding common-planar-metric statement follows as well.

The parent’s ≤6-corner result and the coordinator’s separate 4+2 obstruction are inputs to the broader branch context, not substitutes for this endpoint proof. The only seven-corner branch form left by their combination with the present result is **5+1**, up to reflection. No all-seven-corner theorem, actual 3D lift, 110 attainer, or changed complexity bound is asserted. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## 2. Source identity and proof organization

The new journal `research-journal(20260923-223911).md`, including its literal parent, and the complete material `[internal-source-reference]` were read through EOF. The parent is

```text
minimum-0209
SHA256 adebd2f62354466c4f5cdadbb45aec998631c8d8854876b6c92411d83403ff1c
HEX6_SIX_CORNER_SHADOW_OBSTRUCTION_AND_BASE_TANGENT_U2_V5.
```

There is no missing exact dependency for the new theorem or its recovery. The new mechanism is: use the opposite of the SECOND chain corner to prohibit a half-turn in the remaining four edges; then combine its containment in the actual closing-edge halfplane with the negative support forced by the root. This couples the early radius, the middle contraction and the final radius. Independent root-axis width bounds lose this coupling.

The proof has an analytic small-angle part and an exhaustive rational polynomial certificate on three compact boxes. Those three cases are subdivisions of the SAME endpoint6 form, indexed by the corner providing the negative x-support. They are not the already-settled rooted4+2,3+3 forms.

## 3. Angles and the decisive half-turn restriction

Write qi=ri(cosθi,sinθi), with

```text
r0=1,  0=θ0<θ1<…<θ6=ψ<2π.
```

The cyclic angle order follows from true convex corners and 0∈intQ. The closing edge has angular span less thanπ, so ψ>π. For each selected arrow,

```text
ri ≤ r(i−1)cos(θi−θ(i−1)),
0<θi−θ(i−1)<π/2.
```

Even at equality in the arrow, norms strictly decrease away from q0 because

```text
|q(i−1)|²−|qi|² = 2Di,i−1+|q(i−1)−qi|²>0.
```

For any contiguous m-step chain, concavity of logcos gives a radius ratio at most cos^m(span/m). In particular the first three x-coordinate bounds are

```text
(q1)x≥0,  (q2)x≥−1/8,  (q3)x≥−1/4.
```

They follow by maximizing (−cosθ)cos^m(θ/m) where cosθ<0; its maximum is cos^(m+1)(π/(m+1)). This is the inherited radial-chain calculation, also valid for weak arrows. :contentReference[oaicite:2]{index=2}

Set λ=19/60, L=60/19. Suppose, toward a contradiction, that min_i(qi)x≤−λ and −λq2∈Q. Since λ>1/4, some k∈{4,5,6} satisfies (qk)x≤−λ.

**Half-turn lemma.** Necessarily ψ−θ2<π. Otherwise the ray opposite q2 meets the actual boundary on the tail q2,…,q6. If its intersection lies inside an edge [qa,q(a+1)], that point itself has a weak arrow toward qa: along the edge, v·(q(a+1)−qa) is no larger than its nonpositive value at q(a+1). Thus the intersected ray is reached from q2 by at most four weak steps with total angleπ. Its boundary radius is at most r2cos^4(π/4)=r2/4. Chains of three steps give an even smaller bound; fewer steps cannot spanπ with acute increments. This contradicts the assumed point of radius λr2 on that ray. The case ψ−θ2=π is included.

Consequently, putting θ=θ2,

```text
0<θ<π,  0<δ:=ψ−θ<π,  ψ>π.                         (1)
```

This argument does not insert fictitious corners into Q. The only additional point is an actual boundary intersection, used in a scalar chain estimate.

## 4. Reduction to three complete angular cases

For the chosen k let

```text
j=k−2, m=6−k, (j,m)∈{(2,2),(3,1),(4,0)},
φ=θk, α=φ−θ, β=ψ−φ,
θ=2u, α=jv, β=mw,
κ=cos^j v, τ=cos^m w,
c=−cosφ>0, r=r2, R=rk, S=r6.
```

For m=0 take β=0,τ=1, with no w-variable. All group angles are real geometric spans. In particular u,v,w∈(0,π/2) whenever the group exists. Jensen gives

```text
r≤cos²u, R≤rκ, S≤Rτ≤rκτ, Rc≥λ.
```

Therefore

```text
G := Lcos²u κc−1 ≥0,  r≥λ/(κc).                    (2)
```

Now use the actual closing edge q6→q0. Its interior-left support inequality at −λq2 is exactly

```text
det(q0−q6,−λq2−q6)
 = S[−sinψ−λr sinδ]−λr sinθ ≥0.                  (3)
```

Its bracket is positive because the right-hand term λr sinθ is positive. Substituting S≤rκτ and then r≥λ/(κc), using sinδ>0, gives the further necessary inequality

```text
F := τ[L²κ cosφ sinψ−sinδ]+Lcosφ sinθ ≥0.         (4)
```

Thus every putative polygon supplies (1),(2),(4). The remaining proof shows that this necessary relaxation itself is empty. No converse realization claim is needed.

## 5. The whole small-initial-angle sector

Let x=tan u. If 0<x≤1/9, then θ<2/9. From (1),

```text
δ>π−θ>25/8−2/9=209/72.
```

The last four individual turns have total δ. Applying concavity of logcos to the group means as well gives

```text
κτ≤cos⁴(δ/4)<cos⁴(209/288)<(3/4)^4<19/60.
```

The rational inequalities are certified by

```text
16(1/5−1/375)−4/239−25/8 =11183/717000>0,
3/4−[1−(209/288)²/2+(209/288)^4/24]
 =290649791/165112971264>0,
19/60−(3/4)^4=1/3840>0.
```

The first is the alternating-series lower bound in Machin’s identity π=16arctan(1/5)−4arctan(1/239); the second is the alternating Taylor upper bound forcos on this interval.

Expanding sinψ=sin(θ+δ) rewrites (4) as

```text
F=sinθ cosφ[L+L²κτ cosδ]
  +τsinδ[L²κ cosφ cosθ−1].                       (5)
```

Here sinθ>0, cosφ<0, cosθ>0, sinδ>0. The first bracket is greater than L−L²κτ>0; the second is negative. Thus F<0, contradicting (4). This covers the entire sector including x=1/9. The nonphysical x=0 limit is not used as a positive-angle polygon.

## 6. Exact exhaustive certificate for all remaining angles

### 6.1. Compact domains with no angular tail discarded

For x≥1/9 set y=tan v and, when m>0, z=tan w. From (2), cos²u≥λ and κ≥λ. Therefore

```text
1/9≤x≤3/2,
0≤y≤3/2 for j=2,
0≤y≤6/5 for j=3,
0≤y≤1   for j=4.
```

These are safe closed overbounds: L−1=41/19<9/4 and each corresponding (1+ymax²)^j is greater than L². For m>0 compactify the entire remaining z≥0 direction by t=z/(1+z)∈[0,1]. Finite physical z has t<1; the certificate also includes t=1. There is no upper truncation of a last-group tangent.

### 6.2. Literal polynomial input

Use the formal complex products

```text
A=(1+ix)^2, B=(1+iy)^j, C=(1+iz)^m,
H=Re(AB), J=Im(BC), K=Im(ABC),
D=(1+x²)^2(1+y²)^j,
Gpoly=−LH−D,
Fpoly=L²HK−DJ+2LxH(1+y²)^j(1+z²)^m.              (6)
```

The letter J in this new planar problem is an imaginary-part polynomial, not a K2 mass polynomial. Direct sine/cosine denominators show that (2),(4) and (1) require

```text
Gpoly≥0,  J≥0,  K≤0,  Fpoly≥0.                  (7)
```

For example Fpoly is F multiplied by the strictly positive factor

```text
(1+x²)^2(1+y²)^(3j/2)(1+z²)^m.
```

For each polynomial separately replace z=t/(1−t) and multiply by (1−t) to its own degree in z. For m=0 omit z,t entirely. This preserves every necessary sign at physical finite parameters.

On every closed leaf box, the source proves at least one of the four contradiction polynomials

```text
capacity=−Gpoly, delta=−J, closing=K, target=−Fpoly
```

STRICTLY positive. Their full power data are generated by (6), not supplied by a numerical fit.

### 6.3. Complete coverage and verification

The root boxes are the x/y intervals above, times t∈[0,1] when present. At a node test the four guards in the displayed order; accept the first with all tensor Bernstein coefficients strictly positive. Otherwise bisect coordinate depth modulo dimension at its rational midpoint, and process the lower child before the upper. A depth 30 safeguard is included, but no node reaches it. There is no other pruning.

| Negative-support corner k | Group lengths j,m | Nodes | Closed leaves | Strictly positive selected coefficients | Maximum depth |
|---|---:|---:|---:|---:|---:|
|4|2,2|175|88|8886|20|
|5|3,1|353|177|17147|17|
|6|4,0|19|10|460|4|
|Total||547|275|26493||

Leaf guard counts are respectively

```text
k4: capacity39, target45, delta4;
k5: capacity59, closing5, target99, delta14;
k6: capacity2, closing3, target5.
```

The smallest selected coefficients in the three covers are

```text
4471443721930099/6931039826523193344,
1131400677298619/60515942400000000,
2/9.
```

Tensor Bernstein basis functions are nonnegative and sum to1 on the unit box, so positive coefficients give strict positivity throughout the entire closed leaf. The source checks complete binary-prefix coverage and Kraft sum 1. For EVERY leaf it independently recomputes its selected Bernstein coefficients directly from the original power polynomial and its rational box, comparing them to the recursive de Casteljau coefficients. It then reconstructs the full scaled power polynomial by the inverse tensor transformation. All 275 inversions and comparisons pass. All 26493 selected coefficients are strictly positive, including closed box walls; no sampled sign test is substituted.

Therefore (7) has no point in any of the three remaining domains. Together with section 5 this proves (T) over the entire endpoint6 class, including weak-arrow equalities.

## 7. Exact planar controls and the need for the second opposite point

### 7.1. Preserved strict three-tenths control

The coordinator’s existing endpoint6 polygon is preserved unchanged: divide these rows by10^9,

```text
(1000000000,0),
(440691788,496425691),
(−52229194,437541480),
(−222140726,319275645),
(−305493139,156661940),
(−303007708,−4612753),
(−131243132,−152453615).
```

It has six strict selected arrows,14 nonzero boundary primitives, strict convexity,0 interior, and strict containment −(3/10)Q⊂intQ. It fails1/3, as its literal source already establishes. :contentReference[oaicite:3]{index=3} The new exact audit also gives its actual maximum self-containment coefficient

```text
5698653538325253/18802575268045409 ≈0.3030783526770398,
```

limited by edge5–6 and reflected vertex1. This is the value of this particular rational polygon, not the optimum over endpoint6 polygons and not the earlier floating local optimum.

### 7.2. New weak and strict controls defeating the wrong two-point test

Identify the plane with complex numbers and put a=(16+12i)/25. Define

```text
q0=1, q1=a, q2=a², q3=a³, q4=a⁴,
q5=Re(q4), q6=a q5.
```

The complete rational rows are

```text
(1,0),
(16/25,12/25),
(112/625,384/625),
(−2816/15625,7488/15625),
(−134912/390625,86016/390625),
(−134912/390625,0),
(−2158592/9765625,−1618944/9765625).
```

This is a genuine strictly convex seven-gon with 0 interior. All six selected primitives are exactly0, their opposite incident primitives are negative, and0 is the sole strict radial-maximum corner. Its minimum convexity and origin margins are

```text
104441315328/3814697265625,
218414972928/3814697265625.
```

Both −q0/3 and −q1/3 are STRICTLY inside Q: their minimum support margins are both7614972928/3814697265625>0. Nevertheless −q2/3 is outside, with closing-edge margin

```text
−18160768/244140625<0.
```

Thus even the first two reflected chain vertices, not merely the root-axis width, are insufficient. Choosing q2 in the new mechanism is substantive.

For a strict version take exactly qi'=(999/1000)^i qi, without translating the origin. The source verifies all 35 nonincident convexity guards, all 7 origin guards and all 14 nonzero primitives. All six selected arrows are now positive,0 remains the sole strict radial maximum, and both −q0'/3 and −q1'/3 remain strictly inside. The minimum common margin is

```text
24742230589477179159636848945129223813 /
14551915228366851806640625000000000000000 >0,
```

whereas −q2'/3 has margin

```text
−1112928444839383134656472027/14901161193847656250000000000<0.
```

The three controls together have 36 nonzero boundary primitives and six prescribed weak primitives. Full support arrays at3/10,19/60 and1/3, all primitive lists and exact containment limits are regenerated by the capsule. None satisfies −Q/3⊂Q; none is presented as an actual 3D shadow or110 body.

## 8. Mechanical transfer and genuinely remaining work

For a uniformly filled 3D polytope centred at its actual volume centroid, an actual apex tetrahedral fan gives

```text
0=[a+Σ θT(bT+cT+dT)]/4,
−a/3=Σ θT(bT+cT+dT)/3 ∈P.
```

Hence −P/3⊂P, and every linear shadow inherits −Q/3⊂Q. The marginal on the shadow is its real concave fibre-length density, not uniform planar area density. :contentReference[oaicite:4]{index=4} The present endpoint6 obstruction therefore rules out this boundary-tree form for every such rank-two shadow. Combined with the accepted≤6,3+3 and4+2 results, a seven-corner shadow with a sole strict radial maximum must have the5+1 form.

The parent’s exposed-fibre argument remains necessary when transporting planar maxima to true3D weak reachability: an exposed shadow corner lifts to a true vertex or edge, and its strictly negative outgoing boundary prevents escape even when internal edges collapse. Projected edges are not silently identified with true primal edges. :contentReference[oaicite:5]{index=5}

The5+1 universal planar question is not resolved here. A possible planar witness in any remaining class would still need an actual homogeneous3D lift and then the common reciprocal metric, saddle and weak-point checks. Nor does exclusion at a rank-two boundary by itself exclude an SPD component away from that boundary. No canonical incidence register or global bound is changed.

## 9. Execution status and self-contained recovery

The continuous argument is sections 3–6, not an inference from optimizer failure. The three final polynomial covers and all three controls were generated and audited with exact standard-library Fraction arithmetic. Build and check exited 0 with identical stdout; a separate source-only directory rebuilt the same report byte for byte. This is not an independently authored implementation or a proof-assistant formalization.

Observed environment: CPython3.13.5; the supplied source supports CPython≥3.11 and uses no third-party package. Exact inputs, guard order, root boxes, splitting rule, depth safeguard and controls are all literal in the source.

Save the source below as `endpoint6_exact.py`, UTF-8/LF with the final newline. Commands:

```text
python -B -S endpoint6_exact.py build > build.out
python -B -S endpoint6_exact.py check > check.out
cmp build.out check.out
```

Pins:

```text
endpoint6_exact.py:12302 bytes
SHA256 5216c08e72c6573658658440505aa698b970cb37303888167134e1192e72669d
endpoint6_exact.json:1263595 bytes
SHA256 2d3646c0d4b07cb190c0163e634ee01a1aa9c9e759cd8ba890d56a4ed27fc7f9
identical stdout:457 bytes
SHA256 45e34a12635658b945a049054c04c542adb1d154e673737025e653998cd51712
```

Expected terminal markers include

```text
ENTIRE_SMALL_INITIAL_ANGLE_AND_UNBOUNDED_TAIL_REDUCTION_PASS
THREE_TRUE_PLANAR_CONTROLS_36_NONZERO_SIX_WEAK_ARROWS_PASS
ENDPOINT6_ALL_SHAPES_WEAK_WALLS_TWO_ANTIPODES_19_OVER60_PASS 1263595 2d3646c0d4b07cb190c0163e634ee01a1aa9c9e759cd8ba890d56a4ed27fc7f9
```

Supplementary copies: [source](sandbox:/mnt/data/endpoint6_exact.py), [complete bundle](sandbox:/mnt/data/ENDPOINT6_19_OVER60_bundle.zip). The full source below is sufficient without these links or any previous code.

### Complete runnable source

```python
#!/usr/bin/env python3
"""ENDPOINT6_TWO_ANTIPODES_19_OVER60_V1.
CPython >=3.11, standard library only; assertions enabled.
python -B -S endpoint6_exact.py build|check
The continuous geometric proof is in the accompanying handoff. This source
reconstructs its complete scalar cover and exact planar scope controls.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
from collections import Counter
from pathlib import Path
import hashlib,json,sys
assert __debug__ and sys.version_info >= (3,11)
HERE=Path(__file__).resolve().parent
LAM=F(19,60)
L=1/LAM
PARENT=('minimum-0209','adebd2f62354466c4f5cdadbb45aec998631c8d8854876b6c92411d83403ff1c')
MATERIAL='[internal-source-reference]'

# Sparse exact polynomials; exponents always have one fixed dimension.
def clean(p):return {a:F(c) for a,c in p.items() if c}
def plus(*ps):
    r={}
    for p in ps:
        for a,c in p.items():r[a]=r.get(a,F(0))+c
    return clean(r)
def times(p,q):
    r={}
    for a,c in p.items():
        for b,d in q.items():
            e=tuple(x+y for x,y in zip(a,b));r[e]=r.get(e,F(0))+c*d
    return clean(r)
def mul(*ps):
    assert ps
    r=ps[0]
    for p in ps[1:]:r=times(r,p)
    return r
def scale(c,p):return clean({a:c*v for a,v in p.items()})
def mon(n,axis,power=1):
    a=[0]*n;a[axis]=power;return {tuple(a):F(1)}
def power(p,n):
    r={(0,)*len(next(iter(p))):F(1)}
    for _ in range(n):r=times(r,p)
    return r
def parts(n,axis,dim=3):
    r={};s={}
    for a in range(n+1):
        e=[0]*dim;e[axis]=a;(r if a%2==0 else s)[tuple(e)]=F(comb(n,a)*(-1)**(a//2))
    return clean(r),clean(s)
def degrees(p):return tuple(max(a[i] for a in p) for i in range(len(next(iter(p)))))
def grid(d):return tuple(product(*(range(n+1) for n in d)))
def homogenize(p):
    dz=degrees(p)[2];r={}
    for (a,b,k),c in p.items():
        for i in range(dz-k+1):
            e=(a,b,k+i);r[e]=r.get(e,F(0))+c*comb(dz-k,i)*(-1)**i
    return clean(r),dz

def polynomials(j,m):
    one={(0,0,0):F(1)};x=mon(3,0)
    a,b=parts(2,0);c,d=parts(j,1);e,f=parts(m,2)
    nx=plus(one,mon(3,0,2));ny=plus(one,mon(3,1,2));nz=plus(one,mon(3,2,2))
    assert plus(times(a,a),times(b,b))==power(nx,2)
    assert plus(times(c,c),times(d,d))==power(ny,j)
    assert plus(times(e,e),times(f,f))==power(nz,m)
    H=plus(times(a,c),scale(-1,times(b,d)))
    J=plus(times(c,f),times(d,e))
    K=plus(times(a,J),times(b,plus(times(c,e),scale(-1,times(d,f)))))
    D=times(power(nx,2),power(ny,j))
    G=plus(scale(-L,H),scale(-1,D))
    T=plus(scale(L*L,times(H,K)),scale(-1,times(D,J)),scale(2*L,mul(x,H,power(ny,j),power(nz,m))))
    out=[]
    for name,p in (('capacity',scale(-1,G)),('delta',scale(-1,J)),('closing',K),('target',scale(-1,T))):
        if m:q,dz=homogenize(p)
        else:
            assert all(a[2]==0 for a in p)
            q={a[:2]:c for a,c in p.items()};dz=0
        out.append((name,q,dz))
    return out

def affine(p,bounds):
    r=p
    for axis,(a,b) in enumerate(bounds):
        out={}
        for e,c in r.items():
            n=e[axis]
            for k in range(n+1):
                f=list(e);f[axis]=k;f=tuple(f)
                out[f]=out.get(f,F(0))+c*comb(n,k)*a**(n-k)*(b-a)**k
        r=clean(out)
    return r

def tensor_transform(d,values,axis,mat):
    ix=grid(d);data=dict(zip(ix,values));out={};n=d[axis]
    restd=d[:axis]+d[axis+1:]
    for rest in grid(restd):
        def key(k):return rest[:axis]+(k,)+rest[axis:]
        row=[data[key(k)] for k in range(n+1)]
        for k in range(n+1):out[key(k)]=sum(mat[k][i]*row[i] for i in range(n+1))
    return tuple(out[k] for k in ix)

def bernstein(p,bounds,d=None):
    d=degrees(p) if d is None else d;pp=affine(p,bounds)
    vals=tuple(pp.get(a,F(0)) for a in grid(d))
    for axis,n in enumerate(d):
        mat=[[F(comb(k,i),comb(n,i)) if i<=k else F(0) for i in range(n+1)] for k in range(n+1)]
        vals=tensor_transform(d,vals,axis,mat)
    return d,vals

def inverse_bernstein(d,values):
    vals=values
    for axis,n in enumerate(d):
        mat=[[F(comb(n,k)*comb(n-k,i-k)*(-1)**(i-k)) if k<=i else F(0) for k in range(n+1)] for i in range(n+1)]
        vals=tensor_transform(d,vals,axis,mat)
    return clean(dict(zip(grid(d),vals)))

def split(c,axis):
    d,val=c;n=d[axis];ix=grid(d);data=dict(zip(ix,val));left={};right={}
    for rest in grid(d[:axis]+d[axis+1:]):
        def key(k):return rest[:axis]+(k,)+rest[axis:]
        row=[data[key(k)] for k in range(n+1)];a=[row[0]];b=[row[-1]]
        for _ in range(n):
            row=[(x+y)/2 for x,y in zip(row,row[1:])];a.append(row[0]);b.append(row[-1])
        for k in range(n+1):left[key(k)]=a[k];right[key(k)]=b[n-k]
    return (d,tuple(left[k] for k in ix)),(d,tuple(right[k] for k in ix))

def path_box(root,path):
    b=list(root)
    for depth,bit in enumerate(path):
        ax=depth%len(b);a,c=b[ax];mid=(a+c)/2
        b[ax]=(a,mid) if bit=='0' else (mid,c)
    return tuple(b)

def prefix_check(paths):
    leaves=set(paths);assert len(leaves)==len(paths)
    prefixes={p[:i] for p in leaves for i in range(len(p)+1)}
    def visit(p):
        if p in leaves:
            assert p+'0' not in prefixes and p+'1' not in prefixes
            return 1
        assert p+'0' in prefixes and p+'1' in prefixes
        return 1+visit(p+'0')+visit(p+'1')
    n=visit('');assert sum(F(1,2**len(p)) for p in leaves)==1
    return n

EXPECTED={2:(175,88,20,{'capacity':39,'target':45,'delta':4}),3:(353,177,17,{'capacity':59,'closing':5,'target':99,'delta':14}),4:(19,10,4,{'closing':3,'target':5,'capacity':2})}
def cover(j,m):
    root=((F(1,9),F(3,2)),(F(0),{2:F(3,2),3:F(6,5),4:F(1)}[j]))+(((F(0),F(1)),) if m else ())
    ps=polynomials(j,m);cs=[bernstein(p,root) for _,p,_ in ps]
    for (_,p,_),(d,c) in zip(ps,cs):assert inverse_bernstein(d,c)==affine(p,root)
    stack=[('',cs)];leaves=[];nodes=0
    while stack:
        path,cc=stack.pop();nodes+=1
        chosen=next((i for i,c in enumerate(cc) if min(c[1])>0),None)
        if chosen is not None:
            name,p,_=ps[chosen];d,c=cc[chosen];box=path_box(root,path)
            # This recomputes the selected leaf directly from the original
            # power polynomial, independently of the subdivision operations.
            assert bernstein(p,box,d)==(d,c)
            assert inverse_bernstein(d,c)==affine(p,box)
            leaves.append(dict(path=path,guard=name,box=box,degrees=d,coefficients=c,minimum=min(c)))
            continue
        assert len(path)<30,('UNCLOSED_CELL',j,m,path)
        children=[split(c,len(path)%len(root)) for c in cc]
        stack.append((path+'1',[c[1] for c in children]));stack.append((path+'0',[c[0] for c in children]))
    counts=dict(Counter(a['guard'] for a in leaves));depth=max(len(a['path']) for a in leaves)
    assert (nodes,len(leaves),depth,counts)==EXPECTED[j]
    assert prefix_check([a['path'] for a in leaves])==nodes
    coeffs=sum(len(a['coefficients']) for a in leaves)
    print('CLOSED_GROUP',j,m,'NODES',nodes,'LEAVES',len(leaves),'COEFFICIENTS',coeffs,'MAX_DEPTH',depth)
    return dict(j=j,m=m,root_box=root,nodes=nodes,leaves=leaves,counts=counts,max_depth=depth,coefficient_count=coeffs,polynomials=[dict(name=name,power_terms=sorted(p.items()),z_clearing_degree=dz) for name,p,dz in ps])

def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def cmul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

def planar(name,q,kind):
    q=tuple(tuple(map(F,p)) for p in q);assert q[0]==(1,0) and len(q)==len(set(q))==7
    e=tuple(sub(q[(i+1)%7],q[i]) for i in range(7))
    convex=[(i,j,cross(e[i],sub(q[j],q[i]))) for i in range(7) for j in range(7) if j not in (i,(i+1)%7)]
    inside=[cross(q[i],q[(i+1)%7]) for i in range(7)]
    arrows=[(i,j,dot(q[i],sub(q[j],q[i]))) for i in range(7) for j in ((i-1)%7,(i+1)%7)]
    selected=[dot(q[i],sub(q[i-1],q[i])) for i in range(1,7)]
    roots=[i for i in range(7) if all(c<0 for a,b,c in arrows if a==i)]
    assert min(a[2] for a in convex)>0 and min(inside)>0 and min(selected)>=0 and roots==[0]
    assert all(dot(q[i],q[i])<dot(q[i-1],q[i-1]) for i in range(1,7))
    tests=[]
    for lam in (F(3,10),LAM,F(1,3)):
        mat=[[cross(e[i],sub(tuple(-lam*x for x in q[j]),q[i])) for j in range(7)] for i in range(7)]
        cols=[min(row[j] for row in mat) for j in range(7)]
        if lam==LAM:assert min(cols[0],cols[2])<0
        if kind=='inherited' and lam==F(3,10):assert min(cols)>0
        if kind!='inherited' and lam==F(1,3):assert cols[0]>0 and cols[1]>0 and cols[2]<0
        tests.append(dict(lam=lam,all_support_margins=mat,column_minima=cols,minimum=min(cols)))
    if kind=='weak':assert selected==[0]*6 and sum(c==0 for a,b,c in arrows)==6
    else:assert min(selected)>0 and all(c!=0 for a,b,c in arrows)
    limiting=[]
    for i in range(7):
        for j in range(7):
            a=cross(e[i],q[j])
            if a>0:limiting.append((inside[i]/a,i,j))
    cap=min(limiting)
    return dict(name=name,kind=kind,vertices=q,parents=(0,0,1,2,3,4,5),convexity=convex,origin_margins=inside,all_14_arrows=arrows,selected=selected,strict_radial_maxima=roots,containment=tests,exact_maximum_self_containment=cap,actual_3D_lift_claim=False)

def controls():
    nums=((1000000000,0),(440691788,496425691),(-52229194,437541480),(-222140726,319275645),(-305493139,156661940),(-303007708,-4612753),(-131243132,-152453615))
    inherited=tuple(tuple(F(a,10**9) for a in p) for p in nums)
    factor=(F(16,25),F(12,25));q=[(F(1),F(0))]
    for _ in range(4):q.append(cmul(q[-1],factor))
    q.append((q[-1][0],F(0)));q.append(cmul(q[-1],factor))
    strict=tuple(tuple(v*F(999,1000)**i for v in p) for i,p in enumerate(q))
    out=[planar('INHERITED_ENDPOINT6_STRICT_THREE_TENTHS',inherited,'inherited'),planar('NEW_ENDPOINT6_TWO_WRONG_ANTIPODES_WEAK',q,'weak'),planar('NEW_ENDPOINT6_TWO_WRONG_ANTIPODES_STRICT',strict,'strict')]
    assert out[0]['containment'][0]['minimum']==F(578809579116303,1250000000000000000)
    assert out[0]['containment'][2]['minimum']==F(-4556747864895167,300000000000000000)
    assert out[1]['containment'][2]['column_minima'][0]==F(7614972928,3814697265625)
    assert out[1]['containment'][2]['column_minima'][2]==F(-18160768,244140625)
    print('THREE_TRUE_PLANAR_CONTROLS_36_NONZERO_SIX_WEAK_ARROWS_PASS')
    return out

def constants():
    lower_pi=16*(F(1,5)-F(1,375))-F(4,239)
    assert lower_pi-F(25,8)==F(11183,717000)>0
    t=F(209,288);upper_cos=1-t*t/2+t**4/24
    assert F(3,4)-upper_cos==F(290649791,165112971264)>0
    assert LAM-F(3,4)**4==F(1,3840)>0
    assert (F(25,8)-F(2,9))/4==t
    assert L-1<F(3,2)**2
    for j,y in ((2,F(3,2)),(3,F(6,5)),(4,F(1))):assert (1+y*y)**j>L*L
    assert F(1,3)-LAM==F(1,60)
    print('ENTIRE_SMALL_INITIAL_ANGLE_AND_UNBOUNDED_TAIL_REDUCTION_PASS')
    return dict(lam=LAM,L=L,small_x=F(1,9),pi_lower=lower_pi,cos_argument=t,cos_upper=upper_cos,cos_gap=F(3,4)-upper_cos,tail_product_gap=LAM-F(3,4)**4,third_gap=F(1,3)-LAM)

def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [enc(v) for v in x]
    return x
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def main():
    assert sys.argv[1:] in (['build'],['check'])
    c=constants();covers=[cover(j,4-j) for j in (2,3,4)]
    assert sum(len(a['leaves']) for a in covers)==275
    assert sum(a['coefficient_count'] for a in covers)==26493
    out=dict(identity='ENDPOINT6_TWO_ANTIPODES_19_OVER60_V1',parent=PARENT,material=MATERIAL,constants=c,covers=covers,controls=controls(),scope='Every true convex seven-corner endpoint6 weak radial path misses at least one of -19*q0/60 and -19*q2/60. No global five-plus-one, 3D lift, or110 claim.',source_pin=pin(Path(__file__).read_bytes()))
    data=(json.dumps(enc(out),sort_keys=True,separators=(',',':'))+'\n').encode();path=HERE/'endpoint6_exact.json'
    if sys.argv[1]=='check':assert path.read_bytes()==data
    else:
        assert not path.exists() or path.read_bytes()==data
        path.write_bytes(data)
    print('ENDPOINT6_ALL_SHAPES_WEAK_WALLS_TWO_ANTIPODES_19_OVER60_PASS',*pin(data))
if __name__=='__main__':main()

```
