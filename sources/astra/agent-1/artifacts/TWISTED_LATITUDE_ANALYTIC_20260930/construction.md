# Twisted-latitude radial construction (smooth research input, not the requested polyhedron)

For n=(x,y,z) on the unit sphere put f_k(n)=z cos(kx)+y sin(kx), r(n)=1+epsilon f_k(n). The map T_k(x,y,z)=(x,y cos(kx)-z sin(kx),y sin(kx)+z cos(kx)) is a smooth, area-preserving sphere diffeomorphism, with inverse obtained by reversing the angle since x is unchanged. Thus f_k is the ordinary height function after T_k. It has exactly two critical points, n=(0,0,+/-1), for every k. For positive epsilon, the radial surface has exactly two radial critical points. This is a smooth-body statement, not a polyhedral census.

The volume is 4*pi*(1+epsilon^2)/3 because T_k preserves spherical area. Integrating n*r(n)^4/4 gives the first moment. Its x and y coordinates vanish by circular integration and the oddness of sin(kx). Its z coordinate is pi*epsilon*(I1(k)+(3/4)*epsilon^2*I2(k)), where
I1(k)=integral[-1,1](1-x^2)cos(kx)dx=4*(sin(k)-k*cos(k))/k^3,
I2(k)=integral[-1,1](1-x^2)^2 cos(kx)dx=16*((3-k^2)*sin(k)-3*k*cos(k))/k^5.
Choosing the nonzero scalar root near tan(k)=k makes the actual uniform volume centroid zero. The numerical roots below are not exact rational polyhedral constructions.

Strict convexity must be established separately. For a radial graph, positivity of M=r^2 I+2 grad_S(r) tensor grad_S(r)-r Hess_S(r) is the local second-fundamental-form condition. A global numerical directional screen is evidence only, not a proof. Any new polyhedron must have its own complete rational hull, mass and equilibrium audit; none is inherited from this smooth calculation.

## Explicit convexity bound
For 4<k<5, |f|<=1, the ambient Hessian operator norm is at most k^2+1<26, and |n dot grad(f)|<=k/2+1<3.5. Hence the spherical Hessian norm is <29.5. At epsilon=1/100, r>=.99 and r I-epsilon Hess(f) is positive definite, with eigenvalues>.695. Therefore r^2 I+2 grad(r) tensor grad(r)-r Hess(r)>0 everywhere. The radial graph is a closed strictly convex smooth surface. The scalar centroid equation has a root in(4,5): its I1 term changes sign, and the small epsilon^2 I2 term preserves the endpoint signs. The exact construction can define k as that root. The separate numerical screen up to epsilon=.043 is not a global proof for those larger values.

An old cyclic support helper was found to substitute a non-axial point when the designated axial carrier was absent. This is now an explicit ValueError; no result from a missing carrier is promoted. Any new discrete seed below must actually retain its axial vertex.
