# minimum-0045

AI research report · 2026-09-11 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

**LYNX99_LITERAL_INTERSECTION_AND_ONE_BODY_PHYSICAL_FRONTIER_V1**

The literal intersection is complete and reconstructible. G55’s frontier outside its old 17 whole exclusions intersects qvo’s literal 116-whole exclusion set in **8,382 joint-root orbits, 55,661 coupled graph orbits, and 15,357 matching branches across 180 canonical types**. A new continuous geometric theorem excludes **892 complete physical sign domains**, leaving **54,769 graph orbits**. All 8,382 joint roots, all 15,357 matching branches, and all 180 types remain.

A separate new actual-mass certificate proves, for every actual unique-U long-broom realization,

\[
\frac{\operatorname{Vol}\operatorname{conv}(x_0,x_5,x_6,x_7)}{\operatorname{Vol}P}>\frac1{140},\qquad \omega_{567}>\frac1{560}.
\]

This excludes an entire continuous mass sector, including its equality boundary. **No additional complete U root, S root, joint root, or whole type is closed.** No physical feasibility follows from graph survival. There is no C32 attainer or C≥34 theorem; the inherited bracket remains 32≤C_min≤1374.

| Register | Types outside whole exclusions | Joint-root orbits | Coupled graph orbits | Matching branches |
|---|---:|---:|---:|---:|
| Literal G55 outside old 17 | 279 | 12,954 | 87,519 | 23,640 |
| Literal G55 intersected with qvo’s whole filter | 180 | 8,382 | 55,661 | 15,357 |
| After the new physical projection exclusions | 180 | 8,382 | 54,769 | 15,357 |

The exact disjoint catalogue partition is

\[
21,682=8,232\text{ whole-type roots}+40\text{ prior partial roots}+5,028\text{ additional G55 roots outside the whole set}+8,382\text{ remaining roots}.
\]

Thus qvo’s additional whole types remove **4,572** roots, **31,858** graph orbits, and **8,283** matching branches from G55’s previously reported outside-17 frontier. The old figures 13,450 and 12,954 were different covers; their literal intersection is 8,382. Of G55’s 7,805 additional joint-root exclusions, 2,777 lie in qvo’s newly whole-excluded types and 5,028 remain relevant outside them. Of the old 55 partial-root cases, 15 are absorbed by the enlarged whole set and 40 remain.

**Authority and labels.** Both literal immutable parent payloads in the attached `research-journal(10).md` were read and authenticated. Their compact UTF-8 envelopes use `json.dumps({'version':2,'result_markdown':md},ensure_ascii=False,separators=(',',':'))`, with exactly one final LF in `md`:

| Parent | Envelope bytes | SHA-256 |
|---|---:|---|
| minimum-0042 | 62,574 | 392b3b5faac0b8f23783ae9f64223b17e8d8475022dc933d941bdb0460706793 |
| minimum-0043 | 54,473 | 486ba862561f660c9592ca19853855a9fec58d59486048e4a62d863a84bc3882 |

Their authenticated Markdown lengths are 61,527 and 53,757 bytes respectively. The recovery code extracts these exact payloads before executing recovered source. No parent/alias conflict was found. The literal canonical catalogue remains **240,929 bytes**, SHA-256 `efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d`. All vertex labels, maximal-facet labels, oriented cycles, true edges, automorphisms and induced facet automorphisms are retained. TREE ordinals and the MP9:45 parent sphere are not renamed as canonical C32 IDs. qvo’s transport is used only as its literal whole-type exclusion filter; its exhausted transport enumeration is not repeated.

The complete 116-whole filter is:

```text
0,3,4,10,12,13,15,16,17,19,21,22,23,24,26,27,29,30,31,32,33,34,35,37,39,40,
42,43,44,45,46,47,55,59,64,66,67,69,70,71,72,74,76,77,78,79,82,83,85,87,88,
89,90,91,93,98,99,100,101,102,103,105,119,120,122,124,128,138,139,140,143,144,
149,152,157,159,163,164,165,166,167,170,171,172,173,178,192,194,195,208,209,212,
217,242,243,244,245,246,247,248,250,253,254,261,262,263,264,265,268,271,272,
284,288,293,294,295.
```

Outside that filter, the five old partial-U exclusions are `49/U3,51/U3,53/U3,282/U0,290/U3`. G55’s remaining nine unconditional-U exclusions are `50/U3,108/U3,109/U3,113/U3,114/U3,137/U3,191/U3,240/U3,260/U3`. G55’s remaining complete joint-target U exclusions, **48 including those nine**, are:

```text
(2,6),(5,7),(7,8),(9,8),(14,8),(20,1),(25,0),(50,3),(62,8),(73,8),(81,1),
(97,1),(108,3),(109,3),(113,3),(114,3),(115,7),(121,0),(121,6),(127,8),
(131,3),(131,6),(137,3),(147,5),(161,3),(162,3),(174,3),(174,5),(175,3),
(177,7),(179,6),(179,7),(180,8),(191,3),(193,8),(196,7),(197,8),(199,8),
(215,8),(216,3),(229,3),(240,3),(255,8),(260,3),(266,5),(276,0),(276,1),(278,0).
```

The remaining complete target-S exclusions are `57/S0,73/S5,126/S4`. These projections overlap; they are not additive joint-root counts. None is newly proved by the present whole filter. The full 180-type complement and every exact joint-root row are generated by the capsule.

**New physical projection theorem.** Let the actual centred vertices be x_i, the actual maximal-facet poles be q_f with q_f·x≤1, and let M≻0 and N=M⁻¹ be one reciprocal physical pair. Write D_ij=x_iᵀM(x_j−x_i) and A_fg=q_fᵀN(q_g−q_f). Suppose three distinct vertices a,b,c lie in one actual maximal facet f, which may be polygonal, and

\[
D_{ba}\ge0,\qquad D_{cb}\ge0,\qquad D_{ca}<0.
\]

After the physical square-root transform, put y=x_b, u=x_a−x_b, v=x_c−x_b, A=D_ba, B=D_cb, C=−D_ca, a₀=u·u, b₀=v·v. Then u·v=−(A+B+C) and Δ=a₀b₀−(u·v)²>0. The plane foot p=y+αu+βv satisfies

\[
\alpha=\frac{b_0(B+C)+(A+B+C)B}{\Delta}>0,\qquad
\beta-1=\frac{a_0B+(A+B+C)(B+C)}{\Delta}>0.
\]

Its affine coefficients at a,b,c have signs (+,−,+). If ac is an actual boundary edge of f, the pole escape from f across ac is strictly positive. If ab or bc is an actual boundary edge, the corresponding pole escape is strictly negative. Across ac, for the actual neighbouring facet g,

\[
q_g\cdot p-1=(1-\alpha-\beta)(q_g\cdot x_b-1)>0,
\qquad A_{fg}=(q_f^TNq_f)(q_g\cdot p-1).
\]

The other two cases use positive omitted coefficients and give strict negatives. The same proof applies to the actual polar with N and its reciprocal M. It needs no polar-centroid assumption and permits either initial weak escape to vanish.

G55 applied this calculation to maximal triangular facets. The new enumeration applies it to every triple inside each actual maximal polygon and transfers a sign only across a side that is a **true polygon boundary edge**. Diagonals are never escape edges. A contradictory complete sign state is impossible for every continuous realization of its stated lattice and reciprocal metric. Exhaustion gives 450 primal-to-pole contradictions and 442 pole-to-primal contradictions, with no overlap: **892 domains across 162 types**. All matching branches and joint roots still have survivors.

A literal new contradiction is canonical type 1, original intersection-domain index 6. Its facets 0 through 8 are

```text
[[0,1,3],[0,2,4,1],[0,3,5,2],[1,4,6,3],[2,5,7,4],
 [3,6,5],[4,7,8,6],[5,6,8],[5,8,7]].
```

Its complete nonnegative primal arcs are `[(0,1),(1,3),(2,5),(3,6),(4,2),(5,8),(6,4),(7,8)]`; its complete nonnegative pole arcs are `[(0,2),(1,2),(2,5),(3,0),(3,1),(5,7),(6,4),(7,6),(8,4)]`. Every omitted unequal arrow is strictly negative. In facet 3=[1,4,6,3], take (a,b,c)=(6,3,1). The signs D_36≥0,D_13≥0,D_16<0 force A_30<0 across actual edge 31, whereas the complete pole graph contains 3→0. The stored certificate is `[3,6,3,1,3,1,0,false]`. The proposed root pair is U8/S4; other graph states at that root survive.

The complete original seven-field domain is

```text
[2361480479293705293826,76148452270249219196932,
 [1,3,5,6,2,8,4,8,8],[2,2,5,1,4,7,4,6,4],
 2361480479293705293826,76148452270249084979204,[8,4]].
```

Two further valid geometric predicates were exhausted without gain. Two nonnegative boundary-neighbour escapes at a facet vertex prohibit both corresponding corner pole escapes from being strictly negative, by the tangent-cone/plane-foot scalar-product contradiction. Also, the cofacial-chain formula forces A_fg<0 for every other maximal facet g containing the middle vertex b, including nonadjacent facets: its negative affine coefficient multiplies zero slack, while its positive coefficients multiply nonpositive slacks, at least one strictly negative. Both predicates were checked on all 54,769 survivors, with zero contradictions on either side. Their complete no-gain checkers are embedded below.

**New actual-mass theorem and certificate.** Use the actual weak primal broom T=(0,0,1,2,3,4,5,6,0), and its actual terminal maximal triangle 567. Genuinely triangulate the actual maximal facets and cone them from actual vertex x₀. The positive cells, together with zero cofacial cells, belong to one decomposition of the same body. Their actual normalized determinant masses m_t obey

\[
\sum_t m_t=1,\qquad \sum_t m_t\sum_{j\in t}x_j=0.
\]

Every cell is among the 56 four-sets t={0}∪A, with A a three-subset of {1,…,8}. The terminal cell t*={0,5,6,7} has mass m*. The certificate retains all 56 cells; no independent mass solution is substituted.

Set L=140, β=911199, and L_i=2e_ie_iᵀ−e_ie_T(i)ᵀ−e_T(i)e_iᵀ. The embedded source contains all 458 exact integers: nine γ entries, β, and 56×8 nonnegative λ entries. For every cell it constructs

\[
Q_t=L\left(\gamma\chi_t^T+\chi_t\gamma^T+\sum_{i=1}^8\lambda_{ti}L_i\right)+2\beta(L1_{t=t_*}-1)I.
\]

The exact verifier proves **Q_t−I≻0 for all 56 cells**, checking 504 positive leading minors by integer Bareiss elimination and independently by Fraction LDL. It also checks all 2,520 scalar quadratic identities using every basis and basis-pair probe.

