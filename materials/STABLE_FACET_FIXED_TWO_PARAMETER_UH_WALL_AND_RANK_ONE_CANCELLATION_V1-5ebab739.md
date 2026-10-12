# material-5ebab73947b0

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Stable-facet-fixed two-parameter U/H wall and rank-one cancellation

## Identity, evidence and scope
STABLE_FACET_FIXED_TWO_PARAMETER_UH_WALL_AND_RANK_ONE_CANCELLATION_V1.
This is a new coordinator analytical derivation, prompted by the completely read immutable result minimum-0289, SHA256 34d98fdf4c645c0d704314609e30ba0213e34d9c7a1ec981a360eadaab1e6217. Its exact C592=(164,296,134),own121physicalweak000 has u=X150, v=X153 and stable facet q=raw3, opposite incident facet r=raw135. No C592 numerical or exact evaluation of the new family is claimed here. The old rank-two metric pencil is already completely classified and has no110; the families below are different. No new attaining body or global lower bound follows from this note.

All statements below are proved algebraically and geometrically, not by a reported numerical run. They use an actual full-dimensional convex polytope P centred at its own uniform volume centroid, one positive-definite physical metric M0, and N0=M0^{-1}. Varying the metric is equivalent to an invertible linear image of the uniformly filled body, so the actual centroid remains zero. True maximal facets and true edges, never integration diagonals, are used throughout. The derivation in fact applies to any fixed interior mass point, but the intended application uses the actual uniform centroid.

## 1. Hypotheses and an adapted basis
Let u be a strict unstable vertex and [u,v] a strict saddle edge for M0. Put e=v-u. Let q.x=1 and r.x=1 be its two normalized incident support planes. Assume q is a strict stable facet. Its actual metric foot is

Q=q^T N0 q>0,     p=N0 q/Q.

Thus p lies in the relative interior of the actual polygon q.x=1. Put w=u-p. Both w and e lie in ker(q^T). They are linearly independent: otherwise p would lie on the supporting line of the polygon edge [u,v], contrary to strict stability. Hence the frame

F=[p,e,w]

is invertible. In this frame u=(1,0,1), v=(1,1,1), q=(1,0,0) as a covector. Write

r=(a,0,b),     a=r.p,     b=r.w=1-a.

Strict stability of q implies q^T N0(r-q)=Q(a-1)<0, hence b>0. Define

L=e^T M0 e>0, D=w^T M0 e=u^T M0 e<0, W=w^T M0 w>0,
Delta=L W-D^2>0.

Since M0 p=q/Q, the metric matrix in F is

G0=F^T M0 F = [[1/Q,0,0],[0,L,D],[0,D,W]].

The saddle also has D+L>0 and both incident dual primitives negative. These strict inequalities are hypotheses, not conclusions inferred from a graph drawing.

## 2. COMPLETE wall chart preserving the stable foot
Up to positive overall metric scale, every SPD metric preserving the same stable-facet foot p can be normalized by Nq=N0q=Qp. Equivalently Mp=q/Q. Consequently its matrix in F has first row/column (1/Q,0,0), with an arbitrary SPD two-by-two tangent block.

The desired source VE wall is u^T M e=0. In this frame it is exactly the vanishing of the tangent off-diagonal entry. Therefore ALL such wall metrics, modulo positive scale, are exactly

G(A,B)=diag(1/Q,A,B),       A>0, B>0,
M(A,B)=F^{-T}G(A,B)F^{-1},
N(A,B)=F diag(Q,1/A,1/B)F^T.

This is a complete TWO-parameter wall chart, not merely a convenient pencil. The foot p is unchanged and q remains strictly stable for every A,B>0, because every outgoing q-source dual primitive has its original value Q p.(s-q).

The two target-edge dual primitives are

E_qr=-Qb<0,
E_rq=Qab-b^2/B.

The target wall lies strictly inside the actual edge-normal cone exactly on the domain

A>0, 0<B<Bmax,
Bmax=+infinity if a<=0, and Bmax=b/(Qa) if a>0.

Indeed M u=(1/Q-aB/b)q+(B/b)r. Both coefficients are positive precisely on that domain. Thus this normal exposes exactly the true edge [u,v]. Every other outgoing true edge from u has strictly negative primal primitive, while the reverse target primitive is -A<0. The only target contact is the genuine VE packet [0,-,-,-], not a VF or a zero-length edge. No assertion about the other vertices/facets is being silently made.

