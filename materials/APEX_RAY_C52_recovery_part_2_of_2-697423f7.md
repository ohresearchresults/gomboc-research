# material-697423f7be03

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Recovery capsule part 2/2: APEX-RAY-C52 geometric proof and scope
Object identity APEX-RAY-C52. Exact part1 is [internal-source-reference], APEX_RAY_C52_recovery_part_1_of_2.md,10428B,SHA239d4866c1f00632680d405ab38b26dd46b76f34ed7660ef39cfa66a458c9620. Both parts form the complete scientific recovery capsule. Part1 contains all runnable producing/verification source, all exact inputs and output manifests; it has no external dependency. This part provides the full proof rather than treating code transport or hashes as verification.

## Result and scope
A uniformly filled proper strict110 convex polyhedron, with no additional weak equilibria and invariant under an orthogonal half-turn, must satisfy C=2E>=52. This improves the earlier half-turn C>=40 only. General Minimum C>=34 is unchanged; no new own110 figure is constructed and attainment at C52 is not asserted.

Exact first-moment certificates exclude opposite-root escape-depth pairs (5,4),(4,6),(5,5),(6,4),(5,6),(6,5),(5,7),(6,6),(7,5). Nine pairs have108 rational covering intervals. EVERY leaf uses strictly positive moment, none the source's optional geometric-contradiction branch. The general accepted Minimum V>=10,F>=9 is needed only to reduce the final half-turn complexity enumeration to eight of these pairs. The nine depth-pair exclusions themselves do not need that Minimum.

Earlier angular context is in [internal-source-reference] SHA9e731eb268240f09438d6fd680c5baa7faae82847f0fee7e67c8dd0c17bc1d0a. The needed argument is reproved here, so that material is not a dependency of this capsule.

## 1. Mandatory geometry and orbit depths
Put the actual filled-volume centroid at0. The unique unstable vertex and the unique stable facet are fixed by the orthogonal half-turn. The unstable vertex lies on the axis, the stable facet is perpendicular to that axis, and its perpendicular foot lies on the axis. They are on opposite rays: otherwise the stable boundary foot would be between the interior centroid and the unstable boundary vertex, hence interior. Scale the stable supporting plane to z=-1 and write the unstable vertex u=t e_z. These are actual carriers, not an arbitrary reference centre or designated non-equilibrium points.

Every farthest vertex is strict unstable: for any other vertex y, |y|<=|u| gives u.(y-u)=(|y|²-|u|²-|y-u|²)/2<0. Thus the unique unstable vertex is the unique farthest vertex and the whole K lies in the radius-t ball. In particular z<=t. The actual stable plane gives z>=-1.

There is precisely one axis vertex, since the other axial endpoint lies in the relative interior of the stable face. There is precisely one invariant facet: an invariant supporting normal must be axial; the alternative invariant plane through the axis contains the interior centroid and cannot support. The opposite axial support is a vertex, not a facet. Consequently V=2k+1,F=2l+1. Euler gives E=2(k+l), C=4(k+l); degree at least3 gives 2k+3<=4l and 2l+3<=4k.

Every nonroot vertex x has a true edge to y with x.(y-x)>0. Otherwise all tangent-cone directions have nonpositive scalar product, making x either strict unstable or an additional weak equilibrium, both excluded. Chosen positive edges form a strictly squared-radius-increasing forest ending at u. A path cannot contain both members of a half-turn pair, which have equal radii, so its length is at most k. Apply the same argument to Q=K^polar at the SAME origin. Its unique unstable vertex is the stable-face vector -e_z with norm1, and its escape depth is at most l. No claim is made that this origin is the polar body's own volume centroid.

## 2. Angular envelopes and exact rational samples
For an escape path x0,...,xm=u, each step gives |xi|<|xi+1| cos(alpha_i), where alpha_i is the angle between radius vectors. For any unit normal n with n.x0>0, let beta=angle(n,x0), phi=angle(n,e_z). Spherical triangle inequality gives phi<=beta+sum alpha_i. Concavity of log cos on [0,pi/2), then monotonicity of s log cos(phi/s), yields
h_K(n)<=t cos^(k+1)(phi/(k+1)).
Nonpositive projections satisfy this trivially. Apply the polar version and rho_K(s)=1/h_Q(s): for theta=angle(s,e_z),
rho_K(theta)>=sec^(l+1)((pi-theta)/(l+1)).
These hold at EVERY azimuth although the body itself need only have half-turn symmetry. Thus every prescribed inner circle, its disk and its convex hull with the actual apex belong to K.

Let b+i a=(1+i w)^n for rational w>=0 satisfying n atan(w)<pi. With n=k+1 the outer envelope gives the valid meridian plane a x+b z<=t. With n=l+1 the inner radial envelope gives a contained circle of radius a and height -b. Both assertions follow by cancelling the common factor sec^n(atan w) in the complex-power cosine/sine representation. The source computes these rational polynomials by repeated multiplication.

The literal UMAX values satisfy (k+1)atan(w)<157/50<pi. A41-term alternating upper bound proves the first inequality. Machin pi=16atan(1/5)-4atan(1/239), with10-term lower and9-term upper alternating bounds, proves the second. No floating trigonometry enters. All sampled a>=0, and for w>0 b<1 because d Re(1+iw)^n/dw=-n Im(1+iw)^(n-1)<0 on this arc.

