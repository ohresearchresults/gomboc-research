# minimum-0062

AI research report · 2026-09-12 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

**NIMBLE99_C34_COMMON_BODY_GEOMETRIC_GAPS_AND_PROJECTIVE_V3.** The new global result is constructive: every actual joint candidate in the entire (V,E,F)=(10,17,9) slice has separated facet poles, quantitatively recoverable actual slacks, and

\[
\Lambda_{ab}+\Lambda_{ba}<2-10^{-501}\qquad(a\ne b).
\]
The proof uses the common ordinary volume centroid, genuine polygonal measures, the reciprocal metric, and a quantitative obstruction to an approximate translation between two actual facets. It includes nonsimple vertices and all weak escape walls. Separately, the full admissible **y-projective family of the literal local520 body has S≥2 for every SPD metric**. This strictly enlarges the previously excluded union of affine orbits. A uniform all-realization pole tube around the old x-family is excluded too. The whole three-parameter projective class now has an exact compact physical weak-tree formulation in eight variables and 41 polynomial inequalities.

**These results do not exclude a whole combinatorial type or a complete global joint-root orbit. The unchanged register is 633 genuine types and 52,635 joint-root orbits. The accepted bounds remain V≥10, F≥9, C≥34.** No negative search is used as evidence of physical impossibility.

Authority and dependencies. The literal incidence parent remains `minimum-0060`, serialized-payload SHA-256 `edb029e956d9cea65c7297fabb387c1b16376de0664afb87b8a65dc23b745a04`. It was authenticated in the supplied journal `research-journal(20260911-201143).md`, 4,819,934 bytes, SHA-256 `d988781f9e7530d991ec3428ead665c1cdf52b2d273948aa8f75e98812182b50`; no incidence conflict was found. The catalogue SHA remains `1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77`. The immediately preceding literal handoff is `NIMBLE99_C34_PROJECTIVE_AND_COMPACT_ACTUAL_JOINT_V2`, `result.json` including LF: 63,266 bytes, SHA-256 `0683fa0308e90a01ba8a987a2a02c1621d64b7d4a83322c0e4892695d158b686`. It has no newly invented assignment ID. Its complete literal recovery source is the predecessor input needed by the new x-tube patch. The journal supplies the other exact inherited coefficient source, `minimum-0021`, SHA-256 `5eba4891ccbcf0917f0390ff3e42f18b1fcd040b72f92a3a7fc8a18f1b2a6557`, containing `NOVA24_WEIGHTED_CAP_7_6_V1`. The entire-column actual pair identities used below are `minimum-0058`, SHA-256 `159513b19201b45a7b7495a919e077021333865f6f160c989e63debf72597df3`. The inherited seven-vector weak reflection theorem is `minimum-0011`, SHA-256 `c25517a4392be3ff8fcd2adbe08ec8acf4db02b86b1903a4003799e1970e25c6`, at factor 1663/5000. These inherited proofs are inputs, not newly claimed discoveries.

The following literal local C34/V10/F9:520 data retain every parent label. They do not identify a C32 type or a sphere alias:

```python
FACETS=[[0,1,3],[0,2,5,4,1],[0,3,6,2],[1,4,8,9,7,3],
        [2,6,8,5],[3,7,6],[4,5,8],[6,7,9],[6,9,8]]
A=[8,22,5,14,22,8,2,10,14,10]
NVERT=[[-1,-1,0],[-1,-2,6],[0,-1,-3],[-2,2,3],[1,-2,6],
       [1,-1,0],[0,0,-1],[-1,2,2],[2,2,3],[1,2,2]]
QRAW=[[-6,-2,2],[0,-8,1],[-9,1,-2],[0,1,4],[9,1,-2],
      [-6,4,-2],[6,-2,2],[0,7,-2],[6,4,-2]]
# v_a=NVERT[a]/A[a], componentwise exact rational division.
```

All true edges are the boundaries of these maximal polygons. The sixteen first-vertex fan triangles serve only integration. The source verifies the complete hull and reconstructs the true edge graphs directly.

