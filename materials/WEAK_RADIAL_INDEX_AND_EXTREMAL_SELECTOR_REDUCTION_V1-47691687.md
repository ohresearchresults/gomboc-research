# material-4769168726df

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# WEAK_RADIAL_INDEX_AND_EXTREMAL_SELECTOR_REDUCTION_V1

Coordinator analytic theorem. This source is a continuation of the full result minimum-0227, SHA256 57bf2cc803fdd3e5ace5587e000d4b1b6372f42306aaff28e467e2b94f1ca8db, read completely in two exact pages. It also uses the definitions and strict-extremum persistence recorded in branch [internal-source-reference], read completely. No independent replay of the parent's control source is claimed or needed. New supplementary exact homogeneous VF control: [internal-source-reference]. Its build and separate check both passed in the coordinator container, with the source/output pins stated there.

## 1. Statement and scope

Let P be a genuine full-dimensional finite convex 3-polytope, o any interior point, and M positive definite. Count ONLY strict stable facet equilibria S, strict unstable vertex equilibria U, and strict saddle edge equilibria H. Permit any additional weak physical contacts of types VE, EF and VF; count a physical point once, not once per incident edge.

Then

                         S + U - H = 2.                 (1)

Every weak physical equilibrium has local radial Euler index ZERO. Stable and unstable strict equilibria have index +1; a strict saddle has index -1. Neither genericity nor homogeneity is needed for this statement. In particular the weak-inclusive actual homogeneous joint S=U=1 family already has H=0. This does NOT make it proper110: weak index-zero points can remain, and their removal in the same realization space is not automatic.

The proof below treats degeneracy rather than applying a theorem stated only for nondegenerate polyhedra. A useful primary reference for definitions and the nondegenerate framework is B. Ludmany, Z. Langi, G. Domokos, Morse-Smale complexes on convex polyhedra, arXiv:2106.11626v2, Sections 1 and 3, especially Definition7. The paper explicitly assumes nondegeneracy in its polyhedral development; we do not cite it as proving (1) with weak contacts. The local proof below is our extension for the present problem.
Primary reference: https://arxiv.org/html/2106.11626v2

## 2. Exact local radial chart

Translate o to0 and use the single physical linear change M^(1/2); after this legitimate congruence the metric is Euclidean. It suffices to prove the claim there. Write P={x:q_f.x<=1}, using only its true maximal facets.

Fix p=r u in the boundary, |u|=1. Let I be the set of its incident facets. All q_f.u=1/r for f in I. For y in u-perp near0 put

u(y)=(u+y)/sqrt(1+|y|^2),
a_f=r proj_(u-perp)(q_f),
A=conv{a_f:f in I},   h_A(y)=max_(a in A) a.y.

The inactive facets have strict slack at p and remain inactive in a sufficiently small angular neighborhood. Therefore the radial function has the EXACT expression

                 R(y)=r sqrt(1+|y|^2)/(1+h_A(y)).         (2)

It follows that

                 R(y)<r iff h_A(y)>sqrt(1+|y|^2)-1.     (3)

The right-hand side is strictly positive for y!=0 and is O(|y|^2). On a ray y=t theta, |theta|=1, the strict lower excursion is empty when h_A(theta)<=0. When h_A(theta)>0 it is a nonempty initial open interval 0<t<T(theta), truncated by the neighborhood radius. This follows directly from (3), or from

d/dt log(R(t theta)/r)=(t-h_A(theta))/[(1+t^2)(1+t h_A(theta))].

The open interval endpoints vary continuously on the open set

                 Omega(A)={theta in S^1:h_A(theta)>0}.  (4)

Choosing a continuous positive radius smaller than both the neighborhood radius and T(theta) gives a section. Radial contraction onto this section shows that the punctured strict lower local excursion has the homotopy type of Omega(A). The same finite local link description can be obtained from a small fixed circle with h_A(theta)>(sqrt(1+epsilon^2)-1)/epsilon; for small enough epsilon the components are the same. No infinitesimal linearization is substituted for a zero first derivative: the positive quadratic term in (3) is essential.

