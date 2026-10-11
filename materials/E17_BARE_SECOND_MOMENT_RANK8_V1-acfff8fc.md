# material-acfff8fcf552

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# E17_BARE_SECOND_MOMENT_RANK8_V1

## Accepted analytic determination and scope

For every actual full-dimensional convex 3-polytope P with genuine f-vector (V,E,F)=(10,17,9), translated to its own uniform-volume centroid, let q_i.x<=1 be its nine maximal supporting inequalities, c_i the actual uniform-area centroid of facet i, and T_i=E_Fi(xx^T) its actual second area moment. The matrix B with columns

B_i=(q_i,vec(q_i c_i^T),c_i,vec_sym T_i)

has rank at least8. Equivalently, dim ker B<=1. This includes the previously unresolved degree pattern(4,4,4,4,3,3,3,3,3,3). No equilibrium hypothesis, generic-position hypothesis, simplicial-facet hypothesis, or metric-condition-number restriction enters the proof.

Together with the actual one-vertex quadratic-flux theorem, one of the six scalar rows (q_i.r)(T_i)_ab, 1<=a<=b<=3, suffices to raise the rank to9 whenever B has rank8. Thus six single-row charts replace the previous possible fifteen two-row charts. There is no asserted uniform lower bound on a selected minor and no assertion that bare B always has rank9.

This is a mass-identification theorem, NOT an exclusion of homogeneous110 on E17. No full combinatorial type or root class is removed. The accepted universal minimum bound remains C>=34 and no exact minimum is claimed. The proof below is self-contained at the level of elementary convex-polytope geometry and the planar Brunn-Minkowski inequality; even the needed planar inequality and graph connectivity arguments are supplied. No computation, numerical certificate, code, or new coordinate control is used.

## 1. Exact physical identities

Write W=Vol(P), A_i=Area(F_i), h_i=1/||q_i|| and omega_i=A_i h_i/(3W). These are actual cone-volume fractions of conv(0,F_i), all positive. Actual cone decomposition, its first moments, and divergence give

sum omega_i=1,
sum omega_i c_i=0,
sum omega_i q_i=0,
sum omega_i q_i c_i^T=I/3.                                      (1)

The cone over a facet has centroid3c_i/4, which proves the second identity because P's volume centroid is0. The other two nontrivial identities are the divergence formulas for constant and coordinate vector fields. Since q_i.c_i=1, any nu in L=ker B satisfies sum nu_i=0 by taking the trace of its q_i c_i^T block. Consequently nu also annihilates all actual scalar facet moments through degree2, including the constant row.

For a genuine vertex v let Star(v) be its incident maximal facets and ell_v(i)=1-q_i.v. This is zero exactly on Star(v) and strictly positive elsewhere. For every nu in L,

sum ell_v(i)nu_i=0,
sum ell_v(i)nu_i c_i=0.                                      (2)

The second equality is sum nu_i c_i-(sum nu_i c_i q_i^T)v=0. It uses the same physical facet means and common flux block, not independently selected moment arrays.

## 2. Sparse independence of actual scalar facet moments

Let M_d have columns all actual means E_Fi x^alpha, |alpha|<=d, including1.

Lemma1: any at most2d+1 columns of M_d are linearly independent.

Proof: a nonzero dependence nu has both signs because its constant moment vanishes. Reverse its sign so that its negative support I has size<=d. The polynomial f(x)=product_{j in I}(1-q_j.x) has degree<=d, vanishes on every negative facet, and is strictly positive on the relative interior of every other maximal facet. Hence sum nu_i E_Fi f>0, a contradiction. Distinct maximal facets cannot contain one another's relative interiors; all positive area integrals are therefore strictly positive. This argument includes lower-rank geometric coincidences of unrelated vertices and arbitrary nonsimplicial facets.

In particular, any three columns(1,c_i) are independent, so any three facet centroids are noncollinear; and any five columns of M_2 are independent.

## 3. A facet cone has at most one quarter of the volume; equality is a pyramid

Lemma2: for any full-dimensional convex3-body with a planar facet F,

Area(F) dist(g(P),aff F)/(3Vol(P))<=1/4,

with equality exactly when P is a pyramid with base F.

