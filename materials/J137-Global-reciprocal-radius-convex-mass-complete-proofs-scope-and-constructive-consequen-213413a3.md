# material-213413a39703

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J137 global reciprocal-radius convex mass

This note is a derived research method, NOT an own110 construction or a claim of historical novelty for a general convex-geometric theorem. Canonical own110 remainsC622. It removes a physical-centroid nuisance globally, including changes of incidence, but does not remove the hard equilibrium constraints.

## 1. Setting and exact formula on a complete fan
Fix distinct nonzero ray vectors R_1,...,R_n in R^3 with0 strictly inside conv{R_i}. For t_i>0 put x_i(t)=R_i/t_i and K(t)=conv{x_i(t)}. The origin remains strictly inside K(t): any strictly positive balanced coefficients for the R_i can be multiplied by t_i and normalized to obtain a strictly positive convex representation of0 using x_i(t).

Let F be an oriented complete simplicial radial fan whose rays are selected from the R_i. Every cone f=(i,j,k) has D_f=det(R_i,R_j,R_k)>0. Its piecewise planar radial body S_F(t), the union of tetrahedra conv(0,x_i,x_j,x_k), is well defined for every positive t, whether or not that body is convex. Distinct fan cones have disjoint interiors, so
 V_F(t)=sum_f D_f/(6 t_i t_j t_k),
 M_F(t)=sum_f D_f*(R_i/t_i+R_j/t_j+R_k/t_k)/(24 t_i t_j t_k).
Every tetrahedron lies in K(t), hence V_F(t)<=V(t):=Vol K(t). No convexity of S_F(t) is needed for this global lower bound.

For one term v=a/(t_i t_j t_k), its Hessian on the three participating coordinates is v*(diag(1/t_i^2,1/t_j^2,1/t_k^2)+u u^T), u=(1/t_i,1/t_j,1/t_k). It is positive definite. Thus V_F is convex on the entire positive orthant, strictly convex if every ray occurs in some positive-volume triangle of F.

## 2. Convexity of the TRUE hull volume, without retaining the fan
Let L(t)=K(t)^polar={y:R_i.y<=t_i for every i}. Its support function q_t(u)=h_L(t)(u)>0 on the unit sphere is the gauge of K(t). By elementary finite linear-program duality,
 q_t(u)=min{sum_i lambda_i t_i:sum_i lambda_i R_i=u, lambda_i>=0}.
The feasible coefficient set is independent of t, so q_t(u) is concave in t. Equivalently L(theta t+(1-theta)s) contains theta L(t)+(1-theta)L(s), giving the same support-function concavity. Since r->r^-3 is strictly convex and decreasing on positive r,
 q_{theta t+(1-theta)s}(u)^-3 <= (theta q_t(u)+(1-theta)q_s(u))^-3 <= theta q_t(u)^-3+(1-theta)q_s(u)^-3.
Integrating the radial volume formula V(t)=(1/3) integral_S2 q_t(u)^-3 dOmega proves GLOBAL convexity of V on t>0. This is not limited to one incidence chamber.

A finite alternative characterization supplies an implementable convex oracle. Among all complete geometric simplicial fans using subsets of these finitely many rays, every V_F is a global lower function as above. A triangulation of the actual hull boundary produces a fan attaining V(t). Consequently
 V(t)=max_F V_F(t).
There are finitely many such fans, although far too many to enumerate naively. Facet flips, coplanarity and redundant/retired points are part of this global convex function. It may be nonsmooth; do not reuse a single fan's gradient as a globally smooth gradient at a combinatorial wall.

## 3. Balanced positive weights close the ACTUAL physical mass
Choose any w_i>0 satisfying sum_i w_i R_i=0. Minimize the globally convex function
 F_w(t)=V(t)+sum_i w_i t_i, t_i>0.
A minimizer exists. In a sublevel F_w<=A, positivity gives t_i<=A/w_i. For each i choose j,k with nonzero det(R_i,R_j,R_k), possible because the rays span3D. The tetrahedron conv(0,x_i,x_j,x_k) is inside K(t), and its positive absolute volume is |det|/(6 t_i t_j t_k). The already obtained upper bounds on t_j,t_k therefore force a strictly positive lower bound on t_i. Sublevels are compact subsets of the positive orthant; continuity finishes existence.

