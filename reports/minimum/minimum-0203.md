# minimum-0203

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# HEX6_INDEPENDENT_COMPLETION_NONAPICAL_MAXIMUM_V2

## 1. Main result and change to the boundary

**A genuine family with five independent cuts and three independently varying base-plane coefficients is now excluded from full U1 at the degree-six apex, for every SPD metric.** The cuts range independently over the entire interval (0,1/10], with no positive lower bound. This is not a metric sweep or another coordinate neighborhood of either previously closed ten-vertex centre.

More precisely, every metric on every actual own-centred body in the family has a **strict unstable vertex other than apex 0**. Consequently, whenever apex 0 is strict U, there are at least two strict U vertices. The proof includes finite weak-arrow boundaries, ties between nonroot radii, and arbitrarily ill-conditioned SPD metrics.

Within the whole subfamily whose five cuts are at most 1/25, the local/apical sharp-five phenomenon persists: on each SAME actual body, every proper four-arrow subsystem has a strict physical witness with apex 0 strictly unstable, while the five-arrow union remains weakly impossible. Nevertheless, the complete rooted-U1 cone is empty throughout this subfamily.

There are two further advances beyond that exclusion. First, I prove a **global vertex-centred projective centring theorem**, replacing the local small-cut centroid repair by a uniquely determined global construction. It supplies prescribed-pole, actual-centred completions throughout the entire open five-cut cube (0,1)^5. Second, I preserve two exact distant completions: one defeats extrapolation of the new highest-nonroot obstruction, and another is bounded even though releasing its two cut facets gives an unbounded virtual pyramid. Both remain in the local apical sharp-five chamber.

No full-U1 witness was obtained. No proper110 construction, whole-incidence exclusion, canonical count change, or change to 34≤C_min≤622 follows. The preceding parent’s two all-SPD centre exclusions remain accepted inputs, rather than new claims here.

## 2. Source identity and actual geometry

The complete new journal, including its literal parent through the actual EOF, and ROOT_CORE_AND_RECIPROCAL_CONVEX_SLICES_V1 were read. The scientific parent is minimum-0200, declared SHA256 a566957d22256c142aa1a484f71dd6c5d46618ad5efc4bf2c1e14798389ceeca. No scientific scope conflict with that literal payload was found.

Actual supplied file pins:

    ROOT_CORE_AND_RECIPROCAL_CONVEX_SLICES_V1.md
    14418 bytes
    SHA256 2ff66026d671b789528ccc6268ba6dcb11d592ec5d425e93a91bb19c240a8583

    research-journal(20260923-071033).md
    283133 bytes
    SHA256 ec9e1f23df83d1f46c2c4ecf1d4d93de74178646d4cf14e545155041f9cf5b85

The starting cone is the parent’s CHANGED degree-six hexagon, not its original integer hexagon and not either degree-five control. Its fixed raw planar poles are

    p = 1/100000 * (
      (60401,-32565),
      (80000,-20000),
      (0,60000),
      (-80000,80000),
      (-483861,-325040),
      (-447814,-355009)).

Put A=(0,0,1), q_i=(p_i,1), and

    s0=(-1743742,-1088172,1000000)/1000000,
    rho=1/1000000,
    |s_k-s0_k|≤rho, k=1,2,3,
    b=-3s.

The six virtual base vertices are the exact three-plane intersections

    B_i=[q_i;q_((i+1) mod 6);b]^-1 (1,1,1).

For five independent cut fractions (x,y,z,u,v), define

    Y0=A,
    Y1=B1, Y2=B2, Y3=B4, Y4=B5,
    Y5=B0+x(A-B0),
    Y6=B0+y(B5-B0),
    Y7=B0+z(B1-B0),
    Y8=B3+u(A-B3),
    Y9=B3+v(B4-B3).

Here x,y,z,u,v denote cut fractions, not the spatial coordinates of a point. The actual body is P=conv(Y0,...,Y9), uniformly filled. Its centroid is recomputed after every change of any cut or base coefficient.

The true outward maximal facets are

    F0=(0,4,6,5), F1=(0,5,7,1), F2=(0,1,2),
    F3=(0,2,8), F4=(0,8,9,3), F5=(0,3,4),
    F6=(4,3,9,2,1,7,6), F7=(5,6,7), F8=(9,8,2).

The true edges are

    01,02,03,04,05,08,12,17,28,29,34,39,46,56,57,67,89.

Thus (V,E,F)=(10,17,9), vertex 0 has degree six, vertex 2 has degree four, and all other vertices have degree three. These are maximal facets and actual edges, not integration triangles or diagonals.

### Why the independent-cut chart is geometrically valid

The parent pyramid is conv(A,B0,B1,B2,B3,B4,B5). The two base ears (B5,B0,B1) and (B2,B3,B4) have disjoint interiors; their complement contains the genuine quadrilateral (B1,B2,B4,B5). The first cut removes the tetrahedron

    conv(B0,Y5,Y6,Y7),

and the second removes

    conv(B3,B2,Y8,Y9).

The second plane passes through the EXISTING vertex B2. It is not a generic second truncation.

This construction is valid for all five fractions in (0,1), not only small equal fractions. In the simple-vertex cone at B0, the three edge coordinates of a point outside its ear have sum at least one. Dividing each by its cut fraction, which is less than one, retains that point strictly. At B3 the retained inequality is alpha+beta/u+gamma/v≥1, with B2=(1,0,0); every other old vertex is strictly retained. The first cut’s new vertices are convex combinations of points strictly retained by the second cut. The two removed tetrahedra therefore remain disjoint, and the stated lattice persists.

The full-domain metric theorem below is restricted to fractions at most 1/10. Fractions zero or one are not called actual ten-vertex members; zero-cut strata are used only as closed polynomial certificate boundaries.

## 3. Coupled actual centroid formulas

Let

    d_i=|det(B0-A,B_i-A,B_(i+1)-A)|, i=1,2,3,4,
    Dp=sum_i d_i,
    Lp=sum_i d_i(A+B0+B_i+B_(i+1)),

    c0=|det(A-B0,B5-B0,B1-B0)|,
    c3=|det(B2-B3,A-B3,B4-B3)|.

The exact moments of the SAME actual body are

    D=6 Vol(P)=Dp-c0*x*y*z-c3*u*v,

    L=24 integral_P Y
      =Lp-c0*x*y*z*((4-x-y-z)B0+xA+yB5+zB1)
          -c3*u*v*((3-u-v)B3+B2+uA+vB4),

    g=L/(4D),   X_i=Y_i-g.

These are genuine removed tetrahedra with their actual volumes and centroids. Their masses are not independent completion variables. The remaining quadrilateral cone gives Dp-c0-c3>0. Over the certified eight-parameter domain the exact interval calculation gives 0<D<6.

For stable exact interval evaluation under base-plane motion, use fixed signed cone generators v_i parallel to q_i×q_(i+1), chosen with b·v_i>0. Then

    B_i=A+r_i v_i,   r_i=(1-b·A)/(b·v_i)>0.

Every determinant above factors into a fixed signed determinant of the v_i and a product of positive r_i. This avoids subtracting nearly coincident base vertices in a small-ear determinant. It is a reusable improvement over direct independent vertex enclosures.

## 4. Highest-nonroot theorem: six cases, no tree enumeration

For an arbitrary SPD M, write n_i=X_i^T M X_i. Choose i maximizing n_i among the nine nonroot vertices.

For every true neighbor j≠0,

    D_ij=(n_j-n_i-|X_j-X_i|_M^2)/2<0.