Proof: measure height t inward from F. Let h be the maximum height, a(t) the parallel-section area, a0=a(0)>0, W=int_0^h a(t)dt, m=W^-1 int_0^h t a(t)dt. A pyramid over F with any point of maximum height as apex lies in P, so W>=a0 h/3. Put H=3W/a0>=h and compare with a_*(t)=a0(1-t/H)^2 on[0,H], extending a by0 after h. The two integrals are W.

Brunn concavity says f(t)=sqrt(a(t)/a0) is concave on[0,h]. Thus g(t)=f(t)-(1-t/H) is concave with g(0)=0, and g(t)/t is nonincreasing for t>0. Hence a-a_* has at most one change of sign, from positive to negative; a possible jump to0 at h has the same direction. Equal integrals exclude an everywhere nonzero single sign. At a crossing point b,

int_0^H t(a-a_*)dt=int_0^H(t-b)(a-a_*)dt<=0.

It follows that m<=H/4 and a0m/(3W)<=1/4. If equality holds, the last integrand is nonpositive and has zero integral, so a=a_* almost everywhere. Thus h=H. The contained pyramid over F then has volume a0h/3=W and equals P: a proper inclusion of two full-dimensional convex compact bodies has strictly smaller volume. Conversely, direct pyramid integration gives equality.

The required planar Brunn-Minkowski argument can be recalled explicitly. Normalize two planar convex bodies A,B to area1 and let a(x),b(y) be vertical-section lengths. The increasing transport T matching accumulated section areas satisfies T'=a/b(T) almost everywhere in their positive interior projection intervals. A section of (1-lambda)A+lambda B at (1-lambda)x+lambda T(x) contains the sum of the two section intervals. Thus its area is at least

int[(1-lambda)a+lambda b(T)][(1-lambda)+lambda a/b(T)]dx>=int a dx=1,

using b+a^2/b>=2a. Rescaling A and B and replacing lambda gives the ordinary square-root area inequality for arbitrary positive areas. Endpoint limits do not affect integrals. Convexity of P includes the Minkowski combination of any two parallel sections in the corresponding intermediate section, giving the stated concavity of sqrt(a(t)). No equality classification of Brunn-Minkowski was needed.

## 4. Eight coplanar facet centroids would force a pyramid

Lemma3: if all but at most one of the actual facet centroids of a homogeneous3-polytope lie in a plane, it is a pyramid with that exceptional facet as base. All facet centroids cannot be coplanar.

Proof: let the plane be a.x=b with a!=0 and d_i=a.c_i-b. Equations(1) give

sum omega_i d_i=-b,
sum omega_i d_i q_i=a/3.                                    (3)

If all d_i vanish, the second equality contradicts a!=0. If only d_j can be nonzero, then omega_jd_j=-b and omega_jd_jq_j=a/3. Therefore b!=0, a=-3bq_j, and d_j=-4b since q_j.c_j=1. Hence omega_j=1/4 and Lemma2 proves the claim.

An E17 body is not a pyramid: a pyramid with9facets has an octagonal base and9vertices, not10. Therefore no plane contains eight of the nine E17 facet centroids.

## 5. General kernel bounds and degrees5/6

In a convex3-polytope the number of maximal facets incident to a vertex is its true-edge degree; two adjacent vertices share exactly the two facets containing their edge. The graph has minimum degree3 and

sum_v(deg(v)-3)=2E-3V=4.                                    (4)

Some degree is between4and7 and none exceeds7.

At a degree4 vertex v, multiplication nu->ell_v nu is injective on L: its kernel would be supported on the four facets of Star(v) and would annihilate M_2, contradicting Lemma1. By(2) its image lies in the affine moment kernel M_1 on the other five facets. This kernel has dimension<=2. Thus dim L<=2, and if dim L=2 those five centroids lie in a unique plane: their M_1 rank is exactly3 and every three columns are independent.

At a degree5 vertex the same operator is injective by M_2 independence on five facets; its image lies in an affine moment kernel on four facets, of dimension<=1. Thus dim L<=1.

At a degree6 vertex v, equation(2) and M_1 independence on the three outside facets show supp nu subset Star(v). Choose a true neighbour w. Multiplication by ell_w is injective on L because its kernel is supported on the two facets of edge vw. Its image is in the M_1 kernel on the four facets Star(v) minus Star(w), of dimension<=1. Again dim L<=1.

## 6. The degree7 case

