# minimum-0273

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# ROOT_FOOT_COMPLETE_SIGN_STRATA_DEGREE32_V1

## Result and scope

The substantive result is a **complete sign-stratum extension of the fixed-foot quadratic model**. For a fixed rational actual body and a chosen stable facet, it handles every genuine primal and polar escape alternative, including zero-arrow strata and physical weak-contact boundaries. It does not replace a closed sign cell by its closure without checking where the determinant equation is met.

The extension has three useful conclusions.

**Low-dimensional extremum certificates.** For

    Q(a,b,c,d)=ac−b²−d,

on any nonempty compact polytope in four variables, a minimum occurs at a vertex or on an edge. A maximum occurs at a vertex, on an edge, or on a two-dimensional face. Degenerate stationary sets do not require a nonsingular four-dimensional optimization problem.

**Complete physical sign-cell test.** There is an exact rational test for whether Q=0 meets the relative interior of a sign cell. This is stronger than testing min Q≤0≤max Q on the closed cell: the latter can accept a point at which one of the required strict signs has changed. Conversely, a tangential physical intersection must not be rejected merely because Q does not change sign.

**A degree-32 two-variable description.** For a fixed rational actual E17 body, the set of feet admitting a physical joint S1/U1 metric with a specified stable facet has a finite Boolean description using rational polynomials of degree at most32 in the two foot coordinates. The same assertion holds with proper110 required. There are no remaining existential metric variables in this description. The construction incorporates all68 true-edge primitives, not one selected five-sign packet or an independently chosen polar metric.

This is an analytic finite-elimination result, **not an executed E17 exclusion**. I do not claim that a newly computed actual foot region is empty, that a full physical U1/110 example has been found, or that the resulting two-variable decision problem has been run. The complete five-parameter H5 family is already U2 and is not proposed as new coverage.

### Input and execution limitation

The current tool calls did not return inspectable file text or execution output. In particular, I cannot certify a complete read of journal lines101–3025 or of the three new exact source files in this execution. I also cannot cross-check the literal contents of the two required parents against their manifest hashes. Their supplied identities remain

    minimum-0268
    c199a4de7b66fb757fbc3f1b2beeb903f7002fe567611824a9f0626b32aa2fc5

    minimum-0225
    c772d9b01329dcd809a288ef999d910676c13c3334cff8c96e7d59a51b887bdd.

The unread exact dependencies are `ROOT_FOOT_QUADRATIC_ELIMINATION_AND_ACTUAL_HULL_GAP_V1.md`, `root_fibre_exact.py.txt`, and `COMMON_HEIGHT_CONICS_AND_REGRESSION_DOMAIN_V1(1).md`. Their native paths alone are not treated as evidence that I inspected their contents. Consequently, I make no claim that the supplied actual countercontrol has been extended or independently replayed, and no novelty-priority claim relative to details that might already be in those files.

The argument below re-derives the needed chart from the physical setup stated in the assignment. The new verification unit is complete but **unexecuted**. No new output hash, completed atlas, or observed terminal marker is asserted.

## 1. Actual body, stable foot, and one physical inverse

Fix a full-dimensional rational convex polytope P, uniformly filled and translated to its actual volume centroid. Its centered vertices are x_i, its actual normalized poles are q_j, and its true edges and maximal facets are fixed. Choose a facet F with pole q, so q·x=1 on F.

Choose rational tangent vectors t1,t2 spanning q-perp and a rational point f0 in relint F. Parameterize a possible stable foot by

    f(u,v)=f0+u t1+v t2,
    H(u,v)=[t1,t2,f(u,v)].

Because q·t1=q·t2=0 and q·f=1, H is invertible and its determinant is independent of u,v.

If f is the foot under a physical M>0, rescale M by the positive scalar qᵀM⁻¹q. The rescaled metric, still denoted M, obeys

    Mf=q,    qᵀM⁻¹q=1.

This normalization is a change of physical scale, not a new independently selected inverse. Symmetry gives

    HᵀMH = diag(G,1),
    G = [[a,b],[b,c]].

