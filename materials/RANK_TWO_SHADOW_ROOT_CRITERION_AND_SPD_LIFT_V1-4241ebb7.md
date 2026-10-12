# material-4241ebb7bd4e

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# RANK_TWO_SHADOW_ROOT_CRITERION_AND_SPD_LIFT_V1

## Scope and source of the question
This is a coordinator analytical theorem, not an executed numerical search, a whole-type exclusion, or a construction of class110. It sharpens the collapsed-fibre observation in the completely read immutable result minimum-0208 (SHA256 8009afaa54e6d97c95b01bfbc40ea119fcc3fd87a4cb1528b21a5e4a2b70b9d9). That result excludes all nonzero PSD rooted trees throughout its specified deep independent-cut band and gives an actual-centred collapsed-edge countercontrol. The present statements concern arbitrary fixed full-dimensional convex polytopes. They require no uniformity for their graph equivalence. When applied to the minimum problem, the origin must still be the actual volume centroid, and the planar measure is its actual fibre-length marginal, not uniform area.

Let P=conv{X_i} be a full-dimensional convex three-polytope with its true vertex-edge graph. Assume 0 is in int P. Let M0=L^T L have rank two, with L:R^3->R^2 surjective, and put y_i=LX_i, Q=LP. Define the directed weak-arrow graph G by including each true directed edge i->j for which D_ij=X_i^T M0(X_j-X_i)=y_i.(y_j-y_i)>=0. Both directions of a collapsed edge are included. A rooted arborescence toward a means every nonroot has a chosen outgoing true edge and the selected arrows lead to a. Rooted means reachability, not merely one outgoing arrow per nonroot.

A strict radial maximum corner y of Q means y.(z-y)<0 for both neighboring polygon corners z. Equivalently y uniquely maximizes the linear functional x->y.x on Q. This is the strict unstable-vertex test for the planar polygon with reference0. No claim about physical weak equilibria or a uniform planar mass is implicit.

## Theorem 1. Exact correspondence of sinks and projected maxima
The sink strongly connected components of G are in canonical bijection with the strict radial maximum corners of Q. The component over such a corner y consists of exactly the true vertices of the exposed fibre F_y=P intersect L^{-1}{y}. This fibre is either one true vertex or one true edge. In the edge case its endpoints form a two-cycle of zero arrows. Consequently G admits a weak arborescence toward a if and only if Q has exactly one strict radial maximum corner y and X_a belongs to F_y.

Proof. For every weak arrow,
 |y_j|^2-|y_i|^2=2D_ij+|y_j-y_i|^2>=|y_j-y_i|^2.
Summing around a directed cycle shows every projected displacement on the cycle is zero. Strong connectivity therefore forces one common projected point for an entire component. All its vertices lie on a line parallel to ker L. A line contains at most two true vertices of a convex polytope: among three distinct collinear points one would not be extreme. Thus a nontrivial strongly connected component has two vertices, joined by a true edge, and all its internal arrows vanish.

Let T be a sink component and y its common projection. Every true outgoing edge from T has D<0. Set n=L^T y. At a singleton, n has strictly negative value on every outgoing edge direction, so the tangent-cone description at a vertex shows that this vertex is the unique global maximizer of n.x on P. For a two-vertex component, n vanishes on their joining edge and is strictly negative on all other incident edge directions at both endpoints. The same tangent-cone argument shows that its maximizing face is exactly this edge. The vector y cannot be zero: then every incident arrow would vanish, so a sink would have no edge leading to a different projected point, contradicting connectedness and full-dimensionality. Thus the projected face maximizing y.x is exactly the singleton{y}, and y is a strict radial maximum corner of Q.

Conversely, if y is a strict radial maximum corner, the functional x->y.x exposes exactly y in Q. Its pullback n=L^T y exposes F_y in P. Since L has a one-dimensional kernel, dim F_y<=1. Hence F_y is a vertex or edge. All true edges leaving it have negative D; its only possible internal edge is collapsed, with both zero arrows. Its vertex set is precisely a sink component.

A finite digraph admits an arborescence toward a if and only if every vertex can reach a. In the present graph this is equivalent to having exactly one sink component containing a: every vertex reaches a sink, and the sink is strongly connected. This proves the final equivalence. In particular, singular strict-vertex counts alone are insufficient; an exposed collapsed edge is a second sink even though neither endpoint is strictly unstable under M0. QED.

## Theorem 2. Only polygon-path cones are needed at a fixed kernel
Choose any surjective B:R^3->R^2 with the specified kernel, list the k TRUE corners p_0,...,p_{k-1} of BP in cyclic order, and write a rank-two metric as M0=B^T H B with H in Sym2 positive definite. The corner set and order depend on B's kernel, not on H. If BX_a is not a true corner, rooted feasibility is impossible. Otherwise set p_r=BX_a. Rooted feasibility is equivalent to the union of the following k homogeneous linear systems in the THREE entries of H:
 - delete one of the k polygon boundary edges;
 - orient the resulting spanning path toward r;
 - require p_i^T H(p_j-p_i)>=0 on every oriented edge of that path;
 - require H positive definite.

This uses true corners of the projected polygon, not every projected original vertex. Every original vertex in the root fibre is handled by Theorem1; no artificial edge in the projection is declared a true mechanical edge of P.

