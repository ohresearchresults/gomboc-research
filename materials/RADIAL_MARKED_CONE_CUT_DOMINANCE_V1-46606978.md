# material-4660697874d9

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# RADIAL_MARKED_CONE_CUT_DOMINANCE_V1

## Status and significance

New coordinator analytic result. This is a proof for the auxiliary actual-volume pair trace, not a mechanical construction and not an improvement of 34 <= C_min <= 622. It removes negative-z material from an arbitrary convex body at trace above 2 by a strict, finite, actual-moment improvement. No polyhedrality, stationarity, fixed facet lattice, or positive c,d assumption is used. A second marked-point cut gives a global endpoint-asymmetry theorem, strengthening an earlier necessary condition for polytopal local maxima.

The proof below is complete given the explicitly stated previously proved joint-moment input J. That input is preserved in material [internal-source-reference], SHA-256 2c460625df162099bfba6437818bd8eff154d6d2f17d3f21e9ac2e4211c4d18e, name JOINT_MASS_EQUALITY_AND_E17_NO_UNIFORM_GAP_V1 complete equality classification compactness theorem and exact recovery.md. The present coordinator read its complete 25358-character text. Its equality classification is needed only for the strict boundary case in the B-cut theorem, not for the A-cut theorem.

Relevant earlier but not logically necessary source: [internal-source-reference], SHA-256 3d8b947f80c16dced9a1fbcc48a4c7f5f92159a58e91cac8f365441d4b20ba3d, FULL_PATCH_A_STAR_FLATTENING_V1.md. That source proves a local-maximal polytope A-star flattening; the present result is a nonstationary convex-body value comparison. Its introductory source hashes for J and high-trace attainment should not be reused: the actual J hash is the one above, and the actual high-trace-attainment material [internal-source-reference] has SHA-256 52786c239b2ed0a438f276cb7c2baa108b5617168f5398a25da747e2b7515379.

## 1. Actual-body conventions

Let A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0), and T0=conv(A,B,C,D). Let P be any bounded full-dimensional convex body containing T0, with P contained in {x>=0,y>=0,ell>=0}. The coordinate-plane facets may be larger than the fixed triangles ABC and ABD. Set

ell(x,y,z)=a+(d-a)x+(c-a)y-(a-b)z,

a>=b>0, c>=0, d>=0,

s=a+b, h_c=s+c, h_d=s+d, n(x,y,z)=h_c*x+h_d*y.

Thus ell(A)=a, ell(B)=b, ell(C)=c, ell(D)=d, n(C)=h_d and n(D)=h_c. All integrals are with uniform volume density on the displayed actual body:

V=int_P 1, t=6V, E=int_P ell, mu=E/V, N=int_P n,
r=N/V, T=N/(6VE)=r/(t*mu), q=N/E=t*T.

The reference tetrahedron has volume 1/6, so t>=1. E,N,T are positive. Define the affine first-variation density

G(p)=n(p)-r-q*ell(p).

It depends on the current actual body. Whenever the body changes, V,E,N,r,q,G and its centroid are recomputed from that body. No prescribed or inherited centroid is held fixed.

## 2. Joint-moment input J and a direct cone inequality

The previously proved input J, valid for every such P independently of ell, is

4*g_x <= t, 4*g_y <= t, 4*(g_x+g_y) <= t+1,

where g is the volume centroid. Equality in the last inequality implies T<=2 for every affine ell nonnegative on P with the stated marked values. Consequently that last inequality is strict when T>2. The cited J source supplies its full convex-body proof and equality classification; this is not a polytopal-only input.

For completeness the other required inequality has the following direct proof for convex bodies:

(CONE)  n(p)+t*ell(p) <= 4*t*mu, for every p in P.

Indeed, the divergence theorem for the vector field (x-p)*ell(x) gives

4E-V*ell(p)=int_boundary(P) ell(x)*(x-p).nu(x) dA(x).

