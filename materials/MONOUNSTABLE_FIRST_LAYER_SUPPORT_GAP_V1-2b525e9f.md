# material-2b525e9ff76a

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# MONOUNSTABLE_FIRST_LAYER_SUPPORT_GAP_V1

## Result, status and scope

Coordinator analytic theorem, with exact finite arithmetic and two actual-body moment controls. The global lower bound and attaining construction remain separate and unchanged: 34 <= C_min <= 622. This is not an exclusion of all E17 bodies, not a new own110 attainer, and not a numerical improvement of the universal 83/10 orthogonal factor.

Let P be a full-dimensional uniformly filled convex three-polytope with exactly ten true vertices and at most nine true facets. Let g and Sigma be its actual volume centroid and covariance. Suppose some nonzero positive-semidefinite quadratic metric admits a rooted weak-arrow tree on the ten true vertices, where i->j means

    (z_i-g)^T M (z_j-z_i) >= 0.

The tree can be in the complete vertex graph; no claim that a singular metric defines ordinary physical equilibria is needed. In particular this hypothesis holds whenever an SPD metric gives exactly one strict unstable vertex, even if other physical weak equilibria occur.

For every nonzero linear functional u, put

    h = max_P u.(x-g),       b = -min_P u.(x-g),
    epsilon_10,9 = 2^(-(2^124+19)).

Then the following uniform, affine-invariant, mechanically conditioned strict inequality holds:

    3h^2 - 2hb + 3b^2 < (40-epsilon_10,9) u^T Sigma u.       (1)

No S=1 hypothesis, inverse metric, lower eigenvalue floor, proper110 density theorem, or absence of additional weak contacts is used. The metric may approach a nonzero singular PSD boundary in the proof. In particular (1) applies to every hypothetical own110 V10/E17/F9 body. The constant is explicit but far too small to assert a useful numerical-scale improvement without additional analysis.

## Inputs actually read and their exact identities

A. The accepted nonzero-PSD nine-vertex refinement obstruction is [internal-source-reference], NINE_VERTEX_NONZERO_PSD_REFINEMENT_COLLAR_V1, 5230 bytes, SHA256 3052074db1f19530ac423145576607e4c86366b7e45a96cf9f17f880f0aee65b. It excludes a rooted complete weak-arrow tree on any contained labelled refinement of an actual uniform hull with at most nine true vertices, including coincident and nonextreme labels. This is stronger than an SPD-only bound. It is used as an accepted internal theorem, not independently replayed here.

B. The exact supporting-cycle centroid lemma and its effective-algebraic setting were read in [internal-source-reference], TEN_VERTEX_EFFECTIVE_DELETION_GAP_AND_CLOSED_CENTROID_CYCLES_V1.md, 12859 bytes, SHA256 c891d9f5064e9d1d2a244f62481ec9814edb08a5f8248117f64c9fa1c30dc890. The faithful joint 23-variable atlas and realization regularity were read in [internal-source-reference], 19651 bytes, SHA256 dcf2cf5c0aa9fdcc106b5375502e4fe198b43833ae0b70405698f082e6bf770a. The present proof deliberately removes the polar tree and replaces its positive metric floor by PSD. It does not claim the resulting larger closed family is exactly joint S1/U1. That stronger faithfulness is unnecessary for (1).

C. The actual-volume support inequality

    40 u^T Sigma u >= 3h^2-2hb+3b^2

and its pyramid/double-pyramid equality classification were read in the archived coordinator analytic material [internal-source-reference], 67222 bytes, SHA256 7f4026760df5ed056aa41521007582426c7603e928f0033502e328d11a0c9430. Its complete argument uses positive tent mixtures of the concave square-root section density. Equality polytopes satisfy E >= 2V-2. The independently accepted full lower convex-order theorem is also in completely read minimum-0264, SHA256 bfcc1a56683308cd9ba36d337656a9bbebb9065375f6d531d489c9f28c03c4b5. The new step here is a uniform effective gap under the actual weak-tree condition, not a new proof of those support/equality results.

D. External primary input: Gabriela Jeronimo, Daniel Perrucci and Elias Tsigaridas, On the minimum of a polynomial function on a basic closed semialgebraic set and applications, arXiv:1112.0544, Theorem 1, equation (1), page 2. The primary PDF at https://arxiv.org/pdf/1112.0544 was read, including the rendered theorem page. For a compact connected component of an integer basic-closed set in n variables with even degree bound d, coefficient height H and m defining polynomials, a nonzero minimum of an integer polynomial with those bounds has absolute value at least

    (2^(4-n/2) Htilde d^n)^(-n 2^n d^n),
    Htilde=max(H,2n+2m).

No constraint regularity assumption is inserted. This published theorem, not the arithmetic control below, supplies the effective separation.

## 1. A compact primal-only closed chart

