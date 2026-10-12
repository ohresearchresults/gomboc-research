# material-c2fe832ad973

AI research material

---

# RANK2_ZERO_ARROW_STRICT_LIFT_ALTERNATIVE_AND_RECIPROCAL_TAIL_V1

## Scope and evidence
Coordinator analytic result. No numerical search, executable computation, new polyhedron, census, or bound improvement is claimed. This source contains the complete argument. It applies to any fixed full-dimensional convex three-polytope P with 0 in its interior, using its true vertices and true edges. For the homogeneous problem these coordinates must be centred at the actual volume centroid; this theorem never changes that body or its centroid. It resolves the previously open zero-arrow lifting alternative at a FIXED rank-two metric, not actual coverage of all shapes or kernels. It also identifies precisely why a lift close to that singular metric is not itself a proper110 construction.

Write vertices x_i as columns. For an oriented true edge e=(i,j), let
 A_e = sym(x_i (x_j-x_i)^T),
 D_e(M) = tr(M A_e) = x_i^T M(x_j-x_i).
Here sym(B)=(B+B^T)/2 and M is the primal physical metric. A rooted tree T is oriented from every nonroot vertex toward a specified root a. Fix M0 positive semidefinite of rank two, with unit kernel vector k, and suppose D_e(M0)>=0 for all e in T. Define Z={e in T:D_e(M0)=0}.

## 1. Exact lift theorem, including nonsmooth and higher-order proposed paths
The following are equivalent:
(A) Some SPD M satisfies D_e(M)>0 for EVERY e in T.
(B) Some symmetric Delta and epsilon0>0 satisfy: M0+epsilon Delta is SPD and all D_e(M0+epsilon Delta)>0 for every 0<epsilon<epsilon0.
(C) The strict LINEAR system in Delta is feasible:
       k^T Delta k > 0;
       tr(Delta A_e)>0 for every e in Z.
Only the zero arrows appear in (C).

Proof A=>C: take Delta=M-M0. Its kernel entry is k^T M k>0, and on each zero arrow its primitive equals D_e(M)>0. This implication requires neither proximity of M to M0 nor any differentiability of a proposed path. Proof C=>B is the block estimate below; B=>A is immediate. Thus there is no hidden second-order-only lift for a fixed weak tree. Conversely, failure of (C) excludes that tree's strict feasibility at EVERY SPD metric, not just near M0.

For an explicit bound choose orthonormal coordinates k=e3 and write
 M0=diag(H0,0), H0 SPD;
 Delta=[[B,u],[u^T,d]], d>0.
Set h=lambda_min(H0), b=||B||op, v=||u||. Impose
 0<epsilon<1,
 epsilon b < h/2 when b>0,
 epsilon v^2 < d h/4 when v>0.
Then H0+epsilon B >= (h/2)I, while its Schur complement is at least epsilon d/2>0. For each e in T\Z having c_e=tr(Delta A_e)<0 also impose
 epsilon < D_e(M0)/(2|c_e|).
There are finitely many strictly positive upper bounds. Every originally positive tree arrow stays positive; every zero tree arrow becomes epsilon tr(Delta A_e)>0. This is a constructive pencil, not an unspecified limiting argument.

The body remains unchanged. Under any SPD metric with all tree arrows strictly positive, every nonroot vertex has a positive escape and the root is STRICT unstable. Indeed D_ij>=0 on a nonzero edge gives
 |x_j|_M^2-|x_i|_M^2 = 2D_ij+|x_j-x_i|_M^2 >0.
If the root had a nonnegative outgoing edge, following that edge and then the selected tree back to the root would give an impossible norm-increasing cycle. Thus there is exactly one unstable vertex and there is no weak vertex equilibrium. This by itself says nothing about the numbers of stable facets and saddles.

## 2. Complete dual obstruction and its weak/strict distinction
System (C) is infeasible if and only if there are lambda0>=0 and lambda_e>=0, not all zero, satisfying
       lambda0 k k^T + sum_(e in Z) lambda_e A_e = 0.       (2.1)
At least one arrow weight is nonzero.

