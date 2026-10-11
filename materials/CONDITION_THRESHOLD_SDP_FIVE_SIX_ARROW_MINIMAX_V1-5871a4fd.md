# material-5871a4fd00aa

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# CONDITION_THRESHOLD_SDP_FIVE_SIX_ARROW_MINIMAX_V1

## Contribution and limits
For a fixed actual shape, the smallest covariance-weighted condition number compatible with a packet of weak escape arrows is the optimum of ONE linear semidefinite program, with an explicit complete dual. Its value is the maximum of the values of its subpackets of at most five arrows for two-layer geometry, or at most six arrows for arbitrary three-dimensional geometry. Combining this bottleneck identity with the finite set of rooted true-edge trees gives an exact minimax reformulation of the best possible U1 condition number. This extends the method beyond the literal parallel H5 chart; it does not assert feasibility or exclusion of any uncomputed realization.

A second result identifies precisely when strict rational certificate atlases are guaranteed locally and on compact shape domains. It distinguishes a strict condition threshold above a prescribed cap from equality at that cap. Failure of a strict-certificate search is not a feasibility result.

This is analytic research, not a new numerical atlas or attaining polyhedron. No global minimum bound changes: 34<=C_min<=622; whole H5 and the full V10/E17/F9 layer remain open.

## Exact source dependencies and attribution
The directly preceding coordinator theorem is H5_CONDITIONED_FIVE_ARROW_AND_INDEFINITE_STRESS_V1, material [internal-source-reference], SHA256 38da6f51cf9c20311135a3485de074668c1e230d613e4cea7f8d3ec5960baa97. Its projection argument and real dual are used below. Its independent exact four-arrow control is recovered from [internal-source-reference]. The parent unrestricted five-arrow theorem is the fully read result minimum-0251, SHA256 c6740ff1f093f61efe88b3be1e4fbc19f4163ffa98e8ce686fb621ac0237d252.

The GENERAL V10/F9 finite-height premise was read completely in [internal-source-reference], 10171 bytes, SHA256 e7daf31f7dddffac638b3bb0d7005af5613e4b2473b0979daff4357ebf5894db. It gives the actual covariance-weighted joint S1/U1 cap p*q=9599306095407/200000000000<48, not only an H5 cap. Its primal/polar escape-tree hypotheses also cover unique strict S/U with incidental weak rests, as explained in fully read minimum-0252, SHA256 c166ef43daf3b0236b4e6c5360246aaf15fec13adfb79c3a1f22541c4d49bce9. Its covariance input uses the actual filled-body centroid and covariance, never the vertex average or an independently recentered polar.

Homogeneous normalization of positive-definite condition-number minimization is standard semidefinite optimization, not claimed here as a new general optimization principle. The official MOSEK Modeling Cookbook, section 6.2.2, describes that normalization at `https://docs.mosek.com/modeling-cookbook/sdo.html` (HTML read in this coordinator turn). The contributions developed here are its exact arrow-cone dual, the five/six-arrow threshold identity, and the ensuing strict-certificate/shape-boundary distinctions in this research problem.

## 1. Definition and a single linear SDP
Let z_i in R3 be fixed vertices, g a fixed interior reference, and Sigma a fixed SPD matrix. In the homogeneous application g and Sigma are the actual volume centroid and covariance. For each selected directed genuine edge e=(i,j), define

    A_e=sym((z_i-g)(z_j-z_i)^T),
    D_e(M)=tr(A_e M).

For a finite arrow packet J define the extended real number

    kappa_J = inf condition(Sigma^(1/2) M Sigma^(1/2)),

where the infimum is over M>0 satisfying D_e(M)>=0 for every e in J. Set kappa_J=+infinity if no such SPD metric exists. The empty packet has kappa_empty=1. Put S=Sigma^-1.

The exact primal program is

    minimize k
    subject to M-S >=0,
               k S-M >=0,
               tr(A_e M)>=0 for e in J.                         (P)

The two matrix inequalities are Loewner PSD inequalities. This is linear in the six symmetric entries of M and in k. There is no product of two decision variables and no condition-number bisection is needed.

