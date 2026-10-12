# minimum-0052

AI research report · 2026-09-11 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

**Result.** I obtained **36 new complete physical joint-root exclusions in canonical C32 type 1**, removing **204 graph domains and 70 matching branches**. The exact remaining frontier is **95 canonical types, 4,337 joint-root orbits, 27,688 graph orbits, and 7,848 matching branches**. Canonical1 now has only **four roots, 26 graph domains, and four matching branches**. No additional whole type is closed, and no universal facet-number lower bound is claimed.

There are two additional facet-side results: a sharp actual-edge second-moment inequality applying to all sixteen strict matching edges, coupled to the body's actual common volume covariance; and a simultaneous actual-vertex facet Loewner inequality rejecting all seven counterfeit prism side blocks from the previous parent, including the version passing signed Loewner cap 2.

The successful root exclusions use actual tetrahedral-fan volume and centroid identities with signed true-edge inequalities. Their success does **not** require a new second-moment assumption. The edge/covariance theorem is a separate necessary physical obstruction.

**Authority and literal intersection.** The exact source-bearing input is research-journal(20260911-093142).md, 4,038,860 bytes, SHA-256 62e00f309cafece2f1ad7070b56304086c3edd0b202b030e1c0666eefd0e9b63. The parents are:

- Bright: minimum-0046, SHA-256 9107ca2a331bcf1600b8876c5d64643efee0fc82da507e19dcd4c043b7c0aee5.
- Nimble: minimum-0045, declared SHA-256 c82384226f8c3c55830961f5991a2d11e0c64173cd0da666e5dbb97471d8bfdd.
- Quiet: minimum-0047, SHA-256 347418089174031ed0b8b897e3103b2b0b3a9d5655c8d4f9252f22195e1abed9.

Bright's compact JSON envelope authenticates as 64,458 bytes with its declared hash; Quiet's authenticates as 33,540 bytes with its declared hash. **There is a Nimble envelope-rendering discrepancy:** wrapping the displayed Markdown with one final LF in the same compact JSON envelope gives 50,028 bytes and SHA-256 46bdc6f1c95bc9bd98de488bdf08b714ea70a64b9b3a1f733692d9ded3fd91e3, rather than the declared identifier. No semantic, label, incidence, or sign conflict was found. Nimble's complete embedded recovery source authenticates as 27,269 bytes/SHA-256 56b10360b46a590a0934dad7c3586b2cf8874ddce2fcbc06b25e672ce30106ca; its decoded source package and both reproduced frontier outputs match their published pins. I use those literal authenticated sources and report the envelope discrepancy without inventing missing bytes.

The literal intersection and final update are:

| Stage | Types | Joint roots | Graphs | Matching branches |
|---|---:|---:|---:|---:|
| Nimble prefilter | 180 | 8,382 | 54,769 | 15,357 |
| Literal whole201 intersection | 95 | 4,373 | 27,892 | 7,918 |
| After new physical certificates | 95 | 4,337 | 27,688 | 7,848 |

The exact root partition is

\[
21682=14504_{\rm whole201}+18_{\rm old\ partial}+2787_{\rm additional\ G55}+36_{\rm new}+4337_{\rm remaining}.
\]

Bright's 7,178 preliminary roots split as 18+2787+4373 before the new exclusions. The whole201 filter removes 4,009 roots, 26,877 graphs, and 7,439 branches from Nimble's prefilter. On the remaining 95 types, inherited geometric projection removes 536 of 28,428 pre-projection graphs: 280 primal-to-pole and 256 pole-to-primal cuts. These are literal intersections.

There were 745 single-graph complete roots at the first intersection. Excluding reserved canonical73/285, the smallest was canonical1/U4/S5, whose complete surviving cover was original domain96. Its first exact certificate closed that root and eleven additional graph domains. Extending the same construction produced 37 distinct certificates. I did not regenerate the old TREE281 or whole201 exclusion coefficients.

**Precise continuous exclusion theorem.** Let P be an actual full-dimensional homogeneous convex polyhedron with canonical1's maximal facets:

