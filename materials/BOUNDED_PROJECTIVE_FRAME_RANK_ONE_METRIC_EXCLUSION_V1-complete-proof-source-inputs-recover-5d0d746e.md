# material-5d0d746e2df5

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# BOUNDED_PROJECTIVE_FRAME_RANK_ONE_METRIC_EXCLUSION_V1

Coordinator theorem and exact computation. This single recovery capsule contains the complete proof, all literal inputs, full standalone source, reconstruction commands and output pins. It is not a new110 construction and does not exclude all metrics on any full projective star. It removes a uniform neighborhood of RANK-ONE metrics in seven full bounded projective-frame domains. Rank-two metric degeneration remains open. Accepted minimum interval34..622 is unchanged.

## 1. General two-sided metric lemma

Let K be any full-dimensional convex polytope containing0 in its interior, with genuine vertices x_i. Assume r B_2 is contained in K and |x_i|<=R for all i. Let one symmetric positive definite mechanical metric M have eigenvalues lambda1>=lambda2>=lambda3>0. If

    lambda2 R^2 < lambda1 r^2,                                  (1)

then at least two vertices are STRICT unstable equilibria relative to0 under M. Uniform density is not needed for this lemma; it enters the own-centroid bound in Section2.

Proof. Choose a unit eigenvector a of M for lambda1. Since K contains the r-ball, it has vertices with a.x>=r and with a.x<=-r. In each closed half a.x>=0 and a.x<=0, choose a vertex maximizing q(x)=x^T M x among the vertices of that half. Each selected value is at least lambda1 r^2. A vertex on the separating plane has q<=lambda2 R^2, so both selected vertices lie strictly on their respective sides and are distinct.

Fix either selected vertex x. For any other vertex y in the same closed half, q(y)<=q(x), and

    x^T M(y-x)=[q(y)-q(x)-(y-x)^T M(y-x)]/2<0.

For a vertex y in the opposite open half, the principal-axis contribution to x^T M y is nonpositive. On the perpendicular two-dimensional subspace the operator norm of M is lambda2, so x^T M y<=lambda2 R^2<q(x). Again x^T M(y-x)<0. Thus ALL outgoing primitives from x to any other vertex are strictly negative, in particular every genuine incident-edge primitive. Both selected vertices are strict unstable points. No assumption of a unique quadratic maximum, generic eigenvector, nonzero edge height, or strict ordering among same-side vertices was used. Ties are harmless because the positive definite distance term is strictly positive.

A slightly sharper pointwise version replaces r^2 by min(h_plus^2,h_minus^2), where h_plus=max_i a.x_i and h_minus=-min_i a.x_i, and R^2 by a valid bound on products of transverse vertex lengths. The uniform version(1) is sufficient below.

## 2. Uniform own-centroid radius in a bounded frame

Suppose a uniformly volume-filled3-body K contains the standard tetrahedron Delta=conv(0,e1,e2,e3) and is contained in the rectangular box product_k[0,L_k]. Let g be its ACTUAL volume centroid. Then

    (1/(4 sqrt(3))) B_2 is contained in K-g,
    |x-g|^2 <= L_1^2+L_2^2+L_3^2 for every x in K.              (2)

The outer inequality follows because g and x both belong to the box. For the inner inequality, first recall the actual uniform centroid support bound: if a3-polytope has support projections m<=a.x<=h and centroid projection0, then h<=-3m and -m<=3h. A direct proof takes a tetrahedral fan from a vertex of minimum projection m. Every tetrahedron has the other three vertices at projection at most h, so its centroid projection is at most(m+3h)/4. Averaging the tetrahedra with their true positive volume weights gives0<=(m+3h)/4. Reversing a gives the other inequality. The result holds for arbitrary support directions, not merely facets. Therefore each support distance from the centroid is at least one quarter of the total width.

For a unit vector a, the projections of the standard tetrahedron are0,a1,a2,a3. Their interval has width w with |a_k|<=w, hence1=sum a_k^2<=3w^2. Every width of K is at least1/sqrt(3). Its support distances from g are thus at least1/(4sqrt(3)), proving(2). This also proves the statement for limits of the bounded full-dimensional bodies by the same convex support argument; it does not transport the centroid through a projectivity.

