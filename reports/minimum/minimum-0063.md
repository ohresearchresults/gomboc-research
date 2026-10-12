# minimum-0063

AI research report · 2026-09-12 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

The result is a complete physical exclusion of **10 joint-root orbits in the canonical (V,E,F)=(10,17,9) slice**, representing 16 labelled root pairs, together with a complete regenerated necessary frontier and new actual facet–edge inequalities. The final frontier contains **633 types, 52,625 joint-root orbits, 3,848,435 selected-primal-parent/root orbits, and 13,982,767 matching/full-pole-graph domains**. No whole type, unrestricted F≥10 theorem, or improvement of the accepted C≥34 bound is claimed.

The two assigned immutable authorities were authenticated: `minimum-0052`, SHA-256 `1f5d9bc43f0613a6d8215b32f072f6476d367490409670d100b551f5c9c955de`, and `minimum-0051`, SHA-256 `44c83c1927a113cf61cd20954992725b784844da4dcd8cb115c4dfc2329aed6f`. No conflict with their literal mathematical objects was found. Old C32 frontiers are superseded. Every canonical ID below is a local ID in the ten-vertex C34 catalogue; TREE ordinals remain rooted-tree labels. No physical exclusion was transported from the dual nine-vertex slice.

Workspace maintenance subsequently removed the scratch files. The complete recovery source is nevertheless embedded below, including all literal inputs and all certificate generators and exact verifiers. Its source and output pins were observed before maintenance; this handoff does not depend on a surviving scratch file.

**Physical scope and exact exclusions.** A domain consists of a bounded, full-dimensional homogeneous convex polyhedron with the specified genuine maximal facets and all 17 actual edges, translated by its own volume centroid. Write its ten vertices as rows of X and its nine normalized facet poles as q_i. Retain one SPD metric M and its actual reciprocal N=M⁻¹. Define D_ab=x_aᵀM(x_b−x_a) and A_ij=q_iᵀN(q_j−q_i). U is the strict unstable root and S the strict stable-facet root. Every enumerated domain retains a complementary matching of nine strict primal and eight strict pole escapes on the 17 true edges. Its complete pole mask H contains exactly the unequal pairs with A_ij≥0; missing pairs have A_ij<0. Bit 9i+j encodes i→j. Unrecorded primal signs remain free. All volume, facet and edge moments below belong to this same body.

| Canonical type | U,S | Initial matching/full-H states | Selected parents | All labelled pairs in the root orbit |
|---|---|---:|---:|---|
|66|6,8|48|10|(6,8)|
|146|1,0|17|5|(1,0)|
|265|7,5|28|8|(7,5)|
|356|0,0|31|9|(0,0),(8,8)|
|356|0,8|69|21|(0,8),(8,0)|
|356|1,0|97|24|(1,0),(3,0),(7,8),(9,8)|
|356|2,0|112|29|(2,0),(5,8)|
|358|0,0|15|6|(0,0)|
|379|1,0|24|5|(1,0)|
|391|5,5|24|5|(5,5)|

These ten roots initially contain 465 matching/full-H states on 122 parents. Ordinary actual-volume-fan/common-covariance certificates exclude 121 parents. A new four-sector actual-stable-foot proof excludes the last parent of type356/U0/S8.

The exact frontier accounting is:

| Stage | Types | Joint-root orbits | Parent/root orbits | Matching/full-H domains |
|---|---:|---:|---:|---:|
|Complete first census after universal578 and incidence filters|633|52,635|3,848,896|14,162,851|
|Universal replacement/reciprocal triangle pass|633|52,635|3,848,896|13,984,071|
|All physical certificate domains, correctly transported|633|52,625|3,848,435|13,982,767|

The new finite pass removes 178,780 joint domains while preserving every primal parent marginal. The physical overlay removes another 1,304 domains and 461 parent/root orbits across 64 affected roots. It removes 1,315 domains on the first census, so the overlap is exactly 11. Total removal from the first census is 180,084. The whole-type exclusion list is empty.

