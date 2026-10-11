# material-9558c1fd25a2

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# ORTHOGONAL_REFERENCE_CONVEX_SUBLEVELS_V1

## Scope

A further analytic consequence of the self-polar orthogonal factor in [internal-source-reference] is that designing a reference ellipsoid with a fixed target factor is a convex matrix-feasibility problem. This is not a claim that the full mixed-product objective is convex, and no new numerical optimum or enlarged H5 region is claimed here. The result replaces an unjustified reliance on local Cholesky optimization with an exact global formulation and finite rational certificate options.

All vectors and polars below use the SAME fixed origin. Physical M is not an optimization variable in this reference problem. Choosing C and then transforming H_C=C^.5 M C^.5 preserves the original physical inverse as explained in the parent. P may be any full-dimensional compact convex body with0 in its interior; actual-centroid uniformity is needed only when a subsequent physical theorem explicitly invokes it.

## 1. Rank-one equivalence and convex reference cones

For C>0, fixed vectors w,n and a constant U>=0,

    (w^T C^-1 w)(n^T C n)<=U

is equivalent to the linear matrix inequality

    U C-(n^T C n) w w^T >=0.                            (1)

Indeed, congruence by C^-1/2 gives U I-(n^T C n)zz^T, with z=C^-1/2w. Its only potentially smaller eigenvalue is U-(n^T C n)|z|^2. The assertion includes zero vectors. All entries in(1) are linear in the entries of C for FIXED U,w,n.

Let O(P)={(w,n):w in P,n in P^circ,w.n=0}. The orthogonal factor therefore obeys

    Upsilon_C(P)<=U
    iff C>0 and U C-(n^T C n)ww^T>=0 for all(w,n) in O(P). (2)

Consequently its fixed-U sublevel set is a convex homogeneous cone in the positive-definite C matrices. The factor is scale invariant, so one may add tr(C)=1, or any fixed positive reference trace normalization. Minimizing Upsilon_C is a quasiconvex optimization problem: its feasibility is monotone in the scalar U. This statement is global in the full five-dimensional space of reference ellipsoids, not only the canonical one-parameter family.

The same rank-one equivalence applies to Gamma_C using all true vertex/pole pairs. In that separate-radius case there are only finitely many pairs and no orthogonality curve. An old Gamma-template obstruction remains valid; replacing a local search by a convex feasibility solver cannot evade a proved universal lower floor for that template.

## 2. The optimal orthogonal reference is attained

Fix Euclidean balls rB subset P and rho B subset P^circ with r,rho>0. Let e_min,e_max be orthonormal eigenvectors of C corresponding to its smallest and largest eigenvalues; in the scalar-matrix case choose any orthonormal pair. Then w=r e_min and n=rho e_max form a legitimate orthogonal pair, giving

    Upsilon_C(P)>=r^2 rho^2 condition(C).                (3)

Normalize tr(C)=1. Any nonempty bounded-objective sublevel therefore has uniformly bounded condition number, and its eigenvalues stay a positive distance from0. The sublevel is closed in that compact positive-definite set because Upsilon is the maximum over a fixed compact pair set of a jointly continuous function. Thus the infimum over all references is attained by some positive-definite C. No claim of uniqueness is made. The argument works in every dimension at least2.

This existence result also shows why a reference optimizer approaching a singular matrix is not an unrecognized better finite optimum when the body remains fixed and full dimensional.

## 3. Adding angle caps and exact alignment

For a fixed marked primal vector a and covector q with a.q nonzero, the condition

    chi_C(a,q)=(a^T C^-1 a)(q^T C q)/(a.q)^2-1<=eta

is the linear matrix inequality

    (1+eta)(a.q)^2 C-(q^T C q)aa^T>=0.                 (4)

Therefore fixed orthogonal-factor cap U and any list of fixed angle caps eta_j form one convex reference-feasibility problem, with all physical vectors and covectors unchanged. Separate top-specific references may be designed by separate such problems; none is an independently chosen physical or polar metric.

The special case eta=0 is equality in Cauchy-Schwarz and is equivalent to Cq being proportional to a. With the normalization q^T C q=1 it is the affine constraint

    Cq=a/(a.q).                                         (5)

The sign of a.q may be negative, as for an upper vertex and the basal pole; the formula still has q^T Cq=1 and does not contradict positive definiteness. The exact H5 reference aligned to top9 in the parent is an explicit example of this affine slice.

For a given geometric target T>1 and condition majorant K=F U^2>=1, the sufficient hybrid inequality L_K(chi)<=T can be converted to a fixed angle cap whenever

    s=log[(sqrt(T)+sqrt(T-1))/(sqrt(F)U)]>=0.

