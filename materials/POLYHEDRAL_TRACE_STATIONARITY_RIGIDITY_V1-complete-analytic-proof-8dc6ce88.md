# material-8dc6ce881229

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# POLYHEDRAL_TRACE_STATIONARITY_RIGIDITY_V1

## Determination and exact scope

For fixed 0<b<1 and c,d>0, every POLYHEDRAL Hausdorff local maximum of the original adjacent-triangle trace in the full marked support-patch class defined below has at most 90 true vertices. This includes arbitrarily many initially allowed positive-ell auxiliary vertices. A sharper local statement says that every unprotected facet containing exactly one canonical point is a triangle with rigid values of a particular affine first-variation density at its vertices.

This is an analytic theorem, not a numerical exclusion and not a claimed global 90-vertex supremum reduction. In particular, no proof is given that the unrestricted convex-body maximum has a polyhedral maximizer. The theorem does not preserve an input face lattice, its full first moment, its own centroid, or mechanical equilibrium counts. It changes neither the accepted 34<=Cmin<=622 interval nor the open true10/17/9 layer. The local-maximum hypothesis is in the class with ALL face lattices and vertex counts allowed, not merely within one realization stratum.

## 1. The actual-body problem

Put A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0), and T0=conv(A,B,C,D). Define

    ell(x,y,z)=1+(d-1)x+(c-1)y+(b-1)z,
    n(x,y,z)=(1+b+c)x+(1+b+d)y.

The marked support-patch class consists of bounded, full-dimensional convex bodies P such that

    T0 subset P subset {x>=0,y>=0,ell>=0},

and P intersect {ell=0} has positive two-dimensional area. In this note P is a polytope at the proposed local maximum, but its competitors may have different true face lattices. The coordinate support faces may be larger patches containing ABC and ABD. In particular, C and D need not be true vertices. A root facet means a genuine positive-area maximal facet, not a collapsed support set.

All integrals use the ORIGINAL uniformly filled body in these coordinates. Write

    V=int_P 1, B_ell=int_P ell, N=int_P n,
    T(P)=N/(6 V B_ell).

The retained tetrahedron gives V>0, B_ell>0 and N>0. Define

    q=N/B_ell, r=N/V,
    g=n-r-q ell.

This is an affine function fixed at the candidate P. We have

    int_P g=-N<0,
    g(A)=-r-q<0, g(B)=-r-qb<0,
    partial_z g=q(1-b)>0.

Throughout the proof, auxiliary means a TRUE vertex of P not equal to A,B,C,D. It does not mean a redundant input label. Positive-ell auxiliary vertices and auxiliary root vertices are both covered.

## 2. Exact finite variation test

For a disjoint added region R write w=int_R1, e=int_Rell, f=int_Rn. Direct cross multiplication, with positive denominators, gives

    T(P union R)>T(P)
      iff f-rw-qe > N w e/(V B_ell)
      iff int_R g > N w e/(V B_ell).

This formula is used only when the union is the actual convex competitor under consideration. For removal R subset P, with the remainder convex and with positive volume and ell-integral,

    T(P minus R)>T(P)
      iff -int_R g > N w e/(V B_ell).

For small local regions near the fixed bounded body, e=O(w), so the right side is O(w^2). These exact tests avoid replacing a finite trace variation by an unjustified sign heuristic.

## 3. Every auxiliary vertex has strictly positive g

Suppose v is an auxiliary true vertex. If g(v)<0, cut off a sufficiently small cap at v, avoiding all four canonical marks. On that cap the average of g remains strictly negative. The removed volume tends to zero, and the exact removal test improves T. The coordinate inequalities, containment of T0 and positive root area persist. Thus g(v)>=0 at a local maximum.

The equality case needs a thin-edge cap, rather than a generic homothetic vertex cap. Assume g(v)=0. Some incident true edge vX has g(X)<0. Indeed, otherwise g would be nondecreasing in every edge direction of the tangent cone at v, so v would minimize g on all of P, contradicting g(A)<0.

Choose an affine function h0 nonnegative on P and zero exactly on the edge vX; a positive sum of the two incident facet slacks supplies it. Choose an affine function h1 nonnegative on P, zero exactly at v, and scaled to h1(X)=1. Because v is not canonical, choose 0<eta<1 smaller than h1(Y) for every canonical mark Y on that edge. For small epsilon>0 remove

    R_epsilon=P intersect {h0+epsilon h1<epsilon eta}.

All canonical marks remain: those outside the edge have a fixed positive h0, while those on it have h1>eta. The root retains positive area. The new bodies converge to P in Hausdorff distance, since the removed wedge is transversely O(epsilon), including at v; no fixed-length edge is removed at a fixed transverse depth.

