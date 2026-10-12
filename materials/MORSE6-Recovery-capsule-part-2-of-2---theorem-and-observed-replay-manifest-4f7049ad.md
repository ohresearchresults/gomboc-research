# material-4f7049ad41e6

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# MORSE6_RATIONAL_A7_100 — exact smooth body, not a polyhedron

This is an analytical construction resource for equilibrium-aware finite realization. It does NOT meet the requested finite-polyhedron/E<=249 goal and has no polyhedral V/E/F count. All exact coefficients and the entire proof checker are in Recovery capsule part1, material [internal-source-reference]. This part supplies the mathematical implication and actual observed replay receipts. No sandbox file is required to recover the body.

## Exact object

For -1<=x<=1, put y=x². At first physical coordinate X=lambda*x, take the disk with transverse centre d(x)=(P(y),x Q(y)) and squared radius H(y)=(1-y)B(y)². The filled body is

K={(lambda*x,P(x²)+u,x Q(x²)+v): -1<=x<=1, u²+v²<=H(x²)}.

The exact source fixes a=7/100, lambda=1029667/1000000. P(0)=a. Coefficients P_k/a for k=1,3,4,5,6 are [-7736016,-11309209,49285282,-72918101,33874704]/1000000. Coefficients Q_k/a for k=0..6 are [3992830,-9033836,7320751,-36032083,88425030,-81073624,27231889]/1000000. B=[1,-42040/1000000,19011/1000000,-150151/1000000]. The only remaining P coefficient is exact mass closure:

P_2=62596542623293333606272461/134072992002035843625000000.

Equivalently, start with P_2=0 and replace it by -M(HP)/M(y²H), where M(sum a_k y^k)=sum a_k/(2k+1). This is the actual uniform-volume moment, not a vertex or surface-area moment. The normalized coefficients from numerical optimization are not the exact object until rationalization and this exact closure are performed.

## Global certificate and geometric implication

Use primes for y derivatives. Define D=P²+yQ², R=HD, J=lambda²*y+H+D,
A=HH'+2yHH''-yH'²,
N=2P'+4yP'', L=6Q'+4yQ''.
Set mu=3/10, eps=1/2000, K0=-R'-mu D, C0=-A-eps.