To prove equivalence, given a feasible SPD metric rescale it so the smallest eigenvalue of H=Sigma^(1/2) M Sigma^(1/2) is one. Homogeneity preserves every arrow sign and gives I<=H<=condition(H) I. Conversely every feasible point of (P) is SPD and has condition(H)<=k. Taking infima proves equality. If kappa_J is finite, it is attained: a minimizing sequence with bounded k lies in a compact matrix interval S<=M<=K S. Its limit satisfies all closed constraints. Rescaling an optimum, if needed, sets lambda_min(H)=1 without increasing k. Thus no singular limiting metric substitutes for an SPD optimizer in this normalization.

## 2. Complete dual, including limiting cases
The exact dual is

    maximize tr(S P)
    subject to P>=0, N>=0, w_e>=0,
               P-N=-sum_{e in J} w_e A_e,
               tr(S N)=1.                                      (D)

For any primal and dual feasible points, write Q=P-N. From the arrow constraints tr(MQ)<=0. From M>=S and M<=kS,

    tr(MQ) = tr(MP)-tr(MN)
            >= tr(SP)-k tr(SN)=tr(SP)-k.

Hence tr(SP)<=k. This proves weak duality without numerical assumptions.

Equality of the optimum values, and the relevant attainments, follow directly from the cone separation already proved in the preceding source.

If 1<kappa_J<infinity, the open cone of metrics with covariance-weighted condition number less than kappa_J is disjoint from the packet cone. A nonzero separator has Q=P-N=-sum w_e A_e with P,N PSD and tr(S(P-kappa_J N))>=0. Because the packet is feasible under some unrestricted SPD metric, Q cannot be a nonzero PSD matrix. Thus N is nonzero and tr(SN)>0. Normalize to tr(SN)=1. The resulting dual objective is at least kappa_J, while weak duality gives the reverse inequality. The dual optimum is attained.

If kappa_J=1, take w=0 and P=N=Sigma/3. This is dual feasible with objective one, and the primal optimum is attained as above.

If kappa_J=+infinity, unrestricted SPD infeasibility supplies a nonzero PSD separator Q=-sum w_e A_e. Put N=Sigma/3, P=N+tQ and replace w by t w for t>=0. These are dual feasible, and tr(SP)=1+t tr(SQ) tends to infinity. Thus the dual is unbounded. No finite optimum is invented at a singular metric.

These assertions are over the reals. Exact rational optimum matrices or weights are not promised for arbitrary rational input. Section 5 gives rational strict certificates when the target cap is separated by a positive gap.

## 3. Five- and six-arrow bottleneck identities
For arbitrary fixed three-dimensional geometry and reference, the trace-one slice of the SPD metric cone has dimension five. Intersecting it with an open convex condition-number cone and with each selected weak arrow halfspace gives convex sets in R5. Finite Helly therefore gives the universal bound SIX: an infeasible packet in that open conditioned cone has an infeasible subpacket of at most six arrows.

For vertices on two parallel planes with the reference strictly between them, the preceding coordinator theorem improves six to FIVE. Writing M=[[G,b],[b^T,m]] and trG=1 leaves four projected coordinates (G,b). The fibre of any open convex metric cone at fixed (G,b) is an open interval in m. Every cross-layer arrow is an upper bound on m, and every same-layer arrow is independent of m. Thus intersection commutes with this projection for a finite arrow packet; finite Helly applies in R4. No contraction outside the conditioned cone is used.

Let s=6 in general, and s=5 for such two-layer geometry. Then

    kappa_J = max_{K subset J, |K|<=s} kappa_K.                  (1)

Monotonicity gives the >= direction. For the converse let alpha be the maximum on the right. If alpha is finite, choose any c>alpha. Every small subpacket has a feasible metric of condition number less than c. The appropriate Helly theorem implies that the complete packet has one common metric in that SAME open cone. Therefore kappa_J<c for every c>alpha, hence kappa_J<=alpha. If alpha is infinite, monotonicity gives kappa_J=infinity. This also proves that if kappa_J is infinite some small subpacket is already unrestricted-SPD infeasible; otherwise the finite maximum alpha would contradict the preceding argument.

