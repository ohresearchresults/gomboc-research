# material-dcf92edaf8ab

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# E17_PROJECTIVE_BOUNDARY_COMPACTNESS_AND_TWO_CAP_TOTAL_COLLAR_V1

## Status and dependencies
Coordinator analytical synthesis. No new numerical computation, sampling, or independent replay is asserted.
1. NINE_VERTEX_NONZERO_PSD_REFINEMENT_COLLAR_V1, [internal-source-reference], SHA3052074db1f19530ac423145576607e4c86366b7e45a96cf9f17f880f0aee65b. An actual full-dimensional uniform body with <=9 true vertices has no complete weak rooted escape tree for any nonzero PSD metric, even on arbitrary finite contained refinement labels. Bounded-label affine convergence to such a body gives an all-SPD U>=2 collar.
2. minimum-0217, SHA d855f740fcfc32469432ae2866c68ca98d0ad139ac857c8d7bd8c391897262d0, read completely through EOF. Its Sections3-5 give the bounded interior-reference projective chart, maximum-volume-tetrahedron normalization and arbitrary-rate source/face-label bounds, together with the literal two-cap family and all limiting-prism label strata. Its exact recovery preserves the genuine nonpyramidal8/14/8 control; that control is not being discarded or renamed.

This synthesis closes boundary questions deliberately left open in dependency2 because only the <=7-vertex obstruction was supplied there. Its boundary cores have at most eight true vertices, so even the accepted <=8 predecessor suffices for the two-cap consequence below. The new <=9 theorem additionally closes the general E17 facet-size8 case.

## 1. Interior-reference projective chart
Let P be a bounded full-dimensional polytope and choose w in its interior. Modulo an affine change of output coordinates, every projective image whose denominator is strictly positive on P can be represented by
 Z_q(x)=(x-w)/(1+q dot(x-w)),
 q in D(P,w)={q:1+q dot(v-w)>0 for every true vertex v}.
If P-w contains a radius-r ball, ||q||<1/r. Thus the closure of D is a compact polytope. An arbitrary affine numerator introduces no additional issue because both the newly uniform-filled body and its own centroid transform affinely; all physical SPD metrics are already allowed. A reference w used to compactify q is not a replacement mechanical centroid.

## 2. Arbitrary-rate boundary normalizations
For completeness the accepted normalization mechanism is reproduced here. Suppose finitely labelled source polytopes P_n=conv(v_i,n) converge labelwise to a full-dimensional P0, with a common interior reference w and common inner ball. Let q_n converge to a boundary q_* of D(P0,w), with all actual denominators positive. Let F be the exposed zero-denominator face of P0, and m(F) the number of ALL retained limiting labels on F, not just its true vertices.

The transformed bodies contain a common ball around0. Choose a maximum-volume tetrahedron among their actual transformed vertices, and send its four vertices affinely to0,e1,e2,e3. The replacing-one-vertex maximality property bounds every barycentric coordinate in absolute value by1. Therefore every normalized labelled point U_i,n is bounded and the normalized hull contains the standard tetrahedron. Write the normalizer A_n z+b_n. The transformed common ball implies A_n is uniformly bounded; 0 in the transformed hull implies b_n is bounded. Pass to a subsequence with A_n->A,b_n->b and all U_i,n convergent. The limit K is bounded and full-dimensional.

For a label in F, f_i,n=1+q_n dot(v_i,n-w)->0 and
 A_n(v_i,n-w)=f_i,n(U_i,n-b_n)->0.
Thus A annihilates span(F-w), of dimension dim(F)+1. Outside F,
 U_i=b+A(v_i,0-w)/(1+q_* dot(v_i,0-w)).
Consequently:
- If F is a facet, A=0 and all outside labels become one point: V(K)<=m(F)+1.
- If F is an edge, rank(A)<=1 and the outside hull is an interval: V(K)<=m(F)+2.
- If F is a vertex v, A(v-w)=0. The outside hull is an affine image of the section of the actual tangent cone at v by q_* dot u=1. That section has deg_P0(v) vertices, so V(K)<=m(F)+deg_P0(v).
These estimates allow arbitrary relative rates of source-shape and denominator changes. Actual uniform volume centroids converge after normalization, since the hulls are bounded with a positive-volume limit. No projected area weights replace actual three-dimensional volume weights.

Whenever the relevant vertex-count bound is <=9, dependency1 excludes every approaching U1 sequence in every SPD metric, including arbitrarily ill-conditioned metrics and coalescing labels.

## 3. All projective boundaries of ANY fixed V10/E17/F9 realization are excluded
Let P be any fixed actual realization of V10/E17/F9. Every vertex has degree at least3 and
 sum_v(deg(v)-3)=2E-3V=4.
Therefore max degree<=7. Every facet has at most8 vertices: a facet with9 vertices would leave only one outside vertex. Each of the nine facet vertices needs an incident edge leaving that facet, so all nine would connect to the remaining apex. Together with the nine boundary edges this would require E>=18, contrary to E17. (A full-dimensional polytope cannot have a facet containing all10 vertices.)