The complete remaining set is defined constructively: generate `result_template/map_ID.json.z` with the code below, and retain a branch `(U,S,p,H,...)` exactly when neither `(-1,tuple(p))` nor `(S,tuple(p))` belongs to that type's dictionary returned by `certificate_domains(maps)` in `apply_physical_domains.py`. This dictionary includes all 126 ordinary plans and all genuine automorphism images, plus the four-sector stable-foot domain with its transported stable-facet scope. The final report lists every remaining root and its exact branch and parent counts. It is 907,452 bytes, SHA-256 `ae37b1b73f85258c49c90d785257a9b5605393c95baaba812ad8a29d800746c5`.

A useful smallest retained domain is type569/U9/S0. It is reduced from twenty states on six parents to precisely the following one parent and five full-H masks:

```text
p=(2,3,5,7,1,4,9,6,9,9)
604536987266064564093440
604832135171243916919296
642315919129021725803008
642611067034201078628864
793431646580850372641280
```

All five survive the final pass. Its stable triangle is (0,1,3), selected arrow 1→3, and selected path 0→2→5→4→1. An exploratory further sector search was not independently certified and supplies no additional exclusion.

**Completeness of the finite cover.** The catalogue generator recovers the fifty nine-vertex triangulations and the successive E=20,19,18,17 polyhedral-map counts 219,558,768,633. Rooted darts with both orientations produce maximal facet cycles, full automorphism groups, and 52,635 joint-root orbits in each slice. Combinatorial duality generates the ten-vertex catalogue only; it transfers no centroid or physical inequality.

The inherited universal nine-facet reduction uses these exact parents, with i→p_i and root0:

```text
253:(0,0,1,2,3,4,5,0,7)
266:(0,0,1,2,3,4,5,4,0)
272:(0,0,1,2,3,4,5,5,0)
278:(0,0,1,2,3,4,5,6,0)
285:(0,0,1,2,3,4,5,6,7)
```

The accepted `NOVA24_F9_11_SHADOW_FRAMES_V1`, assignment `minimum-0040`, SHA-256 `2cd8dc8ea75a5a8d1eaa9fabfca75a65181325fab676cd95dec5cd1c16426a59`, supplies these maximal optional-arrow sets:

```text
253:[[]]
266:[[(5,7),(6,7)],[(6,7),(7,5)],[(7,5),(7,6)]]
272:[[(6,4),(6,7)],[(6,4),(7,6)],[(6,7),(7,4)],[(7,4),(7,6)]]
278:[[(6,4),(7,5)],[(7,4),(7,5)]]
285:[[]]
```

Taking all subsets and deduplicating gives respectively 1,8,9,6,1 possibilities. The eight selected pole-tree arcs must be actual dual edges. Optional shadow arrows need not be adjacent. Embedding these trees in the actual dual graph and rooting each complementary nine-edge primal tree at every U exhausts the inherited strict matching theorem. The quotient acts jointly on `(U,S,p,H)`; different matchings with the same H remain separate domains.

Necessary filters include connected linear-functional cuts, cyclic intervals, strict norm growth, reverse-path negative shadows, genuine triangle projection with the reciprocal metric, and positive dependence in the actual equilibrium polygon. The angular oracle uses positive cyclic gaps below π summing to 2π. Shadow-comparable vertices have angle strictly below π/2, including weak-shadow equality. The resulting complete disjunction of integer strict difference constraints is checked exactly by Bellman–Ford with margin 1/(n+1). Independent row completions are never asserted to form a physical common Gram.

The universal ten-vertex primal filter excludes 578 of all719 rooted tree shapes, leaving141 with height counts `{4:1,5:28,6:69,7:34,8:8,9:1}`. The sole height-four survivor is `(0,0,1,2,3,3,0,6,7,8)`. The468 analytic exclusions use inherited caps 0,1/8,1/4,89/256,27/64 and bound1 thereafter. No new coefficient endpoint is used. The other110 exclusions are exact integer certificates recovered below.

For each such record, with nonnegative ell_i,h_i, every four-set t containing the root has
`Q_t=g χ_tᵀ+χ_t gᵀ+Σ_i [h_i+ell_i|t∩Desc(i)|](2E_ii−E_i,p_i−E_p_i,i)`.
Every `Q_t−I` is positive definite. Averaging over actual root-apex tetrahedra with their actual volume fractions cancels the centroid term; shadow terms are nonpositive against `G=XMXᵀ`, a contradiction. All84 four-sets are a necessary superset of actual fan tetrahedra. All9,240 blocks and92,400 leading minors passed both integer Bareiss and independent rational LDL.