Suppose deg(v)=7. Equation(4) makes every other vertex trivalent. There are exactly two facets A,D outside Star(v). Equation(2) first gives supp nu subset Star(v). If dim L>=2, for each neighbour w the same injective multiplier ell_w maps into the M_1 kernel on the five facets Star(v) minus Star(w). Consequently dim L=2 and all these five-centroid sets are coplanar.

The seven facets around v have a cyclic order; the two containing edge vw form a consecutive pair. Any two complements of consecutive pairs have at least three common centroids, which are noncollinear by Lemma1. Their planes thus coincide, and together they contain all seven incident facet centroids.

This is geometrically impossible. Translate v to0 just for this coplanarity argument. Its seven incident supporting planes bound its pointed tangent cone. The two other halfspaces can be written a.x<=1 and d.x<=1. Both actually give facets of P. On a polygonal transverse section of the cone, the line(a-d).x=0 separates nonempty regions where the two cuts are first. It crosses exactly two edges, not a vertex: a vertex crossing would create another vertex of P incident to the two side facets and both cuts, of degree>=4, contrary to(4). Thus exactly two side facets are mixed quadrilaterals, while the other five are triangles cut wholly by A or wholly by D. At least three triangles use one common cut, say A. Their centroids lie in a.x=2/3 and are noncollinear by Lemma1.

A mixed side-facet centroid lies strictly below a.x=2/3. Triangulate that quadrilateral from v. The two other vertices of each triangle have a.x<=1; at least one triangle has a vertex strictly below the A plane. Its centroid has a.x<2/3 and the others have a.x<=2/3. Positive area averaging proves the strict inequality. Therefore the seven incident centroids cannot all lie in the plane determined by the three pure-A triangle centroids. Contradiction. Hence dim L<=1 also at degree7.

## 7. The four degree4 vertices cannot be independent

Lemma4: in the genuine E17 graph with degree pattern(4,4,4,4,3,3,3,3,3,3), two degree4 vertices are adjacent.

Proof: suppose the four degree4 vertices form an independent set X and let Y be the other six. All16edges incident to X join Y. The total degree of Y is18, so exactly one edge uv is internal to Y. Every triangle must contain uv.

Euler gives F=9, and the sum of face boundary lengths is34. If t faces are triangular, 34>=3t+4(9-t)=36-t, so t>=2. Only the two faces incident to uv can be triangles, so t=2. Those two triangles are uva and uvb with distinct a,b in X. Since u,v have degree3, their neighbours are each other and a,b. Removing a,b disconnects the pair u,v from the other six vertices, contradicting 3-connectivity of a convex3-polytope graph.

For completeness, the needed connectivity statement has the standard Balinski argument. Remove a set S of at most two vertices and choose a third vertex w. There is a nonzero affine functional f vanishing on S union{w}, but not on the whole full-dimensional polytope. Any nonmaximal vertex has a true edge strictly increasing f, because its edge directions generate its tangent cone; otherwise it would be a global maximum. Such paths connect every vertex with f>=0 to the maximum face without touching S after their first step. Decreasing paths similarly connect f<=0 vertices to the minimum face. If both signs occur, w joins the two parts; if only one sign occurs, the corresponding paths suffice. Graphs of faces are connected. Thus removing S cannot disconnect the graph.

## 8. Closing the last possible rank7 case

The only degree pattern not settled by Sections5/6 is four degree4 and six degree3 vertices. Suppose dim L=2. Choose adjacent degree4 vertices v,w by Lemma4. The five facet centroids outside Star(v), and the five outside Star(w), each determine a plane by Section5. The stars share exactly two facets, so the two five-element complements have three common facets and seven in their union. Their three common centroids are noncollinear, hence their planes coincide. Let S be these seven facets and let a.x=b be the common centroid plane.

By Lemma3 and the fact that E17 is not a pyramid, the other two facet centroids, say of A,D, BOTH lie outside this plane. For any nu in L put d_i=a.c_i-b. From the B equations,

sum nu_i d_i=0,
sum nu_i d_i q_i=0.                                        (5)

Only A,D contribute. The two columns(1,q_A),(1,q_D) are independent because distinct maximal facets have distinct normalized poles. Since d_A,d_D are nonzero, (5) forces nu_A=nu_D=0. Thus all of the hypothesized two-dimensional L is supported on S.

