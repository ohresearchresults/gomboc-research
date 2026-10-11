# material-5052276824a0

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# ROOT_ONLY_TRANSVERSE_FACE_REDUCTION_V1

## Identity, evidence and scope

This is a coordinator-authored analytic continuation of the actual transverse-shadow method. It is a proof, not a reported computer search. No numerical execution or independent replay is asserted. Background dependencies are the fully read proof TRANSVERSE_SHADOW_MOMENT_CHAMBER_V1, material [internal-source-reference] (SHA-256 dadeea4827575c8f57d1614c3cffbb42c2bb77f6a2bb57a531e3614539e71b7e), and the accepted actual-body slide result minimum-0128 (SHA-256 9b8fa9986220926caf778450ec66563e7e5fe300aa1c9fb53433306b415efa34). The argument below supplies its own definitions and elementary proofs and needs no local file or code to reconstruct it.

The result reduces the supremum of the ORIGINAL uniform-volume adjacent-triangle trace in the ROOT-ONLY class to proper bodies with at most 16 true vertices. An exact limiting support-patch representative has at most 9 true facets and 14 true vertices. These are not an upper bound for the trace, not an E17 equilibrium exclusion, and not a reduction of arbitrary positive-ell auxiliary vertices to the root. The limiting patch need not have ABC and ABD as maximal triangular facets. The final proper approximations do, but need not preserve the original volume, root area or centroid exactly. These distinctions are essential.

## 1. Exact class and functional

Fix
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
T0=conv(A,B,C,D), and parameters 0<b<1, c>0, d>0.
Write
ell(x,y,z)=1+(d-1)x+(c-1)y+(b-1)z,
n(x,y,z)=(1+b+c)x+(1+b+d)y.
Thus ell(A),ell(B),ell(C),ell(D)=(1,b,c,d).

Let R be a positive-area convex polygon in the plane ell=0, every vertex of which satisfies x>0,y>0. Set P=conv(T0,R). Then P is full-dimensional, ell>=0 on P, and x=0 and y=0 support exactly the genuine triangles ABC and ABD. Call these proper root-only bodies. The relevant integrals are
v(P)=integral_P 1,
beta(P)=integral_P ell,
nu(P)=integral_P n,
and the original trace is T(P)=nu(P)/(6 v(P) beta(P)). No projective refill or independent moments are introduced.

Allow a marked support-patch closure by replacing x>0,y>0 on the root with x>=0,y>=0, retaining the four fixed points A,B,C,D and retaining positive root area. The true polygon is still R=P intersect {ell=0}. The coordinate support facets may now be larger than ABC and ABD. Integrals and the displayed ratio extend continuously to these bodies. Always
v>=1/6 and beta>=integral_T0 ell=(1+b+c+d)/24>0.

Put alpha=1-b, nx=1+b+c, ny=1+b+d, and choose
u0=grad(ell) cross grad(n)
=(alpha*ny,-alpha*nx,(d-1)*ny-(c-1)*nx).
The notation nu0 denotes a VECTOR and nu(P) denotes the n-moment. They must not be identified. We have ell_lin(nu0)=n(nu0)=0, (nu0)_x>0, (nu0)_y<0. In particular nu0 is nonzero and is parallel to the root plane.

## 2. A collective shadow realization chamber

At any current marked support-patch body, let r be the number of true vertices among A,B,C,D and k the number of true root vertices. Keep the four canonical points fixed and move every true root vertex independently by
p_i(s)=p_i+s_i*nu0, i=1,...,k.
Deleted redundant root labels are not retained as fixed constraints. Their removal leaves exactly the same convex hull.

All oriented affine four-point determinants are affine functions of the entire vector s. This follows by expanding multilinearly: every term using at least two moving columns contains two parallel copies of nu0 and vanishes. The same statement holds for oriented planar three-point determinants in any fixed plane parallel to nu0.

For a true facet f not parallel to nu0, projection along nu0 maps its plane bijectively to a fixed two-dimensional quotient plane. The projections of all labeled points are fixed throughout the motion. Choose three facet vertices with affinely independent projections. The facet is the graph of an affine height function over these projections; its coefficients are affine functions of the three vertex heights. Each of its other k_f-3 true vertices contributes at most one affine coplanarity equation. Requiring a fixed marked nonvertex to lie on this facet contributes at most one more affine equation. Every supporting-side inequality is also affine: substitute the fixed projected position and the affine moving height in that graph equation. Convex cyclic order in this transverse facet is determined by its fixed projection.

For a true facet parallel to nu0, keep its original plane. All its moving vertices remain in that plane automatically; all fixed vertices and marked nonvertices already lie in it. No coplanarity equation is required. Its cyclic convexity and marked-point inclusion can be imposed by oriented planar determinant inequalities, which are affine by the preceding expansion. In particular the root facet requires no coplanarity equations.

Together with x>=0,y>=0 and the current incidences, these equations and inequalities define a relatively open polyhedral realization chamber containing the current point in its relative interior. Its closure allows only the stated convex support degenerations; it does not replace true facets by artificial triangulation facets. Finite triangulations are used only for integration.

