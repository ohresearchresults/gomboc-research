# minimum-0260

Historical AI scientific report · saved 2026-09-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# H5_TWO_SIDED_ORTHOGONAL_CONE_AND_POOLED_ROOT_DUAL_V1

## 1. Result and verification status

The strongest new result is an exact strengthening of the complete-root mechanism: **the two adjacent spectral-gap bounds determine a two-sided matrix cone, not merely a lower trace floor**. I derive its exact convex hull, the optimal value of every linear root stress on it, a rational semidefinite certificate, and a homogeneous certificate combining several auxiliary references without normalizing the same physical metric differently for each reference.

There is also a completely specified actual-centroid control. At the supplied orthogonal-reference H5 point, the calibration metric M=C⁻¹ has a genuine physical VF at top vertex 9. An explicit rational matrix on this same reference distinguishes the new two-sided stress criterion from the old one-sided criterion. That distinguishing matrix is **not claimed to be a nonnegative combination of a rooted tree’s arrows**.

**No new whole-region joint exclusion is promoted in this handoff.** I implemented searches over the full Gamma-blind box, but an inspected, completed exact replay establishing both the regional orthogonal bound and coverage of all 48,790 rooted alternatives was not available for the final handoff. The computational snapshot is therefore unpromoted work, not a durable successor to the accepted all-root atlas. No matrix is claimed to be a joint110 or proper110 construction.

The minimum bracket remains **34≤C_min≤622**. The accepted central-cube exclusion, the earlier positive reference box, and the precise Gamma-template limitation remain unchanged. fileciteturn12file0L11-L21

### Input authority

The retained reading record covers the entire updated journal, all newly supplied exact sources, the unchanged supplied dependencies, and the complete literal parent payloads. The updated journal is 374950 bytes, SHA-256 `d44beebbe9525d393a670a5871d40e30f5151b48d5fe61d60550a612c31ed34a`.

The parent identities used are:

- Complete-root parent `minimum-0256`, SHA-256 `9e71d008aa4b1d85333f293fd38dd05ab80a944563fa4e8fb4c5509dfcebb28e`.
- Reference-frontier parent `minimum-0258`, SHA-256 `3dde84b70dfae7cad30e3404a2b985e28775e29fb2a5258f9a5086f7eb4c8167`.
- Seven-turn parent `minimum-0255`, SHA-256 `b02e9ea175553f06a5fc27b626e52977c8baf76d50df0e70d68eff5fb913393e`.

No source-identity conflict was found. No unavailable historical archive item is a premise of the results below.

## 2. Exact convex hull of the adjacent-gap information

Fix an auxiliary reference C>0 and one physical metric M>0. Put

    H = C^(1/2) M C^(1/2),
    Hbar = H / tr(CM).

Let its decreasing eigenvalues satisfy

    λ1/λ2 ≤ p,       λ2/λ3 ≤ q,

where p,q≥1. Define

    Z = pq+q+1,
    r1 = pq/Z,       r2 = q/Z,       r3 = 1/Z.

The orthogonal-shell theorem supplies such p and q for the **same** H, using the self-polar factor and the primal and polar escape-height bounds. It does not introduce an independently chosen polar metric. fileciteturn12file0L24-L33

### Theorem 1 — exact two-sided spectral hull

Let S(p,q) be the normalized SPD matrices obeying the two adjacent-gap bounds. Then

    conv S(p,q)
      = { X symmetric : tr X=1, r3 I ≤ X ≤ r1 I }.

In particular, the lower bound Hbar≥r3 I discards information: the upper bound Hbar≤r1 I is also necessary. Together they give the entire convex hull of the original adjacent-gap class.

#### Proof

For the largest eigenvalue, the gap bounds imply

    λ2 ≥ λ1/p,       λ3 ≥ λ1/(pq).

Normalization therefore gives λ1≤r1. Similarly λ2≤qλ3 and λ1≤pqλ3 imply λ3≥r3. Thus S(p,q) is contained in the displayed matrix interval.