## 3. Geometry of A and local indices

The dimension of A is 0,1 or2 according as p lies in the relative interior of a true facet, edge or vertex. Indeed the incident normalized poles form the corresponding genuine dual face, and projection is an affine isomorphism on its plane q.p=1. Thus a true primal vertex cannot have a spurious collinear A.

Physical equilibrium is equivalent to0 in A: r u belongs to the positive normal cone at p exactly when its tangent projection can be expressed as a convex combination equal to0. With normalized poles their u-components are identical and positive, so the usual positive normal combination and this convex combination are equivalent.

The local radial Euler index is 1-chi(Omega(A)), using the ordinary homotopy Euler characteristic of the descending link. The possibilities are exhaustive:

(a) Strict stable facet: A={0}; Omega is empty, index+1.

(b) Strict saddle edge: A is a nontrivial segment with0 in its relative interior. Its support is positive except in the two directions perpendicular to the segment. Omega is the union of two disjoint open arcs, chi2, index-1.

(c) Strict unstable vertex: A is a full two-dimensional polygon with0 in its interior. Its support is positive in every direction. Omega=S^1, chi0, index+1.

(d) Weak EF: A=[0,a] with a!=0. Omega={theta:a.theta>0}, one open semicircle, chi1, index0.

(e) Weak VE or VF at a vertex: A is a full two-dimensional polygon with0 on its boundary. Since0 belongs to A, h_A>=0. Its zero directions form the intersection of S^1 with the normal cone of A at0. If0 lies inside an edge of A, this is a single direction (VE). If0 is a vertex of A, it is one closed arc of angle strictly less than pi (VF). In both cases its complement is one connected open arc. Hence chi(Omega)=1 and the index is0.

(f) A non-equilibrium point has0 outside A. A strict separating vector e satisfies a.e>0 for every a in A. Each open semicircle {theta:a.theta>0} contains e/|e| and excludes -e/|e|. Their union Omega is one contractible proper arc, so index0. In particular auxiliary stratified critical events at vertices or edge feet which are not physical equilibria have zero contribution.

These are indices of ONE physical point. In case VF, adding separate hypothetical VE, EF or edge indices for the same point would be wrong.

## 4. Why the local index sum equals2, including coincident values

Here the standard Euler proof of the descending-link formula can be made directly on the polyhedral surface. On every open planar facet, squared radial distance is a strictly convex quadratic. Its only possible interior critical event is the perpendicular foot. On every open true edge the restriction is also a strictly convex quadratic and has at most one interior foot. Include all true vertices as potential events. Thus the event set is finite.

Away from these event values, intersections of a moving sphere with the interiors of faces are circular arcs, and their crossings with true edges are transverse. The combinatorics and topology of the sublevel surface are constant between successive event values. Locally at an event, the descending-link Euler formula follows by triangulating the finitely many local arc sectors: adjoining their common event point is adjoining the cone on the descending link, whose relative Euler contribution is 1-chi(link). Equivalently, in an adapted triangulation every simplex is charged to its highest event; the sum of its alternating face counts is this same descending-link index. Ordinary regular subdivisions have an interval as lower link and contribute zero. Formula (2)-(4) gives the actual local lower excursion and its link, including all zero-derivative directions, so the argument does not assume a smooth gradient at an edge or a vertex.

Distinct events at one radial value are handled in disjoint neighborhoods and their contributions add; no perturbation of the actual reference point is necessary. Initially the radial sublevel on the boundary is empty, and finally it is all of the boundary, a sphere with Euler characteristic2. Summing the indices in Section3 proves (1). This is an elementary Euler sweep of a finite piecewise-quadratic radial function, not an application of smooth Morse theory to a nonsmooth function without checking its local data.

## 5. Exact reduced local escape selectors

