# material-c50a8a961e24

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J139 recovery capsule, part 1/4: proofs and evidence boundaries

NOT an own110 construction. Canonical V176/E311/F137,C622 is unchanged; E<=249 remains unmet. The new work concerns globally centered radial models, exact failures of two weight policies, and a finite-direction obstruction identifying a necessary new angular freedom.

## Recovery set
J139 part2 supplies the complete exact cycle auditor and both literal checkpoints; part3 supplies the complete root-envelope, reflection-propagation and one-ray programs; part4 preserves numerical producers and finite searches. These additionally require TWO already durable, completely read J137 materials: [internal-source-reference], SHA38656c528889da98e3528106be5e76bc9bce4947dcd7213e24656d88af3781bb, contains exact137.py; [internal-source-reference], SHAd6d7d18bc06cc2c3cf440493880f39810b20291156a6c9762be346adc113c01c, contains LOW43.json. The entire recovery set is thus six readable native materials, not an implicit archive. An envelope-only successor needs parts1+3 and both J137 materials, not the numerical optimizer sources.

LOW43.json:1534B,SHA c9cfe9c62a5835f6aecbbb77513ab9727a6a2a08f34429d22e0873d76f9dc6f6. exact137.py:6536B,SHA140298b0806f9be76b2345c5c5a8ea45b3d629edfa86c03109d7b8f24ef902d2. Both were copied byte-identically for the new work. The auditor uses integer/Fraction predicates, maximal coplanar facets, true edges, uniform volume/moments, explicit S/U/H/additional-weak tests and every positive P/Q. This was not an independent replay of the author's entire LOW43 package.

## Global reciprocal-radius mass theorem
Let nonzero rational rays R_i positively span R^3 and K(t)=conv{R_i/t_i},t_i>0. Here R_i are the original LOW43 points minus their EXACT original homogeneous centroid g0. Origin0 remains strictly inside every K(t).

A positively oriented cone T=(i,j,k) gives a_T=|det(R_i,R_j,R_k)|/6 and v_T(t)=a_T/(t_i t_j t_k). A complete fan's tetrahedral star lies in K, its volume is sum v_T, and its moment is sum v_T(x_i+x_j+x_k)/4. The actual hull fan attains equality. Thus true V(t) is the maximum of convex fan-volume functions over ALL fans, including flips and retired labels. Each reciprocal product has positive Hessian.

For positive balanced w, sum w_i R_i=0, minimize F(t)=V(t)+w.t. Its sublevels bound each t_i above by its linear cost and away from0 using any nonzero tetrahedron with origin, ray i and two other rays; hence a global minimizer exists. A projective perturbation t->t+R b maps x->x/(1+b.x), with Jacobian(1+b.x)^-4. Therefore D_b V=-4M for the ACTUAL uniform first moment. The balanced linear term has zero derivative, so EVERY global minimizer has M=0. No fixed-fan assumption or uniqueness claim is needed. J137 [internal-source-reference] gives the earlier full proof; J139 supplies a globally certified executed inner solve.

## Positive weighted cone-cycle certificate
A volume lower certificate can replace a list of complete fans by nonnegative rational triangle weights gamma_T. Orient every cone positively. Require exact weighted cancellation on EVERY oriented spherical edge and exact angular coverage1 at one direction on no boundary. Coverage is locally constant across the finite edge arrangement because each signed edge jump cancels; connectedness makes it1 almost everywhere. The program checks all edge weights and an exact generic probe(1,k,k^2).

Each tetrahedron conv(0,x_i,x_j,x_k) lies in K. Its weighted radial density contributes gamma_T up to its radial endpoint; since angular coverage is1, the aggregate density satisfies0<=f_t<=1_K. Thus W(t)=sum gamma_T a_T/(t_i t_j t_k)<=V(t) globally, with known moment m(t). This proof is valid even without recovering constituent fans. It also justifies the mass-defect enclosure below.

The HIGH and ROOT cycle checkpoints exactly aggregate their original positive fan mixtures:43/21 fans become119/91 positive weighted triangles. Executed exact comparison gave identical t, balanced w, actual body, objective bounds, mass enclosures, minimizer boxes and own census. This is an exact representation change, not a different object or precision alias.