Parametrize the edge by (1-t)v+tX. Away from its endpoints, the transverse tangent wedge is fixed. Its cross-sectional area in R_epsilon is

    k epsilon^2(eta-t)^2+o(epsilon^2), 0<t<eta,

with k>0. The endpoint region at v has only O(epsilon^3) volume. Fubini or a direct wedge-coordinate integration therefore gives

    vol(R_epsilon)/epsilon^2 -> k eta^3/3,
    (int_R_epsilon g)/vol(R_epsilon) -> eta g(X)/4<0.

The exact removal test again strictly improves T. Consequently

    g(v)>0 for EVERY auxiliary true vertex.                 (P)

As a useful corollary, P intersect {x=y=0}=AB at a local maximum. On this axis g=-r-qell<0. The two endpoints of the axis segment are true vertices of P because both x>=0 and y>=0 are supporting inequalities. By (P) they must be canonical; the only canonical axis points are A,B. In particular A and B are true vertices even in the enlarged support-patch class.

## 4. A necessary inequality on every unprotected facet

Call the three facet planes x=0, y=0, ell=0 protected. Let F be any other true facet, with area centroid c_F. Take p in relint F and move it a small positive distance outward from P, obtaining p_epsilon. For a sufficiently small displacement, the only violated supporting plane is F. Thus

    conv(P,p_epsilon) minus P

is exactly the pyramid with base F and apex p_epsilon. It stays in the protected halfspaces and retains T0 and the root. An affine function averaged over this pyramid has value

    (3g(c_F)+g(p_epsilon))/4.

The addition test rules out a positive limiting value. Taking p to any maximizing point of g on F, through relative-interior points and choosing smaller outward distances as necessary, proves

    max_F g + 3 average_F g <= 0.                            (A)

In particular an unprotected facet cannot have g positive everywhere. Since auxiliary vertices have positive g, every unprotected facet contains at least one canonical point. A facet of constant positive g is impossible.

## 5. One-canonical facets are rigid triangles

Let F contain exactly one canonical point X. Necessarily X is a true vertex of F and g(X)<0: all other true vertices are auxiliary with positive g, and otherwise (A) would fail. Thus no interpretation of a redundant canonical point as a vertex is being made.

Keep the other supporting halfspaces fixed and tilt the plane of F through X. For small parameters of either sign, the resulting bounded convex polytope stays in the marked class. The other canonical points are strictly off this plane, the root retains positive area, and all protected planes stay fixed. Nonsimple vertices may split; that is allowed and is precisely why this argument is not restricted to a fixed-lattice tangent space.

For an affine normal displacement L on F with L(X)=0, the actual first variation is proportional to int_F g L. Edges have zero area and do not change this Hadamard first-variation formula, even if the face lattice changes on the two sides. Both parameter signs are feasible, so stationarity holds. Choose L=g-g(X). Then

    int_F g(g-g(X))=0.                                     (T)

Scale g on F by -g(X)>0, so its value at X is -1. Fan-triangulate F from X using its actual boundary vertices. On a fan triangle the other two normalized g-values u,v are strictly positive. Let E denote the area-weighted average over these triangles and put

    S=E(u+v), Q=E(u^2+v^2+uv), M=max_F g.

The exact affine first and second simplex moments turn (T) into

    Q+S=1.

The necessary addition inequality (A) becomes

    M-1+S<=0.

Because u,v<=M,

    Q+S<=3M^2+2M,

so M>=1/3. On the other hand

    u^2+v^2+uv <= (3M/2)(u+v),

hence

    1=Q+S <= (1+3M/2)S <= (1+3M/2)(1-M).

The last expression is less than one for M>1/3. Therefore M=1/3, and every inequality is an equality. In particular all non-X true vertices have normalized g-value 1/3. They lie on one affine level line in F. A polygon can have at most two true vertices on that line. Therefore F is a triangle [X,Y,Z], and

    g(Y)=g(Z)=-g(X)/3.                                    (R)

This proof treats an entire nonsimplicial facet at once. It does not assume that an individual auxiliary vertex has a nonzero fixed-volume motion.

## 6. At most nine special facets

Let S be the set consisting of the root facet and every facet containing at least two distinct canonical points. Let s=|S|. The coordinate facets F_x and F_y contain ABC and ABD respectively.

Two distinct points of a convex three-polytope can belong together to at most two true facets: if the smallest common face has dimension two there is one, and if it has dimension one it is an edge with exactly two. This statement also applies to nonvertex canonical marks.

The pair AB already lies in both coordinate facets, so it supplies no additional facet. Each of AC,BC,AD,BD lies in its coordinate facet and can supply at most one further facet. The pair CD supplies at most two. Every additional facet with at least two canonical marks uses at least one of these available pair incidences. Counting facets by available incidences can overcount but cannot undercount. Finally add the root. Thus

    3<=s<=2+4+2+1=9.

