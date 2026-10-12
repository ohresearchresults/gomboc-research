# minimum-0279

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# E17_ACTUAL_CENTROID_FLOW_BLIND_CONE_V1

## 1. Main result: an exact obstruction to a natural volume-to-tree coupling

The degree-six incidence polynomials suggest a natural mechanical certificate: integrate nonnegative spatial multipliers against the **one actual volume law**, obtain nonnegative centroidal vertex loads, and send those loads along a proposed complete rooted tree. This continuation determines the exact strength of that construction and proves that it loses essential edgewise information.

**Theorem A — higher polynomial degree does not strengthen this construction.** For a fixed actual centered polytope and a fixed true-edge rooted tree, the closure of all polynomially weighted, centroid-balanced subtree stresses is exactly the finite cone obtained from all nonnegative vertex representations of the actual centroid. In dimension three, these representations have extreme supports of at most four vertices. For ten vertices, at most 210 basic representations suffice. Increasing the polynomial degree, or retaining all of the parent's actual-volume flux identities, cannot enlarge this particular stress cone at a fixed actual shape.

**Theorem B — an actual E17 separation.** A new rational uniformly filled 10/17/9 control and the literal rooted shape TREE410 satisfy

\[
\boxed{Q=-2A_{12}-6A_{25}-A_{39}-A_{60}\succ0,}
\tag{1}
\]

where \(A_{ij}=\operatorname{sym}(X_i(X_j-X_i)^T)\) and \(X_i\) are centered at the control's **actual volume centroid**. Consequently the complete selected tree is impossible for **every nonzero PSD metric**, including every SPD metric and every weak-arrow boundary.

Nevertheless, there is a closed six-dimensional physical metric cube on which **every** normalized centroid-balanced subtree aggregate has strictly positive total arrow work, greater than \(1/4\). This holds for every admissible polynomial multiplier at every degree, not merely a finite moment truncation. Every metric in the cube has actual-covariance adjacent eigenvalue ratios **below 6**, condition number **below 36**, and both normalized primal and inverse eigenvalue floors **above \(1/43\)**. The proposed root is the unique global quadratic-norm maximum. A designated actual facet is strictly stable under the same inverse metric.

Thus the obstruction is not caused by forgetting the actual centroid, using a formal endpoint law, violating the inherited universal spectral window, or selecting a spurious root. It is caused by an unnecessary restriction on the allowed certificate coefficients.

The actual control has strict census \((S,U,H)=(3,5,6)\), weak000, throughout the metric cube. It is **not** a feasible weak tree or a 110 body: (1) excludes the selected tree outright. The result separates an aggregation method from the complete physical obligations it is intended to test.

An important limit is also preserved: the complementary **dual** tree is not blind on this control. An explicit same-origin pole circuit rejects the entire metric cube. Therefore this is **not** a counterexample to simultaneous primal-plus-dual centroid-flow testing.

No new universal orthogonal factor, whole-E17 exclusion, catalogue subtraction, or attaining upper example follows. The accepted \(\Upsilon_\Sigma<41/5\), E17 condition ceiling below 40, and global bracket \(34\le C_{\min}\le622\) remain unchanged.

## 2. Input authority and reading status

The new journal was read consecutively through EOF: **2240 lines, 369164 bytes**, SHA-256

`18c250406334a6db9271476d62e9f0096609be2a58804bbcc5df1bb8d628ca8d`.

The entire coordinator archive was read, including both complete programs: **30923 bytes**, SHA-256

`272046ff1cc2a729826b0c0fe2c09354c6e5c19d2bcfe4222b166e295a3ae908`.

The literal parent is **minimum-0276**, SHA-256

`08ba2642537a354443744c217de7b00b23a5e4e61bea4a3ea0f2931e867f36c0`.

Its compact UTF-8 version-2 JSON envelope reconstructs to **58506 bytes** with that digest when the literal Markdown retains its final LF. No new source-authority conflict was found. The older correction remains: the accepted probe tuples are ordered as \((\theta,\eta)\), not \((\eta,\theta)\).

The coordinator's result that all visible-coordinate projectivities preserve the projected nonconcave countercontrol is accepted as supplied. No further projected-probe search or duplicate profile-Hessian verification is used here. The new control is full spatial **uniform volume**, not that projected countermeasure.

Earlier unchanged evidence is retained. The new recovery program is standalone: it requires no inaccessible archive, parent program, saved moment table, or originating sandbox. “Centroid-balanced” below describes an auxiliary stress construction, never a replacement physical mass distribution.

## 3. Actual incidence polynomials and complete-tree work

Let \(P=\operatorname{conv}\{X_0,\ldots,X_{n-1}\}\subset\mathbb R^d\) be full-dimensional and translated so its **uniform volume centroid is 0**. Write \(\mu=dx/\operatorname{Vol}P\). Fix a tree on genuine edges, directed to root r, with parent \(p(i)\) for each \(i\ne r\). Put

\[
A_i=\operatorname{sym}\bigl(X_i(X_{p(i)}-X_i)^T\bigr),
\qquad D_i(M)=\operatorname{tr}(MA_i).
\tag{2}
\]

The complete weak packet is \(D_i(M)\ge0\) for **all** \(i\ne r\), with one common metric. For SPD M, every distinct weak arrow strictly increases quadratic norm; no strict-arrow assumption is inserted.

For each source k define its path tensor and cumulative work

\[
T_k=\sum_{i\text{ on the path }k\to r}A_i,
\qquad s_k(M)=\operatorname{tr}(MT_k),
\quad T_r=0.
\tag{3}
\]

The polytope of nonnegative representations of the actual centroid is

\[
\mathcal C(P)=\left\{\lambda\in\mathbb R^n_{\ge0}:
\sum_k\lambda_k=1,\quad\sum_k\lambda_kX_k=0\right\}.
\tag{4}
\]

For \(\lambda\in\mathcal C(P)\), let \(m_i(\lambda)=\sum_{k\in\operatorname{Desc}(i)}\lambda_k\). Interchanging the finite sums gives

