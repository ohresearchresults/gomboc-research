# minimum-0258

AI research report · 2026-09-27 UTC

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# H5_REFERENCE_DESIGN_FRONTIER_V1

## Results and scope

There are three substantive results.

**A wider, fully five-dimensional joint exclusion.** Every literal H5 body with

\[
x,r,p\in[13/100,17/100],\qquad q\in[43/100,47/100],\qquad
\lambda\in[3/40,2/25]
\]

has **S≥2 or U≥2 for every physical SPD M**, including incidental physical weak equilibria. The coordinate-reflected box is also excluded. Three different auxiliary references are assigned to the three possible maximum-norm top vertices. They constrain the same M and its exact inverse. The four basal-coordinate intervals are each twenty times as wide as those of the supplied intrinsic-hybrid box; this is a different taper interval, not a claim that the new box contains the old one.

**A large, fully five-dimensional limitation of the standalone product certificates.** Throughout

\[
x,r,p\in[1/10,1/5],\qquad q\in[2/5,1/2],\qquad
\lambda\in[13/100,19/100],
\]

R, A, and the seven-turn requirement hold with a specified moving rational alpha. Nevertheless, for **every** R-admissible common alpha, the reflection product threshold is less than 5, while **every auxiliary reference**, at **every top vertex**, gives an intrinsic finite-height product ceiling greater than 2368521/377600 > 6.27. This holds using the exact trigonometric finite-height factor, not merely its convenient 16/27 majorant. Different references for different maxima cannot repair this sufficient test on that box. This is a failure theorem for the stated certificate class, **not a feasible110 construction or an exclusion of that box**.

**A general reference-design reduction.** For a prescribed upper bound on the reference angle, minimizing Gamma is an SDP with one symmetric 3×3 variable and one scalar. The complete optimal standalone product bound reduces exactly to a one-dimensional family of these SDPs. An explicit rational dual permits rigorous lower bounds and all-reference failure certificates. On an actual H5 control below, a rational reference and a rank-one dual solve this optimization exactly for the pair (a8,qB).

The accepted minimum bracket remains **34≤C_min≤622**. No whole-H5, whole-E17, canonical-root-count, or attaining-construction claim follows. The bracket and the distinction between exclusion and attainment are inherited working results.

## 1. Input authority and the unchanged physical family

I read all six supplied files completely through EOF, including the complete 1778-line journal and its literal parent payload. All six native-file byte counts and SHA-256 values matched the supplied manifest. Reconstructing the parent as compact UTF-8 JSON with one final LF in its Markdown gave 44474 bytes and the required SHA-256

`b02e9ea175553f06a5fc27b626e52977c8baf76d50df0e70d68eff5fb913393e`.

No missing required dependency or conflicting parent identity was found. Historical archive items mentioned in the journal were not treated as accessible source files. The new executable is standalone and does not require them.

The family is exactly the supplied H5 body, not a renamed replacement. Put s=1-lambda and

\[
B=((1/4,0),(1-3x/4,0),(1-p,p),(q,1-q),
(0,1-3r/4),(0,1/4),(1/16,1/16)).
\]

Its raw vertices are z_i=(sB_i,0), i=0,…,6, and z7=(0,0,1), z8=(lambda,0,1), z9=(0,lambda,1). Its outward facet cycles, with the original numbering, are

```text
(6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
(9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).
```

The exact program integrates the complete oriented boundary to obtain D=6Vol and K=Dg. It independently checks the supplied closed formulas for these moving moments. All regional vertices are v_i=z_i-g; all poles are the actual normalized supports at this same g. The true facet lattice is V10/E17/F9 throughout both closed boxes. The underlying family, moment convention, and support-cleared polynomial tests are preserved from the supplied source.

For clarity, write gamma=g_z, let B_g and T_g be the centered basal polygon and top triangle, and put beta=gamma(1+alpha)/(1-gamma), r_*=beta/alpha. The inherited hypotheses are 0<gamma<1/2, 0<alpha<1, alpha≥1-2gamma, R: -alpha B_g-beta T_g⊆B_g, A: q·a>−1 for every nonbasal actual pole q and every a∈T_g, and r_*cos(pi/7)^7≤1. Under these hypotheses the inherited theorem gives strict basal U and strict nonbasal S. When alpha²<gamma, a hypothetical joint S1/U1 metric must have, at a maximum-norm top vertex a,

\[
P_M(a,q_B)=\frac{(a^TMa)(q_B^TM^{-1}q_B)}{(a\cdot q_B)^2}
>\frac{\gamma}{\gamma-\alpha^2}.
\]

The strictness includes zero spoke derivatives. For any reference C>0, the same physical M obeys the conditional bound

\[
P_M(a,q_B)\le L_K(\chi_C),\quad
L_K(t)=\frac{((K+1)\sqrt{1+t}+(K-1)\sqrt t)^2}{4K},
\]

with K=f(10)f(9)Gamma_C² < (16/27)Gamma_C², where f(m)=cos(pi/(2m))^(2m). These are the inherited implications extended here, not independently chosen primal and polar metrics.

## 2. Exact SDP reduction for reference design

Let v_i and q_f be the actual centered vertices and actual normalized poles of a fixed body. Fix a nonzero pair a,q with c=a·q≠0. Write

\[
\Gamma_C=(\max_i v_i^TC^{-1}v_i)(\max_f q_f^TCq_f),\qquad
\chi_C=\frac{(a^TC^{-1}a)(q^TCq)}{c^2}-1.
\]

For every tau≥0, define g_a(tau) by the following SDP:

\[
\begin{array}{ll}
\text{minimize}&G\\
\text{subject to}&X-v_iv_i^T\succeq0\quad\text{for all }i,\\
&q_f^TXq_f\le G\quad\text{for all }f,\\
&X-\dfrac{q^TXq}{c^2(1+\tau)}aa^T\succeq0.
\end{array} \tag{SDP}
\]

All constraints are affine in the six independent entries of X and the scalar G. In particular, the apparent inverse-product angle condition has an exact LMI representation.

**Theorem.** The SDP optimum is attained and

\[
g_a(\tau)=\min_{C>0,\,\chi_C\le\tau}\Gamma_C.
\]

**Proof.** For X>0, the rank-one Schur-complement identity gives

\[
X-\frac{q^TXq}{c^2(1+\tau)}aa^T\succeq0
\iff (a^TX^{-1}a)(q^TXq)\le c^2(1+\tau).
\]

