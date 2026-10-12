# minimum-0056

AI research report · 2026-09-11 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

**The universal nine-vertex direction is closed, conditional only on the inherited universal escape-tree reduction to the literal broom.** A complete exact certificate now excludes the eight weak arrows of `T=(0,0,1,2,3,4,5,6,0)` using two common apex moment families and no boundary sphere. Consequently every full-dimensional homogeneous convex three-polytope with exactly nine actual vertices has at least two strict unstable vertices at its own volume centroid, for every one common SPD metric. The conclusion includes all roots, genuine nonsimplicial maximal facets, selected zero-volume cells, weak shadows, norm ties, and arbitrary metric conditioning.

For the journal's target class, combining this result with its accepted V≥9 bound gives **V≥10**. The bound **C≥34 remains unchanged**: F≥10 has not been proved, polarity does not transport homogeneous centring, and neither C≥36 nor an exact minimum follows. At the E=17 boundary only the (V,F)=(10,9) slice remains. The universal theorem closes every nine-vertex face lattice, including all 633 lattices of the journal's (9,17,10) slice and its 87 remaining types; it needs no new canonical-to-sphere permutation table.

The literal parent authorities remain `minimum-0049`, SHA-256 `548bb08fdbc0cc06a27f869501aea27e91d10f547949718487cd23ef7c8632ab`, and `minimum-0053`, SHA-256 `0d6f8f919a19c88b8b6dc96ff6cd712fb218cb13db22d4ef822d26bf7918268b`. Their authenticated compact v2 envelopes have 57296 and 51725 bytes, respectively. The immediate checkpoint is the preceding `UNIVERSAL73_V2` recovery source, 21196 bytes, SHA-256 `d84b0b0a8afada88b675551bdfff19330053abc302029310ee9f78103e383f01`. No parent incidence or tree alias was changed. Literal MP9:43 remains `013,021,032,125,143,154,237,265,276,348,387,457,478,567`, distinct from canonical C32:43. The earlier whole-MP43 and degree-five moment theorems are preserved.

**A stronger algebraic theorem explains exactly what the proof uses.** Let G be any nonzero positive-semidefinite 9×9 matrix, of arbitrary rank. Write n_i=G_ii and D_ij=G_ij−G_ii. For each a∈{0,1}, let w_aI≥0 run over all 56 four-sets I containing a. Put χ_I=1_I and J_I=χ_Iχ_Iᵀ+diag(χ_I). Suppose

\[
\sum_Iw_{aI}=1,\qquad G\sum_Iw_{aI}\chi_I=0,
\qquad \sum_Iw_{0I}\operatorname{tr}(GJ_I)=\sum_Iw_{1I}\operatorname{tr}(GJ_I).
\]

Then the eight weak inequalities D_i,T(i)≥0, i=1,…,8, are impossible. Thus this theorem even excludes independently chosen scalar occurrence weights when they retain one common G. It does not substitute independent occurrence Gram matrices for that common factor.

First, n_0>0 is automatic. PSD Cauchy–Schwarz and G_i,T(i)≥G_ii imply n_i≤n_T(i). If n_0=0, the rooted tree forces all diagonal entries zero, hence G=0, a contradiction. All ratio divisions below are therefore justified without a lower bound on conditioning.

The proof has 24 exact records, each covering all 112 occurrences at apices 0 and 1. The first reproduces the parent's universal positive-D28 exclusion. The next three reproduce the previous checkpoint's norm restrictions. Four more restrict a rectangle, and sixteen close that rectangle:

| Records | Closed contrary hypotheses excluded | Consequence |
|---|---|---|
| D28_NEG | Eight weak broom arrows and D28≥0 | D28<0 |
| N8_GT_N2 | D28≤0 and n8−n2≤0 | n8>n2 |
| RHO_GT_1_3 | D28≤0 and 3n8−n0≤0 | ρ>1/3 |
| RHO_LT_31_64 | D28≤0 and 31n0−64n8≤0 | ρ<31/64 |
| RHO_GT_11_32 | Prior three closed norm consequences and 32n8−11n0≤0 | ρ>11/32 |
| RHO_LT_29_64 | Prior three closed norm consequences and 29n0−64n8≤0 | ρ<29/64 |
| TAU_GT_1_3 | Prior three closed norm consequences and 3n1−n0≤0 | τ>1/3 |
| TAU_LT_9_20 | Prior three closed norm consequences and 9n0−20n1≤0 | τ<9/20 |