**Global constructive theorem and proof.** Throughout this theorem, P is one actual homogeneous three-polytope with V10/E17/F9, ordinary centroid zero and covariance I, admitting both weak trees for one reciprocal pair M,N=M⁻¹. The inherited covariance and finite-depth theorem gives √(5/3)B⊂P⊂√15B and condition(M)<47. The inherited V2 constructive constants are

\[
C=6769,\quad K=72\cdot10^{12},\quad
 a=(32CK)^{-1}=1/15595776000000000000,\quad
 \beta=(a/10)^3/256.
\]
Every distinct primal vertex pair is farther apart than a, every primal vertex has distance greater than β from the hull of the others, and every actual facet coefficient d_i=area(F_i)h_i/Vol(P) exceeds aβ/640. These premises require both trees. Define

\[
e_0=(2^{20}12690)^{-1},\quad
 a_q=e_0/C=1/90071220879360,\quad d_q=a_q/12,\quad b_q=d_q^3/256,
\]
\[
m=a\beta/640,\quad h=a\beta a_q/48,\quad
\theta=\beta/1024,\quad \gamma=(\theta mh/16)^2.
\]
Then

\[
\|q_i-q_j\|>a_q,\qquad
\operatorname{dist}(q_i,\operatorname{conv}\{q_j:j\ne i\})>b_q,
\]
\[
 b_q=1/323252469868097072451258749086744006002475008000,
\quad 2-\Lambda_{ab}-\Lambda_{ba}>\gamma>10^{-501}.
\]
The rational formula for γ is the exact datum; its numerator is one and its denominator has 501 decimal digits. No arbitrary gap has been inserted.

First make the inherited eight-vector theorem robust. Eight nonzero vectors with a rooted weak tree cannot have apex-excluded coefficient rows ν satisfying 0≤ν_ij≤7/6, Σ_jν_ij=3 and Σ_jν_ijq_j=−k_iq_i when |k_i−1|≤η_k=2⁻¹⁷. Here is the complete perturbation of its finite proof. The 115 rooted types consist of analytic classes of sizes 30,28,7,30,1,2 and 17 matrix types. The analytic root and first-child projections have margins at least 1/500; replacing the target by k_i loses at most η_k. For the sole height-four broom, the small first-child norm branch has margin 5893/65536; the large branch has minimum 19/384 before the same loss. Thus all analytic classes remain excluded.

For the five matrix types requiring a secondary row, the inherited reduction keeps the exact disjunction: H=−q₀·q₂−||q₂||²/4≥−(3η_k/2)||q₂||²; or, only for the pure chain, both H₀=−q₀·q₂−(389/2000)||q₂||²≥−(3η_k/2)||q₂||² and J=−(2/3)q₀·q₂−||q₂||²−(7/6)q₂·(q₆+q₇)≥−η_k||q₂||². Indeed the secondary capped-row extreme has root coefficient 7/6 or 2/3; omitting the root contradicts the 499/500 subtree bound. Its former thresholds 14003/56000,145/512,557/1792 and83/256 are all above1/4, and changing its target by η_k reduces a threshold by at most3η_k/2. The exceptional marked chain pair {6,7} retains H₀ and J instead of imposing H incorrectly.

Write E=Σ||q_i||²>0. The 1,785 ordinary and 105 exceptional identities have positive quadratic remainder greater than E/4096. Their fixed common direction has coefficient ℓ¹ norm at most8. The new exact audit of every literal multiplier, including all22 ordinary and9 exceptional overrides, gives λ_H≤34801/6000<6 and (3/2)λ_H₀+λ_J≤265/32<9. Thus secondary errors cost less than9η_kE. Average the105 extreme root rows; its perturbed left side is (1−k₀)d·q₀, of absolute value at most8η_kE. The remaining margin is

\[
1/4096-17/131072=15/131072>0.
\]
This proves the robust theorem uniformly over all weak walls, dimensions and SPD metrics. The capsule checks the unchanged1,890 shifted PD identities and the entire115-type coverage, then every new error bound.