This is a value identity, not merely the existence of one small obstruction at a preselected cap. It does not assert a universal four-arrow shortcut or five-arrow sufficiency for arbitrary nonparallel geometry.

## 4. Rooted-tree minimax and joint110 use
At a vertex which is not a strict U, at least one true adjacent edge has a nonnegative radial derivative. Along any such arrow,

    ||z_j-g||_M^2-||z_i-g||_M^2
      =2D_e(M)+||z_j-z_i||_M^2>0.

Selecting one nonnegative exit from every nonroot therefore cannot create a directed cycle. If the unique strict unstable vertex is the only root, the selected arrows form a rooted tree. Conversely a complete rooted tree of nonnegative arrows gives every nonroot an exit and makes its root the unique global norm maximum, hence a strict U. Weak exits remain allowed; the edge's positive length supplies strict norm growth.

For the finite set of all rooted true-edge trees of the fixed graph, define

    kappa_U(P,g,Sigma)
      = min_T kappa_T
      = min_T max_{K subset T, |K|<=s} kappa_K.                 (2)

This is the exact smallest covariance-weighted condition compatible with exactly one strict U at that reference. It is not a stable-facet condition. When finite, it has an actual SPD optimizer because there are finitely many trees and each finite kappa_T is attained.

For an actual homogeneous V10/F9 body, proper110 requires condition(H)<48 by the accepted finite-height theorem. Thus kappa_U>=48 excludes proper110 for that fixed body, including the boundary case kappa_U=48 because the required bound is strict. A stronger input p*q may be substituted for 48. A surviving conditioned U1 metric still requires an actual-inverse stable/saddle/physical-weak audit; it is not an attaining proper110 construction.

This formulation applies to arbitrary nonparallel realizations with the SIX-arrow bound. It does not assume that all E17 realizations belong to the literal H5 chart. No value of kappa_U for an uncomputed full shape is asserted here.

The formulation is affine invariant: under z'=Lz, g'=Lg, Sigma'=L Sigma L^T, A'_e=L A_e L^T and M'=L^-T M L^-1, arrow pairings and the eigenvalues of the covariance-weighted physical metric are unchanged. This transports one physical metric; it does not whiten the body and reset its metric.

## 5. Strict rational certificates and a quantitative rounding bound
Suppose Sigma and every A_e are rational and kappa_J>K>1 for a prescribed rational cap K. The complete dual supplies a certificate Q=P-N with nonnegative weights and

    delta=tr(Sigma^-1(P-KN))>0.

For finite kappa_J take an optimum dual; delta=kappa_J-K after normalization. For infinite kappa_J use the PSD separator, which has positive pairing with Sigma^-1. By the bottleneck identity a certificate may be supported on at most s arrows for this fixed shape.

Choose rational nonnegative weights on that same support, giving Q_r, and a rational symmetric approximation N_r to N. For any sufficiently small positive rational eta the approximations can satisfy

    ||Sigma^-1/2(Q_r-Q)Sigma^-1/2||_op <= eta,
    ||Sigma^-1/2(N_r-N)Sigma^-1/2||_op <= eta.

Define

    N_new=N_r+3 eta Sigma,
    P_new=Q_r+N_new.

Then N_new is positive definite and P_new is positive definite. In relative coordinates N_new differs from N by an error bounded by eta plus 3 eta I, while P_new differs from P by two errors bounded by eta each plus 3 eta I. Their strict lower margins are therefore at least 2 eta and eta, respectively.

The trace gap satisfies the explicit estimate

    tr(Sigma^-1(P_new-K N_new))
      >= delta-(12K-9)eta.                                    (3)

Indeed the Q error contributes at worst -3eta, the N rounding term at worst -3(K-1)eta, and the common regularizer contributes -9(K-1)eta. Choosing eta<delta/(12K-9) preserves a positive gap. The exact identity P_new-N_new=Q_r=-sum w_r A_e is automatic; no independent rounding of P breaks it.