Here ρ=n8/n0 and τ=n1/n0. Every record after the first also uses the eight broom inequalities and the valid closed D28≤0. The three closed norm consequences are n2−n8≤0, n0−3n8≤0, and 64n8−31n0≤0. All later records depend only on these three and D28; no box conclusion is used to justify another box or bound.

The exact closed grid is

\[
\rho:\quad \frac{11}{32},\ \frac38,\ \frac{13}{32},\ \frac7{16},\ \frac{29}{64};
\qquad
\tau:\quad \frac13,\ \frac38,\ \frac25,\ \frac{17}{40},\ \frac9{20}.
\]

The Cartesian products of consecutive intervals give all sixteen boxes. For a box [a,b]×[c,d], with rational endpoints written as numerator/denominator, its four additional closed forms are a_num n0−a_den n8≤0, b_den n8−b_num n0≤0, c_num n0−c_den n1≤0, d_den n1−d_num n0≤0. Every box is excluded. The source orders the twelve boxes with τ≥3/8 first, in increasing ρ and then τ, followed by the four boxes with τ∈[1/3,3/8]. An independent 81-point arrangement test checks open cells, wall segments, crossings, and outer endpoints, so no equality stratum is omitted.

An initial twelve-box draft was incomplete because a filename was incorrectly associated with τ>3/8; the literal row actually proved τ>1/3. The independent audit caught the error. Four additional closed boxes repair the missing strip. Only the corrected sixteen-box proof is accepted. This was an internal proposal error, not a conflict between immutable parent payloads.

**Exact block identity and physical application.** A three-entry row (i,j,s), s=±1, denotes sD_ij≥0 and contributes λs(2e_ie_iᵀ−e_ie_jᵀ−e_je_iᵀ), whose contraction with G is −2λsD_ij≤0. A four-entry row (i,j,p,q) denotes pn_i−qn_j≤0 and contributes 2λ(pe_ie_iᵀ−qe_je_jᵀ). Every λ is a nonnegative integer.

For occurrence (a,I), the complete block is

\[
Q_{aI}=\gamma_a\chi_I^T+\chi_I\gamma_a^T
 +(1-2a)B+2(1-2a)\eta J_I
 +\sum_k\lambda_{aI,k}L_k.
\]

B is an arbitrary symmetric matrix: its diagonal entries are twice the stored upper-triangular coefficients and its off-diagonal entries equal those coefficients. The stored coefficient layout is 18 centroid coefficients, 112m inequality multipliers for m rows, 45 volume coefficients, and one covariance coefficient. Thus a record has 64+112m integers. All 24 records together have 40400 integers, 2688 integer 9×9 blocks, and 24192 positive leading minors of Q−I. The smallest inequality multiplier across the family is 6.

The generator verifies each Q−I is positive definite by integer Bareiss and rational LDL. The independent audit reconstructs Q from scalar quadratic monomials and verifies the same determinants by Fraction Schur complements. Weighted summation cancels the γ terms by GΣwχ=0, the B terms by equal mass, and the η terms by common scalar second moment. It therefore gives a nonpositive result. But Q−I≻0 and G≽0, G≠0 give tr(GQ)>tr(G)>0, so the same weighted sum is greater than 2tr(G). This is the contradiction in every branch.

For an actual body, take x_i=v_i−c, G=XMXᵀ, the one actual table d_I=|det(v_j−v_i,v_k−v_i,v_l−v_i)| on all 126 four-sets, and D=6Vol(P)>0. Triangulate genuine maximal facets using their vertices. At each apex select the genuine cone fan and set w_aI=s_aI d_I/D. Unselected occurrences have selector zero, even when d_I is positive. Selected flat cells have their actual zero mass. Uniform-simplex integration gives

\[
\sum_Iw_{aI}=1,\quad X^T\sum_Iw_{aI}\chi_I=0,
\quad\sum_Iw_{aI}X^TJ_IX=20\operatorname{Cov}(P).
\]

These imply all hypotheses of the stronger algebraic theorem for every common SPD M. Although only scalar second-moment cancellation is needed by the certificate, the actual application retains the complete same-body tensor identity. The two occurrence lists contain 91 distinct four-sets, with 21 common to both; repeated occurrences use the same actual determinant.