## 3. Dimension count including nonvertex canonical marks

A and B remain true vertices throughout the marked closure. Indeed n is strictly positive at every root vertex initially, remains fixed at that label, and is therefore bounded below by a positive constant on every subsequent root polygon. Since x,y>=0, no root point has x=y=0. Consequently P intersect {x=y=0} is exactly AB. Both ends are extreme.

It follows that 2<=r<=4. Only C and D can cease to be true vertices. Each such fixed nonvertex lies on a coordinate support facet. If it is in the relative interior of a true facet, one facet-incidence equation retains its supporting position. If it lies in the relative interior of a true edge, at most two such equations are needed, since a true edge of a convex three-polytope belongs to exactly two maximal facets. Its inclusion in the corresponding polygon/edge is retained by the affine inequalities above.

Let f denote the number of true facets and e the number of true edges of the current hull. Euler gives e=k+r+f-2. Also sum_f k_f=2e. The total number of coplanarity equations supplied by all non-root true facets is at most
sum_{f != root}(k_f-3)=2e-3f-(k-3)=k+2r-f-1.
This is an upper bound even if some facets are parallel to nu0, since those impose no equations. Retaining the 4-r fixed canonical nonvertices costs at most 2(4-r) additional equations. Hence the total affine-equation rank is at most
k+2r-f-1+2(4-r)=k+7-f.
The collective shadow chamber consequently has dimension at least
DIM >= f-7.                                      (1)

Coordinate-patch contacts are already included in this count, not extra uncounted restrictions. For example, if C is a true vertex, A,B,C determine the fixed plane x=0 and its other root vertices contribute the counted k_f-3 equations. If C is no longer a true vertex, the extra incidence equation for the fixed mark C fixes the same plane. The analogous statement holds for D and y=0.

## 4. The actual integrals are affine in a chamber

Triangulate each current maximal facet by its cyclic true vertices, with an oriented fan, and cone the boundary triangles to fixed A. This signed formula also covers facets through A, whose tetrahedral contributions vanish. On the genuine convex chamber the total is the actual volume.

Each tetrahedral determinant is affine in s by the parallel-column argument. For either affine function ell or n, its integral over a tetrahedron is its oriented volume times the arithmetic mean of its values at the four vertices. These values are CONSTANT under every root motion and at the four fixed canonical vertices. Therefore v, beta and nu are affine throughout the chamber. The oriented area of R in its fixed plane is likewise affine, since all second-order cross terms contain parallel vectors nu0. Its positive orientation is retained by the convexity guards.

These formulas remain valid and continuous at a chamber wall. Recompute the true hull and use its true facets after a degeneration. A vanishing artificial diagonal is not a true-edge event and is not counted as one.

## 5. Compactness and a monotone segment

Each root label has fixed positive n_i. Since its x,y coordinates remain nonnegative and nx,ny>0,
0<=x_i<=n_i/nx, 0<=y_i<=n_i/ny.
The equation ell=0 determines z_i because b-1 != 0. Thus the entire marked root-position set is bounded. In particular every closed realization chamber intersected with affine integral constraints is compact; there is no escape to infinity along a putative motion.

Preserve v and the actual positive root area. These are at most two affine equations. If f>=10, (1) leaves a nonzero direction through the current relative-interior point satisfying both constraints. Along the resulting straight segment, beta and nu are affine and beta stays positive. Thus
T(t)=(nu0_scalar+t*nu1_scalar)/(6*v0*(beta0+t*beta1))
has derivative of constant sign (or is constant). Choose the orientation in which T is nondecreasing, and proceed to the first boundary of the compact feasible chamber. This is a real convex-body deformation, not a formal moment variation.

For rational parameters and a rational starting polytope, the linear equations and inequalities are rational. A nonzero rational direction and its exact rational first endpoint can be chosen. No numerical optimizer or determinant tolerance is required by this existence construction.

## 6. Why repeated wall passage terminates

At a boundary, distinguish two kinds of event.

(1) The actual true face lattice coarsens. Root vertices may become nonextreme, maximal facets may merge, or a facet polygon may collapse. The boundary body remains full-dimensional because it contains T0, and the root stays two-dimensional because its area was fixed positive. The true vertex count and true facet count cannot increase. For vertices this follows because each extreme point of a limiting finite convex hull is the limit of an old true vertex. A previously nonvertex fixed C or D cannot become extreme: an old moving root vertex has ell=0 and therefore cannot converge to C or D, whose ell-values are strictly positive. For facets, the old supporting facet polygons have supporting limits and their union covers the limiting boundary; every positive-area limiting facet is a union of such limiting polygons, so no additional maximal facet appears. If the true lattice changes, either a true vertex is lost or distinct old facets coalesce/lose area. Hence e=v_count+f-2 strictly decreases. Remove redundant root labels and replace all merged facets by their actual maximal facets.