Every integrand is nonnegative because ell>=0 and p belongs to P. On the boundary triangle ABC in the plane x=0, the contribution is p_x*(a+b+c)/6=p_x*h_c/6. On ABD it is p_y*h_d/6. These two surface patches overlap only in a set of area zero. Dropping all remaining nonnegative contributions and multiplying by 6 proves CONE. The identity holds for any p in P, including its boundary, by continuity. It does not require a polyhedral boundary.

At p=g, CONE yields T<=3. It is not necessary below to prove strictness of this bound.

Interchange (C,y,c) with (D,x,d) if necessary, so c>=d and h_c>=h_d. Then J gives

4r=(h_c-h_d)*4g_x+h_d*4(g_x+g_y) <= h_c*t+h_d.

CONE at C gives 4t*mu>=t*c+h_d. Combining these inequalities yields

(DMU) D_mu:=s-4*(T-1)*mu >=0.

If T>2, D_mu>0: h_d>0 makes the joint-moment contribution strictly smaller, regardless of whether c=d. The conclusions are symmetric in c,d, so DMU holds without the temporary ordering assumption.

CONE at an arbitrary p also gives the pointwise estimate

(GMAX) G(p) <= t*(4-T)*mu-t*(T+1)*ell(p) <= t*(4-T)*mu.

Put M_G=t*(4-T)*mu. We use M_G as a valid upper bound, not as an assertion that a maximizer of G actually attains it.

## 3. Exact radial-removal lemma

Let X belong to a convex body K, let G be affine on K, and suppose

G(X)=-3L and G(p)<=L-delta for all p in K,

with delta>0. Let H be any closed halfspace whose boundary passes through X. Write R=K\H and W=Vol(R). Then

(RADIAL) int_R G <= -(3/4)*delta*W.

Proof. In polar coordinates about X, a ray meeting R consists, up to endpoints, of the entire interval 0<rho<rho_K(u). This is because K is convex and contains X, while the defining affine function of H vanishes at X and has constant sign along each ray. If Y=X+rho_K(u)*u is the terminal point, then

int_0^rho_K(u) G(X+rho*u)*rho^2 d rho
= rho_K(u)^3 * [G(X)+3G(Y)]/12
<= -delta*rho_K(u)^3/4.

Integrating over the removed directions and using W=int rho_K(u)^3/3 proves the claim. This argument applies whether X is a vertex, lies in a larger face, or is a nonsmooth/nonpolyhedral boundary point. Zero-length directions and boundary rays do not affect volume integrals.

Now take K=P, with its actual trace quantities from section 1, and Q=P intersect H. Let E_R=int_R ell and N_R=int_R n. Because Q contains T0 in all applications below, its V-W and E-E_R are positive. Direct algebra gives the exact, not first-order, identity

(EXACT) T(Q)-T(P)
= [-int_R G-6*T(P)*W*E_R] / [6*(V-W)*(E-E_R)].

Therefore, if W>0 and E_R<delta/[8*T(P)], RADIAL implies T(Q)>T(P). If W=0, the two traces agree. In particular, arbitrarily small positive-volume removed radial wedges give strict ascent. This accounts for the full volume and affine-height normalization change; it is not a frozen-centroid or linearized calculation.

## 4. Uniform A-point gap

At A, G(A)=-t*T*(mu+a). Define L_A=t*T*(mu+a)/3. For T>1, elementary algebra gives

3*(T-1)*(L_A-M_G)
=t*[Psi_A(T)+(3-T)*D_mu],

where Psi_A(T)=a*T^2+b*T-3*(a+b).

For T>=2,

Psi_A(T)-(a-b)*(T-1)=(T-2)*[a*(T+1)+2b]>=0.

Since T<=3 and D_mu>=0, if a>b and T>=2 then

L_A-M_G >= delta_A:=t*(a-b)/3>0.

If a=b and T>2, the same identity gives

