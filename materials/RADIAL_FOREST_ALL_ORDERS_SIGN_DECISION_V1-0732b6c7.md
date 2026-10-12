# material-0732b6c7d33a

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# RADIAL_FOREST_ALL_ORDERS_SIGN_DECISION_V1

Coordinator analytic continuation. Exact sources read completely: minimum-0239, SHA256 02d2c6a3a9b0e54366f01c86b298d2055aea3037c342d8389b23e4b4dd465a38; [internal-source-reference], SHA256 2c914bd63d8483930ed596e79f628c464417de6ca62b250afe09cfb822544b39; [internal-source-reference], SHA256 ce9f3503f2111b0c739ba2a18d21337bcb02390c81dbbca5dc19062b83c0fc70. Their actual geometry and centroid-actuator statements are premises, not independently replayed computations. This new analytic proof needs no numerical input or code. It does not assert an actual weakS1U1 body or change 34<=C_min<=622.

## 1. The exact reduced physical system

Use the parallel heptagon-triangle setting and physical normalization of the literal sources: M=N=I, F:z=h, T:z=k with h>0>k, q=q_T=e_z/k, actual uniform centroid0. For every lateral pole r_i prescribe r_i(f_i)=q+(r_i-q)/(1-f_i). Both end planes and all top vertices are fixed. Let D contain the genuine interior-spoke EF arrows i->j. The physical foot is unique at its bearing facet and |r_j|^2>|r_i|^2, so D is a forest with outdegree at most one. Orient each component toward its unique root. It is a subgraph of the seven-facet lateral cycle.

For edge e:i->j put
A=|r_i|^2-q.r_i>0, L=q.(r_i-q), D_e=q.(r_j-r_i), B=A+D_e.
The physical EF exit has, up to its positive denominator, numerator
E_e(f,g)=(A-L f)g-B f+(L+D_e)f^2,
where f=f_i,g=f_j. Locally A-L f>0. Write
T_e(f)=[B f-(L+D_e)f^2]/(A-L f).
Then its exact selected request is g>T_e(f).

A source-side basal VE partner adds g-f>0; its physical incidence forces D_e=0, so T_e(f)=f and the requests coincide exactly. A target-side basal VE adds f-gamma g>0, with gamma<1, D_e>0, B>A>0. When 0<gamma<1, define
Delta=A/gamma-B,
kappa=L(1-1/gamma)+D_e>0.
The last strict inequality is the actual-incidence identity d_z(k-h)/[k^2(1-h r_iz)]>0, not a formal coefficient assumption. A basal F-VF will use the sufficient selector f>0,g>0. Incidence then gives D_e=0; the source proves that both F-source dual exits and a genuine complementary primal exit open. This chosen VF selector is sufficient, not asserted to exhaust all possible VF motions.

Some poles may be prescribed exactly fixed; let H be their set, imposing f_i identically0. In the full-packet application H is the reduced protected footprint from the sources.

## 2. Three signs, with exact local compatibility rules

Use the signs -,0,+; sign0 means an identically zero coordinate in the constructed germ. A retained sign assignment has sign0 at every node in H. The following edge tests completely characterize sufficiently small solutions of the displayed reduced system.

For an unpaired EF, or a source-side VE/EF pair, the allowed ordered (source,target) signs are:

B>0: (-,-),(-,0),(-,+),(0,+),(+,+).
B<0: (+,-),(+,0),(+,+),(0,+),(-,+).
B=0: (-,+),(0,+),(+,+).

A source-side pair always uses B=A>0. For the B=0 row, physical coefficients give
L+D_e=L-A=-|r_i-q|^2<0,
so T_e(f)=|r_i-q|^2 f^2/(A-Lf)>=0. Hence the target is strictly positive even at f=0. This identity is needed: the B=0 rule is not stated for arbitrary unrelated polynomial coefficients.

