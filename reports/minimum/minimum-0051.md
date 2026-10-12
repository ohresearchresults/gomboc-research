# minimum-0051

AI research report · 2026-09-11 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

**The new result is a physical exclusion on explicit complete domains, together with stronger constraints coupling the actual covariance, the same Lambda, and genuine face incidence. No universal F≥10 theorem is claimed.**

The accepted conclusions are:

- For an arbitrary actual homogeneous nine-facet polytope, **TREE285 is impossible whenever**
  \[
  \operatorname{cond}(\Sigma^{-1/2}N\Sigma^{-1/2})\le\frac{1001}{999},\qquad N=M^{-1}.
  \]
  This covers the entire indicated metric sector, all shapes, all compatible incidences, and all weak-shadow equalities.
- For actual homogeneous nine-facet pyramids, with **arbitrary reciprocal SPD metric**, exact certificates exclude **37 of the 45 tree/base-label domains**. In particular, **TREE253 and TREE285 are completely excluded within the pyramid class**. The eight remaining pyramid domains are listed below.
- As an analytic consequence of the actual pyramid covariance and the certified base-root cases, **every homogeneous nine-facet pyramid has at least two strictly stable facets throughout the larger closed sector**
  \[
  \operatorname{cond}(\Sigma^{-1/2}N\Sigma^{-1/2})\le5+2\sqrt6.
  \]
- Independently, **TREE285 is impossible on the entire homogeneous affine-heptagonal-prism domain**, for every reciprocal SPD metric.

The computational conclusions use **38 exact records, 2,666 integer symmetric 9×9 matrices, and 23,994 positive leading principal minors**, checked by both integer Bareiss elimination and a separate Fraction LDL calculation. The complete generator and verifier were reconstructed and executed in clean directories with identical certificate bytes. The literal recovery capsule below contains every source byte needed to reproduce these results.

The new universal physical inequality is
\[
\boxed{(Hz)_i(\Lambda^Tz)_i\le\frac45(\mathbf1^Tz)^2\quad(z\ge0).}\tag{1}
\]
It has an exact two-slack reduction and a stronger extension using actual affine ranks and face incidence. These inequalities are **copositive assertions**, not signed Loewner inequalities. A separate new family of signed support-Hessian inequalities is also derived below. Its common rank-four kernel gives an exact barrier to direct mechanical-Gram contractions.

**Parent authority and exact bindings.** I used the literal immutable payloads

- `minimum-0048`, SHA-256 `90cd69cfe89b74ee6093225b2b6a5dedb495c93c47a96481a7bb23ac0ada05a6`;
- `minimum-0037`, SHA-256 `ae4df745aca2add81c72f0c89bec859bd3af211defc8e00d55b5b5766687b596`.

No conflict in their literal tree arrays or frame meanings was found. There is a notation collision: the capped-row parent sometimes calls the mechanical Gram matrix H. Here it is consistently called **G**, while **H** denotes the actual volume slack moment.

The five bindings are exactly

```text
TREE253 (0,0,1,2,3,4,5,0,7)
TREE266 (0,0,1,2,3,4,5,4,0)
TREE272 (0,0,1,2,3,4,5,5,0)
TREE278 (0,0,1,2,3,4,5,6,0)
TREE285 (0,0,1,2,3,4,5,6,7)
```

Here p[0]=0 is a root convention and each other entry means i→p[i]. These TREE labels are not canonical C32 labels. In particular the previously excluded canonical C32:285 is a different object.

For continuation, the literal parent's complete 25-frame table is reproduced here. Each inner list is an extra-arrow set added to its eight-arrow base tree:

```python
FRAMES={
253:[
 [(1,8)],
 [(2,8)],
 [(3,8)],
 [(7,6)],
 [(8,4),(8,5),(8,6)]
],
266:[
 [(2,8),(5,7),(6,7)],
 [(2,8),(6,7),(7,5)],
 [(2,8),(7,5),(7,6)],
 [(7,5),(7,6),(7,8)]
],
272:[
 [(2,8),(6,4),(6,7)],
 [(6,4),(6,7),(6,8)],
 [(2,8),(6,7),(7,4)],
 [(2,8),(6,4),(7,6)],
 [(2,8),(7,4),(7,6)],
 [(7,4),(7,6),(7,8)]
],
278:[
 [(1,8)],
 [(3,8)],
 [(2,8),(6,4),(7,5)],
 [(2,8),(7,4),(7,5)],
 [(7,4),(7,5),(7,8)],
 [(8,7)]
],
285:[
 [(2,0)],
 [(3,0)],
 [(7,0)],
 [(8,0)]
]}
```

An actual full nonnegative-shadow graph is a subgraph of one of these frames containing the selected base tree. Optional arrows are not mandatory, and a frame is not a facet-incidence graph. The accepted certificates below require only the base-tree arrows, so every compatible optional-frame choice is covered automatically. The later journaled frame sharpening is not needed for these certificates.

**One actual body and one reciprocal metric throughout.** Let
\[
P=\{x\in\mathbb R^3:q_i^Tx\le1\}
\]
be full dimensional, with all maximal facets retained, its own uniform-volume centroid zero, volume V and actual covariance Σ. Define
\[
Y=\mathbf1-Qx,\quad H=E_PYY^T=J+Q\Sigma Q^T,
\]
\[
d_i=\frac{A_i}{V\|q_i\|},\quad\omega_i=d_i/3,\quad
\lambda_i=\Lambda[:,i]=d_iE_{F_i}Y,
\]
\[
K_i=d_iE_{F_i}YY^T,\qquad G=QNQ^T,\quad N=M^{-1}>0.
\]
The same actual quantities satisfy
\[
\Lambda\mathbf1=3\mathbf1,\quad\Lambda Q=-Q,\quad
\Lambda H=H\Lambda^T=4J-H,
\]
\[
K_ie_i=0,\quad K_i\omega=\lambda_i,\quad
\sum_iK_i=5H-2J.
\]
The inherited signed cap remains a Loewner inequality with constant 25/12; the smaller nonnegative-affine bounds remain copositive. None is replaced by an assertion that a quadrilateral is a parallelogram. No polar is assigned its own fictitious centroid, and no fitted covariance or independently chosen facet measure is used as a mechanical witness.