(2) The true hull lattice is unchanged but a fixed nonvertex C or D acquires a new boundary incidence, for example moving from the interior of a coordinate facet onto one of its edges. Freeze that new incidence, and work in the corresponding marked chamber. Each of the at most two such marks is contained in at most two distinct true facets as long as it is not a true vertex. Between actual coarsenings only finitely many such incidence increases are possible; old incidences are retained until a genuine coarsening is recomputed. Inequalities that are redundant on the affine hull do not constitute a first boundary event.

There cannot be infinitely many iterations: actual coarsenings strictly decrease a nonnegative integer e; between them the marked-incidence increases are finite. At each stage the same count (1) applies with the NEW true facet and vertex lists. A nonzero motion of at least one true root vertex cannot leave the entire convex hull fixed, since the moved point was extreme in the relative interior of that stage.

The process therefore reaches a marked support-patch root-only hull Q with f(Q)<=9, v(Q)=v(P), area(R_Q)=area(R_P)>0 and T(Q)>=T(P). The elementary three-polytope inequalities 3*v_count<=2e and Euler imply
v_count(Q)<=2*f(Q)-4<=14.                         (2)

This proves the exact PATCH representative theorem. It does not yet say that ABC and ABD remain maximal triangular facets.

## 7. Root-only proper resolution and the 16-vertex statement

Choose q in relint(R_Q) with q_x>0,q_y>0. Such a point exists because R_Q has positive area in ell=0 and lies in x,y>=0; the intersections of its plane with x=0 or y=0 are only lines. For 0<epsilon<1 put
R_epsilon=(1-epsilon)R_Q+epsilon*q,
P_epsilon=conv(T0,R_epsilon).
Every root vertex now has positive x and y, so ABC and ABD are genuine maximal triangular facets and P_epsilon is again a proper root-only body with the SAME b,c,d and the same ell,n. It converges to Q as epsilon decreases to zero, and T(P_epsilon) converges to T(Q).

This construction equals the earlier marked-patch resolution conv(T0,(1-epsilon)Q+epsilon*q), not a different enlarged hull. To see this, q belongs to R_epsilon, and for each canonical point X the displaced point (1-epsilon)X+epsilon*q is in conv(X,R_epsilon). Thus no additional displaced canonical vertices are needed.

If Q has k true root vertices and r true canonical vertices, r>=2 and k+r<=14. The resolved hull has at most k+4<=16 true vertices. In particular, for any real threshold tau,
T(P)>tau => there exists proper root-only P_epsilon with <=16 true vertices and T(P_epsilon)>tau.   (3)
For every proper P and every delta>0 one obtains such a body with T(P_epsilon)>T(P)-delta. Therefore the supremum of T over all proper root-only polytopes at fixed b,c,d equals the supremum over those with at most 16 true vertices. The same equality holds when b,c,d vary over any specified allowed set, since the operation leaves them fixed.

The strict-threshold qualification in (3) is indispensable. From T(Q)=tau alone one cannot infer a proper resolution with T>=tau, and this theorem does not prove that a proper maximizer exists. If an upper bound T<=tau is proved on the <=16 class, it extends to all proper root-only bodies. A pointwise strict bound on the <=16 class by itself does not exclude equality arising as a limiting supremum for another class.

## 8. Other exact-moment variants

The same proof gives the following optional variants within the marked patch closure.

- Preserve v, beta and root area (three affine constraints), and choose the direction in which nu does not decrease. If f>=11 a direction exists. The terminal body has f<=10 and at most16 true vertices, with T not decreased.
- Preserve v, beta, nu and root area (four affine constraints). If f>=12 a direction exists. The terminal body has f<=11 and at most18 true vertices, with exactly the same displayed moments and trace.

Proper root-only resolutions then use at most18 and20 true vertices, respectively, and approximate the limiting trace. They generally do NOT preserve these moments exactly after resolution. The first variant is stronger than necessary for the main supremum result, but may be useful when a downstream inequality uses beta explicitly.

No variant above preserves the full first moment vector J or the actual centroid. The components of J annihilating nu0 are controlled by v,beta,nu, but the remaining component can be quadratic under collective motions. Full equilibrium labels, a common SPD metric, E17 complexity and strict/physical-weak census are not preserved by the variational reduction. It is a trace tool only.

## 9. Remaining scientific task and limits

The new finite reduction does not determine the <=16 root-only supremum and does not establish T<51/25. It leaves arbitrary positive-ell auxiliary vertices outside its domain; the accepted exact deletion/binary-projection countercontrols remain valid and prevent substituting root-only results for unrestricted bodies. It also does not repair a proof that treats a coordinate support patch as a genuine triangular facet without the explicit resolution above.

The useful next step is a genuine extremal inequality in this smaller finite class, or a further geometric description of the terminal <=9-facet marked hulls. A separate extension must address the collectively movable and individually rigid positive-ell auxiliary vertices identified in minimum-0128. No global bound for C_min is changed by this analytic reduction: the accepted interval remains34<=C_min<=622, with10/17/9 the first open layer.