Every facet outside S is an unprotected one-canonical triangle of Section 5.

## 7. Every auxiliary vertex meets a special facet

Suppose an auxiliary true vertex p meets no facet in S. Every incident facet is then an ordinary triangle containing one canonical vertex and two auxiliary vertices. In the vertex link at p, canonical and auxiliary neighbors alternate. The link has at least four vertices, and therefore p has at least two distinct auxiliary neighbors q1,q2.

By (R), each auxiliary neighbor has the same g-value as p. Every canonical neighbor has negative g-value. Thus p is a local maximum of the affine function g on its edge tangent cone, and hence a global maximum on P. The two true edge directions pq1 and pq2 cannot be collinear: coincident positive directions would not give distinct edges, while opposite directions would make p nonextreme. Therefore p,q1,q2 span a two-dimensional exposed face on which g is a positive constant. Since g is nonconstant in space, this is a facet.

It cannot be unprotected, by (A). It cannot be a coordinate facet because each coordinate facet contains A and B with different g-values (0<b<1). It cannot be the root because on ell=0 the function is n-r, which is nonconstant there: grad ell has nonzero z component whereas grad n has zero z component and is nonzero. This contradiction proves that every auxiliary vertex is incident to at least one special facet.

## 8. Counting true vertices

Let L be the set of distinct positive values -g(X)/3 from canonical points X with g(X)<0. Its size l is at most four. Every auxiliary vertex incident to an ordinary triangle has g-value in L, by (R), and also lies on a special facet, by Section 7.

No special facet is constant at a positive g-level. For the root and coordinate facets this was proved in Section 7; for any other special facet it follows from (A). Therefore the intersection of a special facet with a prescribed level from L is a line segment or is empty, and has at most two true vertices of P. This bounds the auxiliary vertices incident to ordinary triangles by

    2 s l.

The remaining auxiliary vertices meet only special facets. Form the polyhedron Q by intersecting just the s special supporting halfspaces. It is full-dimensional and contains P. At each of those remaining vertices the incident special normals already span R^3, since they are all the incident normals of P at that true vertex. Thus every such point is a vertex of Q.

A full-dimensional three-dimensional polyhedron with at most s facets has at most 2s-4 vertices. For completeness: if it is bounded, this is Euler's bound. If it has lineality, it has no vertices. Otherwise its recession cone is pointed. A plane transverse to the cone, placed beyond all finite vertices, truncates it to a bounded polytope with at most s+1 facets and at least three new cap vertices. Euler gives at most 2s-2 total vertices after truncation, and hence at most 2s-5 old vertices. The weaker uniform bound 2s-4 suffices.

Adding at most four canonical vertices gives

    V_true(P) <= 2sl+(2s-4)+4 = 2s(l+1) <= 90.

If c=d then g(C)=g(D), so l<=3 and the same argument gives V_true<=72. If g(C),g(D)>=0, then l<=2 and V_true<=54. These refinements remain conditional local-maximum statements, not global trace estimates.

## 9. Relation to earlier work and the unresolved next step

The exact finite variation formulas and the whole-facet tilt complement the preserved individual fixed-volume auxiliary slide of minimum-0128, SHA 9b8fa9986220926caf778450ec66563e7e5fe300aa1c9fb53433306b415efa34. That source was fully read through EOF. Its two individually rigid positive-ell auxiliary vertices are not being renamed or merged with the older jb58 construction. The fully read ROOT_ONLY_TRANSVERSE_FACE_REDUCTION_V1, material [internal-source-reference], SHA 5052276824a0f332449deeb71c26427470ebb70eb1201728d8f985722aebc333, supplies a DIFFERENT finite, constructive supremum reduction only when every noncanonical vertex is on the root. The present theorem does not replace its finite-wall proof or strengthen it to all auxiliary vertices by implication.

A positive trace improvement of a marked patch can be transferred to a sufficiently close proper triangular-pair body by choosing a point q in the relative interior of the root with x(q),y(q)>0 and forming conv(T0,(1-epsilon)P+epsilon q). The protected coordinate intersections then are exactly ABC and ABD and the root remains positive-area. Actual V,B_ell,N converge. This transfers STRICT inequalities, not equalities, moment preservation, stationary character, or a fixed f-vector.

The remaining essential question for using the 90-vertex bound globally is polyhedral attainment or a finite improving construction. General compactness of a high-trace convex-body domain by itself does not supply a polyhedral maximizer. Smooth or ruled free boundaries may require additional analysis. No assertion that such boundaries are absent, and no finite ascent termination theorem for the new facet tilts, is made here.