~~~text
[[0,1,3],[0,2,4,1],[0,3,5,2],[1,4,6,3],[2,5,7,4],
 [3,6,5],[4,7,8,6],[5,6,8],[5,8,7]]
~~~

Its sixteen true edges are:

~~~text
[[0,1],[0,2],[0,3],[1,3],[1,4],[2,4],[2,5],[3,5],
 [3,6],[4,6],[4,7],[5,6],[5,7],[5,8],[6,8],[7,8]]
~~~

Use this body's own volume centroid, one SPD physical metric M and its reciprocal N=M⁻¹, the genuine support poles, all incidences and strict nonincidences, and the parent's complete strict matching condition. Here U is the unstable-vertex root and S the stable-facet root. The following 36 joint roots are impossible throughout the complete continuous physical domain:

| U | Newly excluded S |
|---:|---|
|0|1, 3, 4, 6, 7, 8|
|1|4|
|2|7, 8|
|3|1, 6, 7, 8|
|4|0, 1, 2, 5, 7, 8|
|5|8|
|6|0, 2, 8|
|7|0, 1, 4, 5, 6, 7, 8|
|8|1, 2, 3, 4, 6, 8|

This covers every affine realization and allowed metric, hence the full parent 21-variable domain: fifteen free vertex coordinates and six metric entries after fixing four affine-gauge vertices. Its actual centroid, genuine facets, all 144 unequal primal/pole shadow signs, and all sixteen strict matching escapes are retained. No independently chosen covariance or facet block substitutes for a physical quantity. The polar need not be volume-centred.

**Certificate proof.** In each recorded broom labeling let Gᵢⱼ=xᵢᵀMxⱼ. Then G is nonzero PSD. A genuine vertex-apex fan cones triangulated nonincident facets into positive-volume tetrahedra. If δₜ=Vol(Tₜ)/Vol(P) and χₜ is the four-vertex indicator, each actual fan satisfies

\[
\sum_t\delta_t=1,\qquad
\sum_t\delta_t\sum_{v\in t}x_v=4\operatorname{centroid}(P)=0.
\]

For a valid signed primitive sDᵢⱼ≥0, with Dᵢⱼ=xᵢᵀM(xⱼ−xᵢ), define

\[
S_{ij}^{s}=s(2e_ie_i^T-e_ie_j^T-e_je_i^T).
\]

Its contraction with G is −2sDᵢⱼ≤0. Each certificate supplies g₀,g₁, a symmetric cancellation multiplier H, and nonnegative integer λₐₜₗ satisfying

\[
Q_{at}=g_a\chi_t^T+\chi_tg_a^T+(-1)^aH+\sum_l\lambda_{atl}S_l,
\qquad Q_{at}-I\succ0.
\]

Pair with the actual G, weight by actual δₜ, and sum over both fans. Actual centroid terms vanish, H cancels because both fan masses equal one, and every signed-shadow contribution is nonpositive. The sum is therefore at most zero. But every Qₐₜ is greater than I and G is nonzero PSD, so every summand is strictly positive: contradiction. H is a certificate multiplier, not a physical facet-area moment.

The embedded package verifies **37 certificates, 591 nine-by-nine blocks and 5,319 positive leading minors of Q−I**, with independent matrix expansion, integer Bareiss and rational LDL checks. Every coefficient, representative original domain, broom map, signed true-edge form, incidence and all sixteen selected matching escapes is embedded. All accepted records use ordinary two-fan identities; the optional covariance branch in the verifier is unused.

The updater applies each verified positive/negative mask predicate to every original surviving domain, then recomputes branches and roots from survivors. A root is removed only when its entire cover is gone. The certificates themselves allow equality in all selected signs. The inherited full-root perturbation theorem covers unused-shadow equality strata while preserving the sixteen strict matching escapes. Thus these are complete-root exclusions, not exclusions of selected interiors.

**Exact residual cases.** Canonical1 has trivial vertex and facet automorphism groups. Its only remaining roots are:

| Root | Original domain indices | Graphs | Branches | Actual stable facet |
|---|---|---:|---:|---|
| U3/S3 | 175,176,177,178 | 4 | 1 | [1,4,6,3] |
| U4/S3 | 70,71,72,73 | 4 | 1 | [1,4,6,3] |
| U7/S2 | 152,153,154,155,156,157,158,159,160 | 9 | 1 | [0,3,5,2] |
| U7/S3 | 114,115,116,117,118,119,120,121,122 | 9 | 1 | [1,4,6,3] |

Their strict primal parent arrays, paired with S, are:

~~~text
([1,3,0,3,2,8,3,4,7],3)
([2,0,4,1,4,8,3,4,6],3)
([2,0,4,1,7,3,5,7,7],2)
([2,0,4,1,7,6,3,7,7],3)
~~~

Each has exactly eight nonnegative primal arrows, all strict. The 26 states differ through optional pole arrows, with one fixed strict eight-arrow pole matching per root. The complete residual source embedded below contains every literal mask and both parent arrays. The full frontier reconstruction retains all 95 types and every root, graph, strict mask, incidence and branch. The other 94 types have exactly their inherited filtered frontiers. The complete 95-ID list is the literal REMAINING array in the recovered source. No TREE ordinal was renamed as a canonical C32 ID.

Outside reserved canonical73/285, the next smallest individual complete roots are canonical2/U2/S3, U2/S5, U5/S5 and U7/S5, each with one domain and one branch. Canonical1 is now the smallest whole-type workload.

**Sharp actual-edge second-moment obstruction.** For a genuine edge with endpoints u,v and adjoining actual facet poles qᵢ,qⱼ, retain all four cross-incidences qᵢᵀu=qᵢᵀv=qⱼᵀu=qⱼᵀv=1 and the same reciprocal metric pair. Define actual uniform-segment moments

\[
U_e=(u^TMu+v^TMv+u^TMv)/3,
\quad V_e=(q_i^TNq_i+q_j^TNq_j+q_i^TNq_j)/3,
\]
\[
L_e^2=((v-u)^TM(v-u))((q_j-q_i)^TN(q_j-q_i)).
\]

If any of the four directed primal/pole endpoint escapes on this edge is strictly positive, then

\[
\boxed{U_eV_e>(1+L_e/6)^2.}
\]

This holds on **all sixteen edges simultaneously** in every parent strict matching domain. The other primitives may be negative, zero or unused positive primitives.

For the proof set m=(u+v)/2, h=(v−u)/2, n=(qᵢ+qⱼ)/2 and k=(qⱼ−qᵢ)/2. Transform primal vectors by M¹ᐟ² and pole vectors by M⁻¹ᐟ². Actual cross-incidences give n·m=1 and n·h=k·m=k·h=0. In three dimensions choose orthogonal coordinates

\[
h=He_1,\quad k=Ke_2,\quad m=aHe_1+ce_3,\quad n=bKe_2+c^{-1}e_3.
\]

Here H,K>0 and c≠0. A strict owner implies a²>1 or b²>1. Genuine interval variances give

\[
U_e=c^2+H^2(a^2+1/3),\qquad V_e=c^{-2}+K^2(b^2+1/3).
\]

AM–GM gives

\[
U_eV_e\ge\left(1+HK\sqrt{(a^2+1/3)(b^2+1/3)}\right)^2
>(1+(2/3)HK)^2=(1+L_e/6)^2.
\]

Weak ownership gives the non-strict version. No polar-centroid assumption is used.

The local coefficient 1/6 is sharp even for homogeneous tetrahedra at their own volume centroid. Put a=1+ε, ε>0, and take

~~~text
(a−1,0,1), (a+1,0,1), (−a,−2,−1), (−a,2,−1),
M=diag(1,1,2), N=diag(1,1,1/2).
~~~

The centroid is zero, volume is 8/3, and the two poles adjoining the first edge are (0,−1,1),(0,1,1). On it Dᵤᵥ=2ε>0, Uₑ=a²+7/3, Vₑ=5/6 and Lₑ=4. Thus UₑVₑ−25/9=(5/6)(a²−1) tends to zero. Every larger universal local coefficient fails. The exact control uses ε=1/1024, checks every actual support, centroid, covariance and edge quadrature, and explicitly refutes 1/6+1/1000. This is a sharp local control, not a C32 or strict110 example.

