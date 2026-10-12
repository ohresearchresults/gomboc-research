# material-c891d9f5064e

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# TEN_VERTEX_EFFECTIVE_DELETION_GAP_AND_CLOSED_CENTROID_CYCLES_V1

## Status and scope

Coordinator analytic theorem, conditional on the already accepted internal nine-vertex nonzero-PSD refinement obstruction. This is not a new exclusion of all E17 bodies and does not change 34 <= C_min <= 622. The new uniform gap is explicit but extremely small. The proof is geometric plus an externally published effective real-algebraic minimum bound. The accompanying exact program checks coefficient arithmetic, a reusable polynomial compiler and two controls; it does not enumerate all shapes or replay the accepted nine-vertex theorem.

Primary internal input, read completely: [internal-source-reference], NINE_VERTEX_NONZERO_PSD_REFINEMENT_COLLAR_V1, SHA256 3052074db1f19530ac423145576607e4c86366b7e45a96cf9f17f880f0aee65b. Its accepted statement is: for any full-dimensional homogeneous convex hull with at most nine true vertices, centred at its actual uniform volume centroid, and any nonzero positive-semidefinite metric, the complete weak-arrow graph on any finite contained labelled refinement including every true vertex has no rooted spanning tree. Coincident and nonextreme labels are permitted. This is stronger than an SPD assertion and is not obtained here by a continuity shortcut.

Additional application source, read completely: [internal-source-reference], HEPTAGON_ALL_MODULI_UNIFORM_GAUGE_AND_EXPLICIT_DEGENERATION_GAPS_V1, SHA256 a78ff4287c53f66c405271a3c0f63170a77c72763d2f81dd2a9b33ec724aa6f6. Its Gamma_9,192 was positive but unevaluated. This material supplies an explicit lower bound for it, not an alias or a replacement of its normalization.

## 1. A faithful closed actual-centroid encoding

Let z_0,...,z_8 be arbitrary points of [-1,1]^3. Choose an oriented list C of at most fourteen triangles with labels in {0,...,8}. Repeated triangles are permitted. Require the formal oriented boundary of C to be zero. For each listed (a,b,c) and each label l impose

    det(z_b-z_a,z_c-z_a,z_l-z_a) <= 0.

Thus every nondegenerate listed triangle has an outward supporting orientation. Define

    D = sum_C det(z_a,z_b,z_c),
    J = sum_C det(z_a,z_b,z_c) (z_a+z_b+z_c).

Impose D >= 1/32. Then K = conv(z_0,...,z_8) is full-dimensional and

    g(K) = J/(4D)

is its actual uniform volume centroid. This remains true at coincident labels, nonextreme labels and degenerate listed triangles.

Proof. Regard the finite oriented triangle list as a geometric two-chain, subdividing along every intersection when necessary. The geometric boundary is zero because the formal boundary is zero; a degenerate triangle contributes the zero two-chain, and its geometric one-boundary is also zero. If K were contained in an affine plane, the coefficient of this compact two-cycle in the plane would be locally constant across all subdividing edges, hence globally constant and zero outside its compact support. The cycle would be zero and D would vanish. Lower dimensions are immediate. Thus D > 0 forces dimension three.

For full-dimensional K every nondegenerate listed triangle lies on a true supporting facet of K and is positively oriented there. Subdivide the whole boundary of K by their edges. Across each small interior edge, and across each true hull edge, the zero-boundary condition makes the nonnegative integer covering coefficient agree on the adjacent cells. The boundary sphere is connected, so the whole geometric chain equals c times the outward boundary of K for one integer c >= 0. D > 0 gives c >= 1. The ordinary signed tetrahedral volume and first-moment identities give

    D = 6c Vol(K),       J = 24c integral_K x dx.

The same covering integer cancels in J/(4D). It is not a free mass variable. The original list need not be an embedded sphere or a nonoverlapping triangulation for this conclusion. This is why this closed encoding does not create the earlier fake-centroid relaxation.

Conversely, every actual three-dimensional hull with at most nine true vertices has an outward triangulation of its boundary with at most 2V-4 <= 14 triangles, using true vertices only. If Vol(K) >= 1/192, its ordinary degree-one boundary has D = 6 Vol(K) >= 1/32. Therefore the family of these closed systems includes every actual nine-vertex body needed below. The systems may also include positive multiple boundary covers, but their centroids remain exact and they have at most nine true vertices.

