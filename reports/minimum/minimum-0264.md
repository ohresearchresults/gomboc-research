# minimum-0264

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# PROJECTIVE_TWO_PROBE_83_OVER_10_V1

## 1. Main result and scientific change

For every full-dimensional compact convex three-body P, uniformly filled and translated to its **actual volume centroid**, let Σ be its actual covariance. Then

\[
\boxed{\Upsilon_\Sigma(P)<\frac{83}{10}=8.3,}
\qquad
\Upsilon_C(P)=\max_{\substack{w\in P,\ n\in P^\circ\\w\cdot n=0}}
(w^TC^{-1}w)(n^TCn).
\tag{1}
\]

The polar is taken at that same origin. In particular,

\[
\boxed{\inf_{C\succ0}\Upsilon_C(P)<8.3.}
\tag{2}
\]

The result holds in the **unchanged actual covariance reference**, not only after finding a new auxiliary ellipsoid. It improves the accepted 8.5 theorem. It does not assert the bound for every arbitrary C.

The advance uses the projective-refill family jointly rather than selecting a better single parameter in the parent's separate Taylor estimates. The two probes are exactly

\[
\theta_0=3/20,\qquad \theta_1=1/4.
\]

A first probe constrains the same radial endpoint law that is tested by the second. Five literal rational dual inequalities, proved pointwise on a closed two-dimensional rectangle, yield a contradiction to a ratio of 8.3. Their exact acceptance requires **154 Bernstein rectangles and 10010 strictly positive coefficient checks**, with maximum depth 12. There is no sampled-extremum acceptance, no numerical-feasibility assumption, and no independently assigned projective moment law.

There is also a reusable sharp actual-volume theorem. If a scalar projection of a uniform-centroid convex three-body has support \([-b,h]\), then

\[
\boxed{40\operatorname{Var}(X)\ge3h^2-2hb+3b^2
=(h+b)^2+2(h-b)^2.}
\tag{3}
\]

More strongly, its law dominates a particular squared-tent law in convex order. Equality in (3) forces that exact scalar density. Actual double pyramids attain equality. This supplies a new support constraint for the radial endpoints near an outer covariance extremum.

### Same-metric E17 consequence

For an actual 10/17/9 polytope under hypothetical joint S1/U1, set

\[
H=\Sigma^{1/2}M\Sigma^{1/2},\qquad
\lambda_1\ge\lambda_2\ge\lambda_3>0.
\]

The same-origin polar uses exactly \(H^{-1}\). Both finite-height gaps now satisfy

\[
\frac{\lambda_1}{\lambda_2}<p=\frac{116613589}{18000000},\qquad
\frac{\lambda_2}{\lambda_3}<q=\frac{189027769}{30000000},
\]

\[
\boxed{\operatorname{cond}(H)
<\frac{22043206563752941}{540000000000000}
=40.8207528958387\ldots.}
\tag{4}
\]

Relative to the accepted 42.811720085997… ceiling, this reduces the ceiling by exactly \(336/7225\), approximately **4.6505%**. The new trace-one floors are

\[
\frac{H}{\operatorname{tr}H}
>\frac{540000000000000}{25985706405752941}I,
\qquad
\frac{H^{-1}}{\operatorname{tr}H^{-1}}
>\frac{540000000000000}{26081614233752941}I.
\tag{5}
\]

The primal floor is approximately 0.0207806550096499. These are necessary-condition improvements, including incidental weak contacts. They do not prove E17 infeasibility, remove a catalogue entry, or construct a 110 body. The previous ceiling and its scope are in the literal accepted parent.

## 2. Input audit and source authority

I read the complete new `research-journal.md` consecutively through EOF, including the full literal parent payload. Its mounted representation is **337207 bytes, 1888 lines**, SHA-256

`57eb4feb39472c6eff02eb19459c51bb04920999663a962c53727818fca46d08`.

The required parent remains **minimum-0261**, SHA-256

`c858f67518fd87fccd41d8bf201b5d9b2be0d809750afdcaeb410696e568b021`.

Reconstructing the compact UTF-8 JSON envelope from its literal Markdown, with a final LF in `result_markdown`, gives **37862 bytes** and this digest. There is no parent-identity conflict. Earlier unchanged exact sources remain available from this chat and were retained. No unavailable archive payload or additional H5 program is needed for the new result.

The parent's actual radial identity, upper convex-order comparison, and projective Jacobian are retained, with their reasoning reproduced below. The new pieces are the lower convex-order support theorem, the simultaneous-probe moment formulation, and its exact finite certificate. The only classical geometric input is planar Brunn–Minkowski section concavity, also used in the supplied covariance proof.

The earlier actual pyramid P0, the cut/cut/stack 10/17/9 family, their all-reference lower obstruction, and the six-pair optimality theorem are unchanged. No new body is being substituted for those objects. The new square-bipyramid control in Section 3 is solely an equality calibration for (3).

## 3. Sharp lower convex order at fixed projection endpoints

### Theorem 1

Let X be a scalar linear coordinate of a uniformly filled full-dimensional convex three-body, after subtracting its actual centroid. Let its support be \([-b,h]\), where b,h>0. Define

\[
c=\frac{b-h}{2},\qquad L=b+h,
\]

and the probability density

