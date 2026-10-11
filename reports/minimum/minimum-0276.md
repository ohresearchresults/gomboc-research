# minimum-0276

Historical AI scientific report · saved 2026-09-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# CROSS_APEX_COMMON_LAW_AND_FINITE_MOMENT_SUPPORT_RECOVERY_V1

## 1. Results and change of direction

The new constraint is that **one actual uniform volume law must have a positive cone-endpoint functional at every point of its own body**. Changing the apex does not refill, recenter, or change the body. This supplies a different coupling from adding more projective parameters to one chosen radial law.

Three conclusions are proved below.

**Low-order common-law separation.** An explicit 18-by-18 cross-apex moment matrix, requiring endpoint moments only through total degree four, is positive semidefinite for every actual three-body. A small integer quadratic test makes it strictly negative on the literal five-atom axial barrier in the accepted parent:

\[
\boxed{\mathcal J(Q)=
-\frac{2379981614040424343931488307784376887}
{3178455093485431200129463961518080000}<-\frac7{10}.}
\tag{1}
\]

This is a new exact rejection of that **nonphysical law**, not an actual-body bound of 8. The matrix uses two independent draws from the **same** endpoint distribution; its entries are quadratic in that one moment sequence. It cannot be implemented by assigning the two copies independent moments.

**Finite support determination at the first layer.** From the actual uniform moments of a polytope P, define the nested apex-moment outer sets \(\mathcal A_k(P)\) in Section 3. The first set is exactly the familiar covariance ellipsoid. If P has F true facets, then

\[
\boxed{\mathcal A_{F-1}(P)=P.}
\tag{2}
\]

This first exact degree is sharp for this hierarchy: \(\mathcal A_k(P)\supsetneq P\) for every \(k<F-1\). In particular, every actual polytope with at most nine facets is determined by its uniform moments through degree **16**. The degree-eight square matrix has 165 rows in dimension three. This statement assumes actual uniform moments; it does not assert that arbitrary truncated moments passing the matrix tests are physically realizable.

**Completeness and its dimensional boundary.** All cross-apex square tests characterize uniform volume on a full-dimensional convex hull when the radial exponent equals the full spatial dimension. In contrast, an explicit smooth positive law on a square passes **every** projected exponent-three cross-apex test and both inherited coordinate convex orders, yet cannot be the projection of uniform volume from any convex three-body. Thus using only the two projected coordinates cannot make the new hierarchy complete. The third spatial coordinate or actual fiber concavity is essential.

A further actual-incidence identity gives degree-six polynomial flux multipliers on every nine-facet body, including nonsimple vertices. These provide linear common-volume moment identities rather than freely assigned boundary masses. A genuine 10/17/9 bevel control verifies the construction, all nine degree-eight facet isolators, and a fourth-moment support cut strictly stronger than its covariance ellipsoid.

**What does not change:** the universal factor remains the accepted \(\Upsilon_\Sigma<41/5\), and the same-H E17 condition bound remains below 40 with both trace floors above I/48. No whole first-layer exclusion, new 110 attainer, or catalogue subtraction is claimed. The global bracket remains \(34\le C_{\min}\le622\). The inherited factor and the fact that the entire five-parameter H5 family is separately closed are recorded in the supplied update. fileciteturn39file0L122-L130

## 2. Input authority and a notation correction

The complete new journal was read consecutively through EOF: **360498 bytes, 2250 lines**, SHA-256

`10788779c44db310472362ab657663fe598ec5fe0738ef00b76d504751b2d67e`.

Both new exact materials were read in full:

- `MONOUNSTABLE_FIRST_LAYER_SUPPORT_GAP_V1.md`, 14486 bytes, SHA `2b525e9ff76a616d5cceeeceafa67044f09930f3f20e057b2a31768b562a916e`;
- `support_gap_arithmetic.py.txt`, 4369 bytes, SHA `0295a350373473ce2dc4d28179853c5498d33fed548b253c448f656784517117`.

The literal parent is **minimum-0268**, SHA

`c199a4de7b66fb757fbc3f1b2beeb903f7002fe567611824a9f0626b32aa2fc5`.

Its compact UTF-8 version-2 JSON envelope reconstructs to **54502 bytes** with that digest, taking the literal Markdown with its final LF. Earlier unchanged evidence is retained; no missing source is required by the new exact programs or proofs.

There is one summary-level notation conflict. The branch summary labels the parent's tuples as `(eta,theta)`, whereas the literal parent and its code use **(theta,eta)**. The authoritative tuples are

\[
(\theta,\eta)=(3/10,0),(3/5,-1/5),(3/10,1/10),
\quad g=1-\theta/3+\theta D+\eta W.
\]

This is an order-label error in the summary, not a change of the accepted probes. fileciteturn44file1L24-L27 fileciteturn40file0L104-L110

The one-apex radial-mixture idea is classical: alpha-unimodality and its unique radial-mixture representation are described in Van Parys, Goulart and Kuhn, *Generalized Gauss Inequalities via Semidefinite Programming*, Definition 7 and Theorem 3. No historical priority for that framework is claimed here. The all-apex proofs, finite polytope degree statement and exact controls below are supplied independently, so the executable recovery has no literature dependency. citeturn974752view0

## 3. The apex functional and finite exact support recovery

Let \(\mu\) be a compactly supported probability measure in \(\mathbb R^d\). For an apex a and a continuously differentiable test function \(\phi\), define

\[
\mathcal E_a(\phi)
=\int\left[\phi(x)+\frac1d(x-a)\cdot\nabla\phi(x)\right]d\mu(x).
\tag{3}
\]

(3) is invariant under simultaneous invertible affine transport of the measure, apex and test function, by the chain rule. The apex is an auxiliary coning point, not a new mass center or a replacement physical origin.

### Actual uniform-volume identity

When \(\mu=1_P\,dx/V\) for a convex body P of positive volume, the divergence theorem gives

\[
\boxed{\mathcal E_a(\phi)
=\frac1{dV}\int_{\partial P}\phi(x)(x-a)\cdot n(x)\,dS(x).}
\tag{4}
\]

For \(a\in P\), the right side is a positive probability functional: the support plane at x gives \((x-a)\cdot n(x)\ge0\), and its total mass is 1. It is exactly the actual radial cone-endpoint law from a. The statement includes boundary apices and zero weights on their incident facets.

For a polytope with true facet inequalities \(\ell_f(x)=h_f-n_f\cdot x\ge0\), (4) is

\[
\mathcal E_a(\phi)=
\sum_f\frac{\ell_f(a)}{dV\|n_f\|}\int_{F_f}\phi\,dS.
\tag{5}
\]

Neither triangulation diagonals nor arbitrary vertex quadrature weights appear.

### Apex-moment matrices

Write \(m_\alpha=\int x^\alpha d\mu\). On the monomial basis \(\mathcal P_k\) of total degree at most k, define

\[
B_a^{(k)}[\alpha,\beta]
=\frac{d+|\alpha+\beta|}{d}m_{\alpha+\beta}
-\frac1d\sum_j a_j(\alpha_j+\beta_j)
 m_{\alpha+\beta-e_j}.
\tag{6}
\]

Terms with zero coefficient are omitted. Thus \(q^TB_a^{(k)}q=\mathcal E_a(q(x)^2)\). For actual uniform P, put

\[
\mathcal A_k(P)=\{a\in\mathbb R^d:B_a^{(k)}\succeq0\}.
\tag{7}
\]

These are closed convex sets, linear-matrix-inequality sets in a at fixed moments, and

\[
P\subseteq\mathcal A_{k+1}(P)\subseteq\mathcal A_k(P).
\]

At the actual centroid 0, with covariance \(\Sigma\),

\[
B_a^{(1)}=
\begin{pmatrix}
1&-a^T/d\\
-a/d&(d+2)\Sigma/d
\end{pmatrix}.
\]

The Schur complement shows

\[
\mathcal A_1(P)=\{a:a^T\Sigma^{-1}a\le d(d+2)\}.
\tag{8}
\]