\[
\sum_{i\ne r}m_i(\lambda)D_i(M)
=\sum_k\lambda_k s_k(M)
=\operatorname{tr}\left(M\sum_k\lambda_kT_k\right).
\tag{5}
\]

Therefore

\[
Q(\lambda)=-\sum_k\lambda_kT_k\succ0
\tag{6}
\]

excludes the complete tree for every nonzero PSD M. This is the centroid-subtree mechanism already recorded in the notebook. The new results determine its full polynomial closure and demonstrate its strict inadequacy on an actual first-layer control.

For the parent's true-incidence polynomials, write the actual facets as \(\ell_f(x)=h_f-n_f\cdot x\ge0\). At each vertex choose a fan of its true polar face and set, in dimension three,

\[
w_i(x)=\sum_{\tau\text{ in that fan}}
|\det(n_{\tau_1},n_{\tau_2},n_{\tau_3})|
\prod_{f\notin\tau}\ell_f(x),
\qquad W(x)=\sum_iw_i(x).
\tag{7}
\]

When F=9 these have degree at most six, are positive in the interior, nonnegative on P, and satisfy

\[
\sum_iw_i(x)(X_i-x)=0,
\qquad
\mathcal E_{X_i}(w_i\phi)=0,
\quad
\mathcal E_a(\phi)=\mathbb E_\mu[\phi+(x-a)\cdot\nabla\phi/3].
\tag{8}
\]

These are genuine same-volume identities, including at nonsimple vertices. The polar in their derivation is auxiliary geometry, not a newly centered uniform body. The complete parent proof supplies (7)–(8). The connection to the literature on Wachspress polynomial coordinates is background, not a priority claim for those coordinates.

## 4. Exact polynomial-flow closure

Let \(w_i\) be any continuous nonnegative polynomial system, positive in the interior, satisfying the first identity in (8). This includes (7). For every polynomial \(h\ge0\) on P satisfying

\[
\mathbb E_\mu[hW]=1,
\qquad \mathbb E_\mu[hW x]=0,
\tag{9}
\]

define

\[
\lambda_i(h)=\mathbb E_\mu[h w_i],
\qquad
m_i(h)=\mathbb E_\mu\left[h\sum_{k\in\operatorname{Desc}(i)}w_k\right].
\tag{10}
\]

Every integral is against the **unchanged actual uniform law**. The function h is a test multiplier, not a physical refill or independently fitted mass law. The centroid condition in (9) is essential: dropping it describes a different, larger certificate family.

### Theorem A

The closure of \(\{\lambda(h):h\text{ satisfies (9)}\}\) is exactly \(\mathcal C(P)\). Consequently the closure of the associated normalized stress set is exactly

\[
\left\{-\sum_k\lambda_kT_k:\lambda\in\mathcal C(P)\right\}.
\tag{11}
\]

In dimension three this is the convex hull of stresses from centroid representations supported on at most four true vertices. Ten vertices require at most \(\binom{10}{4}=210\) basic representations, including degenerate supports through zero basic coordinates. An integrated polynomial-flow stress is positive definite at some finite degree **if and only if** some \(Q(\lambda)\) in (6) is positive definite.

### Proof

Positivity, normalization and linear precision immediately give

\[
\lambda(h)\in\mathcal C(P),\qquad
\sum_i\lambda_i(h)X_i=\mathbb E[hWx]=0.
\]

For the converse put \(b_i(x)=w_i(x)/W(x)\) in the interior. These are nonnegative barycentric coordinates. They interpolate each vertex in the limiting sense. Choose a linear functional exposing \(X_j\) uniquely. Then

\[
\sum_{i\ne j}b_i(x)[\ell(X_j)-\ell(X_i)]
=\ell(X_j)-\ell(x)\longrightarrow0
\quad(x\to X_j).
\]

Thus \(b_j(x)\to1\) and the other \(b_i(x)\to0\). No nonzero value of W at a nonsimple boundary vertex is required.

Choose an affine \(t_j\) strictly positive on P, at most 1, and equal to 1 only at \(X_j\). The probability measures

\[
d\nu_{j,N}=\frac{W(x)t_j(x)^N}{\mathbb E_\mu[Wt_j^N]}\,d\mu(x)
\]

converge weakly to \(\delta_{X_j}\). Outside any neighborhood of \(X_j\), \(t_j\le a<1\); inside a smaller neighborhood there is a positive-volume interior set on which \(t_j>b>a\) and W is positive. The ratio of exterior to interior integrals tends to zero. Hence their means \(z_{j,N}\to X_j\), and \(\mathbb E_{\nu_{j,N}}b_i\to\delta_{ij}\).

First take \(\lambda\in\mathcal C(P)\) with every coordinate positive. Select d+1 affinely independent vertices. The corresponding d+1 columns of the matrix with columns \((1,z_{j,N})\) are invertible for large N. Correct only those d+1 coefficients of λ to obtain positive coefficients \(c_{j,N}\to\lambda_j\) satisfying

\[
\sum_jc_{j,N}=1,\qquad \sum_jc_{j,N}z_{j,N}=0.
\]

Then

\[
h_N(x)=\sum_j\frac{c_{j,N}t_j(x)^N}{\mathbb E_\mu[Wt_j^N]}
\]

is a positive polynomial satisfying (9), and \(\lambda_i(h_N)\to\lambda_i\). For a boundary λ, first mix it with the strictly positive centroid representation \(b(0)\), then let the mixing parameter tend to zero. This proves the closure assertion.

The matrix of constraints in (4) has rank d+1. Every extreme point has at most d+1 positive coordinates; a smaller independent support extends to a full basis. In dimension three this is a four-column basis. Linear images preserve convex combinations. Positive definiteness is open, so approximation in (11) proves the finite-degree equivalence. No finite-order physical moment-realizability assertion is used.

### Consequence for full flux

Within this construction, adding more equations \(\mathcal E_{X_i}(w_i\phi)=0\) cannot make the resulting edge coefficients leave (11). They remain subtree sums of the same nonnegative centroidal loads. This does **not** say that full spatial flux is useless. Its use solely through (9)–(10) discards its additional information at a fixed actual shape. The theorem does not limit using flux to constrain varying realizations or eliminate nonphysical moment sequences.

