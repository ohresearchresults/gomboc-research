# minimum-0218

AI research report · 2026-09-24 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# HEX6_FULL_RANK_NORMAL_PORT_AND_FIVE_CONTACT_ALTERNATIVE_V8

## 1. Result and precise status

I obtained two constraints on the FULL-RANK problem, rather than another rank-two kernel box.

**First, a full-rank base-normal descent theorem turns the accepted V7 obstruction into a forest-free routing condition under the SAME physical inverse metric.** On the V7 cylinder, whenever the actual base-normal foot direction belongs to the excluded cap-sign chamber, every actual U1 system must use a weak escape whose positive base-height contribution is essential. Such escapes can originate only at the two nonapical cap vertices5 and8. There is an explicit mixed primal/inverse upper bound on each essential escape.

In a virtual-horizon sector this becomes a particularly restrictive whole-metric statement: **one cap vertex is the only possible source of an essential escape.** Its allowed outgoing edge or edges are determined by the sign of its actual height relative to the centroid. Every other outgoing edge at that vertex is strictly negative. This is a statement about the complete true weak-arrow graph, not a selected convenient tree.

The resulting portal-versus-normal-radius inequality excludes an entire full-rank normal-height fibre when an explicit scalar inequality fails. A two-by-two negative-semidefinite test, equivalently an explicit adjugate quadratic in the actual base foot, excludes every tangent metric and every positive normal height at that foot. The hypotheses and all equality cases are stated below. I have not evaluated this last geometric footprint test over a new closed cut box, so it is not reported as a newly certified numerical shape-domain exclusion.

**Second, there is an exact finite-contact alternative for full-rank U1 components which avoid rank-two feasibility.** At a fixed actual body, such a component necessarily contains an SPD metric determined by FIVE independent zero-arrow equations at five distinct true source vertices. For the literal graph, there are at most36288 candidate five-arrow sets at root0, or106596 sets when all roots are considered together, before elementary rejection and deduplication. These are finite metric candidates determined by the actual geometry, not independently chosen moments.

Thus a full-rank U1 system on a V7 body must lead either to a genuine rank-two rooted system outside the already excluded kernel domains, or to one of these finite actual five-zero-arrow metric rays. This identifies the missing interior-metric alternative explicitly; it does not assume that every U1 component approaches a singular metric.

**No new actual U1 or110 member has been constructed, and the entire V7 cylinder is not newly excluded for arbitrary full-rank metrics.** No global bound, canonical count, or attaining example changes. The new results are analytic; no new computational coverage count, body census, or execution receipt is claimed.

## 2. Exact authority and retained actual model

The scientific parent is

    minimum-0213
    SHA256 eef7fc03921fc710f376ec0ed821855e6e406e4ccad2801e31738c4cef2b73e6
    HEX6_FULL_APICAL_CUT_HALF_BASE_STRIP_AND_ALL_KERNEL_CAP_CHAMBER_V7.

The current journal update and literal parent are retained as supplied authority. The parent’s completed interval certificate is not replayed or enlarged by assertion here. In particular, its145 boundary paths are not treated as all true rooted spanning trees.

For self-contained continuation, the unchanged literal source model is

    p=(1/100000)*(
       (60401,-32565),(80000,-20000),(0,60000),
       (-80000,80000),(-483861,-325040),(-447814,-355009));
    A=(0,0,1), qi=(pi,1);
    b=(2615613/500000,816129/250000,-3);
    Bi=[qi;q(i+1 mod6);b]^-1(1,1,1).

For source fractions x,y,z,u,v in the open five-cube,

    Y0=A; Y1=B1; Y2=B2; Y3=B4; Y4=B5;
    Y5=B0+x(A-B0);
    Y6=B0+y(B5-B0);
    Y7=B0+z(B1-B0);
    Y8=B3+u(A-B3);
    Y9=B3+v(B4-B3).

The true maximal facet cycles are

    F0=(0,4,6,5), F1=(0,5,7,1), F2=(0,1,2),
    F3=(0,2,8), F4=(0,8,9,3), F5=(0,3,4),
    F6=(4,3,9,2,1,7,6), F7=(5,6,7), F8=(9,8,2).

The17 true edges are

    01,02,03,04,05,08,12,17,28,29,34,39,46,56,57,67,89.

In particular the only vertices outside F6 are0,5,8, and5--8 is NOT an edge.

