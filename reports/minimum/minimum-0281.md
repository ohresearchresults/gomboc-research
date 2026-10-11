# minimum-0281

Historical AI scientific report · saved 2026-09-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# SHARP_FULL_FACET_MATRIX_ONE_FIFTH_V1

## 1. Result

**The proposed full-matrix inequality is true.** Let P be a full-dimensional compact convex three-body, uniformly filled and translated to its actual volume centroid. For a whole genuine positive-area facet F with q·x=1, define

    alpha = Area(F)/(||q|| Vol(P)),
    c = E_F x,    T = E_F xx^T,    Sigma = E_P xx^T,
    B = alpha^(-1) T^(-1) − qq^T.

Then

    B >= Sigma^(-1)/5,

or, equivalently,

    5 Sigma >= alpha T + alpha^2/(1−alpha) cc^T.       (M)

Moreover **B−Sigma^(-1)/5 is positive definite unless P is a pyramid with base exactly F**. In that exceptional case its rank is two, its kernel is span(c), and the generalized eigenvalues of B relative to Sigma^(-1) are exactly (1/5,4/5,4/5). Thus the coefficient1/5 is universally sharp, with a complete marked-facet equality classification.

The missing mixed moments are controlled by applying one-constraint localization to a **convex variance-corrected boundary functional**, not by treating a tangential direction as the selected facet normal. The proof below includes a uniform shrinking-layer error; no limiting needle is chosen after inspecting a numerical optimizer.

The accepted normal theorem, frustum calculations and cone-law bound are retained. The cone-law denominator is still **3−alpha** in its original argument. The stronger denominator **1−alpha** is justified here by a separate localization proof. The predecessor explicitly distinguished these claims. fileciteturn46file0L37-L60

This is an actual-shape moment theorem, not a new equilibrium census, a whole-E17 exclusion, or an attainer. The accepted minimum bracket **34≤C_min≤622** remains unchanged. fileciteturn46file4L9-L11

### Input and evidence status

All five current input files were read completely through EOF, and their byte counts and SHA-256 values matched the supplied manifest. The complete updated journal is286362bytes, SHA `0aad76fd53371b7b005bab2d497ec24b2fb937668ca2c1e22c7f5225a7a495e3`. No required input was inaccessible.

The main inherited proof is `SHARP_FACET_NORMAL_VARIANCE_AND_PROFILE_COUPLING_V1.md`, SHA `984fc0c74293ab6727b77265c3e64e3011653d95d5c4ed3f6df94641f2e37c35`; the fixed-kernel profile source retains SHA `272046ff1cc2a729826b0c0fe2c09354c6e5c19d2bcfe4222b166e295a3ae908`.

The universal proof is analytic. Its non-elementary input is the precisely stated localization theorem in Section3; the equality argument additionally uses metrizable Choquet representation. The supplied exact executable checks all polynomial identities and27 whole actual facets, including genuine nonzero cross-covariance examples. It was run normally, in a directory containing only the exact source, and after decoding the inline recovery into another fresh directory. All three report and stdout copies were byte-identical. These executions are supporting algebra/geometry checks, not a proof-assistant formalization or a claimed coordinator replay.

## 2. The affine-square formulation

It suffices to prove, for every real s and every covector b,

    alpha E_F(s+b·x)^2 <= s^2+5 b^T Sigma b.          (T)

Indeed the associated positive-semidefinite block matrix is

    [[1−alpha,       −alpha c^T],
     [−alpha c, 5 Sigma−alpha T]].

Since 0<alpha≤3/4, its scalar Schur complement is exactly(M). The identities Tq=c and q·c=1 imply

    B^(-1)=alpha T+alpha^2/(1−alpha)cc^T.

Inversion then gives the stated inequality for B. All these are moments of the same actual body and the complete facet. fileciteturn46file0L11-L35

