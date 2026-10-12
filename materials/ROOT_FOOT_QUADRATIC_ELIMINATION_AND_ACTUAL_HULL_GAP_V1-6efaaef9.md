# material-6efaaef9ed31

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# ROOT_FOOT_QUADRATIC_ELIMINATION_AND_ACTUAL_HULL_GAP_V1

## Status and scientific scope

Coordinator analytic reduction plus an observed exact computational countercontrol. Bounds 34 <= C_min <= 622 are unchanged. No complete new rooted-tree cover, no whole E17 exclusion and no new class110 attainer is claimed.

The established fixed-shear determinant lift is NOT being rediscovered as a new theorem: its full source is [internal-source-reference], COMMON_HEIGHT_CONICS_AND_REGRESSION_DOMAIN_V1.md, SHA 6bc1f2062d78b1ebdb3bf9231d4ca3bdcc6348ae2ca8746c85165243fe8ae093. What is added here is an exact finite completion of that lift at a fixed actual stable foot, a rational metric box uniform over the whole root facet, a two-variable outer reduction, and an actual well-conditioned mixed-sign packet that survives all three reciprocal-hull facets but fails the single physical determinant relation.

Accepted inputs read completely before this work:

- minimum-0268, SHA c199a4de7b66fb757fbc3f1b2beeb903f7002fe567611824a9f0626b32aa2fc5: actual-covariance Upsilon < 41/5; hypothetical actual E17 joint S1/U1 has condition number of Sigma^(1/2) M Sigma^(1/2) less than 40, and both trace-normalized metric and inverse exceed I/48. This is not an arbitrary-reference or unrestricted U2 assertion.
- minimum-0225, SHA c772d9b01329dcd809a288ef999d910676c13c3334cff8c96e7d59a51b887bdd: complete actual nine-modulus parallel/eleven-modulus projective heptagon–triangle chart and moment fan.
- minimum-0269, SHA 8b4cb712a53d69060ede95fbed7a083b623f87f5d5f4a8aef994b80d7f117684: actual whole-facet convex-hull gap and closed actual-foot disjunction. Its controls are DIFFERENT metrics from the two constructed here.
- minimum-0271, SHA 78c5ee7f94706f5d44ca425624faab7a07c6d99a3b0fee6ba7cb32938ba2b290: the entire five-parameter H5 family is already unconditionally U>=2. The example below is therefore a method countercontrol, not additional minimum coverage.

The elementary rational-extremum argument below is supplied in full. Generic rational quadratic-programming witness theory is established literature, not a novelty claim here; background includes Del Pia, Dey and Molinaro, Mixed-integer quadratic programming is in NP, Mathematical Programming 162 (2017), 225–240, DOI 10.1007/s10107-016-1036-0, whose primary publisher abstract explicitly identifies the classical continuous quadratic-programming predecessor of Vavasis. The present four-variable mechanical specialization and its actual-body certificate do not depend on an unquoted external algorithm.

## 1. Exact physical fibre at a fixed actual foot

Let P be a full-dimensional rational convex polyhedron. Subtract its actual uniform-volume centroid g. Write the centered true vertices as x_i and the true supporting facet poles as q_j, normalized by q_j.x_i=1 on the facet and <1 off it. All metric statements refer to affine images of this actual uniformly filled body; M>0 and N=M^(-1) are one physical pair.

Fix a true facet F with pole q, rational independent tangent vectors t_1,t_2 satisfying q.t_i=0, and a foot f in the closed facet q.f=1. Set H=[t_1,t_2,f]. The foot condition is

f = M^(-1) q / (q^T M^(-1) q).

After the unique positive scalar normalization that makes M f=q, every such physical metric has exactly the form

M = H^(-T) diag(G,1) H^(-1),
N = H diag(G^(-1),1) H^T,
G = [[a,b],[b,c]] > 0.

Indeed H^T M H sends e_3 to e_3 and is symmetric positive definite, so the cross block vanishes and its last diagonal entry is 1. Conversely this block form has M f=q and N q=f. The normalization does not change any equilibrium signs or the covariance condition number.

Introduce d as an independent variable only temporarily. The EXACT physical compatibility is

Q(a,b,c,d) := ac-b^2-d = 0,
a>0, d>0.

At Q=0 these inequalities imply G>0. They are not replaceable by treating d as a second freely chosen height.

