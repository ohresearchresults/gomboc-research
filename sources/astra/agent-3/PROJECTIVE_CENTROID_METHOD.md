# Canonical projective closure of the physical volume centroid

For a full-dimensional convex body K containing the origin, use the physical
map T_p(x)=x/(1+p·x) on the domain where every denominator is positive. Its
Jacobian determinant is (1+p·x)^(-4). The density of the *new* body is uniform;
we integrate its actual volume, first moments, and second moments.

Let g be the new volume centroid and M2=E[yy^T] its uncentered second moment.
An incremental parameter delta acts as y -> y/(1+delta·y). Differentiating the
actual transformed volume and first moments gives

    D_p g = -5 M2 + 4 g g^T = -5 Cov(y) - g g^T.

This matrix is negative definite because the covariance of a full-dimensional
solid is positive definite. Thus centroid closure is a nonsingular three-variable
Newton problem. This statement concerns the centroid only; it says nothing by
itself about the equilibrium census after the map.

The volume function V(p)=integral_K (1+p·x)^(-4) dx has gradient -4V(p)g(p) and
positive definite Hessian. Its blow-up at the boundary of its parameter domain
provides the unique minimizer, which is the centered projective representative.
Numerical implementations still fail explicitly if their finite iteration or
positive-denominator checks do not succeed.

For the oriented tetrahedron (0,a,b,c), the second-moment contribution equals
its signed volume times [aa^T+bb^T+cc^T+(a+b+c)(a+b+c)^T]/20. Summing these over
the actual facet triangulation is mass integration only; those triangles are
not asserted to be maximal facets.

If Q_i·x <= 1 are the physical support inequalities, the same map gives
(Q_i+p)·y <= 1. This is one consistent physical embedding, rather than a
separate primal and dual metric. Implicit differentiation of g(p,q)=0 supplies
D_q p. Both the coordinate and half-space implementations recheck their final
physical own-centroid census.

Implementations: canonical_projective_mass.py,
projectively_centered_shadow_goal.py, projectively_centered_normal_goal.py.
Independent derivative checks are in artifacts/canonical_projective_mass_derivative_check.json
and artifacts/projectively_centered_normal_derivative_check.json.

Numerical centering is not an acceptance certificate. A candidate is the saved
literal rational body. Its exact uniform centroid, true hull incidence, strict
equilibria and all weak contacts must be recomputed by the native exact audit.
No qualifying Figure had been found when this method note was written.
