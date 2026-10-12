# material-4263f2c0cdd5

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# MIXED_5P5Q_PACKET_COVER_COMPLETENESS_V1

Coordinator analytic result. This is a general convex-geometric theorem applied to the actual common-inverse research frontier, not a new E17 exclusion. The motivating completed result is minimum-0229, SHA256 325b2943769ef476fd483b07ac9289dcfd2b090aef1847f44a0df8e59eabd187, read from cursor 0 through eof in this turn. Its literal actual cylinder, labels, moments and recovery remain authoritative. No computational replay or new computed body is asserted.

## 1. Fixed-shape theorem

Let E and F be real affine spaces of dimension d. Let K be a nonempty compact convex subset of E x F. A primal row p_i depends affinely only on a in E, and a polar row q_j depends affinely only on b in F. A packet is feasible when (a,b) belongs to K and all its rows are nonnegative.

If a finite packet is infeasible, there is an infeasible subpacket of one of the following types:

* at most d+1 primal rows and no polar rows;
* at most d+1 polar rows and no primal rows;
* at most d primal rows AND at most d polar rows.

In particular, for d=5 every excluded packet has a strictly separating subpacket with either at most six rows on one side, or at most 5+5 rows when both sides are needed. A mixed inclusion-minimal excluded packet has at most five rows on each side. The universal total bound is ten, improving the independent six-per-side compression in this application.

### Proof

Choose an inclusion-minimal infeasible subpacket, partitioned as I,J. First suppose both I and J are nonempty. Minimality implies K with only the J constraints is nonempty. Let D be its projection to E; D is nonempty compact convex. The primal halfspaces H_i={a:p_i(a)>=0} have nonempty total intersection: otherwise the I constraints alone would be infeasible even without K, contradicting minimality since J is nonempty.

Yet D intersected with all H_i is empty. Helly's theorem in dimension d supplies an empty intersection of at most d+1 of these convex sets. This subfamily MUST include D because every subfamily of the H_i has nonempty intersection. Hence at most d primal halfspaces already contradict D. Minimality forces |I|<=d. Interchanging E,F gives |J|<=d.

If only I is present, apply Helly to the projection of K to E and the primal halfspaces. At most d+1 primal rows suffice; when the halfspaces themselves have nonempty intersection, at most d suffice. The polar-only case is identical.

For completeness, the finite Helly fact used here follows from Radon's argument: d+2 points are affinely dependent and split into two sets with intersecting convex hulls. In an inclusion-minimal empty family of more than d+1 convex sets, select a point in all but each one of d+2 selected sets. The Radon intersection then belongs to every set, a contradiction; the usual induction removes any additional sets. No numerical or generic-position premise is used.

## 2. Positive-gap certificate, including weak signs

List the rows in such a subpacket as f_1,...,f_m and set

 delta = min_{x in K} max_i[-f_i(x)].

Compactness and emptiness of the simultaneous closed nonnegative halfspaces give delta>0. Convex minimax for the affine functions gives

 delta = max_{lambda_i>=0, sum lambda_i=1} min_{x in K}[-sum_i lambda_i f_i(x)].

One direct justification is separation of the compact convex row image {f(x):x in K} from the closed nonnegative orthant. The separating normal has nonnegative coordinates because the orthant is unbounded in every positive coordinate. The two sets have positive distance; normalize the nonzero normal to sum one. This gives a strictly positive lower bound, which is sufficient here without needing the minimax equality.

Thus a positive-gap dual witness exists using the same at-most-ten rows. In a mixed inclusion-minimal packet its coefficients can be chosen positive on every retained row: a zero coefficient would give an infeasible proper subpacket. This last statement concerns a minimal packet, not arbitrary redundant coefficients returned by an optimizer.

The rows are weakly required >=0; exclusion does not rely on moving them to strict inequalities or on discarding weak contacts.

## 3. Physical application and exact dimension

At one genuine homogeneous body with actual volume centroid g and covariance C>0, use the two trace-normalized matrices

 A=C^(1/2) M C^(1/2)/tr(CM),
 B=C^(-1/2) M^-1 C^(-1/2)/tr(C^-1 M^-1).

