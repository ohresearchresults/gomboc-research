# material-471eaeee3d9f

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# CENTERED_CIRCUIT_RANK3_V1
## A rank and positivity theorem from full first moments, with an exact cubic realization model

### Status and scope
This is a new coordinator-derived algebraic theorem and its physical application. Its proof is below; the accompanying exact computations are controls of the formulas, not a substitute for the proof. It neither excludes all (10,17,9) bodies nor raises the current universal lower bound C>=34. It applies to arbitrary fixed genuine convex-three-polytope incidence, not only TREE253/K2. Homogeneous mass always means constant volume density, centered at the body's own volume centroid. No assumption about the polar body's own centroid is made.

The full determinant family is essential. This result does not assert exactness of a moment relaxation with independent per-cell Gram matrices, only supported moments, or omitted determinant-extension equations. The equations below remain bilinear, and positivity of the anchor includes a cubic inequality; removing explicit rank and global PSD constraints does not make the problem convex.

### 1. Algebraic definitions
Let n>=4, let e_i be the coordinate vectors of R^n, and let D_t be real numbers indexed by every increasing four-subset t of {0,...,n-1}. Extend D by alternation to ordered four-tuples. Let chi_t=sum_(i in t)e_i. For an increasing five-set S=(s_0,...,s_4), put

c_j=(-1)^j D_(S without s_j),
v_S=sum_(j=0)^4 c_j,
z_S=sum_(j=0)^4 c_j e_(s_j),
m_S=sum_(j=0)^4 c_j chi_(S without s_j).

The elementary identity m_S=v_S chi_S-z_S will be used repeatedly.

Let G be a REAL SYMMETRIC n by n matrix. Initially G need not be positive semidefinite and no rank bound is imposed. Fix an increasing anchor A=(a_0,a_1,a_2,a_3) with D_A!=0 and a vector b with 1^T b!=0. Suppose

G b=0,
v_(A union {j})=0 and G m_(A union {j})=0 for every j outside A.       (1)

Only these n-4 anchor circuits, not all five-sets, are required in the next theorem. Define the n by 3 matrix T with columns e_(a_k)-e_(a_0), k=1,2,3, and K=T^T G T.

### 2. Rank is forced by centering
**Theorem 1.** Under (1), rank G<=3. If the three leading principal minors of K are strictly positive, then G is positive semidefinite of rank exactly3.

**Proof of the rank assertion.** For every j outside A, the coefficient of e_j in z_(A union {j}) is either D_A or -D_A and is nonzero. Divide z by that coefficient and call the result w_j. By m_S=-z_S and (1), G w_j=0. Each w_j has zero coordinate sum. Its coordinates outside A are zero except for the jth coordinate, which equals1. Therefore the n-4 vectors w_j are linearly independent. Any linear combination of them has coordinate sum zero. Since 1^T b!=0, b is independent of all of them. Thus ker G has dimension at least n-3, proving rank G<=3. For n=4 the empty family w_j and b alone give the same conclusion. This argument uses no positivity.

**Proof of the positivity assertion.** Positive leading minors give K positive definite by the elementary symmetric elimination criterion. In particular T has three independent columns and rank G>=3. Hence rank G=3. Complete the columns of T to a basis of R^n. In this basis G has the symmetric block matrix [K B;B^T C]. Congruence by block elimination gives [K 0;0 C-B^T K^(-1)B]. Its total rank is3 and K has rank3, so the Schur complement is identically zero. The congruent matrix is therefore positive semidefinite; so is G. This proves the theorem. QED.

The criterion needs only three strict polynomial inequalities of degrees1,2,3 in the entries of G. It does not require all principal minors of G or any four by four rank-minor equations.

### 3. All first moments force the true determinant family
Assume, in addition, v_S=0 and G m_S=0 for EVERY five-set S, and the positive anchor hypothesis of Theorem1. Factor G=X X^T with X an n by3 matrix of rank3, and write x_i for its rows. Since K=(X^T T)^T(X^T T) is positive definite, the three differences x_(a_k)-x_(a_0) are independent. Thus the points are affinely full-dimensional.

**Theorem 2.** There is one common nonzero real number c such that

D_abcd=c det(x_b-x_a,x_c-x_a,x_d-x_a)                        (2)

for every increasing a<b<c<d.