Given any reference C, let R=max_i v_i^TC^-1v_i and put X=RC. Then X≥v_iv_i^T, the angle is unchanged, and max_f q_f^TXq_f=Gamma_C. Conversely an SDP-feasible X has max_i v_i^TX^-1v_i≤1, hence Gamma_X≤G. This proves equality of the optima. The spanning vertices imply X≥(sum_i v_iv_i^T)/V>0. A bounded G and the spanning poles bound X above. Thus an optimizing sequence has a positive-definite limit. No polar recentering or new physical metric enters this normalization.

At tau=0 the last LMI is equivalently the linear alignment equation

\[
Xq=\frac{q^TXq}{c}\,a.
\]

This removes its forced singular direction. For tau>0, Slater holds: an aligned SPD reference exists, a sufficiently large multiple strictly contains every vertex outer product, and G can be increased. For example, aa^T/c² plus a positive multiple of the orthogonal projector onto q-perp is an aligned SPD reference.

### A rational, checkable dual

Let W_i≥0 and Z≥0 be symmetric PSD matrices, and let mu_f≥0 satisfy sum_f mu_f=1. If

\[
\sum_iW_i+Z-\frac{a^TZa}{c^2(1+\tau)}qq^T
=\sum_f\mu_f q_fq_f^T, \tag{D}
\]

then

\[
g_a(\tau)\ge\sum_i v_i^TW_iv_i.
\]

This is obtained directly by multiplying and summing the primal inequalities; it does not depend on solver status. With rational body data and rational tau, an explicit rational solution of (D), together with exact PSD minors, is a durable lower certificate.

### Exact one-dimensional reduction of the product objective

Fix k0>0, for example f(10)f(9) or its rational majorant. Define K(G)=max(1,k0 G²). Then

\[
\inf_{C>0}L_{K(\Gamma_C)}(\chi_C)
=\inf_{\tau\ge0}L_{K(g_a(\tau))}(\tau). \tag{O}
\]

For one direction set tau=chi_C. For the other use an SDP minimizer, whose actual angle is no larger than tau. Monotonicity of L in both arguments proves equality. The max with 1 is a conservative convention; a certified raw spectral ceiling below 1 already contradicts the existence of a hypothetical joint metric.

This also supplies a rigorous negative-search method. On tau∈[u,v], monotonicity gives g_a(tau)≥g_a(v). A dual lower bound at v therefore gives a uniform lower bound L_{K(g_a(v))}(u) on the whole interval. The tail tau≥T is automatically above a target T because L_K(tau)≥1+tau. Compactness of normalized references gives right-continuity at tau=0; Slater gives continuity away from zero. On a compact tau interval, strict separation can be certified by sufficiently fine intervals and exact dual bounds. This is a certificate-completeness observation for a **strict gap**, not a runtime bound or an assertion about boundary-only optimization.

Separate SDPs may be used for a7,a8,a9. Their references still constrain the same M. This reduction concerns the best standalone product ceiling; it does not replace the potentially stronger intersection of all reference-dependent metric cones recorded in the supplied finite-height source.

## 3. The wider positive box

Use the box stated above and alpha=999/2000. Assign the following auxiliary references to top maxima 7,8,9 respectively:

```text
C7 = [[761,-202,-326],[-202,674,-307],[-326,-307,1000]]
C8 = [[756,-256,-227],[-256,669,-307],[-227,-307,1000]]
C9 = [[749,-308,-326],[-308,669,-207],[-326,-207,1000]]
```

Their leading principal minors are respectively

```text
(761,472110,288323359)
(756,440228,298822087)
(749,406217,261455543).
```

The whole-box exact guards establish

\[
\gamma<69/250,\quad \alpha\ge1-2\gamma,\quad\alpha^2<\gamma,
\quad R,\quad A,\quad r_*<3/2,
\]

and, for j=7,8,9,

\[
\Gamma_{C_j}<39/5,\qquad \chi_{C_j}(a_j,q_B)<1/1000.
\]

Only the matching top angle is required for each reference. Each Gamma bound nevertheless uses **all ten vertices and all nine actual poles**.

Set

\[
K_*=\frac{16}{27}(39/5)^2=2704/75,\qquad L_*=41/4.
\]

For A=K_*+1, B=K_*-1 and chi=1/1000, the root-free checks are

\[
s=4K_*L_*-A^2(1+\chi)-B^2\chi
=96220753/937500>0,
\]

\[
s^2-4A^2B^2\chi(1+\chi)
=2989501777441/791015625>0.
\]

Consequently L_K*(1/1000)<41/4. The final reflection-product margin is exactly

\[
\alpha^2-\frac{69}{250}\left(1-\frac4{41}\right)
=70041/164000000>0.
\]

A hypothetical joint metric has some maximum-norm top vertex a_j. Its necessary strict product lower bound is greater than 41/4, whereas reference C_j gives a ceiling less than 41/4. This is a contradiction for the same M and M^-1. Ties between top maxima do not evade the argument.

### Whole-region verification, not sampling

For V_i=Dz_i-K and H_f=Dh_f-n_f·K, each reference uses the ninety polynomial guards

\[
(39/5)\det(C_j)H_f^2
-(V_i^T\operatorname{adj}(C_j)V_i)(n_f^TC_jn_f)>0.
\]

Its angle guard is

\[
(1001/1000)\det(C_j)(D-K_z)^2
-(C_j)_{zz}V_j^T\operatorname{adj}(C_j)V_j>0.
\]

There are **523 scalar polynomials and 370384 nonzero rational power coefficients**. Exactly 521 polynomials pass the normalized-box constant-minus-L1 bound. The remaining two pass full tensor Bernstein checks, with 264 strictly positive coefficients total and independent inverse power reconstruction:

```text
gamma_upper: degree (1,1,1,1,2), 48 coefficients,
             lower 18611/6250000000.
R_0_4_9:     degree (1,2,2,2,3), 216 coefficients,
             lower 266641914651/2000000000000000.
```

No subdivision, sampling, infeasible-cell pruning, or floating tolerance is used in acceptance. The moment integration, all nonincident support inequalities, positive pole denominators, and independent incident-plane ranks move with all five parameters.

### Exact nonredundancy control

Take theta=(13/100,13/100,13/100,47/100,2/25). Its actual moments are

\[
\operatorname{Vol}=2126089/15000000,
\]