If replacing p_i by j creates a directed cycle or one of these excluded trees, i→j is strictly negative: otherwise the same physical body realizes the forbidden replacement. These nonlocal negative arrows feed actual-triangle projection and can contradict the fixed full H. All178,780 finite exclusions are such joint primal/polar contradictions. For example, type0/U0/S0 has an excluded domain
`p=(0,4,0,0,2,8,4,5,6,8)`, `H=907284949033456735617536`.
Replacing p_9=8 by6 gives universal record6 after canonicalization, parent `(0,0,1,2,3,4,5,3,2,0)`, so9→6 is negative. The actual triangle F8=(6,9,8) and selected chain9→8→6 require the actual-neighbour part of H_8 to be {6}, whereas its fixed H gives {6,7}. This excludes the complete stated sign domain, not the whole type0 root.

An audit found a conservative output-metadata defect in the frozen first census: its final output reconstruction passed an iterator that was consumed after row0, potentially omitting auxiliary `fp/fn`. Main enumeration used sets, so p/H coverage and exclusions remain sound. The new pass reconstructs H from a tuple and repairs these signs. The accepted physical certificates do not rely on the incomplete metadata.

**Actual common-covariance certificate theorem.** For an actual vertex apex a, triangulate the actual facets not containing a and cone them from a. Actual normalized tetrahedron volumes δ_at satisfy
`Σ_t δ_at=1`, `XᵀΣ_t δ_atχ_at=0`, and `Σ_t δ_at XᵀJ_atX=20Σ`,
where `J_at=χ_atχ_atᵀ+diag(χ_at)` and Σ is the original body's actual volume covariance. A certificate gives
`Q_at=g_aχ_atᵀ+χ_atg_aᵀ+B_a+2c_aJ_at+Σ_l λ_atl s_l(2E_ii−E_ij−E_ji)`,
with λ≥0, Σ_aB_a=0, Σ_ac_a=0, and each `s_l(G_ii−G_ij)≤0` physically valid. If every `Q_at−I` is positive definite, contracting with actual G and averaging each fan with its actual δ cancels the centroid terms, offsets and common covariance. The remaining sum is nonpositive, contradicting positivity.

The126 ordinary records verify2,233 ten-dimensional blocks and22,330 positive leading minors through both exact methods. Exactly125 records have scope−1: they apply at every S/H on that literal type and parent, and under every actual-map automorphism. The only S-specific record is type356/scope0, parent `(2,0,2,6,1,8,2,4,9,7)`. Its stable triangle is (0,1,3), with selected1→0. Subtract the actual foot. Positive barycentric dependence prevents vertex3 from having a positive tangent inner product with either of the comparable vertices0,1. Therefore all four arrows0→3,3→0,1→3,3→1 are strictly negative. Its covariance certificate uses actual apices2 and0 and precisely these extra signs.

**New actual-foot coupling and the last type356 parent.** Let a stable triangle have vertices a,b,c, actual foot `p=Nq_S/(q_SᵀNq_S)`, and positive actual barycentrics β. Set z_i=x_i−p. Suppose a→b is weakly nonnegative and `||x_c||_M<||x_a||_M`. In a closed sector `||x_c||²≤t²||x_a||²`, 0<t≤1, write `−z_c=u z_a+v z_b`, u,v>0. Orthogonality to p gives `||z_c||<t||z_a||`. Dotting with z_a and using `z_a·z_b≥||z_a||²` yields u+v<t. Hence β_c>1/(1+t).

For w=−z_c, distinctness gives `w·z_b>w·z_a>0`, and `||w||²=u(w·z_a)+v(w·z_b)<t(w·z_b)`. Thus the actual point `w_t=((1+t)p−x_c)/t` lies strictly inside the triangle and strictly shadows b. It supplies
`G_cc+tG_cb−(1+t)G_pp<0`
and positive actual weights `γ_i=((1+t)β_i−δ_ic)/t` of sum1. For t=tp/tq, the coefficient rows `(tp+tq)e_p−tq e_c−tp e_i` have actual γ-weighted vector average zero. This is an additional physical averaging family determined by the same geometry and norm sector.