## 5. Finite affine dual and the missing sign condition

For a fixed physical M, finite-dimensional linear programming gives

\[
\min_{\lambda\in\mathcal C(P)}\sum_i\lambda_i s_i(M)
=\max_{\gamma,b}\left\{\gamma:
 s_i(M)\ge\gamma+b\cdot X_i\text{ for every }i\right\}.
\tag{12}
\]

Both sides attain their values. The primal polytope is nonempty and compact, and the affine constraints have full rank. An explicit positive γ and affine b therefore prove failure of **all** centroid-balanced subtree stresses at once, not just a selected set of polynomial tests.

There is an exact alternative: no positive-definite stress exists in (11) if and only if some nonzero PSD M admits an affine lower bound in (12) with \(\gamma\ge0\). Separate the finite cone generated by (11) from the open positive-definite cone. Its separating functional is a nonzero PSD M; (12) supplies the affine bound. The reverse implication follows by pairing M with a proposed stress.

The restriction is visible directly in the source loads:

\[
\lambda_i=m_i-\sum_{j:p(j)=i}m_j\ge0\quad(i\ne r),
\qquad
\lambda_r=1-\sum_{j:p(j)=r}m_j\ge0.
\tag{13}
\]

Nonnegative **arrow-certificate multipliers** need not obey (13). They are auxiliary dual coefficients, not volume masses. The four-arrow stress below has negative source differences at two vertices although every arrow multiplier is nonnegative. Requiring a nonnegative physical-load interpretation of those coefficients would incorrectly forbid a valid mechanical certificate.

## 6. Literal actual-body control and complete TREE410 packet

Define an eight-parameter labeled construction. Begin with

\[
B_-=(-1,0,0),\quad B_+=(1,0,0),\quad
B_0=(0,-b,0),\ B_1=(0,1,0),\ B_2=(0,0,1).
\]

For \(j=0,1,2\), put

\[
L_j=B_-+f_j(B_j-B_-),\qquad
R_j=B_++k_j(B_j-B_+),\qquad C=(L_0+L_1+L_2)/3.
\]

Take the convex hull of \(B_0,B_1,B_2,L_0,L_1,L_2,R_0,R_1,R_2,C+t(B_--C)\), with

\[
(b,f_0,f_1,f_2,k_0,k_1,k_2,t)
=(1/15,19/25,37/100,67/100,11/50,23/50,11/25,69/100).
\tag{14}
\]

This is a different rational control in a two-cut-and-stack construction. It is **not** the accepted fixed \(b=1/6\), symmetric-small-cut \(P_\varepsilon\) family and does not rename or replace that family's lower bounds.

The exact raw vertex order is

```
0 = (0, -1/15, 0)
1 = (0, 1, 0)
2 = (0, 0, 1)
3 = (-6/25, -19/375, 0)
4 = (-63/100, 37/100, 0)
5 = (-33/100, 0, 67/100)
6 = (39/50, -11/750, 0)
7 = (27/50, 23/50, 0)
8 = (14/25, 0, 11/25)
9 = (-407/500, 14849/450000, 2077/30000).
```

The complete outward maximal facet cycles are

```
F0=(0,3,4,1,7,6)    F1=(0,2,5,3)    F2=(0,6,8,2)
F3=(1,4,5,2)        F4=(1,2,8,7)    F5=(3,9,4)
F6=(3,5,9)          F7=(4,9,5)      F8=(6,7,8).
```

The 17 true edges are

```
02,03,06,12,14,17,25,28,34,35,39,45,49,59,67,68,78.
```

The source exhausts all supporting vertex triples, proves every nonincidence strictly positive, checks three independent incident normals at every vertex, and recovers these facets and edges without integration diagonals.

Actual uniform integration gives

\[
V=\frac{47426669}{140625000},\qquad
g=\left(\frac{305383217}{94853338000},
\frac{6871784228327}{28456001400000},
\frac{487569104171}{1897066760000}\right).
\tag{15}
\]

All \(X_i=Y_i-g\), the covariance, the 165 centered moments through degree eight, the ten polynomials (7), and their true polar-face fans regenerate exactly. One hundred flux tests with \(\deg\phi\le2\) are checked. All-degree validity follows analytically from actual uniform volume and the true boundary identities, not from those one hundred checks.

The raw parent vector is

\[
p=(3,2,5,9,9,4,0,8,6,9),\qquad r=9.
\tag{16}
\]

Its underlying path is

```
1—2—5—4—9—3—0—6—8—7,
```

oriented toward 9. The relabeling

```
canonical_to_raw=(9,3,0,6,8,7,4,5,2,1)
```

gives exactly TREE410's literal parent vector

```
(0,0,1,2,3,4,0,6,7,8).
```

Every selected arrow is a true edge. TREE410 remains in the recorded rooted-shape remainder, but this control is **not asserted to lie outside every previously closed labeled incidence sector**. No registry novelty or subtraction follows from the shape name.

### Independent mechanical separation

The four selected edges and integer weights in (1) are

\[
(1\to2,2),\quad(2\to5,6),\quad(3\to9,1),\quad(6\to0,1).
\]

The exact symmetric Q has positive leading minors

\[
\frac{21811813675421}{47426669000000},\quad
\frac{311007381822888392839771363747}{569351261022751378125000000000},\quad
\frac{20472879883129441030896745327912583}{45548100881820110250000000000000000}.
\tag{17}
\]

Sylvester's criterion proves \(Q\succ0\). Hence for every \(M\succeq0\), \(M\ne0\),

\[
2D_{12}+6D_{25}+D_{39}+D_{60}=-\operatorname{tr}(MQ)<0.
\tag{18}
\]

This contradicts the complete selected weak packet on the whole PSD cone, not merely at sampled metrics.

## 7. A whole physical metric cube passes every balanced-flow aggregate

Take

\[
M_0=\begin{pmatrix}
589/2&267&946/5\\
267&4089/10&329\\
946/5&329&310
\end{pmatrix},\qquad
\mathcal K=\{M=M^T:|M_{ij}-(M_0)_{ij}|\le1/100\}.
\tag{19}
\]

