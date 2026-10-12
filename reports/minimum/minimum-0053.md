# minimum-0053

AI research report · 2026-09-11 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

**Completed: a homogeneous whole-MP9:43 theorem, with 23 additional whole canonical C32 exclusions.** Relative to the fixed authoritative parent, the whole register increases from 201 to **224 of 296 types**, leaving **72**. The proof has **206 exact certificates, 5,454 integer blocks, and 49,086 positive leading principal minors in each of two arithmetic implementations**. All accepted certificates use only the eight base weak escapes. No norm or ratio hypothesis remains.

The authoritative parent is `minimum-0046`, SHA-256 `9107ca2a331bcf1600b8876c5d64643efee0fc82da507e19dcd4c043b7c0aee5`. I read the attached journal and reconstructed the immutable v2 result envelope exactly: 64,458 bytes with that SHA. The extracted Markdown requires its final LF before compact UTF-8 JSON serialization with keys `version`, `result_markdown`. Both embedded parent recovery-source pins and the complete `future3.json` pin also matched. No parent incidence or alias conflict was found. The inherited universal285 rooted-tree reduction and omitted-terminal-cell reduction remain accepted mathematical premises; they are not claimed as new results.

**Continuous theorem.** Let P be a full-dimensional homogeneous convex three-polytope whose nine distinct actual extreme vertices, labelled 0 through 8, admit the genuine coherently oriented boundary triangulation

```text
013 021 032 125 143 154 237 265 276 348 387 457 478 567
```

Triangles may belong to common polygonal maximal facets. At P's own uniform-volume centroid c, for every one common real SPD metric M, P has at least two strict unstable vertices. Vertex i is strictly unstable when `(v_i-c)^T M(v_j-v_i)<0` for every true-edge neighbor j. The theorem includes every vertex root, every genuine maximal-facet coarsening of this triangulation, all actual zero-volume cells, weak escape equalities, all norm ties and ratio endpoints, and arbitrarily ill-conditioned SPD metrics. Actual extreme vertices and a genuine boundary triangulation are hypotheses; arbitrary weak supporting inequalities on listed points do not suffice. Lower-dimensional bodies and singular metrics are outside the statement.

This is literal **MP9:43**, not canonical C32:43. The latter has the different maximal facets `013,0241,0352,143,25874,347,365,3786,568`.

Put `x_i=v_i-c` and `n_i=x_i^T M x_i`. A maximum of n_i is strictly unstable, including ties, because distinct vertices give `2 x_i^T M(x_j-x_i)=n_j-n_i-||x_j-x_i||_M^2<0`. If there were exactly one unstable vertex, every other vertex would have a true-edge weak escape i→p(i). Along each arrow,

```text
n_p(i)-n_i = 2 x_i^T M(x_p(i)-x_i) + ||x_p(i)-x_i||_M^2 > 0.
```

Thus the arrows form a rooted tree even on equality walls. The inherited reductions leave the long broom: b0 is the root, bj→b(j−1) for j=1,...,7, b8→b0, and terminal triple b5,b6,b7 occurs in the chosen genuine boundary triangulation. Enumerating triangulation-edge brooms is a safe superset of true-edge brooms on every coarsening.

The exact automorphisms, as images of vertices 0,...,8, are

```text
012345678 013254876 652741038 657214830 843751026 847315620
```

The root orbits are `{0,6,8}`, `{1,4,5}`, `{2,3,7}`. There are 1,236 labelled terminal brooms, partitioned freely into **206** automorphism orbits. The sorted representatives have root counts 54,80,72 at roots 0,1,2. The complete array is regenerated and pinned: **4,122 bytes**, SHA-256 `de7d5a2d72c9aa2c4f78fad709479151dc358447780e305ea75488e3c984654e`.

**The geometric strengthening is the full fourteen-dimensional cycle space.** MP43 has 66 distinct apex four-set cells. Its 84×66 signed boundary matrix has exact rank 52 and kernel dimension 14. The nine fan rows have rank 9, but their differences span only dimension 8. Copying MP49's eight-cycle conclusion to MP43 would lose six valid identities. Independent exact Fraction elimination and a 52×52 boundary minor of determinant −1 verify the rank without assumptions about geometric minor rank.

A compact geometric full basis consists of `f_a−f_8`, a=0,...,7, together with oriented four-simplex boundaries on these six five-sets:

```text
01234 01235 01237 12567 23478 23567
```

Their additional scalar identities in the single actual determinant table are

```text
 d0123 - d0124 - d0134 - d0234 + d1234 = 0
 d0123 - d0125 - d0135 - d0235 + d1235 = 0
 d0123 - d0127 - d0137 - d0237 + d1237 = 0
-d1256 + d1257 - d1267 - d1567 + d2567 = 0
 d2347 - d2348 - d2378 - d2478 + d3478 = 0
 d2356 - d2357 + d2367 - d2567 + d3567 = 0
```

