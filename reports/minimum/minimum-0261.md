# minimum-0261

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# RADIAL_PROJECTIVE_BERWALD_17_OVER_2_V1

## Result

At the specified origin, write

\[
P^\circ=\{n:n\cdot x\le1\text{ for all }x\in P\},\qquad
\Upsilon_C(P)=\max_{\substack{w\in P,\ n\in P^\circ\\ w\cdot n=0}}
(w^TC^{-1}w)(n^TCn).
\]

There is a new universal upper theorem, stronger than the accepted 8.97 bound, and it holds in the **actual covariance reference itself**:

\[
\boxed{\Upsilon_{\Sigma_P}(P)<\frac{17}{2}=8.5.}
\tag{1}
\]

Here P is any full-dimensional compact convex three-body, uniformly filled and translated to its actual volume centroid, and \(\Sigma_P\) is its actual volume covariance. Consequently

\[
\boxed{\mathcal U(P):=\inf_{C\succ0}\Upsilon_C(P)<8.5.}
\tag{2}
\]

This is not a bound for every arbitrary reference C. It supplies a universal admissible reference, namely the actual covariance, and therefore an upper bound after reference optimization. No mechanical hypothesis is needed for (1)-(2).

The new mechanism combines three pieces of the **same actual volume geometry**: a one-dimensional convex-order consequence of section concavity; a fourth-degree regression estimate in the actual radial endpoint law; and an affine Berwald inequality imposed after a positive-denominator projective image is **uniformly refilled**, with its Jacobian retained. A single explicit projective parameter, \(13/100\), suffices. The final numerical step is one degree-39 polynomial whose **40 Bernstein coefficients are strictly positive on one closed interval, without subdivision**.

For an actual 10/17/9 polytope under hypothetical joint S1/U1, this improves both gaps of the same covariance-weighted physical matrix and its inverse:

\[
\frac{\lambda_1}{\lambda_2}<\frac{23884711}{3600000},\qquad
\frac{\lambda_2}{\lambda_3}<\frac{38716531}{6000000},
\]

\[
\boxed{\operatorname{cond}(\Sigma^{1/2}M\Sigma^{1/2})
<\frac{924733153857541}{21600000000000}
=42.811720085997\ldots.}
\tag{3}
\]

The new coupled trace-one floors are

\[
\frac{H}{\operatorname{tr}H}
>\frac{21600000000000}{1085712665457541}I,
\qquad
\frac{H^{-1}}{\operatorname{tr}H^{-1}}
>\frac{21600000000000}{1089641419857541}I,
\quad H=\Sigma^{1/2}M\Sigma^{1/2}.
\tag{4}
\]

The first floor is approximately 0.0198947665319. The condition ceiling improves the accepted 47.677087 ceiling without changing its covariance reference. It is a necessary-condition improvement, not an E17 exclusion, a new equilibrium census, or a 110 attainer. Incidental weak contacts do not evade the spectral application.

## Input audit and authority

I read the entire updated 2107-line notebook consecutively through EOF, including the complete literal parent, and all four new exact source files. Earlier unchanged covariance, finite-height, intrinsic-reference, self-polar, and own-result sources were retained from this chat. No exact dependency required for the new proof is inaccessible.

The new attachments match their manifest:

| Exact input | Bytes | SHA-256 |
|---|---:|---|
| GEODESIC_MIXED_REFERENCE_OPTIMIZATION_V1.md | 9708 | 498098f99b56efd67efeb3fcba25aa80ba63f837dd9b281d676434ab5107b72c |
| H5_ALL_REFERENCE_ORTHOGONAL_MIXED_BARRIER_V1.md | 7256 | 6e8b37885e0fa0322d35051a3adcbb8802ffe9f76c5924e29f40326f870b8d4f |
| h5_reference_core.py.txt | 9461 | 54374c6e67c89467a37f68dca0c076ee20a8581acc2791d228f0c8e8f6d9aad8 |
| h5_mixed_reference_exact.py.txt | 6460 | 1c8dff377cfe601bf2d7b42e249720f65c2b8a90c9b6f46eb39d2a0b4e5ff764 |
| research-journal.md | 344147 | c5019e7734f4cf1c20c5859e9257e2c672bcfe5ade961fb0ffee6f95ea80324b |

The literal accepted parent remains **minimum-0259**, SHA-256 **8d8074c6ed14ca5e25ee185d88db4854b031af2a547c70baef834e3659ced6df**. Reconstructing its compact UTF-8 JSON envelope, with the Markdown's final LF, gives exactly 48569 bytes and this digest. Its actual pyramid P0 and cut/cut/stack family are not renamed or modified here.

The new geodesic theorem and the four-pair H5 barrier were read as supporting context, not replayed as a new computation. The former concerns reference optimization with a fixed body and physical metric; the latter obstructs a sufficient single-reference mixed template, not S1/U1 feasibility. Neither is used as an unproved actual-volume identity in the argument below.

The affine inequality used below is the classical three-dimensional Berwald inequality, also checked against Langharst–Putterman, *Weighted Berwald's Inequality*, equation (1) and Corollary 1.4. In the affine case needed here, Section 2 below proves it directly from the same section comparison, so general Berwald is not an additional black-box dependency. The planar Brunn–Minkowski section-concavity input is the same classical input as in the supplied covariance proof.

