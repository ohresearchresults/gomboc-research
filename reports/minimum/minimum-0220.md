# minimum-0220

Historical AI scientific report · saved 2026-09-24 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# HEX6_PHYSICAL_FIVE_CONTACT_INTERIOR_FILTER_V9

## 1. Main advance and its limitation

The full-rank alternative can be strengthened materially: **a positive-definite U1 component which does not approach a feasible singular metric must contain a metric with at least FIVE DISTINCT PHYSICAL vertex-based weak equilibria.** Five arbitrary zero primitives, especially harmless zeros, are not sufficient.

This replaces V8’s selected-tree vertex test by a stricter test on the actual body. At the required metric, each of the five source vertices has no positive outgoing true primitive. Its radial supporting plane exposes a genuine edge or maximal facet. The five points are actual VE or VF weak equilibria under the same pair M,N=M^-1, with VF duplication across two edges counted only once.

The strengthening is important for the concrete candidate enumeration: a cofactor ray whose selected zero arrows include harmless sources cannot, by itself, account for an isolated full-rank U1 component. Such rays may be vertices of an individual tree cone, but they are not the required minimum over the complete U1 component. The harmless constraints can be bypassed while staying in U1.

There is also a constructive consequence. If a surviving metric has exactly five such nonroot weak vertices and five independent selected zero arrows, it admits a nearby strict-escape U1 metric on the SAME actual body. If these are precisely five simple VE points and all other physical primitives are nonzero, an explicit affine metric perturbation preserves the complete strict S/U/H census while removing all five weak points. Thus a finite-distance weak110 metric of this specific kind would produce a proper110 member without moving the geometry or its volume centroid. This does not suffer from the S>=2 obstruction attached to sufficiently small rank-two lifts.

**No actual five-contact candidate has been certified as U1 in this handoff. No new numerical shape box is claimed closed for all full-rank metrics.** The attempted all-tree stress extension is not promoted into a theorem or a durable certificate. The proved advance is the physical-contact obstruction and the constructive full-rank completion test below. The whole fixed-five-cube problem remains open.

## 2. Authority, actual geometry, and conventions

The authoritative parent is

    minimum-0218
    SHA256 d2708a7da6c6867a9f47f2960251aa8600f88769bc3d919060ca8719add3a723
    HEX6_FULL_RANK_NORMAL_PORT_AND_FIVE_CONTACT_ALTERNATIVE_V8.

The literal V7 geometry and its certified145 boundary paths are retained in exactly their accepted scope. They are not reinterpreted as all true rooted trees. The current journal is the supplied `research-journal(20260924-010358).md`; the new conclusions below do not depend on a replay of V7’s numerical certificate.

Throughout, P is an actual full-dimensional uniformly filled convex body at its own volume centroid0. Its maximal facets and genuine edges are used. A physical metric is SPD M, and the polar metric is always N=M^-1 at the SAME origin. Put

    D_ij(M)=X_i^T M(X_j-X_i).

A true vertex i is strict U exactly when all its outgoing genuine edge primitives are negative. A nonroot vertex with at least one positive outgoing primitive is locally harmless for U1, even when other outgoing primitives vanish. A vertex with no positive outgoing primitive and at least one zero is treated separately below.

For any SPD M, a nonnegative true arrow has strict norm growth:

    |X_j|_M^2-|X_i|_M^2
       =2D_ij(M)+|X_j-X_i|_M^2>0.

Therefore a true weak-arrow graph with one strict sink has routes from every vertex to that sink; selected routes can be reduced to an arborescence. No singular strict-vertex-count shortcut is used.

## 3. The physical-contact minimum theorem

### 3.1 Statement

Fix the actual body P and a proposed strict unstable root r. Let Sigma be its ACTUAL uniform volume covariance, and normalize metrics by

    tr(Sigma M)=1.

Let U_r be the set of SPD metrics for which r is the unique strict unstable vertex. Other physical weak equilibria are allowed in this definition.

Consider a connected component C of U_r whose closure in the normalized PSD slice contains no singular matrix. Then C contains a metric M_* with the following properties:

