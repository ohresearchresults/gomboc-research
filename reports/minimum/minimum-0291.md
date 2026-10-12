# minimum-0291

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# FULL_WEIGHT_NEGATIVE_PENCIL_TETRAHEDRAL_EXCLUSION_V1

## 1. Result and evidence boundary

There is an independent analytic exclusion with **the entire stack-weight triangle**, all positive base parameters, and the entire negative part of each maximal projective pencil. It is not restricted to a small neighborhood of the previously fixed stack weights.

The result covers a small-lateral-coefficient region of the full eleven-parameter chart. It does **not** enlarge the fixed numerical pencil at p=(1/5,2/5,3/5), q=(1/4,1/3,1/2), s=4/5. Those lateral coefficients are outside the new hypothesis. The new region instead allows all six lateral coefficients to vary independently subject to explicit relative bounds, all positive s, both independent stack weights over their full triangle, all beta in (0,1), and all a in (-1/s,0]. In particular, it includes the regular a=0 section and the outer a<0 sector absent from the original finite opposite-apex operation.

**Input-audit limitation.** I cannot attest to a complete new-file EOF audit in this execution. The new read attempts did not provide inspectable complete contents here. I have retained the literal chart formulas and the source excerpts supplied in the conversation, including the mandatory pencil-source correction, but I do not claim to have reconstructed or executed the new pencil/beta recovery package. The theorem below is a standalone analytic derivation from explicit convex hulls and actual tetrahedral volumes; it is not a computational descendant of those certificates. No new numerical cover, output hash, or cold execution is claimed.

The immediate accepted native parent remains `minimum-0288`, SHA-256 `1fb69ab6a025ffb6447da6c61bb868da91a9aff2245797c948bce580f97cad6b`. Its native deep-deficit theorem is not silently relabeled as a full-chart result. The relation needed for the new theorem is derived below.

## 2. Full-weight theorem

Use the full-chart coordinates

\[
B_0=(0,-\beta,0),\quad B_1=(0,1-\beta,0),\quad B_2=(0,0,1),
\]

\[
L_j=\frac{(-p_j,(B_j)_y,(B_j)_z)}{1+ap_j},\qquad
R_j=\frac{(q_j,(B_j)_y,(B_j)_z)}{1+(1-a)q_j},
\]

\[
S=\frac{(-s,\sum_j u_j(B_j)_y,\sum_j u_j(B_j)_z)}{1+as}.
\tag{1}
\]

Let P be the actual convex hull of these ten points, in the order

\[
(B_0,B_1,B_2,L_0,L_1,L_2,R_0,R_1,R_2,S).
\]

Fill P uniformly and subtract its actual volume centroid g.

### Theorem

Assume

\[
0<\beta<1,\qquad s>0,\qquad u_j\ge0,\qquad\sum_j u_j=1,
\]

\[
\boxed{
0<p_j\le\frac{s}{1024},\qquad
0<q_j\le\frac{\min(1,s)}{1024},\qquad
-\frac1s<a\le0.}
\tag{2}
\]

Then every physical SPD metric on the actual own-centroid body has at least **two strict unstable vertices**. More strongly, every complete weak rooted tree on its true vertices is impossible for every nonzero PSD matrix.

For u0,u1,u2>0 the body has the literal true 10/17/9 incidence of the full chart. The theorem also holds on the entire closed stack-weight triangle, including its facet-merging edges and vertex-loss corners, with the true features of the resulting body used in the mechanical interpretation.

For every selected complete rooted tree there are three of its true arrows, each with coefficient 1, such that

\[
\boxed{
-\sum_{\nu=1}^3
\operatorname{sym}\bigl((Y_{i_\nu}-g)(Y_{j_\nu}-Y_{i_\nu})^T\bigr)
\succ\frac5{128}\Sigma_P,}
\tag{3}
\]

where Sigma_P is the actual uniform covariance. Hence for every nonzero PSD M,

\[
\boxed{
\frac13\sum_{\nu=1}^3
(Y_{i_\nu}-g)^TM(Y_{j_\nu}-Y_{i_\nu})
<-\frac5{384}\operatorname{tr}(M\Sigma_P).}
\tag{4}
\]

