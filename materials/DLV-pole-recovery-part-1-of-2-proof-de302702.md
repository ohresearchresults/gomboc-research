# material-de30270213ea

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# DLV pole recovery capsule part 1/2: complete analytic proof and exact computational scope
Object identity DLV_POLE_AND_MOBIUS_BOX_20260923. Part2 contains the complete executable pole_cert.py; both parts are necessary for the computed box theorem. This is not a new110 body. Literal source formula was read in full from [internal-source-reference], SHAeb98472f555c7b6a0d2eda279f83359c396b2a5c966738af7c72fa8535b725d1; original capsule parts1/2 [internal-source-reference],[internal-source-reference]. Those sources establish provenance, not missing computational dependencies.

## Literal radial surface
For fixed0<a<1 define
F_a(x)=[a*x^2+(1-a)*(1-x)^2*a*x/(a+x)]/[a*x+(1-a)*(1-x)^2],
f(theta)=pi*F_a(theta/pi+1/2)-pi/2,
g(theta)=-pi*F_a(-theta/pi+1/2)+pi/2,
u=cos(phi)^2*cos(f)^2,v=sin(phi)^2*cos(g)^2,
rho=(u*sin(f)+v*sin(g))/(u+v),r=1+d*rho,
p=(r*cos(theta)*cos(phi),r*cos(theta)*sin(phi),r*sin(theta)).
Poles use continuous limits. Symmetry is the two VERTICAL reflections x->-x,y->-y, not rotationalD2.

## Theorem A: unchanged fine inscribed top stars have at least two strict U at own mass
Elementary differentiation gives F(0)=0,F(1)=1,F'(0)=F'(1)=1. Let R=1+d,theta=pi/2-epsilon. Then f,g=pi/2-epsilon+O_a(epsilon^2). Since u+v=epsilon^2(1+O_a(epsilon)) uniformly in phi, rho=1-epsilon^2/2+O_a(epsilon^3), uniformly in phi. Thus
r=R-d*epsilon^2/2+O(epsilon^3),
z=R-(1+2d)*epsilon^2/2+O(epsilon^3),
x^2+y^2=R^2*epsilon^2+O(epsilon^4).
For A=(0,0,R),C=(0,0,t),
J=(p-C)dot(A-p)=[(R-t)*(1+2d)/2-R^2]*epsilon^2+O_a,d,t(epsilon^3).
At reference0 the coefficient is -R/2, independently of a.

Fix0<a<1,0<d<1/2. There exists epsilon_0(a,d)>0 such that EVERY full-dimensional convex polyhedron P which is a finite hull of literal surface points, contains A, is invariant under both vertical reflections, and has ALL true-edge neighbours of A at0<pi/2-theta<epsilon_0, has at least TWO strict unstable vertices at its OWN uniform filled-volume centroid. Weak-equilibrium absence is not assumed.

Proof. Weighted-sine rho satisfies|rho|<=1, so all points have r<=R and z>=-R. A is the unique highest point. Cone A to a triangulation of boundary facets not containing A. Each positive-volume tetrahedron has centroid height at least(R-3R)/4=-R/2. Their positive-volume average gives t>=-R/2; symmetry makes the centroid axial and full dimension gives t<R. More generally topheightR and minimumvertexheightl imply t>=(R+3l)/4 by the same argument. On the compact t-interval[-R/2,R], J's leading coefficient is at most R*(2d-1)/4<0. The remainder is uniform over t and phi; choose epsilon_0 so every incoming true edge to A is strictly negative. A itself is strictU because (A-C)dot(w-A)=(R-t)*(z_w-R)<0 for every other vertex. Let q be a maximal-centred-radius vertex among all vertices except A. For every distinct non-A w,
(q-C)dot(w-q)=(|w-C|^2-|q-C|^2-|w-q|^2)/2<0,
even at radius ties. If q is adjacent to A, its last outgoing score is negative by the top-star condition; otherwise there is no such edge. Thus q is another strictU. QED.

Scope: sufficiently fine UNCHANGED INSCRIBED top stars, literal radial formula, two vertical reflections,d<1/2. Not coarser top stars, changed terminal points, lifted apex, circumscribed H approximations, all reflection-symmetric polyhedra, or earlier exact H controls. No smooth convexity or quadrature is assumed.

