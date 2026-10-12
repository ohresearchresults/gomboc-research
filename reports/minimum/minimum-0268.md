# minimum-0268

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# OBLIQUE_REFILL_41_OVER_5_AND_AXIAL_BARRIER_V1

## 1. Results

For every full-dimensional compact convex three-body P, uniformly filled and translated to its **actual volume centroid**, with actual covariance Σ,

\[
\boxed{\Upsilon_\Sigma(P)<\frac{41}{5}=8.2,}
\qquad
\Upsilon_C(P)=\max_{\substack{w\in P,\ n\in P^\circ\\w\cdot n=0}}
(w^TC^{-1}w)(n^TCn).
\tag{1}
\]

The polar uses the same origin. Consequently \(\inf_{C\succ0}\Upsilon_C(P)<8.2\). The bound holds in the **unchanged actual covariance reference**, not merely in a newly optimized reference.

The new mechanism uses three projective refills with coefficient pairs

\[
(\theta,\eta)=(3/10,0),\quad(3/5,-1/5),\quad(3/10,1/10).
\]

The η coordinate tilts the projective denominator toward the tested support direction. These are not three separately chosen endpoint measures: all inequalities concern **one actual radial volume law**. A cubic consequence of the full upper convex order is retained alongside the parent's quartic inequalities. Seven exact pointwise duals close **220 closed Bernstein rectangles, with 42650 strictly positive coefficient checks**.

There is a complementary exact limitation theorem. A five-atom common-law over-cover has ratio

\[
\boxed{\frac{2384557056}{296272099}=8.04853735484555\ldots>8,}
\tag{2}
\]

satisfies the complete vertical-projectivity quadratic family for **every permitted parameter**, and satisfies the full inherited lower-tent and both upper-cone convex-order comparisons in each of the two coordinate projections. Nevertheless, one transverse projective probe violates the required actual-body inequality. This is **not an actual-body lower bound**: the witness is a nonphysical probability law. It proves that extending only the old vertical probe list, even to the continuum and with those full coordinate convex orders, cannot establish a factor of 8. The transverse constraints supply genuinely additional information.

### Physical consequence on E17

For a hypothetical actual 10/17/9 joint S1/U1 body and one physical SPD metric M, put \(H=\Sigma^{1/2}M\Sigma^{1/2}\). Its ordered eigenvalues satisfy

\[
\frac{\lambda_1}{\lambda_2}<p=\frac{57604303}{9000000},\qquad
\frac{\lambda_2}{\lambda_3}<q=\frac{93375163}{15000000},
\]

\[
\boxed{\operatorname{cond}(H)<
\frac{5378811182126389}{135000000000000}
=39.8430457935288\ldots<40.}
\tag{3}
\]

Both normalized physical matrices now have the convenient floor

\[
\boxed{H/\operatorname{tr}H\succ I/48,\qquad
H^{-1}/\operatorname{tr}H^{-1}\succ I/48.}
\tag{4}
\]

The exact stronger floors and stress coefficient appear in Section 7. The condition ceiling decreases by exactly \(165/6889\), about 2.3951%, relative to the accepted 8.3-based ceiling. Incidental weak contacts are included. No E17 exclusion, new attaining 110 body, or catalogue subtraction follows merely from these stronger necessary conditions.

## 2. Input authority and verification status

I read the entire new 2023-line journal consecutively through EOF, including the literal parent. The file has **346475 bytes**, SHA-256

`eb2145264314290148edda4f3f0e9d9ffe6a665f42bb717d2003ad3f0cd86894`.

The parent is **minimum-0264**, SHA-256

`bfcc1a56683308cd9ba36d337656a9bbebb9065375f6d531d489c9f28c03c4b5`.

Its compact UTF-8 JSON envelope reconstructs to **43316 bytes** with that digest. Earlier unchanged covariance, finite-height and self-polar evidence was retained. No inaccessible exact dependency is used. The archived coordinator support theorem was not needed or reconstructed from its summary.

The inherited 8.3 theorem and actual lower counterfamilies keep their literal identities. The new sources below have been executed normally and rebuilt from the source blocks in this handoff in a clean directory. These are author exact executions and an analytic proof, not a coordinator replay or proof-assistant formalization. The accepted parent and its physical scope are recorded in the current notebook. fileciteturn30file0L45-L54

## 3. Actual-volume reduction

### Radial identities

An origin-fixing affine change and homothety give an actual body K with

\[
\mathbb E_KX=0,\qquad\operatorname{Cov}(K)=3I/5.
\]

The factor becomes \(\Upsilon_I(K)\), and is unchanged by the homothety. It is the maximum of \(\|y\|^2/h_K(-e)^2\) over unit e and \(y\in K\cap e^\perp\): the polar vector \(-e/h_K(-e)\) gives one direction of this identity, and radial extension of a polar vector gives the other. The same pair exchange proves self-polarity. fileciteturn23file7L21-L39

Choose orthonormal coordinates for a nonzero tested point so that \(y=Re_3\), with relevant support \(X_1\le a\). Polar integration about y gives

\[
X=(1-T)y+TZ,\qquad T\sim3t^2\,dt\quad(0\le t\le1),
\]

where T is independent of the **actual** far-endpoint law ν. Its angular density is \(\rho(\omega)^3/(3\operatorname{Vol}K)\). Actual first and second moments imply

\[
\mathbb E_\nu Z=-y/3,\qquad \mathbb E_\nu ZZ^T=I.
\tag{5}
\]

For the second identity, the \(yy^T\) terms cancel because
\(\mathbb E(1-T)^2-(2/3)\mathbb E[T(1-T)]=1/10-(2/3)(3/20)=0\).
Applying (5) at any point gives \(K\subset3B\).

### The two inherited convex-order comparisons

For a centered scalar coordinate with upper support a, section concavity gives the upper comparison

\[
\mathbb E\varphi(X_1)\le
\int_{-3a}^{a}\varphi(x)\frac{3(x+3a)^2}{64a^3}\,dx
\quad(\varphi\text{ convex}).
\tag{6}
\]

Here is the argument, including its actual-body content. Rays from a support-minimizing point give the centroid reflection inequality \(-\min X_1\le3a\). The square root of the actual scalar density is concave by planar Brunn–Minkowski. Subtracting the affine square root of the comparison density gives a concave function, so the density difference has sign pattern nonpositive, nonnegative, nonpositive. Subtract the chord of φ across its positive interval; the product has nonpositive sign. The affine part integrates to zero by the common mass and mean. In particular (6) gives a≥1. This is the section argument in the supplied covariance source. fileciteturn23file11L42-L66

For true scalar support \([-b,h]\), the parent's lower comparison is against the centered squared tent with peak at \(c=(b-h)/2\):

\[
\tau_{b,h}(x)=\frac3{b+h}
\begin{cases}
((x+b)/(c+b))^2,&-b\le x\le c,\\
((h-x)/(h-c))^2,&c\le x\le h.
\end{cases}
\tag{7}
\]

Zero-length legs are omitted. Centroid reflection puts c inside the support. The difference of square roots is concave on each leg; unless the densities coincide, their difference has sign pattern nonnegative, nonpositive, nonnegative. The same chord argument proves \(\tau_{b,h}\preceq_{cx}\mathcal L(X)\). Direct integration yields

\[
40\operatorname{Var}(X)\ge3h^2-2hb+3b^2.
\tag{8}
\]

This is an inherited theorem, not a new claim of priority. The complete parent proof and its equality calibration are in the supplied payload. fileciteturn30file0L173-L225

### Common coordinates and support rectangle

Set

