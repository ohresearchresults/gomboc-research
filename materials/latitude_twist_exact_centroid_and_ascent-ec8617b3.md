# material-ec8617b341ce

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Exact-centroid latitude twist: smooth auxiliary construction and polyhedral obstruction
Evidence: coordinator mathematical derivation, independent of C622 sources and all worker results. NOT a finite polyhedron, NOT a C<500 record, no novelty claim. Accepted C622 remains unchanged.

## Exact homogeneous centroid
Let k be the unique root of sin(k)-k cos(k)=0 in (pi,3pi/2), k=4.493409457909...<4.5. The derivative is k sin(k)<0 on that interval. For u=(x,y,z) on S^2 put f=x cos(kz)+y sin(kz). Phi(u)=(f,-x sin(kz)+y cos(kz),z) is an analytic sphere diffeomorphism, inverted by opposite rotation at unchanged z. Thus f is a height function composed with a diffeomorphism and has exactly two Morse critical points, u=(+/-1,0,0), values +/-1.
Azimuthal integration gives integral f z=0; integral f y=pi integral_-1^1 (1-z^2)sin(kz)dz=0; integral f x=pi integral_-1^1 (1-z^2)cos(kz)dz=4pi(sin(k)-k cos(k))/k^3=0. The radial solid r(u)=(1+A f(u))^(1/4),0<A<1, has first moment M=(1/4)integral r^4 u dOmega=0 exactly, so its own homogeneous centroid is the origin.
For a smooth strictly convex radial graph, boundary normal is proportional to r u-grad_S r. Equilibrium at that own centroid is exactly grad_S r=0. Support-height critical points do not provide an independent extra set of equilibria under these strict-convexity and own-centroid assumptions.

## Rigorous convexity for A<1/8
Put t=-x sin(kz)+y cos(kz). Ambient gradient is (cos(kz),sin(kz),kt); only nonzero Hessian entries are H_xz=H_zx=-k sin(kz),H_yz=H_zy=k cos(kz),H_zz=-k^2 f. Spherical Hessian is tangent restriction minus (f+kzt)I. Since |f|<=1,|zt|<=1/2, ||Hess_S f||<=k^2+k+1+k/2<28.
The radial convexity matrix divided by r^2 is Q=I-A Hess_S f/[4(1+A f)]+5 A^2 grad_S f tensor grad_S f/[16(1+A f)^2]. Hence Q>=[1-7A/(1-A)]I>0 for 0<A<1/8; at A=.1 the bound is 2/9. These are explicit analytic strictly convex homogeneous smooth bodies with S1,U1,H0 and no other weak equilibria.
At the minimum (-1,0,0), Hess_S f in tangent coordinates(y,z)=[[1,k],[k,1+k^2]]. Its eigenvalues are (k^2+2 +/- k sqrt(k^2+4))/2. A<4/(lambda_plus+4)~.15299 is necessary there, not a global sufficiency claim. The smaller eigenvalue~.045 is a flat critical direction relevant to discretization.

## Nonlinear twist and numerical correction
Any smooth odd psi(z),psi(0)=0 preserves the two-critical-point diffeomorphism argument. For f=x cos(psi)+y sin(psi), own-centroid closure of r^4=1+A f reduces to integral_-1^1(1-z^2)cos(psi(z))dz=0. With p=psi',q=psi'',t=-x sin(psi)+y cos(psi), ambient gradient=(cos(psi),sin(psi),pt); Hessian cross terms are -p sin(psi),p cos(psi),H_zz=q t-p^2 f. Spherical Hessian subtracts(f+zpt)I.
For psi=k[(1-b-c)z+bz^3+cz^5], first positive root of that dipole equation, a sampled optimization on 41x72 directions,160-point Gauss-Legendre integration,differential_evolution(seed72831,popsize6,maxiter15,bounds[(-.5,1.2),(-.7,.7)]) produced b=.43858426127879624,c=-.7,k=3.3732129438650644,A_grid_limit=.16530147098687759. This is NOT a convexity certificate and the optimizer did not converge. Exact code still requires separate preservation.
CORRECTION: an earlier context summary's b=.25,c=0,k=5.3720219657,A_limit~.1779 is inconsistent with the specified dipole integral. Direct quadrature at that k gives~.09355793657417, not 0. The actual first root is k=11.411088441810803 and sampled convexity limit~.048924. Do not propagate that earlier claimed cubic improvement. The quintic candidate above is distinct.

## Discrete ascent necessary condition
Let a convex polyhedron have center 0,one unstable vertex,no weak vertex equilibria. Every other vertex v has a neighbor w with v dot(v-w)<0; thus v dot w>||v||^2. If theta is their directional angle then cos(theta)>0 and r_w/r_v>sec(theta), so radius strictly increases. A path choosing such edges terminates at the unique unstable vertex. For m edges and endpoint spherical separation d, d<=sum theta_i and log(r_end/r_v)>sum[-log cos(theta_i)]>=sum(theta_i^2)/2>=d^2/(2m). Consequently m>d^2/[2log(r_end/r_v)],m<=V-1. This is shape-dependent, not a universal complexity bound.
For vertices inscribed in r^4=1+A f, log(r_max/r_min)=(1/4)log((1+A)/(1-A)). At A=.1 this~.0501677. An exact antipodal starting vertex to the unique unstable vertex requires m>98.36,V>=100, PROVIDED the discretized body's own centroid remains 0. Generic triangular hulls C<500 have V<=85, so this particular antipodal A=.1 inscribed case is excluded. It is not a no-go for nontriangular/higher-amplitude/nonantipodal meshes, other seeds, or a displaced own centroid (recompute all quantities there).

## Next question
Optimize nonlinear twist/radial profile for discrete margins, not merely smooth convexity. Build sparse gradient-aligned hulls, recompute actual volume centroid, merge only truly coplanar facets, count all strict and weak equilibria, retain failures as sampled rather than exact exclusions. Acceptance remains finite homogeneous strict110 without weak equilibria,C=2E<500.
