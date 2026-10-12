# material-a2edffd255ed

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# RECIPROCAL_ONE_CURVE_HULL_V1
## Recovery capsule part 1/2: complete analytical derivation

Coordinator result. No historical-priority claim. This is a theorem about the exact convex hull of a bounded normalized reciprocal PAIR, not a homogeneous-polyhedron construction or a whole E17 exclusion. Accepted mechanical bounds remain34<=C_min<=622. Deliver both parts for computational use; part2 is the complete3798-byte source, with no external data.

The earlier equal-gap proof [internal-source-reference], SHAbdc9e45a6d95b687c51dfa89cb99db370748f61a95561be9c962f7f4007aeddd, was read completely. Its three-effect lemma is re-proved here, and the new frontier theorem below does not require its polynomial table. The asymmetric precursor was read completely in archived coordinator output [internal-source-reference], SHA6684a1711cbfb3da000e6a950b9462e25c01ec07da57e0c078b51d00839b67e7. That precursor shows, for p>q>=4, that no FINITE collection of genuine reciprocal spectral orbits generates the whole capped PAIR hull. The ONE-CURVE theorem is compatible with this obstruction, not a single-corner claim.

## 1. Universal strict-saddle theorem

Let n>=3, A be real SPD with trA=1, eta=1/tr(A^-1), and B=eta A^-1. For fixed symmetric Q,R let f(A)=tr(QA)+tr(RB). A nonconstant such functional has NO local minimum or maximum on the open trace-one SPD manifold. In fact EVERY stationary point is a strict saddle.

Write r0=tr(RB), T=R-r0 I, C=A^(-1/2) T A^(-1/2). Then trC=0. Direct differentiation on a trace-zero symmetric direction H gives

 df[H]=tr([Q-eta A^-1 T A^-1]H).

Thus at a stationary point Q=eta A^-1 T A^-1+mu I. Put Z=A^(-1/2) H A^(-1/2). Differentiating the quotient tr(RA^-1)/tr(A^-1) a second time gives

 d2f[H,H]=2eta[tr(C Z^2)-tr(BZ)tr(CZ)].             (1)

This second-derivative formula holds whether or not the first derivative vanishes; the linear Q term has zero Hessian.

For any unit vector v put t=v^T A v, Z=vv^T-t I, H=A^(1/2) Z A^(1/2). Then trH=0 and (1) reduces exactly to

 d2f[H,H]=2eta(v^T C v)[1-v^T(A+B)v].              (2)

The factor in square brackets is STRICTLY positive. Indeed A and B commute. For an eigenvalue a_i of A, set s=sum_(j!=i)a_j and t_i=sum_(j!=i)1/a_j. Since trA=1, the inequality a_i+eta/a_i<1 is equivalent to s*t_i>1. Cauchy-Schwarz gives s*t_i>=(n-1)^2>1. Hence A+B<I.

If C is nonzero, its zero trace gives both positive and negative quadratic directions. Equation(2) therefore gives Hessian directions of both signs. If C=0, R is scalar, and stationarity forces Q scalar, so the entire functional is constant. This proves the theorem, including the scalar exception. For n=2, A+B=I and the theorem does not apply.

A useful equivalent consequence: the image pair of ANY point is an interior point of the convex hull of EVERY sufficiently small open neighborhood of that point, relative to the affine space trA=trB=1. Otherwise a supporting affine functional would have a local minimum there. The same argument shows that this local hull has full affine dimension n(n+1)-2: a nontrivial affine dependence on an open patch would also be a local extremum.

## 2. Localization on the genuine spectral boundary

Now n=3. Write the ordered eigenvalues of A as

 (rt,t,1)/(rt+t+1), r>=1,t>=1.

The corresponding paired eigenvalues of B, in the SAME ordered basis, are

 (1,r,rt)/(rt+r+1).

For p>=q>1 define R_(p,q) by r<=p,t<=q, and H_(p,q)=conv R_(p,q). The reciprocal set is compact and uniformly SPD. Its boundary in the trace-one SPD manifold consists precisely of the two cap walls r=p OR t=q. A repeated-eigenvalue wall r=1 or t=1 is NOT a boundary of this constrained manifold when both cap inequalities are strict.

By Section1, a nonconstant linear pair functional attains its minimum on one of the two actual cap walls. Constant functionals are immaterial. Compact convex sets are determined by all their linear minima. Therefore H_(p,q) is exactly the convex hull of those TWO one-parameter orthogonal-orbit families. No generic-eigenvalue assumption is used.

## 3. Absorption of one entire wall when p>=q>=2