\[
r=R^2,\quad W=Z_1/a,\quad D=Z_3/R+1/3,
\quad\delta=\mathbb E_\nu D^2=1/r-1/9.
\]

Then

\[
\mathbb EW=\mathbb ED=\mathbb EWD=0,\quad
\mathbb EW^2=1/a^2\le1,\quad -3\le W\le1.
\tag{9}
\]

Suppose for contradiction \(r/a^2\ge C=41/5\). Therefore

\[
C\le r\le9,\qquad0\le\delta\le4/369,
\qquad\mathbb EW^2\ge C(\mathbb ED^2+1/9).
\tag{10}
\]

Apply (8) vertically, where actual h≥R and b≤3. Since \(R>1\), the expression in (8) increases with h on h≥R. Hence

\[
3R^2-2Rb+3b^2\le24,
\quad b/R\le1/3+\sqrt{8\delta},
\quad D\ge-\sqrt{8\delta}.
\]

Also \(D\le1/3+3/\sqrt C\). Thus the whole contrary sector is contained in the closed rectangle

\[
\boxed{\mathcal R=[-3,1]\times[-3/10,7/5].}
\tag{11}
\]

The exact checks are \((3/10)^2>32/369\) and \((7/5-1/3)^2>45/41\).

## 4. Eight common polynomial inequalities and oblique refill

Define, in this order,

\[
A_0=W^2-CD^2-C/9,\qquad A_1=1-W^2,
\]

\[
A_{2+j}=13/5+8k_j/5+54k_j^2/35-W^4+2k_jW^3-(54/35)k_j^2W^2,
\]

with \((k_0,k_1,k_2,k_3,k_4)=(-3/2,-1,-3/4,-1/2,0)\), and

\[
\boxed{A_7=22/5-(18/5)W^2+W^3.}
\tag{12}
\]

All eight have nonnegative expectation under the actual ν. The first two follow from (9)-(10). For the quartics apply (6) to
\(\psi_k(x)=(7/3)x^4-4kx^3+(18/7)k^2x^2\), whose second derivative is \(28(x-3k/7)^2\). The standardized reference moments through order four are \(1,0,3/5,-2/5,39/35\); radial moments are \(\mathbb ET^j=3/(j+3)\).

The cubic is a further consequence of the **full** comparison, not a separately assigned third moment. The function \((1-x)^3\) is convex on \([-3,1]\), and its reference expectation is 16/5. Since \(X_1/a=TW\),

\[
1+(9/5)\mathbb EW^2-(1/2)\mathbb EW^3\le16/5,
\]

which is precisely \(\mathbb EA_7\ge0\).

For any θ,η with a positive denominator, use the actual convex projective image

\[
K_{\theta,\eta}=
\left\{\frac{x}{1+(\eta/a)x_1+(\theta/R)x_3}:x\in K\right\}
\]

and fill this image **uniformly**. Put

\[
g=1-\theta/3+\theta D+\eta W,
\quad f=1-W,
\quad M_j=\mathbb E_\nu\frac{f^j}{g^{3+j}}.
\tag{13}
\]