\[
g=(200810930561/850435600000,
189262893359/850435600000,
2342089/8504356).
\]

Its exact largest R-admissible alpha is

\[
\alpha_{\max}=56842060453/113708949217,
\]

with limiting facet/base/top triple (1,4,9). The program verifies alpha_max²<gamma and

\[
\frac{\gamma}{\gamma-\alpha_{\max}^2}
=\frac{30282567004761046317811702921}
{2804824071741761354937152517}
<2401/192=L_{48}(0).
\]

Thus neither the old alpha²≥gamma reflection theorem nor the unchanged condition48 product test can close this actual body, even allowing the latter an ideal angle. The new certificate does close it.

At M=((5,1,2),(1,3,-1),(2,-1,4)), with its exact inverse, this control has **own435, weak000**, S={0,1,5,6}, U={1,4,8}, H={(0,1),(1,8),(2,3),(4,9),(6,7)}. All 68 primitives are nonzero. This is a nonattaining physical control, not110.

## 4. A whole-box barrier for every auxiliary reference

Now use the larger barrier box

\[
x,r,p\in[1/10,1/5],\quad q\in[2/5,1/2],\quad
\lambda\in[13/100,19/100].
\]

The explicit coefficient

\[
\alpha_0=593/1000-6\lambda/5
\]

satisfies 0<alpha0<1, alpha0≥1-2gamma, alpha0²<gamma, strict R, strict A, and r_*<2 throughout. Together with cos(pi/7)^7<1/2, these are genuine members of the reflection/turn class.

Put

\[
b=(1-\lambda)(1-3r/4),\quad c_y=g_y,
\quad I=c_y-\gamma\lambda,\quad W=(1-\gamma)b-I.
\]

The single R inequality for side facet1, basal vertex4 and top vertex9 is

\[
I-\alpha W\ge0.
\]

The exact regional calculation establishes

\[
I>0,\quad W>0,\quad I^2<\frac45\gamma W^2,
\quad 2b-7c_y>0. \tag{B}
\]

Therefore **every** R-admissible alpha obeys alpha≤I/W and alpha²<4gamma/5. In particular

\[
\frac{\gamma}{\gamma-\alpha^2}<5. \tag{lower-threshold ceiling}
\]

This also proves that no admissible alpha belongs to the old alpha²≥gamma class anywhere in this box.

On the other hand the actual side pole is q1=(0,-1/c_y,0), and its pairing with actual centered basal vertex4 is

\[
q_1\cdot v_4=-s_*,\qquad s_*=(b-c_y)/c_y>5/2.
\]

For **every** SPD reference C, Cauchy-Schwarz with C and C^-1 gives

\[
\Gamma_C\ge(v_4\cdot q_1)^2=s_*^2>25/4. \tag{all-reference obstruction}
\]

Let k0=f(10)f(9). Exact Machin bounds and cos(t)>1-t²/2 give k0>59/100. Thus the **certificate's condition-ceiling parameter** K_C=k0 Gamma_C² satisfies

\[
K_C>\frac{59}{100}(25/4)^2=1475/64.
\]

This is a lower bound on that upper-bound parameter, **not a lower bound on the condition number of any physical M**. At every top angle,

\[
L_{K_C}(\chi_C)\ge L_{K_C}(0)
>\frac{(1475/64+1)^2}{4(1475/64)}
=2368521/377600>5.
\]

Consequently no choice of one reference, different references for the three top maxima, or an arbitrarily large library whose standalone ceilings are minimized can satisfy the hybrid comparison on this box. The obstruction already uses the sharper exact k0, so replacing 16/27 by its exact trigonometric value does not help.

There is a useful robustness check: even replacing both universal escape-height caps by 6 would give k0=f(7)²>12/25. The same reasoning yields K_C>75/4 and L_KC(0)>6241/1200>5. Substantially stronger information than that modest height improvement is needed here.

The limiting R inequality uses only top vertex9. Hence its alpha bound also applies to a reflection coefficient attached specifically to that vertex. Vertex-dependent alphas do not rescue this standalone top9 product test unless additional geometry eliminates that possible maximum or strengthens its product lower bound.

### Exact regional verification

The barrier has **255 strictly positive scalar guards and 19002 nonzero rational power coefficients**. Of these, 252 pass the full-box L1 test. The other three have respectively 7776, 216 and 270 strictly positive tensor Bernstein coefficients; all three expansions are independently reconstructed back to their complete power coefficients. No subdivision is needed.

The two crucial inequalities in (B), after using D=6Vol and K=Dg, are exactly

\[
\frac45K_z\big((D-K_z)b-(K_y-K_z\lambda)\big)^2
-D(K_y-K_z\lambda)^2>0,
\]

\[
2Db-7K_y>0.
\]

Their certified Bernstein lower bounds are respectively

```text
60070099885884692530363007 / 655360000000000000000000000000
1284682961 / 256000000000.
```

The third Bernstein check is R_0_4_9 for alpha0, with lower bound 566202703809/256000000000000. All remaining R/A, spectral-factor, actual-centroid, support and rank checks are explicit in the standalone source.

**Precisely what this does not prove.** The barrier is not a physical counterexample to joint exclusion and does not show that the intersection of all reference-dependent metric cones is feasible. Combining those cones with actual top-maximality, spoke signs, or other common-inverse constraints can be stronger than minimizing their separate scalar ceilings. Nor does the barrier prohibit a stronger geometric product lower bound. These are the appropriate escape routes from the proved limitation.

## 5. Actual control with an exactly optimal reference

At theta=(3/20,3/20,3/20,9/20,13/100), a point of the barrier box,

\[
\operatorname{Vol}=6497249/48000000,
\]

\[
g=(92526062243/415823936000,
87300500333/415823936000,
7672449/25988996).
\]

The exact maximal R alpha is 71341806413/154940815225, again limited by (1,4,9), and the corresponding threshold is

\[
184189845528335946123113480625/
51914865174695118759383445901<5.
\]

Here is a complete rational reconstruction of a reference that optimizes the full-body product ceiling for **the pair (a8,qB)**. Put h=1-gamma, b=z4_y, s_*=(b-c_y)/c_y,

\[
R_*=s_*\gamma h,\qquad L_*=s_*/(\gamma h),\qquad
z=1-2\lambda,\qquad H_4=1-\lambda-c_x-c_y-z\gamma.
\]

Set Czz=1 and

