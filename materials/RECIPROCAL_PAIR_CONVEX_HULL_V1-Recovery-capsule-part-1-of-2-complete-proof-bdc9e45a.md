# material-bdc9e45a6d95

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# RECIPROCAL_PAIR_CONVEX_HULL_V1
## Recovery capsule part 1/2: complete proof and exact joint-arrow separation

Coordinator analytical advance. The normalized reciprocal PAIR has an exact three-LMI convex hull in real dimension three. This strictly strengthens the preceding SUM-only and independent one-sided relaxations. It does NOT identify convex-hull feasibility with a physical reciprocal metric, prove an E17 exclusion, change a canonical registry count, or construct110. The accepted mechanical interval remains34<=C_min<=622. The algebraic verification/control source is in companion part2; preserve and deliver BOTH parts for computational continuation.

Read source premises: [internal-source-reference], RECIPROCAL_NORMALIZED_SUM_BUDGET_V1 part1, SHA9602faff6f074210688078e47506926d0cfe8984ea82817735b80ff5bad3fc69; and [internal-source-reference], actual-covariance theorem, SHAe43bdb2b1745cf265601df70863e60face5ee25d5ebc4e36d120c8d361bed173. Both read completely. No old worker computation is replayed or renamed here. The new proof below is self-contained except the explicitly identified actual-S=U1=>adjacent-ratio9 specialization. No historical-priority claim is made.

## 1. Exact statement
Let Sym3 be the real symmetric3x3 matrices. For M>0 and an arbitrary SPD preconditioner C define
 A=C^(1/2) M C^(1/2)/tr(CM),
 B=C^(-1/2) M^(-1) C^(-1/2)/tr(C^(-1)M^(-1)).
Then trA=trB=1 and B=A^(-1)/tr(A^(-1)). Keep BOTH normalizing traces. Put k>1 and d=k^2+k+1. Let R_k be the set of these pairs whose ordered consecutive eigenvalue ratios of A are<=k.

THEOREM: conv(R_k) is EXACTLY the set D_k of pairs with trA=trB=1 and
 (i)  A+B <= (k^2+1)I/d,
 (ii) kA+B >= k(k+1)I/d,
 (iii) A+kB >= k(k+1)I/d.
These three matrix inequalities already imply A,B>0. No separate commutation or reciprocity equation is imposed on D_k. The convex hull for ratios strictly<k is exactly the relative interior, obtained by making all three inequalities strict.

For unrestricted SPD, the convex hull is exactly
 trA=trB=1, A>0, B>0, I-A-B>0.
Its closure replaces the three strict PSD inequalities by nonstrict ones. This is dimension-three-specific.

In the actual uniform-polyhedron S=U1 covariance gauge C=Sigma, the accepted covariance theorem gives k=9 strictly. Therefore
 A+B <82I/91,
 9A+B >90I/91,
 A+9B >90I/91.
This physical specialization is NOT U1-only and does not use the polar's own volume covariance.

## 2. Complete scalar proof of the three inequalities
The sum inequality can be proved directly. For a selected eigenvector, rescale its eigenvalue to1 and write the other two x,y>0. Its A+B eigenvalue is
 f(x,y)=1/(1+x+y)+xy/(x+y+xy).
The exact identities are
 1-f(x,y)=(x^2+xy+y^2)/[(1+x+y)(x+y+xy)],
 f(x,x^2)-f(x,y)=(x^2-y)^2/[(1+x+y)(1+x+x^2)(x+y+xy)],
 (k^2+1)/d-f(x,x^2)=(k-x)(kx-1)/[d(x^2+x+1)].
Choose x to be an adjacent ordered neighbor, so1/k<=x<=k. All denominators are positive. This proves (i), strictly when consecutive ratios are<k, and the unrestricted upper bound.

For (ii), scale the ordered eigenvalues of A before trace normalization to(uv,u,1),1<=u,v<=k. Set P=uv+u+1,Q=uv+v+1. The three eigenvalues of d(kA+B)-k(k+1)I, multiplied by the positive PQ, are
 N1=d(k uv Q+P)-k(k+1)PQ,
 N2=d(k u Q+vP)-k(k+1)PQ,
 N3=d(k Q+uvP)-k(k+1)PQ.
