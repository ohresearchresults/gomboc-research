# figure-0334

AI research report · 2026-09-07 UTC

---

# VH06 constructive handoff: sequential support geometry, a whole-basin obstruction, and the remaining physical gate

## Acceptance status

No new homogeneous own-centred strict (1,1,0) polyhedron with E<500 is promoted in this handoff. The accepted strict (1,1,0) fallback remains FUSION258_PN03_C1374, not H88.

The usable exact starting object remains the lead’s COORD-H88-S1U2-R14: 172 vertices, 258 true edges, 88 maximal facets, actual own-centroid class (1,2,1), stable support 87 with cycle [15,20,154,158], unstable vertices [44,159], and saddle [44,88]. Its defining table, reconstruction and original independent acceptance are in the journal. 

In the earlier part of this assignment, the all-triples exact audit and an independently constructed clipped-body exact audit completed on H88 and agreed on their shared exact output. The observed markers were:

```text
EXACT_A_ALL_TRIPLES_BOUNDED_TRUE_FEATURES_MASS_CENSUS 172 258 88 [87] [44, 159] [[44, 88]] NO_DEGENERACY_NO_ZERO
EXACT_B_CLIPPED_BOUNDARY_APEX_GLOBAL_CONES 172 258 88 [87] [44, 159] [[44, 88]] NO_DEGENERACY
```

Those executions establish the parent only. Later certificate and successor-audit jobs were launched, but their terminal results were not visible in the retained record. They are not counted as passes. In particular, the H88 application of the obstruction below and the rationalized two-stage successor remain certificate candidates, not newly accepted computed objects. The general mathematical lemmas below have proofs independent of those unobserved executions.

### A literal-data discrepancy that must not propagate

The journal describes a 56-vertex minor basin but its printed list contains **54** entries:

```text
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,34,35,36,37,39,40,41,42,44,45,46,52,53,54,55,57,63,65,68,74,75,79,81,84]
```

I retain that literal list rather than inventing two missing vertices. Counting the list does not itself independently certify basin membership.

## 1. Main mathematical finding: an oblique compulsory core can block the whole basin

The lead’s sharp one-wave bound on the ray through vertex 44 does not control every point in its basin. The important new direction was to optimize the compulsory diameter-envelope over directions, rather than only at the current unstable vertex.

For a body K with an interior reference g, define

```text
D_g(K) = {z : B((g+z)/2, |z-g|/2) is contained in K}.
```

Consider a cut

```text
w·(x-g) <= t,     t>0,
```

whose perpendicular foot from g lies outside the SAME ORIGINAL K. Every such cut retains every point of D_g(K). Indeed, if it removed z, its foot p=g+t w/|w|² would satisfy

```text
|p-(g+z)/2|² - |z-g|²/4
    = t(t-w·(z-g))/|w|² < 0.
```

The foot would therefore lie inside the diameter ball and hence inside K, a contradiction. This applies simultaneously to any finite collection of one-wave cuts, however many facets they introduce.

### A quantitative, asymmetric two-compartment obstruction

Here is a general statement that does not require symmetry.

Suppose K outside a closed ball B(0,r) has two distinct components containing z_A and z_B. Suppose both diameter balls based at the parent centroid g are contained in K. Let L be a finite intersection of K with cuts of the preceding one-wave kind, and let h be the **actual ordinary-volume centroid of L**. If

```text
|g| < epsilon,
|h-g| <= delta,
min(|z_A|,|z_B|) > r + 2(delta+epsilon),
```

then L has at least two strict unstable vertices.

Proof: both points survive every cut. In each of the two compact compartment closures intersected with L, maximize |x-h|. The surviving point has distance greater than r+delta+epsilon, whereas every artificial compartment-boundary point on |x|=r has distance at most r+delta+epsilon. Thus each maximum occurs away from the artificial spherical boundary and is a local maximum on L itself. A local maximum of squared distance on a finite convex polyhedron is a vertex. Every incident edge derivative is strictly negative: a zero derivative would give a positive quadratic increase along that edge. These are two genuine strict vertex equilibria, not an Euler-identity inference.

This statement excludes only one-wave inward replacements with the stated centroid-displacement bound. It does not exclude sequential cuts, outward supporting-plane motion, large physical centroid relocation, or general E<500 constructions.

### H88 certificate candidate

The following simple rational points were found inside the numerical compulsory envelope:

```text
z_A = (-1080,1201,-306)/1000
z_B = (649,-1382,-78)/1000
```

Their squared norms are exactly

```text
|z_A|² = 2702437/1000000
|z_B|² = 2337209/1000000.
```

The numerical minimum of 2-q_i·z-|q_i||z| over the original H88 poles was approximately 0.0028393 for z_A and 0.0027711 for z_B. The oblique compulsory peak near the minor basin had radius approximately 1.6465243, substantially greater than the old saddle radius approximately 1.4802993. This is why the earlier retained-radius estimate about 1.4303 on the particular v44 ray did not settle the whole-basin question.