More generally, for any affine y on P, with mu the uniform probability measure,

    alpha E_F y^2 <= 5 E_mu y^2−4(E_mu y)^2
                  = (E_mu y)^2+5 Var_mu(y).          (T')

The **positive** squared-mean term in the violation functional is important: it allows the localized measure's mean of y to vary while preserving convexity. There is no extra constraint imposing an independently chosen tangential centroid.

## 3. Localization input and exact one-dimensional inequality

### Localization input

For compact convex K, an upper-semicontinuous constraint f, and s-concave probability measures nu supported in K with integral f dnu≥0, where s≤1/2, a convex upper-semicontinuous functional has a maximizer either at an admissible Dirac mass or at an s-affine probability on a segment satisfying integral f dnu=0. We use s=1/3. Its segment density is the square of a nonnegative affine function. The additional one-sided integral condition on extremal needles is unnecessary because the estimates below hold for all such mean-constrained needles.

This is Fradelizi–Guédon, *The Extreme Points of Subsets of s-Concave Probabilities and a Geometric Localization Theorem*, Discrete & Computational Geometry31(2004),327–335, Theorems1–2, especially p330, DOI10.1007/s00454-003-2868-y. I checked the primary theorem statement, including its semicontinuity and s≤1/2 hypotheses. citeturn281360view0

### Needle inequality

On 0≤z≤1 take probability density

    rho_r(z) = (1+(r−1)z)^2/I,    I=(r^2+r+1)/3,    r≥0.

Put U=r²+r+1, W=3r²+2r+1. Its first two moments and endpoint mass parameter are

    m=E z=W/(4U),
    m2=E z^2=(1+3r+6r^2)/(10U),
    beta=m rho_r(0)=3W/(4U^2).

For any affine Y(z)=A+D z,

    m rho_r(0) Y(0)^2 <= (E Y)^2+5 Var(Y).           (N)

A complete exact certificate is as follows. The difference in(N) is the quadratic form in(A,D) with matrix Q(r)/(4U²), where

    Q00 = 1+2r+3r^2+8r^3+4r^4,
    Q01 = 1+3r+6r^2+5r^3+3r^4,
    Q11 = 1+4r+10r^2+6r^3+3r^4.

Its determinant is

    det Q(r)=3r^4(r^2+2r+3)(r^2+4r+1).

Q00 is strictly positive. Hence the matrix is PSD for every r≥0 and PD for r>0. At r=0 the difference is exactly (A+D)²/4. Thus a nonzero affine Y gives equality only when r=0 and Y(1)=0.

A general nonnegative affine-root density has endpoint values u,v≥0, not both zero. For u>0, divide by u and take r=v/u. The omitted endpoint case u=0 is rho(z)=3z²; its boundary term is zero and its variance is positive, so(N) is strict for every nonzero affine Y. This includes all possible endpoint degeneracies.

The formula is compatible with the inherited normal-frustum calculation, but the exact polynomial identity just displayed suffices here; no numerical root, optimizer or full sharp-alpha normal theorem is needed for(N). The earlier normal theorem alone was not a full-matrix statement. fileciteturn46file0L103-L116

## 4. Uniform facet-layer proof of the full matrix theorem

Let

    t(x)=1−q·x ≥0 on P,
    E_mu t=1,
    R=max_{x in P}|y(x)|.

For 0<epsilon≤1/2 define the functional on probabilities nu supported in P

    Phi_epsilon(nu)
      = (1/epsilon) E_nu[1_{t≤epsilon} y^2]
        −5 E_nu y^2+4(E_nu y)^2.                    (L)

It is convex and upper semicontinuous in the weak topology. The first integrand is bounded and upper semicontinuous because {t≤epsilon} is closed and y²≥0; the other moment terms are continuous. Apply localization with the **single** constraint E_nu(t−1)≥0. The actual uniform3D measure is1/3-concave and satisfies it with equality.

A Dirac maximizer has t≥1, so its layer term is zero and Phi_epsilon=−y²≤0. A segment on which t is constant similarly has no layer mass. A segment missing the layer also has nonpositive Phi_epsilon.

It remains to bound a nonconstant segment meeting the layer. Orient its parameter z∈[0,1] so that

    t=a+Lz,    0≤a≤epsilon,    L>0.

The localized measure satisfies E_nu t=1. Write m=E_nu z, so

    L=(1−a)/m,
    1/L≤m/(1−epsilon)≤1/(1−epsilon).                (4.1)

Normalize the affine root as ell(z)=(1−z)u+zv with u,v≥0 and u+v=1. Then

    integral ell^2=(u^2+uv+v^2)/3 ≥1/4,
    0≤rho≤4,    |rho'|≤8.

The restriction Y of y has |Y|≤R and |Y'|≤2R. Therefore

    |(rho Y^2)'|≤24R².                              (4.2)

These estimates are uniform over all needle endpoints, all orientations and all allowed zero density endpoints.

Let delta=(epsilon−a)/L. Since the mean of t is1>epsilon, delta<1. Integrating(4.2) yields

    (1/epsilon) integral_0^delta rho Y^2
       ≤ rho(0)Y(0)^2/L+12R² epsilon/L².

Write D_nu=(E_nuY)²+5Var_nuY, so 0≤D_nu≤5R². By(N) and(4.1),

    (1/epsilon) E_nu[1_{t≤epsilon}Y²]
       ≤ D_nu/(1−epsilon)
          +12R² epsilon/(1−epsilon)².

Consequently every relevant needle satisfies

    Phi_epsilon(nu)
       ≤ R² epsilon[5/(1−epsilon)+12/(1−epsilon)²]
       ≤58R² epsilon.                              (4.3)

Localization now gives the **same bound for the actual mu**.

Finally, the sections of P at t↓0 converge to the entire facet F. Outer convergence follows from compactness; joining F to any interior point supplies inner convergence. Uniform convergence of the restricted affine function and planar convex-section area convergence therefore give

    lim_(epsilon↓0) (1/epsilon) E_mu[1_{t≤epsilon}y²]
       = (1/(Vol(P)||q||)) integral_F y²
       = alpha E_Fy².

Taking the limit in(4.3) proves(T'), hence(T) and(M).

**What controls the mixed moments:** the test y is an arbitrary signed affine function of all three physical coordinates. Its square and its own first moment remain coupled inside the convex functional(L) under localization. Nothing identifies y with the original normal coordinate, changes the body's centroid, assigns independent endpoint masses, or assumes uniform density on the polar.

## 5. Equality and strictness

Here is the equality argument, separate from the finite-layer inequality.

Let C be the weakly closed convex hull of the mean-constrained1/3-concave probabilities used above. It is a compact metrizable convex subset of the probabilities on P. Metrizable Choquet representation expresses the actual mu as a barycenter of its extreme measures. Those extreme measures are among the Dirac/segment measures identified by the localization theorem. The representation fact is the standard compact metrizable Choquet theorem; see Choquet, *Le théorème de représentation intégrale dans les ensembles convexes compacts*, Annales de l'Institut Fourier10(1960),333–344, DOI10.5802/aif.105. citeturn102336view0

Write this representation as mu=integral nu dPi(nu), and let m_nu=E_nu y and s=E_mu y. Because E_nu t≥1 and their average is1, E_nu t=1 almost surely. For every epsilon,

    Phi_epsilon(mu)
       = integral Phi_epsilon(nu) dPi(nu)
          −4 Var_Pi(m_nu).                          (5.1)

The same representing measure Pi is used for every epsilon. For each fixed extreme nu the limit phi(nu)=lim Phi_epsilon(nu) exists. We have −5R²≤Phi_epsilon(nu)≤58epsilon R², so dominated convergence applies. Also phi(nu)≤0.

If a nonzero affine y attains equality in(T'),(5.1) implies

    m_nu=s and phi(nu)=0,    Pi-almost surely.        (5.2)

A Dirac mass, a segment missing t=0, a constant-t segment, or a needle whose density vanishes at its t=0 endpoint can have phi=0 only when y vanishes on its support. The same is true for a needle with both density endpoints positive, by the positive determinant in Section3.

The sole nonzero possibility is the r=0 needle: density3(1−z)², initial t=0, final y=0. Its mean z is1/4; E_nu t=1 forces its far endpoint to have t=4. If s=0, all these needles also have y identically zero, contradicting a nonzero affine function on a full-dimensional body. Thus s≠0, and(5.2) gives on almost every representing needle

    y=(s/3)(4−t).

The barycenter representation and full dimensionality make this an identity on P. Moreover all these needles have the same normal marginal

    rho_t(t)=(3/4)(1−t/4)²,    0≤t≤4.

Thus alpha=3/4 and P reaches t=4. Choose any a in its far support face t=4. Conv(F,a) lies in P and has volume

    Area(F) [4/||q||]/3 = Vol(P).

Containment and equality of volumes of full-dimensional convex bodies imply P=conv(F,a). Hence P is a pyramid with base F.

Conversely, at such a pyramid the actual centroid identity gives a=−3c, alpha=3/4, and Sigma=3T/5. Therefore

    5Sigma−B^(-1)=(9/4)(T−cc^T),

which has rank two and kernel span(q). Equivalently B−Sigma^(-1)/5 has kernel span(c), and the generalized eigenvalues are(1/5,4/5,4/5), as also seen in the inherited pyramid calibration. fileciteturn46file0L128-L141

This proves the complete equality classification. In particular, all facets of a nonpyramid have a positive-definite gap. A10-vertex pyramid has18 rather than17 true edges, so every actual10/17/9 body has a strict gap at each facet. **No numerical uniform margin on the entire E17 realization space is claimed.**

## 6. Explicit mixed-covariance consequence and profile interpretation

Choose any tangent frame t1,t2 and H=[t1,t2,c]. Since q·c=1, in these actual coordinates the marked facet moments and volume covariance have blocks

    H^(-1) T H^(-T) = [[C_F,0],[0,1]],
    H^(-1) Sigma H^(-T) = [[A,z],[z^T,sigma]],

where C_F>0 and sigma=q^T Sigma q. The new theorem is exactly

    [[5A−alpha C_F, 5z],
     [5z^T, 5sigma−alpha/(1−alpha)]] >=0.            (6.1)

Writing delta=5sigma−alpha/(1−alpha), it implies

    z in range(5A−alpha C_F),
    25 z^T(5A−alpha C_F)^+z ≤ delta.

For delta>0 the equivalent tangential Schur condition is

    5A−alpha C_F >= 25 zz^T/delta.                  (6.2)

For delta=0 it forces z=0. These are the quantitative cross-moment restrictions absent from a normal-variance assertion alone. They concern one actual set of volume and facet moments.

At any physical M>0, taking a trace pairing with(M) gives

    alpha E_F ||x||_M²
      +alpha²/(1−alpha) ||c||_M²
       ≤5 tr(M Sigma).

This can be used directly as an actual-facet realization constraint in a mechanical packet. It does not say that a separately chosen M or polar covariance is physical.

For the fixed released kernel's regular active centroid completion, the supplied derivative identity is B=−Hess log V. Thus the profile now satisfies

    −Hess log V(z) >= Sigma(P_z)^(-1)/5,

strictly unless the marked completion is a pyramid. The matrix moment theorem holds for every actual body; this **Hessian interpretation** still requires the fixed-kernel variation. It is not a Hessian formula for moving all other facets independently. fileciteturn46file2L1-L3

The separate conjecture alpha c^T Sigma^(-1)c≤3/2 is **not resolved here**. The present theorem gives alpha c^T Sigma^(-1)c≤5(1−alpha), which implies3/2 when alpha≥7/10 but does not cover the remaining masses. The original source correctly treated the universal3/2 claim as numerical. fileciteturn46file0L188-L190

## 7. Exact actual controls, including nonzero cross covariance

The exact program reconstructs27 whole true facets on four bodies: a tetrahedron; the following nonhomothetic pentagonal prism; a seven-vertex asymmetric body; and a fixed affine image of the prism. It recovers all maximal supporting planes from all input triples, strips redundant/collinear face points, constructs genuine edges, checks strict facet corners and incident rank, and integrates each complete facet. Signed boundary volume integration is independently checked against a positive interior-apex tetrahedral fan through second moments.

### Nonhomothetic prism

Take

    P=[0,1]^3 intersect {x+z≤3/2},    F=P intersect {z=0}.

Its true vertices are (x,y,z) with y∈{0,1} and

    (x,z)∈{(0,0),(1,0),(1,1/2),(1/2,1),(0,1)}.

It has actual(V,E,F)=(10,15,7). The selected facet is the **entire unit square**. Exact moments are

    Vol=7/8,
    g=(19/42,1/2,19/42),

    Sigma=[[265/3528,0,−121/7056],
           [0,1/12,0],
           [−121/7056,0,265/3528]],

    alpha=76/147,
    c=(1/21,0,−19/42),    q=(0,0,−42/19),

    T=[[151/1764,0,−19/882],
       [0,1/12,0],
       [−19/882,0,361/1764]].

The centroid-regression defect is genuinely nonzero:

    c−Sigma q/(q^T Sigma q)=(−59/1060,0,0).

Its exact matrix gap is

    5Sigma−B^(-1)
      =[[82675/250488,0,−31403/500976],
        [0,659/1764,0],
        [−31403/500976,0,39203/250488]].

The three leading principal minors are

    82675/250488,
    54482825/441860832,
    111178717639/6235540061184,

all positive. The report contains all seven principal minors, the exact B, its inverse, every other whole-facet moment and the complete true incidence.

The asymmetric control has literal raw vertices

    (0,0,0),(1,0,0),(1,1,0),(0,1,0),
    (0,0,1),(1,1,3/2),(2/5,1/3,2).

All nine of its marked-facet gaps are positive definite. The affine transport check uses

    L=[[2,1,0],[0,1,1],[1,0,1]],
    a=(2/3,−1/5,7/4).

The source verifies Sigma'=L Sigma L^T, T'=LTL^T, c'=Lc, q'=L^(-T)q, alpha'=alpha and B'=L^(-T)BL^(-1). There is no independent polar transformation. None of these controls is claimed to be110; no equilibrium census was needed or asserted.

## 8. Work tried, reproducibility, and scope of computation

An initial actual-hull search with a square selected facet and three positive-height supplied points returned a numerical ratio1.0000000000000022 for the largest eigenvalue of B^(-1) relative to5Sigma, after2970 calls. Its hull retained five vertices and discarded two redundant supplied points. This was another numerical pyramid calibration, **not a violation** and not incidence coverage. The complete source, seed928444 and all nondefault settings are preserved in the recovery but play no role in acceptance.

The decisive change was rewriting the desired inequality as(T') and recognizing that its violation is a convex functional of the measure under one normal-mean constraint. This keeps the mixed moments without adding a second localization constraint. The one-dimensional determinant has an elementary positive-coefficient factorization; the uniform58epsilonR² bound makes the passage from actual facet area to localized needles rigorous. Choquet representation then supplies the marked-pyramid rigidity argument.

The exact program was executed under **CPython3.13.5, standard library only**, with assertions enabled. Normal, source-only and decoded-capsule runs reproduced identical outputs. Optional discovery uses NumPy2.3.5/SciPy1.17.0 with single-thread OpenBLAS; its floating output pin identifies that run, not a cross-platform exact assertion.

### Complete source-only recovery

Save the complete block below, with its final LF, as `recover_facet_matrix.py`. It contains both full source units, not proof outputs or external imports. Run

    python -B -S recover_facet_matrix.py fresh
    cd fresh
    python -B -S facet_matrix_exact.py > facet_matrix_exact.out

Expected terminal markers:

    FULL_FACET_MATRIX_COMPLETE_SOURCE_RECOVERY_PASS
    SHARP_FULL_FACET_MATRIX_ONE_FIFTH_EXACT_PASS

The exact verifier prints ACTUAL_FACET_CONTROLS27. It needs no source file from an earlier branch. Its mathematical continuum premise is the analytic localization proof above, not a saved computational certificate.

Optional numerical discovery replay:

    OPENBLAS_NUM_THREADS=1 python -B explore.py 3 4 928444 0

That source explicitly fixes bounds[−3,3], exponentiated heights, maxiter180, popsize10, tol1e−10, polishFalse, workers1 and the stated random generator seed.

Pins:

    facet_matrix_exact.py:11905bytes
    d9c0671ab4deee1b8b28ce42843f0183786581c6281153fdff741829710daefb

    facet_matrix_exact_report.json:90079bytes
    d2eaabe3699ede1fe8ad419960fa35f70dc19459462ed7dcbc1ff5f4ba84738a

    facet_matrix_exact.out:226bytes
    1735b360895d6eabd73e55f6ab39fa3e816200bfca1ce3c460dde6d2f1554a30

    explore.py:2403bytes
    fc47d9277386469fe1b59550e958d291120b7ebbd6e6b4d0961252d7c17ad6f7

    explore_3_4_928444_0.json:1885bytes
    1f9288225477ace6aff0789c804ca87710149edaa47d02de73c299e1ae96c06d

    Complete decoded two-source map:14844bytes
    1ddcf0e7507d2b1e320325826be893aff12ffef5ea518dbd6decb70bbe4ac474

    recover_facet_matrix.py:8377bytes
    26bb1cee127a8d9982d940c59beb6404398a4c18c888dd7e22b371c10ea10472

Convenience copies supplement, but are not required by, the inline recovery: [exact source](sandbox:/mnt/data/facet_matrix/facet_matrix_exact.py), [full exact report](sandbox:/mnt/data/facet_matrix/facet_matrix_exact_report.json), and [recovery source](sandbox:/mnt/data/facet_matrix/recover_facet_matrix.py).

```python
"""Recover both complete source units; exact acceptance has no numeric dependency."""
from pathlib import Path
import base64, hashlib, json, sys, zlib
PAYLOAD = r"""
c-pNy33J*=)_+CosjpB&b4d6Kq*IF>yCxZLE|bjG5=JGY24sUo)B=Mu`S1H)A389e%vOClWU2dI{jPp}`1{c`T5xgH`+mf?t3{IX
)@pauJBpU8B+aZue2o*);_)U*lXz5n|KaN0#m(T>d-wTY-tgB?SA*BLwK1zXwXd;8iPy{3&hmv7ufE39G+A0Ah*rCnSovAxFDwmq
nZz5u{dK)q(2sL?UZrW0RuC3Z>@Q{po=3BdzYy~ZNV3YJW%S4mP#8_8JmoPm^7tlMtg|SIH45;bFQSQo{Q#f2(03w<so242zs4b-
TC0U0`>B0FdS7E}&I)1ei&2mE+%f52u#3^Wwc%+N1ze2#3A<=5xgXp9HWI8u`UBSKFV`$ywH|qz2)j%AZ;LOxOS^;s^=Xn?krl;O
>c=x~FL(@WC0}bJ5Z+Hye`k*pdNGQ|@UWwXL;g>}jX@9}fdZf@?2Q;X<0d>iV+v1KzY}<CyGT*6jcAGWvJkSte2@~Jb<ytj-{Ol6
^pbVPQ(I6$8h|nU=SGmWgCtU(t<%`LpaZ&Gw+HlXd(h0`WeYxtQKZQHOxPE6l|*qSC}6W|Fe8@(1R~con9|E@mMgsf0f(~zyx`u>
5eey6tnh(=zCTp;{e^u1g9xzbLRzGm0E>qQsltiCK`D=Fg*>yr5Yj&F3&Fk=>TpOOT!uY7$R^Sk^Jtne`{4mh{w|66xGn@KYp-n|
*8u~qC@ssQ7<+3mjUyW0HD5({HTv*C1?UkJS%tU<koyAW3;lw0f@H(qwr#f~2^X4`vQYUX{TWLd^0n_TR&$>XuIn>2F`)DV7EGHn
pp^OP474pF>X+9I`O>zXrhFmwoOD0~<jgnB#F(vc=}8^LA^imhFZX9$(+d7ss8S@04YvVG(TJw#A3g0OVH9LG5L|OMT_k>H^UbK~
j0pukkWsKhFurMJ$s!V&O=!+Yftyc4Q~v?1ox^46ntLYlSP_H;L;yJ;O`?#^iZ)CKOU~d2Rcez@dK=A_K7%2Yuvt)ifOB467oSr<
;2AQ_9WC!8MR=%@njlEmu?-fVP{DafgCqv;j>~}nk*^|Mrhs@t>Mq)66}96DBpQrwZ-h@s8~{Qnyo)H#-&INhJYZ=}xX9S3qg=Kh
_=|;rPwYWi*6|7>YpXKMW07FCq?K|p_g5eQq$c3C+CdOJg7dp$=Adnj<Q50PEp+GY%2oiRuSfo<`6QD&!$gVz5;T~DpIN%=ZJ0?6
xjd*ni*EzI$}GE>5@_LUH&HxT%v9?a^d9+2jJrAf6iI-bn^&j<;3(Nkg^YS*Hrmjw9@bcPNKmKY@a9=>l|r7eYhT{HzZneQynlx?
+|{Qymo>Vf)5TiM*$})=3aR-uH`3mM9iDY;&;T9TP0aJO@?%_&X{sy^1`m@ZWTdITUSuA$+UO&ME+NH0a5Cq-11WGNV3K1FzJjaG
mFH0KI|i~t^Fxx}^At0f6bYxaeFaM;VDQOd^cB#k7DfVGpQk&R#lP3$S}&%xcmh8rw1$$@deUcW#`LwGd4o2zD>P{H0>V0gcz~u!
k}PacO-r|sA0QWG8#b-!D#QC8|A7A!cpwA#f$BH3$&VJ!$hAIB(l#KH)<X*V@G`#5Z0u@<P-X~Q4TB1Jc=voKq>*R@Q3vtml1A<8
*SJRd%D6y>=E7<Zp+*rV+0@2WbAyj~UhFTq=P_3Eyrmz-o>%K(Oe0Y!8X$mX8>!n$gS+3*g$AjaO6&2M5cEWx&`l$Gb*y4crHHTb
5j~QL2iRw6wDtJb4>DD${qm3YTBPks6t^L%TB}_)PvS15o+JEwg@72ikPa6@78}`|TT=)x3wqZ6qA3Ymim(MaqdA3{WsYEAr)BGF
eEC7rw7M;)+d82*r^lh6h89#)sh{pz*1N<qrC3TKh{1CqVy)26d}?8R6R*~pB`Zy!Hv|Dtq9|Ukp)5<21k#e=LNb>wkb;skC{~<y
*IFcCv*^*sn4(skWGES^CIbT^H8oCM<4sc-6aWfS<z4FrEJ&|45C&G3pgJ^AkSsxcl7pZqP`C~<4Gemj8@O2zQfm<`|3*PM_XYM*
Sy`HSAWSmbrxVgMDFkZ)dt2X0yKLzW%fQEIC4mUNwmX;=Wf`@eR57#lYQgPo^DwGHQZ-=(&Gx}h>l3UDeR#l|Gp72jgKZtvOZA(B
ZI0^IRIz#*6clkx0}Ld^ZGZ#^==&NxOUuwW-~p7e@Nd8H?G_k*ELMr&WkfYz9AJH50GB|EUhKoDCyJFqQ6jknMmcq;tYr(jq%|;f
Hb7^)Pe)PM9)MS6(*bj6qiB0dlS~x;7T<lt&kw`rCEqp<+f+8fn`uM>#ycQF0G$pFQ_SkyLWuOhfUtb9_i=4>KT7J|XAQ-7+&;|l
+Kw2zQ=IN9n9mZ6;tkqc&dXNFl$Z5=Avmt<RI_m+Ib5e5(!y2jefP`#(Zz;NsiA`nkgZAXM^T)lqTsHX4j3!DVnqad^sE<;8w%3=
F_87a=xz-En)3T@T(7$dnMw_nbC7LlQ5VRKlrBvCt-_y43gu*I;W**nt4{f=jswS_mfsG_paB$*SDkzToI*Cwq74><bHnbD$wD_K
jnRDEhdGu(GPLXV77Ca+S)%wbpxo6S2{CvhobtAH04v4A;}}*lkW=mYV^zC45ZdionOJ#k&b?q40E}K%Mxmf_?mTI-Vlfs9(NpW-
OdEp%z_qqex{aOziT=Tmj4Bf?AkVPG;GvD2pwM6oe>n+#E9z+x(56Tc^g5<{P0o01G$HdF4ABOw(|aSaG$ozDx?`kKGv!zr%B5k)
{WaY%Bv>FBZ=8(Qn5frdQn!QA2H!Vh(u8*Nj_n3U;V+U0s4quAcD0f(sySB&jI<=)!yG1WS))ii@`}0AZ{%QP)2IoNrr#h4Bl41U
dh)vk1*}a9TB^|pwlOG_?D0*p5EDw(<e&sn;Hm_&NlKvKatY-3z67dqPXh2LrsVGddP5PySCfU1Hvj?Wt`5J7&C1CDz(&39*!Yi{
`eU7fa5A4zpHO@WFt?MJogSdH^w^E4_Y51cn%&wEU6Oge&{9EyjP85mhGcj@&VyvelO>0h7Nn8~qeUerD<|ruzp}6CO6TR33WEny
9<hMTU^ZbG!xsIeiDEPg_Wei6jOee=<g^k#fu&H%zA-DbqcwV03MHj2{dr&RDA^T*8wx}}-a(S;=^B$4{d1=5P$2ikf{o@)-CR<G
0vT6mqYcCYjP(+hXZUu21%jzg^uAbYyIGonW8BMX&L!t^yI715kzqjQDI3f|)g0YdmKZ_L*w|Pl5h{>8kJn3B;ba_%B7FgrP4M}+
ky1_pKn1g^luKnkMZN{a^HSKPYPqsA0VcY>+_Ag1@e4ls7+lXL?t+vQ!~`ZfH^rfqrEH-%b}0o<dsCd=`?v{|r|Iu1uTK#j#~@LQ
@SOh8BzZX7bKYr0ZG@JLt9p|}$^%!<zN$iL@9tHr0Kp0;Gtnhpu}&2VXC9;`$I{bawloxDc4S6Esv_K1caJ5+K7WkKjE%5wWZyT0
+CY||Ds72M4O2xnRoGq*`&pD`dB+`ATd(#8D|O$3^rCk^bV|||#90rJ=x9ugKTMy@6-rMfPXs4cJL<-Sh4GDU@vAgGJvK}kSOfXG
&VG`<U}e}fj%aWe3#D)Y)=|aWRE3%xncColP?6IV0!nd76JI3=X&56&3X1q^hJ|<kH#Wkb<9fIMmZ<{0<fQwfD;E+>D_z>UGagr+
rBsePH1~m~v+poCvy}<m6?KjJZa`Vn51CriDyIM(2zxWb_}~wX2|j}7mV0G}uNy4HQU8V*VI94xeSDz2-is^2ild5ZSDwmkIZu-w
z{;hU5LDr;aOSHby;UG@saj-&ZMTDa_f^Bce$|1>)l{jkixmDF>8tHz#YeAGUemWk(`!1K^^DHIyZcbgO9V~-7i$287fj&j?>x?6
77{YUTNzB|{+x%YzW|HFT2gL<Siah{vXZGa{Pg+C%6GyQy+jL%%kDfBjWO=>2qNvmJD;`FYgap_Tk=d-yJjC`s>~mM>7h!CCLt!3
%<#YXDAwh+c5|w|l;++EdG^`*3^4Z`NqMr`XGut<QcFywmY~T@GTcvR!uWlH4*XN+@4t4z;j1K2wZFOA|DO$j{>P8T=jFN5b6%fN
?e_pL{qf_+zwmokJHA`?{Er`rG;Ka3<9r?NM+0N8RVn@(W521lw~W1Y&6+Mq(h#c)hz*9z{IbXYuT$==a>C2P2ZuxBgZ}?l>I1F)
jpSEFdSFjVe5mnFksshIA#K~OE3mlmq=zS-WD=-yBIQNTxzTNdJ)k-+5$Zvu&F)Xr=EuL2HNkyQ6W~DFf1Y<AFoFab4z>F{v>lgz
EQ4L<3G=o{n3tqK#KS$4DsSm<2*n~prCmabEYLLr#RX9I6Y8Z*sI-)LOS$$EdiL|~utZ$IVh_(uOiG#+HJa*yg#Rs<U$>Pj`ciU}
M~kQR+qwp8zc#cwFJ<RTaN#aJCQlOLa$^taH>d;xwIu_he1rI9>ex*Exu{Mp>If5qYDk{UG2eig8tX-g*+o<)p$H5Ot~%kZyTv&%
Ee?qbmt8LH3wjZOXmSs*AU^X~W$GvDbhRWIAdx;m!BUFpeK+_j2*V0X^^!_)3?syaaZdiiP`rjvJ|Vz{RA^|@1sbW+g9R1;YeD~x
j=G0*L=G6XkO&#?$&&I}%7uU`lc{OO_?dEmrB0Y=%);f$t)xs#CR>xQ<q5nxIFh>v3{tIJe=(JBlXU4X7)-&_Db(R?PW_bo9-aq!
s?UQoIm_nkmR92(&)0d%L(fEx{)q>aoPDbtutTtVN{0MY{t}Pa>5vWS1p`O&w4K;Rw8v)(wT~wU>VX2+!Yg3GsK937;n`jgtw2_#
Vy66OkB}bD#!n+Z4mf+N+x*UeR~W>Dr3nu*R<s<@gT&dpBZ1@tMP4~YWq(te1=XT=Wb|S<zt+IFXfAoVK^A4IN3B)$@<^>8O43LW
eK}z?J+S&6n+p)H+oz@b5&HgvQbR$`6rMmb_WTvNPD0CV;6Smt3!$A(?mhitsS`(E0E;k+XVyB7q}DSIL>D{UCx#jpTC(|)L$TU2
r#=zXsQFfv+G)<Wr&MdP1-K%w9GN6>yJv;leZ5tAldrNzwlX{CzB;rqoybw2b>K`ZSBNi>IxGU^>1&5H>`A3(lK1RSvAA2KaH#?;
&KFj~hQK()w{kMG%HfwvPQ5K@N*ztUp~yF#@?w~7t96sVzfEzcPLm1<pbsTQ<8Itw+xo7mH54!~!hrth){xuC@~dDRRCa7(j2pJ8
ZyP~{-o|W7#+-)>?)i%upQOHRh<;`^q;Wj&)DP1CJ#TXHfrZY0@}@36PK{H1>vR}c7L<HUL35w!XNYC^YIf=GfcCB9FlhcAnl-%R
Xn0q_|3||+RKopEip_e+ad@f`XA)y+11}2rC3qlD;Xf(uQDsTWpudaVc899Jh_l2?e=felq;*W4A}^RVMTsF(l%$j6`~j@<b<!`^
N3dhtKK}fN3k9=~OF?shKeg;DYe)WY8z<HmKecy6%~JIpSndy(8WQq|(iVgb8W(k;4}oHc@SSBl4Lbz~695m%Y7>P#v?e?2bGxe-
mgYi1Wz8qg6xFdIPRow|>E@PIZ=K5K)EfpK_L-)n-R&>&{dat~9k>35^p`HS{71HQJJ_NomSy`*K>^R9j_aBV%*#)vU+6-^0TBdc
y0SS8=Hy_@g8)tea8h5o&ExvA{uHvfWoH*qqzMm(15&2dgenpnz2*z9R86IHNtf=Px7d1Ipk^()esk~*Hw?iB)XBFNuHsNmG}fAR
@P2|ZcUOQ{Kq9p!$r|r<>@4&`Dm^0KfB3fcL&zI4U6*9QO7?^_RY40QVY0S8FT3jJI0ENbT4D|p^*zi8&4s_?X?~eZZOg738|L(^
H?Nq}KBm^6={%|Z`I4RI?g|Yr8TRb3-Tl<J<{Tz+>rWec>N^Mo*?#=#54S4fdE>Z#%%DdO=%ns8z_*~`<oxNJjJZU{I3x`j*^nzx
o#ntRz3&wRdpX0?xuDjqr+*yR?G!@Nt*4DHQSZm_?vUC6BKnd~=}?u`Gyz2U!>!Rg0L{w*GE&c;w5n&c?RC5?@#g+w3JNH0>2jE$
7j~ZJalR9g#0a1grPul7C9)L24nv^|bHMKic~5$p^hQmX_jH3vVrz~OejKKxrbmi30Ldwis-zU5am9#RGa$UBW$&Gmd!W$Cdgghm
Rqm*<{G3duYMGnWPe|JOXNNlbsaj%>YO18FjnVHNdP??^p@vd*Qf>Tn4=f$kWPB?M2UmrfhAhw!Of5oG;8DOI*2V{ylF;>h^;{bx
Di-U24VglXy|m2&>r5z8Dy$LX;vlo7T9)7Lugc`&&@9T!y~m|qU|-(eUilH!@X{K}7V@d)5qQ-Tilgjfi~?%_u`Fz<i@Gh{(MM9;
#gQ2LZq1{txRBR=R+Z%?(i_zd6yz{|x(^|1@k1TP?kX7r_Y-=ixe302g#{1QMTN9*8I5mH<(2ADO)X#0{L)k~H_L1WJ!<KOJ)OPN
i5O;g&1F=3esPmqw6s_)@D8o80K=qrU+k8D6+=!QL-Oa-90h-LfGJ?~Yi(#3odoSI@4=A$*h1E&&?-rv{#5K=tN|=7w@}r{c*vp&
tSkKKG>Wl~T3NxI2loOm<LmWe8!ySqdQ4xmK?P@40$qBxxnX!?s;G53Y7m`rSxfD_Q#BZ8P`_w^LzcB|(@{e|gM2{xH(BX+&kcO5
UDO+6HYxVL^FMo+3^KzFEJpON5|j_TmE#r5(%N|cyi0N_r6LUcC6ZI9x}DIQ>@Z@HE%6sJ@VM=Ukh;b;oeFcZL(8)7(=>U6G6g`v
s&eZB81zc<VrUyj__60Ed+}6C!5gNSj1Ka6dPKM><?14D%Q%FtKq>^4o5~Mz2!B}Cn$F#YwyLlyIZK))^GBqVxDTOS6fB;gT}XCO
zDAZiH?r`F@U#hPK~}r{b@1tfcm4V1#=9O|UJbo}4ThiI{M&o~?#jD<b3Odk`{LB7TFJ5f1s#1_$+D50MU;<F3|gv8Hl`-aKzu?d
dK!b7<`OXxBrDEp19@RtUS3wWmfOl{tR?t9R+4B7EsT!g7S^9Q<pEylrg8aFF<xJGoDSYozH-j+R}dC!%#W>dX}0oHe~Go7PzqCH
@E}>R8+8qFA&D^^S6apX11n!w*A<M?Jo(wR^%fMkNto}i%DeEjr`NzeMNZwAHy7n6yNnBY`A4UiG+>f|=ixPM&%@vL@Iwt(Or!Wa
5V!9?f4aP?$>|L62-TOFTVn3JC#SNlHRszff_YE>-b;b~>FUG#PeX-`{P(f3?Ro6M<?!>sxZdUacf(KbZ*FT84=|D7tcYZlx@Kwv
LfzpvK38NeGoqh5_0_+Dv-e?edt3X9OaH2@{2CwqphqjHSNDHya^xO&y7Xuo9G`_R+_SUp`RVcLiz#;|CofJ;I{d}SdFZ}y9Jez$
<C95v%1<Z9VdurE<DR(TS>T-c;pz13X#DJT|B>Uo=$z1_@I}x$J#&0O=N#ytPu%l>AG_zr-D$@;@1C8Xo}4?useA4?C*5f{ot_;#
=kAL$rxW^oIyoBu`0-z;^>q^
"""
def main():
    raw=zlib.decompress(base64.b85decode(''.join(PAYLOAD.split())))
    assert len(raw)==14844 and hashlib.sha256(raw).hexdigest()=="1ddcf0e7507d2b1e320325826be893aff12ffef5ea518dbd6decb70bbe4ac474"
    obj=json.loads(raw)
    root=Path(sys.argv[1] if len(sys.argv)>1 else 'facet_matrix_recovered')
    root.mkdir(parents=True,exist_ok=True)
    for name,source in sorted(obj['files'].items()):
        assert Path(name).name==name
        data=source.encode();pin=[len(data),hashlib.sha256(data).hexdigest()]
        assert pin==obj['pins'][name]
        path=root/name
        if path.exists() and path.read_bytes()!=data:raise FileExistsError(str(path))
        path.write_bytes(data);print(name,*pin)
    print('FULL_FACET_MATRIX_COMPLETE_SOURCE_RECOVERY_PASS')
if __name__=='__main__':main()
```

## 9. Continuation

The full1/5 question is resolved by the theorem above. The useful continuation is to impose its entire block inequality on the same actual facet/volume moment data used in physical escape certificates, or to use the strict nonpyramid gap on a separately justified compact actual-shape domain. The sharper fixed-alpha full-matrix envelope and the remaining universal3/2 centroid-leverage question are not settled by this proof. Neither the curvature interpretation nor the strict marked-facet gap alone supplies the missing complete E17 mechanical obstruction.