Put H^(-1)x_i=(v_i,h_i) with v_i in R^2, and H^Tq_j=(alpha_j,beta_j). Then every true oriented primal primitive is affine in a,b,c:

D_ij = v_i^T G(v_j-v_i) + h_i(h_j-h_i).

After multiplication by the same positive d, every true oriented polar primitive is affine in a,b,c,d:

d E_jk = alpha_j^T adj(G)(alpha_k-alpha_j) + d beta_j(beta_k-beta_j).

Here adj(G)=[[c,-b],[-b,a]] is linear. Selected true-arrow inequalities, negative cap inequalities, and squared-norm comparisons therefore become linear inequalities in four variables. This does not add edges to the mechanical graph. At Q=0, every row uses the same actual inverse N.

For f in the relative interior of F, the root polar outgoing inequalities are automatically strict: E_Fj=q_j.f-1<0 after normalization. A closed-foot domain is safe for lower exclusions; it does not by itself assert a proper stable root at boundary feet.

## 2. A rational compact box uniform over the entire actual root facet

Let Sigma be the actual covariance of the fixed centered P. Suppose the physical covariance metric H_cov=Sigma^(1/2) M Sigma^(1/2) has condition <=K, where K>1 is rational. Set

B(f)=H^T Sigma^(-1) H,
S=[t_1,t_2]^T Sigma^(-1)[t_1,t_2],
L=1/(q^T Sigma q),
U=max_{p a true vertex of F} p^T Sigma^(-1)p.

S is positive definite, L>0, U>=L, and both S and L,U are independent of the foot f. Cauchy–Schwarz and convexity give

L <= f^T Sigma^(-1) f <= U

on the whole closed facet.

For some alpha>0, alpha Sigma^(-1) <= M <= K alpha Sigma^(-1). In root coordinates this becomes

alpha B(f) <= diag(G,1) <= K alpha B(f).

Its last diagonal entry gives 1/(K B_33)<=alpha<=1/B_33. Taking the tangent principal block yields the useful UNIFORM inequalities

S/(K U) <= G <= K S/L.

Consequently all such normalized physical metrics lie in the rational box

a_min=S_11/(K U) <= a <= a_max=K S_11/L,
c_min=S_22/(K U) <= c <= c_max=K S_22/L,
|b| <= (a_max+c_max)/2,
d_min=det(S)/(K^2 U^2) <= d <= d_max=K^2 det(S)/L^2.

The determinant bounds use monotonicity of determinant on positive definite 2x2 matrices. The b bound follows from b^2<ac and the arithmetic–geometric mean inequality. The box is an OUTER bound, not an exact replacement for the condition-number restriction.

For an actual joint S1/U1 candidate in V10/E17/F9, the accepted result above permits K=40. This box does not restrict all U1 or all U2 questions unconditionally. A zero of Q in the box can reconstruct a physical metric outside the original condition gate; an exclusion on the box excludes every metric inside the gate, while a positive feasibility result must be interpreted only with the constraints actually imposed.

## 3. Complete fixed-foot feasibility by rational quadratic extrema

Take a rational fixed f and any finite closed linear packet. Intersect its lifted rows with a rational compact box having a_min>0 and d_min>0, and call the resulting polytope P_f. It may be lower-dimensional or empty.

If nonempty, physical feasibility inside this box is EXACTLY

min_{P_f} Q <= 0 <= max_{P_f} Q.

Necessity is immediate. For sufficiency, choose a point with nonpositive Q and one with nonnegative Q. Their joining segment stays in P_f. Continuity supplies a zero, and a,d>0 there give G>0 and the exact common inverse.

This criterion includes tangencies and isolated zeros. Strict-positive/strict-negative sampling alone would miss a tangent zero. Conversely feasibility of the linear lift alone says nothing about the zero equation.

### 3.1 Exact exhaustive extremum algorithm

Write a quadratic as q(x)=x^T T x/2 + ell^T x+q_0 in n=4 variables and P={Ax>=b}. At an extremizer x*, let F* be its minimal face. Choose an independent subset I of the active rows spanning the affine hull of F*. If Z_I spans ker(A_I), relative stationarity is the RATIONAL LINEAR system

A_I x=b_I,
Z_I^T(T x+ell)=0.

This has the form E_I x=r_I. The quadratic is constant on its entire stationary affine solution set: for the difference v of two solutions, A_I v=0, Z_I^T T v=0, and the tangent first-order term vanishes; hence v^T T v=0 as well.