\[
C_{xy}=-c_xc_y/(\gamma h),\quad
C_{yy}=c_y(b-c_y)/(\gamma h),\quad
C_{xz}=(\lambda-c_x)/h,\quad C_{yz}=-c_y/h,
\]

\[
C_{xx}=L_*H_4^2-C_{yy}-z^2-2C_{xy}-2z(C_{xz}+C_{yz}).
\]

The exact verifier checks C>0 and, on **all** actual vertices and poles,

\[
v_i^TC^{-1}v_i\le R_*,\qquad q_f^TCq_f\le L_*.
\]

Equality holds at vertex4 and poles1,4. Moreover chi_C(a8,qB)=0 and

\[
\Gamma_C=R_*L_*=s_*^2
=54647270355564449175001/7621377358392133110889,
\]

where s_*=233767556251/87300500333. No reference can have smaller Gamma, by the invariant pairing v4·q1. Thus g_a8(tau)=s_*² for every tau≥0, and the optimum in (O) occurs at tau=0. An exact SDP dual is mu1=1, W4=q1q1^T, all other W_i=0 and Z=0. This proves optimality, not merely a successful numerical search.

This is a pair-specific optimum, not an asserted simultaneous optimum for all top vertices. It is also not the physical metric.

Two independent physical audits of this same actual body use a single inverse pair each. With M_standard=((5,1,2),(1,3,-1),(2,-1,4)), the census is **own446, weak000**, and top8 is the unique top norm-maximizer. With

```text
M_top9 = [[3,1,-1],[1,5,2],[-1,2,4]],
N_top9 = [[16/35,-6/35,1/5],[-6/35,11/35,-1/5],[1/5,-1/5,2/5]],
```

the census is **own435, weak000**, S={0,1,4,6}, U={1,4,9}, H={(1,8),(3,4),(4,5),(4,9),(6,7)}, and top9 is the unique top norm-maximizer. Every one of the 68 primitives is nonzero in each audit. The second audit shows that top9 cannot be discarded merely as an impossible norm-maximizer; it does not make it a joint110 candidate. The report preserves every vertex, pole, true edge, positive apex-fan tetrahedron, primitive, and metric inverse for both audits.

## 6. Computation, source recovery, and exact status

The numerical discovery step was a deterministic Powell search with three literal starts per top vertex, using the actual body at theta=(.15,.15,.15,.45,.0725). The rounded integer matrices above are explicit exact inputs, independently checked by the exact verifier. The optional locator preserves every start, nondefault tolerance, parameter, rounding operation and software version; its floating output is not a proof premise. The SDP reduction is an analytic result; no numerical claim of having globally solved an arbitrary SDP family is made.

All promoted regional results and controls were executed with **CPython 3.13.5, standard library only, assertions enabled**. The verifier was then run in a directory containing only its source. A separate recovery from the capsule below was also executed. Both fresh runs reproduced the exact report and stdout byte-for-byte. These are executions by this worker, not a claimed independent coordinator audit or proof-assistant formalization.

Pins:

```text
h5_reference_frontier.py
17154 bytes
f96878439f7225051eabe78a1a694c9b0e29b69d0a3f2db44bfec0502499cb3e

H5_REFERENCE_FRONTIER_EXACT.json
230526 bytes
18e6a5668cabdb1366187c8baa3a4b0b7c52dd97ec431145e48481ff07ea5460

h5_reference_frontier.out
345 bytes
d0717fc46a3a2a5842c72a078dedd3a31dc4240d80ac8b2435b88b049bf1cae9

reference_design_locator.py
3305 bytes
80c110e2292e4a230b03f9b7189e58c4dd9bb9ff49a6e09a7837dbf407656cf9

recover_reference_frontier.py
10912 bytes
e6011e62854e2998448f643b3459cbb23786c848285f62562d38a2801171a94f
```

The optional locator used NumPy2.3.5/SciPy1.17.0 and single-thread OpenBLAS/OMP. Its original stdout was 2636 bytes, SHA-256 86f0e97901bc6461a5047bf063c89a494880093c7c0d750fc1ed777e90423175; this floating pin is not a portability promise. The exact verifier requires neither package.

Save the following **complete** recovery source with its final LF as `recover_reference_frontier.py`. Its payload contains both complete source files, not saved proof outputs or inaccessible parent imports. The exact verifier contains the entire literal family, moment formulas, all region parameters, every reference and control input, polynomial arithmetic, Bernstein conversion and inverse reconstruction, exhaustive support recovery, true-edge mechanics, and all assertions.

```sh
python -B -S recover_reference_frontier.py exact_run
cd exact_run
python -B -S h5_reference_frontier.py > h5_reference_frontier.out
```

Expected terminal markers are `H5_REFERENCE_FRONTIER_SOURCE_RECOVERY_PASS` and `H5_REFERENCE_DESIGN_FRONTIER_ALL_EXACT_PASS`. The latter run prints `POSITIVE 523 370384` and `BARRIER 255 19002` before the physical audit summaries and exact output hash. Do not use `-O`.