A self-contained separation proof: take the finite set consisting of kk^T and the A_e, and its compact convex hull K in the Euclidean space of symmetric matrices. If 0 belongs to K, a normalized convex combination gives (2.1), which contradicts any strictly positive inner products. If 0 does not belong to K, let Q be the point of K closest to 0. The first variation toward any B in K gives tr(QB)>=||Q||_F^2>0. Taking Delta=Q satisfies (C). This proves both alternatives, including all zero boundaries.

For ANY SPD M, identity (2.1) yields
       sum lambda_e D_e(M) = -lambda0 k^T M k <=0.
If lambda0>0, the selected zero-arrow subsystem cannot even be ALL WEAK at an SPD metric. If lambda0=0, it cannot be ALL STRICT; weak feasibility can remain on the simultaneous equality face. These two certificate strengths must not be conflated. Proper110 without extra weak vertex equilibria needs a strict escape tree, but a count of strict unstable vertices while allowing weak vertex contacts is a different condition.

## 3. At most FIVE zero arrows suffice to obstruct a rank-two lift
Normalize k^T Delta k=1, which is allowed by positive scaling. Adding any scalar multiple of M0 to Delta does not change this entry or any zero-arrow inequality. Fix the gauge tr(M0 Delta)=0. These are two independent affine conditions on Sym3, leaving an affine space of dimension FOUR. Each zero arrow is one strict affine halfspace in that four-dimensional space.

If their intersection is empty, at most five of those halfspaces already have empty intersection. For completeness, the finite Helly argument here does not require closed halfspaces: in a minimal empty family choose, for each member i, a point w_i satisfying all other members. If there were more than d+1 members in dimension d, a Radon partition of a dependent subset of the w_i would give a point in the convex hull of each part. For every halfspace, at least one part uses only points strictly satisfying it. Their common convex-hull point therefore lies in every open halfspace, a contradiction. Here d=4.

Applying section2 to that subfamily gives an obstruction (2.1) supported on at most FIVE zero arrows, plus the kernel term if needed. The support may depend on the body, metric, root and tree. This is not one universal five-arrow list and is not a new exclusion of all E17 trees. It is sharper than treating all six entries of Delta as independent, and it explains why a small exact linear certificate suffices at a fixed rank-two boundary point.

For rational vertex coordinates and rational M0 (using a rational nonzero kernel vector rather than unit normalization when convenient), all constraints are rational. A feasible strict system has a rational solution by density in its open feasible set; one can scale its positive margins to at least1. An infeasible system has a rational nonnegative dependence obtained by solving the finite rational linear system. This is an exact finite linear-algebra decision problem; no floating tolerance is part of the theorem.

## 4. Finite-tree alternative for ALL nearby robust U1 metrics
Call robust U1 a metric at which the root is strict unstable and EVERY other vertex has a strictly positive true-edge escape. This excludes additional weak vertex equilibria. For a fixed root and M0, the existence of arbitrarily close robust U1 metrics is equivalent to feasibility of (C) for at least one rooted tree which is weak at M0.

Necessity: from each approaching robust U1 metric choose one positive outgoing edge at every nonroot. Strict norm increase makes these choices a rooted tree. There are finitely many choices, so a subsequence uses one fixed T. Its limit inequalities are weak at M0; section1 then gives (C). Sufficiency is its explicit straight-line lift. No rotating sequence of trees or nondifferentiable metric curve can escape this finite alternative.

If all weak trees at M0 fail (C), a genuine neighborhood of M0 contains no robust U1 metrics for this root. Each weak tree is globally strictly infeasible by section2. Every other tree has at least one arrow negative at M0, which remains negative in a sufficiently small neighborhood. Taking the minimum over this finite list gives a neighborhood excluding them all. An explicit Frobenius-radius guard for an arrow with D_e(M0)<0 is -D_e(M0)/(2||A_e||_F). This requires actual complete tree/zero-arrow coverage; merely finding several short obstructions is not coverage.

Equivalently one may enumerate positive-escape choices only at vertices lacking an already positive M0 escape, while preserving the true graph and ensuring the resulting choices reach the root. Shadow boundary edges may not be substituted for genuine edges without a separate fibre argument.

## 5. Generic weak-free U1 is available after a strict lift, but S1 is separate
The strict SPD/tree conditions define a nonempty open set once a lift exists. Inside it one can avoid all finitely many primal and reciprocal facet-adjacency primitive zeros. Each primal primitive is a nonzero linear polynomial in M: sym(x_i(x_j-x_i)^T) cannot vanish for a true edge with x_i nonzero. Each reciprocal primitive is the corresponding nonzero linear polynomial in N=M^-1, transported by an analytic diffeomorphism of the SPD cone. Its zero set also has empty interior. A finite union of these proper zero sets cannot exhaust the open tree cone.

