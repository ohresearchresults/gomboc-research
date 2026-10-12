# minimum-0215

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# POSITIVE_PROJECTIVE_TWO_CAP_AXIAL_ORBIT_AND_FINITE_HORIZONS_V1

## 1. Main conclusions

**The entire axial positive-projective orbit is all-root U1-empty.** For every real

`0<epsilon<=5,  -1<t<infinity`,

the actual uniformly refilled body

`T_t(P_epsilon),  T_t(Y)=Y/(1+t Y_z)`,

centred at its **NEW actual solid volume centroid**, has **at least TWO strict unstable vertices for EVERY SPD physical metric**. This includes arbitrary conditioning, all ten roots, every finite weak-arrow wall and radius tie, and both projective tails. It is a new two-parameter actual-shape theorem, not another metric pencil on an unchanged body.

The exact certificate uses **2,023 integer stresses, 9,532 nonzero weights, seven closed parameter strips, 4,672 stress/strip applications, 1,569,792 positive-definite tensor-Bernstein matrices and 4,709,376 positive leading minors**. Every strip covers the entire epsilon interval. All43,200 rooted true spanning trees are covered in each strip.

**A separate analytical result controls the finite boundary of the full three-parameter projective domain.** All finite horizon strata exposing a nonapical vertex, a true edge, or the quadrilateral cap have an all-root/all-SPD U2 collar. The only finite boundary point not covered by this theorem is

`c_H=(2/7,0,-1)`,

which exposes the heptagonal cap. The proof handles arbitrary relative rates of vanishing actual denominators and retains collapsed/nonextreme labels in the limiting weak-tree problem.

There is also an explicit full-dimensional projective band:

`|c_x|<=2^-147,  |c_y|<=2^-147(1+c_z),  c_z>-1`,

on which every member, for every0<epsilon<=5, has U>=2 under every SPD. Its small transverse width is a supplementary robustness consequence; the main advances are the complete unbounded axial family and the general finite-horizon mechanism.

An exact actual **525,weak000** control at epsilon5 and c=(0,0,6) makes all three true arrows **6->8,7->0,8->5 strictly positive**, although their positive weighted combination was forbidden throughout the original family under every metric. Thus the original stresses cannot simply be transported projectively. Five additional exact controls attain **222,weak000**, including two with apex0 not unstable.

**The full three-parameter positive-projective interior remains unresolved outside the proved band. No U1 or110 construction, whole combinatorial-type exclusion, canonical count subtraction or bound change is claimed.** The accepted global interval remains34<=C_min<=622. The parent’s all-root theorem covered the original family and affine images, not these projective refills. :contentReference[oaicite:0]{index=0}

## 2. Source authority and evidence

The authoritative parent is `minimum-0212`, SHA-256 `379283a8bce355e851ffb8f006473eea2eb45aa7d50e46c5f0c071a3ddb31285`. Its literal geometry is unchanged.

The complete updated `research-journal(20260923-223040).md`, including the full immutable parent payload and recovery capsule, was read through EOF. Its actual mounted bytes are275321, SHA-256 `c4c960f936655bbcbb79e634eaf9459cf7bd59f974040f969e6fe16f5f2ee8ae`. The complete decoded parent source was also read. No mathematical conflict or missing exact dependency was encountered.

The new certificate was author-executed and rebuilt and checked from the embedded source alone. The finite-horizon theorem is analytical; its proof is given below and is not inferred from sampled controls. No old theorem is claimed to have received a new independent replay.

## 3. Literal family, full positive-projective chart and true incidence

### Original geometry

Use raw apex Y0=(0,0,0), and section z=1. Put

```
L=(-1/4,5/4), T=(7/2,13/4), R=(1/40,27/4).
```

For t in the ordered list(2/5,1/4,3/25,0), define

`b(t)=(L+t(R-L)-epsilon*t*(1-t)*(1,0),1)`.

These are b1,b2,b3,b4. With s=3/50, let

```
b5=(L+s(T-L)-epsilon*s*(1-s)*(0,1),1),
b6=(T,1), b7=(R,1).
```

Intersect their pointed cone with the two true caps

```
l7(Y)=z-(2/7)x<=1,
l8(Y)=z+(5/7)x<=1.
```

For i=1,...,5, Yi=bi/[1-(2/7)bix]; for i=6,7, Yi=bi/[1+(5/7)bix]. Vertices Y8,Y9 are the x=0 intersections of[b5,b6] and[b7,b1]. On an ordered segment[a,b], the exact formula is

`a-a_x*(b-a)/(b_x-a_x)`.

The true outward maximal facets are

```
F0=(0,2,1)       F1=(0,3,2)       F2=(0,4,3)
F3=(0,5,4)       F4=(0,6,8,5)     F5=(0,7,6)
F6=(0,1,9,7)     F7=(1,2,3,4,5,8,9)
F8=(6,7,9,8).
```

The seventeen true edges, in the exact order used below, are

```
01,02,03,04,05,06,07,12,19,23,34,45,58,67,68,79,89.
```

The degree sequence is7 followed by nine3s. F7 is heptagonal and F8 quadrilateral. **08 and09 are not mechanical edges; triangle089 is an internal interface, not a maximal facet.** These are the parent’s actual labels and facets. :contentReference[oaicite:1]{index=1}

### Complete positive-projective moment chart

For any c with every actual denominator

`d_i(c)=1+c.Y_i>0`,

put Z_i=Y_i/d_i. If a raw facet is n_f.Y<=h_f, its transformed support is

`(n_f+h_f*c).Z<=h_f`.

Indeed its slack at a transformed vertex is the old slack divided by d_i. Thus positivity preserves the **entire maximal-facet/true-edge lattice**, not merely the f-vector.

The seven positive apex-fan tetrahedra have base triangles

```
(1,2,3),(1,3,4),(1,4,5),(1,5,8),(1,8,9),
(6,7,9),(6,9,8).
```

For a triangle(i,j,k), its new six-volume is

`det(Y_i,Y_j,Y_k)/(d_i*d_j*d_k)`.

Writing this weight as w_ijk gives the **actual uniformly refilled** moments

```
D_c=sum w_ijk=6Vol(T_c(P)),
g_c=sum w_ijk*(Z_i+Z_j+Z_k)/(4D_c).
```

For each full cap, D_s and J_s denote its corresponding sums. Its real area centroid is J_s/(3D_s), and its real cone-volume fraction is D_s/D_c. Hence, after the ONE actual translation,

`X0+3 sum_s (D_s/D_c)*(J_s/(3D_s)-g_c)=0`.

The same-origin poles are exactly

`q_f(c)=(n_f+h_f*c)/[h_f-(n_f+h_f*c).g_c]`.

Every physical statement uses one SPD M and **N=M^-1** on these poles. Neither an old centroid nor a separately centred polar body is substituted. The parent’s cap-moment identity is the starting actual-mass convention. :contentReference[oaicite:2]{index=2}

The new source includes `projective_body(epsilon,c)` for arbitrary rational positive c and a full exact facet/edge/reciprocal auditor. Its weak output is a list of physical edge packets; future nonempty VF packets would require point deduplication before reporting weak-point counts. All six controls here have no zero primitive and no weak packet, so their weak000 classifications are complete.

## 4. Compactification of the entire axial orbit

For c=(0,0,t), the exact positive domain is **t>-1**: all original vertices have0<=Y_z<=1 and the two seam vertices have Y_z=1.

Use

```
u=1/(t+2),  0<u<1,
A_u=diag(1/u,(1-u)/u,(1-u)/u),
Q_(epsilon,u)=A_u T_t(P_epsilon).
```

Affine normalization preserves uniform filling and transports the already recomputed new centroid by A_u. For a ray b_i, put a_i=-2/7 for i1,...,5 and a_i=5/7 for i6,7. The normalized vertices are

`W_i=(b_ix,(1-u)b_iy,1-u)/(1-u+a_i*u*b_ix)`.

The apex remains0, and both seam vertices remain their original(0,y,1). These formulas are rational in epsilon,u and retain exactly the displayed true lattice throughout the physical domain.

At u=0 the limit is a heptagonal pyramid with additional nonextreme seam labels. At u=1, rays1,...,5 collapse to(-7/2,0,0), rays6,7 collapse to(7/5,0,0), and the two seam endpoints remain: the limit is a tetrahedron. These are **algebraic proof limits, not E17 members**. Likewise epsilon=0 is only a merged limiting geometry. The physical endpoint epsilon5 is included.

The source proves all35 nonincident section-polygon determinants over0<epsilon<=5. The first five section x-coordinates are negative and the other two positive, so the seam crosses exactly the stated two genuine section edges. The cone construction and positive-projective slack identity prove the full true lattice throughout.

## 5. Exact all-root certificate on the complete two-parameter family

### Polynomial stress construction

Recompute the actual cap-fan moments of W and set X_i=W_i-g. A common polynomial denominator d(epsilon,u) makes Z_i=d X_i integer polynomial vectors. Its degree is(9,13). The source verifies its nine factors are nonvanishing on the complete closed proof rectangle.

For every directed true edge define

`A_ij=sym(X_i*(X_j-X_i)^T),  D_ij(M)=tr(M A_ij)`.

The34 directed edges are indexed from the seventeen lexicographic undirected edges above: index2k is i->j for i<j, and2k+1 is its reverse.

The raw integer polynomial tensors

`Z_i*(Z_j-Z_i)^T+(Z_j-Z_i)*Z_i^T`

share an exact common factor f of degree(5,6). Its42 tensor-Bernstein coefficients on the complete rectangle are strictly positive. Division gives degree at most(15,20) tensors L_ij, with the exact identity

`f L_ij=2d^2 A_ij`.

For a nonnegative integer row w, the certificate is

`Q_w=-sum_ij w_ij L_ij`.

The entire2,023-row table and all strip assignments are literal in the embedded source. There are9,532 nonzero weights, all<=1000. Support sizes are

```
3 arrows:252 rows; 4:636; 5:686; 6:351; 7:88; 8:10.
```

### Closed coverage

Each row/strip application is verified by all336 tensor-Bernstein matrices:16 in epsilon/5 and21 in the local u parameter. The seven strips are

|Code|Closed u interval|Applications|
|---|---|---:|
|0|[0,1/2]|552|
|10|[1/2,3/4]|631|
|110|[3/4,7/8]|772|
|1110|[7/8,15/16]|760|
|11110|[15/16,31/32]|744|
|111110|[31/32,63/64]|632|
|111111|[63/64,1]|581|

**Every strip covers epsilon in[0,5].** The prefix-free codes have exact Kraft sum1, so the strips cover the entire closed parameter square, including every common boundary. There is no sampled feasibility pruning.

All **1,569,792** coefficient matrices are positive definite. The code checks **4,709,376** strictly positive leading minors, a second fraction-free determinant identity, exact common-factor multiplication and inverse Bernstein-to-power reconstruction in **both variables**. Thus every applied Q_w is positive definite on its complete strip.

### Why this excludes every possible root

For SPD M, a weak true arrow implies

`n_j-n_i=2D_ij+||X_j-X_i||_M^2>0`.

If there were one strict unstable vertex r, every other vertex would have a nonnegative true outgoing edge. Choosing one at each nonroot produces an acyclic rooted true spanning tree toward r, even if some chosen arrows are zero or other physical weak contacts exist.

Exact enumeration gives4,320 true spanning trees, independently matched by a Matrix-Tree determinant, and4,320 orientations toward **each** of the ten roots. In every strip, every one of these43,200 rooted trees contains the support of at least one applied row. The source checks directed-edge containment, not undirected containment or a triangulation supergraph.

For such a weak tree,

`f tr(M Q_w)=-2d^2 sum w_ij D_ij<=0`,

whereas f>0 and M,Q_w are positive definite. This contradiction excludes every root. A global norm maximum is always strict U, so the result is U>=2, not merely an assertion that some selected root is unavailable.

These are raw tree counts for this labelled graph, **not canonical registry counts**.

### Uniform margin, including singular arrow systems

For a positive-definite3x3 matrix B,

`lambda_min(B)>=4det(B)/(tr B)^2`.

The source retains every tensor scale and the full actual-centroid denominator. On every application it verifies a lower bound for the normalized negative weighted arrow tensor exceeding

`mu=2^-128`.

Consequently, for every nonzero PSD M and every rooted true tree, some arrow has

`D_ij(M)<=-mu tr(M)`.

For singular M this is a statement about an arrow cone, **not a physical equilibrium census**. The physical all-SPD theorem includes all finite weak-arrow walls without excluding them by assumption.

Sixteen additional positive-definite coefficient matrices, not included in the primary counts above, certify the old row2D68+2D70+100D85<0 for **all original epsilon** at u=1/2. They support the actual projective countercontrol in section8.

## 6. A full-dimensional unbounded projective band

The compact raw vertices satisfy

`|W_x|<=7/2,  0<=W_y<=27/4,  0<=W_z<=1`,

so ||W||<8. The actual centroid therefore has norm<8, while centred vertices and true edge differences have norms<16.

Any actual own-centred same-labelled-graph body whose centred vertices differ by at most

`r=mu/128=2^-135`

from some physical Q_(epsilon,u) also has U>=2 for every SPD. Indeed the change of any arrow is bounded by

