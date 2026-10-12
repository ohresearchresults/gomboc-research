# material-374567256c73

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# ACTUAL_PROJECTION_MOMENT_CAPACITY_V1
## Recovery capsule part 2 of 2: complete analytic proof, exact formal separations, reconstruction

## 1. Status and scientific scope
The new claims are necessary conditions for the ACTUAL projected geometry of a uniformly filled two-anchor convex body at a FULL marked-body/affine-root joint local maximum. They are not sufficient realization conditions, a determination of the trace maximum, a new equilibrium construction, or an exclusion of all V10/E17/F9. The accepted complexity interval remains 34<=C_min<=622. A formal moment tuple is NEVER called a body here. In particular the exact controls P1 and P2 below have no asserted polyhedral realization.

The analytic results are: sharp all-degree projected-moment upper bounds with equality cases; an explicit strictly positive gap above the root-area Cauchy bound forced by actual planar level-set capacity; covariance-eliminated first/second projected-moment cuts; and additional moment-capacity inequalities. The finite exact computation certifies two specified formal separations and selected algebraic checks, not the universal proofs.

Exact prior sources used, all read completely by the author:
- [internal-source-reference], JOINT_MASS_EQUALITY_AND_E17_NO_UNIFORM_GAP_V1, SHA256 2c460625df162099bfba6437818bd8eff154d6d2f17d3f21e9ac2e4211c4d18e, 40615 bytes. Contains the first-degree planar section lemma. Section 3 below extends its one-crossing argument to all increasing functions and applies it to the ACTUAL projection rather than just an auxiliary radial body.
- [internal-source-reference], TWO_ANCHOR_PROJECTED_MASS_OBSTRUCTION_V1, SHA256 04208701b3956e834908a02b2ffacbc4a05ce01be9e36a1535905bf5fdc2df72, 17871 bytes. Its exact-code recovery erratum is [internal-source-reference], SHA256 af41a30f6e0977119943bc9ecf98885ae9b10988c58ed93399f0dfafd0605de3. We do not need to execute that earlier source for the present certificate.
- [internal-source-reference], ROOT_DUALITY_JOINT_VARIATIONS_V1, SHA256 73eb04d63deeab693d29533819d3b95c4e1af3cc01d756987381aaa2bb4c2ed8, 18784 bytes. Gives actual joint root moments and canonical-fixing projective covariance identities used below.
- [internal-source-reference], ROOT_FAN_BERWALD_MOMENT_OBSTRUCTION_V1, SHA256 b1d05ed4c84512cf48852d5383ffcc3ff2a066c1b7f6b5777fe62d372c0cb559, 20592 bytes. Gives earlier selected actual fan/covariance necessary tests. Its old formal51/25 datum was subsequently excluded by projection and is not a body.
- [internal-source-reference], POLYHEDRAL_TRACE_STATIONARITY_RIGIDITY_V1, SHA256 8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9. Gives the conditional two-anchor sector. Its historical90-bound and attainment caveat do not replace later results.

## 2. Notation and the actual-geometric premises
Let A0=(0,0,0), B=(0,0,1), C=(0,1,0), D0=(1,0,0), and T0=conv(A0,B,C,D0). The uniformly filled convex body P contains T0 and is contained in {x>=0,y>=0,ell>=0}, where
ell=a+(d-a)x+(c-a)y+(b-a)z,
a>b>0, c>0, d>0.
ell is an affine supporting function, NOT a mass density. All volume means and covariances below are those of the actual uniform body P.

Put alpha=a-b, hc=a+b+c, hd=a+b+d, n=hc*x+hd*y, D=hc*hd, hmin=min(hc,hd), hmax=max(hc,hd). Write V=vol(P)=t/6, g=(u,v,z)=centroid(P), p=u+v, r=n(g), Eell=integral_P ell, N=integral_P n, T=N/(6 V Eell), q=N/Eell=t*T, mu=ell(g)=r/q, m=3p/t. Define G=n-r-q*ell. Assume the full marked-body/root joint local-maximum conditions, the actual two-anchor geometry, and G(C),G(D0)>=0. Thus G(C)=hd-r-q*c and G(D0)=hc-r-q*d; in particular 0<r<hmin.

The high-trace sector used here has t>1 and q>3p. Then actual root moments below imply r>nw. We do not infer these premises for an arbitrary body or a fixed-lattice-only maximum.