\[
f_{b,h}(x)=\frac3L
\begin{cases}
\left(\dfrac{x+b}{c+b}\right)^2,&-b\le x\le c,\\[4pt]
\left(\dfrac{h-x}{h-c}\right)^2,&c\le x\le h.
\end{cases}
\tag{6}
\]

A zero-length piece is omitted. Then c lies in \([-b,h]\), the density has mean 0, and for every convex function φ on that interval,

\[
\mathbb E\varphi(X)\ge\int_{-b}^{h}\varphi(x)f_{b,h}(x)\,dx.
\tag{7}
\]

In particular (3) holds. Equality in (3) holds if and only if the actual scalar density equals (6) almost everywhere.

### Proof

First, actual centroid reflection gives \(h\le3b\) and \(b\le3h\). One direct proof uses rays from a maximizing point: uniform volume has radial parameter T with density \(3t^2\), so its scalar mean is \(h/4+(3/4)\mathbb E Z\), where every far endpoint has coordinate at least −b. Thus \(0\ge(h-3b)/4\). The minimizing-point argument gives the other inequality. These inequalities are exactly what is needed for \(-b\le c\le h\).

Let f be the actual probability density. Planar section concavity says \(\sqrt f\) is concave. The square root of (6) is affine on each side of c, is zero at the corresponding outside endpoint, and has common height \(\sqrt{3/L}\) at c. Its squared integral is 1. Writing the two leg lengths as \(A=c+b\), \(B=h-c\), its mean is

\[
c+\frac{B-A}{4}=\frac{2c+h-b}{4}=0.
\]

Compare \(\sqrt f\) with this tent. If their difference at c is nonnegative, concavity on each leg and nonnegativity at the outside endpoints make the difference nonnegative throughout. Equal total masses then force equality. Otherwise, the negative set on the left leg is a terminal interval adjoining c, and the negative set on the right leg is an initial interval adjoining c. Thus the sign pattern of \(f-f_{b,h}\) is **nonnegative, nonpositive, nonnegative**, with a single central negative interval, say \((\alpha,\beta)\). This argument includes a zero-length leg by using the remaining affine piece.

Subtract from φ its affine chord through α and β. The remainder is nonpositive inside the interval and nonnegative outside. Its product with \(f-f_{b,h}\) is therefore nonnegative. The affine part integrates to zero because both densities have the same mass and mean. This proves (7). For the strictly convex function \(\varphi(x)=x^2\), equality forces the densities to agree almost everywhere. Direct integration of (6) gives

\[
\int x^2 f_{b,h}(x)\,dx=\frac{3h^2-2hb+3b^2}{40},
\]

proving all claims.

### Actual sharpness and preserved calibration

Take any planar convex base of positive area and area centroid on the vertical axis, in the plane z=c. Join it to the two axial points of heights −b and h. The two actual cones have cross-sectional areas proportional to the two pieces in (6), so their uniformly filled convex hull has exactly that density and actual vertical centroid 0. When c is an endpoint, this becomes a single pyramid. This shows sharpness for the whole admissible endpoint-ratio range; it does not classify every body with the same projection density.

A rational calibration is the actual square bipyramid with vertices

```
(1,1,0), (-1,1,0), (-1,-1,0), (1,-1,0), (0,0,1), (0,0,-1).
```

Its eight maximal facets are \((a,i,i+1\bmod4)\), with \(a=4,5\) and \(i=0,1,2,3\). Its true f-vector is 6/12/8. The four tetrahedra

```
(4,0,1,2), (4,0,2,3), (5,0,1,2), (5,0,2,3)
```

partition its volume, each of volume 2/3. Actual integration gives volume 8/3, centroid 0, and covariance \(\operatorname{diag}(1/5,1/5,1/10)\). For its vertical projection h=b=1, equality in (3) is \(4=40/10\). The executable verifies the supporting facets, actual tetrahedral moments, and equality. No mechanical census or orthogonal-factor extremality is asserted for this calibration.

## 4. The actual endpoint law and the new support restriction

Normalize the original body by an origin-fixing affine map and homothety so that

\[
\mathbb E_KX=0,\qquad \operatorname{Cov}(K)=\frac35 I.
\tag{8}
\]

The orthogonal factor is unchanged under this reciprocal coordinate transport. It equals

\[
\sup_{\|e\|=1,\ y\in K\cap e^\perp}\frac{\|y\|^2}{h_K(-e)^2}.
\]

For a fixed e, the polar boundary vector \(-e/h_K(-e)\) gives the displayed ratio, and radial extension of any nonzero polar vector gives the converse. This is also the identity supplying the same-origin self-polar bridge.

Choose orthonormal coordinates for a tested pair so that \(y=Re_3\), \(y_1=0\), and the relevant support is \(X_1\le a\). The zero point is trivial. In polar integration about y,

\[
X=(1-T)y+TZ,\qquad T\sim3t^2\,dt\text{ on }[0,1],
\]

and T is independent of the **actual** far-endpoint law ν. Its angular density is \(\rho(\omega)^3/(3\operatorname{Vol}K)\). It is not a vertex-mass model. The actual first and second moments give

\[
\mathbb E_\nu Z=-y/3,\qquad \mathbb E_\nu ZZ^T=I.
\tag{9}
\]