Both this basis and the locator's deterministic integral RREF basis are completely reconstructed and verified by the capsule.

For every four-set t={a,b,c,d}, use the actual `d_t=|det(v_b-v_a,v_c-v_a,v_d-v_a)|`. This is one table on all 126 four-sets; each triangulation or fan selects from it. Put D=6Vol(P)>0, let X be the 9×3 centered vertex matrix, let χ_t indicate the four vertices, and put `J_t=χ_tχ_t^T+diag(χ_t)`. Actual uniform-simplex integration gives, for every apex fan f_a,

```text
sum_t f_at d_t = D,
X^T sum_t f_at d_t χ_t = 0,
sum_t f_at d_t X^T J_t X = 20 D Cov(P).
```

Every full formal-cycle row h gives the same equations with zero right sides. These are actual moments of the same homogeneous body and the same covariance, not independently fitted moments.

For completeness, all fourteen cycle directions have a direct geometric justification. Assign each sorted tetrahedron its fixed combinatorial orientation σ_t; every apex occurrence agrees. Genuine outward support implies `σ_t det(v_b-v_a,v_c-v_a,v_d-v_a)=d_t≥0`. If Rh=0 is its formal boundary equation, choose for a polynomial p the two-form `α=(integral_0^x1 p(s,x2,x3) ds) dx2∧dx3`. Stokes on the affine oriented tetrahedra gives `sum_t h_t integral_[σ_t t] p dx = integral_(Rh) α = 0`. Taking p of degree 0,1,2 in the same centered coordinates proves the required identities. Degenerate affine simplex maps are included; no determinant is divided out. Actual zero-volume columns therefore remain in the complete cycle ledger.

**Exact certificate contradiction.** Set `G=X M X^T`, a nonzero PSD matrix. The escape form `L_i=2e_i e_i^T−e_i e_p^T−e_p e_i^T` has `tr(G L_i)≤0`. Every integer block Q_t combines free first-moment terms, free symmetric matrices multiplying valid volume relations, common covariance terms, and nonnegative integer multiples of the eight escape forms. Independent scalar expansion checks the construction. Weighting with the actual d_t cancels all free terms, so the resulting contraction is nonpositive. Exact integer Bareiss and independent rational LDL both verify **Q_t−I is positive definite** for every block. At least one root-fan cell has positive actual mass, making that same weighted contraction strictly positive: a contradiction. Repeated cells in ordinary fans use the same determinant; shared and cycle cases identify the cell once.

The complete accepted cover is:

| Method | Certificates | Blocks | Representatives at roots 0 / 1 / 2 |
|---|---:|---:|---|
| Ordinary root/first-chain two-fan | 158 | 2,854 | 28 / 66 / 64 |
| Shared root/first-chain two-fan with common covariance | 12 | 224 | 8 / 2 / 2 |
| Root first-moment row plus all 14 full cycles | 36 | 2,376 | 18 / 12 / 6 |
| Total | 206 | 5,454 | 54 / 80 / 72 |

The 36 full-cycle indices in the pinned broom order are

```text
0,1,2,3,4,5,6,7,10,11,20,21,32,33,34,35,46,47,56,57,58,59,60,61,62,63,64,65,116,117,134,135,148,149,172,173
```

Shared indices are `9,29,31,43,45,49,51,53,55,73,136,174`; every other index is ordinary. Rounding power 10 is used at `1,2,3,4,5,7,10,11,20,32,33,34,35,46,57,59,60,61,63,65,116,117,135,148,149,173`; all other records use power 8. The verifier binds the complete ordered record set to regenerated brooms, roots, parent arrows, method, apex specification, source pins, and coefficient bytes. Unexpected record fields and all norm comparisons are rejected. No shadow or optional-arrow sign is accepted.

I tried ordinary two-fan, shared two-fan and then full-cycle certificates. A short norm-slot probe was subsumed by the completed unconditional cover. Numerical searches only proposed integer coefficients. Failed attempts are not infeasibility proofs, and the computation does not prove that the six extra cycles are necessary. The successful final method requires no norm slots or ratio subdivision; all such weak boundaries and endpoints are covered directly by the same certificates.

**Physical controls and checks of the actual coefficients.** The exact family

```text
V0=(0,0,0)       V1=(920,0,0)     V2=(340,376,-48+t)
V3=(0,920,0)     V4=(380,496,-35) V5=(460,368,-46)
V6=(365,428,-45) V7=(295,540,-38) V8=(225,652,-25)
```