Set Ui=Yi-A and di=1+c·Ui. The actual vertices are

    Xi=A+Ui/di,

where c is the unique positive-ACTUAL-denominator star parameter giving the newly uniformly filled body centroid0. The actual positive apex-fan triples are

    (4,3,9),(4,9,2),(4,2,1),(4,1,7),(4,7,6),(5,6,7),(9,8,2).

Their volumes are det(Ui,Uj,Uk)/(6di dj dk), and their actual centroids are (A+Xi+Xj+Xk)/4. These determine the same actual volume and first moment used everywhere below. No transformed old centroid, free cap mass, or uniform planar shadow is substituted.

Equivalently, put

    W(c)=product(i=1,...,9) di,
    Z(c)=sum_T [det(Ui,Uj,Uk)/6] product(l notin {0,i,j,k}) dl.

The actual c is the unique positive-domain root of

    Z_x W-Z W_x=0,
    Z_y W-Z W_y=0,
    Z_z W-Z W_z-4ZW=0,

where these derivatives are with respect to c. Rational fractions specify an exact algebraic body, not necessarily rational coordinates.

The V7 cylinder used when invoking its mechanical theorem is exactly

    x in[3/4,17/20], y in[13/20,3/4], z in[1/200,1/10],
    0<u<1, 0<v<=1/2.

All actual members remain10/17/9. Closed-cube merged-incidence limits are not counted as witnesses.

## 3. A full-rank descent that preserves the actual reference and base foot

This section is valid for any fixed convex body at its specified interior reference. For mechanics below that reference is its actual uniform centroid.

Let B be a true facet with actual pole q, so q·Xi=1 on B. Let M be SPD, N=M^-1, and define

    hi=q·Xi,
    s=q^T N q>0,
    Mbar=M-qq^T/s.

Then Mbar is PSD of rank two, with kernel span(Nq). This follows directly from

    (q·v)^2 <= (v^T Mv)(q^T Nq),

with equality precisely for v proportional to Nq.

For every TRUE directed edge e=(i,j), put

    De(M)=Xi^T M(Xj-Xi),
    beta_e=hi(hj-hi).

The exact identity is

    De(Mbar)=De(M)-beta_e/s.                         (3.1)

No vertex, facet, density or centroid changes. The matrix Mbar is only a singular limiting quadratic form; it has no inverse physical metric.

For the full-rank path

    M(t)=M-tqq^T,  0<=t<1/s,

Sherman-Morrison gives the ONE reciprocal matrix

    N(t)=N+[t/(1-ts)]Nq q^T N.

The physical foot of B is fixed throughout:

    N(t)q/[q^T N(t)q]=Nq/s.

Every polar primitive originating at B is multiplied by the same positive factor1/(1-ts). Hence strict stability, closed-foot membership, or failure of B’s root fan is preserved exactly along this descent. No such preservation is asserted for other stable facets, saddles or physical weak contacts.

### A necessary cutset of essential height-supported arrows

Suppose M has unique strict U at root r, allowing other physical weak equilibria for the moment. Then every nonroot has a true weak escape, and any choice of one such escape per nonroot is an arborescence toward r: positive-definite norm growth forbids cycles.

Suppose Mbar is known to admit NO true weak rooted tree at r. Define the directed set

    W_B(M)={e=(i,j): i!=r,
             beta_e>0 and 0<=s De(M)<beta_e}.        (3.2)

**Every true weak arborescence of M toward r intersects W_B(M).** Indeed, if a tree avoided it, each selected edge would remain nonnegative in (3.1): beta<=0 only improves an arrow, and beta>0 outside W has sD>=beta.

This has a forest-free form. Remove W_B(M) from the actual weak-arrow graph of M. Some nonempty vertex set T, not containing r, then cannot reach r. Every weak true edge leaving T belongs to W_B(M). All its other genuine outgoing edges are strictly negative. The set is determined by actual graph reachability; it is not an assumed selected forest.

The strict inequality in (3.2) is essential. An edge with sD=beta remains zero after descent and does not obstruct weak rootedness at Mbar.

## 4. Applying the descent to the whole V7 cylinder

Take B=F6, q=q6, and root r=0. The normal kernel is oriented by

    k=-Nq.