`(48r+2r^2)tr(M)<(mu/2)tr(M)`.

The negative weighted rows and their complete tree coverage survive.

Now write an unrestricted projective parameter in the form

`c=(a,bh,h-1),  h>0,  u=1/(1+h)`.

Projective composition and the same affine normalization give the exact identity

`A_u T_c(P_epsilon)=T_p(Q_(epsilon,u)),  p=(ua,b,0)`.

For any bounded raw body with ||W||<=8 and8||p||<1/2, the actual refilled centroid obeys

`D_p g_p=-5Sigma_p-g_p g_p^T`.

Since every intermediate projective image has radius<=16,

`0<=5Sigma_p+g_p g_p^T<=5E[WW^T]<=1280 I`.

A vertex derivative has norm at most256||p||. Thus the **centred** vertex displacement is at most1536||p||. This explicitly includes the actual uniform-refill centroid shift.

Taking

`|a|,|b|<=mu/2^19=2^-147`

gives ||p||<=2*2^-147 and centred displacement<r. It also guarantees every actual denominator is positive. Therefore

**`|c_x|<=2^-147, |c_y|<=2^-147(1+c_z), c_z>-1` implies U>=2 for every SPD, for all0<epsilon<=5.**

No independent reference displacement or mass replacement is used. This band includes unbounded c_z and approaches the axial finite horizon; it is not a bounded metric neighborhood.

## 7. A geometry-wide finite-horizon obstruction

### 7.1 Low-complexity PSD/refinement lemma

Let K be an actual uniformly filled full-dimensional convex3-polytope with at most **five true vertices**, at its own volume centroid. For any nonzero PSD M, set p_i=M^(1/2)x_i. Consider the **complete** weak-arrow graph on these projected vertices, with arrow i->j when

`p_i.(p_j-p_i)>=0`.

Every strongly connected component consists of coincident projected points: summing norm increases around a directed cycle gives a sum of squared displacements equal to0.

Suppose there were a unique sink component. Choose a weak rooted tree toward one of its vertices r. The sink point is nonzero, because0 has outgoing zero arrows to every projected point, and full-dimensionality with nonzero M prevents every point being0. Normalize ||p_r||=1.

A vertex reaching r in d weak steps has

`p_i.p_r>=-b_d`,

where

```
b1=0, b2=1/8, b3=1/4,
b4=(11+5sqrt(5))/64<3/8.
```

For completeness, a weak arrow gives ||p_i||<=||p_j||cos(theta_ij), with theta_ij in[0,pi/2]. If phi is the endpoint angle, the spherical triangle inequality and concavity of log cos give the bound by cos(phi)cos^d(phi/d) on the relevant negative-projection range. Its minimum is

`-cos^(d+1)(pi/(d+1))`.

Coincident steps and zero intermediate points cause no difficulty; they only weaken the estimate.

An actual positive tetrahedral fan from r gives

`-p_r=sum_(i!=r) theta_i p_i`,

with0<=theta_i<=1 and sum theta_i=3. These theta_i are **true fan-volume inclusion fractions**. The sorted depths of at most four nonroot vertices satisfy d_j<=j. Taking the root projection would therefore give

`0=1+sum theta_i p_i.p_r >=1-(b1+b2+b3+b4)>1/4`,

a contradiction. Hence there are at least two distinct sink projected points.

This conclusion survives **arbitrary finite refinement labels contained in K**, as long as all its true vertices are included. At a sink projected point p, the arrow to every different projected core vertex is strictly negative. Convexity makes the arrow to every point of K with a different projection strictly negative as well. The labels in that projected fibre form a closed weak-arrow set. Two such disjoint sets cannot both drain to one root, regardless of the selected label graph.

**Limit consequence.** Suppose a continuous actual uniformly filled family admits invertible affine normalizations whose labelled vertices stay bounded and tend to a full-dimensional limit with at most five true vertices. Then all sufficiently nearby members have U>=2 for every SPD. Otherwise choose one recurring true rooted tree from a U1 sequence, normalize the transported metrics to trace1, and pass to a nonzero PSD limit. Actual uniform centroids converge with the bounded full-dimensional convex bodies. The limiting labelled tree is weak and contradicts the refinement lemma.

This handles arbitrary conditioning, collapsed edges and nonextreme limiting labels. It does not infer a physical singular-metric U count by dropping those labels.

### 7.2 Three complete horizon normalizations

Let P be a fixed full-dimensional convex3-polytope with0 in P, and let c* be a **finite** boundary point of its positive-projectivity domain. Put n=-c*. Its exposed true face F has n.Y=1, while every other vertex has n.Y<1. For c approaching c* from the positive domain put h_i=1+c.Y_i>0. All bodies below are uniformly filled and subsequently centred at their own actual centroid.

**Vertex horizon.** Suppose F={v} and degree(v)<=4. Set

`A_c=I+(h_v-1)v n^T`.

Its determinant is h_v>0 and A_c T_c(v)=v. Every other vertex tends to

`[Y_i-v(n.Y_i)]/[1-n.Y_i]`,

in the plane n.X=0. Their hull is the section of the genuine tangent cone at v, whose extreme points come from the genuine edges incident to v. The limit is a bounded full-dimensional pyramid with degree(v)+1<=5 true vertices. The PSD/refinement lemma supplies an all-root/all-metric collar.

**Edge horizon.** Suppose F=[v,w] is a true edge. The vectors v,w are independent because n.v=n.w=1. Complete them by k to B=[v w k], and set

`A_c=B diag(h_v,h_w,1) B^-1`.

The endpoints stay v,w. Write Y_i=alpha_i v+beta_i w+gamma_i k. Every other vertex tends to

`gamma_i k/[1-n.Y_i]`.

The scalar interval[a,b] formed by these limits is nondegenerate. If every scalar were equal, all original vertices, including v,w, would lie in one affine plane. The limit is therefore the full-dimensional tetrahedron conv(v,w,a k,b k). **No bound on h_v/h_w is imposed.**

**Triangular or quadrilateral facet horizon.** On the transformed facet choose an actual vertex triangle of maximal area. Along a subsequence its original labels i1,i2,i3 are fixed. With B=[Y_i1 Y_i2 Y_i3], set

`A_c=diag(h_i1,h_i2,h_i3) B^-1`.

Those image vertices become e1,e2,e3. Each remaining facet vertex has barycentric coordinates summing to1, each of absolute value<=1 by maximal-area choice. Thus it stays bounded. Every off-facet vertex tends to0 because A_c tends to0 while its denominator has a positive limit. The limit contains0,e1,e2,e3 and at most one additional point, so it is full-dimensional with at most five true vertices. All denominator-rate hierarchies and maximal-triangle ties are included.

In all three cases, the actual uniform centroids converge. This follows either from the actual tetrahedral moment formulas or bounded full-dimensional convex convergence. **The separately centred equilibrium mechanics of component pyramids are never glued.** The limiting own-centred whole body is what enters the lemma.

### 7.3 Disposition of the full finite boundary for this family

For every fixed0<epsilon<=5, the finite projective boundary has strata exposing

- nine nonapical vertices, all simple;
- ten true edges not incident to apex0;
- the two true caps.

The vertex and edge strata are covered by the preceding theorem. The quadrilateral-cap point

`c_Q=(-5/7,0,-1)`

is covered as well. **Only the heptagonal-cap point c_H=(2/7,0,-1) remains outside this finite-horizon theorem.** These20 covered strata out of21 are strata of the projective parameter polyhedron, not canonical polytope or rooted-orbit counts.

A uniform compact consequence is useful. For any epsilon0>0, R<infinity and eta>0, potential U1 parameters satisfying

`epsilon in[epsilon0,5], ||c||<=R, ||c-c_H||>=eta`

have all actual denominators bounded below by some positive delta(epsilon0,R,eta). Otherwise a convergent sequence would reach one of the excluded finite horizons. No effective numerical value of this general delta is claimed.

The limitation is substantive: at the heptagonal-cap horizon the same normalization can leave a pyramid with up to eight true vertices. The five-vertex PSD/refinement argument does not cover that case. An ordinary SPD U2 statement for a limiting body alone would not justify a uniform collar when the metrics approach singularity. Unbounded c, epsilon->0 and the unclassified positive interior are also separate from this finite-horizon theorem.

## 8. Exact actual countercontrols and sharpness

### A real opening of an old forbidden forest

Take epsilon5 and t6, hence u1/8 and A_u=diag(8,7,7). On the normalized actual body use

```
M=(1/1000)*((3,-2,24),
            (-2,12,-103),
            (24,-103,921)),
N=M^-1.
```

Its leading minors are3/1000,32/10^6,621/10^9, all positive. Its actual normalized volume and centroid are

```
V=70588892109971564/16423304836041675,
g=(38697662061787758974534525033/113240819844739440580450946904,
   10685504856865223606830836522622693/4121965842348515637128414467305600,
   318206215096439795990878919975/452963279378957762321803787616).
```

Before the affine normalization, the projective volume is

`2521031861070413/229926267704583450`,

and its true centroid is A_u^-1 g. The original projective denominators are

```
(1,646/121,4099/739,1683/283,33/5,327/47,19/7,131/19,7,7).
```

The source proves **D68,D70,D85>1/20000**. Yet on every original P_epsilon, the old row

`2D68+2D70+100D85<0`

holds for every SPD, now independently verified by the sixteen extra coefficient matrices at u1/2. This new body is therefore not a **labelled affine copy** of any member of the original family. No unlabelled affine-isomorphism classification is claimed.

The complete actual reciprocal census is

```
S={F0,F4,F5,F6,F7},
U={0,5},
H={01,02,06,19,67},
physical weak000; all68 true-edge primitives nonzero.
```

Thus opening the old local forest does not produce a global U1 witness: another true vertex remains unstable. This is a genuine geometric failure of direct stress transport, not an independently feasible primal/dual pair or a formal Gram control.

### Five rational Euclidean U2 controls

For the following five actual shapes use the SAME integer physical map

```
C=((16384,32768,-16384),
   (896,-512,-128),
   (-1,-1,-3)),
M=C^T C, N=M^-1.
```

Its determinant is66*128^3>0. The physical rational Euclidean vertices are C(W_i-g), with actual centroid0 and actual volume det(C)*Vol(Q). Every input and every moment is regenerated exactly.

|epsilon|u|t|Strict stable facets|Strict unstable vertices|True saddle edges|
|---:|---:|---:|---|---|---|
|1/10|1/64|62|5,8|0,7|06,12|
|1|1/4|2|5,8|0,7|06,12|
|2|3/4|-2/3|6,8|0,9|19,67|
|4|63/64|-62/63|6,7|2,9|19,67|
|5|1023/1024|-1022/1023|6,7|2,9|19,79|

All five are **222,weak000**. The last two have apex0 not U. Together with the525 control, all **408** true-edge primitives are nonzero.

Every census uses exact maximal supporting facets, actual volume centring, two agreeing volume/second-moment fans, the actual same-origin polar hull and the reciprocal metric. No continuous weak-free path between these six controls is asserted.

## 9. Remaining problem and useful continuation

The full axial projective orbit and its stated transverse band are settled at U>=2 for all roots and all metrics. The general finite-horizon theorem further prevents a bounded-parameter U1 sequence from approaching any finite boundary other than the heptagonal-cap point, when epsilon stays bounded away from0.

The unresolved full-orbit regions are the positive interior outside the band, neighborhoods of c_H, general unbounded c directions, and joint epsilon->0 limits. None is declared feasible merely because the present certificates do not cover it. U1, S1 and absence of physical weak contacts remain separate obligations; a singular-limit U1 mechanism would still need the actual reciprocal mechanics checked before any110 claim.

The most useful continuation is to use the supplied exact general-c moment/audit routines on the remaining interior or heptagonal-horizon chart, while preserving the actual denominator and centroid coupling. The old-row countercontrol shows that enforcing the parent’s individual stresses unchanged would discard genuine new geometry. Conversely, the PSD/refinement lemma shows how to exclude complete horizon sectors without mistaking collapsed-label weak paths for physical U1.

## 10. Autonomous recovery and observed execution

The complete capsule below reconstructs **118896 bytes of `projective_twocap.py`**, including all2,023 literal integer rows, every one of the seven cover lists, every helper, the true moment generator, exact tensor/matrix verification, all-root tree coverage, margin/band checks, the old-row comparison and all six controls. It requires no parent source, cache, optimizer, external array or network source.

Verification environment actually used: **CPython3.13.5, SymPy1.14.0, NumPy2.3.5**, assertions enabled. NumPy verification arrays use Python integer objects or exact bitmasks; no floating-point feasibility tolerance or numerical optimizer enters the verifier. Exploratory optimization located candidate rows and metrics; the frozen literal inputs and this exact unit reproduce all reported findings without that locator.

The author build completed. The final embedded decoder was executed into a fresh directory; **build and check both completed**, and their report bytes and stdout matched the author build. This is source-only exact reconstruction of this implementation, not a proof-assistant formalization or an independently authored verifier.

Save the capsule as `recover_projective_twocap.py`, with its final LF, and run

```sh
python -B -S recover_projective_twocap.py fresh
cd fresh
python -B projective_twocap.py build > build.stdout
python -B projective_twocap.py check > check.stdout
cmp build.stdout check.stdout
```