At raw-origin radius r=3/2, the numerical true-edge superlevel graph had two components of sizes 52 and 38. The first contained vertex 31 and the second vertex 159. The segments z_A--v31 and z_B--v159 stayed outside that sphere. A conservative exact certificate target is therefore

```text
r = 3/2,
delta = 7/500,
epsilon = 1/10^12,
min(|z_A|,|z_B|) > 15287/10000
                  > r+2(delta+epsilon).
```

The replay source below checks all these finite assertions exactly, including the diameter balls relative to the actual parent centroid. Its complete terminal acceptance was not observed here, so this particular H88 corollary is not promoted as an executed exact exclusion.

The connectivity certificate is not a mechanical-edge count. It checks the true-edge graph and a facet-fan triangulation graph and requires identical components. Added fan diagonals are used only to certify topology; they are never counted as true edges. The graph test is sufficient because each convex facet outside its intersection with the ball can be pushed to its polygon boundary, and radial expansion pushes K outside the ball to the boundary of K.

## 2. Constructive escape: the depth of support ancestry matters

The obstruction has a concrete escape, not just a negative conclusion.

For a nonzero pole p, let a new pole q satisfy

```text
q·p > |q|².
```

Its face foot at the origin is excluded by p. Equivalently q lies in the open diameter ball B(p/2,|p|/2).

For a chain of m such strict steps, starting at p and ending at q_m, the supremum of q_m·u for a unit direction u is

```text
|p| cos(theta/(m+1))^(m+1),
where theta = angle(p,u),  m>=1.
```

To prove the upper bound, write each permissible radial contraction as at most the cosine of the change of direction. Include the final angle to u as one more factor. The total angular length is at least theta. Concavity of log(cos t) on (-pi/2,pi/2) bounds the product by equal angular increments. The bound is approached by equally spaced directions on the shortest great-circle arc, with arbitrarily small strict radial shrinkage at every step.

For m=1 this recovers the diameter-ball formula. For m=2 it gives genuinely deeper support geometry: the second face foot may lie inside the original K while being excluded by the first added plane.

### A deterministic two-stage construction from H88

Use original pole p=q76, z=z_A, u=z/|z|, theta=angle(p,u), alpha=theta/3, and rho=9999/10000. Let c=cos(alpha), t=|p|/|z|. The two poles can be written without sine terms:

```text
q88 = rho * (2 c² p + t c z)/(4 c²-1)
q89 = rho² * (c² p + 2 t c³ z)/(4 c²-1).
```

Here c is the unique root in (1/2,1) of

```text
4 c³ - 3 c = (p·z)/(|p||z|).
```

This is a complete algebraic definition. The replay rounds each coordinate to the nearest multiple of 10^-14 using certified rational interval bounds, not a floating trigonometric implementation. It retains the original 88 inequalities and appends these two rows. Redundant supports are allowed and are removed only by exact maximal-facet reconstruction.

Before rounding, the strict ancestry margins are explicit:

```text
q88·p - |q88|² = rho(1-rho)|p|² c² > 0
q89·q88 - |q89|² = rho³(1-rho)|p|² c⁴ > 0.
```

The numerical poles were approximately

```text
q88 = (0.000117681894, 0.775562892, -0.0705723239)
q89 = (-0.25572916, 0.67218839, -0.10775590).
```

Numerically q88·z_A was about 0.9529191, while q89·z_A was about 1.1164591. The first cut retains z_A and the second removes it. The resulting retained radius on that ray is below 1.473, hence below the old saddle radius. The exact replay additionally checks that the second foot is strictly inside every original halfspace but outside the first cut, and that the original stable foot survives. Those are the relevant geometric escape assertions; they are not a claim of U/H cancellation.

## 3. What the ordinary mass actually did

The unrounded two-stage numerical body had 172 vertices, 258 true edges and 88 active facets despite 90 supplied supports; original rows 60 and 72 became inactive. At the old reference it had numerical class (1,5,4), with U=[16,34,45,64,159]. Its actual uniform-volume centroid was approximately

```text
(0.018127926848162307,
 -0.03184454002413518,
 0.005072309369254061),
```

and its volume was approximately 9.480401318115277. At that actual centroid the numerical census was (49,17,64), not (1,5,4). Thus the sequential construction crosses the old one-wave gate but does not solve the homogeneous problem.

Actual three-moment closure using the two leaf planes 71 and 74 was also reached numerically while keeping those poles inside their predecessor balls, with parents 55 and 52. That restored numerical own-centred S1 but produced a (1,10,9) body. The important failure was not an appointed-reference error: it was the creation of new ascent failures around the mass-control region. The floating control coordinates from that earlier run are not a retained exact checkpoint and are not promoted. A complete driver for regenerating this physical experiment is included below.

This agrees with the local differential but exposes its limitation. For an active plane q_f·x=1,

```text
dM = -B_f dq_f / |q_f|,
B_f = integral_F x x^T dA.
```

B_f is positive definite because a nonzero homogeneous linear form cannot vanish on an entire two-dimensional affine face whose plane avoids the origin. Therefore one physical plane can locally control all three first moments. That rank statement does not preserve neighboring vertex escapes, does not imply a finite continuation remains in the same mechanical chamber, and does not guarantee boundedness after large motion.