For example, the \(yy^T\) terms cancel because
\(\mathbb E(1-T)^2-(2/3)\mathbb E[T(1-T)]=1/10-(2/3)(3/20)=0\). Applying (9) to any marked point proves \(K\subset3B\).

We also need the upper convex-order comparison from the parent. If a scalar coordinate has upper endpoint a and actual mean 0, its law is convex-order dominated by

\[
\frac{3(x+3a)^2}{64a^3}\,1_{[-3a,a]}(x)\,dx.
\tag{10}
\]

For completeness, centroid reflection places its entire support inside this interval. The difference between the square root of its density and the affine square root in (10) is concave on its support. The density difference therefore has sign pattern nonpositive, nonnegative, nonpositive. Subtracting the affine chord of any convex test function across the positive interval proves the comparison. The zeroth and first moments agree. Taking the quadratic test and (8) gives \(a\ge1\).

Set

\[
r=R^2,\quad W=Z_1/a,\quad D=Z_3/R+1/3,\quad
\delta=\mathbb E D^2=1/r-1/9.
\tag{11}
\]

Then

\[
\mathbb EW=\mathbb ED=\mathbb EWD=0,\qquad
\mathbb EW^2=1/a^2,\qquad -3\le W\le1.
\tag{12}
\]

Suppose for contradiction that

\[
R^2/a^2\ge c_*:=83/10.
\tag{13}
\]

Thus \(r\ge c_*>1\), \(r\le9\), and \(0\le\delta\le7/747\).

Let the actual vertical support interval of K be \([-b,h]\). Here \(h\ge R\) and \(b\le3\). Theorem 1 and (8) imply

\[
3h^2-2hb+3b^2\le24.
\]

For h≥R>1 and b≤3, the left side increases with h. Consequently

\[
3R^2-2Rb+3b^2\le24,
\qquad
\frac bR\le\frac13+\sqrt{8\delta}.
\]

Every endpoint therefore satisfies

\[
D\ge-\sqrt{8\delta}.
\tag{14}
\]

This is the new support restriction: the negative endpoint deviations must shrink with the actual radial variance deficit. It is stronger than the uniform outer-ball bound used in the parent.

For the rational certificate, we use the slightly larger closed rectangle

\[
\boxed{(W,D)\in\mathcal R=[-3,1]\times[-83/300,83/60].}
\tag{15}
\]

Indeed, \((83/300)^2>8(7/747)\). At the other end, \(Z_3/R\le3/R\le3/\sqrt{c_*}<21/20\), so \(D<21/20+1/3=83/60\). Both comparisons are checked exactly.

## 5. Seven common moment inequalities

Define the following seven polynomials on the same rectangle:

\[
A_0=W^2-c_*D^2-c_*/9,\qquad A_1=1-W^2,
\tag{16}
\]

and, in the order

\[
(\kappa_0,\kappa_1,\kappa_2,\kappa_3,\kappa_4)
=(-3/2,-1,-3/4,-1/2,0),
\]

put

\[
A_{2+j}=\frac{13}{5}+\frac85\kappa_j+\frac{54}{35}\kappa_j^2
-W^4+2\kappa_jW^3-\frac{54}{35}\kappa_j^2W^2.
\tag{17}
\]

The actual law ν under (13) satisfies

\[
\boxed{\mathbb E_\nu A_i\ge0\quad(0\le i\le6).}
\tag{18}
\]

For A0 this is exactly \(1/a^2\ge c_*/r=c_*(\delta+1/9)\). For A1 it is a≥1. For the remaining inequalities, use the globally convex polynomial

\[
\psi_\kappa(x)=\frac73x^4-4\kappa x^3+\frac{18}{7}\kappa^2x^2,
\qquad \psi_\kappa''(x)=28(x-3\kappa/7)^2.
\]

Apply (10) to \(X_1/a=TW\). Its reference moments of orders 0 through 4 are

\[
1,\ 0,\ 3/5,\ -2/5,\ 39/35.
\]

Because \(\mathbb ET^j=3/(3+j)\), the inequality is precisely

\[
\mathbb E[W^4-2\kappa W^3+(54/35)\kappa^2W^2]
\le13/5+(8/5)\kappa+(54/35)\kappa^2,
\]

which proves (17)-(18). These five inequalities retain the third and fourth moments as **common variables**. They do not replace them by separate extremal values or invoke an unattested concave density.

## 6. Two actual projective refills and a secant formulation

For θ equal to 3/20 or 1/4, let

\[
g_\theta(D)=1-\theta/3+\theta D=1+\theta Z_3/R,
\quad f(W)=1-W,
\quad M_j(\theta)=\mathbb E_\nu\frac{f(W)^j}{g_\theta(D)^{3+j}}.
\tag{19}
\]

These denominators are positive on the entire over-cover (15). Form the actual convex projective image

\[
K_\theta=\{x/[1+(\theta/R)x_3]:x\in K\},
\]

