# minimum-0064

AI research report · 2026-09-13 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

**VIVID63_ACTUAL_LAMBDA_SYNCHRONIZATION_AND_TRIANGLE_FRONTIER_V4**

No whole TREE266, TREE272 or TREE278 is excluded. The accepted monostability bounds remain **V≥10, F≥9, C≥34**. The principal new result is a necessary-and-sufficient physicality criterion for the common Λ: exact facet means and eight scalar equations on genuine shared edges force the physical facet masses and the body's own volume centroid. Further results include complete continuous triangle-star exclusions, a complete topological refinement, new deletion inequalities, and exact quadrilateral moment elimination. All scope restrictions and remaining domains are stated below.

**Authority.** I continued `research-journal(20260911-194223).md`, 4,757,248 bytes, SHA-256 `19c3d6ce189e55b1832eaca4cbda886026a0d4d05ba556d997baca6f3aa2fa81`, including literal immutable parent `minimum-0058`, declared payload SHA-256 `159513b19201b45a7b7495a919e077021333865f6f160c989e63debf72597df3`. The immediate reconstructible continuation is `VIVID63_COMMON_LAMBDA_FACET_SHAPE_CLOSURE_V1`; its handoff Markdown is 50,475 bytes, SHA-256 `7c430ee25909dab84b6559dcbe7b2d6ed0bee37ef9f64d4150877bd32d3b3862`, and its recovery source is 21,182 bytes, SHA-256 `d5d8366ea02d8413b511f746cb65b2e83f0866ecee74e6f13a33949c7a7644e3`. No journal was modified. No mathematical array or incidence conflict was found. The prior distinction between an immutable serialized-payload hash and extracted Markdown bytes is preserved.

The literal bindings remain:

```python
TREES={253:(0,0,1,2,3,4,5,0,7),
       266:(0,0,1,2,3,4,5,4,0),
       272:(0,0,1,2,3,4,5,5,0),
       278:(0,0,1,2,3,4,5,6,0)}
OJ={253:[[]],
    266:[[(5,7),(6,7)],[(6,7),(7,5)],[(7,5),(7,6)]],
    272:[[(6,4),(6,7)],[(6,4),(7,6)],[(6,7),(7,4)],[(7,4),(7,6)]],
    278:[[(6,4),(7,5)],[(7,4),(7,5)]]}
TREE285=(0,0,1,2,3,4,5,6,7)
```

Root is 0; each i>0 has selected arrow i→p[i]. The selected tree consists of true dual edges. OJ extras are optional shadows, never presumed present or genuine edges. These are the stronger ten maximal frames and their 24 subgraphs, not the older seventeen-frame cover. TREE285 remains previously excluded and is unrelated to canonical C32:285. TREE253 is outside the new tree-specific work here.

**One actual body.** Throughout, P={x:q_iᵀx≤1} is full-dimensional with distinct maximal facets and its own uniform-volume centroid at zero. Set Y=1−Qx, d_i=A_i/(Vol(P)‖q_i‖), ω=d/3, λ_i=Λ[:,i]=d_i E_FiY, K_i=d_i E_FiYYᵀ, Σ=E_Pxxᵀ and H=11ᵀ+QΣQᵀ. Retain one reciprocal SPD pair N=M⁻¹, G=QNQᵀ and n_i=G_ii. Weak escape a→b means G_ab≥n_a. All facet, edge and volume expectations belong to this one P.

Divergence gives Λ1=3·1, ΛQ=−Q, Λ²+Λ=4·1dᵀ, d_i=(Λ²)_ii/4, Σ_i d_i=3, Qᵀd=0, Σ_iK_i=5H−2·11ᵀ and K_iω=λ_i. Rank Λ=rank H=4 and rank K_i=3. The accepted covariance band R⁻¹/15≺Σ≺R⁻¹/3 remains in force without a mechanical condition-number restriction. Signed Loewner bounds and copositive nonnegative-affine bounds remain distinct. No redundant averaged quadratic projection is counted as new strength.

**1. Exact physicality from actual means and eight shared-edge equations.** Let a candidate F×F Λ satisfy rank Λ=4, Λ_ii=0, Λ_ji>0 for j≠i, Λ1=3·1 and Λ²+Λ=4·1dᵀ with d>0. These imply Σd=3, d_i=(Λ²)_ii/4 and dᵀΛ=3dᵀ; the last follows by comparing Λ(Λ²+Λ) and (Λ²+Λ)Λ. The polynomial t(t+1)(t−3) annihilates Λ. Its rank-one right side makes the 3-eigenspace one-dimensional, so the −1 eigenspace has dimension three. Choose a basis Q of that eigenspace.

The single carrier body is

P_Λ={x:Qx≤1}, with slack image range(Λ)∩R_+^F∩{ωᵀy=1}.

It is bounded and full-dimensional: 0 is strictly interior, and a recession direction u has Qu≤0 and dᵀQu=0, hence Qu=0 and u=0. Every listed inequality is a distinct maximal facet, since λ_i/d_i is a carrier point with exactly coordinate i zero. At this stage the origin need not be its volume centroid.

Recover the actual vertices and true facet cycles of this carrier. Require its exact uniform facet means

(M) E_FiY=λ_i/d_i for every i.

For a genuine edge ij let π_ij be the area fraction of the triangle in F_i whose apex is the uniform facet centroid and whose base is E_ij. On any spanning tree T of the actual dual graph impose

(E) d_i²π_ij/Λ_ji=d_j²π_ji/Λ_ij, for ij∈T.

**Theorem:** (M),(E) are necessary and sufficient for Λ to be the actual homogeneous-volume Λ of P_Λ at its own volume centroid. For nine facets only eight scalar equations are required; the selected true escape tree supplies T.

Proof: let γ_i=A_i/(Vol(P_Λ)‖q_i‖) be the actual geometric masses before assuming centering, c_i the actual facet centroids, and m_ji=E_FiY_j. Pyramid integration gives Σγ=3 and volume centroid g=(1/4)Σγ_ic_i. With η_ij=length(E_ij)/(Vol(P_Λ)‖q_i×q_j‖), the actual centroid-to-edge distance gives π_ij=η_ijm_ji/(2γ_i). Consequently γ_iπ_ij/m_ji=γ_jπ_ji/m_ij. Substituting Λ_ji=d_im_ji into (E) gives d_i/γ_i=d_j/γ_j on the tree. Connectivity and equal sums force d=γ. Then Λ1=3·1 and (M) imply QΣd_ic_i=0, hence Σd_ic_i=0 and g=0. Every Λ column is therefore its actual area integral. The same calculation proves necessity.

The criterion is rational on valid carrier charts. In any three independent coordinates on range(Λ)∩{y_i=0}, for actual cyclic vertex slacks y_r and mean m_i,

π_i,r=det[m_i,y_r,y_(r+1)]/Σ_sdet[m_i,y_s,y_(s+1)].

All determinants have one common nonzero sign. Triangle means are vertex averages. For a quadrilateral with diagonal intersection o, m_i=(Σ_ry_r−y_o)/3. Thus on the two-triangle/seven-quadrilateral E17 subclass all mean and synchronization equations are rational in the common Λ. Larger facets use their actual polygon integrals. Once the criterion passes, H,K_i and all edge moments come from this reconstructed body; they cannot remain independently assigned. The mechanical completion is one SPD N, M=N⁻¹, satisfying the required tree and OJ signs.

**Exact application.** The recovery starts only from Λ for six actual E17 controls, reconstructs every vertex, edge, cycle and mean, checks eight tree equations, and independently verifies the actual zero centroid, all masses, the complete slack vertex set, all 81 H entries and all 729 K entries. Inputs are the complete inherited epsilon family at ε=1/2,1/10,1/100 and radius family at r=3/4,1,5/4; their full generators are embedded below.

**Exact barrier to dropping (E).** Take the regular octagonal pyramid with base inradius1 at z=−1 and apex(0,0,3). Put b=√2−1, n_j=(cos(jπ/4),sin(jπ/4)), t_j=(−(n_j)_2,(n_j)_1). Its base vertices are (n_j+b t_j,−1), its actual centroid is zero, and its counts are (9,16,9), not E17. Actual masses are d_0*=3/4, d_(j+1)*=9/32. Keep its actual poles q_0=(0,0,−1), q_(j+1)=(4n_j/3,1/3), its own true covariance and every normalized actual facet measure, but use

d_0=3/4, d_(j+1)=9/32+ε(−1)^j, 0<|ε|≤1/1024.

The alternating mode has frequency four, whereas global vector boundary flux through degree two has normal frequencies at most three. Thus all those flux identities, full Λ algebra, rank-three K_i, their common sum and contractions, the same actual R,Σ and every exact triangle completion persist. Exact arithmetic also verifies K_i≼2(H−He_ie_iᵀH/H_ii), entrywise K_i≤(5/4)H, Λ_ai≤10/9, K_i,aa≤2 and all Λ pair LMIs. The positive endpoint is checked exactly; the negative endpoint is a cyclic relabeling, and convexity of the affine matrix/scalar inequalities proves the whole interval.

Every base-side equation (E) nevertheless fails: its ratio is d_j/d_j*=1+(32/9)ε(−1)^(j−1), equal to 1±1/288 at the endpoint. Those eight edges form a spanning tree. This is a nonphysical mass assignment on fixed actual geometry, not a body with those masses, not E17 and not a monostable witness. No untested higher lift is claimed.

**A complete E17 resolution of that barrier.** Let K={u:n_j·u≤1} be the same octagon. For every ε>0 define P_ε(z)=(1−z)K+[−ε,ε]e_x, 0≤z≤1, equivalently z≥0 and n_j·(x,y)+z≤1+ε|(n_j)_x|. Its base vertices are v_j=(n_j+b t_j+ε sign((n_j+b t_j)_x)e_x,0), j=0,…,7; ridge vertices are v_8=(ε,0,1),v_9=(−ε,0,1). Its complete cyclic facets are

(7,6,5,4,3,2,1,0),(7,0,8),(0,1,8),(1,2,9,8),(2,3,9),(3,4,9),(4,5,9),(5,6,8,9),(6,7,8).

The section formula proves genuine counts (10,17,9) for the entire ε>0 domain: six triangles, two quadrilaterals and an octagonal base. Volume is 8b/3+2ε; the own centroid is (0,0,(b+ε)/(4b+3ε)). No catalogue alias or S1 claim is assigned.

For raw outward normal a_i put s_i=A_i/‖a_i‖ and p_i=s_ic_i. The base has a_0=(0,0,−1),s_0=8b+4ε,p_0=0. Side j+1 has a_(j+1)=(n_j,1). For j≠2,6, s_(j+1)=b and p_(j+1)=(2b n_j/3+bε sign((n_j)_x)e_x,b/3). For j=2,6, s_(j+1)=b+2ε and p_(j+1)=(0,(n_j)_y(2b/3+ε),b/3+ε), obtained by integrating its width2[b(1−z)+ε].

Let Φ be the12×9 matrix whose column i consists of a_is_i and then a_ip_iᵀ in lexicographic order. Its rows(0,1,2,3,4,7,8,9,11) have determinant

cε³[1+(1+√2)ε/2][1+3(1+√2)ε/4], c=(−1008640+713216√2)/81<0.

The integer sign certificate is1008640²−2·713216²=524288>0. Hence rank Φ=9 for every ε>0. The source proves the polynomial identity by exact interpolation at0,…,9; the determinant has degree at most nine because every entry is affine.

Therefore global vector flux through degree one uniquely forces every facet weight on this entire family. Explicitly, for actual geometric mass γ_i=s_ih_i'/Vol(P_ε), q_i=a_i/h_i', and perturbation e_i=d_i−γ_i, the flux difference is Φ(e_i/γ_i)/Vol(P_ε). Positive column rescaling and translation of the polynomial basis preserve rank. Under (M), the existing Λ algebra supplies these flux identities, so the edge equations are redundant on this family. At ε=0, Φ has rank six and the ridge collapses to the pyramid apex. There is no uniform conditioning gap along this actual E17 resolution. General E17 mass rigidity and the whole two-triangle/seven-quad case remain open.

**2. Complete topological removal of336 triangle-chart domains.** For a genuine triangle i with true neighbor triple J, form B_i=Λ−1Λ[i,:], choose a rank-three column basis C, and set V_i=C(C[J,:])⁻¹. The inherited recognition theorem states V_i≥0 iff the actual maximal facet is triangular with exactly J. With ℓ=Λ[J,i], its actual moment is K_i=3V_i[diag(ℓ²)+ℓℓᵀ]V_iᵀ/(4d_i). Thus every record(i,J,k,K) is a whole continuous domain in one common Λ; nonsimple zero slacks and changes of valid column chart are retained.

