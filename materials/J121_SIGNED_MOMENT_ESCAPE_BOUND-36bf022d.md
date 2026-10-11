# material-36bf022dd067

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J121: quantitative physical escape from a mandatory-core moment obstruction

This is a coordinator derivation, not a new computed polyhedron. It uses as working premises the exact scalar bounds reported in the completely read KF27E result figure-0594, SHA b2bcbd146cc5aeea6dbb20ac817fd59129fd84f1ff3de578f0def2178c582d1b. That immutable parent contains its entire60-file recovery capsule and all rational geometry. The coordinator has not independently replayed those geometric certificates. The argument below is complete and does not need those files except to instantiate the reported numerical bounds on that particular geometry.

## General statement, allowing both deletion and addition
Let Omega be a bounded measurable envelope of positive volume V_Omega, let B_c be a mandatory measurable core contained in Omega, let b be a reference centre, and let w be a nonzero vector. Put ell(x)=w dot (x-b), ell_+(x)=max(ell(x),0). Suppose a certified scalar Gamma satisfies

Gamma <= integral_Omega min(ell,0) + integral_B_c ell_+.

For any proposed finite-volume body L, define the removed core T=B_c minus L and the outer added material A=L minus Omega. Assume ell(x)>=-B on A for some B>=0. If the actual uniform-volume centroid g_L satisfies ||g_L-b||_infinity <= delta, then

integral_T ell_+ + (B + delta ||w||_1) volume(A)
    >= Gamma - delta ||w||_1 V_Omega.                 (1)

No convexity, number-of-cuts, adjacency, fixed fan, infinitesimal motion or fixed density other than uniform volume is used. Thus the bound applies to every convex candidate satisfying its stated core/envelope/moment hypotheses. It is necessary, not sufficient for centroid feasibility or equilibrium cancellation.

Proof: On Omega, including every negative-ell point and only the retained positive mandatory core can only lower the moment. Hence integral_(L intersect Omega) ell >= Gamma - integral_T ell_+. The added portion contributes at least -B volume(A). On the other hand, the actual centroid constraint gives integral_L ell = volume(L) w dot (g_L-b) <= delta ||w||_1 volume(L) <= delta ||w||_1 [V_Omega+volume(A)]. Rearrangement proves (1).

If the entire core is retained, (1) requires

volume(A)/V_Omega >= max(0, ||w||_1 (rho-delta)/(B+delta||w||_1)),
where rho=Gamma/(||w||_1 V_Omega), provided the denominator is positive.

If no outer material is added, the deleted positive core moment must be at least Gamma-delta||w||_1 V_Omega. A change in labels or a larger count of cuts does not supply that signed moment. A new reference centre, deeper cuts that genuinely remove the core, and outside material with adequate negative moment are distinct possible escape mechanisms.

## Instantiation of the two separate KF27E certificates
Do not identify or union these two cores without checking their literal inputs. The two results have different mandatory-core hypotheses and different w.

1. KF27E's first certificate uses the core inside the old saddle inball together with the retained old elder, the COVER_G8 envelope, and w=(-536,-84,840), ||w||_1=1460. It reports rho in the open interval (4444705761179,4444705761180)/10^15, strictly above1/250. For delta=1/250, a retained-core candidate with ell>=-B on outer material necessarily has

volume(A)/V_Omega > [32463520566067/50000000000000] / [B+146/25].

The numerator is .64927041132134. The strict sign follows from the strict lower endpoint of the reported rho interval. This statement does not assert that all ownS1 bodies retain that core or lie in that centre cube.

2. KF27E's depth-at-most-seven positive-ancestor certificate uses its98-point rational mandatory core and w=(90,744,662), ||w||_1=1496. It reports rho in (2389464635296,2389464635297)/10^15, strictly above1/500. At delta=1/500, retaining that core gives

volume(A)/V_Omega > [2275933962511/3906250000000] / [B+374/125].

The numerator is .582639094402816. This is not an exclusion of all long-chain geometry: the mandatory core applies to the stated geometric positive-ancestor reachability family. Merely calling a chain 'deep' while its final normals remain in the seven-link reachable union does not leave it.

The complete arithmetic producing these two rational coefficients is:
```python
from fractions import Fraction as F
cases=[(1460,4444705761179,F(1,250)),(1496,2389464635296,F(1,500))]
expected=[F(32463520566067,50000000000000),F(2275933962511,3906250000000)]
for (s,a,d),want in zip(cases,expected):
 coefficient=s*(F(a,10**15)-d)
 assert coefficient==want
 print(coefficient, 'denominator offset', s*d)
print('J121_MOMENT_ESCAPE_COEFFICIENTS_PASS')
```
Python3.13.5 standard library was used for the coefficient arithmetic. This is not a replay of the KF27E geometric engine.

## Optional bound on B from a retained unique unstable vertex
For a convex polyhedron about an interior centre g, every globally farthest vertex is strictly unstable. Indeed for a farthest vertex v and any other vertex x,
2(v-g) dot (x-v) = |x-g|^2 - |v-g|^2 - |x-v|^2 < 0.
Thus if a proposed final ownU1 body retains a specified vertex v_star as its unique U, every point x of the body satisfies |x-g|<=|v_star-g|. If ||g-b||_infinity<=delta and R0=|v_star-b|, the triangle inequality gives |x-b|<=R0+2 sqrt(3) delta. Consequently B=||w||_2 [R0+2 sqrt(3) delta] is a valid global outer-moment bound, without choosing an ad hoc bounded control region.

For both KF27E integer w above, ||w||_2<1000 (squared norms999952 and999880). A rational upper bound on R0 and sqrt(3)<7/4 therefore gives an entirely rational conservative B. This consequence is conditional on retaining that particular sole U; changing the global elder is a genuine escape from it. No numerical R0 or added-material construction was computed here.

## Constructive implication
The next computation should compare actual removable-core positive moment and admissible negative moment of an outer hull addition, together with the full primal/polar witness census and E<=249. Rank alone, restoration of a selected centre without current-own equilibria, or removal only of the old superlevel component is insufficient. The original KF27E cover removes the old high component but creates lower junior basins. The mass condition and those new basins must be addressed together; satisfying (1) alone does not remove them.