Let G=XMXᵀ be the actual nonzero physical Gram matrix and E_i=x_iᵀM(x_T(i)−x_i)≥0. Averaging with the actual m_t cancels the γ terms by the actual first moments. Since ⟨L_i,G⟩=−2E_i,

\[
2L\beta(m_*-1/140)\operatorname{tr}G-2L\sum_i\bar\lambda_iE_i>\operatorname{tr}G,
\qquad \bar\lambda_i=\sum_t m_t\lambda_{ti}.
\]

Therefore

\[
\boxed{m_*>\frac1{140}+\frac1{255135720}+\frac{\sum_i\bar\lambda_iE_i}{911199\operatorname{tr}G}.}
\]

The componentwise minimum λ values may replace the averages for a weaker triangulation-independent bound:

```text
11490975,23405854,26877376,26911063,22919364,14398614,5980613,1643.
```

For the actual pole q_F of F=567, the same root-apex first moment gives

\[
0=q_F\cdot x_0+\sum_t m_t\sum_{j\in t\setminus\{0\}}q_F\cdot x_j\le q_F\cdot x_0+3.
\]

Thus 1−q_F·x₀≤4. Actual pyramid volumes give m*=ω_F(1−q_F·x₀), so ω_F>1/560. This is an **unconditional unique-U necessary condition**, using arbitrary SPD M and weak broom escapes. It permits zero cofacial cells and arbitrarily small other positive cells. In a joint target, the uniquely compatible matching is strict; its primal tree can be relabelled as this broom. The alternative description exchanges labels 1 and 8 and leaves the terminal tetrahedron unchanged. This preserves G55’s distinction between uniqueness of the compatible complementary matching and uniqueness of arbitrary escape trees.

The numerical locator found the literal integer certificate; proof and recovery use exact standard-library arithmetic. The locator environment was CPython 3.12.14, NumPy 2.3.5, SciPy 1.17.0, one BLAS thread, no randomness. A preliminary 7/1000 certificate was superseded by 1/140. Attempts using the forced negative shadows produced no stronger accepted certificate. Failed searches are not nonexistence evidence or bounds on the optimal mass constant. The old universal-tree numerical certificates were not rerun.

**Exact single-body remaining domain.** The supplied generator emits a nonlinear-real system for each surviving graph domain, retaining canonical labels. It uses 21 scalar variables: 15 coordinates after an affine gauge and six symmetric-metric entries. Let a,b,c be the first three vertices of canonical facet 0 and d the least vertex outside it. Fix v_a=0,v_b=e₁,v_c=e₂,v_d=−e₃. Every actual realization admits this orientation-preserving affine gauge; the transformed SPD metric is normalized by tr M=1. The five remaining facet-coplanarity equations are retained without assuming their independence on exceptional strata.

For the canonical polygon fans define δ_t=det(v_i−v_d,v_j−v_d,v_k−v_d), D=Σδ_t>0, C=Σδ_t(v_d+v_i+v_j+v_k), and

\[
X_i=4D v_i-C=4D(v_i-g),
\]

where g is the actual ordinary volume centroid. Every n_f is computed from its actual facet vertices, every support h_f=n_f·X_i is positive, and every pole is n_f/h_f. The primal shadow numerator is X_iᵀM(X_j−X_i). The pole shadow numerator is

\[
n_f^T\operatorname{adj}(M)(h_fn_g-h_gn_f),
\]

whose removed denominator det(M)h_f²h_g is positive. Strict maximal supports, exact coplanarities, strict polygon convexity, all 144 complete unequal-pair signs, and the unique sixteen strict true-edge matching escapes are imposed. Present unused shadows may vanish; omitted shadows remain strictly negative. Every actual cone determinant, facet cone mass, facet area centroid and Λ numerator is derived from these same X_i. The terminal determinant/cone bounds and minimum-multiplier energy inequality are included. No centroid, mass, pole or second metric is independent.

The system is equivalent to a physical realization in its complete sign domain, using the inherited strict-matching equivalence. No nonlinear solver result is claimed. The emitted canonical type 1, original-domain 0 system is **100,082 bytes**, SHA-256 `9b5fe891c7c0931e6f6aebe1c1fab284813bbcc12e423ce9e491e6c4045ecc13`. Two exact physical controls verify the emitted geometry, all 144 signs and actual moments after the affine gauge, with 307 assertions each. All 55,661 original matching descriptions pass reconstruction of their genuine terminal triangle. The separate exact candidate verifier reconstructs the maximal hull, true edges, actual centroid with ten apex integrations, cofacial-zero determinant ledger, reciprocal metric and all equilibrium types. Its controls retain the old negative four-minor and have (S,U,H)=(4,4,6) and (4,5,7); neither is a target.

**Complete-root boundary reduction.** For one fixed actual strict110 body, each primal primitive is a nonzero linear polynomial in symmetric M, and each pole numerator q_fᵀadj(M)(q_g−q_f) is a nonzero polynomial. The latter cannot vanish identically because inversion maps the SPD cone onto itself. The zero set of their product has empty interior. An arbitrarily small SPD perturbation avoids all 144 zero primitives while preserving the sixteen strict matching escapes and every formerly strict sign. The actual body, moments and roots are unchanged. Therefore, excluding every all-strict chamber over a **complete root or type** also excludes unused-zero targets. A weak graph may perturb to a smaller graph; failure of one graph’s strict interior does not exclude its weak boundary in isolation.

An all-strict target also has a nearby rational Euclidean realization of the same maximal lattice. Absorb M by its square root. The planar bipartite vertex/facet incidence graph is 3-degenerate. Reverse a degree-at-most-three peeling, solving each node’s incidence equations through a nonzero coordinate minor. Its at-most-three neighbour vectors are independent because they are distinct vertices of one strictly convex primal or polar facet in a plane with support one. This gives a local rational chart. Rational approximations preserve strict incidence and mechanical signs; the actual rational centroid can then be subtracted. The chart itself is older journal material. Its application here rules out an irrational-only or unused-zero-only target escaping a complete all-strict rational search, while finite failed searches remain inconclusive.

**A relaxation that cannot advance the remainder.** The bare shared Gram PSD test is vacuous after dropping rank three and actual mass/null-vector constraints. For any DAG with topological ranks r_i, set A_ii=1024^{r_i}, A_ij=A_ji=2·1024^{r_i} on an arrow i→j, and other off-diagonal entries zero. Its shadows have exactly the prescribed strict signs. Diagonal normalization gives off-diagonal row sums at most 1/2, hence A≽I/2. Construct B for the pole graph and let C be the 0–1 incidence matrix. Since ||C||₂≤9,

\[
\begin{pmatrix}32A&C\\C^T&32B\end{pmatrix}\succeq7I_{18}.
\]

It satisfies cross-incidence equalities, strict nonincidence upper bounds and both shadow blocks, but is an artificial rank-18 object with no positive centroid null vector. The exact scan covers all 55,661 pairs and 25,597 distinct individual masks; all are DAGs, and the maximum observed normalized row sum is 65/512. The complete constructive checker is embedded below.

**Recovery and observed checks.** The lossless capsule below embeds all eight complete runnable source units and every exact certificate integer. Its only external research input is the specified attached journal containing the authenticated literal parents. All later inputs are regenerated. Assertions must remain enabled. New work ran under CPython 3.12.14, standard library only; the inherited G55 sources declare 3.13.5 and reproduced their exact pins under 3.12.14.

Save the complete code as `recover_lynx99.py`, UTF-8/LF with one final LF, and run:

```sh
python -S recover_lynx99.py build '/absolute/path/research-journal(10).md'
python -S recover_lynx99.py check '/absolute/path/research-journal(10).md'
```

`build` authenticates the parents, reconstructs the catalogue and G55 frontier, applies qvo’s literal filter, generates the projection successor, and executes the mass, physical-body, affine-domain, no-gain and artificial-PSD checks. `extract` writes the eight readable sources without running them. `check` reuses the pinned inherited outputs and repeats successor checks. No scheduler is invoked, the journal is not modified, qvo transport is not repeated, and no nonlinear feasibility solver is run.

The cold execution of this complete capsule succeeded and reproduced every listed output pin. Its final marker was `LYNX99_COMPLETE_INTERSECTION_PHYSICAL_REFINEMENT_AND_RECOVERY_PASS`. Recovery source: **27,269 bytes**, SHA-256 `56b10360b46a590a0934dad7c3586b2cf8874ddce2fcbc06b25e672ce30106ca`. Decoded source package: **49,679 bytes**, SHA-256 `7ef18711c9c575f45c652f07343bafbaf995f30a0c41ac21391d2bacda5178e3`. Source manifest: **788 bytes**, SHA-256 `3dcb0def3d704baca87ee664862040dbbdc605ca297ae78dee5053c507ae599e`.

| Source | Bytes | SHA-256 |
|---|---:|---|
| intersect_frontier.py | 8020 | c5fcdf5ab6e59fbfe1185a3cfb22926c33ac8fe334e8d7a0379ecb01b2e2d942 |
| geometric_projection.py | 5784 | 8fef93cf5cdf269a6c3ae6401abda6c765974014ae8ffc2fafb23d1a5a773b45 |
| terminal_mass_exact.py | 8284 | 5582f021793b1c7d9121bbda19a6463125e6553c9e5e1c0dc0ad0b8698c3a055 |
| verify_candidate.py | 10929 | 08120488361975b8dcc789982799f82ffc5b4df4e1edba58903f9a34965e5740 |
| physical_domain.py | 10867 | f7d4426ec2ef31548d1292333f6389ca46560e1ddad3de54bade593e4c23f580 |
| relaxation_control.py | 1947 | 172e676400ddf97fa1ae502cef98f5d1096f7c0691a1833b07ccae36acf02bac |
| corner_no_gain.py | 1462 | 6097232d40b09f0effc9db76fc120f72a4762a316b8c0440a2b9092677ef7dfc |
| middle_incidence_no_gain.py | 1257 | cd28df1805eb246b6ae9bc2b90f36e36af751ce04aaac5b19aae869c50dc9924 |

| New output | Bytes | SHA-256 |
|---|---:|---|
| literal_intersection.json | 9513727 | a7cbd09b84862ee646cc9ce269c97dcd246c4624082c96f86545bae78baa54db |
| geometric_frontier.json | 11728807 | 9e01776fe87d26c08dbd52c13f3d9e316d861770f69e978b1babdbd8bf8d4a4b |
| terminal_mass_exact.json | 5494 | 599c40ce062ed7a00c8373e326cda2703f305f511504ff1dd90609be5fb02033 |
| one_body_control.json | 61676 | 84826677794ed40c22dc17525b0f0b87469c53a1a472d82bed6f9c3ce7a708d3 |
| physical_domain_check.json | 278 | a01d4e916ed53da7c13c4915b8a9954f9b7bca1e3c07e32a006ec2d0be51f01c |
| relaxation_control.json | 334 | b36b8c748af13003cf90a978fbf341dc0b85c6837256ae21d1fad3db8b4f27f7 |