Two distinct facets of a convex3-polytope share at most two true vertices: their intersection is a face of dimension at most1, and points in the interior of an edge are not vertices of P. Among the four degree4 vertices choose r not incident to BOTH A,D. At least three of its four incident facets belong to S. Therefore ell_r nu is supported on S minus Star(r), at most four facets, and annihilates M_1 by(2).

The multiplier ell_r is injective on L: a vector in its kernel would be supported on at most four facets of Star(r) and annihilate M_2, impossible by Lemma1. But M_1 on at most four actual facets has kernel dimension at most1 because any three columns are independent. A two-dimensional L cannot inject into this kernel. Contradiction.

We have proved rank B>=8 on every actual E17 realization.

## 9. Complete single-scalar quadratic-flux consequence

For a genuine vertex r append the six rows D_r(i)=(q_i.r)vec_sym T_i. The actual weights satisfy sum omega_i D_r(i)=0 by applying divergence to r x_a x_b and using the actual zero volume first moment.

Here is the full rank9 argument, reproduced to avoid relying on a capsule summary. Choose any degree4-7 vertex v. If deg(v)=4or5 set r=v. For nu annihilating[B;D_r], in addition to(2) one has sum ell_v(i)nu_i T_i=0. The localized vector annihilates M_2 and is supported outside Star(v) on at most five facets; it is zero by Lemma1. The remaining nu is supported on at most five incident facets, so nu=0 as well.

If deg(v)=6or7 set r to any actual neighbour of v. First (2) localizes nu to Star(v), since its outside complement has at most three facets. Then the quadratic localized vector ell_r nu has support Star(v) minus Star(r), of size deg(v)-2<=5, and vanishes by M_2 independence. What remains is supported on the two edge facets and also vanishes. Thus[B;D_r] has rank9 in every case.

Since rank B>=8, when its rank is8 its kernel is a single line. At least one of the six scalar components of D_r is nonzero on that line, and that one component alone raises the rank to9. When rank B is9 nothing needs to be added. Consequently six single-row choices cover all geometries; this is an exact qualitative cover, not a uniform numerical margin.

For actual mass reconstruction the right-hand sides of B are fixed by(1) and sum omega_i T_i=5 Sigma/3, where Sigma is the actual body covariance; the additional scalar flux has zero right-hand side. Subtracting any candidate solution from the actual weights and using rank9 proves uniqueness even among arbitrary real candidate weights. One may not replace the actual Sigma, c_i or T_i by independent fitted PSD arrays and claim the same conclusion.

## 10. Evidence provenance, novelty boundary, and next mathematical obligation

Fully read immutable predecessor: minimum-0075, SHA25617b392631f5a612ddcf377f1d2c5f478d5abcdf45652178d512fdf449e09de43. It establishes actual quadratic flux, sparse moment independence and the six-row rank9 augmentation; none of its proposed or certified coordinate controls is a premise here.

The complete analytic journal entries E17_TWO_SCALAR_FLUX_COMPLETION_V1 and E17_DEGREE7_RANK8_V1 were recovered through the targeted cursor range4368500-4382500; their entry timestamps are16September2026,17:54:07.125 and17:59:30.904. Sections5/6 rederive their degree reductions. The new synthesis is the facet-weight equality/coplanarity argument plus the small graph obstruction, closing Section8 without enumeration.

The classical Brunn-Minkowski and Balinski theorems are not claimed as new. Primary reference for the latter, whose statement was checked on arXiv: G.Pineda-Villavicencio, A new proof of Balinski's theorem on the connectivity of polytopes, arXiv:2009.04658v2, revised30March2021; original M.L.Balinski1961. Standard Brunn-Minkowski reference: R.J.Gardner, The Brunn-Minkowski inequality, Bull.Amer.Math.Soc.39(2002),355-405, DOI10.1090/S0273-0979-02-00941-2. The required restricted proofs are included above, so inaccessible publisher text is not used as an unstated premise.

The next substantive problem is to combine the now at-most-one-dimensional false-weight freedom with actual reciprocal-metric escape inequalities and common facet geometry. Rank alone does not force an extra equilibrium: actual weights always solve the balances. Neither C>=36 nor impossibility of rank8 is inferred. This exact analytic source is the canonical recovery of the new theorem; a longer Russian exposition is only supplementary and no external sandbox is needed to reconstruct this proof.