Combining(1) and(2), a body in this frame with exactly one strict unstable equilibrium necessarily satisfies

    lambda2/lambda1 >= 1/[48(L_1^2+L_2^2+L_3^2)].                (3)

The nonstrict inequality is intentional: the proof excludes ratios STRICTLY below the threshold, not the equality case. If lambda1 is normalized to1, lambda2 is uniformly bounded away from0. There is NO lower bound on lambda3 here, so(3) does not compactify the entire positive definite metric cone or exclude rank-two limits. Eigenvalue ratios refer to M in THIS physical affine frame; they are not invariant under an arbitrary congruence and cannot be copied to a different raw metric chart.

## 3. Full simple-vertex radial stars of the literal bevel body

The exact body B below is the literal10/17/9 body from accepted complete result minimum-0122, SHA-256 a57548bf7f7db6cdd82467ad12462e1f201c78a3b343270a89caa20f94b4229b. Its seven simple vertices are0,2,4,5,6,7,8. This capsule carries its complete coordinates and maximal facets, so the new computation imports no code or data file from that parent. The parent's C9 all-SPD theorem is a separate result; it is not assumed in the metric lemma.

At a simple vertex s, let W have as columns its three true edge vectors, ordered with positive determinant. Put r_i=W^-1(X_i-X_s) and b=-W^-1 X_s. For this body, every r_i is coordinatewise nonnegative and b is strictly positive. For ANY parameter a in the entire orthant R_+^3, set

    lambda=1/(1+b.a), p=lambda W^-T a, D_a=diag(1+a_k),
    Phi_i=D_a r_i/(1+a.r_i).                                   (4)

These are genuine affine-normalized uniformly refilled projective shapes. In detail, l_i=1+p.X_i=lambda(1+a.r_i), A_s=I+X_s p^T, and

    A_s T_p X_i-X_s=(X_i-X_s)/l_i.

Apply the affine map with linear part lambda D_a W^-1 to get(4). For finite a all denominators and lambda are positive, so this is an invertible affine map of T_p B. The true face lattice is preserved. Uniform density is transformed by a constant determinant under this final affine map, so its centroid is the actual centroid of the new body, not a falsely transported projective mass.

Conversely, these a cover the FULL radial-star domain

    R_s={p in D: p.(X_i-X_s)>=0 for every i},

because a_k=(p.edge_k)/(1+p.X_s)>=0 and the displayed inverse identities hold. The four frame vertices are0,e1,e2,e3. For each coordinate,

    0<=Phi_ik<=max(1,r_ik)<=L_k,
    L_k=max_i max(1,r_ik).                                     (5)

If r_ik<=1, the numerator(1+a_k)r_ik is at most1+a_k r_ik, which is at most the denominator. If r_ik>=1, the denominator is at least1+a_k r_ik>=1+a_k, proving the other bound. Thus all parameters, including sequences escaping arbitrarily far in the orthant, share the same contained standard tetrahedron and outer box. The actual own-centroid estimate(2) is uniform over the ENTIRE star, not just a bounded parameter cell. Different escape rates can give different limiting bodies; a unique continuous cube compactification is not asserted.

The exact values from the source are:

|s|ordered neighbors|L|sum L_k^2|necessary lambda2/lambda1 for U1|
|--|--|--|--|--|
|0|2,1,5|(12,27/7,1)|7834/49|49/376032|
|2|3,0,7|(27/7,16,1)|13322/49|49/639456|
|4|1,3,9|(3/2,2,1)|29/4|1/348|
|5|0,6,7|(1,27/7,12)|7834/49|49/376032|
|6|5,1,9|(40/21,1,1)|2482/441|147/39712|
|7|2,5,8|(1,16,27/7)|13322/49|49/639456|
|8|3,7,9|(1,10/7,1)|198/49|49/9504|

