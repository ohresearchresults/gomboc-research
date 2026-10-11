# material-73eb04d63dee

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# ROOT_DUALITY_JOINT_VARIATIONS_V1

## Status and exact scope
These are coordinator-derived analytic theorems about the ORIGINAL adjacent-triangle trace of a uniformly filled marked convex body. They supply a fixed-body polar/radial reformulation, genuine root-plane and projective stationarity, and a second-order root-edge variation. They do NOT prove the universal value T<51/25, eliminate E17, construct a new110 body, or alter34<=Cmin<=622. The rational moment control below is explicitly NOT an actual convex-body/root pair. The executable checks algebra and that formal control, not all analytic admissibility arguments.

Accepted geometric premises, where used: POLYHEDRAL_TRACE_STATIONARITY_RIGIDITY_V1, [internal-source-reference],14798B,SHA8dc6ce8812298f59a61b404ccba7c09fef867bb8844a8952bf1cacc638bcc2b9; and the complete accepted HIGH_TRACE_VARIABLE_ENDPOINT_LOCALIZATION_16_V1 result minimum-0142,40674B,SHA8fb94d359f15a77c8c5b7d6b1395ea099a9bbaecc6be1bbb741498706df275c2. Its global-attainment precursor is [internal-source-reference],15603B,SHA52786c239b2ed0a438f276cb7c2baa108b5617168f5398a25da747e2b7515379. The precise equality-body classification used only to demonstrate nonrealizability of the formal control is [internal-source-reference],40615B,SHA2c460625df162099bfba6437818bd8eff154d6d2f17d3f21e9ac2e4211c4d18e. These sources were read completely before use. No independent replay of the worker's analytic proof is asserted.

## 1. Definitions and identities
A=(0,0,0),B=(0,0,1),C=(0,1,0),D=(1,0,0),T0=conv(A,B,C,D). Let P be bounded full-dimensional convex with T0 subset P subset {x,y>=0}. In the proper class the coordinate sections are precisely the maximal triangular faces ABC and ABD. In the closed marked class they are supporting patches only; canonical points may be redundant. Never silently replace these patches by larger faces in the numerator.

ell(x,y,z)=a+(d-a)x+(c-a)y+(b-a)z>=0 on P is a nonzero auxiliary affine function, not a density. a,b,c,d are its values at A,B,C,D. Define
V=integral_P1, J=(X,Y,Z)=integral_P(x,y,z), g=(u,v,z)=J/V,
E=integral_P ell, N=integral_P n,
s=a+b, n=(s+c)x+(s+d)y,
mu=E/V=ell(g), r=N/V=n(g), q=N/E=r/mu,
t=6V, p=u+v, m=3p/t=(X+Y)/(2V^2), T=N/(6VE)=q/t.
The repeated z symbol means the third component when applied to g; integration variables are otherwise explicit.