The three weights are independent arrow-certificate coefficients, not adjustable volume masses or centroid-balanced source loads.

The numerical constant 1/1024 is a convenient rigorous sufficient bound. No optimality is asserted. The region is a small-lateral-coefficient region, but its stack weights are completely unrestricted and its negative projective pencil has no omitted horizon-near interval.

## 3. Actual realization and its weight-boundary features

Write T for the transverse triangle with vertices

\[
b_0=(-\beta,0),\quad b_1=(1-\beta,0),\quad b_2=(0,1).
\]

Its area is 1/2, and the transverse origin has barycentric coordinates

\[
o=(1-\beta,\beta,0).
\tag{5}
\]

First consider a=0. The left part before stacking is the actual prismatoid between the triangle x=0 and the graph

\[
x=-\sum_j p_j\lambda_j,
\qquad (y,z)=\sum_j\lambda_jb_j,
\quad\lambda_j\ge0,\quad\sum_j\lambda_j=1.
\]

The right part is the actual truncated cone toward the point (1,0,0). In its cone coordinates

\[
(y,z)=\sum_j r_jb_j,\quad r_j\ge0,\quad\sum_jr_j=1-x,
\]

the right cut is x<=sum_j q_j r_j. Its three cut vertices are exactly R_j in (1) at a=0.

The point S=(-s,sum u_jb_j) is beyond the left triangular cut plane because

\[
s-\sum_j u_jp_j\ge s(1-1/1024)>0.
\tag{6}
\]

For positive u it is strictly inside the three transverse side halfspaces. It is also inside every retained right-side halfspace: its transverse barycentric cone coordinates may be taken as u+s o, all nonnegative, and its negative x-coordinate satisfies the right cut inequality strictly. Thus exactly the left triangular cut facet is visible from S.

This proves the stated open incidence directly. Its outward maximal cycles are

```
F0=(0,3,4,1,7,6)
F1=(0,2,5,3)
F2=(0,6,8,2)
F3=(1,4,5,2)
F4=(1,2,8,7)
F5=(3,9,4)
F6=(3,5,9)
F7=(4,9,5)
F8=(6,7,8).
```

The true edges are

```
02,03,06,12,14,17,25,28,34,35,39,45,49,59,67,68,78.
```

There are four triangular facets, four quadrilaterals and one hexagon. No integration diagonal is used as a mechanical edge.

For a in (-1/s,0], apply the positive projectivity

\[
\Phi_a(x)=\frac{x}{1-ax_1}
\tag{7}
\]

to this a=0 hull. The smallest x-coordinate of the hull is -s, and 1+as>0, so its denominator is positive on the entire body. It maps every displayed vertex to (1), preserving convexity and all true incidences in the open weight triangle.

**Uniform density is not transported without correction.** The body in (1) is refilled uniformly. Its actual moments are computed from its transformed tetrahedra below. Equation (7) is used here to establish the geometric hull and incidence, not to claim that the old centroid or equilibrium census is preserved.

### Exact facet-merging edges of the weight triangle

When exactly one weight vanishes and the other two remain positive, ten true vertices remain, but two true facets merge:

```
u0=0: F3 and F7 merge; the edge L1--L2 disappears.
u1=0: F1 and F6 merge; the edge L0--L2 disappears.
u2=0: F0 and F5 merge; the edge L0--L1 disappears.
```

The resulting true f-vector is 10/16/8. For the first two cases, a quadrilateral and a triangle merge into a pentagon. For u2=0 the hexagon and a triangle merge into a heptagon. All other true facets persist. The strict inequality s>max p_j ensures that S remains beyond the old cut plane rather than falling into it.

At a vertex u_j=1 of the weight triangle, S and L_j lie on the line through B_j, and L_j is strictly between S and B_j. That label ceases to be a true vertex. These corners have at most nine true vertices; no ten-vertex claim is made there.

This distinction is important: a single zero stack weight generally merges facets **without deleting a vertex**. The proof below handles those edge boundaries directly and does not invoke the nine-vertex theorem on them.

## 4. Seven positive tetrahedra and a contained comparison tetrahedron

Put