## 2. A compact degree-six model with 46 variables

Add a tenth label z_9 contained in K, represented by nine variables alpha_i >= 0 with sum alpha_i = 1 and z_9 = sum alpha_i z_i. Use six variables for a symmetric M with all seven principal minors nonnegative and tr(M)=1. Add an epigraph variable h with 0 <= h <= 12. There are 30+9+6+1 = 46 variables.

For any fixed rooted tree T on the ten labels impose, for every one of its nine arrows i -> j,

    4D h + (4D z_i - J)^T M (z_j-z_i) >= 0.

After division by 4D this says that each actual-centred weak-arrow defect is at most h. Every centred point and every edge has Euclidean norm at most 2 sqrt(3), so h=12 is always a valid epigraph bound for trace-one PSD M. The complete constraint set is basic closed and compact: the points lie in the cube, alpha lies in a simplex, PSD trace-one matrices are bounded, and h is bounded.

At any feasible point with h=0 the actual hull K, its contained ten-label refinement and the nonzero PSD metric would violate the accepted nine-vertex obstruction. Hence h is strictly positive throughout every nonempty such compact system. No assumption about a positive smallest eigenvalue is used here.

All coefficients are integers. There are at most 219 constraints (230 is a safe common bound): 60 cube inequalities; 9 alpha inequalities, 1 alpha-sum equality and 3 containment equalities; 7 PSD inequalities and 1 trace equality; 2 h bounds; 1 D bound; at most 126 support inequalities; 9 tree inequalities. Their degrees are at most six. Uniform coefficient l1 bounds, hence coefficient-height bounds, are

    ||D||_1 <= 14*6 = 84,
    ||J_r||_1 <= 252,
    ||4D z_{i,r}-J_r||_1 <= 588,
    ||cleared tree epigraph row||_1 <= 9*2*588 + 4*84 = 10920,
    ||32D-1||_1 <= 2689.

Support determinants have l1 norm at most 48. Thus H=2^14 bounds every coefficient. These are symbolic bounds for every allowable list, not merely measurements of the two controls.

## 3. Effective minimum bound

External primary theorem used: Gabriela Jeronimo, Daniel Perrucci and Elias Tsigaridas, 'On the minimum of a polynomial function on a basic closed semialgebraic set and applications', arXiv:1112.0544, Theorem 1, displayed formula (1), page 2. The theorem and formula were read in the primary PDF, including its rendered page.

The needed form is the following. For a compact connected component of a basic closed set in n variables, defined by integer polynomials of degrees at most an even d and coefficient heights at most H, a nonzero minimum of an integer polynomial with the same degree/height bounds has absolute value at least

    (2^(4-n/2) * Htilde * d^n)^(-n*2^n*d^n),
    Htilde = max(H,2n+2m),

where m is the number of defining polynomials. This applies to h on every nonempty connected component of each model above. All components are compact; none has minimum h=0. There are only finitely many triangle lists, choices of redundant label and rooted trees. The same bound applies to all of them without a further counting factor.

For n=46, d=6, H=2^14, m<=230, Htilde=2^14. The base is 6^46/32 and the exponent is 46*12^46. Since 6^3<2^8,

    log2(6^46/32) < 353/3 < 118,
    118*46*12^46
      = 238219416850943619645168464865738088405211151285092352
      < 2^178.

Consequently, with

    b = 2^(-2^178),

for every ten-label refinement of an actual at-most-nine-vertex hull in the cube of volume at least 1/192, every trace-one PSD metric and every rooted ten-label tree,

    max(0, max_{i->j in T} -(z_i-g)^T M(z_j-z_i)) > b.

In particular the earlier Gamma_9,192 > b. This is an explicit but not useful numerical-scale separation; it is not a numerical estimate of the actual best gap.

## 4. Global ten-vertex deletion gap

Let P have ten true vertices, with actual uniform centroid g, and suppose its complete weak-arrow graph for some nonzero PSD M has a rooted tree. In particular, every actual U=1 SPD body has this property using genuine-edge arrows. Choose a maximum-volume vertex tetrahedron and apply an affine map taking its four vertices to 0,e_1,e_2,e_3. Transport M by congruence and normalize its trace to one. Every remaining barycentric coordinate has absolute value at most one, by replacing one tetrahedral vertex; hence the raw transformed vertices y_i lie in Q=[-1,1]^3 and the standard tetrahedron lies in P. In particular Vol(P)>=1/6.