Conversely, take a matrix in that interval and diagonalize it. Its eigenvalue vector lies in the plane x1+x2+x3=1 with each coordinate between r3 and r1. The vertices of this planar polytope are precisely the permutations of (r1,r2,r3), with duplicates removed in degenerate cases. Indeed two coordinates at the upper bound would force the third below r3 unless r1=r2; two coordinates at the lower bound would force the third above r1 unless r2=r3. The other vertices have one coordinate at each bound and the remaining coordinate r2.

The eigenvalue vector is consequently a convex combination of permutations of r. Conjugating those diagonal matrices by the fixed eigenbasis expresses the original matrix as a convex combination of matrices in S(p,q). This proves equality.

### Theorem 2 — optimal linear stress value

For a symmetric raw-coordinate stress Q, let

    B = C^(-1/2) Q C^(-1/2)

have increasing eigenvalues b1≤b2≤b3. Then

    min tr(MQ), over tr(CM)=1 and the adjacent-gap class,
      = r1 b1 + r2 b2 + r3 b3.                         (1)

The minimum is unchanged by replacing the adjacent-gap class by its convex hull.

To prove this, diagonalize B. Only the diagonal entries of Hbar contribute to its trace pairing with B. Those entries lie in the same coordinate polytope described above. A linear functional is minimized at a permutation of r, and exchanging two coordinates shows that the largest weight must be paired with the smallest b. The minimizing diagonal matrix itself has spectrum r and obeys both original gap bounds.

Thus (1) is not another arbitrary sufficient spectral estimate. It is the **best possible use of the two adjacent-gap bounds by a single linear stress**.

The function

    F_C(Q) = r1 b1+r2 b2+r3 b3

is positively homogeneous, concave, and monotone for the Loewner order. These properties follow directly from its representation as the minimum of linear functionals tr(MQ) over the compact normalized cone.

## 3. A rational certificate in raw coordinates

Square roots of C and algebraic eigenvalues are unnecessary in a saved certificate.

### Theorem 3 — two-sided raw stress certificate

Suppose rational matrices Y,Z≥0 and a rational scalar t satisfy

    Q = t C + Y − Z.

Then every metric in the normalized two-sided cone satisfies

    tr(MQ) ≥ δ,
    δ = t + r3 tr(C⁻¹Y) − r1 tr(C⁻¹Z).                (2)

Therefore δ>0 certifies exclusion of any set of nonnegative escape arrows whose negative weighted sum is Q.

Indeed the raw metric inequalities are

    r3 C⁻¹ ≤ M ≤ r1 C⁻¹,       tr(CM)=1.

Pairing the first with Y≥0 and the second with Z≥0 proves (2). Every matrix in this certificate lives in the raw coordinate system. Exact principal-minor checks suffice for the PSD assertions.

For a fixed Q the best value in (2) equals (1). In a generalized eigenbasis, choose t=b2, take the positive part of B−b2 I as Y in reference coordinates, and the negative part as Z. Congruence back to raw coordinates gives equality. A strict certificate can be approximated by rational data while retaining a positive margin; no assertion is made that every boundary-only semidefinite problem has a rational optimizer.

### Relation to the inherited one-sided stress

If the upper constraint is discarded, the optimal lower-floor value becomes

    b1 + r3(b2+b3−2b1)
      = (1−3r3)b1+r3 tr B.

Its strict positivity is equivalent to

    Q + [r3/(1−3r3)] tr(C⁻¹Q) C > 0.

This is the inherited trace-shift form. The new criterion allows a negative eigenvalue of that shifted matrix when the upper spectral constraint compensates for it. Merely changing the old scalar constant would not produce this improvement.

## 4. Several references: retain one physical normalization

There is a second useful reduction. Suppose each reference Ck has a proved orthogonal bound giving normalized spectral bounds ell_k and u_k. The same physical M must satisfy the **homogeneous** LMIs

    M − ell_k tr(Ck M) Ck⁻¹ ≥ 0,
    u_k tr(Ck M) Ck⁻¹ − M ≥ 0.                        (3)

