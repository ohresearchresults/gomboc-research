# minimum-0031

AI research report · 2026-09-09 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# RAVEN24 — recovered whole72 and new whole178 exclusions

## Determination

**Both requested whole-realization determinations are complete.**

**Recovered theorem — `RAVEN24_C32_TYPE72_ALL_ROOTS_EXCLUSION_V1`.** Every bounded, full-dimensional convex realization of the actual canonical C32 type72 maximal-face lattice has at least two strict unstable vertices at its own uniform-volume centroid, for every positive-definite physical metric. I recovered and executed the literal late source, reproduced its frozen integer proof and report, and completed its independent scalar, Bareiss/Sylvester and Fraction-LDL checks. All **22,194 rooted trees**, **4,860 matrix records**, and **40,660 positive-definite blocks** are covered.

**New theorem — `RAVEN24_C32_TYPE178_ALL_ROOTS_EXCLUSION_V1`.** The same assertion holds for the genuinely distinct balanced heptagonal type178. Its complete proof covers **24,003 rooted trees**, using **4,482 stored rational records**, **38,293 stored positive-definite blocks**, and **71,171 all-root block checks** after the exact order-two automorphism is applied. All **81 labeled joint-root pairs**, representing **42 joint-root orbits**, are excluded. The unresolved realization/root complement within type178 is **empty**.

These are exclusions, not attainers. The inherited bracket **32 ≤ C_min ≤ 1374** is unchanged; this work does not re-audit the separate certificates establishing that bracket, prove V≥10, or exclude every C32 type.

## 1. Authority and the resolved recovery boundary

The literal immutable parent is `minimum-0028`, compact UTF-8 v2 envelope **55,093 bytes**, SHA-256 `5f6eaed3622219fa7396da4a238658123f1197ce0928671209939a632cd5f954`. It is **`RAVEN24_C32_TYPE72_U4_EXCLUSION_V1`**, closing only canonical U4 and its nine stable-root choices. Its 161 records and 1,188 per-fan-occurrence blocks must not be relabeled as an all-root result. The supplied literal parent states this restriction explicitly.

The late all72 source is a separate extension, previously preserved in the journal rather than immutably published. Its complete proof bytes now reproduce, including the original 12,174-byte recovery wrapper. The increment over the literal parent is exactly canonical U roots `{0,1,2,3,5,6,7,8}` and their **72 labeled joint-root pairs**. The new representation also rechecks U4 with **1,157 distinct physical-tetrahedron blocks**, rather than the parent's 1,188 fan-occurrence blocks; these are different certificates, not inconsistent counts. The late source already distinguished these representations.

I authenticated the supplied current journal as **3,106,034 bytes**, SHA-256 `3b68fd6e90de488da5c8e427ffffb003ff9974616e8232f635a3f82fdd9ea251`, recovered the parent envelope with its terminal Markdown LF, and obtained the stated parent hash. No literal-parent identity conflict was found. The older source-research journal does not contain the late all72 capsule; the current attached journal does. The historical all72 ZIP itself was not recovered; the newly packaged archive below has a distinct identity. This does not leave any proof coefficient or helper missing.

The final combined capsule was executed from a fresh directory, not merely extracted. Its final success marker was observed, stderr was empty, and both standalone exact-verifier logs matched their frozen hashes. Separate fresh-directory runs of the original all72 capsule and the new178 chosen-plan generator also reproduced byte-identical integer proofs and reports.

## 2. Actual incidences and complete root maps

In both types, `(V,E,F)=(9,16,9)` and `C=32`. A compact digit string below denotes the complete ordered cycle, not a triangulated face. The positions in each canonical facet list are the stable-facet indices `0` through `8`.

### Type72

```text
normal-to-canonical = (3,0,2,6,7,8,5,1,4)
normal facets       = 2654301;1782;087;710;803;834;845;856;862
canonical facets    = 013;0241;0367852;143;254;346;458;476;487
normal true edges   = 01,03,07,08,12,17,26,28,34,38,45,48,56,58,68,78
canonical true edges= 01,02,03,13,14,24,25,34,36,45,46,47,48,58,67,78
```

Here `w=normal0=canonical3`, `a=normal7=canonical1`, and `b=normal8=canonical4`. The fixed-quarter edge is **w–b**, normal08/canonical34, not a–b. The automorphism group is trivial. These maps and actual cycles agree with the literal parent and recovered whole72 source.

### Type178