## 4. Complete literal parent and recovery capsule

Save the following as `H88_N.txt`. Each line gives the first three coefficients of one inequality. Append the common fourth coefficient H=100000000000000 to every line. There is no expansion, normalization or symmetry operation. The resulting four-column text, with single spaces and a final LF, has SHA-256

```text
9ddf27d342c879bdc2a5cdd88c36c7ebd13ce3c849cd13173c5404d467779e6e
```

```text
58734718601330 85932438876 -73357847443834
-30951373015295 -47371543402883 74429356219142
36637945932859 -10485543261238 -86813222434796
-56306875189713 -58487025850441 48892003913763
-58503941672577 15954413706085 -21408993266810
46033074104876 -5889643484230 -82279187074707
-44911253268739 -53670325113276 62980568230767
-35890242675634 20484354844486 -47122396362371
-40608093128026 -47609148494309 -75601447038224
-68898398791700 -65133996538414 -22765382897642
-33938091774053 -43696983730487 -80534919676490
-66998110258316 -63799004646373 -32336067059816
-16756736201636 -31929477632719 -89843834027639
-70345182255318 -66073623808601 1099901819523
20501719459451 -17253294059095 -91546068034555
-62952680640560 -60314221232157 38229412153418
62608221093895 2170732726999 -69819604353559
-25719602986679 -45007990410005 77536756407916
-62025351353698 5429046872558 12792389152988
31513143035353 -12856349080634 -88689701038073
-59685387105103 -59540259389409 43741185047860
-63771502443131 -61631227458054 -43298400495824
-48261011610582 -51973893635703 -68742158624830
3141962783177 -24657083903485 -92741772948390
-68271536365717 -63890132133959 20923737411836
54630734018748 -1979135892988 -76646165363148
-35899512765024 -49654762444758 70918493638536
26083637269387 -15039553233783 -90302434485983
50393739290196 -3910646958099 -79616274783884
-40546096810488 -51756235368294 67094975395182
9045908090134 -21627270532951 -92872274275716
-67236584785998 -62467561663096 26829572382366
-59522028690157 9612716548152 -23352849168843
-52793790768051 -57044632917640 53862948459421
41515638022835 -7906017368844 -84662242168279
-48982053058807 -55477492122995 58537676073021
72880008910495 8445586385120 -57603430736129
-13794062329272 -32313194011829 85500584626464
14815945512579 -19523742514071 -92391495043900
-66227559214852 -60555218717987 32456425919891
66261272829583 4276449213903 -66016607750759
-20242411448487 -42512366263689 80240700474020
-22012873339540 -36140194483178 -87367074196091
-70375955109847 -66165996660569 -6417167277811
-9772309578264 -29862138297033 -91268089319252
-69935177555383 -65656209448821 8058742387634
-27751566602978 -39955241274409 -84343033742244
-69940981276725 -65870628595680 -14232939081233
-14535518762273 -39829020918002 82540511489096
69685052986454 6323407023504 -61956844224547
-12638644748459 -24806337206039 87788142413678
-51816182725492 28521343300152 -20838325437392
75772102399174 10407542530535 -53091210534913
-3367638564381 -41343645870834 82236378220877
77675578592323 14434998102489 -48876730284550
8193077533435 -41817754430672 80819069672210
80535544233389 22358781426967 -39573359497052
-69215154573949 -64918699786306 14704126944223
-3136917843240 -27420255714801 -92219854332695
-10952407394463 -17387019219829 89436991466607
-37103857154874 45245030276000 -5497520161726
79300782712792 18381707760691 -44333248467722
81291134742349 31137983135119 -29771057774250
-16291125400123 5284187509281 88608884767013
-43441112604630 39568181291288 -15553504770938
80759292776702 35795698742002 -24775113428560
-12935692484177 -7073055766612 89962720228739
81408647148309 26308721037169 -34501183611347
-7339721739339 296123186309 90392959501164
80804059518118 38890492553081 -17816745203971
57516943846916 50800950570629 -39369019031582
20090342637501 -39357373200232 79019694556241
7528690444806 64795055718697 -29327411310896
-4101364074471 42767908423304 55256743081336
80697896003630 -3072874573177 -42847269736439
-53948133795590 27236278993940 32437854006825
29350447886727 78041818179643 -1758476672550
-30867506337536 42269488725597 63256688148134
80423243682438 41486200352118 -10424753287570
74227401466973 50822728557255 -1668054672123
6123033161865 -18147968837655 88093380178630
85124662439044 21971835516768 -25999741573709
-17787584807055 18812645494477 85313698078441
66252378590977 58801868006020 6903637223392
49214947281171 70742325495033 5842536201050
-5675136891321 50691300990348 -43904573745541
-19962104158376 38788721140812 -46623112720988
-57735026919000 -57735026919000 -57735026919000
```

### Exact moments and canonical feature convention