Proof. For a positive-definite planar H, weak arrows between distinct polygon corners strictly increase the H-norm squared. The polygon weak-arrow graph is therefore acyclic. Having only the strict radial maximum r is equivalent to every other corner having a weak outgoing boundary arrow. Following arrows then reaches r, and an arborescence can be selected. Every undirected spanning tree of the k-cycle is precisely that cycle with one edge removed. Conversely any one of these weak rooted paths forces every nonroot corner to have an escape and makes r strictly globally farthest, hence its two outgoing boundary arrows are negative. Theorem1 transfers this statement to the true graph of P, including projected vertices that are not polygon corners. QED.

The feasibility union is exact, including planar weak-arrow equalities. Separate path cones need not have strict interiors. Weak feasibility must not be silently replaced by strict feasibility. For rational B,P the constraints are exact rational binary-quadratic forms plus the 2x2 SPD condition; no complete elimination implementation or execution is claimed here.

For a FIXED P, projection-hull combinatorics can additionally be stratified by the finite great-circle arrangement
 u.((X_j-X_i) cross (X_k-X_i))=0
for triples of vertices, with kernel direction u considered up to sign. These signs determine projected orientations. Degenerate strata, particularly kernel directions parallel to true edges and roots projecting into lower-dimensional hull faces, must be retained. This is a finite geometric stratification, not a completed catalogue or a uniform stratification over moving bodies.

## Theorem 3. A sufficient constructive lift to a genuine SPD U1 body
Assume Theorem1 gives the unique root sink F. Assume in addition that every true vertex outside F has at least one STRICT positive M0-arrow to a true neighbor. This extra hypothesis is not implied by weak rooted reachability. Then each chosen endpoint of F can be made the sole strict unstable vertex of the SAME actual body under a sufficiently small positive-definite perturbation of M0.

If F is a singleton{X_a}, its outgoing arrows are all strictly negative and every other vertex has a chosen strict positive escape. M_epsilon=M0+epsilon I preserves these finitely many signs for every sufficiently small epsilon>0 and is SPD. Thus a is the sole strict unstable vertex.

If F is an edge, take coordinates X=(y,z) in which M0=diag(H,0), H>0, and write its endpoints a=(y,z_a), b=(y,z_b) with z_a>z_b. Their common y is nonzero by Theorem1. To choose a as root, fix any delta>0 and choose k in R2 with k.y+delta z_b=1. Define
 M_epsilon=[[H,epsilon k],[epsilon k^T,epsilon delta]].
Its Schur complement is epsilon delta-epsilon^2 k^T H^{-1}k, so it is SPD for all sufficiently small epsilon>0. The formerly collapsed primitives are exactly
 D_ba=epsilon(z_a-z_b)>0,
 D_ab=-epsilon(z_a-z_b)[1+delta(z_a-z_b)]<0.
All boundary primitives of a,b were strictly negative at epsilon0 and remain so. Every outside vertex retains its selected strict escape. Therefore a is the sole strict unstable vertex. To select b instead, choose k.y+delta z_a=-1 and reverse the calculation.

This is an explicit constructive perturbation and does not move the body or its centroid. It proves U1 only, not S1, H0, or absence of all physical weak equilibria. In fact a rank-two primal limit entails a rank-one-dominated reciprocal metric, so the already accepted two-half spectral obstruction on the actual polar is relevant to S1 near that limit. No 110 attainer or change to34<=Cmin<=622 follows.

## A useful sufficient test for the extra strict-escape hypothesis
At a vertex whose projection p is a nonzero interior point of Q, there is a strict positive true escape: the nonzero functional x->p.x cannot be maximized at an interior point of Q, so its pullback is not maximized at that vertex; one incident true edge has positive derivative. At a projected polygon corner with a strict positive planar boundary arrow, the same tangent-cone argument yields a strict positive true escape from each vertex in its fibre. Therefore, when no original vertex projects to0 and no original vertex projects to the interior of a polygon boundary edge, a STRICT feasible planar rooted path supplies the hypothesis of Theorem3. Generic projection alone is not enough if the path is merely weak or its cone has empty strict interior. Interior points of projected boundary edges, projected zero vertices, and additional zero-arrow traps must be tested separately.

## Consequence for the open atlas
For the actual fixed-six-pole five-cut atlas, a substantive next question is whether any geometry outside the certified deep band admits one of these rank-two projected rooted-path cones. The criterion incorporates collapsed root and nonroot fibres correctly and reduces a fixed-kernel test from arbitrary 4335 true-graph trees to at most10 polygon paths. A strict witness satisfying Theorem3 immediately supplies an actual U1 countercontrol to a proposed all-cube nonapical-U prohibition. A nonroot projected radial maximum excludes the rooted system and is robust if its boundary signs are strict. Absence of a finite sampled witness is not exclusion of any unsampled direction or shape. Even complete rank-two exclusion alone does not rule out an SPD feasible component whose closure avoids the rank-two boundary; no such continuation theorem is claimed.

## Evidence and reproducibility
All statements above are analytic and their full arguments are included. There are no hidden numerical inputs, omitted solver parameters, code files, or an unexecuted numerical certificate promoted as proof. The immutable worker parent named at the start contains its own autonomous exact recovery and remains authoritative for its distinct body, 330-cell band, 389 stresses, and singular countercontrol. The present theorem neither renames those objects nor changes their incidence or accepted scope.