**Proof.** Gm=0 is equivalent to X^T m=0: if Gm=0 then ||X^T m||^2=m^T Gm=0, and the converse is immediate. Together with v_S=0 and m_S=-z_S, this gives sum_j c_j x_(s_j)=0, as well as sum_j c_j=0.

View D as an element of the exterior space Lambda^4(R^n), with coordinates D_t in the increasing coordinate basis. Let w_0=1 and w_1,w_2,w_3 be the three coordinate columns of X. The last equations are exactly D wedge w_k=0 for k=0,1,2,3 (the expansion on each five-set has the signs (-1)^j). These four vectors are independent by affine full-dimensionality. Complete them to a basis of R^n and expand D in the induced exterior basis. Wedge with w_0 forces every nonzero basis monomial to contain w_0: distinct monomials omitting w_0 have distinct products with w_0 and cannot cancel. Repeating with w_1,w_2,w_3 leaves only a multiple of w_0 wedge w_1 wedge w_2 wedge w_3. Its coordinates are the four-row affine determinants, equal to the determinant of the three difference rows in (2). Since D_A!=0, the multiple is nonzero. QED.

Consequently all higher polynomial simplex-chain moment identities follow in this full, noncollapsed model; imposing second moments separately is unnecessary for physical determinant recovery. For example, with J_t=chi_t chi_t^T+diag(chi_t), one obtains sum_t r_t D_t X^T J_t X=0 for every five-simplex boundary row r. To see the general statement directly, map an oriented abstract four-simplex affinely to R^3 and apply Stokes to the pullback of p(x) dx_1 wedge dx_2 wedge dx_3: its exterior derivative is zero. The oriented tetrahedral integral of any polynomial p therefore sums to zero. This consequence concerns the full nonlinear shared-coordinate model, not the weaker separated matrix-certificate cone.

### 4. A complete fixed-incidence physical realization system of degree at most3
Fix the genuine face lattice of an abstract convex three-polytope with n vertices and f maximal facets, including each facet's cyclic true-vertex boundary. The input is a valid polytope face lattice, not merely an arbitrary incidence table. Coherently orient the boundary sphere. Let U be all four-sets formed by three vertices of one facet and a vertex outside that facet. For each occurrence (a,b,c,d) in cyclic facet order, let epsilon_t be its orientation parity relative to increasing order. Choose the coherent global sign; all occurrences agree for a valid convex face lattice. Actual coordinates with this boundary orientation satisfy D_t=sigma epsilon_t times a positive unsigned determinant, for one common sigma.

Let Z be all four-sets contained in a listed facet. Fix an apex vertex and triangulate each nonincident genuine polygonal facet by a fan from its first cyclic vertex. Denote the resulting reference tetrahedra by f0(t) (multiplicity1; the formulation also allows the literal multiplicity if needed). This is an integration triangulation, not a new mechanical edge set. Define

w_t=epsilon_t D_t for t in U,
N=sum_(t in reference) f0(t) w_t,
b=sum_(t in reference) f0(t) w_t chi_t.

Choose ANY anchor A in U. Its strict positivity will ensure D_A!=0. Introduce variables G=G^T, the entire D family, and u_f in R^3 for every listed facet. Form T,K as above and define

B_vf=(G T u_f)_v,
J_fg=u_f^T K u_g.

Impose the following polynomial conditions:

(a) v_S=0 and Gm_S=0 for every five-set S;
(b) D_t=0 for t in Z, w_t>0 for t in U;
(c) N=1 and Gb=0;
(d) all three leading principal minors of K are positive;
(e) B_vf=1 at every listed vertex-facet incidence, and B_vf<1 at every nonincidence.

**Theorem 3.** This system is equivalent, up to Euclidean orthogonal transformations and the harmless common determinant normalization, to a full-dimensional convex realization of precisely the prescribed true face lattice, at its own homogeneous volume centroid. The variables J are the Gram values of its genuine facet poles relative to that same origin. No PSD condition or explicit rank constraint is needed beyond (a)-(e).

**Forward proof.** Since N=1, the definition of b gives 1^T b=4. Theorems1 and2 apply: G=X X^T has rank3, the anchor differences span R^3, and all D are one common multiple of the actual affine determinants. Let H=X^T T, an invertible three by three matrix, and q_f=H u_f. Then B_vf=x_v dot q_f and J_fg=q_f dot q_g. Conditions(e) are exact supporting-plane inequalities q_f dot x<=1 with strict separation of all nonincident vertices.

