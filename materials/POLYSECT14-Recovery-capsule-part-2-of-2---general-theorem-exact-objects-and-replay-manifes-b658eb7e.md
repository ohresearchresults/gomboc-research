# material-b658eb7e4f5a

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# POLYSECT14: complete mathematical recovery and evidence boundary

This capsule defines two new exact uniformly filled smooth strictly convex solids, POLYSECT14_AXIAL_V1 and POLYSECT14_VARIABLE_V1. Each has its actual volume centroid at the origin, exactly one nondegenerate stable and one nondegenerate unstable equilibrium, and no other equilibrium. They are NOT polyhedra; neither is assigned V,E,F or C. Neither reaches the requested strict110/weak000 polyhedral C<500 target. They do not replace the independently preserved C622 polyhedron. They are analytic construction resources and simple-arithmetic controls for the unresolved finite discretization problem.

Recovery consists of this proof/manifest and the ENTIRE immutable source material [internal-source-reference], named verify_sections.py when saved for execution. That source is 4915 UTF-8 bytes, SHA-256 fb4e4c61fa427bcbe78b5a1c4937e4ed53e343482575df03e64c9db5d56116e5. It contains every input, rational polynomial operation, certificate construction, oracle and output rule. No initial checkpoint, worker result, old sandbox, numerical optimizer or external source is needed. The separate numerical scouting method is supplementary, not an exact recovery dependency.

## General variable-radius section theorem

Let y=x^2. Choose rational polynomials P(y), Q(y), B(y) and rational lambda>0. Require B(0)=1 and B(y)>0 on [0,1]. Set H(y)=(1-y)B(y)^2. Consider the solid

K = { (lambda*x,u,v): -1<=x<=1, (u-P(x^2))^2+(v-xQ(x^2))^2<=H(x^2) }.

The section at x is a filled disk with centre d(x)=(P(x^2),xQ(x^2)) and radius r(x)=sqrt(H(x^2)). The map

(x,s,t) -> (lambda*x, P(x^2)+B(x^2)*s, xQ(x^2)+B(x^2)*t)

maps the closed unit ball bijectively onto K. Its Jacobian is lambda B(x^2)^2>0. Because B remains positive on a neighborhood of [-1,1], the map and its inverse are smooth there. Thus the complete boundary, including both tips, is globally C-infinity. This statement is stronger than the C1 tip regularity of the older CIRCLE5 seed.

For any polynomial Z define M(Z)=sum_j Z_j/(2j+1). Fubini integration over filled disks gives

Volume(K)=2*pi*lambda*M(H).

The x and v first moments vanish by parity. The u first moment is 2*pi*lambda*M(H P). Consequently the ACTUAL uniform-volume centroid equals zero exactly when M(H P)=0. This is not a prescribed reference centre. Changing H changes the mass constraint, and the code eliminates the quadratic coefficient of P using this weighted identity.

Use primes for differentiation in y and define

D=P^2+y Q^2,
R=H D,
J=lambda^2 y+H+D,
A=H H'+2y H H''-y(H')^2,
N=2P'+4yP'',
L=6Q'+4yQ'',
W=(R')^2-R(J')^2,
G=A^2-H^3(N^2+yL^2).

Suppose the SIX polynomials B, D, -R', W, -A, G are strictly positive on the entire CLOSED interval [0,1], and P(0)=a with 0<a<1. These sufficient conditions establish the claims below. They are not a necessary characterization and their failure does not exclude a solid.

### Strict convexity

For -1<x<1, direct differentiation gives

r''(x)=A(x^2)/H(x^2)^(3/2),
||d''(x)||^2=N(x^2)^2+x^2 L(x^2)^2.

The inequalities -A>0 and G>0 imply r''+||d''||<0. For every fixed unit vector e in the section plane, the scalar section support e.d(x)+r(x) is therefore strictly concave. Its physical axial second derivative is multiplied by lambda^(-2), so the same sign holds after axial scaling. K is the intersection, over e, of the sets e.(u,v)<=e.d(x)+r(x), with x in [-1,1]. These concave support profiles imply convexity. Strict concavity handles any segment whose endpoints have different x, while strict convexity of each nonzero-radius disk handles equal x. No nontrivial boundary segment exists; the two endpoint disks are singletons. Hence K is strictly convex.

### Exhaustive equilibrium classification