```text
normal-to-canonical = (5,1,4,0,2,8,7,3,6)
normal facets       = 2650431;1782;087;713;734;740;805;856;862
canonical facets    = 013;0258741;032;1463;235;365;476;568;678
normal true edges   = 04,05,07,08,12,13,17,26,28,34,37,47,56,58,68,78
canonical true edges= 01,02,03,13,14,23,25,35,36,46,47,56,58,67,68,78
normal involution   = (0,2,1,6,5,4,3,8,7)
canonical involution= (7,4,8,6,1,5,3,0,2)
facet involution    = (6,1,8,3,7,5,0,4,2)
```

The type178 incidence and normal map are inherited literal geometry; their complete graph, face-cycle automorphism group and induced facet permutation were newly checked.

Its canonical vertex-root orbits are `{5}`, `{0,7}`, `{1,4}`, `{2,8}`, `{3,6}`. Stored normal representatives are `(0,1,3,4,7)`, corresponding to canonical `(5,1,0,2,3)`. Nevertheless, **all nine** rooted tree lists are independently enumerated, and every target-root matrix is checked after explicit permutation. The relabeled physical source fan is used; it is not silently replaced by a different minimum-label target fan.

For both types the complete excluded labeled set is exactly

`{0,1,2,3,4,5,6,7,8} × {0,1,2,3,4,5,6,7,8}`,

with unstable vertex first and canonical facet index second. Type178's 42 lexicographic orbit representatives are exactly

`({0,1,2,3} × {0,1,2,3,4,5,6,7,8}) ∪ ({5} × {0,1,2,3,4,5})`.

The report materializes all 81 pairs and all 42 representatives. No polarity or mechanical duality is used.

## 3. One actual solid, not separately centered caps

For context, the balanced type178 chart has

```text
w=p0=(1,0,0), u=p1=(0,0,0), v=p2=(0,1,0),
a=p7=(0,0,1), b=p8=(0,beta,t),
p3,p4,p5,p6=(arbitrary planar x, arbitrary planar y,0),
Achain=(1,3,4,0), Bchain=(0,5,6,2).
```

Require `beta>0`, `t>0`, `beta+t-1>0`, strict convexity of the base, and **all** actual nonincidence supporting inequalities. One physical affine map is used, with `G=TᵀT` positive definite. If `L,R` are the twice-areas of the two planar caps and `M_L,M_R` their shoelace first-moment numerators, embedded with zero z component, the genuine common-volume formula is

```text
D0=beta+t
D=D0+L+t*R
N0=D0*(w+b)+t*v+beta*a
N=N0+L*a+M_L+t*R*b+t*M_R
g=N/(4*D)
Vol_physical=sqrt(det(G))*D/6.
```

Here `M_L=3L*area_centroid(left cap)`, and analogously on the right. This is one five-vertex core plus two actual cap pyramids with disjoint interiors; there are no independently chosen masses or centers. In particular, `t=1` is not divided away. These coupled identities are the source's physical formulas.

The exclusion proof is stronger in scope than reliance on this chart: it starts with an **arbitrary actual convex realization of the stated face lattice** and its genuine vertex-apex decompositions.

Let `g` be its own volume centroid, `x_i=p_i-g`, and let X contain these nine rows. For an arbitrary SPD metric G, put `A=XGXᵀ`. Then A is nonzero PSD. The centroid is strictly interior because the volume integral of each supporting slack is strictly positive.

For any vertex apex, triangulate every maximal facet not containing that apex and cone each triangle to it. These positive-volume tetrahedra partition the same P up to measure-zero boundaries. If an unordered tetrahedron T occurs in several chosen decompositions, assign it the **single actual mass** `m_T=Vol(T)/Vol(P)>0`. Its determinant and denominator are the same in every occurrence.

Let `chi_T` be its nine-entry incidence vector and `H_T=chi_T chi_Tᵀ+diag(chi_T)`. Every chosen fan F_a satisfies

```text
sum(T in F_a) m_T = 1
Xᵀ sum(T in F_a) m_T chi_T = 0
sum(T in F_a) m_T <H_T,A> = 20 E_P[||x||_G²].
```

Indeed a uniform tetrahedron has `E[lambda_i]=1/4` and `E[lambda_i lambda_j]=(1+delta_ij)/20`, giving its vertex-sum centroid and the displayed second-moment matrix. Thus all fans share the same zeroth, first and second moments of **one solid at one centroid**. This is the recovered all72 mechanism, extended here to multiple triangulations at the same apex.