\[
d_j=1+ap_j,\qquad e_j=1+(1-a)q_j,\qquad d_s=1+as,
\quad\Delta=s-\sum_j u_jp_j.
\]

All are positive in (2), including Delta. The actual body is triangulated by the following seven tetrahedra:

```
(B0,B1,B2,L2)
(B0,B1,L1,L2)
(B0,L0,L1,L2)
(S,L0,L1,L2)
(B0,B1,B2,R2)
(B0,B1,R1,R2)
(B0,R0,R1,R2).
```

Their positive six-volumes are, in the same order,

\[
\frac{p_2}{d_2},\quad
\frac{p_1}{d_1d_2},\quad
\frac{p_0}{d_0d_1d_2},\quad
\frac{\Delta}{d_s d_0d_1d_2},\quad
\frac{q_2}{e_2},\quad
\frac{q_1}{e_1e_2},\quad
\frac{q_0}{e_0e_1e_2}.
\tag{8}
\]

At a=0 these follow by direct determinants in the prismatoid, cap and right truncated cone. The positive projectivity changes a simplex determinant by the reciprocal product of its four vertex denominators; this gives (8) for all a in the stated interval. Thus the formulas compute actual uniform volumes after refilling, not the pushforward of the old probability measure.

Let D be the sum in (8). If C_l is the sum of the four vertex vectors of the l-th cell and Q_l the sum of their four outer products, the complete actual moment reconstruction is

\[
\operatorname{Vol}P=D/6,\qquad
 g=\frac{\sum_l w_l C_l}{4D},
\]

\[
\mathbb E_P YY^T=
\frac{\sum_l w_l(C_lC_l^T+Q_l)}{20D},\qquad
\Sigma_P=\mathbb E_P YY^T-gg^T.
\tag{9}
\]

These are the positive-cell identities also visible in the supplied chart source. fileciteturn92file0L9-L27

The actual tetrahedron

\[
T_* = \operatorname{conv}(B_0,B_1,B_2,S)
\tag{10}
\]

is contained in P. Its six-volume is s/d_s. It is full-dimensional throughout the complete weight triangle and every permitted a. It will be normalized affinely, not used as a substitute volume law.

## 5. Uniform volume excess throughout the negative pencil

Write epsilon=1/1024. From a>-1/s and a<=0,

\[
1-\epsilon\le d_j\le1,\qquad
0<d_s\le1,\qquad e_j\ge1.
\tag{11}
\]

The ratio of actual body volume to the volume of T_* is

\[
\frac{\operatorname{Vol}P}{\operatorname{Vol}T_*}
=\frac{d_sD}{s}.
\]

The three left-prism cells contribute at most

\[
\frac{3\epsilon}{(1-\epsilon)^3}.
\]

The cap contributes exactly

\[
\frac{1-\sum_j u_jp_j/s}{d_0d_1d_2}
\le\frac1{(1-\epsilon)^3},
\]

and the three right cells contribute at most 3epsilon, using q_j/s<=epsilon. Consequently the volume excess over the contained tetrahedron satisfies

\[
0\le\frac{\operatorname{Vol}P}{\operatorname{Vol}T_*}-1
\le\frac{1+3\epsilon}{(1-\epsilon)^3}-1+3\epsilon
<11\epsilon.
\tag{12}
\]

For the last bound, when 0<=epsilon<=1/16,

\[
(1+4\epsilon)(1-\epsilon)^3-1
=\epsilon(1-9\epsilon+11\epsilon^2-4\epsilon^3)\ge0.
\]

Hence the middle expression in (12) is at most 10epsilon+12epsilon^2, which is less than 11epsilon at epsilon=1/1024.

In particular the **actual** volume fraction q of P outside T_* obeys

\[
\boxed{q<11/1024.}
\tag{13}
\]

This estimate is uniform as a approaches -1/s. Individual unnormalized cell volumes may diverge there, but the ratio to the actual contained tetrahedron remains controlled. No positive distance from the projective horizon is assumed.

## 6. Affine regularization of the contained tetrahedron

Let an affine map send B0,B1,B2,S to the regular tetrahedral corners

