# material-2b7ece164c04

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# OCTAGON_NEUTRAL_SHARP_GERMS_V2

Coordinator analytic continuation. This strengthens a CONDITIONAL finite all-orders screen and gluing theorem; it does not assert that every physical packet passes, global weak-S1U1 regularizability, a whole C34 exclusion, or a new attaining proper110 body. Bounds34<=C_min<=622 remain unchanged.

## Exact dependencies

The earlier coordinator theorem is [internal-source-reference], NEUTRAL_GERM_DECISION_OCTAGON_V1.md, SHA256 c858c235717653324f30c8c1415afcb5270a9670275f6773f53be035ad4b6cbe. Its degree15 and carrier-order46 octagonal estimates remain valid but are sharpened here. Complete source dependency [internal-source-reference] is neutral_germ.py.txt,10736B, SHA25613029a0a2ece104b85e4bbc3739b652a05029d8b844f8eb556a5de87a62666e0.

Underlying exact geometric parents, already fully read through EOF, are minimum-0232 (8f50ef8265eca079539078c4b0edce571a7ca4548fba2850729bd16d2e756f03) and minimum-0233 (a4bef2adf830eae50e01705edefbc80edc6388626b8e4e627efe6db99c7bb875). They supply the genuine same-lattice carrier flow, actual-original-centroid correction, exact neutrality, paired VF selectors, and the literal B8_SIX_VE control. No independently centred polar is introduced.

## I. A sharp improvement of the abstract rational-germ order bound

Suppose all selected inequalities, after clearing only locally positive geometric denominators, are A_i(sigma)+tau B_i(sigma)>0 with deg A_i,deg B_i<=d, d>=1, A_i(0)=0. Every physical VF contributes both members of a valid complementary selector. The V1 decision is unchanged: check the sigma=0 axis and each side sigma=epsilon t, epsilon=+1,-1. On a side let a_i=A_i(epsilon t), b_i=B_i(epsilon t). An identically zero b_i requires a positive a_i. Nonzero b_i gives eventual lower or upper rational bound r_i=-a_i/b_i for tau. Let L=max lower and U=min upper, with infinite missing bounds. Feasibility approaching0 is exactly L<U eventually and lim L<=0<=lim U.

The explicit V1 witness can ALWAYS make every positive row have vanishing order at most2d, improving3d. Here is the proof, including possible denominators vanishing before cancellation.

If both endpoint limits are0, choose tau=(L+U)/2. Each endpoint belongs to the closed feasible interval, so every scalar row at L and at U is nonnegative. For nonzero b_i, at least one endpoint value is strictly positive because L<U. Each endpoint value is of the form
(a_i b_j-b_i a_j)/b_j,
where j is the row defining that endpoint. Its numerator has degree<=2d, and dividing by b_j subtracts a nonnegative vanishing order. A positive nonzero endpoint value therefore has order<=2d. All endpoint values have analytic extensions because L,U tend to0. Their average cannot cancel a positive leading term: both are nonnegative. Identically b_i=0 gives order<=d directly.

If lim L<0<lim U, take tau=0; row orders are<=d. If lim L=0<lim U, take tau=L+t. At L all rows are nonnegative. For lower rows b_i>0, adding b_i t is positive, so no leading cancellation occurs; each summand has order<=2d or<=d+1. For an upper row b_i<0, r_i>=U has positive or infinite limiting value, whereas L tends to0. Thus (a_i+b_i L)=(-b_i)(r_i-L) has positive leading term of order at most ord(b_i), and the negative perturbation b_i t occurs strictly later. Its positive order is again<=2d. The case lim L<0=lim U and tau=U-t is symmetric. Missing infinite bounds cause no change. Axis witnesses have order1. This proves the claimed2d bound.