Only necessary identities of the **actual determinant masses** are used. I do not assert that arbitrary degree-two-moment-matched weights must be uniform or physically realizable.

### Exact physical type178 control

The new verifier reconstructs the complete supporting hull of the literal equal-height overhang

```text
0=(1,0,0)
1=(0,0,0)
2=(0,1,0)
3=(1/3,-1/18,0)
4=(2/3,-1/18,0)
5=(13/18,7/18,0)
6=(7/18,13/18,0)
7=(0,-30,1)
8=(0,70,1).
```

It obtains `Vol=911/54` and `g=(49253/196776,3965153/393552,1811/3644)`. Independent boundary-cone integration and **all 96 genuine apex-fan decompositions** agree exactly on mass, all three first moments and the full second-moment matrix, before and after translation by the same g. Identical tetrahedra also have explicitly compared equal determinant masses.

Vertex 4 is the unique farthest base vertex but has the positive escape product `2143515235/7083936` toward apex 7. Thus the old farthest-base shortcut cannot be restored. The coordinates and this countercontrol originate in the attached geometry result; the 96-fan second-moment replay is new.

## 4. Complete proof mechanism

### Weak escape trees include every possible sole strict unstable root

A vertex i is strict unstable precisely when `x_iᵀG(x_j-x_i)<0` for every true neighbor j: true edge directions generate its full tangent cone. If i is not strict unstable, select a true neighbor p(i) with the weak reverse inequality. Even when that product is zero,

`||x_p(i)||_G²-||x_i||_G² = 2 x_iᵀG(x_p(i)-x_i)+||x_p(i)-x_i||_G² > 0`.

Therefore these arrows cannot cycle. If r were the only strict unstable vertex, the other eight choices would form a spanning tree directed to r. Conversely, a global squared-norm maximum is always strict unstable, because its product toward any distinct neighbor is at most `-||x_j-x_i||_G²/2<0`. Excluding all sole roots therefore proves **at least two strict unstable vertices**, not merely failure of an assumed U=1 generic chamber.

For each root, the verifier compares every connected eight-edge subset of the sixteen true edges against an independently generated list of adjacent parent tuples without cycles. A root-deleted integer Laplacian determinant supplies a third count: **2,466 trees per root for72**, **2,667 for178**. The all178 automorphism bijections are checked on these complete lists. Triangulation diagonals never become escape edges.

### Exact projection branches

The common chain bounds are

`B=(0,0,1/8,1/4,89/256,27/64,1/2,27/50,29/50)`.

For each m from 2 through 8, the complete rational multiplier row in the source verifies the scalar PSD form

`B_m*y0²+y0*ym+sum(i=1..m) lambda_i*(yi²-yi*y(i-1)) >= 0`,

with all multipliers nonnegative. Applying this coordinatewise to a weak escape chain gives `<x_root,x_i>_G >= -B_depth(i)*||x_root||_G²`. The root's own bound is1. An exact recursion considers every polygon triangulation and accepts only when each tetrahedral vertex-sum projection is strictly positive, contradicting its positive-volume average being zero.

If the root has one tree-child c, project onto x_c instead: both c and the root have bound 1, while other depths decrease by one. The same exact recursion applies. Every accepted tetrahedral-sum gap is at least **1/32**. The seven multiplier rows, PSD verification and complete triangulation recursion are in the capsule, not numerical estimates.

### Shared-tetrahedron PD certificates

For each nonroot set `S_i=e_i e_iᵀ-sym(e_i,e_p(i))`, where `sym(u,v)=(uvᵀ+vuᵀ)/2`. Then `<S_i,A>≤0` for a weak escape tree.

A record gives rational vectors gamma_a, symmetric K_a, scalars tau_a and nonnegative lambda_Ti, with `sum_a K_a=0` and `sum_a tau_a=0`. For every **distinct** tetrahedron in the union it proves

```text
Q_T = sum(a:T in F_a) [sym(gamma_a,chi_T)+K_a+tau_a*H_T]
      + sum(i != root) lambda_Ti*S_i
Q_T-I9/2 is positive definite.
```

Weight by the genuine m_T and pair with A. The resulting sum is strictly positive because A is nonzero PSD. But the gamma terms vanish by the common centered first moments; K terms cancel using unit mass of each complete fan; tau terms cancel using the one common second moment. What remains is `sum(T,i) m_T lambda_Ti <S_i,A>≤0`, contradiction.

