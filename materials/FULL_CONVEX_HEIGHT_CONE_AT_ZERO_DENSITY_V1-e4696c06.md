# material-e4696c06ab19

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# The full convex-height necessary condition includes zero-density contacts

## Dependencies and scope
This coordinator analytical extension combines the fully read literal minimum-0295, SHA c5da795d12e9ffc99d28fd53e74ba1cc2494cdcc24117b6b85633536d62c0819, with the exact global3D-to-affine-height equivalence in minimum-0290, SHA a1afff32561b16a73bf7a017e7ad3233330ac76bf67282f7cac952c02cc464a8, and strong attainment in [internal-source-reference]. The earlier actual height-variation theorem and one-apex countercontrol are in [internal-source-reference]. All these sources were read completely.

The new statement is a NECESSARY condition at an affine-height representative attaining the GLOBAL centered whole-facet strong supremum. It is not asserted at a maximum confined to a fixed support, to affine densities, or to a fixed polytope incidence. Its use of the global3D/affine-height equivalence is essential, because its perturbations generally leave the affine-height subclass. It proves neither the universal three-halves bound nor a new equilibrium exclusion. Separate global attainment of the leverage supremum remains unproved.

## Theorem
Let K be compact convex and full dimensional in the plane, ell a nonzero nonnegative affine function, and e=K intersect{t=0} a genuine whole edge with t>=0 on K and B0>0. Let Y be an affine test centered under the ACTUAL density ell. Define

    V=int_K ell, J=int_K t ell, I=int_K ell Y²,
    Bj=int_e ell Y^j ds/|grad t|,
    R=J B2/(V I), eta=B1/B2,
    Phi=t/J-1/V-Y²/I-2 eta Y/V.

Assume I,B2>0 and this actual uniformly filled lift, marked whole facet and test attain the GLOBAL3D strong supremum. Define a signed measure on K by

    nu = Phi dx + (Y²/B2) d_sigma|e.

Then, WITHOUT any strict-positivity assumption on ell,

    nu(a)=0 for every affine a,
    nu(phi)>=0 for every continuous convex phi on K.

Thus the full convex-function comparison condition includes density-zero edges, isolated zero contacts and zero-density marked endpoints. The prior one-sided caveat was correct for height changes on fixed K constrained to remain nonnegative there; it is not an exception at the global problem once actual clipping is allowed.

## Proof by genuine concave-height clipping
Fix a continuous convex phi on K and s>=0 sufficiently small. Put

    h_s(x)=ell(x)-s phi(x),
    K_s={x in K:h_s(x)>=0},
    P_s={(x,z):x in K,2|z|<=h_s(x)}.

The function h_s is concave, so K_s and P_s are convex. Equivalently the final constraint is2|z|+s phi(x)<=ell(x), a convex sublevel constraint on convex K times the real line. The upper and lower height graphs are not required to be affine. The horizontal projection is K_s, the actual marginal is h_s on K_s, and the entire marked facet is P_s intersect{t=0}. No independent signed density or facet surrogate is used.

The set where clipping changes the formal raw integral lies in0<=ell<=s max_K|phi|. The proof of the literal parent's strip estimate used only boundedness and continuity of the perturbation, not its affinity. For every bounded continuous raw test f,

    int_{K_s} f h_s = int_K f(ell-s phi)+O(s²).

If ell is nonconstant, the absolute error is at most

    ||f||_infty diam(K) (max_K|phi|)² s²/(2|grad ell|).

If ell is constant positive, no clipping occurs for small s. The analogous whole-edge estimate holds; at a zero-density marked endpoint its denominator is2|D_e ell||grad t|. Since B0>0, ell cannot vanish identically on e. Therefore small s preserves full-dimensional volume and positive marked area. Contracting toward points of positive ell proves K_s and the entire marked edge converge to their original sets.