Normalize N to trace one and put y_i=N^{1/2}q_i, Q=conv{y_i}. Its true polar P₀ is a linear image of the ORIGINAL centroid-zero primal body. The licensed joint bounds give rB⊂Q⊂RB, r²>1/2115, R<1, (R/r)²<423, and −Q/3⊂Q. Suppose a repaired hull Q′⊂Q has at most eight labels, a weak tree and Hausdorff error e<e₀. Then (1−e/r)Q⊂Q′. True polarity gives P₀⊂P′=(Q′)*⊂(1−e/r)⁻¹P₀. Comparing actual uniform volumes shows

\[
\|g(P')\|\le\frac{1-(1-e/r)^3}{r(1-e/r)}
 \le6e/r^2<12690e<2^{-20}.
\]
The weak labelled tree descends to genuine vertices by removing duplicate steps and expressing nongenuine successors as convex combinations; distinct weak arrows strictly increase norm. With eight genuine poles z_i, put t_i=z_i·g(P′), so |t_i|<η=2⁻²⁰. The actual centered poles are p_i=z_i/(1−t_i). Their actual homogeneous facet rows μ have cap10/9, sum3, and represent−p_i. Set λ_ij=μ_ij(1−t_i)/(1−t_j), S_i=Σλ_ij, ν_ij=3λ_ij/S_i, k_i=3/S_i. Then ν has cap at most (10/9)((1+η)/(1−η))²<7/6 and |k_i−1|≤2η/(1−η)<2⁻¹⁷, contradicting the robust theorem. With at most seven genuine poles, −[(1−e/r)/3]Q′⊂Q′; its factor exceeds1663/5000 because e/r<47e₀<11/5000, contradicting the inherited seven-vector theorem. This treats every loss of labels without assigning a homogeneous centroid to Q or Q′.

If two original poles have distance Δ≤a_q, delete the smaller-norm y-label and redirect its children to the other. Replacement parents have greater old norms; shadow errors are at most E=RΔ. Scale each retained depth-j point by s^j, s=1−2E/r². Depth≤8 suffices; after positive scaling, each repaired shadow is at least−E+(1−s)||y||²≥E>0. Movements are at most16ER/r², so e≤[1+16(R/r)²]Δ<CΔ≤e₀: contradiction. Therefore all pole pairs are separated by a_q.

Their y-distances exceed d_q because λ_min(N)>1/141>1/144. If y_v were within ζ≤b_q of the remaining hull, it could not be the maximal root, whose distance exceeds d_q²/(2R). For each child y of v, a convex approximation w has 1−λ_y>d_q/(4R). Averaging the old escape through w gives a retained z≠y with shadow at least−E, E=4R²ζ/d_q. Since E<d_q²/2, z has greater old norm. The same repair has e≤ζ+16ER/r²<135361ζ/d_q≤135361d_q²/256<e₀, again impossible. Since N≤I this also proves the stated original-coordinate extremality bound.

Now use actual polygonal moments. Define Y_a(x)=1−q_a·x, Λ_ai=d_i E_{F_i}Y_a, K_i,ab=d_i E_{F_i}(Y_aY_b), ω_i=d_i/3, with uniform area expectations. Three genuine vertices in any maximal facet have a longest side>a and altitude>β: the perpendicular foot lies on that longest side, which belongs to the hull of the other vertices. Their support distance is>1, hence their determinant exceeds aβ. Their norms are<4. For distinct facets a,c, inverse-matrix cross products therefore imply

\[
\|q_a-q_c\|\le48\max_{F_c}Y_a/(a\beta),\qquad
\max_{F_c}Y_a>h.
\]
A fan from a maximizing vertex gives E_{F_c}Y_a>h/3. The inherited genuine planar inequality3E(fg)≥2E(f)E(g) for nonnegative affine f,g yields, for c≠a,b,

\[
K_{c,ab}>2d_ch^2/27,\qquad
\omega_cK_{c,ab}>2m^2h^2/81.
\]
Also every off-diagonal actual Λ entry exceeds mh/3. These are shared actual facet measures, not independent moment choices.

Let s=Λ_ab,t=Λ_ba,ε=2−s−t. The actual pair inequality (6−5s)(6−5t)≥1 gives |t−1|≤2√ε when0≤ε≤1. Put v=d_a E_{F_a}(Y_bx), so ||v||<t√15<5. The inherited full-column identities are

\[
\delta=2\mathbf1-K_ae_b-K_be_a,\quad0\le\delta_c\le4\epsilon,
\]
\[
\sum_c\omega_cK_{c,ab}[(K_{a,bc}-1)^2+(K_{b,ac}-1)^2]\le2\epsilon,
\qquad K_ae_b=t\mathbf1-Qv.
\]
The moment floor gives |K_{a,bc}−1|≤9√ε/(mh) for c≠a,b, and the two special coordinates follow from δ. Consequently

\[
\|Qv-(e_a-e_b)\|_\infty\le11\sqrt\epsilon/(mh).
\]

No ||v||<5 can have this residual≤θ. Such a v has ||v||>1/2 and q_a·v>1/2. If a vertex x belonged to neither selected facet, a unit exposing normal n with gap>β exists. Both n±(β/16)w are in its true normal cone for every unit w, because all chords are<8. Their nonnegative expansions in incident normalized poles have coefficient sums<8. All those pole pairings with v have absolute value≤θ. Taking w=v/||v|| yields ||v||≤128θ/β<1/4, contradiction. Thus F_a∪F_b contains every vertex.

Every other maximal facet is a triangle or quadrilateral, since its intersection with each selected facet contains at most two vertices. Suppose a triangular side facet has x,y exclusive to F_a and z exclusive to F_b. Each cross edge xz or yz has two side-facet poles q_c,q_d. The support identity (q_c×q_d)×x=q_d−q_c gives ||q_c×q_d||>a_q/4. Their pairings with v are≤θ, so the component w of v perpendicular to the edge has norm≤8θ/a_q. Write u=x−z=|u|e and v=ℓe+w. Then |ℓ|>1/4. With t₀=(q_a·u)/(q_a·v),

\[
u-t_0v=(|u|/\ell)[-w+v(q_a\cdot w)/(q_a\cdot v)],
\quad\|u-t_0v\|<2816\theta/a_q.
\]
The same t₀ works for y−z. Hence ||x−y||<5632θ/a_q<a, impossible. Every triangular side facet must therefore contain a shared vertex of the two selected facets.

Let j=|F_a∩F_b|∈{0,1,2}. The two facets account for10+j vertex incidences; the seven side facets account for24−j. If T are triangular,28−T=24−j, so T=4+j. Yet a side facet through a shared vertex must be the triangle consisting of that vertex and one exclusive vertex from each selected facet. It is adjacent to both selected facets in the cyclic vertex figure. If j=1, those two facets are nonadjacent there, so at most two such side triangles occur. If j=2, they are adjacent at each endpoint, so at most one side triangle occurs at each, again at most two; the same third facet cannot contain both endpoints because their edge already has its two incident maximal facets. If j=0 there are none. This contradicts T=4+j. No simplicity assumption was made.

For ε≤γ, the displayed residual is≤11θ/16<θ. Thus ε>γ, proving the uniform actual joint pair gap on the entire slice.

**Constructive Λ reconstruction and actual fan masses.** For any actual joint vertex x and any unit u, strengthen the same cone argument to n±(β/8)u. Each positive incident-pole expansion has coefficient sum x·n′<4(1+β/8)<9/2. Choose the sign with |n′·u|≥β/8. It follows that max_{i incident x}|q_i·u|>β/36, hence σ_min(Q_I)>β/36, including nonsimple vertices.

Let W=[d_ic_i], R=I+Λ. The inherited actual identities Λ=1dᵀ−QW, WQ=I, W1=0, dᵀ1=3 imply, for arbitrary z,

\[
z=Qt+w,\quad t=Wz,\quad w=(I-\mathbf1d^T/4)Rz,
\quad\|w\|\le(13/4)\|Rz\|.
\]
Since ||Q||<3, the incident singular bound gives

\[
\|z\|\le\beta^{-1}[108\|z_I\|+(1417/4)\|Rz\|],
\quad108^2+(1417/4)^2<2^{18}.
\]
Thus the exact incidence reconstruction matrix A_x=RᵀR+Diag(1_I) satisfies

\[
(\beta^2/2^{18})I\prec A_x\preceq91I,
\qquad s_x=A_x^{-1}(4R^T\mathbf1).
\]
For two actual candidates of the same incidence, the resolvent bounds ||A′−A||≤20e, ||b′−b||≤12e, ||s_x||≤12, e=||Λ′−Λ||_F, give

\[
\|s'_x-s_x\|\le(252\,2^{18}/\beta^2)e.
\]
The segment between the candidates need not be physical. Every triangle of three genuine vertices of one maximal facet has oriented origin determinant>aβ. Since the total origin-fan determinant D<960, every canonical normalized origin-fan mass exceeds aβ/960. This does not give positive mass to an arbitrary degenerate apex-fan cell. All these quantitative improvements are JOINT-only; a false-centroid Λ is still inadmissible.

**Full projective class: constructive walls and eight-variable exact formulation.** Write t∈R³, d_a=1+t·v_a, L_a=A_ad_a. The entire bounded projective class modulo affine maps is

\[
P_t=\operatorname{conv}\{v_a/d_a\},\quad
T=\{t:d_a>0\}=\operatorname{int}\operatorname{conv}\{-q_i^{raw}\}.
\]
For an integration triangle abc put τ_abc=|det(n_a,n_b,n_c)|. Define the exact integer polynomials

\[
D=\prod_aL_a,\quad N=\sum_{abc}\tau_{abc}\prod_{k\notin\{a,b,c\}}L_k,
\quad V=N/(6D).
\]
N has degree6 and49 monomials; D has degree10 and152. This is actual transformed volume. The Jacobian of x↦x/(1+t·x) is (1+t·x)⁻⁴, hence ∇V=−4m and ∇²V=20V E_{P_t}xxᵀ. Put

\[
E=D\nabla N-N\nabla D,\quad K=4ND,
\]
\[
J_{ab}=D^2N_{ab}-D(N_aD_b+N_bD_a+ND_{ab})+2ND_aD_b,
\quad G=4NJ-5EE^T.
\]
Then the actual centroid is c=−E/K and covariance Σ=G/(5K²)≻0. In particular ∇²logV=20Σ+4ccᵀ and ∇²(V⁻¹/⁴)=−5V⁻¹/⁴Σ. Set r_i=q_i^{raw}+t, H_i=K+r_i·E>0 and Z_a=Kn_a+L_aE. Actual centered vertices and poles are x_a=Z_a/(L_aK), p_i=Kr_i/H_i. Their shared actual slacks are S_ia=S⁰_ia/(d_a(H_i/K)).

A new use of true polygonal incidence removes every projective boundary. Four cyclic facet vertices have an affine circuit c with two positive and two negative entries. After deformation its coefficients are c_ad_a. For one same-sign pair a,b, the Radon point belongs to the opposite pair's segment, so β-extremality and chord length<8 imply d_b/d_a>(β/8)|c_a/c_b|. The literal polygons generate22 circuits,36 directed same-sign arcs, and paths of length≤3 for all90 ordered vertex pairs with coefficient≥5/11. All circuits and paths are deterministically regenerated and checked. The exact origin weights (2/9,0,0,7/36,0,2/9,1/6,0,7/36,0) give Σw_ad_a=1. Consequently every hypothetical actual joint member satisfies

\[
d_a>\eta=(5/11)(\beta/8)^3\quad\hbox{for every }a.
\]
This is approximately9.69×10⁻¹⁹³, and its denominator has638 binary digits. The compact polytope T_η={d_a≥η} lies inside T, retaining all joint candidates without a guessed cutoff.

Use eight variables (t_x,t_y,t_z,m00,m11,m01,m02,m12) and M=[[m00,m01,m02],[m01,m11,m12],[m02,m12,1]]. For any chosen pair of rooted TRUE edge trees impose the ten walls d_a≥η, all seven nonempty principal minors of each matrix

\[
164\det(G)M-3\operatorname{tr}(MG)\operatorname{adj}(G),
\qquad3337\operatorname{tr}(MG)\operatorname{adj}(G)-3878\det(G)M,
\]
plus the nine primal and eight pole weak inequalities

\[
\operatorname{tr}(MB_{ab})\le0,\quad
B_{ab}=2L_bZ_aZ_a^T-L_a(Z_aZ_b^T+Z_bZ_a^T),
\]
\[
\operatorname{tr}(\operatorname{adj}(M)C_{ij})\le0,\quad
C_{ij}=2H_jr_ir_i^T-H_i(r_ir_j^T+r_jr_i^T).
\]
The clearing factors are strictly positive; adj(M) is exactly the reciprocal metric multiplied by det(M). The two matrix inequalities are the inherited derived normalized bounds3/164 and3337/3878 in the actual covariance gauge. After congruence, the first becomes164C−3tr(C)I≽0, C=G^{1/2}MG^{1/2}. Trace zero would force M=0, contrary to M22=1. Thus M≻0. On compact T_η, G is uniformly positive definite; the same inequality and M22=1 bound M uniformly. All41 polynomial inequalities therefore define a compact, actual, closed weak-tree domain. Degrees are at most273. No independent centroid, rank-free Gram matrix or free moments remain.

The source function `build(primal_parent,pole_parent)` accepts any genuine rooted tree pair, using `None` as the root marker. Its default two BFS trees at root0 merely demonstrate the builder and are not claimed feasible. The union over all true tree pairs is the complete physical weak-tree class in this fixed projective orbit; it contains every strict joint110 member but also retains degenerate equilibrium walls. No such branch has been proved empty by this formulation alone.

For an already-actual slack matrix recovered from Λ and incidence, projective-orbit membership has a small exact test. Its positive nonincidence graph has19 nodes and56 edges; a BFS spanning tree leaves38 fundamental cycles. Equate the alternating products of S_ia/S⁰_ia around each cycle. The resulting33 quadratic and5 cubic binomials are equivalent to positive row/column scaling. Rank-four homogeneous slack factorizations then give projective equivalence. This is not a physical-realizability test for arbitrary low-degree matrix data: actual centroid and determinant reconstruction remain mandatory.

**Complete new physical family exclusion and old-family tube.** For the literal vertices above, P_t^y=conv{v_a/(1+t(v_a)_y)} has its full positive-denominator interval−5<t<5. Every member, at its own ordinary centroid, has S≥2 for every SPD metric, as do all its affine images. No joint condition-number restriction is used.

For each of the sixteen integration triangles, use its actual transformed mass w_abc/(d_ad_bd_c), with w_abc=|det(v_a,v_b,v_c)|/6. Their sum is V; one quarter of the mass-weighted sum of the three transformed vertices is m; c=m/V. Set

\[
\Delta=(1-t/8)^3(1-t/11)^3(1-t/5)^2(1+t/7)^2(1+t/5)^3,
\quad\mathcal V=3339212800000\Delta V,
\quad\mathcal m=3339212800000\Delta m.
\]
The resulting integer degrees are10 for volume and (zero,9,10) for first moment. With r_i=q_i^{raw}+t e_y and H_i=Vcal−r_i·mcal, compactify each endpoint E∈{−5,5} using ε=1−t/E and L=I+(ε−1)Π_E, where

\[
\Pi_5=\begin{pmatrix}0&0&0\\0&1/10&3/10\\0&3/10&9/10\end{pmatrix},\ I_5=\{1,2,4\},
\quad
\Pi_{-5}=\begin{pmatrix}1&0&0\\0&1/2&1/2\\0&1/2&1/2\end{pmatrix},\ I_{-5}=\{3,7\}.
\]
Here detL=ε at+5 and ε² at−5. Put R′=εr+(1−ε)Πr and V1=Vcal/ε. Divide R′_i and H_i by ε exactly for i∈I_E, and divide neither otherwise, obtaining R*_i,H*_i. Then the actual compactified centered poles are q*_i=V1R*_i/H*_i. This pole formula uses L⁻ᵀ and is valid for both determinant ranks. V1(5)=22394880000 and V1(−5)=71991296000. All required H* and V1 are positive, including the auxiliary polynomial endpoints; neither endpoint is asserted to be an original physical family member.

For a true directed facet edge i→j, set

\[
C_{ij}=H_j^*R_i^*(R_i^*)^T-H_i^*\operatorname{sym}(R_i^*(R_j^*)^T)
=\frac{(H_i^*)^2H_j^*}{V1^2}
[q_i^*(q_i^*)^T-\operatorname{sym}(q_i^*(q_j^*)^T)].
\]
The multiplier is positive. The complete literal certificate set has2337 arrays,7764 positive integer weights, maximum1000, and support sizes3–6. Its lossless optimized recovery exploits1138 reflected-array backreferences and40-bit interval masks; it reconstructs the ORIGINAL exact arrays, ordering and two original coefficient hashes. It changes no mathematics.

On all40 quarter-cells [k/4,(k+1)/4], k=−20,…,19, there are12892 certificate/cell incidences. Degree14 Bernstein coefficients prove193380 matrices positive definite by580140 strictly positive leading principal minors. On EVERY cell, their true-edge supports cover all45279 rooted facet spanning trees,5031 at each root; Kirchhoff's determinant checks the undirected count. Thus1,811,160 cell/tree cases are covered. If a unique stable facet existed, each other pole would have a weak true-edge escape; distinct weak escapes strictly increase norm, giving a covered rooted tree. Its selected shadows have nonpositive contraction with the pole metric, whereas the positively weighted certificate matrix is PD and has positive contraction. This is a contradiction for every SPD metric, including every selected zero and unused-shadow wall.

The new y-line is not merely an old affine orbit. The exact control P_y(1) has centroid (0,−407347/10782240,−194999/3080640). All990 pairs of chords in the entire old x-family have parallel collisions only at0 and ±{1/4,22/25,4/3,2,22/7,4,62/13,90/17,11/2,23/4,6}. Only x=0 has a parallel class of four. The y=1 control's unique four-class is05,14,38,79, with normalized sorted lengths(1,5/3,5/2,20/7), versus(1,11/5,11/4,22/7) at x=0. An affine map preserves these within-direction ratios, so arbitrary relabeling cannot make the control equivalent to any old x-family member. This exhaustive algebraic check is in the standalone y verifier.

The old x-family also has a new uniform actual pole tube. For every compactified parent template q*(t),0≤t≤7, and its reflected negative half (vertex permutation[5,4,2,8,1,0,6,9,3,7], facet permutation[6,1,4,3,2,8,0,7,5]), any actual body of the same complete labelled maximal incidence whose OWN-centroid poles satisfy max_i||q_i−q_i*(t)||≤2⁻²⁰ has S≥2 for every SPD metric. No arbitrary perturbed pole array is asserted realizable. For every parent Bernstein certificate matrix B, use λ=4det(B)/tr(B)²<λ_min(B); take the minimum over its cell. Exact positive denominator bounds give a pole norm bound K and an upper bound μ on its sum of positive clearing-weight factors. The shadow perturbation norm is≤4Kδ+2δ². Thus δ≤min(1,λ/[2(4K+2)μ]) retains a positive certificate. Sort the finite certificates by this radius and retain enough to cover every rooted tree in each cell. The exact global radius exceeds2⁻²⁰; the bottleneck is cell26, [13/2,27/4], approximately1.231542984×10⁻⁶. This patches the pinned parent certificate source without new numerical optimization. The full ledger is regenerated, not an irrecoverable list of radii.

**What remains.** The projective lines and tube do not cover all three projective parameters, and even the entire fixed projective class is only a subset of local520's realization space. The new positive pair gap alone does not contradict any remaining actual branch. The exact8-variable model still requires a continuous infeasibility certificate over all allowed parameters and a complete set of coupled true-tree branches before any projective-class or rooted-domain closure can be claimed. Other catalogue types must keep their literal incidences. A useful next step is to exploit the explicit Radon denominator walls, actual rational covariance and constructive Λ conditioning when certifying regions in the full t-space; the universal pole/pair bounds are available simultaneously. A formulation or an unsuccessful search cannot replace that proof. No global register is recomputed or reduced here.

**Deterministic recovery, verification and observed pins.** The capsule below is the complete new runnable source unit, including every y-certificate coefficient. Its only external inputs are two already-literal research parents: the exact attached journal above and the **previous V2 answer's literal `recover.py`**, 34,967 bytes, SHA-256 `d1870b0f7717c6b7732eaf1023b0254504276ec20d962c94f825199fed3891d2`. Save that prior literal code as `recover_V2.py`; it is an exact reconstructible parent dependency, not a new file-only checkpoint. The new decoder validates both parents, extracts only their pinned source payloads without executing journal text, and reconstructs every new source. It reads the inherited cap source from the literal journal capsule, and the old x-certificate source from the prior V2 capsule. Thus no numerical solver, download, absent coefficient row or hidden helper is needed. All other new modules, including the y-family verifier, are standalone.

Save the following complete code as `recover_V3.py`, UTF-8/LF with final LF. Use **CPython3.12.14**, standard library only, assertions enabled. In an empty output directory run:

```bash
python -S /absolute/path/recover_V3.py /absolute/path/research-journal\(20260911-201143\).md /absolute/path/recover_V2.py
```

The decoder uses four independent subprocess workers only to reduce replay time. There is no random seed or numerical search. The DAG builder's exact default controls and all nondefault settings are embedded. An individual branch can be rebuilt with `build(primal_parent,pole_parent)` from the recovered global source; root markers are `None` and all parent arrows must be genuine edges forming one rooted tree.

A clean reconstruction and complete exact replay was run. The y-line recovered40 cells,2337 certificates,193380 PD matrices and580140 positive minors. The x-tube recovered150423 parent Bernstein matrices and all28 complete root covers. The robust cap audit recovered all1890 shifted PD identities,5040 increasing parent arrays and115 rooted types, then every new error budget. The global model compared all41 DAG expressions to direct actual geometry at12 exact parameter/metric controls, including off-diagonal metrics; its actual moment formulas and all directed true arrows were also checked at six rational three-dimensional parameters. These finite controls check implementation, while the displayed algebraic and geometric proofs establish the continuous assertions. All ten output byte/hash pins are asserted by the capsule.

Expected final marker:

```text
NIMBLE99_C34_COMMON_BODY_GEOMETRIC_GAPS_AND_PROJECTIVE_V3_RECOVERY_PASS
```

The exact sourcepack is68,075 UTF-8 JSON bytes, SHA-256 `18a2456f184b8392c95a97f8f0bda8880b5c2efdbb0f2fdcb10c9174e80b20ca`; its XZ representation is28,128 bytes, SHA-256 `8d0947df5cd7f32dbfe42e32608ffd212a597c74f2c6f859f8a1e2a217ad841b`. The base64 data, ignoring wrapping whitespace, is37,504 bytes, SHA-256 `768475bddaf54815510d711c7868951838103a0478fa153be1f86dcc1d76a9f8`. The full recovery source below is42,718 bytes, SHA-256 `5a2dd6f90d2ec494eacc55f8ce555f64a02598d07dbcbd4028183631e8121257`.

The irreducible y-coefficient JSON is124,054 bytes, SHA-256 `55e9b3e21fea300b998d77d33edeff8c22c7d5792f4e7080c9f4f94b46efc327`; its original unsigned-varint stream is30,929 bytes, SHA-256 `1eb901d377a980259d61d79fd4a1260fe5beecb43de790273b6c2ff56fb44ea0`. Both are reconstructed and checked by the lossless compact source, not supplied merely as hashes. The complete regenerated y tree stream is2,263,951 bytes, SHA-256 `2dd6d27a5dba005a7546aa03dad3a01a4f408068f9164302c2edea4904859207`.

The convenience bundle C34_COMMON_BODY_GAPS_AND_PROJECTIVE_V3.zip includes the readable proof, the full capsule, pinned sources, regenerated outputs and auxiliary review materials. It supplements the literal capsule below; it is not its source of authority.


[Encoded source block omitted; the code in this passage is incomplete.]