For a target-side VE/EF pair:
* gamma<0: target is +; source may be -,0,+.
* gamma=0: source and target are both +.
* 0<gamma<1, Delta>0: both are +.
* 0<gamma<1, Delta<0: both are -.
* 0<gamma<1, Delta=0: both are + or both are -.

For the chosen basal F-VF selector, both signs are +.

### Necessity
For B nonzero, T_e(f) has the sign of Bf near0 whenever f is nonzero; at f=0 it is0. Together with g>T_e(f) this gives the listed unpaired rules. The B=0 identity above supplies that case exactly.

For a target partner with gamma<0, g<=0 and f-gamma g>0 would force f>0, whence T_e(f)>0 because B>0, contradicting g>T_e(f). For gamma=0, f>0 and then g>0. For 0<gamma<1 the two inequalities force f,g nonzero with the same sign. Their available interval has width
f/gamma-T_e(f)=f(Delta+kappa f)/(A-L f).
For Delta nonzero its sign is that of f Delta locally. At Delta=0 it is positive for either nonzero sign of f. These give precisely the target-pair rules. The VF rule is its retained sufficient selector itself.

Consequently an approaching sequence of solutions has a subsequence with one of finitely many compatible sign assignments. This conclusion does not require an a priori analytic arc. Conversely, the explicit construction below gives one whenever a sign assignment exists. Failure of this finite screen therefore rules out all sufficiently small solutions of this retained radial system, not merely its first jets.

## 3. Backward construction through every resonance

Choose a compatible sign assignment. Set a free root coordinate to t, -t or0 as required. Traverse from roots toward predecessors. For each edge i->j the target g(t) has already been fixed, while its source f(t) has no other outgoing constraint. Its incoming edges will be handled later. Every nonzero coordinate constructed below has leading order one.

For an unpaired edge choose as follows; all constants refer to that edge.

B>0:
- g>0: choose f=(A/(2B))g for source+, f=-g for source-, f=0 for source0.
- g<0: the allowed source is -; choose f=(2A/B)g.
- g=0: the allowed source is -; choose f=-t.

B<0:
- g>0: choose f=g for source+, f=(A/(2B))g for source-, f=0 for source0.
- g<0: the allowed source is +; choose f=(2A/B)g.
- g=0: the allowed source is +; choose f=t.

B=0, necessarily g>0: choose f=g, -g or0 to match its sign.

In all these cases E_e has a strictly positive order-one leading coefficient. The same construction handles source-side partners because T_e=f and E_e=(A-Lf)(g-f).

For a target pair with gamma<0, necessarily g>0: choose f=(A/(2B))g for source+, f=(gamma/2)g for source-, or f=0. Both A-B(f/g) and (f/g)-gamma are positive. For gamma=0 choose f=(A/(2B))g.

For a target pair with 0<gamma<1 and Delta nonzero, set
c=(gamma+A/B)/2, f=cg.
If Delta>0 then gamma<c<A/B and g>0; if Delta<0 then A/B<c<gamma and g<0. Thus BOTH physical exits have positive order-one terms.

For a resonant target pair Delta=0, B=A/gamma>0. Define
alpha=gamma^2 kappa/(2B)>0,
f=gamma g+alpha g^2.
Then, exactly, f-gamma g=alpha g^2>0. Expanding the exact EF polynomial, its quadratic coefficient as a function of g is
gamma^2 kappa-B alpha=gamma^2 kappa/2>0.
Higher terms are O(g^3). Thus the EF and the VE both open at order TWO, for either sign of g. The source has the same leading sign and the same leading order one as g. This is the key compatibility fact: resonance does not consume a new asymptotic scale and does not force a higher-order variable that would upset a neighboring pair.

For the chosen basal VF selector, use f=g/2 with g>0. Its EF opens at order one. The basal displacement has two strictly negative horizontal incident-plane products, hence lies in the interior of the original basal tangent cone. At least one true primal edge has positive first derivative; both complementary F-source dual rows are positive. Select the matching complementary pair as in the exact source. All selected VF exits have order one.