Set Pc=pq+q+1, Qc=pq+p+1. The corner pair has paired eigenvalue points

 c0=(pq/Pc,1/Qc), c1=(q/Pc,p/Qc), c2=(1/Pc,pq/Qc).

On r=p, put P=pt+t+1,Q=pt+p+1,1<=t<=q. The three paired points have barycentric coordinate columns

 w_i=C0^-1 (Pc*a_i,Qc*b_i,1)^T,
 C0=[[pq,q,1],[1,p,pq],[1,1,1]],
 a=(pt,t,1)/P, b=(1,p,pt)/Q.

Here detC0=-(p-1)(q-1)(pq-1), so these coordinates are unique. Let W have rows w_i^T. Every row sums to1. Since trA=trB=1, summing the defining three equations over i shows that every column also sums to1. Thus it remains to prove all nine entries nonnegative.

Use the positive denominator factors, independent of row,

 D0=(p-1)(pq-1)PQ,
 D1=(p-1)(q-1)PQ,
 D2=(q-1)(pq-1)PQ.

Each N_ij=D_j W_ij is a degree-at-most-two polynomial in t. Substitute t=1+(q-1)x and express it in degree-two Bernstein form on0<=x<=1. The six off-diagonal numerators can also be read directly:

 N01=p(p-t)(q-t),
 N02=p(q-t)(pqt-pt-p+qt+q-1),
 N10=p(q-t)(p^2t-1),
 N12=(q-t)(p^3qt+p^2qt+p^2q-pt-p-1),
 N20=p(p+1)(p-t)(q-t),
 N21=(p+1)(q-t)(p^2t-1).

The diagonal Bernstein triples are

 00: (p-1)(2p^3q+3p^2q-3p-2);
     (3p^4q^2+p^4q+p^3q^2+p^3q-3p^2q^2-6p^2q-3p^2+pq+p+q+3)/2;
     (p-1)(pq-1)QcPc.
 11: (p-1)(p+1)^2(q-1);
     (q-1)(2p^3q+p^3+p^2q+3p^2-3pq-p-q-2)/2;
     (p-1)(q-1)QcPc.
 22: (q-1)(p^3q+2p^2q-2p-1);
     (q-1)(2p^3q^2+p^3q+3p^2q^2+2p^2q-2pq-3p-q-2)/2;
     (q-1)(pq-1)QcPc.

Every coefficient of every one of the27 Bernstein entries becomes nonnegative on expanding p=2+v+u,q=2+v with u,v>=0. Part2 derives all27 entries directly from C0^-1, reconstructs their ENTIRE symbolic polynomials, and checks every rational coefficient of these two-variable expansions. The respective positive-coefficient counts are

 20,25,30,9,5,0,11,15,0,14,18,0,14,18,22,18,22,0,14,9,0,14,18,0,18,22,26.

Thus this is a finite exact polynomial-identity/positivity certificate for the continuum p>=q>=2, not a sample grid. Bernstein weights are nonnegative, proving W>=0 throughout the whole wall.

A doubly stochastic matrix is a convex combination of permutations: its positive-support bipartite graph has a perfect matching by the row/column sum condition and Hall's counting argument; subtract the smallest matching entry, rescale the remainder, and iterate until the number of positive entries decreases to a permutation. Applying this simultaneously to the paired eigenvalue points proves that the ENTIRE r=p wall lies in the convex hull of the SINGLE corner(p,q) orthogonal orbit.

The range assumption is real: for p=2,q=6/5,t=1, W02=-1/70. That exact control does not show the strongest possible threshold, but prevents extending this proof to every q>1.

## 4. Exact one-curve hull and its strict interior

THEOREM. For real Sym3 and p>=q>=2,

 H_(p,q)=conv { (O diag(rq,q,1) O^T/P_r,
                 O diag(1,r,rq) O^T/Q_r):
                  q<=r<=p, O orthogonal },          (3)

where P_r=rq+q+1,Q_r=rq+r+1.

Proof: Section2 reduces the hull to r=p and t=q. Section3 absorbs r=p into the corner(p,q), already in(3). On t=q with1<=r<=q, invert the normalized pair, interchanging A and B and reversing the basis. This changes the two adjacent ratios from(r,q) to(q,r). Apply Section3 with p=q: the entire r=q wall is absorbed into the corner(q,q). That corner is invariant under interchanging A,B up to the reversed basis, so the original t=q,r<=q portion is also absorbed there. The remaining t=q,q<=r<=p portion is exactly(3). Every generator in(3) is an actual member of the capped set, giving both inclusions. This proof does not require an independent equal-gap table.