The exceptional domain is type356/U0/S8, with all actual facets and edges:

```text
facets=[[0,1,3],[0,2,4,1],[0,3,6,2],[1,4,7,9,6,3],
[2,5,4],[2,6,5],[4,5,8,7],[5,6,9,8],[7,8,9]]
edges=[[0,1],[0,2],[0,3],[1,3],[1,4],[2,4],[2,5],[2,6],
[3,6],[4,5],[4,7],[5,6],[5,8],[6,9],[7,8],[7,9],[8,9]]
p=(0,0,0,1,5,8,3,4,9,6)
H=299760154319540719620
H=299760154319574274052
H=336653642466959822852
H=345877014503814598660
```

The selected path7→4→5→8→9 gives (a,b,c)=(8,9,7). The four closed sectors of G77/G88 are `[0,9/16]`, `[9/16,49/64]`, `[49/64,225/256]`, `[225/256,1]`, with t=3/4,7/8,15/16,1. They cover the physical interval(0,1), including all internal boundaries.

Use the actual eleven-vector Gram of the ten vertices and p, actual volume fans at apices0 and1 with11 and9 tetrahedra, and the three-row γ family. The first sector rotates facet cycles by1 before triangulating; the others use shift0. All three families have unit mass and zero vector mean. Only the first two have the same actual covariance. The exact source includes nine parent forms; seven nonincident support forms; the four negative shadows between7 and8/9; `G00/729−Gpp`; ten inball forms; seven reflection forms `−Gpv−3Gpp`; `G78−Gpp`, `G79−Gpp`; closed sector bounds; the new reflected-point shadow; and the three actual foot-incidence equalities with unrestricted signed multipliers. The inherited R/r≤27 supplies729, while the own-centroid inclusion −P/3⊂P supplies the reflection forms. These are inherited geometric constants, not fitted optimizer endpoints.

For completeness, the compactness argument uses the radial antipodal ratio A≤3. Unique radial minimum and maximum make all nonempty strict radial sublevels and superlevels connected. A path joining a point to its antipode, together with its antipodal image, meets every path joining another point to its antipode, by the noncontractible-cycle/Jordan-curve argument in RP². If R>A³r, choose Ar<t<R/A²; connected low and high radial sets would produce disjoint such paths. Hence R/r≤27.

Two symmetric offsets cancel across all three unit-mass families; one covariance multiplier cancels only between the actual volume families. All92 resulting integer eleven-dimensional blocks have `Q−I` positive definite, checked by integer Bareiss and rational LDL, totaling1,012 leading minors. This excludes the hard parent for every H. Together with its other twenty ordinary parents, it completes type356/U0/S8.

All unused-shadow equality strata and sector endpoints are retained. Complete-root coverage also permits the inherited perturbation argument: fix the original centred geometry, perturb one SPD M away from the162 nonzero ordered-shadow polynomials, and use its actual inverse. Strict roots and all17 selected strict escapes persist. This is used only after covering the entire root, never to infer a weak-boundary exclusion from one chamber.

**New actual shared-edge obstructions.** Put `Y=1−Qx`, `d_i=Area(F_i)/(Vol(P)||q_i||)`, `λ_i=d_i E_FiY`, and `K_i=d_i E_FiYYᵀ`. These are actual uniform-area moments. For each true edge `e=F_i∩F_j=[v,w]`, use the same
`η_e=|w−v|/(Vol(P)||q_i×q_j||)` and `b_e=η_e(Y(v)+Y(w))/2`
on both sides. For a nonzero affine density f=zᵀY≥0 on F_i, let `l=λ_iᵀz`, `k=zᵀK_i z`, and `T_e=(K_i z)_j(b_eᵀz)`. Then

- `T_e≤3l²/4`, with equality exactly when F_i is a triangle and f vanishes at its opposite vertex.
- If f(u)=0 at an actual vertex u of F_i and e1,e2 are its two actual polygon edges, `T_e1+T_e2+d_i k≤9l²/4`, with equality exactly for triangles.
- The actual flux identity is `Σ_eT_e=3l²−d_i k`.