Recompute the actual mean, write Y_s=Y-int_{K_s}h_sY/V_s, and form the actual uniform-body ratio. The exact first-variation formula, with perturbation psi=-phi, gives

    d/ds log R(P_s,Y_s)|0+ = -nu(phi).

Global maximality implies this derivative is nonpositive, proving nu(phi)>=0. An affine a and its negative are both convex; applying the same argument to both gives nu(a)=0. Alternatively, the literal parent's affine clipping theorem already supplies the affine equalities. There is no density-zero boundary exception because the clipped mass and the clipped edge correction start at second order. This completes the proof.

The equivalence and strong attainment ensure that a hypothetical universal strong counterexample has a globally maximizing affine-height representative to which this theorem applies. They do NOT make the theorem valid at every affine-density stationary point or every local conic candidate.

## Concrete necessary tests
Because nu annihilates affine functions, all centered or translated versions of the following conditions are equivalent.

1. Quadratic tests. With x=(t,Y), the symmetric2x2 matrix

    Q_nu=int_K Phi x x^T dx + (1/B2)int_e Y² x x^T d_sigma

must be positive semidefinite. In particular its entries are

    Qtt=int_K t² Phi,
    QtY=int_K tY Phi,
    QYY=int_K Y² Phi + int_e Y^4 d_sigma/B2.

This is an UNWEIGHTED bulk-moment condition; replacing dx by ell dx is incorrect. Any negative eigenvalue supplies an explicit concave quadratic height ascent after clipping. The affine mean equalities alone do not supply this matrix condition.

2. Every section ridge. For any affine f and real r,

    int_K Phi (f-r)_+ dx
      +(1/B2)int_e Y²(f-r)_+ d_sigma >=0.

A strict failure supplies the actual concave-height deformation h_s=ell-s(f-r)_+. It is piecewise affine when K is polygonal and ell,f are affine, hence gives a genuine uniform polytope after clipping. The facet used is the full marked facet of that polytope. Conditions for all one-dimensional ridges need not exhaust the full planar convex cone; no such completeness claim is made. In particular the old single-apex tests are not complete, as shown by the exact section-ridge control in [internal-source-reference].

3. The same comparison holds for arbitrary convex piecewise-affine maxima, not merely a sum of independent one-apex tents. This may expose a candidate that passes quadratic or ridge tests. Conversely, passing any finite collection is not a proof of the full convex-order condition.

## Second-order extension along a first-order-neutral convex test
The literal parent's clipping asymptotic also extends to continuous phi. Let Gamma=K intersect{ell=0}. For the perturbation psi=-phi and s->0+, the bulk second-order coefficient is

    (1/|grad ell|) int_Gamma Phi (phi_+)² ds

in the SECOND DERIVATIVE of log R, with the additional marked-endpoint term

    sum_{p in e intersect Gamma} Y(p)²(phi(p)_+)²/[B2 |D_e ell| |grad t|].

It vanishes on a point-only Gamma in the bulk; o(s²), not generally O(s³), is the appropriate raw-integral remainder there. If nu(phi)=0, the sum of the formal fixed-support log Hessian and these corrections must be nonpositive. The parent's formula for the formal Hessian in terms of the five raw first variations remains valid for any bounded perturbation, because it is an algebraic differentiation identity, not an affinity assumption. The parent contains its complete derivation and runnable check. For a non-affine test only this one-sided deformation has been shown concave; an opposite one-sided inequality must not be assumed automatically.

## Remaining frontier
The complete arbitrary-support uniform-density theorem is already proved. The exact triangle-lift bound is now45/32 by [internal-source-reference]. The new parent's at-most-two-arc classification, affine clipping stationarity and disjoint-zero-edge Hessian condition sharply constrain the nonconstant-density alternatives. The present theorem supplies a further global necessary convex-cone condition at those same alternatives, including their zero edges. It does not assert that any one of these tests rules out every remaining one/two-arc body. The shared minimum bracket remains34..622.