## 1. Actual radial law and normalization

An origin-fixing affine change and a scalar rescaling reduce (1) to an actual uniformly filled K with

\[
\mathbb E_K X=0,\qquad \mathbb E_K XX^T=\frac35I.
\tag{5}
\]

Indeed, reciprocal change of coordinates gives \(\Upsilon_\Sigma(P)=\Upsilon_I(\Sigma^{-1/2}P)\), and a homothety leaves this product unchanged. For a body K containing 0 in its interior,

\[
\Upsilon_I(K)=\sup_{\substack{\|e\|=1,\ y\in K\\ e\cdot y=0}}
\frac{\|y\|^2}{h_K(-e)^2}.
\]

For fixed e, the vector \(-e/h_K(-e)\) lies on the polar boundary. Conversely, extending a nonzero polar vector radially to the boundary preserves orthogonality and increases the norm product, proving the identity. Fix a point y in K. Polar integration about y, including when y is on the boundary, gives the exact representation

\[
X=(1-T)y+TZ,
\tag{6}
\]

where T is independent of the far endpoint Z, and T has density \(3t^2\) on \([0,1]\). The endpoint law \(\nu\) is the actual angular cone-volume law: on rays of length \(\rho(\omega)\), its density is \(\rho(\omega)^3/(3\operatorname{Vol}K)\). It is not freely assigned to boundary points.

Since

\[
\mathbb ET=\frac34,\quad \mathbb ET^2=\frac35,\quad
\mathbb E(1-T)^2=\frac1{10},\quad
\mathbb E[T(1-T)]=\frac3{20},
\]

equation (5) gives

\[
\boxed{\mathbb E_\nu Z=-\frac y3,\qquad
\mathbb E_\nu ZZ^T=I.}
\tag{7}
\]

For example, the \(yy^T\) terms in the second identity cancel because
\(1/10-(2/3)(3/20)=0\). Therefore \(I-yy^T/9\succeq0\), so every point of K has norm at most 3. This is the outer covariance bound, obtained from the actual radial law without vertex quadrature.

For the joint ratio, use orthonormal coordinates in which

\[
y=R e_3,\qquad X_1\le a:=h_K(e_1),\qquad y_1=0.
\]

The sign of \(e_1\) can be chosen to represent the original support \(h_K(-e)\). The case y=0 is trivial. Put

\[
r=R^2,\quad p=Z_3/R,\quad D=p+1/3,\quad
\delta=\mathbb E_\nu D^2=\frac1r-\frac19,\quad W=Z_1/a.
\tag{8}
\]

Then

\[
\mathbb E p=-1/3,\quad \mathbb E D=0,\quad
\mathbb EW=\mathbb E(WD)=0,\quad \mathbb EW^2=1/a^2.
\tag{9}
\]

These identities all use one common endpoint law. In particular, the mixed identity comes from \(\mathbb E Z_1Z_3=0\), not an independent orthogonality assumption about moments.

## 2. A full scalar convex-order comparison

### Lemma 1

Let X be uniform in a full-dimensional convex three-body with actual centroid 0. For a scalar linear coordinate \(X_1\), let \(a=\max X_1>0\). Then, for every convex function \(\varphi\) on \([-3a,a]\),

\[
\mathbb E\varphi(X_1)\le
\int_{-3a}^{a}\varphi(x)\frac{3(x+3a)^2}{64a^3}\,dx.
\tag{10}
\]

### Proof

Write \(\min X_1=-b\). Apply the actual radial decomposition at a minimizing point: its coordinate is \(-b\), all radial endpoints have coordinate at most a, and the first-moment identity gives
\(0=-b/4+(3/4)\mathbb E Z_1\le-b/4+3a/4\). Thus \(b\le3a\).

Let f be the probability density of \(X_1\). By planar Brunn–Minkowski, \(\sqrt f\) is concave on its support \([-b,a]\). Let

\[
f_0(x)=\frac{3(x+3a)^2}{64a^3}\,1_{[-3a,a]}(x).
\]

Both f and \(f_0\) have total mass 1 and mean 0. On \([-b,a]\), \(\sqrt f-\sqrt{f_0}\) is concave, since \(\sqrt{f_0}\) is affine. Hence the positive set of \(f-f_0\) is an interval, say with endpoints \(\alpha,\beta\). Outside the support of f its difference from \(f_0\) is nonpositive.

Subtract from \(\varphi\) the affine chord through \(\alpha,\beta\). The remainder is nonpositive inside that interval and nonnegative outside it. Multiplying by \(f-f_0\) gives a nonpositive integrand everywhere. The affine part integrates to zero by the common zeroth and first moments. This proves (10). An empty positive interval forces equality of the densities; endpoint values do not affect the integrals.

In the normalized body (5), taking \(\varphi(x)=x^2\) gives \(3/5\le3a^2/5\), so

\[
a\ge1.
\tag{11}
\]

More generally, apply this comparison after subtracting the actual centroid and use the scalar coordinate \(\mathbb E f-f\), where f is a nonnegative affine function on any uniformly filled convex three-body. Its upper support is at most \(\mathbb E f\). Thus