All matrices in \(\mathcal K\) are positive definite. No origin or metric reset is made.

At \(M_0\), the exact minimum in (12) is

\[
\gamma_*=
\frac{1628856684166461969192973709315813}{5457747542623056122576400000000000}
=0.2984485213\ldots>29/100.
\tag{20}
\]

A primal attaining representation is supported on \(\{1,2,8,9\}\), defined exactly by

\[
\sum_{i\in\{1,2,8,9\}}\lambda_i(1,X_i)=(1,0,0,0).
\tag{21}
\]

All four coefficients are positive. The affine dual slope is

\[
b=\left(
-\frac{8117487601713845670923}{1278640069840840000000},
-\frac{3181366384456008511309}{255728013968168000000},
\frac{6602534078431240318969}{153436808380900800000}
\right).
\tag{22}
\]

It satisfies \(s_i(M_0)\ge\gamma_*+b\cdot X_i\) at all ten vertices, with equality on (21). These ten exact inequalities and the positive representation prove the global minimum (20), without an optimizer verdict.

Let \(\|T\|_{1,\mathrm{entry}}=\sum_{j,k}|T_{jk}|\). The source verifies all ten strict inequalities

\[
s_i(M_0)-b\cdot X_i-\frac14-rac1{100}\|T_i\|_{1,\mathrm{entry}}>0.
\tag{23}
\]

Linearity in M proves throughout the **whole closed cube** that \(s_i(M)>1/4+b\cdot X_i\). Therefore

\[
\boxed{\sum_{i\ne r}m_i(\lambda)D_i(M)>\frac14
\quad\forall M\in\mathcal K,\ \forall\lambda\in\mathcal C(P).}
\tag{24}
\]

Every stress in (11) pairs negatively with every M in this cube. None can be positive definite, or positive on a physical spectral cone containing the cube.

The degree-six version is direct. At \(M_0\), set \(r_i=s_i(M_0)-\gamma_*-b\cdot X_i\ge0\). Linear precision gives

\[
\sum_iw_i(x)s_i(M_0)-W(x)(\gamma_*+b\cdot x)
=\sum_i r_iw_i(x)\ge0.
\tag{25}
\]

Multiplication by **any** nonnegative polynomial h satisfying (9), followed by integration against the actual uniform law, gives the lower bound (20). The robust version gives (24). More actual moments and all flux equations leave this obstruction unchanged.

### The inherited physical spectral window does not repair the failure

Let \(\Sigma\) be the actual covariance and \(H=\Sigma^{1/2}M\Sigma^{1/2}\). Exact characteristic-polynomial signs at \(M_0\) isolate one eigenvalue in each interval

\[
(1,1001/1000),\quad(59/10,5901/1000),\quad(35,35003/1000).
\tag{26}
\]

For every M in (19),

\[
\|\Sigma^{1/2}(M-M_0)\Sigma^{1/2}\|_{\mathrm{op}}
\le\frac3{100}\operatorname{tr}\Sigma<\frac1{200}.
\tag{27}
\]

Enlarging each interval by \(1/200\) covers the full cube. Direct rational comparisons give, in decreasing eigenvalue order,

\[
\lambda_1(H)/\lambda_2(H)<6,\qquad
\lambda_2(H)/\lambda_3(H)<6,\qquad
\operatorname{cond}(H)<36,
\tag{28}
\]

\[
H/\operatorname{tr}H\succ I/43,\qquad
H^{-1}/\operatorname{tr}H^{-1}\succ I/43.
\tag{29}
\]

These are stricter than the retained universal E17 caps \(p=57604303/9000000\), \(q=93375163/15000000\), their product and their trace floors. They are properties of this control's metric cube, **not improved universal constants**.

### Actual roots and census throughout the cube

All primal linear and polar cofactor-quadratic signs are certified on the whole cube. For each quadratic in the six metric entries, the source reconstructs every coefficient by exact symmetric differences and uses the constant coefficient minus the sum of absolute nonconstant contributions. No sampled-corner acceptance is used.

Throughout \(\mathcal K\), with \(N=M^{-1}\) and every pole at the actual primal centroid:

```
Stable facets:        0,2,3
Unstable vertices:    1,2,6,7,9
Strict saddle edges:  06,12,14,17,25,67
Physical weak points: none
Zero edge primitives: none, out of all 68.
```

Vertex 9 is the unique global quadratic-norm maximum, with whole-cube strict comparisons against every other vertex. Facet 0 is a genuine strictly stable root candidate and its full root fan is negative under the same N. The other strict equilibria remain. This is a nonattaining physical control, not weak110 or proper110.

## 8. Preserved limit: the complementary dual tree detects the control

The obstruction concerns the **primal centroid-balanced subtree ansatz**, not a simultaneously feasible joint relaxation. The complement of the selected primal tree has actual dual edges

```
(1,2),(0,3),(0,4),(2,4),(0,5),(1,6),(6,7),(0,8).
```

Oriented to stable facet 0, its parent vector is

```
(0,2,4,0,0,0,1,6,0).
```

For the actual same-origin poles \(q_f\), the unique positive circuit on \(\{0,2,4,7\}\) is defined by

\[
\sum_{f\in\{0,2,4,7\}}\eta_f(1,q_f)=(1,0,0,0).
\tag{30}
\]

For cumulative dual work along that complementary tree,

\[
\sum_f\eta_f s_f^\circ(M_0^{-1})<-1/4.
\tag{31}
\]

The sign remains negative on the entire metric cube. Multiplication by \(\det M>0\) gives a quadratic in the same six entries; the complete coefficient bound certifies its sign. The standalone source reconstructs the circuit, its exact rational value and the whole-cube certificate.

Equation (30) is a geometric positive pole dependence, **not** the uniform centroid of the polar. No polar refill or mass-center substitution occurs. Thus the common inverse and complete dual obligations repair this particular false pass. No blind cone for both complete packets together, or feasibility of all physical necessary conditions, is claimed.

## 9. Consequences and useful continuation