## Exact mass error, global objective bracket and minimizer box
At a rational test t, write v_T=gamma_T a_T/(t_i t_j t_k), W=sum v_T, d_i=sum_{T contains i}v_T/t_i and m=sum v_T(x_i+x_j+x_k)/4. Then sum R_i d_i=4m exactly. Put delta=V-W>=0. The nonnegative missing density1_K-f_t has mass delta, so for every coordinate k:
 (m_k+delta min_i x_ik)/V <= g_k <= (m_k+delta max_i x_ik)/V.
The exact actual g is also directly integrated and checked against these intervals.

Allocate alpha_Ti=(v_T/t_i)(w_i/d_i), so sum_T alpha_Ti=w_i. For any positive s, AM-GM gives
 gamma_T a_T/(s_i s_j s_k)+alpha_Ti s_i+alpha_Tj s_j+alpha_Tk s_k >=4g_T,
 g_T=v_T [w_i w_j w_k/(d_i d_j d_k)]^(1/4).
Summing proves L*=4sum g_T<=min F<=UB=V(t)+w.t. Downward exact fourth-root bounds on grid10^24, computed by integer isqrt(isqrt(...)), give rational LB<=L*. This bounds the TRUE all-fan global minimum, not only a finite master or an optimizer status.

For four positive terms a_l of product g_T^4,
 sum_l(sqrt(a_l)-sqrt(g_T))^2 <= sum_l a_l-4g_T,
by AM-GM on their square roots. Set Delta=UB-LB and b_i=sum_{T contains i}sqrt(alpha_Ti g_T). Every s with F(s)<=UB satisfies
 w_i(sqrt(s_i)-b_i/w_i)^2<=Delta.
The proof sums the preceding inequalities and completes a square; the discarded variance is nonnegative by Cauchy. Rational square-root enclosures produce a box containing ALL global minimizers.

The cleared global chord from x_i=R_i/s_i to x_j is (R_i.R_j)s_i-|R_i|^2 s_j. Maximizing this linear form on the box uses endpoints selected according to the sign of R_i.R_j. Strict negativity for every j certifies a genuine strict U at EVERY global minimizer, whose actual centroid is0 by the mass theorem. No full class is inferred there beyond these certified U lower bounds.

## Two executed failures and exact nonwinners
Baseline numerical weights were -grad V of the LOW43 fan at t=1. HIGH multiplies weights on the26-node junior high component by exp(-.1) then balances by a three-dimensional positive exponential tilt. ROOT tilts only junior raw vertex34. The smooth-max bundle solver rebuilds actual hulls. Numerical centroid norms reached about1.46e-9 and5.81e-10; neither is exact zero.

Exact t/w checkpoints use grid10^12. At the deterministic max-absolute-determinant ray triple, w is corrected rationally to enforce sum w_i R_i=0; all corrected weights are positive. These RATIONAL balanced weights define the accepted models, not the unrounded transcendental nomination weights.

HIGH139_R12 has true V41/E117/F78,C234 and exact OWN class(25,9,32), additionalweak000, primitive physical/polar directed-edge zeros0/0. It retains8P/24Q, largest depths approximately.5671052129778023/.026777212425690564. Its actual g is approximately(-9.6281266659e-10,-1.0626672171e-9,-2.8728073183e-10), NOT0. Exact enclosure gives ||g||infinity<=6.9500886523e-9 and relative global objective gap(UB-LB)/UB<=1.8960821497e-9, displayed outward. Every global minimizer of this model has at least8 strict U, raw labels[0,2,6,22,25,28,34,39]. More accurate solution of this SAME model cannot give own110.

ROOT139_R12 has true43/123/82,C246, own(27,10,35), additionalweak000, primitive zeros0/0,9P/26Q, largest depths approximately.5163751044285386/.004746851511634576. Actual g approximately(4.7913049291e-10,1.5057894971e-10,2.9268958403e-10), NOT0. Exact enclosure gives ||g||infinity<=8.2346382864e-10 and relative objective gap<=2.1676919515e-10. Every global minimizer has at least9 strict U,[0,20,21,22,28,33,34,35,39].

Frozen-body census is NOT the complete census of the ideal global minimizer. At the latter only exact centering and the stated U LOWER BOUND are claimed. Neither policy excludes other weights or all fixed-ray centered bodies.

## All-path finite-ray envelopes
Suppose conv{s_i R_i},s_i>0 has actual centroid0, one strict U at label r and no weak unstable vertices. Normalize s_r=1. Every non-root true vertex has a positive outgoing global chord; every nonvertex submitted point has a nonnegative outgoing chord because it is a convex combination of other points. Along a nonnegative chord between distinct points, squared norm strictly increases. Thus a finite path ends at the sole U.