For distinct vertex labels v,w, some listed facet contains v but not w, because the input face lattice is that of a polytope. The strict inequalities show x_v!=x_w. Each x_v is an extreme point of P=conv{x_i}: a convex combination of other x_w equal to x_v would have to use only vertices on every listed facet incident to v, by equality in all those support inequalities. The intersection of these vertex sets is {v} in the prescribed face lattice, a contradiction. P is full-dimensional by the anchor.

Each listed facet contains at least three distinct extreme points. Three distinct collinear points cannot all be extreme points of a convex hull, so it is a genuine two-dimensional supporting facet. The support inequalities make its full vertex set exactly the prescribed set. Every prescribed edge is the intersection of its two prescribed facets: their common true-vertex set consists of its two endpoints, and an intersection of two supporting faces is the convex hull of their common vertices. Thus every prescribed edge is a true edge of P. An m-vertex convex polygon has exactly m edges, and its m prescribed cyclic edges have now all been obtained. Therefore each listed facet has no unaccounted boundary edge; every neighboring facet across one of its edges is already listed. The facet-adjacency graph of a convex three-polytope is connected: radial projection from an interior point to the sphere allows a path between facet interiors avoiding the finitely many vertices and crossing only edges. Hence no additional unlisted facet can exist. The prescribed true face lattice is exactly recovered.

The reference apex tetrahedra now genuinely partition P, apart from shared boundaries. By(2) and positivity, their w_t are a common positive multiple of their unsigned determinants. Equation N=1 normalizes their total; their tetrahedral centroids are one quarter of the sum of their vertices. Finally Gb=0 implies X^T b=0, so the actual volume centroid of P is zero. The poles q_f are normalized by q_f dot x=1 and are therefore the genuine polar vertices of this same origin. The positive-density volume centroid lies in the interior: every nonconstant support functional is strictly below its support maximum on a set of positive volume. There is no polar-volume recentering.

**Converse proof.** Take any actual realization of the prescribed incidence, translate its own uniform-volume centroid to zero, and put G=X X^T. Choose the common sign and scale of its actual determinant family so that all w_t>0 and N=1. The signed simplex volume and first-moment identities prove(a); facet planarity proves the zeros in(b); the actual apex fan and its centroid prove(c). Every A in U is a nondegenerate actual tetrahedron, hence K is positive definite. Each true supporting plane has positive offset from the origin and can be uniquely normalized to q_f dot x=1. The invertible anchor difference matrix H gives u_f=H^(-1)q_f, proving(e). All conditions follow. QED.

Degree count: v_S,D_t,N-1 are linear; Gm_S,Gb and B_vf-1 are at most quadratic; the three anchor minors have degrees1,2,3; J_fg and all its differences have degree at most3. Theorem3 is therefore a finite real polynomial realization model of maximal degree3. It is not an executed quantifier-elimination or impossibility certificate.

For n=10,f=9 there are55 G variables,210 determinant variables and27 pole-coordinate variables, total292. All252 five-sets may be used without ambiguity. Alternatively the126 five-set boundaries containing a fixed vertex span all five-set boundary rows, so they suffice for both volume and first moments: the operations r -> sum r_t D_t and r -> sum r_t D_t chi_t are linear in the row r. The spanning identity follows by coning every simplex cycle to that vertex, or by direct boundary cancellation. With this126-row version there are126 volume equations,1260 scalar entries of Gm=0,10 centering equations,1 normalization and34 incidence equations, total1431 before adding the cofacial-flat zeros. All nonincidence inequalities, positive-cell inequalities and anchor inequalities must also be retained. A complete physical input has34 vertex-facet flags because its polygonal boundary has two flags per true edge.

### 4a. Mass signs and cofacial-flat equations are redundant in the full support model
**Corollary 4.** In Theorem3 delete ALL conditions(b), while retaining(a),(c),(d),(e), the full D family and the same reference fan definition. The physical equivalence is unchanged. No explicit nonzero-determinant inequality is required either.