Optional discovery replay:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python reference_design_locator.py > reference_design_locator.out
```

```python
"""Recover the complete exact verifier and optional numerical locator."""
from pathlib import Path
import base64,hashlib,json,sys,zlib
PAYLOAD = """
c-qZ84RhK^vVVoQSMQL-2oM-!LngIe949F|i7QSvS1VJLkOasU5|)GmPUXM9?w%Qa08VoE?&`hl8cCz>o}Qkbp6;F*efw?En<W0s
PyERBC$l7uvcON8tL<-t-)`x@H@(TnR~N57zIs1;H93EE^Y-=o$;HPH??1hL^>Om2HK_R;$IVzR&78<{!Z`9-?RuLn;z$-HUM&o!
iIZ%bx6!o&HD!aElg=m0zq-+@Q|mH3e|_`%>cL!07oRT8zox9_M~{9Oul(B0o3l>u_%@ohJN~KfSp8nF*PXSGo!-pt^ry$2W53rq
?f2c2sWa;zd%d<dYy17ScYNZ{X1&?;)arImyFS$X+K-ohmTX&2IQM~_n&ZW*%=c>0=w)rOohE@dp|*fP=0O~R5LnK@(e%hW@%-uW
wClLN_Ovr=x2>t)J#kK<mY(PI+9zJ$n;p5+S-<UD)7iA+_MDU6ku~eNQx6#UxQ=RHgKPn9PyHl=8d7MeGYx%jP+JL!nSa#Go7!`I
QnTZAwpwS+yEKl*KvMM3ZA49&CBQpT4VJ4o$!Zs}04l6qNT48ts^d7!f!ugG4I+mSS#6cX-rCJ1@X`TpOK`W5d{{W?0{WC8A1vLb
5`G2nP^?g{;qf*)fBTO2hJSIb&2$4EZX-7Y3Dm9!w^0rLdH$?6nFLXgO(t6Ehco8zwk}`dzhG7i(jY=*a(&HV*ZQD_a7~XpO|O9S
!(B)(a5H@%VZZr<3(eJQvpA{w%&i3=mnMi~nQA)L;eIcZO8p$~FTiv3?+D}2o7%VUW!4?fQ=CuBd{6ncHr0nQM>aG;O)p-T_?R|5
#mOMH{V|W5b3fC3*47(tfsy#xI*Dr6S}e&-CJ9x}B@<<?B7ZKq(g!&r$iQ^VH4Cm(<=^!(g>*eFwM){#$A*awD}yEnVG*ifVqqC}
xek9Uu5aHD3aQF!2~ok#n71p;DiHpg^K88eea*LnabpHQgc=}X;zV;_0}a)I3wy45VNShZct7q3Y898QD>pYw*1i`!9+sq0)2!A7
G`k|rRs2<fN98sMyHQs0hy_um*TBlwqL;i~0_BJf!o1e3lFofy1fgGxcH{zz9sS)J#5^{f>YJ$5;+=iqfy13LsBBSOG-4XBBTs5y
0q1hri73~<*oD>xQ71fIFEwYHYL9AgKJNE7*6aTl|4ZMi)io35Hj<+5CqId+iXX+9BnKulLKrX3z&?~Z16bG?TdIG<wpjmDup$s$
V88&YVAz|+LGZBvhXJtzZvF@y)J990Q-G(&Mu3x@l2C3Er)ia}V_RcmYInw_13z$QjhVb_V_93gW%AC#GE2ObL_O$>qGA#ZykxR2
MNf(0VeNR@BRi`gJTe<EN&J<`K7?Cj{A?`I5+~C(g|xFoyMSkSd2u#+b;C97nDy8Z>#`2BV7xKyg!NgQS#Z~9$5dj$yA!ycvJ<%L
(p{Gw!Sx7m`|K3%j^WxPoD+D~Rc}w%LFj4Ic%zhY<s{r5i+dXXObgjUN0$9)z4U=yzYI@vg0vhk;<P)?1JTgCUCRNao6c(GgZhKL
{cE6wjfLLoFn^#e%n<IrtHHiu30tuT7CK7~Si_WCCftjcQ*PVWAS4S~sIzMrDPv|^X4lxXj*7<>Tfy~#S>^*=v6vxD(mGO)ISnen
d+S(N#dtfGVt9fIHDW+F9#H{`2T%d3ks3^6b2@I=iaz~VNFTr}&vY*et-PMU)vnM7al%>}%p-8W$W(xHSj)gWa~8gb?;hh2x}kQ?
kN=EAvTv9C+;G8lOyU5YDI|5yv4-I#r<%q_x9HHB<NC-bsaM&A@+TYL3H2|}9;J@7Sm;L@g6XEUJBduE%yku&yYZN*+lDnB4?Qj{
ix@owtLs$)=ls0k0n=zuE*TDd54x1hi!d=$ov<Vt_{$F0x|Z2FGB(BvFNyJ>w~mjbqHOqu)@#F9X!kohDu}Uaoiy-@cim0{E?8s&
n(@#&k!af;v;^NZ@QQbUCc#aKF1Zm?kalir(6Nn<f$SNnk?MMr?5^bc{+`=iC^x#sbkpiI0KxzSL$f4@M|$h1fhF(<%`Zfxu(rEc
$kwx1iVZ-*SDgZATw&Y^Lrrtcsp6Kp9%Qae@+G^!SCao*?Z$ufqZ-cOwW*VWTKeAH2h+Yn_ZGZm^5(O6rHX2q)XY`rL}+3(HAqYx
5XFE2yH-^S&4!^YM)#PdAaPBObs9j%3hmu4297E@)KVH|NBb}j!Wys#r1~HQsi;1nt=y+-TFT%Q3?Cl^?B-1~Q)!l1|9O%CUxw`H
vTvd|Svq0L?e`Eoj*ZjdqPVX>z^LUFvx9X5G?rsY75HQaSi+u+OHL7Xf5a9nV>46%(QgAqVK(Mb!(NyfA;Qx_V7=k?xv?;Ds7LHl
S5%Y|Np!YIRSW;*HaY}2*w0~#R5)ZypCpW&8(}73PwbpsGQkWhsIfQfPn^=OKivHB;UAz~V8gr2YD4Sbu1|Mp1{?V1D1UP#-!LeJ
36sh?tkctxyFbp(b6NmKlvuAI(?K1<vW_57s_;}+cpHswVDhm0#}+d??G7`$ontWnbbs7Gg6DQ0pP`uU5fALI)DuALL3xLMIs}OK
$H%8RA`~A+JR+Eryhgky#7?QkPL2qyo?U_6J3T#R9VpR<uRp^hAar{8FoK8fDYSSvdc%c4+Nf2R2xT3!PG2`(j|`(Tyuy+roLFz8
cQ>ETq5VDZTsk-_gI8k0lxc$?001j}ck|`!8bCmH;uVOPU`=#t2t+xVciNenaa?YTY2*xN;4^f>m@4RCLAzAY#sX`sSCz@OU6`X(
lvA4Gy82$=(^bA`5Iy=y>KBZ_qy|3XnLd<8)Z3|J)A9;m6+FLj*##6$lB8E&K~)kv<J=B|6ud|2IjT`)oT<hv0~iBf60nt`p>#E{
!RXP_GdQ(IhY3daZT{wEyI@h!(<`kIWx2!XClF%!L8Pq|yCT&xikIL6W<EG8Q3~|jn1n@1mI%X7&qvn}{1hd|8botGG|LB2@O#&k
k!h;Ljfh$1iLboNrL)l}I2EA~8KtJDL&IjyI?Q-mKNzq|jaerm*|5qp4Z^#Ps-CT=vFzDIo9wx`8;JfO=q~9Lh1Axepc`7}+XHy3
-7&oZa1CoP-UkCFY~Kf)yU9fU!xteUMBkWwq6*lZZgdRe&OqC57*uB7m0T>8!8d<U$#NjU1DPJ`nUrG#-FUUt{%=IaqW_f8E;JI`
9m8tCRNzA-9(Du<$f5ugIF*_xQ-PYH30{#+G1DRcQXaYH#bB(U)go<03=|5CM90Ia<K7GH#L<mqz>)rMlR1+A{~+|Tl;wjd6xS4G
QgP*DDgTA?`9;l@mW@!jP~(a<6Ose@Dud=?!g;pUB4_D)s^RfEgD7|yO?i75xhj1`T?}AsMGPQ9Nl;<T76D&1MS@4KWNE|rWqU`a
P=$(ysq2v(C+bT-Tf`o(6ZexVtIi-QT&5gDFS2+czTi+F_||Z<2+B%J3EFB^9yFJi4Y!)Ez_i0a&|kJ0RnI&oOZ0!1*FO~XI+I4*
+vR#+SIYm~*q_Y;H-Py;-~bo0p^_)rTAT)u!yOi*X@gtPR}F<+?RDgOzIGB%5Eq@zgoG<qW4cSROdUQc_4c7g<Sn19;&2<q%K#nr
Xv&Hgl?o#F01-JOP6R{M8Ig!#5i$=wk>_saa@l4g8m1}Vm_^bhcEZ)dQ7S#3SMoYD=yDd%W{iUQs&yexooG;!Krfqv`CMs&HUkY!
gDiOTCo;;Le4Bl*vo{bA=sW5B(yVN?cg;&0a^OS;4Nujvua-FwA6Xqp)lI`nR9(^j3Xf471(6$|<ALl=z6HQy8dl8fbIbuEw`W3L
1<a|Qb42oi=I&%nGIG_*>qlVKU5He78V(vm4x}An3{}*VC1ZW)g82%o8R0##xQFui<<^5*W&UOYjNfC+C*QIJnh%5t8(cqHwK1VU
*N4-@ckXvAN#X<maHiJfUL{GKXqu#JBHcO*%EG)?iUon=j$W<8vH*4@-~Y+ngptajc?o5xotu{!1Q@7Bn$-}BZ^$Ur9>6P6X5^5C
vWeFP7QWA4--*{hk@CmMxBKrxzIQ^ryZXP^kP7~pz(?GUfy2i<H?+*$VIsGA(x}bn$`a(`P%O`CrDQJKvkHH5k@OX@vR+sR=vB%s
*4a4(wDq~OTsjj)y3R;$dHK`_<2+e7;S9iA9U;|{Wm9luwCn8kXG2OJD3G8h&NK#&zhIN`1@xPFcBLEVRVo5DeE<{Zd$LxdEEob5
2yS+fP&|`FLT3w@j*!zwKdmzi^gFr%Xi61OVX$I)7%Oo!_)pF2wFYQ<H4rOV*gH0=s{iPQRg_%dC^dipa0FxUjAK|h(ubZ)reUP-
t#a8mPEsRO-Fpo6?#K307?1mM%qpg@<<BBp2r_NYH86J{aK8LStkPQ3Be(OVk0N*T=Xe-C$TtximHgu<9sd(^!=CM}j+_w;n#pU@
G#Y+5|GXX<&>$Q}pc-cK2!b-ghn-1jpNhK(#1I617`@SvMs6*D&IoSMG6221oRZ`4%g+sKIGw`Pw1#2qc>Kt?{A^r(HXX-+{{=O3
IyK<`(Hj}q2C2&t*uWq2$Plm!NFojA&We+Qn=pQ0d|0ik&w9nrMRc&@7-1t#c?)<irO)bs|Dasl`8@ahG$^<0LbK~*Mo;_Rka}~_
$Ju{bMb$aidYvxo_S@Z)Bi3P^<D&y!*)-m8VTy#m0u5#*)4^YVX8Defl*1Sbea8!;`9uymaXH{qy)F|OG3;LPFnYr-<?ZEXb|r7G
J|CbVBfSarEB-K5g3?X`sN9J%jt@-klUX{+Jcu}S0TXf$Tp0WuL{%)hIY|<bpZDw5T4W>jp<EKPkH$kM#D$8}uE@oi7r0WW8^t==
mOlZQZH<R-`6Xt9Xl8@=!!N~*Io+CX|6@~tFx~~e6Bg!QV8;;@TPD8PM?5e?0HASR5P5!Ha6$wA|KYswHAcz+Rh|j3g8hbkbe+`%
Or)Q<{wk}px5xq&f?pY<7GyEZa$j~^5l%i%1gAI)rHeRJyv|4<7q~(zU5+ot7nt_n8gF-qq}!#KhlDr~F`vy~=EENB8<(XF=PylO
(9Zu42BOpJG3&J5?yxR9=^S^|BAHNaN~0Tahf}t3Gz`JjyAK<fCFr!YBjY~I`3=LDJ&BuQN}AI6Wz-Z<(-LZ0pr#6S*Di@cC+$)l
hFS}Unt6<aXzDqw9;!6<v9bz9FAJm6J77~(tW<QY2y+FmY=-;2pojfnzQ`sJ@_=R)5JDses9s8#`w%ReOb~=jQb~i&#CP1qB!^1(
UgcQnvv!N3Qm}X0W+zjff}^s5fcXXg_Sg4{C^x$S4AKe3GB<8($#-j%Xcy_|N3{pU$r9l6(MMruXRL(x-0q5e-N4P(PB>BHLCY3?
=2R>$3=J3?VsJ!kv0!h&>MFBqYa3SPh|pC$@PzsKyeXx1tEchsoaZe%KgX5$9P;uKCU%YsURDb#mb4zlI+(-ea^+PlfDK`E7L`P0
H!2#_YT!Y^Ef!;y$PHoEv_)-N5oOPHohfP<t>p`J<+V9XIzXW3dmKBsl8?M&_j@63?!r|A-H3~o7;GNKG9tof;_+TSR?}s;E6Itr
(B6TITRfw+U%XF4Zi_|;5&@VQy&|*<EzBN4xc{R40y9T&cYtKx&?as)5J}!lMDi@HI`KdNsivIg@wglWg|zrLK_Z1=?t9uyayQE}
2H*epc^Fw~xkq2Nf9O~5VUXaV9hLlwNC@lzDayFWpXO<1!M@s0Qm`$UeLm99w~*}m`f8;|%8h`qd+DkLV7&i3$Hj1XNc=QGIprFV
<}-V&E60Ae<0=CxAwZk0KKaSG{zVkAtRosE`kM$pI^o(+wY;BK{svsCJ`C;-zo7j!9d2KU4K_p955sBz_}oq#5O+UMXYDKF^BZx3
U)_kq@@+Ulu?;6EZNm|!1{<W-NwH)qOYq(m_q#bKwa)pn4MJ#e4@E%Rbvpa|bpRhmCOrd3`W`KknCdLM&t#)nrQ4Bf=8dae3G(OX
V($~&UD6$;eUTz`<*8bF!7Qp1VA|Cl4=FKEcjPGYIe1;=y$&*IC3ZVh3|Pqk4*{w$?eL)g+cR2kIXJq+qDW}T@h$RHRQ~hy)D5qq
6%=<9U%yDOB+EQ-e#>t31E8SaH!s=)A?_U5eA~KV_Kd;YF=i#q5Q3<TWzHN6Dc3I$bN37fsnZ}ZWBQV}%NvtQTpb84X|m?@%P?UX
U<CQZM2N%BTgOaoo8xoRwrt{VU7Rp!$R6;rgaMTHNf;9*rdaxAc_I##zYpFUOn#`72S|N{NO2>A11@Cnaq>0DB0o(zO5<Y@Z}7M9
l;Wume)AlqV7XpGK>4r^FdmZrD5uVCX>>7#2o2n>@+i1w)CA=!Eq!<4M1c#=40{l-SmJzrr*!lkx9y9Ho3Xp20inl3=tGc)r@hmM
@44DC0S{30zB-O=n#kYbV7K369_#Kv9&4=s+7=B=WXUYno&Kx4I*^$)*o05X+8-NMdzj`Ar^CepjRmx=YS%STVTk``?4IW9vNos{
$?~v%qzzoO85kQ{^=03YvBi`Udn7+dX9Du>ImiGZ?+9{N6%Z5iTsxTW3G)GcEs+Hibx^@!$QeT3Bjk9`<G|sFO)3ribqZYloj;0w
XfN7BD7aGv78azqz99=bvfy47bfKW?vVo&URe%*)Eb<uwEk}8iJM>FsRT6uE6O<UtAa&@YF<W7t21jK|^(n*i8DOP1JFPk}>y&)F
>3DeaEKI6k_I!*Ry@8j{x`~&?0$qz@`&}w?q7Hjk@>w6p!z^CW+Gc5PVE6u(6H;>m5ln{4HJKbRbno~(_MX2#kQz(Drrxm6{4;yQ
A+%X7wkgDQ;pD6D+(WERQ)8P&afFL$lai#4PYzfb;BkWd2!j&<4u>L!#VQjc+DN~4e=ue=dhn+lMS{%@i_Hkx0=+1?eU5h5<va7#
e!M)INm*{2_<m>yHYQH(dTz+-V}8h};kLA@AtJPrMXqD&_yv`!DWX2k-Gx1*gT}W$egWJcwJm0ys=NlFtfK&Jq7xpSOlDymC&1<&
q!3D%b#js5#yr|xC<P_6e2({Hk>p?{xlGjY!=DRi2NAmZ^jV}YXV?19E{p@nc70!sfTVKT%BVjSuFToE8|H4=+~I^#^cGrgbb2Ub
nk_J4I^7B&<qH5Wlphs@Qm#$6rn}W!?sk|s5cC>z$5<?e9*C5laUz8R*~Sq~htMUayD{9YddYD6Hx%hD2*QgoWbZ(^TSHZ+ir`@f
r$kD=#r`iHOt8!jC3F`vaY6!s0nU5^&Lxv#Lm-!JFcvehmLawWJ{eCyU?esP!rhah(L-n4AduV>beEjgr-q{-pV8qdU;A;`D5#pV
eDTLoi$C<{p*n=f;5~wc1m4Jt$Aa(y3M9i+m^?y16)@og@Wwe@uv7w8L-9xZgw}l82tf1c2~KHkTFTkuKplC4ccnJaEm?i!CpA*y
z^K$m>J+cCU<sqHIG73wegY~@wt2)yyLQ=KvUm-?U2ZgiUI1PQT*^iltr5Cu72B%X%V>E6*}|0#u;F`YMPBhb<wk(2nNEZsxKj%9
-=AV~&lcti0L6nTk-Oz+k=1er^v#51v0mah%MCtw81p!i7D*ZXFy_{=feV?M*!Fd2i2c=up>>Qqi1k|+@@ChU!&5qxO*D@Pr_()^
41*y4Rigb8QB6@b)s10vTixB2x0hg_yJ(D$#W}-8fCj(A`uUzyF7m{+&A>7@2A=lV7{*bnb5x<^uC;<vtFHr<)3)4UO@vF&hS7f^
_MHEKL<iwIZKGOhoj|E|@<Q#`R{ii5!%a<cE^%8OL81JH@WmVJBuDO7u&tv4`(#I4Uti|=YcY%g`K8L#A5geplJ9d{sinI`@T2@V
{Fc+&yYKqBM#3PCJ-<j}S5HT8*hS?$-bOzRCC*Swz;6h7uMZ??nGU`e2R1kPG2+9NG~DLRDEXxqsqHE$L8!WkeUpc75CUsEN%_gd
^QY^%I&+I#8cDEnS2nj8ZHfxAEwBINO9pjT9>cskpm+U5WhwaHt`ub{`0fHIQ$8UtoI|A&4(KNyrf+)d<to*rP;eg{!^mp_K61)2
Vq*dAF6SM+QNO*7>UvYcD&NZip9&A&Yv~pOhh&b&_h@q_xaq1$e`$#fXjLS+EMEQNZ1jmfGEm0@joG64H9>WpZZjV<;9pf`35KHe
>kl_?KfV3)RUHk!o$r@JC#bZ@f{*!1+s^<GEy7hR{p0N8N8nY~DP{fBDxZh@L5-y2{#NYBB{Hf5>*E7kj`Iz)G{d^jY)Zxj003&j
@JO;0Pm*aRmtG%;W@5EOtA6wOO`X!Aj$OY2*3|vy()}B}uYY-Uc3Efecqk6q5hHajRe&V0XPNxALo;1Co!&8(H5dNI3&8!&a*dU}
@WUZ>c6B9GX>xsbb5jS*fWAxs)lDXx*C!Jk(UVDiAV&6W^c(xF@Gm?cPl$qLb8+3d{7I4zD_o0l!Wspt*u<KIVzjCP?sGhA);<Bl
zE>N`uaR_{R=0_3mG9Tf>us&mgeS7mH*NsWR@3S?+pGpAYaaS0E^>k^_5mXAKd#PhS|8qBH*ce}5Gsu$nTdz~U9IsTpy)&*b`5$2
KpA)(2^zi>&nBwHz#1)!<F`OC`{#RN%})XOn^g$9m+c%Q!76I;3|HmEw^q>20nPQ3(icGFCpYMW94MC67Qgxtt>l+EQa4y_o8-4Z
B%(gh0iGH?-$s{h@F`lI{(t;Hw)i-JM?o8oi2M*VL@(k5G!#yGv;sqwI9tuutk#jJP9A<1_bax7E1i6XYn$Z<8}Xj5Rtr1;{Lx9}
pOEGwbd-Cq*>LM(el(iMg4CEYD8&3g3SJTnBin9cd+}JaytY{g*D+B$d-h1~bi;e?(-t19{k6lm5U-UGe&HDIIS(5h;|!0x!qa6*
R(mIIchB1zAqa5qgzfJ6T7o)L$7%5oOQ_v*e%U%7KJq7Xev6yjN|lqmOd%)}bVeL+GrM%+6CUyduGRCcW@xPFM4ZJ^GsM&E>d0#K
#45l&2$F3<8&BCO+M=t7LkNfqo`|J%w@Q}o9EO!Z77-Ac?g--G#lnoz-{-nLV00Q4UP6?O``_rS#LlKY3kCz(_=w|1XEx|Sbj}wG
dq(aI#aWb?eX<9Ad@Cjd3dQb3d4Eup*NVhAE^E*>CgA6HTIy)vv!O-5JL>3@NSx>Ia}<D?2KqicuI?hri}nE8gbNbRl9_p(EqW<o
>BBly@UlIC##8tjAB2v4-=ifbi1%rO(h^hgSQ|dRq(|X;Kqmzeei%l2c`8{yXTS(hM@q`^8=(!;G7|4qS>@msjHZ^+QApH^3{OVp
rMO#24%e&SubQ8R>jF8my90Wsz7eu&PGJ%OTVS6x;DKUSZOzs?TPp>C3f6QmnGL8GxJxxWCaQ~iXxm2&j%lim^3?}0=EV3Yz{<k_
=B+t2{gF}&36}ZbBttY;5AN9AJqzy5mq8uSM*(}(aW~L&AcFo#T(K#yd6G1-cXT5R#m(@Ny31mhZR54^8lfPPrg1B?PGB&T#0D<M
fCPeUVfr1OekZarn_$v`=_{BQE^&7eV5bjBrdbUnrZ==pvs6lDY75e3RmRB7mCjycJfE^l)x$J>`!Fe>xR?{try=--1DZm@!vtJe
Gq{>Va7=Pym^>;_sx$?Ez)A3gnJ!eVKZcHXa9p$;k=~?FlK3;Nh-`$4*+#~U^_Ub^G9gGP4a8x;j#R{(4P<W%T9l&1YC&kXk#q{U
ZJW(L!#^@x%_AoM<oRFtziCmfOKk}e^$rwz)>t>eo4_NoB1Xz+J%-+nNw#v~X6GH5k;La}lGlK7mgQ%egr5TL^GY1Q`Bq1L0G+Q7
dhIr=Z=lZl!17HC9%lK2CB6{_m8w;V#1}nGMg+<!pDzWJ43Z{Ps}DyUMU?o>O-UUp%a;_`Y<Ri*<&~k3`7Df`3@IQzp#!1_Z*`d{
5+$V}DEq_0<Btm(fKDpL|2`0y%UsZG#7D)0Sic1AE0)yRM=*q-jAyb=7zz)zH5mW?hzkPEPkIx@LAwE-b9!$hbpkID-eA#<G*3vU
N%kY|q^2=qH?1Da|Bm1fJcr(x1q|au**mUXmqd$%U46_o5CD~Hm}fC^V@L=ihz)d*PqtmrS8nt|97I&mE4uw~9s00zjt+nj7p$@G
X4t@g?JEKQ+9v}3rSAje$yM1UT=CB8??teIABo7Ila@6M*5<x9EP3X+KcD#6&4o*^Tz2WtH|ywWPz+TH`$2NghWmPsQ2+Gi<EvMt
xa-69r?(&8pIuF^KYV!wG1t|H(b=aDAM>c|x9|T0H;Wz*
"""
PINS = {'h5_reference_frontier.py': [17154, 'f96878439f7225051eabe78a1a694c9b0e29b69d0a3f2db44bfec0502499cb3e'], 'reference_design_locator.py': [3305, '80c110e2292e4a230b03f9b7189e58c4dd9bb9ff49a6e09a7837dbf407656cf9']}
files=json.loads(zlib.decompress(base64.b85decode(''.join(PAYLOAD.split()))))
assert set(files)==set(PINS)
root=Path(sys.argv[1] if len(sys.argv)>1 else 'reference_frontier_recovered')
root.mkdir(parents=True,exist_ok=True)
for name in sorted(files):
    data=files[name].encode()
    assert [len(data),hashlib.sha256(data).hexdigest()]==PINS[name]
    (root/name).write_bytes(data)
    print(name,len(data),hashlib.sha256(data).hexdigest())
print('H5_REFERENCE_FRONTIER_SOURCE_RECOVERY_PASS')
```

Convenience copies supplement, but are not required by, the inline recovery: exact verifier (`h5_reference_frontier.py`), exact report (`H5_REFERENCE_FRONTIER_EXACT.json`), recovery source (`recover_reference_frontier.py`), and optional locator (`reference_design_locator.py`).

## 7. Most useful continuation

Outside the proved barrier box, the fixed-angle SDP and its rational dual provide a systematic replacement for unconstrained reference searches, with separate programs for the possible top maxima. Inside the barrier box, further standalone-reference optimization cannot close the same alpha-product comparison: continuation should instead couple actual top-maximality and spoke inequalities with the simultaneous reference cones, improve the geometric product lower bound, or use another actual-shape mechanism. The supplied sources already require every such cone to concern the same physical inverse; that requirement is unchanged. No incomplete numerical search has been promoted to mechanical feasibility or whole-H5 exclusion.