Return to the parent's true-lattice actual-COM setting. Let X_i be the actual centred vertices, q_f the same-origin poles, and N=M^-1. Use true-edge primitives

P_ij=X_i^T M(X_j-X_i),  Q_fh=q_f^T N(q_h-q_f).

Choose a sufficiently small true-lattice neighborhood preserving every originally nonzero primitive sign, and hence all original strict equilibria with their labels. For every original weak unstable vertex choose at least one originally zero outgoing P to become positive. For every original weak stable facet choose at least one originally zero outgoing Q to become positive. Call these the EXTREMAL groups. No extra group on weak edges is needed.

The following are equivalent in that neighborhood:

(i) All original strict S,U,H labels persist and there are no other equilibria, strict or weak.
(ii) Every extremal group has at least one positive exit.

Proof of (ii)=>(i): Original non-equilibrium vertices/facets have a protected positive exit. Original strict vertices/facets are protected by negative exits. Condition(ii) makes the original weak vertices/facets non-equilibria, so the exact strict S,U are unchanged and there are no weak vertices/facets. Every physical weak point must be VE, EF or VF: the minimal true face containing it lies properly inside the exposed supporting face perpendicular to its radius. In3D the only proper dimension pairs are(0,1),(1,2),(0,2). Thus every weak point belongs to a weak vertex or weak stable facet; none remain. By(1), H=S+U-2 equals its original strict value. All original strict saddle labels persist, so there is no new strict saddle. The converse follows because a group without positive exit leaves its vertex/facet weak or makes it a new strict equilibrium.

This is a reduction of the parent's valid larger selector system, not a refutation of its sufficiency. Edge groups were redundant once convexity, the full physical census and the global index identity are retained. Demanding all algebraic zeros become positive is still an unjustified strengthening.

For a weak VE vertex there is exactly one zero outgoing true P. For a weak EF facet there is exactly one zero outgoing true Q. At VF there are exactly two zero outgoing true P at its vertex and exactly two zero outgoing true Q at its facet. This is because the true exposed edge has one incident ray at an endpoint, whereas a true exposed polygonal facet has exactly two incident boundary edges there; apply same-origin polarity for Q.

Let n_VE,n_EF,n_VF count distinct physical points. Then

n_VE+n_VF <= V-U,
n_EF+n_VF <= F-S.

There are m=n_VE+n_EF+2 n_VF extremal groups and at most4^(n_VF) selectors. Each selector uses exactly m source-distinct true rows. For first-layer weak S=U=1, V10/F9, m<=17 and n_VF<=8, giving at most65536 selectors. This is only an upper bound; compatibility can reduce it. It is NOT a bound on arbitrary nonphysical zero rows.

The parent's full first-order mechanical-balance equations and all-cone second-order criterion apply unchanged to each reduced selector. Its common inverse term N''=2H^2-K and actual moving-volume COM terms remain mandatory. No contact stress is eliminated merely by the16-dimensional parameter count.

## 6. Consequences for the first-layer compact atlas

The weak-inclusive joint S1U1 closed atlas in [internal-source-reference] can contain no STRICT saddles, even though H=0 was not an explicit constraint. Earlier statements leaving H unconstrained remain set-theoretically valid but unnecessarily broad in wording. The hypothesis 'and no strict saddle' in the last open question of minimum-0227 is now automatic for a genuine convex joint S1U1 body.

The real remaining distinction is proper110 versus strict110 WITH weak index-zero contacts. The theorem does not prove density, nonemptiness, a full E17 exclusion, or any improved bound. It applies at the own uniform COM but does not authorize arbitrary changes of that COM during a construction. The interval34<=C_min<=622 and the separate attaining obligation are unchanged.

A concrete next question is whether every physically admissible minimal contact packet on a genuine first-layer S1U1 body has a reduced selector free of full realization-space positive stresses, or one with a positive second-jet direction for the entire stress cone. Any failure must now be a true simultaneous extremal-contact obstruction, not a hidden strict saddle or redundant edge-selector incompatibility.