Put u=1+(k-1)x,v=1+(k-1)y,0<=x,y<=1. Each Ni equals (k-1)^2 times a bidegree(2,2) Bernstein polynomial. Rows below are i=0,1,2; entries within each row j=0,1,2. The coefficient multiplies binom(2,i)x^i(1-x)^(2-i)binom(2,j)y^j(1-y)^(2-j).

For N1/(k-1)^2:
 [3(k+1), (5k^2+8k+5)/2, (k+1)(2k^2+3k+2)]
 [(4k^2+7k+4)/2, (k+1)(7k^2+8k+7)/4, d(3k^2+5k+3)/2]
 [(k+1)^3, (k+1)^2 d, (k+1)d^2].
For N2/(k-1)^2:
 [3(k+1), (k+2)(2k+1)/2, k(k+1)]
 [(4k^2+7k+4)/2, (k+1)(3k^2+4k+3)/4, kd/2]
 [(k+1)^3, d^2/2, 0].
For N3/(k-1)^2:
 [3(k+1), (k+2)(2k+1)/2, k(k+1)]
 [(k^2+4k+1)/2, (k+1)^3/4, 0]
 [k(k+1), kd/2, 0].

All24 nonzero coefficients are manifestly positive for k>1; the other3 are zero. Every Ni is strictly positive for u,v<k because the positive00 term then has positive Bernstein weight. These are polynomial identities, not a sample of k or a numerical grid proof. Companion stdlib code reconstructs each entire polynomial over Q[k,x,y] and checks zero residual. This proves (ii). Apply the same result to normalized B, whose adjacent ratios are reversed but have the same bound, to obtain (iii).

## 3. The dimension-three trace-one matrix partition lemma
Let T be the compact convex set of triples X,Y,Z>=0 with
 X+Y+Z=I, trX=trY=trZ=1.
Its extreme points are EXACTLY the triples of mutually orthogonal rank-one projectors.

Proof: Suppose all three ranks are>=2. The vector space of supported symmetric perturbations of a rank-r PSD matrix has dimension r(r+1)/2. Thus the three supported perturbation spaces together have dimension>=9. The constraints deltaX+deltaY+deltaZ=0 and the three zero traces impose at most6+3-1=8 independent linear conditions, since the trace of the sum is redundant. There is a nonzero supported perturbation satisfying all constraints. A sufficiently small perturbation of either sign preserves PSD: on each fixed range the positive eigenvalues have a positive minimum. Hence the triple is not extreme.

An extreme point must therefore have, say, rankX=1. Trace1 makes X a rank-one projector. Positivity and Y+Z=I-X imply that Y and Z annihilate its range. On the orthogonal2-plane they sum to the identity and both have trace1. They commute and have eigenvalues(theta,1-theta) and(1-theta,theta),0<=theta<=1. If0<theta<1 the triple is a nontrivial convex combination of two orthogonal rank-one partitions. Thus at an extreme point theta is0or1. Conversely a triple of orthogonal rank-one projectors is extreme, since a PSD convex decomposition of each rank-one component has the same range and trace and is identical. Compact finite-dimensional convexity proves T is their convex hull.

The argument explicitly handles noncommuting interior triples; no simultaneous diagonalization of arbitrary X,Y,Z is assumed. It uses real Sym3. The corresponding complex proof has supported dimension r^2 and the same rank conclusion, but no complex generalization is required here.

## 4. Affine equivalence and exactness of the pair hull
For any (A,B) in D_k define
 X=[d(kA+B)/(k+1)-kI]/(k-1)^2,
 Y=[(k^2+1)I-d(A+B)]/(k-1)^2,
 Z=[d(A+kB)/(k+1)-kI]/(k-1)^2.
The three LMIs are precisely X,Y,Z>=0. Direct algebra gives X+Y+Z=I and each trace1. The inverse affine map is
 A=(k^2X+kY+Z)/d,
 B=(X+kY+k^2Z)/d.