1. At least five distinct nonroot true vertices are physical vertex-based weak equilibria.
2. From each such vertex choose ANY one of its zero outgoing true edges. The resulting arrow forms, restricted to tr(Sigma H)=0, span the full five-dimensional tangent space.
3. In particular, five of those arrows, with five distinct source vertices, are independent and determine the ray of M_* by their five homogeneous zero equations.

The theorem concerns the whole U1 component, not a component cut out by a selected tree or by an additional stable-facet condition.

### 3.2 Why the component has a minimum

For each rooted true tree T, its normalized feasible set is

    K_T={M PSD: tr(Sigma M)=1,
                    D_e(M)>=0 for every e in T}.

There are finitely many trees. Their union is closed in the normalized PSD slice. On its SPD part, membership is equivalent to unique strict U at r: the selected arrows strictly increase norm toward r, and hence r is strictly farther than every other vertex and is itself strict U.

A component whose closure avoids the singular boundary is therefore compact and consists entirely of SPD matrices. The continuous function

    F(M)=log det(Sigma^(1/2) M Sigma^(1/2))

attains a minimum at some M_* in that component. Sigma is fixed here because the actual body is fixed. It is a normalization tensor derived from that body, not a replacement physical metric or a freely selectable covariance.

### 3.3 Harmless zeros do not constrain this minimum

Define

    Z(M_*)={i!=r: max_{j adjacent to i} D_ij(M_*)=0}.

Every other nonroot vertex has a strictly positive true escape. The root’s outgoing primitives are strictly negative.

For each i in Z choose one true neighbor j_i with D_i,j_i(M_*)=0. Suppose there were a nonzero symmetric H satisfying

    tr(Sigma H)=0,
    D_i,j_i(H)=0 for every i in Z.

For all sufficiently small positive and negative t, M_*+tH remains SPD. Every vertex in Z retains its chosen zero escape. Every other nonroot retains a strictly positive escape, and the strict root remains strict. Thus the entire small two-sided segment lies in U_r, and, being connected to M_*, lies in the same component C.

But log determinant is strictly concave on a nonconstant SPD line:

    d^2/dt^2 log det(M_*+tH)
       =-tr[((M_*+tH)^-1 H)^2]<0.

Consequently at least one of the two nearby endpoints has smaller F than M_*. This contradicts its minimality.

The selected forms must therefore have rank five on the trace-normalized tangent space. There must be at least five distinct source vertices in Z. This proof works for EVERY choice of one zero edge per source. It does not count a second zero at the same vertex as an additional source constraint.

This is the improvement over a vertex of one selected-tree polytope. At such a polytope vertex, a zero selected arrow can be harmless because its source has another positive escape. In the COMPLETE U1 set that constraint can be discarded locally. Only vertices in Z are needed to keep the two-sided perturbation in U1.

## 4. These are genuine physical VE/VF points under M and M^-1

The word “physical” in the theorem has a direct proof.

Let i belong to Z, and let n_i=X_i^T M_*X_i>0. Since every incident edge has nonpositive primitive, the linear functional

    X -> X_i^T M_*X

is maximized over the entire convex body at X_i. This follows because the actual tangent cone at X_i is generated by its genuine incident edge directions. Its normalized supporting covector is

    q_i^*=M_*X_i/n_i.

At least one incident edge has zero primitive, so the exposed face of q_i^* contains that edge. In three dimensions it is a genuine edge or a maximal facet. It cannot be the whole body.

If the exposed face is exactly the edge i--j, let f,g be its two genuine incident facets. Their actual poles satisfy

    q_i^*=alpha q_f+(1-alpha)q_g,
    0<alpha<1.

Since N_*=M_*^-1 and N_*q_i^*=X_i/n_i,

    q_i^{*T}N_*(q_g-q_f)=0.

Therefore the four edge primitives have signs

    D_ij=0,
    D_ji=-|X_j-X_i|_M^2<0,
    D^polar_fg=-(1-alpha)|q_g-q_f|_N^2<0,
    D^polar_gf=-alpha|q_g-q_f|_N^2<0.

