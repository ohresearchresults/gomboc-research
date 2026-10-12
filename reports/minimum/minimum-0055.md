# minimum-0055

AI research report · 2026-09-11 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

**Unrestricted TREE285 exclusion.** No full-dimensional homogeneous convex three-polytope with exactly nine maximal facets, at its own uniform-volume centroid, can satisfy
\[
q_i^TN(q_{i-1}-q_i)\ge0\quad(i=1,\ldots,8)
\]
for one reciprocal SPD metric pair M,N=M⁻¹. Thus the actual nonnegative-shadow graph has no directed Hamiltonian path. This excludes the entire literal TREE285=(0,0,1,2,3,4,5,6,7), with no covariance conditioning, simplicity, adjacency or root-stability assumption. All weak-shadow equality walls are included. TREE285 is different from canonical C32:285.

The proof combines a new physical mixed affine-density lift with an exact finite certificate: **9072 integer matrices and 81648 positive leading principal minors**, checked independently by Bareiss elimination and Fraction LDL. A separate audit checks the complete row-domain cover using all 504 permuted cut normals. The physical lift proof was also independently reviewed. The result reduces the inherited five-tree/25-frame frontier to **four trees and 17 maximal optional shadow frames**. It does not prove F≥10 or change the journal's accepted C≥34 register.

I read the current attached journal and its literal immutable parent `minimum-0051`, SHA-256 `44c83c1927a113cf61cd20954992725b784844da4dcd8cb115c4dfc2329aed6f`. No array, incidence or frame-binding conflict was found. Historical global counts in that payload are superseded by the current assignment's C≥34 state. No journal was edited. The complete new generator below needs no parent source file or discovery checkpoint.

**Actual common data.** Let P={x:q_iᵀx≤1}, E_Px=0, V=Vol(P), Σ=E_Pxxᵀ, Y=1−Qx, J=11ᵀ, and
\[
H=E_PYY^T=J+Q\Sigma Q^T,\quad d_i=A_i/(V\|q_i\|),\quad\omega=d/3,
\]
\[
\lambda_i=\Lambda[:,i]=d_iE_{F_i}Y,\quad K_i=d_iE_{F_i}YY^T,
\quad G=QNQ^T,\quad N=M^{-1}>0.
\]
All expectations use the actual uniform volume, area or length measure. For a true edge ij, put η_ij=length(E_ij)/(V||q_i×q_j||); nonedges have no edge measure. Divergence gives
\[
\Lambda_{aa}=0,\quad\Lambda_{ai}>0\ (a\ne i),\quad
\Lambda1=3\cdot1,\quad\Lambda Q=-Q,\quad
H\Lambda^T=\Lambda H=4J-H,
\]
\[
\operatorname{rank}H=4,\quad\operatorname{rank}K_i=3,\quad K_ie_i=0,
\quad K_i\omega=\lambda_i,\quad\sum_iK_i=5H-2J.
\]
Indeed, for actual facet centroids c_i, ∑d_i=3, ∑d_iq_i=0, ∑d_ic_i=0 and ∑d_ic_iq_iᵀ=I. These imply the row equations and H identity. Integrating div(xYYᵀ)=5YYᵀ−1Yᵀ−Y1ᵀ proves the K sum. No polar is recentered independently and no covariance is fitted.

**Physical mixed-lift theorem.** For nonzero nonnegative affine f=a+bᵀx and g=c+eᵀx, define
\[
h=E_Pfg,\quad l_f[i]=d_iE_{F_i}f,\quad l_g[i]=d_iE_{F_i}g,
\quad k[i]=d_iE_{F_i}fg,
\quad v=k-a l_g-c l_f,\quad D=8ac-5h.
\]
Let B_ij=η_ij E_Eij(fg) on true edges, zero on nonedges, and
\(B_{ii}=4k_i-a l_g[i]-c l_f[i]-\sum_{j\ne i}B_{ij}\). Then
\[
\boxed{\mathcal S(f,g)=
\begin{pmatrix}-B+l_fl_g^T+l_gl_f^T&2v\\2v^T&D\end{pmatrix}\succeq0.}\tag{1}
\]
The matrix test vector may be signed; the two densities must be nonnegative. Every nonnegative affine f is ∑z_iY_i with z_i≥0, since −b/a belongs to conv{q_i}. Bilinearity therefore makes the entire family equivalent to the 45 unordered PSD tests S(Y_a,Y_b), a≤b, at F9. This is a signed Loewner statement, not copositivity.

For a proof, initially take f,g>0 and form the actual 5D convex lift L={(x,t,u):x∈P,0≤t≤f(x),0≤u≤g(x)}. Under original-support variations h_i near 1 and roof-offset variations r,s near 0, its volume is F=∫_{P(h)}(f+r)(g+s). At the reference body,
\[
F/V=h,\quad\nabla(F/V)=(k,c,a)^T,\quad
\nabla^2(F/V)=\begin{pmatrix}B&l_g&l_f\\l_g^T&0&1\\l_f^T&1&0\end{pmatrix}.
\]
Shared-edge differentiation gives B's off-diagonals. Simultaneous scaling of original supports gives B1=4k−a l_g−c l_f, fixing its actual diagonal. Fixed-normal volume is C² also for nonsimple polytopes in this dimension; see [Izmestiev, Appendix A.3 and equation (4)](https://arxiv.org/pdf/0704.0349). Minkowski containment and Brunn–Minkowski make F^(1/5) concave, so its normalized Hessian obeys
\[
\rho(k,c,a)^T(k,c,a)-\nabla^2(F/V)\succeq0,\qquad\rho=4/(5h).
\]
For w=(c,a)ᵀ and J₂=[[0,1],[1,0]], the roof block is ρwwᵀ−J₂, with determinant D/(5h). If D>0 its inverse is −J₂+[ρ/(2ρac−1)]J₂wwᵀJ₂. Its Schur complement is precisely −B+l_fl_gᵀ+l_gl_fᵀ−(4/D)vvᵀ⪰0, equivalent to (1). Replace f,g by f+ε,g+ε for boundary cases: D_ε=D+3ε(a+c)+3ε²>0. Convergence of all actual integrals and closedness of PSD prove (1) even when a lifted facet disappears. This also proves D≥0.

The actual identities 1ᵀl_f=3a, Qᵀl_f=b, 1ᵀk=5h−2ac, Qᵀk=cb+ae and BQ=l_gbᵀ+l_feᵀ show S(1,2)ᵀ=0 and S(Q,0)ᵀ=0. The common affine kernel is retained; direct contraction with diag(G,0) still vanishes.

For different facets i,j, set s=Λ_ij,t=Λ_ji,h=H_ij, all positive. Since Y_iY_j vanishes on every true edge incident to i or j, the principal block on i,j,last is
\[
\begin{pmatrix}t&st&-2t\\st&s&-2s\\-2t&-2s&8-5h\end{pmatrix}\succeq0.
\]
Its minors and determinant st[(8−5h)(1−st)−4(s+t−2st)] give
\[
st\le1,\quad5h+4s\le8,\quad5h+4t\le8,
\quad5h(1-st)+4(s+t)\le8.
\]
In particular **Λ_ij+Λ_ji≤2**. Equality forces s=t=1; the full PSD kernel then gives Λ_ik=Λ_jk for every other k. Parallelism is not inferred. Actual heptagonal-prism caps attain equality.

Multiplying 5H_aj+4Λ_aj≤8 by Λ_aj and summing uses the SAME HΛᵀ=4J−H and proves
\[
\boxed{\sum_j\Lambda_{aj}^2\le1+\tfrac54H_{aa}\le3.}\tag{2}
\]
Here H_aa≤8/5 has a short physical proof: the 4D lift 0≤t≤Y_a has volume V, centroid height H_aa/2, and floor-cone fraction H_aa/8. An nD centroid facet-cone fraction is at most 1/(n+1): if W(t) is inward remaining volume from a facet of area A, concavity of W^(1/n) gives W(t)≤V(1−At/(nV))_+^n; integrate to bound centroid depth. Apply n=4.

For actual F≥5, ∑Λ_aj²<3. Equality would force H_aa=8/5 and every positive weighted pair gap to vanish. Substituting 8−5h=4s into the determinant gives −4st²(s−1)²≥0, hence every off-diagonal s=1 and F−1=3. Tetrahedra attain 3; five sufficiently small successive vertex truncations show it remains a sharp supremum at F9. The certificate uses only the closed bound ≤3.

The stronger common-Lambda energy
\[
\Phi_a=\sum_{j\ne a}\left[s_j^2+
\frac{s_jt_j(s_j-1)^2}{1-s_jt_j}\right]\le1+\tfrac54H_{aa}\le3,
\quad s_j=\Lambda_{aj},\ t_j=\Lambda_{ja},\tag{3}
\]
follows by the same weighted sum of the determinant inequality. At s_jt_j=1, necessarily s_j=t_j=1; define the summand as 1. This is a valid lower-semicontinuous boundary convention, not a path-independent rational limit. Equality classification for Φ is not asserted. The old capped row (10/9,10/9,7/9,0,0,0,0,0) has squared norm 83/27>3 and is excluded. Even the positive row (1109,1109,777,1,1,1,1,1)/1000 has norm²=382937/125000>3 while every entry is below 132/119, an attained lower bound on the sharp individual cap. These are coefficient-domain exclusions, not physical witnesses.