Vertices are all feasible three-plane intersections, deduplicated and sorted by their actual rational Cartesian coordinates. A maximal face is the exact planar hull of the complete equality set on an active input support, oriented outward and rotated to its least vertex index. Facets are ordered by input-row index. Consecutive polygon pairs, deduplicated, are the true edges.

For outward polygon fans, put

```text
W = sum det(a,b,c)
M = sum det(a,b,c) (a+b+c).
```

Then the exact ordinary volume is W/6, the three raw first moments are M/24, and the exact centroid is M/(4W). These finite rational sums, with the full literal defining data and complete reconstruction below, specify the mass fractions without decimal substitution. The centred solid is K-M/(4W), and all three of its first moments are exactly zero.

The parent volume is in (9717046300886,9717046300887)/10^12. Its raw centroid coordinates are respectively in (-2184,-2183)/10^18, (732,733)/10^18 and (209,210)/10^18. The parent incidence hash for compact sorted-key JSON containing only faces and edges is

```text
bdf8de8bb95697c26de7820e1a4d81a2c5d1f5050d480565cb7d49fa30189c12
```

### Complete exact replay source

Save the following as `replay.py`. It uses Python 3.11+ and the standard library only. It is a newly supplied single-program replay, with internal local/global mechanical cross-checks; running it twice is **not** two independent audits. Its successful completion was not observed in the retained continuation, and it must not be represented as an already executed acceptance.

It writes every rational coordinate, every maximal facet and true edge, the exact raw volume and first moments, the exact centroid, and the complete feature census. It also reconstructs the two new support rows by certified algebraic rounding. Inactive input planes are not counted as facets.

