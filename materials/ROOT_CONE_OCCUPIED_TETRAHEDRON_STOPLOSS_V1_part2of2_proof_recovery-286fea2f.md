# material-286fea2f58af

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 2/2: ROOT_CONE_OCCUPIED_TETRAHEDRON_STOPLOSS_V1

## Evidence, scope, and exact dependencies
This is a coordinator analytic necessary-bound theorem for actual uniformly filled root-only bodies, with an exact formal relaxation separator and three actual low-trace controls. It is NOT a proof of the whole T<51/25 theorem, NOT a class110 construction, and NOT an exclusion of V10/E17/F9. The accepted mechanical bounds remain 34<=Cmin<=622.

The complete runnable source, recovery capsule part 1/2, is material [internal-source-reference], named ROOT_CONE_OCCUPIED_TETRAHEDRON_STOPLOSS_V1_part1of2_occupied_exact.py.txt. Its literal UTF-8 content is 10381 bytes, SHA-256 6eb33808fbb382030c89af0d9f673d99bb2658fcae0c7f28d2ab6dab44d52c40. Save it unchanged as occupied_exact.py. It contains every helper, exact input, and parameter. There are no omitted files or external data. It uses only the Python standard library and exact fractions, no RNG or floating optimizer.

Conceptual predecessors, both read completely, are ROOT_A_CONE_LOCATION_MOMENT_V1 ([internal-source-reference], SHA302ded340f271dfe184b72b8f3620ee26dd10bce2e66ec192a63a5bfcec693a8) and ROOT_CONE_SLICE_DEFICIT_V2 ([internal-source-reference], SHA52810e09ba8f0060504a4fdaef2e9638f61d48bc118cea2faea9eb535515196d). The latter's complete usable code is [internal-source-reference], not the inaccessible original code ID mentioned in its prose. The theorem below is self-contained; those older sources are needed only to reconstruct the earlier research history.

## 1. Actual geometry and measure
Normalize a=1. In original coordinates A=0, B=e_z, C=e_y, D=e_x. Let T0=conv(A,B,C,D) and P=conv(T0,F), where F is a compact positive-area convex polygon in ell=0, x>0, y>0. Assume 0<b,c,d<1 and
ell(x,y,z)=1-delta*x-epsilon*y-alpha*z,
alpha=1-b, epsilon=1-c, delta=1-d, eta=alpha*epsilon*delta.
Negative z is unrestricted in number among root vertices; no stationarity is assumed. The protected ABC and ABD are true maximal triangles.

Let V be ORIGINAL uniform volume, g its actual volume centroid, t=6V, u=4g_x, v=4g_y, w=4g_z, m=4ell(g). Change variables X=delta*x, Y=epsilon*y, q=ell. The absolute Jacobian is eta. In these coordinates:
A=(0,0,1), B=(0,0,b), C=(0,epsilon,c), D=(delta,0,d).
Write Delta=conv((0,0),(1,0),(0,1)), K=conv(Delta,F_XY), kappa=2Area(K)>=1, and
Q={(X,Y,q): 0<=q<=1, (X,Y) in (1-q)K}.
The radial A-projections of B,C,D are the three vertices of Delta, so transformed P is contained in Q. Set M=max(b,c,d). For q>=M the canonical tetrahedron section is exactly (1-q)Delta, and every A-to-root segment is filled; therefore P_q=Q_q for q>=M.

The volume/moment normalizations are
Vol(P_tilde)=eta*t/6,
24 integral_P q=eta*t*m,
24 integral_P X=eta*t*delta*u,
24 integral_P Y=eta*t*epsilon*v.
All these refer to one actual body. No projective uniform refilling or independent location variables are used.

## 2. Planar stochastic domination (stronger than just an upper first moment)
Fix positive cost weights A_w,B_w. Put a_w=max(A_w,B_w), b_w=min(A_w,B_w). If A_w>=B_w, let R_K=conv((0,0),(kappa,0),(0,1)); if B_w>A_w, interchange X and Y in this definition. This reference triangle has the same area as K and contains Delta, but is only a comparison body, not an assertion about the actual axes of K.

For every nondecreasing function Psi for which the integrals exist,
integral_K Psi(A_w X+B_w Y) <= integral_R_K Psi(A_w X+B_w Y).    (S)