has all fourteen triangles maximal at t=0. At t=1, triangles021 and125 form the genuine maximal quadrilateral0251, true edge12 disappears, and the only zero determinant among all126 four-sets is0125. All nine vertices remain extreme. The verifier enumerates supporting planes, reconstructs actual facet polygons, checks convexity and true edges, and retains all66 selected cells. These are identity controls, not witnesses satisfying the excluded escapes.

| t | Actual six-volume | Actual volume centroid |
|---:|---:|---|
|0|46783840|(66878495/203408,17200613/50852,−688113/50852)|
|1|46040480|(32950995/100088,4237741/12511,−1335579/100088)|

The example common metric is `[[5,1,2],[1,4,1],[2,1,6]]`, with leading minors5,19,97. All fan and full-cycle cancellations are also checked as 3×3 tensors before metric contraction. The final scope verifier expands **every accepted certificate on both actual fixtures**, subtracts its escape terms and verifies exact tensor cancellation: **412 checks**. Thus these checks use the actual coefficient records, one actual determinant table per body, each body's own centroid and covariance, and arbitrary common SPD contraction.

**Complete canonical transports.** Exhaustion of all12,912 genuine polygon refinements of the296 inherited canonical types finds69 MP43 refinements belonging to51 types. Exactly23 lie outside inherited whole201. Each row below gives literal canonical maximal facets, a permutation π mapping canonical vertices and unstable roots to MP43 labels, the zero-based owner facet of each displayed MP43 triangle, and the common orientation sign. Pull back by π^(-1) to recover each exact polygon triangulation. Oriented ear removal checks every disk; the16 true edges, five added diagonals and full actual-zero-cell ledger are checked separately. A joint root(r,f) maps to vertexπ(r) and the entire actual facet formed by the triangles owned by f. Every stable-facet choice is excluded because a sole unstable vertex is impossible.

```text
id|canonical facets|canonical vertices and roots to MP43|MP43 triangles to facet|orientation
63|013,0241,03652,14763,254,457,568,587,678|216057348|30213321286574|+
95|013,0241,03652,14873,254,376,456,468,678|012356784|01213324235786|+
106|013,0241,03652,1483,254,376,387,4568,678|012356784|01213324265787|+
109|013,0241,03652,1483,254,376,387,456,4678|012356784|01213324265887|+
129|013,0241,032,14763,23685,254,458,487,678|012356847|01213345434786|+
132|013,0241,032,1473,23685,254,376,4587,678|012356847|01213345464787|+
137|013,0241,032,1483,2365,254,376,387,45678|012356784|01213345476888|+
161|013,0241,0362,143,254,26785,3487,376,458|104238567|10321267648555|+
169|013,0241,03762,14873,254,265,456,468,678|012356784|01213324532786|+
174|013,0241,03762,1483,254,265,387,456,4678|012356784|01213324562887|+
188|013,025841,032,1473,235,365,376,487,5678|021364875|21014131356887|-
198|013,02541,032,1473,23685,376,457,587,678|021365874|21014431345786|-
200|013,025841,032,1473,2365,376,467,486,568|012346785|01213141435768|+
206|013,02541,032,1483,2365,376,387,4568,678|012356784|01213341465787|+
210|013,02541,0362,143,265,34786,457,568,587|206137584|30125512156784|-
214|013,02541,0362,143,2675,3476,458,487,578|104325876|01312156725448|-
223|013,02541,0362,1473,2675,376,458,487,578|104325876|01312136725448|-
226|013,02541,0362,14873,265,376,456,468,678|012356784|01213321435786|+
234|013,02541,0362,143,265,3487,376,458,5678|206137548|30125612157884|-
235|013,02541,0362,143,2675,3487,376,458,578|104325876|01312157526448|-
236|013,02541,0362,1483,265,376,387,4568,678|012356784|01213321465787|+
241|013,02541,0362,143,26785,348,376,387,458|104238567|10321256718444|+
255|013,02541,032,14763,236,2675,458,487,578|104325876|01312136743558|-
```

The23 additions contain1,719 joint vertex/maximal-facet root orbits. Wholly excluded types now contain16,223 of21,682 joint root orbits; the remaining72 contain5,459 **before intersection with inherited partial-root exclusions**. The1,719 are not asserted to have all been previously open individual roots. The exact remaining whole-type scope is

```text
1,2,5,6,8,9,11,18,20,25,36,38,41,48,50,51,52,53,54,56,57,58,60,61,62,65,68,73,75,84,92,97,112,113,114,115,116,117,121,123,126,130,131,133,134,135,142,145,148,151,160,176,177,179,181,182,185,186,187,189,190,191,193,196,197,207,211,229,240,249,266,285
```