|Form|Previous pair overcover|Entire domains excluded|Exact topology frontier|
|---|---:|---:|---:|
|266|2456|112|2344|
|272|2426|137|2289|
|278|2091|87|2004|

Every rejected record has no planar three-connected completion at any edge count. Every survivor has an independently verified nine-vertex,seventeen-edge sphere graph containing the selected true tree and exactly the two specified degree-three stars. All36 pairs of triangle labels survive in each form. A graph witness supplies neither actual common moments nor a mechanical realization.

The dual graph of an actual three-polytope is simple, planar and three-connected. A direct proof of the last property chooses a plane through any removed set of at most two vertices, through the interior, and through no other vertex. Each strict side induces a connected graph by edge ascent of the plane-normal functional to its extremal face. The section polygon has a vertex outside the removed set, hence an edge crossing the plane joins the sides. Radial projection gives the sphere embedding. On E17 the facet degree sum34 forces at least two triangles, so the pair disjunction covers that entire slice. The individual exclusions require no E17 premise.

The complete finite proof is as follows. Enumerate all triples containing selected true-tree neighbors and all reciprocal pairs(k∈J) iff(i∈K). Form the connected spanning graph H from the tree and both frozen stars. Enumerate every cyclic neighbor order; retain face permutations with Euler characteristic two. These are exactly the possible sphere embeddings induced from any planar completion. Insert every permitted missing edge as a chord of a facial walk, considering all endpoint occurrences, including repeated vertices. New edges cannot touch the two frozen labels. Requiring the next edge to touch a deficient vertex is complete because any target has such a missing edge, which can be inserted first. If all degrees are at least three but deletion of a pair disconnects the graph, require the next chord to cross two remaining components; every three-connected target contains such an edge, again insertable first. Degree-budget pruning is necessary. Induction on missing target edges proves exhaustive coverage.

At17 edges, independently verify tree/stars, connectivity after zero/one/two deletions, ten simple face cycles,34 directed edges each once, single cyclic vertex links and Euler characteristic two. Retest all270 nonanalytic rejects allowing every edge count through the universal planar maximum21, accepting immediately upon three-connectivity. None exists for90/114/66 records. The other22/23/21 are analytic: adjacent degree-three vertices with the same other two neighbors are isolated by deleting those neighbors. The wrapper checks exact input/output pins, all retest record bindings and every null answer.

Another analytic case: nonadjacent degree-three vertices with the same three neighbors form K_2,3. Any extra vertex lies in one of its three disks and can attach outside only through two unfrozen boundary vertices, contradicting three-connectivity. Such a graph has at most five vertices; the exception need not be a triangular bipyramid. Four TREE266 records are already nonplanar: (6,(a,5,7),8,(0,5,7)), a=0,1,2,3.

**3. Exact uniform star gaps.** Actual triangle area gives r_j=d_i/(3Λ_ji), δ=Σ_Jr_j−1 and Σ_Jr_jq_j=δq_i. Universally Y_a(v)≤4: decompose P into pyramids with apex v and nonincident facets as bases; zero volume centroid expresses −v/3 as a convex combination of their centroids. Equality forces a pyramid with apex v. Thus r_j≥1/4, strictly on E17, but the certificate uses the closed universal bound.

Set w_i=−δ,w_j=r_j and all other entries zero. Then Qᵀw=0,Σw=1 and Gw=0. The entire δ≤1/D domain is the closed simplex with vertices

W_0=(e_i+Σ_Je_j)/4,
W_j=−e_i/D+(1/2+1/D)e_j+(1/4)Σ_(k∈J,k≠j)e_k.

Its barycentric coefficients are (w_i+1/D)/(1/4+1/D) and (w_j−1/4)/(1/4+1/D). Negative δ, δ=0, lower-support strata and weak walls are included.

Tree matrices L_a=2e_ae_aᵀ−e_ae_p[a]ᵀ−e_p[a]e_aᵀ satisfy tr(GL_a)≤0. Where `band=1`, certificates also use these explicit closed norm sectors, α=n_1/n_0,β=n_8/n_0:

|Form|Closed necessary bands|
|---|---|
|266|3/8≤α≤1/2;1/16≤β≤25/64;35/64≤α+β≤49/64|
|272|α≥5/16;59/128≤α+β≤33/32;β≤23/32|
|278|α≥3/10|

The preceding reconstructible continuation supplies the corresponding strict physical sectors. The new conditional certificate theorem is self-contained under these displayed bands; applying it to every monostable literal form invokes those inherited results. It is not a bare-TREE266 theorem with arbitrary extra shadows.

Each certificate supplies one integer g and four nonnegative multiplier vectors m_s with B_s=gW_sᵀ+W_sgᵀ+Σ_km_(s,k)L_k≻0. Multiplication by640D gives the accepted integer matrices. All640 matrices and5760 leading minors pass Bareiss and independent rational LDL. Interpolate using the simplex coefficients: B(w)≻0 but tr(GB(w))=2gᵀGw+Σ_km_k(w)tr(GL_k)≤0, contradicting nonzero G≽0. This is exact exclusion of a whole necessary continuous system, not numerical failure.

|Actual triangle|Complete gate|
|---|---|
|label1, all three forms|δ_1>1/10|
|label2,266/272|δ_2>1/8|
|label2,278|δ_2>1/10|

All six genuine triples for each label are certified. For its three positive entries a,b,c=Λ_ji, the polynomial gate is D(Λ²)_ii(ab+ac+bc)>12(D+1)abc. The full object contains160 sectors:57/55/48 by form,86 without bands and74 with bands. It reconstructs the94/94/84 single-triangle covers and all112 uncertified triples. All literal D, band flags, multipliers and complements are inside the recovery.

Root0 receives only J=(1,2,8),(1,3,8),(1,4,8), with denominators(32,64,128) in266,(64,64,256) in272,(32,64,256) in278. Root triples(1,5,8),(1,6,8),(1,7,8) remain untouched. The inherited full-branch δ_4>1/4 in266 and δ_5>1/4 in272 are not counted as new.

**4. New actual deletion inequalities.** For an actual triangle i with δ>0, deleting it adds its genuine tetrahedral corner and leaves eight maximal facets. With its V_i set z=V_i1,f=λ_i/d_i,s=(z−1)/δ,μ=d_i/(3δ),ν=1+μ,

u=[1+μ(s+3f)/4]/ν,
h=12δ²1+d_i(z−1)+3δλ_i=12δ²νu.

These are the actual tip slacks, volume ratio and old slacks at the new centroid. For retained labels u_a>0 and q'_a=q_a/u_a, with the same N,M. The neighboring halfspaces form a trihedral cone with finite tip. A nonneighbor cutting that tip would already be redundant on the old cone cut by i, contradicting maximality. Thus the added piece is exactly a tetrahedron, the new tip has exactly three incident facets, and nonsimple old vertices are covered.

Brunn–Minkowski applied to the inward volume tail gives Pr(Y_i≥t)≤(1−d_it/3)_+³. Integrating E Y_i=1 yields d_i≤3/4; equality is the pyramid case. Exact side-area transport gives, for neighbor j, ℓ=Λ_ji,d=d_i,

d'_j=3(4δ+ℓ)(3δℓd_j+d²)/[4ℓ(3δ+d)²].

Consequently the common-column physical inequality is

Γ_j=δ(3−4d_j)−ℓd_j−4d²/(3ℓ)+2d≥0,
3/4−d'_j=9δΓ_j/[4(3δ+d)²].

Equality holds exactly when the filled body is a pyramid with base j. On E17, if s_0 deleted-triangle vertices are simple, filling has V'=11−s_0,E'=17−s_0,F'=8. A pyramid requires s_0=3; the new degree-three tip is a base vertex of a heptagonal pyramid. Thus equality is exactly truncation of such a base vertex and has facet-degree multiset(8,4,4,3,3,3,3,3,3). In particular Γ_j>0 throughout the two-triangle/seven-quad subclass.

The whole closed sector d_i≥1/2,d_j≥2/5,Λ_ji≤4d_i/9,0<δ≤2/5 is excluded. With r_j=d_i/(3Λ_ji)≥3/4, the required inequality is δ(3−4d_j)≥d_i(4r_j−2+d_j/(3r_j)). The left side is at most14/25 and the right at least53/90, a contradiction margin13/450. Monotonicity follows from d_j≤3/4 and 4−d_j/(3r_j²)>0.

An exact equality family starts with base(-2,-1,0),(-1,-2,0),(1,-2,0),(2,-1,0),(2,1,0),(0,2,0),(-2,1,0), apex(0,0,1), and imposes −3x−y+5z≤7−2t,0<t<1. Replace the first base vertex v_0 by v_0+t(v_j−v_0),j=1,6,7. Counts are(10,17,9), ordered facet degrees(8,4,3,3,3,3,3,4,3), and new triangle8 has neighbors(0,1,7). Filling returns the pyramid: Γ_0=0,Γ_1,Γ_7>0. The removed volume is t³/3. Exact integrations at t=1/4,1/2,3/4 retain all actual common moments and edge flux. No S1 or catalogue claim is assigned.

Two further strict gates hold for every retained a:

(T) z_a−1<4δ+Λ_ai;
(S) S=15Σ+9μB_i−(v−3μc_i)(v−3μc_i)ᵀ/ν≻0,

where v is the actual tip in old centered coordinates, c_i=E_FiX and B_i=E_FiXXᵀ. For(T), apply the vertex bound to the filled tip: s_a/u_a<4 because an eight-facet pyramid apex would have degree seven, not three. Clearing gives(T). For(S), the vertex-pyramid mixture with base random variable Z gives 15Σ_C−wwᵀ=9Cov(Z)≽0. A nonzero kernel forces all nonincident facets into one plane, making the body a pyramid with apex w. The new tip cannot be such an apex. Actual mixture integration gives S=ν[15Σ_+−(v−c_+)(v−c_+)ᵀ].

In common slack coordinates A=15(H−11ᵀ)+9μ(K_i/d_i−f1ᵀ−1fᵀ+11ᵀ), b=s−1−3μ(f−1), so A−bbᵀ/ν=QSQᵀ≽0 with rank three and kernel ker Qᵀ. This is signed Loewner information.

There is no uniform positive deficit in the normalized filled-tip bound s_a/u_a<4, nor a uniform S≽cΣ,c>0, on actual E17. In the inherited epsilon family, deleting triangle7 gives raw tip(0,ε/4,3−ε), μ=ε³/(384−49ε³). Both bodies tend to the tetrahedron with base(-1,-1,0),(1,-1,0),(0,1,0),apex(0,0,3); their own centroid tends to(0,−1/4,3/4),Σ_zz→27/80 and centered tip height→9/4. Hence S_zz→0 with SPD limiting Σ. **This does not prove a no-gap statement for the cleared quantity4δ+Λ_ai−(z_a−1).**

The certified star gaps do bound actual surgery: if δ>1/D, then μ<D/4 and, for every retained a,

4/(D+4)<u_a<1+3D/4,
Σ_+≻Σ/(1+μ)≻4Σ/(D+4).

Use s_a≤4+3/δ,f_a≤4, the tetrahedron mean(s+3f)/4 and d_i≤3/4; strict δ makes the final bounds strict. Positive tetrahedron covariance proves the covariance inequality. Thus label1/all forms and label2/278 have μ<5/2,2/7<u_a<17/2; label2/266,272 has μ<2,1/3<u_a<7. Arrow retention is not automatic.

**5. Full quadrilateral moment elimination.** For genuine cyclic quadrilateral i with true neighbors j_0,…,j_3, let τ_r=3η_(i,j_r)Λ_(j_r,i)/(2d_i²),δ_r=1−τ_r. The actual deficiency law is δ_r>0,Σδ=1,δ_0δ_2=δ_1δ_3=:p. Normalize vertices to(1,0),(0,1),(−a,0),(0,−b),a,b>0. Edge functions are f_0=1−x−y,f_1=1+x/a−y,f_2=1+x/a+y/b,f_3=1−x+y/b, with means

μ=((1+a+b)/3,(1+a+ab)/(3a),(a+b+ab)/(3ab),(1+b+ab)/(3b)).