Each lies in the five-dimensional affine space of symmetric 3x3 matrices of trace one. Fix any compact allowed spectral domain for the reciprocal pair and let K be its convex hull in this ten-dimensional affine product. For the accepted finite-height caps this is the exact capped reciprocal hull; no special formula for that hull is needed in Sections 1-2.

A true primal arrow divided by tr(CM) is affine (indeed linear in the ambient matrix coordinates) in A only. A true same-origin polar arrow divided by tr(C^-1 M^-1) is affine in B only. Consequently the theorem applies with d=5. It retains actual geometry, the moving uniform centroid and one actual covariance in defining the rows. It does not authorize independently chosen facet centroids, polar recentering, or replacement of true edges by integration diagonals.

For any selected complete 9-primal/8-polar E17 escape packet that is excluded by this convex hull, a six-row one-sided or five-plus-five mixed positive-gap subpacket is enough. This is a bound on a certificate support, NOT on the number of mechanically possible trees or physical weak contacts.

## 4. Compact families: pointwise hull exclusion implies a finite local packet cover

Let T be a compact parameter set of genuine bodies. Suppose actual centroid/covariance and all labelled arrow rows depend continuously on t in T, and use the same normalized capped hull K for every t. Let P be a FINITE list of complete packets whose selection is necessary for the physical class under consideration. The theorem does not establish that necessity; it must come from the accepted actual escape-tree or complementary-tree reduction used in the application.

Assume every packet P in the list is hull-infeasible for every t in T. For any fixed pair (t,P), Sections 1-2 choose an at-most-ten-row support and positive weights with a strict uniform-in-K gap. Continuity gives the same support and weights, with a smaller positive gap, on a relative neighborhood of t. Compactness of T and finiteness of the packet list supply finitely many such local certificates covering all (t,P).

Hence no obstruction from continuously choosing one optimal support or one optimal dual witness exists: different overlapping cells may use different supports. A single global arrow packet or a single optimal witness is not required. Conversely, a finite exact cover of this kind excludes the physical class only if it covers EVERY necessary complete-packet alternative at EVERY shape, including all roots and closed boundaries.

The result is existential and does not bound the number of shape cells, the coefficient bit sizes, subdivision depth, or the computational effort. Numerical samples alone do not produce the required cover.

## 5. Moving-covariance dual witnesses

The literal H5 result provides a useful local implementation. Given C0>0 and a symmetric dual matrix W0 at a centre shape, put H=C0^-1 W0 and, for the true varying covariance C, set

 W(C)=(C H+H^T C)/2.

Then W(C0)=W0 and tr(C^-1 W(C))=tr(H) exactly. Thus strict dual slacks at a centre persist locally without freezing the actual covariance or its centroid. Rational approximation of H and scalar witnesses is safe after reserving a strictly positive slack and objective margin; all relevant functions are continuous on the compact spectral range. A finite rational cover needs exact enclosure of all slacks, as in H5, not just continuity assertions or endpoint sampling.

This paragraph is a preservation of the H5 transport mechanism, not a claim to have reconstructed its complete Taylor verifier or a claim of global certificate coverage.

## 6. Sharp method boundary and the next decisive fork

Convexity of K is ESSENTIAL. The physical reciprocal graph itself is generally nonconvex. An exact common-inverse packet can be infeasible while its convex-hull relaxation is feasible. Such a packet has NO positive-gap joint-linear arrow certificate, with ten rows, twelve rows, or any other support size.

Indeed, if one point of K satisfies all rows of a complete packet, every subpacket and every nonnegative linear combination also pass at that point. Accumulating further certificates against subpackets of that same complete packet cannot remove this relaxed witness. Nonlinear reciprocity, additional physical geometry, or a different relaxation is then needed.

For the H5 cylinder, the practical continuation is therefore a genuine fork: obtain a covering family of small mixed packets for all remaining complete orientations; OR give an actual body in the cylinder and a feasible CAPPED HULL witness for one COMPLETE selected primal/polar packet, showing exactly where the joint-linear programme stops. H5's separately capped independent three-row control is not yet such a witness: independent feasibility is weaker than membership in the exact coupled hull, and three rows are not complete S1/U1 trees.

No new actual shape cell, complete orientation class, or first-layer type is excluded by the abstract support theorem alone. The bounds remain 34<=C_min<=622, and a lower exclusion and an attaining construction remain separate obligations.