L_A-M_G >= delta_A:=t*a*(T-2)*(T+3)/[3*(T-1)]>0.

In both cases G(A)=-3L_A and G<=L_A-delta_A, so the exact radial-removal lemma applies to every sufficiently small admissible halfspace cut through A.

## 5. Global A-cut value dominance, including zero endpoints and nonpolyhedral bodies

Define

P_theta=P intersect {(1-theta)*(x+y)+theta*z>=0}, 0<=theta<=1.

These are nested decreasing convex bodies, all containing T0. P_0=P and P_1=P intersect {z>=0}. Points with z>=0 are retained throughout. For a point with z<0 and x+y>=0, retention is equivalent to theta <= (x+y)/(x+y-z), proving nesting. The exceptional negative vertical axis at theta=0 has volume zero. Dominated convergence therefore proves continuity of all three moment integrals V(theta),E(theta),N(theta), including at both endpoints. T(theta) is continuous because each body contains T0.

Suppose first that a>b and T(P)>=2. On every intermediate body whose trace is at least 2,

delta_A/[8T] >= (a-b)/72,

because t>=1 and T<=3. Choose a finite partition of [0,1] fine enough that each E decrement is strictly smaller than (a-b)/72; this is possible by uniform continuity of E(theta). At each step, the newly imposed halfspace passes through A, and its removed region is a radial set inside the current P_theta. By induction using EXACT, each nonzero-volume step strictly increases T; zero-volume steps leave it unchanged. Thus every intermediate partition trace stays at least T(P), making the gap bound valid at the next step.

If a=b and T(P)=T_start>2, use that f(T)=(T-2)*(T+3)/(T-1)=T+2-4/(T-1) is increasing for T>1. On all intermediate traces at least T_start,

delta_A/[8T] >= a*f(T_start)/72>0.

The same finite-partition argument works.

A point of P with z<0 forces a positive removed volume: mixing it with a small interior ball of T0 yields a small open subset of P with negative z. Hence the total improvement is strict when P has any negative-z point and either a>b,T(P)>=2 or a=b,T(P)>2.

We have proved the universal statement

(A-CUT) T(P) <= max{2, T(P intersect {z>=0})}.

The asserted strict version is as above. The cut may alter the face lattice, add new positive-ell vertices at z=0, and move the actual centroid. None of these changes is prohibited in this auxiliary value problem.

## 6. Global B-endpoint obstruction

Define

Psi_B(T)=b*T^2+a*T-3*(a+b), L_B=t*T*(mu+b)/3.

The exact reflected algebra is

3*(T-1)*(L_B-M_G)
=t*[Psi_B(T)+(3-T)*D_mu].

Claim: every actual body in section 1 with T>2 satisfies

(B-OBSTRUCTION) Psi_B(T)<0.

Proof by contradiction. Suppose T(P)>2 and Psi_B(T(P))>=0. Apply A-CUT first, replacing P by K=P intersect {z>=0}; its trace is no smaller. Since Psi_B is strictly increasing for T>0, it is still nonnegative at T(K).

Now use the nested B-centered cut family

K_theta=K intersect {(1-theta)*(x+y)+theta*(1-x-y-z)>=0}, 0<=theta<=1.

All planes pass through B and retain A,C,D. Nesting and moment continuity follow exactly as for A-CUT, with u=x+y>=0 and v=1-x-y-z. The final body is exactly T0, since K already lies in x,y,z>=0. The tetrahedron's trace is

T(T0)=[2a+2b+c+d]/[a+b+c+d] <=2.

Consequently K is not already contained in the final halfspace: otherwise K=T0 would contradict T(K)>2.

If Psi_B(T(K))>0, a uniform positive B-gap is available for every intermediate trace T>=T(K):

L_B-M_G >= Psi_B(T(K))/6,