**Proof.** N=1 makes D nonzero. Choose any four-set A' with D_(A')!=0; it need not be the predetermined anchor A in(d). Since all five-set moment equations are imposed, the rank proof of Theorem1 applies using A' and the same b, whose coordinate sum is4. This gives rank G<=3 without any determinant sign premise. The positive anchor K from(d), even though based on A rather than A', then gives PSD and rank3 by the independent positivity part of Theorem1. Its coordinate factor has an affinely independent predetermined anchor A. The exterior-algebra proof now recovers ALL determinants up to one common nonzero scalar. The supporting-plane proof in Theorem3 recovers the exact convex body and its genuine facet incidence without using any previously assumed determinant signs. All cofacial determinants are therefore zero automatically. Coherent boundary orientation gives one common sign sigma with epsilon_t times the actual determinant equal to sigma times its positive unsigned determinant on every supported cell. Thus N=c sigma times the positive total reference unsigned determinant. Since N=1, c sigma>0, proving every omitted w_t>0. The centroid argument is consequently the actual positive-volume centroid argument, not a signed-mass substitute. The converse is already included in Theorem3. QED.

Using all126 fixed-vertex cycles, this reduced n=10,f=9 body model has exactly292 real variables,1431 polynomial equalities and59 strict inequalities:56 nonincidence support inequalities and3 anchor minors. No cofacial zero equation, per-cell mass positivity inequality, large PSD constraint or rank equation is needed. The coefficients are integers and all polynomials have degree at most3. These counts describe the body-realization model before adding mechanical constraints. Removing these constraints is justified ONLY when the full determinant/first-moment extension and every genuine support incidence/nonincidence are retained; it is invalid in the earlier supported-moment SDP relaxation.

### 5. Mechanical use and its boundaries
For a true primal edge vw, the radial escape from v to w is G_vw-G_vv. For a true dual edge fg it is J_fg-J_ff. Thus chosen weak primal and polar escape trees add polynomial inequalities of degree1 and3 respectively. Such trees are NECESSARY relaxations of the target mechanics; they allow weak contacts and do not alone impose H=0. No solution of that weakened mechanical system is automatically a polyhedral Gomboc.

For completeness the direct feature tests can be expressed in the same variables. A strict unstable vertex has G_vw<G_vv for every true neighbor w. A strict stable facet has J_fg<J_ff for every g!=f, because its orthogonal projection q_f/(q_f dot q_f) must lie in the relative interior of that true facet.

If the true edge vw is incident to facets f,g, write A=G_vv-G_vw, C=G_ww-G_vw. The perpendicular foot to the edge line is in the relative interior of the segment exactly when A>0 and C>0: its segment parameter is A/(A+C), with A+C=||x_v-x_w||^2>0. The adjacent normals are independent. A supporting foot on that edge can be written alpha q_f+beta q_g, and its two plane equations give

alpha=(J_gg-J_fg)/(J_ff J_gg-J_fg^2),
beta=(J_ff-J_fg)/(J_ff J_gg-J_fg^2).

The denominator is positive. Consequently a STRICT saddle is exactly
A>0, C>0, J_gg>J_fg, J_ff>J_fg.
A relative-interior-edge equilibrium allowing the boundary of the normal cone uses >= in the last two inequalities. Its absence is the polynomial disjunction A<=0 or C<=0 or J_gg<J_fg or J_ff<J_fg. Endpoint contacts are tested at the actual vertices, not counted as extra interior-edge points.

A nondegenerate no-extra-contact (1,1,0) model can be obtained by requiring strict root tests, a strict outgoing true-edge escape at every other vertex and polar vertex, and absence of every relative-interior-edge equilibrium including normal-boundary contacts. If only the weaker counts of strict features are intended, the weak-contact strata must instead be retained and classified. The physical-realization equivalence of Theorem3 is independent of this convention; the universal lower-bound search may safely use the larger necessary weak-tree model for exclusions.

### 6. Complete exact audit and evidence limitations
The complete standard-library audit, immutable source [internal-source-reference], is centered_rank3_audit.py,8224bytes,SHA256 d2fe3ab67865e54a14d0732e86c9bf5cca4e82b7aa48e4619ccbc6702a20a480. No external files, numerical dependencies or random seed are used. All rational inputs, facet cycles and normalization choices are literal in that source.

Reconstruction: save the immutable source exactly as centered_rank3_audit.py.
Verification, assertions enabled:
python -S centered_rank3_audit.py
python -S centered_rank3_audit.py --verify