**1. Affine-density lift and the sharp common-covariance inequality.**

For f=zᵀY≥0, z≥0, z≠0, put α=E_Pf=1ᵀz. Construct the actual four-dimensional convex polytope
\[
L_f=\{(x,t):x\in P,\ 0\le t\le f(x)\}.
\]
Its volume and centroid are obtained directly by Fubini:
\[
\operatorname{Vol}_4(L_f)=V\alpha,\qquad
(g_x,g_t)=\left(\frac{E_P(xf)}\alpha,\frac{E_Pf^2}{2\alpha}\right).
\]
The normalized cone volume of its vertical facet i, based at this computed centroid, is
\[
\frac{(Hz)_i(\Lambda^Tz)_i}{4\alpha^2}.\tag{2}
\]
Indeed, its centroid-to-support distance factor is E_P(Y_if)/α=(Hz)_i/α, and its facet measure divided by \(V\|q_i\|\) is d_iE_{F_i}f=(Λᵀz)_i. If f vanishes identically on F_i, this facet has zero measure and the left side is zero.

Here is a self-contained proof of the singleton cone bound used in (2). For an n-dimensional convex body with a facet of area A, let W(t) be the volume beyond inward distance t from that facet. Brunn–Minkowski makes W(t)^(1/n) concave. Its tangent at zero, where W(0)=V and W′(0)=−A, gives
\[
W(t)\le V\left(1-\frac{At}{nV}\right)_+^n.
\]
The actual centroid depth h is V⁻¹∫W(t)dt. Therefore Ah/V≤n/(n+1), or equivalently the centroid-based facet-cone fraction is at most 1/(n+1). Applying this in dimension four proves (1).

