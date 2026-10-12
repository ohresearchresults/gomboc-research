# minimum-0259

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# ORTHOGONAL_REFERENCE_OBSTRUCTION_5088862_AND_E17_FAMILY_V2

## 1. Main result

Write

\[
\mathcal U(P)=\inf_{C\succ0}\Upsilon_C(P),\qquad
\Upsilon_C(P)=\max_{w\in P,\ n\in P^\circ,\ w\cdot n=0}
(w^TC^{-1}w)(n^TCn),
\]

always at the specified origin. There is now a genuine **all-reference obstruction above 5**, not merely a covariance-gauge obstruction:

\[
\boxed{5.088862048<\mathcal U(P_0)
\le\frac{1392798627996514850352929}{273695497031792201468544}
<5.088862050.}
\tag{1}
\]

Here \(P_0\) is an explicitly given, uniformly filled, actual-centroid quadrilateral pyramid. It is an affine copy of the accepted parent's \(u=1/6\) control. The lower bound is an exact six-pair rank-one PSD dual. The rational upper reference is checked on **all 64 true primal/polar edge pairs**, including their interior orthogonality curves. Its exact factor is the middle rational number in (1). No local optimizer failure is used as evidence.

The obstruction persists beyond pyramids. There is an explicit simplicial triangular-bipyramid family with \(\mathcal U>5\), and, more importantly, an explicit continuous family \(P_\epsilon\) of actual **10/17/9** polytopes for which

\[
\boxed{5.08<\mathcal U(P_\epsilon)
\le\Upsilon_{C_0}(P_\epsilon)<5.094,
\qquad 0<\epsilon\le1/2000.}
\tag{2}
\]

Every body is separately centred at its own uniform volume centroid. Its true maximal face sizes are \(3,3,3,3,4,4,4,4,6\). This is not an H5 regional replay.

A general structural result accompanies the controls: **in dimension three, every optimal pure-factor reference has an exact optimality certificate supported on at most six active orthogonal pairs, with rank-one PSD multipliers**. For a polytope these pairs lie on true primal/polar edges, allowing vertices. The certificate gives precise equality conditions and a sufficient uniqueness criterion. This strengthens the source's finite-dual option into a necessary-and-sufficient finite critical-pair characterization.

No new universal upper bound below the accepted 8.97 is claimed. No new S1/U1 body, E17 exclusion, complexity improvement, or equilibrium census is claimed. In particular, the new E17 controls refute unconditional geometric factor bounds, not bounds that additionally impose S=U=1.

## 2. Input audit and lineage

I read the complete updated notebook through EOF, both new exact materials, and the complete literal parent payload. The unchanged finite-height, covariance, and intrinsic-reference sources remain available from the preceding turn and were retained rather than treated as missing archive references.

The new attachment bytes and SHA-256 values match the manifest:

- `SELF_POLAR_ORTHOGONAL_SHELL_AND_H5_HYBRID_V1.md`: 20167 bytes; `14c4a841bc3e3482a2e68b20110ccdc434ae3682bc2c5d51bfd3f00b769f93c8`.
- `ORTHOGONAL_REFERENCE_CONVEX_SUBLEVELS_V1.md`: 10127 bytes; `9558c1fd25a29027cabe1cd20b6ecd19abd6017c9330ae1200b408f231cf505f`.
- Updated `research-journal.md`: 325806 bytes; `665f804a540af16d6a47c74476301aaa20b200b84853eff41d1a5a411ec2859e`.

The immutable parent is `minimum-0257`, 35515 bytes, SHA-256 `021513490f20418bb9b9874eadd7521ca0ff54f04c9300bd35fddb0608fe53f7`. Its digest was verified by reconstructing the compact UTF-8 JSON envelope with keys `version`, `result_markdown`, `ensure_ascii=False`, separators `(',', ':')`, and a final LF in the Markdown string. The Markdown-only representation is 34824 bytes; the different counts are an envelope distinction, not a conflicting parent. Its embedded 10547-byte Python source also matches `ede99b2df3bff51b55b51c72d84008977dfdbf043141015a4ad874a35271eaf5`.

The governing source identities are retained: the factor is self-polar under the same origin and reciprocal reference, and changing C changes the transported physical matrix rather than the body or M. The fixed-U sublevels are linear matrix inequalities; this does not make the general mixed factor/angle objective convex.

No unavailable H5 program, historical archive object, or new external mathematical theorem is a dependency of the certificate below.

## 3. Six-active-pair theorem for optimal references

### Theorem

Let P be a full-dimensional compact convex body in \(\mathbb R^d\), \(d\ge2\), with 0 in its interior. Uniform density or centroid centring is not needed for this optimization theorem. Set \(m=d(d+1)/2\).

The infimum defining \(\mathcal U(P)\) is attained. At every minimizing reference \(C_*\), with \(U_* =\Upsilon_{C_*}(P)>0\), there are \(r\le m\) actual orthogonal pairs \((w_i,n_i)\), positive numbers \(\lambda_i\) summing to 1, and

\[
a_i=w_i^TC_*^{-1}w_i,
\quad b_i=n_i^TC_*n_i,
\quad a_i b_i=U_*,
\quad v_i=C_*^{-1}w_i,
\]

such that

\[
\sum_i\lambda_i\bigl(a_i n_i n_i^T-b_i v_i v_i^T\bigr)=0.
\tag{3}
\]

Consequently the rank-one matrices

\[
Z_i=\frac{\lambda_i}{a_i}v_i v_i^T,\quad
S=\sum_i Z_i\ne0,\quad
T=\sum_i(w_i^TZ_iw_i)n_i n_i^T
\]

satisfy the exact identity

\[
T=U_*S.
\tag{4}
\]

These at most m pairs have the same optimized value as the whole body:

\[
\mathcal U(P)=\min_{C\succ0}\max_{1\le i\le r}
(w_i^TC^{-1}w_i)(n_i^TCn_i).
\tag{5}
\]

In dimension three, \(r\le6\). For a three-polytope, all the active pairs used here lie on true primal/polar edges, with endpoints allowed. The theorem does not say that an arbitrary preselected six pairs suffice, or that six pairs evaluate the factor at every other reference.

### Proof

First, choose \(r_0B\subset P\) and \(\rho_0B\subset P^\circ\). Unit eigenvectors of C for its smallest and largest eigenvalues are orthogonal. The corresponding pair \((r_0e_{\min},\rho_0e_{\max})\) gives

\[
\Upsilon_C(P)\ge r_0^2\rho_0^2\operatorname{cond}(C).
\]

After normalizing \(\operatorname{tr}C=1\), any bounded-objective sublevel therefore stays away from singular matrices and is compact. The maximum defining the factor is continuous because its index set is fixed and compact. This proves attainment, as in the supplied existence argument.