If E_I has rank r and its intersection with P is nonempty, that bounded intersection has a vertex. It is obtained by adjoining n-r independent active constraints from the original rows. Thus it suffices to enumerate:

1. every independent active set I of size at most four;
2. its full exact stationary affine system, including inconsistent and rank-deficient cases;
3. every completion by four-rank(E_I) original inequalities;
4. exact feasibility of each resulting point.

All feasible extremizers appear. Extra stationary points do not harm taking the minimum and maximum. Empty P is detected as well, because any nonempty bounded polyhedron has a vertex whose active normals span the ambient space, including the lower-dimensional case.

Every extremal value and a realizing point are rational. Degenerate stationary families do not force irrational optimization data. The number of active/completion combinations is O(m^4) in the number m of inequalities: rank(E_I)>=|I|, so the product of the two enumeration counts never has degree above four. All matrices have fixed bounded dimension. This is a fixed-dimension algorithm, not a polynomial-time assertion for arbitrary-dimensional indefinite quadratic programming.

If the physical zero is obtained between rational extremal points, Q on that segment has degree at most two. Hence a nonempty rational fixed-foot fibre inside the box has a physical metric whose entries are in a real extension of Q of degree at most two. End-point zeros give rational metrics. This degree statement concerns the metric, not a claim that every Euclidean square-root coordinate transformation uses the same degree.

The supplied exact program exercises a nonvertex stationary extremum, a lower-dimensional fibre with b=sqrt(2)/2, an isolated tangent zero, a positive-dimensional stationary slice, and an empty bounded polyhedron.

### 3.2 What remains when the foot varies

Write f=f_0+u t_1+v t_2. Since q.f=1, det(H) is constant and H^(-1) is affine in u,v. Every coefficient of a lifted mechanical row has degree at most two in the TWO foot variables. The box in Section 2 stays constant.

The finite active/stationary/completion construction can therefore be stratified by exact rank and pivot signs. On each such stratum its candidate points and their Q-values are rational functions of u,v. Feasibility and value signs become finite polynomial sign conditions after splitting denominator signs. Pairing a nonpositive and a nonnegative candidate at the SAME foot gives an exact finite semialgebraic description of the physical packet's foot set.

This eliminates the metric as an inner numerical unknown. It is an analytic reduction to a two-variable real-algebraic problem for a fixed actual rational body, not an executed whole-facet arrangement. No full two-variable arrangement, complete nine-/eleven-modulus cover, or complete E17 solve has yet been performed here. Different feet or different shapes cannot be mixed by the segment argument.

For complete monostatic search one must still cover the genuine primal and polar rooted escape alternatives and impose the intended strict/physical-weak conclusions. A packet with selected negative signs is a legitimate closed sign-cell obligation but is not automatically a complete rooted tree. The countercontrol below is explicitly of this limited kind.

## 4. Actual well-conditioned countercontrol beyond the reciprocal hull

Use the UNscaled chart body

z0=(1/4,0,0), z1=(37/40,0,0), z2=(22/25,3/25,0),
z3=(3/5,2/5,0), z4=(0,13/40,0), z5=(0,1/4,0),
z6=(1/16,1/16,0), z7=(0,0,1), z8=(3/17,0,1), z9=(0,3/17,1).

Its true outward facet cycles, indexed 0 through 8, are

(6,5,4,3,2,1,0); (8,7,0,1); (7,6,0); (1,2,8);
(9,8,2,3); (9,3,4); (4,5,7,9); (6,7,5); (7,8,9).

The exact source verifies all coplanarities, strict off-facet support inequalities, strict polygon corners and the 17 true edges. The uniform volume and centroid are

Vol=881291/6936000,
g=(7368835529/23971115200, 3427883561/23971115200, 50317/153268).

All moments are computed by the complete oriented 16-triangle boundary formula. Signed tetrahedral integration is used, so the auxiliary origin need not lie inside the raw body. The exact report contains the complete actual covariance and all matrices.

Set x_i=z_i-g and choose the STRICT F2 foot and frame

f=(x7+x6+x0)/3,
t1=x6-x7, t2=x0-x7, H=[t1,t2,f].

The exact foot is

f=(-14615533087/71913345600, -8785455983/71913345600, 2317/459804).

Take