D>0 means d(x) never vanishes. Locally measure the angle psi on the circle relative to the direction d(x). On the smooth boundary away from the tips, squared distance from the origin is exactly

F(x,psi)=J(x^2)+2 sqrt(R(x^2)) cos(psi).

For |x|<1, H>0 and D>0, so angular criticality requires psi=0 or pi. On these two branches put f_plus(y)=J(y)+2sqrt(R(y)) and f_minus(y)=J(y)-2sqrt(R(y)). For 0<=y<1,

f_plus'=J'+R'/sqrt(R),
f_minus'=J'-R'/sqrt(R).

Since -R'>0 and W>0, one has -R'>sqrt(R)|J'|, hence f_plus'<0<f_minus'. Every critical point with |x|<1 therefore has x=0. At x=0 the only two are

U=(0,1+a,0), S=(0,a-1,0).

The Hessian in coordinates (x,psi) is diagonal at these points. Its x entry is 2 f_plus'(0)<0 at U and 2 f_minus'(0)>0 at S; its angular entry is -2a at U and +2a at S. Both equilibria are nondegenerate. The coordinate change to relative phase is smooth locally and does not alter definiteness.

At the two tips, the unique normal is axial. Their points are (+/-lambda,P(1),+/-Q(1)). D(1)>0 proves that these radial vectors are not axial, so neither tip is an equilibrium. Also H'(1)=-B(1)^2<0 makes the axial tip normal nonzero. This checks the two places excluded from the angular chart rather than silently discarding them.

The origin is a strict interior point because the x=0 disk has radius1 and centre(a,0), a<1. A support equilibrium is precisely an outward radial normal contact there. Thus the preceding radial critical-point classification is the complete equilibrium classification: exactly one S and one U, no saddle, no degenerate or additional equilibrium. The minimum and maximum radial distances are 1-a and 1+a; their ratio is (1-a)/(1+a).

## Exact object identities and all parameters

Both objects use a=1/14 and therefore radial ratio13/15, improving the analytic amplitude1/15 and ratio7/8 of POLYSECT15. This is an analytic comparison, not a polyhedral complexity record.

### POLYSECT14_AXIAL_V1

lambda=497/500,
B(y)=1,
H(y)=1-y,
P(y)=1/14-(279/560)y+(79/240)y^2,
Q(y)=11/40-(37/70)y+(5/49)y^2.

The source gives Q as a times [77/20,-37/5,10/7] and P's linear shape coefficient as -279/40, then derives the same quadratic coefficient by exact mass elimination. Volume/pi=497/375. Actual centroid(0,0,0), U=(0,15/14,0), S=(0,-13/14,0). Exact equatorial branch derivatives are f_plus'(0)=-814361/49000000 and f_minus'(0)=78139/49000000.

### POLYSECT14_VARIABLE_V1

lambda=125/126,
B(y)=1+y/170,
H(y)=1-(84/85)y-(339/28900)y^2-y^3/28900,
P(y)=1/14-(151/308)y+(25188437/80635380)y^2,
Q(y)=362/1323-(268/525)y+(185/2226)y^2.

The source gives Q as a times [724/189,-536/75,185/159], P's linear shape coefficient -151/22, and computes the exact weighted-mass quadratic coefficient. Volume/pi=337961/254898. Actual centroid(0,0,0), U=(0,15/14,0), S=(0,-13/14,0). Exact equatorial derivatives are f_plus'(0)=-472853/218207682 and f_minus'(0)=12236711/3273115230.

The AXIAL solid is simpler arithmetically and must not be discarded merely because VARIABLE opens a larger formal family. The present evidence does not establish that variable radius is the source of the amplitude improvement; axial scale and centre coefficients change too. Neither1/14 nor the numerical nominations are a proved optimum of the family.

## Exact positivity evidence

The source converts each rational power polynomial on [0,1] to its degree-n Bernstein coefficients b_i=sum_{k<=i} p_k*C(i,k)/C(n,k). It accepts a leaf only when EVERY coefficient is strictly positive. Otherwise exact de Casteljau bisection at1/2 is used. The leaves form a complete closed cover of[0,1]. This is a rational certificate, not a grid test or a floating residual.

Both objects have leaf counts {B:1,D:1,minus_Rprime:2,W:2,minus_A:1,curvature_gap:1}. The two-leaf polynomials use [0,1/2] and [1/2,1]; the others use [0,1]. Every full coefficient array and rational leaf bound is regenerated in the output JSON.