Fix an oriented labelled polyhedral map with V=10 and F<=9, an ordered maximum-volume vertex tetrahedron and a rooted tree on the ten labels. There are only finitely many such discrete choices. It is harmless to allow all complete labelled trees; actual U1 examples provide genuine-edge trees.

Normalize the tetrahedron affinely to y0=0,y1=e1,y2=e2,y3=e3. The other six vertices give eighteen variables. Vertex replacement in a maximum tetrahedron puts every raw coordinate in [-1,1]. Require all 210 four-vertex determinants to have absolute value at most one. There are sixteen oriented triangles in a first-vertex fan of all faces, since sum(k_F-2)=2E-2F=2V-4=16. Their formal boundary is zero.

Use five variables for a symmetric trace-one M, with m22=1-m00-m11, and impose all seven principal minors of M nonnegative. Thus M is nonzero PSD; no positive smallest-eigenvalue constraint is imposed.

For each face use its first three vertices to define its normal n_F and impose coplanarity of its other declared vertices. For every listed oriented triangle (a,b,c) and every label l impose

    det(y_b-y_a,y_c-y_a,y_l-y_a) <= 0.

Define

    D = sum det(y_a,y_b,y_c),
    J = sum det(y_a,y_b,y_c)(y_a+y_b+y_c),

and require D>=1. For every arrow i->j of the chosen nine-arrow tree impose

    (4D y_i-J)^T M(y_j-y_i) >= 0.                          (2)

This gives a compact basic-closed set: raw coordinates lie in the cube and PSD trace-one matrices are bounded. The fixed standard tetrahedron protects full dimension.

The outward-supporting formal triangle two-cycle is a positive integer multiple c of the true hull boundary. To see this, subdivide its triangles on the actual boundary; nonnegative covering multiplicities agree across every small edge because the formal boundary is zero, and the boundary sphere is connected. D>0 makes c positive. Therefore g=J/(4D) is the ACTUAL uniform centroid, even before excluding collapsed labels. The same cancellation applies to all volume moments.

If any label were not a distinct true vertex, the hull would have at most nine true vertices. Its ten labels, the actual centroid, nonzero PSD M and (2) would contradict input A. Thus all ten labels are distinct true vertices at every closed feasible point.

No three distinct true vertices are collinear. Consequently each selected face normal is nonzero, its supporting triangle really belongs to a hull facet, and coplanarity places every triangle of the declared face on that same true facet. Every actual facet is covered by the boundary cycle. Hence the hull has at most the number of declared faces, at most nine. Declared faces may still merge; this proof does not need to exclude that possibility. Euler gives

    E_actual = V_actual+F_actual-2 <= 17.

The accepted support inequality is therefore STRICT in every direction throughout the closed chart: its equality classification would instead require E_actual>=2V_actual-2=18.

Conversely, every actual body in the statement has one of these chart representations after affine transport and trace normalization of its nonzero PSD metric. For SPD U1, each nonroot vertex has a genuine nonnegative outgoing derivative; squared norm strictly increases along such an edge, so these choices form a rooted tree. Thus the closed chart contains every claimed physical example, without needing a polar argument or regularization.

## 2. Exact integer support-defect polynomial

Add three variables u with u.u=1. Fix a maximum support label i and a minimum support label j by the twenty closed inequalities

    u.(y_i-y_l)>=0,       u.(y_l-y_j)>=0       for all l.

Support ties are allowed and covered by several finite choices. The variable count is n=26.

For a listed triangle write d=det(a,b,c), s=a+b+c and define the symmetric integer polynomial matrix

    L = sum d [s s^T + a a^T + b b^T + c c^T].

Signed tetrahedral integration, valid even if the raw origin is on or outside a particular integration simplex, gives

    E[YY^T] = L/(20D),
    Sigma = L/(20D) - J J^T/(16D^2).

The positive boundary-cover multiplicity cancels. Put

    alpha = 4D u.y_i-u.J = 4D h,
    beta  = u.J-4D u.y_j = 4D b,
    Q = 32D u^T L u - 40(u.J)^2 - 3alpha^2 + 2alpha beta - 3beta^2.

Then the exact identity is

    Q = 16D^2 [40 u^T Sigma u - 3h^2+2hb-3b^2].          (3)

Section 1 proves Q>0 at every feasible point of every such compact chart, including all singular-metric and mechanical-zero boundaries. This positivity does not come from weakening an arbitrary centroid encoding: the supporting cycle and input A prevent precisely the fake collapsed-body components that would invalidate the argument.

## 3. Uniform degree, height and constraint bounds

Coordinate polynomials have coefficient l1 norm at most one. The moment bounds are

    ||D||_1<=96,       ||J_r||_1<=288,       ||L_rs||_1<=1152,
    ||u^T L u||_1<=10368,       ||u.J||_1<=864,
    ||alpha||_1,||beta||_1<=2016.