\[
z_0=(1,1,1),\quad z_1=(1,-1,-1),\quad
z_2=(-1,1,-1),\quad z_3=(-1,-1,1).
\tag{14}
\]

Call the image body K. The regular tetrahedron has centroid 0, pairwise vertex distance sqrt(8), circumradius sqrt(3), and uniform covariance I/5. These follow from

\[
\sum_i z_i=0,\qquad\sum_i z_iz_i^T=4I
\]

and the exact uniform tetrahedral moment formula.

The affine map transports the actual uniform law, but K is **not assumed centered**. Its actual centroid will be bounded and subtracted.

Let U=sum_j u_j z_j and O=sum_j o_j z_j, where o is (5). Both lie in the regular base triangle. Denote r_j=p_j/s and h_j=q_j/s. Direct barycentric algebra in the tetrahedron (10) gives the following exact image formulas:

\[
L_j^{\rm reg}-z_j
=\frac{r_j d_s}{d_j}(z_3-z_j)
+\frac{r_j}{d_j}(z_j-U),
\tag{15}
\]

\[
R_j^{\rm reg}-z_j
=-\frac{h_jd_s}{e_j}(z_3-z_j)
+\frac{h_j}{e_j}(U-z_j)
+\frac{q_j}{e_j}(O-z_j).
\tag{16}
\]

These formulas explicitly account for the stack barycentrics. No bound depends on any u_j being bounded away from zero.

Because every distance appearing on the right is at most sqrt(8), (11), r_j<=epsilon, h_j<=epsilon and q_j<=epsilon imply

\[
\|L_j^{\rm reg}-z_j\|
\le\frac{2\sqrt8\,\epsilon}{1-\epsilon}<9\epsilon,
\]

\[
\|R_j^{\rm reg}-z_j\|
\le\sqrt8(2h_j+q_j)<9\epsilon.
\tag{17}
\]

Thus all uncentered vertices of K are within 9/1024 of their designated regular corner, in the groups

\[
G_0=\{B_0,L_0,R_0\},\quad
G_1=\{B_1,L_1,R_1\},\quad
G_2=\{B_2,L_2,R_2\},\quad G_3=\{S\}.
\tag{18}
\]

Every point of K therefore has norm less than sqrt(3)+9/1024<2.

### The actual centroid, not a prescribed one

The regular tetrahedron inside K has centroid 0. Decompose the actual uniform integral into that tetrahedron and its genuine complement. From (13),

\[
\|g_K\|\le2q<22/1024.
\tag{19}
\]

After subtracting this actual centroid, every group-i point is consequently within

\[
\boxed{31/1024<1/32}
\tag{20}
\]

of z_i.

The same actual decomposition gives

\[
\mathbb E_Kxx^T\preceq
\left[\frac{1-q}{5}+4q\right]I
\prec\left[\frac15+\frac{19}{5}\frac{11}{1024}\right]I
=\frac{1233}{5120}I\prec\frac14I.
\]

Subtracting g_K g_K^T only decreases the matrix. Hence

\[
\boxed{\Sigma_K\prec I/4.}
\tag{21}
\]

This is the true covariance of the actual image body. The contained tetrahedron is only used to bound it.

## 7. Complete three-arrow mechanical certificate

Consider a rooted tree on the four regular corners (14). For its three arrows set

\[
Q_0=\sum_{i\to j}\operatorname{sym}\bigl(z_i(z_i-z_j)^T\bigr).
\]

Up to an orthogonal permutation of the regular corners, the four rooted-tree types give the following complete literal matrices:

```
star, root at centre:
[[4,0,0],[0,4,0],[0,0,4]]

star, root at a leaf:
[[4,0,2],[0,4,2],[2,2,4]]

path, root at an endpoint:
[[2,-2,1],[-2,6,1],[1,1,4]]

path, root at an internal vertex:
[[2,0,1],[0,6,-1],[1,-1,4]].
```

Their leading principal minors after subtracting (5/8)I are, respectively,

\[
\begin{array}{c|ccc}
&\text{first}&\text{second}&\text{third}\\\hline
\text{star/centre}&27/8&729/64&19683/512\\
\text{star/leaf}&27/8&729/64&5859/512\\
\text{path/endpoint}&11/8&217/64&355/512\\
\text{path/internal}&11/8&473/64&9315/512.
\end{array}
\]