The frozen affine shape derivative is
G=n-r-q ell, beta=grad G=(s+c+q(a-d),s+d+q(a-c),q(a-b)).
In particular G(g)=-r, beta.g=qa, G(A)=-r-qa, G(B)=-r-qb. Omitting the -r term at canonical points is incorrect.
For any change of body at fixed ell, let Delta denote the difference of actual uniform integrals. Direct cross multiplication gives
T(P')>T(P) iff Delta integral G > N Delta V Delta E/(VE).
For a differentiable body/ell family, the numerator of the first variation, up to the positive denominator6VE, is
Ndot-r Vdot-q Edot.

## 2. Exact fixed-body root duality
Define the point
w=(v/(3p),u/(3p),1/3).
Its four canonical barycentric coordinates are lambda_A=lambda_B=1/3,lambda_C=u/(3p),lambda_D=v/(3p), all positive. Thus w is strictly inside T0 and P. Direct evaluation gives
3p ell(w)=r, hence T=m ell(w)/ell(g).                    (2.1)

For a fixed P normalize ell(g)=1. Every affine function so normalized is uniquely
ell(x)=1-xi.(x-g),
and ell>=0 on P iff xi lies in the polar body (P-g)^circ. Therefore
max_{ell>=0,ell not0} T = m[1+gamma_{P-g}(g-w)],          (2.2)
where gamma_K is the Minkowski gauge of the convex body K containing0 internally. Proof: the support function of K^circ equals gamma_K. This follows directly from separation: d in lambda K iff xi.d<=lambda for every xi in K^circ. The maximum exists because the normalized affine cone is compact, or equivalently because this polar is compact.

Let s_* be the radial distance parameter for which g+s_*(g-w) belongs to the boundary of P. When g!=w, gamma(g-w)=1/s_*. Thus the maximum is m(1+1/s_*). If g=w, every normalized affine choice gives T=m and the radial expression is replaced by(2.2).

For any tau>m set
R_tau=(tau g-mw)/(tau-m)
      =(tau t u-v,tau t v-u,tau t z-p)/(tau t-3p).       (2.3)
Then all nonnegative affine roots satisfy T<=tau iff R_tau belongs to P. They all satisfy T<tau iff R_tau belongs to the interior of P. The strict statement uses compactness of the normalized affine cone and separation at a boundary point. Moreover if a particular ell gives T>m, then ell(R_T)=0; this ell is a fixed-body maximizing root iff R_T belongs to P, in which case R_T lies in its zero face.

This is an exact body-membership reformulation, not a proof that R_(51/25) lies in every eligible P. The radial exit may meet an edge or vertex, so no positive-area or unique-root assertion follows from duality alone.

## 3. Interior joint root-plane stationarity
Assume now P is a polyhedral joint local maximum of the marked body/ell problem, ell has a positive-area root facet F=P intersect {ell=0}, and a,b,c,d>0. The maximum is with respect to genuine nearby uniformly filled convex bodies and the auxiliary affine function, not just a fixed vertex count. Assume the accepted local-maximum property G(v)>0 at every noncanonical vertex; in this interior endpoint stratum every root vertex is noncanonical, so G>0 throughout F.

Represent P by all its facet inequalities. Keep every inequality except ell>=0 fixed, and replace the root inequality by ell+epsilon h>=0 for an arbitrary fixed affine h. Let P_epsilon be this actual intersection, and ell_epsilon=ell+epsilon h. Both signs of sufficiently small epsilon are admissible: all four canonical values remain positive, all other fixed supporting inequalities still contain T0, boundedness and full dimension persist, and the supporting coordinate wedge is unchanged. Changes at nonsimple root vertices do not affect the usual first-order facet integral. In coordinates normal to F the outward displacement is epsilon h/|grad ell|.

The explicit affine changes are Edot_explicit=V h(g) and Ndot_explicit=3(X+Y)h(w). The latter is the same barycentric identity(2.1) applied to h. The boundary part of Edot is zero because ell=0 on F. Stationarity therefore gives, for EVERY affine h,
0=3(X+Y)h(w)-qVh(g)+integral_F G h/|grad ell|.           (3.1)
For h=1 and the three coordinate functions:
S_F:=integral_F G/|grad ell|=6V^2(T-m),                 (3.2)
integral_F G x/|grad ell|=6V^2(Tg-mw).                 (3.3)
Since G is positive, T>m, and the G-weighted root centroid is exactly R_T. Positivity of the weight on the whole polygon makes this centroid lie in relint F, not merely in its supporting plane.

Taking h=G in(3.1) yields
integral_F G^2/|grad ell|=6V^2 m[r-n(w)]>0.            (3.4)
Indeed G(g)=-r, ell(w)=r/(3p), so the terms qVr cancel exactly. In particular r>n(w) at such an extremum.

Write rho=Area(F)mu/(3V|grad ell|), the actual volume fraction of the pyramid conv(g,F) in P, and denote unweighted area means on F by bars. Equations(3.2)-(3.4) become
rho barG=r(T-m)/(3T),
rho bar(G^2)=r m[r-n(w)]/(3T).
Cauchy-Schwarz consequently gives
rho >= (T-m)^2/[3Tm(1-n(w)/r)].                         (3.5)
The pyramids from g over the two coordinate supporting patches have fractions m_x/3,m_y/3, where m_x=X/(2V^2),m_y=Y/(2V^2). Their interiors and the root pyramid are disjoint; hence rho<=1-m/3 even when the coordinate faces are larger than the patches. Thus(3.5) is a necessary, genuine root/body coupling. It has not been shown to contradict T>=51/25.

This two-sided affine test theorem is NOT asserted when c=0 or d=0. There the feasible root motions interact with canonical boundary points and some tests become one-sided; the earlier repaired root-cut inequality, not(3.1) without qualification, is available.

## 4. Genuine diagonal projective variation and covariance
This theorem needs a joint local maximum under the following actual families, and does not require strictly positive endpoint values. Use canonical barycentric functions lambda_A=1-x-y-z,lambda_B=z,lambda_C=y,lambda_D=x. For real eta_A,...,eta_D set weights w_i=exp(epsilon eta_i), f_epsilon=sum_i w_i lambda_i, D_epsilon=product_i w_i. Define
Phi_epsilon(x,y,z)=(w_D x,w_C y,w_B z)/f_epsilon.
For both signs of sufficiently small epsilon the denominator is positive on bounded P, the projectivity fixes all four canonical points, preserves the supporting coordinate wedge and convexity, and maps true facets to true facets. The new body Phi_epsilon(P) is filled UNIFORMLY. Its density is NOT the push-forward of the old uniform density. Its Jacobian is D_epsilon/f_epsilon^4.

Set ell'_epsilon(Phi_epsilon(x))=ell(x)/f_epsilon(x). This is affine in the new coordinates, with endpoint values a/w_A,b/w_B,c/w_C,d/w_D, so it remains nonnegative and its actual root is the image of the old root. Zeros stay zeros. Define phi=sum eta_i lambda_i, eta_sum=sum eta_i, and
K=[eta_D(s+c)-eta_A a-eta_B b-eta_C c]x
 +[eta_C(s+d)-eta_A a-eta_B b-eta_D d]y.
Direct differentiation of actual pullback integrals gives
Vdot=eta_sum V-4 integral_P phi,
Edot=eta_sum E-5 integral_P ell phi,
Ndot=eta_sum N+integral_P K-5 integral_P n phi.
The exponents4 and5 are essential. Refilling and merely pushing forward a density are different problems.

At a joint maximum, Ndot-r Vdot-q Edot=0 for all eta. Substitution and G=n-r-qell give
5 integral_P G phi=integral_P K-N[eta_sum+phi(g)].      (4.1)
Let Sigma=Cov_uniform(P). Since integral G phi/V=-r phi(g)+Cov(G,phi), taking phi=x,y,z gives
5 Sigma beta = (4ru-(s+2d)v,
                4rv-(s+2c)u,
                4rz-r-bp).                            (4.2)
No arbitrary covariance or independent volume weights are being inserted in this theorem: Sigma is the actual body's covariance. Its three scalar equations are necessary; they may aggregate other facet stationarity conditions and are not claimed to be independent of every existing variational identity.

Taking the scalar product with beta, write R=5 beta^T Sigma beta. Under the essential equality qmu=r, exact algebra yields
R=2q[(a^2+ab+b^2)p+s c u+s d v+c^2u+d^2v]
  -[s^2p+s(2cu+cv+du+2dv)+2cdp].                     (4.3)
In particular R>0. The determinant/body containment also forces a useful lower covariance bound. Uniform T0 has mean g0=(1/4,1/4,1/4) and Sigma0=(4I-11^T)/80. Its weight in the uniform P is1/t. For t>1, apply the law of total covariance to T0 and the actual measurable remainder P\T0; dropping only the positive remainder covariance gives
Sigma >= Sigma_min:=Sigma0/t+(g-g0)(g-g0)^T/(t-1).       (4.4)
Consequently
R/5 >= Var_T0(beta.x)/t+[beta.(g-g0)]^2/(t-1),
Var_T0(beta.x)=[|beta|^2-(sum beta)^2/4]/20,
beta.(g-g0)=[q(a+b+c+d)-(2s+c+d)]/4.                  (4.5)
At t=1 the body is T0 and is handled directly; do not divide by t-1. Equations(4.2)-(4.5) alone do not prove the desired trace bound.

## 5. Exact second-order test at a maximal-G root edge
Assume the accepted ordinary-facet structure at a fixed-ell local maximum: an ordinary facet is the actual triangle Xvw with X canonical, G(X)=-3L and G(v)=G(w)=L>0. Suppose v,w lie on the actual root F, ell(X)=h_X>0, and the root edge vw is a maximum edge of the nonconstant affine G restricted to F. Thus G decreases into F from this edge and its tangential gradient is nonzero.

Choose a point in the relative interior of vw, move it a small distance outward in the root plane perpendicular to vw, and call the new point p_delta, normalized so G(p_delta)=L+delta. For sufficiently small delta>0, the only facet visible from p_delta is Xvw: the point stays in the root plane, away from the other root-edge endpoints, and on the inner side of all other incident supporting planes. The enlarged convex hull therefore adds exactly the tetrahedron Xvwp_delta. This is a genuine admissible change, not an abstract independent volume increment.

Its volume is
W=h_X length(vw) delta/[6 |grad ell| |grad_F G|].        (5.1)
The affine averages over this tetrahedron are barG=delta/4 and barell=h_X/4. The exact fixed-ell comparison from section1 becomes
W delta/4 > (q/V) W^2 h_X/4,
so improvement occurs iff delta>q h_X W/V. Therefore a local maximum with such a root edge must satisfy
6V |grad ell| |grad_F G| <= q h_X^2 length(vw).          (5.2)
This is genuinely second-order because the first-order averaged G at the edge is zero. It has only been proved for a maximal-G root edge with the stated unique visible ordinary facet. A minimal-G edge or a nonroot special face cannot be silently substituted. The inequality has not been turned into an all-auxiliary reduction or a trace-value exclusion.

## 6. Exact formal moment countercontrol: covariance constraints are insufficient
Take
(a,b,c,d)=(1,1/2,2/5,2/5), t=5, V=5/6,
g=(3/4,3/4,-7/22), T=11/5.
Then p=3/2,m=9/10,mu=57/220,r=57/20,q=11,
beta=(17/2,17/2,11/2),R=3051/40.
All the following necessary scalar conditions hold:
u,v>=1/4;4u,4v<=t;4(u+v)=t+1;
0<a,b,c,d<=4mu;
4tmu>=ct+s+d and4tmu>=dt+s+c;
min(a,b)>=4mu(T-2);T<=1+s/(4mu);
t<45/7,m>13/15.
The gauge candidate is R_T=(15/13,15/13,-10/13), and ell(R_T)=0. This last equality is algebraic and does not assert membership in an actual body.

For these values,
Sigma_min=[[7/100,3/50,-647/8800],
           [3/50,7/100,-647/8800],
           [-647/8800,-647/8800,17077/193600]].
Let target denote the right side of(4.2) divided by5. Then
y=target-Sigma_min beta=(1063/1600,1063/1600,-23961/35200),
delta=beta.y=48323/6400>0.
Set Sigma_formal=Sigma_min+yy^T/delta. It is positive definite, dominates Sigma_min and satisfies the FULL vector equation(4.2), not just its scalar projection. Explicitly
Sigma_formal=[[2483013/19329200,2289721/19329200,-14183881/106310600],
              [2289721/19329200,2483013/19329200,-14183881/106310600],
              [-14183881/106310600,-14183881/106310600,87458837/584708300]].
Its leading principal minors are2483013/19329200,2386367/966460000,77875983/5847083000000, all positive. Var_T0(beta.x)=771/320 and beta.(g-g0)=43/8.

These data CANNOT be realized by an eligible actual P and nonnegative ell. Indeed 4p=t+1 saturates the accepted actual joint-mass inequality. The fully classified equality bodies are P=conv(A,B,C,D,R0), where R0=(r0,s0,z0),r0+s0=t,1-t<=z0<=0 and
 g_x=(r0*t+s0)/(4t), g_y=(s0*t+r0)/(4t), g_z=(1+z0)/4.
For our data these formulas force R0=(5/2,5/2,-25/11). But ell(R0)=-19/22<0. Hence the simultaneous scalar first-moment and projective covariance relaxation admits trace11/5 even though no actual root/body pair has these values. This is a proved limitation of those listed constraints, not a counterexample to T<51/25 and not a claim that it passes every other inherited moment/trace constraint.

## 7. Preserved failed shortcuts and next mathematical question
The fixed-body radial criterion is exact but the universal body inclusion remains unproved. Root-plane stationarity supplies a genuine positive weighted root centroid in the positive-endpoint stratum; that fact by itself is compatible with formal scalar bounds. Positive semidefinite covariance plus the forced tetrahedral mixture and diagonal-projective stationarity remain incomplete, as section6 proves. A stronger proof must exploit actual facet/root shape coupling or additional exact moment realizability, not replace those by independent positive masses.

A separately derived elementary canonical support test may be useful without being a value theorem. Holding the actual body and ell fixed, move the marked C to C'=(0,y,z) in P's x=0 supporting face and affinely renormalize A,B,C',D. The transformed trace numerator, in the old coordinates and common denominator6VE, is y[s+ell(C')]X+(s+d)Y. Its directional derivative at C=(0,1,0) therefore gives
(b+2c)(y-1)+(b-a)z<=0
for every C' in that face at a marked joint maximum. Similarly(b+2d)(x-1)+(b-a)z<=0 on the y=0 face. For a>b these yield, at root points on the coordinate axes, y<=(s+2c)/(s+c) and x<=(s+2d)/(s+d). They show C,D cannot be interior points of the full coordinate supporting faces, but do not rule out their being redundant edge points: the second variation along the stationary support line has the negative sign -2(s+c)(dy)^2, respectively -2(s+d)(dx)^2. One must not assume two special faces containing CD sit on opposite sides of CD; both may provide lower supports. Such an assumption would falsely force x+y<=1. No use of that shortcut is made above.