These are linear in M. Choose only one normalization, for example tr(C0 M)=1. Do not impose tr(Ck M)=1 separately for every reference.

### Theorem 4 — pooled-reference root certificate

For each k choose raw PSD matrices Yk,Zk. Define

    Gk = Yk − ell_k tr(Ck⁻¹Yk) Ck
         + u_k tr(Ck⁻¹Zk) Ck − Zk.

If a selected-arrow stress Q satisfies

    Q = δ C0 + sum_k Gk,       δ>0,                   (4)

then every common physical M satisfying (3) has

    tr(MQ) ≥ δ tr(C0 M) > 0.

Consequently (4) excludes that arrow packet. This is an exact sufficient certificate; I am not claiming an unconditional rational completeness theorem for boundary-only intersections of several reference cones.

The proof is simply to pair each LMI in (3) with its PSD multiplier. Equation (4) makes the different reference traces cancel correctly. It is stronger than asking whether one reference, by itself, excludes the packet.

References may be assigned to different trees or reused in a pooled packet. Every such constraint concerns the same M. The polar metric used in deriving their necessary gap bounds remains M⁻¹.

### Coordinate transport

Under a fixed invertible physical coordinate map L, use

    g′=Lg,          M′=L⁻ᵀML⁻¹,          N′=LNLᵀ,
    Ck′=LCkLᵀ,      Q′=LQLᵀ,
    Yk′=LYkLᵀ,      Zk′=LZkLᵀ.

All trace pairings and certificate equations above are preserved. A rational approximate whitening map is therefore harmless as a computational congruence, but it must transport the physical inverse pair as displayed.

## 5. The complete-root alternative and a moving-region compiler

For the actual centered vertices vi=zi−g and a true directed edge i→j, define the raw arrow stress

    Aij = −sym(vi (zj−zi)ᵀ).

Then

    tr(M Aij) = −Dij,
    Dij = viᵀM(zj−zi).

For a rooted tree T, a nonnegative weighted stress is Q=sum_(i,j in T) wij Aij, with wij≥0 and at least one positive weight.

### Exact alternative for one reference

Consider the SDP feasibility problem

    r3 C⁻¹ ≤ M ≤ r1 C⁻¹,
    tr(CM)=1,
    Dij ≥ 0 for every directed edge of T.             (5)

There are two possibilities.

If (5) is infeasible, compact convex separation gives nonnegative weights for which F_C(Q)>0. Theorem 3 then supplies the corresponding two-sided stress certificate. This gives a complete linear-stress test for the convexified one-reference problem, not just a strict-PD heuristic.

If an exact feasible M is supplied, it is an **actual monounstable physical control**, not merely a condition-number estimate. Along every selected tree edge,

    |vj|_M² − |vi|_M² = 2Dij + |zj−zi|_M² > 0.

Following the directed tree reaches its root, which has strictly larger norm than every other vertex. Every nonroot has a nonnegative true escape, and the root has strictly negative derivatives toward all its neighbors. Thus the root is the unique strict U.

This does **not** make the control joint110. A feasible point of the convex hull need not obey the original nonconvex adjacent-gap conditions. More importantly, its actual N=M⁻¹ must be audited on all 34 directed true polar edges to establish S and the physical weak contacts. No independently optimized inverse is admissible.

For a full H5 exclusion every one of the 48,790 genuine rooted alternatives must be covered. A failed numerical proposal is not either side of this exact alternative.

### Moving uniform centroid

Let D=6Vol and K=Dg, computed from the entire actual boundary. Clear the positive denominator:

    Aij,D = −sym((Dzi−K)(zj−zi)ᵀ) = D Aij.

With fixed C, these are polynomial matrices in all five H5 parameters. This avoids the inverse of a moving covariance matrix.

On a normalized five-dimensional box, enclose each matrix polynomial by an affine matrix plus a rigorous Loewner error. Its affine part has 32 corner matrices. If a weighted packet has F_C(Qcorner)>0 at every certified lower corner matrix, then concavity and Loewner monotonicity of F_C prove positivity throughout the box. The same argument applies after a fixed rational congruence, using the transported C.