The two-anchor representation is
P={x,y>=0: hA(x,y)<=z<=min(1-hB(x,y),H-l0(x,y))},
where hA,hB are convex homogeneous functions, H=a/alpha,
l0=((a-d)x+(a-c)y)/alpha,
k=hA+hB, j=hA+l0.
Its projected fibre length and actual projected sets are
L=min(1-k,H-j)_+,
K={x,y>=0:k<=1,j<=H},
R={x,y>=0:j<=H,j-k>=H-1}.
K is the ACTUAL convex projection of P and contains Delta={x,y>=0:x+y<=1}. R is the actual projection of its root facet. Put A=area(K), AR=area(R). This use of A for area is distinct from canonical A0.

For homogeneous f of degree d>=0, an exact identity is
(d+3) integral_P f = integral_K f+(b/alpha) integral_R f. (2.1)
Here f depends only on x,y. A direct proof: on the nonroot region L-(x,y).grad L=1, on the root region it equals H. Integrate div((x,y) f L) over K. The outer fibre boundary has L=0, and on the coordinate axes the normal product with (x,y) vanishes. Since (x,y).grad f=d*f, integration by parts gives (2.1). Polyhedral break lines have cancelling contributions; the same formula follows by piecewise integration. No independent projected weights are introduced.

Let w=(v/(3p),u/(3p),1/3) and nw=n(w)=(hc*v+hd*u)/(3p). The true joint root variation identities are
W1:=integral_R(n-r)=alpha*t*(q-3p)/6,
W2:=integral_R(n-r)^2=alpha*t*p*(r-nw)/2. (2.2)
In this sector W1,W2>0 and n-r>=0 on R (strict away from irrelevant null boundaries). Consequently
A+(b/alpha)AR=t/2,
NR:=integral_R n=r*AR+W1,
NR2:=integral_R n^2=r^2*AR+2r*W1+W2,
NK:=integral_K n=r*(A+t/6)-b*t*(q-3p)/6. (2.3)
These exact identities are the bridge between shape, area and actual mass. Arbitrary formal tuples satisfying them need not have any realization.

## 3. Sharp projected stochastic and all-degree bounds
THEOREM 3.1. Let K be ANY compact convex subset of the positive quadrant containing Delta and having area A>=1/2. Put s=x+y. The distribution of s outside Delta, with its ordinary area measure, is dominated for every increasing integrand by the profile
b0(w)=(1-w/(2A-1))_+, w=s-1>=0,
with the A=1/2 case interpreted as zero exterior area. In particular
max_K s<=2A,
integral_K s^d <= [2A/((d+1)(d+2))] sum_{i=0}^d (2A)^i, d=0,1,2,... . (3.1)
For each strictly increasing test (in particular d>=1), equality is exactly
K=conv{(0,0),(1,0),(0,1),p0}, p0>=0, p0_x+p0_y=2A,
including the limiting axial triangles and K=Delta when A=1/2.

PROOF. Use coordinates (s,x); their Jacobian relative to (x,y) is one. The width of the section x+y=s is exactly s for 0<=s<=1, since K contains all of Delta and lies in the quadrant. For s=1+w write its width b(w). Convexity makes b concave on its support [0,H], with b(0)=1 and terminal width nonnegative (it can be positive at a terminal edge). Therefore W:=integral b=A-1/2>=H/2, so H<=2W. Compare with b0(w)=(1-w/(2W))_+. On [0,H] the difference b-b0 is concave, vanishes at zero, and its quotient by w is nonincreasing. Hence it has at most one sign change, from positive to negative; beyond H it is nonpositive. Its integral is zero. For any increasing phi, subtract phi at the sign-change point: integral phi*(b-b0)<=0. This proves the stochastic assertion, including bounded increasing indicators by approximation. Integrating (1+w)^d and adding integral_0^1 s^(d+1)ds gives (3.1).
For a strictly increasing test equality forces b=b0 almost everywhere. The convex lower and concave upper section endpoints must then both be affine on [1,2A], because their difference is affine. They start at the unit segment and end at one point p0, giving exactly the asserted quadrilateral or triangle. Conversely each such body has that profile. QED.

The first moments are
integral_K s<=A(2A+1)/3,
integral_K s^2<=A(4A^2+2A+1)/6,
integral_K s^3<=A(2A+1)(4A^2+1)/10.