Proof. Let s=A_w X+B_w Y and let f(s) be the coarea section width, so the cost distribution has density f. Up to s=b_w, the whole quadrant sublevel triangle is contained in Delta, hence f(s)=s/(A_w B_w) and f(b_w)=1/a_w. Beyond b_w, convexity makes f concave on its support. Its remaining mass is (a_w*kappa-b_w)/(2a_w). Concavity above the chord to the terminal support height S gives remaining mass >=(S-b_w)/(2a_w), hence S<=a_w*kappa. Compare with the reference triangle's width g(s)=(a_w*kappa-s)/(a_w*(a_w*kappa-b_w)) on [b_w,a_w*kappa]. On [b_w,S], f-g is concave and zero at b_w; its sign can change only from positive to negative. Past S it is nonpositive after f is set to zero. Equality of total masses implies that every cumulative integral of f-g is nonnegative. Thus the actual cost distribution is stochastically smaller. The kappa=1 or coincident-breakpoint limits follow directly from K=Delta or by continuity. No concavity of the zero extension past S is asserted.

Let R=cone(A,R_K). Applying (S) slice by slice is valid for increasing functions of cost with any fixed q-dependent additive term. Also
24 integral_R (A_w X+B_w Y)=C_w:=a_w*kappa^2+b_w*kappa.

## 3. An exact tetrahedron positive-part integral
For four real knots z0,z1,z2,z3, let
D(z0,z1,z2,z3)=[z0,z1,z2,z3](s_+^4),
the third confluent divided difference; repeated knots use the corresponding derivatives. For an affine function Z on a tetrahedron with these vertex values,
integral_tetra Z_+ = Vol(tetra)*D(z0,z1,z2,z3)/4.             (DD)
For example, the Hermite-Genocchi formula gives D=24 times the integral of Z_+ over the standard simplex, whose volume is 1/6, proving (DD). The source implements a cancellation-free rational formula for all sign patterns and separately checks it against a confluent difference table for all 625 quadruples from {-2,-1,0,1,2}.

## 4. Two-parameter occupied-tetrahedron upper bound
For any H,L in R, write Z=A_w X+B_w Y+Lq-H and define
r_plus=(L-H, -H, b_w-H, a_w*kappa-H),
t_minus=(H-L, H-L*b, H-L*c-B_w*epsilon, H-L*d-A_w*delta).
Then
eta*t*(A_w*delta*u+B_w*epsilon*v)
 <= kappa*D(r_plus)+4*eta*t*H-eta*t*m*L-eta*D(t_minus).       (O1)
Indeed integral_P Z <= integral_Q Z_+ - integral_T0 Z_- because T0 is occupied and P is contained in Q. Domination (S) bounds the positive-part term by R's. Formula (DD), Vol(R)=kappa/6 and Vol(T0_tilde)=eta/6 give (O1).

The subtraction is essential: an area deficit cannot be placed inside the canonical tetrahedron, even if its scalar height law otherwise satisfies Brunn-Minkowski and cone domination.

## 5. Exact top section improvement
Define
r_top_minus=(H-L, H-L*M, H-L*M-b_w*(1-M), H-L*M-a_w*kappa*(1-M)),
t_top_minus=(H-L, H-L*M, H-L*M-A_w*(1-M), H-L*M-B_w*(1-M)).
The right side of (O1) can be decreased by the nonnegative quantity
G_top=(1-M)^3*[kappa*D(r_top_minus)-D(t_top_minus)].          (O2)

Proof. Split the integral at q=M. Below M use the positive-part comparison and subtract only T0 below M. Above M use P_q=Q_q and compare the LINEAR cost integral to R_q; the equal slice areas keep the Lq-H term unchanged. Thus integral_P Z is at most integral_R Z_+ - integral_R_top Z_- - integral_T0 Z_- + integral_T0_top Z_-. This is exactly (O1) minus (O2). R_top contains T0_top because R_K contains Delta, so G_top>=0. This argument does not wrongly subtract an unknown Q-top negative-part integral after replacing Q by R.

In particular set A_w=(1+b+c)/delta and B_w=(1+b+d)/epsilon. The left side is eta*t^2*m*T, where
T=((1+b+c)u+(1+b+d)v)/(t*m).
The two-parameter bound is directly a bound on the original trace of the same body.

## 6. Equivalent convex deficit problem and relation to V2
Put D0=kappa-eta*t, D1=kappa-eta*t*m. Define the fixed available-deficit region
Omega=(R intersect {q<M}) minus T0_tilde.
The top-corrected right side has the particularly useful form
B(H,L)=C_w-4H*D0+L*D1+24 integral_Omega (H-Lq-A_w X-B_w Y)_+. (O3)
This follows from Z_+=Z+Z_-, the exact reference cone moments, and the top subtraction. In particular B is a convex function of the two real parameters H,L. The exact bound is inf_{H,L} B(H,L); a finite minimizing pair need not exist on a boundary case.