In particular A,B>=I/d>0.

By the lemma, every triple is a convex combination of orthogonal rank-one partitions. On each such partition, A has the geometric spectrum(k^2,k,1)/d and B has the reverse spectrum(1,k,k^2)/d in the SAME basis. These are genuine normalized reciprocal pairs in R_k. This proves D_k subset conv(R_k). Section2 gives the opposite inclusion. By Caratheodory, at most11 endpoint pairs suffice in this10-dimensional affine pair space; an explicit decomposition is not needed for the separation certificate.

All strict-ratio pairs lie in int(D_k) by section2. Conversely, if(A,B) is in int(D_k), continuity of the three strict LMIs permits a k' with1<k'<k sufficiently close to k such that(A,B) is in D_k'. Its endpoint pairs have ratios k'<k. This proves the relative-interior assertion, not just density.

For unrestricted SPD, A,B,I-A-B are positive. Conversely every such pair belongs to D_k for sufficiently large k: (i) tends to A+B<I, while (ii) and(iii), after division by k, tend to A>0 and B>0. Finite-k exactness therefore proves the unrestricted open-hull assertion. Closing gives the PSD version. Equivalently its extreme points are orthogonal pure pairs, approached by spectrum(1,t,t^2) as t->0.

## 5. Exact joint-linear optimization and square-root-free arrow certificates
For symmetric H,G, the strongest lower bound on
 Phi=tr(AH)+tr(BG)
over the closed ratio-k reciprocal set equals the following SDP, not merely a SUM-only lower bound:
 d minPhi = min {tr(XF1)+tr(YF2)+tr(ZF3): (X,Y,Z) in T},
 F1=k^2H+G, F2=k(H+G), F3=H+k^2G.
Exactness follows from the full pair hull; the minimum can be attained at one orthogonal rank-one partition. The SDP has the strictly feasible triple I/3,I/3,I/3. Its dual is
 maximize tr(W)+z1+z2+z3,
 subject to F_i-W-z_i I>=0 for i=1,2,3.
Consequently there is no duality gap; strict primal feasibility and compactness give a dual optimal certificate.

For true primal and same-origin polar arrows put
 Qij=-sym[x_i(x_j-x_i)^T], Rfg=-sym[q_f(q_g-q_f)^T].
Take Q=sum lambda_ij Qij,R=sum mu_fg Rfg with nonnegative weights. All selected weak arrows for one physical M and its inverse imply tr(MQ)<=0,tr(M^(-1)R)<=0, hence Phi<=0 for
 H=C^(-1/2)Q C^(-1/2), G=C^(1/2)R C^(1/2).

A square-root-free exact certificate uses a symmetric W0 and scalars z1,z2,z3 with
 k^2 Q+C R C-W0-z1 C>=0,
 k(Q+C R C)-W0-z2 C>=0,
 Q+k^2 C R C-W0-z3 C>=0,
 L=tr(C^(-1)W0)+z1+z2+z3>0.
Then every reciprocal candidate has Phi>=L/d>0, contradicting the weak arrows. The PSD checks require ALL principal minors. With C rational, multiply the scalar inequality by detC>0:
 tr(adj(C)W0)+(z1+z2+z3)detC>0.
No square-root data, inverse-variable independence or coefficient signs outside the stated nonnegative arrow weights are concealed. For fixed actual C these are linear matrix inequalities in Q,R,W0,z.

A zero bound L=0 also excludes strict-ratio metrics if the resulting linear functional is nonconstant on trA=trB=1: a nonconstant functional cannot attain its minimum at an interior point of D_k. This means H and G are not BOTH scalar matrices. If both are scalar and their constants sum to0, the functional is identically zero and gives no exclusion; do NOT drop this exception. A positive constant functional already excludes by the positive-gap rule.