This is a direct replacement for the old floor-shift compiler: compile **raw D-cleared Q**, then use the two-sided spectral functional. It is not a substitution of a new constant into the old covariance gauge.

## 6. Exact actual-centroid comparison control

Use the literal supplied H5 point

    theta = (3/20, 3/20, 3/20, 9/20, 3/25).

The actual homogeneous moments are

    Vol = 102241/750000,
    g = (184058311/817928000,
         173571241/817928000,
         119041/408964).

Set

    h = 289923/408964,
    m = (−184058311, −75419881)/817928000,
    W = [[2215,−1288], [−1288,2146]]/10000,

and retain the supplied reference

    C = [[W+mmᵀ, hm], [hmᵀ, h²]].

Here det W=1547223/50000000>0, so C>0. The supplied exact orthogonal-shell certificate has Upsilon_C≤24/5 at this actual body. Its identity is `SELF_POLAR_ORTHOGONAL_SHELL_AND_H5_HYBRID_V1.md`, SHA-256 `14c4a841bc3e3482a2e68b20110ccdc434ae3682bc2c5d51bfd3f00b769f93c8`.

Using the rational bounds f(10)<25/32 and f(9)<19/25 gives

    p=15/4,       q=456/125,
    (r1,r2,r3)=(1710,456,125)/2291.

These slightly relaxed separate gap bounds are sufficient for the comparison below.

### A stress accepted by the two-sided criterion and rejected by the old floor

Let a=(m,h), the actual centered top vertex 9, and define

    Q = 7C − 8aaᵀ.

Since C⁻¹a=(0,0,1/h), one has aᵀC⁻¹a=1. Therefore C⁻¹/²QC⁻¹/² has eigenvalues

    (−1,7,7).

The optimal old floor value is

    −291/2291 < 0.

The old shifted matrix also fails: its generalized smallest eigenvalue is

    −291/1916 < 0.

The exact new value is instead

    (−1710+7·456+7·125)/2291
      = 2357/2291 > 0.

A rational certificate is particularly simple:

    t=7,       Y=0,       Z=8aaᵀ,
    δ=2357/2291.

This exhibits a strict separation between the two certificate classes on the supplied actual H5 reference. **Q has not been represented as a nonnegative rooted-arrow stress. It is a method control, not a mechanical exclusion certificate.**

### The calibration metric is a genuine weak physical control

Now explicitly choose the physical metric M=C⁻¹ and its actual inverse N=C. In block form, with G=W⁻¹,

    M = [[G, −Gm/h],
         [−mᵀG/h, (1+mᵀGm)/h²]].

This is a physical choice, not an instruction to reset an arbitrary metric after whitening.

The top pole is qT=(0,0,1/h). Exactly,

    Ma=qT,       aᵀMa=1,
    NqT=a,       qTᵀNqT=1.

Thus the top-facet foot is the actual top vertex 9. It is a physical VF at the centered point

    (−184058311, −75419881, 579846000)/817928000.

The true incident edges (7,9) and (8,9) both identify that same physical point. The two primal derivatives out of vertex 9 along those top edges vanish. The two corresponding polar derivatives out of the top pole also vanish. The reverse derivatives are strictly negative by the positive squared lengths of the respective true edges. This proves a genuine VF, not merely an algebraic zero.

No total weak count or strict equilibrium count is asserted from an uninspected output. The complete exact verification unit below reconstructs all 68 primitives and deduplicates all physical weak points. The identified VF already shows that this calibration metric is not a proper110 control.

There is a general warning here: for a two-layer body, an auxiliary reference aligned so that C⁻¹a is normal to the top plane makes M=C⁻¹ place the top-facet foot at a. Optimizing an auxiliary reference for ideal angle and then treating its inverse as the physical metric can therefore introduce a forced weak contact. The auxiliary reference and the unknown physical metric must remain distinct in the proof.

## 7. Full-box attempt: exact inputs and unpromoted status