Avoiding all these zeros is a sufficient condition for no physical weak contacts: vertex/edge endpoint contacts are primal adjacency zeros, and edge/facet boundary contacts are reciprocal facet-adjacency zeros. The conclusion is existence of a nearby metric with U1 and no physical weak equilibrium, NOT S1 or H0. An arbitrary prescribed one-parameter pencil can lie in an unrelated zero set, so the generic perturbation is within the full open metric neighborhood, not necessarily on that pencil.

## 6. Reciprocal rank-one obstruction: every sufficiently small lift has S>=2
This crucial limitation uses the SAME body and reciprocal physical metric. Let Q=P polar, with true facet poles q_f as its vertices. Since 0 is interior to P, it is interior to Q. Put J0=adj(M0). It is a positive multiple of kk^T and has rank one. Let alpha=max_f k.q_f>0 and beta=min_f k.q_f<0. Their exposed vertex sets T+ and T- in Q are nonempty and disjoint.

For any true polar edge f->g leaving T+,
 q_f^T J0(q_g-q_f) = c alpha(k.q_g-alpha)<0,
where c>0. For an edge leaving T-, the same expression is c beta(k.q_g-beta)<0. Both exposed sets therefore have strictly negative outgoing boundaries under J0. Internal zero edges do not supply exits. Boundary signs remain negative for every positive-definite matrix sufficiently close to J0. In each exposed set choose a vertex of maximal positive-definite norm; its internal incident arrows are strictly negative by the norm identity in section1, and its external arrows are negative by the boundary guards. There are therefore at least TWO strict unstable polar vertices.

For a primal facet q_f.x=1, its M-minimum-norm point is Nq_f/(q_f^T Nq_f). It is in the relative interior of the true facet exactly when
 q_f^T N(q_g-q_f)<0
on all neighboring facets. Thus strict unstable vertices of (Q,N) are precisely strict stable facets of (P,M). Positive rescaling of N changes no sign. Since adj(M0+epsilon Delta) tends to J0 and is a positive multiple of N for epsilon>0, every sufficiently small SPD lift has at least TWO strict stable facets.

A completely explicit algebraic tail bound is available. Write
 adj(M0+epsilon Delta)=J0+epsilon J1+epsilon^2 J2,
 J2=adj(Delta), J1=adj(M0+Delta)-adj(M0)-adj(Delta).
For every polar edge leaving T+ or T-, set
 a=-D_fg(J0)>0, b=D_fg(J1), c=D_fg(J2).
Along with the bounds in section1 impose epsilon<1 and, when |b|+|c|>0,
 epsilon < a/[2(|b|+|c|)].
Then every selected outgoing boundary stays at most -a/2. This gives an exact positive interval with BOTH primal U1 and primal S>=2 whenever the lift system is feasible.

Consequently the singular-lift interval is NOT a proper110 attainer. After the generic weak-contact removal of section5, the ordinary equilibrium index gives (S,U,H)=(s,1,s-1) with s>=2. A later continuation at finite distance from the singular boundary may still change the stable count; this theorem does not exclude that possibility or an SPD110 component bounded away from singularity.

## Scientific consequences and limits
The formerly tentative first-order zero-arrow reduction is now an exact necessary-and-sufficient finite linear alternative; nonsmooth and higher-order-only escapes are covered. Every failed tree lift has a certificate using at most five zero arrows, with a precise distinction between excluding weak and excluding strict arrows. A full set of such certificates excludes a neighborhood, not merely one limiting matrix. Conversely a feasible system supplies an explicit robust U1 pencil and generic weak-free U1 controls, but the reciprocal argument proves S>=2 throughout its sufficiently small tail. This separates a useful U1 construction mechanism from the actual common-metric110 obligation.

No actual seven-to-ten-corner shadow has been constructed here. No shape family, canonical type count, lower complexity bound or upper complexity record is changed. The current minimum interval remains34<=Cmin<=622. The actual unequal shadow geometry and finite-distance S1/U1 compatibility remain substantive open directions.