For STRICT caps r<p,t<q, the convex hull is exactly int H_(p,q), relative to trA=trB=1. Each strict pair is interior by Section1 and a small allowed neighborhood. Strict pairs are dense in the closed set: raise every eigenvalue ratio to a power s<1 and let s increase to1, keeping the eigenbasis. Therefore their convex hull is convex and dense in H. In finite dimensions a convex dense subset of a full-dimensional convex body contains its interior: surround an interior point by a sufficiently small simplex and approximate its vertices within the dense convex subset. The point stays in that simplex's convex hull. This proves the reverse inclusion.

Consequently a nonconstant affine functional that is nonnegative on the closed hull is strictly positive at every actual strict-cap pair, even if its minimum on the hull is zero. Constant-zero functionals give no such conclusion.

## 5. Exact one-dimensional family of three-effect SDPs

For fixed r, let a_i,b_i be the three corner coefficients in(3). The orbit hull is precisely

 A=sum_i a_i X_i, B=sum_i b_i X_i,
 X_i>=0, trX_i=1, sum_i X_i=I.                    (4)

Here arbitrary X_i need not commute. To prove exactness, an extreme triple with all three ranks>=2 has at least9 supported symmetric perturbation dimensions but at most8 independent affine equations (matrix sum and three traces, with one redundancy). It is not extreme. If one component has rank1, trace1 makes it a projector. The other two annihilate its range by positivity and sum to I on the orthogonal2-plane. They commute there and have complementary trace-one spectra; unless both are rank-one projectors they admit a nontrivial convex decomposition. Conversely an orthogonal rank-one partition is extreme by its fixed ranges and traces. Compactness gives(4).

For symmetric Q,R define the three quadratic matrix polynomials

 K1(r)=rq Q_r Q+P_r R,
 K2(r)=q Q_r Q+r P_r R,
 K3(r)=Q_r Q+rq P_r R.                             (5)

Then P_r Q_r times the minimum of tr(QA)+tr(RB) on the fixed-r orbit equals

 min sum_i tr(K_i X_i), with the constraints(4).

Its dual is max trW+z1+z2+z3 subject to K_i-W-z_i I>=0. The primal has the strict feasible triple I/3 and a compact feasible set; standard finite-dimensional SDP strong duality therefore gives an attained dual optimum. Background reference only: L.Vandenberghe and S.Boyd, Semidefinite Programming, SIAM Review38(1),49-95(1996), author's publication page at Stanford. No novelty claim is made for SDP duality or the Bernstein basis.

For genuine centred primal and same-origin polar arrows, take Q=sum lambda_ij[-sym(x_i(x_j-x_i)^T)], R=sum mu_fg[-sym(q_f(q_g-q_f)^T)], with nonnegative weights. In an actual covariance gauge C, the physical normalized objective has Qtilde=C^-1/2 Q C^-1/2, Rtilde=C^1/2 R C^1/2. A square-root-free certificate replaces the three costs in(5) by

 rq Q_r Q+P_r C R C,
 q Q_r Q+r P_r C R C,
 Q_r Q+rq P_r C R C,

and uses constraints K_i-W0-z_i C>=0, objective tr(C^-1 W0)+sum z_i. This retains ONE M and its actual inverse; C is the actual covariance, not a separately recentered polar covariance. Clearing detC>0 is exact when desired.

## 6. Complete rational Bernstein hierarchy for STRICT linear separation

Assume p>q>=2, all input matrices Q,R and endpoints p,q rational. A finite certificate consists of rational polynomial W(r), rational scalar polynomials z_i(r), and a rational delta>0 such that, on rescaling [q,p] to[0,1], ALL coefficients in a common finite-degree Bernstein representation satisfy

 coefficients of K_i-W-z_i I are PSD,
 coefficients of trW+sum z_i-delta P_r Q_r are nonnegative.   (6)

Then weak duality and(3) prove tr(QA)+tr(RB)>=delta on the ENTIRE capped reciprocal set. Exact coefficient PSD tests use all principal minors, or an exact PSD factorization; leading minors alone only suffice for a strictly positive definite test. The square-root-free covariance version replaces I by C and trW by tr(C^-1W0).

COMPLETENESS: such a certificate exists whenever this functional has a STRICTLY positive minimum on H_(p,q). This is completeness of the hierarchy for positive-gap linear separation, not of any fixed degree or of the physical nonlinear feasibility problem.