With d=det G, the physical inverse is exactly

    M = H⁻ᵀ diag(G,1) H⁻¹,
    N = M⁻¹ = H diag(adj G/d,1) Hᵀ.                 (1)

Thus a>0, d>0 and

    Q=ac−b²−d=0                                    (2)

are sufficient for G>0 and for a genuine common inverse pair in (1). They also imply c>0. The determinant equation is not a proxy for an independently normalized pair.

### Every original arrow is affine in a,b,c,d

Write the primal coordinates H⁻¹x_i=(r_i,z_i), where r_i is two-dimensional, and write the pole coordinates Hᵀq_j=(s_j,w_j). For a true primal edge i→k,

    D_ik = r_iᵀG(r_k−r_i)+z_i(z_k−z_i).             (3)

For a true polar edge j→l, multiplication by the positive d gives

    d E_jl = s_jᵀ adj(G)(s_l−s_j)+d w_j(w_l−w_j).   (4)

Both expressions are affine in (a,b,c,d).

The dependence on the foot is particularly simple. In the fixed frame H0=[t1,t2,f0], write H0⁻¹x_i=(r_i0,z_i). Then

    r_i=r_i0−z_i(u,v),
    s_j=(q_j·t1,q_j·t2),
    w_j=q_j·f0+s_j·(u,v).

Consequently every coefficient and constant in (3)–(4) is a rational polynomial of foot degree at most2. The tangential part of (4) is independent of the foot. This observation is the basis of the degree bound below.

A non-affine projective refill must first produce its new raw vertices, actual uniform centroid, covariance and normalized supports. No part of (1) permits transporting the old centroid without the volume Jacobian.

For a rational outward boundary triangulation with raw triangle vertices A,B,C and δ=A·(B×C), the actual quantities can be reconstructed by

    D = sum δ = 6 Vol,
    g = sum δ(A+B+C)/(4D),

    Sigma = sum δ[(A+B+C)(A+B+C)ᵀ+AAᵀ+BBᵀ+CCᵀ]/(20D) − ggᵀ.

These are actual boundary integrals. Integration diagonals are never added to the mechanical edge set.

## 2. A uniform positive metric box and an explicit root-foot polygon

The compact box need not be an arbitrary numerical search cutoff.

Let C>0 be a fixed rational reference for this actual body, and suppose every joint candidate under consideration necessarily satisfies

    cond(C¹ᐟ² M C¹ᐟ²) ≤ K,

where K>1 is rational. For the actual-covariance E17 application, C=Sigma and the retained finite-height result supplies the safe K=48. This is a bound in the actual covariance frame, not in an unrelated reference.

Set

    T=qᵀCq,
    W=[t1,t2]ᵀ C⁻¹ [t1,t2].

After the foot normalization qᵀNq=1, the condition bound gives

    C/(KT) ≤ N ≤ KC/T,
    (T/K)C⁻¹ ≤ M ≤ KT C⁻¹.

Therefore the same positive rational box works for every possible foot on F:

    (T/K)W11 ≤ a ≤ KT W11,
    (T/K)W22 ≤ c ≤ KT W22,
    −KT(W11+W22)/2 ≤ b ≤ KT(W11+W22)/2,
    (T/K)² det W ≤ d ≤ (KT)² det W.                 (5)

All lower bounds needed for a and d are strictly positive. The determinant bounds follow from Loewner monotonicity of determinant on positive definite two-by-two matrices.

### Root maximality gives a smaller foot domain

If F is the unique strict stable facet, q is the unique global N-norm maximum among the actual poles. A distinct pole tied at the global maximum would itself have strictly negative derivatives to all its neighbours, producing another stable facet.

For every q_j≠q, q_jᵀNq_j<1. Since Nq=f,

    1−q_j·f > (q_j−q)ᵀN(q_j−q)/2,
    1+q_j·f > (q_j+q)ᵀN(q_j+q)/2.                 (6)

In particular −f lies in int P. Under the same condition bound, every joint candidate belongs to the following **closed rational polygon** in the plane q·f=1:

    −1+(q_j+q)ᵀC(q_j+q)/(4KT)
       ≤ q_j·f
       ≤ 1−(q_j−q)ᵀC(q_j−q)/(4KT),    q_j≠q.       (7)

