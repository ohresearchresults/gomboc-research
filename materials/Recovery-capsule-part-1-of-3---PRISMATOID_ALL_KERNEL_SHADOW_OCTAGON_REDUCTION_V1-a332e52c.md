# material-a332e52cafe0

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# PRISMATOID_ALL_KERNEL_SHADOW_OCTAGON_REDUCTION_V1
## Recovery capsule part 1 of 3: theorem, exact scope, proof and manifest

This is a coordinator analytic/computational continuation of the fully read immutable result minimum-0221, SHA256 20401ae433a796bdb71558693d93418b6b95bdf7d0eaa6354caf222ee47085a6, THREE_LEVEL_NORMAL_RETRACTION_AND_ACTUAL_FIVE_WEAK_CONTROL_V1. That parent contains the actual prismatoid family, uniform moments, normal retraction theorem and exact nonwinning five-contact controls. It is a required conceptual parent, not a claim that those controls were independently replayed. The new finite visibility certificate is executed here and is independent of the parent's code.

The result concerns the WHOLE four-cut heptagon-triangle prismatoid family defined below, and its affine images. It does NOT concern all prismatoids, all realizations of its graph, or the different fixed-six-pole star-centred HEX6 atlas. No new U1 or110 attainer is found. The global interval remains34<=C_min<=622.

## 1. Actual family and unambiguous labels
Parameters satisfy H>0,p>0,q>0,p+q<1,0<a<1-q,a<b<min(2a,1-p). Vertices are

  Y0=(b,0,0), Y1=(1-p,0,0), Y2=(1-p,p,0),
  Y3=(q,1-q,0), Y4=(0,1-q,0), Y5=(0,a,0),
  Y6=(2a-b,b-a,0), Y7=(0,0,H), Y8=(1,0,H), Y9=(0,1,H).