Equality in the singleton cone bound characterizes a pyramid over the chosen facet. This equality statement is also explicitly available in Freyer–Henk–Kipp, Theorem 1.2(i). [Primary source](https://arxiv.org/pdf/2207.08477).

For (1), equality at a positive lifted vertical facet is equivalent to **P being a pyramid over F_i and f vanishing at its apex**. The lift vertices are the endpoints (v,0),(v,f(v)) over vertices v of P. A pyramid over the vertical facet can have only one vertex outside it, giving exactly that characterization.

Taking z=e_a gives
\[
\boxed{H_{ai}\Lambda_{ai}\le4/5.}\tag{3}
\]
The constant is sharp: for any centered tetrahedron, the facet slacks are four times barycentric coordinates, so H_aa=8/5, H_ai=4/5 for a≠i, and Λ_ai=1 for a≠i.

Both the floor and roof of L_f have cone fraction E_Pf²/(8α²). Their singleton bound consequently gives
\[
E_Pf^2\le\frac85(E_Pf)^2.\tag{4}
\]
This recovers the actual three-dimensional affine variance bound directly from the same lift.

For fixed i, (1) is exactly copositivity of
\[
\frac45J-\frac12\big[(He_i)\lambda_i^T+\lambda_i(He_i)^T\big].
\]
It must not be strengthened to PSD without another argument.

The entire nonnegative-affine cone has an exact finite reduction. Set u_a=H_ai and v_a=Λ_ai, and normalize 1ᵀz=1. The attainable pairs (uᵀz,vᵀz) form a convex polygon in the positive quadrant. At a positive maximum of their product, its positive gradient exposes a boundary edge. Thus a maximizer uses at most two original points. It is enough, and necessary, to check every pair a,b and every t∈[0,1]:
\[
[u_a+t(u_b-u_a)][v_a+t(v_b-v_a)]\le4/5.
\]
Writing the product as At²+Bt+C, only its endpoints and, when A<0 and 0<−B/(2A)<1, the value C−B²/(4A) need checking. For nine facets this gives **324 complete quadratic interval tests**, with no sampling of f.

**2. Genuine affine-rank and face-incidence coupling.**

The following extension imports the explicitly stated affine-subspace concentration theorem: for a centered n-polytope, cone masses whose normalized poles lie in an affine subspace of dimension r−1 sum to at most r/(n+1) of the volume. This is Freyer–Henk–Kipp, Theorem 1.1. [Primary source](https://arxiv.org/pdf/2207.08477).

For any subset I of the original facets, let
\[
r_I=\operatorname{rank}[\mathbf1,Q]_I.
\]
Then the same lift proves the universal physical constraint
\[
\boxed{\sum_{i\in I}(Hz)_i(\Lambda^Tz)_i
\le\frac{4r_I}{5}(\mathbf1^Tz)^2\quad(z\ge0).}\tag{5}
\]
The rank is the actual common affine rank. To verify its preservation, let g=E_P(xf)/α. The centered normalized vertical poles are
\[
p_i=\frac{(q_i,0)}{1-q_i^Tg}.
\]
Multiplying their augmented rows by positive denominators produces [1−q_iᵀg,q_i,0], an invertible linear transform of [1,q_i]. Their affine rank is therefore exactly r_I. Apply the concentration theorem in dimension four and discard any additional nonnegative cone masses in that affine span. Vanishing lifted facets contribute zero and cause no exception.

For example, the facets through a true vertex have affine rank three. Four or more incident facets therefore satisfy a joint upper bound 12/5, while merely summing their singleton 4/5 bounds would give at least 16/5. This uses genuine incidence, not a declared coplanarity label.

There is also a lower bound involving nonincident facets. Let F be an actual face of dimension k∈{0,1,2}, let I(F) be its incident facets and J(F) their complement. If f=zᵀY vanishes on F, equivalently z≥0 is supported on I(F), then
\[
\boxed{\sum_{i\in J(F)}(Hz)_i(\Lambda^Tz)_i
\ge\frac{4(k+1)}5(\mathbf1^Tz)^2.}\tag{6}
\]
To prove it, the lifted face F×{0} has dimension k. Its incident poles, including roof and floor, have affine rank 4−k. The two horizontal cone masses together contribute h/(4α²), where h=zᵀHz. Thus
\[
\sum_{i\in I(F)}(Hz)_i(\Lambda^Tz)_i+h
\le\frac{4(4-k)}5\alpha^2.
\]
But the common physical identity HΛᵀ=4J−H gives
\[
\sum_i(Hz)_i(\Lambda^Tz)_i=4\alpha^2-h.
\]
Subtracting proves (6). The rank argument holds at nonsimple faces: incident normals at a k-face in dimension n span an n−k dimensional normal-cone space, and their normalized support equation identifies affine rank with that linear rank.

For a vertex v, the lower bound is strict unless P is a pyramid with apex v. Equality in the lifted vertex concentration theorem makes L_f a pyramid with apex (v,0). A vertex w with f(w)>0 has both lifted endpoints in the opposite base hyperplane, forcing that hyperplane's t coefficient to vanish. All original vertices other than v then lie in one plane. This uses Theorem 1.2(ii) of the same primary source.

For a true edge shared by facets i,j, (6) is a complete two-variable copositive condition. Put A=H_ii, B=H_jj, C=H_ij, x=Λ_ij, y=Λ_ji. The matrix
\[
\boxed{\begin{pmatrix}
12/5-A-xC&12/5-C-(yA+xB)/2\\
12/5-C-(yA+xB)/2&12/5-B-yC
\end{pmatrix}}
\tag{7}
\]
must be copositive. For entries u,v,w this means u,w≥0 and v+√(uw)≥0; when v<0 the latter is exactly v²≤uw. Thus the entire edge-function cone has an exact quadratic acceptance test. No claim is made that (7) is algebraically independent of every combination of all earlier physical identities; its physical derivation and full scope are established.

**3. Mechanical caps from the actual covariance, and the complete TREE285 sector.**

The actual covariance satisfies
\[
1/15\le q_i^T\Sigma q_i\le3/5.\tag{8}
\]
The upper bound follows from (4) applied to Y_i. For completeness, the lower bound has an elementary fan proof. Triangulate P from an actual vertex where q_iᵀx=1. In a tetrahedron of this fan, write m for the conditional mean of q_iᵀx. Its other three vertex values and Cauchy–Schwarz give
\[
E_T(q_i^Tx)^2\ge(16m^2-2m+1)/15.
\]
Average with actual tetrahedron volumes. The actual centroid gives E_P(q_iᵀx)=0, and Jensen gives the lower bound in (8).

Let ε=1/1000. If κ=cond(Σ⁻¹ᐟ²NΣ⁻¹ᐟ²)≤1001/999, a positive rescaling of N, which changes no shadow signs, gives
\[
(1-\varepsilon)\Sigma\preceq N\preceq(1+\varepsilon)\Sigma.
\tag{9}
\]
This is a genuine restriction on the physical covariance–metric pair. Whitening Σ does not make (9) automatic.

For a weak escape a→i, put u=Σ¹ᐟ²q_a, v=Σ¹ᐟ²q_i. Equations (8)–(9) imply
\[
u^Tv\ge(1-\varepsilon)|u|^2-\varepsilon\sqrt{3/5}|u|
\ge(1-4\varepsilon)/15.
\]
The final minimization is valid for ε≤2/5. Hence H_ai≥(16−4ε)/15. Applying (3) in both orientations gives
\[
\boxed{\Lambda_{ai},\Lambda_{ia}\le\frac3{4-\varepsilon}.}\tag{10}
\]
Symmetry of H is essential to the two-way conclusion.

A depth-d chain of weak escapes ending at an ancestor a satisfies
\[
q_a^TNq_i\ge-b_dq_a^TNq_a,
\qquad b_d=\cos^{d+1}\frac{\pi}{d+1}.
\tag{11}
\]
Here is the complete angular proof. Pass to Euclidean coordinates using the same N and normalize the ancestor length to one. Consecutive angles θ_j lie in [0,π/2), and the escape inequalities give successive length ratios at most cos θ_j. If θ is the endpoint angle, θ≤Σθ_j. Concavity and monotonicity of log cos imply an endpoint length at most cos^d(θ/d). A negative endpoint projection is therefore bounded below by cos^d(θ/d)cos θ. Its minimum on [π/2,π] is at θ=dπ/(d+1), giving (11). Nonnegative projections already satisfy it.

Combining (9), (11), (8) and the lift gives
\[
\Lambda_{ai},\Lambda_{ia}
\le\frac4{5-3b_d-3\varepsilon(b_d+1)}.
\tag{12}
\]
We use the inherited global 10/9 cap whenever it is smaller. The rational path bounds used are b₂=1/8, b₃=1/4, b₄<89/256 and b₅=27/64. The fourth follows from b₄=(11+5√5)/64 and √5<9/4.

For TREE285, every pair is an ancestor pair and its depth difference is |i−a|. At ε=1/1000 the exact coefficient caps used in the certificate are

| Distance | Cap |
|---:|---:|
| 1 | 1000/1333 |
| 2 | 32000/36973 |
| 3 | 3200/3397 |
| 4 | 204800/202393 |
| 5 | 256000/238727 |
| 6,7,8 | 10/9 |

The selected physical rows are 0 and 2. Their coefficient polytopes have respectively **228 and 268 vertices**, with common integer denominator **1693095553773352561689** in the recovery generator. All 496 extreme-row matrices pass exact positive-definiteness checks. The averaging argument below proves the whole claimed sector impossible; this is not inference from a locator failure or a sampled metric grid.

**4. Complete pyramid domains and their exact remaining set.**

Every actual homogeneous pyramid can be represented, without losing any physical metric, as
\[
P=\operatorname{conv}\big((B,-1),(0,0,3)\big),
\]
where B has its actual area centroid zero. All affine deformations are retained by the single arbitrary reciprocal pair M,N. For nine facets, B is an actual octagon.

Let p_j be the normalized edge poles of B, c_j^B its actual edge midpoints, Σ_B its actual area covariance, and
\[
\delta_j=\frac{\operatorname{length}(E_j)}{\operatorname{Area}(B)\|p_j\|},
\qquad\sum_j\delta_j=2.
\]
Writing b for the base facet and L for the lateral facets, direct support and uniform-triangle integration give
\[
q_b=(0,0,-1),\quad q_j=(4p_j/3,1/3),\quad
 d_b=3/4,\quad d_j=9\delta_j/8,
\]
\[
\boxed{\Lambda=\begin{pmatrix}0&(3/2)\delta^T\\\mathbf1&C\end{pmatrix},
\quad C_{ij}=\delta_j(1-p_i^Tc_j^B).}\tag{13}
\]
Thus C is the actual two-dimensional facet matrix of the own-area-centred base, not an assigned independent matrix. In particular, every lateral row has base coefficient exactly one and the remaining coefficients sum to two.

The singleton cone bound in dimension two gives δ_j≤2/3, so every entry of the base row is at most one. For the accepted certificates we use only:

- a lateral row: diagonal zero, base entry one, remaining sum two, every remaining entry at most 10/9;
- the base row: diagonal zero, sum three, every off-diagonal entry at most one.

The 10/9 bound is the literal parent's physical trace bound. The sharper planar trace cap was explored but is not required by any record in the final capsule.

The actual second moments are rigidly compatible with (13):
\[
\Sigma_P=\operatorname{diag}((3/5)\Sigma_B,3/5),
\]
\[
H_{LL}=(16/15)(J+P_B\Sigma_BP_B^T),\quad
H_{bL}=(4/5)\mathbf1^T,\quad H_{bb}=8/5.
\tag{14}
\]
These follow from the actual section density 3t²dt, horizontal coordinate tX_B, and vertical coordinate 3−4t. No covariance is adjusted to make the row constraints hold.

For every literal tree, all nine possible base labels b=0,…,8 are considered. The exact accepted cover is:

| Tree | Certified base labels | Remaining base labels | Integer blocks |
|---|---|---|---:|
| 253 | 0,1,2,3,4,5,6,7,8 | none | 476 |
| 266 | 0,1,2,3,4,5,8 | 6,7 | 392 |
| 272 | 0,1,2,3,4,8 | 5,6,7 | 308 |
| 278 | 0,1,2,3,4,8 | 5,6,7 | 350 |
| 285 | 0,1,2,3,4,5,6,7,8 | none | 644 |

This is **37 complete continuous domains and 2,170 blocks**. The only pyramid domains left by this result are exactly

```text
(TREE266, base6), (TREE266, base7),
(TREE272, base5), (TREE272, base6), (TREE272, base7),
(TREE278, base5), (TREE278, base6), (TREE278, base7).
```

They are necessary remaining domains, not realizations.

There is a further complete covariance-sector consequence for these eight domains. Let u=Σ¹ᐟ²q_b and v=Σ¹ᐟ²q_i for a lateral facet. Equation (14) gives
\[
|u|^2=3/5,\quad u^Tv=-1/5,\quad |v|^2=s_i<3/5.
\]
The strict last inequality holds for every actual octagon: the planar affine variance bound is at most 1/2, and equality would force B to be a triangle. Equivalently s_i=1/15+(16/15)p_iᵀΣ_Bp_i<3/5.

Normalize the eigenvalues of Σ⁻¹ᐟ²NΣ⁻¹ᐟ² to write it as c(I+E), with \(\|E\|\le(\kappa-1)/(\kappa+1)\). If κ≤5+2√6, this norm is at most √(2/3). Therefore
\[
q_b^TN(q_i-q_b)/c
\le-4/5+\sqrt{2/3}\sqrt{(3/5)(s_i+1)}<0.
\]
The base is strictly stable. In an S1 pyramid it would have to be the root, but all five base-root domains b=0 were exactly excluded above. Thus **every actual nine-facet pyramid in this closed κ-sector has S≥2**. Any pyramid S1 survivor of this handoff must lie in one of the eight listed domains and satisfy κ>5+2√6.

This does not confuse the journal's older all-pyramid theorem with an S1 theorem: the older result proves S≥2 **or** U≥2 and excludes joint110. That logical distinction was checked and retained.

**5. Why the exact finite certificates prove physical impossibility.**

For a selected tree define
\[
L_i=2e_ie_i^T-e_ie_{p[i]}^T-e_{p[i]}e_i^T.
\]
A weak escape gives tr(L_iG)≤0. Every actual selected row a gives
\[
Q^T(e_a+\Lambda[a,:]^T)=0.
\]
For the pyramid lateral-row polytope its 42 vertices are
\[
w/9=e_a+e_b+(10/9)e_i+(8/9)e_j,
\]
with ordered distinct i,j outside {a,b}. For a base row there are 56 vertices with three off-diagonal entries one. For the metric-sector rows the code enumerates all vertices of the individually bounded coefficient box intersected with the sum-three hyperplane. Completeness follows because at a vertex at most one coefficient can lie strictly between its bounds.

Each record supplies integer gamma vectors, nonnegative integer multipliers μ, and symmetric offsets O_a summing to zero. For each extreme w, with D_a=w[a], it constructs
\[
B_{a,w}=\gamma_aw^T+w\gamma_a^T+
D_a\sum_i\mu_{a,w,i}L_i+D_aO_a.
\tag{15}
\]
Every accepted matrix satisfies B_{a,w}−I₉>0 by exact arithmetic.

Decompose each **actual** coefficient row into its extreme vectors w/D_a with convex weights. Average B_{a,w}/D_a and sum over the selected rows. The gamma terms pair to zero with G by the actual row equations; the offsets cancel; the escape terms pair nonpositively. But the resulting matrix is positive definite and G is nonzero PSD, so their pairing is strictly positive. This contradiction proves impossibility on the entire stated physical domain.

The row polytopes are necessary relaxations. They are never asserted to be actual area measures. Their exact infeasibility is applicable because (1), the actual covariance restrictions, and the actual pyramid formulas prove that every physical candidate in the claimed domain maps into them. No rank-free feasible point is promoted to geometry.

Weak escapes cause no coverage gap. Along distinct actual poles,
\[
G_{p[i],p[i]}-G_{ii}
=2q_i^TN(q_{p[i]}-q_i)+\|q_{p[i]}-q_i\|_N^2>0.
\]
Thus the parent's true-edge escape-tree reduction includes weak-shadow walls. The certificates use closed coefficient caps and weak escape inequalities. They require no positive lower bound on face area, pyramid height, angle, cone mass or shadow margin.

**6. A complete additional physical subclass: affine prisms.**

For a homogeneous affine heptagonal prism, use coordinates P=B×[−1,1] with the actual area centroid of B at zero and retain an arbitrary reciprocal SPD metric. Its actual volume centroid is zero, its covariance is diag(Σ_B,1/3), and its cap poles are q_+=−q_−. Their N-norms are equal for every N.

Every pair of labels is comparable in TREE285. Strict norm increase along its weak arrows would therefore make the two cap norms unequal. Consequently TREE285 is impossible on the **entire affine-prism class**, including all compatible frames, arbitrary base shapes, shears, heights and metrics. This argument is analytic; no finite prism search or fitted moment object is used. No exclusion of the other four trees on all prisms is claimed.

**7. New signed support-Hessian constraints and an exact rank-four barrier.**

This is a useful further physical method, although it is not needed to accept the finite records above. Let f=a+bᵀx≥0, l_i=d_iE_{F_i}f, k_i=d_iE_{F_i}f², h=a²+bᵀΣb. For each genuine edge ij define
\[
\eta_{ij}=\frac{\operatorname{length}(E_{ij})}{V\|q_i\times q_j\|},
\quad\epsilon_{ij}=\eta_{ij}E_{E_{ij}}f,
\quad\zeta_{ij}=\eta_{ij}E_{E_{ij}}f^2.
\]
These are the actual shared-edge measures. Set nonedge coefficients to zero and define
\[
(B_1)_{ij}=\epsilon_{ij},\quad
(B_1)_{ii}=3l_i-ad_i-\sum_{j\sim i}\epsilon_{ij},
\]
\[
(B_2)_{ij}=\zeta_{ij},\quad
(B_2)_{ii}=4k_i-2al_i-\sum_{j\sim i}\zeta_{ij}.
\]
The actual edge-flux identities give
\[
B_1\mathbf1=3l-ad,\quad B_1Q=db^T,
\]
\[
B_2\mathbf1=4k-2al,\quad B_2Q=2lb^T.
\]
Vary the original supports and the roof offset in the four-dimensional lift. Brunn–Minkowski concavity gives
\[
\frac3{4a}\binom l1\binom l1^T-
\begin{pmatrix}B_1&d\\d^T&0\end{pmatrix}\succeq0.
\]
Eliminating the roof variable proves
\[
\boxed{R(f)=ld^T+dl^T-(4a/3)dd^T-B_1\succeq0.}\tag{16}
\]
The quadratic lift with two nonnegative fibre coordinates whose sum is at most f+r has volume one half of ∫(f+r)². It similarly gives
\[
\boxed{\frac4{5h}\binom k{2a}\binom k{2a}^T-
\begin{pmatrix}B_2&2l\\2l^T&2\end{pmatrix}\succeq0.}\tag{17}
\]
For D=8a²−5h>0 its optimized residual is
\[
R_2(f)=-B_2+
\frac{-4kk^T+8a(kl^T+lk^T)-10hll^T}{D}\succeq0.
\]
At D=0, retain the block form: it forces k=2al and gives the valid residual 2llᵀ−B₂≥0.

All these formulas use the actual K_i and actual edge moments: if f=zᵀY, then l_i=zᵀλ_i and k_i=zᵀK_i z. The PSD test vector in support space may be signed; the density f is required to be nonnegative.

For positive f, support-volume differentiability on the full nonsimple fixed-normal domain follows by applying the actual lifted-polytope C² theorem in Izmestiev, Appendix A.3. Boundary zeros are handled by f+ε and closure of the PSD cone. This avoids a generic-position assumption. [Primary source](https://arxiv.org/pdf/0704.0349).

The entire linear-density family (16) reduces exactly to the nine tests R(Y_a)≥0 because every affine f≥0 on P is a nonnegative combination of facet slacks. All these matrices share
\[
R(f)\mathbf1=R(f)Q=0.
\]
The optimized quadratic residual, including its D=0 form, has the same kernel. Thus they act on one common quotient of dimension at most five when F=9.

This gives an **exact barrier**, not a numerical observation:
\[
\operatorname{tr}(R(f)QNQ^T)=0,
\]
and every optimized test confined to span{1,Q} is identically zero. Direct mechanical-Gram contractions cannot strengthen the tree certificates. The true edge graph also cannot be replaced by the sparse shadow graph.

A nontrivial next test uses r_i=G_ii. Expanding rᵀR(f)r≥0 gives
\[
\sum_{\{i,j\}\text{ true edge}}\epsilon_{ij}(r_i-r_j)^2
\ge\sum_i(3l_i-ad_i)r_i^2
-2(l^Tr)(d^Tr)+\frac{4a}{3}(d^Tr)^2.
\]
This preserves the actual common edge conductances and physical squared norms. No whole-tree contradiction from this energy inequality has yet been established.

**8. Complete recovery capsule and exact acceptance.**

The compact source unit below contains the complete literal compressed bytes of the generator and frozen checker. It has no missing helpers, unavailable checkpoint file, URL dependency or omitted coefficient array. Decoding reconstructs the entire source, which deterministically generates every accepted coefficient and checks every matrix. The mathematical hypotheses and the averaging proof are stated above; the program proves their finite matrix acceptance.

Reference environment: **CPython 3.12.14, NumPy 2.3.5, SciPy 1.17.0, threadpoolctl 3.6.0**, x86_64; both numerical libraries used OpenBLAS 0.3.30, pthreads, SkylakeX. The producer fixes one BLAS thread, uses no randomness, and fixes all numerical parameters in the recovered source. They are: initial margin −1; zero free coefficients; local multipliers 1/8; τ=0.05·0.18^outer; at most 12 outer rounds and 70 Newton steps; decrement tolerance min(1e−7,0.001τ); positivity factor 0.99; Armijo factor 0.05; at most 60 halvings; symmetric solve with least-squares fallback rcond=1e−14; candidate margin >1e−8; max-absolute normalization followed by np.rint at scale 10^8. Acceptance is exact Bareiss and Fraction LDL, not the floating-point margin.

Save the following source as `restore_vivid.py`, UTF-8/LF with final LF. Run in an empty directory:

```text
python -S restore_vivid.py > capsule_replay.log
python -S recover_vivid.py check
sha256sum restore_vivid.py recover_vivid.py vivid_physical_certificates.json capsule_replay.log
```

Observed pins:

| Object | Bytes | SHA-256 |
|---|---:|---|
| restore_vivid.py | 5982 | 64295be94e55a9f49e8801cfbb015d48c2c12d9abec1630fea41253f0c20cdc2 |
| recover_vivid.py | 8922 | fdcc64d930ea73817c53982e285588ba15a7b64f56e74cdb292a56606837eabe |
| vivid_physical_certificates.json | 207967 | d97eee464249e704b0217ddd6dbcbf5732e24a8776129cd6740ecc2645a0bdc9 |
| capsule_replay.log | 795 | 0f8d7677222407623a2f9931e9cb02e034c5a8b9c3e491d458a3fd0f18088d9d |

Each individual build/check transcript is 365 bytes, SHA-256 `e937d614e1cf200fc7281b5c13955a4042ff76b3e751740815e9919dacb65f3f`. The exact leading-minor stream has SHA-256 `89d79bf39767516abf136b85cc7951bb1e77ec4de1d41f0ad1859f102ac2f69c`.

Expected acceptance markers, printed twice by the wrapper before its final marker:

```text
EXACT_BAREISS_AND_FRACTION_LDL_PASS 2666 23994
PYRAMID_COMPLETE_PAIRS_37_OF_45_TREES253_AND285_WHOLE_PASS
TREE285_ALL_SHAPES_METRIC_CONDITION_LE_1001_OVER_999_PASS
DATA 207967 d97eee464249e704b0217ddd6dbcbf5732e24a8776129cd6740ecc2645a0bdc9
MINOR_STREAM 89d79bf39767516abf136b85cc7951bb1e77ec4de1d41f0ad1859f102ac2f69c
VIVID_RAVEN_PHYSICAL_LIFT_AND_PYRAMID_V1_PASS
```

The wrapper finishes with `VIVID_COMPLETE_LITERAL_SOURCE_RECOVERY_AND_TWO_EXACT_CHECKS_PASS`. A fresh end-to-end wrapper reconstruction was actually executed successfully. These are exact computational checks, not proof-assistant formalization or external peer review.

```python
"""Complete source recovery; CPython 3.12.14, standard library.
Build dependencies: numpy2.3.5 scipy1.17.0 threadpoolctl3.6.0.
Run: python -S restore_vivid.py
"""
from pathlib import Path
import base64,hashlib,subprocess,sys,zlib
assert __debug__
B=r"""
c-oaYX>;2;lHc_!xT)GDDM2zx-C~d$`N)g&<fAOVyqVRiSUez^77r~CDazFQ@7oQK6eT+|S;r2EMt7qxG`hhLA3l7${dRk8Jx#ye
+*^-d{xQG3n$E1*?dNA}dVg&_{^MzS2lL<bPU9*Lw*kwT<iUSQ=tq8<`L2{OH;&RQ$=%G4Bgu|DiG8=-Oj;%J4;D%83v)Lt0s6;7
_5v8)j&5}Ho+&xGA9xcf%ERr!=yW@MDRuqrLGS3pjwWR<3A4Rz90zU|bUTBN1}u=56viHt@|2~3!=yBWCGEtM0^dpO<RHaSaOg<W
G-U}&luBWqW|G4s7THd~yiVi8hYt;qE(8&6SK#>JHcm3>a{-X-RQfD%d{8z6DJmQ{4jn(TIh{ZW?d+wT4ct%ww*Ul@O86rT8^!yJ
o#GUEP2-59hqPgHVI|A*n3Jz9tMNE}y19Rz)5Suz)3ue%?*9AF{qXU*-=BZWRz~_&yUc$35y?azYpypKyDK&tJHsAh18v+jjJ{(y
1H11r&*_c(?zrprhW2>S8|n7Yag46*YPM%<eS07;NkbB=Y&Q0N6z#je&%eamFWTLmd$_-wZ|1Oy&3fKy*z4P_ZP=bS(%qr4(p*@R
xugEr@w)cP&~=Zk+!50>uitmz-*7M(jD}8s467^~&rdfubNWxC-<>EL(TGkA(j`68hxegMjKSa>-Xod{(iubJe5Q{x#&C2FA8`1n
{}w(}|7!ekfA#R~=IQ2|E)-af3{=9OLwpVm(l4Ha;wj*x0zN9>BY=Z8)8DB4tD8q|JpA!Y<(<FtJ!|`NNPX81EEfZG1+N)PI~WUc
<L2*=H&@RnprH-NgCUW<@sKgr8}y9cm<_d_qZ#_p^SpuQxX!9S>>AAI*`wibpc`Wdg<(%)u4@dySDNFwV|m$VfLo+(U`MH<P8w32
XLPY_NUJ!JvV<|ok0kCJnBzdlPB}2Kqcu~;NFz!9N>UJ;;H-+%l{F`j05U(y8R8}JKBWt7i3FTcu?nT&c!>o7S%7Dj@AFg?z!LU`
XX&5P{ylt-ATCsOQmk|2R4g*;^Av;}Khb`LW^go6y<=~;Eb<gZ-X0P=^gWqWA`rw@)y64a$g;$DWeh8FA4iOEc8Hd+EKefD7B=29
fBllB%Epg8vK1_CG#`kEFiNXM(WU^kDMhSFAsqLMaDt2GsHYlb;qwW<?i%Fb{|B{~q$}Jc?a}znvAJK^OFHJDiprhr7k&w?>9|)B
QY4{(MGDNRl=cVQp+_Y_WDl(QGdZLv&bSk8;n1a7sZ<dFgGs64YaLK%@+t<WYU~%t4+J;4{JI9u*Cid9=Q_Mmp=UHsH7GC&ZxpWO
5tHR`x+z;A;+tUs?gq)(Hl?2xo#>jTsph{_AKlQ9oD@>r1W86J>GBr{+aA1(#>D7DNcZ907?MFx{mXQ1;Q!CR8gC5bv2FH3Z6{Uy
wvDO*CJLgFu_{7GU{HO6GjJL!@Fbs=u6m*L+90-C$3xDJFtkIRbisj3^OUp)r2Tfc>A)W_Xev%iSJh(i6fF<WhICEgj8mG*uH&&N
4lzDKcvN7=gA8yxJ3Gi3q#L9bI{Fho%9LI6S{1sIBQl(@A>jUH)-%(lW{iZT*@@i&UYLASMptO3o1;r~V<h&&NgQ35k(Uw9hC%7U
5=g%auAo+Nh`c_1%Kl3i`=!txXLq#Qyl$s?sNhU35Rkq|MA}EX`zVMuOW?3s(p^1LMWF3#2_%K0fO$&FG9I?7$R<t@yPFh5b5XKw
5tcAq$e6L<NHuwO;}Cq4m*!fG*6<qU;yuh^5G52h1<!BQCWsQgTj7*c`3^vgHN^k886_>H*GFZ5kQyRwYez~u2$bxwWy%ghA6yY-
NB^%+(fG2!bi|i<hY-QLPgFZ{NJNNm>B1b-@oEK?5c-i%SoN*9Y*b>R|1zqN>iOp646BlkfcmhPCcqm!3F)Lo*NY5N7K~q)04l~=
i|P$&Lp2eW39-*22TfX@oO_%rPXTUyOf*npZ3!P?8iSE7#JQ#zmFC(GVX1L5nZRFb%;W45^aVJG(Zp2O!f0zE0N$^gmCQ{=N9{p*
P57v-tLIvRiQbx{I%akxJk=-6Az+DKY=+ClZVA6FYBaB#p~;6^_;1;!V$28d$Hz#r;r4pZ1D7bX514%Z;IqJ!E{_?R@(4wLi|Dr#
=BKGLMM<V~kt`<5V^~a=W?(~7&`qdn_AEI~8+E5|{au{VDJTWMX0aFte$w#7;N<1j<Z$(E{A^k}`4=(7O|^qXgi|<|HXm)4O}_Li
H+ZS*?mxNk7*p_5kO4W5JG#5Lz-gG{Se#pxDulekM1dCw^UNSxJ}a8~&hB^zWI}bhG@*&Z^F%#2;G11D6K>;P^MGV3#wyQ(vqH%x
#0NajUEr%~X>yO7`?|EWr=kQ+>Q(bBtDh&da&1Y0#|I#(rF-g5IJ#$67*Rn%U+aRtazRUhe<H1V;k|2W-o*0iIkEQ?dpQLvdbNWs
s^uIqJnPKZd8Js!cY@gVVE^0uV=9EXh3tcZnV%ixB@`Lc-+1cd6I%%OC`%DubbhCVa2opo^an66>lavy$VXyP#8^;-dp=f*mJ{cg
bP!k5^o#L$ET6K=BRAf$gh4MN%28`;`w3ru5kOb3d>5hg{iMuaHh8a}Kn=vX6a%^1RXo)TASC=Q<Y5;i$*5+ga9}}}EBf9}`eH*R
q^LzoWiG+)1Q+|^Z%Y=W=vcU4ixn32oLV~xPqJ(6JOqWfKFF$8A94&~bGbx$d%Bi^cFBvUlfxJ|(K10@Rv`|>JZ{NLUI+-4JNeeb
tg7(1@bYk*LUo)nSRA7~r3y6HM4rg1+LHe#lGP3a-*^nvHo5V5HZAxIYf|WlpfKP15jYDi4q-;lEQ_$t3;XW*YbZ>V;*czxOFVh8
RL5p!Qf0)5(h>o<C%E0@o4-%5o~=s=$=msy_q3m%0CM|qZ_Tb}*5h<OmkAe(jGO$aR<vdJd-ZVlIJ<ei0qonSxz!z751*}G-{J;`
E)Us4t!@4J<zaRsSRR=m5>8HMGi&~3`gk+9?rxr+Zm)pt{q?Po<i^4{w=haA2=;Rx*VE^zOdu;qN7&u%{lk+r2lmrDnH0XN8SIGp
t1W)Hs>sYSHucJuH<V;ADuj??A`0y-)<hhrn$ZfXt*SC>_4-Yv8o^m^dNf+KAOdb_wC%71=45k*?>|@)r;0KnW5|5PM#^jTFXqG9
B5&&?C;5^ZW;xg{a@ZDPgzq@ph84cnxQ4_Nd`(_?iRh{1`lL_(UlkTV<eVCN!P;5)1gkC`-d>5%-(a~i-8<^96kHkD@pKyOx=5B{
RoFdeCSOcoPBr%^jh!U+0r1s}J=S6G7cE~G7}`k-juaq)>YOFYEu0}_ueK_{o*<~K|IZ91xTZ(0bq5#SuBhQsyemm4tsxZapF~JH
IS-i>`n2UyC9tA;tPIntG6W|tCZw%{!*3hX;ph=Kj1LPA*UcQks~qZd2m@$g^@~vlC^4!-8xET9%HcrrT%8oBB*vv5p_%2-^IwVA
{uKJJGWkjXFWzQ;=>K5!ImsC}ScSVG8~?Sy&2ut4!)-tbT&_p*A{Mx{>rEcFUuNgDqxG8|ebj7n6mw;}6u=i@8K_ZICmd?R@a{_-
pt=Fn9KpJSLzZq1n9`qWa6j4=N&SjGfdw&dF8}rw>Zs#rhSTc<Z39`B*e+A9i2dD9b!zaZLAz=PHOB$fRCCQO4#n^V2+N7{8u9fT
;<kQ~Bife(cif51L-y*oKY2_hSMcxLkU*24(rl2%Lz-~o$>jPcMEP5yKoA8;bp1XNn1n|nw=@J$eSn+%B8O^`Uo5?(xB%2Gm@FfH
OoF6H04C*WXatRjO4i7;Fto}ILJe`op12Q2I|dwb0-ROznF4?lPQ0bbsu2u!$3aWnAI@v(31A4v6jj?IEuAkpUran?NWl;76Z3c^
+%Vw<)Z+Oa>u_SAeM<;*f{dM!ne&BMub|~)WWjheakkC^5!&lR>*suT=X{+7(Cm&(=2V%t=ACEtf;%Tm4wE!vTPmzNCk}y10g|j`
Q#n0^aO`7AY_0sr&lvq|LyqBm*msw0GwFsupc)lij$R7VEd5{3FTskH>a4BzRA}yz*gH@}M}15W_QUSnQkY#fG8or8PcCiN<fNWp
#8MZkI|_TNsjLrw^A0U#oj1K)Y(f>g4>w^U;<O9oB7IjA(nksJ#z4R!fn?I`K#`$N94HkwyaEiiFE+nD(>tUy9yeD|_GbzRjIegT
@bZt^^1>@#pts-`6|ftkgMuJcBxb$CFMk7%wna+dG8;`aS-eJmo^P*XFrI=5sz?lakr)iM(5O}5R~ia41eskWQm~nqtK~W8*lw-&
85Ai|g7k7|aow8U!Gs);m!sUgyrh@qh;!x?7%Jizb6?)grXqJjhinI+<G)w(->P_`qg0sHPem*$u#C9Rf|rjJ4BNufp%k0D`sl?n
UXOCm{Ae1iZ;~WVCR>Pk(YSMJ+UfHU2e*~SA0{P!odKoQCFMsWxx5rNuUykl5I>_5`>>b*2vGS{)oF4j;?@H{iSj;k9mI|ufLw&{
z()BUF@}25P9i^Ar?ndoMSgg^xxbuE=hponch>V4C~U9s!yOdgXOO$!XD1MK5~t90?EEB-@UBwU<!UkhX%@eQM%xO;ztJ`%{*9Br
7ly0mPsBa>id%Iu=^^bv1DayD>PM@1G3i1drgVvJ5Xc4<9tMVGm6#S0>(wDA{OdE&fhscpsth`dPs;GZzawLBa7uR^SpnpfELFsV
V$v_o-C6ko6c^=Ck^OZPCy?&(_*%ya<gS`Iia7dHV5`U8xw@&sk3^@Rp3sxW?{w9bFCs0?J$}e~{|gi6$IE2ovJ^Mwd63b!eTZ4L
z=%-q1c@Tg9<HX(&=>u2|NH&JpZ793l@Yhw8iF^plQp!9f`ys7cEBLTeCMeT9{AB>t@4Av9OmLP!rI6D!27E81*dE3TC+J)J9f%%
g>f54*`TL(vY2<}NR=O{@?WO{b5qZEGj1wcDMBl4_=h(lZULyU5aniC)3r}RNPPZJZvc+HzgP(!TQ)9;(7<~Zv3z;wgBL!<YH4}N
LyCKy>QaZif0t9c$RQ%-@t>bu<Iw8HhLkZ^-pYvUtNLXG$Vu??gSBCYl%J%(bUV?Ij(1@D1hQ^%2`28mircbA1CpR+MK)9o7NxRf
g|-h{Q=U`}B_;xhrk#pk88By;fQ63tSDcYNDfx-ad-|QP#sP0Aiv-&EKTWaZ)c
"""
b=zlib.decompress(base64.b85decode(''.join(B.split())))
assert len(b)==8922 and hashlib.sha256(b).hexdigest()=='fdcc64d930ea73817c53982e285588ba15a7b64f56e74cdb292a56606837eabe'
Path('recover_vivid.py').write_bytes(b)
subprocess.run([sys.executable,'recover_vivid.py'],check=True)
subprocess.run([sys.executable,'-S','recover_vivid.py','check'],check=True)
b=Path('vivid_physical_certificates.json').read_bytes()
assert len(b)==207967 and hashlib.sha256(b).hexdigest()=='d97eee464249e704b0217ddd6dbcbf5732e24a8776129cd6740ecc2645a0bdc9'
print('VIVID_COMPLETE_LITERAL_SOURCE_RECOVERY_AND_TWO_EXACT_CHECKS_PASS')
```

**What remains and the useful continuation.** No unrestricted universal tree among the five is wholly excluded here, and no physical nine-facet S1 realization is supplied. The full unrestricted problem remains outside the explicit cuts above. The C32 whole-type register remains **203 excluded / 93 remaining**; these results do not add whole canonical types or improve C≥32.

The most consequential next targets are the eight exact pyramid tree/base domains, now necessarily outside κ≤5+2√6, and the four other universal trees under the new common-covariance constraints. For arbitrary genuine nine-facet geometry, impose (1), the actual affine-rank bounds (5), the complete true-edge test (7), and the vertex version of (6), together with the parent's signed-cap Schur completion and actual K_i flux. Keep all rows and columns tied to one actual H and Lambda. For support-Hessian work, use test vectors outside span{1,Q}; the zero-contraction barrier above proves why staying inside that carrier cannot help.

I also explored tighter scalar caps, additional frame signs and additional coefficient rows. Those searches produced no further accepted certificate. Their non-success is not evidence of feasibility or infeasibility. Only the exact records reconstructed by this capsule and the separately proved analytic inequalities are promoted as durable results.