## 3. Local cancellation, with the stable foot fixed EXACTLY
At any interior point (A,B) of that domain use

G_epsilon=[[1/Q,0,0],[0,A,epsilon],[0,epsilon,B]].

It is SPD for |epsilon|<sqrt(A B), and still has N_epsilon q=Qp. The target source primitive is epsilon, its reverse is -A-epsilon. The q-source dual primitive stays -Qb; the r-source dual primitive equals

Qab-b^2 A/(A B-epsilon^2),

which is no larger than its strictly negative wall value. All other outgoing edges at u remain strictly negative for sufficiently small |epsilon| by the exposed-edge margin. Hence epsilon<0 gives the original local U/H pair and epsilon>0 removes BOTH designated objects. This is a genuine local annihilation, not unstable-root migration.

If a wall metric has strict(S,U,H)=(1,1,0), with the target VE as its only physical weak equilibrium, then sufficiently small positive epsilon produces proper110physicalweak000 with EXACTLY the same true(V,E,F). Strict or excluding signs for every other physical feature persist. Unchosen primitive zeros are allowed when their packets have a strict positive exclusion; they must not be counted as physical weak equilibria.

For rational input P,M0, any rational A,B in a successful open wall region and a sufficiently small rational positive epsilon give a rational SPD metric and a reproducible homogeneous construction. An exact rational factorization M=Bphys^T Bphys is not necessary to specify the physical ellipsoid; an algebraic positive square root always defines the Euclidean image. A rational Gram factor can instead be used if independently provided. No such successful A,B is asserted for C592 here.

## 4. Primitive equations on the wall and a finite exact search landscape
Let z_i=F^{-1}x_i be actual centred vertex coordinates. For a true arrow i->j, d=z_j-z_i,

VE_ij(A,B)=z_i0*d0/Q + A*z_i1*d1 + B*z_i2*d2.

Thus each primal wall is a LINE in the (A,B) plane. For a normalized facet pole h let pi_h=F^T h. For a true dual arrow h->k put eta=pi_k-pi_h. Then

EF_hk(A,B)=Q*pi_h0*eta0 + pi_h1*eta1/A + pi_h2*eta2/B.

After multiplying by A B>0 its sign is the sign of

H_hk(A,B)=Q*pi_h0*eta0*A B + pi_h1*eta1*B + pi_h2*eta2*A.

Thus every dual wall is an axis-aligned rectangular hyperbola, a line, an identically zero polynomial, or an empty locus. There is NO constant term in H. Two distinct nonproportional such bilinear curves have at most one intersection in A,B>0: eliminate AB to get a line through the origin, substitute, and discard the origin. Degenerate linear/coincident cases must be handled explicitly. A primal line and a dual curve have at most two intersections unless they share a component.

A vertical exact decomposition therefore uses rational or quadratic event coordinates from line-line, line-hyperbola and hyperbola-hyperbola intersections, plus vertical curves, poles/asymptotes and intersections with B=Bmax when finite. On every remaining two-dimensional cell every nonidentically-zero primitive has constant sign. Sample one point, compute the COMPLETE true-feature census, and use actual weak packets. Identically-zero primitives remain in that census and must not be silently deleted.

The absence of additional physical weak equilibria and the strict/excluding feature conditions are open relative to the desired target wall. Consequently a successful wall with only the targeted weak packet has a neighboring full-dimensional parameter cell with the same physical property, even when an unchosen zero at the original point was harmless. This makes the open-cell search sufficient for this clean-wall criterion. It does not classify all metrics preserving only the stable LABEL rather than its precise foot, nor shape changes. No cell enumeration or C592 count is reported in this analytical note.

## 5. Explicit positive rank-one inverse family preserving the stable facet
There is also a one-direction family with an especially simple path certificate. For every lambda>0 set

v_lambda=w-lambda e,
C_lambda=v_lambda^T M0 v_lambda=W-2 lambda D+lambda^2 L,
T_lambda=-D/(lambda Delta)>0.

For s>=0 define

N_lambda(s)=N0+s T_lambda v_lambda v_lambda^T,
M_lambda(s)=M0-[s T_lambda/(1+s T_lambda C_lambda)]
             M0 v_lambda v_lambda^T M0.