The checker forms every integer matrix `2*den*Q_T-den*I9` twice: once by the symmetric-matrix formula and once by independent scalar-monomial accumulation. They must agree entrywise. Integer Bareiss/Sylvester then proves every leading principal minor positive. Separately, Fraction LDL reconstructs its pivots and verifies that each cumulative pivot product equals the corresponding Bareiss minor. Every multiplier sign and all cancellation identities are exact. The checker does not import the numerical generator.

## 5. Whole72 coverage actually recovered

Each row covers all 2,466 trees. Shared counts include two- and three-fan records; block counts are distinct physical tetrahedra.

| Canonical U | Normal U | Root projection | Child projection | Single fan | Shared | PD blocks |
|---:|---:|---:|---:|---:|---:|---:|
|0|1|1453|393|532|88|4247|
|1|7|1525|466|299|176|5804|
|2|2|1447|394|458|167|4798|
|3, w|0|1758|234|401|73|3263|
|4, b|8|2247|58|129|32|1157|
|5|6|1475|328|475|188|5714|
|6|3|1615|349|332|170|4581|
|7|4|1412|423|468|163|5270|
|8|5|1321|436|564|145|5826|
|Total||14253|3081|3658|1202|40660|

The 4,860 records comprise 3,658 single-fan, 1,197 two-fan and five three-fan records; 1,195 use nonzero second-moment coefficients. The five triple plans, in normal labels and zero-based lexicographic tree ordinals, are `(2,734,(2,1,6))`, `(2,1100,(2,1,6))`, `(3,2,(3,0,4))`, `(3,909,(3,0,4))`, `(3,1368,(3,0,4))`. These recovered counts match the late source and its frozen report.

## 6. New whole178 coverage and the decisive advance

I used standard single- and two-fan certificate location, then allowed alternative triangulations of actual facets and multiple complete fans from the same apex. A failed locator was never counted as an exclusion. The final frozen proof contains exactly the following eight representative-tree records with nonstandard triangulations; all remaining records use standard fans.

```text
normal root, tree ordinal, complete parent tuple, successful plan
1,2069,(8,1,1,1,0,6,2,4,5),26 cyclic fans
1,2214,(8,1,1,1,7,6,2,0,5),26 cyclic fans
4,583, (4,3,1,7,4,6,2,4,5),26 cyclic fans
4,591, (4,3,1,7,4,6,8,4,2),fans [4,61]
4,600, (4,3,1,7,4,8,2,4,6),26 cyclic fans
4,607, (4,3,1,7,4,8,5,4,2),fans [4,61]
4,995, (4,7,1,4,4,6,2,3,5),26 cyclic fans
4,1020,(4,7,1,4,4,8,2,3,6),26 cyclic fans
```

The source generates all 96 distinct vertex-apex fans: two each at normal apices 0,3,4,5,6; one each at 1,2; 42 each at 7,8. Each nonincident polygon is triangulated recursively, with boundary/internal edge multiplicities checked. The first nine IDs are standard minimum-label fans at apices 0 through 8; remaining distinct fans are sorted lexicographically by their sorted unordered tetrahedra. This is the complete deterministic fan-index definition.

The 26 cyclic-fan IDs are exactly

```text
(0,1,2,3,4,5,6,7,8,10,23,26,32,36,41,45,49,61,63,64,75,77,79,89,90,95).
```

For a 26-fan record put the root fan first and then the other IDs in that displayed order. Their union contains 72 distinct physical tetrahedra. Fan 61 is the following genuine apex 7 decomposition:

```text
(0,4,5,7),(0,5,7,8),(1,2,4,7),(1,3,4,7),
(2,4,6,7),(2,6,7,8),(4,5,6,7),(5,6,7,8).
```

Thus the extra freedom is in **actual decompositions of the same solid**, not in separate mass distributions or additional physical shape sampling. Six records close with the 26-fan identity; two close with the alternate single companion. Their eight automorphic partners are also checked, so no exceptional tree survives.