The next useful frontier is to combine the exact R_T-in-root condition and true facet/edge geometry in the globally localized <=16-vertex class, or turn the second-order maximal-root-edge test into a real value bound. Interior joint root-plane identities should not be assigned to a zero-endpoint boundary without redoing its admissibility. The currently separate one-zero-endpoint and nonaxial root-only branches address different remaining freedoms.

## 8. Complete reconstruction and evidence levels
The exact runnable source is the ENTIRE immutable material [internal-source-reference], named ROOT_DUALITY_JOINT_VARIATIONS_V1 complete root_duality_variation_audit.py.txt. Save its literal UTF-8 bytes as root_duality_variation_audit.py, with no wrapper or newline transformation. It is4726bytes,SHA2568d8876dc6f157ba690be1e5dce79a88c378d6f835bbdaac4bddb06e2e59a1ef8. No external data, helper files, random seed or nondefault optimization parameters are needed. Observed environment CPython3.13.5,SymPy1.14.0. Assertions must be enabled.

Reconstruction/verification command:
python root_duality_variation_audit.py > root_duality_variation_audit.out
sha256sum root_duality_variation_audit.py root_duality_variation_audit.out

The exact output is494bytes,SHA2565145e066a95435be92607e2974c5a42931336a27cd6cedaac5cfc479d9f6f517, with these complete lines:
FIXED_BODY_ROOT_DUALITY_ALGEBRA_PASS
ROOT_PLANE_FIRST_AND_SECOND_G_MOMENTS_PASS
DIAGONAL_PROJECTIVE_COVARIANCE_IDENTITIES_PASS
FORMAL_COVARIANCE_CONTROL_PASS_NOT_AN_ACTUAL_BODY_ROOT_PAIR
formal_covariance= [[2483013/19329200, 2289721/19329200, -14183881/106310600], [2289721/19329200, 2483013/19329200, -14183881/106310600], [-14183881/106310600, -14183881/106310600, 87458837/584708300]]
covariance_gap= 48323/6400
forced_equality_vertex_ell= -19/22
ROOT_DUALITY_JOINT_VARIATIONS_ALGEBRA_PASS

The source exactly checks the displayed algebraic duality, root first/second-G moment identities, projective coefficient identities and rational formal covariance control. The polar separation, shape derivative admissibility, local-maximum premises, geometric covariance decomposition and spike geometry are analytic proofs in this document, not formally computer-verified. The equality-body classification is an explicitly inherited theorem. This recovery capsule preserves a reusable method and a nonattaining negative control; it does not promote a new canonical attaining polytope.