COROLLARY 3.2. With n=hc*x+hd*y as in Section2,
max_K n<=2A*hmax,
integral_K n^d <= [2A/((d+1)(d+2))] sum_{i=0}^d (2A*hmax)^i*hmin^(d-i). (3.2)
PROOF. Scale x,y by hc/hmin,hd/hmin. The new convex set still contains Delta, its area is A*hmax/hmin, and its s-coordinate is n/hmin. Apply (3.1) and change variables. The bounds are sharp under the ORIGINAL Delta-containment condition: when hc>hd choose K=conv{0,(2A,0),(0,1)}; reflect for hd>hc. When hc=hd all equality quadrilaterals in Theorem3.1 remain. QED.

In particular define
U1(A)=A(hmin+2A*hmax)/3,
U2(A)=A(hmin^2+2A*hmin*hmax+4A^2*hmax^2)/6.
These are stronger than using the coarser t-scaled simplex because actual root area makes 2A<t.

## 4. Actual level-set capacity and a quantitative strict Cauchy gap
For an arbitrary measurable subset R of {x,y>=0,n>=r}, write g0=n-r, with r>0. Ordinary quadrant area pushed forward by g0 has density (r+g0)/D. Therefore the density of the subset R is bounded ABOVE by (r+g0)/D. This elementary geometric capacity, not just positivity of a moment matrix, is essential.

THEOREM 4.1. Suppose W1=integral_R g0>0 and W2=integral_R g0^2>0 are finite. Put
gamma=W2/W1, s0=W1^2/W2,
kappa=4(r+gamma)*gamma/(3D*s0),
epsilon=min(1/2,1/(2*kappa)),
S_epsilon=[s0-4(r+gamma)*gamma*epsilon^3/(3D)]/(1-epsilon^2).
Then
area(R)>S_epsilon>s0,
S_epsilon-s0>=s0*epsilon^2/[2(1-epsilon^2)]>0. (4.1)
No convexity of R is required.

PROOF. For any 0<L<U the polynomial (g0-L)(g0-U) is nonnegative outside [L,U] and nonpositive inside. The density bound therefore gives
W2-(L+U)W1+LU*area(R)
 >= - (2r+L+U)(U-L)^3/(12D). (4.2)
Equality can occur only when R agrees, up to a null set, with the full quadrant band L<=g0<=U. Indeed one must fill the negative interval to its full capacity and use no positive-polynomial mass outside.
Take L=gamma(1-epsilon), U=gamma(1+epsilon). Equation(4.2) gives area(R)>=S_epsilon. Equality is impossible for this choice: in the full band, putting g0=gamma+v, the integral of g0(g0-gamma) has sign equal to
integral_{-epsilon*gamma}^{epsilon*gamma} (r+2gamma)*v^2 dv>0,
whereas the defining relation gamma=W2/W1 requires that integral to be zero. Hence the first inequality is strict. Finally kappa*epsilon<=1/2 and
S_epsilon-s0=s0*epsilon^2*(1-kappa*epsilon)/(1-epsilon^2),
proving the explicit gap. QED.

This is stronger than the qualitative strict Cauchy inequality for planar sets. It quantifies why a root cannot collapse all its area onto the single value W2/W1 while retaining those first two moments. Optimizing L,U in (4.2) may strengthen it further; the explicit rational choice already suffices for exact separations.

## 5. Eliminating the entire root-area parameter
From (2.3), strict Cauchy and Theorem4.1, put
A_C=t/2-(b/alpha)*s0,
A_Q=t/2-(b/alpha)*S_epsilon.
Then every actual body obeys
1/2<=A<A_Q<A_C. (5.1)
In particular A_Q>1/2 is necessary.

Combine NK in (2.3) with NK<=U1(A). This gives
Phi(A):=2hmax*A^2+(hmin-3r)A-r*t/2+b*t*(q-3p)/2>=0. (5.2)
For A>=1/2,
Phi'(A)=4hmax*A+hmin-3r>=2hmax+hmin-3r>0,
because r<hmin. Thus
Phi(A_Q)>0 (and the weaker Phi(A_C)>0) (5.3)
is NECESSARY. This excludes the complete root-area freedom for fixed primitive parameters a,b,c,d,t,u,v,z,T obeying the stationarity identities. It is not a test at one chosen covariance or one chosen rho.

## 6. Eliminating the whole covariance completion fibre
Let Sigma=Cov_uniform(P). Inclusion of the actual tetrahedron T0, whose centroid is g0=(1/4,1/4,1/4) and covariance Sigma0=(4I-11^T)/80, gives
Sigma>=Q0:=Sigma0/t+(g-g0)(g-g0)^T/(t-1). (6.1)
This follows by decomposing uniform volume into T0, of mass fraction1/t, and its complement, retaining the exact between-mean covariance and dropping only the complement's PSD within-covariance. It does not introduce arbitrary masses.