In `literal_intersection.json`, each domain is `[primal_mask,pole_mask,primal_parent,pole_parent,strict_primal_mask,strict_pole_mask,joint_root_representative]`; bit `9*i+j` represents i→j. Each parent array has its root as its unique diagonal entry. In `geometric_frontier.json`, a survivor is `[original_intersection_domain_index,original_domain,new_strict_primal_mask,new_strict_pole_mask]`. A discard is `[original_index,primal_to_pole_certificates,pole_to_primal_certificates]`; each local certificate is `[facet,a,b,c,boundary_v,boundary_w,other_facet,required_positive]`. Pole-side labels use the explicitly retained dual facets and transport to the same canonical primal labels. The entire remaining joint-root array is asserted identical before and after the projection cuts.

For continuation, run `python -S physical_domain.py TYPE ORIGINAL_DOMAIN_INDEX > domain.smt2` inside the recovery directory. Only surviving geometric domains are accepted. Check an exact candidate with `python -S verify_candidate.py literal_intersection.json TYPE ORIGINAL_DOMAIN_INDEX candidate.json`; input requires nine three-entry `vertices` rows and a three-by-three symmetric `metric`, with integer or fraction-string entries. The actual centroid is computed, never supplied or fitted.

The most useful next task is a complete root-orbit proof using the uniquely owned sixteen strict escapes, the quantitative terminal-mass/energy bound, all absent-shadow strict negatives, and the shared 21-variable physical system. Canonical type 260 has 85 graph states over 19 joint roots; type 282 has 102 over 26. These are small complete covers, not feasibility evidence. The all-strict reduction applies to complete root/type proofs; individual weak graph boundaries retain the stated coverage requirement.

Supplementary complete bundle: NIMBLE_LYNX99_C32_PHYSICAL_FRONTIER_V1.zip. The inline source below is sufficient with the specified literal parents; downloading the bundle is optional.