If i is not adjacent to 0, it is already strict U. If it is adjacent to 0, it belongs to the complete list

    i∈{1,2,3,4,5,8}.

It is therefore enough to prove that, whenever such an i maximizes the nonroot radii, D_i0<0. This reduction comes from actual global norm maximization, not from extending the supplied pointwise Helly statement to varying footpoints.

For j≠0,i define

    B_ij=4D(Y_j Y_j^T-Y_i Y_i^T)
         -L(Y_j-Y_i)^T-(Y_j-Y_i)L^T
        =4D(X_j X_j^T-X_i X_i^T),

    C_i=-sym((4D Y_i-L)(A-Y_i)^T),
    sym(uv^T)=(uv^T+vu^T)/2.

Thus

    B_ij:M=4D(n_j-n_i),
    C_i:M=-4D D_i0.

The following SIX exact integer rows suffice. A pair (j,w) is a weight on B_ij; eta is the weight on C_i.

| i | Nonzero (j,w) pairs | eta | Tensor degrees in (x,y,z,u,v) | Coefficient matrices |
|---|---|---:|---|---:|
| 1 | (3,625098), (8,8019), (9,75683) | 1000000 | (2,2,2,3,3) | 432 |
| 2 | (1,195879), (3,627672), (4,111972) | 1000000 | (2,2,2,2,2) | 243 |
| 3 | (1,1000000), (4,100327) | 725834 | (2,2,2,2,2) | 243 |
| 4 | (2,526829), (9,452356) | 1000000 | (2,2,2,2,3) | 324 |
| 5 | (2,666919), (9,607759) | 1000000 | (3,2,2,2,3) | 432 |
| 8 | (1,718048), (4,432840) | 1000000 | (2,2,2,3,2) | 324 |

Set Q_i=sum_j w_ij B_ij+eta_i C_i. The recovery proves, on the WHOLE closed base-coefficient box and WHOLE closed cut cube [0,1/10]^5,

    Q_i-10000 I is positive definite, for each of the six i.

There are 1998 tensor Bernstein coefficient matrices and 5994 strictly positive exact interval leading-minor guards. The base variables are enclosed by rational intervals before the cut-polynomial transformation; the interval bounds cover all simultaneous base changes, not independent fictitious realizations. All 36 central power arrays are reconstructed exactly from their Bernstein arrays. No cell is pruned as allegedly infeasible, no cut ratio is bounded away from zero, and no metric is sampled in this proof.

At a highest nonroot i, contraction with M gives

    10000 tr M < Q_i:M
       =4D sum_j w_ij(n_j-n_i)-4D eta_i D_i0
       ≤-4D eta_i D_i0.

Because D<6 and eta_i≤1000000,

    D_i0 < -tr(M)/2400.

Hence the highest nonroot vertex has every true outgoing primitive strictly negative. This proves:

**Independent-completion theorem.** Throughout the stated eight-parameter actual family, every SPD M has a nonapical strict U. In particular, apex 0 cannot be the unique strict U. The conclusion permits arbitrary other weak contacts and has no S1, H0, selected-tree, reciprocal-root-fan, or conditioning premise.

The exclusion is invariant under simultaneous affine transport of body and metric. The displayed numerical gap uses the literal coordinate frame above.

## 5. Root eligibility is satisfied throughout this excluded family

The supplied core criterion makes unique-global-radius eligibility necessary, but not sufficient, for U1. The present family gives a continuous, explicit actual-geometric separation between those properties.

Use the raw covector ell(Y)=-b·Y and put alpha=ell(A)=-b·A. On the parent base ell=-1, and the actual parent-pyramid mean is

    mu_parent=(alpha-3)/4.

The removed volume fraction is less than 1/100: xyz≤1/1000, uv≤1/100, and the two disjoint ear volumes sum to less than the parent volume. Since the removed mean lies between -1 and alpha, the actual retained mean mu=ell(g) satisfies

    -1/20<mu<1/20.

All nonroot vertices have raw ell between -1 and -1+(alpha+1)/10, which is negative. The exact base enclosure also gives |Y_i|<3 and hence |X_i|<6.

The SINGLE explicit formula

    M_b=b b^T+I/10,   N_b=M_b^-1

therefore makes apex 0 uniquely globally farthest on every body in the entire family. Indeed,

    n_0-n_i > (29/10)^2-(21/20)^2-36/10
              =1483/400,  i≠0.

Thus all these bodies pass the metric-free root-core test, and each has an explicit physical metric making 0 uniquely globally farthest. Yet every metric with apex U has another strict U. The obstruction is genuinely outside root eligibility and radial dominance.

## 6. The whole four-percent subfamily retains apical sharp-five

For every body above with

    0<x,y,z,u,v≤1/25,

let h=1-g_z, t=g_xy/h. Exact coupled moment enclosures place t strictly inside

    -1/10000≤t_x≤1/1000,
    -1/1000≤t_y≤1/10000.

Set

    phat_i=p_i/(1-p_i·t),
    Lg=(1/h)*[[1,0,0],[0,1,0],[t_x,t_y,1]].

The actual side poles are Lg(phat_i,1), and the actual apex chart has A=e3. This uses the new actual centroid after each completion motion.

For omitted arrow r, use

    H_r=[[a_r,b_r],[b_r,100000-a_r]]/100000,
    f_r=(u_r,v_r)/100000,

with the complete rows

| r | a_r | b_r | u_r | v_r |
|---|---:|---:|---:|---:|
| 0 | 35160 | 36716 | 69799 | -23125 |
| 1 | 38769 | -30216 | 490 | 58684 |
| 2 | 40711 | 48169 | -78055 | 78750 |
| 3 | 19798 | -19530 | -125873 | -136772 |
| 4 | 42456 | 33756 | 55139 | -32565 |

Each H_r is SPD. For every delta>0 define

    Nchart=[[H,-Hf],[-f^T H,delta+f^T Hf]],
    Mchart=Nchart^-1,
    Nactual=Lg^-T Nchart Lg^-1,
    Mactual=Lg Mchart Lg^T.

Exact multiplication verifies the reciprocal pair. On the entire closed t-rectangle, f_r is strictly inside the whole phat hexagon and

    (phat_i-f_r)^T H_r(phat_(i+1)-phat_i)>0  for i≠r;

its omitted arrow is negative. Both apex U and these five local signs are independent of delta.

For the impossible union, keep (w1,w3,w4)=(1295,2413,9599) and solve

    [e0 e2]*(w0,w2)^T=-(1295e1+2413e3+9599e4),
    e_i=phat_(i+1)-phat_i.

Throughout the rectangle all five weights are positive and

    Q=-sum_i w_i sym(phat_i e_i^T)

is positive definite. Zero displacement eliminates the footpoint, so sum_i w_i D_i=-tr(HQ)<0 for every SPD H and every footpoint. The five weak arrows are impossible.

This whole-domain proof uses 66 explicit polynomial guards and 1830 strictly positive exact Bernstein coefficients, with full power reconstruction. Positive projective denominators preserve strict convexity of the original polygon. It does not extrapolate from finitely many completed bodies.

Consequently every body in this four-percent subfamily is locally and apically inclusion-minimal with five arrows, but NONE of its proper subsystems can extend to full U1 at apex 0. The metrics for different omissions are different; no single metric is alleged to satisfy their impossible union.

## 7. Global projective centring at a fixed vertex

### STAR_PROJECTIVE_VOLUME_CENTERING_V1