G0=[[513/100,533/100],[533/100,156/25]],
d0=det(G0)=36023/10000,
d_lift=37/25,
r=d_lift/d0=14800/36023,
M0=H^(-T)diag(G0,1)H^(-1),
M1=H^(-T)diag(r G0,1)H^(-1), N1=M1^(-1).

These are TWO separate exact physical metrics on the actual uniformly filled body. Both have the very same strict root foot f. But M0 N1 is not the identity: its eigenvalues are 1/r,1/r,1. The mixed lifted point is (a,b,c,d)=(513/100,533/100,156/25,37/25), not a single physical inverse pair.

### 4.1 It survives the relevant positive and reciprocal restrictions

The source proves, by exact leading principal minors,

(3/20) Sigma^(-1) < M0 < (3/4) Sigma^(-1),
(3/40) Sigma^(-1) < M1 < (3/8) Sigma^(-1).

Thus both actual covariance condition numbers are less than 5. Define

A=H0/tr(H0), B=H1^(-1)/tr(H1^(-1)), H_i=Sigma^(1/2) M_i Sigma^(1/2).

For BOTH k=5 and k=13/2, the source verifies strictly all three reciprocal-hull facets

((k^2+1)/(k^2+k+1)) I - A - B >0,
k A+B-[k(k+1)/(k^2+k+1)]I >0,
A+k B-[k(k+1)/(k^2+k+1)]I >0.

It also verifies A>I/48 and B>I/48. Radical-free congruence by Sigma^(-1/2) evaluates these as rational matrices. k=13/2 exceeds both accepted E17 adjacent-gap ceilings. Therefore this mixed point survives that valid outer reciprocal gate; k=5 shows the gap is not caused by using a loose conditioning threshold.

No claim is made that it survives every stronger nonlinear commutation or common-inverse condition. It deliberately FAILS the exact determinant compatibility.

### 4.2 A closed actual mixed-sign packet separates it from every gated physical metric

The mixed point strictly satisfies

E_6,7 <=0,
D_9,4 <=0,
D_0,1 >=0,
E_1,2 <=0,
D_6,0 <=0.

Primal rows use M0 and polar rows use N1 at the mixed point. For a physical test they would all have to use M,M^(-1). The negative rows are selected sign-cell/cap obligations, NOT all positive arrows of a rooted tree.

After positive primitive-integer rescaling of the lifted rows, the five inequalities are the dot products of the following rows with (a,b,c,d,1), all >=0:

[60868669163655318000, -63554185585986147900, 12084254573768079600, -29593011330043765279, 0]
[-86140111720746732873899, 208148593232705937397874, -71429636109922407907160, 0, 1784450718777208494600]
[8785455983, -26333719274, 17525614616, 0, -13483752300]
[0, 0, 13483752300, -8785455983, 0]
[2, -3, 1, 0, 0].

The Section 2 K=40 bounds for this F2 are strictly inside the simpler rational box

1/20<=a<=231, -222<=b<=222,
1/25<=c<=213, 1/10000<=d<=3172.

The source verifies those inclusions exactly. On the resulting 13-inequality polytope the exhaustive exact quadratic procedure proves

min(ac-b^2-d)
=605818201124721458424534448403904565541192464484047201076833747630633762924922196954450141538125
/1064440400370756632066433402102706252359623948364533190895132267349574080373795916769352614679371008
>1/2000.

The minimum is approximately 0.0005691424347607514. Its unique listed minimizing vertex is reconstructed exactly by setting the FIRST FOUR displayed packet rows to zero. All 1093 active sets of size at most four are considered; 569 consistent stationary affine cases are tested, giving 20 feasible distinct candidates. The entire maximum and all endpoint coordinates are in the deterministic exact report. There is no omitted numerical optimizer in this acceptance calculation.

Therefore no physical M inside the actual K=40 gate, with this exact F2 foot, satisfies this closed mixed packet. The mixed point has G0>0, d_lift>0, satisfies the linear rows strictly, shares one root foot, survives all three reciprocal facets, and nevertheless lies on the wrong side of the determinant surface. This is an ACTUAL-body gap of the relaxation, not a fabricated radial law or a nonrealizable incidence.

### 4.3 Complete physical census of the two controls

The source computes all 68 true primitives for EACH physical metric with its OWN inverse and the actual common raw centroid:

M0: S={0,1,2,4,5,7}, U={1,3,4,6,7}, plus vertex9, hence U={1,3,4,6,7,9}; H consists of edges 06,07,18,23,34,39,49,56,67,79. Proper count (6,6,10).

M1: S={0,1,2,4,5,6,7}, U={0,1,3,4,6,7,9}; H consists of edges 01,06,07,18,23,34,39,49,56,57,67,79. Proper count (7,7,12).

Both have all 68 primitives nonzero and NO physical weak contact. The physical weak test checks that all four primitives on a true edge are nonpositive and at least one vanishes; it is not replaced by Euler's identity. These counts are NOT 110 and are not the 424/525/233 root-mixture controls of the Willow parent or the uncapped222 control of minimum-0270.

The strict sample rows, reciprocal positive matrices, true-lattice guards and the positive compact determinant gap also prove qualitative persistence under sufficiently small actual realization and foot perturbations within the full chart. This is a continuity/compactness conclusion, not an evaluated radius or a new global parameter-domain cover. With positive projective perturbations one must recompute the actual refilled centroid and covariance, not transport the old density.

## 5. Complete durable recovery and observed evidence

Acceptance source: [internal-source-reference], root_fibre_exact.py.txt. Save its exact text as root_fibre_exact.py. Size 16632 bytes; SHA-256 cfdc14d700d7f0c1404200c79bee22a91a0e2066759f716707ec6529f078f10f. It contains ALL actual vertices, true facet cycles, uniform moment formulas, rational metric controls, row generation, complete exact active-set algorithm, all bounds and regression tests. No separate input checkpoint is needed.

Dependency: SymPy 1.14.0. Observed on CPython 3.13.5. No NumPy, SciPy, random seeds or numerical solver is used by the acceptance source.

Reconstruction AND verification command:

python -B root_fibre_exact.py --output-dir OUT

Expected exact output file: root_fibre_report.json, 29674 bytes, SHA-256 b1645226e94d80c1a115d65928493fd36d25b159d2635e2384ef52879c901db5.

Observed standard-output bytes: 504, SHA-256 9ae3a1becdd59a400cd067dff8ba975905cc866178178f409ca931d0ec9c9154. Terminal marker:

ROOT_FOOT_QUADRATIC_ELIMINATION_AND_ACTUAL_HULL_GAP_V1_PASS

The coordinator observed both the ordinary exact run and a fresh directory run containing ONLY the exact source. They produced identical report and stdout bytes. This is evidence for the stated certificate, not independent proof merely from matching a hash.

Optional complete discovery source: [internal-source-reference], root_fibre_discover.py.txt, 5175 bytes, SHA-256 d2ce5758acd2e05f8e7e54e580bb809194075584f2fe5eb93d8f32fbbb0a1ab8. It imports the exact geometry from root_fibre_exact.py and needs NumPy 2.3.5 and SciPy 1.17.0 in addition to SymPy 1.14.0. The explicit seed is 943012, 250 trials maximum, all distributions, tolerances and greedy choices are literal. Run with OPENBLAS_NUM_THREADS=1. Its observed trial7 finds the mixed packet; no numerical infeasibility from that locator is accepted without the exact source.

Discovery command:

OPENBLAS_NUM_THREADS=1 python -B root_fibre_discover.py

Observed discovery JSON: root_fibre_discovery.json, 891 bytes, SHA-256 47fe3de9c1b977f33410c4ff7dcf0687049908307c578a3dc1fa7c0cc07ba8c7. Discovery stdout: 322 bytes, SHA-256 d94773414ffe27b1d2742a348493423b27eccee1df8bd5439a24f6f0fab1c4a9. Floating output is platform-sensitive; the rational acceptance control is not.

The source units above, not an ephemeral sandbox file or just the output hash, reconstruct the complete result. Optional discovery is unnecessary for a computational successor that only needs the exact mechanical solver and countercontrol.

## 6. Next scientific connection

The useful continuation is exact common-inverse feasibility across ACTUAL root-foot domains and genuine complete escape alternatives, preferably in remaining basal/nonparallel moduli or other unresolved E17 geometry. It is not another proof that this already closed five-parameter calibration has U>=2. The five-row countercontrol proves why reciprocal-hull feasibility should not be promoted to a physical surviving metric. The two-foot-variable reduction supplies a way to retain the missing determinant relation without searching independently over six entries of M and six entries of N.