**Actual common-covariance coupling.** Let cᵢ,Sᵢ be the genuine facet area centroid and covariance, Σ the original body's actual volume covariance, and dᵢ=Aᵢ/(Vol(P)‖qᵢ‖). For e=Fᵢ∩Fⱼ define actual area fractions and the parent's actual edge factor

\[
\rho_{i,e}=\operatorname{Area}\operatorname{conv}(c_i,e)/A_i,\qquad
\eta_e=\operatorname{length}(e)/(\operatorname{Vol}(P)\|q_i\times q_j\|).
\]

Using the same endpoints in both facets, define

\[
\beta_e=(d_i\rho_{i,e}+d_j\rho_{j,e})/3
=\eta_e[(1-q_j^Tc_i)+(1-q_i^Tc_j)]/6>0.
\]

These actual weights satisfy

\[
\sum_e\beta_e=1,\qquad \sum_e\beta_e(u_e+v_e)/2=0,
\]
\[
\boxed{\sum_e\beta_e\mathbb E_e(xx^T)
=\frac{10}{3}\Sigma-\frac13\sum_i d_ic_ic_i^T
=\frac53\Sigma+\frac13\sum_i d_iS_i.}
\]

Proof: actual centroid-fan triangle integration on each facet gives

\[
\sum_{e\subset F_i}\rho_{i,e}\mathbb E_e(xx^T)=2S_i+c_ic_i^T.
\]

The genuine edge-height identity is ηₑ(1−qⱼᵀcᵢ)=2dᵢρᵢₑ. Actual coning from the original volume centroid gives Σdᵢ=3, Σdᵢcᵢ=0 and Σdᵢ(Sᵢ+cᵢcᵢᵀ)=5Σ. Summing proves the claimed identities.

Consequently all sixteen strict owners imply the continuous physical obstruction

\[
\boxed{\frac53\operatorname{tr}(M\Sigma)+\frac13\sum_i d_i\operatorname{tr}(MS_i)
>\sum_e\beta_e\frac{(1+L_e/6)^2}{V_e}
\ge\frac{(1+\frac16\sum_e\beta_eL_e)^2}{\sum_e\beta_eV_e}.}
\]

The last step is weighted Cauchy–Schwarz. Equality or reversal of the first inequality excludes the stated physical sector, including unused-shadow equalities. No sharpness claim is made for the summed inequality.

There is an exact polynomial insertion into the unchanged 21-variable domain. With its centred X, normals nᵢ, positive supports hᵢ and qᵢ=nᵢ/hᵢ, put

\[
R=\det(M)h_i^2h_j^2,
\]
\[
C=(X_u^TMX_u+X_v^TMX_v+X_u^TMX_v)
\cdot(h_j^2n_i^T\operatorname{adj}(M)n_i+h_i^2n_j^T\operatorname{adj}(M)n_j+h_ih_jn_i^T\operatorname{adj}(M)n_j),
\]
\[
E=((X_v-X_u)^TM(X_v-X_u))\cdot
((h_jn_i-h_in_j)^T\operatorname{adj}(M)(h_jn_i-h_in_j)),\quad B=4C-36R-E.
\]

Since R>0, the edge inequality is exactly **B>0 and B²−144RE>0**, because UₑVₑ=C/(9R) and Lₑ²=E/R. This supplies two polynomial consequences per genuine edge with no new variable or denominator-sign branch.

**Missing endpoint-to-facet coupling.** With actual slacks Y(x)=1−Qx and actual Kᵢ=dᵢE_Fᵢ(YYᵀ), every actual incident vertex v satisfies

\[
\boxed{K_i-\frac{d_i}{9}Y(v)Y(v)^T\succeq0.}
\]

It is positive definite on the three-dimensional affine-slack space for a genuine nontriangular polygon; for a triangle it has rank two there. Equivalently (v−cᵢ)ᵀSᵢ⁺(v−cᵢ)≤8, strictly below 8 for a nontriangle.

For an affine function with triangle vertex values a,b,c, a complete proof is

\[
108(\mathbb E_Tf^2-a^2/9)=(2a+3b+3c)^2+(a+3b)^2+(a+3c)^2.
\]