For any sufficiently small b in R^3, t+Rb is positive and
 x_i(t+Rb)=x_i(t)/(1+b.x_i(t)),
 K(t+Rb)=T_b K(t), T_b(x)=x/(1+b.x).
The denominators are positive throughout the convex body when positive at every vertex. The Jacobian in dimension3 is (1+b.x)^-4, so at b=0
 D_b V(t+Rb)=-4 integral_K(t) x dx=-4 M(t).
This derivative exists even at incidence walls, because the entire hull is transformed projectively. The linear weight term has derivative sum_i w_i R_i=0. At the interior-orthant minimizer both positive and negative small b are feasible, so stationarity in these three directions gives M(t)=0 EXACTLY. This is the own centroid of filled uniform volume, not a substitute reference point.

The same argument works on a fixed-fan convexity cone or any feasible domain invariant under sufficiently small t->t+Rb, including linear hinge gaps Ht>=epsilon with HR=0. Artificial coordinate bounds can spoil stationarity if active; a numerical solver with bounds must check that they are inactive, or independently recalculate/recenter actual mass.

## 4. Uniqueness and completeness of the global parameterization
If K(t) and K(s) differ, their continuous gauges differ on an open spherical set. The strict second inequality in section2 on that set gives strict convexity of V along their segment. Therefore two minimizers of F_w must represent the same body K.

At any minimizer every ray point is on the boundary: t_i must equal gauge_K(R_i). If t_i were larger, decrease just t_i to this value; the point moves from the interior to the same body's boundary, K and V do not change, and the positive linear weight term strictly decreases. Thus the same body has only one minimizing t representation. Together these observations prove a UNIQUE minimizer for each balanced positive w, despite possible nonsmoothness and redundant nonextreme boundary points.

Conversely, take any convex body represented by these rays, containing0 and with its ACTUAL centroid0. Replace any redundant ray representation by its boundary point, so all t_i=gauge_K(R_i). Triangulate the hull boundary using every boundary ray point, adding edge/face-interior ray points to the triangulation where necessary. Distinct ray directions and0 interior permit a complete fan with all D_f>0 and every index participating. At this t, S_F=K. Set w=-gradient V_F(t). Every w_i>0. The fan formula gives R^T gradient V_F=-4M_F=-4M_K=0, so w is balanced. Convexity of V_F and the global lower bound V>=V_F show
 V(s)+w.s >= V_F(s)+w.s >= V_F(t)+w.t=V(t)+w.t
for every positive s. Hence this body is precisely the unique global minimizer. The weighted convex program therefore parameterizes ALL own-centred convex bodies with the given ray directions, after moving redundant ray labels to their boundary representatives. This is stronger than a first-order rank statement and stronger than preserving one normal fan. It still fixes the ray directions and does not assert that these particular43 directions admit own110.

Scaling weights by alpha^-4 scales the minimizing t by alpha and the physical body by alpha^-1; equilibrium class is unaffected by this uniform scale. For arbitrary positive baseline a_i, every eta can be balanced by w_i=a_i exp(eta_i+R_i.b). The strictly convex function sum_i a_i exp(eta_i+R_i.b) has positive-definite Hessian, tends to infinity as |b| tends to infinity because0 is interior to the convex hull of the rays, and has a unique minimizer satisfying sum_i w_i R_i=0. Normalizing all weights only sets scale. Any already balanced positive w is represented by eta_i=log(w_i/a_i),b=0. This is a complete smooth weight-coordinate system, not an ad hoc redistribution of only one physical tetrahedron.

## 5. Fixed-fan support, physical arrows and centering derivative
On a complete fan f=(i,j,k), write the 3x3 matrix with rows R_i,R_j,R_k as R_f. The normalized facet vector is n_f(t)=R_f^-1 t_f, linear in t, with plane n_f.x=1. Convexity is equivalent to all linear inequalities t_l-R_l.n_f(t)>=0. One correctly oriented adjacent hinge inequality per edge also suffices: the piecewise linear gauge is continuous across the fan walls; nondecreasing one-dimensional derivatives across every codimension-one wall imply convexity on generic lines and then everywhere by continuity. All these rows satisfy HR=0.