Constructive scale, not a construction: for A_epsilon=(0,0,R+lambda*epsilon^2),unchanged p_epsilon,and axial C_epsilon->(0,0,t_0), J's coefficient is (R-t_0)*[lambda+(1+2d)/2]-R^2. At t_0=0 it is positive precisely when lambda>1/2. Actual mass and true-edge incidence still require reconstruction; a positive chord is not automatically an edge.

## Theorem B: linked endpoint slopes cannot repair the top at reference0 while preserving bottom convexity
For any top expansion r=R-k*epsilon^2/2+o(epsilon^2), incoming coefficient at reference0 is R*(k-R)/2, so escape needs k>R. At bottom r=B+k_b*epsilon^2/2+o(epsilon^2),B=1-d, gives z=-B+(B-k_b)*epsilon^2/2+o(epsilon^2); convexity at the lowest pole requires k_b<=B.
Replace F by any C2 increasing endpoint map H with H(0)=0,H(1)=1,positive slopes alpha=H'(0),beta=H'(1),keeping linked f/g and rho. The two top axial k values are d*alpha^2,d*beta^2; the bottom values are the same pair exchanged. Necessary bottom convexity in both axial sections forces both<=B. The effective top k is their positive weighted mean, hence k<=B<R. Every near-top incoming coefficient at reference0 is at most R*(B-R)/2=-R*d<0. This closes linked endpoint-slope repair at reference0, NOT all own-centroid geometries or independently changed top/bottom maps.

## Theorem C: exact asymmetric-warp nonconvexity box
Set x=theta/pi+1/2,w_b(x)=b*x/[1+(b-1)*x],f=pi*F_a(w_b)-pi/2,g=-pi*F_a(1-w_b)+pi/2; physicaltheta is unchanged. Slopesw'(0)=b,w'(1)=1/b give k_top=d/b^2,k_bottom=d*b^2. Positive top escape and necessary bottom convexity can coexist.
Nevertheless EVERY raw radial surface in the CLOSED box
 a in[173/10000,1731/100000],d in[1999/10000,2001/10000],b in[3999/10000,4001/10000]
fails convexity in axial meridianphi0 atx15/16,theta7*pi/16. Onphi0 rho=sin(f), and planar radial convexity requires B_mer=r^2+2*r_theta^2-r*r_theta_theta>=0.
Part2's exact rational interval calculation gives
B_mer in[-9116069,-7969171]/1000000<0,
reference0 top coefficientR*(d/b^2-R)/2 in[29187,30813]/1000000>0,
bottom factor1-d-d*b^2 in[767867,768132]/1000000>0.
Other outward bounds:angle[-401030,-389536]/1e6,r[921707,924266]/1e6,r_theta[1346322,1384623]/1e6,r_theta_theta[13732981,14704412]/1e6. These are the actual cold-reproduced values. Earlier ephemeral summary hashes/bounds were wrong; actual original and clean-directory outputs match exactly.

This excludes the raw surface throughout that box, NOT convex hulls of sampled points, all warps, or the full DLVfamily. No exact mass balance is asserted. The numerical scouta=.017304671757133214 lies in the box but has nonzero finer-quadrature residual.

## Recovery identities and commands
Part2 includes whole5684-byte pole_cert.py, SHA25678ed9c52ac9908634cc63d0c4f7d854cafceba95d4c8373c4a22a3ef8192ea9f. CPython3.13.5 standard library only, assertions enabled; no inputs/dependencies beyond the literal code. Save the code block as pole_cert.py with terminal newline. Run python -B -S pole_cert.py. It constructs exact interval bounds using48-term alternating Machin arctangents, degree40 sin/cos polynomials plus Lagrange remainders, and exact second-order interval automatic derivatives. Output POLE_CERT.json1468bytes SHA25644e0647a425ae87c86939929cf2c21ed0c4f745bc300a6079c9e74afd9b1c521. Observed marker DLV_MOBIUS_SCOPED_NONCONVEXITY_EXACT_PASS 1468 44e0647a425ae87c86939929cf2c21ed0c4f745bc300a6079c9e74afd9b1c521. Clean-directory replay reproduced the exact bytes.

Next constructive direction: independently localized sharp top or finite cap with actual mass/trueedges/globalconvexity checks, not unchanged top refinement or a global latitude warp justified only by pole tests. This theorem's objects/quantifiers are distinct from the separate RA37 fixed-lower-corpus all-heightS>=3 theorem.