This is one actual VE equilibrium, not a harmless zero.

If q_i^* is an actual facet pole, its exposed face is that maximal facet. The radial foot is X_i, a true vertex of the facet. The two incident boundary edges at X_i have the corresponding VF packets. They represent ONE physical point at X_i, not two weak equilibria. A source cannot have three independent zero edge directions: all zero directions lie in that supporting plane, and a true polygon has only two incident boundary edges at a vertex.

Thus the minimum in section3 has at least five distinct physical vertex-based weak equilibria. Additional EF points elsewhere may exist; they are irrelevant to the count and are not silently assumed absent.

This physical interpretation uses the actual poles and the reciprocal N_*. It is not obtained by independently choosing a polar metric.

## 5. Exact full-rank alternative after the new filter

At a fixed actual body, precisely one of the following alternatives must account for any nonempty root-r U1 set:

**Singular-boundary alternative.** Some component approaches a rank-two PSD matrix admitting a TRUE weak rooted tree at r.

**Interior alternative.** Some SPD cofactor metric determined by five zero true arrows has at least five distinct physical nonroot vertex rests and is itself U1 at r.

Rank one cannot occur in the first alternative. For a rank-one form vv^T, the positive and negative extrema of v·X are both nonempty because0 is interior. Each gives a closed exposed set in the weak-arrow graph. No single root can be reached from both. At a singular limit, choose a subsequence with the same selected true tree; all its weak inequalities persist. The limit cannot be zero under the covariance normalization, so it has rank two.

The straight segment from that limit to an SPD member of the same tree cone gives a weak SPD lift. A strict lift requires strict inequalities on the selected zero arrows, as in the separately settled lift alternative; it is not asserted automatically for a merely weak component.

The practical distinction from V8 is exact:

> A five-zero-arrow ray at which fewer than five nonroot vertices have no positive escape is NOT sufficient to represent a component confined to the SPD interior.

It may still be a feasible metric, or a vertex of an individual tree cone. The theorem says that a wholly interior U1 component must contain a different metric passing the physical-source filter.

No inference is made that all components on the present atlas avoid the singular boundary, or that the remaining singular kernels lie in the already excluded V7 chamber.

## 6. The concrete candidate test on the literal atlas

The following is a complete algebraic specification, not a reported executed census.

For the actual star-centred vertices write

    U_i=Y_i-A, d_i=1+c·U_i,
    Z_i=d_i A+U_i,
    E_ij=d_i U_j-d_j U_i.

The positive-denominator-cleared primitive is

    Z_i^T M E_ij=d_i^2 d_j D_ij(M).

In coordinates m=(M11,M22,M33,M12,M13,M23), its row is

    (Z1 E1, Z2 E2, Z3 E3,
     Z1 E2+Z2 E1,
     Z1 E3+Z3 E1,
     Z2 E3+Z3 E2).

Choose five distinct nonroot sources and one genuine outgoing edge from each. A directed cycle can be rejected immediately, since its zero arrows would still have strict SPD norm growth. Form the5-by6 coefficient matrix C. Set

    m_j=(-1)^j det(C with column j deleted), j=0,...,5.

If all cofactors vanish, these equations do not define an isolated full-rank metric ray. This is not a geometry exclusion. Otherwise form

    M_C=((m0,m3,m4),(m3,m1,m5),(m4,m5,m2)).

Test both signs for SPD; at most one succeeds. For the successful sign, the strengthened candidate test is:

    D_i,k(M_C)<=0 for EVERY genuine neighbor k
    at EACH of the five selected source vertices.

Equivalently, by the actual tangent-cone argument, one may test all other vertices k, including nonneighbors. The selected zero then belongs to a true supporting face. A positive alternative escape at even one of these selected sources makes this set of five unsuitable for the physical-critical test.

Next test the COMPLETE true graph. An SPD candidate with only r strictly unstable is U1 at r; the graph’s acyclicity supplies reachability. For continuation it is preferable also to record explicit routes, all physical packets and the actual same-metric polar census.