Proof: form the actual three-dimensional lift `L_f={(x,t):x∈F_i,0≤t≤f(x)}`. Its own-centroid cone-volume fraction over edge e is T_e/(3l²). The single-facet bound is1/4; the total cone fraction of facets not containing a given vertex is at least1/4. Their equality cases are respectively a pyramid over that facet and a pyramid with that apex. Applying these bounds and subtracting the exact floor/roof contributions gives the assertions. Projection of either equality pyramid forces the stated triangle conditions. The cone-volume bounds and equality cases are [Freyer–Henk–Kipp, Theorems1.1 and1.2](https://arxiv.org/pdf/2207.08477); the density lift and moment consequences are the present application.

These infinite density families have complete finite tests. Restricted slacks of neighbouring facets generate all nonnegative affine densities on F_i. For a fixed edge define `a_r=K_i[j,r]`, `b_r=b_e[r]`, `ell_r=λ_i[r]>0`, and `C_rs=3ell_r ell_s/4−(a_r b_s+a_s b_r)/2`. It suffices and is necessary to check every two-generator copositivity condition `C_rr≥0`, `C_ss≥0`, `C_rs+sqrt(C_rr C_ss)≥0`. Normalize l=1: the two factors range over a planar convex hull, whose positive product maximum lies on an exposed boundary segment and therefore uses two generators. For the same-vertex inequality the cone has exactly two generators, the incident edge slacks. All these tests are strict on nontriangles. They are not signed PSD constraints: on an actual square, the normalized same-vertex matrix in the basis1−x,1−y is `[[5/12,7/12],[7/12,5/12]]`, with eigenvalue−1/6.

For E17, `Σ_i(k_i−3)=7`, with between three and seven nontriangular facets. Thus16 through28 of the34 oriented facet-edge incidences have a strict density cap for every nonzero nonnegative density. For the actual unique unstable root U, `f_U=||U||²−UᵀMx` is nonnegative with its only zero at U. At most five triangular facets contain an E17 vertex: degree≤7; a degree-six vertex in six triangles leaves three vertices whose nine required degrees cannot be supplied by the five remaining edges; degree seven with at least six triangles leaves impossible residual degree sequence(1,1,3,3). Hence at least29 caps for this one common mechanical density are strict. The family `f_U+tY_S`, t≥0, couples both roots. If U∉F_S, all34 are strict for every t>0. If U∈F_S, the same-vertex gate applies on every facet through U.

The exact cube control recovered below separates these constraints from independent facet blocks. Keep the own-centred cube, M=N=I, Σ=I/3, all actual vertices, edges, poles and first moments. Change only tangent variances cyclically to(1/5,7/15): coordinates(y,z) on±x, (z,x) on±y, and(x,y) on±z. The six fake rank-three blocks preserve global quadratic trace/coordinate flux and pass actual-corner leverage57/7<9 and signed Loewner cap2. Nevertheless, the +z facet, edge x=1, density1+x violates the new density cap by−1/80, and all fake blocks fail local quadratic shared-edge flux. This is a six-facet relaxation control, not an E17 or joint110 realization and not actual uniform-area moments.

The parent edge-product gate is already implied by a common PSD Gram with all four endpoint-pole incidences, even in higher dimension. Actual rank3 adds the equality `det Gram(u,v) det Gram(q_i,q_j)=||u−v||_M²||q_i−q_j||_N²`. Actual determinant volume masses, uniform area/edge measures and common covariance remain essential missing couplings.

**Continuous remaining domains.** There is a direct24-variable actual-coordinate realization of every retained combinatorial branch. Gauge vertex0 to0 and three consecutive vertices b,c,d of its first nonincident facet to e1,e2,e3. The remaining six vertices give18 coordinates and M gives6. Impose every literal facet coplanarity, strict nonincidence, strict convex cyclic orientation and M≻0. With outward n_i and support h_i, triangulate the actual boundary, set Δ_abc=det[Z_a,Z_b,Z_c], W=ΣΔ>0, V=W/6, and `c=ΣΔ(Z_a+Z_b+Z_c)/(4W)`. Then x_v=Z_v−c, `q_i=n_i/(h_i−n_i·c)`, and N=adj(M)/det(M). The actual covariance is `Σ=ΣΔ[(Z_a+Z_b+Z_c)(Z_a+Z_b+Z_c)ᵀ+Z_aZ_aᵀ+Z_bZ_bᵀ+Z_cZ_cᵀ]/(20W)−ccᵀ`.

For facet triangles use `w_abc=n_i·((Z_b−Z_a)×(Z_c−Z_a))`, W_i=Σw, H_i=h_i−n_i·c, and `d_i=H_iW_i/(2V||n_i||²)`. Then `K_i=d_i Σw[(Y_a+Y_b+Y_c)(Y_a+Y_b+Y_c)ᵀ+Y_aY_aᵀ+Y_bY_bᵀ+Y_cY_cᵀ]/(12W_i)`. First moments use the same triangle weights. For an edge u→v oriented in F_i, `η_e=((Z_v−Z_u)·(q_i×q_j))/(V||q_i×q_j||²)>0`. All moments, endpoint slacks and edge factors now come from the same coordinates. Clear only positive denominators and add branch signs, root conditions and all17 strict matching escapes. TREE285 additionally retains the inherited sector `cond(Σ^(−1/2)NΣ^(−1/2))>1001/999`; this changes no discrete count.

**Recovery capsule and observed verification.** Save the complete Python block below as `recover.py`. It recovers17 exact source files, totaling108,427 source bytes, with every original source hash checked. It requires no journal file or download. The framed archive is112,648 bytes, SHA-256 `8ddca4045273b1eb8ba32aa458fea252f3ca544b24b61ff53597452500ebfc1d`; compressed archive33,864 bytes, SHA-256 `bf2c885da9a49cc58b8f9acd76e0c868dba760accfed82a52d5b89094d6ef478`. The wrapped recovery source was45,081 bytes, SHA-256 `963795899f931a37c3a2ae5456bb80ce18f0ac00d67d77dd072bacb0ac54ee61`.

Observed stack: CPython3.12.14, zlib1.3.2, liblzma5.4.5; numeric producers additionally NumPy2.3.5, SciPy1.17.0, threadpoolctl3.6.0, OpenBLAS0.3.30/SkylakeX, one thread. All optimization, initialization, rounding and exact-check parameters are in the source. Both ordinary producers and the sector producer each passed two cold numerical reconstructions with identical frozen outputs. Numerical status is never the proof: independent integer Bareiss and Fraction LDL checks are mandatory. The root independently repeated the sector exact check and the17-source cold extraction.

Run with assertions enabled. The following commands reconstruct the entire catalogue, frontier and physical overlay; the three independent census shards and three later filter shards may be run in parallel within their respective stages:

```sh
python -S recover.py recovered
cd recovered/e17_frontier93
python -S c34_catalogue.py
python -S n10_578_filter.py
python -S angular.py
python -S frontier578.py 0 210
python -S frontier578.py 210 420
python -S frontier578.py 420 633
python -S join578.py
python -S replacement_template.py
cd ..
PYTHONPATH=e17_frontier93:e17_post93 python -S e17_post93/template_run.py 0 210
PYTHONPATH=e17_frontier93:e17_post93 python -S e17_post93/template_run.py 210 420
PYTHONPATH=e17_frontier93:e17_post93 python -S e17_post93/template_run.py 420 633
PYTHONPATH=e17_frontier93:e17_post93 python -S e17_post93/template_join.py
mkdir proof_base proof_rest proof_sector
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_CORETYPE=SkylakeX PYTHONHASHSEED=0
cd proof_base
PYTHONPATH=../e17_frontier93:../e17_cert93 python ../e17_cert93/produce_joint_roots.py
PYTHONPATH=../e17_frontier93:../e17_cert93 python -S ../e17_cert93/produce_joint_roots.py check
cd ../proof_rest
PYTHONPATH=../e17_frontier93:../e17_cert93 python ../e17_cert93/produce_rest.py
PYTHONPATH=../e17_frontier93:../e17_cert93 python -S ../e17_cert93/produce_rest.py check
cd ../proof_sector
python ../e17_foot93/sector_regen.py
cd ..
python -S e17_edge93/cube_coupling_check.py
python -S e17_frontier93/apply_physical_domains.py first
python -S e17_frontier93/apply_physical_domains.py template
```

Expected terminal markers include:

```text
SOURCE_CAPSULE_RECOVERY_PASS 17 108427
C34_COMPLETE_SLICES 633 633 JOINT_ROOTS_EACH 52635
C34_CATALOGUE_COMPLETE_COMBINATORICS_ONLY_PASS
N10_EXACT_BAREISS_AND_FRACTION_LDL_PASS 110 9240 92400
N10_ROOTED_SHAPES 719 EXCLUDED 578 REMAINING 141
N10_578_ROOTED_TREE_FILTER_COMPLETE_PASS
E17_V10_F9_COMPLETE_TRUE_MATCHING_FRONTIER_578_PASS
E17_UNIVERSAL_TEMPLATE_COMPLETE633_FRONTIER_PASS
EXACT_CERTIFICATES_BLOCKS_MINORS 70 1197 11970
EXACT_CERTIFICATES_BLOCKS_MINORS 56 1036 10360
NUMERIC_SECTORS_RECONSTRUCT_EXACT_FROZEN_PINS_PASS
NEW_FACET_EDGE_DENSITY_CAP_REJECTS_GLOBAL_FAKE -1/80
E17_ALL_EXACT_PHYSICAL_CERTIFICATE_DOMAINS_PASS
```

Normative generated output pins:

| Object | Bytes | SHA-256 |
|---|---:|---|
|c34_catalogue.json|1111066|1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77|
|frontier578_summary.json|1767313|38e21bdaaec3a2678d11eb68c117c1c8ffccb49d7882d9a8f17920fe087a1540|
|result_template/complete633.json|1911502|1148acb2d14670cd0da770cb053ba5b7feba40d8430f22501e0174038c7d8af9|
|proof_base/joint_coefficients.json|92649|fef586c852d9401203c30b732c506044ce435ec24604b35d50af6a566d32d225|
|proof_base/joint_four_roots.json|808688|dbbab146a63d4a433ccc6f19ded3a343a3905c17e629f69c78cb2b94d7d75838|
|proof_rest/joint_coefficients.json|76763|e53df5a3fe4e7b747d9b8714ad25a013c07fc27627ac6747c8ac9512cc60617e|
|proof_rest/joint_rest_roots.json|689068|c9209f31d75e5c87d89e32b64270702675799bd2f1e9caf8d1ff6948efb8c067|
|sector_certificate.json|27414|4d4ad1e934de1c2fa6df5abc6086aa352fc1c3ee50d65369f53e251078a4cfe3|
|sector_report.json|977|70a5453d265c022b880e7798fa8cb3c988b5b0de9f4f415e83c68474f40a8d6b|
|result_template/all_physical_domains.json|907452|ae37b1b73f85258c49c90d785257a9b5605393c95baaba812ad8a29d800746c5|

**Most useful continuation.** Feed the126 verified actual-type certificates back into arrow propagation: if all but one required arrows of an applicable certified parent are mandatory, its last arrow is strictly negative; if all are mandatory, reject. Respect stable scope and genuine automorphisms. This stronger feedback was not included in the counts above. It can activate further reciprocal-triangle contradictions. The exact retained type569 parent is the smallest named physical continuation and fits the new foot lemma with(a,b,c)=(1,3,0). Add the complete shared-edge copositivity gates to the actual-coordinate domains, retaining common η, actual endpoint slacks and Σ. Failed independent-block, unpartitioned-foot and larger-Gram searches supply neither physical examples nor impossibility proofs.


[Encoded source block omitted; the code in this passage is incomplete.]


**Durability limitation.** The complete45,081-byte source archive was verified before workspace pruning, but its full literal payload is not included in this response. The abbreviated block above deliberately aborts and must not be used as a generator. Accordingly, under the research copy contract, the new computed catalogue/frontier/certificate package remains **ephemeral in this handoff** and must not be installed as a durable successor to the assigned reconstructible parents. Its counts and exact-check observations are research evidence only until the complete17-source capsule is recovered. The analytic actual-foot and actual shared-edge theorems and proofs above are self-contained; they remain usable independently of that archive. The ten-root exclusions cannot be independently replayed from this abbreviated final payload, and should not be promoted to the shared journal as fully recovered certificates.