```python
"""LYNX99_LITERAL_INTERSECTION_AND_ONE_BODY_PHYSICAL_FRONTIER_V1.
CPython3.12.14, standard library only; assertions required.
Run: python -S recover_lynx99.py build /absolute/path/research-journal(10).md
Or:  python -S recover_lynx99.py check /absolute/path/research-journal(10).md
Or:  python -S recover_lynx99.py extract
The complete eight source units and exact certificate integers are embedded.
"""
import base64,hashlib,json,os,subprocess,sys,zlib
from pathlib import Path
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
RAW_PIN=[49679, '7ef18711c9c575f45c652f07343bafbaf995f30a0c41ac21391d2bacda5178e3']
DATA=(
 'c-rl~X?Ghr(k}RYeg&)gyhWxA$+<6*({ogkZ0oibmn6I0Lv#2hnMsN=H*t|<x$D2r69Hr<lB8t2y6-'
 ')6=S(ja6A1(Yf!F{9BES9Goy^ABtUaEz`^jLuGyVGO?ysNuzX$KXF0LoznzLisJC-YI^F=aFlUZ6D4mz`B_I0Oru^iWu-XfdT`q^ZZEoOsmdpe'
 'ukWZlJJLcn$;sL$iUXgZlKYB%%ASX?LbYk>GX?#(8n+B8|vQ%%))kH^pB_s3^()3O3P49!5)qs+8|!0%;YklKFN4AV~P*<H)&IcbzRmY;?`Dws'
 'V#%Az3bSe>MUDq*J=rf%YP>aEY?H0#x-'
 'gK?u{?9Q^qayG6thZ#NQ`0UKD6WjAqvU8n1q=SAoUo;HW5_KAVF%UOJ>&|2{Z1i8hZbVyy7dOUlmLY524;JHWKF{WjUee9x;;ndR?0z2Cj^b~B'
 ';!kfftM$a)yfzruvhi}1&5}hXt8z82Fc5du_jh=Cv@_2Z=pk7S7mdYoI?Nh#P%KLujXMBrHU=*&<G*N3sNFIQLo{2)PBNWl<FwHOcC`d(fy7kh'
 '$cSUhuVF%K$#B@<Rw%N$d+z*b=Pns8F${y6PL_+f+4{Her<b)vbYkE-'
 '*tS~hICG6buQr}6nBZ^4ok)xt0O}=}!0u$c7>t)0H|QtvID1$$Zn*0k#=W^pp9J)15$u~^Vx|S!b$*~-'
 'XT6<<;5*S1ePBprtds#qP%I~Yvqu9F9n{6E7J*Srgi4>sv*bP|wr|u+DS~KVh}mq1B&Kfc%(5hHcfKxYKK9f+5;vnQrVZlqdHfJl-JRhiN#|U?'
 'huRoMJe>_j$uOQyhFNUxb&`~4k_J7ZK|eI>qhva-'
 'w|3R^PKIfF0A79&sc4Hf)fqMG>0|^2p{mvT;yO;7yLM|YiA#=0HR6N?Y6;XZ_Bz#<=`tC%iyGIW&lHttzKE?oiRp`&Wh*iE2xaxu;i{m0Lj2I#'
 '#V`u;0`edQz!Gr~o5-vPrRWfQZs12eS&Af*Cb3yeAfSF8<K=kKsQ-R`^{)N<`G>Q^{fmFL&yJ4YzWe?BqW$Ll;_vN)^NX{ii}u00ql3S<-'
 '|t^u)`jduNXUW!8wIGdbF}|Q`|ZX4`*-'
 'cr{i}m_$7gTb|Kt4l?5cfnety*k+^c`SKWZO+Iym`od3=6WFB^Y2J9xK$_V(zoeR1^m`10!LqAs>D<7JJ@^A8sXM<^wZU`}ecdxK%tZdVzHB>7'
 'kI>l3=VRQ!&O0lwKkINm>LUtJud^OK|Y`-'
 '}7caddD6+}dw0&d;unG5(L%UTuS!NJ*Q19+Pzd@1%nn`k2hV)<|r@LxXX@wz$q<MqoLheZE2(@M^x8ExRBgEW#`sFKRS`IhbuK;cs6)Wn?~&&$'
 '9cP<WJ}vRLJHvz^FARvq66_2G4;^*=#Obv}H}jDYc@GEEX&o-7Ia-si#F-'
 'PH20S%)f}*$}3DVzi92$&L$YeFzIAN8s1=Dn`SfA9%U&g@fWQizab(mAOZ9I9RQD(i-'
 'd+US9Q9R;ZP2)sC6(|(wGYwXt&d>v+TFqpU1~%Y+fVJasnIHH3_<%)Qmcz8~S#Z`L5sXM%~Qzqiz(W-'
 'PA^b>)Wmw+TF<Sg}&!{og{;uO%l&d*}5KpBQDNQl-'
 '+hcN7OUd@!W35wY)U4{LG3%uWM$W9d(kxvSFr8J9CrF?uA`92ve^M1XCw;0>5jSk?ZD08|V*`VdJ5&ybacK>2frkHy#A(>h_oH>pZ@iEi*CCz&'
 ';7sZ5}u30{`8u8^(+J=g*`?vvGHlW)0)t^#(eFMML)mtXHp;8&G-'
 '+%rI*X1C{=kH&?Z@w4ZwmY$eIo{*14XtlL^LK2LfJ$xnL=0QX&gfx6T^2HnEZD8ZM*L07Wvnroz!U{4AeOckVj(wqN;-'
 '$6FEOEq*E!2pG$+>eTL(OGjYy0G_Dl0PLYt_BZQ+(Wz12aCa7MqLp-'
 'yMlPn5Dh}$O){L*Z=j-ntIkooJ4m6R;-j5@w(i5-(=15hNmM1WgK^QYicM_-Ejp7<OrLS<>y-&Yzwlb<DMx!(QutpnF=9_Jn6g&x#K_`b;-'
 'ZzD4$Y}yatk5|*Dc7RdpNQyA=^R|GA}G<S=NSH?PrZC5gFBQ<EGi#iquRGXdts>j0%yld)rK!gH|g}np65)0+$rLRdR$y$+&yn7>TKnJfUihAm'
 '@#hE=8v~Zy7n$P;ZZeDY+=gaxocAX4C7zd_+!4?$WeZUeGj^j+-)N6+81|t{W@kP0pJpeualdLKsSK1!Y}Q@hEN9`?F+v-JZ-'
 'apLm9&<N3Y?{3iD#J$sAE0?v-I2tZ<%jiec-mw1@mWzYG9Ut;B8?S09zDYfbHYG4m@x|qk%Gl1F2&^S{Mye3q?r``Cr8=LvWinJ=hx@T$Rt|ew'
 'Lor-B+Os~ak8mD{nimSf5x=5!6yXbLz$86kzIfyIVpwQb%(zHQuxmxd5B-'
 '6N}msTBEt_FU&U8}a)l_mdlN*W}&l``MeRsqn|1gb?e$$i|Zv3FZM+#3086m4KaSej}X6p30wNyg~i{&pS5y<6sn-'
 't@OV9;RG@W=ZQ5!q@*71~I+<SC2a9Sz}5_@tI8xHDeX>X#6LM2j&~;OgBmv-'
 'D@yW!FOdN$r#K4U?bTNNm9Xh?VAZirOoxEEY&37IE7=SI&3pr&tpQN!X_de%)7}fg(s#}0jUikwOH{V<-C>dVw*JRETLX#CgW+BUG-'
 ';b+;&%i>e9wN6TuC!LJxk!WL?8bO>%ov3pw;{)vzR!UWduXL}SU`Sx!?D14%(mymufoii@^pEtZ`bNscl(C78$f8)kiX)WpBC9)3_wmV1%Qgs5'
 ';mJUp`6_*+$tVxz)Dt>Lgb?d0M-'
 'R*{e8AED+tCd!tx9b<~cMjnbQL#oibAhJ{lSy5M!xa6fLYgXojZ5tG8E@6+_I+JFjS+8(!p^jNjRgG2trAlFBuLAlW_fj+0Gj+(%Gcz}E*ZNsA'
 'AH_OZRaj#~M%W2UNTo@MAD)!+&*Q(<F0%eCo6mtwZ8@iPT6Y1Sf^(dH74Qp|SxvH+sAUg$2VI(Cb%w<wJm<N@>7JHa-2q0~O@;(>di`|{-'
 '8`(x)#04ilXuw+Yst=6eW{r*E%OF#Fq9<GWXQXfnn~YS=Z8#sxfc37Rt;CJyIQyPW=VC`_C^&zk=EWwuO^)=$gM1v5%cA!LGI922mh=(OHRI~0'
 '59KV-NwGwut|_+<lz>IU>{TRDQ-'
 '63z?t8E(@@Al$<r!&LM9)57@N2BriSc&O2tJ>P<=6gPhKZC?GFXITqI04wIQCB4TwF8odCG2!(=Aep~frgx#WrAS0c}8GOf>Ra|j4pFSf_opnu'
 '(=flZX(kJ;qqL0oi{o9n$anb8sprVxJ2w?7%Dw(fE&U+B37$3{<t)?Ng>DR*RV^fgv1?oo%$yH*qLZniCytX0D7K^zKa?5^Smqu2YGyjcmx*z1'
 '1n4l}tvy1yO_v)X;WV&FHs{BN$P;8Whm3W0lSLOm6Jg2MV<PSAY;gS-za=~kvp{ZJ0#+qhdOD=eGS$vy9ifY9&g4I7P0IgxMO`6?HMdmDT%f+F'
 '6Dx0-K4V}-'
 'kwZ{8)hYFehGbml^810h!+Y|R><1n`mN@Y;H?+KoS`sMIG^d~3)}PFaze_)#+PBhQCsN@bN+u^3;SuUfgeTrKAH9b;B(2kfe0k(|mQK>CD|WHp'
 '$kdU4ZgeratNweTR#wyp}`SG|VcP1_0VRV|W!T>qKPy}B5Tr_g>-ZE~GLhPBj-k_Y&0sq%zWv2!v5>L*BwNlb>5{xaj*w06-'
 '8P+`RZWV>T%wtn$-n$4@Gg^SSi{+euFQ9*l@a5p;)MX4BP_iY_Uv&BVA(%tERm=A;fkQeJPnmK&-=E`kFQh>247PO9v$zcHFc4D=eMH?!6-'
 '`n%QpTTM=Gt((|d-'
 'qRHDl_>0<meKAKOB{t)klYKQN|nC7e@!jnB4=^y*xfdDeqQm&<?IX;N9=%hyQF}{o`D(e|iMy2klGx_ey6GHQQ^j4$%MAWnF0dbNX!l$WGnbp8'
 '3J~DF%3Tw6a_Nk9X%_+b8$TFOJ@yUtFmj@ebBEe{H9{Sk9MoqwSNQ9A6z>fKG2cul>iz^EU81y0}y{dS+`}DE-BTAC&q$J|;2SttE>^0>3i_OU'
 '<)n*1g`onZR;`Uo6wu8Kr^_7q2T0&0s|PTpg%>C2WB9VV?A}-'
 'CDVCzHu0}_xoUvt8)<c!^PSDNv*RS4AXz1|LzxXDm~QT!e0X@>ELYs5~~SvPox(%%cjHR>%4}+@71`G^ylClk}EXED8S?x7GZQYsoma9;NB(UI'
 'r}+-xdM=-'
 'yWAunk7fDWEQ~cQ9;q4)mbDO_2hbX|+)e+^#`$xb;_6xL^)kbX$sGDd%$FT91aMKs{Of$v_W8fJb^JeNH~anm#StVgZhodETQctxPaf}|zrD35'
 'mluDyZm=IMhKI|31Q28aj!up~9+9r!KdnesAxoF-{j<aNhqL29pjV0$D>4bb?FFu=JCWUSI$keHx@ITr*-'
 'j8TNfz~d*S4LG6=Y!=x`AifcG`^`CyiXIlXgtkHv`iTB1h_Gi7a^I-'
 'Tuenc{V>@yz9@VH~&2Uy>oxu1F~o5ANM`CO*o&vcfGb{I_<YdXCIEwApIBnXO|@BmyDQ)VLGDjhJGgrfu(QteBbOwUSxL@I(=|L&r70S*7d^Fi'
 '%`#W!^};5I}Lp&3EfWD2}7G5QK=`|uxFR?H{e-UD~fg(h;%3LOR_}<A*$~-'
 'ea8tv4le~DMj=c)UE2zRp4;`ao*4yxm}2l=FSX6ElcHDKG(jfI4XsW@XCq-^N^+=$mL{d>!15w16!kFaIa%NbJv-'
 '@P2GXRH_)e5{dqJ9*UeECpH?tzkg9Jss?O-<i%<?nO>H(2n;;SBRmlJ?q>%<Ep8w+>0*9kh7-'
 'RqcEkXla9?D<w2nMBhrCa)88?FjRl1)!DdVO^V=elM_`C~$l`j8q>_EU&m5Hxl&-t-'
 'EFd@^llR7A9%no2lalrUM=9C77Tfv8_%o?YZC?FABO{yX*H%4?TNU$Xf^JAFkeixYDMGrzUqRqz&C|+O8Sd=rZedEHiO^FG#}3>eAT!9%jA+zV'
 'zKr>UJE{^s>kd(=NCqp-7Vs*4B|@_5#yQH_wmi#4=sib!<q5o2IFohP|-'
 'kI9)J*H_OtFZv{yw=vm#s>w0PGbRZL*Zh{e;;2FoudQoJhy(r72V#6e<o+39210OR5uC}bMZ-'
 'L>6Y<`wvpk5EGZ#rHl>Di{&u~5+I1zymLg1`z*KXihq<Kjo}*_p~m^`AP%`!ipXLTR%1t8Fbp$L=JvKAj~wY*+GvrrqMxl{#A@Xacq|Wa4YeD9'
 'UwuQQvAQ6TYCGV%Ckc9Z_E{dSM+7fO1QV!z8(}Fcghskc!1%G0enRKyw?_6`fM8(rceDXyK^(-<k0Va)Y$--~I;6!&?jW7l5ZU^m-'
 'H3;%}(NUCN4rD{=Kvn%8Y|;chEe^J*Z?-G*;@wl6#<@O-1GhS6&6q?uk%LMD*3rLpRfL6y-KOl-sC&6mRk)@8FVSf7pKQEG^6JYUYTb~5h{1~D'
 'IDZ8k)j1uC|s%WaS*ld~lnbxFha{s%Z5Z}yK*jt=XBsGis5_PPI}7No#~78_b9M(%DMpPqiW+W(zaEfVh0*~g=k^Y`#=sRxuCAM9VD4+78`PP$'
 '*n8Q<xF_H=YPtN-_Z|F`swK%vIY*8geXFUsoq(xqv(K$e}$)m?A~g@L(>gBs&xl!@$Nno-z-'
 'A!rXPKS|OI$PQea5qwIa0PN<I(x3*b#(aG{Der)ZB$=K%&d(dBJK4ivzCZ{0`f*xuW#brNMDF^wRV+ze6fmZhg@)XnBEXs?#<3DZ#yuO~$yM59'
 '4z%wE&{5+3Kd;`MpS|0^e0O<tbQsrdC>%SKB0$1FTaFt5HW$#&Y6Z-`>;#kDK$)oDcj^Z1>-'
 '2U@7i@=`H3^aIA?r#<SJbz$#MmNWEkUT@{}7;*mbpFpk<DhY2IBJS5T-'
 '(~`e3JuabmzvTJ@GF7pOb<SB`@Z3(EzzDeTA>uBnF8;hmY}h0Eo}p6p@WpbJ_SFG%KRjl|$T9it^n+y7-'
 'cDgVR0{ugijY4~n}MrDNX%DVz<*>a=VN2~Snm4;8*a>97itGqc8t0EsnIL&6~Qn9P?d&%3?#aJl=;9~`2jgQ&quM#15`%jappw}{pNA7m>Pw)('
 '_%mppyS->#s`c|!6p>J?3RuDwXhxK-woQ3s<x9bg`F#qdqNo!}bxPFC2QqI5X$B2y4q{r*0tt~i(HC|S2(;i1{IfnAz+7ens7M&}1lksHC8|lY'
 '~bAi<t*$=fcBNZwarBZ|Dy0fA<t=7(biUtjdn1KSRN%2GOl*B{mDn1khZA3*afBp=+DO7j70<V>a3vqrHLuZP3He}ExpN8Ry&&7Eclmhznsw}D'
 '`kj8e=R6kqi7S!JIDfDKTDiEmq(5w%}*BL3tv|ZU&Dj?+bUvUEot3WJ&NzemzYDCB8%oluq&RbsE!F*@6U@_62lvH)aOg!dx27H+x)r;cLUfdP'
 '|1FW0A#4~k(uh9My)4nW~#POs2p_%Ymxl_*d@&~!@Z>nQI`A+>-'
 'w&+W~{R}c!VpUFK$Y4VQZ0sF!(dkZcq&P2)1;lZdO&d#!<IsaRlIF6tIdWsR9=S1lCUT=z%TE}qVGPASF2@Eo`Xg~Yk_WrlT*yel`HF)G`oU9M'
 'WCgW#pFuSx4&YZ)F^^Rlyo^0qs^(yQ<Cx8Qa{vktS~{=JW&~(&8P8^D%>duVg<=D?#@;*a`FbRSdZt<Ytr}}I5Ck4Fwz==YFY)rv)uBv@k3$(f'
 '3w}S{;i=!Dy$VUUS~`uTB5kNJYE`G1srkyZ!)Nu5`^$2+nPx2^*`U^&#)muQL1u$?{`Y#f=vOP`vw}PxVoKXZ1n6us&SX@?tzN`n=hL{<{|%-'
 '8SyS|;#=pMhlzE0ODn4s|{Uo4U0@M@fwAoXTdaICnzr^z#lEQyJ{jE=GPM&AXuYbFyr)#|m>B&JHFDbx;&?KmDH=F`SRmjw=2UygMk)oRK=<gb'
 'CvfWHhWG;eQ#K>%FD6PdY1=H3G#n?)misK|HIa9&vKApnP0qbAOM*wLRl7`}3uvnJ0xRU%BUWJ_3mNE$Fd4b85DC4IMBF8kRwjM7KmsUxJs?44'
 'bRgrFn7F~f3Br)-'
 '0V}M2FaO1h44zU(oqA0sLzGO4GWS6iVE0H1W)oGy%jLjg8zX++8V@*K|7SFg;_d<*PpyFx(l;k&E(Z(B8@&<hzKc%J>$ZF6C16_?Hc_Jj_=}DB'
 'JH%FYPzhXTY<QZC*;S}*xQ%unk)yd_kkhNL0JjV+(nC!GLj)n}V>gW$8%W{v#%953joywR&_OrA=s`409ollWJL+g+M{5>8=#RXDt+8^pHzInx'
 'FQ+XGq7|bd$ge0A+it-I~S=ltB)S^U%gJl%}jAlueukU$Sb-'
 ';Wl<+2PNj<fsW*LL>M9WE)lW({ZpyQy$!RY|4#qUF6=cyOv06ndr|=Kf`V`uCILmd6_38TkrUT7P7HZO2xGNB7nFPn0odO6cu`8ktaoQJkW6L='
 'hzf2pw|eIjy*Ob1s7hp`}7&t0=cEpTd4<U#mE*<zrJYnb_Kb2&e;DT@(p%x*0Q>6-'
 '=bR#*!JxwP9fL<5vAGk)9<sKWJqShYsB;FuZ^^vsP+U1kSNSFI=y)DuJOLIx>Kn7LVG|`FGCyie*r&_6%1}y|u+}bJLnqswMp-nt!hyg5y~z-'
 'Nlo@%{EBss%&f&<W-'
 '?yU^KwB<L@;=Tdnd8uthS13~z>#zuVAUYkK)i)5|A%UgyJ#SUky&xxl=w^5iD166Zpt_;Z69;@`Z((B{piq@O``u+Jb0SBf-'
 '<=;%)>o<k^I!BAS2U;^GlRL6;uSM!j9=c3U!?DeTlR(T8v-n}{|j;;%qTF52~AlWai^3kXLgRAz%(dqv2*&*FXBk^Y&C(T-'
 '6#<ZXXe$zfYr#6@E%VUl_QPBnRnEw=FL-7m6fny$EP}_8_&s)cT<zyes(r(kfQM(<-^>&-%Hrn-Fc|yS_|D!>gqOrP5(arwfc0u|_u7>@8@Dla'
 'UT|@p~aUG~H`cETKQ)|6GdlbA`(Vwd~dJx+;#`I6Qi_}*u;L2s3{_2HddH1IO|6eBl-'
 '{Ued>A%zC!$WAik4G0*N1xz592_6g@ztCCgQF`It)+!%{cm)kxHt%q)4F<>`26fh#+SX_|M2!m82~s;J5L2j)h6TN*G+*;>mAi-lr;sCOwp&>Y'
 'qc4%GaoH%6<ammtvzWJdA^<y7I~^bd+1$o^>Ua|G*hLwWOz?uP@^mv%V4GaK5^dRw%(!KSOko785;!#yj>>fuZJGDd$WwT!p6hFI7?>Rp!ASV;'
 'TG9w55=|lWC;I(#Jme+X=|%HOa}6XF`WRQn-TZSq4IzM&_IH2LoeqUBd3mWGZkF#`P+ObS?f|bT94zr)~_p9qNFH9>g)WwxjX)&my6&2Pq1X0<'
 'GN^%YwMxhb#ByOKnfn@HYH!hn;Wk!zKm7FZ}vEQwTHPZG4tU2<!}YcmV_c-kF&lW|5e|viwE^;zU(v}#MhOV;;XUwE&!w3pzf#+>s$QD_r&?|P'
 '_?`x$a+(?A*}k_*i^Rc&L;DDr75?fP7^xc=``(@A>^Y?k5<btL|KK)%%X~^TIf|w)l6tW%~pYXn(?Sbx4=NsL1ISbIrT;hBCI^V9?W52;E;7Qj'
 'F3lLG_TXN*6KUtRP)Lg4KW4Ai@H(Y(3qCX^3LTevjnkStG}Sb+wF(EU4B6Wg*2ZKPKe>}bZ$;45rS=KpTVNt#>#rwGj{3U9TIk|=IgZD-'
 'o|op(5?OPrhRs?Z`50RT;nc*kKY+`XtFFJ(=g{dl{~k}i~)+V0$DW3joR4QEBnd|>y0!6j<amL2QRh$VhoxzjM@dXj!~yuWIUR2(aBJCA~GFw9'
 'a;|s>%fRkn3#;ov<^4xYH+K}DaSHw09acR`-'
 '_2jQY)i}s@s+E<`>^CCZCgGPNrnMV{<dYN(D&t8nUjTuq?^U`^E&epN(ZtSbquD<IHMrXg#LgEy;Jj)2Z6?rlsFB8O&t8!t-'
 'e|2=ZlrkC{ox7b7l@-+=j>yH0B_<&c8%7&B6bm~U7*_IiT{I3nMY-'
 'G(XfUqf_u8<zalr80|trSk2zWzdPv?<+Le)6RVPWLT1!G3D(xsK3pIOr_h9^(8fojUDupWk0Ls_kyHPF49`8nl@E|>}pDp&$By9p^>4<R}DSB0'
 'mN&;k8zWS&L<!}c@n?{QVUDw`JJSoQNL3N8X5~3>sKW<9Qe@8j7(FEObh?F#mK^63x91pZc6B5*=#HW)lj)E@UO-'
 'H+Vro*zb*c4+jWL{8aEmmTthVYmxRtwcHWQN&P{LPVn`5{ItubZiO2kM)?-'
 'x|8sy&=dYXX)oRAL;UsJ%UNA=p2b@kVl{+cO4nF^|1d=G}HVL)}wwJyx!wJ8x?>tYig-'
 '+@uZ01Zk6O&W!vxR!NB{dFD1rm?3zf2X}(m8{Y!88bOum?yfKV{W>nSLrpb3o_)Y2T3Pd2*c-'
 '_!S$C{_@U9qePsg{+2Yx(7;oh26ANweg|3*9E*Zy)ea4b`dWN!}ck?!l@gpjOp^B$3c*5`$3Z)?-'
 'z$;@O!|)X6d3<9HeLB0XU2TA}UIG1%p;y|h1#RTo?rv@v1*ligfcjhQlJoLVRLfoVFj#z*_eHOBcXyOL&{}F6YpJjOiM-'
 '$jbK99LY1@WY91@>}SU!=y?2d2jE!L8j6?f+D=H<e_xQy3Wio0?M1=UvQe<zk2{qOOlkx08iW(n0bbh_*eqmEHPtVcHs<-'
 'afBP?c<xPhg`bP^Qj#7sL~=ul0rG34%+!1+gKYYfHy1)oyVz1cTYIfV<G(mh(<zNF`mQa;DL9r0Zec_uXU&GW${nwi*jH1AxX|F*+47JLJfx2?'
 'aRiJT0HxdLenaTfAVXADb!NkP}<@bywV#(}uFC&kaU`I-bK8WjXHoJy|Rw#uHk5Ehe)%YX}!;QuR-4D+tGjLTQ(-H`Qc-;-'
 'kF82lc{3p`V)&*lec$R(og<Xg%0)w-h-IOdiU%^ZV7sHEQ|3mSb)Z(_c%2h5=m{%7Ix_3V*ZL5}%sPUoC~gCY_V(BQ{0XI=err9o!M$Y~_uZQh'
 'lvonSA2LB$@g+zFFCV8z%i&Prrn+$9#GY+iTYUMvm+g-'
 'K>=JAa6zU`sfqM&L@tHDUb6`jTNqb&0Ia7{ziSPrC|NF<n{hYD}}Nm3#~Sy^n3v|QdYO^UOaC1US79*qIMR;Tr^INmn3+n#vYy3<_BIijk{!Gv'
 'pmtxjtr!Ys~mMrgUjdcMzIx_-<0K&-8L~<m4^FI(y)Y7q2#?rJB;ZG>RoT5-'
 't|W6P0B0GOuN6;_9ahuDb9!XI#jy1G@A`1xztVwo$F(@O`9gXwXz(48Bgx{W;i#Fn@ueS=FQs80I4ghd|qf&$(0422%fJ9qyXev6tc6XarP?Wu'
 '}7^TW`#C=EVOBNR0yXGlh8YYoJw8yC?&7ZU~{7o)WwRRQhSzFnH4Cv0Q4YXD^1)TX;{L7a}DOBLm_pR_OBr)2D+=CfUR{*doMNEJ97SJSyE`AS'
 '{Ds4eMwuYJ~U`JTNMbbq>@pgO10Vr9ac5}qoT~GXEc6=UQepqXGpl#WOv1<+iD~u%xjK7HP*^df%a48q#uiJ;#i_<tQKe480>qqt}Iou(t+HXh'
 'R9PC;byx5F{Bgj)hwtv{N}QipO6$qH*hM3lX3rhjer3IR|sRN7&ob1OCHQpu7aWkziv`Kgthp|4RtsKk{@$v*-'
 '(iV$Xc|Q1cjGq92C(V8p;&dz;_`AF`iy<-'
 '4{(BK}()0$gNd5?B0_$kae5%S!ICEbkOv6!#pDE4r}`yl!V(U1W*;rpdq**vjmd3=7ueGH|$O+SAF>c*0)?!EII}}kiC^Ro^Oios6@e#QZ132<'
 '){?9?EP6XYSW$HEazrY@po0jSv8d<cApe-'
 '!%^I@EH^Tvz!SFPnqKI+!uG=;Z~`AcBFi#;N7!~`MUL+Z%XOmAw_M>xq3K(Wuzc5%Ik3jrtp7DGg?u>TJQ|{~^dR?5tF%<pCKu#(uHr;Tn~7(K'
 'rT|7(6oH1&4^qSOn=M)X!V-u4BCmcZBw~irf+xwSlR^#l<DvWo25I-&{g(|*6K=um8=|mPGF8phyW>kvg|m~d?KV0`{Yt5tHLb5)DHe3-'
 'm+N4M7@*%0*A$$(>g6T$%2<se`@P&y<N%<J+dQ_#u5mJ}6_xjDp32_RolJ)b+)rAP(WwL<#O~FYwczc<)=qu%=FxIIxLsz-cg(Z*sJX@P$_kU>'
 '2E2NmPM_G1DtDAPred4qjbeRh=V?r5#CPQ`nB2JIj<hTL@~z~Xd8L;;BDCJ%>qgu2WMR}rz0uDW+oMUE4UM{fV9Qs(<Sw*=P+Z%Sd-mGOJl`5+'
 'NA)9la<pW~_vooNdAIWWd4(?WTJVboy{~N$BppzgXkJ-'
 'e<q?B1T@%d2Xrwk)S<wx;?M*3(9=5(dafrZ8GfEB0{u5|K*R~`#FD75I@yhkQX2WRxtNDL7jL)Cvtrs9)NhP8Y_rgDTsrImtS5BCG4I?*L^ti('
 '}DCcy~3=>buCE!fXV{@<EK4;v(H}kBaRvC2sMtNY!$5xAEiDVN6w04>2A<yV(@k?B9)Qeqf<vBOyo`AG+T4Pi;>bs9QFRE@;j6TE7H^(1y)Uvx'
 'qrY(QUQ;Cc&jujICdN#9`45ep_bSHi2i-x@IR+~)Yj4mA9#Z7?Jli6fVYqwQoUPryS{-'
 'Ul=?4410xm8yi9FOru!%~q7ynN<m{_f*eEa_0w$5J%kE?{rpsnfGOm#jKgqvGv5d10t*7Z>g5eH^b<cwMRRdhPwI%KKOA?W;Y!E_;|I1E95^%m'
 '2}AHi3&jHA+tgllO}EPI#`>d_Bf$g7a=38S#2~Oj6&ad3$V9A}E>_@?2!?Y^c{S4r%K7WjSi2CVH*DtWs2Ez;w3uxK|!$6qCb6tdQsyu(qkFwh'
 'hXhPYq)=>r?H0ENkgmzxLh~g~f@;Pn~MWVEN&4M0azfqw&7k;cQ3mo5|)xN4fX^zS;fJiixV2K2edU{;IqeKtBX2wJn7lX_Ko#taN1KiV^>qqp'
 'WMnnd)@<JZhRBbu}=`G-'
 '>Z!@&eUp)WH8XAaq4L<vG#w+*XFTGWO(N6$$Yvt@k&ki`zTJGUD+iSKXZA>a>+#`u(=?IA!;vmVj#g&P=fhst$TKEVTYq9pu*)zKwSo;Ts8aOd'
 '(@3f0sOD;UlhwJZdq8C4bxW+veYN>|&{MI()HIxsBg8ez*S2uR_H66^LyszXS26xC+p0=2X>kz}H&^t&8;UC~NZn=%lULYPD1((!(OI92%N*`p'
 'JS;L>sN!MIm=#Vb}62;cLNl)wh*EJAKtd+NIcDg=+A(3VG$idh4amr&qLpjDM{b{<n42v|IS!Hb2|y8LoEa*;Mb%qQ0m+Tk5@4)Hm|L)xVZEnW'
 'GIU9Bq{(R8}E`ier<vJc{(g%+M>5ZF<C-bg$P=aHlF<zZ$m2_Y{BZPEz;!-'
 '(Rd(7qd<3yjZtBxssRF%4Iw+;MIEkx!T40UH4^BL0hX=(RqG>zF}$p^xB+^fvoTD1})xyE7Ts|3H=%=ZJl9)rBz#t*x!Hih7twIxHAgDvs|}*d'
 'HhzTH&VIJPR}Xs_>$9~$((0-2wraRVkNesSfv-226AN~Z{;ZF)^j>Zr2bN3r@fU-'
 'q$<N4d;8yw=a&68>mUSOx7Fhi^LW9lql?qyv;7kuDWSi&5@!9Q(pC}b&7p#;aoRrtx|%#j&rAW=HIAG0?QNMHrnRdULduW+U#x1@V`jg|IFUHN'
 '@2(?G*DCL&#Lk|-JQT-Yv=zDeDrTUs)CDg+F?MCZKNtV|GsAr=$J?K+q5p(xT_4PsY^u~%zIV;R(Use2g-'
 '<KPO9Wlw)d)c#^!vSKLW<$nT7Fpr`X9PtK<l|8>|VvL)T^Liq~a$-'
 'bT*blJ^8Je+uFNstB|}6fkLqCX<V=W*xdvAj?6<+rf=qi8+t@7v^`b?>Gu1}!&+Hcn!0ROB+x}!k%Msk>pW#t?Z*CUJ3B9*6d8&)rSMZ3HA=@X'
 'Af=2TB~rs|eX&9vH5IrmYG>zHWx8g?p<llfa$3flelK70(?O{}lE&{xZZc2~&nNOuDS;~blECA*@t=!@HC6)iJH{UQpY!-'
 'zf0GKKqIA`DDR&S#<Q~5FJ*?0oe$y~js^7jAj=|tr?`H8g&QiO<)7j|O=(jrlEYh&Xm380VWR_+#J%O>T#qL$Y>qOnN;&-'
 '_(lZ?MMZnR?Z9KJwTsKm^?z>w!sHSQ&MMv^>1{*F9eMFFeL@fQlE8*Kij4nyE|%08z9Ha86V3BPUqjC)@$#z1k)v|VFsi#kU^@reuuo5^}`3HR'
 'v`7xnEe)v{Dvv}4v#^|sa9*CsKYoGYfmkIvZOm-xmg@|19%@y<MlZoGWcaBLvkP}siUzc(%8X|MK)a0P|?D0z?<lwT1guq@k?j7a7Di!Si<O*i'
 'So6GCjHbc?rv?Mn%i_uhp}#6f&agpv2tY|o46e%iXr2nVUS*494Ur#ooJ7nkjK`yb&#UR)i&Ip)N>7yD;_x5D=2yZwu!!!|T=`ya<wXGfQpNAR'
 'Z9S1DxoDSX$#xVvaeQ7y3%7cnt_%nR0*i*?5qoY&`JFj|h<a%+C@n5FGWua^#z{zM)T-'
 'M2xFnAYD+DMKvB1KNlnCo!)j!44<)*{sbWPO;@{^*H*dJ(*_ghPIcGj=Wx^RqHK>>L5sm6jU=o(=`N{D9(`irvI}J@CF05!TY70%J~hJ&CYM0p'
 'LmrmME!LCQ~T`v;&lJy`2V7NG3WoN3rX3%O*apztG}94SX)AX{v4RLdSNE_%Vkz)z8?gq{qnMXa{do6C8v3&`!k=%D;H??)~+D(Rhmk|;cQHYG'
 'pYPOpMJS!Gh*^;Nq3U<$hgz>W{$PU^YzNWI!@5b-'
 '@sEF3KXw9>C*JdRKK^&!L0HnydO8`YnL3mlTn9)VYKhxZ8Z5$x)STYK%PIB^N2p1K6m%uPkbx#PM%DAyZi4av4yF+iaGKdx=uL46`t?~S@<(?7'
 '+b<}&ClcC_YbKKy&+xrcK`Gg<}D07I4G8=0a-WlZBYxO$n-4yu*}GcEVweYZ7Ya8--Je~S(X(zq3hw78(6Mw;)iGRQEtr%O)sESMZX_i?Z@)`^'
 'z-;+|5T<bwmjGJqX0l08^j5Gw6#M&@*E5OQx3t<cd5*a9Mf^Bvk34UGsG|71vDxP+|V>lPbL($d{E7E0s<M4--W7nWc!ZkQ8$j~M`6IgF>}D1K'
 'n9)zL>Q!PIyOcU+7_I!9Hbk$rWv5vF$2f<B8eNdBH*EoDS_Uu*}e_ZM;JEnwtOdY2&C!z5s@Nr-'
 '7qqP0;Gr05k{u#dZEwFBRUNC2{>jJTt{V;<<kKm+p<mDqA^%rXi>IZfTSFtP7czut-'
 'vDO0Mc?WC)7NQ9Khh=dg#gGGSl%bjK-#0R6q(KgUAX4>Lx(fXre%(G;}QV<Zx-|5O6dOOf+)PW8g$YX_t~cN|0U%G4Pp|zT-PY4AVu$AV-'
 'rj-a0g1hlUwgCP9bncp*W8b@p5yFBlsnCawbc!2hP4AD=lgh-jLfoS48dA_lah$o41;G?23>YcbDH<a-{I)q|*d5luOe^ei`IVwxTk9jqIG-wT'
 'kKHX5%@D1wGGa?^AIhe(Jvpl`q+-7qj+njcI{<P$MHhkD1az=k4l!yKd^k`5q{Avl*gJOuMg%mX(fLh-'
 '<TfF#UK2i)cn$PgI&4)c11=4L)WprK8a0i^@mrryDfK1n3e*Y<tN)eWvE<V>C)k`BhwN4=1!j~4-'
 'C!YtSb2!%91z}T@&pNWZCVH$+C3BjO#d`dJ;0s!U#XZbW!U{&Y|k2o_jBfkI{Ks<>(9LO42ftbg{*hB6H<Z~U#nI5nwgn>B*Y?8+DC|x#DEx?>'
 'X#pPV&VtVB$Lo*6V!0ZUqOmQ2ahDrK_CCLqZkCd5hQUr=rAt0I=ge>K*YbuaX2bN`%w!vV03v<m{$tER;GH@+uPo##h0$-'
 '1(JTh&Mu!Kwj8zQESp#b}Q&aDu#$jITh6Y>O+SVgRiOb@D-g$l22MiYaCPQ<`02Q0$c6q*Y9AeTwk133a_c4(N$X5ogm@m-'
 'o}6PUZKMkCXLw&RgQEipq`p%eK5GrJp@;1V@*)2Cq)MnpoB8%3nyNLBy@;wNVhQUS^_8~IVhoavL!l(qruRY-'
 'P@CIrJ`dchK6ysXSr%nykY#GTqx(2p<Wl;?-&Pt<W)$CFUN1Sm8u5;}(_!-'
 'U?4iDl_TKg4mQ?Om85LYRcfwIwmZGORfw7d45jplbvYE0~yYjLoA7c7rJ3_9o`p3z)Z{KP4kTxrQF8cJL9{ocf0JLG~FsiGUa7Lw7>UW|ab4Z3'
 'jMK;)1@=JOmRO7W$B}QvpwaWJb0n%>{UzbvvvfNwNZIQ37w5l_n`j<{nD&?(r{^vTd*u0@`Gj2vFdHxmg`Se|f~46nF*AU4Vp?Gf2o-'
 '#OA_*iNc(-'
 '(gZCXHfkWRZSyb3afnLHnh{ikO(0>%f?Oz}{Y}&6IS0qN#7DrFn2z<D3iJX<=(30ui)}&On8X|40v~1+Abl8ZC?Ewg2ua9HwicM_kVOd!$fT;U'
 'Md*<2x(Va!N(%%t7`jr!p*v}Tpm@NtIhxS@l<poQ4=h+5N9s>#Gny&#Dwq#!vU4W!0il4oCP+{XASU{OHUPW3IY<mPVpWTo^nK=WHy|-'
 'V8I%Afmo+~qO{`BefV`S)fgC8afZBpm<Y(kuWI}+Y-3iDhNFE1j1PF2ur$GWDUT2|1C(zO)ywF|&>t?7?5Gl$92##Dxa^--'
 '#Fk2xT2@_~IBvjNp6O-'
 'f!ikgTSV7wN)M$il{&7K8D1i5lz=8=7*YQfuN8ZhUP%?1G~3@DSifvW_chy@6u4GOU+MwH4NSa>9#RzByDNAN3qL_TL(;Q6I2_k<h_Ob~|55gz'
 '$oCbN-CmWkL1czfircr=euK0jbBjDtx?+{M-'
 '=WYxvy4Kl;yg(ShZBEBWmAS?lkq(?p&vyl%1<z69_J~)y63K#rtva<jVWseokstG+{vCV@LlXMMX;{&$rz!&@mG-+}pr?BV5a7;q-'
 'ZrOr`v|AWSBLS+Cs&q)jxJ+~=g3s<Sh+z6`&msGEK0#2<p(Cf-frL1$Ccr(UQV6DpxnP?KP31|q1JGe&*z<ypca`JsP_H>}Vp2n%Ay5WR1koFA'
 '8+0;Y!o7fEawIuXl_t1|=>)sOen#YXkXQs>X(?UHWS_{#I>{m69;gv9Lu0~RA_;W}KPQkj(?nsw90_CNP(6Tvq!yME(;_vkZ_|Q|0GY5`E&~T>'
 'NS?z=6NZ#T7GehCF_Zc>5ta=<+0LAp=mn;U<Qz)}IFqC>VDKIG=CJy4Kst*ZVob2*@Jxe-%u#TLVZF!!0VBZG2}&OU9S|G40jW)b8Id!{I-'
 '5i=lx0K~R)v^glPx9IWs2QkN1#3m14Jy#D%+*?8V!RiYGg8&kR*%rjZ0$-'
 'B+bc(BGU@dbv<@%fo%jdij@FXXUs96HjG4|Y$C5xpb=>a$mR*^CL~b;*MXgwA7RFznpxmUu*1T~1{r)3j3O$yhC!HQvI$MHFac|1NMuN|;KB8T'
 'ps}(+KNj0~2nAG1jwZZB&td-`5*V^-'
 '$8=*g7Rp&so(u>Ou|rFXu7KY{yOH>Xtl`L2%l$&EL&AWUKIDY^Y$#zHe3u7IctmW4Y1^K?7TOXZSBrk}M>jmF>l`py2@`$?Ln7~p1`M=aS}kH$'
 'p=Us5T0meC6}qG`Trv@?Px7c}fP|1+1(p`MgRITK3l6z7kZ}-'
 '`%0kGv$D<5L7993+K^Bmm1rd`T5H+CTVDd_bnEWS;{b^KWXD}qMg2?JY*a4R249iFuJD1&H7%NhQV1Epe7>@)O>x&?VNvk8~9`G=xh<ylJNYJE'
 '3q<U;p&agiq3k^3Stz`4SVe+6|rOC{N+@`g^&8uE;7HCCt0xY0{sEJ3$&144*ijG$q=+u!bL#$LxtonH4A|fAIX?9dK$tV-'
 'd5DdwVHKdRnAetwPD|C3BK<j7efnj<gR-@oMkKHPZHZiPx^#>OoW|JX7g+UdXEQyXS-ElBfAo;{p{{ao43PP43m-Vq)0hhBwD-yZ7gC?X2heX='
 '6XGG#2(d3Xj1yew)YN9x47cx39lAfdhfTE?Pt$^5~5jt3Puwntlc`1c?jNodpQvsXkvjYa7JdjIx7{SPr<Hi(1UF5WcEcmYUS3{G1BvSP@dkQW'
 '&fb9R#E)eWHE$yLpOrK^7^nxeN4rf44vBT@h*5~oT(aFhW+-'
 '#V_c(EvhPxXz#Mj7TW9HY$lLYuzaT&1`?**~T1o<1KR{l0%laQJ=Ef{s}D*r7;&&0pX&UdLv6_&{JJh@-'
 '20`skwiB0cAI=w`#A7$zh20naAw8uOtDy)ZT&k=(}3=HXU@cjV|>ulLQH)(iP`Lr;TE$1bg>&!5DwdY%Prgt|R^D^HDH#P-'
 '(V)^Lv>ukcT6JC@J<fdBLJ#se)41dV^Iakxceq~XOeh-'
 'z$~X;JUDId$k7HeGB?h6Ra)%&CzuGIZcmP~ZXotf#r=I+a&UQv&g#fC0G8!L}t~Y;pDN2RW=&>hrab64m6zGb3WycUyPml^4qTq9#6>WrO*=aj'
 'S;YoHch_1-IO`_NKG!F1Ge6`Ru-|UG|v9N%ITERu);>UYmPb9=NHo;lra}UeG8uetcAaMO*dpbSqJZhlvd0+~N*zWYkxYqHa0*FGe^v_f-'
 '8DWiMY+A>&Cerz@H0BqfIFu%to}#`Q+b45LbqNlM3n#&=0FxSK52$U=o64MEw8`Kfq?q8;r5t;)o&6On2t$(YRk8bxy|#w%oe$+)Z$W~9D6K)E'
 'FsgT+@F(#2O2_zMq88uE)2tdIohm|fNlD{AG*i_{NN*W6GD;<~obKiafW66072_9~t-+D<#G-'
 'k^D*ckK!mJe7PZZLH1gPv8QHyp_a$aZBgoH_u_WNlR_>>&_@HWi;m%6vmQY_eNSW`_8C5QeK_07|R5cCzKCtN6X=2FdYuE8Rl1hsrg=MC;ZAS#'
 'R_hrW}h|ziktub{khhLqwb$LYFy84Oc#h}Sr%W3(K2qHiNluYBx##9Bow5eAM;ppZa*1~l9*Mw=wyo|CY>tuA%ZG=?!9638_Lv|v|zSHeiObu%'
 'o6(ETN~BsOqsUBNLH3f3b7t^+p80|@+>%|HDwQx$DjIPw;Y{%Tcms_ZzxwQTf$Qt-'
 '>OA6?<Ui%E$;}nIXWw$@4r|A4iTFduC3o%Z_C)DcqJ4`KUF6N{jo#z)o{wrf9iDp^H?6wZ#p>s{wIt*zx=i@vk8afo}Hha9lhPZI{tXnKK*cVb'
 '^QM1_~>H&tHl67lGm1bi2wMoe|UjL2W?KNd3^QH_QAWOgTHTV2i9o+4lX{vlwDG!$NQr*nTzvcU#9auIi!4@XXh7BeK5HcoTICY{dY%)7ih(jB'
 'QqMG{ImV`;%Fb$+E?%P&)Qb|{3Cu_uDK5D;E2Abe0-?n?|>3!ejgOrtX|0oT99*d2GI7w$^P-'
 '_hL0rwNZcD*&3`t$cfJO5z6$eK@$2d>#3!?d%BeoUlpP;}7?el#_>KHf`Hw_G>}?K$DB~YCAX3}jRskp9tN3(wQ7u7ft!yHrD67x$x6i-'
 'kH>p1Vy4!5d5}A5jto>+-'
 'ot+)1jbCMiFW2T0`sdHj;|o<!25S&feV|3jZu6K6)=uO8e5Xe79TJQlt08LhuOn4_`Th`;`k1G18zo<B9m=M`x{$u$OevPWlW2xu&zBwkf;1Ce'
 'kwkss`7xVKwmZq3(s#(ravV4-KX_H#*d<!3k6=@N6ix|8DAPC0D&ZynfiTj)9CxxFUUE$NOaHTBpno-'
 'bl`oZ!yHBLad{bWORY@$@s*w9o)cU4wfDy#IJTIeM3gzGT`*Q;fd3jCd<SY}3Yd|E3R_QlC{J_Vv<*@#uCEJu;mDYDp-fI>V1gd3iUC*uhu>JM'
 't(yCJC(=AGlx=mSAw<sm5P`^wnGv!;Mepysz$+u;uROiQ1rH)3GzMD;XQ?V=Q-'
 '^~%;>KNKhz@$}lle;R7Wb@iiZ?yNwE4y{4oLDw7@^941+W=oy*L?$_s>yFWd?6pcybB<|ItL{}1^H-'
 'XD6@R`OFY=6R)SV$ygU>12%NV0X7Zg}vSE?)xE0@RNIx}rVF?}4+C5ruK<>-'
 'CVnsOIT%RirvE;ay>+GS%(vOms`2|u*$8jv1?sXJFshRPj`G&sxb+fkTGhPom9&ZXd9#?3*fy85`ZbwmfkA8>_5sdy3^eAc7QMBTB&4-'
 'tA^Mf<7Qc-II{l?n;^<Ux}wfR7xZWO2+0=0d&E@<?M(J(Z+HD}H7uEvy|R(?Zh{-'
 'rVRPG;G>BEe;Hu%C&8mKV_&np|zZj!iw;LYuO5G;(XL?v4s+FL}W4^Q*v8B&LRTr8jTZqRY2W$&G}y@;#vU<(GNz8xK+OVJH5G5r0OzygIy+$U'
 '|aTw4$PKuw#$en7>=6eXCB^{FACyL7WyJ>elx~9X$t3+2Ax*!&_4;r^ZSUyRK4bv+Rq00hu0K#%ptxZ!O{SZrxdN4g0iM%R|APiZl8Q^;5#*7#'
 'r?G>u8O?HdvvOdZ#<+f-Y~%Oe%EKyz-c;N2C1kgh-'
 '#>8j*NkFR@t8zdKp^V8!NE>a!K&SgP}9@yZooepO;z{dUEC(5EdZnTV2FPIdgXi{}8*;QRX2z<6c8qVRnAP<$<e;LD;)A2dAvYGBD@gU#t`Wn;'
 'eZ700HYe}+j^eCn(Kqy!FTxK>wLJt6E<^1>*0Fn`vz%O6jh*V4f}>Cdu^?t96P+I{=8noqUNvzn*f8HnEcM?DrQwSz8E#%m=G@~M>0p87&9F*j'
 'Y=dli+;)|0oiIV}RFOuzBlqZA3oo<7C&T@s!m`T$A6-*QehbXbat>3q+Ijx>Z>=17(aHr6Y>GN1T@<i_l;D_>sii5^{Nd;!d@l`o){DE$b-'
 '<^tZ8xB~00o;yG#N|9e31%;uCljU&HsD9a0=DZipmQiLr9f+cNnGaQ^>Y=wiy7=BBTho(iQ#WT^?NP$j6^$ytVH(GlUob(LAP~iFRm<@w8|ltA'
 '*QU#j@(SxCUy|Q#HFtNnt(KOYg$GM10`f0DZ{Fx7Q7+RsZT{rwpw#QAqwlyDif&7Hzbh(eOyA5QVZ%xcl$&LvjPGP)xkkn;d#I~CKfKgriJ4M%'
 'rMXC^Do;B6Ci2VnMw3y@H>g@$PR>qk!MTc6dOk@$#Ys{~B(Ub9Ri5@WxCsQ}F)p-'
 'pBD)hxY>MAq`MVIF$Ja9ZPwoCi{8%_~i%KRx;EDe5eyc%^>32f^bm*Th{?Uc+{<W!PRk?rZtDGN;mkoDIWyECgfXXZch(*@U5vK;x&GyS^LxPa'
 'KkD?!!^nEYKRAn&zH8}$fv@up3f=_g}ixht4O>ve|g7_pFG*80VawMqo5n%ox&3Qoo&?kU6gC#3dx$*n$&)lSK%wPtoduqn9bc-'
 'u8{VkDo|E$h6r*QpLC=!*swS4@d9@i&5za7T51_MiU$)LqWt)Ao=M%CqE-k#umqeGI(Sv_}YNuq%<eKxX8{EUM9C~}^sN#KVj-jKM<np)B0j~N'
 '~*44;0|VqC{k2`2?9t|hzPDndWLye@Ul*x36c*PXYU49u-ekxL1iHdq$*_LcR7NufRBrxii(=1IPwFKONU688qx1i%GNp3@C-'
 'NnA35sXhQZ))QkZmK2W$-'
 '>RMem}*#82?sgILIpTm1aCzP7<<Jxr|9j=hQ0NXNpu32HKk+zhP6!;{eu|&fNom;_@z_r%bsb)W2cf8kNspthj1f0DgWcCygroMGOu*-'
 'OeJ%3cHunZK(h+u=D8l%A+<L6^MA$LKRKb)N+;r^bge*ylM{8wsQyB}x6(Wz(RbF6+87z~AG`|L)*@AIC7fIO{RbiO_A-`RFs#+ks#(oP-'
 '4dq;ZS(vv1H8)t{-'
 'Fc>g8=>^0iOLF!1;o9%%A*RJ<;slrKFW|CpTXSCRoey4?uhSqtMbUPq+{_8}&DJF))4r$M`w0Qe5B`<<;Z($FZorh$&Om$LA4w`*VoA{b5Ar34'
 'OUzTg<ReEFK@VTm90nR6DfFDvRs5@tA+Df-'
 '65hQVKEJ0*R^rq(!bfeso&+EkK%Ht9i{ou3MB%R4o^IfhhN3UYWZJokGnPt~lqc)9PYmyCo5e`t_rF;lAfvnskDl@1ex+^Tb`1J(&1Z%(CuaI-'
 '^{U@tKgP5%EWnpGU-fp^h)w1*lK_mA!fVhmdQ9W!9DpM!AcjZqjF~goH5hF|dAu8?$j?7md%vt1p`p;1@&Owe($c1(h9xVtVAqY}IkI!hRkfh%'
 '`=xOf?&ysILUJ)pWhR<dNi$?=FRw!7S#TvbUFpC=!^-'
 'qIZ|_iz`Yv<sVT9YyLyz9H#yXO#sWE`FF?US(!Z3Y3Qe8g1$G@9;7PWnkde~m>*S^4ZXqB->sx98^;@R@N|s5*$-'
 'yeQOFRNsq|km|5u;#fANQ*V?FOcQ~qL88*3Ya#US*Yh<d^*q17mI^=bBZCD&XW_eW9(RMO4GF)*yvu|$K10gXfZC;UZj_+W!x4<yr)+symF^+&'
 'MS@*|}4>))>F=~`(A$s#JcK_=NNk&rKe^}KJ0Mvg;SdTq3JS3JbZo~ikxTduPE>UUtjml3^4t~P(RUaF-|FR7d}GtrV#mMa=-'
 'h4WVNAy0ZCdA(jKEV;eDvYok3LZS$xyqPL;+j(iMgV8BYK+^94;m^lTv-n$eXJjC_`;8wF$-'
 'AdT8+}%FwJnST+U>3ayeU)Uzu7;iu3PjZZCvMCynD6|`S-7`pNuNgJ`aSxjNj-'
 '702&l##%N=}gnDxo$yANH^)$i$tZwQ|GqsPGW<|^|&G<C?EzM-'
 '6zU*J<uh^F4E(Ip5G#T}lN(O#a9*yU5GTZ!p&c$_xNgeIhMz5`xmMcFS%O6m{v*(*Td2=kR=n%jB5;?^*(swS3JW48riIE&<_pA=K`D5d#x}-'
 '0X^A|7j&jx%O>^_r=a4ARlbTYyfYOQC{m$?X=Km0|3V(WqTPC4tKjMDs>4-'
 'JqryGQ5o5NDBpX<+3;1N6H5&cLQI6g4=BAw8{qWT2?RJ?d<O7sjhNTwx|E&AEub2tWn@qF?z?D=CpEt}g%Bfb7cIZSD0cD(*YdroKTyVj_X(0M'
 '!?Xz^JRPPn|z1=Es!qM{WhGJ(fFKfGk`3R|g7UhWd<(&#S@5%Epe|;ZHbcaMd%ChPQ`BTF=;1*-'
 '0riX_=L@Bp}3Mi|~4_>M;=^8(Z9MUiz6kl0w$51fxNbv$NQlO=z=W*?PewrR{1azH}Yqp5X5-TxaQQGS-'
 'oesdJ%4`swc&2QlJ0FBK|+1z5hy%UGx9scnnEOBu~{{*N;m{dIJxg1s!u)MA{}m!RRC#8r1GR$dc-EkgPy{IAeGrZ$`-'
 'c8v6pc6ErEXLVL*mH8(mWy%o#YsoCTmhIVY^b-'
 'FM+^{a{+is*iRo_y5x_M*2q&u9xlUFaEeA@}U{E=!qFWtJ>wgmq`ft4rswLKSbttfILf@1rT>lcqf6uRm`0--M~Zp%Lw0phifToyE&rtn4B68L'
 'KipZ{9I=D(h>_-`lz;o+CeltOh}l!W}tLahL$4*z!0vbFjl`col&#!K-*dQi<Kk3;n(|KeAxCFshQ75RbZM`l15f?T>nDJTa6-'
 'E}eDz_;j%c^F1!<oO}BB%A{7-'
 'R6;C$W5Rs0TW7AF{mdxu&W&eUWi$89h>eMF<Bh$KqiafE|iMYecODYCCWoqO=#ozO(UQygSO|nzG=~wEz5Hwx?t@1W*CNnt?wo_lC`wT)r`uTH'
 'zq0$8*SMZ^wvRc@XCr)8Qq0b*8S3WL4Q6N+nhr8@09PkS(hs+>1y4yUOcgz<gU9DZY7FcKhOR<I^2HKup^sp3R4z~$aE?HjO}2q>7uvCmpr}Dr'
 '0bWK>v)3FzxZ?sG4!0kF+;pI&Cm_3$h1u&DPR7IObcS?xuLOgry*HgF0<ZIIwudPyf`{Iet&U(Kq+uJ?JY%~UR|7@$e7pm+4)s_|LSW0`0VIHP'
 'lhWKZ9SF9^2rpfvU$C=JBthLv$sGcXy7_2SK_j2f-gF;9nP~=bDaaHn_Hs3lwXPGmF560&+*w6@IB%<-'
 'b(akp;meKeim2PrdmQrQljNEecrlK;GjTTWmeNcx_LTCO48ln&m^iLDg@JZHR`j@t6de@Hd86jWSjN)={&dZYG$)acCyZ2%uV*^|MC9-7PCnJ'
)
OUTPUT_PINS={'c32_catalogue.json': [240929, 'efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d'], 'joint_frontier.json': [10444324, '4ddd4d8f8b33c502ceedb617ab7f1c75c5dd3b22dbca0d30a6235ef991df9e93'], 'quotient_frontier.json': [9498762, '95911c6144747036ed4095f6ba035baf205b195fbf757f97718068379b4806f9'], 'physical_cut_control.json': [11453, 'e4354cb415d916e1985c0e529ba71297802e4ae2f8c478d5cdebd38376c10944'], 'literal_intersection.json': [9513727, 'a7cbd09b84862ee646cc9ce269c97dcd246c4624082c96f86545bae78baa54db'], 'geometric_frontier.json': [11728807, '9e01776fe87d26c08dbd52c13f3d9e316d861770f69e978b1babdbd8bf8d4a4b'], 'terminal_mass_exact.json': [5494, '599c40ce062ed7a00c8373e326cda2703f305f511504ff1dd90609be5fb02033'], 'one_body_control.json': [61676, '84826677794ed40c22dc17525b0f0b87469c53a1a472d82bed6f9c3ce7a708d3'], 'physical_domain_check.json': [278, 'a01d4e916ed53da7c13c4915b8a9954f9b7bca1e3c07e32a006ec2d0be51f01c'], 'relaxation_control.json': [334, 'b36b8c748af13003cf90a978fbf341dc0b85c6837256ae21d1fad3db8b4f27f7'], 'domain_1_0.smt2': [100082, '9b5fe891c7c0931e6f6aebe1c1fab284813bbcc12e423ce9e491e6c4045ecc13']}
raw=zlib.decompress(base64.b85decode(DATA));assert pin(raw)==RAW_PIN
sources=json.loads(raw);assert len(sources)==8
root=Path('lynx99_recovery');root.mkdir(exist_ok=True)
manifest={}
for name,text in sorted(sources.items()):
 p=Path(name);assert p.name==name and not p.is_absolute()
 b=text.encode('utf8');manifest[name]=pin(b);p=root/name
 if p.exists():assert p.read_bytes()==b,('SOURCE_CHANGED',name)
 p.write_bytes(b)