Integrating the four triangles from the diagonal intersection gives E(f_rf_s)=[Σ_vf_r(v)f_s(v)−1+9μ_rμ_s]/12. Therefore the normalized diagonal, opposite and adjacent moments are respectively

(3/2)(1−p/τ_r²),
(3/4)(τ_r+τ_(r+2)−1)/(τ_rτ_(r+2)),
(3/4)[1+(δ_rδ_(r+1)+2p)/(τ_rτ_(r+1))].

Their ranges are(9/8,3/2),[2/3,3/4),(3/4,3/2). Opposite lower equality is exactly a parallelogram: the requisite inequality reduces to a+b+a/b+b/a+1/a+1/b≥6, equality only a=b=1. The other bounds follow from0<p/τ_r²<1/4 and Cauchy.

If j_0,j_1 are actual triangles, shared edges eliminate τ_r=d_(j_r)²Λ_(j_r,i)/(d_i²Λ_(i,j_r)),r=0,1. Put x=1−τ_0,y=1−τ_1. Necessarily τ_0+τ_1>1, and

δ=(x,y,y(1−x−y)/(x+y),x(1−x−y)/(x+y)).

This fixes the full ordered shape. Set s=δ_1+δ_2,u=δ_2+δ_3,a=(1−s)/s,b=(1−u)/u. For a rank-three column basis C of Λ−1Λ[i,:], J=(j_0,j_1,j_2), V=C(C[J,:])⁻¹ exists because three consecutive genuine supporting lines cannot concur. Define T_rs=Λ_(j_r,i)Λ_(j_s,i)E(f_rf_s)/(d_iμ_rμ_s),r,s<3. Then **K_i=VTVᵀ**, fully rational in the same Λ. With two opposite triangular neighbors, retain both roots of z²−(1−δ_0−δ_2)z+δ_0δ_2=0, or the single equality branch when its discriminant vanishes.

For adjacent triangular neighbors j,k put u_0=3Λ_jiΛ_ki/(4d_i),v_0=3Λ_ijΛ_kj/(4d_j). The whole closed sector τ_j≤47/50,τ_k≤7/10,u_0≥9/10,v_0≥99/100 is impossible. No true j-k edge or simple common vertex is required. The exact quad entry is u=u_0[1+xy(2−x−y)/((x+y)(1−x)(1−y))]; its correction increases in each variable and the factor at x=3/50,y=3/10 is370/329. Triangle integration gives v=K_j[i,k]≥v_0. The inherited actual three-roof lift forces uv≤1, while this sector gives uv≥1+67/32900. This uses the genuine lift, not its redundant averaged projection.

The actual family P_(a,t)=[0,1]^3∩{x+y+z≥a,x+y+2z≤3,x−(1−a)y−(1−a)z/t≤a},0<a,t<1, has vertices(a,0,0),(0,a,0),(0,0,a),(0,1,0),(1,1,0),(0,0,1),(1,0,1),(0,1,1),(1,1,1/2),(1,0,t), and facets

(1,2,5,7,3),(0,2,5,6,9),(0,1,3,4),(4,8,6,9),(3,4,8,7),(5,6,7),(0,1,2),(6,8,7),(0,4,9).

Labels are x=0,y=0,z=0,x=1,y=1,z=1,then the three cuts. The cuts respectively truncate000; remove111 while passing through101,011; and remove100 while passing through(a,0,0),110. All other nonincident inequalities stay strict, proving counts(10,17,9) throughout the rectangle. On F_2 the adjacent triangular neighbors6,8 meet only at a nonsimple vertex. For D_a=1+a−a², τ_6=1−(1−a)/D_a²,τ_8=1−a(1−a)²/D_a² and τ_6+τ_8−1=a(2−a)/D_a→0. Thus no uniform adjacent-pair gap exists. Exact controls at(a,t)=(1/10,1/4),(1/2,1/2),(9/10,3/4) verify108 normalized identities and972 signed entries. No S1 or catalogue claim is made.

**6. A complete rerouting sector.** For a genuine triangular branch j,k→i→p put r=d_i/(3Λ_pi),x=d_i/(3Λ_ji),y=d_i/(3Λ_ki),δ=r+x+y−1. Exclude the entire sector where h_a≥h_b on all five unchanged tree arrows, the actual sibling shadow j→k is present, Λ_ji≥Λ_ki, and

x(1−√(n_j/n_k))≥1+d_i(y−r)/(12δy+d_i).

For266 use(i,p,j,k)=(4,3,5,7), or swap5,7, with unchanged arrows(1,0),(2,1),(3,2),(6,5),(8,0). For272 use(5,4,6,7), or swap6,7, with unchanged arrows(1,0),(2,1),(3,2),(4,3),(8,0). The h-order preserves the five arrows and the sibling arrow. The triangle identity gives rG_kp=δG_ki−xG_kj−yn_k>[δ−y−x√(n_j/n_k)]n_k; strictness follows because distinct maximal poles cannot be positively proportional. The threshold makes the bracket at least rh_p/h_k, so k→p becomes strict. These seven arrows form an escape arborescence on the actual filled eight-facet body, contradicting the accepted eight-facet exclusion. With B=12δy+d_i>0,A=(x−1)B+d_i(r−y), the threshold is exactly A≥0,A²n_k≥x²B²n_j. All weak walls remain. Optional OJ permission is never substituted for actual sibling presence. The recovery includes a local triangle/SPD diagnostic, expressly not a full body or common Λ.

**Remaining frontier and continuation.** No full form or pair of triangle labels is eliminated. Retain the6637 exact topology records, inherited strict norm/Λ sectors, all applicable star gates, actual mean/eight-edge equations, genuine triangle/quad moments, and complements of the stated deletion, quad and rerouting exclusions. Larger facets,112 uncertified triangle triples, δ above proved thresholds, both valid opposite-quad branches and absent optional sibling shadows remain. Nonsimple vertices, lower-support pole circuits and arbitrary SPD metrics are covered; no uniform gap is inferred from pointwise strictness.

The useful next step is to impose the carrier mean and eight-edge equations on every retained genuine incidence, replacing independently chosen d,Σ,K_i,η by actual geometry, and pull eight-facet certificates through the bounded actual surgery for labels1,2. Substitute full rational quadrilateral moments before applying the three-roof/common-row system. The E17 ridge theorem suggests studying exact first-flux rank on further incidence families, while its singular limit explains why numerical rank alone is insufficient.

**Recovery and verification.** Save the following complete source as `vivid63_v4_recover.py`, retaining its final newline, and run `python -S vivid63_v4_recover.py new-empty-directory`. Use CPython3.12.14, standard library only, assertions enabled. There are no downloads, optimizer dependencies, random seeds or omitted inputs. The decimal integer contains all eleven complete native source units, all160 literal integer certificates, exact controls, and complete frontier generators. The only transport setting is `sys.set_int_max_str_digits(0)`; decoding yields an XZ archive. Computations use integers, Fractions and the embedded exact Q(√2) implementation.

The archive and all eleven decoded source pins were checked. A fresh source-only replay of every mathematical program passed. The decimal transport reconstructs those identical verified bytes. The capsule enforces every output pin, including all270 unrestricted null answers and their exact record correspondence.

|Object|Bytes|SHA-256|
|---|---:|---|
|Recovery source|75637|51d8ccffce0b249df0b1e74cada5eb180546276604b609271aca44b904f28328|
|Decoded complete source JSON|75869|f8cfcf5839df12640a14c8d0150747bb41dba828dff266a4f07640686f3663f1|
|Compressed source archive|28976|7492f0abc7bb96fd4b93798f8f56f4feffe14a8d571dee7cd0db2effe5fa957d|
|Complete verification log|4015|1870907723acf19972bfcc3876a186cf1d5399dcb6c8e9dc8ba6db0f861b917d|

Observed acceptance includes640 PD blocks,5760 minors, all6637 sphere completions, all336 unrestricted pair exclusions, six complete Λ-to-body reconstructions, the exact E17 ridge determinant,108 quad pair identities,972 full quad entries,56 strict filled-tip gates,21 positive covariance minors,567 signed slack entries and the mass-sector margin13/450. Final marker: `VIVID63_COMPLETE_ACTUAL_LAMBDA_TRIANGLE_FRONTIER_V4_RECOVERY_PASS`.