Let beta=grad n-q*grad ell and
hvec=(4r*u-(a+b+2d)*v, 4r*v-(a+b+2c)*u, 4r*z-r-b*p)/5.
The actual canonical-fixing projective variation gives
Sigma*beta=hvec. (6.2)
Set y=hvec-Q0*beta and delta=beta.y. If delta<0, no PSD completion exists. If delta=0, it is necessary that y=0, in which case put Qstar=Q0. If delta>0, put
Qstar=Q0+y*y^T/delta. (6.3)
Every Sigma satisfying (6.1)-(6.2) obeys Sigma>=Qstar. To see this, set S=Sigma-Q0>=0. Then S*beta=y and beta^T*S*beta=delta. Cauchy-Schwarz for the PSD form S gives S>=yy^T/delta. The zero-delta case follows from S*beta=0.

Write sigma_min^2=(grad n)^T Qstar (grad n). Formula(2.1) for n^2 yields
integral_K n^2=r^2(A+t/3)+(5t/6)Var_P(n)-(b/alpha)(2rW1+W2).
Consequently
Psi(A):=U2(A)-r^2(A+t/3)+(b/alpha)(2rW1+W2)-(5t/6)sigma_min^2>=0. (6.4)
Moreover
Psi'(A)=hmin^2/6+(2/3)A*hmin*hmax+2A^2*hmax^2-r^2
 >=hmin^2-r^2>0 for A>=1/2.
Therefore
Psi(A_Q)>0 (and the weaker Psi(A_C)>0) (6.5)
is necessary. Equations(5.3),(6.5) eliminate ALL PSD covariance completions consistent with the retained actual stationarity data. They do not certify that Qstar, or any completion above it, is itself a realizable body covariance.

## 7. Additional reusable capacity constraints
For ANY measurable Q in the positive quadrant with area A, the minimum of integral_Q n^d for increasing n^d is the full triangle cut out by n<=sqrt(2DA). In particular
integral_Q n^d >= (2DA)^((d+2)/2)/((d+2)D), d>=0. (7.1)
This follows by exchanging area at larger n for missing available area at smaller n; equivalently integrate the level density n/D. For d=0 it is equality identically.

A sharper fixed-area/fixed-first-moment statement uses bands. If M1=integral_Q n and M2=integral_Q n^2, the minimum possible M2 at fixed A,M1 is attained by a full band ell0<=n<=h0. Write S=h0+ell0, Delta0=h0-ell0. Then
A=S*Delta0/(2D),
M1/A=S/2+Delta0^2/(6S),
M2/A=(S^2+Delta0^2)/4.
The mean has its minimum at ell0=0 and then increases strictly as S grows, so every feasible mean has a unique such band (up to the degenerate endpoint parameterization). Its optimality is proved by the polynomial (n-ell0)(n-h0), negative exactly inside the full band; equal area and first moment cancel its affine terms. This yields the strict universal variance-capacity inequality
12*M1^2*(A*M2-M1^2)>D^2*A^6 for A>0. (7.2)
For the minimizing band put lambda=Delta0^2/S^2 in (0,1]. The ratio of mean^2*variance to D^2*A^2 is (3-lambda)(3+lambda)^2/324>1/12, since (3-lambda)(3+lambda)^2=27+9lambda-3lambda^2-lambda^3>27. All other sets have at least its second moment. This proves (7.2); no uniform positive gap follows without additional parameter control.

In the stationary two-anchor situation one may also use Omega=K\({n<=r} union R), when the accepted actual core inclusion and disjointness premises hold. If Mj=integral_Omega(n-r)^j and eta=sqrt(r^2+2D*M0)-r, capacity gives
M1>=(r*eta^2/2+eta^3/3)/D,
M2<=(2A*hmax-r)*M1.
The first fills the lowest available levels above r; the second uses the actual projected support bound from Section3. These are necessary, not a claim that all formal controls below pass them. Likewise for Bj=integral_{K\Delta}n^j,
B2<=(hmin+2A*hmax)B1-2A*hmin*hmax*B0,
because hmin<=n<=2A*hmax on K\Delta. Higher-degree localizing tests may be added but do not by themselves prove a geometric realization.