This is an analytic theorem, independent of the finite matrix certificate.

Let P be any bounded full-dimensional convex polytope with a true vertex A. Put K=P-A and C=cone(K). For every z in int C, there is a UNIQUE vector c satisfying

    1+c·u>0 for all u∈K

such that the uniformly filled projective image

    K_c={u/(1+c·u):u∈K}

has actual volume centroid z.

**Proof.** On the open positive-denominator domain D define

    V(c)=integral_K (1+c·u)^(-4) du,
    F_z(c)=log V(c)+4c·z.

The determinant of the projective Jacobian is (1+c·u)^(-4). If m_c and Sigma_c are the ACTUAL centroid and covariance of K_c, differentiation gives

    grad log V=-4m_c,
    Hess log V=20 Sigma_c+4m_c m_c^T>0.

Thus F_z is strictly convex, and its critical-point equation is exactly m_c=z.

At a finite boundary point of D, a denominator vanishes at a nonzero vertex of K. Integrating over a genuine three-dimensional cone at that vertex gives a lower bound proportional to integral r^2/(epsilon+Cr)^4 dr, which diverges as epsilon tends to zero. Hence F_z tends to positive infinity at every finite boundary.

For an unbounded sequence c in D, every limit of c/|c| belongs to C*={v:v·u≥0 for u∈C}. Since z∈int C, there is a positive uniform lower bound on v·z over the unit vectors in C*. On the other hand, if R bounds |u| on K,

    log V(c)≥log Vol(K)-4 log(1+R|c|).

The positive linear term 4c·z dominates this logarithmic lower bound. Therefore F_z is coercive on D. It has a unique interior minimizer, giving the stated actual centroid. Its positive Hessian also gives analytic dependence on any analytic fixed-incidence input family.

### Application to the degree-six completion

Take z=-A. Since every apex facet has q_i·A=1, q_i·(-A)=-1, so -A is strictly inside the apex tangent cone. The transformed absolute body

    T_c(P)={A+(Y-A)/(1+c·(Y-A)):Y∈P}

has actual centroid 0. Every plane through A is preserved. In particular all six prescribed side poles (p_i,1) remain EXACTLY the actual polar face after the uniform refill and centring.

This provides an actual own-centred 10/17/9 completion with these exact six poles for EVERY five-cut vector in (0,1)^5. The five proper-subsystem/apex-U witnesses above apply directly at t=0. The union of all five arrows remains impossible. Global U1 is not thereby supplied.

The five cut parameters remain genuine. If two labelled centred outputs were equal, their raw bodies would differ by a vertex-centred projectivity preserving the original base plane. In A-relative coordinates that plane has equation b·u=h with h≠0. Preservation would require h/(1+e·u)=h on an open part of the plane, hence e·u=0 there and e=0. The original cut fractions then coincide. The same argument at first order rules out loss of differential rank.

This extends the earlier local small-cut centroid repair; it does not assume that the new uniform centroid is the image of the old centroid. The supplied original construction had explicitly restricted its implicit-function repair to sufficiently small cuts.

### Exact algebraic recovery equations

For rational input, this global construction is algebraic, not necessarily rational. It has a finite exact specification, without a hidden optimizer checkpoint.

Write u_i=Y_i-A and d_i(c)=1+c·u_i. The seven positive apex-fan tetrahedra have nonapical triples

    (4,3,9), (4,9,2), (4,2,1), (4,1,7), (4,7,6),
    (5,6,7), (9,8,2).

Let a_T=det(u_i,u_j,u_k)/6>0 for those outward-oriented triples, and define

    W(c)=product_(i=1)^9 d_i(c),
    Z(c)=sum_T a_T * product_(i not in {0} union T) d_i(c).

Then V(c)=Z(c)/W(c). The unique centring parameter is the unique solution with all d_i>0 of

    Z_x W-Z W_x=0,
    Z_y W-Z W_y=0,
    Z_z W-Z W_z-4ZW=0.

The polynomial degrees are at most 14,14,15. The positive Hessian makes the relevant root isolated and nonsingular. These formulas, the literal geometry above, and the positivity domain completely specify the analytic recovery.

Only ACTUAL vertex denominators must be positive. Denominators at the removed virtual B0 or B3 need not be positive. Consequently the global method can leave the bounded-parent-pyramid chart while retaining the actual bounded ten-vertex body and all six fixed apex planes. Releasing cuts after such a motion is not a valid bounded-pyramid reduction.

## 8. Exact nonwinning controls and the genuine residual geometry

The capsule preserves FIVE actual geometries and TWENTY-FOUR complete reciprocal physical censuses, with all 1632 true-edge primitives nonzero. Every reported control is weak000. None is110.

Three finite controls of the certified family are:

    INDEPENDENT_CHAMBER:
      cuts=(1/25,1/40,1/50,1/30,1/100),
      s=s0+rho*(1,-1,1).

    EQUAL_FOUR_PERCENT:
      cuts=(1/25,1/25,1/25,1/25,1/25), s=s0.

    EIGHT_PARAMETER_UPPER_WALL:
      cuts=(1/10,1/10,1/10,1/10,1/10),
      s=s0+rho*(-1,1,-1).

The explicit uniquely-farthest metric M_b has strict census (5,5,8) at all three. At each of the first two, the five proper-subsystem metrics with delta=1/100000 have censuses

    (2,2,2), (3,2,3), (2,2,2), (3,2,3), (2,2,2).

Their full labelled faces, equilibria, actual moments and matrices are regenerated exactly.

### 8.1. Deep completion: the highest nonroot can genuinely escape to the apex

Start with s=s0 and all five raw cuts equal to 1/2. Apply the vertex-centred projectivity with the EXACT rational parameter

    c=(73937418215,-52783343258,22255077115)/10^12.

Refill uniformly and subtract the NEW exact volume centroid. The rational c is not asserted to be the exact algebraic centring solution; the small remaining centroid is recomputed rather than ignored. The resulting actual phat hexagon lies in the certified apical sharp-five chamber.

On this changed actual body take

    M=1/10^9 * (
      (431719526,435572152,-234354122),
      (435572152,440501457,-236815216),
      (-234354122,-236815216,127779017)),
    N=M^-1.

Exact verification gives

    n0>n4>n_i for every i not in {0,4},
    D40>0.

Nevertheless the complete strict census is

    S={1,3,4,6}, U={0,9},
    H={17,01,08,34}, weak000.

This is a genuine countercontrol to extrapolating the highest-nonroot exclusion across the whole completion chart. The highest nonroot 4 has its strict escape to 0; a LOWER nonroot vertex 9 is the remaining U.

The exact positive two-root forest is

    1->2, 2->9, 3->9, 4->0,
    5->0, 6->4, 7->6, 8->9.

It carries a real closed cutset

    T={1,2,3,8,9},
    outgoing boundary={1->0,1->7,2->0,3->0,3->4,8->0},

and all six boundary primitives are strictly negative. As long as these six signs persist, maximizing the norm inside T gives a strict U in T; changing only internal orientations can merely migrate it. A full-U1 continuation at 0 must change at least one genuine outgoing boundary sign. This is a physical cutset obstruction at the recorded control, not an all-SPD assertion about this distant geometry.

The same body also retains all five proper-subsystem/apex-U witnesses, with censuses 222,323,222,323,222. Those are separate metrics from the displayed M; the displayed M is not alleged to realize a prescribed proper four-arrow subsystem.

### 8.2. Horizon-crossed completion: releasing the cuts is genuinely unbounded

