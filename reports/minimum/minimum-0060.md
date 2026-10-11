# minimum-0060

Historical AI scientific report · saved 2026-09-11 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

**A complete physical continuous domain in the open (V,E,F)=(10,17,9) slice is now excluded.** Every SPD metric on the exact local520 body below has at least two strictly stable facets. The same conclusion holds for every actual body with its literal face lattice whose own-centred normalized poles satisfy
\[
\|q_i-Q_i\|_2\le1/4000,\qquad i=0,\ldots,8.
\]
The proof covers **all 45,279 rooted true-edge spanning trees**, every stable-facet root and every weak shadow wall. It uses 254 positive-integer certificates, independently verified. It does not depend on the four surviving pole-tree forms. The minimum S=2 is attained on the reference body by an exact reciprocal metric pair. A second, non-affinely-equivalent actual body lies inside the excluded neighborhood.

Two transferable findings accompany this exclusion: **actual Λ plus literal incidence reconstructs the entire body up to a linear transformation**, giving exact triangle-centroid polynomial constraints; and actual polygon corners strengthen the facet mixed-moment coefficient from 2/3 to 3/4. An exact continuous false-centroid family passes the existing coupled Λ inequalities and the new corner inequalities but fails the reconstruction constraint. This identifies a precise remaining physicality gap.

**Scope.** This is an unconditional S≥2 theorem on the specified physical geometry domain, hence a joint110 exclusion there. It is not a whole local520-type exclusion or a new unconditional U≥2 theorem. The global register remains **633 types and 52,635 joint-root orbits**; C≥34 is unchanged. No joint110 attainer is supplied.

**Source authority and labels.** I used the current attached journal and its literal parent minimum-0057, SHA-256 e7771d552d8bf9cb3d9096179c546abc4221f0503fea5c37776396957633925e. The literal parent Markdown has 43,887 UTF-8 bytes; wrapping it as compact JSON with keys version,result_markdown gives 44,517 bytes and exactly the advertised hash. No incidence conflict was found. No homogeneous-centroid statement is dualized. The catalogue authority remains 1,111,066 bytes, SHA-256 1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77. All local labels below belong to its **V10/F9 slice**. No journal was changed.