For AXIAL the degrees are0,5,5,14,0,6 respectively. Easy bounds include B>=1,D>=1/196,-A>=1,G>=559/78400. The two -R' leaf bounds are341569/11063808000 and171897/245862400. The W leaf bounds are298992273897048438198949/6126512765416243200000000000000 and2517119273031199465665767/8265972424318156800000000000000.

For VARIABLE the degrees are1,5,7,16,5,12. Easy bounds include B>=1,D>=1/196,-A>=84/85,G>=2602871/171348100. The two -R' bounds are32832116228029/335746275485405400 and335545109210232085220277017/752486204844993246876864000000. The W bounds are85158832010579065173390281/3620705851318294064951207972928000 and562674577402633716555410474008455355291196277389907724787139481757707066376767/3661662759015825544481462928813472687060087813997823992652149632688332800000000000000. The generator is the smaller complete representation of all coefficients; no certificate input array is omitted from reconstruction.

## Rational boundary and tangent oracles

Choose rational t in[-1,1] and rational e=(e1,e2) with e1^2+e2^2=1. Set
x=2t/(1+t^2), y=x^2,
rho=(1-t^2)/(1+t^2)*B(y),
p=(lambda*x,P(y)+rho*e1,xQ(y)+rho*e2).
This is an exact rational boundary point, including the tips t=+/-1.

At a boundary point define du=u-P(y),dv=v-xQ(y),px=2xP'(y),qx=Q(y)+2yQ'(y). A rational outward normal and valid global support offset are
n=(-(du*px+dv*qx+xH'(y))/lambda,du,dv), h=n.p.
The source checks the exact boundary identity before returning n,h. Global validity follows from the proved smooth strict convexity. There is no claim that a finite set of these points or planes inherits the analytic equilibrium count.

## Reconstruction and verification commands, exact file manifest

Save the entire source material [internal-source-reference], without a Markdown fence or other wrapper, as verify_sections.py. Run in an otherwise empty directory:

python -B -S verify_sections.py

The same command both reconstructs and verifies. Tested with CPython3.13.5 and standard library only; there are no nondefault hidden parameters, seeds, tolerances or external imports. Assertions must be enabled; do not use python -O. The output serialization is json.dumps(sort_keys=True,separators=(',',':')).encode(), without a final newline. Expected files:

verify_sections.py:4915bytes,SHA256fb4e4c61fa427bcbe78b5a1c4937e4ed53e343482575df03e64c9db5d56116e5.
POLYSECT14_AXIAL_V1.json:4612bytes,SHA256eba244c56cbf10b9d3ac44dc665be71aa277e0a55145aca0aa9d6765a6aab566.
POLYSECT14_VARIABLE_V1.json:12652bytes,SHA256085460e2b69023b1e26f2e782922aa2b1ce1d7d1bc64ad6a74e065f9adc22cbb.

Expected terminal markers:
POLYNOMIAL_CIRCULAR_SECTIONS_EXACT_PASS POLYSECT14_AXIAL_V1 ratio 13/15
POLYNOMIAL_CIRCULAR_SECTIONS_EXACT_PASS POLYSECT14_VARIABLE_V1 ratio 13/15
VARIABLE_RADIUS_SECTIONS_SELF_CONTAINED_RECOVERY_PASS

The first two lines also print the complete leaf-count dictionary stated above. File hashes identify reproduced bytes, not mathematical proof by themselves. The proof is the derivation above plus the exact mass identity, explicit exhaustive critical-point classification and full-interval rational positivity certificates constructed and checked by the source.

## Finite construction frontier

The unresolved task is not visual approximation. The inherited POLYSECT15 fixed m5 finite hull is C304 but has strict68/74/140 at its own filled centroid; all74 vertices are U. No finite realization of either new POLYSECT14 model is accepted here. In a finite own-centred polyhedron every strict positive escape i->j requires |p_j-c|^2-|p_i-c|^2>|p_j-p_i|^2. Coarse chords can defeat smooth radial monotonicity, and refining without regard to the physical gradient can consume the edge budget while preserving many local extrema. A useful next move is a flow-aware sparse vertex/support architecture with a single stable-face patch and unstable apex, coupled to exact finite mass correction. The new rational oracles and general mass/convexity/critical theorem make this route reproducible; they do not solve it.