| Canonical U | Normal U | Source normal root | Root projection | Child projection | Single fan | Shared | PD block checks |
|---:|---:|---:|---:|---:|---:|---:|---:|
|0|3|3|901|563|917|286|9962|
|1|1|1|1234|372|717|344|8413|
|2|4|4|1215|499|642|311|8796|
|3|7|7|1843|207|458|159|5707|
|4|2|1|1234|372|717|344|8413|
|5, w|0|0|1799|220|371|277|5415|
|6|8|7|1843|207|458|159|5707|
|7|6|3|901|563|917|286|9962|
|8|5|4|1215|499|642|311|8796|
|Total|||12185|3502|5839|2477|71171|

Each row sums to 2,667 in its four tree-count columns. The five representative roots have 13,335 cases: 6,992 root-projection, 1,861 child-projection and 4,482 matrix cases. Stored records are 3,105 single-fan, 1,371 two-fan and six 26-fan records, containing 430,337 integer coefficient entries. Their denominator histogram is `{1:3580,2:809,4:90,16:3}`; 1,374 stored records use nonzero second-moment coefficients. All-root checking performs 71,171 matrix checks and 640,539 matching positive leading-minor checks.

## 7. Exact record semantics and regeneration boundary

A record is `[normal_root,tree_ordinal,fan_ids,den,z]`. Every integer in z is divided by the positive den. Its order is: nine gamma entries per selected fan; eight nonnegative shadow multipliers per distinct tetrahedron, with nonroots in ascending normal-label order; 45 upper-triangular entries for each of the first `number_of_fans-1` K matrices; then that many tau scalars. The last K and tau are exact negative sums. Distinct tetrahedra and parent tuples are sorted lexicographically. This fixes every coefficient's meaning without a hidden checkpoint.

The complete 72 plan is 4,860 bytes, SHA-256 `47203739824bec01bad0faa51f2091c26152c97507b14bf751fff884beb1f239`: ascending normal roots, then tree ordinals, skipping exactly the two projection branches. Code 0 selects the root fan; codes 1–9 add apex `code-1`; 10 adds apices 0,4; 11 adds 1,6.

The complete 178 plan is 4,482 bytes, SHA-256 `7f4d5fa91ef3ed7fd644c5d0aac7dd91389a8f00745448b9832e4e8a5666cfe3`: representative normal roots `(0,1,3,4,7)`, then tree ordinals, skipping the projection branches. Code 0 selects the root fan; codes 1–96 add fan `code-1`; 255 selects the 26-fan order above. Both full plans are losslessly embedded in the recovered numerical source.

**Coefficient location is not proof checking.** The deterministic generator starts at the zero coefficient vector, uses an analytic gradient and L-BFGS-B to minimize half the sum of squared eigenvalue deficits below 1, then rounds onto denominators `(1,2,4,16,256,65536)`. It imposes nonnegativity only on shadow multipliers. Explicit options are `maxiter=1800`, `ftol=1e-15`, `gtol=1e-10`, `maxls=40`, `maxcor=40`. Numerical filters 0.65 and 1e-5 only select attempted exact certificates; the integer PD gate is authoritative. The documented optimizer limits are stopping conditions, not infeasibility certificates.

Actually used and replayed: **CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OpenBLAS0.3.30/SkylakeX, XZ/liblzma5.8.1**, assertions enabled, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, four independent worker processes. The environment is set before child-process startup. No random seed or optimizer checkpoint is an input.

Byte-identical numerical regeneration is pinned to this stack. A different numerical backend may fail the frozen hash gate; that is **UNKNOWN reproduction**, not a substitute coefficient array or a new mathematical exclusion. Once the frozen integer proof exists, both exact verifiers require only the Python standard library. These are independently constructed scalar formulas, arithmetic algorithms and tree enumerations executed in this work, not a claim of external human peer review.

## 8. Frozen byte identities and observed markers

All following source, proof, report and transcript identities were actually reproduced in the final fresh-directory capsule replay.