Maximal outward facet cycles, in order F0 through F8, are

  (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
  (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

True edges are

  01,06,07,12,18,23,28,34,39,45,49,56,57,67,78,79,89.

These are10/17/9 genuine features. Write P=conv(Y_i), g for its ACTUAL uniform solid volume centroid, and X_i=Y_i-g. Changing H to1 by z/H is an affine gauge; carry the physical metric rather than replacing it by I. Every metric and inverse below are at this same actual origin.

For complete moment recovery let

  A_A=(a^2+(b-a)^2)/2, A_B=p^2/2, A_C=q^2/2, R=A_A+A_B+A_C,
  J_A=(a(3b^2-6ab+4a^2), b(b^2-3ab+3a^2))/6,
  J_B=(p^2/2-p^3/3,p^3/6), J_C=(q^3/6,q^2/2-q^3/3).

Then

  V=H(1/2-R/3),
  J_x=H[1/6-(J_Ax+J_Bx+J_Cx)/4-A_B/12],
  J_y=H[1/6-(J_Ay+J_By+J_Cy)/4-A_C/12],
  J_z=H^2(1/4-R/12), g=J/V.

These are genuine removed-volume moments from the parent, not fitted planar masses. The new verifier independently uses positive interior-cone tetrahedra at each of its26 rational witness geometries.

## 2. Complete all-parameter generic visibility classification
Set H=1. Every kernel with k_z!=0 has representative k=(u,v,1). Use the projection

  L_k(x,y,z)=(x-u z,y-v z).

Translation by g does not affect shadow corner counts. The seven side-facet visibility values, in the EXACT order F1,...,F7, are

  -v, -u-2v-b, u-p, u+v, v-q, -u, -u-v-a.

F0 is negative and F8 positive. A generic kernel makes all seven values nonzero. A mask has bit j set when F(j+1)'s value is positive, with j=0,...,6.

All possible masks can be classified by homogeneous STRICT linear inequalities in variables (a,b,p,q,u,v). The five shape rows express

  a>0, p>0, q>0, b-a>0, 2a-b>0.

Append the seven visibility rows with the requested signs. No masks are lost by temporarily omitting p+q<1,a+q<1,b+p<1: a positive simultaneous scaling of all six variables preserves every homogeneous sign and makes these three upper bounds true. Conversely every actual body is in this homogeneous shape cone.

The exact executable enumerates all128 masks, without a numerical solver:

-102 masks have a supplied positive INTEGER dependence among their12 strict rows. Every dependence has3 through7 terms, weights1 or2, and its sum is the zero six-vector. This is a complete strict infeasibility certificate.
-26 masks have explicit rational witnesses satisfying the complete actual parameter domain, all visibility signs, all true maximal face supports and all projected hull checks.

The generic corner-count distribution is

  5 corners:3 masks; 6 corners:8 masks; 7 corners:10 masks; 8 corners:5 masks.

There are NO generic9- or10-corner shadows anywhere in the whole family. The five8-corner masks and their canonical unoriented boundary cycles are

  11 : (0,1,8,2,3,9,7,6),
  35 : (0,1,8,9,4,5,7,6),
  71 : (0,1,2,8,9,7,5,6),
  97 : (0,1,8,9,4,5,6,7),
  114: (0,6,5,4,3,9,8,7).

Every step of every cycle is a TRUE edge from the preceding list. No two of these five masks differ in exactly one bit.

Why this finite sign computation counts corners throughout a chamber: for a generic kernel, a true edge is on the silhouette exactly when its two incident facet visibility signs are opposite. No true edge can collapse under the projection, since that would make both incident facets parallel to k. No two consecutive silhouette edges can become collinear without their common facet becoming parallel to k. A projected extreme corner has a singleton true-vertex fibre: a nontrivial fibre would contain a true edge parallel to k. Thus the number of opposite-sign edges equals the number of true shadow corners, throughout the chamber, not merely at its one witness.

The102 exact linear exclusions cover all parameters in the homogeneous cone. The26 witnesses certify existence, but the universal upper count is NOT inferred from sampling those witnesses.

## 3. Every nongeneric visibility wall has at most seven corners
For any fixed admissible actual shape, the seven visibility zero lines in the (u,v) plane are pairwise distinct:

  v=0, u+2v=-b, u=p, u+v=0, v=q, u=0, u+v=-a.

At a point on exactly one line, its two adjacent generic masks differ in one bit. They cannot both belong to the five octagon masks. Hence a generic shadow with at most seven corners approaches every such wall point from at least one side.

At a multiple line intersection, points on exactly one incident line approach the intersection. Apply the preceding argument successively to obtain generic shadows with at most seven corners tending to it. A convex hull of a fixed finite number of continuously moving points cannot gain true vertices at the limit: every strict exposed vertex of the limit persists in a small separated neighborhood. Thus every visibility-wall shadow has at most seven corners.

For k_z=0, each of the two parallel vertex planes projects to an affine line. Their two projected segments have at most four hull corners. This accounts for the missing kernel directions at infinity of the (u,v) chart.

Conclusion: EVERY shadow of this whole family has at most eight true corners, and any eight-corner shadow is strictly inside one of the five displayed open chambers. In particular no unanalysed weak visibility wall can hide an eight-corner candidate.

## 4. Mechanical reduction:320 necessary true boundary-path systems
Here two accepted analytic premises are used, not independently recomputed:

(A) The seven-corner shadow theorem, explicitly used by the immutable parent: a full-dimensional planar Q with0 interior and -Q/3 subset Q, at most seven true corners, cannot have just one strict radial-maximum corner under any planar SPD metric. Actual uniform3D own-centred shadows satisfy this asymmetry condition, and distinct strict maximum corners give distinct closed TRUE exposed fibres.

(B) The parent's normal-level retraction: every SPD weak-U1 metric on a prismatoid can be descended, preserving its selected genuine weak rooted tree, to a rank-two rooted metric. There is no additional singular-disconnected U1 component on this family. Rank-one rooted metrics are impossible.

Combining(A),(B) with Sections2-3: any SPD U1 member anywhere in the entire four-cut family must produce a rank-two rooted metric whose kernel lies in one of the five open octagon chambers above. Its root is one of that cycle's eight singleton true-vertex fibres.

At a planar nonroot corner, failure to be a strict radial maximum implies that at least one of its two boundary arrows is nonnegative. For an SPD planar metric a nonnegative arrow strictly increases squared norm because adjacent projected corners are distinct. Hence those choices are acyclic and contain a spanning boundary path oriented toward the sole root. Each eight-cycle has eight choices of root and eight choices of the deleted edge. This gives

  5 chambers * 8 roots * 8 deleted edges =320

necessary weak rooted boundary-path systems. These are a complete NECESSARY cover for ALL SPD U1 candidates in the whole family, not just an independently chosen singular slice. They have NOT been shown infeasible. Feasibility of one of these paths alone is not an actual U1 construction: other true projected vertices, zero arrows and the normal-height lift still require the parent's complete genuine-graph conditions. S1/H0 and physical weak exclusion require the SAME inverse metric and are not supplied by this reduction.

## 5. Explicit compact metric/kernel bounds for joint S1/U1
This section is analytic and uses only the actual uniform-centroid depth bound and the accepted opposite-cap spectral argument. It is separate from the executed visibility certificate.

In the H=1 coordinates, P is contained in the unit cube. Its top triangle has area1/2; the pyramid joining that triangle to any bottom vertex lies in P, so V>=1/6. The orthogonal projection of the unit cube normal to a unit n has area |n1|+|n2|+|n3|<=sqrt(3), as follows by projecting its three generating segments. Every slice normal to n has area at most that projection area. Thus every width of P is at least1/(6sqrt(3)). The actual uniform centroid is at depth at least one quarter of every width from each support plane, giving

  r B subset P-g subset R B,
  r=1/(24sqrt(3)), R=sqrt(3), Gamma=R^2/r^2=5184.

The opposite-cap maximum argument and its same-origin polar version imply, for S=U=1,

  lambda1/lambda2<Gamma, lambda2/lambda3<Gamma,
  condition(M)<kappa=Gamma^2=26873856.

After tr M=1,

  lambda_min(M)>1/(Gamma^2+Gamma+1)=1/26879041.

These statements do NOT apply to U1 alone. They apply to simultaneous strict S1/U1 even with other weak contacts. The original source-height normalization changes the physical metric; no metric is silently fixed.

For normal descent n=e3, write

  M=[[G,-G w],[-w^T G,w^T G w+delta]],
  w=(u,v), G SPD, delta>0.

Its rank-two endpoint is L_w^T G L_w and has kernel(w,1). Also w is the horizontal part of N e3/(e3^T N e3), N=M^-1. If the extreme eigenvalues of N are m,L, then

  ||N e3||^2 <= (m+L)t-mL, t=e3^T N e3,

by applying (lambda-m)(lambda-L)<=0 spectrally. Optimizing the resulting ratio gives

  ||w||^2 <= (L-m)^2/(4mL).

Consequently condition(M)<Gamma^2 gives the explicit necessary joint bound

  u^2+v^2<2592^2=6718464.

Rescale M so tr G=1. Since condition(G)<=condition(M)<kappa, and since the Schur complement delta lies between lambda_min(M) and lambda_max(M),

  lambda_min(G)>1/(kappa+1)=1/26873857,
  1/(2kappa)<delta<kappa/2,
  i.e. 1/53747712<delta<13436928.

For the last inequalities use lambda_max(M)>=lambda_max(G)>=1/2 and lambda_min(M)<=lambda_min(G)<=1/2. These are effective necessary boxes for a joint110 search in the original parameter chart. They do not supply an evaluated distance of shape parameters from incidence-degeneration boundaries, and do not exclude the320 systems.

## 6. Exact polynomial forms for the remaining systems
With H=1 for the body height and G for the planar physical metric, V has degree at most2 and J has degree at most3 in the four shape variables. The projected centred vertex is

  Z_i=(Y_ix-g_x,Y_iy-g_y)-w(Y_iz-g_z).

Define its denominator-cleared numerator and the projected edge by

  A_i=V(Y_ix,Y_iy)-(J_x,J_y)-w(V Y_iz-J_z),
  E_ij=(Y_jx-Y_ix,Y_jy-Y_iy)-w(Y_jz-Y_iz).

Since V>0, the exact weak arrow condition is

  A_i^T G E_ij>=0.

A_i has degree at most3 in(a,b,p,q,u,v), E_ij degree at most1, so each row is degree at most4 in those geometric variables and LINEAR in the three entries of G. Shape and visibility constraints are linear strict inequalities. This is the actual3D uniform-centroid problem, not a uniformly filled planar polygon or independent moment fit. The parent's normal-height interval and complete graph remain necessary to lift any surviving shadow solution.

## 7. Exact recovery, correction and observed execution
This capsule has THREE required parts. The historical title of part2 says2 of2 because a transcription repair was necessary; that title does not make it standalone authority.

Part1 is this theorem/manifest.
Part2 is [internal-source-reference],12509 bytes, SHA256336ba77e923ba1b362135d91c5bfb112825d1d09288a2f3396d90c7f357cadb9. It contains the full verifier and all128 exact classification cases, but ONE character in the rational witness for mask98 was copied incorrectly. Do NOT execute/promote it without part3.
Part3 is [internal-source-reference], repair_prism_shadow.py.txt,1107 bytes, SHA256cae66b715ce3d9a6fb60c40c611c2b36cca85b0a4e95533d3fd4fe1b9d47495f. Its complete standard-library program asserts the entire part2 input hash, repairs exactly the unique mask98 witness coordinate q from1/5 to2/5, then asserts the entire output hash. No omitted source is required.

Save part2 verbatim as prism_shadow_part2_literal.py.txt and part3 verbatim as repair_prism_shadow.py, preserving UTF-8/LF final newlines. Run

  python -B repair_prism_shadow.py prism_shadow_part2_literal.py.txt prism_shadow_exact.py
  python -B prism_shadow_exact.py build > build.out
  python -B prism_shadow_exact.py check > check.out
  cmp build.out check.out

Python>=3.11, assertions enabled, standard library only. No solver, RNG, floating tolerance, network, old source or external array is required. The discovery exploration used linear programming to find some rows, but no floating status is part of the proof: the final verifier tests all rational witnesses and all positive integer row identities exactly with Fraction arithmetic.

Pins after the REQUIRED repair:

  prism_shadow_exact.py:12509 bytes,
  SHA2565023d1f20dea0654406ca5812431110f2218bd9262e5e2913146e0745f9383c7;
  prism_shadow_exact.json:39477 bytes,
  SHA2561480bb93b6a83e133d174b6dde0763c67839e010d62fffa424eb46ae60bfa870;
  identical build.out/check.out:327 bytes,
  SHA2569a7d88729dc4c034f9e2ccac05b81bf5da6c3759873f7cac21f1c18456e80ec8.

Observed: normal build/check completed, then a new directory received only the recovered source and independently generated the same report and identical stdout. The repair input hash was obtained by changing exactly the stated character in the executed good source; it equals the immutable part2 hash. This is an observed source-only replay of the coordinator's implementation, not a separately authored mathematical verifier or proof-assistant formalization.

Expected stdout:

  EXACT_ALL_128_VISIBILITY_PATTERNS_CLASSIFIED 26 102
  EXACT_GENERIC_CORNER_COUNTS 5:3 6:8 7:10 8:5
  EXACT_FIVE_NONADJACENT_OCTAGON_CHAMBERS 11 35 71 97 114
  ACTUAL_UNIFORM_CENTROIDS_AND_26_RATIONAL_SHADOW_WITNESSES_PASS
  PRISMATOID_SHADOW_OCTAGON_RECOVERY_PASS 39477 1480bb93b6a83e133d174b6dde0763c67839e010d62fffa424eb46ae60bfa870

## 8. Scientific disposition
The exact new conclusion is a whole-family projection classification and a320-system necessary mechanical reduction, plus explicit necessary joint metric/kernel bounds. It removes all other kernel chambers and all visibility walls for U1 by the accepted seven-corner theorem and normal retraction. It does not solve the surviving eight-corner inequalities, produce a U1 body, exclude all realizations of the true graph, or change34<=C_min<=622. The next meaningful research is the actual-centroid octagon systems and their genuine normal-height lifts, rather than enumerating a singular-disconnected component which the parent already excluded.