b=(json.dumps(manifest,sort_keys=True,separators=(',',':'))+'\n').encode()
(root/'source_manifest.json').write_bytes(b)
print('EIGHT_COMPLETE_SOURCES_AND_LITERAL_INTEGER_CERTIFICATE_EXTRACTED',*RAW_PIN,flush=True)
print('SOURCE_MANIFEST',*pin(b),flush=True)
mode=sys.argv[1] if len(sys.argv)>1 else 'extract'
assert mode in ('extract','build','check')
if mode!='extract':
 assert len(sys.argv)==3
 journal=str(Path(sys.argv[2]).resolve());env=dict(os.environ,PYTHONHASHSEED='271828')
 tasks=[['intersect_frontier.py',journal,mode],['geometric_projection.py'],['terminal_mass_exact.py'],
  ['verify_candidate.py','--control'],['physical_domain.py','--check'],
  ['relaxation_control.py','literal_intersection.json'],['corner_no_gain.py'],['middle_incidence_no_gain.py']]
 for task in tasks:
  r=subprocess.run([sys.executable,'-S',*task],cwd=root,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  (root/(task[0]+'.log')).write_bytes(r.stdout)
  print(r.stdout.decode('utf8'),end='',flush=True)
  assert r.returncode==0,('SUBPROCESS_FAILED',task,r.returncode)
 r=subprocess.run([sys.executable,'-S','physical_domain.py','1','0'],cwd=root,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 assert r.returncode==0,r.stderr.decode('utf8')
 (root/'domain_1_0.smt2').write_bytes(r.stdout)
 for name,expected in OUTPUT_PINS.items():assert pin((root/name).read_bytes())==expected,('OUTPUT_CHANGED',name)
 print('LYNX99_COMPLETE_INTERSECTION_PHYSICAL_REFINEMENT_AND_RECOVERY_PASS',flush=True)
print('RECOVERY_SOURCE',*pin(Path(__file__).read_bytes()),flush=True)
```