The factor4 leaves room below the strict inequalities derived from (6). Every upper margin is positive, so this polygon lies strictly inside F. If it is empty, the entire stable-root alternative F is excluded before determinant elimination. If it is nonempty, its points are only candidate feet; (7) does not assert physical feasibility.

There is also a useful affine-in-(a,b,c,d) root-maximality row for every other pole:

    s_jᵀ adj(G)s_j+d(w_j²−1)<0.                    (8)

It may be added to the linear cells. Its foot degree is still at most2. Such rows strengthen the necessary polytope without replacing the physical determinant equation.

The box (5) is only a necessary outer bound. A point in it is not thereby known to satisfy a separately prescribed covariance or reference gate. In the unrestricted mechanical decision below, K is used solely because all genuine joint candidates must obey it; the final reconstructed metric is accepted through (1)–(4) and the complete physical census.

## 3. Extremum face reduction for the determinant completion

Let P4 be any nonempty compact polytope in R⁴, possibly of lower affine dimension, and let

    Q(a,b,c,d)=ac−b²−d.

### Theorem 1

A global minimum of Q on P4 occurs at a vertex or at a stationary point of Q on an edge. A global maximum occurs at a vertex, at a stationary point on an edge, or at a stationary point on a two-dimensional face.

Moreover, extrema can be chosen so that the restricted Hessian is nonsingular on a positive-dimensional supporting face. Thus vertex enumeration and nonsingular KKT systems for edges and two-faces suffice to recover the exact minimum and maximum. Degenerate extrema are not omitted: they can be moved to a smaller face without changing their value.

### Proof

Make the linear change

    A=(a+c)/2,    B=(a−c)/2.

Then Q=A²−B²−b²−d. Its Hessian has inertia(1,2,0), and its kernel is precisely the d-direction. Its derivative in that kernel direction is −1.

At a minimum in the relative interior of a face, the restricted gradient vanishes and the restricted Hessian is positive semidefinite. A subspace of dimension at least2 on which a form of inertia(1,2,0) is positive semidefinite must contain the kernel direction. Stationarity along that direction is impossible. Hence the face has dimension at most1.

At a maximum, the corresponding negative-semidefinite subspace can have dimension at most2 without containing the kernel direction. Therefore the face has dimension at most2.

If the restricted Hessian has a null direction at a stationary extremum, Q is constant along the corresponding line in that face. Compactness lets the point move along that line to a proper boundary face. Repeating terminates. This proves the nonsingular-candidate statement as well.

### Exact candidate equations

Write Q(x)=xᵀJx/2+gᵀx, where

    J=[[0,0,1,0],[0,−2,0,0],[1,0,0,0],[0,0,0,0]],
    g=(0,0,0,−1).

For an active affine system Ex=e of rank r, the stationary equations are

    [[J,Eᵀ],[E,0]] [x,lambda] = [−g,e].            (9)

Use r=3 for an edge, r=2 for a two-face, and r=4 for vertices. The exact systems have sizes7,6 and at most8. Candidate membership in every original inequality is checked. Extraneous feasible stationary candidates do not affect correctness: their values lie between the actual minimum and maximum, and Theorem1 guarantees that both extrema occur in the candidate list.

No assertion of convexity of Q, or of convexity of the physical reciprocal graph, is involved.

## 4. The missing relative-interior test

A complete mechanical sign stratum is relatively open. Its closed polytope alone does not preserve its strict signs.

Let P4° denote relint P4. Let m and M be the exact minimum and maximum of Q on the closed polytope. Let S be the affine stationary set of Q on aff P4, intersected with P4.

### Theorem 2

The relative interior contains a physical determinant completion exactly when

    m<0<M,

or

    S intersects P4° and Q is zero on S.            (10)

The second alternative is a rational linear-feasibility test followed by one rational quadratic evaluation.

### Proof and exact implementation