Put C_ij=max(0,R_i.R_j/|R_i|^2). Every such arrow implies s_i<=C_ij s_j. Let p_r=1 and p_i be the maximum product over paths i->r. Cycle products are products of cosines and never exceed1, so simple paths suffice. The exact program exhibits equality paths and checks EVERY Bellman inequality p_i>=C_ij p_j on all positive-dot pairs. Hence it bounds EVERY possible outgoing policy, not one selected tree. Maximum-product Dijkstra orders p_i^2|R_i|^2, decreased along an edge by cos^2; the complete rational postchecks certify its result independently of the ordering argument.

The actual body lies in H_r=conv{p_i R_i}. Homogeneous centroid0 implies -K/3 subset K: triangulate facets opposite a vertex v and decompose K into tetrahedra with apex v. Their volume-weighted centroid identity represents -v/3 as a convex combination of the opposite triangular centroids. Extend from vertices by convexity. Consequently -R_r/3 must lie in H_r.

Exact supporting planes of H_r strictly separate that reflected root for labels[0,1,2,3,4,6,7,8,12,14]. Every plane is checked against ALL outer points. Root0 uses plane labels[29,12,28], with squared normalized separation approximately2.065272999399102e-5, strictly greater than(9/2000)^2.

A further exact monotone propagation excludes root5. Given valid upper radii b, construct the full exact outer hull H. A halfspace n.x<=h and centroid reflection imply s_i<=3h/(-n.R_i) when -n.R_i>0. Also every non-root obeys s_i<=max_j C_ij b_j, since some outgoing chord exists. Intersect these bounds and round UPWARD on grid10^12. Nine rounds force the normalized root scale<=988248205631/10^12<1. Thus ELEVEN of43 roots are excluded. No remaining root is asserted feasible or excluded.

ORIGIN SCOPE: rays are anchored at the original LOW43 exact centroid. This excludes new bodies whose OWN centroid remains that ray origin; positive balanced-weight global minima satisfy it. Arbitrary physical radial changes followed by recentering elsewhere change the relative directions and are not silently covered.

## Robust angular bound and a one-ray escape witness
Normalize directions u_i and the root radius to1. Envelope endpoints are pi_i u_i, where pi_i is the maximum product of positive direction cosines along simple root paths. There are at most42 edges. If each normalized direction moves by Euclidean distance<=epsilon, each clipped cosine changes by<=2epsilon, each product by<=84epsilon, each endpoint by<=85epsilon and the reflected root by<=epsilon/3. A fixed normalized separating gap can therefore shrink by at most(256/3)epsilon, including changes of optimal path or formerly nonacute edges becoming acute.

The exact root0 gap is>9/2000. For epsilon<=1/20000 it remains>7/30000. This is a conservative open angular exclusion for the same43 labeled directions/root. Deleting rays cannot improve the path envelope; adding rays is outside the exclusion.

Appending z=(-639,68,-766)/1000 as new label43 opens this necessary gate. Recompute every exact path potential for root0. In the new outer envelope, -R0/3 has strictly positive exact barycentric coordinates on labels[4,6,16,20], approximately(.26659777242879756,.051995783221994135,.10397982419993783,.5774266201492705), with nonzero tetrahedral determinant. The point is strictly interior to that tetrahedron, hence to the envelope. The numerical nomination was near the unit bisector of old rays0 and10; exact acceptance uses only the stated rational ray and rational comparisons.

This opens an obstruction, NOT actual mass or U1. Neither the outer envelope nor a completed centered U1/S1 body is asserted to realize the target. One new vertex would use at most44 submitted points/E126, but actual class and mass still need construction. The useful continuation is new angular routes coupled with homogeneous mass and the LOW stable carrier, or deliberate root turnover to an unexcluded label. A root0-retaining exactly centered radial-weight search on the unchanged43 directions cannot reach U1.

## Evidence tier
New exact derivations and computations are one coordinator research line under CPython3.13.5, not independent multi-author audits. Full rational outputs are reproducible from the source/input set; original sandbox paths are not recovery. Numerical dependencies were NumPy2.3.5/SciPy1.17.0. Clarabel/CVXPY was not executed; the implemented solver and exact certificate need neither. Useful nonwinners and finite failed methods are preserved rather than called global exclusions.