The new obstruction is global in polynomial degree, in all centroid representations, and on a closed physical metric cube. It is not a failed search. The actual body supplies full spatial volume, every moment, degree-six flux, true incidence and same-origin inverse geometry. The failing step is an added restriction on **dual certificate coefficients**: requiring every edge weight to come from nonnegative centroidal source loads.

For (1), extend its four weights by zero on the other selected edges. Equation (13) then gives negative source differences at raw vertices 0 and 5. These are legitimate dual stress loads, not negative physical volume masses. The four-arrow certificate is available to the original complete packet and unavailable to the balanced-flow construction.

The strict inequalities persist on a nonempty open neighborhood of the eight labeled parameters (14). The listed planar incidences remain exact by construction; nonincidences, actual moments, the four-point systems, stress minors and metric-cube guards vary continuously. Hence the separation is not isolated. No explicit shape-neighborhood radius, affine-modulus count, or catalogue coverage number is claimed.

Exploration initially produced aggregate false passes outside the known spectral window; those were not promoted. The returned control satisfies a strictly stronger window. Numerical computation only located the tuple, metric and small stress. Every promoted assertion is accepted by exact rational arithmetic below. No unsuccessful search is used as an exclusion theorem.

The useful continuation is to keep **independent nonnegative edge multipliers**, or terms coupling different edge increments to actual shape moments, rather than route all coefficients through (9)–(10). Complete dual obligations must remain in a joint application: Section 8 shows why a stable root fan and covariance caps alone cannot replace them.

The universal \(41/5\) factor, same-H E17 condition bound, canonical C622 attainer, lower counterfamilies and \(34\le C_{\min}\le622\) are unchanged. There is no all-root U2 claim on this control, no full TREE410 realization-class exclusion, and no whole-E17 result.

## 10. Complete deterministic recovery

Save the sole source below, including its final LF, as `centroid_flow_blind.py`. It uses **CPython 3.13.5 standard library only**, is written for Python≥3.9, and requires assertions enabled. All parameters are literal; it reads no input files and uses no random choices or external libraries.

```
python -B -S centroid_flow_blind.py > centroid_flow_blind_report.json
```

Observed JSON acceptance marker:

```
E17_ACTUAL_CENTROID_FLOW_BLIND_CONE_V1 PASS
```

| File | Bytes | SHA-256 |
|---|---:|---|
| centroid_flow_blind.py | 16335 | faf84e0d905d13efd1a1cf0cfc0f047915e25659a1edbeaf1a7d89e96de5d384 |
| centroid_flow_blind_report.json | 251488 | 28a577d1e0654b367b3d81c755e5f94fd95d6e6a0f0d24dc894d21864aad9759 |

The report contains all centered moments through degree eight, incidence polynomials, path tensors, affine residuals, the full stress matrix, inverse, poles, census, complete metric-cube guards and the negative dual application. These arrays regenerate from the source and are not inputs.

Normal exact execution and clean source-only reconstruction both passed with byte-identical source and report. These are author executions, not coordinator replays or proof-assistant formalization. The analytic closure and duality proofs above are separate from the finite checks.

Convenience copies: complete source (`centroid_flow_blind.py`), exact report (`centroid_flow_blind_report.json`), and expanded Markdown handoff (`result_markdown_v7.md`). The complete source follows; none of those links is required for continuation.