Proof in full: At each r0, attained SDP duality gives W,z with positive objective and semidefinite slacks. Lower W by a sufficiently small positive multiple of I. This makes every slack positive definite while losing only three times that small multiple in the objective, so the objective remains positive. The same constant witness works with strict margins in a neighborhood of r0, by continuity of K_i and P_rQ_r. Approximate that witness by rational entries closely enough to retain these strict margins. Compactness gives a finite cover by such rational constant witnesses. A continuous piecewise-linear partition of unity with rational breakpoints subordinate to a refinement of this interval cover yields continuous piecewise-linear W,z with rational coefficients, positive definite slacks and a uniformly positive objective. Convex combination is legitimate pointwise because the constraints and objective are affine in the witnesses. Uniform compactness makes all these margins positive.

Bernstein approximation of each continuous witness entry by sum_j f(j/N) binom(N,j)x^j(1-x)^(N-j) converges uniformly. Here the sampled piecewise-linear values are rational, so the approximating polynomials are rational. Uniform closeness preserves strict matrix and scalar margins. Choose a sufficiently small rational delta>0, leaving all expressions in(6) STRICTLY positive on the interval.

Finally every fixed strictly positive polynomial matrix on a compact interval has positive definite Bernstein coefficients after enough degree elevation. An elementary proof is the exact coefficient formula: for F(x)=sum_(k=0)^d C_k x^k, its degree-N Bernstein coefficient at j is sum_(k<=j) C_k binom(j,k)/binom(N,k). Uniformly over0<=j<=N, binom(j,k)/binom(N,k) tends to(j/N)^k for each fixed k. Hence the coefficient matrices converge uniformly to F(j/N); their positive minimum eigenvalue makes them positive definite eventually. The same argument covers the scalar objective. This proves finite termination of the existence hierarchy for any strict separator.

For p=q, the interval is one point and Section5 alone is the exact SDP. For zero minimum, (6) remains a sufficient nonnegative certificate with delta=0 but this completeness argument does NOT apply. For example a polynomial with an interior zero need not acquire nonnegative Bernstein coefficients at any finite degree. Do not extend the positive-gap claim to weak separation by assertion.

## 7. Mechanical scope and next use

The finite-height first-layer caps from the accepted physical source can be specialized with p=7024915/1000000,q=6832329/1000000, which satisfy p>q>=2. This specialization uses the earlier actual-covariance simultaneous S1/U1 theorem, not U1 alone. The new theorem itself is purely matrix-algebraic and valid for any p>=q>=2.

At a FIXED actual geometry, infeasibility of the CLOSED capped joint-linear arrow relaxation has a positive separating combination of the finitely many weak arrow rows, by compact convex separation. Rational coefficients may be chosen sufficiently close if all geometric data are rational. Sections5–6 then furnish an exact finite rational certificate. Both Q and R require at most6 cone generators each by the6-dimensional symmetric-matrix cone version of Caratheodory; this is a relaxation certificate bound, not a number of physical equilibria.

The image of actual reciprocal metrics remains a proper NONCONVEX subset of this hull. Passing its best possible linear relaxation is not a body, a reciprocal pair, a strict U/S root, or proper110. No geometry sector has yet been forced to fail this new hierarchy. The next useful task is an actual E17 packet or whole genuine shape-cell exclusion with actual moving COM/covariance, not another purely formal spectral counterexample. Lower prohibition and attaining construction remain separate.

## 8. Recovery and author execution

Part2 contains the complete literal reciprocal_frontier.py,3798bytes,SHA256 d67f33c69b3bb307329e704ec599dae3ed2cb08a2e2fc31adb75c382f881ae6d. It has all symbolic inputs, denominator rules, degree-two Bernstein conversion, coefficient-sign checks and a strict-saddle scalar identity. Python>=3.10 and SymPy1.14.0; author executed CPython3.13.5/SymPy1.14.0. No random seeds, external files or hidden parameters.

Save with UTF-8/LF and the final newline, then run in a fresh directory:
 python -B reciprocal_frontier.py build .
 python -B reciprocal_frontier.py check .

Both author runs produced exactly:
 RECIPROCAL_FRONTIER_EXACT_PASS 2741 7aca43abb79f656a99dfec0b302e66d2e9ec5cb2b2a26815554fb93f1e3111a1

The regenerated reciprocal_frontier.json is2741bytes with that SHA256. The exact program checks continuum polynomial identities and coefficient signs. The strict-saddle proof, convex-hull support argument, three-effect extremal argument and hierarchy completeness are analytical derivations, not established by samples or code. No independent second-author replay or proof-assistant formalization is claimed.