Both commands were executed with CPython3.13.5. Reproduced centered_rank3_audit.json:731bytes,SHA256 620524150280dda101893acd0a22314add35ec9f1d9e38521fc2f71f0a0b87a4.
Expected marker:
CENTERED_CIRCUIT_RANK3_EXACT_AUDIT_PASS 8 70 56 3 5 504 5 731 620524150280dda101893acd0a22314add35ec9f1d9e38521fc2f71f0a0b87a4

The positive physical control is the actual own-centered cube with8 true vertices,12 true edges and6 intact quadrilateral facets. It checks all70 determinants,56 five-set volume/first-moment identities, the five-dimensional exact kernel frame, anchor leading minors4,16,64,504 second-moment entries, exact same-origin pole coordinates, and all genuine feature tests, yielding(S,U,H)=(6,8,12). It is deliberately NOT a target construction.

Five exact negative controls show the separate hypotheses cannot simply be dropped: augmenting cube coordinates by a constant gives rank4 with all moment identities but no valid centering vector; a one-coordinate projection gives rank1 with all equalities but no positive anchor; changing the coordinate quadratic form to signature(2,1) gives an indefinite rank3 matrix with all equalities; centered five points in R^4 satisfy the volume identities after projection but fail the first moments; altering a nonanchor determinant of six centered moment-curve points preserves the anchor circuits but violates the full identities. These controls delimit the model, not the unknown minimum.

The archived predecessor [internal-source-reference] described a related rank3 physicality model while assuming rank3/PSD. It is used only as a historical lead: its lost local proof/source is not a dependency of the proofs above. The new rank and positivity implication is proved here from scratch. No historical-priority, contest-eligibility or external-refereeing claim is made.

### 7. Reproducible complete cubic systems, not solved feasibility instances
The complete generator and exact replay is immutable material [internal-source-reference], saved as cubic_realization.py:9961bytes,SHA256 5fa5ba4f10c4292369bff1e9fd8fa1d8c50c817dda4ef007f27857119cfeb01b. Its exact dependencies are flip_moments.py from [internal-source-reference] (13811bytes,SHA256 7542ef43f2e0e5b4759f076086c8de3539da8ef5051c80dae2a71e778a21faa7), native55.txt from [internal-source-reference] (2630bytes,SHA256 58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e), and affine_moments.py from [internal-source-reference] (5980bytes,SHA256 fa8371daf690ac9ff0a9a61b3ad8e8ca2dc6652b2a0f76cc70826163fff01805). Those source files are complete immutable units, not assumptions that an old sandbox survives.

Reconstruct these four exact files in one directory. Run python -S cubic_realization.py verify. This standard-library command constructs all55 base systems and verifies their exact dimension/degree counts, substitutes an actual rational own-centered cube into every equation and strict inequality of its separate physical system, builds the native43/root4 necessary weak-tree system, and checks all three reproduced file hashes. The cube test is independent of the general proof; no native feasibility is decided by this command.

Expected outputs:
- cubic_realization_audit.json:610bytes,SHA256 a66bf39dbf8a2024c3944e088b28a23b45a972c939329259997021bb8f5ff1f6.
- cubic_realization_census.json:7563bytes,SHA256 8f4f74a474f9d7301cd7461d2cb063fbc40aa28025000ee95b890c4002057d04.
- cubic_realization_43_4.json:151770bytes,SHA256 bc5203021cf50d362e639e20f587ce2c9e0a0894df05df0d36a8bd1a10d73132.

Observed final markers:
CUBIC_CENTERED_REALIZATION_EXACT_AUDIT_PASS 610 a66bf39dbf8a2024c3944e088b28a23b45a972c939329259997021bb8f5ff1f6
CUBIC_CENTERED_REALIZATION_NATIVE55_CENSUS_PASS 55 292 1431 59 3 7563 8f4f74a474f9d7301cd7461d2cb063fbc40aa28025000ee95b890c4002057d04
CUBIC_CENTERED_REALIZATION_FROZEN_REPLAY_PASS 3

Individual systems are reconstructed by python -S cubic_realization.py case INDEX, or case INDEX ROOT for an optional internal primal-path root. The latter adds exactly17 nonnegative polynomials:9 true primal path arrows and8 chosen polar-tree arrows. It deliberately does NOT assert that the chosen polar tree is the literal FULL nonnegative pole-arrow graph, does NOT add H=0, and does NOT claim a new exclusion. The whole55 census includes already-excluded rows; it is not a claim that55 rows remain unresolved. All generated coordinates/constraints retain the recorded path-position-to-native-vertex map.