```python
#!/usr/bin/env python3
"""E17_ACTUAL_CENTROID_FLOW_BLIND_CONE_V1, standalone exact acceptance.
CPython 3.13.5 standard library; compatible with Python >=3.9.
Run: python -B -S centroid_flow_blind.py > centroid_flow_blind_report.json
All geometry, moments, four-arrow stress, and WHOLE metric-cube bounds are exact.
No input file, saved moment table, numerical library, or random seed is read.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial, gcd, lcm
import json

OBJECT='E17_ACTUAL_CENTROID_FLOW_BLIND_CONE_V1'
PARENT='minimum-0276'
PARENT_SHA256='08ba2642537a354443744c217de7b00b23a5e4e61bea4a3ea0f2931e867f36c0'
PARAMETERS=tuple(map(F,('1/15','19/25','37/100','67/100','11/50','23/50','11/25','69/100')))
PARENT_OF=(3,2,5,9,9,4,0,8,6,9)
ROOT=9
CANONICAL_TO_RAW=(9,3,0,6,8,7,4,5,2,1)
TREE410=(0,0,1,2,3,4,0,6,7,8)
M=tuple(tuple(F(x,10) for x in row) for row in ((2945,2670,1892),(2670,4089,3290),(1892,3290,3100)))
DELTA=F(1,100)
CRITICAL=(1,2,8,9)
STRESS=((1,2,2),(2,5,6),(3,9,1),(6,0,1))
Z=(0,0,0)
ONE={Z:F(1)}
XS=[{tuple(int(i==j) for i in range(3)):F(1)} for j in range(3)]

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def va(a,b): return tuple(x+y for x,y in zip(a,b))
def vs(a,b): return tuple(x-y for x,y in zip(a,b))
def vm(c,a): return tuple(c*x for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(A): return dot(A[0],cross(A[1],A[2]))
def outer(a,b): return tuple(tuple(x*y for y in b) for x in a)
def ma(A,B): return tuple(va(a,b) for a,b in zip(A,B))
def ms(c,A): return tuple(vm(c,a) for a in A)
def mm(A,B): return tuple(tuple(dot(a,b) for b in zip(*B)) for a in A)
def mv(A,x): return tuple(dot(a,x) for a in A)
def tr(A): return sum((A[i][i] for i in range(3)),F(0))
def adj(A): return tuple(zip(cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1])))
def inv(A):
    d=det(A);assert d>0
    return ms(1/d,adj(A))
def sym(A): return tuple(tuple((A[i][j]+A[j][i])/2 for j in range(3)) for i in range(3))
def minors(A): return (A[0][0],A[0][0]*A[1][1]-A[0][1]**2,det(A))
def solve(A,b):
    R=[list(a)+[v] for a,v in zip(A,b)];n=len(b)
    for j in range(n):
        p=next(i for i in range(j,n) if R[i][j])
        R[j],R[p]=R[p],R[j];v=R[j][j];R[j]=[x/v for x in R[j]]
        for i in range(n):
            if i!=j:
                v=R[i][j];R[i]=[x-v*y for x,y in zip(R[i],R[j])]
    return tuple(a[-1] for a in R)
def add(a,b):
    c=a.copy()
    for k,v in b.items():c[k]=c.get(k,F(0))+v
    return {k:v for k,v in c.items() if v}
def sc(c,a):return {k:c*v for k,v in a.items() if c*v}
def mul(a,b):
    c={}
    for k,v in a.items():
        for l,w in b.items():
            s=tuple(i+j for i,j in zip(k,l));c[s]=c.get(s,F(0))+v*w
    return {k:v for k,v in c.items() if v}
def derivative(a,j):
    out={}
    for k,v in a.items():
        if k[j]:
            s=list(k);s[j]-=1;out[tuple(s)]=k[j]*v
    return out
def poly_sum(a):
    out={}
    for p in a:out=add(out,p)
    return out
def indices(n):return [(i,j,t-i-j) for t in range(n+1) for i in range(t+1) for j in range(t-i+1)]
def raw_vertices():
    b,f0,f1,f2,k0,k1,k2,t=PARAMETERS
    B=tuple(tuple(map(F,v)) for v in ((-1,0,0),(1,0,0),(0,-b,0),(0,1,0),(0,0,1)))
    cuts=[]
    for i,fr in ((0,(f0,f1,f2)),(1,(k0,k1,k2))):
        cuts.append(tuple(va(B[i],vm(u,vs(B[j],B[i]))) for u,j in zip(fr,(2,3,4))))
    c=vm(F(1,3),va(va(cuts[0][0],cuts[0][1]),cuts[0][2]))
    return B[2:]+cuts[0]+cuts[1]+(va(c,vm(t,vs(B[0],c))),)
def plane(n,h):
    d=1
    for x in (*n,h):d=lcm(d,x.denominator)
    a=[int(x*d) for x in (*n,h)];g=0
    for x in a:g=gcd(g,abs(x))
    return tuple(F(x//g) for x in a[:3]),F(a[3]//g)
def cycle(ids,adjacency):
    a=min(ids);out=[a,min(adjacency[a])]
    while len(out)<len(ids):
        b=next(x for x in adjacency[out[-1]] if x!=out[-2]);assert b not in out
        out.append(b)
    assert a in adjacency[out[-1]]
    return tuple(out)
def geometry(Y):
    planes={}
    for i,j,k in combinations(range(10),3):
        n=cross(vs(Y[j],Y[i]),vs(Y[k],Y[i]));h=dot(n,Y[i])
        if not any(n):continue
        sl=[h-dot(n,y) for y in Y]
        if max(sl)<=0:n=vm(-1,n);h=-h;sl=[-a for a in sl]
        if min(sl)<0:continue
        ids=tuple(i for i,x in enumerate(sl) if x==0);planes[ids]=plane(n,h)
    sets=sorted(planes);assert len(sets)==9
    edges=set()
    for a,b in combinations(sets,2):
        meet=set(a)&set(b);assert len(meet)<=2
        if len(meet)==2:edges.add(tuple(sorted(meet)))
    edges=tuple(sorted(edges));assert len(edges)==17
    faces=[];ns=[];hs=[]
    for ids in sets:
        nbr={i:[] for i in ids}
        for i,j in edges:
            if i in nbr and j in nbr:nbr[i].append(j);nbr[j].append(i)
        assert all(len(x)==2 for x in nbr.values())
        cy=cycle(ids,nbr);n,h=planes[ids]
        if dot(n,cross(vs(Y[cy[1]],Y[cy[0]]),vs(Y[cy[2]],Y[cy[1]])))<0:cy=(cy[0],)+cy[:0:-1]
        faces.append(cy);ns.append(n);hs.append(h)
        assert all(h-dot(n,y)==0 if i in ids else h-dot(n,y)>0 for i,y in enumerate(Y))
    ef={e:tuple(f for f,cy in enumerate(faces) if all(i in cy for i in e)) for e in edges}
    assert all(len(x)==2 for x in ef.values())
    for i in range(10):
        inc=[ns[f] for f,cy in enumerate(faces) if i in cy]
        assert any(det(v) for v in combinations(inc,3))
    return tuple(faces),tuple(ns),tuple(hs),edges,ef

def moments(X,faces,n):
    ix=indices(n);ans={a:F(0) for a in ix};cells=[]
    for cy in faces:
        for j in range(1,len(cy)-1):
            ids=(cy[0],cy[j],cy[j+1]);vv=tuple(X[i] for i in ids);d=det(vv);assert d>0
            cells.append((ids,d))
            coeff={a:F(int(a==Z)) for a in ix}
            for v in vv:
                nxt={}
                for a in ix:
                    b=coeff[a]
                    for k in range(3):
                        if a[k]:
                            e=list(a);e[k]-=1;b+=v[k]*nxt[tuple(e)]
                    nxt[a]=b
                coeff=nxt
            for a in ix:ans[a]+=d*F(factorial(a[0])*factorial(a[1])*factorial(a[2]),factorial(sum(a)+3))*coeff[a]
    V=ans[Z];assert V>0 and len(cells)==16
    return V,{a:v/V for a,v in ans.items()},cells

def cube_polynomial_guard(fun):
    # Exact coefficients of a quadratic in the SIX symmetric metric entries.
    Es=[]
    for i,j in ((0,0),(1,1),(2,2),(0,1),(0,2),(1,2)):
        E=[[F(0)]*3 for _ in range(3)];E[i][j]=E[j][i]=F(1);Es.append(tuple(map(tuple,E)))
    f0=fun(M);linear=[];quad=[]
    for E in Es:
        fp,fm=fun(ma(M,E)),fun(ma(M,ms(-1,E)))
        linear.append((fp-fm)/2);quad.append((fp+fm)/2-f0)
    for E,H in combinations(Es,2):quad.append(fun(ma(ma(M,E),H))-fun(ma(M,E))-fun(ma(M,H))+f0)
    margin=abs(f0)-DELTA*sum(map(abs,linear))-DELTA**2*sum(map(abs,quad))
    assert margin>0
    return (f0,linear,quad,margin)

def literal(p):return [(k,v) for k,v in sorted(p.items())]
def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x

def main():
    if not __debug__:raise RuntimeError('Assertions required; do not use -O')
    Y=raw_vertices();faces,ns,hs,edges,ef=geometry(Y)
    o=tuple(sum(y[j] for y in Y)/10 for j in range(3))
    V,mu0,unused=moments(tuple(vs(y,o) for y in Y),faces,2)
    g=va(o,tuple(mu0[next(iter(x))] for x in XS));X=tuple(vs(y,g) for y in Y)
    V2,mu,cells=moments(X,faces,8);assert V2==V==F(47426669,140625000)
    assert g==(F(305383217,94853338000),F(6871784228327,28456001400000),F(487569104171,1897066760000))
    def mean(p):return sum((v*mu[k] for k,v in p.items()),F(0))
    assert all(mean(x)==0 for x in XS)
    Sigma=tuple(tuple(mean(mul(x,y)) for y in XS) for x in XS);assert min(minors(Sigma))>0
    hc=tuple(h-dot(n,g) for n,h in zip(ns,hs));assert min(hc)>0
    poles=tuple(vm(1/h,n) for n,h in zip(ns,hc))
    slacks=[add(sc(h,ONE),sc(-1,poly_sum(sc(n[j],XS[j]) for j in range(3)))) for n,h in zip(ns,hc)]
    weights=[];fans=[]
    for i,v in enumerate(X):
        inc=[f for f,cy in enumerate(faces) if i in cy];nbr={f:[] for f in inc}
        for e,ff in ef.items():
            if i in e:a,b=ff;nbr[a].append(b);nbr[b].append(a)
        assert all(len(a)==2 for a in nbr.values())
        cy=cycle(inc,nbr);w={};fan=[]
        for j in range(1,len(cy)-1):
            tri=(cy[0],cy[j],cy[j+1]);d=abs(det(tuple(ns[f] for f in tri)));assert d>0
            term=sc(d,ONE)
            for f in range(9):
                if f not in tri:term=mul(term,slacks[f])
            w=add(w,term);fan.append((tri,d))
        assert max(map(sum,w))<=6 and w.get(Z,F(0))>0
        weights.append(w);fans.append(fan)
    W=poly_sum(weights)
    for j in range(3):assert not poly_sum(mul(w,add(sc(v[j],ONE),sc(-1,XS[j]))) for w,v in zip(weights,X))
    def euler(v,p):
        out=p.copy()
        for j in range(3):out=add(out,sc(F(1,3),mul(add(XS[j],sc(-v[j],ONE)),derivative(p,j))))
        return mean(out)
    for v,w in zip(X,weights):
        for a in indices(2):assert euler(v,mul(w,{a:F(1)}))==0
    raw_to_can={j:i for i,j in enumerate(CANONICAL_TO_RAW)}
    assert tuple(raw_to_can[PARENT_OF[j]] for j in CANONICAL_TO_RAW)==TREE410
    for i in range(10):
        if i!=ROOT:assert tuple(sorted((i,PARENT_OF[i]))) in edges
    A=tuple(sym(outer(X[i],vs(X[PARENT_OF[i]],X[i]))) for i in range(10))
    path_tensors=[]
    for i in range(10):
        j=i;T=((F(0),)*3,)*3;seen=set()
        while j!=ROOT:
            assert j not in seen;seen.add(j);T=ma(T,A[j]);j=PARENT_OF[j]
        path_tensors.append(T)
    s=tuple(tr(mm(M,T)) for T in path_tensors)
    lam=solve([[F(1)]*4]+[[X[i][j] for i in CRITICAL] for j in range(3)],(F(1),F(0),F(0),F(0)))
    assert min(lam)>0
    beta=solve([[F(1)]+list(X[i]) for i in CRITICAL],[s[i] for i in CRITICAL])
    gamma,b=beta[0],beta[1:]
    assert gamma==F(1628856684166461969192973709315813,5457747542623056122576400000000000)
    assert gamma==sum(t*s[i] for t,i in zip(lam,CRITICAL))>F(29,100)
    residual=[s[i]-gamma-dot(b,X[i]) for i in range(10)];assert min(residual)>=0
    # WHOLE closed six-entry metric cube: no optimization or sampling.
    flow_guards=[s[i]-dot(b,X[i])-F(1,4)-DELTA*sum(abs(a) for row in T for a in row)
                 for i,T in enumerate(path_tensors)]
    assert min(flow_guards)>0
    # Polynomial precision makes the centroid-balanced multiplier collapse exact.
    left=poly_sum(sc(s[i],w) for i,w in enumerate(weights))
    affine=add(sc(gamma,ONE),poly_sum(sc(b[j],XS[j]) for j in range(3)))
    assert add(left,sc(-1,mul(W,affine)))==poly_sum(sc(residual[i],w) for i,w in enumerate(weights))
    Q=((F(0),)*3,)*3
    for i,j,w in STRESS:assert PARENT_OF[i]==j;Q=ma(Q,ms(-w,A[i]))
    qmin=minors(Q);assert min(qmin)>0
    assert qmin==(F(21811813675421,47426669000000),F(311007381822888392839771363747,569351261022751378125000000000),F(20472879883129441030896745327912583,45548100881820110250000000000000000))
    assert min(minors(M))>0
    SM=mm(Sigma,M);t=tr(SM);u=(t*t-tr(mm(SM,SM)))/2;d=det(Sigma)*det(M)
    def characteristic(z):return z**3-t*z*z+u*z-d
    brackets=((F(1),F(1001,1000)),(F(59,10),F(5901,1000)),(F(35),F(35003,1000)))
    signs=((-1,1),(1,-1),(-1,1))
    for iv,ss in zip(brackets,signs):assert all(sign*characteristic(z)>0 for z,sign in zip(iv,ss))
    error=3*DELTA*tr(Sigma);assert error<F(1,200)
    whole=tuple((lo-F(1,200),hi+F(1,200)) for lo,hi in brackets)
    low,mid,high=whole
    assert low[0]>0 and high[1]/mid[0]<6 and mid[1]/low[0]<6 and high[1]/low[0]<36
    assert 1+mid[1]/low[0]+high[1]/low[0]<43
    assert 1+high[1]/mid[0]+high[1]/low[0]<43
    # All strict/weak physical labels are preserved on this WHOLE cube.
    primal={};polar={};prguards=[];qguards=[]
    for a,c in edges:
        for i,j in ((a,c),(c,a)):
            H=sym(outer(X[i],vs(X[j],X[i])));v=tr(mm(M,H));err=DELTA*sum(abs(a) for row in H for a in row)
            assert abs(v)>err;primal[i,j]=v;prguards.append((i,j,v,abs(v)-err))
    for a,c in ef.values():
        for i,j in ((a,c),(c,a)):
            record=cube_polynomial_guard(lambda K:dot(poles[i],mv(adj(K),vs(poles[j],poles[i]))))
            polar[i,j]=record[0];qguards.append((i,j,record))
    unstable=tuple(i for i in range(10) if all(v<0 for (a,c),v in primal.items() if a==i))
    stable=tuple(i for i in range(9) if all(v<0 for (a,c),v in polar.items() if a==i))
    saddle=[];weak=[]
    for i,j in edges:
        a,c=ef[i,j];vv=(primal[i,j],primal[j,i],polar[a,c],polar[c,a])
        if max(vv)<0:saddle.append((i,j))
        elif max(vv)<=0:weak.append((i,j))
    assert (len(stable),len(unstable),len(saddle))==(3,5,6) and not weak
    # Stronger than merely local unstable: raw vertex9 is the unique norm maximum.
    max_guards=[]
    for i in range(9):
        H=ma(outer(X[ROOT],X[ROOT]),ms(-1,outer(X[i],X[i])))
        margin=tr(mm(M,H))-DELTA*sum(abs(a) for row in H for a in row)
        assert margin>0;max_guards.append(margin)
    # Scope limit: the COMPLEMENTARY dual tree is NOT a joint blind witness.
    # Its root0 is one of the actual stable facets. Never recenter the polar.
    chosen={tuple(sorted((i,PARENT_OF[i]))) for i in range(9)}
    dual_edges=tuple(ff for e,ff in ef.items() if e not in chosen)
    nbr=[[] for unused in range(9)]
    for i,j in dual_edges:nbr[i].append(j);nbr[j].append(i)
    dp=[None]*9;dp[0]=0;todo=[0]
    while todo:
        i=todo.pop()
        for j in nbr[i]:
            if dp[j] is None:dp[j]=i;todo.append(j)
    assert all(x is not None for x in dp)
    ci=(0,2,4,7)
    cl=solve([[F(1)]*4]+[[poles[i][j] for i in ci] for j in range(3)],(F(1),F(0),F(0),F(0)))
    assert min(cl)>0
    Tdual=((F(0),)*3,)*3
    for i,weight in zip(ci,cl):
        j=i
        while j!=0:
            Tdual=ma(Tdual,ms(weight,sym(outer(poles[j],vs(poles[dp[j]],poles[j])))))
            j=dp[j]
    dual_value=tr(mm(inv(M),Tdual));assert dual_value < -F(1,4)
    dual_cube_guard=cube_polynomial_guard(lambda K:tr(mm(adj(K),Tdual)))
    assert dual_cube_guard[0]<0
    out={'marker':OBJECT+' PASS','parent':PARENT,'parent_sha256':PARENT_SHA256,
         'scope':'Actual uniform E17 TREE410 packet exclusion; complete centroid-balanced subtree-flow method barrier, not all-root exclusion or 110',
         'parameters_b_first3_second3_stack':PARAMETERS,'raw_vertices':Y,'faces':faces,'true_edges':edges,
         'raw_normals':ns,'raw_offsets':hs,'volume':V,'actual_centroid':g,'actual_covariance':Sigma,
         'centered_vertices':X,'same_origin_poles':poles,'positive_tetrahedra':cells,
         'moment_order':8,'centered_moments':[(a,mu[a]) for a in indices(8)],
         'degree_six_flux_weights':[literal(w) for w in weights],'polar_face_fans':fans,'flux_checks':100,
         'raw_parent':PARENT_OF,'root':ROOT,'canonical_to_raw':CANONICAL_TO_RAW,'canonical_TREE410':TREE410,
         'metric_center':M,'physical_inverse_at_center':inv(M),'closed_entry_cube_radius':DELTA,
         'path_tensors':path_tensors,'center_path_work':s,'critical_indices':CRITICAL,'critical_lambda':lam,
         'exact_balanced_flow_minimum':gamma,'affine_slope':b,'affine_residuals':residual,
         'whole_cube_flow_lower_bound':F(1,4),'whole_cube_flow_guards':flow_guards,
         'independent_arrow_stress':STRESS,'stress_matrix':Q,'stress_positive_leading_minors':qmin,
         'characteristic_coefficients':(-d,u,-t,F(1)),'center_eigenvalue_brackets':brackets,
         'eigenvalue_perturbation_bound':error,'whole_cube_eigenvalue_brackets':whole,
         'whole_cube_adjacent_ratios_strict_upper':6,'whole_cube_condition_strict_upper':36,
         'whole_cube_both_trace_floors_strict_lower':F(1,43),
         'stable':stable,'unstable':unstable,'saddle_edges':saddle,'weak_edges':weak,'zero_primitives':0,
         'whole_cube_primal_sign_guards':prguards,'whole_cube_dual_quadratic_sign_guards':qguards,
         'whole_cube_root_norm_gaps':max_guards,
         'scope_limit_dual_complement':{'root':0,'edges':dual_edges,'parent':dp,'centroid_circuit':ci,
           'positive_circuit_weights':cl,'center_work':dual_value,'whole_cube_negative_guard':dual_cube_guard}}
    print(json.dumps(serial(out),sort_keys=True,indent=2))

if __name__=='__main__':main()
```