The previous upper counts remain upper counts:36288 candidate sets for root0,106596 five-source sets over all roots before rejection and deduplication. They are not reannounced as executed coverage.

Two further exact filters are useful:

* If all five independent zero edges lie in one actual facet F, then q_F q_F^T annihilates all five rows. Their one-dimensional kernel is the singular ray q_F q_F^T, not an SPD ray. In particular, five independent zeros wholly on the heptagonal base cannot produce the required interior candidate.
* If a candidate has a VF source, both of its genuine incident zero edges must be tested physically. The minimum theorem requires rank five for every one-edge-per-source choice. Merely adding two VF packets to reach a count of five is invalid.

The coefficients above have degree at most two in c after clearing the positive denominators, and the metric cofactors have degree at most ten. All signs are to be evaluated at the SAME actual centroid root. A rank-deficient cofactor system, an indefinite ray and a ray failing physical support are different outcomes and must remain distinct in the report.

## 7. Constructive full-rank escape from an admissible five-contact metric

Suppose an actual candidate M0 is SPD and U1 at r. Assume there are exactly five nonroot vertices without a positive escape, and select one zero true arrow from each. Suppose those five forms are independent on

    tr(Sigma H)=0.

The six-by-six linear system

    tr(Sigma H)=0,
    D_e(H)=1 for the five selected arrows

has a unique symmetric solution H. Set

    M_epsilon=M0+epsilon H,
    N_epsilon=M_epsilon^-1.

For every sufficiently small epsilon>0, the five selected escapes equal epsilon. The other nonroot vertices retain their positive escapes, and the root retains all its negative primitives. Hence this is a genuine strict-escape U1 family on the SAME actual body, with unchanged uniform centroid and true lattice.

This conclusion still holds when one of the five vertices is VF: making one genuine exit positive removes its obstruction to vertex-U1. However, no preservation of S/H is inferred in that mixed case, because other zero primal or polar primitives can change sign.

### 7.1 Complete weak-free U1, without an S1 assertion

Once every nonroot has a strict escape and the root is strict, U1 is open in the six-dimensional SPD space. Every genuine primal primitive is a nonzero linear polynomial in M. After multiplication by det M>0, every genuine polar primitive is a nonzero polynomial of degree at most two in M. Neither can vanish identically on an open SPD set.

Therefore a sufficiently small further metric perturbation avoids all primitive-zero hypersurfaces while retaining U1. It gives an actual weak-free U1 member. This is an existence consequence for a candidate that passes the stated tests; no such candidate has been supplied here.

The reciprocal metric is not independently adjusted. Generic avoidance refers to M and its induced inverse only.

### 7.2 A complete interval preserving S/U/H in the five-simple-VE case

There is a stronger constructive statement with explicit bounds. Assume the only zero primitives at M0 are the five selected primal arrows, each forming a simple VE packet, and all other63 true-edge primitives are nonzero.

Let

    d=det M0>0, t=tr M0,
    K=sum_{a,b}|H_ab|>0.

Since lambda_min(M0)>=4d/t^2 and ||H||op<=K, the bound

    epsilon<=d/(t^2 K)

keeps M_epsilon strictly positive definite.

For every other directed primal edge write

    D_e(M_epsilon)=a_e+epsilon b_e,
    a_e!=0.

For every directed true polar edge f→g write

    P_fg(epsilon)
       =q_f^T adj(M0+epsilon H)(q_g-q_f)
       =a_fg+epsilon b_fg+epsilon^2 c_fg,
    a_fg!=0.

The physical polar primitive is P_fg/det M_epsilon, with a positive denominator. Define epsilon_* as the minimum of

    1,
    d/(t^2 K),
    |a_e|/(2|b_e|) for every nonzero b_e,
    |a_fg|/[2(|b_fg|+|c_fg|)] whenever the denominator is nonzero.

This is a positive exact number determined by the actual body and candidate. For EVERY0<epsilon<=epsilon_*, all63 old nonzero signs are preserved and all five selected primal zeros become positive. No physical weak packet remains. The strict S/U/H census is unchanged.