```python
"""VIVID63_ACTUAL_LAMBDA_SYNCHRONIZATION_AND_TRIANGLE_FRONTIER_V4.
Complete deterministic recovery; CPython3.12.14 standard library, assertions on.
The decimal integer is the complete XZ source archive, not an external locator.
The only transport setting is sys.set_int_max_str_digits(0).
Parent minimum-0058, declared payload SHA256
159513b19201b45a7b7495a919e077021333865f6f160c989e63debf72597df3.
Immediate checkpoint VIVID63_COMMON_LAMBDA_FACET_SHAPE_CLOSURE_V1.
Run python -S vivid63_v4_recover.py [new-output-directory].
"""
from pathlib import Path
import hashlib,json,lzma,subprocess,sys
assert __debug__ and sys.version_info[:3]==(3,12,14)
sys.set_int_max_str_digits(0)
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
DATA="""
143379570012788308758013216657501104817638572784318582997223309559345961217336633643503683637924799349006336679306643791
794101849903906300405225410342455258120037541447436319983437340427884935840128791011718191513343549415634689301229698719
400392496394338331381443872549296170696048373463218293920960860963738389010497349387633267738772341792397522937706321248
105689119011055869585241236147111746762515102035300488896222962261221793180084528434502129383454082994965005312383895627
288228737373133248316569745617805864108870425974583937064945452972144455107986184305869961256263873376959031869223384652
330148258299505353791148543000874497635828377591832494604702252040234080990389480975485972347488330643174630072314306055
565876054719365711751116541137515342265697588776562484652103576865032458823137313857476388687866594080606528200638836333
678864893942789992180247770567771339423473793209502067972170734075376231444313527206382816663897072856613732567684725189
534015355044206204336469894071732176008376358395722614713104958750182934709856608353818676059000214943755405592041841564
999829715935142379157116059322572519228881636214872523970022161434062523212399314610852371100127652684689574417732363758
334202480298857168782463598052127046878548267318054523919236645847152652969538485836522770931433423813592975967024957358
095160273250919524871554294283421336429287513691277817841318526498888396292604976767247970983463429365265468296718069963
376386364016760689685326322819908930379780109051456872790979514358944374698389948396270275810028496348634548339199712799
252896890456562311485625325620905726888828118503541650683129427117601587787767139203727792138440354019908706607272860055
835198563572935391530717043953888792759912955766854997280954069890145996822935964445563559653210028874903977491520915742
354490106454047529042200865679759088667843222351347688469564993806706924054485584892440972248389731605374258961852845084
155592263852669317546639672100271741559693399359709192157921935099461552645913414916895591067602746083955217400306346770
662241291478787277924021045658222409660492014766413868156252393123920147146542205934630940095889842924539667967710328175
178324039882999887619540347836215486992349139500084828144854321382063025819173444867882070149419338913827838863544878427
780898580576676126281933559643288172873162227305015566510697298280379640769934880180984986918124205762471992741289001071
299974526496825861570526167376258655898425292036820061983441997316754151482512631362235174929798189702813387621831998237
523728634791920973748346712118022021304546283205669015325586854709516592837109531118838838515742567312454121223735301984
151533693261974181996560513269559104142807826161288720926481711432588195933706443692776763762421028280160540782372199471
347896249680580230149280294576658097420954727762046923303072297426629552664882952474349795951307979747517376239484851707
733150156251236205807668506765973711391478261867523588562171517842341308719263915834812217593433369316074279343678648164
932437007065073639824910868086529326332931349655021295985435495167389385725181743540929339892810832714200330538593093011
571865409810138985395971639119614435208788229383001508604076369962563523724783107685518306860064695053592318445619683214
490204502110873492224513202639951840477465964409812265137281217289756532253662662024890113513907090895009359124353961636
277594497182722606421128885244743868494441119222335115978133781426129847697415064211668876944789756259217000124095001628
684927017116349705754128034313962881989205282106986527614022497526094237620205071942102910483551599042968171430315348687
401161427624848846742184889222901833443047542809882243061903474681250605141966236031297890146337989982785440913423338287
001385596726450267609581989310414678808122255874682136511507026494492130686525488165947016986168930635218061781597757924
404160488201398972781999563790356446807363004963149809091903157509073427594281028193056559688209188415950034070233676473
042050308871543258218122829072661159421895455798772064238086561914428542021291949778398340542891212638155255892775057940
235363972822209349479268918333281776791805538407372832160279109920683307117184648227213049207443855064020527490413598257
241724913282328428344061575056875528978378987832256171088133556753030522404171516071249522743566311979686511711976542989
954330691221187364387505577011083084211060882839405095037464768488765664215431553623582151435010416579129719330807599814
745839730657985769083226478882133961350400456802728534768640346992952128235049640496954067103234086828831003892187156001
822719187739886972973174298596109515774557471250993009153745775749587394983580388941832659652070824203126220157912394620
991082086343338652994372278405345422297292088712747527469179874435273794049908656794759992736520890618200548626869639082
669875899090286758601162798236595125542187176808736749469572411978906142191015114226015166326899026108945680342194263905
506685939912406310094015343600247456056604880069807085815041182922010391028414086676468080636457037473353679307169177034
352783294307626891946384169897567635227270654972173447153158252808372839303087005794915522214004045547442669977071040938
599966174861196913208517356680209216375787658567952804379232258322133984439675452987432990599837776024058333680161482533
278840014078532412524364742248286828328566803591484412078227193170955702356400707760163738472048385463659392309612753396
340552891053608192945981585934137804033415764128647878290805524369181899843745816910303636448440839902677549577688165535
285553957855970278478181844693555547397360358398155491554997741284511611859147198355867941085598303337276427183701486769
378037112217683462918476968643476944071216250604550786497240206393056815986132084674340086262108927393589175714588512500
194661371794660077645322468745271350340007735871722615538034659098125766120384882185891319096716140619406974695454831815
077491864186666262949799901417350784959121768485228542102666717904805006085918703117849064057064266503591324731551579518
247804240774040517989990830200983219862741868994945138680096649502697183982024370726048732887092664831167166595576274459
413129448006030407957538673182214850715854536848589254168896768524149125117999110457369790368563909142147321665186034286
290086563930130352360325838048951449005461511596705301801300291881177274686881823646978682422837330868399783170400821343
766147487615229209771287642771386446707651661053535423402378955430083984276492867704828981366522886746691548520665856561
893987797936220184072044834422479910177197665116428746843516677836948970904502725885500939488528278321464914852122206252
576017009257027896338564145668695233263947431114770205937489582966424185858310646844203967494551726598504540366385289178
306853608821487536022899224187725238019778857918685172241177822649097263036416181917551994182988523936336485319865143458
793936692830151887893065638197264893390448305469688725619780305193554080317338479423225265656106850508272537161646375783
576471752224193842606932242901326793154582943270107825107817688431418621719041897105909786366716491801381097242986101357
488604862782122568145701679138691739692407647940489652570218312711489982080239557955524516601627076646543838605246178373
238256814255118979390218797321766449793019288009774714696948374221678382932308367331401771358209185554127993562040041498
470631585935535251616119088130431058017778360251092973300359311579566644126521186739552591806208928011163921038818461129
663257456765791843099020149024357203238739514991866242297523627495108272078231220574150807115293083275834329698358888494
244065915710303767562764592267389040978797702953445011376018336215970891100407748189018847171815491492702623745943302420
630716033795646726731546225486122508227758122587364694365260190884137894787426384676764822841348974600555107931701436971
060113096565453092916422576011421091983533466897080905745334120567167280485272956869569069172248884868913705878544994716
741173838403582635846560199912631024266355599048512492195410009753167807883438455975429490300214490727481339382852469388
722497003787539199489914349685217983578055495533525823444892651831819150968549888210783638077676102648565876668629681065
095298753999658366318541400726893526543267884233500254822754140110240001852295429449211023399198479854326403725948623522
562797958989303130283810365588939076330664940903763683438056485897243463560805893217708890416482581763791079899946196206
007640522713576778450097155222969371664702598843414210098793089711097334335103584108861509778223423320651089874296168802
593857706433457920791731078208137571313929039118433312169850388237609773674154526214771498823957680092787164487888369575
713371191065157898005955696798504456853665972392289559512169072985517531583992930904974255915657994618849781018236961993
002337297527228203065100472370783391890355901543733456863593035734908805903474163359808850470958917765831905246540149483
992607108527766021946300859802482611237280850085603780558137785213934573735800960944260039396252219013590971037835147835
435585893484000949832397366186189766779526698702804362719308619388677228533600893907192149468578001823763403168649082818
165491066218871351958785513290811458039292361266068818558494666079204342441119036540456351830463080913006215928122147599
113494616867490533792440833491972357281736524114751867523585036620692997727243159098412784778160920130574052051577528617
531023690084219706422476821784877008863262524319343133693338285005583427318796230392776273902098599357157581251009581591
146478483500660996544732803213912806489886039091220351260840773248654711630725212929389006750582230464704176949779472578
893321157660965494909360902667446963770901812865914621332185919703614730861183921232107917535947170067078256164434546550
409490433807070233192447949803652223683042414991205345266181009910654926052795253243760171976276874420895253520811526447
611089882240520415800312325614662889234546968300830632583918632250661034273526442367365477380271539585588532738753169867
391548151208190875666908112342557744961309986904431776719968366290559527043560989063934892417736040980029447906144084939
974284503007664249245567969024008259363828934456580697873609786440203028945208615260633951673008334583257990308777504396
402452113458558558917851290323060015995228396916180491489886511993840794264935795846221020838491914098718817992315801440
086535247008698978163117369813240376041163732704952213326739606416398055272164906047660629351965597393930674542657999873
990226981915278733173008232319218265940788487986444347985873936605839075709268426441739472396059598413794501483317684425
097121929480214308833676789902523817126220987667337479977815780145626552844042868764748644082970806836241385875142638960
205098161249116416868583269235647403656543497168089387295663806920107557965140529325679190375958880275190387514047898159
931264282150785576530018033854361199315189698592356571900925114331282754509407111733388429133174420565386281950396570190
662580181262473915423716150647314190950892977065889823176051086487164126599687143194564606962314206821342933950081547275
941387541685094546583266736547857116249504486534629730772342509010680541261005031519793074774249353599309823763630132409
637453213401410204708293109088200728601402374249160023749723698835189203876019013544896633404290528478435653977217048293
631908054759595060905086921587729028761047114490880637310481601990302455934389491752188401197029025153665525052455946423
955655541429907838356211787414794958564390794302828501081133558761754259261898480707980329801659091415689397699384942975
595580509220242828370914394487019200192131711707521840314484674103092381642210019835871538669622207922711232622743384841
258422608784135325285378369671518720151386232800484840064566741414648785489462582334014380277272927703332365331242935538
684356343489147637165570809845097972143775742071398373639606218783176084095168009184482070390881187575012211061419735581
487489138457807610654119737051792509238294164722463330145994154259775509284625946187462514707750597551773175469591435692
106888187139114551577727652360524335963832026367129766810682154807798245250877787108393279968730863314881908131181534024
063735632175553657790796227014946857159055658233399233089187094015055536005805767692141944863389246686849603816628468535
444191422971057715164398770220229148654213026757551125181613461771268829113056753099702441082589389226952426608731080490
468795107861524225331800697050569470929328672296354606572104629555183466161375473285931766625535896892378156414003477124
880975536020128145742284213254265837492349405025165800799505541331779015710834350289738473054935279978120491948510379972
682771651730771539516993424723867503535459760919843005381076250259295938759806724300219853086323277414519868376405039427
649828192075578797225600491047168977694626728721481010752842793693262193482125564839727806187348066591303546149568769339
079911719300694454978444233349919624271068056438564530518546469052710878616733387221489187922274846786120051097398871680
780909120552431002185094357830908720196027058208037045353226846756232087624931844285679527039607446908779887753270062890
276155448328791363444779112565224255645449172888477624314480552968759817429844865089980516658803827383653514341118025934
862519687357846201103107427875556834032908797442855793231449031675410840121373822724185882416001063098054768307428406401
027148253583591176507665010660487649131469221029869207452952741442497447637751831164829223722961557988872815329532786439
472567532579834926627917541770816956788591788686343533937067891707861274358787726490583472668579900309434107052295883526
946359136845568408795119652024603859974965446133599700121132185423343793727320911251913849716970517056805195271416114422
626370073753480745204208104262737234466326482742476660634226492642289351637812994681261487961003957158034821323829336261
741356548905346560416470670786631885422018331023204734268256371675310444256006582537155078430127218644326503886764702157
000462734644808021688492326176607251665127385741822207813432865515543972646480799066021021568768645079510442628688923760
157671141913795817165418144359450294003051829679448251379966195974356934481491241021647913395152999248076182236882087550
377965017928734953046922095021710974185853304305120854559055469251756308576374257067468256241804060680523955042157142889
730826458529357243030583109551674995015953330006496832826345495535720193803659135652983239861198295433365299008616077487
128969088914776575103731574208758238431389669249790192200959277454268004993993114564308702675243101284366072760152098827
495468055163294572263831000050584853221845814106611892228884606860494820039316244832876801202380304921368838855031848695
193817205142869055810840127352240495772757893979875636575987266169700367727205681896242434143176237185870804591050595443
869100505017561792022683317544211718936710984465943590019558021828985003013020976243783230127512380657304185654427118087
026683971737083520669186370240382751905318364175795280190162404806012244960575044307987568569264133190333774153181739339
385838717685652573985021027394357074554149065436419516615158129025974977239908675546176714008202004215024104720495215918
608225426376082158727197813775059503985524153209248637651396925818281725331553530322298465861684683501883781953308997857
653342555218852614755313501335509905091371644701626840816128565331447821611044153376732635285468377818593861779477656204
211477796163867874378652446878551855619607752594426400979261315528333888467762959502537239141356906112310816643674854753
307397961027526326149951085949199856074499155215850674148593287463236360401072708009954503099479137529808124333638777873
425031278511225250504761708545506857127039743081590544814685402298937780847408493580379187622217070927515067731565453741
570027014280902038437372261864087380804433436104096181270427510564197666535531327320710324370360762778533440232239456869
118245041654768260011576037074211182909904953532985635878533263567015452567535128219269428551024193285232565345289407762
750510621922046966203101488889100121623488806494761489166778985764210611202014465597267364190729984087929983258044466083
617894204493171697454137311151038815174607012970107007503353110695945563547472610138658115339165510999694439679038549498
828465059120798563943175586518715949145948070458117435735009998159147899629481891463741650190450177366466389028706079028
540780753071090761869807329446081927018575951030409164283991137104979857980992076920731759228696165818419102674334500038
740278660473738836911175935659213381996084960833373900204069623905081471934421019683664166883493151191770262991756449899
379106812990613742887317086512122620477243654672451886957867033549717649606075782520945778289343959698760402800610714358
745320443552895057816876855261221173425011761422758477228585138357584478178479072808193989455801178486633385183979162471
416998058112923485329395756138184403902092362847289854800219580791582593550869029972807984477519773538551812645507648778
341134806146960184655623536224989731958945553045106534557330612360290571643969015671543020432133123491436447418574745745
263351905814234709368784152904065475572259643968238076217970855153972099795412253208246557291979299662453563351458301027
120454415960034898684201332027013607151584653305924003838582326146052004058153418313311742558988016286849972805824209314
059478075793530818952185215854011474112257436390994461346381404591202964912701321913284622097310074537386199907000950631
618848265835485693145225237637689264469327822477447035550981443941596958616109942897994566251896529352965075205949459447
991947130429881209525476202931292363579331542750803302888873112537332329354130996366398306189041864813766708105440599504
393805452442288105341279450478598641612403958543175594671100032114724241662219228079985475105675118977288309584274436405
018086132521033078194435060968819738017840514410980476837667734300032930014475754118670769644646532180227378748105152885
747560713674390314016349993093644620539407068391451069398600634488420686478779378282911282259177051832953805102736355532
320161852876199444024086899583682089222219096077771859430757889117234365188936123577692723421715797001707760173924125031
344926275040866697304287629491356719661551654828828966497914629391108827820100347676951110314757362904692460570709807292
904318017593571641978047644484889827097134120564836487614801674971452351593864269673172462031604083691669916310154039057
987008866373773029116193657915992911533570425997596688950198763861637420468556522803837590316201948798366595835307672502
859816592382996648162839112852975451802803790690360787568862561741626636045075109226720325873305339551940517421896141959
204462410084203533162568302549384294289492289794405820428487567965825965997447048003596640482017711830262377275897272353
534241171138291706653310668894172626517428424214486876788835401959625240539594910070525444425421334514366629814565184065
662601817962373778451625837928009253848561666076962333585836463351839199217080448934552650480262954235393378553034807432
524033834219865150660787277059577194818992892404661612226836392492766707112782431999827198339278028046572591616724667506
339675526961031871208279780774824752950458625197961246562087759613302703562504770922594601436941203296804570510173906287
826892894311669054131739609289172765581365929508540341247958767739737850306489981791130939994655088534125107800610336979
545651287208214158980734924252645933136843355454701161071214825465000767135131635678628306584554504862881452239540179022
844563958522854481959689634498170799979544926111574859249065216085028388828349846711683278939925155226705435000439720973
842411941798847562961103500144045542250785843165169643675269998375034445675016647747106596941327203734616896150145547941
331607230468314495606634103265965478830787689809233882244154143703380400897011739392761469228785877426469841892782628187
014328802412799280533586423906892048782541844655169857463103039774118922634630989811983808114960118923296989638358446756
031512266336641530614564982615901436039344132100979812750447553017796527607174279708609120738607928510961848167691676013
898194144440054075252011459550224683189926528410171232156207581735384179751727926498983336090796099754561865472868014282
891037117726121121284705699175043589098556575829816489386754461255952266962649235520483931358420147398753559407098193496
504481984058231076306460038329893875114277444679163610650225772283789910496806600379578493598013912733811044119799500643
440793585245255341123845691953717839262350885189317038796415371334305932154924627597489793390326328508876764362688564305
586760628411531548885771877474923608319739681318354918296480347416644011514936443968447040966647060985955709893292994018
231006108008193922444446579439166208857103098987972488517188513516616589628750252935534866628370077736426873016518718824
328710607132824723568318794349791224669044926443648166363682010593551779103896220945474958704792367097223897472095238516
507968022251608117409943682732201511473787844556142366032233053154473286240218489150731673403277506938510384464387584220
655829564788375666013269836920609505607379182121498150205705771849529932872759577063831231906537916453125609117837123481
439757741045720738431507531745201942002836313201413814313116275649284818878781962181244073386772769818628459437278583794
052741002622819896024907510945951433244669596518254149280486996862206605060501127067270919127590554728027608784201888909
734512977224041884951606751022948845700773200426249453227284048089136567743436139994069577719034721940631658269292216277
192557723364834670407478755311867263658105958229180771617284437146523400520299569474685771111298242033306792414995947872
710676587370351865795408738938911769776014227889635921997722547459696352743990126457183254829244494493476044404119827641
366871366012641750052446968961911352845044329761879084850966420961182218300783364772261727809544262234045516595072813237
253990561541528526906956417367084433043655296743128083208120499109732716418877481863215563244033824740060081488429672913
325379699123488500567837169280489159543902972820087143739783146062113224906831099362513986143139964438880803006505119073
206825376889459649700212672926214362145714260861285801201892710869156796854448496248759406341272962302434846402726223908
326952798399745885507236393607872241652466842288447031830789970109213171128155950561582265170707402828532272226390862291
001135949879761529989353659882614056361931534485606853279428910933265692176753380715229793555193237693344576360181159219
616549482619249557622098152727328647799539018101471651998786217298226793216893043609691477094399477874913414952082553369
082819789615174217926413767561774183290947403416831129963468290536309915740479875020421271472887002250362265312831887298
041654607391868379483148691400305186141610634816878619480475139101639980428183958645774028206140467481090357962803365049
056002451520126025205504072418382340127025742425074098726276276415167643532043282416093558006571691619298330464509805880
503354677859908122338870610028789517659537371069565389324444392962953751517153856943304074973867388869091890892185273770
704964414180573171039926282027867279141947243234115149681628723158995759198877146282995590840860469496147372112943848186
930790124975684135405700042887011138624979898162614426447267247872364670311206422399657956144974004231364367512631493958
849669962259200373652192920673859072047396623013148014923595670986482199513790001865031222840313144165455611020394248890
634916621531964269963449280705001436657054221805737478951329234206466173448398143418729208426056708048957793313580925742
735516988300300730505632617623010728930256621839364139626074267354466935251768700681531468069168454814385706500434030820
481870705753731217573596635731847338863591717645366368511206138718146320188890097867576622926216024561081268429496034034
335025147461359830564603407398252629945104471475541878595125707407069889863127189405266232891772256152696183653296784931
746574657915799489057360616092807218765832580092967612800718284030308583488918740288237438370404691876090676673456365108
476710212410756295856526205024761214896402295118467542605960088667272540172037487873750478227873492036829755661775989275
987930150980443759186666186761867569889685503933920210506665189373966225144805619522069167145944892754235308108678737518
758273733776698797677344247297540911777388147256220081045857457691467453038117501184363432653140763990257425200341731277
651423969874579707843258840903145474313961895920064954870162418609788058236238826316117239748792564954657756579240372460
929701575669301394766317155959457294762196463532808694562199001554937650568652278942230055645913135770587747985364487433
576211318911758331775374694476136238506746083955317198336853324389785794320347044105675665416633656049244399964358098231
946668432035453994234297532552610406167482728798764978248264480766193387775040920191144339453618829281264514632843623585
023544845961800382621139043187244327490043418704741855346915198824783906766515690504163772217061938807848201551334057289
304879252269824911636982066493701243168528223522164450611570828295223656326168686912301980708201252205668785050148497518
314935044983478365807853661487857849559341687208013509017664471549158930685522102425025914189399988307662849265937607371
117250576151627221529748042365310937362400909112747653142107201023386501846262443100232153660992355665938799151344549178
388858824120684250145741833211902420676646834786812781243022839565703675208171245077842112941182098537687969453393589481
429095211075090918558094154422092649253896079316384526445381409191881970987523514061298980173578223482705564012877196337
363582078535575596991561311410875122933797520300386827798993630451463533312655476132457387897789160679963032013507490549
366913814687798919112435912428551526561579325627840654181727249503838774490237266814955035553423396474781640234404941612
591906572277249017106819792721509512784844342076747790987734809360387901806352173881936072281511396869844253488598087371
444344532659031788998824217924910209293338846385027088175617447659420366932493162279798070481514376720234606605440479752
748041507817113080124754875362060224403115651123663042409901818952104832388515801121519875627953839583990295597763152241
745520610425578491556114229532686106052241159675157646308852637517865629209798079812655380390585151558466028442134163903
883958548376064554448919016049329477031714866248562560735289688940048791458601587723192295696426114221376854237698128138
675621708223636778715306877929235701331144526514429138464515659908618027536512576490888937496247257480279451215594346828
548328550067663321372650261494601619625234902227292305507627451271475119205152885675682920642710112480414218600417195799
392494156048430995683680156565694819784223828664465639778017063211918678461088007175869599514760311339085814632441126575
681717238334582603375019071657257119435948424258891491837830965329591495186473243768141235665222377012489098098870837214
806421900163362559479260016948782391086526865356471647815963961579374229120782306264875839184691616764417301590366706593
018461906195799706583993198305278290029971874058494018026281443691285117121771954889258667136134066388572750420417175675
237276528725538730548964526390922500752735717634501959732270754249218889305637163439636970095717814110585229303525387139
811524697933774602228790879269862232340612115354759432429255923983887393610568240970437146338299251043455419272272903200
308929371277894449930158158222960972242113137127394936379426962112255245397856496929113745831550822438502314031825436891
361232402688761497798571228642664425982865294019959141687437167644925617925352292531853099615838767746829579694370990580
085427544826738401683291501206032277145045666889426570797193775670599824106847370681759600105260085978382197906150733611
447894182033437039048761337594057538653016202387981528743370370495112317121328681389409285385288819026548415940741072314
397300435238732823147105319706541714740548706797208228286756593503761438653586700149944548051792958989519656308083067973
545754434656678055971734268139970348294358087461789362982768259585342878767274421174666060288411998388122635692853499275
663867056291297205807365187765779574881273574495372878680569818164902186514251239984885214942568493156047696056186995114
471944461876412444838950363923394995924333886982786791108475562716728292773422448773628819679900222487101661147931099320
360120506030378682550673215112754963010358688882869019876305096547760912666062338737811942907967845871651308927040332978
265466440207329131203372683079707019025415615202842922965281630389161509855686226914881155667968455285198224024825627062
896498767328328831936234984336707469094621584601289674553727766747252150740131340960768710039612730833084392565953821091
403205650007875846007896949909973327139851939703783280427585037959610780878671635757467549312275021734132234123422491125
920162337005306194494745081683763303233907770964435023885267296701428340452784894912236670663633040533128786225253074027
412209715717203470397937752772750556440824887761318701040894684474648300135535638996326756067057076402722581351020815841
657932233201936529232166305241142381982387361772481756839239234660896551829741703491194523265665210975029636953514941283
957541759682271800448573910994624190962702970184812794042053044829229803157541188016935273661218078813870969067450440651
734548781515452908441961739611582327519890279058055482024917290332132894650030032029084571264423662288550801925013231285
681745235527884828295607782277318539774350768874229777579616077835063654639768395438019197975461992110811146497076048997
586767937582117915323495266656216600310907846428313947165859516570439394496113377819624668629889678189086878610533573500
024639084566517282457972645710936495845839803997624364723706465543161809949181418414099915760640220760192302918662346517
702930932166060830647232102055564644466256846953143630216477949299493859866407328012012002701474508505028714957430473434
335411613220048485642380047877982911435530219570939950040649063743788073546291918274066815824839718478014309207572413289
376873679861214831836084178865997665544026677158870560391918297740720366093666132201793420444674210415509779069155819329
971391304563754987532908725976459298360932636750341140536174421150305628280165013248566003856440988856397820962081288613
577013564417603914042605840304966156746914379162063219944319525824869725414212140641225162142663329704865340021574699167
921625759242964868714709292685278191919655198396527802666182641814066490931231486264369347740066958668510182405287755666
498640400621915675481572591623324074601794266801196971645087645275948428311013057137158223895605062907745037661053052579
201209155425664064640295754199145268264975069721865232250413734319699128207505474843714237684981104747987859016030481387
135566949835710994984332230704096827485526868514223576286484247907191988214109955509920671628812394635462753689404872306
778849276720607055946935936699172531133351650677053107338191826878689285287252817799021798514155382699996285121174992034
456092633807214441892774887189045531941908766491594432501101728955446848975553206978854227717121422013061865524757404767
588926583944803140280670506959445259371901753851157537772949582323353287882191194092473718988163265406154866182694272463
310619190903013307208309005408364547422827151394187904327941651512160588467612342959555839621797504908683768918501594871
309213553968330322755579947584974677850542795188994651771866623298524829247421586471587337480552285968342169470903852943
265767092900716949973116277972989198437590247305122304535462636608576729479854584961731468032284926984355467993618902896
102817183634140034029099566235693909785458698212578234356451717884501680414849187858926682543476849716818058301186772714
641996021899018093671112302265276222192503064119765298637592721101474101443252740597702330792132086914702235835304050552
655733712452343823956565234060982022364301182795808729698793268659701054962681720701877540898702372186157250479980520756
830391593377131705067282233043857891766283447607468314592582560048059765579398623343378624212647674929631163040273250807
729115645720333578001836159932495911435591389911575107958049244181733822725575978792726723968516118753501453210028203353
465870589457304508841764532126177747152058213529285697048732772557565492586371924827171334372628828062228601891005971696
567499443912599887245864311026292853799049755717213016772754912559104887464307830265845193225704721919238247997039516591
061449706490885644512442734678271156231674450962194346066401141943820231373420054852352739344744882614155853652481184404
246995990445573728135142201218299490072029241405166524105478881709099148130829737031771343516533485329331653663397436228
755459966749952704132846805564090277372916242502022173829420049664026981630114692418637602627553310093211851658978067589
873329878298220166925193655853849739912717371007021784441739104280037837992772504509534863317299966520564123317159927590
195183982441557702906812287558351519847458444531287884117453811085510454155374123545598262485094132306220577199448691318
498213116324156210934197385351594580787395777980296915326137834435806623062829690963463770577626096640785022755251107392
948762753782023844656214308030350948066500562823635751902048823875255044360921250108069393575148129853710976279781455011
404652313687024515103303707058152567234642422151715519815671251890743725127713054420196090458784212149340372280048927143
161655689234515014702654108538447594012200736523221581845469384958268245894921973109173447468703549377600730657021819485
943379841613132360760228291271258734731437956025949996542645122153012714906632525514700679814301365402066281818761645492
708175949614447188910098566354389964277463649498372327483256935074588478901516646080480823695343647779825557567054272281
804645613383486849715862825005151820797465909233494297954220301495869525676011536860650433705652140212941707739762095388
986607671917796196682042007248645358198416998731494772398682057087153410400239859539859962900650979713876918772600888407
606236403677998686966919456138777934411633807165354415802408576077127757802584536621108447233944938925776088434489750870
018764189277604340121451239146227281830465885201302562119733357991215770714751458580351858866553110525854852538130189352
426107214193942206434532926858393568960523271690327698628507248336699283023793673425781538734225265683127579879985412388
636887914473100504897956030856096339591153705415958515624343927945364850491736156836723062775020198757815555937212086576
032167786141806952139283586275718801352381360836153358224601598957028661071414232351693430526313828184981851767142752336
407167620481850160124150709820841004131807098414370488148392165632839584363493917841166465393871357327922870147514112079
150308847409461073761554480840119971285710333477936266878025989447076142892745797263846037551800594604907620204719474078
325651668456935168650452578478237112892621917987753497604793873228881127857649853799200386636752388145377262759943034756
570993076788621394797571706576612292679351912529457753119314507536712691047322754553775753166792791437650838977318729179
707595266027175666360917934616753700997273698946768550818170355362868783602194534779100978086320796436589530868852620895
738133448029025824399560344753438561281419833483940473730649275353092487397720356068534600928037044840149848175086575408
452627621277183255265004497898058417450783929004938815360270790626354538890253051331928934558206326829120542318056799045
699279889899837499938919058879433272147945224248325426908065891470254046102145020652558064757723799811742032474687728291
086735215808120024931287960521850433577487833561025492908871892099740124110411728571518637996453698224148928384599391202
257107672958238935604080094583384920800922285005621052693630683474568493991957721843615440175570536897640239378167308431
179606131708794362350175287684064962196272454089515758565778446976317643176210160443210341101005245420333717870972223457
583812401919954225047429154982830383415955317615412170581897821222020166116009329012643643549800588558941147252143242379
191661618085534626832366794470162574765366461690022361287172745781202666520834783805161642841632021378839201462779751718
178141723906595745968018581852994400078869145044380600192031432407674654881858609627033317482170326373304491828903730162
119818890066129975884051927965720197982563531254454472162186689769424337038283714849638318465359648271810850035699958221
087222256278296281598015862952790545195140746842167218117604201917867663421566959770183040513397137554109787646989249780
713227224165810013070256464955992879186901252240513871128888448357389508090797620762453854956084578172584792203438408950
400269000080092426862473804906914044648233674968525613995442315864005263563814008244670092301042013218248104912594688190
182514676778839052654148674705753579276549581886548378336819464938738261388240997592183668925660250949426407400139852202
842937307268961782612609899403144060082997141870945606748459925208561645447963667577419653368504793139658473200169751872
281965453801984690389936453405997618082744187012849464230966440125282689495971662768719574704372167297490068792518610934
722255025175332633273753576751973074426351292060173261405599855489293574352418469725868101872970857246745332891341345480
039945860678926724854270100042604705164809417195481661631775239488798642546071477744416809258882157298081021987884607603
593327331845632559742665750668674201714919596383515984233707122302704166576808454904244452165250432211481388179551195509
930717212526221026962012868091459316621955727076547235146726161661059630818261668000166925989803100986683153013845597087
105741214760632061205142119059547795382243771427660263404515928439735692638959462753473373204019160073736442232313368880
186837579715896167462519587833664945316909325070296460689657580473039475926326776608701515822372779246239192440058707521
731543040647222907929403000865858226734971687837417163409680685969105271523275096916095457430002316719820678604146800675
817404084442787197423785851829913599688709121391690668222190097749454724143206425886853921011494200580925736777615642379
411857463850042294838366436476497126985939426040479071714867330235865716909958255398050036702868689107023801226134038368
873497951258303339260820382764683660748716234020086149034782725240202445683377125855387788494821290442810602465142992679
706023028089612113606562981946037022284042863260097334693253636694843536670229269166697094174452502695629487485516567318
481632801397363557255488096416755652939661327805024285410879034889165375788865702800170981898235793529791348220226248225
128243435192052735511937771862382708779997766765819125026663021228791176649780580223554398992584267591699131814984497184
437000549522460855101480390673870960152978228027617109534154129340889722393003550167526759228244250993812639040070033124
836105502640378759921573259312390239182042250138534351806077097693460761370887515218535148146422556820052640339311830130
240386863047535860957244965859023655468548651878925446007475719341079273860492887141297758783944494218385730991624347673
539269161763417755752121553445743390378930205822927223343134568107994493574674463725381203658275844808715154155191748094
127558016532144089419132240785161725559774482664518212640264317700803141786040418710447858855806817801308218604846825234
773843147714794409455969496120574907504489037367128582895584403528669094948020060152279116385502998684931016686925159807
096479347473352889606857434445685614354219405202630620158038114265655488797042396620731417280795603133656036201323137184
525134827788346882407735903008128611158174539122938734711716086290363691485356883905448298654377165601015776346279181977
934077739157765470566124842203530222869811010463228241660521194298929297357357374208770395227420718730300848224147625927
968161233767621847204358475495447834288979691269443021141655302299260402462886164796453294951308387299363484317920090574
444916154541714142600124518388916311016452139816278914892586255898803057783241380405276753521846493746100178629887164953
510265367258278467705544108660531498699285034751821600091859541251820435186288984214918379394855654550811672493883607201
651240101110139219906553608963737217891228775100472937600859307080285372789909074056558371228023119488078584871674995761
111116898994512999064127767472182988529945905663642033651058482439647480361692748465491591649233500963749165440529788005
320542703341384400989893933933435374191030164798131594133151322725373359280212759826971388592906650925665177175773832682
975121306783369189117565735085105426876336959780995384134319128191591748982823544543084270740917339558337280972032158240
721099826256385554390821803025846619059164545961833239045274718816318555344997846041448432951851324291729426594211142623
636934056659651453241815019442340058730943812652865697773013620779075939907298700019407298974140036926460899283998167244
057019431168601308974600995751242333317813824860434853738529040029251946468401102001501656610098971722065061918659774677
634638332819743347245869878043105021043615994413024930086876318903840474583201549613709395181776240408635514757987872525
683409228616064469307192891473340121709911429841824745847149899190915881039167870916711504581183876990136698488805106395
133546205959601695408777591782847995302250421722791615074979244274928318261753681001710817740855868696658636422349924888
261046391864536449582714129215074068626836663229761703276352599518708875187899166745861141318690603363226048032227907778
804510067422082980464169064457664136660606279182478074117777398814645545501489780704570254178235240837925472855483292861
159060748357114059503425487413365993256255713495214210689272198740536387921671245231102984855841980327362073162835795277
996336927742655285050629948253005882866812902745644283712114682945483434715340937688915859319849135329322199366945741245
754506159943181657346559853374983538481750249293821271882066908172633598271044704756814686023099543328750019988586428544
362686484314315124290478274875587220610278987458432447409605648179838928551412179602763443854571753919316258296096639810
207603797362001205249119144257795066129258126514835886098627788646372169115331071841998357752884472289041500263439428103
142985810620415388079778629440204708508904660412531974129991233226827816281746447707755499030140866029850727780434424420
936052932549583592669820602611314269706867171544041969535469493577416028851420773774798596667621581848526240789742790487
103975476741044221064857125378621735247987164949258589718182509969235524392076576181599060099629512117715477913883908773
826321026427133452744960109859518154384455361824512905077829480277878465446497442161162370783080693207905254261009045126
778419820084781717031756193052979663713014994112466750324757171730328547756163379682216637762156805145357893595438078921
669454208428143513324783153202191996623512557121294430077327925713970445964726853760122957316024065185091970127515013918
121411869486529674527545229635902932399273180042937931930776916924367711614265002227103748037814043483671112963899027967
228818378835038235317232729747870436773599255296311585882892278805088553703780609557304766418640789162315148963635694402
578757778317392837438840693750121528347184571087849285971782141703983804788303173157401865030836619360131723802961712779
407812136783822573835852123576634181370386685594082272415494232514156143641475502510114401507514976493448907585963534063
397341483318062493733388876248778274425144656743972476402077976390510946541858491807314710976578280741030723930346385321
926300377463064492416819783765674831406506258957106864079858546768213882720956917551359964874854097041858046288735319772
016612450440182147368396516593441315544995043644053393692145510877841828079560855771339511215600952707615926515193080536
751338662977661719322211088193407173853199140385883800794614459713277067431600083940071417432784146887619016017269729593
906908445483314150320602555949937502228772034083497843615820555272051549354823997184716276600784879187519445929377002557
531991914204798673499519687056855570213288179559512310059751332389528836257435800456939525967622225209653245808463912346
436506531824293848091682310363497589506582949783640195936942062647411653450195400406093666317332336953371138314618656288
352186686029994106880765875910967612248200280011822352648027418709106987363681018696667944725425878963481481453424874747
985869793327782192439507703863207859704201238517797040884842693218932511168298299200085962665986272075381455286662961385
495983968386091446031251933690445807898762981155895724518570260740480213126066208336640693919019994461109764723807029583
860229915299819510604057915249542258342156185177013461030190654709806675575213288928571692102267750876261299609156065641
960893412237015489665358274409612095051203268221192431399572505594775808301972076696082462036562705202266003574201193950
541539574688113760021994824089354191144076096833693119765532601552153263161109594238258937310818082244561160881396852210
080461465001583814272472383480084111085913087197327989550783284067619684123950650171318357454318233634151033395612170649
703312309324226271196389681290764328811979782006118441526267572295914698860527097881842462551879313411759933003766572191
732987193067863798540598106317650837307885902019971180269773892798535078902523971491655919864633838383830854118962282074
917267504490251181868807662934703205620924021153845070852003559642882999812393146354769139532707767840065976655841204092
414236529387429660047654168824012019586027406436702824350638487433493888982130056623934696984883065471050208746824480322
628515558177018764467221159673398782568182275404755873516258370844838816758937437148252339224949537682091193473122262982
697078349840776239199587006759404667762626000070913931436417326322738391494242409078403400709489027343938879756073396494
936252269429158132552089219137188621492140487497552457996489527253171006354563543451242473966758679074615195369001476575
730273121146354968138942267409519299896545281532466340111341569065423160026583975613366626290800835155852109713822739988
600417984038275047315866324396631409855432821623540856093622280437565986570470306535390633572937397996628390225475744417
440276670061328475855631834352470554569659164152659017899026976298310952040299227620446664129325922606752048303421288153
712016062908563727667104080884898664569432695993531454730360016281612589312131990737741177624482967459011564138040174762
331287558040653613846438448213676601358441494048800322280261489587416143796214197685317121898491926369385013128736327211
991865776838809130395966694545782466706616188009296733716780566428868576972364951813336638573102212476117333857424877034
568827612998793479045723225203945619539220214039759723122229650472083202911168839986825006169204577285155054813805813569
002149355490279660594352668073780513276043070335997058683670158519089652202248282410024039398053661051222429291018116393
135182086304965878836004007410911629174438088253892977799040813794151036336808172392078469190212585800432006052924467820
930490563722752283064006984824147408441873870963273496576371899346128734449837764919300627307786751656939536007202500291
603354800781557857494488300042279597526243807728878601827700693694095483838094275852176358194379703415994327432470661742
590937101989941812383627296550158161117870573157269465731225219989049928603130103220994600288250821011872431853555680683
748925294263252668488213568461247880542831129361496483892600619789337813225993673299153313473526896272827598996457581109
476287489782948598249219985452192561768106099533066009832893614449699276664089728053405595022039358695209667136879100696
977584498803781719816772266184428457664878743451406896101074036561704386396319140047366750595873554707417496872087777574
156343548024788837841084133752819828892564711833124491731469827780302367093950042205580637569468666426479248605204978831
956998630937916596061400832810615555951556877202948870988032822801802569487954939894917611678922775101711827835074062253
865782746110033171036981012091777612729509454049408829226762129997253928657628325330672856820041278470781357971234069450
490104750054947204123950415303301585962439606503297470327346752441143388204843639462821299630386899982833043870111734321
385313485662814250410629683740258271220280348292965225977792364650393435515589157310114120521455647961864141861823422891
907445954849305118311265131773244518292437392757254162325720308662721755314903017629375119695648273091715644113001947367
200917575694089723388845838053953781985963878952646259563049569048458225231506815419213019736310126188304125975569658679
533121814883238254252507282163196857160801908726267964976406088994168219814234818261947393349843873755687766122460726324
142315739863994401079731499820272285924494558297888003492032106322197623107707088090614630621708834288849301539346658005
219820103672102587112369775014277856715700625981823923054722472439780896070912942548511773486960459359105441303359870024
342628340833386280742641723748783939202312567374662936213646545187919839487600387903799383333391778571608113470939626867
993570313881112230096942014525366321905060349798773758996374784137139609513314767439804586059183727623964119971359132891
641746749415853775794227356076315975442364092256161964558255697995056042455861391193917026897922316133146388457987942755
853572610060550281366325716290913804733880463868254317355220954769729653077893026596945458807795285989387410200737020329
860719041816870271180285339728253273239855556166568646839431855821084243243041473032341343294240562019230190540172685389
686694622130581806445198483848580245916932936555816612527337713406346889884224001209935675344381390690863514998820584997
980005918253450921112173076368084703603263011562682451954764928324851531206938032210542003352239624573566074367809116561
284627608034310184997132357356336767465922215158404426207079952875777040522791577720585714718113917026144588694446124547
719979273573606612037873508295773241895955175406679722449063216459071097661234234673298148378417856359449628717218735656
823755440661095315185040908079016968738351484673806561004232794270377670547437362430306442790847379934349195251314194880
371882949434384866215953917218439820150417475298479570698162450702350606128244110041034273038572975532314092746022302732
629721052491854691654784766812802898382322165118698376336317188273075363284671134687910250670604921032924848687122884051
606697883530441675304830419722191695712033846887250121438343385029731719618381647901672895622494250906415974260631019573
428583642060830790285057371361189572186684413941116218977020431971845642238636924880891437770387091877790638851457522113
826999310928769004156614698634698669472965853052788642873880359783233886642705233963041643603802383751947736109010711850
373947999724796865744925526198357290971971526129827116737561329886809179927367396503893466219201590000297919487033571806
214541418813726138125560572246842141354989339148479845722861139414044696157797419294097086790553691564778079139677712008
931075814044594416975841719683041146070081181383471192122458529404039915272060040240937971265667171393792844205987024260
637123811305374896816373005592549458599154481697878451234807780409890003857143214996052652833771482977534285997828074972
365897973061976601351568732019159830738438344032557915089853453664311512503546879643071638414826051718050768985781453836
235786468827557046536757102023372516981680951785659797101759435602126575950406827000749688251893300534881062359215494663
150225248167579764988124188225576671592394080799274327922220701414827186656876282580893754470518009055187602017413008743
880007164041817535108898019151075342826005596372602217506588868802907957065089705800246999866984005676529042051123610913
608140710342802312285505467027592301191179865714617246479573405660507566437025245584528318322076354725991889203571069569
208011610659138281384432687414479861735562891814534392599770013622461464322187262501738774193064101797572692432438291070
413183734629569544689264948115657100015268699909771059643201141353597685532735943900171363495609944611707245600576700910
285170483182109980184480987988639138454003667208124896957708331442795972646447286065616601518274222106322547745734011736
535980127541344358238443969097007118098162833759066527335408711595476727242654835223233264684194850925199421407764861882
545523807931367803282665324903504922362360225973486299729037400758286067871500933866156481429974068813185852396665027793
362089601581136597861629946090228129667933057004951740670862101073642966504786474431824467364376019532125155009599695530
824223157065368855341059201087521774183198701757396594589265661154842803182112884119632674955616092556391580021008122623
243665940676274668921968655542612519792933154333355161571021885471484329176097717835977282809689528747748889379187859419
684444338182855258192501431802505266032780295446140353242497887045951048285024818544720085793187211952638224740528613395
863311223127456621935493950987531024863344529399818037575785090820785912481906503674768897445019095944494858156826078803
635323281046643167554937016933026605521455334584262153237377375816395843159900734934275261301273851082893123795001784324
847373239453795489737982888948209240168239227301317035115941267798324451322456447828277392232589229561961358979295558776
054347792947178777040043064887317001815310266733560241200355647781311481315205946000309074223019300951665957774385146916
545564152722910993714286377716591935169182197819126365177079970070315667072094464619849526344503852818026852826886839283
694675039880418105206954733637895404699227146839598816489977653001565754799893696671959999015444298448569938131593327771
536742196393081947217420455270288402684494640013916751852350833892809062763708511842662734553806928190070943168799092948
922871156009053169772495126126746521628828304301306595367449791915771840897187536705370084931103519173441050492503134611
069356297540705870350374222583458119870861357624005164089001384165062663335382451200145842702091726602189071611837331944
890096816418159256547926496395156383662741461558693040048962933307688711333308984393942920394515904037527418120506390098
656925765362010344350219685716185308789076160562616449306502979555271712041338091502434066535848594383626646166652684969
010853773453005702276187402302570862427985638994540473238862484715177878013740945865695785354902837097178346751034769921
433368424874174881264413323958461869121512736044277033973190766346178307513850939605284512884000977802527519828106957939
254846807870181654225455637241030591600100614251750480935994365765632274468753971973050852849238577276569958582761079272
393332547481637975195876468224516192062277518961385618503667217116672890010028379389407428886515786732640126308300859975
634470529127169904684451912174875750539058482866242767367432990860900373260404285650373118078236734911350765568577695184
134005067291158384981210396267392744685290353963055508881746120620578807547375954688429330811383598814889440893657559357
666642683962317005631139419467456081493067811241154278585984481159593643068365165496744866053094462342024074741539301113
580644635779355985906893632725561530516206087497427814967589410042149801991926827065355446164192163608819871649014401525
004817271793438948264304167446842280875901768011474870836241237327350471730959856336472906390346883176331340302167484168
980955215184354096237991475259935513221839454067866301647896263728363218469760050839339787975185011565688707812170636773
219906241735286767883023999391057420066894911615137336683598517543845219920063839287081440560999923793777019868586796814
389956871370479570347534371116279745631386541982188668056153649400001138828176808158713736660705475217146506013542384830
858143943772901983563295862013545707518891370988525765203909970906860826159398622029510291905230797029668826109867760526
087931252742979316592792617602631758290866232268986896510713568317022194381049476259086700217342597887341367304857393896
184411222112270012623662306362155944470238562074312278690880115429558255930500682160543589554126776669960985151124934507
550759698271328784342595084344677734378593168355384339459815064681635850720865300228570044357169317022069682458341289270
013606338872312145499169409122568683784339559877569200890649599146569265335831099866982871050368292828958059846520107933
176516986232839734139484285763756679122559079498197892006988739595148716646174168178304009264233977412142149779155730349
196321794280061539177640785533803024712344304482203407401889983040196071902429194973389122732242350594530879022186587611
976302279027625890532032953948471084414264454860877869760872260135961756431314160151720745993906831576015915031526875322
401149512730132612596063647099754483841309895562199424061993987623513607293519436259109781986465313674001819671944838782
586974472949884436288564023745094980786121268097978119042196586274705934967173896037648517224826948891830640833011079927
574540692786480754311191668655737592271196477334971012317616240293340759392435858484300162771267493584143262420992023118
310680569101465168583280235245097804985220138940867819470243138358091779668283677624744291832755245398349816925596782449
195667557855055852424606208819696467783845922797673779897938419371346884716356101336737288920293570914063894448647266003
664878899210538576552640505913731583607441851897412715968088232429699436666732341783304657436176202682123722434533458940
956908867043709568050207089317516379152308798457649195142658270864109124172063756893713296377018115409129840626419024345
480794796262527651349909369401053015393993588151857511688053834011482873564244355006768343290324817016843558615740556759
301966255186888465657705369798660163696668035895419540700163249074814704816769090854844028271346380182014975557722439687
494560206058593643837857095634591049333740081232018128869028470945051806319337671625638733784799168780305371155768121566
417765041667345991631102376711306420143499696738212192999806330225420733621634808262846717983644871381716936745589158196
016384698519256065817092872159727728850857832465291175488808557013193186194198574177292707485425580571624022097092426610
734776495422474655234482154693599012151580664050704457043285481372273898931571054065802824957238134846356367063881122959
141375287555183277663794632524419051219665989832440527502166301943253002591804228008636222151705794691430842335573448069
964377752726164885055236524125911236452881849778872219317636621534988418267111510257560120664881352388415786655745633085
888710539519264300743126393703682243101346218678028425484214221038523151165866318437769740617702758818988004562489349006
040399111182307019713407898214865794357189461713904632217601823692688343285933570773474617978340749940792690717846010206
573007034634755084073910563954848736870177860438144162386908742474957226385977332692309851905871328790466179536726505145
196564710074170970430077236061155194672641378287617939213739164902820554842191675934718844320252649272883105451199892612
422917310489226764874408233766551557445730256167106879032368915194522737050015254408504156052991700186813806094608326851
269195012636852761702599985850078893595590003455111465563229422699338845231242684837253336341963839284320219749943723657
073047690773147465446690208661789956739952678730785128876403698456780528324032765916617115517820734545726433712341843098
025599555274578061313652642499944166775288115672728538308950984742463619084477979052709688427791542048986298399905421228
252807809041504727703660883216836689942656114846000399575763533835576660590513151321694797975138723078143859415682933777
802376332288060667142052926210652022886286541682747720503405405428125767703714014453603656192531780247958336926532566942
256926736671835700594949315043273637608302025946214353027598693892092976019241837964033306054086456529796955006446649288
105334059636858709798443983046733884938377503482650554344838314294757455140752150425861439498764820683538603354086457182
440365662030387590495061112981142357985940170751734221084938126708263087220027139080150456003800774734276342509226290552
721244922679645820216324599075703491794492203454469850573837244295763523617027203563460300265000313225841532945577036195
910317325597727226758227768439957456593496556216169097993880354709464957814029850735225301753986505513903902775089820719
718179030163636424331577773026180323553543187063476417939692684213698689926709758952152080140999969014266074204741818081
034639157016178255833051195003216178717415884190796825167125732017699328334906383531138377371619490149420357851756036771
752703777198961802304214830521675241517912261872059733649692227079395259633847701284437116651403132335353987579457195874
374299835669277425235447028742246644538499793771345885036486993960194549635479531802240530983613836105289121952289084480
029106712616203629301952833961118497822209524094898080740196835527600915788983747894739227098114157477178018940625197653
831741225141425029815887760346952343659350695676627428188641727983980493354251761287482062661429208555388704156051874038
872089334200185436614501567881730441456809647737766202994229536976379270761207982253584262998376966463437833236578454527
596832188611964463645550938102786018655794065815294251548749258662042604223053491568202374684526720939127189198972395243
103196997242369581223530578804518756733127841770083310700896985337252285553727755301676379036428285841992265647510499330
655789731855374568357621403674845965807967589565904127162246814353606481361747980152860761657939687755105502651267958346
822170813499949643067950092331110587510873960031390185677235080243577258744783354585951505760880180241908881662734541779
272097305910230220587428106617542101518351451758495411304681911187070288542406217598394928000143526017372688670946296015
293154790280481027355294312113733057012830783552413775085770476926009145336747551258948194748019635055300921399703614096
705860016175274261237040686157949496518627729868390711531380367837996903043851070165125324363891896486312130751041504970
206714154078318622510227959825861051972892875753382322626173435688581706626695842536059387722261950823576963323492450294
186373423956431503106231411297353558259277190221330793109704477465356184533966761975282637145665381882597641825507719431
548649600296221829897537704262143240665047874625849968394279065681870927627694965933225342102272984669824098360594404590
132304284914549911619421226550487279549051839018186841720690986606044315872479375614386512065822366862851323483904251704
440031947708441839694608610720817163123251745127952120852229170412844316152177096871128464379271763829205502124030387929
542322536884165569504188533452061179240692322450856841307406265657700372109441189342167606623425803309528906529748061884
505215700338064999933715398814437387139751891993232330700521357489601161555103632039126061317438529910871621993935880425
062302803106630378342508787758093212472413037881849006442301641805736531399243860048964408035555436283914807307055348387
480595440425429482941236597021267315878878370097401732273501354895257306429875644639440774157510995364207544263129305661
832681103840259370787138297191152107684471214562785081169240133590822677860073814319122512558265521568331430284963971483
308314051571259150605828273770188123227744193679407480435830811323524077148103178056251853235564649234177674505182585041
651736391240373101616780753145219889585978530135713014093293838712150019083926917777070013594570178137057101915545333916
002101213816415012727514638381363160859672227307374065359089249508355148884746295434971948371257819280224470345257914195
450825236435033676524090695574357018839095365525838548070206210089489232830822514161382130263818266591148051374480123034
373991108198819345888295857882675398328628005794395917823524481567118819757020399314516329965577672104436981215587914882
820720834074949629176778696760560291647252143168367452428770305205517085912598201248884620842571819942502596224120968573
568217094377596139694104078155241072138147282097551121437117967077078615556327652641426042327276195073469422235209189296
083600577235264578028851260384962868612136704443329510638021933468023999196516943682338700686693867288870451200199227380
034237384746866782836420934641624248505498762357736111080892593890176656335113302616092499222342676663646603083124449241
344112709192506320006173815620434505416769422829112085579859028438626538949993537318379214417554067879293452194409439479
351065591241710700318745194033708095529833202783729478484254432755316447081469837215258391552378628237388702281525041538
108951385803392956350097343420804864315331991848167955189953465557750589456849977889560729860017301899298306238554982878
781749582929963026901690200821110807822242161098491570039735028270288944262195992060695557273926879771384832465541488185
387736387278651953785681240112742680251373191699221867428473510800800314774756691695214467743890813197854689239758206994
794429865602514359508856456186475446450539529847788048602360009010939197467899285777311924637798999862870445559491131119
184128239520217144627582130940861258090896525055724073490213387309147729948336161695407330782040189688419239513819857650
885495989672625557384410387122874998247245767851160138311132192686706813156876490194844566497838984520449862602311406637
490063629844343945379401509722666209673794238691616326980225044002031098748742782233015614613111067422205660493067579390
335950913694936922294161629328006739827482061750016879480201467519781424347005673201609982445632670384546664298836877317
858791907400738083368075625227961127321741671017709102886027395235594387007005008383386536718406288829160181678292750593
996280395755843048828698944735790384193704725130314654520717415802050055437521789764252404001915054532695305332559273086
441959707853833618591495685880676365912002350575730368052891992004210824984758870682413436482901886746078448612917295739
099489457553396899421300576129154211648910621361076361111670073916561124961019685516368367505591358889722298812284611329
269889945890172728365996105701529619146228634343994300663596371111684927444378450833339463394492099755794813847549256677
549229964378472003195999043067003304991910159215288230669868588288565110990785794876035732152160675075712261259775779593
002108468558860168146377564552157677039857600275775440379581369619038548627997093397545742131363875358764134166123045532
953176280728758129849883454399454513622830599615842536359896043521524972015217111965165358102568172286046641027417421726
217984202732841822851678804528477750087259172999283467622427112208541647714807756467551096066370414467956230362026250440
667432580291499029591074301774729076810636357203487606160890804435770175162079467144295909151162809776171802617491892185
194393504004050077322479829630416245146727077520611493745815000810327098809058449458892286448154724257332117360338790161
441693520767079722815644411978591699645529004983575115432895394914212965583335351124002840973922344881972983225218124637
768534838549861717040150919736306404218616460050122346297642319534086917696898785500763991863175085751216200973752201840
584923643484340651722975351248347746278112730338415479119645287132849994759916185346205402084917795987208007648696938804
470686421555215197456689013908072390606667391313384771654918416220916115101135178530415224434387105643834780990516255161
044886498274377017300447401647967739954770727220789066090738694228571204292648541606669812309759145625172881342510557824
670011353002122234652371407179797855153205858293755476652199438723924868175753021020808921257959491470363679886381815669
547973574052905464767489143511093358631465926339408581937309089964824294639298109595723054625037673345588875044678454780
124907809968443820476146922528053615812457700378814694061154979858666355460860144017534814174011285257851173128641354076
643595868831675118881850790886965078027775201617852611381074789336644440596689985736062631134139221381493001558960163995
004505265501273935950615929255119129213981137137291868892561611317859322462407527843434259810404709466656448150887069602
010646568127751940826868994559981131355541153374612667552989891423055095780380965412964295427475158385943839004074907903
642208895034629443160920474357986556483423458863706746436664173493208821574871217084627582929851480709387450559300004386
979378125375013898484036285341564876279429444399041086568521399940902947224472499959441430637975393975736702224096999259
132604929506268591984101508773908433798468305859198640140269273924710628067762000523581609724961238686977625742179373964
874475371300644674083222175768577772946580002501417472217296561908991312896473986114012604946014183957188273818514028280
604104717172162581358449399153910614430283007210246859541991435079695187470326847021850905394287072347708081439591051367
125561152461723616133530854530756692166036330314916182761631596151050493598831556110839349193690881832244160802601226263
925990708139204156069879126348029068905742234100957247367004691561106485727500424450097961974581213042360902619745009088
347777888339887754412839357633865306759180314017384315435345983582689494451071453864954182039344957044867866009377532920
289155001775337483496140531803781200222660547306580453678123094663788326275490417871496263622331938157851217143661325161
322324406169601541546077854299637702601061232402542270106978428387009789316958772246357447416629068186385255161523326651
921131584540872321245615162347905934772000361618477673405245800018367245507272610467746261931712305183800199860949867016
539942105147819482635399928460628375581825482661052427879637073318872720404968735125798823834515765335612531136037126492
655373688067992580942168970097967622742108246650390898392138019130159617947362301724566595095436599771527704459498860641
016129011929281048381831185642641274139345869380740331663874799228626210723397524155876405189711857723517347394949590518
129579499322614451138302485924154078929506068990700963930144882293302707041836745306472407147262624103286461848549636559
82516347818791695313570448386685183438051851738808465894955354
"""
packed=int(''.join(DATA.split())).to_bytes(28976,'big')
assert pin(packed)==[28976, '7492f0abc7bb96fd4b93798f8f56f4feffe14a8d571dee7cd0db2effe5fa957d']
raw=lzma.decompress(packed)
assert pin(raw)==[75869, 'f8cfcf5839df12640a14c8d0150747bb41dba828dff266a4f07640686f3663f1']
sources=json.loads(raw)
SOURCE_PINS={'p2_star_family.py': [8527, 'c99b891f286ceb906512f9b6b34b5ff2d6bcc3aee26ac2f195d739833750c466'], 'k2_triangle_fill.py': [8286, '03f1077f787cff2fabb7ea1a8b452205edebf5a56745c9685eb1fd2191c159e2'], 'b4_triangle_star_recover.py': [15821, 'ba4da596c9920f3a7160cbb69fe272689397b817e830e7e1417db9cffe3e1534'], 'tp4_triangle_pair_frontier.py': [6368, '2af1a5e9b05920b78808e94770790a690550c3b77e5fafa3253ad8a7d1191b64'], 'tp4_any_edge_frontier.py': [1762, 'a37fc99789379d2fa4862ba7fbf5d25c03d16f97c2089c23cc92aa7125ce4e83'], 'm4_mass_sync.py': [7449, '39009811f97beb016390457cde4e50ed6a5e7337fb37672cca1e217610224fe7'], 'm4_e17_lambda_sync.py': [5017, '4a0de38977d4204a415200d8a17bbc98a4d06f934337ec7140740f1cc5e213f4'], 'v4_quad_compact.py': [7295, '16435e4bbca2034a1e52751b86f523fdc4b556acc002efc79de82267c1973696'], 'v4_tip_covariance.py': [6670, '0b983d483124b8da062018b9499a106f12cf787a474c0b7493d73d76148af577'], 'v4_filled_mass_caps.py': [4009, 'a29b8af5dbc9fe330d915b9d3c27d2efba9246f5b4d07148cdd5d75e1638e0ce'], 'm4_ridge_mass_rigidity.py': [3006, 'd7c59f0185b7dc2b8164eb5459ede143a853c24529660cce67b2240b82dc52fb']}
OUTPUT_PINS={'k2_triangle_fill.json': [72434, '67e801e6836f7d4bdecf98305973a8eb0603506eeb01a97084ab6adbedb42d98'], 'tp4_triangle_pair_frontier.json': [1865784, '7f7fd01f2436d2ee24681e7e5b1180eaed808fda167beda761d848b2a7d7fae5'], 'tp4_unrestricted_probe.json': [20009, '2f2e30351f6a4296272619451bda5adf8b7b168c21a5a1a435a08292ac13d4c9'], 'm4_mass_sync.json': [2695, '651bd927d69464e801f4a2b72d629a9e206cbd1149af3fb032c4aa2512f825b2'], 'm4_e17_lambda_sync.json': [1836, '28db0b98ff7d11197a5fa3eead1155485e530b74d3b18be1e70f26c5fe00e4fc'], 'v4_quad_compact.json': [73225, 'c236736481011101b8c1f800e8f348123624cf3deae8b3f16883ec4846f704ce'], 'v4_tip_covariance.json': [10689, '3506664e45183f0f3b1e122e73dceb2f6b3c8034c43612bda8a9d57d72c493ea'], 'v4_filled_mass_caps.json': [83399, '15d9d021a2e8e4873c8695aa791b61e39a853432e37ef9c090e58d4a1ceadfd1'], 'm4_ridge_mass_rigidity.json': [652, 'cb211a2c202b835addad1e29b0a5972cc6678f7dd694a681678f4f47ce4a8765'], 'b4/b4_final_certificate.json': [26161, 'a7a273b57ffa93de3e5d57a782766b83d273bf57aab6476a98683a830345b82b'], 'b4/b4_triangle_star_frontier.json': [5767, '932ebb7a8901893641c55cffb0b2037bdb4724653370d81df538cc7ce71c4874']}
dest=Path(sys.argv[1]if len(sys.argv)>1 else 'vivid63_v4_replay').resolve()
dest.mkdir(parents=True,exist_ok=True)
assert set(sources)==set(SOURCE_PINS)
for name,source in sources.items():
 data=source.encode();assert pin(data)==SOURCE_PINS[name]
 target=dest/name
 if target.exists():assert target.read_bytes()==data
 else:target.write_bytes(data)
logs=[]
commands=[['b4_triangle_star_recover.py','b4'],
 ['m4_mass_sync.py'],['m4_e17_lambda_sync.py'],['m4_ridge_mass_rigidity.py'],['v4_quad_compact.py'],
 ['v4_tip_covariance.py'],['v4_filled_mass_caps.py'],
 ['tp4_triangle_pair_frontier.py'],['tp4_any_edge_frontier.py']]
for command in commands:
 if command[0]=='tp4_any_edge_frontier.py':
  assert pin((dest/'tp4_triangle_pair_frontier.json').read_bytes())==OUTPUT_PINS['tp4_triangle_pair_frontier.json']
 p=subprocess.run([sys.executable,'-S',*command],cwd=dest,capture_output=True)
 assert p.returncode==0 and p.stderr==b'',(command,p.returncode,p.stderr.decode())
 logs.append(p.stdout);sys.stdout.buffer.write(p.stdout);sys.stdout.buffer.flush()
for name,expected in OUTPUT_PINS.items():assert pin((dest/name).read_bytes())==expected
front=json.loads((dest/'tp4_triangle_pair_frontier.json').read_bytes())
unrestricted=json.loads((dest/'tp4_unrestricted_probe.json').read_bytes())
assert {r['form']:len(r['records'])for r in unrestricted}=={266:90,272:114,278:66}
for r in unrestricted:
 expected=[x['branch']for x in front['forms'][str(r['form'])]['excluded']if x['reason']!='forced_two_separator']
 assert [x['branch']for x in r['records']]==expected
 assert all(x['answer']is None for x in r['records'])
end=b'TP4_ALL_336_UNRESTRICTED_NINE_FACET_PAIR_EXCLUSIONS_PASS\nVIVID63_COMPLETE_ACTUAL_LAMBDA_TRIANGLE_FRONTIER_V4_RECOVERY_PASS\n'
log=b''.join(logs)+end
(dest/'verification.log').write_bytes(log)
sys.stdout.buffer.write(end);sys.stdout.buffer.flush()
print('VERIFICATION_LOG',*pin(log))
```

I could not make a separately saved copy available through this turn's file-saving service. The complete inline recovery above is self-contained and requires no saved file from this workspace.