Outer planes tested on the actual stable foot (0,-1) give t>=-b_outer. Inner circle points have z=-b_inner<=t. Therefore t>=low=max of these finitely many exact -b values. This is necessary only, not nesting sufficiency or filled-mass realizability.

## 3. Convex apex rays force coupled mass
Parameterize rays from the mandatory apex by p=(p1,p2) in R²:
(x,y,z)=(h p1,h p2,t-h), h>=0.
The Jacobian is h². Convexity makes the ray intersection an initial segment 0<=h<=H(p), apart from irrelevant null-set boundary conventions. Thus
M_z=integral_R² G_t(H(p)) dp, G_t(h)=t h³/3-h⁴/4.
The stable plane bounds H<=t+1. If t>3, then t+1<4t/3 and G_t(H)>0 wherever H>0; the body's positive volume makes M_z>0, contradicting the centroid. Hence t<=3. The endpoint3 is included explicitly in the interval cover; no unproved strict pyramid shortcut is used.

For a parameter interval ta<=t<=tb and slope bin pl<=|p|<=ph derive alpha<=H<=beta uniformly. An inner disk radius a at height z=-b<ta forces the ray through the disk whenever ph<=a/(tb-z). It then forces H>=ta-z. The source uses an increasing record-slope list to select a valid disk, not an assumed optimal disk. If none qualifies alpha=0 is valid.

Each outer plane gives H*(a|p|-b)<=t*(1-b). Write L(p)=(a p-b)/(1-b)=m p+c, where m>0. Its exact upper envelope at the LEFT slope endpoint pl bounds H<=tb/Lmax(pl) across the bin whenever Lmax(pl)>0. Also H<=tb+1. The smaller valid upper bound is beta. An alpha>beta would exclude the whole t interval geometrically; the nine actual certificates do NOT use this optional branch.

For h>=0, G_t(h)>=G_ta(h). The derivative of G_ta is h²(ta-h), so its only interior extremum is a maximum. Therefore
G_t(H)>=min(G_ta(alpha),G_ta(beta)).
The inequality holds in every azimuth. Integrating over the slope annulus and dividing M_z by pi gives factor ph²-pl². Each rational bin contribution is rounded DOWN to a multiple of2^-80 by integer floor division and then summed. This avoids unbounded denominator growth and keeps a rigorous lower bound even for negative terms.

The omitted slope tail is nonnegative. Set target=3tb/(4ta). Once ANY outer affine line is at least target, beta<=4ta/3 and G_ta is nonnegative on [0,beta]. All line slopes are positive, so the property persists at larger p. Choose pmax at least0, min_lines((target-c)/m), and the maximum forced-disk slope. Beyond it the lower bound0 is valid. The source also integrates any forced positive contribution between that critical slope and the maximum disk slope; an earlier insufficient draft omitted this and was not used for a proof.

A positive summed bound proves M_z/pi>0, excluding all bodies in the t interval. Exact rational bisection partitions [low,3] until every interval is excluded. The source asserts complete adjacency and exact endpoints. A depth-limit failure would be INCONCLUSIVE, not an exclusion; none occurs in these nine runs. The proof never assumes independent selection of negative and positive angular material: convex apex-ray segments enforce their coupling.

## 4. Observed rational result and consequence
Use the complete part1 source with n128 (129 sample parameters including zero), p_bins256,maxdepth10,2^-80 downward rounding and its literal UMAX table. No seed or floating optimizer enters. Leaf counts by pair: (5,4)1,(4,6)1,(5,5)8,(6,4)1,(5,6)13,(6,5)11,(5,7)24,(6,6)35,(7,5)14,total108. Every leaf has positive rational moment and geometric flag False. The smallest (6,6) leaf bound is approximately .005394786691504661 in M_z/pi units; this decimal is explanatory only and the complete fraction is in the regenerated JSON.

Using the accepted general Minimum plus parity, k>=5,l>=4. For k+l<=12, the valence inequalities leave exactly (5,4),(5,5),(5,6),(5,7),(6,4),(6,5),(6,6),(7,5). All are excluded. Hence k+l>=13 and C>=52 in the half-turn subclass. This neither rules out the next sum13 nor proves attainment there; it does not address general non-opposite-root or nonsymmetric bodies. Numerical apex-ray exploration permits some next-sum pairs, so this particular relaxation should not be claimed to close them.

## 5. Recovery completeness and next question
Both capsule parts are durable exact text. Part1 includes the complete deterministic source, inputs, reconstruction/verification command, filenames, byte counts and output hashes. Marker APEX_RATIONAL_NINE_PAIRS_PASS 9 108 records the completed calculation; C2_OWN110_SCOPED_C_GE_52_PASS records the finite combinatorial reduction using the accepted Minimum. Complete cold replay and an additional separate (6,6) rerun matched. This establishes reproducibility, not a second independent mathematical proof.

This convexity-and-mass certificate complements prior angular first-moment/nesting gates and actual finite construction fronts. A horizontal-section cone constraint offers a different relaxation, neither globally dominates the ray bound, and both may be used as necessary tests. Future work could sharpen radius budgets or couple these constraints to finite geometry, but a low numerical relaxed moment is not evidence that a polyhedron exists. The requested C<500 own110 endpoint remains unconstructed here.