Start with s=s0 and all five raw cuts equal to 99/100. Apply the exact rational vertex-centred projectivity

    c=(2508866228100,-856246252299,12197902788)/10^12,

then uniformly refill and subtract its NEW exact centroid.

Every ACTUAL source-vertex projective denominator is strictly greater than 1/2. In contrast,

    1+c·(B3-A)<-3.

The actual body is bounded, with the same true 10/17/9 lattice. But releasing F7 and F8 leaves the apex cone and transformed base plane with an unbounded ray in the B3 direction. This follows directly from the negative virtual denominator: the transformed base plane no longer stops that ray.

All five proper-subsystem metrics at delta=1/100000 still have apex 0 strict U. Their complete censuses are

    323,323,222,323,323,

all weak000, with U={0,9} in every record. The code checks two actual mass fans, the full primal and polar lattices, and the projective tetrahedral volume identities using only actual vertices. It does NOT project a removed tetrahedron across its virtual horizon and treat the result as positive physical mass.

This supplies a concrete residual geometry beyond bounded-pyramid completion arguments, not merely a failed stencil or a formal sign assignment.

## 9. What remains open and the useful continuation

The proved all-metric domain is the explicit five-cut cube through 1/10 with the stated three-coordinate base box. Its four-percent subfamily is entirely apically sharp-five, yet entirely root0-U1-empty. The global projective centring theorem supplies exact prescribed-pole completions beyond that domain, but does not prove their full-U1 feasibility or infeasibility.

The two distant rational controls preserve useful nonwinning geometry. The half-cut control shows that a proof for the wider chart must sometimes control a lower trapped maximum, rather than prohibit the top nonroot’s entry into the apex. Its explicit six-edge cutset identifies the actual boundary that must change. The 99-percent control shows why a proof cannot require positivity at removed virtual vertices or assume that releasing the cut facets gives a bounded pyramid.

No unsuccessful numerical search is used as an exclusion. The exact finite certificates prove only their stated full domains. Full U1 outside them, all proper subsystems being full-U1-compatible on ONE body, and actual110 remain separate unresolved obligations. The generic outside-polar determinant coupling in the supplied reciprocal slice theorem is not removed by these results.

## 10. Complete source-only recovery capsule

The following wrapper contains the complete autonomous 26283-byte standard-library source. It reconstructs the eight-parameter moment formulas, all six literal stress rows, all interval/Bernstein certificates, all five actual bodies, all reciprocal metrics and complete censuses. No parent file, downloaded report, numerical optimizer, floating arithmetic, or unprovided library is needed.

Environment: CPython 3.13.5, standard library, assertions enabled. Save the entire fence as recover_hex6_completion_v2.py, UTF-8/LF, and run in an empty directory:

    python -B -S recover_hex6_completion_v2.py build > build.out
    python -B -S recover_hex6_completion_v2.py check > check.out
    cmp build.out check.out
    sha256sum recover_hex6_completion_v2.py hex6_completion_v2.py hex6_completion_v2.json build.out

Exact final pins:

    recover_hex6_completion_v2.py: 13436 bytes
    SHA256 9a88499681e8a7a0e39c06eb7c33e7a642e2e86c0b2d635fb1aeea86b35e333f

    hex6_completion_v2.py: 26283 bytes
    SHA256 05f5a286918d7c6c9a7398bd8150761fc43eeec629cb773add400b52a795a16a

    hex6_completion_v2.json: 4213189 bytes
    SHA256 522c3a4e4d24dd0c56ffb9f53681bf8d84b247a6c4b06a81492c0e3f749bf7fb

    build.out = check.out: 1505 bytes
    SHA256 392c484bd087e27c8678dd6fb88b36df86e08923d929ed23948e37d42066d032

Expected terminal markers include:

    FULL_INDEPENDENT_FIVE_CUT_AND_THREE_BASE_COORDINATE_ALL_SPD_FAMILY_PASS
    MATRIX_COEFFICIENTS 1998 SHIFTED_INTERVAL_PD_MINORS 5994
    LOCAL_CHAMBER_POLYNOMIALS 66 STRICT_POSITIVE_BERNSTEIN_COEFFICIENTS 1830
    ACTUAL_TRUE_HULLS 5 EXACT_RECIPROCAL_CENSUSES 24 ALL_NONZERO_PRIMITIVES 1632
    TRUE_BOUNDED_COMPLETION_WITH_UNBOUNDED_RELEASED_PYRAMID_PASS
    HEX6_COMPLETION_V2_SOURCE_ONLY_RECOVERY_PASS

The final source build and a fresh directory containing ONLY the wrapper were executed. Fresh build and check agreed byte-for-byte with the recorded report and stdout. The global centring theorem is an analytic proof, not a claim that the program formalizes convex analysis or isolates its general algebraic centring parameter. No independent external audit or proof-assistant verification is claimed.