\[
\boxed{16(\mathbb E f)^2-10\mathbb E f^2\ge0.}
\tag{12}
\]

The constant-function case is immediate. This is exactly the affine Berwald inequality used below. No chosen centroid for a projected or polar body is involved.

## 3. Fourth-degree regression in the actual endpoint law

The reference density in (10) has moments

\[
\mathbb E_0 X_1^2=\frac35a^2,\qquad
\mathbb E_0 X_1^3=-\frac25a^3,\qquad
\mathbb E_0 X_1^4=\frac{39}{35}a^4.
\tag{13}
\]

For any real c, use the globally convex polynomial

\[
\varphi_c(x)=\frac73x^4-4cx^3+\frac{18}{7}c^2x^2,
\qquad \varphi_c''(x)=28(x-3c/7)^2.
\]

Since \(X_1=TZ_1\) in (6), \(\mathbb ET^3=1/2\), \(\mathbb ET^4=3/7\), and \(\mathbb E Z_1^2=1\), (10)-(13) imply

\[
\begin{aligned}
\mathbb E_\nu(Z_1^2-cZ_1-1)^2
&=\frac73\mathbb E_KX_1^4-4c\mathbb E_KX_1^3+c^2-1\\
&\le\frac{13}{5}a^4-1+\frac85ca^3
 +\left[1+\frac{54}{35}(a^2-1)\right]c^2.
\end{aligned}
\tag{14}
\]

Choose

\[
c=-\frac{4a^3}{5d_a},\qquad
 d_a=1+\frac{54}{35}(a^2-1)>0.
\]

Because \(\mathbb E D=\mathbb E(DZ_1)=0\), Cauchy–Schwarz in the **same** law \(\nu\) gives

\[
\boxed{
\left|\mathbb E_\nu(W^2D)\right|
\le\sqrt{\delta\,\mathcal B(a^2)},\qquad
\mathcal B(t)=\frac{13}{5}-\frac1{t^2}
 -\frac{16t}{25[1+(54/35)(t-1)]}.}
\tag{15}
\]

The regression term involving \(Z_1\) matters: separate fourth-moment and third-moment bounds lose a substantial part of this estimate. For \(t\ge1\), \(\mathcal B(1)=24/25\) and

\[
\mathcal B'(t)=\frac2{t^3}+
\frac{304}{875[1+(54/35)(t-1)]^2}>0.
\tag{16}
\]

Thus the function is positive and increasing throughout the domain used below.

## 4. Projective refill gives a new necessary moment inequality

Choose any positive \(\theta\) for which
\(1+(\theta/R)x_3>0\) on K, and form the genuine convex body

\[
K_\theta=\left\{\frac{x}{1+(\theta/R)x_3}:x\in K\right\}.
\]

Positive denominators make the image of each segment the corresponding segment, with positive reparameterized weights; hence the image is again a full-dimensional compact convex body.

**Fill \(K_\theta\) uniformly.** This does not mean pushing forward the old uniform probability without a density change. The volume Jacobian is
\([1+(\theta/R)x_3]^{-4}\).