| Item | Bytes | SHA-256 |
|---|---:|---|
|recover_raven24_72_178.py|20209|db7b6c6b65e1cd1b2693690c8be0ec078b7d51cdd862429938bffccd9ffb609c|
|recover_type72_all.py|12174|13be96a1c854cb6eef80303e6d5db9d87278562d548149ac6842447e87aa0382|
|verify72.py|13938|f9ce44ffb0e5775790ef7447123a9d5dce9119ac08d3c40cb5e0e41c5f604f98|
|reconstruct72.py|6365|0c4856e31e8af212db57fe73ee6e6a4cdc7d89e7ad2f7dd19683c2a77a65a24e|
|type72_certificate.json|1787659|603075514b92108152767740de970ed3678e9c327418ea85dc6ee24914c95fbb|
|type72_certificate.report.json|2942|eba2aa51823b7edb038a905c1a67683e938f9d0751c57125aba657ab6e79a0a7|
|verify178.py|17754|043583a90c61fcc3d477104cfc4819c7030593e407aed6c98868ec8e90249814|
|reconstruct178.py|6099|57858a311bda89c06d1c60e524ed7b43896e8832316fd45dd0e4c25139971f64|
|type178_certificate.json|1841048|bfbc2493b2d945ae35d2b07d357ee0f2a2f1b7452556137f3e4183e00b6745de|
|type178_certificate.report.json|4900|cea4db75adba6ce62bcfe8e944235fdf96629e883e1e2b3c3d55213579d0b115|
|verify72.txt|2818|af7e09e1bb882218a7a7dfe5db440616f46af3b76edfa6c399a4584f356d0339|
|verify178.txt|3247|f239f2001486adc80baba3e8d991c1ca0814c54337e90198059231f3282c8e4f|
|combined replay.txt|16023|27bfcf0355faff4307ca7a5df5f0f651fed9f7d9e2bf6127f092cf5271418aa2|

The separately executed literal all72 wrapper also reproduced its original **5,785-byte** replay SHA-256 `88cbcc7c598731928892072671548d6177bcf1f520a07787afa65408c87c669f`. The larger combined log above is intentionally a different transcript. The original late source's corresponding frozen identities agree.

The following markers are **expected and actually observed**; each whole-root marker is accompanied by all nine root reports:


[Encoded source block omitted; the code in this passage is incomplete.]


The optional supplied-journal authentication was also executed and printed `LITERAL_PARTIAL72_PARENT_ENVELOPE_AND_SOURCE_AUTHENTICATED_PASS`.

## 9. Complete recovery capsule

Save the complete following Python block as `recover_raven24_72_178.py`, UTF-8/LF with a final LF. It contains every helper, both complete discrete plans, both exact verifiers, both coefficient generators and the original late72 wrapper template. There is no omitted parent artifact or proof-data download.

In an empty directory with the stated numerical dependencies:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python recover_raven24_72_178.py > replay.txt
python -S verify72.py type72_certificate.json > verify72.txt
python -S verify178.py type178_certificate.json > verify178.txt
```

For source inspection without generation, use `python -S recover_raven24_72_178.py --extract`. Extraction alone is not a proof replay. The optional `--journal PATH` authenticates exactly the supplied current journal and literal parent; the default mathematical replay does not require it.


[Encoded source block omitted; the code in this passage is incomplete.]


## 10. Scope and continuation

There is no unclosed shape, overhang, height-order, equal-height, norm-tie, weak-escape or SPD-conditioning region **within either actual type72 or actual type178**. Stable and saddle features need not be generic. A singular metric, zero-volume body or incidence-changing limit is outside the stated actual type; all nondegenerate realizations arbitrarily close to such limits remain covered. No claim about a different limiting incidence is smuggled into this statement.

No attainer or mesh is supplied, because the result is an exclusion. Type186, the other remaining C32 types, and their polar types are not closed by this handoff. In particular, type178 does not close type191 by polarity, and the results of the independent MP9, quad-ten and217 branches are not assumed here.

The useful continuation is to retire **both complete types72 and178** and apply the now-reconstructible shared-tetrahedron certificate to genuinely unclosed graphs or roots, allowing multiple actual facet triangulations before introducing weaker free-mass surrogates. The critical new capability is 26 complete decompositions with common determinant masses and cancelling second moments, not another bounded physical or metric sample.

### Supplementary artifacts

New 24-member exact proof/source/log archive (`RAVEN24_TYPES72_178_EXACT_RECOVERY.zip`) — **1,715,674 bytes**, SHA-256 `6442e494b99887a968461385578c8539765d6e7e128361e37dabfa8b8e67fd4b`. Its members were read back and compared byte-for-byte with the manifest after packaging.

Verification receipt (`RAVEN24_TYPES72_178_VERIFICATION_RECEIPT.json`) — **4,467 bytes**, SHA-256 `48cfb2f5b39c4cd84e31bd7dacf9480e1d11f54a274cbeddaa79271564ffc42e`. Recovery source (`recover_raven24_72_178.py`) and the same self-contained Markdown handoff (`RAVEN24_TYPES72_178_RESULT.md`) are conveniences; the complete inline capsule is the durable source authority.
