# material-bca38da0cd0c

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# COORD_SINGLE_CAP_MASS_EXISTENCE_V1

## Evidence identity and scope

Coordinator-authored analytical continuation of the convex facet-mass potential in immutable result figure-0389, SHA-256 7f850f1836d56b8b176c68b6450d4196ecb0bbdd67db15039b4f22673fcbe19a. That result was read from cursor 0 through eof:true before this derivation. The result established uniqueness conditional on existence. The argument below supplies existence under an explicit one-cap boundedness hypothesis. It does NOT supply a new own110 polyhedron, preserve equilibrium counts, preserve a chosen incidence chamber, or assert rationality of the minimizing plane. No numerical execution is used in the proof. No priority or novelty over the literature is claimed.

## Theorem: existence of the physical mass-closing cap

Let H be a closed full-dimensional convex polyhedron in R^3 with 0 in int(H). Suppose there exists q0 such that Q(q0)=H intersect {x:q0 dot x<=1} is bounded. Then there is q* for which Q(q*) is bounded, full-dimensional, and its actual uniformly filled first moment is zero. The physical body Q(q*) is unique. If H is unbounded, or H is bounded with nonzero first moment, the correcting plane is active and its normalized vector q* is unique. If H itself has centroid zero, the unique corrected body is H; several redundant q can represent it.

The same proof works in every finite dimension, but the quantitative bound below is stated in dimension three.

## Proof, including unbounded H

Define the extended-valued potential

Phi(q)=integral_H max(0,1-q dot x) dx.

It is convex as an integral of nonnegative convex functions. It is lower semicontinuous by Fatou's lemma.

Let R=rec(H) be the recession cone. The finite domain of Phi is precisely

D={q: q dot v>0 for every nonzero v in R}.

For bounded H, R={0} and D=R^3. For unbounded H, if q dot v<=0 for a nonzero recession direction, choose a small ball around zero on which 1-q dot x>=1/2. Translating a transverse disk in this ball along t v, t>=0, stays in H and keeps the integrand at least 1/2. This gives an infinite cylinder of positive cross-section and hence Phi(q)=infinity. Conversely, if all recession products are positive, Q(q) has no nonzero recession direction and is bounded; the integrand vanishes outside Q(q), so Phi(q) is finite. Because R is closed polyhedral, the strict condition is open: on R intersect the unit sphere the positive continuous product has a positive minimum. Equivalently one may use the finitely many extreme rays. The assumed q0 belongs to D, so Phi is proper.

Choose a>0 with [-a,a]^3 subset H. For any coordinate i, Jensen's inequality in the other two coordinates gives

Phi(q)>=4 a^2 integral_{-a}^{a} max(0,1-q_i t) dt
       >=4 a^3+2 a^4 |q_i|.

Taking a coordinate with maximal absolute value proves coercivity. In particular every q with Phi(q)<=Phi(q0) satisfies the explicit rational bound

||q||_infinity <= (Phi(q0)-4 a^3)/(2 a^4).

The expression on the right is nonnegative because q0 itself obeys the lower bound. Thus the nonempty sublevel set through q0 is compact. A minimizing sequence has a convergent subsequence, and lower semicontinuity yields a finite global minimizer q*. By the finite-domain characterization, q* is admissible: Q(q*) is bounded. Since 0 is strictly inside H and also strictly satisfies q* dot 0<1, Q(q*) has positive volume.

Every q in D has a neighborhood on which the truncated polyhedra are uniformly bounded. Differentiation under the integral is therefore valid, with the hyperplane q dot x=1 contributing a set of Lebesgue measure zero; at q=0 in the bounded-H case the integrand is locally affine on H. Consequently

nabla Phi(q)=-integral_{Q(q)} x dx=-M(q).

D is open and q* is an unconstrained finite minimizer, so M(q*)=0. Dividing by its positive volume gives the true homogeneous centroid zero.

For uniqueness, let q1,q2 be two zero-moment solutions. On Q(q1) minus Q(q2), (q1-q2) dot x<0; on Q(q2) minus Q(q1), (q1-q2) dot x>0. Hence, if the two full-dimensional convex bodies differ, the integral identity gives

(q1-q2) dot (M(q1)-M(q2))<0,

contradicting their zero moments. Distinct full-dimensional closed convex bodies have a positive-volume symmetric difference, so this is a strict contradiction. The body is unique. If a correcting plane is active, the normalized equation of that exposed two-dimensional face is unique, so q1=q2. If it is inactive, Q=H; this is possible only when H is bounded and already has zero moment. This completes the proof.

## Consequence for the research architecture

Remove one selected facet from any bounded normalized polyhedron containing 0. The old facet vector is an admissible q0 for the remaining intersection H. Therefore a globally mass-closing replacement facet always exists, even when H is unbounded. After changing the design planes, the same conclusion holds whenever 0 remains interior and at least one cap still bounds the resulting H. An unsuccessful finite numerical solver in that admissible family is not evidence that the mass-closing plane does not exist.

This strengthens, rather than contradicts, the parent result's conditional uniqueness. It does not justify arbitrary geometric surgery: the corrected facet may rotate far, remove important material, change topology, or destroy the intended equilibria. One must still verify the genuine maximal complex, actual own centroid and all strict/weak equilibria of the finite corrected body. Within a prescribed normal cone, fixed incidence stratum, small trust region, or protected witness chamber, existence remains unresolved and may fail.

At an active facet F, the parent derivative remains

DM(q)[v]=-K(q)v,
K(q)=integral_F x x^T dA/|q|>0.

Thus a Newton correction is a descent method for the globally convex potential when used with admissibility-preserving line search. The global theorem does not guarantee that undamped Newton iterates are admissible or globally convergent.

## Edge-budget consequence

For a full-dimensional bounded convex 3-polyhedron with F maximal facets, Euler's formula and vertex degree at least three imply E<=3F-6. Thus an architecture with at most 105 planes always has E<=309 and C<=618, independently of contact splitting; redundant planes only improve this upper bound. A family with 61 planes has E<=177. The centered polar of RELEASED8 proposed in the parent therefore has an entire 61-plane mass-corrected architecture below the current record, provided the physical equilibrium gate can be solved. The corrected GRID1000 body's 66-plane physical representation similarly has E<=192, even if moving planes splits its old nonsimple vertices. These are upper bounds, not observed feature counts after deformation.

## Exact arithmetic and rational approximation

For rational H, the unique active q* is a real algebraic vector: there are finitely many incidence regions, the vertex coordinates and filled moments are piecewise rational functions of q with rational coefficients, and their zero set is semialgebraic over Q. A unique point of a Q-semialgebraic set has algebraic coordinates. This is an existence statement, not an exhibited polynomial or isolating box for a particular body.

A construction can instead use a rational approximation to q*, recompute the resulting exact rational filled centroid, and translate by it. If the limiting corrected body has strictly separated desired equilibria and nondegenerate relevant incidences, sufficiently close approximations preserve the mechanical class. This last use requires actual open-margin evidence; a near-zero numerical witness alone is not enough.

## Immediate continuation

Use the support budget to replace an equilibrium/topology search with a coupled design search whose inner mass correction is a proper coercive convex three-variable problem. For the simple 61-plane centered dual, first obtain its actual own-centroid census rather than assuming a polarity swap. For the 66-plane GRID1000 physical family, allow contact splitting deliberately and reclassify maximal facets, using a remote correcting facet and finite geometry changes of the unwanted stable/saddle basin. The remaining question is mechanical reachability, not unconstrained cap-mass existence under the hypotheses above.