The exact source proves STRICT positivity on the whole closed interval [0,1] of
B; D; K0; K0²-HD(J')²; C0; C0²-H³(N²+yL²).
It converts each rational power polynomial to its exact Bernstein coefficients and recursively bisects at rational midpoints. Every leaf has all coefficients strictly positive, hence is a rigorous interval-wide certificate, not a sample. Observed degrees are3,13,19,44,13,32 and respective leaf counts1,1,3,5,1,4. H>=0 follows from its factorization and B>0, with H>0 in [0,1).

### Convexity and smooth tips
Writing rho(x)=sqrt(H(x²)), direct differentiation gives rho''(x)=A/H^(3/2) and d''(x)=(N,xL). The last two positivity certificates imply
-A>eps+H^(3/2)*sqrt(N²+yL²),
so rho''+|d''|<0 on -1<x<1. Thus every transverse directional support d(x).e+rho(x), |e|=1, is strictly concave. The disk body is strictly convex with positive curvature in the open section region. Smoothness at x=+-1 follows from the implicit boundary equation
F=(Y-P(x²))²+(Z-xQ(x²))²-H(x²)=0:
H'(1)=-B(1)²<0, so the x derivative of F at each tip is nonzero; its transverse Hessian there is2I. The caps have positive curvature too. No endpoint conical or flat singularity is used.

### Filled-volume centre
Parity makes the first and third volume moments zero. The second is2*pi*lambda*M(HP)=0 exactly. Volume is
2*pi*lambda*M(H)=pi*170915082372237518129/127968750000000000000>0.
Hence the actual homogeneous centroid is exactly the origin, which lies in the interior.

### Exactly two equilibria
At a non-tip circle, write psi for angle relative to its nonzero centre d(x). Since D>0, this is a smooth local angular coordinate. Squared radius is
F_rad(x,psi)=J(y)+2 sqrt(R(y))*cos(psi).
Angular criticality requires psi=0 or pi. For f_plus/minus(y)=J(y)+/-2sqrt(R(y)), the K0 certificates give
-R'/D > mu+sqrt(H/D)*|J'|.
Consequently f_plus'<0 and f_minus'>0 wherever0<=y<1. At x!=0, the x derivative2x*f_plus/minus' therefore cannot vanish. At x=0 exactly two nondegenerate critical points remain:
U=(0,107/100,0), S=(0,-93/100,0).
The two tips have outward normal along the x axis but transverse position of squared norm D(1)>0, hence are not equilibria. This exhausts the smooth surface; there are no other strict or degenerate equilibria.

In the smooth coordinates (x,psi), the Hessian at the two equilibria is diagonal with entries 2 f_plus/minus'(0) and minus/plus2a. The EXACT rational derivative values are stored in the deterministic output. Observed decimals:
f_plus'(0)=-0.06449907938439,
f_minus'(0)=0.02137980336961.
Each axial derivative magnitude is >mu*a=21/1000. These are coordinate derivative/Hessian bounds, NOT claimed intrinsic Euclidean principal eigenvalues under an orthonormal tangent basis. The radius ratio is93/107. This is a tradeoff: the ratio is slightly worse than POLYSECT14's13/15, but the particularly shallow axial minimum of that seed has been strengthened. No superiority of every shape or finite discretization metric is claimed.

## Rational boundary and support access

Part1's boundary(t,s), with nonnegative rational t and rational s, uses x=(1-t²)/(1+t²), rho=2t B(x²)/(1+t²), cos(theta)=(1-s²)/(1+s²), sin(theta)=2s/(1+s²). It returns exact rational physical boundary coordinates. The missing stereographic parameter infinities have their ordinary limits. At a rational boundary point the implicit outward normal is rational as well:

n_X=[-4x P'(y)(Y-P(y))-2(Q(y)+2yQ'(y))(Z-xQ(y))-2xH'(y)]/lambda,
n_Y=2(Y-P(y)), n_Z=2(Z-xQ(y)).

The plane n.point is its exact supporting plane. This formula is a mathematical access rule; a separate finite hull and its own finite uniform centroid must still be computed. Using the smooth seed's zero centre for a sampled hull is not justified.

## Self-contained reconstruction and actual receipts

Save the ENTIRE literal part1 as verify_morse6.py in UTF-8/LF. It has5289bytes, SHA-2567c1af605fe40ec0ca1c7d3c623706dd0a518f5b9a070d84c20e152af959e2ea2. No inputs besides this source are required; all exact parameters, rounding choices and certificate depth32 are explicit.

Reconstruction and verification command:
python -B -S verify_morse6.py

Actually executed with CPython3.13.5, standard library only. It exits successfully and prints:
MORSE6_EXACT_MASS_CONVEXITY_TWO_CRITICAL_POINTS_PASS
MORSE6_NORMALIZED_RADIAL_GAP_GT_3_10_PASS

Output MORSE6_RATIONAL_A7_100.json is4643bytes, SHA-25663c5fb7bd35376facca8994e770f2dc9e6f5d2b200fe8b006d41926d8393a5ca. It contains complete rational P/Q/B coefficients, exact volume and derivatives, and every Bernstein leaf interval/lower coefficient. Re-running this source reconstructs those output bytes; the hash is not a replacement for the source.

The captured stdout file morse6_exact_stdout.txt is591bytes, SHA-2566e55c38ac2938a2b970a5f3c6cf3ebf19781814e045aa220004bd9a529de8146, provided the source is saved under the prescribed filename. Exact source/output identities were observed, not merely predicted.

## Limits and next constructive question

This improves a reusable analytical seed, not the accepted polyhedral endpoint. A coarse mesh can create many equilibria even when its Hausdorff error is small. A useful finite arrow p->q needs |q|²-|p|²>|q-p|² at the SAME actual finite-body centre. Critical patches require a stable maximal face and unstable vertex rather than blindly copied smooth samples. The remaining research question is whether this more robust profile can support such a finite mass-compatible mesh with E<=249. Neither the numerical profile optimization nor the six sufficient certificates establishes any global maximum of amplitude, any optimality, or an edge bound.