Thus strict rational positive-definite certificates are dense whenever the condition threshold is STRICTLY above the cap. This does not promise a rational zero-gap certificate at kappa_J=K. That equality case may require algebraic separation or a different exact argument. A numerical failure to find a positive gap cannot decide between equality, feasibility below the cap, or an inadequate search.

For arbitrary real continuous input data, strict certificates can likewise be approximated with rational weights and rational N using ordinary matrix-norm estimates, after a small positive regularization. The displayed relative-coordinate constants are the explicit rational-input version used for exact fixed-shape recovery.

## 6. Compact parameter domains: when a finite strict atlas exists
Let theta range over a compact domain, with fixed labelled graph and continuous matrices A_e(theta), Sigma(theta)>0. Assume Sigma stays SPD throughout the INCLUDING-boundary domain. Each kappa_J(theta) is lower semicontinuous: for a convergent theta sequence with bounded liminf kappa_J, use the normalized primal optimizers S(theta)<=M<=k S(theta). Uniform SPD covariance on the compact domain gives a bounded matrix sequence. A convergent subsequence satisfies the limiting closed arrow and matrix constraints. Therefore the limiting threshold is no larger than the liminf. Infinite liminf is harmless.

The finite minimum over rooted trees kappa_U(theta) is also lower semicontinuous, and attains its extended minimum on the compact domain. Consequently, if

    kappa_U(theta)>K for EVERY theta in the compact domain,

then its minimum is strictly above K. Every labelled tree at every shape has a strict certificate. Regularizing its P,N makes both positive definite without consuming the entire positive trace gap. Fixed weights and fixed N then give P(theta)=-sum w A_e(theta)+N; all three strict guards persist on a neighborhood. Compactness and the finite graph supply a finite collection of such certificate neighborhoods covering all shapes and all trees.

When the exact moment data are rational functions of theta with known positive denominators, these guards can be written without square roots: positive leading principal minors of P(theta) and N, and

    tr(adj(Sigma(theta)) [P(theta)-K N])>0.

Clearing positive denominators gives polynomial inequalities suitable for exact interval/Bernstein or algebraic certification. This establishes conditional existence of a finite strict atlas, not a presently constructed atlas or a bound on its number of cells.

The hypotheses matter. Exclusion only of genuine open-parameter bodies does not automatically exclude singular labelled limits on the compact boundary. A collapsed endpoint may admit an indexed escape cone although it is not a ten-vertex body. Likewise kappa_U=K at even one boundary point invalidates the strict-gap assumption while still possibly excluding proper110 there. Neither case licenses a blind positive-margin atlas argument. The actual finite-height and weak-limit mechanisms must be retained separately.

## 7. Optimal spectral geometry
At finite optimum kappa_J>1, normalize H so its smallest eigenvalue is one and its largest is kappa_J. For an optimal dual let P'=Sigma^-1/2 P Sigma^-1/2 and N' similarly. Equality in weak duality gives

    (H-I)P'=0,
    (kappa_J I-H)N'=0,
    w_e D_e(M)=0 for every e.

For the PSD trace terms, zero trace implies zero product; all weighted arrow terms are nonnegative, so each vanishes. Hence P' lives in the smallest-eigenvalue eigenspace and N' in the largest-eigenvalue eigenspace. These spaces are orthogonal when kappa_J>1, so P'N'=0 and rank(P')+rank(N')<=3. Simple extremal eigenvalues give two rank-one parts.

This describes exact optimum geometry, not a mandate that a robust parameter-cell certificate remain rank one. The small positive regularization in Section 5 deliberately gives full-rank guards for continuity and rational rounding.

## Next use and evidence level
The threshold SDP and its sparse bottleneck can guide full-tree certificate discovery and identify when a proposed universal exclusion is losing only at the exact conditioned boundary. The six-arrow version provides the same framework for nonparallel E17 realizations. Existing conditioned work should target actual complete tree coverage, not merely small-packet counts. All assertions in this material are proved analytically from the stated sources; no new numerical threshold, full-shape verdict, finite atlas, exact minimum, or proof-assistant formalization is claimed.