If an interior zero is not stationary, a small displacement in both signs of its nonzero derivative produces positive and negative values inside the cell. Conversely, if m<0<M, density of P4° in P4 supplies interior points of both signs, and their segment contains an interior zero.

The only remaining possibility is an interior stationary zero. The stationary equations on an affine space are linear. If x and y are stationary on that space, their difference is tangent to it, and the stationary equations imply Q(x)=Q(y). Thus Q is constant on the entire stationary affine set.

For a bounded rational polytope, S has rational vertices whenever it is nonempty. It meets P4° exactly when, for each inequality not identically tight on P4, at least one vertex of S has positive slack. Averaging these vertices then gives one point satisfying all those strict inequalities simultaneously. The constant Q-value can be evaluated at any vertex of S.

This handles all three delicate cases:

- A zero only on the boundary of a required strict sign cell is rejected for that cell.
- An isolated tangential zero in its interior is accepted.
- A degenerate stationary line of zeros is accepted when it actually meets the relative interior.

The boundary point rejected for one open cell is not lost: it belongs to its own zero-sign stratum and is tested there with its correct mechanical signs.

## 5. Complete true-arrow coverage without selecting trees first

At a fixed foot, form all genuine primal and polar rows (3)–(4). In E17 there are68 rows. Add the box boundary hyperplanes and, optionally, the valid root-norm rows(8).

Start with every relatively open face of the four-dimensional box. Insert the arrow hyperplanes one at a time, retaining every nonempty negative, zero and positive stratum. Each stratum is convex and relatively open in its affine hull. Its closure is a rational polytope. Exact linear extrema at vertices decide whether a split is needed; all zero strata are retained.

For a completed sign word:

    U={i: every true outgoing primal row at i is negative},
    S={j: every true outgoing polar row at j is negative}.

A true edge is a strict saddle exactly when all its four primitives are negative. It carries a physical weak point only when all four are nonpositive and at least one is zero. For a properness decision, it suffices to reject any such edge; counting a VF twice is unnecessary when the question is whether the weak set is empty.

Retain only sign words with S={F} and |U|=1. For proper110 also require no physical weak edge and H=0. Apply Theorem2 to each retained stratum. A passing point has a>0,d>0,Q=0, so (1) produces a physical SPD metric and its literal inverse. All68 primitive signs are then the signs of that physical pair.

This is complete for the original escape alternatives. On Q=0, every nonnegative arrow strictly increases the corresponding norm, so a directed escape cycle is impossible. Consequently the local nonroot escape clauses already imply genuine rooted trees; there is no need to choose one tree in advance. Directed cycles may also be rejected as an exact preliminary sign-word test.

At a fixed foot, the total number of strata is bounded by the elementary hyperplane-arrangement bound

    sum_{j=0}^4 2^j binomial(m+8,j),

where m is the number of inserted arrow and optional norm hyperplanes. This is a count bound in fixed dimension, not a practical runtime or bit-complexity guarantee. Degenerate arrangements have no more strata. The bound follows by inserting one hyperplane and applying the same recurrence to its induced arrangement.

## 6. Degree-32 elimination of all four metric variables

### Theorem 3

Fix a rational actual body, a rational C,K satisfying the stated necessary condition bound, and a chosen stable facet F. The set of feet in (7) admitting joint S1/U1, or admitting proper110, is describable by a finite Boolean combination of rational polynomials in (u,v), each of total degree at most32.

This is a description of the unrestricted physical mechanical problem using K as a proved necessary bound. An additional independently specified gate must be included or checked separately.

### Constructive degree accounting

Every row coefficient and constant has foot degree at most2. Consider one sign word and one box-face choice. Its zero rows give affine equalities; its nonzero rows give strict inequalities. Enumerate all possible independent equality bases, retaining their exact rank and consistency conditions.

A vertex of the resulting bounded polytope is obtained from four independent affine equations. Its coordinates are rational functions with numerator and denominator degree at most8.

The extremum candidates in Theorem1 come from (9). Its size is at most8 and every entry has degree at most2. Cramer's rule therefore gives candidate coordinates with numerator and denominator degree at most16. The same bound applies to vertices of the possibly degenerate stationary set: retain the equations in variables(x,lambda), add active original inequalities, and enumerate independent bases. Although lambda is not an original metric variable, it is uniquely determined by x when E has full row rank, so this stationary polytope is bounded.