and **fill it uniformly**. The Jacobian is \([1+(\theta/R)x_3]^{-4}\). Along an old ray, put \(A=1+\theta\), \(B=1+\theta Z_3/R\), and \(d(t)=A+(B-A)t\). With \(t'=tB/d(t)\),

\[
\frac{3t^2}{d(t)^4}\,dt=\frac{3(t')^2}{AB^3}\,dt'.
\tag{20}
\]

Thus the new uniform endpoint law is exactly the old law reweighted by B−3, not a chosen new probability law. Its volume ratio is \(M_0/(1+\theta)\); its actual centroid, when needed, is

\[
\frac{y}{4(1+\theta)}+
\frac{3}{4M_0}\mathbb E_\nu\frac{Z}{(1+\theta Z_3/R)^4}.
\]

No centring prescription is imposed on this auxiliary image.

The nonnegative affine slack in the image is

\[
f_\theta(x')=1-x'_1/a-(\theta/R)x'_3.
\]

Its apex value is \(c_\theta=1/(1+\theta)\) and its endpoint value is f/B. The affine Berwald inequality holds on every uniformly filled convex three-body:

\[
16(\mathbb E u)^2\ge10\mathbb E u^2\quad(u\ge0\text{ affine}).
\]

It follows directly from (10), applied after subtracting the actual centroid to the scalar coordinate \(\mathbb E u-u\), whose upper support is at most \(\mathbb E u\). With (20), the radial moments of the slack give the exact necessary inequality

\[
\boxed{3M_1^2+c_\theta M_0M_1-2M_0M_2\ge0.}
\tag{21}
\]

This reproduces the parent's family while retaining its actual Jacobian.

Now suppose numbers \(0<l_\theta<u_\theta\) bound \(M_1/M_0\). The elementary secant inequality

\[
x^2\le(l_\theta+u_\theta)x-l_\theta u_\theta
\quad(l_\theta\le x\le u_\theta)
\]

turns (21) into the **linear expectation constraint**

\[
\mathbb E_\nu G_\theta\ge0,
\tag{22}
\]

where

\[
G_\theta(W,D)=
[3(l_\theta+u_\theta)+c_\theta]\frac f{g_\theta^4}
-3l_\theta u_\theta\frac1{g_\theta^3}
-2\frac{f^2}{g_\theta^5}.
\tag{23}
\]

The term \(-3l_\theta u_\theta/g_\theta^3\) is important. Using only an upper ratio cap and the chord from zero loses this information.

The exact caps are

| Probe | θ | l | u |
|---|---:|---:|---:|
| 0 | 3/20 | 105087/100000 | 52987/50000 |
| 1 | 1/4 | 54527/50000 | 6873/6250 |

The first caps follow from (12) and (18). The second caps additionally use (22) for probe 0. Both projective tests therefore constrain one and the same original endpoint law.

## 7. Literal exact certificate and its acceptance

Write \(\Phi=(A_0,\ldots,A_6)\) for the first two rows below, and \(\Phi=(A_0,\ldots,A_6,G_{\theta_0})\) for the last three. Write \(E=(W,D,WD)\). The objectives are

\[
\begin{array}{ll}
J_{L_i}=f/g_i^4-l_i/g_i^3,&
J_{U_i}=u_i/g_i^3-f/g_i^4,\\
J_{\mathrm{FINAL}}=-G_{\theta_1},& g_i=g_{\theta_i}.
\end{array}
\]

For every row j, the following pointwise inequality holds throughout the closed rectangle (15):

\[
\boxed{J_j-10^{-8}(\lambda_j\cdot\Phi+\alpha_j\cdot E)>10^{-5}.}
\tag{24}
\]

Here are **all** literal integer numerators. Every multiplier is divided by 100000000; no omitted normalization is intended.

```
L0:
 lambda=(2283990,2282148,1437,0,0,0,0)
 alpha=(-122773634,-19328958,77578744)
U0:
 lambda=(9030174,8929277,0,0,0,16329,51708)
 alpha=(122785236,19289986,-77309217)
L1:
 lambda=(8170114,0,0,0,0,0,30700,3124822)
 alpha=(-130156295,-39799953,151025544)
U1:
 lambda=(54146950,0,0,0,1249935,68384,0,19860510)
 alpha=(216435696,35145310,-150098096)
FINAL:
 lambda=(334018869,0,0,456037,12290626,0,0,0)
 alpha=(443450719,2434786,-6355014)
```

All λ entries are nonnegative. These are coefficients of inequalities, **not physical mass weights**.

### Reconstruction of the five polynomial inequalities

Let

\[
Q(D)=g_0(D)^5g_1(D)^5>0.
\]

For each row, multiply the left side of (24), minus \(10^{-5}\), by Q. This gives a rational polynomial \(R_j(W,D)\) of bidegree (4,12). All its coefficients are determined by (16)-(17), (19), (23), and the displayed table. The source implements those formulas directly; it does not read saved polynomials.

For clarity, the numerator of a lower-cap objective with denominator \(g_i^5\) is \(g_i(f-l_i g_i)\), and the upper-cap numerator is \(g_i(u_i g_i-f)\). The secant numerator is

\[
[3(l_i+u_i)+c_{\theta_i}]fg_i-3l_i u_i g_i^2-2f^2.
\]

The certificate proves all five \(R_j>0\) by exact tensor Bernstein arithmetic. On a rectangle, substitute its two affine unit-interval parameters, transform the resulting power coefficients using

\[
b_{ij}=\sum_{k\le i,\ell\le j}a_{k\ell}
\frac{\binom{i}{k}}{\binom{4}{k}}
\frac{\binom{j}{\ell}}{\binom{12}{\ell}}.
\tag{25}
\]

Every accepted rectangle has all 65 coefficients strictly positive. The source independently reconstructs the affine power coefficients from (25). When the initial coefficients do not suffice, midpoint de Casteljau subdivision splits one rectangle into its **two closed children**. The exact deterministic rule chooses the coordinate with the larger maximum adjacent Bernstein-coefficient difference, with W winning ties. Budgets are depth 32 and 200000 nodes; reaching either without proof raises an error rather than accepting a bound.

The observed complete acceptance is:

| Polynomial | Closed leaves | Nodes | Maximum depth | Positive coefficient checks |
|---|---:|---:|---:|---:|
| L0 | 7 | 13 | 6 | 455 |
| U0 | 22 | 43 | 8 | 1430 |
| L1 | 20 | 39 | 8 | 1300 |
| U1 | 56 | 111 | 12 | 3640 |
| FINAL | 49 | 97 | 12 | 3185 |
| **Total** | **154** | **303** | **12** | **10010** |

No body-dependent cell is omitted, and no ellipse or sampled feasibility test prunes the rectangle. The complete coefficient arrays, leaf paths, and exact positive minima regenerate in the report.

### Conclusion of the upper theorem

Take expectations of L0 and U0 in (24). Since \(\mathbb E\Phi\ge0\) and \(\mathbb EE=0\), they give the asserted strict first ratio caps. The actual projective inequality (21) then implies \(\mathbb EG_{\theta_0}\ge0\).

Use this extra common-law inequality in L1 and U1. They give the strict second ratio caps, and (21) for the second actual refill implies \(\mathbb EG_{\theta_1}\ge0\).

Finally, the last row of (24) gives

\[
-\mathbb EG_{\theta_1}>10^{-5},
\]

a contradiction. Thus (13) is impossible. Compactness of the orthogonal-pair set turns the strict pointwise ratio exclusion into (1). Choosing the actual covariance among admissible auxiliary references proves (2).

The finite moment model used for the separation is an over-cover of actual bodies; it is never asserted to realize every probability measure satisfying its lower-degree constraints. Proving the contrary sector impossible in that over-cover is sufficient. The proof does not infer an actual-body counterexample from a feasible or failed numerical relaxation.

## 8. Equality and physical consequences

The coefficient 83/10 is a certified convenient upper bound, not a proposed sharp constant. Equality is excluded by the strict polynomial margin. The argument includes interior and boundary marked points, \(R=3\), and \(a=1\), and does not require smoothness or a particular face lattice. Equality in the separate projection theorem (3) has the precise scalar-density implication stated in Section 3; it is not an equality case for the orthogonal-factor bound.

For physical applications, self-polarity exchanges the two actual vectors:

\[
\Upsilon_C(P)=\Upsilon_{C^{-1}}(P^\circ).
\]

This does not claim uniform centring or covariance normalization of the polar. With \(C=\Sigma\), the primal matrix is H and the polar matrix is its actual inverse. If the true nonnegative escape-tree heights are h and k, the supplied finite-height argument gives

\[
\lambda_1/\lambda_2<\frac{83}{10}f(h+1),\qquad
\lambda_2/\lambda_3<\frac{83}{10}f(k+1),
\quad f(m)=\cos(\pi/(2m))^{2m}.
\tag{26}
\]

The first inequality needs U1; the second needs S1 together with the same primal geometric factor. Joint S1/U1 supplies both. Every distinct nonnegative arrow strictly increases quadratic norm, including zero derivative arrows. Incidental weak contacts therefore do not evade (26).

For E17, use h≤9,k≤8 and

\[
p_0=7024915/10^6>9f(10),\qquad q_0=6832329/10^6>9f(9).
\]

The executable rechecks these inherited trigonometric majorants with rational Machin and cosine bounds. The factors p and q in (4) are \((83/90)p_0\) and \((83/90)q_0\).

Put

\[
D_H=pq+q+1=\frac{25985706405752941}{540000000000000},\quad
D_{H^{-1}}=pq+p+1=\frac{26081614233752941}{540000000000000}.
\]

Besides the floors (5), the exact ceilings are

\[
\frac H{\operatorname{tr}H}
<\frac{22043206563752941}{25985706405752941}I,
\qquad
\frac{H^{-1}}{\operatorname{tr}H^{-1}}
<\frac{22043206563752941}{26081614233752941}I.
\tag{27}
\]

In the original frame, with \(\tau=\operatorname{tr}(\Sigma M)\), the primal window is

\[
D_H\Sigma M\Sigma-\tau\Sigma\succ0,
\qquad pq\,\tau\Sigma-D_H\Sigma M\Sigma\succ0.
\tag{28}
\]

The scalar floor-stress parameter becomes

\[
\boxed{\alpha=\frac1{D_H-3}
=\frac{540000000000000}{24365706405752941}.}
\tag{29}
\]

Its stress interpretation is the unchanged intrinsic-reference construction. Changing a reference changes the transported physical matrix; (28)-(29) are specifically covariance-frame statements.

For arbitrary finite complexity, joint S1/U1 implies adjacent gaps below 83/10, condition below 6889/100, and the common trace window

\[
\frac{100}{7819}I<\frac H{\operatorname{tr}H}<\frac{6889}{7819}I,
\]

with the same common-cap window for the normalized inverse. For Euclidean M=I and only a homothetic normalization \(\operatorname{tr}\Sigma=1\), the physical container becomes

\[
\sqrt{500/23457}\,B\subset P\subset\sqrt{103335/7819}\,B,
\]

with actual origin-centred outer/inner radius ratio strictly below 249/10. These are consequences of the actual covariance sandwich and the new metric window, not anisotropic resets of M.

## 9. What was tried, uncertainty, and useful continuation

Merely inserting a better negative support endpoint into the parent's separate Taylor/Jensen bounds gave little progress. The useful change was to retain several fourth-degree convex-order inequalities simultaneously, use a two-sided secant bound for \(M_1^2/M_0^2\), and impose two projective-refill conditions on a **single underlying actual radial law**. Finite-grid linear programs were locators for the rational coefficients only. Every promoted inequality is accepted by the full exact polynomial verification above; no negative or positive numerical search outcome is an exclusion or an actual body.

The universal covariance and reference-optimized sharp constants remain unidentified. The inherited actual lower controls are not recomputed or changed. With the retained compactness and centred-sandwich continuity, the current strict brackets are

\[
6.131145332531<C_{\mathrm{covariance}}<8.3,
\qquad
5.088862048<\mathcal U_3<8.3.
\]

The covariance lower endpoint is inherited from the actual pyramid family, not newly computed.

The strictness of these universal suprema uses attainment on the normalized compact class \(B\subset K\subset3B\), continuity of actual volume moments, and continuity of the factor under centred homothetic sandwiches. It does not classify maximizers or assert fixed-f-vector attainment. The previous exact all-reference obstruction and its genuine E17 descendants remain valid.

No all-root atlas has been rerun with (29), and no mechanical conclusion is transferred from a projectively refilled auxiliary body back to its source. The H5 paired-arrow and W-only programs remain separate. The minimum bracket \(34\le C_{\min}\le622\), the actual attaining upper example, and all incidence/root counts are unchanged.

A useful next step is to combine the full lower convex-order law (7), not only its variance consequence, with additional projective probes or additional nonnegative affine slacks. The present two-probe certificate demonstrates a finite common-law separation mechanism, but does not prove that these constraints characterize actual uniform convex bodies or that adding more probes will reach the sharp constant.

## 10. Complete deterministic recovery capsule

The sole Python block below is the complete source **projective_two_probe_83_over_10.py**, including its final LF. It uses **CPython 3.13.5, standard library only**, and is written for Python ≥3.9. There are no external data, hidden coefficient arrays, parent-program imports, optimizer calls, floating-point acceptance, or random choices.

Source: **13991 bytes**, SHA-256

`9fac259a29ea6f28b32ce3b801c420438aa85976f646e776404447b1f25bf4f3`.

Reconstruction and verification command, assertions enabled:

```
python -B -S projective_two_probe_83_over_10.py > projective_two_probe_report.out
```

Expected terminal marker:

```
PROJECTIVE_TWO_PROBE_83_OVER_10_V1 PASS
```

Output: **24374 bytes**, SHA-256

`16e97508a6d7b3854d641e156e3d2ab5991ecac77738848d79951a7aae5dd941`.

The output contains all five regenerated primitive coefficient arrays and their pins, every exact leaf path and positive minimum, the actual calibration body's full input and moments, and the new physical constants. The dual coefficients are literal exact inputs in the source; their reproduction does not require rerunning the floating locator. Numerical discovery used NumPy 2.3.5 and SciPy 1.17.0; neither is a dependency of the theorem's recovery or acceptance.

Normal execution and a clean source-only reconstruction extracted from this Markdown both passed with byte-identical source and output. This is author execution, not coordinator replay or proof-assistant formalization. The exact code proves the finite polynomial inequalities and audits the explicit calibration; the analytic actual-volume and convex-order arguments are supplied above.

Convenience copies: complete source (`projective_two_probe_83_over_10.py`), exact report (`projective_two_probe_report.out`), and Markdown handoff (`result_markdown_v4.md`).

```python
#!/usr/bin/env python3
"""PROJECTIVE_TWO_PROBE_83_OVER_10_V1: complete exact recovery.
CPython 3.13.5 standard library only, compatible with Python >=3.9.
Run with assertions: python -B -S projective_two_probe_83_over_10.py > report.out
No files, floating-point arithmetic, optimizers, or random inputs are used.
The accompanying proof supplies the actual-volume and section-concavity steps.
"""
from fractions import Fraction as F
from math import comb, factorial, gcd, lcm
import hashlib
import json

OBJECT = 'PROJECTIVE_TWO_PROBE_83_OVER_10_V1'
PARENT = 'minimum-0261'
PARENT_SHA256 = 'c858f67518fd87fccd41d8bf201b5d9b2be0d809750afdcaeb410696e568b021'
C = F(83, 10)
DLO, DHI = F(-83, 300), F(83, 60)
EPS = F(1, 100000)
DEN = 100000000
KS = (F(-3, 2), F(-1), F(-3, 4), F(-1, 2), F(0))
THETA = (F(3, 20), F(1, 4))
CAPS = ((F(105087, 100000), F(52987, 50000)),
        (F(54527, 50000), F(6873, 6250)))
# Every listed integer is divided by DEN. Multipliers, not physical masses.
# Order: F0, F1, F_{-3/2}, F_{-1}, F_{-3/4}, F_{-1/2}, F_0quartic,
# then the previously proved first-probe secant constraint G0 when present.
# Equality multipliers refer to W, D, WD; their means are zero.
DUALS = (
    ('L0', (2283990, 2282148, 1437, 0, 0, 0, 0),
     (-122773634, -19328958, 77578744)),
    ('U0', (9030174, 8929277, 0, 0, 0, 16329, 51708),
     (122785236, 19289986, -77309217)),
    ('L1', (8170114, 0, 0, 0, 0, 0, 30700, 3124822),
     (-130156295, -39799953, 151025544)),
    ('U1', (54146950, 0, 0, 0, 1249935, 68384, 0, 19860510),
     (216435696, 35145310, -150098096)),
    ('FINAL', (334018869, 0, 0, 456037, 12290626, 0, 0, 0),
     (443450719, 2434786, -6355014)),
)
ONE = {(0, 0): F(1)}
W = {(1, 0): F(1)}
D = {(0, 1): F(1)}


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


def prove_positive(p):
    """Closed two-child cover; fail rather than accept an unproved rectangle."""
    nw, nd = degree(p)
    assert (nw, nd) == (4, 12)
    todo = [(bernstein(p, F(-3), F(1), DLO, DHI), 0, '')]
    leaves, nodes, depth, minimum, paths = 0, 0, 0, None, []
    while todo:
        b, dep, path = todo.pop()
        nodes += 1
        mn = min(map(min, b))
        if mn > 0:
            leaves += 1
            depth = max(depth, dep)
            minimum = mn if minimum is None else min(minimum, mn)
            paths.append(path)
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
    assert nodes == 2*leaves-1 and minimum > 0
    return {'leaves': leaves, 'nodes': nodes, 'maximum_depth': depth,
            'strictly_positive_coefficients': leaves*(nw+1)*(nd+1),
            'minimum_bernstein_coefficient': minimum, 'leaf_paths': paths}


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


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def calibration():
    """Actual square bipyramid: supporting facets and four true volume cells."""
    vertices = tuple(tuple(map(F, x)) for x in
                     ((1, 1, 0), (-1, 1, 0), (-1, -1, 0), (1, -1, 0),
                      (0, 0, 1), (0, 0, -1)))
    faces = tuple((a, i, (i+1) % 4) for a in (4, 5) for i in range(4))
    edges = set()
    for face in faces:
        a, b, c = [vertices[i] for i in face]
        n = cross(sub(b, a), sub(c, a))
        slack = [dot(n, sub(x, a)) for x in vertices]
        assert all(x >= 0 for x in slack) or all(x <= 0 for x in slack)
        assert {i for i, x in enumerate(slack) if x == 0} == set(face)
        for i, j in zip(face, face[1:]+face[:1]):
            edges.add(tuple(sorted((i, j))))
    cells = ((4, 0, 1, 2), (4, 0, 2, 3), (5, 0, 1, 2), (5, 0, 2, 3))
    volume = F(0)
    first = [F(0)]*3
    second = [[F(0)]*3 for unused in range(3)]
    for ids in cells:
        a = [vertices[i] for i in ids]
        mass = abs(dot(sub(a[1], a[0]), cross(sub(a[2], a[0]), sub(a[3], a[0]))))/6
        assert mass == F(2, 3)
        v = [sum(x[i] for x in a) for i in range(3)]
        volume += mass
        for i in range(3):
            first[i] += mass*v[i]/4
            for j in range(3):
                second[i][j] += mass*(v[i]*v[j]+sum(x[i]*x[j] for x in a))/20
    g = [x/volume for x in first]
    cov = [[second[i][j]/volume-g[i]*g[j] for j in range(3)] for i in range(3)]
    assert volume == F(8, 3) and g == [0, 0, 0]
    assert cov == [[F(1, 5), 0, 0], [0, F(1, 5), 0], [0, 0, F(1, 10)]]
    assert (len(vertices), len(edges), len(faces)) == (6, 12, 8)
    assert 3-2+3 == 40*cov[2][2]
    return {'vertices': vertices, 'maximal_facets': faces, 'cells': cells,
            'true_edges': sorted(edges), 'volume': volume, 'centroid': g,
            'covariance': cov, 'two_support_variance_equality': True}


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


def main():
    if not __debug__:
        raise RuntimeError('Assertions are required; do not use -O')
    delta_max = 1/C-F(1, 9)
    assert C > 1 and delta_max == F(7, 747)
    assert DLO < 0 and DLO*DLO > 8*delta_max
    assert DHI-F(1, 3) == F(21, 20)
    assert (DHI-F(1, 3))**2 > 9/C
    density = scale(F(3, 64), power(add(W, scale(3, ONE)), 2))
    moments = [integrate_w(mul(power(W, j), density), F(-3), F(1))
               for j in range(5)]
    assert moments == [1, 0, F(3, 5), F(-2, 5), F(39, 35)]
    base = [add(add(power(W, 2), scale(-C, power(D, 2))), scale(-C/9, ONE)),
            add(ONE, scale(-1, power(W, 2)))]
    for k in KS:
        psi = add(add(scale(F(7, 3), power(W, 4)), scale(-4*k, power(W, 3))),
                  scale(F(18, 7)*k*k, power(W, 2)))
        radial_average = {(i, j): value*F(3, i+3) for (i, j), value in psi.items()}
        ref_average = integrate_w(mul(psi, density), F(-3), F(1))
        assert ref_average == F(13, 5)+F(8, 5)*k+F(54, 35)*k*k
        base.append(add(scale(ref_average, ONE), scale(-1, radial_average)))
    gs = [add(scale(1-t/3, ONE), scale(t, D)) for t in THETA]
    g5 = [power(g, 5) for g in gs]
    denominator = mul(g5[0], g5[1])
    quotients = (g5[1], g5[0])
    assert all(1-t/3+t*DLO > 0 for t in THETA)
    funcs = [mul(denominator, a) for a in base]
    f = add(ONE, scale(-1, W))
    equalities = [mul(denominator, a) for a in (W, D, mul(W, D))]
    certificates = []

    def certify(objective, index):
        name, weights, eq = DUALS[index]
        assert len(weights) == len(funcs) and all(x >= 0 for x in weights)
        residual = objective
        for n, a in zip(weights, funcs):
            residual = add(residual, scale(-F(n, DEN), a))
        for n, a in zip(eq, equalities):
            residual = add(residual, scale(-F(n, DEN), a))
        residual = add(residual, scale(-EPS, denominator))
        cover = prove_positive(residual)
        certificates.append({'name': name, 'degree': degree(residual),
                             'weights_numerator': weights, 'equalities_numerator': eq,
                             'common_multiplier_denominator': DEN, 'strict_gap': EPS,
                             'polynomial': primitive_coefficients(residual), 'cover': cover})

    for i, (t, g, quotient, cap) in enumerate(zip(THETA, gs, quotients, CAPS)):
        lo, up = cap
        assert 0 < lo < up
        lower = mul(quotient, mul(g, add(f, scale(-lo, g))))
        upper = scale(-1, mul(quotient, mul(g, add(f, scale(-up, g)))))
        certify(lower, 2*i)
        certify(upper, 2*i+1)
        numerator = add(add(scale(3*(lo+up)+1/(1+t), mul(f, g)),
                            scale(-3*lo*up, power(g, 2))), scale(-2, power(f, 2)))
        secant = mul(quotient, numerator)
        if i == 0:
            funcs.append(secant)
        else:
            certify(scale(-1, secant), 4)
    expected_leaves = [7, 22, 20, 56, 49]
    expected_depths = [6, 8, 8, 12, 12]
    assert [x['cover']['leaves'] for x in certificates] == expected_leaves
    assert [x['cover']['maximum_depth'] for x in certificates] == expected_depths
    total_leaves = sum(expected_leaves)
    assert total_leaves == 154
    assert sum(x['cover']['strictly_positive_coefficients'] for x in certificates) == 10010
    al, ah = atan_interval(5)
    bl, bh = atan_interval(239)
    pi_lo, pi_hi = 16*al-4*bh, 16*ah-4*bl
    dl, du = F(3141592653589793, 10**15), F(3141592653589794, 10**15)
    assert dl < pi_lo < pi_hi < du
    p0, q0 = F(7024915, 10**6), F(6832329, 10**6)
    assert 9*cos_upper(dl/20)**20 < p0
    assert 9*cos_upper(dl/18)**18 < q0
    p, q = C*p0/9, C*q0/9
    gapD, inverseD = p*q+q+1, p*q+p+1
    assert p == F(116613589, 18000000) and q == F(189027769, 30000000)
    assert p*q == F(22043206563752941, 540000000000000)
    assert 1/gapD == F(540000000000000, 25985706405752941)
    assert 1/inverseD == F(540000000000000, 26081614233752941)
    commonD = C*C+C+1
    report = {'object': OBJECT, 'literal_parent': PARENT, 'parent_sha256': PARENT_SHA256,
              'target_strict_upper': C, 'rectangle': [[-3, 1], [DLO, DHI]],
              'delta_max': delta_max, 'quartic_parameters': KS, 'probes': THETA,
              'ratio_caps': CAPS, 'gap': EPS, 'certificates': certificates,
              'total_rectangles': total_leaves, 'total_positive_coefficients': 10010,
              'cone_comparison_moments': moments, 'actual_sharpness_control': calibration(),
              'E17': {'primal_gap': p, 'polar_gap': q, 'condition': p*q,
                      'primal_trace_floor': 1/gapD, 'inverse_trace_floor': 1/inverseD,
                      'primal_trace_ceiling': p*q/gapD, 'inverse_trace_ceiling': p*q/inverseD,
                      'stress_alpha': 1/(gapD-3), 'relative_condition_improvement': 1-(C/F(17, 2))**2},
              'all_sizes': {'common_gap': C, 'condition': C*C, 'trace_floor': 1/commonD,
                            'trace_ceiling': C*C/commonD, 'inner_radius_squared': F(5, 3)/commonD,
                            'outer_radius_squared': 15*C*C/commonD, 'radius_ratio': 3*C},
              'exact_checks': 'PASS'}
    print(json.dumps(serial(report), sort_keys=True, indent=2))
    print(OBJECT+' PASS')


if __name__ == '__main__':
    main()
```