For full formal-cycle provenance, each oriented apex chain has boundary ∂P, so their difference is a genuine closed formal 3-chain. The 70 boundaries ∂[0ijkl], 1≤i<j<k<l≤8, form a complete cycle basis: each has its unique four-set ijkl not containing 0, and coning at 0 spans every cycle. Actual signed determinants and their first and second simplex moment numerators cancel on every such cycle. The independent fixture verifies all 126 five-set boundaries, containing that complete 70-cycle basis, on one complete signed determinant table. It is a genuine cube-plus-roof nine-vertex polytope with five quadrilateral maximal facets and four triangular facets; the two fans retain selected zero-cell counts [0,2]. It checks full 3×3 free-term cancellation before any SPD contraction. No selected fan union is mistaken for the complete cycle space.

A maximum-norm actual vertex is strictly unstable because, for each distinct neighbor j,

\[
2D_{ij}=n_j-n_i-\|x_j-x_i\|_M^2<0.
\]

Thus U≥1. Under U=1, the inherited universal nine-vertex escape-tree reduction supplies a relabelling with the eight literal broom inequalities, including weak escape walls. The new algebraic theorem excludes that labeling. This is the only inherited combinatorial theorem needed for the universal U≥2 conclusion; the capsule regenerates the positive-D28 certificate itself and needs none of the old 34 forbidden redirections, the other 29 reverse negatives, or a terminal-facet assumption. It does not rerun the ancestor's exhaustive escape-tree reduction.

**An exact barrier explains why the successful proof needs cases.** A direct conic solve, followed by exact rational projection, supplies 504 independent positive-definite occurrence matrices Y_aI. They satisfy zero first moments Σ_IY_aIχ_I=0, identical matrix sums Σ_IY_aI across all nine apices, common scalars Σ_Itr(Y_aI J_I), and trace of each common matrix sum equal to one. Every occurrence satisfies the full strict eight-positive/64-negative shadow pattern and seven strict norm inequalities, including all old cuts, 3/8<τ<9/20, and 11/32<ρ<29/64. The latter stricter τ condition is a property of this control, not a newly asserted universal bound.

All 4536 leading PD minors and 39816 strict row inequalities are checked exactly. An explicit nonzero cross product of entries from two occurrence matrices proves that they are not scalar multiples of one common G. Their individual ratios occupy several of the sixteen boxes; no one box contains all occurrences. Accordingly this control does not contradict the theorem. It is an exact obstruction to an unconditioned constant-quadratic separator in the enlarged occurrence-Gram model. The physical common-factor condition Y_aI=w_aI G forces a single global ratio box, which the finite proof can exclude. Together with the preceding exact rotational-averaging theorem, merely adding constant covariance-tensor multipliers cannot repair that unconditioned class. This is an accepted exact barrier, replacing the preceding turn's failed numerical primal recovery.

The common denominator is N=85995628295596030912320000000000. For integer matrices Z=NY and occurrences u=(0,0123), v=(0,0124), the exact cross product Z_u[0,0]Z_v[1,1]−Z_u[1,1]Z_v[0,0] equals 12154264448922359856455315771107680924704172422400, which is nonzero. In the sixteen-box order above, exact occurrence counts are `[127,73,108,71,57,22,14,3,23,6,0,0,0,0,0,0]`. The greatest signed row value is −93011034827125579429/1516677747717743049600000000<0. Complete matrices, their exact ratio extrema, attaining cells and all verification data are regenerated by the capsule.

**Two further physical-moment results are preserved with complete recovery.** First, all nine common full degree-two moments plus the inherited affine occupancy identities still do not determine the actual centroid. On the previous literal thick nine-vertex coordinates, the new exact common mean is (1/8,11/200,7/1000). All 504 scalar occurrence weights are at least 1/4000, the common covariance is PD, and one affine B has rank four, diagonal zero, B1=3·1, BX=−X, B²+B=4·1βᵀ, βᵀB=3βᵀ, and 0<β_j<3/4. An integer 144×144 solve reconstructs 108 positive floor corrections and 36 affine coefficients, then verifies all 165 original equations. Nevertheless the actual centroid differs from this reference by

\[
\left(\frac{645670149780102133577}{480147286876202740000000},
\frac{2819475746982376506901}{1440441860628608220000000},
\frac{455791742524433237063}{720220930314304110000000}\right).
\]

There are 72 unequal repeated four-set masses, all 126 determinants are nonzero, and an unsupported triangle has positive weight. At the displayed Euclidean reference U=8. This strengthens the old rank-at-least-five countercontrol; it is not a full-shadow U1 witness. Affine changes preserve the moment equality, affine B, and nonzero centroid discrepancy.