The inherited actual trace lemma supplies Λ_ai≤c₃<10/9, where
\[
c_3=\max_{r\ge0}\frac{3(1+2r+3r^2)}{(1+r+r^2)(3+2r+r^2)}.
\]
This is the only older scalar physical input needed. The trace target is m(∫_{t=0}y/||∇t||)/(∫_P y)≤c₃. Its thin-layer proof applies one-constraint s=1/3 localization to nonnegative affine t,y, with m=E_Pt and t=0 a facet. A segment has t=a+Ls, squared-affine density ((1−s)u+sv)² and y=(1−s)p+sq. Normalize u+v=p+q=1 and put A=(u²+uv+v²)/3, T=(u²+2uv+3v²)/12, W=p(A−T)+qT. The mean constraint is m=a+LT/A. A continuous ε-layer yields uniformly, for any putative C>c₃,
\(C(m-\varepsilon)/m<pu^2T/(AW)+36\varepsilon/(m-\varepsilon)\le c_3+36\varepsilon/(m-\varepsilon)\).
The uniform bounds A≥1/4,T≥1/12,A−T≥1/12,W≥1/12 justify this limit; Dirac or constant-t alternatives cannot violate the layer objective. The localization statement is in [Fradelizi, pp.3,17](https://arxiv.org/pdf/0807.0080). Set t=Y_i,y=Y_a, so m=1 and ∫y=V. Strictness follows from the exact positive identity
\[
10(1+r+r^2)(3+2r+r^2)-27(1+2r+3r^2)
=(r-7/15)^2(10r^2+118r/3+203/15)+44r/675+178/3375.
\]

**Finite continuous-domain cover and exact contradiction.** For actual rows a=0,2, the eight off-diagonal entries x lie in the closed polytope C: x≥0, ∑x=3, x_i≤10/9, and all permutations of
\[
(10,10,7,0,0,0,0,0)\cdot x\le27331301/10^6,
\quad(10,9,8,0,0,0,0,0)\cdot x\le6777721/250000.
\]
Cauchy–Schwarz and (2) justify these cuts: the rational thresholds exceed √747 and √735 by exact squared excesses 14352601/10¹² and 1953841/62500000000. C is a necessary outer approximation, stronger than the old capped rows.

Sorting x decreasingly reduces all permuted cuts to those displayed. The chamber has one sum equation and 11 inequalities: seven ordering inequalities, x₈≥0, x₁≤10/9 and two cuts. All 330 choices of seven active inequalities are solved with Fraction arithmetic. Full-polytope active rank removes ordering-only artifacts, leaving exactly:

```text
(10/9,10/9,45981709/63000000,1006097/21000000,0,0,0,0)
(10/9,7993399/7650000,126144179/153000000,995947/51000000,0,0,0,0)
(10/9,2117617/2250000,2117617/2250000,2461/375000,0,0,0,0)
(402721/375000,722279/750000,722279/750000,0,0,0,0,0)
(481237/450000,481237/450000,7640987/9000000,36511/3000000,0,0,0,0)
(777721/750000,777721/750000,347279/375000,0,0,0,0,0)
```

Orbit sizes are 840,1680,840,168,840,168: 4536 vertices per row, denominator D₀=1071000000. Every full-polytope vertex is a vertex of a containing sorted chamber. At a tied coordinate block, maximizing normals permute within that block; their differences span its zero-sum subspace exactly when the cut coefficients vary there. This gives the complete rank-eight criterion, including ties. The independent audit enumerates all 504 actual permuted normals at all 38 feasible chamber vertices, finding rank counts {1:1,2:2,3:3,4:7,5:7,6:7,7:5,8:6} and the same six patterns.

For i=1,...,8 put L_i=2e_ie_iᵀ−e_ie_(i−1)ᵀ−e_(i−1)e_iᵀ. The weak chain gives tr(L_iG)≤0. For each selected row and each vertex, insert D₀ into D₀x at coordinate a to obtain w. The complete source freezes 63 integers specifying γ₀,γ₂ and a symmetric offset O, and reconstructs nonnegative integer μ_(a,w,i), such that all 9072 matrices
\[
B_{a,w}=\gamma_aw^T+w\gamma_a^T+D_0\sum_i\mu_{a,w,i}L_i
+\begin{cases}D_0O&a=0,\\-D_0O&a=2\end{cases}
\]
satisfy B_(a,w)−I₉≻0. Every leading minor is checked by both exact algorithms.

Average B_(a,w)/D₀ according to each actual row's convex decomposition and sum the two rows. Offsets cancel. Since Qᵀ(e_a+Λ[a,:]ᵀ)=0, gamma terms pair to zero with G. Escape terms pair nonpositively, but the averaged sum is positive definite and G is nonzero PSD, a contradiction. This proves the whole physical domain, including zero coordinates of the outer polytope, all weak walls and arbitrary SPD conditioning. The finite projection does not retain all face/rank equations; its exact infeasibility is sufficient because all actual bodies satisfy it. Its feasible points would not be realizations. Loss of full dimension or a maximal facet is a different domain.

**Exact unresolved complement.** The literal bindings are

```text
253 (0,0,1,2,3,4,5,0,7)
266 (0,0,1,2,3,4,5,4,0)
272 (0,0,1,2,3,4,5,5,0)
278 (0,0,1,2,3,4,5,6,0)
285 (0,0,1,2,3,4,5,6,7) EXCLUDED
```

p[0]=0 is a root convention; i>0 means i→p[i]. An actual full nonnegative-shadow graph is a subgraph of a listed maximal frame containing its base tree. Extras are optional shadow arrows, not true adjacencies. The new theorem forbids 1→8 and 7→6 in 253, and 1→8 and 8→7 in 278: each completes a Hamiltonian path. The complete new maximal necessary cover is

```python
REMAINING_FRAMES={
253:[[(2,8)],[(3,8)],[(8,4),(8,5),(8,6)]],
266:[[(2,8),(5,7),(6,7)],[(2,8),(6,7),(7,5)],[(2,8),(7,5),(7,6)],[(7,5),(7,6),(7,8)]],
272:[[(2,8),(6,4),(6,7)],[(6,4),(6,7),(6,8)],[(2,8),(6,7),(7,4)],[(2,8),(6,4),(7,6)],[(2,8),(7,4),(7,6)],[(7,4),(7,6),(7,8)]],
278:[[(3,8)],[(2,8),(6,4),(7,5)],[(2,8),(7,4),(7,5)],[(7,4),(7,5),(7,8)]]}
```

The source contains all 25 original frames literally. It checks all 82 distinct optional subgraphs, rejects nine Hamiltonian cases, and covers the remaining 73 by these 17 frames. They are not asserted realizable. All older subclass exclusions retain their original scope; no other whole tree was excluded by this work.

**Actual edge elimination and a complete E17 moment theorem.** For every convex 3-polytope, the true-pole equilibrium map E_Q(s)_i=∑_(j~i)s_ij(q_j−q_i) is injective. Proof: delete zero-labelled edges of a nonzero hypothetical stress. At every remaining vertex, section its tangent cone by a transverse plane. Equilibrium gives an affine dependence among vertices of the convex section polygon. The cyclic signs require at least four changes, since two sign arcs can be strictly separated. A connected plane graph then has at least 4v changes but at most ∑_faces(2k−4)=4e−4f=4v−8; length-two bridge walks contribute zero. Contradiction. No genericity or simplicity is assumed.

Consequently actual η, ηE_Ef and ηE_Ef² are the unique solutions with loads, respectively,
\[
-2d_iq_i,\qquad d_ib-(3l_i-a d_i)q_i,\qquad
2l_ib-(4k_i-2a l_i)q_i,
\]
where f=a+b·x,l_i=d_iE_Fif,k_i=d_iE_Fif². The full polynomial equation is ∑_(j~i)η_ij E_Eijρ(q_j−q_i)=d_iE_Fi∇ρ−d_iE_Fi(2ρ+x·∇ρ)q_i. At F9,E17 the image has exactly four compatibility conditions inside the 3F−6-dimensional force-and-torque-balanced load space. This is a load-space count, not a claim of symbolic independence after substitution.

Orient actual primal edges e=u→v, t_e=v−u, with outward facet signs σ_Fe, and set (T_rc)_F=∑σ_Fe c_e t_e^⊗r. If T₂ is injective, all T_r,r≥2 are: contract against a vector nonorthogonal to every edge. With actual geometry and masses fixed, candidate measures supported on actual facets and shared edges, satisfying complete polynomial facet flux through degree m, then have all actual moments through degree m. Induct on r: equal lower moments on an edge line make its degree-r error γ_e t_e^⊗r. Crossing the subtracted local flux with q_i gives T_(r+1)γ=0. Edge errors vanish, and radial flux fixes facet errors.

For the following entire genuine E17 lattice this rigidity holds even on the T₂ rank-drop wall, provided the actual global volume moments are retained:

```text
F0=[0,7,8,5,4,3,2,1]
F1=[0,1,6]
F2=[0,6,9,7]
F3=[1,2,6]
F4=[2,3,6]
F5=[3,4,6]
F6=[4,5,6]
F7=[5,8,9,6]
F8=[7,9,8]
```

For every convex realization, actual d, shared edge-supported measures, local polynomial flux through degree 2, and
\(\sum_i d_iE_{F_i}^{candidate}x=0\), \(\sum_i d_iE_{F_i}^{candidate}xx^T=5\Sigma\)
force the actual Λ, K_i and edge first/second moments. Degree-zero edge masses are already forced to actual η by injectivity. This is a complete-incidence moment theorem, not an S1 exclusion.

Proof of its full wall coverage: on a triangle the three edge-direction squares are independent in Sym² of its plane. Thus its six triangular facets kill all T₂ variables except bridges 0–7,5–8,6–9, dual to 02,07,27. Remaining face equations force these three bridges parallel if any coefficient survives. Hence T₂ has rank 17 off det(q₀,q₂,q₇)=0, rank 16 on that wall, with a one-dimensional kernel supported there. Induct on homogeneous degree r. Contracting down to T₂ kills all other edge errors. The weighted support-matrix error ΔB has row sum (r+2) times the facet error and satisfies ΔBQ=0. It is supported on I={0,2,7}, whose normals have rank 2, so ΔB=t uuᵀ for their linear relation u. Since three distinct extreme poles cannot be affinely collinear, 1ᵀu≠0. The SAME actual global volume moment gives 0=1ᵀΔB1=t(1ᵀu)², hence t=0. This proves degree 1,2 and every higher imposed degree, including the parallel wall. Different facet/edge lattices are outside this stated incidence theorem.

**Sharp actual facet-width coupling.** For an actual facet set T_i=max_PY_i, attained at an actual vertex. Then
\[
4/3<T_i\le4,\qquad
 d_i\le\frac{5T_i-6-\sqrt{-2T_i^2+12T_i-12}}{T_i^2}.\tag{4}
\]
Equivalently z_i=d_iT_i² satisfies z_i≤5T_i−6 and z_i²−2(5T_i−6)z_i+3(3T_i−4)²≥0. This needs no opposite parallel facet; the opposite support may be an edge or vertex.

Normalize axial height to t∈[0,1], put μ=1/T, g(t)=sqrt(A(t)/A(0)), I=∫g². Actual centering gives d=μ/I. Brunn–Minkowski makes g concave with g(0)=1,g(1)≥0. Choose the unique L=1+st,s≥−1 with ∫L²=I≥1/3. Concavity makes (g−L)/t nonincreasing, so g²−L² has one sign change from positive to negative. Equal mass implies μ≤μ_L, with equality only when g=L. Writing r=1/(1+s),
\[
I_L=(1+r+r^2)/(3r^2),\quad\mu_L=(r^2+2r+3)/(4(1+r+r^2)).
\]
Both decrease with r, hence I≥I_L(μ). Also g/(1−t) is nondecreasing, so μ≥1/4; finite I gives μ<3/4. Eliminating r yields d²−2μ(5−6μ)d+3μ²(3−4μ)²=0 for the extremal affine density. The lower root, selected at μ=1/2 and continuous without a root collision, is μ[5−6μ−sqrt(12μ(1−μ)−2)], proving (4). Equality is exactly affine g. Actual heptagonal frusta attain every interior parameter; octagonal-pyramid bases attain T=4. Explicitly use conv(rB₀×{0},B₀×{1}), with the audit's heptagon translated to area centroid 0, and then translate by actual centroid (0,0,μ_L). At T=4 use apex (0,0,1) over the octagon [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]×{0}, recentered by (0,0,1/4). These are nine-facet sharpness examples, not S1 witnesses.

Writing Λ=1dᵀ−QCᵀdiag(d), with C the actual facet-centroid matrix, the divergence identities imply Λ²+Λ=4·1dᵀ, hence d_i=(Λ²)_ii/4. Applying the actual nonnegative-affine variance bound to Y_i and T_i−Y_i gives
\[
H_{ii}\le1+\tfrac35\min\{1,(T_i-1)^2\},\quad
\sum_j\Lambda_{ij}^2\le\tfrac94+\tfrac34\min\{1,(T_i-1)^2\}.
\]
Also Λ_ji≤d_iT_j. These couple actual maximizing vertices to the same row norm, column mass and covariance. T_i must be the actual vertex-slack maximum, not a freely chosen upper bound. Small d_i does not imply small T_i. The capsule includes the complete 721-byte exact polynomial audit of the elimination and derivative identities.

**Actual controls and numerical boundary.** The mixed audit reconstructs the actual prism (B−g_B)×[−1,1], with B=conv[(-3,-2),(1,-2),(3,0),(3,1),(2,2),(-2,2),(-3,1)], g_B=(−2/9,1/21), M=N=I. Exact rational integration verifies all actual volume/facet/edge identities, all 45 matrices (1), their common kernels and PSD ranks {5:9,6:36}, all 36 pair bounds and all 9 strict row norms. It has at least two stable caps.

The E17 source reconstructs genuine rational bodies with M=[[5,1,2],[1,4,1],[2,1,6]], N=M⁻¹, and checks 135 edge-moment reconstructions and 540 compatibility equations. Its parallel-wall body has vertices x_j=(j,0,5+j(5−j)),j=0,...,5, x₆=(0,5,5),x₇=(0,0,0),x₈=(5,0,0),x₉=(0,5,0). Actual volume is 575/6, centroid (40/23,35/23,921/230), and normalized pole relation u₀=7/23,u₂=u₇=8/23. Edge-map rank is 17 and T₂ rank 16. Two deliberately incomplete supported-measure controls pass local flux but fail the SAME global centroid or covariance: the first-moment error is (0,0,1/6); the quadratic one retains actual masses, Λ and means, rank-three K_i, K_ie_i=0,K_iω=λ_i,K_i^fake⪯K_i^actual, but fails the actual K sum by −(Qv)(Qv)ᵀ/8, v=(0,0,1). All contraction factors and literal inputs are in the capsule. Neither is a full-relaxation or mechanical witness.

Discovery used adaptive constraint generation. A cold full 9072-block locator returned no candidate even on the domain now exactly excluded. Searches on 253/266/272/278 using more row cuts, selected rows, pair PSD penalties and nonshadow signs produced no further exact certificate. Failed locators prove neither feasibility nor infeasibility; their arrays are not promoted as durable successors.

The useful continuation is (3), the 45 common-edge PSD matrices, the 17-frame cover, and actual maximizing-vertex disjunctions for (4). A shared PSD multiplier T_ab can encode pair coupling without a Cartesian product: add (Λ_ab−1)T_ab to row a and (Λ_ba−1)T_ab to row b; their sum pairs nonpositively with G because Λ_ab+Λ_ba≤2. T_ab must be exactly PSD. On E17 use E_Q's four compatibility equations and, on the displayed complete lattice, the global volume closure that kills the parallel-wall ambiguity. The four unrestricted actual tree domains remain unresolved.

**Complete recovery.** The following single unit contains every byte of all eight standalone sources and all exact inputs, including 63 frozen integer gamma/offset coefficients. No NPZ, parent recovery file, download or omitted helper is required. Reference environment: CPython3.12.14, NumPy2.3.5, SciPy1.17.0, threadpoolctl3.6.0, one OpenBLAS0.3.30 pthreads thread, x86_64 SkylakeX. Only local-multiplier production uses numerical libraries; all acceptance and other audits are exact standard-library code.

Producer parameters are frozen: scale=float.fromhex('0x1.cbd6fbd662fa9p-2'); initial margin −10 and μ=1/8; τ=0.05·0.18^outer, 12 rounds, 70 Newton steps maximum; decrement threshold min(1e−7,0.001τ); positivity factor 0.99, Armijo 0.05, 60 halvings; symmetric solve with least-squares fallback rcond1e−14; positive-margin threshold1e−8; integer rounding np.rint(μ/SCALE·10¹⁰). These generate candidate integers; exact PD checks alone accept them. Clean full reconstruction, independent Bareiss/LDL acceptance and source-literal extraction checks all passed.

Save the unit as recover_vivid_unrestricted.py and run in an empty directory:

```text
python -m pip install numpy==2.3.5 scipy==1.17.0 threadpoolctl==3.6.0
python -S recover_vivid_unrestricted.py > complete_replay.log
python -S recover_tree285_l2.py check
```

Installation is unnecessary if the exact dependencies are present. The last command uses only the standard library and the certificate generated by the complete unit. The embedded uncompressed source archive is 38424 bytes, SHA-256 `c0dca7934b398e4d4da44194de83d69db23cc79ada201c698da59ee14297c480`. The complete unit is 20256 bytes, SHA-256 `130e89749039d818b1148b80ca8deff617bcb697316770d35705d691ade209b6`. The combined observed transcript is 2631 bytes, SHA-256 `ffaf389dd773ec226e6cd56c30ec5348c0e29ab51ef90cb84d256d01b3939749`; final marker `VIVID_UNRESTRICTED_COMPLETE_RECOVERY_PASS`. Every individual source/data/log pin is also enforced literally by the unit.

The decisive certificate is 810007 bytes, SHA-256 `2f9532794e6cd1807a8c22e06dc600f71d4a9aab8678dcfc6686e5f95ba57984`. Its leading-minor stream SHA-256 is `5825f7a15bde46221b34a57b2ce66d35fa5899aa3213419926bc1d09ec0d2e36`. The exact matrix checker prints:

```text
EXACT_CHAMBER_330_SYSTEMS_6_PATTERNS_4536_VERTICES_PASS
TREE285_UNRESTRICTED_9072_BLOCKS_81648_MINORS_EXACT_PASS
DATA 810007 2f9532794e6cd1807a8c22e06dc600f71d4a9aab8678dcfc6686e5f95ba57984
MINOR_STREAM 5825f7a15bde46221b34a57b2ce66d35fa5899aa3213419926bc1d09ec0d2e36
TREE285_UNRESTRICTED_L2_MIXED_LIFT_V1_PASS
```

Other terminal markers include `FULL_PERMUTATION_ACTIVE_RANK_AUDIT_PASS`, `SHADOW_FRAME_25_TO_17_EXACT_PASS`, `PARALLEL_WALL_COMMON_VOLUME_MOMENT_RIGIDITY_V1_PASS`, `PARALLEL_WALL_COMMON_COVARIANCE_IS_NEEDED_V1_PASS`, and `FACET_WIDTH_ALGEBRA_IDENTITIES_PASS`. All complete source, data and individual transcript hashes are literal constants below.

```python
"""Complete research recovery: unrestricted TREE285 and actual moment geometry.
Run python -S recover_vivid_unrestricted.py in an empty directory.
CPython3.12.14; build requires numpy2.3.5 scipy1.17.0 threadpoolctl3.6.0.
All exact checks otherwise use the standard library. All source bytes are below.
"""
from pathlib import Path
import base64,hashlib,json,lzma,subprocess,sys
assert __debug__
B=r"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;FcFN$Xx(Eh=?bXkJYc5K$WC3k@$L^_$^q#pU2gyXd^V3-0LeC_gZ*MMo9?~Z<wiTP&Toc
13W<|dKkb09LmNu_lkc~rY6|wIBd3!TW5(PORrGj*y4|`T?ujAE3SKxP|$4Va{yUjSV>k~hA<`VArX)ya_-`PM<^uca6bz1hrNM_
Px{wn@jx%s$9o6$6V;{s@CDCroY`61n7NVNsSkjt?PiTGRamKhRo%NYV%Bqqx$-C?+TN=%LDO-hYz`tUe2CcI7bl$okkd`c;V^}u
VcTJ$eUq}YdA1z*F0L45hifHf;3WM86*oLm7@UT!n@{6e2uF?(Vokz|BtvC^S->}#&chV2AVh3a=`99Vv)G(b4@)V7G<vq3*IBP8
vK2V$%Q=3i@Z5>3u!dBtb;cDjp*GukMEm!m`qtwDs8^F}LAa94tJS*`!9?XI$)xVsl45-X0D&GCO8%Eu#d*p~HcArqWhPU5(2wNP
-1f<Y-^l|Fx>LH6^-#U7o_vK>eqv#?VQs#w*oME;5{vQb<Be<k9;|)5)g8#IJ?5Kb1*b}aJp`6jye&HXOW{g&MSb^~WyX)N_Q&<D
bU9(Sc4KfR07m5}=4{_w&QW+l=mf-YQ@O^Dgn%i2PI7sdmvz-~Wi4#n;XjK&x)fIJBIAlQLyLGvG3o5d=33y)g@hSFO)0*osu<D&
Az<k{5ODPmFZEzhTatp~&{}b&$|*3tPrnpK^QyU{%cxu9F&Ozun5s?k#`7OWmp1}JYbs6|Pp!(o^HPU{Z~{t&$b#`lk8KlPi^a`}
W3cOnLHPUJWmDfhaQ_dl9jl9)kS@LO==%A53!j<Wp>>=2l0HU-u3OGs8R@kUWhoWMB>|s&H`jsr*x3`pu-MN2Fk+_e*EO#dy#W5p
*xAs&UA(oz!&HV7eJt@TmqC7f&K$v=fikblUjVRD8S!QDMCL^tH<>f>I53`DIB@&>c!^IUT<tjx|G?fbe$E>1<@$K*K_5s5m<HeK
cF6Dx+~9Rp+zFtk&&~)+i!Sy3DhP2M_7>wF-ZpxR6_q2@h9&{|2+v9jBt2(~Lrc`i$T(%G$P(}p`-bF|IU?a85D`aRzeuwEF3nlm
b7!@p%j^Pbp=T&WC*uThD)3?_>!@8w--dn3%&SGKqZ(gCF?8LWIwU}aQ6{)Y#);f{e_`;MRPb~%bze76WIjdHHPR?<^R6u^j#okH
9RMLXYY*9yO{+Il<8Ig1_*@;2$F@OSZ-6gZj*ZKb!?L&kcC*kGYzjVOP7#f4sE8%?FhF!*zOm#B?5oeI+bv%QZu_=7@N=1co7Pi<
*CJ;`2xp_l^DmCX5RL)lcaO&#s%NvXl?gR=e!@m#+J3LI%7|S7M6+y8btJE*Fxu|cOncVBd!9nzXI2C*kS4ecyv=cU+Hx5lzUJ@L
c^aGmg0-*1UAXEqKhn(lR~2LPXWdx15ioZK2M%u?aBu85A6GWt|5#QqIqZg0y0%s_imCPrH;;XJqW<@<pR(q_v(XM`i#<I_S@qLO
+l*7MgW=YwyFi+rO@qVC0EMX#9wro{pm^8+w&&1}O6U8OOXJWzmJ)Tx&Es>u)+Ltb_ZkG0wx!tF1Un{q<h9z&30;*?kbCTjT?q-X
)z2Bqx`~^&6g}pmYle5U5ykQP#2yM6+Sh6PCR)`hfRfVh2oeVx@ls6-eiVKbVuE?yqA|Gl96^zeN&~B2%1?`~5~YJg3m!0kb7gHk
5q2T#<Hp`W7T61I_|>@q{X`)~yboP%XqRxAct+zT=KnNa+R$QbrlB~GgeB%RPy{-eyJMFp$yYl~1&`N5L5=ni_nZnk>uJd`cst!K
y#_8_#$c!%NhWXizlnJ>3Yq<TmrT~5jdChVgqvzXp8S=OQU!>~us~`cERJosOp^)f-Phn4vqBYfJL0?Stxsi5eraCgwD1hY_FS}+
u&kAg$b=uT@=#z|m~ClbI55;>MX~yNQM8?D^k2rHSN`rNa!ihfOHZ(Zp3$veBS!ig9_o_k1Smu?YJgF|=2<4hedGwGP5gwWwU}s9
z16;`g+O-t`*9<p-RB34Wmk@01;C4-Nt|%etXBMg>T0e~_`|%|;dIv6I^@DzdjHM&e!XnA(D_hWOJMtoIFZOwd2HbR+<1!bl>ntT
!a6s^I!LA+;<IsR8{Ouwu+pTu5tGT1z!;s`z9LLbU_akPaS~QAEi}CqVY}I?g=-*Y$Y8~~Y5y~RJf;uBJ>M-H6o&lG7M|#7NZ1LL
8|_=%t_V^r_s0jS855yxzM-L!L&2z$>4LNNVEIbJfRlV0s1$^dH~G-<!%v@&s#SaiIdFUmwdQWLhEcPiUhr2bMxeDYmz#jvA@r`{
85&XXh1EICIo@|vbD(AwEb{@by&_;A)KuQRJ0W`!N%2E=)^Q1IS>H<>AM@S_r+(GCVe_U%`voYDr;(uxEFay+ws;SSh$3(`fQCb$
ef#Ebl|iOr2IWu<jO+I>s7H{I@jEq5n|h$da}EO=KRQsf)LS<{`5f)vrJ+TEt+iq3^nj=kq3e}cgyI=629Zn+&l@ZP^M@BEm%B%V
+>g0a1_C#T2MCXH$}O0>bfhm3;U-}xy27Fx5guz_noHhyQYakGzUXQuPJ`!#cm7bmHNv^YbKaq`E(#tkB=HLZ?jEYj{oFg!u7rva
E+0ur_B*3Z80B?VRCUr9G5xX)MIYvN<~Hayn_kaueF~XGW)6UKzIAQ!XIUcE<KxTr=#yx$>`)lbd@T_0M&svZZ#NoIMjRLdEip%m
x7D%P^4`_zErRGR)_XNve&+7Q`b!%;OIN3k`6;C&rjQ1QcU~U^i&PZ&>6;{LC@xUj<{3U+`lf*p^MiGDF_%*8_G#N-N5xI`y}tgZ
fS)BO^m)5q7Fc%P#vg*{S=8eG_elG;JN5<pjr+p|0=ClaqNelJsC@?d`VXc*4vkMCIvp+B07ek?Ep|I|I6~CD`Y98wkQ1;PkG-%c
S2a0jPP#PI`-ihpB(jfSjJT&sq0qV{J9EKw&Tyk?gqL?X<9tKzAdO(UW_v2XvE!#U8t>sUlBR5Yo|G;9f6v=XOCx+4+cO&w#eo=B
^Kyjg4b}RX+Z!sGM<BtX@s+jdpxeJ&6SA_jGAoh-m#j6l8+Fk7Om8c!8{i3FH)ri}lh%J!bYrbpI)a9U=SA_%8VkB&3(oXy#oJ)$
-L#_^?oQ77=w!N43#%P%@U!*1^43trn@k)*G<W7$W78RxSW+?Z;uJ7*+r8QV!>3*67gw`K1!OzF+z4x@Z7tn72(aSR-af-xo!1dd
PMQu9rvCK=Y$Wn&8*W`rug7+L_x%sJ&m=}>eZKu&3(PdwNb)vE&WQ6|M-5AC%r_JObb|t}`PW~<Zj=XpMz8=q1qH{fLs5)dm5!l}
*62L<J&U?TXSx_dnf*ep5xD~!F{I#-_do%~*UZi<u2{y=GV2hI)NB8}m4|ytB+|)@(s!xPP>~zD<Y1?)x~Lt8cz+8`=xT^A+^2u=
e7>p!MFxbIj4QVgDVPOXVSqE}-xbmY4n>OeK$6^4U;;RrstR@3U%XX6%^Av5?DJED5r9(Zw6M#*1o<VbAKyGVFy-#L5$KAJR}%Ky
MW|m%-qHJ(x0Y6(&Z8L-CH7W1S=F*L6T*;UAG5JkZBR@YC~`bHi*^opJOFSI$^pB|-t?ZEwSu$aV`8KNQ3uV^iZ1v`D(a<xhxA$s
uwH$c27ZEGe%&<XTP8}C#Lie~V^Pk6F!aeNnadD&+(^H(fDyFR?LI~Z^rq{D_sPCq{H+hyasLiO$_&$=Bmd{ipAQ*8x{l%|(;cxj
)yaZsKP}c_R6I{kvK?hpyE!oyFmT<MXXl|PRD6auGfwk`)^Q{jE=mRry3FNUy;!;TPWFCwffzE(Y;SYFWFycDCdFAuG&EP00t|-S
&zc2#sSoZS$vu$2q3Idws&|MN-}6n$_b@(u;z-NSnvIr;>YrNpQf0y?fz46aZey$NtGE|V0mYw*JVFXbo0p*+X2-Cd3m=27m?d;+
a{eZ8*$S33gC`zB)1-Ta6-jQu9SOAx%NLYfS4|CnS9&D$RPobJ2>kSIeuZyJv%%;pHo5CBsgrAX0GS|yC2EW#J#^bI3)d+CZ9Q$9
hE<6c$&}nhR7PD9fZ+?`Yw{!<W_Qxr2ucTAVQd6=KIoHSyZ*&zo2j5NrD~`?o7+hOO7j{w5UADr^%90fSNZKdeQAi7?}SZBY@LTa
4|1q2-+0BOsQd(`u~@^ZS8Ec53FzZ_n;oGin7>fKLAe3m{HH}{bstTnP`GayIyIjAVM+5Le0~}UoInciGpXwGa*U`Jl&21pAiT7B
&n;*jA>ARXWCm6o;sH**!>Ji^53~Vm#)Q1HA}EfL|5fr9S=8omutRL;SDYxk-aQR?-OSX>oe?KQuyD`o^@d%rUksC!LD$oI{M{0f
MkBH>4ZI(05Sn<lMuq3Teavn6qEJHsvf+bEr7{{%|BsZ0a%06<{9=<W@L$(XL|4}(MwZY2eY#IkUFOssmuHPtt5dHhhe>`8(H)fk
SH5u$vSS5g4kwn<?G?reQO~Ox=SaL@40i<$M=s4krC5}HuBd*9E0`XqS{2WV{t7u@8Fs~+kgyzN$S2YMiEf)Xb6%(TadA@k`M^S3
mzqwe!z!Hb@nC5~4)n%5#5&l$%$0-CbS(Ym<_M_JEG<oyA$x);gPgcCv;>9e<Z#cezD>R^Advx0ZY2FpvKiB+%|!$ODwc=Q#k+du
5K9a~c*#35W>3zaP2_%@_zmo$q@-H6j`~zv7U(pX_Q#a<1L%j&f>FE>0D~)va*pi~`C)b@#-p7yqww9(aMyQ=i`$^#4aht-%z$1%
pJDM7vjoySlOJ7TD6tu&K_@7rGWq?z?YOxnxUt)FDwa9r4copo8p!15BZEOO1Fi*_g$zc9P65nr-fQ~m^Ge|aY=9@bU5s~+0+a3(
B%**x)y~`I(h)jmH7fb_S?~w5yBuOe*SaaN<2jo3pyZWLG6FdoQPInEIS4i!(cGOtvv$c$d7{~yF+Q?iHv$nB6BbJ8|Icy?FXqNN
%?x&(f8ZSBq<-mb((m$JKiQRd(?zgGgE?(?p|mx!r$z)%CEmf%PWL_W>sZfa$@Varj9RT)B-Ma7_Anu<Q(1uqjKwUUvRvYami@$#
5wJDRpR%}ex{B2L{uph63a#|$>7(M)!S}PyN^%inP~eZi5%4Y~()<?=Z=QtKR`ICspgIX1pLx*bUkSyr5U~{+KyG=&L`iM2+b6`%
CX$v;#23P};z>z46Cohvw=lQCkqs{4_ISf3?f<%|ZP8I^zZ+bIS^GDeZA>b;dpu|=b0#)msij-jE@)|*3S33*v%z=z!<efc;lN`3
I;>{#ZI-enjYgiu#Uo<QF9{$rZB0>Yr2E1NPko7ipU4~>-_I(SwACi63Rpl;6bEzIxv=>K^S&r}0*9v1?&ha#l@il!OWD0QE~`7l
Q_zD5aq?;k7REEL&G{Ys3vmmAcvU%7)y$@qS#^bUaLbh9=kFNf5P)%Gt}fa`$%k0LqH`EyH28FI)MuG#;kfEIq}XTIYH*!DL~`v^
b2<c$h%H)f)WF{+H~akOWVnhA^HuL*aP~jAdYk5SRPudruk=^eg6_#Qa;#gr{nPaCUiKP1mX6&2+5sTbpfAIo2&if1-|Mh*x7EEK
-{4^$x>7S9mOAizl!T7CKZn_*Ts=(a!XF1Ri8U-<LrD&zCziZ=CQT?jN^a`LH4s%HWjW%M6H0EOwBzbeR2{VXe>w%~6dF6(tHu2C
%CWSyO7|s1{v`1o`0054Ze(IM1*6-ha-m4;noX;cFUQ39CBKk8d73w6F@S7dj`R%mF6yJVK`q@<9e1yG8geK4kbX8nmzpdSokJFB
-0t-4XZ6MB3zf)Tb=5pf3dXOYTTZ4gXyXyr$looCx>|X9I?W@x+((=fF1b$E_FU{?GmzD2<K6p$4Dk(XG0hvvup|L!<{NSx2@_oL
B_ew+L$h&_Y!eZ3a%7FB7EL9p?}W{57}p>a1{hXv;exhs2%L~QLQ#0{yL{i}NTKgCq^s`*#4ub*D<XCkG{cC{prV=HhkbO77PB7d
j=&?aqiR#~$%JlW4Y8^$&pu~S{Cmk6BIaOeyp295=kZ-lGv2|c5ZKA~hzWpABHgzMWDF4-y*mwMTfUdFd9^O%<N(uga%!XPHdBq8
(7ITp#InvCB)8|r_ZwjBdqhX2K0MG(dSx=V3kW<wC(pSS@&&&p`?T)618q{1=&PqEMJZ!8j*-kqp5A!EI&%E^81kTm_<Q*sjl9>D
DX-*7$iXo01geemgj|I6aFM-+1mEAcEGGH80KYYG+?E9dEEV3mLBst=piLY#;qZ$qo`AjlA%rJ&%8G5_f>dtQ7JtqI)NR->&CIwi
stFsuzPiL=N)&z674xTXg;^)$>U)1w&~}I#O%STS1Os^TEv6(lAjJ~0Pwb+$fEY*Xg#uO*CH?&i28+`APCatgYz0Zbq)$AuNhJlP
{?@_1uLcBTOJwiLP0lVB{TS;)R+0LgA9RQVPjG!JTRAL;af<01KSmvX^M;h84iJ$fS4sKg`PV#<Q1Ur(ka@j0OkH=%Rf;z|`CL#^
zYl?P=9=gXZ&*!vX8)6{_bx884s#!?{pmd_{wp*~s(!hY(iA`j%Uv=FYS$JuwH-K6gFDykYqpyvw)(}5J!r#j(8&y5TSzW^?KNob
Vp)#<U^ao+*8-YA?tK#RDeu@7rxB2a0`QtvH1d)6&U<~)Eed@q6^>#ZjRL93N}TQ!y+0M5vQktqZ^~<<=N4^yf-|LLn0k7alhUje
eFrtC@dr96dr6{7r$W+4O3o7x!mybn;)Ho-Ymfsc^MQT8SS)umC1^QGmeXMWmAW>WnP=%T=<K#AQlkWe$u6HLZ3Febq>OKnM3mzt
CFZIb94a4b=TRZ)%U;A23YpOjpZ&>Z-!Yb_YbRO5o>cqI-GmyxyJAO3NL5~`Ff|+=?lsH7Fs1PSCYU4lpLSw^`$3R8nFZsuu=<r*
L&LW>+=wZ%YtuaQr7m1C(pj-@!`T8HRLjJIKx^pRSR)Z77c<fs^ehyH4XpG4L5Mk+0DVDUzgCt!>LWK^!ysxh4hTZ5hyQryP(q4Q
Ztlx@r*B6^KuRjheJxQWvN|IJ*%p&kOsf9r3b9XVeGK7U>x{tA;4(e1;XU{#;AztI^_HI<WLNpMqN=i@xJKW1px3_-911U$z$rKy
jL!)$bMmff7H&ov2hnfZNb(M9=I%<6UJ$p0;%az?1LqGni}r3Ts^x){K{-heRSdILVAVWj5Zw8u9+_^0cU`vmScG`rMBk=3@kkXK
`xnwe8$(<dl|^Sl^9aF<>LAMeC++Za_DkW!MYq=K+F)QbL7MLD8nfxf0;-wF>NWH>t6jya=GH#$1{W=p4HVcgi=zhx!2+;=0Yr4$
;0WZN+*viQi*1<$$u5HnvTO?l$sMG?i_ipr*;?(?*Eaoi({ku$AHVD+aJJwyI3QKf2;opCWtq>?gwoO`*~b-rqP%em#*0BM%XSOR
M&j_Nx_&E*IFJ>kz-wFZIq_H%WFkpf4}=evpS(QRrCwsM?Pe~HXxN(bj45!m#!OYqWU}$o1x_!SJ)>lpKdE7?^WHBPQ#A}ioM@F^
y!upzHUx|8DU&Qe()wl`sJjJVu0#me!Wy_7AVJtp;^vEz&Oz11P6Z2i&tz0!2u>F}-VmkGo+kAZ$y<lq8k<9XEZ-$qD=1dsstE^d
2mU9Eako%jRT>V)K5igkl?2Gimj?4?v~0KcmnhLx3oEhRS#jy#AF4}^bf_=pC|h_{NrSPQ+Ojm9JPs|t=3GtVe$8Z19gMklE|@@<
j@Cpof1ebkWtg-hJYG)Sbq*F5Paoy$A<_95FeY029M7YA?+=^WWPq=Ve?gi&&3y?BkTa#u?nBPfLIzU;Z#EyNU847EjiVSu_M2<b
-L{o{$KE{R5D+kK@ZL5THW`$VEopcD8XSd=?}Owbzaz^e@VFUR<NgMt*ozAQ5nO4RJ0f^?ge~|)8aY#B)Dnt9b+7PVK%%xO9pE;E
HxdBr@?p9bdj^2kg2t48xg8F>0ATp1K*CPw&>QlAD#|WMAqm9WTyDqmz4LNv%%i*K!NhUm19i}YNOlD%DRXjIcD^LEU%ihhgOE+?
buk}rK>`~S=1<{KMdzjeP>t*8L*Y*-aFv$BoB~n`!;?>zjBx|$=FwP#3x)H3O9vx079DRI^KsPfc&Jjjvnx}?dW=oI(6fT<`LUQ$
DO8FOV|k!9n5f4>4O&kIUiCoQGfZJP>`oW<0)y>ImBdO}SciGVJ4RXH_suh6_(VYtHNF=&*}n6d{neW+4Wo>)*_Dgih8JU<sykM}
r^Ow72fk&XJ*)DC4~_#t?BJ%e#L_PdOt))e;kPQ6L|^^xE|adsmA8Q?yk(M*4x`*JVzG&!JH*_J^19h(fFWBl(sEObE82cAM&#wQ
U<_#<maQ7hNI1F6A>s6zf1@b5x6&X8ttLcN-<&=$Oxe$=x~Wd@*moGio>#vSdu?>OYbGdaR(X|%nEz3G{jmFjEA=}hUd>UB%5dgh
S1vYisw{l*O|Lz{humA97slBb{~0iCx-JojNX~Z#dH5f}CC4|D1yM3OPL=&(pmhavF@h#tPVtkU3^_7Zoy+}Bq564(gl45qjn#i1
^U(!Ahz@r@G9FLe)uNiMtzkszDCXx2P0}`6#A421gXTJ{$H-Rg?UgB{AsTCvhMD#UF_UNdo+xcI|FsS?WCb?^$Y-?g#n47@6BR=e
h7n!HIVqQ|jE9f7%b6gpd?nC2>|QI-v1akhFyYa9oCXrk-EcczhJ7*pli+5PY=$#^ljJxL9&O2lh}$spzsyrLIiW)r{I#wn{}$Dt
kntxG#p^<{qVCI)Dq_Zqh6ssW*>q6nM?NNx=oDGbNtP&uxkI#?NO<m|5bIvpUvsFNX9RmeDgKo_I`+p65KngO6M6En#flFvMCg`;
nnUxlhm8KGJNBw5sXw_M{aFT>XVUQmQvy~Xh^#z1jkF_;0@i~K;5~b2;LfQHsU6%@?4l3?=B}mR8YVd^boZTts4i*E3K9~=9TX~f
fNbWURx^S=8o=Qw??lDJq8LDs1T_7f3!%k6&HOqBv<%2tgfe5HSQcr;SRDQHb7wE=!oQ>N*YV3_4CQitdJ`&xoZ49iX&$CFy7W4;
_57KnSe(tX`Tj;_lSbL@pZRfV;~>1_GjH6a^r0{J`vNQ2s81*xS8a^57+rZ4L?fP4wJDm;e_ADADAkZf^Ic6tQDWd!nS=nz_`yop
yV_u)KCxNFq2`E$)uq<&NW}E!vhU^2`p^K{Ghu2@^1~Mj8uP{U;h?IC*gzN-59>VFDQ+;57ywWD^CXX%*A~7eVJ<yhe?=(eG|;YZ
yIsJ*B(Q+a;qlngNP&N@1>wTXaN`v=AqSVLNfFA-juRhL7d9)9RErPEYQ?hLQZL~k-A*kmXfLYnQ#IRi%Afhz?~m2K6S)fT)cx%A
Fy!8EDdlnU@i?PnW+(vymdO>*llhgum&Z<@n+$sVm|EbOHX-Ay>U@3Op~>VD#hTC3SOfd{a=PE0c~Z(@oc+X=x^Nhig7QC%icd5~
ogwYDvMU77QpVIbDo1rfVMi^R^?x?G_KS47q)|lh8)xaGCr;gfgT8_6iNp`bE~e1Qr9PK5<D?b2_hSMxLSj8oD@2N528NO*#@QM)
{#HkA%KR1l`BVW|L*LA!#e`fe_01#dsGYVX=o=)|p6JyY$=}(FrND3F^QjD&?k2=t5BRI0qOQn-uFI6GR%2uMO%K**Gjh3_sDm)p
1JV~samM>Gne52Z%kQq8+wz~)O%5S1chp9_#hrE76#WAK?%=+CWi2|a8oM!KX1nk%F@8>`{2W}NNDydwtK?4NX#fnsBag@}V11e>
^MIRo#GD=Y4KRMTC_;F_*Yv06##vGAnSr_Grrt>q8;`f6EfA*f(=1lmi3!F#0stKhv+@oxjW&lnntdPIqF9{9mvhWOv#TbzKsJz>
J`HqvnFEs*r^f&FQ&(*h{~EV&hmu>i#lu>}jhMg$N@3I2RoBIs14jD9l_zw63tUDE^lAU1i3vMs?4%2}2;I3;q`3o&)b{zge>vCP
>#Z5FhY<#OrTsZJSs=aZ-L{c3$|bg6kR}A{&K$M5k%Cm5RwM~=7>G<@1ZDLEKo%*a%}(DVNM>P0N=Uf?HG+SU(-7O>c)tyPq{RH~
K+xPQwllvEmI-D1M)7%F8abJ_LP6!!=>fbHsRJ}64mjOtCVC<o{AOa;eJK&c7-evlp!qkEXi4c5!R)LnJ#l4JXTwO}kZtN_dL@#&
;r4)@JD1_Lw-XY{)wF^W&Kp_lR?L=&*OtjRb)uJ|4z~^a4wz@#KEC!WQQHq76tO|Lwdx~^qJ24TK7sy8hvBh;RdNmoi~&~v@7Rds
8vW$aB=7Wq5z>BrcS`*W?hBibSj{tLh+5@KK+O;WEjf_X!&7jGVxK%eln^sIx~UkA=ZhyO(EbzvbD`lLwwx3%Sc0|rKgJZesRBO{
-~z?Ux{OULx)H`jR*WZZ&2Kp1d`k_cykKyCiqAg?lqAHCVQhLsG{?`<i81EArn3wH9GG-)v!bhgY(@a2><Qk~MAVOV$rzUJCAc<<
8@n$?9HFryCOtsGc~R_rnv9agm_k^8Lm_V+rU4(>TvZkdRi(CMKa}6b-}q_oA`oi-Ja~3TUOvE%1Z@QFC@-JR?tJJIu-xcA^wY^K
|E#{QoW%;embHcWF!INTk#6E_fPU5CNj25&x*la&*Y`ji-gRg(xg%-_3T3i(`9$HCa{`VXS;0Xx67+B*l;QQFwCQ22>5wqXa?m*}
0i`rqz1Du+7;=V{874m*G-moJ^oSuLC;|s6fNkK>UksSq?a`E-6TAG2z|wcNj?kj@_Cqe$tZ`qMS>0ggwV!o(3fI(iF6Oa-hWR)^
U?#eEJh8wPPl2GGZp0f^43&7lAG_*oYGvP)@9g#F1!}zy2DWu<9%!k`lVSsLF^k~N>%G82d>}AV;1Kp}E`oqNYq(GMHDlKe+qQuw
Ci2-vK4|6Lf{YY^At&yi;S!l462VG>`ye;4$?Rpv54UCn81c($*9X+BnMYk`o@rloEPa}BD67EF64CTYRooueyXANtVgFnGlK@us
);#s<DBEJm*F5*yq>kq*Nmz)~xQizNxrc{R%(US~zG-o-WlH<`vj(jB=O7qmnGNrTdvg+yD$JVllZz*(yHWWI!&B2G{l5^2j(NKU
R@ERNzJw{;10Y1wTjiF6U+5W2A}ndz@fsJR=2n~ayC-er--Nud$sQQql_wce%!P<x$eIl~K5#)(FB<A)+(9}F2PUmM=-gf6;;LWW
5W!u#DN%OJSROX14)@%e26V^0v@B9uy4OPrx9vuk9pEZSi(ixYHBPqo?eUd4Qp9tzso*5AlR0LcHiY=UxlDz?5q_`2syBdnS=-G7
zn87lJf=|Cvlr5_Bd#pibp33|qQjd)&tNYp`<$D;q=()7a{Q~^8F3H<5a5a&ov^=gJ`$tax-$1>a$2Rl{SL_Wkl81Qrj^|Lq!Cgl
)oDR+(nax;Fv>{F9<+^UmhGc@UHUWCzll;IjFGar1W$UHu{;qn5YZ;>CKJ>49K?1JjO4^tX-m`GY+kywptGX^o{VDgYf2MA-f^7f
lG2hDB|S^dt#UKOB-(^PbKbDhT}1D7YMF>J5Vx)d?#oql^m8>EGj;-ZpdzPS^K(A1g4xL0@MNX{)d4%7(O_o?IX`A8K<bU=&}tId
Mnj<Csr*XM%km)+JdV>gg0%Sst~ugon)%o2){b^+G^#_YMkliEvK)^!jZ9Fm=?|X1rSV!<YQ;Q`0xUgqIL>Z9lP-~ri7>W5f8VHz
s=<Gpy05@e9+$768kHGjVnqvyED7N=6i2%YAA>rOu-LHM5YV^CJHK-!J^WdRSFd!kp~XTIY}5n2#|;=L-v`fS)6k$0c2H)soD*zR
s2M6{A;q$YxA369lRG{-^me65^ivX80Yp>0;x58z3^+LzG|L}ju2GwDXXSWqPlx@!XUE#rnPG5ptZd98=~?UYL9MXL_tJh@waa^?
=G1k4_MNU~NEh5dB&4ObQf7I1m5lcu3j&lU{JIh%oH{%H^Vje-@lTu0yi;`0n#A^I;ed3=SZJ=Pm6b)#RSO?niu6w0H!)VKko5~q
Jm1Eshb@fOrT^@7X5(T}8CPcZ43Cf$2StiULLGoEK(s<@7E@dPGQ;K&V-*vV>;snW1~WxkK3jwj$3ch8)$B8|6g;ov=<w33508Oz
`|VkOzq~VzWPM%UQ}A7G!Wo8k7Bzx`<*<MTKxA#2;xwSuUFvZaGhHwSzK@q4bWQxiH*V)yftK|#Nf?ic^()OMn(<*7%sXdEFDzCz
$qE?Y6qb$__-Yv6#Kae8v;xjQ@|ZclhwKE9nWzeY<%7e}HIfpo-J>#3wG+dTl^Y0TrMaRvb(W*!+cF7W)|6D=EYgm9ETrV{2P8Xd
tab4ePX&7YCj(;A8#S$aVbE-Hx~wd1fLY_V$q{5QCu+Q13SuWPB3D?_Lw<L+$j+=Io%(UfA2#>LvunAsk11!~LtWAn`>a|EnN&6M
6=MhGT3F(KP((lc2_;{IUM|)<W&wGWr%VXEjU1Ty{*=LMgtHdu5NF7p-JI3MruL{{Veyk}<?`q3HQl0}nvqGsdme6S*{?>M(Tg42
XAbf-Ny{-h={^*<NnDR=)ERu|mSR!2Q0B(YO`-GyZUrtQpCM<IKFB#d0*pKwl=(*REjp*fMD{1(uGOpOpxCB~YFKR?Dsr=s<Q*5{
?<rN1d=muP!~HWy0xIl;nq-c${$D%948^s%bqUWaguoG+u-?}4l?Qf=T>-7ntZOd)A;`CARp8i8q|;7%LXZQ0Nhnojx!E!#%6B66
0XxSNFU#MC?wRGd|96}Nimn#HJtoeC`uhXnfkYF28qbD$qALXt?-fdnH+ndrW`|%VmLJU@&NetRM67nFoKo)D#1rr!#n#To1d`k&
1eq(xsM<Vw>&QzNgAl384vR0g^bj&y3O{5lOW?dc*kSI9W_Z<|V`f#Bp)9RP!e6gG%pcW9yw-5S);jti?&|T^QRM@mwz_jUeF;O~
RLCIK*vClN7in?K{%+d!>ScfDVTpvET1}zw%gnJ3f6~&QK*Nx4cRJ#qD3W8+3A=70cj~|niX2_8L8hZ*DS%0?xh2f2dIKMpAqTb^
FuJA^vX?~9{uXW-4t;dGI;LN^Wsha4hZ|WVrr!Y?nAJw#HkkekhGHW+0eivTo^0)^cD!YBH{L?7M6JW6ZmT`Grdx)AC;2>3?0?1a
!MSM_5?<Ixtcjo9!*)$XB@Q4~T7H3r8<gREC#5kt_n7qy*p#Zp%($ktmfC>DZd?B#*5Ne7e=K-VM!OLj<OUpRe~_#e`Col~>%(mS
>$62Ge)5+5mRjy)8y!Yp8pZkR()7Kn84u)3{-3Fr7f$OfIPNW*WqzaPK#_Gltm_R{aw>AT;}A7w1f|t9Q0vU(wT27zD^>W<4m>Cs
nwc!h{IVMV?L~E5p3qU{Og@SWNEt_|f^or~lcZyWitm2K#1vEbio^VGAUGi2-ib4QDTMjllk2yNb||4n00Wu$fHn!j^x9b>7@=Ee
ZL8I<fsl)zxF!9hONhS3$c`7mo~-?={y1BG4klKFkU5Dw;gk^H%9XnUO(@#7rI{@*ou_OB&jp@-DRY0(iE4<z!uNsu)z1l+RP^9_
y^C6XXKUi!Czg_+!;~7=z*+>&4b#qZq<h)@jKhlQ02^n8-u*9jG2Ecr5TMXB-&Ii__3KW)4eT954E@WRQo5J!NfZp6*wAn@A${h>
oM}RwvQIdzq^~3<(eL#;K@6(&;%m215#87~EERb2J#neWb9SVRVM}guNM=nFM)wcU6U?M7y_hE~7?b%qDs+_8l4*Hf88x`Bz8q7t
p+-7w9w_|6Bu@eQ$bXmX=F5K5-t0qF?+gMk5#+{5lnA@arpiL-08*ubh6>0T=AQ8Hrj{M;SAH2|Z@hg8(?l90OzV4?si9d0R)+-r
eX%C)j+YeYBhL@seCb59MygCsG`@0=+1<bT<76F{KUt06KO_-*)vX+k*8`<1Byp#~>snsw!9vvWp|AaF4nw&(ENhNA$1$=~JCW1`
$k#uhPg=p=X|4Kr4T(zeWk0eV$7FA5?k-9o+JB(~CrVNY|4mOZHvcfYnArxmZ`r?t=c<W45wOYHl^GfA>Wpn5-a<w@9JR>>FB}jt
b@w8>RNamCNcN}oz+y!cBuBdorwMS!aVPjKlJwp^u%u-nzLW1llSfl5m4C+xkgOfcZQSwG=D4CC%v8P(+{e3)&ZmY&+qB_uu4DmK
%lKdpi5;~5?`1A=ha5Tdk9pC7KZFF1K%M>?<rG~JeOrr|5**TQ{g{Oox4A3{l$CXJBY25xeV80i&`zFhh%vs;7{aK`0~J}y45@xN
v!Jt=AMZaOYT<MAm65h}HFg8dfoGxACsWF%7x1V6(=?TQmI#z|G+kU_i>ZFvW}59%OHw`8Q4&RG=tVlmHGGpQa*V@ZrUs+A09K|%
CKw`~TYkQq988URM<j2&rhlG}Qpjzo7LvNd)xM8%w<#ZHWomZ2AdVG*I08i)WpDb<_X!bijQ%pkQ<M_+|0Qi85Usc0U;1~q+E}8V
-HM%P@++IFu#&*Q!Cz3kbphJ;XE;Fm>V?h?u?WP%_^EL1;$bxp4wRxCJoVMFW7C@ikz!kxe3CR;Z}|O2Z-~uIScbp`djNynBnf#2
(Vnm;m8?uiPU$}KacakJb``Ck{^uCjbnYBLyqSCC;tMhv5XH>^R*%Z8Rga(u^0MYjKn9Zb;A7S-0j<xe+&&E=)Dq5-=bb`G`*<dX
#wBa%zq#c-Kb1lnr+)8Iq*{<@mwS2tZW9Lbn|)YQ`@Y?o4a#rg%{TRSseB4)kLtc4!W=EXAk|+ET@yIH`PFWehMzA_g=XNGxreMy
HZ27NO8qJ6e%%2OC(ZHHWY(OXSY)9{SPp+Qs56`-n+BC~0!Mg<ogG)DIcmaSwc%iM`4cA(%P5C}gZjGh+!emYFhTj9t+&lORoWJD
6Sv*XqI5<*fy9-E5IAKzn5)uJWk<;XjyoyEze+R!D#SPH4gL{)ucgF55FtnW#pE+8q)3*|{Mq;6EK!8CRE`Y1s;(jrz>U`0@U)JG
>L%QBJ)=*%)ReqxW93q7rpr(UPsEf;_+>_7{>`ai79b@YgMeju?76Fz7UmXr?20R>_^iegvlV6S0{}@dO-*1YS)xty9O{e(+H`^J
k=$W6WSvx4QuyU<+^_Isjb{d5Y9drAam99)gd{(kdOdDCv#DdbRhnqBn)hLo#n>XV=P-Lb#U@>j8%}Ls#`T)A^%gjJjyVDZ;W>{W
VM$6GD>dyeekQ)dY}}~2YU8ymKCM8Y;;5;kp@AX_Xq%0o*K6>-R%rt!jlo_5WkGVjA>+q)od=ho_GEZdx%{1y)yr4knfYW=;y9jW
pjDt<G6a1j&Zw*`;e+!1Lel*TJ&<Fpdi{+!Ok+&k@`YUWyW`9hGGb-=m%Bz>ClRiR|G!tjz(z`(Rev8sQ*di|WDCUqZ=&gyWxgK^
o28fg0N5<Ng^@*!*Z5Jh`)qNip9@Dit{e~m>h+1L6S09oCm-%pv)T(Ge--1}ASaN=Cd&Vh7m8a(ASB3f74}{m8<D1f-{zn7hYk>u
bFBb`UXx0H?0BO()!LPOiCxM0=fON@+UiP0?Sh;u+}V1(C%l0qRqF8^lkoJP8O8-)f;!~hgGqAmHkN3(t-LYKcRlktIL;~vh}w5M
P+NTf5iG<Xrdc!k8Kq-%q`n_RTc6B*G8Vc7NOSnO{#Fo5`_hOB1NA-cyBK~wlB7Nc{l<exCt84?XC6X+%`M<d<r8{Yy@I*#Jl(d`
h1d0iNdFjhNmk5I(1wK)9)<kY*e?I6RUxCn*&oaOdf=<P#lM|#TQvCAa-|moc-By>W65K5^e6D<TIh=oiaCL*o-4Y&EkW!`NMu-=
6?86r04a&`O|1*C*<iXu-lGbB7;$x`?`ToBgBD?-BUVcpMiRAP_*2FexZdMB2SERcx1tTAbB#Npz?{SUl~g<8dvf%&SZA+h44M{D
usAZC0*xpcm?;l37IvgW6t-%oA4anmiwyWg1(D`exw7a*?I^bt*^na``5e>F1dHjDa@Z3m#vL|o_%9S5YEMry<^>t%dC2H$K#DGg
K93XT#7mCBQkI|Pv}?MM=0avlbYHlT`7|+8Daxg-ej$0zTECPw73d|$ZT%=d`Je!*6^O=2xMc|NJA-e5xzF;Om%S6&`L?GEJ=Qzc
D+IbnA#aLMM(vRRz+{k6A+5e}n2eOlQ;#^5JygvdH`<u#kv;f%NJEfvSn<J4&N)o{sDAJ_-F+4z8(dqLX7OqQ<K5`;UJ92N0jQRe
>^eGRDmSgC@`m2jP_ZbY$aRn%D+XGYrqw9f2Ymi9RauD3#ynk)w=e=FWty{=7#Z*!Z32#QH<5!SYeJp94LOB2nA^TsO^#azH4;Ad
i^YiuOZP?nHD;6+T_P8_uqbKdy>tLIaEj8YF6bU07)Sm_i9x6}FBa-;FGpqk#_5lolhMcYaQmG5n7I9yj6uj#ebF}|9WKEReYRoU
^^{lP!!3+Zpva>^r$uw)uOdj+G2~E35El4HtLQekt`2p~%f#lDh5j_9GR@$}ZYVuO0V@E^GsFI1fIix0L{w$!B@Ydoss)txl@e1W
%CJ#$k$#bu<)K%SlQ6gHJtjBor?BTL3w>@SL$>oOcx6%Pa+$XWc1hQxTG7KS1|)xI(5SQJ1|-+}O|Z+hMyokHb)7%Zsx2`AF@YI4
bI|vD<G-;*yvX+Wqr9E|C3`(fyi1d$;3{U=1xMsUPzLKgU?T!%jwHp&WeNx6zO)Ovu4Khw3+|!M)%I$_Se#(JndlZO6tz}HkL`+l
XS%80ercL(cK75P>fZ$vhy@K7sUk4xIje=3*0Y-LCpv5*r@{-Z4=}^O2H%wcCJ9Qf!3a6;VUck3%bgzcafP+%e;7u&o&<lT&)|Be
Be3WRw5^N!Zk=K2#RL`NmB9u^uqY)V&p-rNnpw(mthLu0UtoYvrL1;tUh|;rYx;|U07t{$m`v%rid>T9&KUxP+h4TNSd-7yFQ7j9
N$2~PbkzU=9MN&S;))9u00HD@n5+T-*(oyrvBYQl0ssI200dcD
"""
ARCHIVE=[38424, 'c0dca7934b398e4d4da44194de83d69db23cc79ada201c698da59ee14297c480']
SOURCE={'mixed_lift_exact.py': [5675, '39fb90b674f149d583aceb1bc7b9728a48e7c173e1bcc5234a89b32052ed5da9'], 'recover_tree285_l2.py': [9773, 'f83fdeffbaf46a2503d66650fc2486f198a391246680762efa154f4501321a73'], 'audit_tree285_cover.py': [1725, '27cb525047497089c94ab3315de9f2902f4eaf369466cf5ff236898695fe7486'], 'shadow_frame_prune_v1.py': [3000, '3126d37a395121ad93f264dc4685f12ad640960a67edc351fa132ab2fc5b0979'], 'recover.py': [9384, 'eb66244f4ccf9cf1b81ed38e1795b073cd792cdba1a77cb2b7669d5503fee1d9'], 'wall.py': [3694, '5e7bf2b6974583edd8979b995f78099fa2593847bfc7554081cafa9fff865283'], 'wall_quad.py': [3414, '1b8673d0721bdc9410b472d353356f71673e2ae07076473c9c5365e2627ce746'], 'verify_facet_width.py': [721, '6ab9dce89e0bfa26f29373441e27f7ed527ffa41f33680d3f02361f424d2cb2b']}
DATA={'mixed_lift_exact.json': [84315, 'f441cfc6b3f1eaf67ee749623000d7cba0ec86863149b713afe58bcf6d825512'], 'tree285_l2_certificate.json': [810007, '2f9532794e6cd1807a8c22e06dc600f71d4a9aab8678dcfc6686e5f95ba57984'], 'shadow_frame_prune_v1.json': [1716, '83bdc27e4e6302ecad7030e7adec463f5de5545adea10169fe339db33d6f8e5e'], 'control.json': [9916, 'bbd2b67428f3a3cef526218407f72817965cddb3b78a3fb04da75a3007ef6f0d'], 'wall.json': [3165, '177c4ec5d1bb8040f526a81d861f59e80c7d92c12ed37c5a433e732051d60d73'], 'wall_quad.json': [10185, '5c4f3d1bb740d2e391b606015c8c78c0505c8088df8d1b26f0fdf53c7c66bba5']}
JOBS=[(['-S', 'mixed_lift_exact.py'], 278, '2203eaa6236f22d78b17f83e19489c64fcf81f420c3d43e96d94a40a67ada48c'), (['recover_tree285_l2.py'], 311, '83c47f58e3d6a513806ad9b0abaff8456135333d167334849b51aba96575a1cb'), (['-S', 'recover_tree285_l2.py', 'check'], 311, '83c47f58e3d6a513806ad9b0abaff8456135333d167334849b51aba96575a1cb'), (['-B', '-S', 'audit_tree285_cover.py'], 225, '9d7c419b40ad82ac333bd83df99ffb214ac7d2e26c8976cb6014ee7a6a3d1816'), (['-S', 'shadow_frame_prune_v1.py'], 449, '9bc99045c201f578328bae29c78b584eec904d462fc5f910d6a8a0ea55cef4f0'), (['-S', 'recover.py'], 498, '9ebcca348be644c67bf7af5896559dd66c07ed065c621d7a5ad5910b7458fdec'), (['-S', 'wall.py'], 271, 'fd24c9823d6a8aea9068a5fc5f7725d8847acdde83ba6f5655df749c019a98ff'), (['-S', 'wall_quad.py'], 210, '4186915d1a7317d282d59a0978de461573cbf8bfccc6fced2238c2fe0e1bddf9'), (['-S', 'verify_facet_width.py'], 36, 'd127850d5a1486e0f441a83c0c8a586e587d94da4e1f1756b5b31c0e7c8635ce')]
raw=lzma.decompress(base64.b85decode(''.join(B.split())))
def pin(raw,p):assert [len(raw),hashlib.sha256(raw).hexdigest()]==p
pin(raw,ARCHIVE)
sources=json.loads(raw)
assert set(sources)==set(SOURCE)
for name,content in sources.items():
 raw=content.encode();pin(raw,SOURCE[name]);Path(name).write_bytes(raw)
for args,size,sha in JOBS:
 result=subprocess.run([sys.executable]+args,check=True,capture_output=True)
 pin(result.stdout,[size,sha]);sys.stdout.buffer.write(result.stdout)
for name,p in DATA.items():pin(Path(name).read_bytes(),p)
sys.stdout.buffer.write(b'VIVID_UNRESTRICTED_COMPLETE_RECOVERY_PASS\n')
```

Expanded proof copy: vivid_unrestricted_result.md. Standalone source: recover_vivid_unrestricted.py. The complete literal recovery above needs neither link.