Consequently:

> An actual finite-distance weak110 candidate with exactly these five independent simple VE points, no other zero primitives, and one reciprocal metric produces a proper110 body by this explicit metric interval, without any shape or centroid change.

This does not claim such a candidate exists. It identifies a legitimate finite-distance route which the rank-two-tail S>=2 theorem does not rule out.

## 8. A cut-boundary consequence, with the PSD premise kept explicit

The component theorem is the new interior result. The following companion observation records precisely how the supplied boundary information may delimit the remaining geometry. It is not a substitute for an interior exclusion.

Every face of the CLOSED source five-cube has at most nine true vertices. At x=1 or u=1 a cap vertex merges with A; at y=1,z=1,v=1 it merges with a retained base vertex. At x=0, Y5=B0 and Y6,Y7 lie on retained source edges; at y=0 or z=0 analogous redundant points appear. At u=0, Y9 lies on the retained segment B3B4; at v=0, Y8 lies on B3A. Intersections of cube faces do not restore a lost true vertex.

The common retained tetrahedron conv(A,B1,B2,B4), together with the accepted positive-actual-denominator compactification, keeps these limiting bodies full-dimensional. The actual centred vertex map extends continuously to the closed cube. Removed virtual-vertex horizons are unrelated: they can occur at interior cut parameters without reducing the actual vertex count.

### 8.1 U1-only version requires the stronger PSD theorem

Using the current notebook’s recorded nonzero-PSD obstruction for centred homogeneous bodies with at most nine true vertices, no boundary body admits a true weak rooted system under any nonzero PSD metric. This use requires that stronger PSD statement. It does NOT follow merely from the older SPD inequality V>=10.

Contained or duplicated labels cannot evade the obstruction. For rank two, a strict radial-maximum shadow corner exposes a fibre with every arrow to a different projected point strictly negative; for rank one, the two scalar extremal fibres do the same. For SPD, strict unstable vertices give the corresponding closed singleton sets. Refinement labels inside the limiting body cannot connect two such closed sets to a common root.

Let Psi(q,M) be the maximum, over all roots and all true rooted trees of the fixed labelled graph, of the minimum selected primitive. On the closed-cube boundary and tr M=1, M PSD, it is continuous and strictly negative. Thus

    gamma=-max Psi(q,M)>0

on that compact set. This defines an exact positive separation, but its numerical value has not been evaluated here.

The accepted actual bound ||X_i||<=18 gives, for an actual same-graph perturbation with maximum vertex displacement e,

    |D_ij(new)-D_ij(old)|<=72e+2e^2

when tr M=1. Therefore the actual-coordinate collar

    e<=min(1,gamma/148)

is excluded from every weak rooted tree for every nonzero PSD metric. Uniform continuity converts it into some positive source-cut collar around all ten faces of the five-cube. Its width is not reported numerically.

Accordingly, under the explicitly stated PSD premise, any U1 member of the fixed-pole atlas must remain away from genuine cut-degeneration faces, independently of its metric conditioning. This is a source-incidence boundary statement, not a claim that the full cube has been exhausted.

### 8.2 Joint S1/U1 does not need that PSD strengthening

There is a separate joint version using only the accepted SPD V>=10 theorem and the common-metric compactness bound. The atlas has uniform inner/outer bounds, and simultaneous strict S1/U1 has the accepted finite condition-number envelope under the SAME inverse pair. After metric normalization, a boundary sequence of joint S1/U1 systems therefore has a positive-definite limit, not a singular one.

The limiting body has at most nine true vertices, so its two strict unstable vertices prevent a single rooted system, even with the old labels retained. Hence joint S1/U1, and therefore proper110, also stays away from the source-cube boundary.

This paragraph does not assert that U1 alone has a nonsingular metric envelope. It also does not determine a new numerical collar width or reject any positive-definite interior component.

## 9. Complete literal actual-centroid reconstruction