Since q·k=-s<0, the base sign is automatic. The actual inverse-metric conditions

    q0^T Nq<0, q1^T Nq>0,
    q2^T Nq<0, q3^T Nq<0,
    q4^T Nq<0, q5^T Nq<0,
    q8^T Nq<=0                                      (4.1)

put Mbar precisely in V7’s excluded cap-sign chamber. No condition on q7^T Nq is imposed. These are homogeneous linear inequalities in the SAME N=M^-1, not independently feasible polar conditions.

Consequently (3.2) is necessary for every full-rank root0-U1 system satisfying (4.1), at arbitrary scale and conditioning. This is not restricted to metrics close to Mbar.

All base vertices have hi=1, and every vertex outside the base has hi<1. Thus a directed edge from a base vertex to another base vertex has beta=0, while an edge from a base vertex to an outside vertex has beta<0. Since the root0 has no selected outgoing edge, the ONLY possible sources of essential arrows in (3.2) are vertices5 and8.

Therefore:

> Every full-rank root0-U1 system on the V7 cylinder satisfying (4.1) has a genuine nonroot cutset whose weak exits are essential height-supported arrows originating at5 or8. For each such exit,
>
>     0<= (q^T Nq) Xi^T M(Xj-Xi) < (q·Xi) q·(Xj-Xi).

This is a mixed primal/inverse restriction on a full-rank physical metric. It does not follow from merely knowing that a rank-two metric is infeasible: the exact rank-one descent and the signs of every true edge are what make it valid.

The inverse-metric cone in (4.1) is not intrinsically a small perturbation domain. Given any admissible direction k in the parent’s chamber, put p=-k/[q·(-k)], so q·p=1. For every delta>0,

    N_delta=pp^T+delta[I-qq^T/(q·q)],
    M_delta=qq^T+delta^-1(I-qp^T)(I-pq^T)

are mutually inverse SPD matrices with N_delta q=p. Thus the same normal-foot condition can be maintained along an entire full-rank family. This observation is a construction of admissible metric coordinates, not a new U1 or full-census claim for those matrices.

## 5. A new actual-geometry fact: the two virtual horizons cannot both be crossed

Let

    d_Bi=1+c·(Bi-A)

be the virtual denominator. The source base hexagon is strictly convex in cyclic order B0,...,B5. Its chords B0B3 and B1B4 cross at a point R in their relative interiors. Hence

    R=(1-lambda)B0+lambda B3=(1-mu)B1+mu B4,
    0<lambda,mu<1.

The vertices B1 and B4 are retained ACTUAL source vertices. Their projective denominators are positive. Affinity therefore gives

    (1-lambda)d_B0+lambda d_B3
      =(1-mu)d_B1+mu d_B4>0.                        (5.1)

In particular, d_B0 and d_B3 cannot both be nonpositive. No boundedness assumption on either released virtual pyramid was used.

This identity is fully reconstructible from the literal data. For example lambda is the ratio of two planar cross products obtained by solving the intersection of B0B3 and B1B4 in their x,y coordinates; the base plane has nonzero z coefficient, so that projection is nonsingular. Its sign bounds follow from strict convexity, not a numerical locator.

Put H0=1+4c_z and a=q·A. The actual base pole and heights obey

    q=(b+4c)/H0,
    a=1-4/H0,   -3<a<0,

    h5-a=4(1-x)d_B0/(H0 d5),
    h8-a=4(1-u)d_B3/(H0 d8).                       (5.2)

The accepted atlas bounds give H0>0 and -3<a<0. The two last identities also follow directly by transforming the base support. Thus at most one of vertices5 and8 can lie at or beyond A in the negative base-normal direction.

This is a geometric statement on the entire actual open five-cube. It is not an assertion that both horizon sectors intersect every previously certified subcylinder.

## 6. Horizon sector: a forced sole exit and a finite normal-height obstruction

Assume the body is in the V7 cylinder, (4.1) holds, and

    d_B3<=0.

Then (5.1)–(5.2) give

    h8<=a<0,  a<h5<1.

All three normal coefficients for exits from8 are nonpositive:

    beta_80=h8(a-h8)<=0,
    beta_82=beta_89=h8(1-h8)<0.

There are now positive normal coefficients at only ONE possible source, vertex5.

### 6.1 Complete direction switch at vertex5

If a<h5<0, the only positive normal coefficient is

    beta_50=h5(a-h5)>0.