It is equivalent to chi<=sinh(s)^2. This follows from

    L_K(chi)=cosh((1/2)log K+asinh(sqrt(chi)))^2.

At each fixed U the resulting reference problem is convex through(2) and(4). HOWEVER, increasing U loosens the factor condition while tightening this angle cap, so feasibility of the combined hybrid slices need not be monotone in U. Do not call the full mixed objective globally quasiconvex or use ordinary bisection without an additional argument. The one-parameter canonical strict-convexity theorem in [internal-source-reference] remains a special stronger structure, not a general proof of convexity of the mixed objective.

## 4. Finite true-edge-pair matrix certificates

In three dimensions the parent proves that the maximum factor is attained on true primal/polar edges. Their feasible orthogonality parameter intervals depend ONLY on the fixed body, not on C. On a nondegenerate edge-pair interval write

    w(s)=a+s u,
    n(s)=(N0+s N1)/(c+d s).

After multiplying(1) by(c+d s)^2 the matrix polynomial is

    U(c+d s)^2 C
       -[(N0+s N1)^T C(N0+s N1)](a+s u)(a+s u)^T.       (6)

Its degree is at most4 and its coefficients are linear in C for fixed U. A sufficient exact certificate is to subdivide the feasible rational interval and require EVERY Bernstein coefficient MATRIX of(6) to be positive semidefinite. Each such requirement is a linear matrix inequality in C; for a rational candidate, positive semidefiniteness may be checked by all principal minors or an exact rational factorization. Positive diagonal entries alone do not suffice.

The degenerate vertical fibres and constant constraints are reduced to their endpoints as in the parent. Before applying a strict-certificate convergence statement, cancel a common zero of the linear numerator and denominator: at such an endpoint the rational n(s) has a removable singularity and extends as a constant. If the denominator has a zero with nonzero constraint numerator, no closed feasible interval can approach that zero because t would leave[0,1]. Thus all nondegenerate closed feasible pieces can be represented with a nonvanishing denominator after cancellation.

For a fixed rational C and a STRICT bound U>Upsilon_C(P), all matrices(1) are uniformly positive definite on the compact pair set. After the above cancellations, each matrix polynomial(6) is uniformly positive definite on its closed interval. Under repeated interval subdivision its Bernstein coefficient matrices converge uniformly to values of the matrix polynomial; this follows by expanding the finitely many power coefficients after an affine rescaling, with all higher-order interval terms tending uniformly to zero. Hence some finite subdivision has positive-definite Bernstein coefficient matrices. Rational strict certificates therefore exist in this hierarchy whenever the claimed strict bound is true. Equality at the optimum may require another representation and is not promised to certify at a fixed finite depth.

This is a route to a global reference-search implementation, not a claim that such a matrix-coefficient solver has been executed here. The parent's scalar quartic verifier has already been executed for a specified rational C; it remains the exact regional evidence.

## 5. Exact finite dual obstructions

A useful obstruction can come from a finite subset of actual orthogonal pairs without solving the entire continuum. For pairs(w_i,n_i), choose positive-semidefinite matrices Z_i and put

    S=sum_i Z_i,
    T=sum_i (w_i^T Z_i w_i)n_i n_i^T.

Taking the trace pairing of Z_i with(1) and summing shows that any feasible reference must satisfy

    U tr(CS)>=tr(CT).                                   (7)

If S is nonzero and T>=U0 S, then C>0 gives tr(CS)>0 and therefore U>=U0. Rational pairs and rational positive-semidefinite Z_i with this dominance provide an exact all-reference lower certificate. No origin change or reference whitening is hidden in it. If T-U S is positive semidefinite and nonzero, feasibility at that particular U is impossible because tr[C(T-U S)]>0.

At a putative optimum, null directions of the active rank-one matrix inequalities may suggest Z_i, but numerical stationarity is only a locator. A claimed global lower certificate must supply the literal rational pairs, the full matrices, and the exact dominance proof. No such optimized H5 dual witness is claimed in this material.

## Scientific consequence and next step

The new reference design is not restricted to a trial-and-error local search. Fixed U/angle cap slices are convex, the pure-factor optimum exists, and both positive and negative exact certificate formats are available. The next useful computation is a globally controlled reference or dual obstruction across a substantial H5 region, or a genuine universal bound on the optimized orthogonal factor. The actual covariance countercontrols above6 in minimum-0257 do not automatically refute a smaller bound after optimizing C: their metric gauge is part of their statement. Conversely, changing C changes H_C and must be transported in every subsequent physical argument.

This material is an elementary analytic derivation from the parent. No new numerical computation, software dependency, minimum value, or attaining construction is asserted. The global bracket34..622 and the unresolved whole-H5/E17 gap remain unchanged.