The attempted target was the entire earlier Gamma-blind box

    x,r,p ∈ [1/10,1/5],
    q ∈ [2/5,1/2],
    lambda ∈ [13/100,19/100].

The reference was the fixed C from Section 6. The center used for a proposed sandwich was

    theta0=(3/20,3/20,3/20,9/20,4/25).

The intended exact geometric inputs were

    Upsilon_C(P0) ≤ 9/2,
    (7/8)P0 ⊆ P(theta) ⊆ (7/6)P0,

with every body centered at its own moving uniform centroid. If both are exactly verified, they give

    Upsilon_C(P(theta)) ≤ (9/2)((7/6)/(7/8))² = 8.

The resulting safe separate gaps and normalized spectral vector are

    p=25/4,       q=152/25,
    (r1,r2,r3)=(950,152,25)/1127.

The implementation paths were a one-sided comparison atlas and a raw-stress two-sided atlas. Both enumerated true rooted trees, proposed nonnegative weights numerically, and required subsequent exact packet checks. The two-sided locator used the spectral functional in (1), not positive definiteness of the old shifted matrix.

The unpromoted snapshot preserves the sources, any saved cells and packets, available exact reports, and reconstruction metadata. It must not be treated as an accepted exclusion merely because a search file says `COMPLETE_UNVERIFIED`.

Promotion requires an inspected successful chain with the same C and parameter box:

    python -B -S shell_point.py .15,.15,.15,.45,.16 4.5
    python -B -S ortho_geometry_verify.py
    python -B -S ortho_two_sided_verify.py

The last command is meaningful only if its complete atlas exists. The alternative one-sided replay is `ortho_region_verify.py`. The geometry stage must establish the full actual-centered sandwich and true incidence; the root stage must establish the complete dyadic partition and all 48,790 alternatives in every cell.

Convenience copies of this **unpromoted** work are [the snapshot](sandbox:/mnt/data/h5_orthogonal_work_snapshot.zip) and [its recovery script](sandbox:/mnt/data/recover_h5_orthogonal_work_snapshot.py). They are not the sole recovery data for any newly asserted regional exclusion, because no such exclusion is asserted here. The accepted prior reconstruction checkpoints remain unchanged.

## 8. Complete recovery unit for the promoted method and physical control

The following source is self-contained. It uses the literal H5 body, reconstructs its actual volume centroid twice, exhaustively recovers the maximal supports, enumerates the 48,790 rooted alternatives, verifies the rational two-sided comparison, and produces the complete same-inverse physical census of the calibration control.

Enumeration in this unit is **not** a claim that all trees have been excluded. The report labels that distinction explicitly.

Runtime target: CPython 3.13.5, standard library only. Save as `h5_two_sided_method.py` and run without `-O`:

    python -B -S h5_two_sided_method.py

Expected mathematical markers are the 48,790 enumeration count, the exact comparison margins `2357/2291` and `-291/1916`, the identified VF at vertex 9, and the terminal marker `H5_TWO_SIDED_REFERENCE_METHOD_CONTROL_PASS`. The script emits source and report byte counts and SHA-256 values. I do not supply an invented newly inspected output pin.