It is SHARP for this general algebraic class: the two rows
-t^d+tau>0,
t^d-(1-t^d)tau>0
trap tau strictly between t^d and t^d/(1-t^d), a width of order2d. The midpoint has both row orders exactly2d, and no path with sigma=t can open both sooner. This is an algebraic control, not asserted to be a physical weak packet. A different parametrization can rescale orders; sharpness is in the normalized sigma=epsilon t formulation used here.

Apply the accepted carrier-opening analytic flow at amplitude eta=t^(2d+1), followed by this successful neutral family. Off-carrier positive terms of order<=2d cannot be destroyed by its O(eta) perturbation. Within-carrier selected exits are preserved exactly or multiplied by positive analytic factors by neutrality. All original nonzero lattice and strict-equilibrium guards persist locally. Thus the conditional carrier gluing order improves to2d+1. For the previous general degree d=6n+3, it is12n+7; n denotes the number of vertices outside the primal carrier. No rational-degree assertion is made for the implicit dual-carrier centring map.

## II. Actual-centred octagonal neutral coordinates are only quadratic

Let P be an actual uniformly filled, centred convex polytope with (V,E,F)=(10,17,9), a true octagonal facet F in q.x=1, and two outside vertices a,b. Keep a physical SPD metric M and its common inverse D.

### Combinatorial geometry used
The edge ab exists. If q.a<q.b, the nonminimal vertex b has an incident edge descending for the linear functional q; all facet vertices have larger value1, so this edge must go to a. The reversed case is symmetric. If q.a=q.b, their segment is the exposed minimal face and hence an edge. This uses the elementary tangent-cone fact that incident edge directions generate feasible directions at a vertex; absence of a descending incident edge would imply global minimality.

Eight facet boundary edges and ab leave exactly eight edges between the facet and the two outside vertices. Every facet vertex needs at least one such edge because its degree is at least3. Therefore each has exactly one outside neighbour. In particular, no non-F facet can consist of a,b and just one facet vertex. Every non-F facet contains exactly two facet vertices, forming a true facet boundary edge: its intersection with the plane of F is an exposed edge of the genuine polygon. Facets not containing a, apart from F itself, must consequently be triangles (b,u,v).

### Vertex-based exact volume decomposition
Triangulate the volume from the vertex a using all true boundary facets not incident to a. Facet F produces the cone(a,F), of positive volume C. Let CB be the sum of volume times the three base vertices over a triangulation of this cone; equivalently CB=3C c_F for the uniform area centroid c_F of F. Each other face contributes a tetrahedron (a,b,u,v) of positive volume B_k. Put B=sum B_k and HB=sum B_k(u+v). Here B>0: b is a genuine extreme vertex outside cone(a,F). The initial true total volume is C+B and actual uniform centroid0 means exactly
(C+B)a+B b+CB+HB=0.
All these constants concern original uniform volume, not an arbitrary vertex barycentre.

Put h_a=1-q.a>0, h_b=1-q.b>0,
d_a=1+sigma h_a, d_b=1+sigma h_b,
W=C d_b+B, H=d_b CB+HB,
Q=h_a d_b W+B h_b d_a.

Under T_sigma(x)=x/[1+sigma(1-q.x)], the base polygon is fixed. A tetrahedron with one outside vertex a has volume factor(1+sigma)/d_a; one with a,b has factor(1+sigma)/(d_a d_b). This follows either by its homogeneous determinant or direct subtraction of the fixed base vertices. Consequently the raw actual centroid is
4g=a/d_a+H/W+B b/(d_b W),
and
1-q.g=(1+sigma)Q/(4 d_a d_b W).

Now apply the exact actual-centroid plane-fixing correction C_g(y)=y-g(1-q.y)/(1-q.g). The two final outside vertices are
X_a=[B h_b a-h_a B b-h_a d_b H]/Q,
X_b=[(h_a b-h_b a)W-h_b d_a H]/Q.
Every coordinate numerator and their common denominator Q have degree<=2 in sigma. At0 Q>0. The eight facet vertices are constant and can also be written with the same common denominator Q. These formulas are derived by substituting the displayed g into C_g; no approximation or independent centroid choice is involved.

