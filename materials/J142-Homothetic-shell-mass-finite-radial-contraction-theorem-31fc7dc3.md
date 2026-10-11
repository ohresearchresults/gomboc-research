# material-31fc7dc3eef5

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J142 — finite homogeneous-moment capacity of radial envelopes

## Scientific result and scope
No new own110 body is claimed. Canonical V176/E311/F137,C622 is unchanged and outside the requested C<500 goal.

On the exact rays from the ACTUAL homogeneous centroid of QW49J_LOW62_G9, any own-centred weak-U-free single-U construction whose unique root is raw9 must contract at least one radius by MORE THAN 167881/500000 = 33.5762% relative to its root9 all-path envelope. For root raw45, the necessary contraction exceeds 368197/1000000 = 36.8197%. These are finite necessary changes, not sufficient construction conditions and not exclusions of the whole fixed-ray family. Root-normalization, the exact original origin, and the specified ray set matter. Another root, new or moved directions, a different origin, and larger nonuniform contractions remain open.

The direct immutable input result figure-0622 was read completely, unchanged SHA256 f63d80e0ada03ac98308d1bd82ccb12165bfc671f6f98a9f940ef747fa5d511e. This is not an independent replay of all its mechanics. Its selected input is QW49J_LOW62_G9_INPUT.json,2182 bytes,SHA25690cc88f1a89396ed5cbe20e84cb4fc8265ae1b4170cc2d5bf245c024d4c4662e. The new calculation reconstructs its exact hull and homogeneous centroid because those are the actual required ray coordinates. Its reported own121/weak000/primitive000 census is not reclassified by the present source.

## 1. A signed-moment inclusion theorem
Let A and B be full-dimensional convex bodies with 0 interior and A subset B. Let n be any nonzero vector. Define
Jplus(T)=integral_T max(n.x,0) dx,
Jminus(T)=integral_T max(-n.x,0) dx.
For ANY measurable filled L satisfying alpha*A subset L subset B,0<alpha<=1,

integral_L n.x dx >= alpha^4 Jplus(A)-Jminus(B).

Indeed the positive integral contains that of alpha*A, the negative integral cannot exceed that of B, and in three dimensions volume times a linear functional scales by alpha^4. Therefore a strictly positive right side rules out centroid0 for every such L. This relaxes convexity of L, all intermediate incidences, the number of points/facets and any equilibrium condition. It is a finite physical mass-capacity inequality, not a Jacobian-rank or optimizer-status argument.

For A=B=H the displayed lower bound is attained by the measurable set alpha*H union (H intersect {n.x<=0}). That union is generally NONCONVEX. Its moment sharpness does not prove that a homogeneous convex polyhedron realizes the relaxation or that the chosen directional threshold is optimal among all separators.

## 2. Why the bound applies to every single-root radial policy
Write the exact LOW62 raw vertices as x_i, their exact homogeneous centroid as g, and R_i=x_i-g. For a candidate K=conv{a_i R_i},a_i>0,centroid0,unique strict U at r and no weakU, normalize a_r=1 by a common positive homothety.

Every nonroot submitted point has a nonnegative outgoing global chord to a distinct submitted extreme point. For an extreme nonroot this follows from exclusion of both strict and weak U; for a nonextreme point it follows by writing that point as a convex combination of extreme points. A nonnegative chord between distinct points strictly increases squared radius, so these arrows terminate at the sole root. Along an arrow i->j,
a_i <= C_ij*a_j, C_ij=max(0,R_i.R_j/|R_i|^2).
Let p_i be the greatest product along ALL paths to r, with p_r=1. Then a_i<=p_i, independently of the selected witness tree, input retirement or later adjacency. The exact program reconstructs p from rational equality paths and verifies EVERY Bellman inequality, including the root; the equality paths establish attainment of the closed envelope values.

Set H=conv{p_i R_i}. To avoid unnecessarily large output arithmetic, round each exact p_i DOWN and UP on denominator10^12, obtaining p_i^-<=p_i<=p_i^+ and H^-/H^+. The exact original positive spanning of the rays persists under any positive radial factors. If all k_i=a_i/p_i are at least alpha, then
alpha*H^- subset K subset H^+.
For example, alpha*p_i^- R_i is a convex combination of a_iR_i and0; the other inclusion is analogous. Thus the signed-moment theorem applies even when submitted candidate points retire.