Do not use `-S` for the verifier, which imports SymPy and NumPy. Do not disable assertions.

|Object|Bytes|SHA-256|
|---|---:|---|
|recover_projective_twocap.py|32356|6b3d839a196fee7bc31b9489a1d71cd00ae13341ced36c02c1d19b2479a35cf5|
|projective_twocap.py|118896|5f1e9adae012dd4782d6be84a78fa4327a634ac4f1d3a67ca756c704d654a2eb|
|projective_twocap.json|296097|b4718ab6502113e10f514b1c109041945d30996a2725f97d7147143e5a48cdfc|
|identical build/check stdout|1153|b258d8fa51a9f4b254454abd3f88583a04eafd9134c1290c376a11579e36f7af|

Observed principal terminal markers:


[Encoded source block omitted; the code in this passage is incomplete.]


The finite-horizon theorem is established by section7, not by these computational markers.

### Complete source-only capsule

```python
#!/usr/bin/env python3
"""Complete source-only projective two-cap recovery; standard-library decoder.
Exact verifier: CPython3.13.5, SymPy1.14.0, NumPy2.3.5, assertions enabled.
python -B -S recover_projective_twocap.py fresh
cd fresh; python -B projective_twocap.py build; python -B projective_twocap.py check
"""
import base64,hashlib,lzma,sys
from pathlib import Path
DATA="""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;m~hj`dt7Kh(bq-BQwKy4>SE$m+hy=@aif<Hp(x6uSQQU^?{g(Ma4M^3OZ1oXjV@M$KP4@
@!a2tEZ}64FN=Su`^!WT<A2Q+5jz?8jH`2}p4avV%PC-62KnfnJk-w5DE0S*q|FMv_9Eb2uaML)9ocTd^2X(6dwFL}I-*Cj@i>r_
f5;bz1l5%@LVm+p5!kHp1IP<=Q=xq48c7}u?3Bt)4e+7nxilZ2Gky7>l~B~ofOb?;kv0DD=}A4|y1J4kl(jC4jCmk*_Fd$}Q?3D)
A^p}mH@1PWf5!qOB1)<IU>c%{hQ{5ay~}HIXy=0{ragb$w6ffV==fVTj#V$)ZKo-hjrrBi{N++*QsT!Z8C}db@SePJ_xF5zGcpjj
IwYxgj#VHW7QW;O=+|<H5K{wwCGqTWkewazHliWUHgP<FYlMgvvHA=?QnyUnzzC?oN^wpel|=}c#Yr`M-ymwiTldNJ8))z!JDMB1
|3SvBORcZ8`+fZgV(+C=TwmBNYCz~7-j#${VY;Jn7#A1%N1StAc-CUAS~$xX6WkB6H$_foHaZqI26%9Al8)ocGauD@xk)e!e;<N}
F`hev^4w*!rNMs%PHqe+H|SVXKo#RaRWBrB1v+D9&8#k>d%mz|OIn^11M}oz<awMM5U?NH+8rpI&X#K{B(n)`a++^(B_2caVNe&R
TN|S>CyELr10_uaw#GEnRvyL`vvD0Eeaaw+TXj4&l3(P(r{%S<fW!4rqy`h!x*Du`x1m(U!(s#eLz0$%n=$tnQU~7cIL`x;%#1Od
xEwavkBQZp;bcZ-A4;O61ggCsj{5;a`LVi1XI|#=cODF49zt{2WWgl;!S1mW&GDrv0F36UBjXX41G8^yo8gkW#d{d_=lqsN2E{C;
6dP%m@e@L|+7hlmJZk>?hd04?!?SKxh{pBrH~kPDE8<GL@pt|yY-m9#Kw||4%m)JR7+hY)cJ!DnKX@~`e>iMKcOhr>EY$(*Rjb;z
7DWCb#~yHvxg}3lVW-Q!-a6L4zpE@jUPtl~5&W>A+&&X6Y84#VCtIDa=8+K8K~H<b9LVo{!h;rW;)@(6Vl0x<plOwyhq;Rz4>dXY
DQQq^5%P@8Ze<#P$DV#mJe((kL?K*0YhVQYXAJ%vaWm<;3Ue+bD9lp{<?_3P1%b3P`WsqeaCnMfWYrAkC3hhiTF0ZtGt8hVflO(?
MV}su4PvN-d-~q)I@|{eWinPjTEC?WzfgtClG7FWUg1?`J{>jr4bS(k1U9E1LI&xRiq*-0M9hXCo*(p&p4&R*(fSI>ig(%8_3*DL
<CU}9ZCi2b_>)kou-Q|P(OUpkX3^K-cw4!msist=056%PaBkNR$Sxdd8mYbWv*Ki;>Q1_;ZyuEERLvc{ir8m0Nm)<RLU7wTXo3Z$
Sv8cmIc2ZwvI*ryYHQ}t?rGuacRT6MDwQP6deMG$wNWU!SpGvWO?t0}Xhg4S(4xJmTm^0OL@wXP@CMqtaqNLLk|w*zc4tqBEtqc&
gv!^VyOeC=N|hKI1T;rQfDZJBA*aFkvy^6uc5aub>GTEP@f*Y#t(qG@6<8_e+m`c9g*|1y8f%nXP~%tLM}9Ic@Y|P`OEFmxgT>n%
HjM-1_Cd`8;aV}9U+9hC^$XDM-yBF7VA@*TTrw~<sW0e>Jsteyv25_=JeLJUp18E>hkxB-%Gkows;v#J8oS*97%5*(x&I}t*FWLQ
Gs_X%EMwdps%{O5OG<T1UiwYP$6$F7T`9~rbs670Qs4g!u!6knz(wO0rqm@cdl1OzSf#M?t7I94<aNx~0<b_6Jxkqj>1gx~kjfLY
o#}Q32A%fx%|&*rCxUwRV^?gAgn)fIzZY^5Ym9UBAfI`YZBAx>w`yh<3Jv2b*!{EB0?GysV*g5K^?&T$#6rF=RTuqo9u<V}VUzhl
<nM|%@d1TW1Q}r_MJ)dik-r~`e#B|^%;HB76d9}Ww*1#m*qB}X#$%FMdHPFY{(~n*gdtjWxd<U;VkGGz%RHilrfnd(Il9u`wqCCz
qyW>>^1cWN$erz^VfPPECPBAtrya=TtH`I{`z2k_K%ZSxg5ic>0Jgqm3n{h}mVzXV`-CRw9M0beN%1B#tCOkl>M<HtyX4Fr^_PW}
*Wn4tf+cXqqT3TV8l@rY?dRdPwFta2pIhv?wJ*{Me!YWJnfgXkZQL0SZ$!;i=5*rUC;hOqjStbE(#Zcf(j*MQKJC{@Qnd<@RaAUj
##|p325fh>McLW1&{V3ySSXDN$?QP7(N332gHD^_1;YMV<N1vppK9Xvp1Gg0su?d8j@n{EZk!E>|B8RI%zb_6>~k`B5SlDEr?hZS
1QZ{MGqw|@Kr}%|fxj`>kxWLbE@aWc?-g~WH*mZ>YL|@6QyA#O(+G0@jQ(C88p65@cp9S7n(b<}+k#2=nKV*H`nIV;GR-TLPz~<A
kVpSSA&J(KyS8npi}uH|LkNe^QM*yP&nf%<SaOy$nHc&M07$`iOCE(k2--tNJXJE0pRZrUXCUl@M*_9z7xk7^9!p?`@W+?S95NMx
Pm^~Vtc;goGPM9iw4R({Pa509kl0jZOZPS)-B`5Yu3yOy3an*VKbHRzwhmsvFfmg^c?wMjBcVEHSELK~heqcn562qelmW0zUyzlj
Md^hj2x)VJrEEd(Q)#t9QmS~@Ba!^pK9>2u=|_xWovbDIjA{7ju3$9bEijd<4WN4-h4v|AxpI!x;AD89r?@p$p~eEC+jnqkC@ceX
By_-~UTF=`q-i(GD3A8#M@QLSRo5+gUMaG9_V-X&R0h-b{tzU6h77{kA=|H94sTKl%DL60`+Kw8A3d+POa{4oZd}9yee`M_OAqfW
Nk+#v%+^Q)gNdnRGISqf(DkscN``NfOcI}YnEUa2OEKBYm5XzIE?a)F=du#5C#S1Ej)NU-Fuml<E5FyG!<Au{E7B#!I7=E+R1F&A
)+B+&`-A5hX!ttQ!+Z-xc;skgTNK7{Mulw~j3)IiLYIIQX&V4a%MKvDc+=M;2g|P!lzAxTJx?NU4H}Tv%{)vPV^M{BWQP4Ep_e{8
)+3ypRQ9TU&PVeJGzOyYkzO6u)an51tg&lRR?qrKsb)~Xa;*tqXWa^F#}G)(slh$+Pgq|ZhsH!fnyT*8z9edfxvnA4(0^|Wxc(11
WFoiDS<&Z5Vr08|&H(%H1xfqrc=8%DLMloyGD@GcpsJ&m5vY@uh>jHxDLS&(V3G|t6CRSrBje5_0NQM@E?3DN>Ku2Z2*PxOMF*<A
RCFEwS^houHs<4IWSjM<s5!GC3O3>$w&VymFrck>LZ*|23qE}m#w8zrXJojU|Mg?8s?@yd2E)_F(spOYO*a~vty=^tq8a}X4f+Kq
WBiR>F`Xd_2qcKd6kR$tBd1>CU;$(~wuoc(P<7C?Q03B`DUkEryVA?{MDhxP)LuXWdI9gXc&5}qF(=0U8WuW6yD1sIMkL>@JZv}0
$g7N|q%fys=^IApfN;>nuiaCz>yRB*>$P_rezi7+MCtp8Zv7TXh>`+MG^3ku*2?@TEGCe#BK%)fEQSCzNZyMmpGBevX?MjRp%Zj!
sU!eUcobHQQ%BWKN}ku47xRAP5$9+vfbHT>{_)`GaAbbBPCyXzB4{Hl*`vc{?tacVEw5I9L)y;l98S*l5S)0w$`R?k7t{26;jhNm
P#~)~%-ba?c)NQ3&562Gr<D5`l2CW|oc@fQoV8sU>}%1~AwTV$7n7Y~h7kLBEN6ZIlp(TAfY6^mF~tVwfj()1o5VSR!|(qdm=O_{
lGpp#tI5s=BZ@0`)MV#it4xqlh8@y}wR=eyMA;ow-=7V8{Zmw^rb^#EikZ5VO4eJT>xPJg#(Cs8djr+lb&|JHThwtW1RAJwg7n<&
RTRmc6VNbO`5f%JdjVWFS_-uAW-bS-^0myiFKjijJ@vF{P0XAVRTZ9V`KdWWD`eC!8n5lc-_ZU@ATNfvA{enW#1@Hu=R07-aEu?^
i(usE?lA(r)?1b1eQz<?q08pNo_g&G`vlWH)B|mh;1^8L;CVp=_2ny4d~2X-{4F*eU57r>PwgXe{KPong>iL21ziz!n+Hk9%B(6f
VbBq9tB1Gm)M8>Ssp^Hzq=LyqU#-XB@}$Tr<_}uHqP?BjFtrL->2)N2AX`&P@p@ux-1P@|y!=&qy%_0A(0Q>iZpto27cb~=pt7S=
=?>r6l<D|Vx|-!)zk80N$b&7_^&#aFM2T_xedARS_(N$kqmvHpeT^M?B2rX)qGydhg2=KZlA(wJdgg^)inCvVL?f-*d23dMo7NLa
0i|SJm$e@%G6aNM+40~Sc$7-j%mQ*P+qP6}=~$API4W7`S`xeYg4&d5;8Q*Vt#3xgR{AuCbx2Mf<GA4vGoh@XF6l%PtKL1OmdXdZ
@@Y#0hT^BjE?}rbcvS6K^W`h1m&9Gxmm~JqAHDh$C%)^pNP!?{l<W{%d&41ZHvRhPHz9Rf7M0NqH=8b}Cg1Od&@-{NJ3+MZD&c+{
Nv*C+=pxifYlEPJbhPP4nY8XIyM_U^`vXV{2yf1$I%iUe$gu{R7lng-s#YV%cAgm67WEPX+efvpR+D!ty_vdBcT_g|4w>!!J<=Oc
gSQhbo<}fcGD+s+e+jilgd*T=j_tqW>RuIPa{vKD@4@l}^Q9)<13*wPvAeo{&QAa0P#Q@G7JXv2XJ1<a^~cx$CqLPWV%D*)a%a%@
oSb9$H`LY;M!<J}{BtPxw<vDKB@@C&k*=)f*3_OVN`IyR0qHcUhB+mkoW>5@W-&2Dq;H@)bRGVLU?oQ;)A!f#_cFag3E$um-h6K3
#Xvnwwa4UAvW(-HGZ$OFYxI|y3bW$jG)=V`_OqcE2m%-2Y)nwW#n?XiX)v@p&QYB-i^Qd}8&JYfRjB)w!s{h+0Q+n!D$ue&b}&&_
Dc`G_w~?hg?{*>^909B5$2%AFSo&c5HD{><Q?MlFyOxLhGW(~PzbFc`UP#m?VFdCiD18~boFPWR`V3aMv~yWi!`^mA<$`rKTM5J-
1Om5;EJaY_)VN#xG*kQlR&?QY+OF9VcO~@o3CaJ73IJ8oeh8);3w24^g+y}jNu&Sm&!+D&BtXXj{j4)!A#(@Zh;q6jd<}~0AZXqP
vYGl_ub$|^YfmF<mD9YjSo};Z+EIBDy+0L##Z4X{Solj;K_EJ%L7}0@3BdswhFs@$-goy3eDJ@ZjNa`~U?iqPjihaE2|R!dA1gGF
GbQufUiw5`VH3u`LJiGmIEv$m_6Y|-NTpqsJSukXS6fYu{V1MRt7fc`P1b9FKVNbOJ?>SU!<-`8H^M3`3HNpgf|4)xvl<TWs_~&J
5i)!R?Ha5|OObx(AfjMbqP<|qeYN<&Ps9ZPpo{nK60YGHVzw6gTw+dVw>ZCQ7oYe)5JJpO{Fpg94Mj4!&`+cDO;NNnEOLwCouWg~
>bdFt!d4opw(Fe=*>=e)bJ?SkCimS5r$ADWtdSm`+2YS!5Z4LNgrb*l;h>+Q5d2x)=V?||*Z{nJ2`uLa>e_7#^{}w8ZtKMig3N@=
;;*xB@R2N~x$2kp^z1Ao^Fg{2yS(9D+_R?2WyYVYTC3hnrK4W`*rKY%lm*uKNyd6tcnFj!(R5>YMStrzpgX%woG#V=sjjvrJAsB}
dfDP}YiSt3Cm%^hwpQ<F<OUtKNRmRkl19gyhmF|uA|WEPsnDK1IOobf?>4_g30ahtq@xD}bUfu{O)_XL$}xe@u)n9uuis05m0Wsa
Xv(te15$Zmv!?~JP04suV2=pXbv#dD@Vh(-ely;F5>eN&Xsau%1oq!Dcz{q2x^-4|CYNfiWL8oAnbiU=KMsXkhf*YoN(*yzhow~r
*FIOBQDsfAQtWq$^IeuTwjEt;F-izDa^38fbOi|A5fT(LF#2e@d-@0)V5Q(l5}WI_@^SgMgD{JSL1zooNn7F^KD%B6%np`N24EBY
RhA6T<m0vRkDff@TwS~YQcubHtka~m_vo8YPVkD43CBaCe*w;n`L{Ce43j#l%PkTY8x02j;0vr~OY5y+h><@r?J$e{193W|Hz7-A
Y~p~+#me6ci=5dRp;?&m@lA`#ENn!be}itV>oE)lSD$s}tw<%re$yjlnHoH<YTALf&tfm^S$id_hID6xWbRjcy~-0pt?LbYP-HN3
ZFJByt9uot&}%<&-vyGrocvHBt0l3N$%r4;qob<W9OMvIniDtkMmV?fpIinEl!UHQs+37@xhT{H4$92w-p0_E&D39=#iuHnhvjcc
1nT~Xds{*`seEUe-y~Qmw%PO`dkVV+R49E3){bBs^tB{N(wdx@Eqd6-!oPz>ESwy*rpL|&sA=(zdKAH)i-Bb`m^H&baA=P;$?*}2
Ti5FVX!j#XmNgr3*i0Wf&}J*;a+2pdKT73MpSLk)wsf+*L5%2BJ10<$cH{~c^>dI=a@ylV>qOE4RFV_M&LQKg*t5eR<^%eK?c@Nz
o3Y7|3N1>6L_lz#maKzAJNN)L0-1(}gTaDP)Q?jeh(%L94XRflmeTw3g(05oX$m)fQ}`f%UrocSTi)%@8DJ;%$`&ALkLs?_T;L^>
%{*PG!(4cYjk01;6HiDwD(~i*cn<k#5(!)88uZV%{6V0KYN1W<SVez5Z+;~cWvmAdy$!UVh#13|e-ch^9C>edCzj`ux^a=eY$BHO
_}g3-v1A&p<q*5MW@NTzA;l%$kR3vWy@#6US6>_;6U@mBT6pwBjAyjVeI^8SQi8e*<3IT>$B?x-LoICMHwQy4+TMj3K6@8gt?|Po
(FMq8edE(djzFC6K&CVRrmFtIs{pvh!fdNAWSQuht=h(akT_(@!{0K*iQs>dK%XHHB6;qdUGo+N@kSNU{BI%<xA-t&(AkZ#5O3vS
g$2RBCN~WQKtIc>2i9UbGsJ67lj-IB{kvt>cU8aC+<cBSN$`!JbjRN)#O6#?4k41Uv>bmBhmbAf)JPY5@NoP#0GMF(x?O&_RFa?H
evM6@wg={Dj%6%72O95=!AMd`(_t3vF4G2@!YH0jsmLfN?_>;)U>bwy-Fu7O09%_!m551LZ79sc=+y%-4{~`M#%(5*liU18wW)~r
6&}nh8&9eiu$BN2`4#}PbaS6HR8uZY$JIRqcRgT&)aUnQ1~>GFZ<08}{dseW`bVzN+H!HgqxUQEM6=h&lyH|hw}c{+iH3>W!wsjT
+t<7>zSyuqDpQRYxLa#Y*zwvUwSVu?C?xwGf{L>dXg9!kZmTmwcY%o#Dxwu>@#+QTzU5w?R=Ju-E+8vC3TF`9t`;Gc?maxIFaKh(
dzhxb!wlpl6rPQ;u`;0u$4hbhpv}Oig8sRfZZy|44vy})urBV3);oDsw<G3fV=XO5y2l-t1?pf@JJ0%~`|?SmlrO_fpQ>-yul{uZ
aD{B&^zPAPV(>YQ5nF27nuQ$Pk76AWjPPN18?_?aKrVj_p_r5HQUd)oGGV?=lkb&S{_Cj?Uu^P0`=*>2!bx8!TXHCzboxSkw$0qP
L(M!0V(X|qWBofFpka5j(LWocBG`IkJHtAF+pH8Rd9)#?2{(qg3aM(cpz9B1LSgjKSQ_D)Dl6=B5+AysEB2L1W@;BH>27@t2=D$}
vUN}flM?`*wXKTjmtAR|;Jkaui>ZgZ%`rDw^gx6VtGoG*)3(XY`IIb@>K0ArjdXYq&RaJ!I$X^A7XUblfyt7?V~L7vOEAeMD1ng-
4UldtK^8~gu@fe?-}HqGrnIEUq!7v@Zi*)XwJuI|gi_^uU&;E>*WZFnyGbZ}r8%>6n;C+G)t>+4CgO&Dx;fX_o$7ZQ#I-Dbm$9eG
Vv*zbvKojgolrMyp(2yb-J>CCD{EEx@BUIc^s;OF9^`OYxMN0RK1dI?2;yG2P5X{Ky!bhO_I<yHg<Nbptvg>Z7?7->(#Spc7)nLm
C(~5xI*sDq&}LLwwB(>XYY0gPB*I;i(I0)iH6d@LSTc)%JB2V8dAs>fK|B_2zKVisoosy!$1(v;25efq1ZcAdlS76FP!}d$39X4|
@M!_kpKvNG+V<<_Eapgh3^ur=cg`$d`DU6(A}*^<#IioS`?o}9Vud+4jQt1fJ3cYnA;IyvLg2~5HfewlrO=r|5Ic=7rwO-N;Z{pq
uVik6*nEne3iW>6Rt!jQI$Xm&;mHb>&&Mhy38i`!IJ{5i<$kWn4+P6_>&G)U;$LmlDF?Xk7<F6%$?QcX$><2hK5Ft>o*m-cSCpYL
o{eWbq%O}|$qwaLl-)DT3$L0Z;K=%j5J=m-*Mg%Av;HLxPEQc{H_#}pYD3ko$vB}rZ(;eWO90zvHqc7wirBbIiW6^bb6?8B;no1{
N5><?3at*$t+tiRC3OANJVvLoI$C_NXRpOpRopZ3MOPRTz%@MTeO2a3<1s{H4^m95-%!iARFMs#78Cd!8xfdBMUrGbkDXOKxD4Tm
avF{4JVAUk%rSWahN?I!iv{jSUJItB%}fo;IZjeAq2+a-6=Q@2au^9e^Pl`7Jrk}p{$-GAm9*@k8sphxb6?CDp@hAVVq@|eV>k$^
%F)^D;tNQ}SP->i51(pQFBRRuWdN4%o}tHAU<^VJV83ZpyH8;7j&z|8l*ETW=QM@Ez5vI58W$7ElWywYBa!l#A;)1p2Y2pT@rc!=
re>_S43FGmZ>_m;{wgl+2btgAyuNL+oc;V-8UroM#obB+L^U@(_T53Hhg|enLCZvSJ9Z^6otQgU)BkYFpU2;ZsF9!zNhA`o{%=R&
d%TF2W!@<7;`*DyMEatHCUu%*e#7%MZ2keJLj0!b(fzfxZ^}3vv?|{0;#TY7qO>CZ4i=w^qHCC}<w6tE3a8RLp)f`b^@ws|V61{*
Dv;Z&`&7(}U*F`n2NfGw?1g3);X4*E%&I$B0$QpCAlJ8Bb=#}NCOo45hTgWVB*`0XV7%KEZbtMq_v(7dw?pp2OspwaCzwoTYG&RU
$rt(+8Le(-KcqXzRt&x4O|c+t{dYj4<j{k6cVCk<Bzf|2K}xB2EiH(;Y+R`scsS%$9o%=QE$|!Xn7|(z=a4S%=(OfdmdioCp4xS!
;oTCV<mT+~J%VQR0k_@byRdLdD&y|a`WglEYrg_VSwTt*6#7;*`0<G~*F2RKh)HWj85*_co<K$Y#rInR`;M8808z3q(j5Sbmp$3-
R`U#SWU%dwHoQd)@Fd<0zkv4Pvq9n<CWe6CK!#GfpgHgFB%tu36tmhqDvN_tV~J)GgLuJ>4USnI1huemrp{u=|6*yOe@a%MT^-TL
s|Zn7XiQzkZ=QB7WG1&tcop3~tO7)Slps18S~oq9`k?Psi)ZB#47{=tMExOjg-QT+(=6CTTnnAep6SL+O2eJ*HsTTo1D07YQ`BKc
X4iGAMgqM3pCTbt!pck1l=;vr?v{w5s%kX(^p*mbY_Mn_5p|J=R@@{T&8>+r9lOeHm611Za#8nz_=JHJvFVTEulE(ZJ65o|W*YZP
betfHR`%hEO6|Wbu#rAa@3B}B_=k^YNt3^gq|jOojmSOdRg>a^>b~!J4APbm&?LX6ghGW(|J|auDIiLj#~#Fq_^|hVAN^V=87uql
3EMek9`n94f?Z+1P1F-n*ke%nNxmc*(yL_brywTU4hZ0=pV*;Fq!~<i>17ew*Tz4D8`;AUJAP(4(v#tNX3nuv1Wkmi-(rGiKG>oF
_Eh;qY)Q`HM#yz2cTKf>jZ*%V2}{Qzm73`I6}@E0t?YbrSRpyk!^e{;_|!cuHSr%yIcFiKs#8wSjRkBHiCmtCSj<0|7S?;&*IsmY
_S~+m64sz%l=dpyw%I(*i~9~hdr2t+DEm779W)H#^uK3Vp677)<RiO*_c;AJ`nATlVxH1d%>K-$YC{T()d#;Tk*VpyejY6M;~BG7
Gnn!<RP>W88fT`pWB9(v+mC#EBkUy_9QkRHDyuI03bt<rNd`D^<a>@;TnHg)krTR`-?47N)}~aLkMWvJ6O@D4k{p<DyM;<aw~f06
E8`n$K0Rpeh`np9!>rVt`keC}7?j|j%Ua$Om6qUwHg16Pv+tsbV+`qj_JwLV=e{?vsD=eJ7FJr+THX&&o`m$^H0qCN;S<-4-8b}(
X$TG{yE9qxsD?4*+rN^X2g2b4Vz|;$h=3-+bEHbHa<c<s86xGxx@NqEE~{Os8m&A^3ZdsfO;b~G^>s?W=j+N~-YlBSOSwGhG>PDn
!zY=8kt#>S8im&hnedGoUp{E3CVT^mYy~ukcRgWqK!=T|E;UWE?NSsHdV*ht>p+l%B+A_smWiA<kcwC6I{M*$PPuWZ4GDwn`y4J9
5SHOrBfr(>@ZVR4@Zhjs<yVT`-=RY1rJ^DiEMS}>C7MKzs|*Gaigw)*s1Yf<)$B7#9TJ_xg*sXMc+{Re8&A1kmxA+f)c?#}6Opby
Md2NbiJ52XC1ypOdxH?iX`gx5H<`2_5MyBClOIQ;=<JP9l%WMpdPPlpM4-*6*aq0lDbUQiLRxIbhkJ~yABj=gHe9SayUhDf8$NSN
bYKzDPO7h1C+Sf9)1=ctsMp*HyRm{795VWmh~V>6VW<E!G3O;`0Y#Q>Ww+{+p-`(ygpvFJevEEi=`kOtCDx3}N|GXY+5JoYhRzFt
b<?f%@^4QaPFV-m0zv0~;rFT$h?mVw(1uKV!}+Z*-J4-(SH(F_H`R3YJ1^mYJ-^UCUsDSolzF+BhMZSc`Ps4qp0!9}s@Uc1Eg`={
?uvGbiU~dIDq^(n9r>1(dhIdX#Ny$SdUQjg?o68bETiW;t5)uZ3HlNlI4y>AF+gMcgUY_7z`>JXk+C-KXd^@YlVAP#fp-c#q{Co8
xb7mD*LYi#e?RCj{|El<6&U#!J7zO2bd=}lRA?X--}7H8lz-mSx;bmUMFH0~>=KIq+b=IsnW3*aF}H4Q2b6POankR@yTGKa>(2t@
%wHv^3cpF6meO8&oiS#qY0TznH;bV!5Ev0wEBD2}(b9PCp?4sC-3#ai6XzP3bc}>huoBnH+DFVe(-iN<kO%u4Iup1b=2Zu?-fku|
1l=w9uFw$|S|QT35{!qaJ{|(#^rZ5D(%^eGc|Bngfs$*@{w&Vik(`)HkZSTGb-D1W#`#8J+s~>Cm%3`mNT#2~UPsfnY)2g3>BkKT
mnRg^PaXVgPJ(Z$bzVW)TH(zd*gJQ&L~3Mk-wGnLd3qbKn9`P{aDiZ*?SPAnna7&|a->hB&KxR;A&#+;4{0=krfti(4Xnugtg|fB
9r(akHS4slL0_iQ^C16jcScVx%<@~NIM5M>JYPOaHCt_8KEhvL889ZuVFRa46CHZ^b$dNo<X;fWhnV4z4kQso)8yr^p<cBZJ6J(a
#eV1CYRFrKw${z0rI2)Rtw>)WD6Z}6=ejHhy*H@Y{OMqag-zVAupMFyT)iTTW8M#4ct^2nUHp_zH?fvoK@<x25Ca}-XG#zVQQusd
r?9I23u;f8b?d8Wha#;`nWiJEph(3eKf9byY&6`S?&m%S4}bgHW)5aHCM!3EVPeClrf9=+35J5l6&q^~(tLZWH30?ktQ$*wnx_`K
D$g;?13dA`UFgw^STEvU7t;evFH2p*Hpi5<(H6kQyT`)OIGP1pNu*{hdA?o|ZK^quvzjH`9;D~0A58|~`V+iATsax%fVbb<R?VxW
jzp0C-hp#`WZaHWB@g`itA;JU2A`7H-?2ZPmm-QD#RZNF8v~JhcM~21e<cEjO&G%${h$VHUX{o%V`KD99#q@u)q3m|<c0L&o^9p>
kc*;$nB-#CNi#0Gzph4Mqd*W5KWQ6*1qH#mwig$gW>@IgVT~E<mD1mJ0AyX#{q=9W1wM~y0QlaTlH?Kx*CBvBvBN2@m28^@z;(ZN
i2H8;I;DUT-;L^~GfqQ&T_h+>{PAT<UeL3YdrE@&Z}2!wPb=&^CtkpD!01UDDx;{%>|AI!sPwv6gKBE#$pN1Sa3skpF3gm1#68>0
Hlurh6O{C;8GH*Bm|WrMM7zhJ*->9Ss>-AT%qFe{_?SH4?CD7dDvP26r$zl-MM-pPF}-kyX{Cs$Xh6Kh$~9X`Ef#o?rx^86kb2~^
ywkfWptWA3shmG<&N;Xr@4f0*DbGX;k1+nS*@SI=+A0ABKuE4MPo<a`Vd68k*^DS<XFmg;ha?gN-^!P!DZoV+s6rZ?ZAN^w<IU?v
9A7_Sy7tNL-dHY6lls1k2zO>x0wMNRr|6WL-o)-wqOSF`cOs8{(&2EKx#{jt;NF3*Jo;th{*>pW&Cju0u$kVgg@ZCJVMLdqCw+*V
IBrN-vso<)4QzcB!`#~6r{iezhf`~wKwq2qf73z-o|bFh;v&PNzwTW=HS+cG>*s@hOhLtU!|!Ut6SI?HaH0R6W&m##SjU=f3juf_
!KjHln2#z#`^uY7#nMG&)K$BCR5e<1+_#G7BsQ^<-FetI6_o<{OQnOqj@DrPhWh}PPw$nA^mWZTq5ibKT`(8L{;SG4r1%~Y_6-A`
VcF6kyrBr$kQea~QI2i4X>Qb4%`Pq%Nw*(}VK<R7dDKxfrL&{KmCz<B796oNtBrQc2%SzMp~m;}D5QKHV5Uz!m|N;XDlCASA4MEZ
)vA}IlfMgI>^vxW{Eb8TlxQ+$(q>(<Hq}419y&l(;xoef2cGH)Ncw=9rjAeWxY9XFZ|gFOdi80&RI*}aZX?^(Egn@?W=NN9`y_Wo
j?pxho(Ftn!@tn2#r!NF_3honZLFA$vj)4qy8}uG`G4b^>lZMW{&#$hPE2%&d$m9=NXgixgxwdUuN??DecTcf9p6tq!h$&4kg29D
C4HvKSU|K^&Rrl&gd1q4siPl*DP|Lv&#I&4%c&0EbZJ-IDx!ZU=;nc7ik3atVr{zO+t2p8W(w#*)5^4v6epO00be39uT`K$gP8|W
m_ZYLf^doHXe_>U*t?rl9bawo=hHfC4<LuR)M^MJ(`;qxl#>cQOx&|5qTg4wzYw?PQ4fdo5R#nBx-Y-t+=ZcvR;UW$DvgNoJN!PW
btgqAhzD_2H6O!O<#s)JEjGN392h1`=<)==Lw{d4;3W}V!$WxbyJ`v+T_r=BQ|$=4%x+`B%Eb+kL)@65eXE02&6ckxM@jkMQPkm)
UY_m7@_^tH;*^ncsi9;BHwB>T$S&6CNerNoKJGC$7B^b4khZM?t+UzFWDjKRb=-*&QCQAf$MN#3?qQL9dm>9)32IncuoY?Kqa2z)
2OFAh7>Zx#c|^PLCm1lX++eRHhKtQ2$t)@$Ywg+`&k>q=Loq!x3t2QYysDR)i?o_!Wr8xB$Qp~R@E!9K4J$-ULBHNmAGA#siZltG
xXpe`pRa&_D#Yt(L$9vTA*)EsoGi(Dx%Ap%rdbZB?qfA_Z0)trrnPUTGUVtTtHMs6%<X(lwHR=bwiBiDUt^i&)}+)EWuE7-i#bpM
VY>2#oGuh%ZII<FKzRgKE)2rc1QnR@m&_XXM9cFYNtU8>=hes#>j%H?LIO)KW?esY)EG*pZ;!YbVa;j4EdwBhXJN-!=XEq1l(Wx$
6R%T4lSD-2p=diGEI(QP?f|V0B{dDcDtLT(=j3LqZ&T3<{v{|KauH|Qu><>mI~j=0e&MNT^wHyy1R<c~62Ac=|A;ia8r*HB$H#I|
`OMhm+Z)5bK_8{JWAl+05)|LdrvC(EDY1%t)3E@z-Ak{GgY(dTm`0UT*2@8Cv_UX8g*?{3Ka6%Lds$n`qn3hmj7KQp(j8(R=*jfi
@Ssn3=e^IO(*~l;(NsF2Psxn}ANi!D4b-a6X^D_3L9OO!T^Rc%Y-9KAs7;E<4}3qN$BSlg3>6Q6>vV&^V_Fx-WEmK*i_x~FGnv?O
@bs09s4w6Q!r*=0PULS@3sVWy3BShU>aAzaHSST<pLs)1{DCBZd$P+3CM1jvQkkkz5&HODSAJc65Yb@jvigDl2w@8A<=5IY7zV9S
Apc{b$5i4gVt{(y`eYi4FFoG{lQ`^%Y`XvD07EmwLmRD?BQVf_aB&}Tn%d7Ce!lrpw?LiL{8Bw=4E3CNp02BlxS?_EN@%qhwmhS~
30tqC)2_yJ)4+SFx+$=2{$*Z#{uIhF2{O7L%*L(wI!a^`lbNVs|8^Kj!0S4+X9*^u$;{bQ!@z-)j&KW-0itR|$48}C>1cYJOyW{z
yp6xnn4H<7ko0;=_%?J+N;!bGNV~o*nuGT}&%?)jLo{V^<jO-)l-yECnG|JkHPuCJ)aR1BnbU2HI9qhs!X}>AWHjD54$yUl9fBuH
U<Ql)M{4!br3rCD)OVx4pg5LJt?egJucQJNDs9+^c@MkiP2@@QtiHX>&qVFDYr#1P*kGNVe#ji@5)6$|(Kq|2HJ?d$?-;~E+OgRz
*2|zuZ_pLa#*5B6VFHxf48(>Iq26d2y0)92E;dWHPDTN{V%I1yfVCuDm&Ii$Bpfl`BNNR$rNHw=N8hP3ggM()_)ds+KJ8xysBFML
>z-ZP$j684Y$UuIU`I_0O7oV*H11{k93KQFl*R{Z630Cni}zmmfcn0%4Y5xfGkDliQ=K(pEj({K5?;6j1)uVop+fVrr%~uhZH+U?
?Gd7zfE>g<H8u*p%vKn>^T$Hdyz{X_pMEu`r>zcIxVt^|lmloCKXsX#_9gK-%@?sBecRy}w*C2}vT7P}se1oRj4D@Gf{#+NR=4Ao
r0t^K{l~H?b~CvtMKe;O^E<|g9$T{VvL2vtsy&~!2bj#N?*Ui#)?niHB+1s}fm!D6JoMf!lnZaNL^aQkqIjc+;+s6;AdK2OW$6lQ
HB-aY;|Cby!8oGeclQ!cx}CbB>>to?=tFk5#1W#DZ8{@-_G!ogy?7ZV-q+8`dK&(;>2u9nM4xJb9o=HAp3Ah@)rrYd`6A|bcs#2Z
Cuy*$C#cQ{Z8h^KObj5u2DQz9A6<Mn99{^VE4=_FQyo^ijQ-x^?S#GV+K{IM7ayA>pz&4ryP8<q<)UI@NUFqjr#m2)-}E~9p{J{&
oh!=BtEnvn-OMQ)HbfYb8Hk7kH$x7Rv7S->HSkafeZSOcZK@Byq>|`i(9QYCZR8v=O|PbN!@BNMLAT2lmP*tToRXUN3a^S4Sc8yT
1!Cb&!(_uxXFoSWg>}q1-g##LBlxD~=3XU*RZtXGV587#7Nk993Kw`z<+If1RcL^QSmEY1N3(wU;wiVdFqnzIa4dWT%E09T`n8UV
j&Usc4{NAlrxAn+Az@{Gl@>`mmdet~(7O535I4HSEhb8jUuU~r#z+?GhBU-GHA&4bLpQ3>7vC$1fG@+IuRZCS!#%jc`=O*^>vf_s
{7U8*hfy=03+irEG6J0%fvx`4f-D(L`Cn+6^5+M8W5aG($&S2(q~vWkSV65t?5r{Lv#tCsmjr$~_j=mM$pIe&vBfo~;TlCjRAG@W
!k^KXA3S|r>LU^%uk5(syUmUo!lx3;+u_8&>GKqsxZTfsrT63{mn8}~kL;4i{<Z*=*^KY__{;X#w*xPPQLXlCNZ64DQP_7Kbho@6
;Rw5Ngf%h2F6F)p+#0jul{7;59NAH~1eTae-!qkkE|Y;ZIBDhk3>FM7ED-2+t)}JXA!Uje?!;L{G+d-1a%yrg9Yp)MpwYhCtVzdt
4h2_euTD26Mo2~}Sk7I^Z1?{hYh~wR>T<xr&z21K6+1z<<$!z28`Vm1YSZThZ2{eOex1wJ4^2B*ZF5AMhH8EiJpc*`n8>|fox@HM
_~Fs83&w&F!~Kwi-l3e(DBXyeUHu|cdh|fuJ=e>39$PO2w}Pp$nOM99=E-w9TWAUkRGeV2zQHeJMb<LLO`g~Qa{QUMJ5)NDwW!AP
IiAP^-`#Hoc^=mA6*tP<Au|l}=_rg40HA*O5>Iw8!i-HBo+bq-O77wI1LZUn<OoS!ckUD`jwyErA>W-~1#SP#qV>n{ql4YGHp7ji
$7{^9Q~&k>6@q>!#~Vm7_GE#6Tm}WHsV&utEcLB=nNV84hfTxsN*2aI2#b{$c@!A6av^*h#A9|WK4L&7BYbTbs$!r~Hm4EWh_}RM
nTP!oqGCx>KBV4L=j>gb?fc~oeKGzR7|11(MMEk(>HgLb=4#dX$W5?aiypNt*FiYOZ-BY8l=4->E9!a+lpL^3Xs3H{KcvG+&FhB?
q&ZAAPs?e{OZ?hUJn4O*1}Z9GuBcqeaQ?z@82PR`VXhREFv)!LF6&bmHiW^@DrmeKpdZdnV5_cdX{4^mrGOs?ysQ(s+JJ@W#6)*#
uhN9(xB)m*+9FSLAI~@U80^k|5x0aMG%}w=Fy!@Abv51NKW++_?YPI@I@PX7sL?pp6lm1WWk>)0o{e&u)#P{czfCvg?3YNxXmykv
U5{p0vf;dEi0{-qAhQ|L*gtTXV=;K8u-98}h~yib+Zd-M^JQ|sOa$&)Hn@OSK&BP?UWlcQU;q~@fs!OJ$JkV3K9;Buk<D5sWYoc%
Qcs@tIM;meqGw;65w7grG<Lu4qf+#UR^%zCPo)YXh@a?Al!bcC_lTG3gFYPyxDOv+#`I}1&O%(jV>DUc6<aZt9zqjj7<%xNw+rA2
JOdGpvUveiR*Yj;0Yk6LJHojoC&bZzw)<jGnqZa?`vU*{pfN?G$$&rL7l^StVHzOmF>bnsCYO6+8V41F9kPZrH)wN9PZ$=RSLPI+
it#&vI4@nJ7Q&%h_-EP%lj4my8D^I1_VrQ{SSyr(+_(x&?&K^1zyA#mn!c~?h9+d40{&?wrl}|pgV~w!E*V=lr5j#kW=;1y^SPUu
!11A5=BHPEzzN1?(i~T%6rJq(S;ng0t?V-<PBVDaPfeoZs8xJBGeOP>Ja14EJ5;c?xAgr#wUs$9w}eHp>SPiMi~hiLnT*!@{#}>S
26oRk;iSU~iqdz<ecu2i$_Xt|ISQpoMLW~hJY9cEo6yp7{W$~HcRAG}?v7j;4;tr|VcE<gYR)Lilc?;duG9)cAV65=0d13HpR-j9
iA_+ebjb-0PbrA+wvJQroRc^4Hr6@QdZwDsH6umD{nGOMe#=PQwffyA-Kbg?2dCQ(KJN_=OjnW-d3vw0vX}@<<)tHzHQJ=AAfd^q
G(7qC{~?W^>R})s`+mE2bdmDY0KdU+l_Rh2E6H--jxNRk>=(%k1kS4|*w{`$?#%fBB(;=iGMt+?{$&~4e0X00!OLYWmBKXp_jm`P
XcH@MKYc~n8gyevFf|O~7OC0rxe{vjrUI}U3CX3`IV#ZU4ZaR$pO&SrLpOm&`m8af{fE8aXC_&ft2gt!<?>-bKjMYc%<>YTS1}Ib
&eH=xt`ZXuzM=dz9agSvfnfk1=6GAZ`9<X=M(N{Rz`F@2^ekDF>8}wTiI)(vc5}69;2Y%C>*P`~%{dg6>BEUj%OMI=ShO!SFB{^f
>#V;;FY!kGCsjqw_z)%IhLObVnWREBTkp*AGS71w5)-S%t>)rFR&jeC+aQDdJr3)1(du?U0C>iuJoEp|Y96T~)q@A7EjwJ}tjBAO
Yjj#-2`fQ463xapdgPlj!|wP5IA*OR$Gl1!XBHJWapjnyq=LDlW&AN^3RYo;V*ukypG|RQCOfd4&tx-YJaAqa_iMEY8C@2!vQ+Sa
m~4@OT9<ib5`0g93bIIRf;})5N-<?%dC1JLPw??)Ue9Z9-aiE((4UQjp7yaR9WSq!Q+(gLWVe~qnmWmHy=!?RswlV%Q;ox?+JI~H
noBaZ-Ym<F1h^N7PTrbM1}86Prxj4N3adCzpbs<n?)#a`hyX{;nQolljEKxdpsqLLF9eQpgfJ;BW2^*;$tAZ%lmIJsgM2we?3cZ<
V}Hd6a5g?+c}Y`kt7O;V<1(4AnQciA-Sel>uW-C#plkKmm(3Tt!rR3I4DnQqW4z`!#@r#0kE11e0DM_+lD_(qFY`(Tzax0JOm^Yq
=vIuTv-B-dL@W7r7}e^pno$a04up9l^>viBeJpcly$$5V*W$8ee6sz?I@*!<-)ilj+_8!4TOi`!yMeVyF%5*WR?}1e>yS_%!$ifZ
{>UJpPq${Y5B)q!0vSbih;%1wMNkA*Q*ox=WM8K*U_c&2(w@?FPO}-ru4-Yu-pV2SgDb}xP5PZZc#q3*z{R}{bc=!s>m6SK=O>^9
>7m(XLPh@q^ao`9O~j7GUwzY2qxQYCu2;tSu)&iUA|8)@zG`vOkF_~6awnEPyXE9AS|%1Fa`3RD@NZG#ZAw--c!dowmMN8nc(ddL
(1m-IY+){mV4cViSsD|sk~%~evc67qT`8h(gCRv6Zj}}df6#bTa5E+UU%W<H-4dgpWzKcMtRLs$Eks#M97$X2@q)FIMDkJL4r&Eu
%%_pP{hicw6D9g*V70B|d&IMNz7bpA=l?GbdGZe@3-XsC)o@5+k+yux{Y>7?xEEJ37><#c9!T*keS7d^F+qUv2Gw_0h*B=Db(*SV
TN54d1jr!I2J14__?N%i(b8vyMC|?Ct16zkfWx?1b~aY5a#9mfD=v8Z3*&gRqdl%>d~nNx10sOA$rKHQDp{BXkq98~Zat)mAa9LV
Z9I!SLS4BdLL8KxLk2@j*Y?d89Yh<cWKzBp!(1)MzvHC=pr=B0>%pNVUt&%w338%zd>A4%F1=4AN-W&U)sKm1qX6|ySj*>!dH0KN
*3CU7hGA1l-(?aX@Gz{Q{rJJN!KY4jyIs?tKp&n$ISVj~Fv7J^go0KQ)^~JG!Y@ao(^irfpwXzR83}(4YCy{QSz%r9>*D)o$~&P3
#UJ0RE8Iw?s{|#qt(#OK%eM*d*r&reU4J+9%FJT>n7Uf1waW7L{cxxirw}sMu)*t%y8|8gjY$vDauE}{)gWiN9JmSv0T$tDPKiGT
6)>vAR@S~%u&YwF;*_E5j|(MjVsYQI;w}peP8BaVmWTNFqy`0ksE$G?IJeUpND;Ch=U<Eo1LU8coX36)ipx5F3Rd#E-aX5wSo=$T
21F#I6b!hwwic+3dQmnf*NE~ySPr=CS1jgQBOaIJ$V;zm90+@ar@PSEUO&Z2DCl<5u~|gupZZ9~s=S*cfDI#c(_Z9IB;za=@x(Wa
Bnm5{jU5PvKEXXj>&iP7SBaL+5G-72e??AqkB}uHN$K*xdy}*W>X1<(P1Usph_%KDUR1rA<V9N+8*E`BRif&nuv^_+h5`QvR#J2{
JX;bjC>Y~}kZi^}5cp+-Yo$X7+D@313PZVGpDyYs-OfOpmC}m>%|R6?ZRh$YK-sUuH8~{2=fd<!$;7=qS<@EfueR930}5P(GTveV
i!Pu_f%|mJ%~(SYknOkl3bxe6zY{mIdNn-eNrkC#)6yUnY-(M~b;XjiW#etq5P^OcSA%DP;CFp?WPl_r&+F#5vu<&^6NTw~n9Q>X
@esPi%pT_S*3)DZqCnW700|o%2PEa@SF++(6niWGTf5J{v^TzjW3Ug0!O(4)jFOX)zmDbg#FcLTXxurB7f%UE(c)=CXCoSNAR3mB
?Qh6}9#D1n!nGPWcmGa~VhhU^OHZ?sQmNGHzPyMRo#d)ks}lLqA<Bw{-r@j+{eWGtbN_&@5T&NU<x~mbFgz7ODQ9<ntc`fyDfq?+
WX21$Le2CnlL`3x49Gc#7a_+lMkab{K=b`1N-<iPKgmrJBW?hm^XPEx<JRMU(`5y!qbbgXnt%M;xb<Md1=%uT1_Gq%SpJ}}BXW&J
KWx!FNe`MR+=^RGIM^~2sxIJ^rqhcUt#mLAHDA>R@eUMe7_Hn}8jXeMtx+BycPkSu#BB)AjanqpKNAtl^`-_PYG{r=-lcK%fD_Hm
!kEs;`Chm8Fd?V>0#aqn?zwq(v@ErTAj0m8G(Q*@^v^^&xK?ved+dtFVkol0zp;~j#Vi8Nz5(F|7q1J5d&@|D^nhBR3Kg)}ZImo7
X#Zj<=*0xotzthYccDAMqF<8tsVz`ZTeodt9}>Cu=xme8b7d_ZI$b8p=lV>J7sBm13zXC_6YBd`@PYdDo@Lqz(by!QMFsyX0)m?V
E+Zw<sD~51Ga&f^C_VY+T4UcAP@BdhHniZrj9uLYWe)ke`=^&H{@P>pBHlpk2jr--`-G=RVjcf_&Ti+1<|D_NOV_cv8iIw@>91!?
I(9m3#$#74d(-pIKPl>D{eB`8W^kw6Gp{5yULhEvD#pM)w~-n=96|UO_HWS%gYu5$RshYmfKDxlqq|!codpk%0+aZzHk|@*Ziv}i
bQNz|hgh&8y-61J#l!1J{vt<kzZE>$7IsOJJ%?yfW>X`)Im`e_*_W7lGXB0dx0mi*G*9vz85TX68#LE=qb%wT?Sc^pP7O0>+2`V=
=N@73MnCb)ypqbh;Tj1xuQKq8VGT+|yuBGDKNnZX`?T~9hy{qXEtgYIF6F`BA29Q>t1@19FUl}tf<v$LZ!5z|yS~mF$=uG3S@AtR
ye&b6I1L!nIV1h|gLD~MAtr>u7U0_uYWo30BB-UwcE7AyHZy6;zmLe{YP8qKsy*yAV7&Z|;X}*rLXEl=bq+a<T$%rBOX)*tN%ydD
SQI1py_ws_#0z)#@Q9}YzM<TE%|2q#-`+|bligZcLW!LjD4#Z}H;V#&iP*aVzLVyqShlpG`C;<K4JqJ-4n)tJq{VeC+S+e6Oz{s2
mhuw*b8{5wK4Sul*+oKoZ>l9h096$8x@w{;-`XzTZju6Tt#Kl#Zv?|^1qtQsXu_!|piE-Rrf&DK>JXhE=|}I%E<E_nYjiFH<v=o5
@C%W+MWCIzS&f^JUm}aK`szTI(tubRDdZ7|&b+;WdtO7<+auwjEEd5taUm_L+XCRo_Ok>f_Sg4^eR!mWpkrkNtdX%ru+m!SrO1jQ
Wb3r{5kU^vn8?1%N`)wnCFszh=9lj1huUT!5-^Q3PB3LgsYv}Vif82P;IyQvU!k~eUk%HJ8pn=Az;>W|?l6hq(c$KB;sOpVE1Iie
b|bHY*B?+5s^oC=K_$_lH;L}I86Y`dnphJdmM+GV?`u7*OCSp5#BI5=EqD(ebDrPTk-26NW&qvJ&{1edPYI|oy63H$WlKJ6wqO<I
=y(vi`?y+5%k?L9)y?hx_;tIR&LPs@7-;w2A^F!4Ix2P(+t(@rnO*!heW3jwkD<I1LJWG+u>$t2K7f}1HE-O*$0D%t*o!iix0(Xz
kuy!3rCkK0Z?Jl&^1dv9F^ZorK~|Qugx88Y$&Boz$2>D61w%0^jzOh5V%Yb)Z%=`EJ{;JZ8n`uNy3A#*cdt7FX&q!H+mns6s=B%R
=BZrV;6ky+s2*K2j4vf~;n{O1fjZsdL|M7w)XNa^wuOA9H%q^x+F!!!4zZmS#bl6v6UOFQ61K__h>qMWGY>{#x^<&wOM8=Hh*Fp1
G%ZdiTk00?-bP*5C^TUAH_j^HGqT??l0>qYqZmrE*S>J0IA0lFW}Y&#11d#f4>I;<m)IRMq4=86fD(4<0R}9*6+e)qw7q#&&BXji
R?}XNlu>gLn<?GGSH0#cGPY#_r`!6<j%h*X^5I4+^dM+vh2)^%d%JZ9@&psVsCJf!dNkpz`{f-E+^csO?CvkD1Vc=y&;wXKycShw
J9-kF!su0uJ3OrA`l_YA<6zbon<2*-@q<E;!#$HUMvyQ9gqsaIBsc`LZAWTEJn>VJ@=^kd?S|3#7EEMc$#t?Zn{$fdVZYt6p5hoD
P6kOU<0y4er;b!7+z4=j1KrK(u-X0*TNb?DcvMfAs#rp;I9lyE%wm+edkA6m$&KmYT*jbCb!Wm8xB-`aX-oz>VAGj}fA=Ce75lBn
f4ArI!EZ~AnM?2<T^?Ca`K#-S!zOCHyT88We*z6cja_>1;_%-UE?6mX%Xw_<?m}AUr{utjc<J#wO-eyM-WroZM&Z-1A_CI8GP;5%
NeCSfmHSl@(a*X>qS4=%=LEw{NwZziucB~0U5SrInR$Wbf&ei1RS}#wuC<D6WokBL)OJ=vHMb2dF~^$niS%WmQY*PlbYS~1TTYXc
Doid@wC#!%w;)N<%>s*}tC}x%rT2mg{()?nP6~QQ4Ui1MTI2tLEq$F*e~6_b-=P9Q!a2u-%^TgdDO>Mv5pL&Hqe(Zhw(>ih!4i9<
9@a2=k&H)m7ty+G&dzx{5C2MRa{KtY!P<C`6pTFM7Qwk0IZGRInsRV6dgOVMf|Oys@mm|Ko#<y-U0V|G6o_AXz)RMx8I?MaTO#Mj
5AdQiV5hmv#aJIbUTN>|Gb&?WtzOC^;eJN080F#~05RvNnJG0!Cj>cwQ&HkK!67K6JtWMXgMug_G1~w7T9hw4MKL<y5PUF3I%Moj
*#K8ONFod<fx+BTVU~)Lx=OCqCEhQ;?z#*pYn&p6{8!A+HjjtW3v2sXqPw8kD*X;)R_P)kYt6c_<GyNlKb;73)+9M*ge@3)*Ni0(
x6rKhw2iEPzizHRj>+>T$aHG;2C@eOPgEvQmKtYo>0`B(d`*|bJVpwrmVZy-&lZT3ryRTvl<0QEl%vfu3aNy+uKn41I$#~A(QJE6
Reohqy+(vg^p8LQ*E<Z$i!dOD6v$(l8=<H#=Ad9B%_*V42=E?sxu+OgNQrTF9bwwpjeEl$5?OiWW7Esfs^SG+a=kU@gLLjZJcpw;
!`g~B|0D=+RRBr|6ERg_h{Wp=Nf~KPqC7e3H9DflK;=NU`^iTUUMM+cE+?CCZ7BZNz4=W(z6tv}HlSEq*UlzQKg_JJ)Lq@AXT3aX
Fx9VC9VdUKa?F(J$syPgMbw<A%f=0R7P9i1Q9=}I+IMe4ifQtf2!Vn8-#&|*GkE8FCX82+6IEDQKz&NO(}CuX+HT0^p$R(HQwu`C
vI!EoJSp8>8Gtpv!mAd9hO;wt7r2^hWV{DsD<Fk>h#NulDk5gn$+5!qz{iOd?;Uk9Ft<S*rqtd!zCNy#)PEcl6M2U}{X!P4!C@oI
`3_@Y3ZUs-;Sr$11Xq9AZmoFQb&Q`hknQ+)MydPm9gSyFVL-Cdj2cczS_k5+NkxX7f&3@e%`7h7ac;JChdL4h4gBz5QVb=d$A7^s
o2H31YbOj1Tr%i|BsKjS^S`ZkWafb8aR2OhA0m%EIY=#)=K(Gl<XA(OQ2+ZU36qij#2vod?bhp~8kbs0yqR!CKX+!S|ARIeo_6EM
^bIWYj?$ZQqsZ+?m5}LsboFLnIG!ICI8#53mQeszlss$x&F3nB8Z3m_CEQ1*s5OL-%EVwfJyW<-n-lQR7LRxrh6i4eH~<PKCVlX;
wwD^4i%K2S!&D*9gHI>dx(Qb6r*678&*zfdKP46)9gq~*YwH5-M11jy0E~3nb6s>6$9ST$>2J(L`K!=gKSadeMI6F~+viX%OD~Z6
8AR^`I`%&m$^qo(+D1Em@R#@*a){9M#0PaednKZ5hZ&3adtpt?c*jX3z4EC6UT9cqQrfpYK20}5-E1$`hMV-%ajmAc5vk78yhB0A
wXpR6=aiwLM$c~!ZYq=ktK0SUo{|c_KN{LHe_inv5r@Ws)={PM+X~#_A8Cv3RAM8Lz{bPOgA(LO24ZY9ngnT3>7A{1uAHiz%=R;!
r29upl4@?Bagc|{vrR6RF8`(c8zXxIQc~(XA=#)8cq3`A{<So(%dAs++Ma(yT@$7>zqQ}vY}9V-l=D2~43Bn4(Nu{M9CbO9Npu}i
*cQ5V^h8IjCyIIOo$qt=<dJScT0o+Gh@9d_xnY!?)F<NN@`J&(hu^hP>us~&geD&!JojkHo!ocp+)W){gI<%6=ts}V*?<pZnerEy
4@7FfB2ZiT$^lTUb*94&Q|7Ag)X2;oPW}zOn=;86D}5%*`%?56q?z|d7r(TMOs4Naq$b{GW%Z!DIm1*I2MH(;SuiL;Sul5%6E;HY
8APSM)U2dkLsM2jbK+-<gVV&BVvyC-CEpp#QQCSg0!u3x_zu*96w0~1Da*a!X!cZu)$k~d|J#BAAjWyNr?@IYqp*N`Z@QA)&FF~^
b)*L)qM}MtVT>v+tlw#Y@f${*l^y)h|LvUv7dD8bE;%$PdWVt!_mmroDno>RR73Pr0Y=jd5(D)U;qyO8X56Ksg@$DTS&#uz+jz>B
lTU2i4AI2pu2zH~DNn~*0vcfzott~UA(&h0zBu|Q*FglfsDR5t8^PMb4w?gKLZ!;1?T|uS3xU?giWeTk1bJJ&R18Jddr)cG%ku8_
l(9JQZZN+Rq!Rw+n&sGmQh>n%;<sU9N$e1sus&M1fkj?2GOp7U=i3TEk12Vp0_#+;U!kQ~pP<?h(xuDCd3tMBoRF)JksDm5Z8Ike
dQ|Oi2<qtlPxCHnuhEG1!FSwKjiVEZuN|EEC5okl)z>Vv=^`M2!!SZoZdxnxM+Wo1YdtoxD)06gIxz{6Aoy%U22v1#3FA4s?$ev{
bx5M3-5ZU#pUY56MyYRTLYuWM)=M8Bz<+eY3CrT2l6DR?9~3a@C~lF*SP+W*#u<CvQ^Q@5A|(R^`D-*&ZNFTvpJ|t7ugpf;o=-d6
&2Iwcy?unpfb~=m!>(KYf#C2OO`;Y4Og-Ho;PbZh52nHj{mUDeWlyeurzkzc(D+_M64so4ZmV0yGhYjv2fUawlS4><+P^@Wq)<&L
7gS9vL90>DfOxx~mzBn~P(6WUB4)E{fl+ur;#I7=EqB9+#+XB`potuGCr*nkD(1J4A3AoH-q)qRAaFbc)}?SU96t%@xsD_&$Zont
@CKIV^x@j^d3*bCZu?Rz>ZKmH=v|PuRop43=S6GJWs+@%-baquXHAnnmPo+>fKjVawIzo)@32UbFwfA#z7F%R1oK+fb1zxsS|mU0
#+$65615)H;*46ui4}R%e3n=||InB2Id0W!T+|&2gv4I$=m5KP7&sc8;%t7afzL&yG5f3$4rV!b|KKkc_vJB<X)ax269O=2vW;j~
HMP1Dw}$mMpX7T@t!ODM0yu(9$EKdf`q>g>%brj}Ri;Z$A9YY33l0A(I42Lhz>p<B0Tp^NqjK5ab&g|xuks1ZkLfUdBWKbD!x4@;
Ye87U8l~rM%}z}ZP?SNfzy%AEo!W4Eo!vpBVHb`Wue#cAsl8Ikj)H!M&s$P;+7H}dH-_^4SOq;ISRPFFb;bYWH=>fE9sxas(Z2Qm
cZ|w?&d$f4e`fco=6+uNM%K~x!%gdLz*SI;LnzCT`trQ-3HI^KlyN?6(D&j}iVvuIbU;8S!Pl9bP+wisCA)g9)#!-{;X}6v;JoUD
(q?+ej*(fTxKVj0XGkST-_QM>?1T;zNd5h%K;CgeyBx_UkFAbh9yhu{e-}KD>3#>!&tCr$rTV+cIb=0L_?Hq&y&5mMi%##@0&p%b
ops<SqOUK6V*^d<qyLqr+Yt7*mf^HAhV&H(Y>10Xj+5gIGRE<H-OZ(QYU68_n792{c?`se<D}(*H53iJAp;3ZT0!iZD+mX<i+Mvm
AOv_@VFf2>LPDt21tu4oquzJIr$oYB^8WDCE&CtsJ&#D;Ymdelu3hiPK`MzjpS4U=7G^wJ))uZYl{hgwCuE7(SNJ$xmWCF4DnqZ$
uAv_FozNV3Z?Oqw)@{}+Qokcv!%#J-AG~NGU$~dP9sSx4B?_$;h59LOj))-N@Dvd+cWu~lm<C38hbn^?Z!)Ayet;NI&M{cGN^F-a
vGSW*_+{^)tr3I6*v(X?$vC9WbZCM>P25C|QLf*L1Rz@Kr<oQHWy7Cz9z>?h3$qKnGt1^w>TgXvoGYI>Moy))a<ObStqc(DbEz(X
s9uQQ{!BByK~4efTk7sTdq4QPu>bew4T=RE_MyGe(aT(EeYBxsn&&o=pIuNY@n}GKSC>!p{pbC3OQ9Q+uf2G-bTuYdb*dlSdIbC}
zAGn;FN1D`AqV`(iKa$!$Y$7~4Y9}KP3tscDiVo<1IMGo7`}oQ=7~P_6@uVnwY11=%fH;5StE6u?kaTPNpacVdgWJ#8+{7~WP~hU
pXW{FL*KawLT(d6LUM4{X@n!_y5&OApTU?qHy$z@Wgnh&V?~f_U*Z|^&#dBP@#P%B9En2w8J)Ap3!Hv8|LJW0==ESmHw5J@E_d+-
e9SlM0_QrLe0n0S;3{r}qm`pHlK8Rt3`8@B9;Auf2XBF-izrQ+dypZVjFoFv42~G3VUE#tiZccbFSW$DDUFFN+004`PzEJ|jOdo{
0v^v8_A>456L-|RTl2Cb=&T+Mso<S-c9dcoD(HT^pGp-3tSZIGbcBFCN7#eOdEf*nBvcW7orFdwVxX`@j%S=nUM1=SWFd<zx?mTo
F6A|M`7nk|RSc-}^Xwc+MI73AJoWACX)Gpu<RboCYF1iKmpk~2I2o$1^)hSSlg|CTc#Ej>bYj=9%cB(;4M3Xycx3jV(C&7I`+oFI
n33Ku!ii5P{CS-f<RJt}V;{@c(@^T|K6TsY)z9COPvj=(MjbzjZfMlcVTn8VD*>X3ZNv_En1fxP!2VR@niAiFJ4iI2wKPdDK$#bW
>BYLkKqwnI*Hcj<!3Uptb2N3n*%jm6p?*2&Gt-)n&LJ?|PK;&QZ2HIYVRE<>qn@VO@N3dh`9}gV)i<xkT4u^5gd{KUdPYXjuz;>C
Erjy28-D}Ql>@v`v~^5MM^k`WR^I;r|6E;>{7dPMK^wtEjOw_{ubb%iEEKlwx6O}})c-W=GM;M0iywJay0cIM)Kgw7eHTK)DM1xs
b`9t(ChkVwv3MmqFTOcSht3@z<rW89L3<6-&(>*iY6`;yWdN_y=HS{{=)X0^O1m@9#5hIXMit{>v!oStldSq~1MWyB9_(tsufdvz
_Jge~(*ffj3|CcVDAx){=0M4OUyXaKQ3ta+!C)GDjTjPnwnSFSVitwt|8#@sE~N6ycr&gNBO0<fojjsOk6j)A7^#s_)-!#YAzTU&
=|!%s6k8rAW2WOnjK<|%XK23rLk(~GWT?!d_8tx&LETeOiqrzuAt(exMRTObK7U!0Z2~o;kMo6KB^O|45=!R~B)`9uA;wHHRfCpX
9k5)m0g{K7x}LOT?g{{|z;$8J5m&t^W)^-Xg*-utZ~e(f)lUKt)pE;^(s_Nf@aJ%Rv2e!DHOY5kV%5j(G5sE6YNB*N*}GLBR#0M~
kB3Z4uA5f&pHoRhL9hM%f;|xv)4Tlsad#6KH%@a)K4mX@C<K`Cp4@9!yqyxluAxj@%UxeieEaQd1F^Y~C`7mxo?W*~JmpV5&r)gN
;__KgxIPggr}UbUiHH=`ce(`8OufHmcb9<CqTuuNcfW7H;ZFQEYBR<bN$AgYa_>`fE1<$0d|dU2_e<d9`5hnFu`A%LE!-?g3I5p_
i<>d^K>X_#re2|!^?|ku+wVqF`(o7Lz;uREnrIRuyi7XjI`DEl?^u2tZjk)JLG!Lti=M(L=uYv_C->zZD!8NFt%Lz0Pg;R#@OQ+i
KIy%Fb+a<8kF%ErOv3IO(f-AdMBU3Er_$$|19_CgTO?RL4IAmn?0bPn&`z^jJZZ>rP(aw}Clp#}x_7d}87}a8C2f|MIYW|=#t-JI
gHru0xbob9jWy2Ux2a~t?`1^D_EKd|VJXif1hndMnpfb8Y211%rWnx#z~VTB`%mMn6YxM%$|wYaBFN;(GR7`J07DC6Z_ky3s1H}1
8TK$A24fc;O(lP3LJK!bcsxUrv-6Kg&Gc#xE62R{FgD--BHIt82tIYYS1Q^CU1q;E_rGjvNSw|6;q+`%c3q-`<@m{$Da~&z;+Jkr
M?0Q_mFa6SyQU*cOzG{U#+a)RsT=xA06f|+APS$wvTvi$`~4?sdRYNbm6kNpVq?0OVeTq-$-iOik<nTOHsp+yQxIR$uN6=lbf<`?
00tSyoZMSt$`WanF{q@#LlwM01g7+(OsZo51x`Jk^;HsdLK-?n(%3@E8%8hCBBrhE;fL3*+6AN9LuBX3S-U+;GKcGsjOv9>PB)Lk
7*f$_u5FBqyYJ7T!O+>^3f^&a4n#+SEAFw~HJL^(g@xEIIlUtof5$8_i{h0kDenO9sMliZC6+1qRr0YB4Qxq!KDmERsBpDriU>Fd
jm#y!pJ15q?bI+%x)B|}k_;*yy}m(af6(7C;R)n(Jbef%oTi9IPuQfl2d+^(A>}=pt!=k+^3_9F_KGj}_yf9l`-~?aQs`z@l6*2K
_+ayCaJ|(}cD1HyaixAxgKZB@Do+epik;FiPtlS=;4M15GtTY(@7lT!*e0A7UiV^9ozh`NAApc{D&J^Xc%gRhPvtRa%$E>O;oXM`
&~s_u_|iADaP0~tms}D(`*SziVyofmYB4nGDsA~RJt?)SpoT3%6j^cRULhg{4pm3N9z28@^`7YGbsD%7^veKz>ltq9l!Xlz1C*{y
sZ5?9mi)a!-nr2bH66&?W)2X~#&CyKq_$+;^Y3q6n+Mr!x{Q^SM2@MoRsd_BSQsk3K2EY)OvK%ce9Zg$fshv|vsjj__(Ml6@2qi7
dbG_*g5&_Be?6)*{i-tXYZvP`;9-E<zQvDPfqiM-jPl35qGW8;M(%gkiduu9r9#Bi)jhlI^k=jBx>3{>8h{2xzk%;=-3B#8WWS|Z
6zXMZv_YA*Z}~V)GvEp!ci)Zu8z7z0mc)0xG4uU_zFTZf`jX!A<Z4lf$LxjOl1B2la<#6_$*+Juy|s`K_??2U(*Ql+gO9xPVs7^+
w86K0q|oooow+{%kDC4cUSqx?w{5ez%3n9)R`sm<0^_TPuF>Tajl{Yh(xs;1usQ*b%!%Mi;{r?FFu_3Wc!{G<lb=}7q$nd(hEL^S
`<51F9VHL)o%uJJp~XPhnn*qlSudkRuKs=@8ZBCms)M;PMse&h{1#H7C4;>KOt@H1O(k`!JaZdP2Xp7Ukh14SAeMp0xW}{nyl&nt
V??g*bCPGL6njmxax1Wb2fjACQr_StJmSSwaK6g`vpMhS1fiTP1Qa_PHTlT*icw@h>X`Hz=Vw@M`bha&{h+s#ws(chrwmTXpjJ3~
J-9`5cTWoYl-ODephcvHjqbxUw;FYYkV)Q*7o2i^`>`Iz_q?m*Tbb&H+QuQW^^otFA=s5L?StMg`iucix{csSX9R-b334>acouB<
)`5%j4J)EgV#k41JA`PjZO11oyRlwAlP`d4f7_Avz1l6~a7%k%!UZ6R{c;x6d=n%eURx)+742x|<FjNrd|u-4I#eEYVOnDKud5jK
Bi?53wz$N9;qL}p*-J;v5W(kdr{i4S(Ob4<w9BdI0mnj79!0G9rV8`^<l<MBh-=}nB89Ss8<RV!;CiJ_F1f(cfO~)VBw3vJH(V_%
D`c=s>p#3wm@U1NfQb$<kXm@4hYWS33Gn>wErD>?bZC+k)>|clAxf3fl0rKi2(-oQuRnX@5`aj%+0}?^hm{w)-%(VMl#;pUn9(B-
^h)cN@ncU_OYn~Qx8LiKe5E5o0jCJu9~8doP<XFG3NfvAJqiS<CmPgXMttPSY`i6<cY6p(iHw5`YPpT|q;ryaQp_%J>^m)IcFV$+
{EN}BUF2ff_Ey<sMQ)8-qFl1ev8i)MoD-EHwUmFvrlbz$yw>J`o@Es^_~Bf-Ocy*~U+UOnqoZF9qKvb?#^neJP^Gjtgac$V0!!o5
#7u1gM7~mA$l|jV0cs06@Euw#r=A{zz0j4T%~wd_%h*nH9*OUid_H*~w392d{0LWG$eSD_STzE8as8}+M(s54jip*<{vP7UsDh@S
@jT<l>b{aELet$)hy8j&T(%-0ZL$}T)pscD-5AtJ1e$>Dc{!-%HAV8K{zqp~=t>znp8M^iP`!A836j}(Hc1xCB<4?mXXt10lA&!0
kl0P>(0D2_dFd)_VP#PY63H@fOXf}k_?++wl}<_R&~iF5xSa`fe)NXIRK5OjiAeJ}%i{eb;z{@~TZDZXc*3OZvqInnWGK#E<l_gp
+wd0~fjFE?>*ezPM@-nsMy|T8x^%@&Y5Jo`@8BU-|K+{%t~Q-XqJ>XxXDIPbxGPNhBIOPUtb@5ZmF8Zpi|TQ3sl=YttVt;F!i8TS
ydm+dX!VDWc5H1T$P)oPh7+AE@wnMbZp#QvVVv8kW)Gv@-?m=mv+RG8l8T;XtY6P6X^?0EjPCJQ#p|Zs#`ie!Q98Bf!i$Dg&$j{>
$oOC5?*}cx;zdFgv;Dg?=?p;v{y^6bScjdAlN0`(wdDT$*LUyxa)Oh-ADO+Krp>7H+{)Ed|A<T8Ga_0{j+CEX9=K^)2a5te=rROE
pq8VxL0dzvMegxIVZQ(S!nNooG)@&7Lt#*%sd9wz6IW-NAO%xAx%OFGYf9&)<>1!aUiWOoT@vi<r}kck-w`VCQpHl)esnz)4Kh1<
kTn}e*KHzPG!1Al)kNtFM7A+5jtsT@_NHg}n8oC=3~Z}J%qK5-4AoAA|JzKCwEGxj0)f@)`gmDI@j9lJP%K9GCFxT4F<V1oq&D^<
xrj81lLI=GKLsi73k#TkOjq;6Y~vuUlkHnk)?7~y_j#a^i%rncVAXz53rnDNkZ8VaH}!JPpGItI5BZXC-FY_2rxsOC9@8=e%t8RN
yfXzFz~PqQr~8=GUj!t*L6jz5d;K|U_~aItw@n^fG{NEr1!VsA<Gn%+<O#+gTH;*%3j`U-^@|_QjwD8|ZP7I&Ta&8B`R)*LZVigl
p5o%2fpG%QjTsRfS=ID(s5_jqgt)fl=IC<@x@O6vK8w;&<04x&Sx|+`B$ZWIzI(xb5d3u&Pr_~m`bb>sN8Y|AE_Y63W8>4N`W7Ic
u1lzF3ZQQ}9kuYDqq)B&XtWMZ<V0$}l&|sy501+|`*=*jN3(%UQ9BXTz*!wdMjYYYNZn&)`v0~++voFLh0IWp@m-yy6;HOCly$49
obYq@ZSGFA9yTf$Cus=i5qsLpcZfsbM>xD&g-R^)6(2&zNNCB#dHk@*UTffkiUhGl*Rd1^;`6#grwts4GMQkj|G)Zo-<X4o(9{bt
QPa(+7a_8GfyXbcrdYFZR7-e|_<gsXCDwQe$4A6KA3;CG`EVqB&joSZ$A*&_U<v72OsOs3peyk&O4N@;<{b!=I&NQSK%(@vTNN$d
O`e`X35lU+KI=kgYt9cHs395sHi;_Hs#s~v2KHX=_<X)?gc36n%&%M28cF;!AxTC7z8j|+Mv;V}=9L;yaCx1z5YmAdX}NU}Ozwye
BIC&!_?_>m{42^M_pY_(>daL)lP*2nS<>7U5XR(OR6JDql4|1tqSz=U{94vDBnI^n4Fpp67-vmP^5}5Je!ks}rFIjk5YD2+Wn>`n
<bVB5Lyfslr_w@1r;>f20kErBNf&id9*bn{G6%qdK&cYvbf>If6zm1&EnxJ*?7@dh0syE7<Ka!#GKM9#98v^WZ}!xCd}FOGpK&u{
MuF`y9(`xLy`E=om&T?Pk~9ffng0()IIj+CXq1;7Eht#cMogIMc5Q&J-Zy^KDv*UuB7uYg=kNqEUM6fc@&%6bL$~V2nIB?5);IlG
aLXK40vkGpLIrY8iP8K?1C)N_-Xjxm+5&`C!gfv*t^HgE(g?AmgGuiW3>@bZ3~|C!ev@fxhIX-d2E?eC;YO%le(SxxfQoqK9}v7T
<GJoi6}3Kin8%Zl4B-C)-QvAaJ=?ZYxvAtUADyP#5Cvq6q`eu0Nhc{0^~^V`4*|cA1As7?+rr+3I^@vx^{tI?ZWEsNS(;s$d|aqm
5z%<2j#cFb1|Lte^TVL3{+jY@bvu44Zy8(uEGj*qGhXJM<6@r+GK8p=eM_?_E5OEX)!#vzkt$T8J-vLa9u+KJzG~SmzoI1Or^(By
M;%7hC6)A85g85gS`6;;y10Ip^sj^{Q<0(AxsDuA9W)TW?c-#Q6Pl=nuEiW<`)iBcMnU5hcwIH(;kN#R+T)BeQ?^3xHgi{{-SJs0
#xNl5Dm5!}SX*lv-|_UzF#=c3z9#@dL!}VK&oEUXKO+;$Ap$s^NXf|EsX1QAJq3*{Vq(%b4$@!81JaBYwZe#lAvpU{*r?b4XAoit
8Bl1iK)Z@FZz@)XHkEb`0iYw{wXeKU8VCbl)SgWkidfCmMnQ{j15Og+oob&oPtncDy{pWYqQUB$cx+si)NNy!l`bwLU-|#Pe2#{U
LkF`t;14A;w8UoN5TW(>XG+df-<M_VY{%3A)XSlhxsSM%a)Q_I!#N?Zb(U@aLhWmuvB}M@Vpx@7r6acjk?zK!dJq?b+Vbz$wlG+|
A&le*>}!?&Y)wC~PnWfC^88D0^-E|NXKms6=zCo*7-fhsAHh_x)6)cLlGWY?lBvs+aCmFBF#rGni1>8>Ds#Ka00EZ50q~#)$ET#G
vBYQl0ssI200dcD
"""
if len(sys.argv)!=2:raise SystemExit('python -B -S recover_projective_twocap.py fresh')
b=lzma.decompress(base64.b85decode(''.join(DATA.split())))
assert len(b)==118896 and hashlib.sha256(b).hexdigest()=='5f1e9adae012dd4782d6be84a78fa4327a634ac4f1d3a67ca756c704d654a2eb'
p=Path(sys.argv[1]);p.mkdir(parents=True,exist_ok=True);p=p/'projective_twocap.py'
if p.exists() and p.read_bytes()!=b:raise SystemExit('Refusing to replace different source')
p.write_bytes(b)
print('PROJECTIVE_TWOCAP_SOURCE_RECOVERED',len(b),hashlib.sha256(b).hexdigest())
```

Optional convenience copies: [autonomous source](sandbox:/mnt/data/projective_twocap.py), [exact report](sandbox:/mnt/data/projective_twocap.json), [source-only recovery capsule](sandbox:/mnt/data/recover_projective_twocap.py). The embedded capsule is sufficient without these links.