Every entry is positive, so

\[
Q_0\succ(5/8)I.
\tag{22}
\]

Now allow each source and target to be any centered actual point from the corresponding groups (18), with displacement at most r=1/32. Different arrows may use different actual points in one group. For a source z_i+v and target z_j+w,

\[
\left\|\operatorname{sym}\bigl((z_i+v)(z_i+v-z_j-w)^T
-z_i(z_i-z_j)^T\bigr)\right\|_{\rm op}
\le(2\sqrt3+\sqrt8)r+2r^2.
\]

Since 2sqrt(3)+sqrt(8)<13/2, the sum of three errors is less than

\[
3\left(\frac{13}{2}\frac1{32}+2\frac1{32^2}\right)
=\frac{630}{1024}.
\]

The regular lower bound is 5/8=640/1024. Therefore the actual three-arrow stress satisfies

\[
\boxed{Q\succ\frac5{512}I.}
\tag{23}
\]

Together with (21), this gives Q>(5/128)Sigma_K.

### Why no rooted alternative is omitted

Take any complete rooted tree on the true vertices of P. All four groups in (18) contain true vertices: the three Bj remain genuine corners at the join between the left and right portions, and S is the unique point with sufficiently negative first coordinate. This remains so on the closed weight triangle; at a weight corner only an intermediate Lj becomes redundant.

Contract the four groups and discard arrows staying within one group. Every group can still reach the root group, because each original vertex-to-root path gives a directed quotient walk. Any finite directed graph with that property contains an in-arborescence: at each nonroot group choose an edge decreasing its shortest directed distance to the root. The resulting three cross-group arrows are selected arrows of the original true tree.

They form one of the four regular rooted types used in (22), so their actual stress satisfies (23). Pairing with any nonzero PSD matrix is strictly positive, whereas all three forward weak arrows would make that pairing nonpositive. This is the contradiction.

The argument covers every complete tree rather than only a root fan or a chosen path. It does not need the groups to induce connected subtrees, and it does not identify an unproved highest-norm vertex with a selected parent.

For the open 10/17/9 graph, a finite support list may be recovered without any real coefficients: select three cross-group true edges whose group pairs form a spanning tree, orient them toward one of the four root groups, and give each coefficient 1. The cross-group multiplicities are 2,3,1,3,1,1 on the six pairs. The corresponding cofactor

\[
\begin{pmatrix}6&-2&-3\\-2&6&-3\\-3&-3&7\end{pmatrix}
\]

has determinant 80, yielding 320 rooted supports. This is the same finite tetrahedral-group certificate mechanism, now justified by the full-chart actual-volume bounds (12)–(20). At facet-merging or vertex-loss boundaries the quotient proof uses the boundary body's true edges; it does not freeze a triangulation edge as a physical feature.

Finally undo the affine regularization. Covariances and arrow matrices undergo the same congruence, while the physical matrix undergoes the reciprocal congruence. Thus (23) and (21) become (3) and (4) in the original chart coordinates.

## 8. Scope relative to the supplied full-beta pencil

This result retains **all beta in (0,1)** and the **entire stack simplex**, not only weights near (1/5,2/5,2/5). It also retains the whole interval (-1/s,0] in each of its pencils. Because s exceeds every p_j, -1/s is exactly that pencil's left endpoint. There is no omitted horizon collar and no physical conditioning cutoff.

The positive-a part

\[
0<a<1+1/\max_jq_j
\]

is not covered by this proof. There, the right vertices can no longer be uniformly assigned to their original base-corner groups by estimates (16)–(17). This is a concrete geometric obstruction to the present comparison, not evidence that a U1 metric exists there.

The new coefficient region does not contain the coordinator's fixed p=(1/5,2/5,3/5), q=(1/4,1/3,1/2), s=4/5. In particular, the largest p_j/s there is 3/4, rather than at most 1/1024. I therefore do not describe this as an enlargement of that fixed numerical rectangle or its nine-transverse tube. It is a separate full-dimensional actual-shape region in the full chart.

