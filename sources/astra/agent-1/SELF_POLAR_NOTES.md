# Negative self-polar physical construction branch

## Scope
No own110 example has been found. This is an alternative construction family and a concrete local mass-balancing derivation, not an exclusion theorem or a completed goal.

## External mathematical input
Alathea Jensen, *Self-polar polytopes*, arXiv:1902.00784v1, Theorem7.4 and Corollary7.5: https://arxiv.org/pdf/1902.00784 . For P=-P° and a point x beyond exactly one facet, adding x and cutting by x·y>=-1 commute when the removed dual vertex and added pyramid lie on opposite sides of that facet. The resulting body remains negative self-polar. The theorem's conditions are checked numerically in the exploratory script; no blanket success claim is made for arbitrary x.

## Agent1 derivation: physical centroid balance by orthogonal cone sections
If P=-P° in R3, its cone C={(t,tx): t>=0,x in P} is self-dual in Euclidean R4, since (1,x)·(1,y)=1+x·y>=0. Apply an orthogonal matrix to this entire cone and intersect with t=1. This changes the actual three-dimensional physical body and preserves negative self-polarity; it does not nominate a new mass centre for an unchanged body.

For b=theta*u, use the orthogonal rotation whose projective section map is

    T_b(x) = [x + ((cos(theta)-1)(u·x)+sin(theta))u]
             / [cos(theta)-sin(theta)(u·x)].

Every denominator must remain positive. At b=0, delta x = b+x(b·x), and the projective volume Jacobian is 1+4(b·x)+O(|b|^2). Consequently, for actual uniform-volume mean c and second moment A=E[xx^T],

    delta c = [I+5A-4cc^T] b.

This matrix equals I+5Cov(x)+cc^T and is positive definite. The script uses this exact first-order identity for Newton steps, then recomputes the actual finite body volume/centroid and backtracks if needed. The identity is algebraically derived above. A global uniqueness/existence theorem for all cone sections has NOT been established or invoked here.

For an oriented tetrahedron (0,a,b,c), volume is det(a,b,c)/6, mean is (a+b+c)/4, and second moment is [ss^T+aa^T+bb^T+cc^T]/20, s=a+b+c. Summing these gives the body moments used by the Newton solve.

## Executed branches
`selfpolar_search.py` starts with a negative-self-polar 9-gon pyramid (V=F=10,C36) and samples finite add/cut candidates, balancing every candidate's actual centroid by the above map. V<=83 ensures even a later generic rational support perturbation has E<=243. `artifacts/selfpolar-b` records rounds0..17, ending V=F83,E164,C328, approximately own9/9, centroid norm1.05e-16. It is NOT110 and has multiple positive bars.

A second seed uses two predetermined add/cut construction steps on a rational regular tetrahedral seed BEFORE any objective or equilibrium search; its first searched body is V=F11,C40. No search is performed below the requested C34 lower boundary. `artifacts/selfpolar-tetra` records this exploration.

`selfpolar_opt.py` optimizes vertex coordinates with all symmetric contact equations xi·xj=-1, homogeneous centroid c=0, noncontact inequalities xi·xj>=-1, and positive integration triangles. Its scalar objective uses radial persistence. Approximate equality residual is never treated as an exact physical certificate. `artifacts/selfpolar-opt39` ended with residual6.15e-14, own22/22 numerically, two substantial positive bars~.4227,.4475 and many small defects. `artifacts/selfpolar-opt83` is the larger realization-space trial.

All claimed final bodies would be independently reconstructed and rationally audited at their actual volume centroid. Neither a negative-polar identity alone nor a small residual meets the goal.