Thus

    ||Q||_1 <=32*96*10368+40*864^2+8*2016^2
             =94224384 < 2^27.

Its degree is at most ten: D has degree three, J degree four and L degree five, while u is variable. The degree of (2) is at most six, and its coefficient l1 norm is at most

    9*(4*96+288)*3*2 =36288.

Trace elimination makes each M entry have l1 norm at most three; its determinant has norm at most 6*3^3. Supports, face planarity, unit-u and extremal-support rows have smaller degree and height. Therefore d=10 and H=2^27 simultaneously bound the objective and all constraints.

A conservative defining-polynomial count is

    36 cube +420 tetrahedron +160 triangle support +16 planarity
    +1 D +7 PSD +9 tree +1 sphere +20 support selection =670<700.

The 16 planarity count is a harmless common upper bound over all F<=9 maps; for exact E17 it is seven. Hence m<=700 and Htilde=H in input D.

Since 10^3<2^10,

    log2(2^(4-26/2) 2^27 10^26)
      <18+260/3 =314/3 <105.

The exponent in the effective minimum bound is 26*20^26. Exact integer arithmetic gives

    105*26*20^26
      =18320719872000000000000000000000000000 <2^124.

Every nonempty connected component therefore has

    min Q > 2^(-2^124).                                  (4)

The common degree/height bounds apply to every finite map, support-label and tree choice, so no count of charts or components weakens (4). Empty charts cause no difficulty and no existence of a U1 body is inferred.

## 4. Coordinate-free relative gap

Throughout the cube chart, D<=96 follows directly from its coefficient l1 bound. For unit u, actual variance is at most E[(u.Y)^2]<=E|Y|^2<=3. Consequently

    16D^2 u^T Sigma u <=16*96^2*3=442368<2^19.

Divide (3) and (4) by this positive denominator. This proves (1) with epsilon_10,9=2^(-(2^124+19)). Both its support expression and variance scale quadratically in u, and both are transported by the same affine map. Thus removing the unit-direction and maximum-tetrahedron gauge returns exactly the claimed affine-invariant statement for every nonzero original linear functional.

An immediate weaker consequence is

    h b < (10-epsilon_10,9/4) u^T Sigma u,

because 3h^2-2hb+3b^2=4hb+3(h-b)^2. Neither inequality is an existence or nonexistence proof for the whole first layer.

## 5. What changes, and what does not

The older strictness statement for each V10/E17 body was not a uniform unconditional gap: the literal archived P_epsilon family has support defect asymptotic to (17/6)epsilon^4. There is no contradiction. The present theorem additionally requires an actual rooted weak tree under one nonzero PSD metric. That condition blocks vertex-loss degeneration through the accepted nine-vertex refinement theorem. In particular an equality-approaching E17 sequence cannot keep the normalized relative defect arbitrarily small while retaining such a tree.

The positive gap was initially investigated only for the already compact joint S1/U1 atlas. The proof above is stronger: the stable-root requirement and positive metric floor are unnecessary. This is a new connection between actual volume support equality, true feature count and the nonzero-PSD nine-vertex obstruction. It is not a rediscovery of the earlier Hausdorff/incidence compactness theorem, which remains preserved independently.

Do NOT apply this conditioned constant to every projectively refilled body used by the universal 83/10 proof: an actual refill need not preserve U1 or a rooted weak tree. Do NOT declare a numerical improvement of 83/10 from the extremely small gap alone. The proper weak-free class, nonempty first-layer cells and global minimum remain unresolved.

## 6. Exact finite-algebra recovery

Complete standalone source is [internal-source-reference]. Save its exact UTF-8 content as support_gap_arithmetic.py:4369 bytes, SHA256 0295a350373473ce2dc4d28179853c5498d33fed548b253c448f656784517117. It has no input files, random seed or optional numerical parameter and uses only Python standard library. Observed CPython3.13.5 run, assertions enabled:

    python -B -S support_gap_arithmetic.py > support_gap_report.txt

Output support_gap_report.json:994 bytes, SHA256 e52e86030bda4fd4352ce218a726b669031a61a0ba6e5432d45b0e5f947a047f.
Output support_gap_report.txt:266 bytes, SHA256 b4c07c14a538638dbf1b702021b1bf9af17f42965282e45ae1b2fbd38d847db9.
Final marker: MONOUNSTABLE_FIRST_LAYER_SUPPORT_GAP_FINITE_ALGEBRA_PASS.

The script checks the exact exponent and coefficient arithmetic, signed boundary second moments and identity (3) on a standard tetrahedron and cube. The tetrahedron has Q=0, variance3/80 and four strict unstable vertices in metric I, so it is an equality control OUTSIDE the theorem hypothesis. The unit cube has Q=1344, defect7/3 and U8. Neither is an own110 attainer. No global 26-variable quantifier-elimination, all-chart numerical solve, or independent replay of the accepted nine-vertex/equality theorems is claimed.