## 3. Executed exact constants
For root9 use n=(-242532,101335,-964837)/10^6 and alpha=332119/500000=.664238. Exact rational integration gives
alpha^4 Jplus(H^-)-Jminus(H^+) in (437296,437297)/10^12 >0.
The directional rounded-envelope critical alpha lies strictly between664237732872/10^12 and664237732873/10^12. This interval is not a global optimum or an existence threshold. H^- and H^+ both have62 vertices,180 true edges,120 triangular maximal facets. Their volumes are approximately3.68578408414819 and3.685784084154884; their centroids are near(-.0504866197984,-.0230242441690,-.3059685280833), not0.

For root45 use n=(-69210,724445,685850)/10^6 and alpha=631803/1000000. Exact gap:
alpha^4 Jplus(H^-)-Jminus(H^+) in (45932,45933)/10^12 >0.
The analogous directional critical interval is(631802808024,631802808025)/10^12. Both rounded envelopes again have62/180/120. Their volumes are approximately1.0711029543814365 and1.0711029543847213, with centroids near(.0622751975889,.1067901630374,.1648951916717), not0.

The normal vectors need not be unit: positive scaling leaves the sign and alpha threshold unchanged. The exact result is a contradiction to centroid0 whenever ALL candidate radii lie inside the respective closed envelope box. Consequently at least one ratio k_i is STRICTLY below the stated alpha. It does not identify a sufficient set of contractions or prove any target mechanical class.

## 4. Exact integration and geometric reconstruction
The source exhausts all integer supporting triples for the parent and four rounded envelopes, constructs maximal facet polygons by exact planar convex hulls, and checks opposite oriented edge incidences, Euler, total outward area vector0 and positive origin support heights. No Qhull proposal or floating plane grouping is used by the verifier. Exact homogeneous mass fixes the ray origin.

Triangulate each outward maximal face and join to0, producing positive tetrahedra. For one tetrahedron of volume v, let a<=b<=c be the three nonzero-vertex values of n.x; the fourth value is0. Its positive first moment is v/4 times:
0 if c<=0;
a+b+c if a>=0;
c^3/((c-a)(c-b)) if b<=0<c;
[bc(b+c)-a(b^2+bc+c^2)]/((b-a)(c-a)) if a<0<b.
The one-positive case follows by clipping to a similar tetrahedron at the positive vertex. The two-positive formula follows by subtracting the one-negative contribution from the total affine integral and cancelling the repeated-height factor. Denominators only join opposite-sign heights; equal-height cases are safe. These formulas supply exact Jplus; Jminus=Jplus-n.M.

## 5. Preservation, execution and limitations
The companion complete exact source consists of the unchanged2182-byte input,506-byte RECIPE142.json and7386-byte exact142.py. It is standard-library Python, uses Fraction and integer hull predicates, and reconstructs the entire result without an originating sandbox, numerical solver or inherited mechanics engine. Run python -B -S exact142.py with assertions enabled. Executed under CPython3.13.5.
RECIPE142.json SHA2564522da08fce645bdf50dd63a44e2198a1d476aeb1e5c516fc1daa94a9d34e20c.
exact142.py SHA2564db4b57869d417d2f8b9045e0fbb76c93e439bafbf746194c6201d3e17e06dd1.
Executed EXACT142.json196328 bytes,SHA256178abeb7f0a404c1db0021fe7f1c4ec580b0eb9970a6279e890f7c7955b6fd6f.
Markers J142_HOMOTHETIC_SHELL_EXACT_RADIAL_BOX_EXCLUDED for roots9/45, then J142_TWO_FINITE_MASS_GAPS_EXACT_PASS_NO_110.

Numerical separator nomination used an unconstrained two-dimensional convex minimization of Jplus(n) with fixed n.M. Root9 returned a precision-loss status with small gradient; root45 reported convergence. NEITHER solver status is used as evidence of optimality or of the exclusion. Only the frozen integer normals and subsequent exact strictly positive gaps are the certificates. Complete numerical nomination source and input are preserved separately with the producing methods.

This result transfers the earlier finite shell-capacity mechanism to the current all-policy radial problem. It greatly enlarges the specific J141 small excluded neighborhoods, while leaving the actual construction problem open. The scientific next step is a finite nonlocal radial/angular change with compatible uniform mass and both CURRENT equilibrium landscapes, rather than tiny descent about either maximal envelope.