By an origin-fixing reciprocal change of coordinates, take \(C_*=I\). For a fixed pair, the derivative of

\(f_{w,n}(C)=(w^TC^{-1}w)(n^TCn)\)

at I is the trace pairing with

\[
G_{w,n}=|w|^2nn^T-|n|^2ww^T.
\]

All these matrices have trace zero. The gradients of the active pairs form a compact subset of the \((m-1)\)-dimensional space of traceless symmetric matrices.

If 0 were outside their convex hull, finite-dimensional strict separation would give a traceless symmetric perturbation H that strictly decreases every active function to first order. The derivative is jointly continuous in the pair and C. Hence the decrease is uniform on a neighborhood of the active pairs. On the compact complement, the function values have a fixed gap below \(U_*\). A sufficiently small perturbation \(I+tH\) is positive definite, preserves the trace, and decreases the maximum over both parts. This contradicts minimality.

Thus 0 is in the convex hull of the active gradients. At most m gradients are needed: whenever a finite convex representation uses more than m points in an \((m-1)\)-dimensional affine space, an affine dependence permits changing its coefficients until one becomes zero, without changing the represented point. Repeating gives the claimed count. Removing zero coefficients gives positive \(\lambda_i\). Transforming back proves (3).

Since \(a_i b_i=U_*\), equation (3) gives

\[
T=\sum_i\lambda_i a_i n_i n_i^T
 =\sum_i\lambda_i b_i v_i v_i^T
 =U_*\sum_i\frac{\lambda_i}{a_i}v_i v_i^T=U_*S.
\]

For any C, let U be the maximum over these selected pairs. The rank-one equivalence gives

\[
UC-(n_i^TCn_i)w_iw_i^T\succeq0.
\]

Pairing with \(Z_i\), summing, and using (4) yields

\[
U\operatorname{tr}(CS)\ge\operatorname{tr}(CT)
=U_*\operatorname{tr}(CS).
\]

Here \(\operatorname{tr}(CS)>0\). Therefore \(U\ge U_*\), while \(C_*\) attains equality on every selected pair. This proves (5). It also shows that an **exact active-gradient balance is globally sufficient**, once the claimed all-pair upper value at C is established. Numerical stationarity without an exact identity remains only a locator.

For the edge assertion, an active pair has both vectors nonzero. Fix n. If w were not an extreme point of \(P\cap n^\perp\), strict convexity of \(w^TC_*^{-1}w\) would produce a larger value on that section, contradicting global maximality. Thus w is a section extreme point and lies on a true edge or vertex. Apply the same argument to n with w fixed. This includes nonsimple and nonsimplicial polytopes and does not introduce triangulation diagonals.

### Equality and uniqueness implications

Suppose \(C'\) is another minimizing reference. Every nonnegative trace summand in the preceding proof must vanish. For each positive multiplier,

\[
\bigl[U_*C'-(n_i^TC'n_i)w_iw_i^T\bigr]v_i=0.
\tag{6}
\]

In the \(C_*\)-whitened frame, \(z_i=C_*^{-1/2}w_i\) is therefore an eigenvector of