### Poles and mechanical primitive degrees
A non-F true facet has fixed base edge u,v and at least one outside vertex w. Let n=u cross v. Its exact normalized pole is
R=q+[(1-q.X_w)/(n.X_w)]n.
The denominator n.X_w is nonzero at0 because u,v,w define a true facet distinct from F; after inserting X_w=N_w/Q, all numerator and denominator degrees are<=2. Signs of every required denominator are fixed in a sufficiently small neighbourhood.

For M_tau=M+tau qq^T, every primal row X_i^T M_tau(X_j-X_i), on the common denominator Q^2, has sigma-degree<=4 and is affine in tau. The inverse pencil is
D_tau=[D+tau(sD-Dq q^TD)]/(1+tau s), s=q^TDq.
A polar row R_f^T D_tau(R_h-R_f) has sigma-degree<=6 after clearing the locally positive factor consisting of the source pole denominator squared, the target denominator, and1+tau s. It too is affine in tau.

Thus the exact all-orders neutral-germ test for any mixed physical off-carrier selector in the OCTAGONAL layer uses d=6, pairwise comparison degree<=12, positive witness orders<=12, and carrier gluing order13. If all off-carrier selected exits are primal VE rows, d=4 gives comparison degree<=8, positive orders<=8 and carrier order9. A VF generally needs its complementary primal/polar pair, so it uses the mixed bound unless a different valid physical argument applies.

The previously established calibrated completeness still applies: the actual-centred same-lattice shape fibre fixing the complete spatial octagon has dimension E-2m=1, and the axial velocity cannot vanish at both distinct outside vertices. Metrics preserving the tangent restriction and carrier foot are precisely the normal pencil. Therefore this screen is exhaustive for that calibrated local family. It is NOT exhaustive for movements of the carrier polygon or every deformation merely preserving some zero rows. A failed screen is not a full-shape obstruction.

## III. Exact execution and recovery capsule

New full companion source: [internal-source-reference], octagon_quadratic.py.txt,4070B, SHA25621ce15b04af590f802d6f4eb4627c25f786b660ba6f4f4512b61547a71dfea73. It requires the COMPLETE10736B neutral_germ.py source [internal-source-reference]; both materials must be supplied to a computational successor. Save them in one directory as octagon_quadratic.py and neutral_germ.py, with original LF endings and final newlines. The source checks its dependency hash.

Executed environment CPython3.13.5, SymPy1.14.0. No external input, seed or numerical optimization. Commands:
python octagon_quadratic.py build
python octagon_quadratic.py check
Terminal marker OCTAGON_NEUTRAL_SHARP_ALL_68_ROWS_PASS.
Output octagon_quadratic_report.json:11675B, SHA256442c50ee14a8d9b19d604596beff8b116e84b87e2935792623761a52740ee77d.
Normal build/check and a clean source-only cold build/check were actually executed; report bytes matched. The unpreserved earlier working script with carrier order19 is superseded by these exact V2 bytes, not a separate canonical object.

The code uses Nyhe's LITERAL B8_SIX_VE control, still strict(S,U,H)=(2,4,4), six weak VE points, NOT S1U1. It checks the vertex-based moment identity, both quadratic coordinate formulas against the original actual-centroid implementation, exact symbolic centroid0, every true facet incidence, and all68 directed primal/polar mechanical rows. All coordinate degrees are<=2, all primal numerator degrees<=4 and polar<=6, with tau-degree<=1. Five abstract strips d=1,2,4,6,15 give exact orders2d, demonstrating the order bound's algebraic sharpness. They are not promoted to physical equilibrium packets.

The general statements above are analytic proofs supported by these symbolic checks, not inferences from a single control, not proof-assistant formalizations, and not a new lower or upper bound on the minimum.