In dimension three this is the old covariance outer ellipsoid with coefficient 15. Thus the new hierarchy begins with, and refines, the supplied actual covariance containment rather than changing its normalization. fileciteturn33file14L22-L40

### Theorem 1: exact contact kernel and first exact degree

Suppose P is a full-dimensional polytope with F distinct true facets. For \(a\in P\), let

\[
s(a)=\#\{f:a\notin F_f\},\qquad
R_a(x)=\prod_{f:a\notin F_f}\ell_f(x).
\]

Then

\[
\boxed{\ker B_a^{(k)}=R_a\mathcal P_{k-s(a)},}
\tag{9}
\]

with the right side understood as zero for \(k<s(a)\). Its dimension is \(\binom{d+k-s(a)}d\) when \(k\ge s(a)\).

**Proof.** All coefficients in (5) are nonnegative, and those for the s(a) nonincident facets are positive. Hence \(\mathcal E_a(q^2)=0\) exactly when q vanishes on each of those facets. Vanishing on a relative-open subset of a facet plane implies divisibility by its affine equation. The equations of distinct facets are distinct irreducible linear factors, so their product divides q. The converse follows immediately from (5). Positive semidefiniteness identifies this zero-quadratic-form space with the matrix kernel. This proves (9), including all boundary contacts.

For each facet f take the degree-F−1 isolator

\[
q_f(x)=\prod_{j\ne f}\ell_j(x).
\]

All facet integrals except the f-th vanish. Therefore, for **every** apex \(a\in\mathbb R^d\), including exterior points,

\[
\mathcal E_a(q_f^2)=\kappa_f\ell_f(a),
\qquad
\kappa_f=\frac1{dV\|n_f\|}\int_{F_f}q_f^2\,dS>0.
\tag{10}
\]

Positivity is strict because every other slack is positive on the relative interior of \(F_f\). Consequently \(B_a^{(F-1)}\succeq0\) forces every true facet inequality, proving \(\mathcal A_{F-1}(P)=P\).

For sharpness, choose a in the relative interior of a true facet. Then \(s(a)=F-1\). For \(k<F-1\), (9) makes \(B_a^{(k)}\) positive definite. Continuity gives a full open neighborhood of feasible apices, including exterior points. Thus \(\mathcal A_k(P)\supsetneq P\) at every lower degree. This is sharpness of the specified moment hierarchy, not a lower bound for every possible moment-reconstruction method.

### First-layer consequences

For F≤9, actual moments through degree 16 give \(\mathcal A_8(P)=P\). There are **969** scalar monomials through degree 16 in three variables; the square-test basis through degree 8 has **165** elements. Two actual uniformly filled polytopes, each with at most nine facets and with identical moments through degree 16 in the same coordinates, must therefore be identical.

At a true E17 vertex of degree j, the first possible kernel occurs at \(k=9-j\). At a relative-interior facet point, \(B_a^{(8)}\) has exactly one null direction, its isolator \(q_f\). These are exact contact implications, not statements that a particular contact is a mechanical equilibrium.

Importantly, **finite support determination is not finite uniformity characterization**. It starts from the body's actual uniform moment sequence. Merely fitting a truncated sequence to (6) does not certify that it is the sequence of a uniform polytope.

## 4. All-apex positivity characterizes uniform volume

### Theorem 2

Let K be a compact full-dimensional convex set and \(\mu\) a probability measure supported in K. Let S be any set whose closed convex hull is K. The following are equivalent:

1. \(\mu\) is normalized uniform volume on K.
2. For every \(a\in S\) and every polynomial q, \(\mathcal E_a(q^2)\ge0\).

Thus the **true vertices suffice** for a polytope, provided all polynomial degrees are retained.

**Proof of the nontrivial direction.** The functional is affine in a, so positivity extends from S to all of K. It also extends from polynomial squares to nonnegative continuously differentiable functions. Indeed, approximate \(\sqrt{\phi+\varepsilon}\) and its first derivatives uniformly on a surrounding box by polynomials, square, and then let \(\varepsilon\downarrow0\). The needed C1 approximation follows, for example, from tensor Bernstein approximation: its first derivatives are the Bernstein averages of first finite differences, which converge uniformly to the first derivatives of a C1 function.

For a fixed \(a\in K\), set \(T_{a,t}x=a+t(x-a)\). For nonnegative C1 \(\phi\),

\[
\frac{d}{dt}\left[t^d\int\phi(T_{a,t}x)d\mu(x)\right]
=d t^{d-1}\mathcal E_a(\phi\circ T_{a,t})\ge0.
\]

Hence, for \(0<t<1\), the measure inequality

\[
\mu\ge t^d(T_{a,t})_\#\mu
\tag{11}
\]

holds. Equivalently, for every Borel A,

\[
\mu(tA+(1-t)a)\ge t^d\mu(A).
\tag{12}
\]

We first prove absolute continuity; it is not assumed. Average (12) over a small ball of apices inside K. If A is Lebesgue-null, Fubini gives

\[
\int\mu(tA+(1-t)a)\,da=0,
\]

because for every fixed x the set of a with \(x\in tA+(1-t)a\) is a translate and rescaling of a null set. Thus \(\mu(A)=0\).

Write \(d\mu=\rho\,dx\). The density form of (11) is

\[
\rho(a+t(x-a))\ge\rho(x)
\quad\text{for almost every x, for each }a\in K.
\tag{13}
\]

Let \(K_\varepsilon=\{x\in K:\operatorname{dist}(x,\partial K)\ge\varepsilon\}\) have nonempty interior. Choose a fixed positive t so small that
\(t\operatorname{diam}K/(1-t)<\varepsilon\). For x,z in \(K_\varepsilon\),

\[
a=\frac{z-tx}{1-t}\in K.
\]

Fubini and the invertible linear change \((x,a)\mapsto(x,z)\) turn (13) into \(\rho(z)\ge\rho(x)\) for almost every pair x,z in \(K_\varepsilon\). Interchanging them forces equality. Thus \(\rho\) is constant on each nested inner body; letting \(\varepsilon\downarrow0\) makes it constant almost everywhere on K. Normalization gives \(\rho=1/\operatorname{Vol}K\). Conversely, uniform volume satisfies (4).

This theorem does not need smoothness of K, initial absolute continuity of μ, an SPD mechanical metric, or any centroid prescription. In the physical application the centroid is still computed from that same μ.

## 5. The cross-apex common-law hierarchy

Let ν be any compactly supported probability law in \(\mathbb R^d\), choose y, and let

\[
X=(1-T)y+TZ',\qquad T\sim d t^{d-1}dt,
\quad Z'\sim\nu,
\tag{14}
\]

independently. Denote its law by μ. The elementary radial integration identity is