At fixed actual geometry, infeasibility of the CLOSED D_k relaxation for all chosen weak-arrow inequalities admits such a positive-gap separation after choosing nonnegative arrow weights. This is compact convex separation, and the displayed SDP dual supplies its certificate. Each of Q,R can be represented with at most6 arrow generators by conic Caratheodory in Sym3. This gives at most12 total arrows for this relaxation certificate; it is NOT a count of equilibrium contacts or a claim that every true reciprocal infeasibility is detected.

For the unrestricted pair hull use T with X=A,Y=I-A-B,Z=B and costs F1=H,F2=0,F3=G, with no d factor. This yields an exact unrestricted joint-linear relaxation as well.

## 6. Two exact formal controls and the remaining boundary
FIRST control proves that the new conditions are not consequences of the old constraints even when each independent matrix satisfies the exact ratio bound:
 A=diag(1,8,31)/40,
 B=diag(10,26,4)/40.
Both have trace1, positive eigenvalues, consecutive ratios<9, and every eigenvalue lies strictly between1/91 and81/91. Their SUM diag(11,34,35)/40 lies strictly between18I/91 and82I/91. Yet the first diagonal entry of9A+B is19/40<90/91, a violation of1871/3640.
With H=9e1e1^T-(45/91)I and G=e1e1^T-(45/91)I, both individual contractions tr(AH),tr(BG) are strictly negative, while every strict-ratio reciprocal pair makes their sum strictly positive. This is a FORMAL spectral separator, not a realized polyhedron or a true-arrow support packet.

SECOND control proves that the exact hull is still a relaxation of reciprocity. Put w=(1,2,3), O=I-ww^T/7, an exact rational orthogonal reflection. Let A0=diag(81,9,1)/91 and B0=diag(1,9,81)/91, and set
 A=(A0+O A0 O)/4+I/6,
 B=(B0+O B0 O)/4+I/6.
Its corresponding X,Y,Z are (P_i+O P_i O)/4+I/6, hence all positive. Thus this pair lies strictly inside D_9, the convex hull even of STRICT ratio9 reciprocal pairs. But [A,B]01=5760/405769 !=0, so A and B are NOT normalized reciprocals. The companion checker verifies the exact commutator. No test consisting only of affine inequalities in normalized A,B can remove this point. Nonlinear reciprocity/geometry can remain necessary after the optimal joint-linear step.

## 7. Reproducible algebra and scope of execution
Companion part2 contains complete reciprocal_pair.py and the small original SymPy exploration unit explore.py. Save their fenced contents with UTF8/LF and the final newline. In a fresh directory run
 python -B -S reciprocal_pair.py build
 python -B -S reciprocal_pair.py check
Expected exact marker:
 RECIPROCAL_PAIR_EXACT_PASS 1370 89424339a0b4208d0cac18e30e84ce85e9cc177e3582ba2c47592800a05d1a45
Pins:
 reciprocal_pair.py6139 bytes SHA7071b25cdd1bcd3efde82d54fcb48aa959e1510f89a4fa37976e261aa7545980;
 reciprocal_pair.json1370 bytes SHA89424339a0b4208d0cac18e30e84ce85e9cc177e3582ba2c47592800a05d1a45;
 explore.py651 bytes SHAf82ebb39473a34f81bdc6a50b1d80692a27e9879fd86ef0a15fcc4327b1f8c11.
Coordinator executed build and check in CPython3.13.5 stdlib. The source supports Python>=3.10. Optional discovery command python explore.py uses SymPy1.14.0. The continuum inequality is certified by the full symbolic identities; the convex-hull/extremal/duality arguments are analytic proofs, not established by sampled matrices. No proof-assistant formalization or independent second authored replay is claimed.

Next scientific use: add this exact PAIR convex domain, not just the SUM cap, to actual-COM/covariance primal–polar arrow coverage on genuinely open E17 shape sectors. Seek literal root/complement packets or a whole genuine shape cell excluded by rational joint certificates. Passing the SDP is not a U1/S1 witness; the second formal control makes that distinction explicit. Existing all-SPD U2-closed shape families must not be counted again. Lower prohibition and attaining construction remain separate unresolved obligations.