```python
#!/usr/bin/env python3
"""Self-contained exact recovery: CPython 3.13.5 standard library."""
import base64,hashlib,runpy,sys,zlib
from pathlib import Path
DATA = r"""
c-rNC`*Y$*lJM{TE3`9lfrJY;5)Wh3H4%0jkJ<3s?w<DYu?iu{ARCY@35<Jg{`bqws?q~+ckkYPaX;MdjFIY*Rh5;M@6!DGw-1XX
{xAyWAN=`Ji{8>nIB)Fy^2;y1mE)!w{JU_bn&*#W->)UXN^`?mH1*RUoNJHHESSD^wNKa7O>69#jlGtZq~0_b?d=F)TJ2b?-Dwkl
)wc7#_R`vm-n7von0o)|PJH)y=V&_B#(p^S(>QRoU>+^fM04hzhNC8F>?es9hp$i;``R=}{n(lA;Y@cP<8Y=u#xPfaoM^!;3gc8e
l?9rUXs4o0<fIdrnrd+kuRHR2;v`tbo|14b8qc6swS<X}L@AD&hT$|DCW=FE;ihsDi@95>jeV%})gZ}RvUAPT1t38ee^2!lGwb+2
LwgKkZ3PR*Rf;!wz;|75*PC^d)f!f--7=Wo!49luQ9q{FSzA8UL`_G%Ham?@TXX~nRMOn<m`x~Ywd(Z)!!UO4ILxAE?l&9zO-oJ&
nqpbK(=qq+GGpiX=&onq9-Z_*-|<u3%xZQ%eZIFp9bL;pct1P3IPTqMWme1Bxj(-WLy2x;2zoY*?)_OGE9E=OfWx5f)Pb$<AMOAd
K5Did%!Aan^~9e(vK4#dm*Lzu4mEt=n}#sl%IMO|B)}Ifc+}psAkna$=1&t}do#KK(#IVUoj!8eL5<;fo*E)FU}P=iZlH%oH}=y-
JlFcV?717lA0~Ul%Oo&%pnpsNxCEr2&i%23Y8+;OYO*t{NsxwWo-9U%NyrZPx?7{ksCMzzhSX%2fU1VG#dQ0sUid%`Ud`7-FEB4T
ziM%%R5Q%6F$?DUi@|2j3Vs9zXfQ4ZRWnHAh3^H+?X!@3G7nQNq)n-R<Ty^Zu=Hvlsl@m|Gm}pRl*N7&ucH`vhpx6u%^&879cWzD
E<{QRl3<>s&fN9&ko65gFMUMzH-E+9s2SCkq{!=V`nHuQU0!FNBug64<9|Z$Lm169{=!kbGCg`*$ZkZa8F4q#M@HA<Uf`x;6&|dX
*n`iIPimt*Zx7hgEYXcaZ{QEPw>S1v-DiCrj?b<Ot>p@F#yWud*GN?M`qMwGxy5nCWYo}qZ6n*!I@#i4wvlb#kea+pw(D5=^RF^4
%5%cDRQt$Y*D-}v+E_B<)$W^Mzw8a$eG4K$-y^UkZ!lK)94mZQU*E&%&yai>B~`tTG(3{zh^tc7qcw6IF&s=%B#kS3d10zMMYxNZ
uCJ;aE5bGgtBX#6`%<UDs<ySmkXi$YthL_#PHR}co-(J<x|-(F%@K_}Kxy8@8PtdHPgQpY<`Dj=Is<D6|J3N+lJDlws8LH(wXDC>
vOY9+sin2v(v&UDyd}*im@jcYuxngQO>v#UKnFQxRI7Th`(zkZsI~OLz!|KDgSR2Ai*OJ-^Rcft43am0<H4{X&<j<ozwxJ`@xi0o
r(&(>5R{4(s;n)zlFP_2B9|$)02aem`3@kB#84pA3b_raP4Pd?LtSsMHfRV39n>vAdoT~+;ehS8+MNa}4Y{B<m<7$@{h-y^$5z;L
zrAn4W0RStc|eb)9u3h$DHhnSUT;|YqTRmL>NJ|rtO?C5*0S0iOAOy^S&deE9a@W;wcG6jIm>o^f4_CG-mF7|?wg%@vqNJx8&*fC
K!s+1?Fei+&%O@)5Yz=I1R97UJ{a`%Raq$;7L~H=VK+%QHmX5Sw%Ucih30p|?#M}eKBzUSNdnu##Dh5mHd1TA3-+otcIm+wcAW@;
!35<W6E<Ia0l^&Y4(N?wM+iHLpvsLy7=P-_MxLX=**hHI{#QrhC|LLeW67twpc1NO@<|>9ss(sn5W{i^s{Zma2!;&)0?C`kf3%0j
I%&3XcE4($CSeHN=rLINsHczT@Z+Lb8~bz6&(knYwATRi=qOBrG+2VD^XDNb3skkYBfv7xL&*MoF~d&2j&mUn9SH7*n1n_K2=0&d
L#&1Qabz>FnI1A<oV#w;upulFj#r@<4I+lXt}t<_XrR)Pf>J;YQd(SM{8r!5Mk78TmKQM`Bt|Im=*YPu!;2F}6CDapua>BL+0?~+
<r%Djlvg8rFzRo0#bHqV!~A0;lPax^{_eu&<UoNZ4QS=hf)bv|GN`kF;T{c*jV&@+i>4NF6bN2obf-XK^b9O90yw)P+<W;DWDhVd
JQ`|m*0v^LrX1_J%&9cD&a)-7=<iQ0pv7qV(7%EG8`RUHzs(=_Z!n8BMgQfJ50tJV#CkAK^(W2)W1ZQy;FRN``fCGgfU_<LHTI1y
*pe@oJK6~sKqI3DLbdv>>eg$E>ayxKcC>Rj;uO)D*H?ADSp$Ju`({)#9IvVZ>2FxnqM~p3D6lO-LeEBRQCm{KhT0N~9u^Y766>1z
9<A@g1Mn`IRcaI{dyRb|ZPVb4;4=crXl4ilTRIL)+1s12Kxr9ZZaERKQ1S96o2&P40-$(r3;}_vF}y6r2!Qv8JtvC%xu=UsIu0&m
H?8V#Z}3zT?^_lIJA6a>o}f#)4wPX<oer#awR~w(+nX}hUc;Cm52gT;ZV2ZWNT+5BMbYP|Fg@ThAK<7M-ERSvAbV(5PedU*H>mLp
W>C|=1p{YT^#`Nju8&XfJ_62U(O{#^NjdA2B2BM6{F53Uhk$XbREE&$cQmYFwRjKk-Kd?bS-{f>pPb>(&p==k{z5NY$ZK^bo_-p{
4RLBG-BB9z2|H&G>;~zA2@VZsnjtTZ*fe5pow*HTN62O1m4P!AYFSwscGzjjzH^Mt7X4iPp(bc2GVufk;Bd18npjz%Ke6RA8gMj+
r6ftVB;_fydN!d5&kmagNoo{kPy(}*8kj<gBi8HB-O%&Bg082dKWfig%%Viku)&frPVHy^E#dcIT!2j*IYQWSy~5!ChZV3>D*ta@
G4=#VUFf(YKc2Vrh<W~)xu9@JuMML2S4}wlQh%PHxFm;Pq9u{<29E)V^~jH<7p@B;-hX@y+`ylwi59}@>IiQ5&lX7ZZ~-JEIS3tK
=^)dqx}XaW#FY@qB$53wX<XV1N5w~3b1PxaMQa9|6rav?s{0?gCoR8BB11QVC(o}lf7AWno@A@1LaS#O6ZDicm@j;6{K{ee)hY@{
e`P4E5&D#1KNIxB*DC0V=n>SPm~Sw8^5BX3z3g&fAOao~qkA#3jfT=4Wp0Sw7$x7^4ru1bpkV=$(}}OSfbrOw7B@h1;@ElXYAtB%
`8XaHF6P0~0dh%w4LZydSk4Uft#KTHbbLNsDz!%vG_LR`Hj0fBB>BQNARx|{aH4X;hDK6?tcrpacW^$=P4<6<I<%NS51iGo`;ByT
wL=Aw9z#dLET5k_9zHm{-Dm2=pQ!xXE|-Q}TzfLAv~MwkCq&9XXbjKKg7MAAAceTtT7Qf{SZq|keIPQ4p#>pwKF&54aau$u)+^FQ
T3kv~!(Td68}t%Ch6gx`01&7BO;Ufsl~JU9n7WHlh(Ha_>%t4*R-qTmN!Q2;?VA`*xae)ba`;GRNKz0dlgH>jE~fIi;MxT!ic6zI
o?{~<N%YV!fWG4CTQDDM(OV4Ay#$AJ0zshY>_CToEeSlIOaZ1LmluwF^z5e^P;?r&K9b{iWB|vZfnXO-jLPv)$^B7T9~}vgkPzTe
x$fG?Bsn=1QIQFlv}ue(0a_hWvxYVU5l&?64$!qYM2AVqS{SQiGp0Qz0Aw-zs@>!2Uqe8~EL;M=^c}E$roIC<4<W_}v`>6boL;by
pb?5oFq9Snyb_XL7LFGOQ%A-&09KN6FRFpYiQ1-|2$qul0LuM@mkH{GDJIf&>bzO?Cbe>db5!<Jn+&8kA%L_?@C;^4o1UGz9LR-M
unFBXOo4dnU6cgQjLWFWUNUj4R$G?@94N&M(GSN*I@!=U>?`eEs&A+s<c2L4Za)FIi7p}^YF!lH>k49v*zers$WV}rl$i)R4MSi(
-I1F!ppvqZ`3ehKjl*O)bRK|>J>-IC-v}iO^dOQ50JK;uj~J@&rDg;u3SleIm+C4~l8fEaYjgR35sU)+b&37Div4~E5^Vm$2T(>4
L@tHI3TU33(<G@K@pPdWqll1bV6wS!DB&#0UH?jxc}4OeiGb>OFb`%9AE2*$SZx$Jzd-Ta6&MzpCcwvIhOR`4C6G^1k<7oNvDS3*
^^i8e`AD!$X&C$zJmftHja+U_`2OVkA)F+9H0cr4e>72{Ky)l{jg{JJ5{JYwfD55Ik!+J>Kyw0Zpwe?Mfxp-vR*;pJqX#%dR>f2Y
f-H{d-XijlA1d{d#)gUF_=X|Q^e)HE!DFr%A_W|fSNkhY<`%~zjgBFy9CFfI3aTKVyNo8XnAz|f#`ZLP^<#S!g49U3m?IHj6r*Wg
IX$}QpFh}ly-!z{C-%kBSNluv_P+PE!U9(5U*7j_zZ{+0*C+O;tKR8p|5Lwrd4FeLAKl$m7>xBeT_h7yfems-h4TcN9Qm1K;QG_m
1!~pPFj>SPirf%6k*B30sF<i<ft&-Z1A_)LdE(49v0m-f55|)eC6u?xVDr$X(FN%_SQqKV203p#N57MUEV(wF0uxrzF2|89HU+|+
esCP>GQ}>?4hgHIZ{43?!Tx?sQ?bh*xp;yjcYoGL(pV!VtDqCmj-sH!*iW!XctPefcaho!C6p=0i!H^xEhVw|VH5%ZArDBlLEhWT
a0+6Vqika0nTj*qb8o`P-;5-Ny^~4sm~uLuP!XoKpTO|GJ%%|@#JGvh;sSZuK(R6E4dl;S4Sp$--Y*4jJC0!F^H)0~NHXC>?l^-Y
Y;jO*A;-8pHWPp41!Gu|j^L1zV;^KU)GkD-0dKSk(8QSm8x`owH=hX_w9^6>Qka?K&pRrNXaNKK<(FUXz=(s>Ea(zw5(WSQj>731
dQ2Unh*T;W1R@N)8VpV831RG^Qx%jdOo;fon56zED35jH@Ki-5UBOTO{L9!9qXdz4s?1kk=(y_&?)$Ox$fEe}_8=y~3Jcn<gF#G3
1~JJczq>4i+$`PW&c7JKv}6EtSse2x0+{P@cUs8z<L=bthjDj>kwO4-`Qrd)xEa6%m8w46eMITxgD8S0a|nPjZt2Llr9@#VZdpL$
&qOWVa?}zJs4MY+>`ydGOCiW*6{Tdgiu0?Yl*C7K`2J#rkAe{Men|e>QV~$v35uFx%)%<gC%1$+1aMRibMK1C&e3HMWyRhOSJgM>
Fw@w{{3Vv1xuECH%x7e-Nrnsx>duCOD|xUlHCSUSNB&jo=hpi4EjQA^Zg3~sER<&+1QninFy~V(0rMdCK_(F|LM#4M`8Z3av^1o_
Yz4wF4VJ%~_-;rS>N`G`cfk3p5;S-fz=#Zi0=T<Hld+6LsHzG(8oGdb@(h2Bs*qw}iBn-s6zW2P)kG!O=~%o&Iy0;nJ>MLl?a;0W
PC^x1d<~X3WQ%m&*?{e7#_zfj$YGGV68y}Q;Flc<(g8%R*^_btNlyVriE)zBr{D{P5T=7Zg>Ptz;0n+cRMZl&FxS#iMI?GdC2O;q
Naz&o^2|e27EO!{UeF~_2KXBF(-LPEP0?~s(Sk&^z!i8z*#8z9{{^qi1}eMn`eR^TTT!>+jv;>LmN1F$oF-USdk~jgA#}U;I`svX
4W-2LO}q=ug_MLf+gB;q1O1uN=9i)v=&^-L0zWj2qG|!W=Aw6h+y8XObr8snmf42C?R~S&+6Vgw2dri_ObgTgOxEb^x1pd>x1hFp
P-m@9yVJy3=@x6&_f3;EJ0>>S@6=l@w%^%r)hSAE0;mqFnFp;#9e%7<XTJfzFpiAfH?3x?%^Hn;_}glkjRTc#D448B%d{yiQ^y2F
*wt_bymCZ=GAPM?oHM5Dr@)WRER}Gio?)oM8zykkQ!Q&OS}Y1JmRXfx%G1yVrAp~sxo0cox)Ae#C(vrlzYHed>%h?Q-RMrhniGzm
h@}PP{2Iuthrv-1(V38$b4{U8gQ*gD!Llu(RtmH#$9E|ftVBk^8@yepDAx&_Ov+BINn#vkjVrL+C*LK#wh&3TE4vu22n^^g0ZIRg
q%1neGj_%v`Nl>nL*z`@xXKHJmhKt(wl-HwC;C_IdP`7Wo7llWE%-}rwmtHtazr@d7O}^21V6%N&zAZb>k(E3t5+*^Vwjv<m=1Ff
kTPm>QV2K?XF>~@8^-1Y+hT%GT)O(Yejcn-Tl<u6?33Eo@&rKX2t0pn22$7X16Bt3Xh;|UWD*G{6zp8r<FZE&6|^4aCUo;5gqaCD
2^I?CZ=O~dWi#*rkZzp_xNc;wPnisCGSfO}(W$nYW`j=eLF?c^2;)b`Rl}De<q9>3z~_QH6j6jLj|oLFA?39SP_kY5ReQAqjcb3{
!3TX3RXqa@=^5xKThlsV&;O8#Bo@G<HCHE;7%-vy7o2?+;jkiZVrpbjqsEX{CK}<==xMm4ZJ@4RVSiu>*CtXetg(hP{~KGn12{aw
$--s)vjGd)!<h0wAbUMBY;6XMt!yvWPs0zfPG=GnJ|``JtLYYP2j_txXH&iIn#xs`5xBE1nAe?HP<kW1Ui=SCB7sR&>C9mWxF-U_
yVv4ZygL|>E}~UL`0SfHAofNugd%QbH4yAgML5H51cjUgAb3-0yauS$LJvRD989rZqB|RO*w{zcwwD{X1-lhJFTvv*X}ba55|{xD
M_e-q(L`}nx=<=8S4WLQm^KVFMh40wqXcrx%yP@E21yh|)?~s5&K}t+spR~G&`C1vMo>3!K1}k`D3V_3h)tC5^BS4!u<QFmPDB$S
5%71oT_R|&uf;(>=z>BfM%Bv-3sd=HSV#~8j`{k^253Cx=7jGL4bJmAbE6K~wMTn_IS6Qmy}lwT&~%9od|wiRC>f~|C(BJJEyLKP
vf(B<7H2L-hv6kLZd-q~v4Mi07(#jt|2Vrk@7YJ6?mr)$+n;)u_qSL56Z_NI(e1r`blv|1rFZahZJ+kP^lasj5njWR%dn^)ruHaY
aa~f9!KAkf<TfLRkzG<1g$JrqEUOeeP|!<gisHCXdYmnNid;wjNBm82Z6+l$dB>!@236<u=u=N<giQt-8C~-Lg$`61d;;30UyF6<
x5ExtgPt0!NfH5|L#+utFom)OF!m{3vcu2-?VbECp$m8dnt;$0V+pvVc3Sio`-|}`CQ?6}^!I?qlcUgIY$?Wrc^L&Oy_`h+-%40S
m}E5rck=b43@TX}Gbf@@9>arMJu;LMJJXNYaXtZ=7V8>$@FWL$EUA#PWsk&wlC!<(^8%1l9TbwM4Lg6nnb13z3BAbC^b1x*hDhQD
ZRmo6j-*6-4gCU{mvmg}7o{k~g^EF3lp_!qMyArq$UqpYAf>t!RXaa9NB3SaWgvVc=37uk6zAQ;M7M0|4WoOK$79z+Xdb^nZW0WM
`J9Wi!fMs3o@|keK|WRQw|e&^3q2^AS3oB)Ta3n?W1dqmL}WY_hIyi4)Nt>NWqj~*i+iTSKj&;PI6?mS&K_=0$~IU|CFcfk-HVKu
NOZFkX{^jblw<k>16k}REMze-lho&@4oG)I*cY;#yMN~c{2f*s-FrSz&s&q#$Q_7f1d@~w{x~oX(e-x-5&<*_F^JG09yd{GGBkA`
jheL0F>x|v4+C@}4(azv{epxW4!a^Hejx4)gawhcT;jkWIogGgm-icqAuU;obW=y|hU~H}xv%?WmwSK(%)0$M>7d?+CQFt^=2X}W
)@}yz4)0~28uzMtvP5wQf8ky5Yj|C$+_jaQ3kbb>wtHXL-`TxPJzGS0WiObI?a5*~)gN%o?Kc3?ErCi5Mg)Mq<{%ybTgssG5{gL_
+DMNY?!g15$J1)ikaqdtLB+#~;-K@eI~OJd8BimJ*<bMBG7(6F&7Om-tuy%lu$a=6OgVA4IW>R7=J{2HhoR_-{2`eduwNKgNB1SX
edP5+Si~M~1uXcRKgZ<+(gsP&)+w~7Ie<Bl6e3N~U!YOw-MYI-6P7esZobM;#82W>oDL@cn1)QQrws5005-aqDPK<BC|mc(d;rW9
FL?|$vfC*K1x~f-S8Z(1cF(hdaWychX*eIN1pI(KG4~KrcC2h%moWdtj+I^b0Lmb|fsi{!sdkJBx5tAP$Tx%p!WM6AWG__nR(yw!
-_&~p8ZYt}g0&<sL>!C(aj^T#!Qn8^$$Aj^j`;>4`^Rm=eGqvXb99dEl5-?$wT*hz5W}LF!S2Fa@E~*N2?^#0F9#uE<T-T;5~JQY
d)iWYiIfrdSSs!zma#Q6xEoEKxsO>wUEdqSgGv*A47?S4ER!rLRw5a#aI%ownUd?(QIx7et59fkM_e2#RZ`a2=fE64j^ybZ)kIM-
<@2GSC}T8N2SvFK0z@Zbdo;-PlHz$3r!Cz$ZCfOxVCI4+szl+(f&PTVE$VWvp0U&C?fuK%fhSgkl4W~{bqU=08KRyGqZon|#I`7@
4t++syC%=ad}IajWgOBD?g7sM{^2a9sk|vIJ*aws?scGzp`qa7Cg-V4rPc%sB{b=~BBcq?j_X-Msg>`H7`2cjqb>+<$N^659W~61
J2F92#PSz&@8|gcfnxoXvLaB0`b&LH0LZ%}GPeZirO4)&Tyiz6V+APY8WbrkaP^8TKk^Z^nTwn{(bqVnB@p))s9YAXA(odRKx8^U
U;`4JJX3cFA<W5p>eK+Hzt$vV(ij_a!7rel(fulH>?Iqo9UgbdT;Q~+0`paZQ5sV|pu6P!3+=f3lu1a`fp2~K>HsObD*G;SVt`hY
sSY(@Xp5wlzJ|3tZBMFlC7pTtwkNLcIHN?*RHS1#3b6G5iCa1t^g5RJM~>wco#X%34V}_VM+|`%>~Gx>atDP?b}470OQY0<gqcGk
NOV~jl%7aotkUh6n%k%@s>>Y>I3(Sg$!dz1W{&eaGvdn3adu<oSY4PAfbt77$MU|+aeiG!+?F~1-es9+$)YC~WdxOpqzwuNx^Gvb
C6UyW6SZ1R=xqEzux9!?K|I_NBwN?V@xbC$a|-GsLuEn}7pZ&U)Pvo~HF7m$)H@ubbn1n2PQB*-YpK`6_nWJ$_|&T^aw>t<t!t-n
p2c)_#AOwA*cDb$w26aHj#hEPbtM@wp?q#^@}S|n-1i0m{+TPKPcrX!tAwXWffTFjhpvu6@Ci3-W6Z=#CF_~6G1}2a_k0XC7`|s(
=TLAMrV8O5vm4+IGaKLsD!@=W4>&U8b4>R9Iw6&_U@DFcR=iRAb=bWTZO#MsA}U@eDK<yI*9nXw*%z>MCBR-_+MJt(E|bAw8}|-<
nG(%;pvz#<TChtcFiZgU3od#cRNiKwRR5PUmTwGoJ@bWqMK%Hxf=Q7QuGHo=CmZquVhW^j+jwhbhVBLqrhzEI{g=BTWmy|#8OvW_
AST$gUFbqt<n*qx%lR>jo!9*JfhFN0b_)%%qh7E|3Yu@Gzi{y*On5H%f>1N*uS|F2Uzp0u;$!w0#7Sxkp2Gjm5)96J>ir&JXVdt~
qHqeoH;j_G^7(z8$P!sUVL+GXV+KS91e5ZVMH5gRq6tk^X6Y4j@w|x1Wb{HQFc!sdnc$!*t_rhH7KuIzy*GBjE(>WcGjvv6!u}S0
K(mMo2UT}2o-UE**^NXEf*DlQS}I^;Q2{L_d!we6VK+jJz59~u?WE-~{h6V8sg$#|Bo#-n3|+Q;!uZ@_l!#1h>0$c{Ha{t-Uoi<A
-|}#Z>W+gjeM)zNUW(l>*^TOcgWYdrcZn6`*%5L;e0af!Ml(C0Q9+l?Pi;xT{LIzKDlsOdr7b@SBS0iWlL8ba#e_QtFSf!lz1srk
;Co<Rwt_k11H$AF@lTEeX9Y_fKr1+!$pCN<26Zxk_Vf$L92y_%!xFCUj9vWsY}D}Q4ApPo4vrTDd?2@Lway>?#N~emhd7+Bd)e$9
oSpX$O5Wl2MLu-L@7QPlnVs=7_Ub#&C~PqmlFh^UH$M*TC=O;6@=AES!|)9(>L_8D?#f>%`}Kmunc$b~?)pR|A;8I+MQk2niWDx2
{$dt8<wJ|?R$v*4E6-cvP8P9##vZ}?ou>JxCot?@@QUtezk@J36W@9OYr1wOKKJm!0~u616W@G*av8pd;$in$-HoT{`Xf@?rF4&+
(Wfy6&*bWpC8j7r^Oq_ZK8soH($3%{(Td!GRSyQgqayl*_8P_*;pqc4-Aw)(?hdexsNQg-Qazc`q5)cg>d};ahD9E9$u7z~DBD!n
3CY7k<iJzGB|Il}xUN_FmnXgJ9{jnySJ9w~3>CJ-m!_KXi&HK6+sMB_g;@u8nEF=CmA=DRM6tjuR*Nhl`k!9u-C&gJ^y>4iecijo
XcdfIOcFM#EinQ?CGS=lK>zo%d;9w6_UNK_4}Csg104I0qw{kFB$Kr>Ahq>rmga5NO4BsTw>2pfMSAKey%+FDU)up*&C8BFbc6^N
p37k1<47I&C4uS)=|lL`(UbFYZuRaZDNh&3p<S1+%OiCrTz62RvsIyV732-YBG6$C7}{)h8Vpm&iTl>c28ULkD?*7v79`(|-;fdI
$#8k5m{>C{lr84L%fh!GK^{+h5bcuExa%?}3NRxHm_X#mm^_@kCCHNivC`_MIRfUu<SuM|W(sWP>U<|#=VHPxCp>2!`DfS+sN^E9
A@=5c43hR@QVdt*70~)pw%(`)JQ^^H!3ys*tM_+BV0aC|Mf_?SW%MMH*<Y3w0<=cRyet=DfPKB)JLy;Ddr`nRw_C?z62dt68xLnv
I#cN&oDDxx=mM!>P<d}-E5p(qnGi%p>U$iwjN_(Bj$Zgep26he#Sar$<ZkgY%%>}iWW%W@+N=D2esv6-<M!$bIL1KI>uOk#k9y^<
!T`gpa#jI@gyvll0dVL+U0w$jF%)3#JAJ8KeEs12>mHT^=*3IU&~wW*XV3Q|I4cXhgCUQMxQ5Er_YX0>uUa*&f}=;@ZyYrCn`Xx{
TddZy_B)M6vthM5%(ARjtG>T)nsnc<$e9E~H@5QAqK1#N1Zn_jtv4IyzIo8H+N{}Vwf12&3zIG3rD<A}6`2(`oAp-RY_|5XLAwJ*
CViPGYh5U3rnSGne^58~agG-h&Rfwc55Ds~A)M2&yTSJaM=ZFt%G|H`+7!%iDG7gBCj3H6X&NgpFGl>!0|<o&L9#3%@W(6^*hs{2
6IcWD5omuFbI*z2c-bkNC#@6*!%0!Pi-^KUGzjIm$cbWMVWJsuu2aTmo}wT!Uh7$kLWk9h_jski$QJ1rvS<`g1Ni`y;ssn?W<aQ{
2a)ekr%Z=BWjf#>BF{qPI~3Ep-yKRoCrA0_{Vu`u(h4eC-@DoM8l+&FCVqZH`d>)={9hC$g2?MX5GSG$k=V}vclq%@COxt}c~44g
mjz<6xT#Vgob-Cv_NS|h>+{}y|LW4dzq+<BuP#v{*k?y~_8so<JxK_=cLxeZufnvSkrWy}%A;Fm=*5xGuP~EpBcbZw7A+ZChVN%#
6*aCjjBK#S@NOV)7T=^T#Wy$=ia=x%k?+~!BB!1BDaRs)7x17M1k*S~cVfmp)I)w@FntYe8b_Xg@q@s}({KcWkt$*1?c$_<Mj^~l
AWcAj8jOQcFa>kQ7GG-6@mmWhAU8h1&^`XqrxKiLG;z5423p2dPIc?xfJ~W>)Pin}il<5N@l<crg`opt5kC?l(gsFsRPga1=b>I;
o~gQRPF$Hf86OWYYZ<>rk=ae%*#cN64OD9wADXqe+DDsI4Q&|cqKu8gL@{L(ra4>C9N~v1NQDI^Db`Sv6~E#7=$pf;Ma|rmc2QMV
gYBAR6cBhgqvDdO=vS>;0L!8}@!V*a;9+B4uqf6N5#=RjaSYG<zxR)!@bhK=<}=pa-k<gE?(IMN_h;&!vplz-f0U94G`_N@!Q6LZ
dqT;BV%u^*C)6YQZE-Wq<Fpr<(@$Q*RUgKt>#1sYkecQ7R5^ljUKTE^&K5E^kyl35(Le8Z`yb4Dg^AC2h*Ka(mKTcY@-F<VzTY$n
<KP>P{5=J5RZ;*23$a@DPN&_rtd5Bvy6&{vR<mujETUu!@3PcEE9`910VS#blp461R)QM<DDnKcN`-K@Wk3j#vgS{&ptoWf#DvtJ
gHUo<SBB*;6RMdYg`)yOqNV_U&=`KKHU3X34?i+P-TxyhgImxR?r(wL9AACDJn5YjwFcrmpD$I-ZSTBybO#UD54XU$PPQ>23GwXe
w*L=+@V}=5NDd`g-S)dr30DV&qAK!y2)EQb9SVo&=VkTGfiqbMirCP7v>4lVW(+~kJtrQE#1i`6kt{$PhOk132Y?m&4<1x7L&TY>
&jIlAr<%HS&5dup?AArSfp1YBHa_HJbX_2m%qiMMbDVFr$-9zQ^Y?i6jz%TCv1`_M&E3{+3-=A9v%+nr{Ia}q*8AGFOHS9E8bN=R
<aBZLwSV#X!v11aD1IeEdVt(uJf|pG#Yx8YTjw9oy-w?(UH2YlU#;5bDEhjHjwclr1C*CBD^9E3K4|TG=pkskX47&U(`j~^kNc+Q
wcVE2Y`4vh<F))pw>f&WT+=t3`v;vy=fL%S*P%&Zz)%F+u7!}Lz47_oE`4;K8B8D=_llLaMr;%-><R6U_{@YrKX>s<ZyTtm?O@xn
t~P^3ledKEGzW$ax5q20R41Lg>RPJUDx-`42@H<^;S0U8<v+=RUmL85goXm~axN+N5PR>v#zE@aqqo#gbiC<Mj{Q>;IFg=hfhhub
KUaP7<@5P@i8#b14baz)KsCBQyX^rNLkj+Mb#;5vzdX9{*+<X?!z@zMB94`_sf!~JR$oh>h^gQ{m9A%G9}fXZRJl9rpWXutEPi3;
qJMdHt2(~-?GO?_a#&#=Ww%SN&L1wXF8W9300Wr;(Zir3u92V^t4Ou)`s%KKk86f*mv{HQ{^i=#WzWr9C&kg_?H6MDXMj>Us+$<Q
7OV8W9-(2_`_#X_71Qip-hIC7K`TKw6+|hV#eei}uk7pF{sm15steR3MxyN`k0ipUi!EyxpRufbpE(mC$OsCD|BGecU46d&)U&TH
QDX*m_)G6L+t7eM-T_0|Hc*^xBgeJv%Aw%AJO2erMOY;
"""
raw=zlib.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==26283
assert hashlib.sha256(raw).hexdigest()=='05f5a286918d7c6c9a7398bd8150761fc43eeec629cb773add400b52a795a16a'
Path('hex6_completion_v2.py').write_bytes(raw)
mode=sys.argv[1] if len(sys.argv)>1 else 'build'
assert mode in ('build','check')
sys.argv=['hex6_completion_v2.py',mode]
runpy.run_path('hex6_completion_v2.py',run_name='__main__')
r=Path('hex6_completion_v2.json').read_bytes()
assert len(r)==4213189
assert hashlib.sha256(r).hexdigest()=='522c3a4e4d24dd0c56ffb9f53681bf8d84b247a6c4b06a81492c0e3f749bf7fb'
```

Convenience copies, not dependencies: recovery wrapper (`recover_hex6_completion_v2.py`), complete readable source (`hex6_completion_v2.py`), exact report (`hex6_completion_v2.json`), stdout (`hex6_completion_v2.out`).