Triangulate the actual polygon from v and average with actual positive areas. Equality would put every other vertex on one affine level line, impossible for a genuine polygon with at least four vertices unless the function vanishes on the facet. The scalar constant also follows from the parent's 9/8 theorem; the added value is simultaneous use of the **same actual vertex** across incident facets.

For the counterfeit prism sides, the affine raw moment is diag(1,1/6,1/3), versus actual diag(1,1/3,1/3). For the actual vertex a=(1,1,1) and z=(1,6,3),

\[
z^T(9B_{\rm fake}-aa^T)z=-10,\qquad \det(9B_{\rm fake}-aa^T)=-9/2.
\]

With actual dᵢ=2/7, the original K residual is −20/63. Thus all seven fake sides fail the actual-vertex test despite their surviving global flux and cap-2 properties. The complete rational checker is embedded below.

**Uncertainty and continuation.** No certificate is supplied for the four residual type1 roots. Additional apex fans and actual common volume second-moment equalities were explored without another accepted exact certificate; these numerical failures establish no feasibility claim. Every retained exclusion is reproduced by exact integer verification independently of numerical discovery.

The most focused physical continuation is now the four type1 roots: all stable facets are quadrilaterals, each primal strict matching is fixed, and only 26 optional pole-shadow strata remain. Enforce actual edge-to-facet relations, shared-vertex Loewner constraints and all sixteen polynomial edge-product gates in the unchanged one-body domain. Independent PSD facet blocks do not determine actual edge moments; independent metrics lose the reciprocal cross-incidence normal form; fitted edge weights lose the actual common-covariance identity. Relaxation feasibility remains insufficient for physical realization.

**Complete recovery capsules.** The two source blocks below contain all continuation-critical data and all required helpers. The first contains every coefficient and the complete exact verifier, losslessly encoded. The second contains all five complete method sources: literal frontier recovery, certified updater, standalone literal26-domain recovery, sharp edge-moment control, and fake-side endpoint control. No new coefficient download is required.

Use CPython 3.12.14, standard library only, assertions enabled. The frontier rebuild uses eight deterministic map-part jobs and PYTHONHASHSEED=271828, without regenerating inherited exclusion coefficients. Save the two sources with UTF-8/LF and final LF, then run:

~~~text
python -S recover_quiet93_methods.py 'research-journal(20260911-093142).md' canonical1_sweep_final.py quiet93_run
~~~

This verifies the exact journal input, reconstructs all pinned parent checkpoints, verifies the certificate before applying cuts, rebuilds the final frontier, checks every field of the independent literal26-domain reconstruction against it, and runs both moment controls. With no arguments the methods capsule only extracts its five source files. The complete command was executed from an empty output directory and passed.

| Normative object | Bytes | SHA-256 |
|---|---:|---|
| canonical1_sweep_final.py | 22894 | e7dfcfbbead2527568341751c037df7e75a80cdaf383e64e27286132cb5c11b6 |
| recover_quiet93_methods.py | 15115 | af9717aaa4425361eb3442c7c68dc4790d6b6836c2948eac7eab30c928d76f31 |
| frontier95.json | 6064232 | a7ac1caf3c9d526fb01f61db521e66f7f579bc5b293d2c952dc358fc97b70a3a |
| canonical1_sweep.json | 345890 | 94f6bca08878a2fda6afa4af8980ae14b7f1dd035714d381234368b1c94f85ab |
| frontier_after_certificates.json | 6129660 | b6f53aeeff426f030ba23fe28dc8835c9243b4f52e0a9e9d47ddd9490e39653a |
| canonical1_residual26.json | 6114 | 551152dbb61d78f978ed6104c7934bfb4880f84eb758646ec2da1721cd13a8ce |
| edge_product.json | 1070 | 1e0db9bb1340ec7e35bc1860d18fb8bf4fc6a94a06949138097adc236b7860ad |

The certificate additionally authenticates its complete 3,957-byte verifier source and 53,355-byte coefficient JSON through the literal pins in the capsule. The methods package authenticates each complete recovered source individually.

Expected principal markers, all observed:

~~~text
NIMBLE_RENDERED_ENVELOPE_DIFFERS_DECLARED_ID_SOURCE_CAPSULE_PIN_MATCHES
LITERAL_WHOLE201_GEOMETRIC_INTERSECTION_PASS 95 4373 27892 7918
CANONICAL1_SIGNED_TRUE_EDGE_FAN_SWEEP_EXACT_PASS
CERTIFICATES 37 BLOCKS 591 MINORS 5319
ALL16_STRICT_TRUE_EDGE_MATCHING_ESCAPES_RETAINED_PER_DOMAIN
EXACT_PHYSICAL_CERTIFICATE_PACKAGE_FRONTIER_UPDATE_PASS
REMAINING 95 4337 27688 7848
NEW_WHOLE_TYPES []
REMOVED_GRAPH_COUNT 204 REMOVED_MATCHING_BRANCH_COUNT 70
CANONICAL1_FOUR_ROOTS_26_DOMAINS_4_MATCHINGS_EXACT_RECONSTRUCTION_PASS
OWN_CENTROID_RECIPROCAL_METRIC_TRUE_EDGE_PRODUCT_SHARPNESS_PASS
ACTUAL_SHARED_EDGE_QUADRATURE_COMMON_VOLUME_COVARIANCE_PASS
ACTUAL_SHARED_VERTEX_REJECTS_FAKE_SIDE_PASS -10 -9/2 -20/63
QUIET93_36_PHYSICAL_ROOT_EXCLUSIONS_RECOVERY_PASS 95 4337 27688 7848
~~~

The updater saves the certificate's own output in final95/certificate_check.log; running canonical1_sweep_final.py directly prints its certificate markers.

**Complete source: canonical1_sweep_final.py.**