At any such candidate,

    Q(x)=(p_a p_c−p_b²−p_d Delta)/Delta²,

with all numerator degrees at most32. Original inequality membership has numerator degree at most18. Determinant/rank guards have degree at most16. **Split on the sign of Delta** when interpreting a rational inequality, rather than multiplying it into a numerator and unnecessarily increasing the degree.

Strict linear feasibility of a sign cell is also expressible by vertex predicates: each required strict inequality must be strict at some vertex, and an average gives simultaneous strictness. The stationary relative-interior condition in Theorem2 has the same form. Thus all predicates are Boolean combinations of polynomial signs of degree at most32.

Finally take the finite disjunction over mechanically admissible sign words and equality-basis branches. Rank-drop curves, foot-boundary cells, tangencies and zero-arrow strata are included by equality predicates; they are not discarded as nongeneric.

This constructs the asserted two-variable formula. It does not claim a small number of polynomials, a degree32 formula when the body's shape variables are also free, or a completed two-variable decomposition for a supplied E17 example.

### Witness complexity at a fixed rational foot

Every feasible fixed rational-foot instance has a physical witness over a real extension of degree at most2.

In the sign-change case, take rational relative-interior points x−,x+ of opposite Q signs. The unique root in(0,1) of Q(x−+t(x+−x−)) is linear or quadratic over Q. In the stationary case, the rational stationary-polytope average is already a rational zero.

For proper110 with only the rational foot fixed and no additional exact metric equalities, a rational G can be chosen: properness is open in the three physical entries of G, including when some unselected zeros are harmless. This may change the harmless-zero sign stratum. There is no claim that every prescribed zero stratum has a rational point.

## 7. Complete fixed-foot verification unit

The following standard-library source implements Theorems1–2 for bounded rational polytopes. It includes the exact low-face enumeration, degenerate stationary-set test, relative-interior check, and a quadratic-segment witness. The literal tests cover an edge minimum, a two-face maximum, interior tangency, a closure-only false positive, an irrational completion and a stationary line.

These tests are **formal chart controls**, not actual-polyhedron countercontrols. The source has not been observably executed here. Its expected ranges follow directly from the displayed one- and two-variable restrictions. No output pins are claimed.

Save as `root_foot_strata_exact.py` and run with assertions enabled:

    python -B -S root_foot_strata_exact.py

Expected final marker:

    ROOT_FOOT_RELATIVE_STRATA_EXACT_PASS