In particular the single threshold49/639456 works simultaneously in all seven normalized stars. For a putative U1 realization in any one of them, scale that frame's metric to lambda1=1 and retain lambda2>=49/639456. The closure of this remaining normalized set includes only full-rank and rank-two positive semidefinite matrices, never rank one. This is a useful reduction of the unresolved metric boundary, NOT an all-SPD exclusion of the seven stars.

## 4. Exact computation and recovery

The source below constructs the genuine facets from their exact support equations, verifies that each listed face is exactly the support equality set, constructs true edges by facet intersections, verifies Euler and all simple-vertex tangent frames, and computes the complete r_i,b,L and thresholds. It is not a mechanical U1 search and does not numerically sample a continuous parameter. The continuous statements are proved in Sections1-3.

Save the entire Python code fence below as metric_thin.py, including its final newline. Equivalently, save this material as capsule.md and extract with:

    python -c "from pathlib import Path; s=Path('capsule.md').read_text(); Path('metric_thin.py').write_text(s.split('```python\n',1)[1].split('\n```',1)[0]+'\n')"

The exact dependency environment used was CPython3.13.5, standard library only, assertions enabled, no RNG, no network, no non-default parameters. In an empty directory run:

    python metric_thin.py build > metric_thin_build.txt
    python metric_thin.py check > metric_thin_check.txt
    cmp metric_thin_build.txt metric_thin_check.txt
    sha256sum metric_thin.py metric_thin.json metric_thin_build.txt metric_thin_check.txt

Expected pins:
- metric_thin.py:3825 UTF-8 bytes, SHA-25636999a09c32e4353798aafb91a10535595b321effd570f98b1e2135a879b4c68.
- metric_thin.json:3094 bytes, SHA-256dd1c2dddf464e8237b97450b4dd335868de3260f01905c0fc8c9b55e05f52121.
- Each stdout file:185 bytes, SHA-256e33512867ee33eb9227d46703d09610db800d9218a1c7c71bfc87aa47aeff525.

The complete stdout is:

    EXACT_SEVEN_RADIAL_STAR_FRAME_BOUNDS_PASS
    metric_thin.json 3094 dd1c2dddf464e8237b97450b4dd335868de3260f01905c0fc8c9b55e05f52121
    BOUNDED_PROJECTIVE_FRAME_RANK_ONE_METRIC_EXCLUSION_PASS

Original build/check completed successfully. A second empty directory received ONLY the source and completed build/check; source, report and stdout hashes and byte comparisons agreed. These executions produce new frame constants, not a routine independent replay of the parent's all-SPD certificate. The analytic rank-one theorem does not depend on successful execution as its proof.

## 5. Complete standalone source