\[
\boxed{\mathcal E_y(\phi)=\mathbb E_\nu\phi(Z').}
\tag{15}
\]

To check it, differentiate \(t^d\phi(y+t(Z'-y))\) and integrate from 0 to 1. Thus changing the apex is not permission to choose a new endpoint law with independently matched moments.

Take another independent draw \(Z\sim\nu\), and for a polynomial Q in the two vector arguments define

\[
\mathcal J(Q)=\mathbb E_{X,Z}\left[
Q(X,Z)^2+\frac1d(X-Z)\cdot\nabla_X Q(X,Z)^2\right].
\tag{16}
\]

### Theorem 3

If \(K=\operatorname{conv}(\{y\}\cup\operatorname{supp}\nu)\) has affine dimension d, then

\[
\boxed{\mathcal J(Q)\ge0\text{ for every polynomial Q}
\iff\mu\text{ is uniform volume on K}.}
\tag{17}
\]

When these hold, ν is the actual far-endpoint cone law from y.

**Proof.** For an actual uniform μ, condition on Z and apply (4), since every Z lies in K. Conversely, take \(Q(x,z)=q(x)r(z)\). For fixed q, \(F_q(z)=\mathcal E_z(q^2)\) is continuous and affine in z. If it were negative at a point of \(\operatorname{supp}\nu\), it would be negative on a neighborhood of positive ν measure. A continuous function supported there, followed by uniform polynomial approximation for r, would make \(\int r^2F_q\,d\nu<0\). Thus \(\mathcal E_z(q^2)\ge0\) for all z in the support and all q. Equation (15) supplies positivity at y. Theorem 2 gives uniform volume on their convex hull. Equation (15) then identifies ν with the actual endpoint law, not merely a measure having its first two moments.

For explicit moment tests let \(n_\gamma=\mathbb E_\nu Z^\gamma\) and \(m_\alpha=\mathbb E_\mu X^\alpha\), linked by (14). On the basis \(x^\alpha z^\gamma\), with \(|\alpha|\le k,|\gamma|\le l\), the matrix is

\[
C_{k,l}[(\alpha,\gamma),(\beta,\delta)]
=\frac{d+|A|}{d}m_A n_G
-\frac1d\sum_j A_jm_{A-e_j}n_{G+e_j},
\quad A=\alpha+\beta,\ G=\gamma+\delta.
\tag{18}
\]

All these matrices must be PSD. All of them together are complete in the precise sense of (17). Their entries are **products of moments of the same ν**, not a linear or globally convex moment model. A separate matrix of freely fitted products would lose the assertion.

### Exact low-degree rejection of the parent's axial barrier

Retain the parent's literal five atoms, with weights

\[
\omega=(3/64,9/64,15/64,21/64,1/4),\quad
W=(-7/3,-13/9,-7/15,11/21,1),
\]

\[
p=(-376927/3356640,-223771/671328,-284887/671328,
-1188667/3356640,-32591/124320).
\tag{19}
\]

They are the same law generated by \(D=(W^2-(m_3/m_2)W-m_2)/12\), \(p=D-1/3\), \(m_2=296/315\), \(m_3=-74017/99225\). The parent proves its ratio \(2384557056/296272099>8\), all axial probe inequalities and the stated full coordinate convex orders; it explicitly does not realize actual volume. fileciteturn41file0L146-L186 fileciteturn41file0L216-L262

For a full formal spatial completion use endpoint atoms \((W,\pm1,p)\), each of weight \(\omega/2\), and apex \((0,0,1)\). The following test ignores the middle coordinate but keeps the **three-dimensional Euler exponent**. Set

\[
\xi=TW',\qquad\zeta=1-T+Tp',
\]

where \((W',p')\) and the tested apex \((W,p)\) are independent draws from the same five atoms. Use

\[
\begin{aligned}
Q_{W,p}(\xi,\zeta)={}&(22+55p-8W)+(2+p-3W)\zeta\\
&+(-9-23p+3W)\xi+(-24-47p+16W)\zeta^2\\
&+(-15-36p+6W)\xi\zeta+(-13-33p+4W)\xi^2.
\end{aligned}
\tag{20}
\]

This is the integer vector

```
22,55,-8, 2,1,-3, -9,-23,3,
-24,-47,16, -15,-36,6, -13,-33,4
```

on the ordered basis
\((1,\zeta,\xi,\zeta^2,\xi\zeta,\xi^2)\otimes(1,p,W)\).
It gives the exact negative value (1). Source A verifies it both by (18) and independently by conditioning on each of the five apices.

Only endpoint moments through total degree four are needed: μ moments through degree four come from the same ν moments, and the other endpoint factors in (18) have degree at most three. The quadratic products in the matrix must still be retained exactly.

Two negative-result qualifications are useful. The corresponding 9-by-9 \(C_{1,1}\) block is **positive definite**. Also the two-coordinate degree-four-square blocks \(B_a^{(4)}\), of size 15, are positive definite at both \(a=(0,0)\) and \(a=(0,-1/3)\). Exact rational LDL factorizations establish all three assertions. Thus this cross-apex test beats both the displayed lower cross block and raising those two **fixed, two-coordinate** apex tests to moment order eight. No assertion is made that every full-spatial block of those orders is positive.

### A separate finite-ray annihilator certificate

A reusable higher-degree separator is also preserved. Let

\[
Q_0(\xi,\zeta)=\prod_{i=1}^5[(p_i-1)\xi-W_i(\zeta-1)],
\qquad R=\partial_\zeta Q_0.
\]

Normalize \(Q_0\) to primitive integer coefficients as Source A specifies. It vanishes on the five radial segments, and

\[
\xi\partial_\xi Q_0+(\zeta-1)\partial_\zeta Q_0=5Q_0.
\]

For the apex 0, put \(S=\mathbb E_\mu R^2>0\), \(T_0=\mathcal E_0(R^2)\). Then

\[
\mathcal E_0(Q_0^2)=0,\qquad
\mathcal E_0(Q_0R)=S/3.
\]

Choosing \(\epsilon=S/[3(|T_0|+S)]\) gives

\[
\mathcal E_0((Q_0-\epsilon R)^2)
=-2\epsilon S/3+\epsilon^2T_0<0.
\tag{21}
\]

This is a degree-ten linear moment cut. Together with the exact positive degree-four block, it identifies degree five as the first failing square degree in this particular **two-coordinate, center-apex** hierarchy. The full exact integer polynomial is regenerated by the complete source; no coefficient array or root selection is missing. It is a method for rejecting radial-segment over-covers, not a physical obstruction at a convex body's genuine apex.

## 6. A rigorous boundary: projected cross-apex completeness fails

The full-dimension requirement in Theorems 2 and 3 matters. On \(D=[-1,1]^2\), consider the smooth positive probability density

\[
\boxed{\rho(u,v)=\frac3{13}(1+u^2/4).}
\tag{22}
\]

It has mean 0 and covariance \(\operatorname{diag}(23/65,1/3)\). For every a in D and every nonnegative C1 \(\phi\), define the projected functional with exponent **3**:

\[
\mathcal E_a^{[3]}(\phi)
=\int_D[\phi+(x-a)\cdot\nabla\phi/3]\rho\,dx.
\]

Two-dimensional integration by parts gives positive boundary terms and the bulk density

\[
\frac{\rho-(x-a)\cdot\nabla\rho}{3}
=\frac1{13}(1-u^2/4+a_1u/2)\ge\frac1{52}.
\tag{23}
\]

For the last inequality, at \(a_1=\pm1\) the numerator minus 1/4 equals \((1\pm u)(3\mp u)/4\ge0\); interpolate in \(a_1\). Therefore **every** projected apex square test, and every projected cross-apex square test, passes. Nonzero polynomial-square tests are even strictly positive.

To exhibit one common radial law explicitly, use source apex 0 and exponent three. Its endpoint distribution has:

- bulk density \((1-u^2/4)/13\) on D;
- density 5/52 with respect to length on each vertical edge;
- density \((1+u^2/4)/13\) on each horizontal edge.

The respective total masses are \(11/39,5/13,1/3\). This distribution is \(\mathcal E_0^{[3]}\). For every homogeneous degree-j polynomial, its moment is \((1+j/3)\) times the moment under ρ. Radial mixing multiplies it by \(3/(3+j)\); hence it reconstructs ρ exactly by compact moment uniqueness. The endpoint law is supported in D, so conditioning on every endpoint also proves the full projected cross-apex hierarchy, not merely a few sampled apices.

It retains the two coordinate convex-order controls. The horizontal marginal is \(6/13+3u^2/26\). Its difference from the upper reference cone \(3(u+3)^2/64\) on \([-3,1]\), restricted to \([-1,1]\), is

\[
(57u^2-234u+33)/832.
\]

This is strictly decreasing there, positive at −1 and negative at 1. Outside on \([-3,-1)\), the difference is negative. Thus its sign pattern is −,+,−. With equal mass and mean, the chord argument proves the full upper convex order. Symmetry supplies the opposite-sign upper cone. On \([0,1]\), the difference from the centered squared tent \((3/2)(1-u)^2\) is

\[
(-27+78u-36u^2)/26,
\]

strictly increasing from negative to positive. Symmetry gives +,−,+ and the full lower convex order. For the vertical uniform marginal, the corresponding differences are \((5-18v-3v^2)/64\) and \(-1+3v-3v^2/2\), with the same sign arguments.

Nevertheless (22) is **not the projection of uniform volume from a convex three-body**. Such a projection's density is proportional to the length of its one-dimensional fibers. The upper fiber endpoint is concave and the lower endpoint convex, so their difference is concave. But

\[
\rho(1/2,0)-\rho(0,0)
=\rho(-1/2,0)-\rho(0,0)=3/208>0,
\]

violating midpoint concavity. This is an exact nonphysical projected-law obstruction, not an actual-body counterexample, and no high orthogonal ratio or mechanical tree is claimed for it. It proves that even the **entire** projected exponent-three cross-apex hierarchy plus those full coordinate convex orders cannot replace actual fiber concavity or the full spatial law.

## 7. Degree-six true-incidence flux identities

Here P is an actual polytope in dimension three, with F true facet slacks \(\ell_f=h_f-n_f\cdot x\). At each true vertex \(v_i\), choose a fan triangulation \(\mathcal T_i\) of its **true polar face**, using the cyclic incident facets. Define

\[
w_i(x)=\sum_{\tau\in\mathcal T_i}
|\det(n_{\tau_1},n_{\tau_2},n_{\tau_3})|
\prod_{f\notin\tau}\ell_f(x).
\tag{24}
\]

These polynomials have degree at most F−3, are nonnegative on P and positive in its interior. They are geometric polynomial multipliers, **not actual volume masses or selectable vertex quadrature weights**.

They satisfy polynomial linear precision:

\[
\boxed{\sum_iw_i(x)(v_i-x)=0.}
\tag{25}
\]

**Proof.** For an interior x, the polar of \(P-x\) has vertices \(n_f/\ell_f(x)\). A triangle on its face corresponding to \(v_i\) has outward vector area

\[
\frac12\left|\det\left(\frac{n_{\tau_1}}{\ell_{\tau_1}},
\frac{n_{\tau_2}}{\ell_{\tau_2}},
\frac{n_{\tau_3}}{\ell_{\tau_3}}\right)\right|(v_i-x).
\]

The sum of all outward vector areas of a closed polytope is zero. Multiplying by \(2\prod_f\ell_f(x)\) yields (25). It holds on an open set, hence polynomially everywhere. This proof uses a polar as an auxiliary geometric identity; it does not assign that polar a uniform centroid or a physical metric.

For the **one actual uniform volume law** of P,

\[
\boxed{\mathcal E_{v_i}(w_i\phi)=0
\quad\text{for every polynomial }\phi.}
\tag{26}
\]

Indeed, on a facet incident to \(v_i\), the flux coefficient in (5) is zero. On any nonincident facet, every term of \(w_i\) contains that facet's slack and vanishes. This proves (26) without an independently integrated facet law.

There is also a useful synchronization explanation. Differentiating (25) gives the pointwise identity

\[
\sum_i\left[w_i\phi+\frac13(x-v_i)\cdot\nabla(w_i\phi)\right]=0.
\]

Whenever full apex positivity is known, every term integrated against the common law with \(\phi=q^2\) is nonnegative, because \(w_iq^2\ge0\) on P; their sum forces all of them to vanish. A truncated square hierarchy alone need not imply positivity of these nonsquare localizers, so (26) should be retained as explicit linear moment identities when working at a finite order.

For F=9, \(\deg w_i\le6\). Tests with \(\deg\phi\le j\) use moments through degree 6+j. Nonsimple vertices are covered by their genuine polar-face fans; a tetrahedral integration diagonal is never declared to be a mechanical edge. These low-degree identities complement the degree-16 exact support statement. They do not by themselves establish a whole E17 mechanical contradiction.

## 8. Actual 10/17/9 calibration and a strict fourth-moment support cut

Use the **unchanged half-bevel raw fixture**, not the parent's pyramid or cut/cut/stack lower family:

```
0=(-1,-1/2,-1)   1=(1,-1/2,-1)
2=(1,1,-1)      3=(-1,1,-1)
4=(-1,-1,-1/2)  5=(1,-1,-1/2)
6=(-1,-1,1)     7=(1,-1,1)
8=(-1,1,1)      9=(1,2,3)
```

Its inherited raw identity is recorded in the supplied notebook. The metric and the new moment calculations below are specified separately, so older censuses of other metrics are not overwritten. fileciteturn44file0L9-L13

Source B independently reconstructs every supporting vertex triple, all maximal facets and the 17 true edges. Its outward cycles are

```
(0,3,2,1), (0,1,5,4), (0,4,6,8,3),
(1,2,9,7,5), (2,3,9), (3,8,9),
(4,5,7,6), (6,7,9), (6,9,8).
```

The 16 origin tetrahedra are actual positive cells. Exact integration gives

\[
V=47/4,\qquad g=(4/47,77/282,125/282),
\]

\[
\Sigma=\begin{pmatrix}
10429/33135&410/6627&3262/33135\\
410/6627&361877/795240&298603/1590480\\
3262/33135&298603/1590480&544661/795240
\end{pmatrix}.
\tag{27}
\]

All 969 moments through degree 16 regenerate exactly. The computation verifies (25) as a polynomial identity, all **100** instances of (26) for the ten vertices and monomials \(\deg\phi\le2\), and the nine exact recovered facet rows (10). It does not need to form or numerically diagonalize a 165-by-165 matrix: the analytic positivity and the nine isolators prove exact support recovery.

Already the square \(q(x,y,z)=(z+1)^2\), requiring only fourth moments, yields the valid raw support cut

\[
\boxed{a_z\le\frac{887813}{275444}=3.223206895\ldots.}
\tag{28}
\]

The true maximum is 3. The covariance-only upper support cap is \(g_z+\sqrt{15\Sigma_{zz}}\); (28) is strictly smaller, checked by squaring the positive differences. The literal exterior point

\[
a=\left(
\frac{455813857692}{937647528025},
\frac{1946226669277}{1875295056050},
\frac{11132093}{3443050}\right)
\]

satisfies \((a-g)^T\Sigma^{-1}(a-g)<15\) but

\[
\mathcal E_a(q^2)=-68861/846000<0.
\]

Thus it survives the covariance ellipsoid and fails the fourth-moment support test. It is an exterior test point, not a proposed vertex or body.

For a physical calibration use

\[
M=\begin{pmatrix}5&1&2\\1&3&-1\\2&-1&4\end{pmatrix},
\qquad N=M^{-1},
\]

after subtracting the **actual** g. The exact census is strict \((S,U,H)=(7,6,11)\), weak000, with all 68 true-edge primitives nonzero. Stable facets are \(0,1,3,5,6,7,8\), unstable vertices \(0,2,3,5,6,9\). The eleven saddle edges, all poles, both inverse matrices and all support data regenerate in Source B. This is a genuine uniformly filled nonwinner, not a 110 attainer or an all-metric survivor. The same underlying bevel family was already excluded by other all-SPD results; this calculation is a calibration of the new moment mechanism, not new atlas coverage.

## 9. Mechanical use and exact limitations

The supplied coordinator theorem proves, for actual ten-vertex bodies with at most nine facets admitting one nonzero-PSD weak rooted tree,

\[
3h^2-2hb+3b^2<(40-\varepsilon)u^T\Sigma u,
\qquad\varepsilon=2^{-(2^{124}+19)}.
\tag{29}
\]

It needs neither S1 nor a positive eigenvalue floor and includes incidental weak contacts. Its very small constant is not replaced here. fileciteturn33file0L7-L22

The new operators can be imposed **simultaneously with (29) on the same body**: changing an apex in (3) leaves the actual volume law, its centroid, covariance, incidence and physical metric unchanged. This is exactly the distinction from arbitrary projective refills, which may lose the rooted tree. The supplied warning against transferring the conditioned gap to such refills remains necessary. fileciteturn33file0L165-L169

For an actual first-layer candidate with vertices \(v_i\), centroid g and one chosen weak tree under \(M\succeq0, M\ne0\), the following are common obligations, not independently satisfiable modules:

\[
(v_i-g)^TM(v_{\mathrm{parent}(i)}-v_i)\ge0,
\quad B_{v_i}^{(k)}\succeq0,
\quad\mathcal E_{v_i}(w_i\phi)=0,
\quad C_{k,l}\succeq0,
\]

together with its actual volume moments and (29). The square matrices are linear in an apex only when the moments are fixed; unknown shape and cross-moment products do not make this a globally convex semidefinite feasibility problem.

A support envelope can also sharpen the finite-height route on a particular actual body. In the frame \(C^{-1/2}P\), a certified upper bound U for the support/central-section factor obtained from the true supports and a set \(\mathcal A_k\) containing P is a valid upper bound on \(\Upsilon_C(P)\). For a true primal tree of height h and polar tree of height j, the existing same-origin self-polar argument then gives

\[
\lambda_1/\lambda_2\le U f(h+1),\qquad
\lambda_2/\lambda_3\le U f(j+1),
\quad f(m)=\cos(\pi/(2m))^{2m}.
\tag{30}
\]

No uniform polar moment assumption is needed or allowed. It is the already proved orthogonal-pair identity that transfers U to the polar. A different C changes the transported H. fileciteturn33file10L21-L39 fileciteturn33file10L43-L63

No full factor U smaller than 41/5 has been certified here. Thus for \(H=\Sigma^{1/2}M\Sigma^{1/2}\), the retained E17 constants are exactly

\[
p=57604303/9000000,\quad q=93375163/15000000,
\quad pq=5378811182126389/135000000000000<40,
\]

\[
\frac H{\operatorname{tr}H}\succ
\frac{135000000000000}{6354187649126389}I,\qquad
\frac{H^{-1}}{\operatorname{tr}H^{-1}}\succ
\frac{135000000000000}{6377875727126389}I.
\]

Both exceed I/48. These remain conditional on actual joint S1/U1; the new unconditional geometric identities do not supply its existence or nonexistence. fileciteturn44file1L25-L30

The first-layer payoff is therefore structural and exact: a low-order test removes an old common-law false candidate, degree-six identities synchronize actual boundary incidence with volume moments, and degree-16 actual moments recover the whole support geometry. The dimension-two countercontrol precisely blocks a tempting completeness shortcut. None of these conclusions changes the known minimum interval or the accepted genuine lower counterfamilies.

## 10. What was tried and the continuation point

Exploratory support/slack and oblique-probe searches did not produce a certified new universal numerical constant. Their failures are not impossibility results. The consequential change was to require compatibility of cone laws from several apices of the **same** putative body, rather than continue optimizing one radial-probe family.

The exact 18-coefficient separator was located from the least eigenvector of the displayed rational matrix, rounded by the fully specified optional locator, and then accepted by two independent rational evaluations. Exact LDL factorizations, not a floating solver verdict, certify the positive smaller blocks. The finite-support and flux statements have analytic proofs; the actual control checks their explicit realization without pretending to prove them by example.

The most useful continuation is a full-spatial first-layer moment relaxation retaining the quadratic common-law products and the true degree-six flux identities, with a complete rooted-tree packet. Staying only in the projected W,D law cannot be complete, as Section 6 proves. A failed finite relaxation remains an over-cover limitation, never an actual uniformly filled body.

## 11. Complete deterministic recovery capsule

The two source blocks below are complete standalone units, including their final LF. Both exact modes use **CPython 3.13.5 standard library only**, compatible with Python≥3.9, assertions enabled. They read no parent program, saved output, hidden table, optimizer state or external file. The optional locator inside Source A uses NumPy2.3.5, solely when `--locate` is supplied.

| Source or exact report | Bytes | SHA-256 |
|---|---:|---|
| apex_consistency_barrier.py | 10329 | 0de046064b2eb74724b9b0db4d90dbdd8d506f33abc2a53b0b8d7524864bf7a5 |
| apex_barrier_report.out | 25193 | 56c8c304a4dce457d265f8973f90c15b02cb9026df7d7e5a023d630d79cf5397 |
| finite_apex_support.py | 10656 | 74e5c6c24326ee4cdabccc8bfccbd3f8ccd578dbfb9d5ccc9125eee970496409 |
| finite_apex_support_report.out | 235374 | 716d5064c430e1b7ae96fb63e53db94e464777f9d565d2586105b57e76790d76 |

Reconstruction and exact verification:

```
python -B -S apex_consistency_barrier.py > apex_barrier_report.out
python -B -S finite_apex_support.py > finite_apex_support_report.out
```

Expected terminal markers:

```
FINITE_APEX_COMMON_LAW_BARRIER_V1 PASS
FINITE_APEX_SUPPORT_E17_V1 PASS
```

Optional deterministic locator:

```
OPENBLAS_NUM_THREADS=1 python apex_consistency_barrier.py --locate
```

It diagonalizes the 18-by-18 matrix, makes the first eigenvector coefficient positive, and rounds 100 times that vector to the literal integer test (20). The exact mode never imports NumPy. The optional locator is not a whole-domain acceptance test.

Source B generates moments by exact integration on each actual positive origin tetrahedron with outer vertices a,b,c:

\[
\int_{\operatorname{conv}(0,a,b,c)}x^\alpha dx
=\frac{\det(a,b,c)\,\alpha!}{(|\alpha|+3)!}
[z^\alpha]\prod_{v\in\{a,b,c\}}(1-v\cdot z)^{-1}.
\]

The ascending total-degree recurrence in the code reconstructs all coefficients, the 969 moments, all polynomial multipliers and isolators. The reports are outputs, not required inputs.

Normal exact execution and clean source-only extraction from these Markdown blocks both passed with byte-identical source and exact report pins. The optional locator also reproduced the literal vector. These are author executions, not coordinator replays or proof-assistant formalizations.

Convenience copies: [Source A](sandbox:/mnt/data/joint_support_v6/apex_consistency_barrier.py), [Source B](sandbox:/mnt/data/joint_support_v6/finite_apex_support.py), [A report](sandbox:/mnt/data/joint_support_v6/apex_barrier_report.out), [B report](sandbox:/mnt/data/joint_support_v6/finite_apex_support_report.out), and [complete Markdown handoff](sandbox:/mnt/data/joint_support_v6/result_markdown_v6.md).

### Source A: apex_consistency_barrier.py

```python
#!/usr/bin/env python3
"""FINITE_APEX_COMMON_LAW_BARRIER_V1: exact standalone recovery.
CPython 3.13.5, standard library only; compatible with Python >=3.9.
Run with assertions: python -B -S apex_consistency_barrier.py > apex_barrier_report.out
The five-ray input is the literal NONPHYSICAL parent law, not a uniform body.
"""
from fractions import Fraction as F
from math import factorial, gcd, lcm
from functools import lru_cache
import hashlib
import json
import sys

PARENT = 'minimum-0268'
PARENT_SHA256 = 'c199a4de7b66fb757fbc3f1b2beeb903f7002fe567611824a9f0626b32aa2fc5'
OBJECT = 'FINITE_APEX_COMMON_LAW_BARRIER_V1'
WEIGHTS = tuple(map(F, ('3/64','9/64','15/64','21/64','1/4')))
WS = tuple(map(F, ('-7/3','-13/9','-7/15','11/21','1')))
M2 = sum(t*w*w for t,w in zip(WEIGHTS,WS))
M3 = sum(t*w**3 for t,w in zip(WEIGHTS,WS))
DS = tuple((w*w-M3*w/M2-M2)/12 for w in WS)
PS = tuple(d-F(1,3) for d in DS)
ONE={(0,0):F(1)}
X={(1,0):F(1)}
Z={(0,1):F(1)}

def add(a,b):
    c=a.copy()
    for k,v in b.items(): c[k]=c.get(k,F(0))+v
    return {k:v for k,v in c.items() if v}

def scale(t,a): return {k:t*v for k,v in a.items() if t*v}

def mul(a,b):
    c={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            c[i+k,j+l]=c.get((i+k,j+l),F(0))+v*w
    return {k:v for k,v in c.items() if v}

def deriv(a,axis):
    c={}
    for ij,v in a.items():
        k=list(ij)
        if k[axis]:
            fac=k[axis];k[axis]-=1;c[tuple(k)]=fac*v
    return c

@lru_cache(None)
def moment(i,j):
    if i<0 or j<0: return F(0)
    # X=T*W, Z=1-T+T*p, T has density 3*T^2, independent of the five atoms.
    return sum((F(3*factorial(i+k+2)*factorial(j),factorial(k)*factorial(i+j+3))
                *sum(t*w**i*p**k for t,w,p in zip(WEIGHTS,WS,PS))
                for k in range(j+1)),F(0))

def mean(a): return sum((v*moment(*ij) for ij,v in a.items()),F(0))

def euler(a,apex=(F(0),F(0))):
    # Normalized endpoint functional for dimension THREE, even for these 2D tests.
    b=a.copy()
    for axis,var in enumerate((X,Z)):
        b=add(b,scale(F(1,3),mul(add(var,scale(-apex[axis],ONE)),deriv(a,axis))))
    return mean(b)

def block(k,apex):
    basis=[(i,total-i) for total in range(k+1) for i in range(total+1)]
    B=[[euler({(i+u,j+v):F(1)},apex) for u,v in basis] for i,j in basis]
    return basis,B

def ldl(B):
    n=len(B);L=[[F(int(i==j)) for j in range(n)] for i in range(n)];D=[]
    for i in range(n):
        d=B[i][i]-sum(L[i][j]**2*D[j] for j in range(i))
        assert d>0,('nonpositive pivot',i,d)
        D.append(d)
        for j in range(i+1,n):
            L[j][i]=(B[j][i]-sum(L[j][h]*L[i][h]*D[h] for h in range(i)))/d
    assert all(B[i][j]==sum(L[i][h]*D[h]*L[j][h] for h in range(n))
               for i in range(n) for j in range(n))
    return D

@lru_cache(None)
def endpoint_moment(i,j):
    return sum(t*w**i*p**j for t,w,p in zip(WEIGHTS,WS,PS))

def cross_block(k,l):
    bx=[(i,total-i) for total in range(k+1) for i in range(total+1)]
    ba=[(i,total-i) for total in range(l+1) for i in range(total+1)]
    basis=[(i,j,u,v) for i,j in bx for u,v in ba]
    B=[]
    for i,j,u,v in basis:
        row=[]
        for a,b,c,d in basis:
            I,J,U,V=i+a,j+b,u+c,v+d
            row.append(F(3+I+J,3)*moment(I,J)*endpoint_moment(U,V)
                       -F(I,3)*moment(I-1,J)*endpoint_moment(U+1,V)
                       -F(J,3)*moment(I,J-1)*endpoint_moment(U,V+1))
        B.append(row)
    return basis,B

def quadratic(B,q):
    return sum((F(q[i]*q[j])*B[i][j] for i in range(len(q)) for j in range(len(q))),F(0))


def literal(a): return [(i,j,str(v)) for (i,j),v in sorted(a.items())]

def normalize(a):
    den=1
    for v in a.values():den=lcm(den,v.denominator)
    g=0
    for v in a.values():g=gcd(g,abs(int(v*den)))
    return scale(F(den,g),a)

def serial(a):
    if isinstance(a,F):return str(a)
    if isinstance(a,dict):return {str(k):serial(v) for k,v in a.items()}
    if isinstance(a,(tuple,list)):return [serial(v) for v in a]
    return a

def projected_dimension_control():
    # A full two-dimensional probability density, not a projection of any
    # uniformly filled convex THREE-body. Its exponent-three apex tests all pass.
    rho=(F(3,13),F(0),F(3,52))
    bulk=(F(1,13),F(0),F(-1,52))
    edge=(F(1,13),F(0),F(1,52))
    def integral(coeff,shift=0):
        return sum((c*F(1-(-1)**(j+shift+1),j+shift+1)
                    for j,c in enumerate(coeff)),F(0))
    assert 2*integral(rho)==1 and 2*integral(rho,2)==F(23,65)
    assert 2*integral(bulk)==F(11,39)
    assert 4*F(5,52)==F(5,13) and 2*integral(edge)==F(1,3)
    assert F(11,39)+F(5,13)+F(1,3)==1
    fx=tuple(2*x for x in rho)
    cone=(F(27,64),F(18,64),F(3,64))
    tent=(F(3,2),F(-3),F(3,2))
    diff_upper=tuple(a-b for a,b in zip(fx,cone))
    diff_lower=tuple(a-b for a,b in zip(fx,tent))
    assert diff_upper==(F(33,832),F(-234,832),F(57,832))
    assert diff_lower==(F(-27,26),F(3),F(-18,13))
    assert rho[2]/4==F(3,208)>0
    # 1-u^2/4+a*u/2 >= 1/4 on [-1,1]^2. At a=+/-1,
    # the difference is (1+/-u)*(3-/+u)/4; interpolate linearly in a.
    return {'density_on_square':rho,'actual_mean':(0,0),
            'covariance_diagonal':(F(23,65),F(1,3)),
            'dimension':2,'Euler_exponent':3,
            'radial_endpoint_bulk_density':bulk,
            'radial_endpoint_vertical_edge_density':F(5,52),
            'radial_endpoint_horizontal_edge_density':edge,
            'bulk_and_edge_masses':(F(11,39),F(5,13),F(1,3)),
            'unnormalized_Euler_density_lower_bound':F(1,4),
            'midpoint_concavity_violation':F(3,208),
            'upper_cone_difference_coefficients':diff_upper,
            'lower_tent_difference_coefficients':diff_lower,
            'scope':'All projected exponent-three apex tests and coordinate convex orders pass; no convex three-body lift'}


def main():
    if not __debug__:raise RuntimeError('Assertions required; do not use -O')
    assert M2==F(296,315) and M3==F(-74017,99225)
    assert PS==tuple(map(F,('-376927/3356640','-223771/671328','-284887/671328',
                            '-1188667/3356640','-32591/124320')))
    assert sum(WEIGHTS)==1 and moment(1,0)==moment(0,1)==moment(1,1)==0
    delta=sum(t*d*d for t,d in zip(WEIGHTS,DS));r=1/(delta+F(1,9));a2=1/M2
    assert r/a2==F(2384557056,296272099)
    assert moment(2,0)==F(3,5)*M2 and moment(0,2)==F(3,5)/r
    Q=ONE
    for w,p in zip(WS,PS):
        Q=mul(Q,add(scale(p-1,X),scale(-w,add(Z,scale(-1,ONE)))))
    Q=normalize(Q)
    R=deriv(Q,1)
    # Exact polynomial Euler identity about (0,1), not a sampled check.
    lhs=add(mul(X,deriv(Q,0)),mul(add(Z,scale(-1,ONE)),deriv(Q,1)))
    assert lhs==scale(5,Q)
    assert mean(mul(Q,Q))==0 and mean(mul(Q,R))==0
    S=mean(mul(R,R));T=euler(mul(R,R))
    assert S>0 and euler(mul(Q,Q))==0 and euler(mul(Q,R))==S/3
    # A small rational multiple of R opens the zero-square kernel negatively.
    eps=S/(3*(abs(T)+S))
    test=add(Q,scale(-eps,R))
    defect=euler(mul(test,test))
    assert defect==-2*eps*S/3+eps*eps*T<0
    # Integer-normalized certificate is more convenient to transport.
    q=normalize(test);val=euler(mul(q,q));assert val<0
    apices=[(F(0),F(0)),(F(0),F(-1,3))]
    low=[]
    for apex in apices:
        basis,B=block(4,apex);pivots=ldl(B)
        assert len(pivots)==15
        low.append({'apex':apex,'basis':basis,'positive_LDL_pivots':pivots})
    # The old source-apex functional remains genuinely nonnegative on this square.
    original=euler(mul(q,q),(F(0),F(1)))
    endpoint=sum(t*sum(v*w**i*p**j for (i,j),v in mul(q,q).items())
                 for t,w,p in zip(WEIGHTS,WS,PS))
    assert original==endpoint>0
    # At the actual-centroid point, this is a strict degree-ten linear moment cut.
    coefficients=literal(q)
    raw=json.dumps(coefficients,separators=(',',':')).encode()
    cross_basis,B=cross_block(2,1)
    cross_q=[22,55,-8,2,1,-3,-9,-23,3,-24,-47,16,-15,-36,6,-13,-33,4]
    cross_value=quadratic(B,cross_q)
    assert cross_value < -F(7,10)
    # Independent evaluation: condition on the actual old endpoint atom.
    terms=[]
    for t,w,p in zip(WEIGHTS,WS,PS):
        pol={}
        for (i,j,u,v),co in zip(cross_basis,cross_q):
            pol=add(pol,{(i,j):F(co)*w**u*p**v})
        terms.append(euler(mul(pol,pol),(w,p)))
    assert sum(t*v for t,v in zip(WEIGHTS,terms))==cross_value
    small_basis,small_B=cross_block(1,1)
    small_pivots=ldl(small_B)
    if '--locate' in sys.argv:
        # Optional locator only. The exact main acceptance never imports NumPy.
        import numpy as np
        if np.__version__!='2.3.5': raise RuntimeError('Locator requires NumPy 2.3.5')
        eig,V=np.linalg.eigh(np.array(B,dtype=float))
        v=V[:,0]
        if v[0]<0:v=-v
        found=np.rint(100*v).astype(int).tolist()
        assert found==cross_q
        print('OPTIONAL_LOCATOR',found)
    out={'object':OBJECT,'parent':PARENT,'parent_sha256':PARENT_SHA256,
         'status':'Exact rejection of a nonphysical law; not a body counterexample',
         'atoms_mass_W_p':list(zip(WEIGHTS,WS,PS)), 'radial_apex':(0,1),
         'raw_spatial_endpoint_atoms':[(t/2,(w,sign,p)) for t,w,p in zip(WEIGHTS,WS,PS) for sign in (-1,1)],
         'dimension':3,'ratio':r/a2,'center':(0,0),
         'Q':literal(Q),'R_dQ_dz':literal(R),'S_E_R_squared':S,'T_Euler_R_squared':T,
         'epsilon':eps,'q_integer_coefficients':coefficients,'Euler_q_squared':val,
         'test_degree':5,'moment_degree':10,'old_apex_value':original,
         'coefficient_bytes':len(raw),'coefficient_sha256':hashlib.sha256(raw).hexdigest(),
         'degree_four_blocks':low,
         'cross_apex_basis':cross_basis,'cross_apex_q':cross_q,
         'cross_apex_value':cross_value,'cross_apex_conditional_values':terms,
         'cross_apex_11_positive_pivots':small_pivots,
         'cross_apex_endpoint_moment_order':4,'cross_apex_matrix_size':18,
         'all_moments_through_ten':[(i,j,moment(i,j)) for total in range(11)
                                  for i in range(total+1) for j in [total-i]],
         'projected_dimension_control':projected_dimension_control(),
         'exact_checks':'PASS'}
    print(json.dumps(serial(out),sort_keys=True,indent=2))
    print(OBJECT+' PASS')

if __name__=='__main__':main()
```

### Source B: finite_apex_support.py

```python
#!/usr/bin/env python3
"""FINITE_APEX_SUPPORT_E17_V1: actual-body polynomial support/flux audit.
CPython 3.13.5 standard library, compatible with Python >=3.9.
Run: python -B -S finite_apex_support.py > finite_apex_support_report.out
The actual raw body is the unchanged ten-vertex epsilon=1/2 bevel fixture.
No independently assigned volume or facet masses are used.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial,gcd,lcm
import hashlib,json

OBJECT='FINITE_APEX_SUPPORT_E17_V1'
PARENT='minimum-0268'
PARENT_SHA256='c199a4de7b66fb757fbc3f1b2beeb903f7002fe567611824a9f0626b32aa2fc5'
RAW=((-1,F(-1,2),-1),(1,F(-1,2),-1),(1,1,-1),(-1,1,-1),
     (-1,-1,F(-1,2)),(1,-1,F(-1,2)),(-1,-1,1),(1,-1,1),(-1,1,1),(1,2,3))
RAW=tuple(tuple(map(F,p)) for p in RAW)
M=((F(5),F(1),F(2)),(F(1),F(3),F(-1)),(F(2),F(-1),F(4)))
ZERO=(0,0,0)
ONE={ZERO:F(1)}
XS=[{tuple(int(i==j) for i in range(3)):F(1)} for j in range(3)]

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def mv(A,x):return tuple(dot(row,x) for row in A)
def inv(A):
    d=det(*A); assert d>0
    rows=(cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))
    return tuple(tuple(rows[j][i]/d for j in range(3)) for i in range(3))
def add(a,b):
    c=a.copy()
    for k,v in b.items():c[k]=c.get(k,F(0))+v
    return {k:v for k,v in c.items() if v}
def scale(c,a):return {k:c*v for k,v in a.items() if c*v}
def mul(a,b):
    c={}
    for k,v in a.items():
        for l,w in b.items():
            kl=tuple(x+y for x,y in zip(k,l));c[kl]=c.get(kl,F(0))+v*w
    return {k:v for k,v in c.items() if v}
def deriv(a,j):
    c={}
    for k,v in a.items():
        if k[j]:
            l=list(k);l[j]-=1;c[tuple(l)]=k[j]*v
    return c

def primitive_plane(n,h):
    den=1
    for x in (*n,h):den=lcm(den,x.denominator)
    vals=[int(x*den) for x in (*n,h)];g=0
    for x in vals:g=gcd(g,abs(x))
    return tuple(F(x//g) for x in vals[:3]),F(vals[3]//g)

def cycle(nodes,adj):
    first=min(nodes);second=min(adj[first]);out=[first,second]
    while len(out)<len(nodes):
        nxt=next(j for j in adj[out[-1]] if j!=out[-2])
        assert nxt not in out
        out.append(nxt)
    assert first in adj[out[-1]]
    return tuple(out)

def geometry():
    planes={}
    for a,b,c in combinations(range(10),3):
        n=cross(sub(RAW[b],RAW[a]),sub(RAW[c],RAW[a]));h=dot(n,RAW[a])
        if not any(n):continue
        sl=[h-dot(n,x) for x in RAW]
        if all(v<=0 for v in sl):n=tuple(-x for x in n);h=-h;sl=[-x for x in sl]
        if not all(v>=0 for v in sl):continue
        ids=tuple(i for i,v in enumerate(sl) if v==0)
        planes[ids]=primitive_plane(n,h)
    facesets=sorted(planes)
    assert len(facesets)==9
    edges=set()
    for a,b in combinations(facesets,2):
        meet=sorted(set(a)&set(b))
        assert len(meet)<=2
        if len(meet)==2:edges.add(tuple(meet))
    edges=sorted(edges);assert len(edges)==17
    faces=[];ns=[];hs=[]
    for ids in facesets:
        adj={i:[] for i in ids}
        for a,b in edges:
            if a in adj and b in adj:adj[a].append(b);adj[b].append(a)
        assert all(len(v)==2 for v in adj.values())
        cyc=cycle(ids,adj);n,h=planes[ids]
        if dot(n,cross(sub(RAW[cyc[1]],RAW[cyc[0]]),sub(RAW[cyc[2]],RAW[cyc[1]])))<0:
            cyc=(cyc[0],)+cyc[:0:-1]
        faces.append(cyc);ns.append(n);hs.append(h)
        assert h>0
        assert all(h-dot(n,x)==0 if i in ids else h-dot(n,x)>0 for i,x in enumerate(RAW))
    ef={e:tuple(f for f,ids in enumerate(faces) if all(i in ids for i in e)) for e in edges}
    assert all(len(v)==2 for v in ef.values())
    return faces,ns,hs,edges,ef

def all_indices(n):
    return [ (i,j,total-i-j) for total in range(n+1) for i in range(total+1) for j in range(total-i+1)]

def moments(faces,n):
    inds=all_indices(n);ints={a:F(0) for a in inds}
    # Exact rational generating series on each actual positive origin tetrahedron.
    # int_T x^a dx = det(a,b,c)*a!/(|a|+3)! * [z^a] prod_v(1-v.z)^-1.
    cells=[]
    for face in faces:
        for j in range(1,len(face)-1):
            ids=(face[0],face[j],face[j+1]);vv=[RAW[i] for i in ids]
            d=det(*vv);assert d>0;cells.append((ids,d))
            coeff={a:F(int(a==ZERO)) for a in inds}
            for v in vv:
                nxt={}
                for a in inds:
                    t=coeff[a]
                    for k in range(3):
                        if a[k]:
                            b=list(a);b[k]-=1;t+=v[k]*nxt[tuple(b)]
                    nxt[a]=t
                coeff=nxt
            for a in inds:
                fac=factorial(a[0])*factorial(a[1])*factorial(a[2])
                ints[a]+=d*F(fac,factorial(sum(a)+3))*coeff[a]
    V=ints[ZERO]
    assert len(cells)==16 and V==F(47,4)
    return V,{a:t/V for a,t in ints.items()},cells

def literal(p):return [(list(k),str(v)) for k,v in sorted(p.items())]
def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    return x

def main():
    if not __debug__:raise RuntimeError('Assertions required')
    faces,ns,hs,edges,ef=geometry()
    V,mu,cells=moments(faces,16)
    def mean(pol):return sum((v*mu[k] for k,v in pol.items()),F(0))
    def Euler_poly(a,pol):
        out=pol.copy()
        for j in range(3):out=add(out,scale(F(1,3),mul(add(XS[j],scale(-a[j],ONE)),deriv(pol,j))))
        return out
    g=tuple(mean(x) for x in XS)
    assert g==(F(4,47),F(77,282),F(125,282))
    Sigma=tuple(tuple(mean(mul(x,y))-g[i]*g[j] for j,y in enumerate(XS)) for i,x in enumerate(XS))
    slacks=[add(scale(h,ONE),scale(-1,sum_polys([scale(n[j],XS[j]) for j in range(3)]))) for n,h in zip(ns,hs)]
    weights=[];fans=[]
    for i,v in enumerate(RAW):
        inc=[f for f,ids in enumerate(faces) if i in ids]
        adj={f:[] for f in inc}
        for e,pair in ef.items():
            if i in e:
                a,b=pair;adj[a].append(b);adj[b].append(a)
        assert all(len(vv)==2 for vv in adj.values())
        cyc=cycle(inc,adj);p={};fan=[]
        for j in range(1,len(cyc)-1):
            tri=(cyc[0],cyc[j],cyc[j+1]);d=abs(det(*(ns[f] for f in tri)));assert d>0
            term=scale(d,ONE)
            for f in range(9):
                if f not in tri:term=mul(term,slacks[f])
            p=add(p,term);fan.append((tri,d))
        assert max(map(sum,p))<=6 and value(p,g)>0
        weights.append(p);fans.append(fan)
    # Exact global polynomial linear precision. No masses are fitted.
    for j in range(3):
        assert not sum_polys([mul(p,add(scale(v[j],ONE),scale(-1,XS[j]))) for p,v in zip(weights,RAW)])
    zero_checks=0
    for v,p in zip(RAW,weights):
        for a in all_indices(2):
            test=mul(p,{a:F(1)})
            assert mean(Euler_poly(v,test))==0
            zero_checks+=1
    assert zero_checks==100
    # Each degree-eight facet isolator supplies the exact corresponding row
    # of the degree-sixteen moment support envelope.
    isolators=[]
    for f in range(9):
        qf=ONE
        for j in range(9):
            if j!=f:qf=mul(qf,slacks[j])
        square=mul(qf,qf)
        A=mean(Euler_poly((F(0),)*3,square))
        B=tuple(mean(deriv(square,j))/3 for j in range(3))
        j=next(k for k in range(3) if ns[f][k])
        factor=B[j]/ns[f][j]
        assert factor>0 and A==factor*hs[f]
        assert all(B[j]==factor*ns[f][j] for j in range(3))
        isolators.append({'facet':f,'q_coefficients':literal(qf),
                          'positive_recovered_row_factor':factor,
                          'recovered_normal':B,'recovered_offset':A})
    # A fourth-moment support halfspace, using q=(z+1)^2.
    q=mul(add(XS[2],ONE),add(XS[2],ONE));q2=mul(q,q)
    c=mean(Euler_poly((F(0),)*3,q2))
    normal=tuple(mean(deriv(q2,j))/3 for j in range(3))
    assert normal[0]==normal[1]==0 and normal[2]>0
    upper=c/normal[2]
    assert upper>3 and upper>g[2]
    assert (upper-g[2])**2<15*Sigma[2][2]
    # A literal exterior point that survives the covariance ellipsoid but fails this cut.
    covcap=15*Sigma[2][2]
    dz=upper-g[2]+F(1,100)
    exterior=tuple(g[j]+dz*Sigma[j][2]/Sigma[2][2] for j in range(3))
    assert dz*dz<covcap and exterior[2]>upper
    assert mean(Euler_poly(exterior,q2))<0
    N=inv(M);assert M[0][0]>0 and M[0][0]*M[1][1]-M[0][1]**2>0
    vv=[sub(x,g) for x in RAW]
    poles=[tuple(t/(h-dot(n,g)) for t in n) for n,h in zip(ns,hs)]
    dp={(i,j):dot(vv[i],mv(M,sub(vv[j],vv[i]))) for e in edges for i,j in (e,e[::-1])}
    dual=sorted(tuple(sorted(x)) for x in ef.values())
    dq={(i,j):dot(poles[i],mv(N,sub(poles[j],poles[i]))) for e in dual for i,j in (e,e[::-1])}
    U=[i for i in range(10) if all(v<0 for (a,b),v in dp.items() if a==i)]
    S=[i for i in range(9) if all(v<0 for (a,b),v in dq.items() if a==i)]
    H=[];weak=[]
    for i,j in edges:
        a,b=ef[i,j];pr=(dp[i,j],dp[j,i],dq[a,b],dq[b,a])
        if all(v<0 for v in pr):H.append((i,j))
        elif all(v<=0 for v in pr):weak.append((i,j))
    assert not weak and all(v for v in (*dp.values(),*dq.values()))
    assert len(S)+len(U)-len(H)==2 and (len(S),len(U))!=(1,1)
    out={'object':OBJECT,'parent':PARENT,'parent_sha256':PARENT_SHA256,
         'raw_bevel_half_vertices':RAW,'maximal_facets':faces,'facet_normals':ns,'facet_offsets':hs,
         'true_edges':edges,'positive_origin_cells':cells,'volume':V,'actual_centroid':g,'actual_covariance':Sigma,
         'polar_face_fans':fans,'polynomial_apex_weights':[literal(p) for p in weights],
         'exact_flux_checks':zero_checks,'moment_order':16,'facet_isolators':isolators,
         'raw_moments_through_sixteen':[(list(a),v) for a,v in mu.items()],
         'quartic_support_q':literal(q),'quartic_support_upper_z':upper,
         'covariance_support_cap_squared':covcap,
         'covariance_only_exterior_point':exterior,'exterior_Euler_value':mean(Euler_poly(exterior,q2)),
         'physical_M':M,'physical_inverse':N,'same_origin_poles':poles,
         'strict_S_U_H':(S,U,H),'weak_edges':weak,'zero_primitives':0,'exact_checks':'PASS'}
    print(json.dumps(serial(out),sort_keys=True,indent=2))
    print(OBJECT+' PASS')

def sum_polys(polys):
    out={}
    for p in polys:out=add(out,p)
    return out

def value(p,x):return sum((v*x[0]**k[0]*x[1]**k[1]*x[2]**k[2] for k,v in p.items()),F(0))

if __name__=='__main__':main()
```