For a fixed source, the labels are exactly its true vertices. Every boundary denominator exposes a vertex, an edge or a facet, with bounds respectively
 1+deg(v)<=8,
 2+2=4,
 number of facet vertices+1<=9.
Section2 and dependency1 therefore exclude every projective-boundary U1 sequence, for all physical SPD metrics.

It follows that there is a geometry-dependent delta(P,w)>0 such that every newly uniform-filled positive projective image with U1 in some SPD metric satisfies
 min_i [1+q dot(v_i-w)]>=delta(P,w).
Proof: otherwise take q_n with the minimum tending to0 and a convergent subsequence in the compact q-domain, contradicting the corresponding boundary collar. If there are no U1 images the conclusion is vacuous. No numerical delta is asserted.

Thus the possible projective parameters of U1 bodies lie in a compact subset of the positive-denominator interior. This is a theorem about ANY fixed E17 realization, not only the known two-cap family. It is not a uniform theorem over all changing E17 realization spaces: a joint source degeneration must retain its own face-label counts and full-dimensional limit.

## 4. The ENTIRE two-cap noncompact boundary is now closed
Use the literal P_epsilon of dependency2,0<epsilon<=5, with w=(451/2280,1741/798,366/665). The family has a common contained tetrahedron and bound. Its epsilon0 source is a full-dimensional six-vertex triangular prism, retaining10 limiting labels. The source provides complete face-label counts:
- Facets carry respectively7,5,3,7,4 old labels, so every facet-boundary normalization has <=8 true vertices.
- The long prism edge carries5 labels, another carries3, the other7 carry2; all edge bounds are<=7.
- Each prism vertex is simple and has one label, giving bound4.
An interior q-limit at epsilon0 gives a projective image of the six-vertex prism, also covered by dependency1.

For positive limiting epsilon, the actual body has maximum degree7 and maximum facet size7, so every boundary normalization has at most8 true vertices. Hence ALL projective boundary sequences, including unbounded original c, and ALL epsilon->0 sequences, including every joint rate hierarchy, are excluded for U1 in every SPD metric.

In particular both old escape channels q_H=(2280/4039,0,-1140/577) and q_LR=(280/73,-14/73,175/146) are now closed. The actual nonpyramidal8/14/8 LR control remains valid: it has three strict shadow maxima, not a weak rooted system. One must not falsely reduce its vertex count to seven. The <=8/9 contained-refinement theorem handles its actual eight-vertex geometry and the possible cofacial merger, including retained old edges that become diagonals.

Uniform compact-core formulation: there exist epsilon_*>0 and delta_*>0 such that every U1 member of this entire projective/refill family obeys
 epsilon_*<=epsilon<=5,
 min_i[1+q dot(Y_i(epsilon)-w)]>=delta_*.
Otherwise compactness of epsilon and q yields one of the excluded limiting cases. This is stronger than localization away from two exceptional points: no noncompact channel remains. Neither epsilon_* nor delta_* is computed, and finite positive-interior U1 components are not excluded.

## 5. Reciprocal metrics: a compact proper-S1/U1 search domain
For any fixed centred polytope K with B_r subset K subset B_R, let the SPD eigenvalues be lambda1>=lambda2>=lambda3>0. If lambda1*r^2>lambda2*R^2, maximize x^T M x separately on K intersect {x dot e1>=0} and K intersect {x dot e1<=0}, where e1 is a top eigenvector. The equatorial section has value<=lambda2 R^2, while +/-r e1 have value lambda1 r^2. Each half has a maximizing genuine vertex strictly away from the equator. It is a local maximum on K, and strict convexity along every incident edge gives strictly negative outgoing derivatives. Thus there are two distinct strict unstable vertices.

Consequently U1 implies lambda1/lambda2<= (R/r)^2. The same geometric argument applies to the actual SAME-ORIGIN polar K* with metric N=M^-1; no uniform density or polar recentering is needed for this radial-maximum statement. Since B_(1/R) subset K* subset B_(1/r), S1 of K implies U1 of (K*,N), hence lambda2/lambda3<= (R/r)^2. Therefore
 S1 and U1 imply condition(M)<= (R/r)^4.
The proof deliberately uses a strict spectral threshold; this weak necessary bound is sufficient for compactness without resolving equality refinements.

On the compact projective parameter sets of Sections3-4 the newly uniform-filled, own-centred bodies have a common r>0 and finite R by centroid continuity and unchanged full-dimensional geometry. Normalize tr(M)=1. The condition bound puts all S1/U1 metrics in a compact subset of SPD: for example lambda_min>=1/(3(R/r)^4). Thus the remaining proper110 search in each fixed E17 projective orbit, and in the entire literal two-cap family, has no parameter-infinity or metric-singularity escape. This supplies no evaluated compact box or finite certificate coverage.

## 6. Remaining scope
These are boundary/compactness theorems, not interior exclusions. The global lower bound remains34 and the canonical proper110 upper attainer remains622. The marked/whole-facet K2 theorem is an independent mechanism. Across arbitrary changing E17 sources, a compact affine-normalized limit may retain10 true vertices or contain more labels on one exposed face; the counts above must not be silently transferred to that larger moduli problem.