Every true weak tree would have to use5→0. More strongly, EVERY weak outgoing edge at5 can be extended to a true weak arborescence, since the whole weak graph is acyclic and all vertices reach0. Therefore a root0-U1 system necessarily satisfies

    D56<0, D57<0,
    0<=s D50<h5(a-h5).                              (6.1)

So5→0 is the only possible weak exit at5 in the COMPLETE graph. This is not a forced edge merely in one chosen certificate tree.

If h5=0, no nonroot true edge has a positive normal coefficient. The descent preserves every selected weak arrow, contradicting V7. **Root0-U1 is impossible in this height-zero case under the stated normal-foot conditions.** No claim of a numerically established nonempty height-zero slice of the V7 cylinder is made.

If 0<h5<1, the only positive normal coefficients are beta_56=beta_57=h5(1-h5). Then root0-U1 requires

    D50<0,
    at least one of D56,D57 is nonnegative,
    every nonnegative one satisfies sD5j<h5(1-h5).    (6.2)

Thus the actual sign of the cap height determines whether its only permitted route is directly toward A or back into the base.

For d_B0<=0 the reflected statement holds with5 and8 interchanged: the possible positive exits are8→0 when a<h8<0, or8→2/9 when0<h8<1. The actual neighbor sets remain those of the literal graph; they are not relabelled as a graph symmetry.

### 6.2 An entire full-rank fibre, not only a singular endpoint

The following formulas apply in the strict sector h8<a and a<h5<0. Fix an actual base foot direction p with q·p=1 satisfying the signs (4.1), and let K be any PSD rank-two matrix with kernel span(p). Every

    M_tau=K+tau qq^T, tau>0,

is SPD. Its inverse obeys N_tau q=p/tau, hence s=1/tau, and its maximal base-normal descent is exactly K.

Define

    beta=h5(a-h5)>0,
    kappa=h8^2-a^2>0,
    d=X5^T K(A-X5),
    Delta=A^T K A-X8^T K X8.

Equation (6.1), together with the compulsory unique-global-radius property of a sole U, gives the necessary conditions

    d<0, Delta>0,
    -d/beta <=tau<Delta/kappa,
    beta Delta+kappa d>0.                            (6.3)

Failure of ANY of these conditions excludes root0-U1 for the ENTIRE positive normal-height fibre. The last inequality compares the normal height needed to activate the sole cap exit with the height at which the overhanging vertex8 becomes at least as far as A.

For strict-escape U1, the lower inequality in (6.3) is strict. At equality D50=0 while D56,D57<0: the supporting radial plane at5 exposes exactly the true edge50. This is a genuine simple vertex-edge weak equilibrium, not a harmless zero. Thus proper110 cannot attain the lower endpoint. The upper endpoint is always excluded even from weak-tree U1, because distinct vertices0 and8 have equal norm there.

At the exact horizon h8=a, kappa=0. The correct conclusion is Delta>0 and the lower activation bound; no finite upper bound is obtained from vertex8. This finite weak boundary is not discarded.

### 6.3 A geometric footprint test eliminating all tangent metrics

In the strict sector above put

    J=beta(AA^T-X8X8^T)
       +kappa sym[X5(A-X5)^T].

The last expression in (6.3) is J:K. For a fixed p, all K with kernel p are excluded whenever the restriction of J to p-perp is negative semidefinite.

The three vectors A,X5,X8 are independent in the actual open atlas. In that vector basis J has coefficient matrix

    S=((beta,kappa/2,0),
       (kappa/2,-kappa,0),
       (0,0,-beta)).

Its inertia is (+,--). Therefore the negative-semidefinite restriction condition is equivalent to the single exact quadratic inequality

    p^T adj(J)p>=0.                                  (6.4)

Indeed, every two-plane intersects J’s two-dimensional negative subspace, while the determinant of the restriction, up to a positive factor, is p^T adj(J)p. Thus a nonnegative determinant forces both restricted eigenvalues to be nonpositive. Equality is included.

For an entirely literal formula, write p=w0 A+w5 X5+w8 X8. Condition (6.4) has the sign of

    beta*kappa*w0^2 + beta*kappa*w0*w5
       -beta^2*w5^2-kappa*(beta+kappa/4)*w8^2 >=0,

with the actual foot-plane equation

    a*w0+h5*w5+h8*w8=1.