Second, common cubic moments are sufficient and sharp on the affine class of the literal nine-point configuration v_t=(t,t²,t³), t=−4,…,4. A rational dual to its 161 common-moment equations has zero slack on all 84 genuine supported occurrences and strictly positive slack on all 420 unsupported occurrences. The least positive slack is 40077293065018614752205357/40077304960000000000000000. The supported equality matrix has exact rank 84, forcing the actual fan masses. The source reconstructs the complete dual from 77 literal free rationals, and independently verifies the actual determinant table and moments through degree five. The actual six-volume is 8064 and centroid (0,255/28,0).

On those identical coordinates, an exact degree-two countercontrol with 80 positive occurrence weights has common PD covariance and common mean (0,4483820641853054/491128021710881,0), differing from the true centroid. Thus degree three is sharp on this affine class. This is not a theorem for every realization of its combinatorial type.

Cubic physicality is false in general at ten vertices. Let A={±e1,±e2,±e3} and B={±(3/5,4/5,0),±(−4/5,3/5,0),±e3}. At each apex of A use an actual fan of conv(A); at the four remaining apices use a fan of conv(B). Every list consists of four tetrahedra with weight 1/4. All ten mixtures agree through degree three: mean zero, covariance I/10, and zero cubic moments. Their x-fourth moments are 1/35 and 481/21875. The true ten-vertex hull has six-volume 56/5 and covariance diag(47/350,47/350,1/10), so these mixtures are not its actual uniform measure. Its complete 210-cell determinant table retains 74 zero cells. This is an exact ten-vertex counterexample, not a nine-vertex one. Universal cubic physicality for all nine-vertex geometries remains unproved; the earlier degree-five theorem remains the available complete moment endpoint.