~~~python
"""CANONICAL1_SIGNED_TRUE_EDGE_FAN_SWEEP_V1. CPython3.12.14, stdlib only.
Run python -S canonical1_sweep_final.py. Full source and coefficient tables
are embedded losslessly; exact verification uses no numerical libraries.
Parents: Bright minimum-0046
9107ca2a331bcf1600b8876c5d64643efee0fc82da507e19dcd4c043b7c0aee5;
Nimble minimum-0045
c82384226f8c3c55830961f5991a2d11e0c64173cd0da666e5dbb97471d8bfdd;
Quiet minimum-0047
347418089174031ed0b8b897e3103b2b0b3a9d5655c8d4f9252f22195e1abed9.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,lzma,base64,struct
assert __debug__
FACETS=[[0,1,3],[0,2,4,1],[0,3,5,2],[1,4,6,3],[2,5,7,4],[3,6,5],[4,7,8,6],[5,6,8],[5,8,7]]
PAYLOAD_PIN=[45314, 'a62e1ea86b29dd2cac2c0a0e18aedc8b5cbc44ddc2fe76fcdeb9dbae891509e4']
CODE_PIN=[3957, '1ef47da877f72dec717b72424302fbea1d25285126b259bb5ecd818e802cb02f']
DATA_PIN=[53355, 'bb9132135f6a1343dd72498e3deb38bbd3aca6c279099c4af66b7126270deb96']
B64=(
'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'
)
payload=lzma.decompress(base64.b64decode(B64))
assert [len(payload),hashlib.sha256(payload).hexdigest()]==PAYLOAD_PIN
nm,nc,nz=struct.unpack('<III',payload[:12]);assert len(payload)==12+nm+nc+2*nz
DATA=json.loads(payload[12:12+nm]);code=payload[12+nm:12+nm+nc]
assert [len(code),hashlib.sha256(code).hexdigest()]==CODE_PIN
planes=payload[12+nm+nc:];packed=bytearray(2*nz)
packed[::2]=planes[:nz];packed[1::2]=planes[nz:]
zs=struct.unpack('<'+'h'*nz,packed);at=0
for r in DATA:n=r['z'];r['z']=list(zs[at:at+n]);at+=n
assert at==nz
raw=(json.dumps(DATA,sort_keys=True,separators=(',',':'))+'\n').encode()
assert [len(raw),hashlib.sha256(raw).hexdigest()]==DATA_PIN
exec(compile(code,'<embedded exact verifier>','exec'),globals())
~~~

**Complete source: recover_quiet93_methods.py.**

~~~python
"""QUIET93 complete recovery: 36 physical joint-root exclusions and edge moments.
CPython3.12.14, standard library, assertions enabled; no network or optimizer.
Usage: python -S recover_quiet93_methods.py JOURNAL.md CERTIFICATE.py OUTPUT_DIR
All five method sources are embedded; the complete pinned certificate is input.
With no arguments, extract the five sources to quiet93_recovery only.
"""
from pathlib import Path
import base64,lzma,hashlib,json,subprocess,sys
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
RAW_PIN=[23080, 'a92dc54a3af806dbc00f17bd28e31c83148307f5ea3534fe8c6e507fa9a0602f']
OUTPUT_PINS={'parent95/frontier95.json': [6064232, 'a7ac1caf3c9d526fb01f61db521e66f7f579bc5b293d2c952dc358fc97b70a3a'], 'final95/canonical1_sweep.json': [345890, '94f6bca08878a2fda6afa4af8980ae14b7f1dd035714d381234368b1c94f85ab'], 'final95/frontier_after_certificates.json': [6129660, 'b6f53aeeff426f030ba23fe28dc8835c9243b4f52e0a9e9d47ddd9490e39653a'], 'canonical1_residual26.json': [6114, '551152dbb61d78f978ed6104c7934bfb4880f84eb758646ec2da1721cd13a8ce'], 'edge_product.json': [1070, '1e0db9bb1340ec7e35bc1860d18fb8bf4fc6a94a06949138097adc236b7860ad']}
DATA=(
'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'
)
raw=lzma.decompress(base64.b64decode(DATA));assert pin(raw)==RAW_PIN
package=json.loads(raw)
out=Path(sys.argv[3] if len(sys.argv)>3 else 'quiet93_recovery').resolve();out.mkdir(exist_ok=True)
for name,item in package.items():
 assert Path(name).name==name
 b=item['source'].encode();assert pin(b)==item['pin'];(out/name).write_bytes(b)
print('FIVE_COMPLETE_PINNED_METHOD_SOURCE_UNITS_RECOVERED',flush=True)
if len(sys.argv)>1:
 certificate=Path(sys.argv[2]).read_bytes()
 assert pin(certificate)==[22894,'e7dfcfbbead2527568341751c037df7e75a80cdaf383e64e27286132cb5c11b6']
 (out/'canonical1_sweep_final.py').write_bytes(certificate)
 journal=Path(sys.argv[1]).resolve()
 assert pin(journal.read_bytes())==[4038860,'62e00f309cafece2f1ad7070b56304086c3edd0b202b030e1c0666eefd0e9b63']
 jobs=[['recover_frontier93.py',str(journal),'parent95'],['apply_final_certificates.py','parent95/frontier95.json','canonical1_sweep_final.py','final95'],['canonical1_residual26.py'],['edge_product.py'],['fake_vertex_check.py']]
 for args in jobs:
  p=subprocess.run([sys.executable,'-S',*args],cwd=out,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  (out/(args[0]+'.log')).write_bytes(p.stdout)
  assert p.returncode==0,(args,p.stdout.decode())
  print(p.stdout.decode(),end='',flush=True)
 for name,expected in OUTPUT_PINS.items():assert pin((out/name).read_bytes())==expected
 final=json.loads((out/'final95/frontier_after_certificates.json').read_bytes())
 residual=json.loads((out/'canonical1_residual26.json').read_bytes())
 actual=next(r for r in final['maps'] if r['id']==1)
 for key in ['facets','dual_facets','edges','automorphisms','facet_automorphisms','remaining_joint_roots','matching_branches','domains']:
  assert actual[key]==residual[key],key
 assert final['new_whole_types']==[]
 assert len(final['removed_joint_roots'])==36
 print('QUIET93_36_PHYSICAL_ROOT_EXCLUSIONS_RECOVERY_PASS 95 4337 27688 7848')
print('RECOVERY_SOURCE',*pin(Path(__file__).read_bytes()))
~~~