```python
from fractions import Fraction as F
from itertools import combinations, count
from pathlib import Path
import hashlib
import json

J=((0,0,1,0),(0,-2,0,0),(1,0,0,0),(0,0,0,0))
g=(F(0),F(0),F(0),F(-1))

def dot(a,b):
    return sum((F(x)*F(y) for x,y in zip(a,b)),F(0))

def q(x):
    a,b,c,d=x
    return a*c-b*b-d

def reduced(rows,n):
    B=[[F(x) for x in a]+[F(b)] for a,b in rows]
    r=0
    for col in range(n):
        k=next((k for k in range(r,len(B)) if B[k][col]),None)
        if k is None:
            continue
        B[r],B[k]=B[k],B[r]
        t=B[r][col]
        B[r]=[x/t for x in B[r]]
        for k in range(len(B)):
            if k!=r and B[k][col]:
                t=B[k][col]
                B[k]=[x-t*y for x,y in zip(B[k],B[r])]
        r+=1
    if any(not any(z[:n]) and z[n] for z in B):
        return None
    return [(tuple(z[:n]),z[n]) for z in B[:r]]

def unique(rows,n):
    R=reduced(rows,n)
    if R is None or len(R)!=n:
        return None
    x=tuple(b for a,b in R)
    assert all(dot(a,x)==b for a,b in rows)
    return x

def nullspace(matrix,n=4):
    R=reduced([(a,F(0)) for a in matrix],n)
    assert R is not None
    piv=[next(i for i,x in enumerate(a) if x) for a,b in R]
    out=[]
    for j in range(n):
        if j in piv:
            continue
        x=[F(0)]*n
        x[j]=1
        for (a,b),i in zip(R,piv):
            x[i]=-a[j]
        out.append(tuple(x))
    return out

def vertices(A,E=()):
    R=reduced(E,4)
    if R is None:
        return []
    out=set()
    for chosen in combinations(A,4-len(R)):
        x=unique(R+list(chosen),4)
        if x is None:
            continue
        if all(dot(a,x)<=b for a,b in A):
            assert all(dot(a,x)==b for a,b in E)
            out.add(x)
    return sorted(out)

def affine_hull(V):
    assert V
    v=V[0]
    normals=nullspace([tuple(x-y for x,y in zip(w,v)) for w in V[1:]])
    return [(a,dot(a,v)) for a in normals]

def feasible(x,A,E):
    return all(dot(a,x)<=b for a,b in A) and all(dot(a,x)==b for a,b in E)

def extrema(A,E=()):
    V=vertices(A,E)
    if not V:
        return None
    E0=affine_hull(V)
    r0=len(E0)
    candidates=set(V)
    for r in (2,3):
        if r<r0:
            continue
        for chosen in combinations(A,r-r0):
            EE=reduced(E0+list(chosen),4)
            if EE is None or len(EE)!=r:
                continue
            rows=[]
            for i in range(4):
                rows.append((tuple(J[i])+tuple(a[i] for a,b in EE),-g[i]))
            for a,b in EE:
                rows.append((tuple(a)+(F(0),)*r,b))
            answer=unique(rows,4+r)
            if answer is None:
                continue
            x=answer[:4]
            if feasible(x,A,E0):
                candidates.add(x)
    candidates=sorted(candidates)
    vals=[q(x) for x in candidates]
    return {'vertices':V,'equalities':E0,'candidates':candidates,
            'minimum':min(vals),'maximum':max(vals)}

def mean(points):
    assert points
    return tuple(sum((p[i] for p in points),F(0))/len(points) for i in range(4))

def in_relative_interior(x,A,V):
    for a,b in A:
        if any(dot(a,v)<b for v in V):
            if not dot(a,x)<b:
                return False
        elif dot(a,x)!=b:
            return False
    return True

def stationary_vertices(A,E0):
    tangent=nullspace([a for a,b in E0])
    EE=list(E0)
    for l in tangent:
        row=tuple(sum((l[i]*J[i][j] for i in range(4)),F(0)) for j in range(4))
        EE.append((row,-dot(l,g)))
    return vertices(A,EE)

def interior_shift(x,c,sgn):
    for k in count(1):
        e=F(1,2**k)
        y=tuple((1-e)*a+e*b for a,b in zip(x,c))
        if sgn*q(y)>0:
            return y

def relative_zero(A,E=()):
    R=extrema(A,E)
    if R is None:
        return {'feasible':False,'reason':'empty closed polytope'}
    lo,hi=R['minimum'],R['maximum']
    base={'range':[lo,hi]}
    if lo<0<hi:
        c=mean(R['vertices'])
        xm=next(x for x in R['candidates'] if q(x)<0)
        xp=next(x for x in R['candidates'] if q(x)>0)
        left=interior_shift(xm,c,-1)
        right=interior_shift(xp,c,1)
        assert in_relative_interior(left,A,R['vertices'])
        assert in_relative_interior(right,A,R['vertices'])
        e=tuple(b-a for a,b in zip(left,right))
        grad=tuple(dot(J[i],left)+g[i] for i in range(4))
        polynomial=(q(left),dot(grad,e),dot(e,tuple(dot(J[i],e) for i in range(4)))/2)
        assert polynomial[0]<0 and sum(polynomial)>0
        base.update(feasible=True,kind='quadratic_segment',left=left,right=right,
                    polynomial_ascending=polynomial,unique_root_interval=[0,1])
        return base
    if lo>0 or hi<0:
        base.update(feasible=False,reason='strict one-sided quadratic range')
        return base
    SV=stationary_vertices(A,R['equalities'])
    if SV:
        value=q(SV[0])
        assert all(q(v)==value for v in SV)
        x=mean(SV)
        assert q(x)==value
        if value==0 and in_relative_interior(x,A,R['vertices']):
            base.update(feasible=True,kind='rational_stationary',point=x)
            return base
    base.update(feasible=False,reason='zero only outside relative interior')
    return base

def box(bounds):
    rows=[]
    for i,(lo,hi) in enumerate(bounds):
        a=[F(0)]*4
        a[i]=1
        rows.append((tuple(a),F(hi)))
        a[i]=-1
        rows.append((tuple(a),-F(lo)))
    return rows

def enc(x):
    if isinstance(x,F):
        return str(x)
    if isinstance(x,dict):
        return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [enc(v) for v in x]
    return x

def main():
    assert __debug__
    report={}
    A=box([(F(1,2),F(3,2)),(-1,1),(F(1,2),F(3,2)),(1,3)])
    E=[((1,0,-1,0),0),((0,1,0,0),0),((-2,0,0,1),0)]
    R=extrema(A,E)
    assert (R['minimum'],R['maximum'])==(F(-1),F(-3,4))
    report['edge_minimum']=relative_zero(A,E)
    bounds=[(F(3,4),F(5,4)),(F(-1,4),F(1,4)),
            (F(3,4),F(5,4)),(F(1,2),F(1,2))]
    A=box(bounds);E=[((1,0,1,0),2)]
    R=extrema(A,E)
    assert (R['minimum'],R['maximum'])==(F(3,8),F(1,2))
    report['two_face_maximum']=relative_zero(A,E)
    bounds[-1]=(F(1),F(1))
    A=box(bounds)
    T=relative_zero(A,E)
    assert T['feasible'] and T['kind']=='rational_stationary'
    assert T['point']==(F(1),F(0),F(1),F(1))
    assert T['range']==[F(-1,8),F(0)]
    report['interior_tangency']=T
    A=box([(1,1),(0,0),(1,1),(F(1,2),1)])
    T=relative_zero(A)
    assert not T['feasible'] and T['range']==[F(0),F(1,2)]
    report['closure_trap']=T
    A=box([(1,1),(F(1,2),1),(1,1),(F(1,2),F(1,2))])
    T=relative_zero(A)
    assert T['feasible'] and T['kind']=='quadratic_segment'
    assert T['range']==[F(-1,2),F(1,4)]
    report['quadratic_field_completion']=T
    A=box([(1,1),(0,0),(1,2),(1,2)])
    T=relative_zero(A,[((0,0,-1,1),0)])
    assert T['feasible'] and T['point']==(F(1),F(0),F(3,2),F(3,2))
    report['stationary_line']=T
    raw=(json.dumps(enc(report),sort_keys=True,indent=2)+'\n').encode()
    Path('root_foot_strata_exact.json').write_bytes(raw)
    source=Path(__file__).read_bytes()
    print('SOURCE',len(source),hashlib.sha256(source).hexdigest())
    print('REPORT',len(raw),hashlib.sha256(raw).hexdigest())
    print('ROOT_FOOT_RELATIVE_STRATA_EXACT_PASS')

if __name__=='__main__':
    main()
```

## 8. Continuation and what remains undecided

The immediate substantive use is to take a genuinely unresolved actual body from the full nine- or eleven-modulus chart, compute its real centroid and covariance, form the root polygons(7), and apply the complete sign-stratum test rather than a selected mixed packet. A surviving stratum must return a determinant-compatible metric and a complete physical census. An exclusion must exhaust every root polygon and all its strata, including lower-dimensional zero-arrow cases.

The new finite reduction does not decide whether any such unresolved body's foot set is empty. The supplied five-sign convex-hull countercontrol cannot be promoted to a full-tree obstruction without its literal data and the remaining rows. Likewise, satisfying box(5) is not satisfaction of every original reference gate.

No completed old605-cell replay was performed, and no new five-parameter H5 coverage is claimed. The internal accepted bracket34≤C_min≤622 remains unchanged.