These are one actual inverse pair and remain SPD for all s>=0. Since q.v_lambda=0, N_lambda(s)q=N0q EXACTLY: the stable foot and every outgoing q-source dual primitive are unchanged. Across the target edge the other dual primitive is

E_rq(s)=E_rq(0)-s T_lambda(r.v_lambda)^2<0.

Write A0=u^T M0 v_lambda=W-lambda D, B0=e^T M0 v_lambda=D-lambda L. Direct expansion gives

D C_lambda-A0 B0=lambda Delta>0,
u^T M_lambda(s)e=D(1-s)/(1+s T_lambda C_lambda).

At s=1 the edge-normal coefficients are strictly positive because both target dual primitives remain negative. M_lambda(s) is a convex combination of M0 and M_lambda(1) for 0<=s<=1, with interpolation coefficient

[s T_lambda/(1+s T_lambda C_lambda)] /
[T_lambda/(1+T_lambda C_lambda)].

Hence every other outgoing edge at u and the reverse target arrow stay negative on the entire prefix. The target U and H remain strict until s=1 and disappear locally after1. Other equilibria can still be born elsewhere; preserving the original stable facet does NOT prove S=1 globally.

This lambda family exhausts all positive rank-one additions to N0 annihilating q which reach this source VE wall at a finite positive parameter, up to rescaling the update vector. Indeed ker(q^T)=span(w,e). For v=alpha w+beta e,

D(v^T M0v)-(u^T M0v)(e^T M0v)=-alpha beta Delta.

A crossing requires alpha beta<0, exactly the directions w-lambda e with lambda>0. This exhaustion is restricted to POSITIVE rank-one inverse updates; negative rank-one updates and rank-two changes are not excluded.

At the wall, relative condition number is

kappa_lambda=1+T_lambda C_lambda.

Its minimum over this whole positive rank-one class occurs at lambda=sqrt(W/L) and equals

(sqrt(W L)-D)/(sqrt(W L)+D).

This is a restricted optimum, not the unrestricted sharp condition found in the C592 parent's different rank-two pencil.

## 6. Quadratic critical-wall test for the rank-one subclass
For any actual primal arrow let d_ij=x_i^T M0(x_j-x_i), alpha_i=x_i^T M0v_lambda, beta_ij=(x_j-x_i)^T M0v_lambda. Then

lambda Delta(1+s T_lambda C_lambda) VE_ij(s)
=lambda Delta*d_ij-s D(C_lambda*d_ij-alpha_i beta_ij).

For any actual dual arrow h->k with f_hk=h^T N0(k-h),

lambda Delta*EF_hk(s)
=lambda Delta*f_hk-s D(h.v_lambda)((k-h).v_lambda).

At s=1 both right sides are polynomials of degree at most TWO in lambda; the target primal polynomial is identically zero. Their exact positive roots partition the entire lambda>0 axis into sign-constant cells. Thus the clean targeted-wall criterion for the entire positive rank-one subclass is a univariate quadratic arrangement. Initial nonzero signs and identical critical-wall signs for all untargeted primitives are a sufficient certificate of a birth-free prefix, because each scaled numerator is affine in s. A final successful wall need not have the original unchosen sign pattern; a complete physical census, not that sufficient test alone, is decisive.

## 7. Exact algebraic control and limits
For the uniformly filled cube [-1,1]^3 at its actual centroid, take M0=I, q=(0,0,1), r=(0,1,0), u=(1,1,1), e=(-2,0,0), p=(0,0,1), w=(1,1,0). Then Q=1,L=4,D=-2,W=2,Delta=4. At lambda=1/2, v_lambda=(2,1,0),T_lambda=1. The critical matrices are

N(1)=[[5,2,0],[2,2,0],[0,0,1]],
M(1)=(1/6)[[2,-2,0],[-2,5,0],[0,0,6]],
M(1)u=(0,1/2,1).

They satisfy all stated target and stable-foot identities by direct multiplication. The cube has other equilibria and symmetry-related collisions; this is an algebraic control, NOT an isolated110 endpoint or a new minimum candidate.

The constructive question left for C592 is whether its complete two-parameter wall chart contains a clean target-only weakS1U1 region, or whether genuine shape changes/other stable-foot motions are necessary. The positive rank-one subclass gives a smaller exact decision problem, not a substitute for that full chart or for the original minimum problem. CanonicalC622 and34<=Cmin<=622 are unchanged.