There is no unresolved realization, root, genuine-cofacial, actual-flat-cell, weak-equality, norm, ratio or SPD stratum within the stated whole-MP43 theorem or its23 new whole canonical domains. This does not prove feasibility of any remaining type, a new global complexity lower bound, or an attaining example. The previous six-type physical targets already closed by MP49 are not reused as new exclusions.

The most useful continuation is to combine this exact delta with the independently active MP9:19 direction, preserving literal sphere identities and computing each sphere's full formal kernel. The pinned parent future3 generator, filtered by the new remaining72 in this capsule, gives **70 prospective MP19 types**, missing canonical73 and285, and **56 prospective MP38 types**, including285. These are combinatorial opportunities, not physical exclusions. MP43's canonical transport is exhausted. The short-leaf norm-slot and common-ratio machinery remains available for harder spheres; it is unnecessary here.

**Complete durable recovery capsule.** Fresh numerical reconstruction from the literal sphere and finite plan, without coefficient input, reproduced all206 records byte-for-byte. A separate standard-library-only frozen run passed, as did independent arithmetic/wrapper audits and the bundled scope/physical audit. The source below embeds all13 required source units: numerical and exact helpers, complete catalogue and transport generators, literal geometry controls, independent structure audit, the complete finite plan, and the scope verifier. No attachment, journal, coefficient download or external file is needed to reconstruct the new objects. Only the two explicitly stated inherited mathematical reductions remain premises.

Save the complete block as `recover_whole43.py`, UTF-8/LF with a final LF and assertions enabled. The tested build environment is CPython3.12.14, NumPy2.3.5, SciPy1.17.0, OpenBLAS0.3.30, Linux x86_64/glibc2.39. NumPy uses ILP64 BLAS and SciPy LP64. The wrapper sets `OPENBLAS_CORETYPE=SkylakeX`, `OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`, and `PYTHONHASHSEED=0`; four numerical workers execute the fixed plan. There is no random input. The locator uses `eps=1e-8,maxouter=14`; every remaining parameter is literal in the embedded complete sources. Floating calculations propose integers; byte drift or failed exact positivity is rejected.

```bash
python recover_whole43.py
python -S recover_whole43.py check
```

For extraction without reconstruction, use `python -S recover_whole43.py extract`. The frozen check requires only the standard library after the build has generated its records. Expected final markers are


[Encoded source block omitted; the code in this passage is incomplete.]


The wrapper is **32,934 bytes**, SHA-256 `26810caf418a188d47eee8ecc5c6bfec17939b2fe177e5bdd34019a317351890`. Its decoded13-source payload is81,462bytes, SHA-256 `c1960cc645ab3e082767ae71edcb6312bc59a4219e7ed830c41a795c67a0ed72`. Its complete individual-source manifest is1,237bytes, SHA-256 `1b70fa81cb12a55c71f4f1690b5639dffe5eb0b9bd027d11834662dbbe7bce73`. All206 per-case record pins and scalar hashes are reconstructed in the pinned whole report.

| Material exact object | Bytes | SHA-256 |
|---|---:|---|
|206 coefficient records|699540|6402688079e84132ccb8cf5bdd1af163238553dba281ced67f358803485b733b|
|206 sorted broom representatives|4122|de7d5a2d72c9aa2c4f78fad709479151dc358447780e305ea75488e3c984654e|
|Full signed structure and both cycle bases|19714|6dfd35cc993e0ec23db680b0295f1910c43ea53338ff4463b8f47a8a0954d954|
|Independent Fraction structure/broom audit|8649|0a6cbcb0218d9a4e443b2602bce72ff9c64adc549bb799defe4e8ff2c3fc9ff6|
|Complete canonical transport and root-subset ledger|83300|c0a67007293d76bafa0bd6400094f41ea09b63a4a22017a58a0a39516b9d91de|
|Literal23-map table|1747|3872737007399874f82ba119d707bd3a7d79bddc8ec0909fefe763d027442ece|
|Actual physical controls,126-cell tables and tensor moments|26533|061dfdc92613d9a67f81cc8f2e70a5576a32c045eae8c04aaa7002cda2f12bc1|
|Complete whole224 scope and per-case audit|38048|3851362231c6fdc8b7da1aa6965cd08b030ed5cb5895dafb58d4cbe563b80f16|
|Rebuilt inherited canonical296 catalogue|240929|efb10a4657a891cd13f6f62db94164bd4b3005e908dc55aae87db450930f704d|
|Rebuilt inherited future3 ledger|148643|c4ad2a6251069a01ee6e117b9621f033c5965740bc6502034f3694c38f335516|

A convenience copy is [recover_whole43.py](sandbox:/workspace/scratch/2d4a4bd60c77/recover_whole43.py). The full source below is the recovery authority; the link is supplementary.


[Encoded source block omitted; the code in this passage is incomplete.]