```python
"""Own-centroid rank-one metric exclusion in bounded projective frames.
CPython 3.13.5; standard library only; no randomness. Usage: build | check.
This script constructs exact seven-star frame bounds, not a U1 census.
"""
from fractions import Fraction as Q
from itertools import combinations
import hashlib, json, sys
from pathlib import Path
assert __debug__

def dot(x,y): return sum((a*b for a,b in zip(x,y)),Q(0))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def cross(x,y): return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def det(a): return dot(a[0],cross(a[1],a[2]))
def mv(a,x): return tuple(dot(row,x) for row in a)
def inverse(a):
    d=det(a); assert d
    return tuple(tuple(cross(a[(j+1)%3],a[(j+2)%3])[i]/d for j in range(3)) for i in range(3))
def vec(x): return tuple(Q(a) for a in x)
X=list(map(vec,[(-1,-1,'-3/4'),(-1,-1,1),(-1,'-3/4',-1),(-1,1,-1),(-1,1,1),
                (1,-1,'-3/4'),(1,-1,1),(1,'-3/4',-1),(1,1,-1),(1,2,3)]))
FACETS=[(0,1,4,3,2),(1,9,4),(3,4,9),(0,5,6,1),(1,6,9),(2,3,8,7),(3,9,8),(5,7,8,9,6),(0,2,7,5)]
AH=[((-1,0,0),1),((-2,0,2),4),((-1,2,0),3),((0,-1,0),1),((0,-2,3),5),
    ((0,0,-1),1),((0,4,-1),5),((1,0,0),1),((0,-1,-1),'7/4')]

def build():
    for face,(normal,h) in zip(FACETS,AH):
        normal=vec(normal); h=Q(h); assert h>0
        slacks=[h-dot(normal,x) for x in X]
        assert min(slacks)>=0 and set(face)=={i for i,z in enumerate(slacks) if z==0}
        assert any(cross(sub(X[j],X[i]),sub(X[k],X[i]))!=(0,0,0) for i,j,k in combinations(face,3))
    edges=[]
    for f,h in combinations(FACETS,2):
        meet=tuple(sorted(set(f)&set(h)))
        assert len(meet)<=2
        if len(meet)==2: edges.append(meet)
    edges=sorted(set(edges)); assert len(edges)==17 and len(X)-len(edges)+len(FACETS)==2
    adj=[[j if i==s else i for i,j in edges if s in (i,j)] for s in range(len(X))]
    simple=[s for s in range(len(X)) if len(adj[s])==3]
    assert simple==[0,2,4,5,6,7,8]
    rows=[]
    for s in simple:
        ns=sorted(adj[s]); e=[sub(X[i],X[s]) for i in ns]
        W=tuple(tuple(e[j][i] for j in range(3)) for i in range(3))
        if det(W)<0:
            ns[0],ns[1]=ns[1],ns[0]
            e=[sub(X[i],X[s]) for i in ns]
            W=tuple(tuple(e[j][i] for j in range(3)) for i in range(3))
        assert det(W)>0
        R=inverse(W); rs=[mv(R,sub(x,X[s])) for x in X]
        b=tuple(-a for a in mv(R,X[s]))
        assert all(a>0 for a in b) and all(a>=0 for r in rs for a in r)
        for j,n in enumerate(ns): assert rs[n]==tuple(Q(i==j) for i in range(3))
        L=tuple(max(Q(1),max(r[k] for r in rs)) for k in range(3))
        L2=dot(L,L); threshold=1/(48*L2)
        rows.append({'s':s,'neighbors':ns,'W':W,'r':rs,'b':b,'L':L,'L_squared':L2,
                     'necessary_U1_second_to_first_eigenvalue_ratio':threshold})
    return {'identity':'BOUNDED_PROJECTIVE_FRAME_RANK_ONE_METRIC_EXCLUSION_V1',
            'vertices':X,'facets':FACETS,'true_edges':edges,'simple_star_bounds':rows,
            'global_seven_star_threshold':min(row['necessary_U1_second_to_first_eigenvalue_ratio'] for row in rows)}

def enc(obj):
    if isinstance(obj,Q): return str(obj)
    if isinstance(obj,dict): return {k:enc(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)): return [enc(v) for v in obj]
    return obj

def main():
    assert sys.argv[1:] in (['build'],['check'])
    obj=build(); data=(json.dumps(enc(obj),sort_keys=True,separators=(',',':'))+'\n').encode()
    p=Path('metric_thin.json')
    if sys.argv[1]=='build':p.write_bytes(data)
    else:assert p.read_bytes()==data
    print('EXACT_SEVEN_RADIAL_STAR_FRAME_BOUNDS_PASS')
    print(p.name,len(data),hashlib.sha256(data).hexdigest())
    print('BOUNDED_PROJECTIVE_FRAME_RANK_ONE_METRIC_EXCLUSION_PASS')
if __name__=='__main__':main()
```

## 6. Next substantive boundary

The full-star affine frame prevents body collapse and now prevents normalized rank-one metric limits for U1. What remains is the rank-two boundary and its coupled true centroid/edge-escape geometry, together with the full-rank region and other projective stars. A planar projection equipped with the chord-length density of a3-body is NOT a uniformly filled planar polygon; replacing it by an unweighted polygon would change its centroid. A future rank-two argument must keep that induced density or work directly with the actual three-dimensional moments. This capsule supplies a necessary constraint for such work, not the missing exclusion itself.