The unchanged geometry needed to apply the new tests is repeated here; no earlier sandbox object is required to define it.

    p=(1/100000)*(
      (60401,-32565),(80000,-20000),(0,60000),
      (-80000,80000),(-483861,-325040),(-447814,-355009));
    A=(0,0,1), q_i=(p_i,1);
    b=(2615613/500000,816129/250000,-3);
    B_i=[q_i;q_(i+1 mod6);b]^-1(1,1,1).

For0<x,y,z,u,v<1,

    Y0=A;
    Y1=B1; Y2=B2; Y3=B4; Y4=B5;
    Y5=B0+x(A-B0);
    Y6=B0+y(B5-B0);
    Y7=B0+z(B1-B0);
    Y8=B3+u(A-B3);
    Y9=B3+v(B4-B3).

True maximal facet cycles:

    (0,4,6,5), (0,5,7,1), (0,1,2), (0,2,8),
    (0,8,9,3), (0,3,4), (4,3,9,2,1,7,6),
    (5,6,7), (9,8,2).

True edges:

    01,02,03,04,05,08,12,17,28,29,34,39,46,56,57,67,89.

Set U_i=Y_i-A and d_i=1+c·U_i. The positive apex-fan triples are

    (4,3,9),(4,9,2),(4,2,1),(4,1,7),
    (4,7,6),(5,6,7),(9,8,2).

For T={i,j,k}, put

    a_T=det(U_i,U_j,U_k)/6,
    W=product_(i=1)^9 d_i,
    Z=sum_T a_T product_(l notin {0,i,j,k}) d_l.

Select the unique root with all ACTUAL d_i>0 of

    Z_x W-Z W_x=0,
    Z_y W-Z W_y=0,
    Z_z W-Z W_z-4ZW=0.

Then X_i=A+U_i/d_i is the uniformly refilled own-centred body, with volume Z/W. The first and second moments for the covariance normalization use the genuine positive tetrahedra, each with vertices A,X_i,X_j,X_k and volume a_T/(d_i d_j d_k). For a tetrahedron with vertex sum S,

    mean X=S/4,
    mean XX^T=(SS^T+sum_vertices XX^T)/20.

Every facet pole is obtained from its actual maximal plane at this same origin. For a raw support n·Y<=h, its pole after the star map is

    q_actual=[n+(h-n·A)c]/[h+(h-n·A)c·A].

The support denominator is positive on the actual centred body. Virtual denominators at removed B0 or B3 need not be positive.

These formulas specify all coordinates, moments, five-contact cofactor matrices, exact perturbations, and reciprocal physical signs in sections3–7. They do not supply a new successful contact selection.

## 10. What was tried, what is durable, and what remains

I investigated extending the existing three-dimensional stresses from silhouette paths to all genuine rooted trees at a genuinely unequal completion. That work is not delivered as a complete exact all-tree cover with an autonomous verified successor certificate. No new row count, coverage percentage, numerical absence of U1, or source-only replay claim from that exploration enters this result. It is not a durable replacement for V7.

The durable new result is analytical: minimizing log determinant over the COMPLETE U1 component forces five distinct physical vertex rests, not five arbitrary selected zeros. This substantially strengthens the candidate filter while explicitly preserving the possible singular alternative. The full-rank perturbation then explains how an admissible five-contact metric can produce a real strict-escape U1 member, and under the stated simple-VE hypotheses can preserve the complete strict census and remove all weak points.

No code materially establishes these new claims, so there is no new computational object, hash pin, observed terminal marker, or omitted certificate array being asserted. The determinant construction, actual-centroid selector and metric-interval formulas are given completely above. The existing V7 autonomous source and controls remain unchanged.

The most useful unresolved calculation is now concrete: evaluate the physical-filtered cofactor rays on an actual unequal body or a rigorously enclosed shape cell. Rejecting a harmless selected zero is legitimate; rejecting a rank-deficient stratum as infeasible is not. A surviving U1 ray with exactly five independent physical weak sources is already sufficient for the constructive strict-U1 step. A successful same-metric110 conclusion still requires the full actual polar and weak-packet census, and may not be inferred from the primal contact calculation alone.