```python
from fractions import Fraction as F
from itertools import combinations
from math import lcm, isqrt
from pathlib import Path
import hashlib, json, sys
sys.set_int_max_str_digits(0)
assert __debug__
H0 = 10**14
PARENT_SHA = '9ddf27d342c879bdc2a5cdd88c36c7ebd13ce3c849cd13173c5404d467779e6e'
INC_SHA = 'bdf8de8bb95697c26de7820e1a4d81a2c5d1f5050d480565cb7d49fa30189c12'

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(t,a): return tuple(t*x for x in a)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def canonical(rows):
    return chr(10).join(' '.join(map(str,r)) for r in rows)+chr(10)
def sha(text): return hashlib.sha256(text.encode()).hexdigest()
def read_rows(path):
    rows=[]
    for line in Path(path).read_text().splitlines():
        if not line.strip(): continue
        r=list(map(int,line.split()))
        if len(r)==3: r.append(H0)
        assert len(r)==4 and r[3]>0 and any(r[:3])
        rows.append(r)
    return rows

def reachable(adj,start):
    seen={start}; todo=[start]
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen: seen.add(v); todo.append(v)
    return seen

def polygon(X,ids,n):
    drop=max(range(3),key=lambda k:abs(n[k]))
    axes=[k for k in range(3) if k!=drop]
    def xy(i): return (X[i][axes[0]],X[i][axes[1]])
    def turn(a,b,c):
        a,b,c=xy(a),xy(b),xy(c)
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    order=sorted(ids,key=xy)
    lo=[]; hi=[]
    for i in order:
        while len(lo)>1 and turn(lo[-2],lo[-1],i)<=0: lo.pop()
        lo.append(i)
    for i in reversed(order):
        while len(hi)>1 and turn(hi[-2],hi[-1],i)<=0: hi.pop()
        hi.append(i)
    co=lo[:-1]+hi[:-1]
    if len(co)<3: return []
    if dot(n,cross(sub(X[co[1]],X[co[0]]),sub(X[co[2]],X[co[0]])))<0:
        co.reverse()
    k=co.index(min(co)); return co[k:]+co[:k]

def build(rows):
    pts=set()
    for i,j,k in combinations(range(len(rows)),3):
        ni,nj,nk=[rows[t][:3] for t in (i,j,k)]
        d=det(ni,nj,nk)
        if not d: continue
        p=add(add(scale(rows[i][3],cross(nj,nk)),scale(rows[j][3],cross(nk,ni))),scale(rows[k][3],cross(ni,nj)))
        if d<0: d=-d; p=scale(-1,p)
        if all(dot(r[:3],p)<=r[3]*d for r in rows):
            pts.add(tuple(F(t,d) for t in p))
    X=sorted(pts); assert len(X)>=4
    faces=[]; edges={}; area_sum=(F(0),)*3
    for f,r in enumerate(rows):
        ids=[i for i,x in enumerate(X) if dot(r[:3],x)==r[3]]
        if len(ids)<3: continue
        co=polygon(X,ids,r[:3])
        if not co: continue
        assert set(co)==set(ids)
        area=(F(0),)*3
        for a,b in zip(co,co[1:]+co[:1]):
            e=sub(X[b],X[a])
            assert all(dot(r[:3],cross(e,sub(X[c],X[a])))>0 for c in co if c not in (a,b))
            area=add(area,cross(X[a],X[b]))
            edges.setdefault(tuple(sorted((a,b))),[]).append((f,a,b))
        axis=next(k for k in range(3) if r[k])
        factor=area[axis]/r[axis]
        assert factor>0 and area==scale(factor,r[:3])
        area_sum=add(area_sum,area); faces.append((f,co))
    assert area_sum==(0,0,0)
    assert all(len(u)==2 and u[0][1:]==u[1][1:][::-1] for u in edges.values())
    assert len(X)-len(edges)+len(faces)==2
    adj={i:set() for i in range(len(X))}
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    assert reachable(adj,0)==set(adj)
    for v in range(len(X)):
        link={}; incident=[]
        for f,co in faces:
            if v not in co: continue
            incident.append(f); k=co.index(v); a=co[k-1]; b=co[(k+1)%len(co)]
            link.setdefault(a,set()).add(b); link.setdefault(b,set()).add(a)
        assert link and all(len(a)==2 for a in link.values())
        assert reachable(link,min(link))==set(link)
        assert any(det(rows[i][:3],rows[j][:3],rows[k][:3]) for i,j,k in combinations(incident,3))
    # Positive area-normal dependence and rank three prove boundedness.
    W=F(0); M=[F(0)]*3; avsum=(F(0),)*3
    C=[[F(0) for j in range(3)] for i in range(3)]
    for f,co in faces:
        for k in range(1,len(co)-1):
            a,b,c=[X[t] for t in (co[0],co[k],co[k+1])]
            w=det(a,b,c); assert w>0
            s=add(add(a,b),c); av=add(add(cross(a,b),cross(b,c)),cross(c,a))
            W+=w; avsum=add(avsum,av)
            for i in range(3):
                M[i]+=w*s[i]
                for j in range(3): C[i][j]+=s[i]*av[j]
    assert W>0 and avsum==(0,0,0)
    assert C==[[W if i==j else 0 for j in range(3)] for i in range(3)]
    g=tuple(t/(4*W) for t in M)
    # These identities check the expanded translated determinant polynomial.
    assert all(M[i]-4*W*g[i]==0 for i in range(3))
    return X,faces,edges,W,tuple(M),g

def hp(v):
    v=tuple(map(F,v)); d=lcm(*(x.denominator for x in v))
    return tuple(x.numerator*(d//x.denominator) for x in v),d

def foot(row,G,D):
    n=row[:3]; nn=dot(n,n); hc=row[3]*D-dot(n,G)
    assert hc>0
    return add(scale(nn,G),scale(hc,n)),D*nn

def census(rows,X,faces,edges,g):
    P=[hp(v) for v in X]; G,D=hp(g)
    A=[tuple(D*p[k]-d*G[k] for k in range(3)) for p,d in P]
    adj={i:set() for i in range(len(X))}
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    S=[]; U=[]; HH=[]; deg=[]; zeros=0
    for f,co in faces:
        n=rows[f][:3]; fp,fd=foot(rows[f],G,D); sides=[]
        for i,j in zip(co,co[1:]+co[:1]):
            pa,da=P[i]; pb,db=P[j]
            e=sub(scale(da,pb),scale(db,pa)); w=sub(scale(da,fp),scale(fd,pa))
            sides.append(dot(n,cross(e,w)))
        other=[r[3]*fd-dot(r[:3],fp) for j,r in enumerate(rows) if j!=f]
        assert (min(sides)>0)==(min(other)>0)
        assert (min(sides)>=0)==(min(other)>=0)
        zeros+=sum(t==0 for t in sides)
        if min(sides)>0: S.append(f)
        elif min(sides)>=0: deg.append(['face',f])
    for i,(pa,da) in enumerate(P):
        vals={j:dot(A[i],sub(scale(da,pb),scale(db,pa))) for j,(pb,db) in enumerate(P) if j!=i}
        local=[vals[j] for j in adj[i]]
        assert (max(vals.values())<0)==(max(local)<0)
        assert (max(vals.values())<=0)==(max(local)<=0)
        zeros+=sum(t==0 for t in local)
        if max(vals.values())<0: U.append(i)
        elif max(vals.values())<=0: deg.append(['vertex',i])
    for (i,j),uses in sorted(edges.items()):
        pa,da=P[i]; pb,db=P[j]
        e=sub(scale(da,pb),scale(db,pa)); ee=dot(e,e); ae=dot(A[i],e)
        tn=-ae*db; td=D*ee; z=sub(scale(ee,A[i]),scale(ae,e))
        n,m=[rows[u[0]][:3] for u in uses]
        assert dot(n,n)*dot(m,m)-dot(n,m)**2>0
        ga=dot(z,n)*dot(m,m)-dot(z,m)*dot(n,m)
        gb=dot(z,m)*dot(n,n)-dot(z,n)*dot(n,m)
        vals=[dot(z,sub(scale(da,pc),scale(dc,pa))) for k,(pc,dc) in enumerate(P) if k not in (i,j)]
        strong=0<tn<td and ga>0 and gb>0
        weak=0<=tn<=td and ga>=0 and gb>=0
        assert strong==(0<tn<td and max(vals)<0)
        assert weak==(0<=tn<=td and max(vals)<=0)
        zeros+=sum(t==0 for t in (tn,td-tn,ga,gb))
        if strong: HH.append([i,j])
        elif weak: deg.append(['edge',i,j])
    return dict(S=S,U=U,H=HH,degeneracies=deg,ordinary_zeros=zeros)

def audit(rows):
    X,faces,edges,W,M,g=build(rows)
    d=census(rows,X,faces,edges,g)
    d.update(V=len(X),E=len(edges),F=len(faces),rows=rows,
             vertices=[[str(t) for t in v] for v in X],
             face_rows=[f for f,co in faces],faces=[co for f,co in faces],
             edges=[list(e) for e in sorted(edges)],volume=str(W/6),
             first_moments=[str(t/24) for t in M],centroid=[str(t) for t in g],
             centred_first_moments=['0','0','0'],source_sha256=sha(canonical(rows)))
    inc=dict(faces=d['faces'],edges=d['edges'])
    d['incidence_sha256']=sha(json.dumps(inc,sort_keys=True,separators=(',',':')))
    return d,(X,faces,edges,g)

# Rational interval operations for certified algebraic rounding.
def ip(a,b): return (a[0]+b[0],a[1]+b[1])
def im(a,b):
    v=[x*y for x in a for y in b]; return min(v),max(v)
def isc(t,a): return im((t,t),a)
def inv(a):
    assert a[0]>0; return 1/a[1],1/a[0]
def idiv(a,b): return im(a,inv(b))
def sqrt_bounds(x,bits):
    k=isqrt((x.numerator << (2*bits))//x.denominator)
    return F(k,1<<bits),F(k+1,1<<bits)
def cos_third_bounds(gamma,bits):
    assert -1<=gamma<=1
    lo=F(1,2); hi=F(1)
    for k in range(bits):
        m=(lo+hi)/2
        if 4*m*m*m-3*m<gamma: lo=m
        else: hi=m
    return lo,hi

def two_cuts(rows):
    p=tuple(F(x,rows[76][3]) for x in rows[76][:3])
    z=tuple(F(x,1000) for x in (-1080,1201,-306))
    P=dot(p,p); Z=dot(z,z); C=dot(p,z); rho=F(9999,10000)
    assert C>0
    for bits in (32,64,128,256,512):
        t=sqrt_bounds(P/Z,bits)
        gam=(C/(t[1]*Z),C/(t[0]*Z))
        c=(cos_third_bounds(gam[0],bits)[0],cos_third_bounds(gam[1],bits)[1])
        c2=im(c,c); c3=im(c2,c); den=ip(isc(4,c2),(-F(1),-F(1)))
        intervals=[]
        for stage in (1,2):
            for k in range(3):
                if stage==1:
                    num=isc(rho,ip(isc(2*p[k],c2),isc(z[k],im(t,c))))
                else:
                    num=isc(rho*rho,ip(isc(p[k],c2),isc(2*z[k],im(t,c3))))
                intervals.append(idiv(num,den))
        integers=[]
        for lo,hi in intervals:
            a=H0*lo+F(1,2); b=H0*hi+F(1,2)
            na=a.numerator//a.denominator; nb=b.numerator//b.denominator
            if na!=nb or not (F(na)-F(1,2)<H0*lo and H0*hi<F(na)+F(1,2)): break
            integers.append(na)
        if len(integers)==6:
            return [integers[:3]+[H0],integers[3:]+[H0]]
    raise ArithmeticError('rounding not isolated; increase interval precision')

def minnorm(a,b):
    e=sub(b,a); ee=dot(e,e)
    if not ee: return dot(a,a)
    t=-dot(a,e)/ee; t=max(F(0),min(F(1),t))
    w=add(a,scale(t,e)); return dot(w,w)

def obstruction(rows,state):
    X,faces,edges,g=state; G,D=hp(g)
    eps=F(1,10**12); delta=F(7,500); r=F(3,2)
    assert dot(G,G)*10**24<D*D
    zz=[tuple(F(x,1000) for x in v) for v in [(-1080,1201,-306),(649,-1382,-78)]]
    for z in zz:
        p,d=hp(z); diff=sub(scale(D,p),scale(d,G)); summ=add(scale(D,p),scale(d,G))
        for row in rows:
            n=row[:3]; a=2*row[3]*d*D-dot(n,summ)
            assert a>0 and a*a>dot(n,n)*dot(diff,diff)
        assert dot(z,z)>F(15287,10000)**2
    assert F(15287,10000)>r+2*(delta+eps)
    all_edges=set(edges)
    for f,co in faces:
        for k in range(1,len(co)-1):
            for a,b in combinations((co[0],co[k],co[k+1]),2): all_edges.add(tuple(sorted((a,b))))
    def comps(ee):
        out={i for i,x in enumerate(X) if dot(x,x)>r*r}
        assert all(dot(x,x)!=r*r for x in X)
        adj={i:set() for i in out}
        for a,b in ee:
            m=minnorm(X[a],X[b]); assert m!=r*r
            if m>r*r: adj[a].add(b); adj[b].add(a)
        ans=[]
        while out:
            c=reachable(adj,min(out)); ans.append(sorted(c)); out-=c
        return ans
    c=comps(all_edges); assert c==comps(edges) and len(c)==2
    assert [len(a) for a in c]==[52,38]
    assert any(31 in a and 159 not in a for a in c)
    assert minnorm(zz[0],X[31])>r*r and minnorm(zz[1],X[159])>r*r
    return dict(radius=str(r),delta=str(delta),epsilon=str(eps),components=c,
                true_edges=len(edges),topological_graph_edges=len(all_edges),
                status='EXACT_ONE_WAVE_CERTIFICATE_PASS')

def escape_checks(rows,newrows,state):
    X,faces,edges,g=state; G,D=hp(g); a,b=newrows
    assert dot(a[:3],rows[76][:3])>dot(a[:3],a[:3])
    assert dot(b[:3],a[:3])>dot(b[:3],b[:3])
    p,d=foot(a,G,D)
    assert dot(rows[76][:3],p)>rows[76][3]*d
    p,d=foot(b,G,D)
    assert all(dot(r[:3],p)<r[3]*d for r in rows)
    assert dot(a[:3],p)>a[3]*d
    p,d=foot(rows[87],G,D)
    assert all(dot(r[:3],p)<r[3]*d for r in newrows)
    z=(-1080,1201,-306)
    assert dot(a[:3],z)<a[3]*1000 and dot(b[:3],z)>b[3]*1000
    qz=F(dot(b[:3],z),b[3]*1000)
    assert F(dot(z,z),1000**2)<F(1473,1000)**2*qz*qz

def write_json(path,obj):
    Path(path).write_text(json.dumps(obj,sort_keys=True,indent=2))

def main():
    if len(sys.argv)==4 and sys.argv[1]=='verify':
        d,state=audit(read_rows(sys.argv[2])); write_json(sys.argv[3],d)
        print(d['V'],d['E'],d['F'],d['S'],d['U'],d['H'],d['degeneracies'],d['ordinary_zeros'])
        return
    if len(sys.argv)!=3:
        raise SystemExit('usage: replay.py H88_N.txt OUTPUT_DIR; or replay.py verify ROWS.txt OUTPUT.json')
    rows=read_rows(sys.argv[1]); out=Path(sys.argv[2]); out.mkdir(parents=True,exist_ok=True)
    assert len(rows)==88 and sha(canonical(rows))==PARENT_SHA
    d,state=audit(rows); write_json(out/'parent.json',d)
    assert (d['V'],d['E'],d['F'],d['S'],d['U'],d['H'])==(172,258,88,[87],[44,159],[[44,88]])
    assert not d['degeneracies'] and d['ordinary_zeros']==0 and d['incidence_sha256']==INC_SHA
    assert next(co for f,co in state[1] if f==87)==[15,20,154,158]
    assert F(9717046300886,10**12)<F(d['volume'])<F(9717046300887,10**12)
    for x,(lo,hi) in zip(state[3],[(-2184,-2183),(732,733),(209,210)]):
        assert F(lo,10**18)<x<F(hi,10**18)
    cuts=two_cuts(rows); full=rows+cuts
    (out/'TWO_STAGE_90.txt').write_text(canonical(full))
    escape_checks(rows,cuts,state)
    e,newstate=audit(full); write_json(out/'two_stage_own_centroid.json',e)
    old_reference=census(full,newstate[0],newstate[1],newstate[2],state[3])
    write_json(out/'two_stage_old_reference.json',old_reference)
    proof=obstruction(rows,state); write_json(out/'one_wave_certificate.json',proof)
    print('NEW_ROWS',cuts,'NEW_ROWS_SHA256',sha(canonical(full)))
    print('ACTUAL_CENSUS',e['V'],e['E'],e['F'],e['S'],e['U'],e['H'],e['degeneracies'],e['ordinary_zeros'])
    print('OLD_REFERENCE_CENSUS',old_reference)
    print('EXACT_SINGLE_PROGRAM_REPLAY_FINISHED')

if __name__=='__main__': main()
```