This supplies a whole-footpoint, all-tangent-metric, all-positive-normal-height exclusion criterion under the stated actual shape and normal-foot hypotheses. Its intersection with a particular numerical cut region has not been computed here. In particular I do not report an unverified positive-volume footprint subdomain or a new all-metric closure of the cylinder.

## 7. Full-rank components away from the singular boundary: a finite-contact theorem

The preceding descent is useful but may fail because essential normal ports are present. There is a separate exact alternative which handles components that avoid ALL rank-two feasibility, not merely the base-normal direction.

### Theorem: five-zero-arrow alternative

Fix any actual full-dimensional own-centred polytope P and a root r. If an SPD metric realizes a true weak rooted tree at r, then at least one of the following occurs on the SAME actual body:

1. A rank-two PSD metric realizes a true weak rooted tree, and that tree has an SPD weak lift.
2. An SPD metric realizing a true weak rooted tree is determined, up to positive scale, by FIVE independent zero-arrow equations at five distinct nonroot source vertices.

The second metric need not equal the initially given metric. It has exactly one strict U at r, but may have additional physical weak equilibria. Five zero edge primitives are not automatically five physical weak points.

### Proof

Choose a weak rooted tree T for the given metric and normalize trace M=1. Consider

    K_T={M PSD: tr M=1, D_e(M)>=0 for every e in T}.

It is compact and convex and contains a positive-definite point.

No rank-one point belongs to K_T. For M=vv^T, the actual interior origin gives both positive and negative values among v·Xi. The positive-maximum and negative-minimum exposed vertex sets are disjoint closed sets of the weak-arrow graph. No one root can be reached from both.

If K_T contains a singular point M0, it consequently has rank two. The difference between the original positive-definite point and M0 supplies a weak SPD lift: it is positive on the kernel and nonnegative on each selected zero arrow. Small straight segments preserve the other positive rows. This is the first alternative; it retains true rooted reachability, not singular strict-U counts.

Otherwise every point of K_T is SPD. Define the affine polyhedron

    P_T={symmetric M: tr M=1, D_e(M)>=0 for e in T}.

It equals K_T. If P_T contained a non-SPD matrix, the segment from its SPD point would first meet a nonzero singular PSD matrix of trace1, contradicting the preceding assumption. Hence P_T is a compact polytope entirely inside the SPD cone.

At any vertex of this five-dimensional affine polyhedron, at least five active arrow equations are independent. If their rank were below five, a nonzero trace-zero symmetric perturbation would preserve them, preserve all inactive inequalities for sufficiently small perturbations of either sign, and remain SPD. The point would not be a vertex.

Select five independent active equations. Their source vertices are distinct because they belong to a rooted tree. Their homogeneous kernel in Sym3 is one-dimensional and contains the SPD metric. This proves the second alternative.

The root is genuinely strict U: norm growth along the selected tree makes its norm strictly larger than that of every other true vertex, which makes all its outgoing primitives negative. Each nonroot has its selected nonnegative escape. Thus this is full vertex-U1, not merely apical instability.

## 8. Exact finite candidates on this atlas

Use coordinates

    m=(M11,M22,M33,M12,M13,M23).

For an edge e=(i,j), write zi=di A+Ui and ve=di Uj-dj Ui. The positive-denominator-cleared arrow is

    zi^T M ve=(di^2 dj) D_ij(M).

Its six coefficients are

    (zi1 ve1, zi2 ve2, zi3 ve3,
     zi1 ve2+zi2 ve1,
     zi1 ve3+zi3 ve1,
     zi2 ve3+zi3 ve2).                               (8.1)

Take five distinct source vertices and choose one genuine neighbor for each. Reject directed cycles. Form the5x6 matrix C of rows (8.1). For columns j=0,...,5 define

    mj=(-1)^j det(C with column j deleted).

If all six minors vanish, these rows do not define an isolated metric ray. Otherwise form

    M_C=((m0,m3,m4),(m3,m1,m5),(m4,m5,m2)).

Test M_C and -M_C for positive definiteness. At most one sign works. Normalize the successful matrix by its positive trace, and test the COMPLETE true weak graph for rooted reachability. This is the exact finite candidate construction; there is no arbitrary metric-fitting parameter left in such a candidate.

For root0, the eligible source degrees are4 and eight copies of3. The number before cycle rejection and deduplication is bounded by the coefficient of t^5 in

    (1+4t)(1+3t)^8,

namely

    56*243+4*70*81=36288.