The associated reference deficit problem minimizes integral_Omega cost*f subject to 0<=f<=1, integral f=D0/6, integral q*f=D1/24. For any H,L, the lower bound on this cost is H D0/6-L D1/24-integral_Omega(H-Lq-cost)_+. Thus (O3) is its two-moment dual. An actual P supplies an admissible slice-mass deficit on the reference region because Area(R_q)=Area(Q_q), Area(T0_q)<=Area(P_q)<=Area(Q_q), and P_q=Q_q above M. This is a relaxation of geometry, not a construction of P from an optimizer. Interior differentiable optima satisfy that the removed halfspace in Omega has volume D0/6 and q moment D1/24. The convex formulation avoids a misleading nonconvex search over independent centroid variables.

For comparison with the old quadrant barrier let
Theta_low=eta*D(t_minus)-(1-M)^3*D(t_top_minus)>=0.
Using integral_quadrant (s-A_w X-B_w Y)_+=s_+^3/(6A_w B_w) gives
C_w-eta*t*(A_w*delta*u+B_w*epsilon*v)
 >=4H*D0-L*D1-[4/(A_w B_w)] integral_0^M (H-Lq)_+^3 dq+Theta_low. (O4)
The integral is [H_+^4-(H-LM)_+^4]/(4L) for L!=0, and M H_+^3 for L=0. The finite-reference bound (O3) is at least as strong as (O4). Removing Theta_low gives a V2 affine-test consequence. Thus the new family strengthens the old family by a compulsory location correction, not by changing the height marginal.

## 7. Full-height version and concrete next interface
For every measurable test profile phi(q), the slice argument proves
integral_Pq cost <= integral_Rq (cost-phi(q))_+ + phi(q)*Area(P_q)
                    - integral_T0q (phi(q)-cost)_+.         (O5)
The canonical slice is the explicit polygon
X,Y>=0, X+Y<=1-q,
((d-b)/delta)X+((c-b)/epsilon)Y <= q-b.
For a prescribed actual height density, d_*(q)=kappa(1-q)^2-eta*t*p(q)/3 is twice the deficit area. In the reference slice the deficit of area d_*/2 must be selected from R_q minus T0_q, not from the whole quadrant. Its least cost is obtained by cost sublevel sets in that available polygon. The sublevel area is piecewise quadratic in the threshold; the threshold is recovered from the exact area demand. This is the natural next coupling to the existing exact four/seven C-fan height laws. A global optimization over the admissible endpoint/volume/fan data, or a T>=51/25 contradiction, has NOT been carried out here.

## 8. Exact formal separator from all old V2 families
The source uses
b=1/2, c=13/20, d=1/10, h=1/2, kappa=1,
eta=63/400, D=1-h^2*c=67/80,
t=D/eta=335/63, m=(1-h^2*c^2)/D=1431/1340,
u=(1-h^3*c)/((1-d)*D)=245/201,
v=(1-h^3*c)/((1-c)*D)=735/469,
w=(4-(1-d)u-(1-c)v-m)/(1-b)=20583/18760.
These are the actual moments of the SHADOW cone R_Delta cut by X+Y+(h/c)q>=h. That shadow excludes canonical B, so it is NOT a proper root-only body.

Its complete normalized height law is
p(q)=3[(1-q)^2-h^2(1-q/c)_+^2]/D.
It is positive for 0<=q<1; its square root is concave on the lower quadratic interval and linear above c, with a C1 join at c. The lower quadratic has nonpositive 4ac-b^2, directly giving square-root concavity. Cone domination is immediate. The source verifies exact piecewise polynomial identity to the positive four-law mixture
lambda*mu[1,b,c,d]+rho*mu[c,0,0,0]+omega*mu[c,d,0,0]+gamma*mu[c,b,d,0],
with lambda=63/335, rho=39/67, omega=14/335, gamma=63/335.
The exact seven C-fan masses in the canonical order T0,CFFF,CBFF,CDFF,CAFF,CBDF,CADF are [lambda,rho,0,omega,0,gamma,0]. They are formal masses, not a realization claim.