It is also not obtained by simply reusing the native eight-parameter deficit inequalities. The proof explicitly constructs the a=0 hull, applies the positive projectivity only for geometry, recomputes the seven actual cell volumes after refilling, and compares the resulting actual centroid with an included tetrahedron. The full-chart weights u are never fixed to native cut-face-centroid weights.

## 9. Mechanical and minimum consequences

For SPD M, if there were exactly one strict unstable vertex, every other true vertex would have a genuine incident weak escape. Each distinct weak arrow strictly increases quadratic norm, so choosing one exit per nonroot would form a complete rooted tree. Section 7 excludes it. Therefore U>=2, including arbitrary incidental weak contacts.

The proof is primal and unconditional on S. It already makes a joint S1/U1 metric impossible in the region. No independent polar relaxation is introduced: under any affine map with linear part A, the centered primal metric is A^(-T) M A^(-1), and the same-origin polar metric is exactly its inverse. Uniform volume centering of the polar is never assumed.

The covariance margin in (4) is specific to this shape region. It does not improve the accepted universal factor 41/5 or the global E17 spectral window. No attaining construction, whole-incidence exclusion, or canonical count subtraction is claimed. The global minimum bracket remains 34<=C_min<=622.

The weight-boundary conclusion is stronger than invoking the facet-count lower bound only at u_j=0: it excludes complete primal weak trees on those boundaries and throughout all positive weights in the region, with a uniform affine-covariant stress margin. Nevertheless, it does not show that the same weight boundaries of an arbitrary full-chart body are U2. The small-lateral-coefficient hypothesis is used essentially in (12) and (17).

## 10. Exact recovery data and verification limits

No numerical computation materially supports the new theorem. Its complete recovery data are literal:

1. Parameters: beta in (0,1), s>0, u in the closed probability triangle, p_j in (0,s/1024], q_j in (0,min(1,s)/1024], and a in (-1/s,0].
2. Ten vertices: formula (1), with the displayed fixed label order.
3. Actual seven-cell triangulation and its positive six-volumes: Section 4.
4. Actual centroid and covariance: formula (9).
5. Open-domain true facets and edges: Section 3; the single-zero merging rules and the weight-corner redundancy are explicitly identified there.
6. Comparison tetrahedron: (B0,B1,B2,S), sent in that order to the four integer vectors (14).
7. Stress selection: contract the four groups (18), choose a directed group in-arborescence from the selected true tree, and give its three actual arrows coefficient 1.
8. Matrix acceptance: the four complete integer matrices and their twelve shifted positive minors in Section 7, followed by the exact error bound 630/1024 and actual covariance bound 1233/5120<I/4.

These data require no downloaded coefficient array, optimizer, root isolation, parent program, or saved certificate. They constitute an analytic recovery capsule, not a claim of executed source-code verification. I do not supply a fictitious byte count, SHA-256, terminal PASS, or physical census for an unexecuted program.

The supplied numerical packages retain their own separate dependency obligations. In particular, any future computational descendant of the fixed-pencil/beta certificates must retain the mandatory correction from `visit(right,mid,hi,pending,depth+1)` to `visit(right,middle,hi,pending,depth+1)` in the original pencil source, together with both pencil materials and both beta materials. That patch is explicitly present in the available source excerpt; it has not been executed here. fileciteturn92file2L248-L269

## 11. What remains

The requested fixed-p/q broad weight triangle over the **entire maximal a pencil** remains undecided by this handoff. No actual full-tree SPD survivor was found or certified, and no failed finite stress library is being called feasible.

The new result proves an independent full-weight mechanical region and handles its facet-merging boundaries without a false nine-vertex shortcut. Its limitation is explicit: the tetrahedral-corner comparison requires the six lateral coefficients to be small in the stated relative sense, and it presently controls only a<=0. The useful next step is a different grouping or an independent-edge stress cover when the right cap becomes large in the positive-a sector, while retaining the actual common volume and complete rooted alternatives.

The incomplete new-file EOF audit remains an execution limitation of this handoff. No claim is made that this response completes the supplied numerical-package research program or reauthenticates the coordinator's existing certificates.