The forest property makes these prescriptions simultaneously consistent: a node is prescribed only once, by its one outgoing edge or as a root. Two incoming edges can choose their distinct source coordinates after their common target is fixed. The resulting functions are polynomials in t; each resonance at most doubles the current degree, but every nonzero coordinate still has order one. Finite many rows therefore have one common positive neighborhood. No selected EF/partner exit has positive leading order greater than two, regardless of the number of resonant edges.

## 4. Finite decision, and what a failure really says

One may enumerate at most 3^7=2187 sign assignments, impose zeros on H, and use the tables. Equivalently use three-state dynamic programming on the rooted forest: a permitted target sign must have at least one compatible source sign in each predecessor subtree. This is a complete decision for the retained reduced radial inequalities. It is strictly stronger than the first-order rate test, which incorrectly rejects isolated Delta=0 pairs.

For 0<gamma<1, target-pair edges require the two node signs to agree, while nonresonant edges pin that common sign by Delta. Oppositely pinned edges in the same such connected component are therefore a genuine all-orders obstruction WITHIN THIS RADIAL SYSTEM. Such a coefficient pattern has NOT been shown to occur in an actual body, much less a weakS1U1 body. Other sign-table incompatibilities or fixed-node conflicts are also possible in the formal reduced decision. The physical incidence and unique-U restrictions on their occurrence remain a meaningful separate question.

The decision includes only the specified sufficient F-VF selector. Its failure need not rule out another complementary VF choice even in the same radial family. Still less does it prove failure of the full calibrated fibre or all genuine shape changes. Exhausted centroid actuators are an independent geometric limitation.

## 5. Genuine complete-packet corollaries with actual uniform centroid

Suppose two lateral triangles avoid all EF endpoint poles. If the complete original weak packet consists of T-carried contacts, the spoke EFs, and their selected possible basal weak endpoints, and the sign screen with H empty succeeds, the entire packet regularizes at fixed physical metric, same lattice and actual uniform centroid. Use the polynomial pole germ above, correct the actual centroid using those two triangles and the fully read nonparallel actuator, and then open the top carrier at amplitude t^3. The correctors cannot change an EF pole or its basal source vertex; any motion of the other endpoint of a partner basal edge changes only its positive length factor. Every T-carried row remains exactly neutral during the first stage. The selected EF/partner orders are at most two and the top opening has order three. Thus the complete packet has selected orders at most THREE, independent of the number of pairs, provided these explicit hypotheses hold.

More generally retain the reduced protected footprint H for all other physical groups, including both members of their complementary VF selectors. Assume two triangular correctors avoid H and every EF endpoint pole. If the finite sign screen succeeds with f_i=0 for i in H, use the sources' auxiliary non-spoke opening at epsilon=t^3, then apply this same radial germ and centroid correction. Original EF/partner positive terms of order at most two survive O(epsilon) changes. Every other selected row remains exactly fixed or receives a positive factor, as proved by the literal footprint construction. Their auxiliary positive orders at most ten become at most THIRTY. The nonparallel actuator ensures validity on the slightly nonparallel auxiliary input. This gives a complete-packet order30 theorem in this explicit isolation class, not universal proper110 density.

For a weakS1U1 input satisfying either corollary, the inherited selector and index statements give proper110 at the same face lattice. No existence of such an input is asserted. The first open 10/17/9 layer, global minimum and separate attaining Figure are unchanged.

## 6. Evidence boundary and continuation

This is a complete analytic proof unit. No code materially produced the result; no numerical certificate, new exact polyhedron or cold replay is claimed. Its geometric prerequisites remain the three exact sources identified at the beginning. The new reduction replaces an unresolved generic higher-order multi-pair radial question by a finite sign question, while explicitly preserving the missing physical sign-compatibility and centroid-footprint obligations. A conceptual successor should study whether actual weakS1U1 geometry forbids all incompatible sign cores, or develop actuators when every lateral triangle participates. It should not treat a formal sign conflict as a physical obstruction.