On a ray of (6), write \(A=1+\theta\), \(B_p=1+\theta p\), and
\(d(t)=A+(B_p-A)t\). The new fractional radial coordinate is
\(t'=tB_p/d(t)\). Direct differentiation gives the exact change of measure

\[
\frac{3t^2}{d(t)^4}\,dt
=\frac{1}{A B_p^3}\,3(t')^2\,dt'.
\tag{17}
\]

Therefore the new uniform radial endpoint law is the old law reweighted by \(B_p^{-3}\), followed by the actual projective endpoint map. The new radial parameter still has density \(3(t')^2\). In the notation (18) below, its actual volume ratio is \(M_0/(1+\theta)\), and its actual centroid is

\[
g_\theta=\frac{y}{4(1+\theta)}+\frac{3}{4M_0}\mathbb E_\nu\frac{Z}{(1+\theta p)^4}.
\]

No centroid is prescribed independently; only scalar slack moments of this actual uniform law are needed.

The affine nonnegative slack on the new body is

\[
f_\theta(x')=1-x'_1/a-(\theta/R)x'_3.
\]

Its value at the new apex is \(c_\theta=1/(1+\theta)\), and at the new endpoint it is \((1-W)/(1+\theta p)\). Define actual weighted expectations

\[
M_j=\mathbb E_\nu\frac{(1-W)^j}{(1+\theta p)^{3+j}},
\qquad j=0,1,2.
\tag{18}
\]

Apply (12) to uniform volume in \(K_\theta\), using (17). The first and second radial moments of an affine slack are
\((c+3m)/4\) and \((c^2+3cm+6q)/10\), respectively. Clearing the positive normalization \(M_0\) yields

\[
\boxed{3M_1^2+\frac{1}{1+\theta}M_0M_1-2M_0M_2\ge0.}
\tag{19}
\]

Equation (19) holds for every permitted projective parameter, not just the one used in the numerical ceiling. It is an actual-body restriction beyond assigning the first two endpoint moments. Its derivation retains the new uniform volume law exactly; it neither assumes a uniformly centred polar nor claims that projective refill preserves mechanical equilibria.

## 5. Quantitative bounds under the contrary hypothesis

Suppose, contrary to (1), that

\[
\frac{R^2}{a^2}\ge\frac{17}{2}.
\tag{20}
\]

By (7) and (11),

\[
17/2\le r\le9,\qquad 1\le a^2\le2r/17.
\]

Set

\[
v=\sqrt\delta,\quad r=\frac9{1+9v^2},\quad
0\le v\le\frac1{\sqrt{153}}<\frac{81}{1000}.
\tag{21}
\]

All endpoint heights satisfy \(|p|\le3/R<30/29\). We use the following fixed rational parameters:

\[
\theta=\frac{13}{100},\quad m=-\frac13,\quad b=\frac{30}{29},\quad
z=1+\theta m=\frac{287}{300}.
\]

The denominator is strictly positive throughout K because \(1-\theta b>0\).

For \(F_k(p)=(1+\theta p)^{-k}\), let

\[
c_k(x)=\frac{F_k(x)-F_k(m)-F_k'(m)(x-m)}{(x-m)^2}.
\]

The continuous divided remainder equals
\(\int_0^1(1-t)F_k''(m+t(x-m))\,dt\). Since \(F_k'''<0\), it decreases with x. Exact rational arithmetic gives

\[
c_3(b)=\frac{473333723109000}{4930820589180521}>\frac{19}{200},
\]

\[
c_4(-b)=\frac{2092262225523606630000}{7728662979090224252207}
<\frac{271}{1000}.
\tag{22}
\]

Using \(\mathbb ED=0\), and using \(0\le1-W\le4\) together with \(\mathbb E[(1-W)D]=0\), equations (18) and (22) imply

\[
M_0\ge L(v):=z^{-3}+\frac{19}{200}v^2,
\qquad
M_1\le U(v):=z^{-4}+\frac{271}{250}v^2.
\tag{23}
\]

For \(M_2\), use the probability law obtained by weighting \(\nu\) by \((1-W)^2\). Its mass before normalization is \(A_a=1+1/a^2\), and its mean height is

\[
m+\frac{\mathbb E(W^2D)}{A_a}.
\]

Jensen's inequality for the convex decreasing function \(F_5\), followed by (15)-(16), gives a lower bound. Write

\[
t(v)=\frac{2r}{17}=\frac{18}{17(1+9v^2)},\quad
Q(v)=\frac v2\,[\mathcal B(t(v))+1],\quad
A(v)=1+\frac{17}{2r}=\frac{35+153v^2}{18}.
\]

Indeed, \(a^2\le t(v)\), \(\mathcal B\) increases, and
\(\sqrt{x}\le(x+1)/2\) gives
\(\mathbb E(W^2D)\le Q(v)\). Also \(A_a\ge A(v)\). For fixed \(Q\ge0\), the function
\(A\mapsto A(z+\theta Q/A)^{-5}\) is increasing, since its logarithmic derivative is
\((zA+6\theta Q)/[A(zA+\theta Q)]>0\). Consequently

\[
M_2\ge V(v):=\frac{A(v)}{[z+\theta Q(v)/A(v)]^5}.
\tag{24}
\]

Thus a contradiction to (19) follows from the single scalar inequality

\[
E(v):=3U(v)^2+L(v)\left[\frac{100}{113}U(v)-2V(v)\right]<0.
\tag{25}
\]

The sign when replacing \(M_0\) is important. If (25) holds, its bracket is negative because \(3U^2>0\) and L>0. Then (23)-(24) make the actual bracket no larger, and \(M_0\ge L\) gives
\(3M_1^2+M_0[(100/113)M_1-2M_2]\le E(v)<0\). There is no unlicensed multiplication of a lower bound by an unknown-sign expression.

## 6. Complete exact polynomial certificate for (25)

Define the following literal polynomials:

\[
\begin{aligned}
K(v)&=649-2907v^2,\\
J(v)&=35+153v^2,\\
N(v)&=2193979-29633499v^2-351135v^4+340249815v^6,\\
H(v)&=17220K(v)J(v)+13vN(v).
\end{aligned}
\tag{26}
\]

Direct substitution gives

\[
\mathcal B(t(v))+1=\frac{N(v)}{1620K(v)},\quad
zA(v)+\theta Q(v)=\frac{H(v)}{324000K(v)},
\]

\[
V(v)=\frac{J(v)^6[324000K(v)]^5}{18^6H(v)^5}.
\]

All these denominators are positive on the actual interval (21). The executable also certifies their positivity on the slightly larger closed interval \([0,81/1000]\).

With L,U from (23), form the degree-39 rational polynomial

\[
\begin{aligned}
P(v)={}&226L(v)J(v)^6[324000K(v)]^5\\
&-18^6H(v)^5\{339U(v)^2+100L(v)U(v)\}.
\end{aligned}
\tag{27}
\]

It satisfies the exact identity

\[
-E(v)=\frac{P(v)}{113\,18^6H(v)^5}.
\tag{28}
\]

Write \(P(v)=\sum_{j=0}^{39}p_jv^j\), and let \(h=81/1000\). Its degree-39 Bernstein coefficient of index k on \([0,h]\), normalized by \(P(0)>0\), is

\[
\beta_k=\frac1{P(0)}\sum_{j=0}^k
p_jh^j\frac{\binom{k}{j}}{\binom{39}{j}}.
\tag{29}
\]

The following are **exact integer lower numerators with denominator \(10^6\)** for all 40 normalized coefficients, in increasing index order. They are computed by rational arithmetic, not rounded floating estimates:

```
1000000, 931110, 864485, 800147, 738119, 678427, 621092, 566139,
513591, 463471, 415804, 370612, 327920, 287750, 250127, 215074,
182613, 152770, 125568, 101029, 79178, 60038, 43631, 29981,
19111, 11044, 5801, 3406, 3879, 7242, 13516, 22722,
34879, 50006, 68122, 89246, 113393, 140579, 170821, 204131
```

In particular every \(\beta_k>1/300\). Bernstein basis functions are nonnegative and sum to 1. Therefore

\[
P(v)>P(0)/300>0\qquad(0\le v\le81/1000).
\]

This proves (25), contradicts (19), and excludes (20), including equality. The maximum over the compact orthogonal pair set consequently gives (1), and choosing \(C=\Sigma_P\) gives (2).

No unsupported density realization enters this certificate. The cone density in Section 2 is a comparison distribution used for an inequality, not a replacement for the actual body; all endpoint and projectively refilled expectations come from the actual K.

## 7. Equality, polarity, weak contacts, and physical windows

### Strictness and geometric scope

The constant 17/2 is a convenient rational ceiling, not a proposed sharp constant. Its equality case is excluded by the positive coefficient margin in Section 6. The proof includes \(v=0\), hence \(R=3\), and includes \(a=1\). It applies to compact convex bodies, not only polytopes, and to every point y in the central section, not only its vertices.

The affine covariance reference cannot be replaced by a freely assigned vertex covariance. Likewise, the endpoint law cannot be optimized independently of the body while retaining the projective condition (19).

### Both finite-height gaps, one physical metric

For a polytope at its actual uniform centroid, let \(M\succ0\) be its physical metric and set \(H=\Sigma^{1/2}M\Sigma^{1/2}\). The supplied self-polar identity is

\[
\Upsilon_\Sigma(P)=\Upsilon_{\Sigma^{-1}}(P^\circ).
\]

It swaps the actual orthogonal pair at the same origin, without asserting anything about the polar's uniform volume centroid. Therefore, if primal and dual nonnegative true-edge escape trees have heights h and k, respectively, the new bound gives

\[
\lambda_1(H)/\lambda_2(H)<\frac{17}{2}f(h+1),\qquad
\lambda_2(H)/\lambda_3(H)<\frac{17}{2}f(k+1),
\]

\[
f(m)=\cos(\pi/(2m))^{2m}.
\tag{30}
\]

The first inequality needs U1; the second needs S1 and the same primal actual-body bound. Joint S1/U1 supplies both. A distinct nonnegative arrow strictly increases quadratic norm, so incidental weak contacts still admit the rooted-tree argument. No positive-escape hypothesis or independent polar metric has been added.

At V=10,F=9 use h<=9,k<=8 and the inherited strict rational trigonometric majorants

\[
p_0=7024915/10^6>9f(10),\qquad q_0=6832329/10^6>9f(9).
\]

The new executable rechecks these via rational Machin and cosine bounds, independently of the parent executable. Multiplication by \(17/18\) gives the exact p,q in (3). Put

\[
D=pq+q+1=\frac{1085712665457541}{21600000000000},\qquad
D_{\rm inv}=pq+p+1=\frac{1089641419857541}{21600000000000}.
\]

Then the complete individual trace windows are

\[
\frac1D I<\frac H{\operatorname{tr}H}<\frac{pq}{D}I,
\qquad
\frac1{D_{\rm inv}}I<\frac{H^{-1}}{\operatorname{tr}H^{-1}}
<\frac{pq}{D_{\rm inv}}I.
\tag{31}
\]

In the original frame, with \(\tau=\operatorname{tr}(\Sigma M)\), the primal floor and ceiling read

\[
D\Sigma M\Sigma-\tau\Sigma\succ0,
\qquad pq\,\tau\Sigma-D\Sigma M\Sigma\succ0.
\tag{32}
\]

The corresponding scalar trace-floor stress parameter is

\[
\boxed{\alpha=\frac1{D-3}
=\frac{21600000000000}{1020912665457541}.}
\tag{33}
\]

These constants belong to the actual covariance frame. Substituting them into an unrelated frozen reference frame without the prescribed congruence is not justified. The trace-floor stress interpretation is the supplied intrinsic-reference construction.

### Without an f-vector restriction

Since \(f(m)<1\) for finite m, every actual uniform joint S1/U1 polytope, of any complexity, satisfies

\[
\lambda_1/\lambda_2<17/2,\quad \lambda_2/\lambda_3<17/2,
\quad\operatorname{cond}(H)<289/4,
\]

\[
\frac4{327}I<\frac H{\operatorname{tr}H}<\frac{289}{327}I,
\]

with the same common-cap window for the normalized inverse. For Euclidean physical M=I, the actual covariance and inertia consequences are intrinsic. In the homothetic normalization \(\operatorname{tr}\Sigma=1\),

\[
\sqrt{20/981}\,B\subset P\subset\sqrt{1445/109}\,B,
\]

and its origin-centred outer/inner radius ratio is strictly below \(51/2\). These follow by combining the new trace window with the actual covariance sandwich; no anisotropic reset of the physical metric is made.

## 8. What changed, what did not, and continuation

I explored the critical-pair route but did not obtain a new upper theorem from projector balance alone. The productive change was to require the endpoint data to remain compatible with **uniformly refilled projective images of the same convex body**. Keeping just the radial second moments loses (19); keeping separate third and fourth bounds loses the regression improvement (15). The exact proof combines them.

The accepted parent's six-active-pair optimality theorem, exact \(5.088862048\ldots\) all-reference obstruction, actual pyramid P0, simplicial bipyramid controls, and cut/cut/stack 10/17/9 family remain unchanged. No new lower counterexample or relabelled body is being promoted. In particular the parent's literal E17 sequence remains an obstruction to unconditional optimized factors at or below 5, not a sequence of joint S1/U1 bodies.

Using the retained covariance-normalized compactness and centred-sandwich continuity, the universal maxima are attained among full-dimensional convex bodies. Hence the current strict upper brackets can be written

\[
6.131145332531<C_{\rm covariance}<8.5,
\qquad
5.088862048<\mathcal U_3<8.5.
\tag{34}
\]

The lower endpoints are inherited, not newly computed. For strictness of the upper suprema, recall that \(B\subset K\subset3B\) gives a compact Hausdorff class, actual volume moments pass to its limits, and centred sandwiches give continuity of the orthogonal factor and its optimized value. The new theorem excludes equality at every limiting body as well. No maximizing polytope, fixed-f-vector maximizer, or extremizer classification is asserted.

This result does not defeat the supplied H5 mixed-template barrier. That barrier lower-bounds \(\Upsilon_C e^{\delta_C}\) for every C at one marked body; (1) upper-bounds the pure factor at its actual covariance. The marked-angle and mechanical requirements have not disappeared. No H5 regional computation was duplicated, and no complete-root certificate has been rerun with the new floor.

The most useful continuation is to retain the full necessary inequality (19), the exact regression function (15), and the actual a,R dependence before the conservative replacements in Section 5. Varying the projective parameter or adding other actual-volume constraints may improve the upper constant further. Such an improvement would need a new exact certificate; the present calculation neither identifies the sharp constant nor establishes the sufficiency of any finite moment relaxation.

The global complexity bracket \(34\le C_{\min}\le622\), all incidence/root catalogues, the actual 110 attainer, and the separate regularization program are unchanged.

## 9. Complete deterministic recovery capsule

The sole Python block below is the complete source **radial_projective_17_over_2.py**, including its final LF. It uses **CPython 3.13.5, standard library only**; no external input, installed optimization solver, random seed, H5 program, or parent executable is required. It is also written for Python >=3.9. Assertions must remain enabled.

Source: **9746 bytes**, SHA-256 **2c3371a25d156e17e0e3a46ae9955b8649bc5c00099897a38281a42bcb75ade0**.

Command:

```
python -B -S radial_projective_17_over_2.py > radial_projective_report.out
```

Expected final marker:

```
RADIAL_PROJECTIVE_BERWALD_17_OVER_2_V1 PASS
```

Output: **7113 bytes**, SHA-256 **b5756ba7063ec30110814acbeddd940e59396b0fdfde764ac3aa450e2e585139**.

The code reconstructs the exact polynomial from (23), (26), and (27), clears its denominators without changing its sign, and checks every normalized Bernstein coefficient is greater than 1/300. It outputs the complete primitive coefficient array, all 40 exact lower numerators, the auxiliary positivity guards, the cone moments, and all new physical metric constants. Thus the polynomial is not an ephemeral hash-only object.

Normal execution and a clean source-only reconstruction extracted from this Markdown both passed, reproducing source and output byte-for-byte. This is author execution, not a coordinator replay or proof-assistant formalization. The analytic geometry proof is above; the executable checks its exact finite algebra and constants. Numerical trial evaluations located the useful parameter, but no numerical result or optimizer state is a proof dependency.

Convenience copies: complete runnable source (`radial_projective_17_over_2.py`), exact report (`radial_projective_report.out`), and Markdown handoff (`result_markdown_v3.md`).

```python
#!/usr/bin/env python3
"""RADIAL_PROJECTIVE_BERWALD_17_OVER_2_V1: exact recovery certificate.
CPython 3.13.5, standard library only; compatible with Python >=3.9.
Run with assertions: python -B -S radial_projective_17_over_2.py > report.out
No files, numerical locators, random choices, or external data are read.
The accompanying proof supplies the convex-body and projective-volume arguments.
"""
from fractions import Fraction as F
from math import comb, factorial, gcd, lcm
import json

OBJECT = 'RADIAL_PROJECTIVE_BERWALD_17_OVER_2_V1'
PARENT = 'minimum-0259'
PARENT_SHA256 = '8d8074c6ed14ca5e25ee185d88db4854b031af2a547c70baef834e3659ced6df'
TARGET = F(17, 2)
THETA = F(13, 100)
M = F(-1, 3)
B = F(30, 29)
Z = 1 + THETA*M
VMAX = F(81, 1000)


def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    c = [F(0)]*max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c)


def scale(t, a):
    return trim([t*x for x in a])


def mul(a, b):
    c = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def power(a, k):
    if k < 0:
        raise ValueError('Nonnegative integer polynomial power required')
    out = [F(1)]
    for unused in range(k):
        out = mul(out, a)
    return out


def integral(a, lo, hi):
    return sum((c*(hi**(j+1)-lo**(j+1))/(j+1)
                for j, c in enumerate(a)), F(0))


def bernstein(p, lo, hi):
    """Exact power-to-Bernstein conversion on the entire closed interval."""
    n = len(p)-1
    aa = [(hi-lo)**k*sum((p[j]*comb(j, k)*lo**(j-k)
                          for j in range(k, n+1)), F(0))
          for k in range(n+1)]
    return [sum((aa[k]*F(comb(i, k), comb(n, k))
                 for k in range(i+1)), F(0)) for i in range(n+1)]


def primitive_integer(p):
    den = 1
    for c in p:
        den = lcm(den, c.denominator)
    nums = [int(c*den) for c in p]
    common = 0
    for c in nums:
        common = gcd(common, abs(c))
    assert common > 0
    return [c//common for c in nums], den, common


def remainder_coefficient(k, x):
    h = x-M
    assert h != 0 and 1+THETA*x > 0
    return ((1+THETA*x)**(-k)-Z**(-k)
            +k*THETA*Z**(-k-1)*h)/(h*h)


def atan_interval(inv, terms=30):
    x = F(1, inv)
    a = sum(((-1)**j*x**(2*j+1)/(2*j+1)
             for j in range(terms)), F(0))
    b = a + (-1)**terms*x**(2*terms+1)/(2*terms+1)
    return min(a, b), max(a, b)


def cos_upper(x):
    assert 0 < x < 1
    return sum(((-1)**j*x**(2*j)/factorial(2*j)
                for j in range(5)), F(0))


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
    assert TARGET > F(29, 10)**2
    assert 1-THETA*B > 0 and Z == F(287, 300)
    assert VMAX*VMAX > 1/TARGET-F(1, 9) == F(1, 153)

    # The reference one-dimensional cone density is 3(x+3)^2/64 on [-3,1].
    density = scale(F(3, 64), power([3, 1], 2))
    moments = [integral([F(0)]*k+density, F(-3), F(1))
               for k in range(5)]
    assert moments == [F(1), F(0), F(3, 5), F(-2, 5), F(39, 35)]
    # Coefficients of phi_c''=28(x-3c/7)^2, as polynomials in x,c.
    assert [F(36, 7), F(-24), F(28)] == [28*F(3, 7)**2, -56*F(3, 7), F(28)]
    ET = [F(3, 3+k) for k in range(5)]
    assert ET[1] == F(3, 4) and ET[2] == F(3, 5)
    assert ET[3] == F(1, 2) and ET[4] == F(3, 7)
    assert 1-2*ET[1]+ET[2] == F(1, 10)
    assert ET[1]-ET[2] == F(3, 20)
    assert F(1, 10)-F(2, 3)*F(3, 20) == 0

    # All polynomials below have ascending coefficients in v=sqrt(1/R^2-1/9).
    vv = [0, 1]
    v2 = power(vv, 2)
    w = add([1], scale(9, v2))
    K = add([972], scale(-323, w))
    J = add([18], scale(17, w))
    assert K == [649, 0, -2907]
    assert J == [35, 0, 153]
    # With t=18/(17w), B(t)+1=N/(1620K).
    N = add(mul(add([5832], scale(-1445, power(w, 2))), K), [-653184])
    assert N == [2193979, 0, -29633499, 0, -351135, 0, 340249815]
    BN = add(N, scale(-1620, K))
    assert BN == [1142599, 0, -24924159, 0, -351135, 0, 340249815]
    # This independently checks the rational identity B(t) using cross-products.
    # B(t)=13/5-1/t^2-(16/25)t/[1+(54/35)(t-1)].
    expected_BN = add(mul(add([4212], scale(-1445, power(w, 2))), K), [-653184])
    assert BN == expected_BN
    # qbar=v(B(t)+1)/2=vN/(3240K), Abar=J/18.
    # Z*Abar+theta*qbar=H/(324000K).
    H = add(scale(17220, mul(K, J)), scale(13, mul(vv, N)))
    assert H == [391152300, 28521727, -42154560, -385235487,
                 -7658956620, -4564755, 0, 4423247595]

    c3 = remainder_coefficient(3, B)
    c4 = remainder_coefficient(4, -B)
    assert c3 == F(473333723109000, 4930820589180521)
    assert c4 == F(2092262225523606630000, 7728662979090224252207)
    lower_c3, upper_c4 = F(19, 200), F(271, 1000)
    assert c3 > lower_c3 > 0 and 0 < c4 < upper_c4
    lo = add([Z**(-3)], scale(lower_c3, v2))
    up = add([Z**(-4)], scale(4*upper_c4, v2))
    # -E(v)=P(v)/(113*18^6*H(v)^5), where
    # E=3*up^2+lo*(up/(1+theta)-2*J^6*(324000K)^5/(18^6H^5)).
    first = scale(226, mul(lo, mul(power(J, 6), power(scale(324000, K), 5))))
    second = scale(18**6, mul(power(H, 5),
                    add(scale(339, power(up, 2)), scale(100, mul(lo, up)))))
    raw_polynomial = add(first, scale(-1, second))
    poly, clear_denominator, common_integer_factor = primitive_integer(raw_polynomial)
    assert len(poly) == 40 and poly[0] > 0
    assert poly[0] == 44848244828511921722862843566092338314062500000000000000000000000000
    guards = {}
    for name, p in [('K', K), ('J', J), ('N', N), ('B_numerator', BN), ('H', H)]:
        co = bernstein(p, F(0), VMAX)
        assert min(co) > 0
        guards[name] = {'degree': len(p)-1, 'minimum_bernstein': min(co)}
    coeff = bernstein(poly, F(0), VMAX)
    normalized = [c/poly[0] for c in coeff]
    assert len(coeff) == 40 and min(normalized) > F(1, 300)
    assert normalized.index(min(normalized)) == 27
    lower_millionths = [(c*10**6).numerator//(c*10**6).denominator
                         for c in normalized]
    assert min(lower_millionths) == 3406

    # Reconfirm inherited trigonometric majorants without a parent executable.
    al, ah = atan_interval(5)
    bl, bh = atan_interval(239)
    pi_lower, pi_upper = 16*al-4*bh, 16*ah-4*bl
    dl, du = F(3141592653589793, 10**15), F(3141592653589794, 10**15)
    assert dl < pi_lower < pi_upper < du
    p0, q0 = F(7024915, 10**6), F(6832329, 10**6)
    assert 9*cos_upper(dl/20)**20 < p0
    assert 9*cos_upper(dl/18)**18 < q0
    p, q = TARGET*p0/9, TARGET*q0/9
    D, Di = p*q+q+1, p*q+p+1
    assert p == F(23884711, 3600000)
    assert q == F(38716531, 6000000)
    assert p*q == F(924733153857541, 21600000000000)
    assert 1/D == F(21600000000000, 1085712665457541)
    assert 1/Di == F(21600000000000, 1089641419857541)
    assert 1/(D-3) == F(21600000000000, 1020912665457541)
    all_size_D = TARGET**2+TARGET+1
    assert all_size_D == F(327, 4)

    report = {
        'object': OBJECT, 'exact_checks': 'PASS',
        'literal_parent': PARENT, 'literal_parent_sha256': PARENT_SHA256,
        'covariance_and_optimized_factor_strict_upper': TARGET,
        'parameters': {'theta': THETA, 'height_mean': M, 'height_bound': B,
                       'z': Z, 'v_interval': [F(0), VMAX],
                       'actual_v_squared_upper': F(1, 153), 'sqrt_majorant_anchor': 1},
        'cone_moments_0_through_4': moments, 'radial_T_moments_0_through_4': ET,
        'taylor_constants': {'c3_exact': c3, 'c4_exact': c4,
                              'c3_used_lower': lower_c3, 'c4_used_upper': upper_c4},
        'denominator_guards': guards,
        'polynomial': {'degree': len(poly)-1, 'coefficients_ascending': poly,
                       'raw_denominator_lcm': clear_denominator,
                       'raw_integer_gcd': common_integer_factor,
                       'primitive_constant_coefficient': poly[0]},
        'certificate': {'interval': [F(0), VMAX], 'leaves': 1, 'depth': 0,
                        'positive_coefficients': 40, 'normalization': 'P_primitive(0)',
                        'coefficient_lower_bound': F(1, 300),
                        'minimum_index': 27, 'minimum_coefficient': min(normalized),
                        'lower_millionths_ascending': lower_millionths},
        'E17_same_covariance_reference': {'primal_gap': p, 'polar_gap': q,
                       'condition': p*q, 'primal_trace_floor': 1/D,
                       'primal_trace_ceiling': p*q/D, 'inverse_trace_floor': 1/Di,
                       'inverse_trace_ceiling': p*q/Di, 'stress_alpha': 1/(D-3)},
        'all_sizes_same_covariance_reference': {'adjacent_gap_upper': TARGET,
                       'condition_upper': TARGET**2, 'trace_floor': 1/all_size_D,
                       'trace_ceiling': TARGET**2/all_size_D,
                       'physical_inner_radius_squared': F(5, 3)/all_size_D,
                       'physical_outer_radius_squared': 15*TARGET**2/all_size_D,
                       'physical_radius_ratio_upper': 3*TARGET},
        'scope': 'Actual uniform-centroid convex three-bodies. Spectral applications use one physical M and its same-origin inverse; no equilibrium existence or exclusion is asserted.'}
    print(json.dumps(serial(report), sort_keys=True, indent=2))
    print(OBJECT+' PASS')


if __name__ == '__main__':
    main()
```