For any vertex y_j let K=conv{y_i:i!=j}, choose its nearest point q in K, and put delta=|y_j-q|. Replace only y_j by q to form a ten-label refinement z of K. We have

    P subset K + [0,delta] n,
    Vol(P)-Vol(K) <= 4 sqrt(3) delta,

because the area of any orthogonal projection of the cube is at most 4 sqrt(3). If delta <= 1/84 then Vol(K)>=1/12, since 4 sqrt(3)/84 < 1/12. Decomposing the first moment into K and P\K gives

    |g(P)-g(K)| <= 144 delta.

Indeed the removed-volume fraction is at most 24 sqrt(3) delta and both relevant barycentres are in a cube of diameter 2 sqrt(3). Each centred labelled point changes by at most 145 delta. An edge changes by at most delta. Therefore, for every ordered label pair,

    |D_ij(P,M)-D_ij(K,M)|
      <= 292 sqrt(3) delta < 512 delta,

where D_ij=(y_i-g)^T M(y_j-y_i). If delta <= b/512 then delta<1/84 and every arrow of the original weak tree has defect < b on K, contradicting Section 3. Thus all ten vertices satisfy the explicit affine-normalized inequality

    dist(y_j, conv{y_i:i!=j}) > 2^(-(2^178+9)).

The same bound works for every chosen maximum-volume tetrahedron. This is a global U=1 necessary condition, not only a parallel-prismatoid statement. It does not assume S=1, F=9, or a metric condition-number bound. It uses the nine-vertex nonzero-PSD theorem precisely at the collapsed hull.

## 5. Consequence for the existing parallel-heptagon gaps

Keep exactly the normalization and parameter meanings of [internal-source-reference]. Its proof permits any xi <= min(1/960,Gamma_9,192/12969). The explicit choice

    xi = b/2^14

is valid. Accordingly every parallel-heptagon U=1 candidate in that chart has

    rho > b/2^15,
    each of the ten listed chart-wall quantities > b^2/2^29
       = 2^(-(2^179+29)).

Those ten quantities are c-b, d-a, 2(1-p-q), 2p, 2q, 1-c, 1-d, u, v, and min(a,b)(1-u/b-v/a). These bounds follow from rho>=xi/(2-xi) and each wall>=rho*xi, so the strict relaxed inequalities displayed here are safe. The previously accepted independent exclusion rho>=7 remains much stronger than the new upper estimate rho<1/xi. No positive-interior cell is thereby closed, and this parameter statement is not transferred to arbitrary nonparallel projective charts.

## 6. Exact recovery and computation boundary

Complete code is immutable material [internal-source-reference]. Copy its literal UTF-8 text to ten_vertex_gap_arithmetic.py without changing line endings. Input source: 9495 bytes, SHA256 307a74325bca0b084787c38aba83770958c7376f0691ad11016c0c408f673c4b. It is self-contained and uses only the Python standard library; no seed, external data, floating-point tolerance or optional parameter exists. The observed run used CPython 3.13.5 with assertions enabled.

Reconstruction/verification command:

    python -B -S ten_vertex_gap_arithmetic.py ten_vertex_gap_report.json

Expected terminal marker: TEN_VERTEX_EFFECTIVE_GAP_ARITHMETIC_AND_MODEL_PASS.
Expected output ten_vertex_gap_report.json: 1195 bytes, SHA256 bf5757cd472277177c01f8c44ea60ca8752f8b2baf53a3ac346f3e54b127ddd5.

The first exact control is a rational octagonal pyramid, all 219 polynomial constraints at a deliberately large defect epigraph h=12, D=28/5, actual centroid (0,0,1/4). The second is a twice-covered tetrahedral boundary: D=2 although physical 6V=1, and the formula still gives the actual centroid (1/4,1/4,1/4). It checks the intentional covering-degree cancellation. Neither is a U=1 example or an attaining construction. Observed compiled maximum degree is 6, maximum coefficient height 32 and maximum l1 norm 10164; the proved uniform bounds remain degree 6, height 16384 and l1 10920.

The exact printed integer above and these source/output pins supersede any scratchpad transcription of them. Source integrity is not an independent proof of the nine-vertex input theorem. The new analytic claims are the supporting-cycle centroid lemma, the effective gap deduction and its perturbative applications. The minimum and the first-layer feasibility question remain open in this run.