For all roots together, enumerate each five-source set just once. The degree product is

    (1+6t)(1+4t)(1+3t)^8,

whose t^5 coefficient is

    56*243+10*70*81+24*56*27=106596.

These are upper counts of candidate contact sets, not canonical orbits and not a reported executed census.

A useful automatic rejection is geometric. If five independent zero-arrow rows all lie within one actual facet with pole qf, then qf qf^T annihilates them all. Their one-dimensional kernel is therefore the rank-one ray qf qf^T, not an SPD ray. In particular a full-rank critical candidate cannot have all five zero edges inside the heptagonal base. Opposite directions on one edge and any directed zero cycle are also impossible for SPD metrics by strict norm growth.

Every entry in (8.1) is polynomial of degree at most two in the actual star parameter c after clearing the positive denominators. Thus the cofactor candidate entries have degree at most ten in c. Their principal-minor and full-graph sign tests are exact algebraic shape conditions evaluated at the SAME actual-centroid root, not free conditions on c.

This recipe handles deficient-rank strata correctly: a vanishing cofactor vector is not declared an infeasible geometry. It merely cannot supply the interior vertex in the second alternative; feasible components on such a stratum must still be considered through the other independent contact sets or the rank-two alternative.

## 9. What this says about the remaining full-rank search

On a V7 body, a full-rank root0-U1 system now has two possible destinations:

- a genuine rooted rank-two system outside the accepted excluded kernel domains, with its real collapsed-fibre and lift conditions; or
- one of at most36288 actual five-zero-arrow SPD candidates on that very body.

The first destination is further constrained by the base-normal portal theorem. If the metric’s base-normal direction lies in V7’s chamber, flattening it can fail only through the two explicit cap sources and the mixed inequalities in (3.2). A one-horizon geometry leaves only one source and forces the direction switch in section6.

The second destination is an exact way to detect a full-rank component that never approaches rank two. It must not be discarded merely because every tested singular system was infeasible.

If a tree T has no singular feasible point, its entire normalized feasible metric set is the convex hull of its five-zero-arrow SPD vertex metrics. Any one of its metrics is a convex combination of at most six such vertices: an affine dependence among more than six points in trace-one Sym3 permits eliminating a coefficient while preserving the combination. A strict selected tree is feasible exactly when its inequalities are not forced to zero throughout that polytope; averaging suitable vertex metrics supplies a strict point.

This also retains the proper110 distinction. Along a convex combination M(theta) of these actual SPD metrics, primal primitives are affine in theta, but reciprocal polar primitives have the sign of expressions involving adj(M(theta)) and are quadratic in theta. Stability, saddles and physical weak packets cannot be inferred from the censuses at the vertices of that metric polytope. A full common-metric110 test must retain those quadratic polar expressions and all four primitives on every true edge.

No five-zero-arrow candidate on the current atlas has been newly evaluated in this handoff, and no actual rank-two rooted system outside the accepted exclusions is supplied. The new result is the proved full-rank alternative and the actual normal-port obstruction, not an empty-search claim.

## 10. Continuation and preservation

The most direct next calculation is to apply the finite candidate recipe to a genuinely unequal actual body or a controlled shape cell, while using the normal-port inequalities to prune impossible routing. This differs from repeating the145 silhouette tests: it targets the possible positive-definite interior rays themselves. A candidate that passes full true rooted reachability is already an actual vertex-U1 metric, although its same-metric S/H/weak census still needs to be computed. If all critical candidates are rejected for a body, every U1 component on it must instead have a genuine rank-two rooted boundary outside the settled chambers.

For the horizon direction, the strict scalar gate and the adjugate footprint test in section6 are useful whole-fibre targets. They require actual heights, the true base foot and the actual three outside vertices; the retained-core geometry proves that both virtual overhangs cannot be present simultaneously. No released-pyramid boundedness assumption is needed.

All new claims above are derived analytically. No program materially produced a new theorem, object or census here, so no new code hash, byte count, sandbox-only certificate or claimed cold replay is supplied. The exact graph, literal coordinates, actual-centroid equations, determinant recipe and metric formulas needed to continue are included in full. The accepted V7 numerical cylinder and its prior nonwinning controls remain unchanged. The unresolved issue is genuine full-rank rooted feasibility or same-metric110 on the remaining actual geometry, not local apexU or a singular outgoing-arrow count.