Reconstruction and verification commands:

```sh
python -S replay.py H88_N.txt out
python -S replay.py verify out/TWO_STAGE_90.txt out/two_stage_repeated.json
```

The second command is a repeat of the same implementation, not an independent audit. Any eventual promoted successor still needs a separately authored complete exact verification, for example independent cube clipping, different tetrahedral integration, and independently implemented all-feature mechanics.

### Complete physical mass-clamp driver

Save this as `clamp.py` beside `replay.py`. The earlier numerical environment used NumPy 2.3.5 and SciPy 1.17.0. This driver is exploratory: it writes literal rounded supports, and those supports must subsequently be audited at their recomputed exact centroid. It does not declare a winner from an optimizer status or a small centroid residual.

```python
from pathlib import Path
import sys
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
from replay import read_rows, two_cuts, canonical, sha, H0

rows=read_rows(sys.argv[1]); rows=rows+two_cuts(rows)
q=np.array([np.array(r[:3],float)/r[3] for r in rows])
ids=np.array([71,74]); parents=np.array([55,52]); old=q[ids].copy()
cache=[None,None]

def geometry(qq):
    hull=ConvexHull(qq)
    if max(hull.equations[:,3])>=0: raise ValueError('unbounded physical intersection')
    tri=hull.simplices
    v=np.linalg.solve(qq[tri],np.ones((len(tri),3,1)))[:,:,0]
    W=0.0; M=np.zeros(3); f1=np.zeros_like(qq); f2=np.zeros((len(qq),3,3))
    for i in sorted(hull.vertices.tolist()):
        js=np.where((tri==i).any(axis=1))[0]; points=v[js]; centre=points.mean(axis=0)
        n=qq[i]/np.linalg.norm(qq[i]); axis=np.eye(3)[np.argmin(abs(n))]
        e1=np.cross(axis,n); e1/=np.linalg.norm(e1); e2=np.cross(n,e1)
        co=js[np.argsort(np.arctan2((points-centre)@e2,(points-centre)@e1))]
        for j in range(1,len(co)-1):
            a,b,c=v[[co[0],co[j],co[j+1]]]; s=a+b+c
            w=a@np.cross(b,c); W+=w; M+=w*s
            area=np.linalg.norm(np.cross(b-a,c-a))/2
            f1[i]+=area*s/3
            f2[i]+=area*(np.outer(s,s)+np.outer(a,a)+np.outer(b,b)+np.outer(c,c))/12
    if W<=0: raise ValueError('nonpositive volume')
    volume=W/6; centre=M/(4*W); J=np.zeros((3,len(qq),3))
    for i in range(len(qq)):
        J[:,i,:]=(-f2[i]+np.outer(centre,f1[i]))/(volume*np.linalg.norm(qq[i]))
    return centre,J

def state(x):
    if cache[0] is None or not np.array_equal(x,cache[0]):
        qq=q.copy(); qq[ids]=x.reshape(2,3)
        cache[:]=[x.copy(),geometry(qq)]
    return cache[1]
def eq(x): return state(x)[0]
def eqjac(x): return state(x)[1][:,ids,:].reshape(3,6)
def ball(x):
    a=x.reshape(2,3)
    return np.einsum('ij,ij->i',a,q[parents])-np.einsum('ij,ij->i',a,a)-1e-10
def balljac(x):
    a=x.reshape(2,3); J=np.zeros((2,6))
    J[0,:3]=q[parents[0]]-2*a[0]; J[1,3:]=q[parents[1]]-2*a[1]
    return J

result=minimize(lambda x:0.5*np.sum((x-old.ravel())**2),old.ravel(),
    jac=lambda x:x-old.ravel(),method='SLSQP',
    constraints=[dict(type='eq',fun=eq,jac=eqjac),dict(type='ineq',fun=ball,jac=balljac)],
    options=dict(ftol=1e-15,maxiter=200))
centre=eq(result.x); reserves=ball(result.x)
print('NUMERICAL_ONLY',result.success,result.message,centre,reserves)
if np.linalg.norm(centre)>=1e-12 or min(reserves)<-1e-12:
    raise RuntimeError('physical mass/leaf constraints not closed')
for j,i in enumerate(ids):
    rows[int(i)]=[int(round(H0*t)) for t in result.x.reshape(2,3)[j]]+[H0]
text=canonical(rows); Path(sys.argv[2]).write_text(text)
print('CONTROL_ROWS',rows[71],rows[74])
print('CANDIDATE_SHA256',sha(text))
```