Its Jacobian is denominator−4. Along an old ray, let \(A=1+\theta\), \(B=g(Z)\), \(d(t)=A+(B-A)t\). The new radial parameter is \(t'=tB/d(t)\), and

\[
\frac{3t^2}{d(t)^4}\,dt=\frac{3(t')^2}{AB^3}\,dt'.
\tag{14}
\]

Thus the new endpoint law is exactly ν reweighted by B−3 and normalized by M0. The actual volume ratio is \(M_0/A\); its actual centroid is

\[
\frac{y}{4A}+\frac{3}{4M_0}\mathbb E_\nu\frac Z{B^4}.
\]

No new centroid is prescribed. In particular, this is not a pushforward of old uniform probability without the Jacobian correction.

The transformed nonnegative affine slack is

\[
u_{\theta,\eta}(x')=1-(1+\eta)x'_1/a-(\theta/R)x'_3.
\]

Its apex value is \(c_\theta=1/(1+\theta)\), and its endpoint value is f/B. On any uniformly filled convex three-body, (6), applied after subtracting its actual centroid to \(\mathbb Eu-u\), gives the affine Berwald inequality \(16(\mathbb Eu)^2\ge10\mathbb Eu^2\). The first two radial slack moments are \((c_\theta+3m)/4\) and \((c_\theta^2+3c_\theta m+6q)/10\), with \(m=M_1/M_0,q=M_2/M_0\). Consequently

\[
\boxed{3M_1^2+c_\theta M_0M_1-2M_0M_2\ge0.}
\tag{15}
\]

This is the oblique extension of the parent's family. Each instance remains an inequality about the **same original ν**.

If \(l\le M_1/M_0\le u\), the square secant implies

\[
\mathbb EG\ge0,\qquad
G=[3(l+u)+c_\theta]f/g^4-3lu/g^3-2f^2/g^5.
\tag{16}
\]

The exact probes and caps are:

| i | θ | η | l | u | Minimum g on the entire rectangle |
|---|---:|---:|---:|---:|---:|
| 0 | 3/10 | 0 | 27501/25000 | 114863/100000 | 81/100 |
| 1 | 3/5 | −1/5 | 59513/100000 | 14861/20000 | 21/50 |
| 2 | 3/10 | 1/10 | 173513/100000 | 35149/20000 | 51/100 |

All projective maps therefore stay uniformly away from their horizons in the proof.

## 5. Exact finite separation and proof of (1)

For each probe let \(g_i\) be (13), \(G_i\) be (16) using its displayed caps, and define objectives

\[
J_{L_i}=f/g_i^4-l_i/g_i^3,\quad
J_{U_i}=u_i/g_i^3-f/g_i^4,\quad J_F=-G_2.
\]

Set \(E=(W,D,WD)\). The seven integer rows **DUALS** in Source A below are the complete literal certificate. Their common denominator is \(10^9\). For the two rows with subscript i, the nonnegative multiplier vector λ acts on

\[
\Phi_i=(A_0,\ldots,A_7,G_0,\ldots,G_{i-1});
\]

for the final row it acts on \(\Phi_2\). The unrestricted vector α acts on E. The source proves, pointwise throughout the **whole closed rectangle** (11),

\[
\boxed{J-10^{-9}(\lambda\cdot\Phi_i+\alpha\cdot E)>10^{-6}.}
\tag{17}
\]

No coefficients or row normalizations are omitted: every integer is literal in Source A. They are dual multipliers, not volume masses.

To reconstruct the polynomials, clear the denominators \(g_j^5\) used by that row. The numerator of \(G_j\) is

\[
[3(l_j+u_j)+c_{\theta_j}]fg_j-3l_ju_jg_j^2-2f^2.
\]

The lower-cap numerator is \(g_i(f-l_ig_i)\), and the upper-cap numerator is \(g_i(u_ig_i-f)\). Subtract the dual terms and \(10^{-6}\) times the common denominator. Every common denominator is strictly positive by the table.

The resulting seven rational polynomials have the following complete exact acceptance:

| Row | Bidegree in (W,D) | Closed leaves | Maximum depth | Strictly positive coefficient checks |
|---|---:|---:|---:|---:|
| L0 | (4,7) | 6 | 5 | 240 |
| U0 | (4,7) | 23 | 8 | 920 |
| L1 | (9,12) | 36 | 11 | 4680 |
| U1 | (9,12) | 36 | 11 | 4680 |
| L2 | (14,17) | 53 | 11 | 14310 |
| U2 | (14,17) | 26 | 9 | 7020 |
| FINAL | (14,17) | 40 | 10 | 10800 |
| **Total** | | **220** | **11** | **42650** |

For completeness, on an affine unit-square parametrization, power coefficients \(a_{k\ell}\) of bidegree (n,m) convert to Bernstein coefficients

\[
b_{ij}=\sum_{k\le i,\ell\le j}a_{k\ell}
\frac{\binom{i}{k}}{\binom n k}\frac{\binom j\ell}{\binom m\ell}.
\]

The source checks the inverse power reconstruction exactly. Midpoint de Casteljau subdivision preserves the polynomial and splits into two **closed** children. The splitting coordinate has the larger maximum adjacent coefficient difference, with W winning ties. All terminal coefficients are strictly positive. Depth 32 or 200000 nodes without proof raises an error; neither limit is approached. There are 433 total nodes. No infeasible-cell pruning or sampled acceptance is used.

Now integrate the two i=0 inequalities in (17). Equations (9), (12) give the strict first caps, and (15) then gives \(\mathbb EG_0\ge0\). Repeat for i=1 and i=2, using the previously derived common-law inequalities. Thus \(\mathbb EG_2\ge0\). The final row instead gives \(-\mathbb EG_2>10^{-6}\), a contradiction.

This excludes \(r/a^2\ge41/5\), including equality. Compactness of the orthogonal-pair set proves (1). The proof applies to every actual compact convex body of positive volume, not just polytopes, and includes a=1 and R=3. No extremizer or sharpness claim is made.

## 6. Exact obstruction to vertical-only continuation

### A precisely specified nonphysical over-cover

Use the following five atoms (ω,W,p):

| ω | W | p |
|---:|---:|---:|
| 3/64 | −7/3 | −376927/3356640 |
| 9/64 | −13/9 | −223771/671328 |
| 15/64 | −7/15 | −284887/671328 |
| 21/64 | 11/21 | −1188667/3356640 |
| 1/4 | 1 | −32591/124320 |

A compact deterministic generator explains these exact values. On W∈[−3,1], take density \(3(W+3)/32\) and an additional atom of mass 1/4 at W=1. Replace W on each of the four unit subintervals by its conditional mean; retain the atom. With the resulting \(m_j=\mathbb EW^j\), define

\[
D=(W^2-(m_3/m_2)W-m_2)/12,\qquad p=D-1/3.
\]

Then

\[
m_2=296/315,\quad m_3=-74017/99225,\quad
\delta=\mathbb ED^2=14314339/2537619840,
\]

\[
\mathbb EW=\mathbb ED=\mathbb EWD=0,
\quad r=\frac{2537619840}{296272099},\quad a^2=\frac{315}{296},
\quad r/a^2=\frac{2384557056}{296272099}>8.
\tag{18}
\]

It has \(m_2<1\), \(\min D> -\sqrt{8\delta}\), and every endpoint satisfies \(a^2W^2+1+rp^2<9\). Every real-parameter quartic inequality in (12), not just the five selected ones, and the cubic inequality hold strictly.

There is even a full three-dimensional **formal second-moment completion**: give each raw endpoint \((W,\pm1,p)\) weight ω/2, use raw apex \((0,0,1)\), and the independent radial parameter T with density 3t². This probability law has mean zero and covariance

\[
\operatorname{diag}((3/5)m_2,3/5,3/(5r)).
\]

Scaling by \(\operatorname{diag}(a,1,\sqrt r)\) gives the same radial first/second identities and covariance 3I/5 as the actual-body normalization, while retaining outer radius below 3.

**It is not uniform volume in a convex body.** Its spatial probability is supported on ten line segments. Its two-coordinate projection is supported on five segments, whereas the projection of uniform volume from a full-dimensional convex three-body is absolutely continuous on a set of positive area. The convex hull of its marks is not a license to substitute these weights for that hull's actual volume. Thus (18) is not an actual-body counterexample to a factor of 8.

### Full coordinate convex orders are retained

Let \(U=TW\), \(V=1-T+Tp\). Their supports are respectively

\[
[-7/3,1],\qquad[-284887/671328,1].
\]

Each scalar law dominates its centered squared tent (7), and is dominated by both applicable one-sided upper cones (6), one for each sign of the coordinate. These are full convex-order assertions, not just moment tests.

There is a simple analytic reason for the horizontal positive-side upper comparison. Let W₀ have the uncoarsened endpoint law. Direct integration shows that TW₀ has density \(3(x+3)^2/64\) on [−3,1]. Conditional Jensen, independently of T, shows that replacing W₀ by its conditional means decreases every convex scalar expectation. The other comparisons are certified below without relying on a guessed concave density.

Here is the complete exact acceptance recipe. For a radial scalar \(c+T(z-c)\), its stop-loss \(\mathbb E(s-X)_+\) is zero below both endpoints, \(s-(c+3z)/4\) above both endpoints, and between them is

\[
\frac{(s-c)^4}{4(z-c)^3}\quad(c<s<z),
\]

or

\[
s-c+3(c-z)/4+\frac{(c-s)^4}{4(c-z)^3}\quad(z<s<c).
\]

Sum these functions with the literal weights. The upper-cone stop-loss on \([-3h,h]\) is \((s+3h)^4/(256h^3)\) inside its support, with outer pieces 0 and s. The opposite upper comparison is this formula for b at −s, plus s. The lower-tent stop-loss is obtained by integrating its two quadratic-density legs.

All breakpoints are rational. Source B partitions at every endpoint and tent peak and proves all three quartic differences nonnegative. There are **48 polynomial comparisons, 50 closed leaves and 218 nonnegative coefficient checks**. The midpoint selects only the polynomial formula between consecutive known knots; it is not a sampled sign test. The outer tails agree identically. Equal means and the stop-loss representation of a convex function prove the full assertions for every convex test function.

### Every vertical probe passes, but a transverse probe fails

For η=0, all permitted denominators for the formal support marks are positive exactly on

\[
-1<\theta<\Theta:=671328/284887.
\]

For **every** θ in that open interval, this same measure satisfies strictly

\[
3M_1(\theta)^2+M_0(\theta)M_1(\theta)/(1+\theta)
-2M_0(\theta)M_2(\theta)>0.
\tag{19}
\]

This is an exact whole-interval theorem. Put \(g_i=1+\theta p_i\), \(Q=\prod_i g_i^5\), and

\[
A_j=\sum_i\omega_i(1-W_i)^j g_i^{2-j}\prod_{\ell\ne i}g_\ell^5.
\]

Then \(M_j=A_j/Q\). The polynomial

\[
P(\theta)=\frac{(1+\theta)(3A_1^2-2A_0A_2)+A_0A_1}
{\prod_i g_i^2}
\tag{20}
\]

is exactly of degree 33; the division is exact. All 34 Bernstein coefficients are strictly positive on each of the two closed intervals

\[
[-1,(\Theta-1)/2],\qquad[(\Theta-1)/2,\Theta].
\]

The **68 positive coefficients**, full polynomial, and exact division identity regenerate in Source B. Equation (20) proves (19) on the permitted open interval, including arbitrarily close approaches to either horizon. No endpoint body realization is asserted.

In contrast, take the purely horizontal projectivity η=−3/5, θ=0. Its endpoint denominators are at least 2/5, but

\[
\boxed{3M_1^2+M_0M_1-2M_0M_2
=-\frac{3450181886488350318828125}{14194917943690523037401088}<0.}
\tag{21}
\]

Thus the transverse actual-refill condition removes this law. Equations (18)-(21) establish the claimed limitation of the vertical-only over-cover and strict additional power of non-collinear probes. They neither raise the known actual-body lower bound nor prove that all oblique moment constraints characterize actual convex volume.

## 7. Exact joint windows, weak contacts and scope

Self-polarity is the identity \(\Upsilon_C(P)=\Upsilon_{C^{-1}}(P^\circ)\), obtained by exchanging the actual orthogonal pair. It does **not** assert that the polar is uniformly centered. In the actual covariance reference, the two physical matrices are H and its same-origin inverse. The supplied true-edge finite-height argument therefore gives

\[
\lambda_1/\lambda_2<(41/5)f(h+1),\qquad
\lambda_2/\lambda_3<(41/5)f(k+1),
\quad f(m)=\cos(\pi/(2m))^{2m}.
\tag{22}
\]

U1 supplies the first tree; S1 supplies the polar tree. A distinct nonnegative arrow strictly increases quadratic norm, so extra weak contacts do not defeat either tree. No positive-arrow-only assumption has been added. fileciteturn23file7L43-L63

At V=10,F=9, use h≤9,k≤8 and the exact inherited majorants \(p_0=7024915/10^6>9f(10)\), \(q_0=6832329/10^6>9f(9)\). Source A rechecks them using rational Machin and cosine bounds. Multiplication by 41/45 gives p and q in (3).

Let \(D_H=pq+q+1\), \(D_{H^{-1}}=pq+p+1\). The exact trace windows are

\[
\frac{135000000000000}{6354187649126389}I
\prec\frac H{\operatorname{tr}H}
\prec\frac{5378811182126389}{6354187649126389}I,
\]

\[
\frac{135000000000000}{6377875727126389}I
\prec\frac{H^{-1}}{\operatorname{tr}H^{-1}}
\prec\frac{5378811182126389}{6377875727126389}I.
\tag{23}
\]

With \(\tau=\operatorname{tr}(\Sigma M)\), the primal version in original coordinates is

\[
D_H\Sigma M\Sigma-\tau\Sigma\succ0,
\qquad pq\,\tau\Sigma-D_H\Sigma M\Sigma\succ0.
\]

The exact stress coefficient becomes

\[
\boxed{\alpha=\frac1{D_H-3}
=\frac{135000000000000}{5949187649126389}>\frac1{45}.}
\tag{24}
\]

In particular the rounded floor I/48 permits the convenient sufficient stress test
\(Q+(1/45)\operatorname{tr}(\Sigma^{-1}Q)\Sigma\succ0\), where Q is the negative weighted sum of the true primal arrow tensors. Under hypothetical joint S1/U1 it forces some selected arrow to be negative. This uses the existing floor-dual identity; it is not an all-SPD U2 assertion. fileciteturn23file12L59-L71

For arbitrary finite f-vector joint S1/U1 polytopes, the common adjacent cap is 41/5, condition is below 1681/25, and both normalized matrices have the common window

\[
(25/1911)I\prec H/\operatorname{tr}H\prec(1681/1911)I,
\]

and the analogous window for the normalized inverse. For Euclidean physical M=I and only a homothety making \(\operatorname{tr}\Sigma=1\),

\[
\sqrt{125/5733}\,B\subset P\subset\sqrt{8405/637}\,B,
\]

with radius ratio strictly below 123/5. These follow from the actual covariance sandwich; an anisotropic physical-metric reset is not made. fileciteturn23file11L68-L82

The universal maxima over covariance-normalized bodies remain attained, by the retained compact sandwich and moment continuity. Thus the current strict brackets are

\[
6.131145332531<C_{\rm covariance}<8.2,
\qquad 5.088862048<\mathcal U_3<8.2.
\]

The lower endpoints are inherited actual-body results, not the nonphysical number in (18). The literal pyramid P0, simplicial bipyramid controls and cut/cut/stack E17 family are unchanged. fileciteturn29file0L165-L169 fileciteturn30file0L14-L20

## 8. What was tried and what remains

The useful change was to allow projective denominators with a genuine support-direction component and to retain their consequences on the same endpoint law. The cubic constraint is especially inexpensive. Repeating vertical probes alone has a rigorous limitation at factor 8, even after the specified full coordinate convex-order comparisons: Section 6 is an exact over-cover obstruction, not a numerical failure promoted to a body.

Exploratory larger probe and moment lists did not establish a stronger certified universal constant than the one returned here. No conclusion of feasibility or impossibility is drawn from those failures. The full oblique hierarchy, the sharp geometric constant, and a direct relation to true escape-path configurations remain unresolved by this result.

No regional atlas has been rerun with the new floor, and no equilibrium census is transferred through an auxiliary projective refill. A change of auxiliary reference still changes the transported physical matrix. The minimum bracket **34≤C_min≤622**, all root/incidence counts, and the attaining upper construction are unchanged. fileciteturn23file0L10-L11

The most useful continuation is to couple additional actual directional support information or true path vertices to the oblique common-law tests. Section 6 identifies exactly why supplying more tests in only the old vertical direction cannot replace that missing geometry.

## 9. Complete deterministic recovery

All continuation-critical exact data are in the three complete source blocks below. Sources A and B are independent **CPython 3.13.5 standard-library** programs, written for Python≥3.9; assertions must be enabled. Neither reads a parent program, saved table, locator output or external data. Source C preserves the optional numerical locator with every non-default parameter; it is not an acceptance test.

| Source / output | Bytes | SHA-256 |
|---|---:|---|
| oblique_refill_41_over_5.py | 12520 | 885919926b6d4b729aef8e68f66acb3e166ae627c7af5760c810a4de40cad305 |
| oblique_refill_report.out | 54479 | d1416021d1e05dfc6bdfd34c6d68644533f9e4c62745227d8dfdc1038f42e0b1 |
| axial_common_law_barrier.py | 9928 | 171380865e772646dd8c0c29e551588020963a219e61febd78a537ef764217d7 |
| axial_barrier_report.out | 45807 | bd6914645bcee0524861103d158112d8a415753670b78c3e60a45d0f6b72f37c |
| locate_oblique_duals.py | 2897 | 4a5326bdd22acbafb55e0645a32e2e9c81effe6c09182f3ce69e034a6ce74449 |
| located_duals.json | 2154 | 71bf7fa775743b26e10fe49946ee2be3ae6afad5aaf0d80da42295002eb4ebc9 |

Commands:

```
python -B -S oblique_refill_41_over_5.py > oblique_refill_report.out
python -B -S axial_common_law_barrier.py > axial_barrier_report.out
```

Expected final markers:

```
OBLIQUE_REFILL_41_OVER_5_V1 PASS
AXIAL_COMMON_LAW_BARRIER_ABOVE_EIGHT_V1 PASS
```

Optional locator command, pinned to NumPy2.3.5/SciPy1.17.0:

```
OPENBLAS_NUM_THREADS=1 python locate_oblique_duals.py > located_duals.json
```

Its exact saved output reproduces the literal caps and duals in Source A. Floating linear programs only locate candidates; the whole-domain rational checks in A are the acceptance. Both exact programs and the optional locator were regenerated from the blocks below in a clean directory, and all outputs matched byte-for-byte. No independent coordinator replay is claimed.

The reports include the complete regenerated polynomial coefficient arrays, cover paths, exact minima, moments and spectral constants. Their hashes are pins, not substitutes for data: every array regenerates from the literal source without a download.

Convenience copies: [Source A](sandbox:/mnt/data/joint_support_v5/oblique_refill_41_over_5.py), [Source B](sandbox:/mnt/data/joint_support_v5/axial_common_law_barrier.py), [Source C](sandbox:/mnt/data/joint_support_v5/locate_oblique_duals.py), [A report](sandbox:/mnt/data/joint_support_v5/oblique_refill_report.out), [B report](sandbox:/mnt/data/joint_support_v5/axial_barrier_report.out), [locator output](sandbox:/mnt/data/joint_support_v5/located_duals.json), and [Markdown handoff](sandbox:/mnt/data/joint_support_v5/result_markdown_v5.md).

### Source A: oblique_refill_41_over_5.py

```python
#!/usr/bin/env python3
"""OBLIQUE_REFILL_41_OVER_5_V1, exact standalone acceptance.
CPython 3.13.5 standard library; compatible with Python >=3.9.
Run: python -B -S oblique_refill_41_over_5.py > oblique_refill_report.out
No files, numerical locators, random choices, or external inputs are read.
The accompanying handoff proves the actual-volume reduction.
"""
from fractions import Fraction as F
from math import comb, factorial, gcd, lcm
import hashlib
import json

OBJECT = 'OBLIQUE_REFILL_41_OVER_5_V1'
PARENT = 'minimum-0264'
PARENT_SHA256 = 'bfcc1a56683308cd9ba36d337656a9bbebb9065375f6d531d489c9f28c03c4b5'
C = F(41, 5)
DLO, DHI = F(-3, 10), F(7, 5)
EPS, DEN = F(1, 1000000), 1000000000
KS = (F(-3, 2), F(-1), F(-3, 4), F(-1, 2), F(0))
PROBES = ((F(3, 10), F(0)), (F(3, 5), F(-1, 5)), (F(3, 10), F(1, 10)))
CAPS = ((F(27501, 25000), F(114863, 100000)),
        (F(59513, 100000), F(14861, 20000)),
        (F(173513, 100000), F(35149, 20000)))
# All integer multipliers below have denominator DEN.
# Base order: target, inner, the five quartics in KS order, cubic.
# Later rows append G0, then G1. Equality order: W,D,WD.
DUALS = (
    ('L0', (133503410, 133298562, 211493, 0, 0, 0, 0, 0),
     (-1524200325, -514787840, 2051567280)),
    ('U0', (436940820, 364621878, 4559284, 0, 0, 0, 0, 14438139),
     (1524615433, 475605176, -2138160658)),
    ('L1', (7083047871, 0, 504949423, 0, 0, 0, 0, 0, 2003188643),
     (8886198150, -1266518848, 2560257142)),
    ('U1', (8295611361, 0, 0, 0, 0, 0, 63243338, 557651638, 1239900866),
     (7367268640, 478012277, -1646448546)),
    ('L2', (5564314681, 0, 0, 0, 0, 0, 67646766, 0, 1147474994, 134417052),
     (4026120541, -1785334834, 4384598486)),
    ('U2', (3056562621, 0, 0, 0, 0, 0, 186928338, 0, 1052396596, 11481160),
     (6536271982, 991049449, -3490584754)),
    ('FINAL', (55049087925, 0, 0, 0, 0, 0, 683126910, 0, 13824239587, 1360614880),
     (78169734640, -3968872911, 4899046851)),
)
ONE, W, D = {(0, 0): F(1)}, {(1, 0): F(1)}, {(0, 1): F(1)}


def add(a, b):
    c = a.copy()
    for k, v in b.items():
        c[k] = c.get(k, F(0)) + v
    return {k: v for k, v in c.items() if v}

def scale(t, a):
    t = F(t)
    return {k: t*v for k, v in a.items() if t*v}

def mul(a, b):
    c = {}
    for (i, j), x in a.items():
        for (k, ell), y in b.items():
            key = (i+k, j+ell)
            c[key] = c.get(key, F(0)) + x*y
    return {k: v for k, v in c.items() if v}

def power(a, n):
    if n < 0:
        raise ValueError('Nonnegative polynomial power required')
    b = ONE
    for unused in range(n):
        b = mul(b, a)
    return b

def degree(p):
    return max(i for i, j in p), max(j for i, j in p)

def bernstein(p, wl, wh, dl, dh):
    """Full tensor power-to-Bernstein conversion, with exact inverse audit."""
    nw, nd = degree(p)
    aa = [[F(0)]*(nd+1) for unused in range(nw+1)]
    for (i, j), c in p.items():
        for k in range(i+1):
            for ell in range(j+1):
                aa[k][ell] += (c*comb(i, k)*comb(j, ell)*wl**(i-k)
                              *(wh-wl)**k*dl**(j-ell)*(dh-dl)**ell)
    bb = [[sum((aa[k][ell]*F(comb(i, k), comb(nw, k))
                *F(comb(j, ell), comb(nd, ell))
                for k in range(i+1) for ell in range(j+1)), F(0))
           for j in range(nd+1)] for i in range(nw+1)]
    for i in range(nw+1):
        for j in range(nd+1):
            recovered = comb(nw, i)*comb(nd, j)*sum(
                ((-1)**(i-k+j-ell)*comb(i, k)*comb(j, ell)*bb[k][ell]
                 for k in range(i+1) for ell in range(j+1)), F(0))
            assert recovered == aa[i][j]
    return bb

def split_line(a):
    levels = [a]
    while len(levels[-1]) > 1:
        p = levels[-1]
        levels.append([(p[i]+p[i+1])/2 for i in range(len(p)-1)])
    return [p[0] for p in levels], [p[-1] for p in levels[::-1]]

def split_grid(b, axis):
    if axis == 1:
        pairs = [split_line(row) for row in b]
        return [x[0] for x in pairs], [x[1] for x in pairs]
    left, right = split_grid([list(x) for x in zip(*b)], 1)
    return [list(x) for x in zip(*left)], [list(x) for x in zip(*right)]

def primitive_coefficients(p):
    den = 1
    for c in p.values():
        den = lcm(den, c.denominator)
    nums = {k: int(c*den) for k, c in p.items()}
    common = 0
    for c in nums.values():
        common = gcd(common, abs(c))
    assert common > 0
    nw, nd = degree(p)
    rows = [[nums.get((i, j), 0)//common for j in range(nd+1)]
            for i in range(nw+1)]
    raw = json.dumps(rows, separators=(',', ':')).encode()
    return {'ascending_W_then_D': rows, 'raw_denominator_lcm': den,
            'raw_integer_gcd': common, 'coefficient_json_bytes': len(raw),
            'coefficient_json_sha256': hashlib.sha256(raw).hexdigest()}

def integrate_w(p, lo, hi):
    assert all(j == 0 for i, j in p)
    return sum((c*(hi**(i+1)-lo**(i+1))/(i+1)
                for (i, j), c in p.items()), F(0))

def atan_interval(inv, terms=30):
    x = F(1, inv)
    a = sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(terms)), F(0))
    b = a+(-1)**terms*x**(2*terms+1)/(2*terms+1)
    return min(a, b), max(a, b)

def cos_upper(x):
    assert 0 < x < 1
    return sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(5)), F(0))

def serial(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [serial(v) for v in x]
    return x

def prove_positive(poly):
    nw, nd = degree(poly)
    todo = [(bernstein(poly, F(-3), F(1), DLO, DHI), 0, '')]
    leaves, nodes, depth, minimum = [], 0, 0, None
    while todo:
        b, dep, path = todo.pop()
        nodes += 1
        mn = min(map(min, b))
        if mn > 0:
            leaves.append(path)
            depth = max(depth, dep)
            minimum = mn if minimum is None else min(minimum, mn)
            continue
        if dep >= 32 or nodes >= 200000:
            raise ArithmeticError('Unclosed Bernstein rectangle: '+path)
        dw = max(abs(b[i+1][j]-b[i][j])
                 for i in range(nw) for j in range(nd+1))
        dd = max(abs(row[j+1]-row[j]) for row in b for j in range(nd))
        axis = 0 if dw >= dd else 1
        left, right = split_grid(b, axis)
        letter = 'W' if axis == 0 else 'D'
        todo.append((right, dep+1, path+letter+'1'))
        todo.append((left, dep+1, path+letter+'0'))
    assert nodes == 2*len(leaves)-1 and minimum > 0
    return {'degree': (nw, nd), 'leaves': leaves, 'nodes': nodes,
            'maximum_depth': depth, 'minimum_bernstein': minimum,
            'positive_coefficients': len(leaves)*(nw+1)*(nd+1)}


def main():
    if not __debug__:
        raise RuntimeError('Assertions are required; do not use -O')
    delta_max = 1/C-F(1, 9)
    assert delta_max == F(4, 369) and C > 1
    assert DLO < 0 and DLO**2 > 8*delta_max
    assert DHI-F(1, 3) > 0 and (DHI-F(1, 3))**2 > 9/C
    density = scale(F(3, 64), power(add(W, scale(3, ONE)), 2))
    moments = [integrate_w(mul(power(W, j), density), F(-3), F(1))
               for j in range(5)]
    assert moments == [1, 0, F(3, 5), F(-2, 5), F(39, 35)]
    base = [add(add(power(W, 2), scale(-C, power(D, 2))), scale(-C/9, ONE)),
            add(ONE, scale(-1, power(W, 2)))]
    for k in KS:
        psi = add(add(scale(F(7, 3), power(W, 4)), scale(-4*k, power(W, 3))),
                  scale(F(18, 7)*k*k, power(W, 2)))
        radial = {(i, j): x*F(3, i+3) for (i, j), x in psi.items()}
        ref = integrate_w(mul(psi, density), F(-3), F(1))
        assert ref == F(13, 5)+F(8, 5)*k+F(54, 35)*k*k
        base.append(add(scale(ref, ONE), scale(-1, radial)))
    f = add(ONE, scale(-1, W))
    psi = power(f, 3)
    radial = {(i, j): x*F(3, i+3) for (i, j), x in psi.items()}
    ref = integrate_w(mul(psi, density), F(-3), F(1))
    assert ref == F(16, 5)
    cubic = add(add(scale(F(22, 5), ONE), scale(-F(18, 5), power(W, 2))), power(W, 3))
    assert cubic == add(scale(2, add(scale(ref, ONE), scale(-1, radial))), scale(-F(9, 2), W))
    base.append(cubic)
    gs = [add(add(scale(1-t/3, ONE), scale(t, D)), scale(e, W)) for t, e in PROBES]
    minima = [min(1-t/3+t*d+e*w for d in (DLO, DHI) for w in (F(-3), F(1)))
              for t, e in PROBES]
    assert minima == [F(81, 100), F(21, 50), F(51, 100)]
    g5 = [power(g, 5) for g in gs]
    secants = []
    for (t, e), g, (lo, up) in zip(PROBES, gs, CAPS):
        assert 0 < lo < up and 1+t > 0
        secants.append(add(add(scale(3*(lo+up)+1/(1+t), mul(f, g)),
                                scale(-3*lo*up, power(g, 2))), scale(-2, power(f, 2))))
    equalities = (W, D, mul(W, D))
    reports = []
    for name, weights, alpha in DUALS:
        i = 2 if name == 'FINAL' else int(name[1:])
        assert len(weights) == 8+i and all(x >= 0 for x in weights)
        assert len(alpha) == 3
        active = {i} | {j for j, n in enumerate(weights[8:]) if n}
        assert all(j <= i for j in active)
        denominator = ONE
        for j in sorted(active):
            denominator = mul(denominator, g5[j])
        def cleared(numerator, j):
            for k in sorted(active):
                if k != j:
                    numerator = mul(numerator, g5[k])
            return numerator
        if name == 'FINAL':
            objective = cleared(scale(-1, secants[i]), i)
        elif name[0] == 'L':
            objective = cleared(mul(gs[i], add(f, scale(-CAPS[i][0], gs[i]))), i)
        else:
            objective = cleared(mul(gs[i], add(scale(CAPS[i][1], gs[i]), scale(-1, f))), i)
        residual = objective
        for n, a in zip(weights[:8], base):
            residual = add(residual, scale(-F(n, DEN), mul(denominator, a)))
        for j, n in enumerate(weights[8:]):
            if n:
                residual = add(residual, scale(-F(n, DEN), cleared(secants[j], j)))
        for n, a in zip(alpha, equalities):
            residual = add(residual, scale(-F(n, DEN), mul(denominator, a)))
        residual = add(residual, scale(-EPS, denominator))
        reports.append({'name': name, 'active_denominators': sorted(active),
                        'weights': weights, 'equality_weights': alpha,
                        'polynomial': primitive_coefficients(residual),
                        'cover': prove_positive(residual)})
    assert [len(x['cover']['leaves']) for x in reports] == [6, 23, 36, 36, 53, 26, 40]
    assert [x['cover']['maximum_depth'] for x in reports] == [5, 8, 11, 11, 11, 9, 10]
    assert sum(x['cover']['positive_coefficients'] for x in reports) == 42650
    assert sum(x['cover']['nodes'] for x in reports) == 433
    al, ah = atan_interval(5)
    bl, bh = atan_interval(239)
    pi_lo, pi_hi = 16*al-4*bh, 16*ah-4*bl
    dl, du = F(3141592653589793, 10**15), F(3141592653589794, 10**15)
    assert dl < pi_lo < pi_hi < du
    p0, q0 = F(7024915, 10**6), F(6832329, 10**6)
    assert 9*cos_upper(dl/20)**20 < p0 and 9*cos_upper(dl/18)**18 < q0
    p, q = C*p0/9, C*q0/9
    dh, di = p*q+q+1, p*q+p+1
    assert p == F(57604303, 9000000) and q == F(93375163, 15000000)
    assert p*q == F(5378811182126389, 135000000000000) < 40
    assert 1/dh == F(135000000000000, 6354187649126389) > F(1, 48)
    assert 1/di == F(135000000000000, 6377875727126389) > F(1, 48)
    assert 1/(dh-3) == F(135000000000000, 5949187649126389) > F(1, 45)
    common = C*C+C+1
    assert common == F(1911, 25)
    out = {'object': OBJECT, 'parent': PARENT, 'parent_sha256': PARENT_SHA256,
           'target': C, 'rectangle': [[-3, 1], [DLO, DHI]], 'delta_max': delta_max,
           'quartics': KS, 'probes': PROBES, 'caps': CAPS, 'denominator_minima': minima,
           'pointwise_gap': EPS, 'multiplier_denominator': DEN, 'certificates': reports,
           'rectangles': 220, 'positive_coefficients': 42650,
           'E17': {'p': p, 'q': q, 'condition': p*q, 'floor': 1/dh, 'inverse_floor': 1/di,
                   'ceiling': p*q/dh, 'inverse_ceiling': p*q/di, 'stress_alpha': 1/(dh-3),
                   'relative_condition_improvement': 1-(C/F(83, 10))**2},
           'all_sizes': {'gap': C, 'condition': C*C, 'floor': 1/common,
                         'ceiling': C*C/common, 'inner_squared': F(5, 3)/common,
                         'outer_squared': 15*C*C/common, 'radius_ratio': 3*C},
           'exact_checks': 'PASS'}
    print(json.dumps(serial(out), sort_keys=True, indent=2))
    print(OBJECT+' PASS')


if __name__ == '__main__':
    main()
```

### Source B: axial_common_law_barrier.py

```python
#!/usr/bin/env python3
"""AXIAL_COMMON_LAW_BARRIER_ABOVE_EIGHT_V1, exact standalone recovery.
CPython 3.13.5 standard library only, compatible with Python >=3.9.
Run: python -B -S axial_common_law_barrier.py > axial_barrier_report.out
This constructs a probability over-cover witness, NOT an actual convex body.
"""
from fractions import Fraction as F
from math import comb, gcd, lcm
import hashlib
import json

OBJECT = 'AXIAL_COMMON_LAW_BARRIER_ABOVE_EIGHT_V1'
PARENT = 'minimum-0264'
PARENT_SHA256 = 'bfcc1a56683308cd9ba36d337656a9bbebb9065375f6d531d489c9f28c03c4b5'


def trim(a):
 a=list(map(F,a))
 while len(a)>1 and not a[-1]:a.pop()
 return a

def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return trim(c)

def scale(t,a):return trim([t*x for x in a])

def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)

def power(a,k):
 r=[F(1)]
 for i in range(k):r=mul(r,a)
 return r

def divide(a,b):
 r=trim(a);b=trim(b);q=[F(0)]*max(1,len(r)-len(b)+1)
 while any(r) and len(r)>=len(b):
  k=len(r)-len(b);v=r[-1]/b[-1];q[k]+=v
  r=add(r,scale(-v,[0]*k+b))
 assert not any(r)
 return trim(q)

def value(p,x):
 r=F(0)
 for c in p[::-1]:r=c+x*r
 return r

def bern(p,lo,hi):
 n=len(p)-1
 a=[(hi-lo)**k*sum((p[j]*comb(j,k)*lo**(j-k) for j in range(k,n+1)),F(0)) for k in range(n+1)]
 b=[sum((a[k]*F(comb(i,k),comb(n,k)) for k in range(i+1)),F(0)) for i in range(n+1)]
 for k in range(n+1):
  assert comb(n,k)*sum(((-1)**(k-i)*comb(k,i)*b[i] for i in range(k+1)),F(0))==a[k]
 return b

def split(b):
 ll=[b]
 while len(ll[-1])>1:ll.append([(x+y)/2 for x,y in zip(ll[-1],ll[-1][1:])])
 return [x[0] for x in ll],[x[-1] for x in ll[::-1]]

def integrate(p,lo,hi):return sum((c*(hi**(i+1)-lo**(i+1))/(i+1) for i,c in enumerate(p)),F(0))

def stop_pdf(p,lo,hi,sample):
 # Polynomial in s for the stop loss contribution from one polynomial-density leg.
 if sample<=lo:return [F(0)]
 if sample>=hi:return [-integrate([0]+p,lo,hi),integrate(p,lo,hi)]
 out=[F(0)]
 for i,c in enumerate(p):
  out=add(out,[c*lo**(i+2)/(i+2),-c*lo**(i+1)/(i+1)])
  out=add(out,[F(0)]*(i+2)+[c/F((i+1)*(i+2))])
 return out

def raystop(c,z,sample):
 if sample<=min(c,z):return [F(0)]
 if sample>=max(c,z):return [-(c+3*z)/4,F(1)]
 if z>c:return scale(1/(4*(z-c)**3),power([-c,1],4))
 return add([-c+3*(c-z)/4,F(1)],scale(1/(4*(c-z)**3),power([c,-1],4)))

def tentstop(b,h,sample):
 c=(b-h)/2;out=[F(0)]
 if c>-b:out=add(out,stop_pdf(scale(3/((b+h)*(c+b)**2),power([b,1],2)),-b,c,sample))
 if c<h:out=add(out,stop_pdf(scale(3/((b+h)*(h-c)**2),power([h,-1],2)),c,h,sample))
 return out

def conestop(h,sample):
 if sample<=-3*h:return [F(0)]
 if sample>=h:return [F(0),F(1)]
 return scale(1/(256*h**3),power([3*h,1],4))

def prove(poly, lo, hi, strict=True):
    todo = [(bern(poly, lo, hi), '')]
    leaves, minimum = [], None
    while todo:
        b, path = todo.pop()
        ok = min(b) > 0 if strict else min(b) >= 0
        if ok:
            leaves.append(path)
            minimum = min(b) if minimum is None else min(minimum, min(b))
        else:
            if len(path) >= 30:
                raise ArithmeticError('Unproved interval: '+path)
            left, right = split(b)
            todo.extend([(right, path+'1'), (left, path+'0')])
    return {'degree': len(poly)-1, 'leaves': leaves, 'minimum': minimum,
            'coefficient_checks': len(leaves)*len(poly)}


def primitive(poly):
    den = 1
    for c in poly:
        den = lcm(den, c.denominator)
    nums = [int(c*den) for c in poly]
    common = 0
    for c in nums:
        common = gcd(common, abs(c))
    assert common > 0
    out = [c//common for c in nums]
    raw = json.dumps(out, separators=(',', ':')).encode()
    return {'coefficients_ascending': out, 'denominator_lcm': den,
            'integer_gcd': common, 'coefficient_bytes': len(raw),
            'coefficient_sha256': hashlib.sha256(raw).hexdigest()}


def serial(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [serial(v) for v in x]
    return x


def main():
    if not __debug__:
        raise RuntimeError('Assertions are required; do not use -O')
    weights, ws = [], []
    # Conditional means of density 3(w+3)/32 on four unit intervals.
    for i in range(4):
        a, b = F(-3+i), F(-2+i)
        mass = F(3, 32)*((b*b-a*a)/2+3*(b-a))
        first = F(3, 32)*((b**3-a**3)/3+F(3, 2)*(b*b-a*a))
        weights.append(mass)
        ws.append(first/mass)
    weights.append(F(1, 4))
    ws.append(F(1))
    weights, ws = tuple(weights), tuple(ws)
    assert weights == (F(3, 64), F(9, 64), F(15, 64), F(21, 64), F(1, 4))
    assert ws == (F(-7, 3), F(-13, 9), F(-7, 15), F(11, 21), F(1))
    m2 = sum(t*w*w for t, w in zip(weights, ws))
    m3 = sum(t*w**3 for t, w in zip(weights, ws))
    m4 = sum(t*w**4 for t, w in zip(weights, ws))
    ds = tuple((w*w-m3*w/m2-m2)/12 for w in ws)
    ps = tuple(d-F(1, 3) for d in ds)
    delta = sum(t*d*d for t, d in zip(weights, ds))
    r = 1/(delta+F(1, 9))
    a2 = 1/m2
    ratio = r/a2
    assert sum(weights) == 1 and sum(t*w for t, w in zip(weights, ws)) == 0
    assert sum(t*d for t, d in zip(weights, ds)) == 0
    assert sum(t*w*d for t, w, d in zip(weights, ws, ds)) == 0
    assert m2 == F(296, 315) and m3 == F(-74017, 99225)
    assert delta == F(14314339, 2537619840)
    assert ratio == F(2384557056, 296272099) > 8
    assert 0 < m2 < 1 and 0 < r < 9 and max(ws) == 1
    assert min(ds) < 0 and min(ds)**2 < 8*delta
    assert all(a2*w*w+1+r*p*p < 9 for w, p in zip(ws, ps))
    assert all(p < 0 for p in ps)
    # All real quartic parameters k, not only a selected finite list.
    qa, qb, qc = F(54, 35)*(1-m2), F(8, 5)+2*m3, F(13, 5)-m4
    assert qa > 0 and qc > 0 and 4*qa*qc-qb*qb > 0
    assert F(22, 5)-F(18, 5)*m2+m3 > 0
    gs = [[F(1), p] for p in ps]
    common, factor = [F(1)], [F(1)]
    for g in gs:
        common = mul(common, power(g, 5))
        factor = mul(factor, power(g, 2))
    moments = [[F(0)] for j in range(3)]
    for j in range(3):
        for i in range(5):
            term = scale(weights[i]*(1-ws[i])**j, power(gs[i], 2-j))
            for k in range(5):
                if k != i:
                    term = mul(term, power(gs[k], 5))
            moments[j] = add(moments[j], term)
    raw = add(mul([1, 1], add(scale(3, mul(moments[1], moments[1])),
                              scale(-2, mul(moments[0], moments[2])))),
              mul(moments[0], moments[1]))
    poly = divide(raw, factor)
    assert mul(poly, factor) == raw and len(poly) == 34
    horizon = -1/min(ps)
    assert horizon == F(671328, 284887)
    vertical = prove(poly, F(-1), horizon)
    assert vertical['leaves'] == ['0', '1'] and vertical['coefficient_checks'] == 68
    orders = []
    for name, c, zs in [('horizontal', F(0), ws), ('vertical', F(1), ps)]:
        b, h = -min((c,)+zs), max((c,)+zs)
        assert 0 < h <= 3*b and b <= 3*h
        knots = sorted(set((c,)+zs+(-b, h, (b-h)/2, -3*h, 3*b)))
        rows = []
        for lo, hi in zip(knots, knots[1:]):
            sample = (lo+hi)/2
            actual = [F(0)]
            for t, z in zip(weights, zs):
                actual = add(actual, scale(t, raystop(c, z, sample)))
            lower = add(actual, scale(-1, tentstop(b, h, sample)))
            upper = add(conestop(h, sample), scale(-1, actual))
            opposite = [(-1)**i*v for i, v in enumerate(conestop(b, -sample))]
            upper_other = add(add(opposite, [0, 1]), scale(-1, actual))
            for tag, gap in [('lower_tent', lower), ('upper_positive', upper),
                             ('upper_negative', upper_other)]:
                cert = prove(gap, lo, hi, strict=False)
                rows.append({'comparison': tag, 'interval': (lo, hi),
                             'gap_coefficients': gap, 'cover': cert})
        assert len(rows) == 24
        orders.append({'axis': name, 'support': (-b, h), 'knots': knots, 'rows': rows})
    assert [sum(len(z['cover']['leaves']) for z in x['rows']) for x in orders] == [26, 24]
    eta = F(-3, 5)
    g = tuple(1+eta*w for w in ws)
    assert min(g) == F(2, 5)
    transverse = [sum(t*(1-w)**j/gg**(3+j) for t, w, gg in zip(weights, ws, g))
                  for j in range(3)]
    defect = (3*transverse[1]**2+transverse[0]*transverse[1]
              -2*transverse[0]*transverse[2])
    assert defect == F(-3450181886488350318828125, 14194917943690523037401088) < 0
    out = {'object': OBJECT, 'parent': PARENT, 'parent_sha256': PARENT_SHA256,
           'status': 'Nonphysical common-law over-cover witness, not a convex body',
           'atoms_mass_W_p': list(zip(weights, ws, ps)), 'D': ds,
           'm2': m2, 'm3': m3, 'm4': m4, 'delta': delta, 'r': r, 'a_squared': a2,
           'ratio': ratio, 'ratio_minus_eight': ratio-8,
           'formal_full_radial_covariance_raw': ((F(3, 5)*m2, F(0), F(0)),
                                                (F(0), F(3, 5), F(0)),
                                                (F(0), F(0), F(3, 5)/r)),
           'formal_raw_endpoint_atoms': [(t/2, (w, sign, p)) for t, w, p in zip(weights, ws, ps)
                                         for sign in (F(-1), F(1))],
           'quartic_parameter_discriminant_gap': 4*qa*qc-qb*qb,
           'vertical_parameter_interval_open': (F(-1), horizon),
           'vertical_polynomial': primitive(poly), 'vertical_cover': vertical,
           'axis_convex_orders': orders,
           'horizontal_probe_eta': eta, 'horizontal_probe_M': transverse,
           'horizontal_probe_Berwald_defect': defect, 'exact_checks': 'PASS'}
    print(json.dumps(serial(out), sort_keys=True, indent=2))
    print(OBJECT+' PASS')


if __name__ == '__main__':
    main()
```

### Source C: locate_oblique_duals.py

```python
#!/usr/bin/env python3
"""Optional numerical discovery, NOT proof acceptance.
CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0.
Run: OPENBLAS_NUM_THREADS=1 python locate_oblique_duals.py > located_duals.json
The two exact programs require neither this code nor its output.
"""
from fractions import Fraction as F
import json
import math
import numpy as np
import scipy
from scipy.optimize import linprog

C, DLO, DHI = F(41, 5), F(-3, 10), F(7, 5)
PROBES = ((F(3, 10), F(0)), (F(3, 5), F(-1, 5)), (F(3, 10), F(1, 10)))
N, DEN, BUFFER, CAP_GRID = 161, 10**9, 0.002, 100000


def main():
    if np.__version__ != '2.3.5' or scipy.__version__ != '1.17.0':
        raise RuntimeError('This locator is pinned to NumPy 2.3.5 and SciPy 1.17.0')
    w, d = np.meshgrid(np.linspace(-3, 1, N),
                       np.linspace(float(DLO), float(DHI), N), indexing='ij')
    w, d = w.ravel(), d.ravel()
    eq = np.array([np.ones_like(w), w, d, w*d])
    beq = [1, 0, 0, 0]
    phi = [w*w-float(C)*d*d-float(C)/9, 1-w*w]
    for k in [-1.5, -1, -0.75, -0.5, 0]:
        phi.append(13/5+8*k/5+54*k*k/35-w**4+2*k*w**3-54*k*k/35*w*w)
    phi.append(22/5-18/5*w*w+w**3)
    rows, caps = [], []
    def solve(obj, equations, tolerance):
        res = linprog(obj, A_ub=-np.array(phi), b_ub=np.zeros(len(phi)),
                      A_eq=equations, b_eq=beq, bounds=(0, None), method='highs',
                      options={'dual_feasibility_tolerance': tolerance,
                               'primal_feasibility_tolerance': tolerance})
        if not res.success:
            raise RuntimeError(res.message)
        return res
    def dual(obj, name):
        res = solve(obj, eq, 1e-8)
        weights = [max(0, round(-x*DEN)) for x in res.ineqlin.marginals]
        equality = [round(x*DEN) for x in res.eqlin.marginals[1:]]
        rows.append((name, weights, equality))
    for i, (tq, etaq) in enumerate(PROBES):
        t, eta = float(tq), float(etaq)
        g, f = 1-t/3+t*d+eta*w, 1-w
        assert g.min() > 0
        m0, m1, m2 = 1/g**3, f/g**4, f*f/g**5
        equations = np.array([m0, w, d, w*d])
        low = solve(m1, equations, 1e-9)
        high = solve(-m1, equations, 1e-9)
        lo = F(math.floor((low.fun-BUFFER)*CAP_GRID), CAP_GRID)
        up = F(math.ceil((-high.fun+BUFFER)*CAP_GRID), CAP_GRID)
        caps.append((lo, up))
        dual(m1-float(lo)*m0, 'L'+str(i))
        dual(float(up)*m0-m1, 'U'+str(i))
        secant = (3*float(lo+up)+1/(1+t))*m1-3*float(lo*up)*m0-2*m2
        if i < 2:
            phi.append(secant)
        else:
            dual(-secant, 'FINAL')
    print(json.dumps({'C': str(C), 'rectangle': [str(DLO), str(DHI)],
                      'probes': [[str(t), str(e)] for t, e in PROBES],
                      'caps': [[str(l), str(u)] for l, u in caps],
                      'DEN': DEN, 'duals': rows}, indent=2))


if __name__ == '__main__':
    main()
```