The deficit is d_*=h^2(1-q/c)_+^2, so D0=h^2*c, D1=h^2*c^2,
Lx=Ly=h^3*c, I=integral d_*^(3/2)=h^3*c/4.
Thus the unweighted V2 inequality Lx+Ly>=8I is equality. Every weighted V2 inequality follows from (A_w+B_w)>=2sqrt(A_w B_w). All affine Holder/test consequences hold because this is the actual nonnegative deficit density and the basic weighted bound holds. The integral strip constraints also hold: integral d_*^2/(1-q)<=h^4*c/4, hence 3 times this integral < h^3*c since h=1/2. The inequality follows pointwise from (1-q/c)/(1-q)<=1 and integration of (1-q/c)^3 over [0,c]. The radial inequality lambda*(4-m)^3>27eta and the listed endpoint/location scalar constraints are checked exactly.

At A_w=B_w=1, H=h=1/2, L=h/c=10/13, the old affine quadrant bound is equality and G_top=0. The occupied-tetrahedron correction is exactly
Theta_low=729/2768480>0,
so the new bound strictly excludes this formal tuple. Its trace is only
T=42973/31959 approximately 1.34463 <51/25.
This is a strict separation of necessary-condition families, not a high-trace counterexample. The source does not claim every historical stationarity or product inequality passes.

## 9. Exact actual controls
All original inputs are in part 1/2. The three controls have a=1 and the following b,c,d and four root points in XY coordinates:
I: (1/2,13/20,1/10), root [(1/10,3/20),(6/5,1/5),(13/10,7/10),(1/5,11/10)].
II: (4/5,2/5,1/5), root [(1/8,1/8),(9/8,1/8),(5/4,1),(1/8,5/4)].
III: (1/4,3/5,2/5), same root list as I.
All have three negative-z root vertices, exact f-vector (8,17,11), actual protected ABC and ABD, and one maximal root quadrilateral. They are geometric trace controls, not own110 examples; in particular V=8 violates the accepted own110 vertex lower bound.
The source reconstructs all maximal facets/true edges with rational determinant signs and matches exact volume and first moments from two different complete apex fans, based at A and C. It checks seven H,L pairs for each of two cost weights on all three bodies, giving 42 exact top-corrected bound checks.
The exact resulting values are:
I: t=562/45, kappa=227/100, m=83499/78680, T=275606515/328485066.
II: t=295/12, kappa=85/32, m=9807/9440, T=3361647/7714840.
III: t=98/9, kappa=227/100, m=4229/3920, T=1642383/1657768.
These computations are controls of the stated analytic bound; no equilibrium census or generic independent worker audit is implied.

## 10. Reconstruction and exact byte verification
Environment used: CPython 3.13.5, standard library only, assertions enabled. No non-default numerical tolerances, random seeds, or external inputs. The code itself generates the complete report deterministically. In a directory containing the unchanged part 1/2 source saved as occupied_exact.py, run:

    python -S occupied_exact.py > occupied.out
    wc -c occupied_exact.py occupied_controls.json occupied.out
    sha256sum occupied_exact.py occupied_controls.json occupied.out

Expected files:
occupied_exact.py: 10381 bytes, SHA256 6eb33808fbb382030c89af0d9f673d99bb2658fcae0c7f28d2ab6dab44d52c40
occupied_controls.json: 18333 bytes, SHA256 aa9120c204ab1b9322d20b14ba0408f0b0134813cb79cfbcdd721978413fd608
occupied.out: 475 bytes, SHA256 431b9766c9e1c9f53bb717f771fcc2def65782816c60425c4566e1e181b046bd

The complete expected terminal output is:
EXACT_CONFLUENT_STOPLOSS_625_KNOT_QUADRUPLES_PASS
FULL_HEIGHT_LAW_AND_ALL_V2_FAMILIES_FORMAL_SEPARATOR_PASS
OCCUPIED_CANONICAL_TETRAHEDRON_STRICTLY_EXCLUDES_FORMAL_POINT
formal_T=42973/31959
formal_obstacle=729/2768480
THREE_ACTUAL_MULTIPLE_NEGATIVE_ROOTS_TWO_VOLUME_FANS_PASS
42_EXACT_TOP_CORRECTED_STOPLOSS_TESTS_PASS
report_bytes=18333
report_sha256=aa9120c204ab1b9322d20b14ba0408f0b0134813cb79cfbcdd721978413fd608
ROOT_CONE_OCCUPIED_TETRAHEDRON_STOPLOSS_V1_RECOVERY_PASS

A coordinator execution produced these exact files and passed all assertions. The proof, exact code, and literal inputs are now durable in these two parts. Hashes only identify bytes; reconstruction depends on the supplied complete source. No separate cold reproduction is claimed.