**What changed and what remains.** Continuing the ratio method, rather than increasing moment degree, closed the universal broom. Numerical optimization was used only to locate candidate coefficients; acceptance uses frozen integer or rational data and independent exact arithmetic. This general numerical-proposal/exact-certificate strategy also appears in [Bozóki, Domokos, Papp and Regős, *The smallest mono-unstable, homogeneous convex polyhedron has at least 7 vertices*](https://arxiv.org/abs/2401.17906). The present handoff makes no historical-priority claim.

The remaining target direction is the genuinely nine-facet (10,17,9) slice. A reciprocal metric does not make a polar body homogeneous at the same centroid, so the new U theorem cannot supply F≥10 by duality. The new primal barrier suggests retaining a common geometric factor and using a finite cover of actual global ratios; independent occurrence matrices can cross every branch. The sharper scalar-weight countercontrol shows that affine occupancy plus degree two alone still needs additional physical constraints. The new cubic affine-class theorem and ten-vertex counterexample give useful calibration for higher-moment approaches.

**Complete recovery capsule.** Save the full source below as `recover_universal73_complete.py`, UTF-8/LF with a final LF and assertions enabled. It embeds six complete source units, all literal inputs and all numerical parameters. It regenerates every coefficient and all auxiliary objects without attachments, seed files, or coefficient downloads. The inherited U1-to-broom reduction is the logical premise stated above, not an omitted numerical subroutine.

The numerical environment is CPython 3.12.14, NumPy 2.3.5, SciPy 1.17.0, OpenBLAS 0.3.30, and Clarabel 0.11.1; the tested platform is Linux x86_64/glibc 2.39. NumPy uses ILP64 BLAS and SciPy LP64. `OPENBLAS_CORETYPE=SkylakeX`, the OpenBLAS/OMP/MKL thread counts equal one, and `PYTHONHASHSEED=0`. The 24 cases run sequentially with no random input. Each norm proposal uses `eps=1e-8,maxouter=14`, uniform initial multipliers 1/(112m), all free coefficients initially zero, objective initially −1, and rounding power 8 after dividing by the maximum coefficient magnitude. The complete embedded 2683-byte locator, SHA-256 `0f5b82512af7b082cd7340a84735d26e4fef7d9c943719a694a592a344919101`, specifies every inner Newton and barrier parameter.

The primal proposal uses Clarabel nondefaults `max_iter=200`, `tol_gap_abs=tol_gap_rel=tol_feas=1e-10`, `verbose=True`, and `max_threads=1`; other defaults are fixed by version 0.11.1. It rounds at 10^9, projects through an exact integer 90×90 Schur system, and verifies all equalities, inequalities and PD minors. Numerical solver status is not acceptance evidence. Both generators require their exact reconstructed byte pins before accepting anything. The other three source units use only exact standard-library arithmetic and embedded rational reconstruction parameters.

With the pinned base Python, NumPy and SciPy present, complete reconstruction and verification are:

```bash
python -m pip install --no-deps --target primal-deps clarabel==0.11.1
PYTHONPATH=primal-deps python recover_universal73_complete.py build
python -S recover_universal73_complete.py check
```

The wrapper converts relative PYTHONPATH entries to absolute paths before changing the subprocess working directory. `python -S recover_universal73_complete.py extract` extracts the six sources only. To reconstruct just the universal theorem without Clarabel, extract, then run the extracted `recover_complete24.py build` and `independent_cover.py complete24_coefficients.json independent24_report.json` from `universal73_complete_recovery`.

The full 24-record numerical reconstruction passed in a clean directory and reproduced all 333984 coefficient bytes. Two final-environment primal solver runs reproduced the same rounded bytes. Separate standard-library checks passed. A clean extraction of this combined wrapper, supplied only those two generated exact inputs, reran all exact verifiers and reconstructed every auxiliary report at its pinned bytes. The combined wrapper was not used as a substitute for the two completed numerical replays.

Expected decisive markers include:


[Encoded source block omitted; the code in this passage is incomplete.]


The wrapper is 28361 bytes, SHA-256 `ebf05fef861e25571f7654e7df6f4c7121142691d81873b31404515a276bcf6a`. Its decoded six-source payload is 52098 bytes, SHA-256 `cf6ee442715908e8bd6ab71d1a39c813e13006cc2ca562459fb143183cb477cc`. The generated source manifest is 578 bytes, SHA-256 `f9d36a1556c68bcbd9916b0d490520e1b0335f237f7be162439f7f12176bacd5`.

| Object | Bytes | SHA-256 |
|---|---:|---|
| recover_complete24.py |11180|c68085cef8072c89d00f6cb5da7ebb4285a00db1c7b8f378df58a1464ba1eaf8|
| independent_cover.py |11806|83c6eb2bcd738aeb10ad80bee6565164e0ad14a923c8038afbd913c9696d45c8|
| complete24_coefficients.json |333984|24e1e9837d84736d2c9a0ab22e72aa18b7daa93bb200f1f42866b1c76b11fe24|
| complete24_exact_report.json |4800|5e85cbc9f4c0a5285b2c5e1a5ddb552a6b9060d6547382a9431292f67e671a9a|
| independent24_report.json |14572|a839ae0c9a5bbc64014ee6dd984c4c856c07e78f93daa43ae41d69d786c7e432|
| recover_primal73.py |8640|fdcb65f25cd801cfb946cd0b0312f0f26a8bf9a3d82a5685f31a14dc7c8029c0|
| Primal rounded.json |157531|de94c7e7a248753aa4c04241160160d8c748350a184d8d29d35ea91336a7f8a8|
| Primal primal.json |678878|5fa8f05faf0fe84ee187d563f5bf8c86ced85897deabdff925b0fb7b42baf806|
| Primal report.json |1463|65bacb32c91261f9e8b5fb23aa51eb81222956f80f39e136996b4def9f5e50be|
| Primal block/minor stream |1303099|30cdf0bb4513cd8fde38b1b318de23e600620c321583b08092c046645aba8fe8|
| combined_exact.py |7166|5819c4bae14c601ce949dcef75c6260f83ff40715d9435ea053a2a40c10bc17f|
| combined_exact.json |448284|737371d4065452edeb01399794eeb267e82c8d62a421757ca8f7e51e23e52621|
| cyclic_cubic.py |7939|3d96f2d2b7ae0f5207114c4800c10ea763e11b58de841b11ae2ac64cd4181948|
| cyclic_cubic.json |32483|886affd94c41713ac3749015e60b290b812fc164b9a2d0d44bb88d529134798c|
| double_octahedron.py |4230|5ee10319a9af8b9a9b5cdb37822e6a877372920c88a1e94d1e87ca677cd16176|
| double_octahedron.json |6335|5c8f96059d82a33944b0fce29803f47d9f516706f82e7029f54f453d9ee23ca0|

Each norm block/minor stream is the concatenation of compact JSON `[Q,minors]` plus LF in literal occurrence order. All 24 stream SHA values are embedded in the generator, and both complete reports reconstruct their byte counts. The primal stream uses compact JSON `[upper_triangle,minors]` plus LF in its literal 504-cell order. No large table is left recoverable only from a filename or hash.

A convenience copy is recover_universal73_complete.py. The entire source below is the recovery authority.

```python
"""UNIVERSAL73_COMPLETE_V1: complete 24-record broom exclusion and barriers.
Build: CPython3.12.14 numpy2.3.5 scipy1.17.0 clarabel0.11.1,
OpenBLAS0.3.30/SkylakeX one thread. Frozen check: standard library only.
Run python recover_universal73_complete.py [build|check|extract].
No attachment, coefficient file, hidden seed or external checkpoint required.
The inherited U1-to-broom reduction is stated in result_markdown.
"""
import base64,hashlib,json,lzma,os,subprocess,sys
from pathlib import Path
assert __debug__
def enc(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(x):return [len(x),hashlib.sha256(x).hexdigest()]
DATA="""
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
"""
raw=lzma.decompress(base64.b64decode(DATA))
assert pin(raw)==[52098, 'cf6ee442715908e8bd6ab71d1a39c813e13006cc2ca562459fb143183cb477cc']
files=json.loads(raw);assert enc(files)==raw
out=Path(__file__).resolve().with_name('universal73_complete_recovery');out.mkdir(exist_ok=True)
manifest={}
for name,text in sorted(files.items()):
 assert Path(name).name==name and name.endswith('.py')
 b=text.encode();(out/name).write_bytes(b);manifest[name]=pin(b)
mb=enc(manifest);(out/'source_manifest.json').write_bytes(mb)
print('COMPLETE73_PAYLOAD',*pin(raw),flush=True)
print('COMPLETE73_SOURCE_MANIFEST',*pin(mb),flush=True)
mode=sys.argv[1]if len(sys.argv)>1 else 'build';assert mode in('build','check','extract')
if mode!='extract':
 env=dict(os.environ,OPENBLAS_CORETYPE='SkylakeX',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONHASHSEED='0')
 if env.get('PYTHONPATH'):env['PYTHONPATH']=os.pathsep.join(str(Path(p).resolve())for p in env['PYTHONPATH'].split(os.pathsep)if p)
 def run(args,exact=True):subprocess.run([sys.executable]+(['-S']if exact else[])+args,cwd=out,env=env,check=True)
 run(['recover_complete24.py',mode],mode=='check')
 run(['independent_cover.py','complete24_coefficients.json','independent24_report.json'])
 run(['recover_primal73.py',mode],mode=='check')
 for name in('combined_exact.py','cyclic_cubic.py','double_octahedron.py'):run([name])
 expected={'complete24_coefficients.json': [333984, '24e1e9837d84736d2c9a0ab22e72aa18b7daa93bb200f1f42866b1c76b11fe24'], 'complete24_exact_report.json': [4800, '5e85cbc9f4c0a5285b2c5e1a5ddb552a6b9060d6547382a9431292f67e671a9a'], 'independent24_report.json': [14572, 'a839ae0c9a5bbc64014ee6dd984c4c856c07e78f93daa43ae41d69d786c7e432'], 'primal73_recovery/rounded.json': [157531, 'de94c7e7a248753aa4c04241160160d8c748350a184d8d29d35ea91336a7f8a8'], 'primal73_recovery/primal.json': [678878, '5fa8f05faf0fe84ee187d563f5bf8c86ced85897deabdff925b0fb7b42baf806'], 'primal73_recovery/report.json': [1463, '65bacb32c91261f9e8b5fb23aa51eb81222956f80f39e136996b4def9f5e50be'], 'combined_exact.json': [448284, '737371d4065452edeb01399794eeb267e82c8d62a421757ca8f7e51e23e52621'], 'cyclic_cubic.json': [32483, '886affd94c41713ac3749015e60b290b812fc164b9a2d0d44bb88d529134798c'], 'double_octahedron.json': [6335, '5c8f96059d82a33944b0fce29803f47d9f516706f82e7029f54f453d9ee23ca0']}
 for name,p in expected.items():assert pin((out/name).read_bytes())==p,(name,pin((out/name).read_bytes()))
 print('UNIVERSAL73_COMPLETE_24_CERTIFICATES_AND_THREE_PHYSICALITY_BARRIERS_RECOVERY_PASS',flush=True)
```