**Exact actual body.** In canonical local520 labels the maximal facet cycles and uncentered vertices are:
```python
FACETS=[
 [0,1,3],[0,2,5,4,1],[0,3,6,2],[1,4,8,9,7,3],
 [2,6,8,5],[3,7,6],[4,5,8],[6,7,9],[6,9,8]]
VERT=[
 ["-1/8","-1/8","0"],["-1/22","-1/11","3/11"],
 ["0","-1/5","-3/5"],["-1/7","1/7","3/14"],
 ["1/22","-1/11","3/11"],["1/8","-1/8","0"],
 ["0","0","-1/2"],["-1/10","1/5","1/5"],
 ["1/7","1/7","3/14"],["1/10","1/5","1/5"]]
```
The actual volume and ordinary volume centroid are
\[
V=19903/677600,\qquad
c=(0,-662559/245204960,-1515121/61301240).
\]
Put x_v=VERT_v−c. For the first three vertices a,b,c′ of facet i, set
\[
n_i=(x_b-x_a)\times(x_{c'}-x_a),\qquad Q_i=n_i/(n_i\cdot x_a).
\]
This reconstructs all reference poles exactly. Every listed polygon is a genuine maximal facet, every listed vertex is extreme, and every boundary edge supports all other vertices of its polygon on the correct strict side. The facet-adjacency edges are exactly
\[
01,02,03,12,13,14,16,24,25,35,36,37,38,46,48,57,78.
\]
They come from true polygon boundaries. Integration diagonals never enter this graph.

**Complete continuous physical exclusion.** For a directed genuine facet adjacency define
\[
A_{ij}(q)=q_iq_i^T-\tfrac12(q_iq_j^T+q_jq_i^T),\qquad
 e_{ij}(q,N)=q_i^TN(q_j-q_i),\quad N=M^{-1}\succ0.
\]
Then tr(NA_ij)=−e_ij. The embedded source contains 254 certificates C, each a complete literal list of triples (i,j,w_ij) with positive integer weights. Write
\[
W_C=\sum w_{ij},\qquad B_C(q)=\sum w_{ij}A_{ij}(q).
\]
Exact arithmetic proves, for every certificate,
\[
\boxed{B_C(Q)\succ(W_C/80)I_3.}\tag{1}
\]
A redundant independent shift gives B_C(Q)≻I₃/10. There are 821 positive weights, maximum individual weight 20, and maximum W_C=33. The two shifts give 508 positive-definite matrices and 1,524 positive leading principal minors. An independent Fraction LDL implementation verifies all 508 matrices.

The 17-edge facet graph has 5,031 undirected spanning trees, checked by an exact Kirchhoff determinant. Exhausting all 8-edge subsets and rooting every tree at all nine facets gives 45,279 rooted trees, exactly 5,031 at each root. **Every rooted tree contains the complete directed support of at least one certificate.** A separate parent-choice enumeration independently obtains the same 45,279 trees and verifies every support inclusion.

If a facet is not strictly stable, its pole has a weak escape along a true neighboring facet. This follows from the tangent cone generated by true polar edges and the metric-normal-foot criterion. Every weak escape strictly increases squared N-norm:
\[
q_j^TNq_j-q_i^TNq_i
=2e_{ij}+(q_j-q_i)^TN(q_j-q_i)>0.
\]
If exactly one facet were strictly stable, selecting a weak escape from every other facet would therefore produce a rooted spanning tree. Its contained certificate would have every selected e_ij≥0, whereas
\[
\sum w_{ij}e_{ij}=-\operatorname{tr}(NB_C)
<-\frac{W_C}{80}\operatorname{tr}N<0.
\]
This is impossible. A pole of maximal squared N-norm has all outgoing shadows strictly negative, so at least one strictly stable facet always exists. Hence **S≥2**.

This proof uses actual same-centroid poles and one reciprocal pair M,N. It remains valid when selected or unused shadows vanish. It requires neither simplicity nor a strict-graph perturbation lemma and does not transfer homogeneous statements to the polar.

The verifier establishes ||Q_i||₂<10. If ||q_i−Q_i||₂≤δ, expansion of the outer products gives
\[
\|A_{ij}(q)-A_{ij}(Q)\|_{\rm op}\le40\delta+2\delta^2.
\]
Consequently
\[
B_C(q)\succ W_C(1/80-40\delta-2\delta^2)I.
\]
At δ=1/4000 the coefficient equals 19999/8000000>1/500. This proves the **closed physical pole-ball domain**. The coordinate box |q_i,a−Q_i,a|≤1/8000 is a sufficient subdomain because 3/8000²<1/4000². Throughout the ball, every rooted spanning tree contains a true edge satisfying
\[
\boxed{e_{ij}(q,N)<-\operatorname{tr}(N)/500.}\tag{2}
\]
There is no condition-number restriction on N.

More generally, the same 254 certificates exclude every actual realization of this incidence for which all B_C(q) are positive definite. Their three positive leading principal minors give a reusable finite polynomial domain; the ball is an explicitly certified subset. All invertible linear images are also excluded with the reciprocal metric transformed consistently.

**Sharpness and a distinct actual neighbor.** The mutually orthogonal vectors u=(1,2,3), v=(1,1,−1), w=(−5,4,−1) give the exact pair
\[
M=\frac{100}{14}uu^T+\frac1{300}vv^T+\frac1{42}ww^T,\qquad
N=\frac1{1400}uu^T+\frac{100}{3}vv^T+\frac1{42}ww^T.
\]
The verifier checks MN=I and det M=det N=1. The eigenvalues of M are 100,1/100,1. On the reference body, strict unstable vertices are exactly [2,9] and strict stable facets exactly [0,4]. All 68 directed true-edge vertex/facet shadows are nonzero. Thus S=2 is sharp over this body's entire SPD metric family. This is not a joint110 attainer.

For ε=10⁻⁸, transform the uncentered vertices by p_v^ε=p_v/(1−ε(p_v)_y). The source recomputes the new body's own volume centroid, maximal polygons, determinant masses, poles and moments. It proves
\[
\sum_i\|q_i^\varepsilon-Q_i\|_2^2<10^{-14},
\]
placing it inside even radius 1/20000. The complete vertex automorphisms are the identity and (5,4,2,8,1,0,6,9,3,7); their facet permutations are the identity and (6,1,4,3,2,8,0,7,5). The two actual normalized Λ matrices differ under both permutations, so these bodies are not affinely equivalent even without fixed labels. The formula and integration code recover every rational witness.

**Reconstruction theorem: actual Λ and incidence fix the body.** Let
\[
Y(x)=\mathbf1-Qx,\quad d_i=A_i/(V\|q_i\|),\quad
\lambda_i=\Lambda[:,i]=d_i\mathbb E_{F_i}Y,\quad
H=\mathbb E_PYY^T,\quad K_i=d_i\mathbb E_{F_i}YY^T.
\]
Every expectation here is an actual uniform measure. With actual facet centroids c_i and W=[d_ic_i], inherited divergence identities give
\[
\Lambda=\mathbf1d^T-QW,\quad WQ=I,\quad W\mathbf1=0,\quad
d^TQ=0,\quad d^T\mathbf1=3,\quad
\Lambda^2+\Lambda=4\mathbf1d^T.
\]
These identities and d_i=(Λ²)_ii/4 are inherited.

Set R=I+Λ. Then ker R=col Q: RQ=0; conversely Rz=0 implies dᵀz=0 and z=QWz. At literal vertex v let I(v) contain **all** incident facets and set
\[
A_v=R^TR+\operatorname{diag}(\mathbf1_{i\in I(v)}),\qquad b=4R^T\mathbf1.
\]
Incident normals span ℝ³, including at nonsimple vertices; otherwise a short segment through the vertex would preserve all incident equalities and strict nonincident inequalities, contradicting extremality. Thus
\[
\boxed{A_v\succ0,\qquad s_v=A_v^{-1}b.}\tag{3}
\]
Indeed a zero quadratic value forces z=Qt and every incident q_i·t=0, hence z=0. The actual vertex slack s_v=1−Qx_v satisfies Rs_v=4·1 and every incident zero, proving (3).

Equal labeled Λ and incidence give equal full vertex slack matrices S=(s_v). The rank-three factorizations S−J=−QX imply the centered bodies differ by one invertible linear transformation. All actual normalized volume, facet and shared-edge moments are fixed. The mechanical freedom is one reciprocal SPD metric pair.

For explicit recovery select three independent rows r of J−S, set x_v*=(1−S_rv)_r, and solve q_a*ᵀx_v*=1−S_av. Fan-triangulate each literal polygon solely for integration. For triangle t=(u,v,w), put Δ_t=|det(x_u*,x_v*,x_w*)| and D=Σ_tΔ_t. Then
\[
V^*=D/6,\quad d_i=3\sum_{t\subset F_i}\Delta_t/D,\quad
\widehat\lambda_i=\sum_{t\subset F_i}(\Delta_t/D)\sum_{v\in t}s_v.\tag{4}
\]
These actual determinant masses are shared by all first and second moments in the complete integration source. Every true edge uses the same endpoint slacks in both incident facets.

A finite necessary-and-sufficient candidate physicality test is now available: require Λ1=3·1 and all A_v≻0; recover (3); explicitly require Rs_v=4·1, incident zeros, strict nonincident positivity and rank(S−J)=3; reconstruct coordinates; verify the full actual convex hull, extreme vertices and exactly the literal maximal polygons; verify all pole/slack equations; integrate (4) and require Λ̂=Λ. The zero-residual equations are essential: A_v⁻¹b alone only solves normal equations. Sufficiency constructs and integrates an actual body, rather than inferring physicality from low-degree agreement. Its origin is interior, and the actual flux equation Λ̂1=3·1−4Qg forces its ordinary volume centroid g=0.

Each genuine triangular facet yields the economical polynomial constraint
\[
3\Lambda_{ai}=d_i\sum_{v\in F_i}(A_v^{-1}b)_a,
\]
or, clearing only positive determinants,
\[
\boxed{12\Lambda_{ai}\prod_{v\in F_i}\det A_v
=(\Lambda^2)_{ii}\sum_{v\in F_i}
(\operatorname{adj}(A_v)b)_a\prod_{w\in F_i,\ w\ne v}\det A_w.}\tag{5}
\]
It includes every mechanical weak wall. Total facet degree 34 guarantees at least two triangular facets in every V10/F9 type.

There is stronger conditional centroid rigidity for the whole local520 incidence. Nontriangular facets are 1,2,3,4; facets 1,2,4 meet at trivalent vertex 2, while facet 3 does not. Their four augmented normals (1,q_iᵀ) are therefore independent in every realization. For fixed actual Q,d, correct centroids on the five triangles together with W1=0 and WQ=I force all four remaining polygon centroids: the difference is supported on these four columns and annihilates an invertible augmented-normal matrix. This does not make fitted masses physical.

**Actual corner constraints.** Nonzero affine f,g≥0 on an actual convex polygon, sharing a zero, satisfy
\[
\boxed{\mathbb E(fg)\ge\tfrac34\mathbb Ef\,\mathbb Eg.}\tag{6}
\]
Equality holds exactly for a triangle when f,g vanish on two distinct edges. Every genuine nontriangle therefore gives strict inequality.

Here is a full proof. Normalize both means to 1 and put h=f+g. The planar upper bound gives Ef²,Eg²≤3/2. To prove that bound, decompose the concave piecewise-linear slice-length density on [0,T] into positive triangular densities with modes U. Their moments are (T+U)/3 and (T²+TU+U²)/6. Since EU²≤T EU, the second moment is at most Tm−T²/6≤3m²/2. Subtracting a positive minimum handles arbitrary nonnegative affine functions.

Fan-triangulate from a common-zero vertex. On triangle T, let h have values 0,a_T,b_T, actual area fraction w_T, and mean m_T=(a_T+b_T)/3. Then
\[
\mathbb E_T h^2=\tfrac98m_T^2+(a_T-b_T)^2/24.
\]
Since Σw_Tm_T=2,
\[
\mathbb Eh^2-9/2
=\sum_Tw_T(a_T-b_T)^2/24+\tfrac98\sum_Tw_T(m_T-2)^2\ge0.
\]
Subtract the two upper second moments to get (6). Equality places all non-apex vertices on one level line, forcing a triangle. The triangle vertex-value formula gives precisely the stated distinct-zero-edge equality case. Nonsimple corners are included. The signed vertex covariance inequality underneath this argument is inherited; the new finite consequence is the explicit incidence-sensitive mixed-entry bound.

For a≠b define C_ab={i∉{a,b}:F_i∩F_a∩F_b is nonempty} and P_i=Λ_aiΛ_bi/d_i. Then K_i[a,b]≥(3/4)P_i on C_ab, with the strictness above; elsewhere the inherited 2/3 applies. Actual divergence gives
\[
\boxed{15H_{ab}\ge6+2\sum_iP_i+\tfrac14\sum_{i\in C_{ab}}P_i.}\tag{7}
\]
Any strictly classified contributing corner makes this strict.

For a Λ-only version, set t_i=Λ_ir−d_r, t_i±=max(±t_i,0), and ℓ_i=3/4 on C_ab, 2/3 otherwise. Coordinate divergence gives Σt_iK_i[a,b]=2d_r−Λ_ar−Λ_br, whence
\[
\boxed{\sum_i(\ell_it_i^+-\tfrac32t_i^-)P_i
\le2d_r-\Lambda_{ar}-\Lambda_{br}
\le\sum_i(\tfrac32t_i^+-\ell_it_i^-)P_i.}\tag{8}
\]
The lower side is strict if a strict corner has t_i>0; the upper is strict if one has t_i<0. Also K_i[a,b]<(3/2)P_i for distinct i,a,b: proportional restrictions would put three extreme poles on a line. Thus the lower side is always strict when r,a,b are distinct.

The complete catalogue recovery records 46,443 common-vertex cases across all 633 types, including 26,524 nontriangular integration facets and 38,397 strict cases under the full triangle classification. There are 16,326 enhanced unordered facet-pair bounds, 15,409 with a strict contribution. These sign-independent physical constraints cover all 52,635 joint-root orbits but **exclude none by themselves**. The included nonuniform-triangle control passes the older finite generator-pair bounds but violates (6) by −1/20. It already fails the inherited full endpoint test, so independence from that stronger test is not claimed.

**Exact continuous barrier.** Keep the actual local520 Q,d,H fixed and perturb actual facet centroids in the direction
```text
[
 [-22264/123525,1936/8235,-12584/41175],
 [1936/80703,1936/134505,15488/134505],
 [968/46665,-792/5185,-176/1037],
 [121/3678,-7502/112179,3751/224358],
 [-56/3111,-56/5185,-448/5185],
 [9/305,166/305,1],
 [0,0,0],[0,0,0],[0,0,0]
]
```
This satisfies q_iᵀδc_i=0, Σd_iδc_i=0, Σd_iδc_iq_iᵀ=0. The exact 21×27 constraint matrix has rank 20 and nullity 7. Define Λ(ε)_ai=Λ(0)_ai−εd_iq_aᵀδc_i.

For **every ε∈[0,1/16]**, the family retains the same recovered actual vertex slacks, candidate centroids strictly inside the facets, inherited rank/spectrum/row/quadratic identities, the actual common H identity, all off-diagonal 10/9 caps, all pair LMIs and mixed-pair inequalities, all nine strict row/width/Φ energy bounds, all 18 full nine-variable copositive sandwiches, all 81 diagonal sandwiches including adjacent 9/8 factors, all 324 inequalities (8), and all 36 inequalities (7).

Precisely, the copositive tests use D_i=λ_iλ_iᵀ/d_i, B_r=2d_rJ−λ_r1ᵀ−1λ_rᵀ, and
\[
U_r=\sum_i(t_i+t_i^+/2)D_i-B_r,\qquad
L_r=B_r-\sum_i(t_i-t_i^-/2)D_i.
\]
The complete simplex stationary-face tests are checked exactly, not merely diagonal or two-coordinate restrictions.

Nevertheless every ε≠0 violates triangle compatibility:
\[
\boxed{3\Lambda(\varepsilon)_{60}-d_0\sum_{v\in F_0}S_{6v}
=(1469424/1214083)\varepsilon.}\tag{9}
\]
At ε=1/16 the gap is 91839/1214083. Incidence injectivity prevents another geometry from rescuing this Λ. Thus the entire coefficient interval (0,1/16] is nonphysical despite passing the listed weaker tests.

The interval proof uses two closed sign cells separated at 37589359/1324106784. Exact Bernstein positivity verifies 7,808 scalar coefficients, including Φ numerators after multiplication by certified positive denominators. The cubic copositive tests have 144 Bernstein coefficient matrices, each tested on all 511 nonempty simplex supports. A negative simplex minimum with smallest support cannot have a singular bordered stationary system: a kernel direction would preserve both sum and objective until a coordinate vanished. The finite stationary-face test therefore covers singular faces. Every tested minimum-support candidate has positive value.

This false family is neither physical nor a joint110 witness. It is not feasible for the entire mixed-K_i system: keeping actual K_i while changing Λ breaks K_iω=λ_i. Its role is to demonstrate the exact actual-centroid compatibility gap remaining after the listed strong Λ/H and corner tests.

**Work performed and remaining barrier.** Exact polygon reconstruction supplied the body and actual moments. Initial numerical matrix locators found certificates for 1,502 embeddings of the four surviving pole trees. The proof was enlarged to all 45,279 genuine rooted trees, and every accepted coefficient was replaced by a literal positive integer checked rationally. The final theorem has no dependency on numerical non-success or the four-form classification. Independent arithmetic-mean-apex integration, parent-choice enumeration and Fraction LDL verify geometry, coverage and all matrix inequalities.

The remaining physical domain is the rest of local520's realization space outside the certified polynomial domain and its affine images, together with the other 632 types. No global root/type count can be subtracted. The useful continuation is a rigorous cover of further actual realization domains by these 254 tests or newly verified certificates, combined with (5) to remove false facet-centroid candidates. The corner bounds alone cannot close that gap, as the full interval countercontrol establishes.

**Complete deterministic recovery.** The capsule below embeds nine complete source units: the literal 254 coefficient arrays, independent verifier, full inherited catalogue generator, actual polygon/edge integration, both exact bodies, reciprocal metric, corner register and continuous false-centroid proof. It requires no attachment or source download. Reproduction used **CPython 3.12.14, standard library only, assertions enabled**, with no randomness or numerical tolerance.

Save the entire code as recover_c34_polygon.py, UTF-8/LF with one final LF, and run:
```text
python -S recover_c34_polygon.py C34_polygon_recovery
```
Wrapper: 26,454 bytes, SHA-256 2a5aea45a9b55246bd1d4402ff03db8c5a5d76f6b04803e5049226db5506f3ae. Embedded source pack: 61,763 bytes, SHA-256 92109df2b1d692245f368180a39451913fa961448fc2545a1b43ea4fe39e93a2. Base64 data: 23,648 characters. Primary physical verifier: 14,234 bytes, SHA-256 4fda1fdd3b5595ad3f9c68dd664036422457e76e97bd9be2fedba1bb776870da. Independent verifier: 4,768 bytes, SHA-256 c74c16c5ff459a0cb719826336335664d9daaf5802df896aae5aaba774c7bdca.

The complete integer coefficient stream is 7,082 bytes, SHA-256 5ad39998189721966454c7ef58c153eb4593a783efdaf0629f8251cae4f2e5b8. Regenerated rooted-tree stream: 2,263,951 bytes, SHA-256 2dd6d27a5dba005a7546aa03dad3a01a4f408068f9164302c2edea4904859207. The sources reconstruct both. All eleven output byte counts and hashes are literal in PINS and checked after execution.

Observed terminal markers:
```text
C34_LOCAL520_ALL_SPD_STABLE2_NEIGHBORHOOD_PASS
INDEPENDENT_FIXED520_REVIEW_PASS 254 508 45279 [5031, 5031, 5031, 5031, 5031, 5031, 5031, 5031, 5031]
C34_LOCAL520_ACTUAL_COMMON_METRIC_U2_S2_PASS [2, 9] [0, 4]
C34_LOCAL520_NONAFFINE_ACTUAL_NEIGHBOR_INSIDE_POLE_BALL_PASS
C34_V10_CORNER_GATE_PASS 633 52635 46443 26524 38397 16326 14948 15409
LAMBDA_VERTEX_RECOVERY_AND_FALSE_TRIANGLE_CENTROID_PASS 10 7 4
LAMBDA_FALSE_CENTROID_COMPLETE_CONTINUOUS_INTERVAL_PASS 7808 144
C34_V10_ACTUAL_POLYGON_PHYSICAL_DOMAIN_COMPLETE_PASS 9 11
```
A fresh-directory execution reproduced all eleven pins and exited 0. The supplementary [C34_V10_ACTUAL_POLYGON_DOMAIN_V1.zip](sandbox:/workspace/scratch/4946fd71afc5/C34_V10_ACTUAL_POLYGON_DOMAIN_V1.zip) contains 25 files, 546,245 bytes, SHA-256 b588ea330a8b9e0d35c477c7b2368b5fee9107355bdc6bfa0c5a40654ed90195. The inline capsule is sufficient without that archive.

```python
"""Complete C34/V10 actual-polygon domain recovery; Python3.12.14, stdlib."""
assert __debug__
import base64,hashlib,json,lzma,subprocess,sys
from pathlib import Path
DATA="""
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
"""
raw=lzma.decompress(base64.b64decode(''.join(DATA.split())))
assert len(raw)==61763 and hashlib.sha256(raw).hexdigest()=='92109df2b1d692245f368180a39451913fa961448fc2545a1b43ea4fe39e93a2'
files=json.loads(raw)
root=Path(sys.argv[1] if len(sys.argv)>1 else 'C34_polygon_recovery').resolve()
root.mkdir(parents=True,exist_ok=True)
for name,source in files.items():
 p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(source.encode())
COMMANDS=[['c34_catalogue.py'], ['actual_control/polygon520.py'], ['actual_control/metric520.py'], ['actual_control/nearby520.py'], ['fixed520/fixed520_neighborhood.py'], ['polygon_moments/review_fixed520.py', 'fixed520/fixed520_neighborhood.py', 'c34_catalogue.json'], ['polygon_moments/corner_gate.py', 'c34_catalogue.json'], ['facet_incidence/lambda_interval.py']]
for command in COMMANDS:
 subprocess.run([sys.executable,'-S',*command],cwd=root,check=True)
PINS={'c34_catalogue.json': [1111066, '1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77'], 'actual_control/polygon520.json': [73936, 'e869385416f591cd09f7e32e6b98a06e8b69133a5eac4370c42c186c522111b3'], 'actual_control/metric520.json': [3781, 'f1647ad7a4bb146794c432b7d7dd75726e068f7b54e9ea3521cf90b75ca46fcc'], 'actual_control/nearby520.json': [10711, 'a5603f4bdc6e2ba57c4d12557a875dd99a380caa427110b1c6ac16728a0dfa94'], 'actual_control/nearby520_body.json': [549237, '65340b20211ae0e98d3c96e6ca17d74a4687d576a7cce119b5b97556e973772e'], 'fixed520/fixed520_neighborhood.json': [10172, '6473642119846aa88176ebff7f9190aa282c1d8df3a0debc1d092264d265b99a'], 'fixed520_review.json': [496292, '552d24a15cb5aee2c96805700cdf4d62486ba76ac2bdfa0a94d8da933ae60852'], 'polygon_corner_control.json': [1467, '89f62be6f2692eaa3015359c08a91a9d8e4ba86c0a6798cade52cec3995ce638'], 'c34_v10_corner_gate.json': [1474967, '535beead9cd418f97dbe838f1307c8b1507bb6c82cc2304e41f7f4fa9f6cbacc'], 'facet_incidence/lambda_recovery.json': [134565, '048da48463d7fa496ea207b5ee838a33c70c26c1cb1d904c0203a45c76390681'], 'facet_incidence/lambda_interval.json': [19299, 'ce2e1fef4a6ce620247c27a93cf786ce04e96f0b60e8b6f5d432d36ae5ddabcb']}
for name,(size,digest) in PINS.items():
 b=(root/name).read_bytes()
 assert len(b)==size and hashlib.sha256(b).hexdigest()==digest,(name,len(b),hashlib.sha256(b).hexdigest())
print('C34_V10_ACTUAL_POLYGON_PHYSICAL_DOMAIN_COMPLETE_PASS',len(files),len(PINS))
```