A physical root-excluding arrow i->j satisfies
 x_i.(x_j-x_i)>0 iff (R_i.R_j)t_i-|R_i|^2 t_j>0.
These are linear in t. Polar arrows n_f.(n_g-n_f)>0 are quadratic, not linear. A selected outgoing positive arrow at every vertex except one forces an acyclic positive-radius forest and U1; the analogous polar statement forces S1. A failed selected tree does not exclude another tree, another root, another fan or another ray family.

Raw second moment Q=int_K xx^T dx is positive definite. Projective differentiation gives D_b M=-5Q. At an exactly centred fixed-fan t, if M_t denotes the unrestricted t Jacobian of the first moment, the local derivative of re-centering is
 K_section=I+R(5Q)^-1 M_t.
It satisfies M_t K_section=0 and K_section R=0. This is a tangent map, not by itself a finite mass capacity theorem. Executed numerical continuation re-solves actual centering at every trial and rejects nonpositive denominators; using only this tangent projection would be insufficient.

Any convex projective-invariant barrier Psi(t), with Psi(t+Rb)=Psi(t), can be added without altering the mass-stationarity conclusion where a minimizer exists. Example on a strict fixed fan: -sum_e mu_e log((Ht)_e),mu_e>0. This can keep facets separate, but it does not preserve their equilibrium signs. Completeness for fixed positive weights with an arbitrary added barrier does NOT follow from the unbarriered converse above.

## 6. Executed evidence and limitations
Unchanged exact QW49I_LOW43_G9 is43/123/82,C246,own121/weak000. Three new rational reference centres on the same body are exact110/weak000, but all differ from its actual uniform centroid. Complete audits/inputs: [internal-source-reference] and [internal-source-reference]. The numerical nearest-cell MILP at positive margin1e-7 had L-infinity objective.2950452272592313. That solver optimum is not an exact all-cell lower bound. A chosen reciprocal-radius tree was numerically infeasible, while the root-free physical-arrow MILP found feasible alternatives: one-tree infeasibility did NOT exclude the cone.

Fixed-fan positive-weight HIGH and ROOT paths preserved actual centering numerically but produced many S/U. Their near-coplanar endpoints were rationally coalesced with exact support and mass checks. Complete recovery [internal-source-reference] gives HIGH_M01 true40/105/67,C210,own(23,7,28),and HIGH_M4 true32/66/36,C132,own(12,5,15),both weak000/primitive000. Neither is a better single-basin entrance. The HIGH control is the26-node graph superlevel component above old death.23912616515768817, not the author's36-node full-P complement.

The first global fan-epigraph experiment used HIGH strength-.1 and20 growing fan lower functions. The actual final numerical hull had42vertices and S22/U8; relative true-volume/epigraph gap~9.19668e-5 and |actual g|~2.04684e-5. Thus it DID NOT solve the global optimization to mass closure and is not a certificate or a candidate110. It demonstrates an implementable lower-function method and an unresolved numerical convergence obstacle. More fan additions, better nonsmooth convex optimization, equilibrium-aware outer weight choices and angular redesign remain open. A finite failed weight path, a stalled safe-centred continuation, or a failed bound-constrained optimizer proves no global exclusion.

The barrier scout likewise did not solve the equilibrium problem. Small successful trials already produced extra equilibria; larger SLSQP status4 trials violated the intended fixed-fan margins, and their fan-moment formula must NOT be called the actual hull centroid. One later inactive-point census raised an exception. These are explicit numerical/domain failures, not counterexamples to the convex/mass theorem.

Next constructive use: optimize the whole current P/Q landscape in positive balanced-weight coordinates while allowing fan changes, or apply the exact geometry/centroid separation to a new angular fan with adequate edge reserve. Preserve the existing clean own121/own211 entrances rather than replacing them with these fragmented nonwinners. The target is still exact own110,weak000,E<=249, not reference110, small mass residual, low E alone, or convergence of a convex inner problem.