## 8. Two exact formal separations
Both controls use T=51/25, a=1, c=d=k, u=v=p/2, and mu=r/q fixes z by
z=[1+(k-1)p-mu]/(1-b).
The six coordinates (b,k,t,p,rho,added) are literal rational values with denominator10^6:
P1=(269757,48915,1243298,554790,151063,27397)/10^6.
P2=(148111,4990,1138318,526978,136441,29360)/10^6.
Their formal root area is AR=t(1-b)rho/(2mu), and their covariance is
Q=Qstar+added*v0*v0^T/(v0.v0),
v0=(beta_z,beta_z,-2beta_x).
Symmetry makes v0 perpendicular to beta. Both Q are exactly positive definite, dominate Qstar, and satisfy Q*beta=hvec. No actual body realizing Q is asserted.

The companion exact code explicitly enumerates THIRTY selected prior positivity/fan/projection tests, including actual tetrahedral lower covariance, ell-Berwald, root-rho bounds, root fan-BERWALD, Omega and exterior Hankel tests, an earlier scalar root-band test, a root-centroid container and K-Berwald. Its test list is the precise claim; it is NOT stated to be every necessary condition in the historical archive. The square root in the old root-band test is bypassed by exact rational lower cutoffs79/100 for P1 and67/100 for P2, checked against the defining quadratic.

P1 passes all thirty selected tests strictly, but Phi(A)<0 and even Phi(A_C)<0. The new planar first-moment cut therefore excludes the WHOLE root-area/covariance fibre over its primitive parameters, rather than just the displayed covariance.

P2 passes all thirty selected tests strictly and also Phi(A)>0, Phi(A_C)>0 and Psi(A_C)>0. Nevertheless Phi(A_Q)<0. Numerically only for readability, A is about0.5252048635, A_Q about0.5240524714, Phi(A) about0.00095181313 and Phi(A_Q) about-0.00106478516. The proof uses rational signs in the code, not these decimals. Thus the quantitative area gap supplies a genuine further separation beyond the earlier planar-first/Cauchy and displayed minimum-second checks. Strict signs also persist in an open neighborhood of these formal primitive parameters, but this is not a neighborhood of known actual polyhedra.

One exploratory four-parameter point passed Phi(A_C),Psi(A_C) but failed the already known Omega-first-moment condition. It is NOT a separation against the full old projection test set and is not promoted as one. Numerical search failure elsewhere is not a continuum exclusion.

## 9. Exact recovery, dependencies and terminal markers
The complete self-contained runnable source is part1, material [internal-source-reference]. Its literal bytes are the file exact_capacity_audit.py:
5898 bytes; SHA256 b5ce93ff47f37767ad19e160516ef8ca30378e8354533245e8c87eb303ca9276.
It uses only Python3.13.5 standard library (fractions, json, argparse, pathlib). There are no external numerical inputs, random seeds, omitted helpers or unstated tolerance decisions in the exact audit. Both rational checkpoints, every nondefault parameter and all tests are contained in that complete source.

Reconstruction command, after saving part1 verbatim under the stated filename:
python exact_capacity_audit.py --out projection_capacity_audit.json

The same command is the exact verification command: every assertion must pass. Expected terminal markers, in order:
EXACT_PLANAR_PROFILE_MOMENTS_OK
P1_SELECTED_30_TESTS_PASS_PHI_CAUCHY_FAILS
P2_SELECTED_30_TESTS_AND_PLANAR_FIRST_PASS_CAPACITY_FAILS
EXACT_CAPACITY_CONTROLS_OK

Expected reproduced output:
projection_capacity_audit.json,15721 bytes,
SHA256 ab9713d188a983b1092e963f593cf1166655a204a8283dd8ee99d7a6598d5325.
It is sorted/indented ASCII JSON, every exact Fraction serialized as a reduced rational string, ending with one newline. It contains all thirty positive margins, complete exact Qstar and Q, area bounds and Phi/Psi values for both controls. The source also audits the closed planar moment formula for degrees0..8 at A=1/2,3/4,2,17/6; this finite check supplements, rather than replaces, the all-degree analytic proof.

Byte/hash verification command:
python -c "from pathlib import Path;from hashlib import sha256;[(print(p,len(Path(p).read_bytes()),sha256(Path(p).read_bytes()).hexdigest())) for p in ['exact_capacity_audit.py','projection_capacity_audit.json']]"

Floating locators used for discovery are not prerequisites for recovering or verifying this result. Their complete method sources are preserved separately as an explicitly nonproof companion. This two-part capsule contains everything required for the exact claimed construction of FORMAL moment controls and its mathematical verification; it contains no purported equilibrium attainer.