\(D=C_*^{-1/2}C'C_*^{-1/2}\).

If the \(z_i\) span \(\mathbb R^d\) and the graph joining i and j when \(z_i\cdot z_j\ne0\) is connected, all their eigenvalues are equal: nonorthogonal eigenvectors of a symmetric matrix cannot have different eigenvalues. Thus \(C'\) is a positive scalar multiple of \(C_*\). Without those hypotheses uniqueness is not asserted.

The rounded reference below is not asserted to equal \(C_*\); the theorem's equality conditions are not being inferred from numerical near-equalities.

A useful companion fact is symmetry averaging. If an orthogonal finite group preserves P, averaging the conjugates of a feasible C stays in the same fixed-factor sublevel, by its convexity. Thus an optimal group-invariant reference exists. For the control below, reflection in the first coordinate permits a block reference, but its lower certificate applies to **all** positive-definite C, including references not invariant under that reflection.

## 4. Actual prototype and its relationship to the covariance control

Let \(Q_0\) be the convex hull of

\[
R=(1,0,0),\quad L=(-1,0,0),\quad
T=(0,1,0),\quad B=(0,-1/6,0),\quad A=(0,0,1).
\tag{7}
\]

The quadrilateral base has cycle \((R,T,L,B)\). The other facets are the four actual side triangles. Thus the true f-vector is \((5,8,5)\).

The two actual tetrahedra \((R,T,B,A)\), \((L,T,B,A)\) partition the body and each has volume \(7/36\). Uniform integration gives

\[
V_0=\frac7{18},\qquad
g_0=(0,5/24,1/4),
\]

\[
\Sigma_0=
\begin{pmatrix}
1/10&0&0\\
0&41/960&-1/96\\
0&-1/96&3/80
\end{pmatrix}.
\tag{8}
\]

Set \(P_0=Q_0-g_0\). These are actual volume moments, not vertex averages.

For a tetrahedron with vertices \(a_0,a_1,a_2,a_3\), all moment calculations here use

\[
g_{\rm tet}=\frac14\sum_i a_i,\qquad
W_{\rm tet}=\frac{\sum_i a_i a_i^T+(\sum_i a_i)(\sum_i a_i)^T}{20}.
\tag{9}
\]

The mixing coefficients are the actual determinant volumes of the indicated disjoint cells, or actual removed and added volumes.

The parent's \(u=1/6\) pyramid maps to (7) by

\[
(x,y,z)\longmapsto(1-x-2y-z,x,z).
\]

Its linear determinant is 2; it maps the actual centroid to \(g_0\). After subtracting those true centroids, the change is origin-fixing. The third orthogonal pair below has covariance-gauge product exactly \(1053/172>6\), while its body's globally optimized factor obeys (1). Therefore the new result distinguishes covariance-gauge sharpness from reference-optimized sharpness quantitatively.

For completeness, under any invertible origin-fixing A,

\[
\Upsilon_{ACA^T}(AP)=\Upsilon_C(P),\qquad
\mathcal U(AP)=\mathcal U(P).
\]

The polar covector transforms as \(A^{-T}n\). If a physical metric is present, it transforms as \(A^{-T}MA^{-1}\); it is not reset to I.

## 5. Six literal pairs and the exact all-reference lower certificate

The poles of \(P_0\) are

\[
q_{\pm}=(\pm24/13,24/13,24/13),\qquad
r_{\pm}=(\pm1/2,-3,1/2),\qquad q_B=(0,0,-4).
\]

Let \(J=\operatorname{diag}(-1,1,1)\). Use the following three pairs and their reflected pairs \((Jw_i,Jn_i)\):

\[
\begin{array}{c|c|c}
i&w_i&n_i\\ \hline
1&(0,19/24,-1/4)&(19/13,6/13,19/13)\\
2&(13/48,25/48,-1/4)&(-24/13,24/13,24/13)\\
3&(1,-5/24,-1/4)&(-1/2,-3,1/2).
\end{array}
\tag{10}
\]

All satisfy \(w_i\cdot n_i=0\). Their membership is explicit: \(w_1=T-g_0\), \(n_1=(5q_++2r_+)/7\); \(w_2=(13R+35T)/48-g_0\), \(n_2=q_-\); \(w_3=R-g_0\), \(n_3=r_-\). Thus the first pair uses a true polar edge, the second a true primal edge, and the third actual vertices of the two bodies. Reflection supplies the other three pairs.

Define the complete PSD dual matrices by their exact rank-one factorizations:

\[
Z_i=k_i z_i z_i^T,\qquad Z_{i+3}=JZ_iJ,
\]

with

```
z1 = (0,          9704218318, -2414155513)
z2 = (1785496094, 8941375193, -4106557361)
z3 = (6687351908,-4477546045, -5935562810)
(k1,k2,k3) = (5337688699, 567023276, 4095288025).
```

There is **no omitted normalization** in these matrices. Their common scale is immaterial. They are optimization-dual multipliers, not weights assigned to the body's vertices or density.

Let S and T be the sums in the source's dual criterion. Put

\[
L_0=\frac{159026939}{31250000}=5.088862048.
\]

Exact multiplication gives

\[
T-L_0S=\frac{1}{380250000000}
\begin{pmatrix}
185033698774918486374756688644781&0&0\\
0&448125998546582215581363296292900&4513984110160077126026919369906\\
0&4513984110160077126026919369906&70875280544872879339212662194717
\end{pmatrix}.
\tag{11}
\]

This is visibly positive definite: the first diagonal entry is positive, the lower off-diagonal entry is positive, and each lower diagonal entry exceeds it. Equivalently, subtract that off-diagonal entry times \((0,1,1)(0,1,1)^T\); the remaining diagonal matrix is strictly positive.

For every C, the six pair inequalities give

\[
\Upsilon_C(P_0)\operatorname{tr}(CS)\ge\operatorname{tr}(CT)
>L_0\operatorname{tr}(CS).
\]

The optimum is attained, so \(\mathcal U(P_0)>L_0\). This is the lower half of (1). It is a complete all-reference obstruction, not the failure of a chosen optimization parameterization. The same matrices also certify \(T-(L_0+10^{-10})S\succ0\): its positive diagonal entries strictly exceed their row off-diagonal sums. This extra margin will give a literal E17 control above \(L_0\), rather than only a limiting supremum.

### Smaller nonrecord certificate

The same six pairs admit a much smaller certificate already proving \(\mathcal U(P_0)>101/20=5.05\). Use

```
z1=(0,4,-1), z2=(4,20,-9), z3=(9,-6,-8),
(k1,k2,k3)=(280,1,20), with the same reflection rule.
```

Then

\[
S=\begin{pmatrix}3272&0&0\\0&11200&-680\\0&-680&3282\end{pmatrix},
\]

\[
T-\frac{101}{20}S=
\begin{pmatrix}
13987601/60840&0&0\\
0&48605/338&261067/2028\\
0&261067/2028&10915181/60840
\end{pmatrix}\succ0.
\tag{12}
\]

The lower two-by-two determinant is \(56139787/6084>0\). This smaller, less precise certificate is retained as a reusable hand-checkable obstruction to factors 5 and 9/2.

## 6. Exact global upper reference for the prototype

Use the rational reference

\[
C_0=\frac1{10^{10}}
\begin{pmatrix}
10^{10}&0&0\\
0&3652685940&-408231944\\
0&-408231944&3124599586
\end{pmatrix}\succ0.
\tag{13}
\]

The exact factor is

\[
\Upsilon_{C_0}(P_0)
=R_0:=\frac{1392798627996514850352929}{273695497031792201468544}.
\tag{14}
\]

The first pair in (10) attains \(R_0\). The upper proof does not stop at the six selected pairs. It uses the supplied true-edge-pair reduction over the entire body and polar.

For each of the 64 edge pairs, write \(w=a+su\), \(n=b+tv\). The orthogonality relation is

\(A+Bs+ct+dst=0\).

On a nondegenerate feasible interval,

\[
t=-\frac{A+Bs}{c+ds},\quad
n=\frac{N_0+sN_1}{c+ds},\quad
N_0=cb-Av,\quad N_1=db-Bv.
\]

The verifier proves the quartic inequality

\[
R_0(c+ds)^2
-[(a+su)^TC_0^{-1}(a+su)]
 [(N_0+sN_1)^TC_0(N_0+sN_1)]\ge0
\tag{15}
\]

on every feasible interval. Breakpoints include 0, 1, the denominator zero, and the t=0 and t=1 points. Common linear factors are cancelled. Complete vertical fibers and the cases in which orthogonality is independent of t are checked at their appropriate endpoints, by convexity.

For a degree-d polynomial \(p(s)=\sum c_js^j\) on \([l,h]\), the source computes

\[
\widetilde c_j=(h-l)^j\sum_{k\ge j}c_k\binom{k}{j}l^{k-j},\qquad
b_k=\sum_{j\le k}\widetilde c_j\frac{\binom{k}{j}}{\binom{d}{j}}.
\]

Nonnegative Bernstein coefficients \(b_k\) certify (15). The actual execution covers **54 feasible intervals, 54 Bernstein leaves, maximum subdivision depth 0, and 122 endpoint/fiber checks**. Zero coefficients are allowed because (14) is an equality value, not an asserted strict all-pair bound. The largest checked endpoint value is exactly \(R_0\). All computations are rational.

The exact comparison \(R_0<101777241/20000000=5.088862050\) completes (1). The numerical minimizing reference itself has not been expressed as an exact algebraic object. Equation (13) is a certified near-minimizer, not an assertion of equality with the unknown exact optimizer.

## 7. Genuine nonpyramidal counterfamily

For \(\zeta>0\), replace B in (7) by

\[
B_\zeta=(0,-(1+\zeta)/6,-\zeta),
\]

and retain R,L,T,A. Denote the raw hull by \(Q_\zeta\), and subtract its actual centroid to obtain \(P_\zeta\).

The equatorial triangle \((T,B_\zeta,A)\) lies in x=0. The point 0 is in its relative interior, with barycentric weights

\[
\lambda_T=1/7,\quad
\lambda_B=6/[7(1+\zeta)],\quad
\lambda_A=6\zeta/[7(1+\zeta)].
\]

Thus the two tetrahedra with apices R and L form a genuine convex triangular bipyramid, with true f-vector \((5,9,6)\). Their equal actual volumes give

\[
V_\zeta=7(1+\zeta)/18,\qquad
g_\zeta=(0,(5-\zeta)/24,(1-\zeta)/4),
\]

\[
\Sigma_\zeta=
\begin{pmatrix}
1/10&0&0\\
0&(\zeta^2+6\zeta+41)/960&(3\zeta^2+10\zeta-5)/480\\
0&(3\zeta^2+10\zeta-5)/480&(3\zeta^2+2\zeta+3)/80
\end{pmatrix}.
\tag{16}
\]

For the four unchanged raw vertices, the centred displacement from \(P_0\) is \((0,\zeta/24,\zeta/4)\). For the changed vertex it is \((0,-\zeta/8,-3\zeta/4)\). Every pole of \(P_0\) evaluates each displacement in absolute value at most \(3\zeta\). Therefore, for \(3\zeta<1\), support-function comparison gives

\[
(1-3\zeta)P_0\subset P_\zeta\subset(1+3\zeta)P_0.
\]

The bilateral sandwich lemma proved next implies

\[
\mathcal U(P_\zeta)>
L_0\left(\frac{1-3\zeta}{1+3\zeta}\right)^2>5
\qquad(0<\zeta\le1/1000).
\tag{17}
\]

This is an actual continuous nonpyramidal obstruction, not only a limiting pyramid. The exact source independently audits the hull and moments at \(\zeta=1/1000\).

## 8. Whole actual 10/17/9 family

### Construction and true face lattice

For \(0<\epsilon<1\), cut both simple vertices R and L of \(Q_0\) by

\(x\le1-\epsilon\), \(x\ge-1+\epsilon\).

The two cuts are disjoint. Write

\[
r_T=(1-\epsilon,\epsilon,0),\quad
r_B=(1-\epsilon,-\epsilon/6,0),\quad
r_A=(1-\epsilon,0,\epsilon),
\]

and \(l_T=Jr_T,l_B=Jr_B,l_A=Jr_A\). The centroid of the right cut triangle is

\(c_R=(1-\epsilon,5\epsilon/18,\epsilon/3)\).

Stack the point

\[
s_\epsilon=(R+c_R)/2=(1-\epsilon/2,5\epsilon/36,\epsilon/6)
\tag{18}
\]

over that cut triangle. This point is outside its cut plane and strictly inside every other supporting halfspace of the cut body. It lies inside the tetrahedron actually removed from R. Thus only the right triangular cut facet is replaced, by three true triangular facets.

Use the literal vertex order

\[
(T,B,A,r_T,r_B,r_A,l_T,l_B,l_A,s_\epsilon).
\tag{19}
\]

The complete maximal facet cycles, valid throughout \(0<\epsilon<1\), are

```
(0,3,4,1,7,6)
(0,2,5,3)  (0,2,8,6)
(1,2,5,4)  (1,2,8,7)
(3,4,9)    (3,5,9)    (4,5,9)
(6,7,8).
```

Two simple-vertex cuts change \((V,E,F)\) by \((4,6,2)\); stacking changes it by \((1,3,2)\). Hence the result has true \((10,17,9)\). Its six-sided base and four quadrilateral side facets are maximal; no integration diagonals are counted as edges.

### Actual volume, centroid and covariance recovery

Let the raw body be \(Q_\epsilon\). The removed tetrahedra are

\((R,r_T,r_B,r_A)\), \((L,l_T,l_B,l_A)\),

each of actual volume \(v_\epsilon=7\epsilon^3/36\). The added tetrahedron is

\((s_\epsilon,r_T,r_B,r_A)\),

of actual volume \(v_\epsilon/2\). Therefore

\[
V_\epsilon=\frac7{18}\left(1-\frac34\epsilon^3\right),
\]

\[
g_\epsilon=
\left(
\frac{\epsilon^3(8-7\epsilon)}{8(4-3\epsilon^3)},
\frac{5(24-17\epsilon^4)}{144(4-3\epsilon^3)},
\frac{24-17\epsilon^4}{24(4-3\epsilon^3)}
\right).
\tag{20}
\]

Set \(P_\epsilon=Q_\epsilon-g_\epsilon\), not \(Q_\epsilon-g_0\).

Here is a complete compact recovery formula for the actual covariance at every parameter. Compute the raw tetrahedral second matrices \(W_R,W_L,W_s\) from the literal vertices above using (9). Then

\[
W_\epsilon=
\frac{V_0(\Sigma_0+g_0g_0^T)-v_\epsilon(W_R+W_L)
 +(v_\epsilon/2)W_s}{V_\epsilon},\qquad
\Sigma_\epsilon=W_\epsilon-g_\epsilon g_\epsilon^T.
\tag{21}
\]

This signed identity subtracts actual removed regions and adds an actual disjoint cap. It does not assign independent masses to overlapping cells. The program independently re-integrates the reconstructed maximal hull at \(\epsilon=1/2000,1/10000,10^{-12}\), and matches (20)-(21) exactly.

### Centred sandwich and all-reference bounds

Let \(d=g_\epsilon-g_0\) and \(D=4-3\epsilon^3\). The five original poles evaluate d as

\[
\frac{\epsilon^3}{D}
\left(
\frac{342-313\epsilon}{78},
\frac{54-61\epsilon}{78},
\frac{47\epsilon-48}{48},
\frac{89\epsilon-96}{48},
-\frac{18-17\epsilon}{6}
\right),
\tag{22}
\]

in the order \(q_+,q_-,r_+,r_-,q_B\). For \(0<\epsilon\le1/2\), \(D\ge29/8\), and each absolute coefficient is strictly less than 2. Thus

\(\pm d\in2\epsilon^3P_0\).

Before the centroid correction, the body contains \((1-\epsilon)P_0\) about \(\g_0\): shrinking the original pyramid by \(1-\epsilon\) about \(g_0\) satisfies both cuts. The stacked body stays inside the original pyramid. Adding the exact centroid displacement therefore gives

\[
a_\epsilon P_0\subset P_\epsilon\subset b_\epsilon P_0,
\quad a_\epsilon=1-\epsilon-2\epsilon^3,
\quad b_\epsilon=1+2\epsilon^3.
\tag{23}
\]

Both inclusions are about 0 after each body's own centroid has been subtracted.

For any two origin-containing bodies with \(aP\subset Q\subset bP\), the source's orthogonal-pair scaling argument and its reversed application give

\[
(a/b)^2\Upsilon_C(P)\le\Upsilon_C(Q)
\le(b/a)^2\Upsilon_C(P)
\quad\text{for every fixed C}.
\tag{24}
\]

Indeed, \((w/b,an)\) maps an orthogonal pair of Q into one of P. Interchange P and Q for the other inequality. Taking infima preserves both inequalities for \(\mathcal U\).

On \((0,1/2000]\), \(a_\epsilon/b_\epsilon\) decreases with \(\epsilon\). Exact rational evaluation at \(\epsilon=1/2000\), using (1), yields

\[
L_0(a_\epsilon/b_\epsilon)^2>127/25=5.08,
\]

\[
\Upsilon_{C_0}(P_\epsilon)
\le R_0(b_\epsilon/a_\epsilon)^2
<2547/500=5.094.
\]

This proves (2) on the entire parameter interval, not merely the audited samples.

There is also a literal E17 control reaching the prototype's displayed lower threshold. At \(\epsilon=10^{-12}\), the extra dual margin in Section 5 gives

\[
\mathcal U(P_{10^{-12}})>
(L_0+10^{-10})
\left(\frac{1-10^{-12}-2\cdot10^{-36}}{1+2\cdot10^{-36}}\right)^2
>L_0.
\tag{24a}
\]

The last inequality is checked exactly. This body has ten distinct rational vertices and the same nine true maximal facets; its volume and full covariance are independently audited in the source. Tiny features do not make it an unattained relaxation.

Moreover, (24) shows \(\mathcal U(P_\epsilon)\to\mathcal U(P_0)\). Consequently the supremum of the optimized factor over actual 10/17/9 bodies is **at least \(\mathcal U(P_0)>5.088862048\)**. Feature sizes tend to zero in this particular sequence. That is not a sequence of claimed joint S1/U1 bodies, and it does not contradict the minimum program's separate compactness results under mechanical hypotheses.

## 9. Physical finite-height consequence: same M, same inverse

For every \(P_\epsilon\) in (2), hold the auxiliary reference (13) fixed and put

\[
H=C_0^{1/2}MC_0^{1/2},\qquad
\mu_1\ge\mu_2\ge\mu_3>0.
\]

If a physical M had S=U=1, the accepted self-polar finite-height theorem would give

\[
\mu_1/\mu_2\le\Upsilon_{C_0}(P_\epsilon)f(10),\qquad
\mu_2/\mu_3\le\Upsilon_{C_0}(P_\epsilon)f(9),
\]

where \(f(m)=\cos(\pi/(2m))^{2m}\). The polar uses exactly \(H^{-1}\), by self-polarity; no polar volume-centroid assumption enters. The theorem admits nonnegative true escape arrows, so incidental weak contacts do not evade it.

Use the already certified strict trigonometric majorants \(p_0=7024915/10^6>9f(10)\), \(q_0=6832329/10^6>9f(9)\). Since \((2547/500)/9=283/500\), all such hypothetical joint metrics obey

\[
\frac{\mu_1}{\mu_2}<p=\frac{397610189}{100000000},\qquad
\frac{\mu_2}{\mu_3}<q=\frac{1933549107}{500000000},
\]

\[
\boxed{\operatorname{cond}(H)
<\frac{768798825875051223}{50000000000000000}
=15.37597651750102446.}
\tag{25}
\]

The coupled trace-one floors are

\[
\frac{H}{\operatorname{tr}H}
>\frac{50000000000000000}{1012153736575051223}I,
\]

\[
\frac{H^{-1}}{\operatorname{tr}H^{-1}}
>\frac{50000000000000000}{1017603920375051223}I.
\tag{26}
\]

The first is approximately 0.0493996101513107. With \(D=pq+q+1\) and \(\tau=\operatorname{tr}(C_0M)\), its original-frame form is

\[
D C_0MC_0-\tau C_0\succ0,
\]

and the corresponding ceiling is

\(pq\,\tau C_0-D C_0MC_0\succ0\).

The scalar trace-floor stress parameter is

\[
\alpha=1/(D-3)=
\frac{50000000000000000}{862153736575051223}.
\]

These are new necessary reference-window bounds for the entire constructed family, **not an exclusion obtained from them**. They are not bounds for the unchanged covariance-gauge H unless C is actually the covariance. The universal 47.677087 ceiling from the accepted 8.97 result remains the current global ceiling in that covariance gauge.

## 10. Universal limitation, uncertainty, and continuation

The optimized functional is affine invariant, self-polar, and continuous under centred homothetic approximation. Self-polarity follows by taking the infimum in the fixed-reference identity and replacing C by \(C^{-1}\). Continuity follows directly from (24).

There is also no unattained-singular-body issue for the universal optimized constant over all actual convex three-bodies. Normalize by the actual covariance so that \(\operatorname{Cov}(P)=3I/5\). The supplied covariance sandwich gives \(B\subset P\subset3B\). This class is compact in the Hausdorff topology: its support functions are uniformly bounded and uniformly Lipschitz, and their limits remain support functions with the same inner ball. Actual first and second volume moments converge by dominated convergence off the measure-zero convex boundary, so centring and covariance are retained. Continuity of \(\mathcal U\) then gives an actual maximizing body; each body's optimal reference is attained by Section 3. This is attainment among convex bodies, not a claim that a maximizing polytope exists in a fixed f-vector class.

Thus, if \(\mathcal U_3\) is the universal reference-optimized constant,

\[
\boxed{5.088862048<\mathcal U_3
\le47263586279502290403/5269120000000000000<8.97.}
\tag{27}
\]

The upper endpoint is the accepted covariance theorem, used by choosing C to be the actual covariance; it is not a new upper estimate. The same new lower obstruction holds for the supremum over actual 10/17/9 polytopes, by Section 8. Neither statement imposes S=U=1.

I tried symmetry-reduced frusta, quadrilateral pyramids, and actual tetrahedral-fan controls to locate an optimized-reference obstruction. The productive route was the parent's reflected \(u=1/6\) pyramid, followed by exact rational PSD rounding and a complete true-edge upper certificate. Numerical reference searches were used only as locators; the final recovery has no optimizer dependency, random seed, or numerical tolerance. No failed numerical search is being presented as an exclusion. The stronger radial-cone-volume upper problem has not been resolved in this continuation.

The exact optimizer of \(P_0\), the sharp value of \(\mathcal U_3\), and a body-extremizer classification remain undetermined. Equation (1) is a globally certified enclosure, not an exact algebraic solution for its minimizing matrix. The six-active-pair theorem reduces **reference optimality**, not the space of possible uniformly filled bodies.

The most useful continuation is to use the six-pair balance (3)-(4) together with actual uniform-centroid constraints to seek a universal upper theorem. Any proposed bound at or below 5 must now use an additional mechanical restriction or fail on the literal bodies above; the covariance counterexamples can no longer be dismissed merely as a poor choice of auxiliary reference.

## 11. Complete recovery capsule and verification status

The sole Python block below is the complete source `orthogonal_reference_obstruction_v2.py`, including its final LF. All vertices, exact dual factors, references, parameters, moment formulas, and verification helpers are contained in it. It imports only the standard library and **SymPy 1.14.0**. The tested interpreter is **CPython 3.13.5**. No originating sandbox, parent program, H5 program, or numerical-search state is required to reconstruct any new object.

Source: **15412 bytes**, SHA-256 `69aa9db755f2906421ad6a8fb6f965a5be2d22bd42219aebc093fc4aa859ae0a`.

Command, assertions enabled:

```
python3 orthogonal_reference_obstruction_v2.py > reference_report.out
```

Expected terminal marker:

```
ORTHOGONAL_REFERENCE_OBSTRUCTION_5088862_AND_E17_FAMILY_V2 PASS
```

Output: **19259 bytes**, SHA-256 `984cccba67645c7d8b7e0244d6c5e4a3567b0e433ad08b45668ccaac6c79eeea`.

The output includes both complete exact S/T matrices, both dual checks, the all-edge upper-certificate counts, all three literal E17 controls with full coordinates/facets/edges/volume/centroid/covariance, the bipyramid covariance, and the exact physical metric constants. The code generates the polynomial coefficients rather than depending on an external table. Its all-triples hull audit recovers true maximal facets independently of the stated construction and integrates an actual positive interior fan.

Normal execution and a source-only reconstruction extracted from this Markdown into a clean directory both passed with byte-identical source and output. This is an author replay, not an independent coordinator replay or proof-assistant formalization. The finite certificates and analytic proofs above are the mathematical evidence; the hashes identify their exact recovery units.

Convenience files: complete runnable source (`orthogonal_reference_obstruction_v2.py`), exact report (`reference_report.out`), and Markdown handoff (`result_markdown_v2.md`).

```python
#!/usr/bin/env python3
"""ORTHOGONAL_REFERENCE_OBSTRUCTION_5088862_AND_E17_FAMILY_V2.
Exact certificate; CPython 3.13.5 / SymPy 1.14.0; no external input or randomness.
Run with assertions enabled: python3 orthogonal_reference_obstruction_v2.py > report.json
The geometric proof and actual cut/stack interpretation accompany this source.
"""
import json
from itertools import combinations
from math import comb
import sympy as s

F = s.Rational
I = s.eye(3)
J = s.diag(-1, 1, 1)
LO = F(5088862048, 10**9)
HI = F(5088862050, 10**9)
C = s.Matrix([[1, 0, 0],
              [0, F(3652685940, 10**10), -F(408231944, 10**10)],
              [0, -F(408231944, 10**10), F(3124599586, 10**10)]])
RAW = [s.Matrix(x) for x in
       [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -F(1, 6), 0), (0, 0, 1)]]
G0 = s.Matrix([0, F(5, 24), F(1, 4)])
V0 = F(7, 18)
SIGMA0 = s.Matrix([[F(1, 10), 0, 0],
                   [0, F(41, 960), -F(1, 96)],
                   [0, -F(1, 96), F(3, 80)]])
PAIRS = [(s.Matrix([0, F(19, 24), -F(1, 4)]),
          s.Matrix([F(19, 13), F(6, 13), F(19, 13)])),
         (s.Matrix([F(13, 48), F(25, 48), -F(1, 4)]),
          s.Matrix([-F(24, 13), F(24, 13), F(24, 13)])),
         (s.Matrix([1, -F(5, 24), -F(1, 4)]),
          s.Matrix([-F(1, 2), -3, F(1, 2)]))]
ZROWS = [(0, 9704218318, -2414155513),
         (1785496094, 8941375193, -4106557361),
         (6687351908, -4477546045, -5935562810)]
WEIGHTS = [5337688699, 567023276, 4095288025]


def mat(M):
    return [[str(s.factor(x)) for x in M.row(i)] for i in range(M.rows)]


def minors(M):
    return [s.factor(M[:j, :j].det()) for j in (1, 2, 3)]


def pd(M):
    assert M == M.T
    out = minors(M)
    assert all(x > 0 for x in out)
    return [str(x) for x in out]


def tetra(a):
    z = sum(a, s.zeros(3, 1))
    return z/4, (sum((v*v.T for v in a), s.zeros(3)) + z*z.T)/20


def hull(v):
    """All supporting triples, then true maximal facets, edges, and poles."""
    o = sum(v, s.zeros(3, 1))/len(v)
    planes = {}
    for ids in combinations(range(len(v)), 3):
        a, b, c = [v[i] for i in ids]
        n = (b-a).cross(c-a)
        if n == s.zeros(3, 1):
            continue
        h = n.dot(a)
        vals = [h-n.dot(x) for x in v]
        if all(z <= 0 for z in vals):
            n, h, vals = -n, -h, [-z for z in vals]
        if not all(z >= 0 for z in vals):
            continue
        face = tuple(i for i, z in enumerate(vals) if z == 0)
        assert h-n.dot(o) > 0
        planes[face] = (n, h)
    faces = sorted(planes)
    edges = [ij for ij in combinations(range(len(v)), 2)
             if sum(set(ij) <= set(f) for f in faces) == 2]
    cycles = []
    for f in faces:
        neighbors = {i: sorted(j for j in f if tuple(sorted((i, j))) in edges)
                     for i in f}
        assert all(len(a) == 2 for a in neighbors.values())
        walk = [min(f), neighbors[min(f)][0]]
        while True:
            nxt = next(j for j in neighbors[walk[-1]] if j != walk[-2])
            if nxt == walk[0]:
                break
            assert nxt not in walk
            walk.append(nxt)
        assert set(walk) == set(f)
        cycles.append(walk)
    assert len(v)-len(edges)+len(faces) == 2
    for i in range(len(v)):
        normals = [planes[f][0] for f in faces if i in f]
        assert s.Matrix.hstack(*normals).rank() == 3
    vol = F(0)
    first = s.zeros(3, 1)
    second = s.zeros(3)
    for f in cycles:
        for j in range(1, len(f)-1):
            a = [o, v[f[0]], v[f[j]], v[f[j+1]]]
            mass = abs(s.Matrix.hstack(*[a[k]-o for k in (1, 2, 3)]).det())/6
            assert mass > 0
            gg, ww = tetra(a)
            vol += mass
            first += mass*gg
            second += mass*ww
    g = first/vol
    cov = second/vol-g*g.T
    q = [n/(h-n.dot(g)) for n, h in [planes[f] for f in faces]]
    dual = [ij for ij in combinations(range(len(faces)), 2)
            if len(set(faces[ij[0]]) & set(faces[ij[1]])) == 2]
    assert len(dual) == len(edges)
    for i, pole in enumerate(q):
        assert all(pole.dot(x-g) <= 1 for x in v)
        assert {j for j, x in enumerate(v) if pole.dot(x-g) == 1} == set(faces[i])
    return vol, g, cov, faces, cycles, edges, q, dual


def scalar(w, n, ref=C):
    return (w.T*ref.inv()*w)[0]*(n.T*ref*n)[0]


def bernstein(poly, lo, hi):
    p = s.Poly(poly, X)
    d = p.degree()
    if d < 0:
        return [F(0)]
    cc = [p.nth(j) for j in range(d+1)]
    aa = [(hi-lo)**j*sum(cc[k]*comb(k, j)*lo**(k-j)
                         for k in range(j, d+1)) for j in range(d+1)]
    return [sum(aa[j]*F(comb(k, j), comb(d, j)) for j in range(k+1))
            for k in range(d+1)]


X = s.symbols('X')


def upper_certificate(v, poles, edges, dual):
    inv = C.inv()
    cap = scalar(*PAIRS[0])
    assert cap < HI
    endpoint_values, leaves = [], []
    intervals = 0

    def check_point(w, n):
        assert w.dot(n) == 0
        z = (w.T*inv*w)[0]*(n.T*C*n)[0]
        assert z <= cap
        endpoint_values.append(z)

    def certify(p, lo, hi, depth=0):
        bb = bernstein(p, lo, hi)
        if min(bb) >= 0:
            leaves.append((depth, min(bb)))
            return
        assert depth < 24, 'Bernstein depth exhausted: NO certificate'
        mid = (lo+hi)/2
        certify(p, lo, mid, depth+1)
        certify(p, mid, hi, depth+1)

    for ie in edges:
        a = v[ie[0]]
        u = v[ie[1]]-a
        for je in dual:
            b = poles[je[0]]
            z = poles[je[1]]-b
            A, B, c, d = a.dot(b), u.dot(b), a.dot(z), u.dot(z)
            if c == d == 0:
                if B != 0:
                    x = -A/B
                    if 0 <= x <= 1:
                        check_point(a+x*u, b)
                        check_point(a+x*u, b+z)
                elif A == 0:
                    for w in (a, a+u):
                        for n in (b, b+z):
                            check_point(w, n)
                continue
            cuts = {F(0), F(1)}
            for aa, bb in ((c, d), (A, B), (A+c, B+d)):
                if bb != 0 and 0 < -aa/bb < 1:
                    cuts.add(-aa/bb)
            cuts = sorted(cuts)
            for x in cuts:
                den, num = c+d*x, A+B*x
                if den != 0:
                    t = -num/den
                    if 0 <= t <= 1:
                        check_point(a+x*u, b+t*z)
                elif num == 0:
                    check_point(a+x*u, b)
                    check_point(a+x*u, b+z)
            for lo, hi in zip(cuts, cuts[1:]):
                mid = (lo+hi)/2
                t = -(A+B*mid)/(c+d*mid)
                if not 0 <= t <= 1:
                    continue
                intervals += 1
                if d != 0 and A*d == B*c:
                    den = F(1)
                    nn = b-(B/d)*z
                else:
                    assert (c+d*lo)*(c+d*hi) != 0
                    den = c+d*X
                    nn = (c*b-A*z)+X*(d*b-B*z)
                ww = a+X*u
                p = s.expand(cap*den**2-(ww.T*inv*ww)[0]*(nn.T*C*nn)[0])
                certify(p, lo, hi)
    assert max(endpoint_values) == cap
    return {'exact_reference_factor': str(cap), 'true_edge_pairs': len(edges)*len(dual), 'feasible_intervals': intervals,
            'endpoint_checks': len(endpoint_values), 'bernstein_leaves': len(leaves),
            'maximum_depth': max(d for d, b in leaves),
            'minimum_bernstein_coefficient': str(min(b for d, b in leaves)),
            'largest_endpoint_value': str(max(endpoint_values))}


def dual_certificate(rows, weights, target):
    S, T = s.zeros(3), s.zeros(3)
    for (w, n), vv, k in zip(PAIRS, rows, weights):
        vv = s.Matrix(vv)
        Z = k*vv*vv.T
        assert k > 0
        for A in (I, J):
            ww, nn, zz = A*w, A*n, A*Z*A
            assert ww.dot(nn) == 0
            S += zz
            T += (ww.T*zz*ww)[0]*nn*nn.T
    return S, T, pd(S), pd(T-target*S)


def e17_raw(e):
    r = [s.Matrix([1-e, e, 0]), s.Matrix([1-e, -e/6, 0]),
         s.Matrix([1-e, 0, e])]
    l = [J*x for x in r]
    stack = s.Matrix([1-e/2, 5*e/36, e/6])
    return RAW[2:]+r+l+[stack]


def e17_moments(e):
    r, l = e17_raw(e)[3:6], e17_raw(e)[6:9]
    stack = e17_raw(e)[9]
    mr, wr = tetra([RAW[0]]+r)
    ml, wl = tetra([RAW[1]]+l)
    ma, wa = tetra([stack]+r)
    removed = F(7, 36)*e**3
    vol = V0-F(3, 2)*removed
    g = (V0*G0-removed*(mr+ml)+removed*ma/2)/vol
    raw_second = (V0*(SIGMA0+G0*G0.T)-removed*(wr+wl)+removed*wa/2)/vol
    return vol, g, raw_second-g*g.T


def main():
    assert s.__version__ == '1.14.0'
    pd(C)
    vol, g, sig, faces, cycles, edges, poles, dual = hull(RAW)
    assert vol == V0 and g == G0 and sig == SIGMA0
    assert (len(RAW), len(edges), len(faces)) == (5, 8, 5)
    v = [x-g for x in RAW]
    # Literal pair membership, including the reflection mates.
    for w, n in PAIRS:
        for A in (I, J):
            ww, nn = A*w, A*n
            assert ww.dot(nn) == 0
            assert all(q.dot(ww) <= 1 for q in poles)
            assert all(nn.dot(x) <= 1 for x in v)
    assert scalar(*PAIRS[2], ref=SIGMA0) == F(1053, 172)
    upper = upper_certificate(v, poles, edges, dual)
    S, T, sm, dm = dual_certificate(ZROWS, WEIGHTS, LO)
    fine_numerator = s.Matrix([
        [185033698774918486374756688644781, 0, 0],
        [0, 448125998546582215581363296292900, 4513984110160077126026919369906],
        [0, 4513984110160077126026919369906, 70875280544872879339212662194717]])
    fine_denominator = 380250000000
    assert T-LO*S == fine_numerator/fine_denominator
    assert fine_numerator[0, 0] > 0
    assert fine_numerator[1, 1] > abs(fine_numerator[1, 2])
    assert fine_numerator[2, 2] > abs(fine_numerator[1, 2])
    extra_gap = F(1, 10**10)
    extra_matrix = T-(LO+extra_gap)*S
    extra_gap_minors = pd(extra_matrix)
    assert all(extra_matrix[i, i] > sum(abs(extra_matrix[i, j])
               for j in range(3) if j != i) for i in range(3))
    Ssmall, Tsmall, unused, dsmall = dual_certificate(
        [(0, 4, -1), (4, 20, -9), (9, -6, -8)], [280, 1, 20], F(101, 20))
    expected = s.Matrix([[F(13987601, 60840), 0, 0],
                         [0, F(48605, 338), F(261067, 2028)],
                         [0, F(261067, 2028), F(10915181, 60840)]])
    assert Tsmall-F(101, 20)*Ssmall == expected
    assert expected[1:, 1:].det() == F(56139787, 6084)
    # A genuinely simplicial bipyramid at positive z, with actual fan moments.
    z = s.symbols('z', nonnegative=True)
    vv = RAW.copy()
    vv[3] = s.Matrix([0, -(1+z)/6, -z])
    g1, W1 = tetra([vv[i] for i in (0, 2, 3, 4)])
    g2, W2 = tetra([vv[i] for i in (1, 2, 3, 4)])
    gz = (g1+g2)/2
    covz = s.simplify((W1+W2)/2-gz*gz.T)
    assert gz == s.Matrix([0, (5-z)/24, (1-z)/4])
    for q in poles:
        for old, new in zip(v, [x-gz for x in vv]):
            coefficient = s.simplify(q.dot(new-old)/z)
            assert abs(coefficient) <= 3
    zz = F(1, 1000)
    bz = hull([x.subs(z, zz) for x in vv])
    assert (5, len(bz[5]), len(bz[3])) == (5, 9, 6)
    assert bz[0] == F(7, 18)*(1+zz) and bz[1] == gz.subs(z, zz)
    assert bz[2] == covz.subs(z, zz)
    assert LO*((1-3*zz)/(1+3*zz))**2 > 5
    # Exact symbolic actual-centroid identity for the cut/cut/stack E17 family.
    e = s.symbols('e', positive=True)
    ve, ge, se = e17_moments(e)
    expected_g = s.Matrix([e**3*(8-7*e)/(8*(4-3*e**3)),
                          5*(24-17*e**4)/(144*(4-3*e**3)),
                          (24-17*e**4)/(24*(4-3*e**3))])
    assert s.simplify(ve-F(7, 18)*(1-3*e**3/4)) == 0
    assert s.simplify(ge-expected_g) == s.zeros(3, 1)
    # On 0<e<=1/2: |q.(g_e-g0)| <= 2e^3; rational polynomial checks.
    shift_guards = []
    for q in poles:
        t = s.cancel(q.dot(ge-G0)/e**3)
        for p in (2-t, 2+t):
            num, den = s.fraction(s.factor(p))
            # Fix a common denominator sign, then certify on [0,1/2].
            if den.subs(e, 0) < 0:
                num, den = -num, -den
            nb = bernstein(num.subs(e, X), F(0), F(1, 2))
            db = bernstein(den.subs(e, X), F(0), F(1, 2))
            assert min(nb) > 0 and min(db) > 0
            shift_guards.append(str(min(nb)))
    em = F(1, 2000)
    a, b = 1-em-2*em**3, 1+2*em**3
    lower_family = LO*(a/b)**2
    upper_family = HI*(b/a)**2
    UF = F(2547, 500)
    assert lower_family > F(127, 25) and upper_family < UF
    tiny = F(1, 10**12)
    tiny_ratio = (1-tiny-2*tiny**3)/(1+2*tiny**3)
    assert (LO+extra_gap)*tiny_ratio**2 > LO
    controls = []
    for ee in (F(1, 2000), F(1, 10000), F(1, 10**12)):
        raw = e17_raw(ee)
        actual = hull(raw)
        av, ag, ac = e17_moments(ee)
        assert actual[0] == av and actual[1] == ag and actual[2] == ac
        assert (len(raw), len(actual[5]), len(actual[3])) == (10, 17, 9)
        assert sorted(map(len, actual[3])) == [3, 3, 3, 3, 4, 4, 4, 4, 6]
        pd(ac)
        controls.append({'epsilon': str(ee), 'vertices': [mat(x) for x in raw],
                         'volume': str(av), 'centroid': mat(ag), 'covariance': mat(ac),
                         'maximal_facets': actual[4], 'true_edges': actual[5]})
    # The trigonometric p0,q0 are inherited already certified majorants.
    p0, q0 = F(7024915, 10**6), F(6832329, 10**6)
    p, q = UF*p0/9, UF*q0/9
    D, Di = p*q+q+1, p*q+p+1
    assert p == F(397610189, 10**8) and q == F(1933549107, 500000000)
    assert p*q == F(768798825875051223, 50000000000000000)
    report = {'object': 'ORTHOGONAL_REFERENCE_OBSTRUCTION_5088862_AND_E17_FAMILY_V2',
              'pure_reference_lower_strict': str(LO), 'fixed_reference_upper_strict': str(HI),
              'reference_C': mat(C), 'reference_leading_minors': pd(C),
              'actual_parent_volume': str(vol), 'actual_parent_centroid': mat(g),
              'actual_parent_covariance': mat(sig), 'true_parent_facets': cycles,
              'small_dual_S': mat(Ssmall), 'small_dual_T_minus_101_over_20_S': mat(expected),
              'small_dual_gap_leading_minors': dsmall,
              'fine_dual_S': mat(S), 'fine_dual_T': mat(T),
              'fine_dual_gap_numerator': mat(fine_numerator),
              'fine_dual_gap_denominator': fine_denominator,
              'fine_dual_additional_gap': str(extra_gap),
              'fine_dual_additional_gap_minors': extra_gap_minors,
              'fine_dual_S_leading_minors': sm, 'fine_dual_gap_leading_minors': dm,
              'all_edge_pair_upper_certificate': upper,
              'bipyramid_covariance_polynomial': mat(covz),
              'bipyramid_1_over_1000_lower': str(LO*((1-3*zz)/(1+3*zz))**2),
              'centroid_shift_guard_minima': shift_guards,
              'E17_family_lower': str(lower_family), 'E17_family_upper': str(upper_family),
              'E17_tiny_control_lower': str((LO+extra_gap)*tiny_ratio**2),
              'E17_controls': controls,
              'finite_height_E17': {'U': str(UF), 'primal_gap': str(p), 'polar_gap': str(q),
                                    'condition': str(p*q), 'primal_trace_floor': str(1/D),
                                    'inverse_trace_floor': str(1/Di), 'stress_alpha': str(1/(D-3))},
              'exact_checks': 'PASS'}
    print(json.dumps(report, sort_keys=True, indent=2))
    print('ORTHOGONAL_REFERENCE_OBSTRUCTION_5088862_AND_E17_FAMILY_V2 PASS')


if __name__ == '__main__':
    main()
```