Commands:

```sh
python clamp.py H88_N.txt BALANCED_90.txt
python -S replay.py verify BALANCED_90.txt balanced_exact.json
```

The literal parent, exact algebraic two-stage definition, all parameters, rational rounding procedure, geometry reconstruction, mass formulas and full single-program census are present above. Neither optimizer state nor a surviving sandbox file is needed to reconstruct these candidate experiments.

## 5. Most useful continuation

The next consequential step is to obtain an observed completion of the supplied certificate and candidate audits, without retrospectively treating the launched jobs as passes. If the H88 obstruction certificate passes, it rules out an entire small-centroid-displacement one-wave search family, not merely a finite direction screen. The two-stage support construction already identifies the precise way to leave that family: a later foot must be inside the original body and excluded by an earlier new support.

The constructive problem after that is genuinely joint. The minor-basin replacement and the incident stars of physical mass-control facets 71 and 74 must be allowed to change together. Preserving the polar S1 forest and solving three actual moments is insufficient; ascent routes in the compensating region must also be repaired, with additional normals and transient U/H pairs allowed. The original basin and the compensator region should not be optimized as independent local charts. No fixed-normal-pool, affine, or global E<500 impossibility claim follows from the finite failures recorded here.

The durable outcome is therefore a proved support-ancestry depth law, a proved general whole-basin one-wave obstruction, a concrete rational-certificate target for H88, and a complete deterministic sequential support escape whose physical-centroid failure is exposed rather than hidden. It is not an accepted new polyhedral Gömböc.