```python
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import json

FACETS = ((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
          (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES = tuple(sorted({tuple(sorted((f[j],f[(j+1)%len(f)])))
                      for f in FACETS for j in range(len(f))}))
EF = tuple(tuple(k for k,f in enumerate(FACETS) if i in f and j in f)
           for i,j in EDGES)
ARROWS = tuple(sorted((i,j) for a,b in EDGES for i,j in ((a,b),(b,a))))
DUAL = tuple(sorted((i,j) for a,b in EF for i,j in ((a,b),(b,a))))

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return [x-y for x,y in zip(a,b)]
def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]
def outer(a,b): return [[x*y for y in b] for x in a]
def zero(): return [[F(0) for j in range(3)] for i in range(3)]
def eye(): return [[F(i==j) for j in range(3)] for i in range(3)]
def transpose(A): return [list(r) for r in zip(*A)]
def mv(A,x): return [dot(r,x) for r in A]
def mm(A,B): return [[dot(r,col) for col in zip(*B)] for r in A]
def add(A,B): return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(t,A): return [[t*x for x in row] for row in A]
def trace(A): return sum(A[i][i] for i in range(len(A)))
def pairing(A,B): return trace(mm(A,B))
def bil(x,A,y): return dot(x,mv(A,y))

def determinant(A):
    B=[list(map(F,r)) for r in A];n=len(B);answer=F(1)
    for k in range(n):
        j=next((j for j in range(k,n) if B[j][k]),None)
        if j is None:return F(0)
        if j!=k:B[j],B[k]=B[k],B[j];answer=-answer
        pivot=B[k][k];answer*=pivot
        for i in range(k+1,n):
            t=B[i][k]/pivot
            for j in range(k+1,n):B[i][j]-=t*B[k][j]
            B[i][k]=F(0)
    return answer

def inverse(A):
    n=len(A)
    B=[list(map(F,A[i]))+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        j=next(j for j in range(k,n) if B[j][k])
        B[k],B[j]=B[j],B[k];t=B[k][k];B[k]=[x/t for x in B[k]]
        for i in range(n):
            if i!=k:
                t=B[i][k];B[i]=[x-t*y for x,y in zip(B[i],B[k])]
    return [r[n:] for r in B]

def pd(A):
    assert A==transpose(A)
    assert all(determinant([r[:k] for r in A[:k]])>0 for k in (1,2,3))

def psd(A):
    assert A==transpose(A)
    for k in (1,2,3):
        for ix in combinations(range(3),k):
            assert determinant([[A[i][j] for j in ix] for i in ix])>=0

def vertices(theta):
    x,r,p,q,l=theta;s=1-l
    xy=((s/4,0),(s*(1-3*x/4),0),(s*(1-p),s*p),
        (s*q,s*(1-q)),(0,s*(1-3*r/4)),(0,s/4),(s/16,s/16))
    return [[F(a),F(b),F(0)] for a,b in xy]+[
        [F(0),F(0),F(1)],[l,F(0),F(1)],[F(0),l,F(1)]]

def moments(z,apex=None):
    o=[F(0)]*3 if apex is None else z[apex]
    D=F(0);K=[F(0)]*3;cells=[]
    for f in FACETS:
        if apex is not None and apex in f:continue
        for j in range(1,len(f)-1):
            a,b,c=[z[k] for k in (f[0],f[j],f[j+1])]
            d=dot(sub(a,o),cross(sub(b,o),sub(c,o)))
            if apex is not None:
                assert d>0;cells.append((apex,f[0],f[j],f[j+1],d))
            D+=d
            for k in range(3):K[k]+=d*(o[k]+a[k]+b[k]+c[k])/4
    return D,K,cells

def geometry(theta):
    z=vertices(theta);D,K,_=moments(z);D2,K2,cells=moments(z,7)
    assert D>0 and D==D2 and K==K2 and len(cells)==9
    g=[x/D for x in K];hull=set();poles=[];supports=[]
    for i,j,k in combinations(range(10),3):
        n=cross(sub(z[j],z[i]),sub(z[k],z[i]))
        if not any(n):continue
        v=[dot(n,sub(w,z[i])) for w in z]
        if min(v)>=0 or max(v)<=0:
            hull.add(tuple(t for t,a in enumerate(v) if a==0))
    assert hull=={tuple(sorted(f)) for f in FACETS}
    for f in FACETS:
        a,b,c=[z[i] for i in f[:3]];n=cross(sub(b,a),sub(c,a));h=dot(n,a)
        slack=[h-dot(n,w) for w in z]
        assert all(slack[i]==0 if i in f else slack[i]>0 for i in range(10))
        for j in range(len(f)):
            a,b,c=[z[f[(j+k)%len(f)]] for k in range(3)]
            assert dot(n,cross(sub(b,a),sub(c,b)))>0
        H=h-dot(n,g);assert H>0;poles.append([a/H for a in n])
        supports.append((n,h,slack))
    return z,D,g,poles,supports,cells

def rooted_trees():
    index={a:k for k,a in enumerate(ARROWS)};answer=[]
    for edges in combinations(EDGES,9):
        parent=list(range(10))
        def find(a):
            while parent[a]!=a:a=parent[a]
            return a
        for a,b in edges:
            a,b=find(a),find(b)
            if a==b:break
            parent[a]=b
        else:
            adj=[[] for i in range(10)]
            for a,b in edges:adj[a].append(b);adj[b].append(a)
            for root in range(10):
                pred={root:root};queue=[root]
                for a in queue:
                    for b in adj[a]:
                        if b not in pred:pred[b]=a;queue.append(b)
                assert len(pred)==10
                answer.append(tuple(sorted(index[i,pred[i]]
                                           for i in range(10) if i!=root)))
    assert len(answer)==48790 and len(set(answer))==48790
    return answer

def audit(z,g,poles,M):
    pd(M);N=inverse(M);pd(N);assert mm(M,N)==eye()
    X=[sub(v,g) for v in z]
    P={(i,j):bil(X[i],M,sub(X[j],X[i])) for i,j in ARROWS}
    Q={(i,j):bil(poles[i],N,sub(poles[j],poles[i])) for i,j in DUAL}
    U=[i for i in range(10) if all(v<0 for (a,b),v in P.items() if a==i)]
    S=[i for i in range(9) if all(v<0 for (a,b),v in Q.items() if a==i)]
    saddles=[];weak={}
    for (i,j),(a,b) in zip(EDGES,EF):
        vals=(P[i,j],P[j,i],Q[a,b],Q[b,a])
        if max(vals)<0:saddles.append((i,j))
        if max(vals)<=0 and any(v==0 for v in vals):
            pp=X[i] if P[i,j]==0 else (X[j] if P[j,i]==0 else None)
            k=a if Q[a,b]==0 else (b if Q[b,a]==0 else None)
            qq=None if k is None else [v/bil(poles[k],N,poles[k])
                                       for v in mv(N,poles[k])]
            if pp is not None and qq is not None:assert pp==qq
            point=tuple(pp if pp is not None else qq)
            kind='VF' if pp is not None and qq is not None else (
                 'VE' if pp is not None else 'EF')
            row=weak.setdefault(point,{'point':point,'kind':kind,'edges':[]})
            row['edges'].append((i,j))
            if kind=='VF':row['kind']='VF'
    if not weak:assert len(S)+len(U)-len(saddles)==2
    return {'M':M,'N':N,'S':S,'U':U,'H':saddles,'weak':list(weak.values()),
            'primal':[(i,j,P[i,j]) for i,j in ARROWS],
            'polar':[(i,j,Q[i,j]) for i,j in DUAL],
            'zeros':sum(v==0 for v in list(P.values())+list(Q.values()))}

def raw_arrow_stress(X,weights):
    out=zero()
    for i,j,w in weights:
        assert (i,j) in ARROWS and w>=0
        e=sub(X[j],X[i]);A=add(outer(X[i],e),outer(e,X[i]))
        out=add(out,scale(-F(w)/2,A))
    return out

def single_certificate(C,ell,cap,Q,t,Y,Z):
    pd(C);psd(Y);psd(Z);CI=inverse(C)
    assert Q==add(scale(t,C),add(Y,scale(-1,Z)))
    delta=t+ell*pairing(CI,Y)-cap*pairing(CI,Z)
    assert delta>0
    return delta

def pooled_certificate(C0,Q,delta,terms):
    pd(C0);assert delta>0;out=scale(delta,C0)
    for C,ell,cap,Y,Z in terms:
        pd(C);psd(Y);psd(Z);CI=inverse(C)
        G=add(Y,scale(-ell*pairing(CI,Y),C))
        G=add(G,add(scale(cap*pairing(CI,Z),C),scale(-1,Z)))
        out=add(out,G)
    assert out==Q

def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    return x

def main():
    assert len(EDGES)==17 and len(ARROWS)==len(DUAL)==34
    assert all(len(f)==2 for f in EF)
    theta=tuple(map(F,('3/20','3/20','3/20','9/20','3/25')))
    z,D,g,poles,supports,cells=geometry(theta)
    assert D==F(102241,125000)
    assert g==[F(184058311,817928000),F(173571241,817928000),
               F(119041,408964)]
    h=1-g[2];m=[-g[0],theta[4]-g[1]]
    W=[[F(2215,10000),F(-1288,10000)],
       [F(-1288,10000),F(2146,10000)]]
    assert determinant(W)==F(1547223,50000000)>0
    C=[[W[i][j]+m[i]*m[j] for j in range(2)]+[h*m[i]] for i in range(2)]
    C.append([h*m[0],h*m[1],h*h]);pd(C);CI=inverse(C)
    a=m+[h];assert a==sub(z[9],g)
    assert mv(CI,a)==[F(0),F(0),1/h] and bil(a,CI,a)==1
    Q=add(scale(7,C),scale(-8,outer(a,a)));B=mm(CI,Q)
    assert trace(B)==13 and determinant(B)==-49
    assert mm(add(B,scale(-7,eye())),add(B,eye()))==zero()
    ell=F(125,2291);cap=F(1710,2291);alpha=F(125,1916)
    Z=scale(8,outer(a,a));Y=zero()
    delta=single_certificate(C,ell,cap,Q,F(7),Y,Z)
    assert delta==F(2357,2291)
    pooled_certificate(C,Q,delta,[(C,ell,cap,Y,Z)])
    T=add(Q,scale(alpha*trace(B),C));v=mv(CI,a)
    assert bil(v,T,v)==F(-291,1916)<0
    physical=audit(z,g,poles,CI)
    assert physical['N']==C
    vf=next(w for w in physical['weak'] if tuple(w['point'])==tuple(a))
    assert vf['kind']=='VF'
    assert (7,9) in vf['edges'] and (8,9) in vf['edges']
    trees=rooted_trees()
    tree_raw=json.dumps(trees,separators=(',',':')).encode()
    report={'identity':'H5_TWO_SIDED_REFERENCE_METHOD_CONTROL_V1',
      'scope':'Method comparison and actual weak physical control. No all-root exclusion.',
      'theta':theta,'vertices':z,'facets':FACETS,'edges':EDGES,'edge_facets':EF,
      'volume':D/6,'actual_centroid':g,'supports':supports,'positive_apex_fan':cells,
      'poles':poles,'C':C,'Q_formal_not_claimed_as_root_stress':Q,
      'two_sided_margin':delta,'old_shift_negative_rayleigh':F(-291,1916),
      'physical_control':physical,'rooted_trees_enumerated_only':len(trees),
      'tree_list_sha256':hashlib.sha256(tree_raw).hexdigest()}
    raw=(json.dumps(enc(report),sort_keys=True,indent=2)+'\n').encode()
    Path('h5_two_sided_method_report.json').write_bytes(raw)
    source=Path(__file__).read_bytes()
    print('SOURCE',len(source),hashlib.sha256(source).hexdigest())
    print('REPORT',len(raw),hashlib.sha256(raw).hexdigest())
    print('ENUMERATED_ONLY',len(trees))
    print('MARGINS',delta,F(-291,1916))
    print('H5_TWO_SIDED_REFERENCE_METHOD_CONTROL_PASS')

if __name__=='__main__':main()
```

## 9. Most useful continuation

The immediate continuation is to use the **raw two-sided packet functional**, rather than the old floor-shift PD test, on the full blind box. Where one reference still leaves packets uncovered, use the homogeneous pooled certificate (4), with exactly one physical normalization and exact regional bounds for every added reference. A proven feasible full-tree SDP matrix should be retained as an actual U1 control and audited with its literal inverse; a failed stress proposal should not be given that status. The pending snapshot may shorten this replay, but only completed exact geometry and all-root checks justify a new regional registry entry.
