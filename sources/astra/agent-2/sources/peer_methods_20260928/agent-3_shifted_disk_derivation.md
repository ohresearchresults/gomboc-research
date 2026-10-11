# Exact shifted-disk smooth construction (not the requested polyhedron)

Derived in this agent's work. This is a smooth starting family, not a claim of bibliographic novelty and not a Figure solution. It was motivated by Sloan's analytic radial family and shifted-disk footnote (arXiv:2306.14914). The formulas below differ by making the horizontal disk displacement exact.

Let P(z)=(3*pi/2)*(z-z^3/3), r(z)=sqrt(1-z^2), mu(z)=beta*(cos(P(z)),sin(P(z))). Define K_beta by -1<=z<=1 and |(x,y)-mu(z)|<=r(z).

1. Uniform volume is exactly 4*pi/3. Every horizontal disk has area pi*(1-z^2), unchanged by its translation.
2. M_z=0 by oddness. The complex first moment M_x+i*M_y is pi*beta*integral_-1^1 (1-z^2)*exp(iP(z)) dz. Since P'=(3*pi/2)*(1-z^2) and P runs from -pi to pi, this equals (2*beta/3)*integral_-pi^pi exp(iP) dP=0. Its actual uniform centroid is therefore exactly the origin.
3. For horizontal unit n, the slice support is h_n(z)=n.mu(z)+r(z). If beta<4/(9*pi^2), all h_n are strictly concave. Indeed r''=-(1-z^2)^(-3/2), and |mu''|=beta*sqrt(9*pi^2*z^2+(81*pi^4/16)*(1-z^2)^4). The maximum of (1-z^2)^(3/2)*|mu''|/beta is 9*pi^2/4 at z=0. To check the maximum, put t=z^2: its square is 9*pi^2*t*(1-t)^3+(81*pi^4/16)*(1-t)^7; its derivative is negative on [0,1/4] because (63*pi^2/16)*(1-t)^4>1, and on [1/4,1) because both derivative terms are nonpositive. Concavity of every horizontal slice support makes K_beta convex; strict inequalities and circular sections give strict curvature.
4. On the smooth lateral surface, in coordinates (z,psi=phi-P(z)), squared distance to the actual centroid is 1+beta^2+2*beta*sqrt(1-z^2)*cos(psi). Its only critical points are z=0,psi=0 and z=0,psi=pi. The Hessians are negative/positive definite respectively. At either endpoint z=+-1, the normal is vertical but the radius has horizontal component -beta, so neither tip is an equilibrium. Thus the smooth body has exactly one strict U and one strict S, at (1+beta,0,0) and (-1+beta,0,0), with no saddle.

The ambient map (x,y,z)->(x+mu_x(z),y+mu_y(z),z) has Jacobian1 and maps the unit ball to K_beta, explaining the volume identity. Its restriction to the sphere is smooth at both tips.

The polyhedral experiments use piecewise linear homothetic polygon sections, which retain exact planar side faces. Their actual hull, volume centroid and equilibria must be recomputed. Eighteen finite layered optimization trials at4/6/8 sides did not yield110. The smooth proof is not transferred to any such polyhedron.