because t>=1, 1<T<=3, D_mu>=0, and Psi_B is increasing. Thus delta/[8T] >= Psi_B(T(K))/144. A finite E-small partition, as in section 5, forces the trace to increase or remain constant all the way to T0. This contradicts T(T0)<=2<T(K).

It remains to handle Psi_B(T(K))=0. Here T(K)<3, since Psi_B(3)=6b>0. Also D_mu>0 by the strict J input when T>2. Hence the displayed B-gap identity gives L_B-M_G>0 at K. Because the final cut removes a positive volume and the nested family has continuous E, one can choose a first genuinely nonzero B-cut with arbitrarily small E removal, even if the family leaves K unchanged up to a positive onset parameter. The exact radial lemma makes this first cut strictly increase T. Psi_B is then strictly positive. The preceding uniform-gap argument applies to the remainder of the family and again contradicts the final tetrahedral trace. This proves B-OBSTRUCTION.

No strict T<3 theorem was needed: the only case requiring 3-T>0 was Psi_B=0, and Psi_B(3)>0 supplies it directly.

## 7. Endpoint consequences

If a=b, then Psi_B(T)=a*(T-2)*(T+3)>0 for T>2, contradicting B-OBSTRUCTION. Therefore

(BALANCED) a=b implies T(P)<=2 for every actual body in the enlarged class, including c=0 and/or d=0 and arbitrary nonpolyhedral boundaries.

The value 2 is attained in this auxiliary class by P=T0, a=b>0, c=d=0. This is not a mechanical class110 example.

If a>b, let

Theta_B=[-a+sqrt(a^2+12b(a+b))]/(2b).

Since Psi_B(2)=b-a<0 and Psi_B(3)=6b>0, one has 2<Theta_B<3. B-OBSTRUCTION, together with the trivial case T<=2, proves the global strict bound T(P)<Theta_B.

For every T(P)>2,

b/a < (3-T)/(T^2-3).

The right-hand side decreases on [2,3], as its derivative has numerator T^2-6T+3<0. In particular,

T(P)>=51/25 implies a>b and b/a<100/121.

Combining this strict ratio with s>=4*(T-1)*mu yields, on the same high-trace stratum,

a-b > (2184/5525)*mu,
a > (12584/5525)*mu.

These are global actual-body endpoint restrictions, not just stationary or root-only restrictions. The numerical constants are exact rational consequences of T>=51/25, not sampled estimates.

## 8. Scope, dependencies, and remaining frontier

1. A-CUT is an actual-body trace comparison. The clipped body P intersect {z>=0} need not equal a previously named root-only parent P0. In a negative-root extension, clipping may create extra positive-ell vertices at z=0. Thus this theorem does NOT claim T(P)<=max{2,T(the original root-only parent)}. Such parent comparisons retain their separate geometric hypotheses.
2. A-CUT is not the false projection-prism monotonicity statement for cutting by x+y<=1. Known countercontrols to that different cut remain valid.
3. A-CUT eliminates negative z for the full convex-body value supremum, including zero endpoints, without first proving existence or polyhedrality of a high-trace maximizer. It does NOT prove the remaining zero-endpoint octant value bound or a zero-endpoint polyhedral-maximizer theorem.
4. The earlier A-star source applies to polytopal local maxima, including zero c,d. High-trace attainment [internal-source-reference] only promotes all-positive a!=b,c,d>0 maximizers to <=16-vertex polytopes. The present theorem bypasses that gap for negative-z elimination only; it does not silently extend the old polyhedral theorem.
5. The full all-positive octant, exactly-one-expanded-coordinate-facet, both-G_C,G_D-nonpositive stationary sector and the nonpolyhedral/zero-endpoint octant sector remain distinct scientific frontiers unless separately closed by exact new results.
6. No computational search or code materially produced this proof. Its exact data are the displayed definitions, rational constants, and complete analytic argument. The only external-to-this-unit logical input is the explicitly identified immutable J source; attach that source along with this unit to a fresh successor that needs the underlying proof.
