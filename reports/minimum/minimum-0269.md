# minimum-0269

AI research report · 2026-09-27 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# ACTUAL_H5_ROOT_HULL_GAP_AND_TWO_CELL_REPAIR_V1

## 1. Result and its precise scope

**The whole-stable-facet convex dual has a genuine, exactly realized arrow-packet gap, even after every edge LMI is imposed. Two closed foot cells repair that gap.**

The new packet is the true path

`2 -> 8 -> 1 -> 0`, with selected root `F2=(7,6,0)`.

On the five-dimensional closed H5 box specified below, **no physical SPD metric whose actual normal foot lies anywhere in closed F2 can make all three arrows weakly nonnegative**. A two-cell certificate covers the entire closed root triangle, including its edges, vertices, and the internal subdivision boundary.

Nevertheless, throughout a smaller five-dimensional closed box, **the average of two actual strictly F2-rooted SPD metrics makes all three arrows strictly positive**. The atoms, weights, actual centroids, and common-inverse computations are explicit. Consequently **no nonzero nonnegative combination of these three arrow tensors belongs to the negative dual of the whole F2 root cone**. This rules out every single whole-facet linear arrow-stress certificate for this packet, not merely the tested solver formulation, ordinary NSD stresses, a particular reference matrix, or a failed positive-margin search.

The repair retains a disjunction on the **actual same-inverse foot**, rather than replacing that foot by the foot of a convex average. This yields a root-specific implication with a quantitative margin and covers 1,736 labelled primal-tree alternatives, including **779 nonleaf complementary F2-root cases**. Of those nonleaf cases, 773 do not contain the previously certified path `4->9->7->0`.

This is **complete foot coverage for the displayed packet, not complete H5 shape or all-root obligation coverage**. At the literal W_ONLY_RESIDUAL point, complete U1 packets are already excluded by the parent's ordinary-PSD cover; that point is not reopened or re-solved here. The new result identifies an exact limitation and a working repair of the whole-root convex relaxation. No canonical registry count, global complexity bound, or attaining construction changes. The supplied working memory retains `34 <= C_min <= 622` and no whole H5/E17 exclusion.

## 2. Input authority and recovery status

I read the entire continuation journal through line 1948/EOF, including the complete literal parent and all three readable source units. The continuation attachment is 340,448 bytes, SHA-256 `0cafa59672d2268c56f6f89843e5fa2037fd6d62303810c617c2b8d8da0af813`.

The immutable parent is `minimum-0266`. Its version-2 JSON envelope was reconstructed exactly as 50,332 bytes with SHA-256 `c25bbc9175cc5da3e8b8eccfd35887b88123a91e51497e6a7b0e0490e7ab9e7e`. In this parent, the Markdown has no terminating LF; serialization with `json.dumps(envelope, ensure_ascii=False, indent=2)` reproduces the specified bytes. The three mounted source files match their literal parent fences byte-for-byte:

```
willow_root_cover.py        12008  fb8bdcb79580924c4f7e1f5988f098e7614a693c74d3e0168bcbab3fbafd436b
willow_root_region.py       11634  762f229c97f04deee611db0df260d1d10370a9551762febfdf2747a31c36cc8a
willow_root_diagnostics.py   4475  591002f52ea0fa02c01cb77da7cdbd678f9fa8606eac383699890f70e9901a77
```

The authoritative root theorem remains `ROOT_FACET_EDGE_SLEMMA_V1.md`, SHA-256 `c9db1bd5bf6233a7336f5a268c0270c5617a7a4ffe6c7f7ce09abf3b8ba498a2`. The exact H5 source remains SHA-256 `54374c6e67c89467a37f68dca0c076ee20a8581acc2791d228f0c8e8f6d9aad8`. The retained zip contains a differently presented draft result envelope; I did not use it as parent authority. Its computational source units agree with the literal parent. No mathematical or input-geometry conflict was found.

**No additional exact source is missing for the present result.** The new verifier is standalone and does not read a prior executable, saved certificate, atlas, journal, or external geometry file. No research connector, spectral theorem, covariance floor, or independently chosen polar metric is a dependency.

## 3. Actual H5 geometry and centering

Let `theta=(x,r,p,q,lambda)` and `s=1-lambda`. The seven basal vertices are `z_i=(s*b_i,0)` with

```
b0=(1/4,0)
b1=(1-3*x/4,0)
b2=(1-p,p)
b3=(q,1-q)
b4=(0,1-3*r/4)
b5=(0,1/4)
b6=(1/16,1/16).
```

The top vertices are `z7=(0,0,1)`, `z8=(lambda,0,1)`, `z9=(0,lambda,1)`. The complete outward maximal facet cycles are

```
F0=(6,5,4,3,2,1,0)
F1=(8,7,0,1)
F2=(7,6,0)
F3=(1,2,8)
F4=(9,8,2,3)
F5=(9,3,4)
F6=(4,5,7,9)
F7=(6,7,5)
F8=(7,8,9).
```

The true edge list is

```
(0,1),(0,6),(0,7),(1,2),(1,8),(2,3),(2,8),(3,4),
(3,9),(4,5),(4,9),(5,6),(5,7),(6,7),(7,8),(7,9),(8,9).
```

These are the supplied geometry and labels, not a graph-only replacement.

The actual uniform-volume moments are

```
a  = (31-24*x*p-24*r*q)/64
bx = 509/3072-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
by = 509/3072-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
D  = lambda+2*a*s*s
Kx = 3*s**3*bx/2+s*s*lambda*(1-3*x*p/4)/4+lambda**2/4
Ky = 3*s**3*by/2+s*s*lambda*(1-3*r*q/4)/4+lambda**2/4
Kz = a*s*s/2+lambda/2+lambda**2/4
g  = K/D.
```

Here `D=6 Vol(P)` and `K=6 integral_P z dz`. The verifier independently integrates the oriented maximal-facet boundary and proves these identities symbolically. Write `v_i=z_i-g`,

\[
T_{ij}=\operatorname{sym}(v_i(z_j-z_i)^T),\qquad
D_{ij}(M)=\operatorname{tr}(T_{ij}M).
\]

Every pole is normalized using this same actual `g`. In particular

\[
n_2=(-1,-3,-s/4),\quad h_2=-s/4,\quad
q_2=n_2/(h_2-n_2\cdot g).
\]

### The broad closed parameter box

The physical packet exclusion holds on

```
x      in [1/10,1/5]
r      in [1/100,9/10]
p      in [1/100,3/25]
q      in [1/100,3/5]
lambda in [29/200,31/200].                         (B)
```

All endpoints are genuine 10/17/9 bodies. This varies all five parameters and is not contained in the parent's narrow `r≈.9,q≈.6` root-packet box.

Exact positivity checks cover all nonincident support slacks, all centered support heights, a fixed-sign component of each normal, strict planar support of every listed polygon edge against every other vertex of that polygon, and independent incident normals at every vertex. Every listed polygon is therefore an actual maximal facet with the displayed true boundary edges. Each such edge has exactly two listed incident facets; connectedness of the convex hull's facet-adjacency graph then rules out an omitted facet. At the reference point, all supporting vertex triples are additionally enumerated directly. The regional geometry stage has **159 scalar certificates and 2,825 positive Bernstein coefficients**. No auxiliary integration diagonal is treated as a mechanical edge.

## 4. Root-location subdivision: theorem and exact certificate

### Polygonal foot domains

The supplied whole-root theorem applies to the true facet polygon. Its root-fibre proof also gives the following useful version for an arbitrary full-dimensional convex polygon `K` contained in that facet plane. If `q.p=1` on `K`, and

\[
q^TUq\le0,\qquad
\lambda_e\operatorname{sym}(a_e b_e^T)-U\succeq0,
\quad\lambda_e\ge0
\]

for every boundary edge `[a_e,b_e]` of **the foot domain K**, then `tr(UM)<=0` for every SPD `M` whose actual foot is in closed `K`. These domain edges are not asserted to be edges of the polyhedron, and they do not supply mechanical arrows. The stress below uses only true arrows. The original root theorem and its closed-foot argument are supplied explicitly.

For completeness, if `f=M^-1 q/(q^T M^-1 q)`, put `alpha=f^TMf`. Then

\[
M=\alpha qq^T+L,\qquad L\succeq0,\qquad Lf=0.
\]

This is Cauchy–Schwarz in the M-inner product. In a spectral decomposition of `L`, each vector `w` satisfies `w.f=0`. Since `f` lies in `K`, the values `w.a` at its vertices straddle zero. Some boundary edge has `(w.a_e)(w.b_e)<=0`. Its LMI gives `w^TUw<=0`. Adding these contractions and the normal term proves the assertion, including boundary feet. For `U=A+delta*C`, any nonzero PSD `C` and `delta>0` give

\[
\operatorname{tr}(AM)\le-\delta\operatorname{tr}(CM)<0.
\]

### Actual moving root frame and two-cell cover

Define the **origin-fixing linear frame**

\[
H=[\,z_6-z_7,\ z_0-z_7,\ z_7-g\,],\qquad X_i=H^{-1}v_i.
\]

Then `X7=(0,0,1)`, `X6=(1,0,1)`, `X0=(0,1,1)`, and the root pole is `e3`. A physical foot has canonical coordinates `(a,b,1)` with `a,b>=0`, `a+b<=1`. Its barycentric coordinates on `(7,6,0)` are `(1-a-b,a,b)`.

Use these two closed foot domains, in cyclic order:

```
K_in : (0,0,1), (1/2,0,1), (0,1/2,1)
K_out: (1/2,0,1), (1,0,1), (0,1,1), (0,1/2,1).
```

They cover the full closed triangle, with shared boundary `a+b=1/2`. Put

\[
C_\theta=(z_6-z_7)(z_6-z_7)^T+(z_0-z_7)(z_0-z_7)^T
       =H\operatorname{diag}(1,1,0)H^T.
\]

This is a nonzero rank-two PSD tangent reference, not a freely assigned covariance. It annihilates `q2` and is nonzero throughout B.

The complete fixed rational certificate is

| Foot domain | Weights on `(28,81,10)` | Margin `delta` | Cyclic domain-edge multipliers |
|---|---|---|---|
| `K_in` | `(17,40,10)` | `1/10` | `(70,118,67)` |
| `K_out` | `(0,9,4)` | `1/4` | `(22,11,37,86)` |

Thus throughout B,

\[
\begin{array}{ll}
f\in K_{\rm in}:&17D_{28}+40D_{81}+10D_{10}\le-\operatorname{tr}(C_\theta M)/10,\\
f\in K_{\rm out}:&9D_{81}+4D_{10}\le-\operatorname{tr}(C_\theta M)/4.
\end{array}
\]

In particular the complete root-conditioned implication is

\[
\boxed{f\in F_2,\ D_{81},D_{10}\ge0
\ \Longrightarrow\ a+b<\tfrac12,
\quad D_{28}\le-\operatorname{tr}(C_\theta M)/170<0.}
\]

This is the claimed three-arrow exclusion. Minimality of the three-arrow packet is **not** asserted.

The branch variable is itself an actual common-inverse quantity. With `Mhat=H^T M H`, the sign of `a+b-1/2` is the sign of

\[
2(\operatorname{adj}\widehat M)_{13}
+2(\operatorname{adj}\widehat M)_{23}
-(\operatorname{adj}\widehat M)_{33}.
\]

The denominator `(adj Mhat)33` is positive. The repair therefore retains a quadratic same-inverse foot distinction that a single convex hull discards.

### Exact continuum acceptance

Let `R_i=D*z_i-K`, and for each weight row let

\[
U=\sum w_{ij}\operatorname{sym}(R_i(z_j-z_i)^T),\qquad A=U/D.
\]

For a canonical cell vertex `(a,b,1)`, its denominator-cleared actual foot is

`Rfoot=R7+a*(R6-R7)+b*(R0-R7)`.

The checker proves

\[
-n_2^TU n_2>0,
\qquad
\lambda_e\operatorname{sym}(R_{{\rm foot},i}R_{{\rm foot},j}^T)
-DU-\delta D^2C_\theta\succ0.
\]

These are polynomial tests with the actual moving centroid cleared by a positive denominator; no foot, pole, or mass is frozen.

Every edge matrix has multidegree `(4,4,4,4,6)` and 4,375 tensor Bernstein coefficients. Only the first edge of `K_in` requires a parameter subdivision, at `r=91/200`, into the two closed children. All other edge matrices use the entire B. Totals are **8 matrix/shape applications, 35,000 PD coefficient matrices, and 245,000 strictly positive principal-minor checks**. All seven principal minors are checked, not just numerical eigenvalues.

The two normal polynomials pass on the full B without subdivision:

```
K_in : degrees (3,2,3,2,4), 720 coefficients,
       minimum 438222406168526923/128000000000000000.
K_out: degrees (3,2,2,2,4), 540 coefficients,
       minimum 189339750752919/320000000000000.
```

## 5. Actual strict-root atoms defeat the whole-facet convex dual

At the literal point

```
theta0=(1/10,9/10,3/25,3/5,3/20),
Vol=881291/9600000,
g=(7368835529/28201312000,
   3427883561/28201312000,
   50317/153268),
```

use the actual frame H above. For a planar foot `u`, direction `d`, and `epsilon>0`, define

\[
G=dd^T+\epsilon I_2,\qquad
R(u,d,\epsilon)=
\begin{pmatrix}G&-Gu\\-u^TG&\epsilon+u^TGu\end{pmatrix}.
\]

Its Schur complement is `epsilon`, so it is SPD and its exact top-plane foot is `(u,1)`.

Set

```
epsilon=1/10000
u0=(1/200,1/200), d0=(7/8,1)
u1=(99/100,1/200), d1=(1,3/20)
R0=R(u0,d0,epsilon)
R1=(9/100)*R(u1,d1,epsilon)
Rbar=(R0+R1)/2
Mj=H^-T Rj H^-1.
```

Both atom feet are strictly inside F2. In raw coordinates they are `(17/12800,17/64000,99/100)` and `(1717/32000,1683/32000,1/200)` respectively. The multiplier `9/100` is part of the exact second metric, not a change of its foot.

For an additional literal check,

\[
R_0+R_1=
\begin{pmatrix}
427867/500000&1777/2000&-19476007/200000000\\
1777/2000&501067/500000&-2275067/100000000\\
-19476007/200000000&-2275067/100000000&708387339/8000000000
\end{pmatrix}.
\]

The mean's canonical foot is

\[
\left(\frac{2579129123323}{2270929545200},
-\frac{558780327131}{567732386300},1\right),
\]

outside the root triangle. Its three exact arrow values, ordered `(28,81,10)`, are

```
381736201019767945608525423/197304031469054539328000000000
113088347642891158979904061/29682907389149797952000000000
130617810266773310407668717/46424477992718715136000000000.
```

All are strictly positive. Suppose a nonzero nonnegative weighted sum A of these three tensors belonged to the whole-root negative dual. Since both atoms are strictly root-stable, `tr(A M0)<=0` and `tr(A M1)<=0`, hence `tr(A Mbar)<=0`. The displayed strict arrows instead give `tr(A Mbar)>0`. This proves the impossibility of **every** such whole-facet stress, including any proposed positive PSD-reference shift. It also rules out every nonzero nonnegative NSD primal stress on this packet.

The full-root convex-hull theorem already warns that a hull foot can lie outside the facet. The new control strengthens that warning to an **actual strict true-arrow packet whose physical closed-root intersection is empty but whose whole-root convex relaxation has a strict feasible point**. The general hull theorem itself is not contradicted.

### Full physical censuses at theta0

Each row below is one physical metric with its own exact inverse on the same actual-centered body; the mean also has a genuine physical census, but F2 is not its stable root.

| Metric | Strict S facets | Strict U vertices | Strict H edges | `(S,U,H)` |
|---|---|---|---|---|
| `M0` | `0,1,2,6` | `0,3` | `07,23,45,67` | `(4,2,4)` |
| `M1` | `0,2,4,6,7` | `1,4` | `06,23,57,67,79` | `(5,2,5)` |
| `Mbar` | `0,6` | `0,3,4` | `34,56,89` | `(2,3,3)` |

All 68 true-edge primitives are nonzero in each metric, and all three bodies have zero physical weak points. The verifier returns every primitive, metric, inverse, actual foot, and census. These are nonattaining physical controls, not independent primal/polar feasibility witnesses for S1/U1.

### A five-dimensional region of strict hull false positives

Keep the same two canonical atoms but transport them by the **moving actual H(theta)**. On the closed box

```
x      in [1/10,101/1000]
r      in [899/1000,9/10]
p      in [119/1000,3/25]
q      in [599/1000,3/5]
lambda in [149/1000,151/1000],                     (H)
```

which lies inside B, all three mean-metric arrow values are **strictly greater than `1/5000`**. Every atom remains strictly F2-rooted because its fixed canonical foot remains interior. Thus the single-whole-root-stress obstruction is regional, not merely a point phenomenon. Other equilibrium counts are only asserted at theta0, not throughout H.

The exact regional proof avoids a symbolic matrix inverse. Put `HF=D*h2-n2.K>0`, and for each raw vertex z define

```
Bz = z_x+3*z_y+s*(z_z-1)/4
V  = (16*(HF*z_y-Ky*Bz),
      4*(HF*(z_x-z_y)-(Kx-Ky)*Bz),
      s*(HF-D*Bz)).
```

The verifier checks the polynomial identity `H*V/(s*HF)=z-g` after clearing D. Hence `X=V/(s*HF)`. It certifies, for each selected arrow,

`Vi^T Rbar (Vj-Vi) - (s*HF)^2/5000 > 0`.

All three polynomials have multidegree `(4,4,4,4,8)`. Their **16,875 Bernstein coefficients are strictly positive without subdivision**. Thus all parameter boundaries in H are covered exactly.

## 6. Mechanical alternatives covered, and those not covered

The exact graph enumeration gives 4,879 unrooted spanning trees and 48,790 labelled primal rooted trees. Complementary dual connectivity is checked directly from the actual facet-edge map.

Precisely **1,736** primal rooted trees contain `2->8->1->0`. Their root counts are

```
0:527, 3:93, 4:155, 5:248, 6:341, 7:248, 9:124.
```

The complementary dual root F2 has degree

```
1:957, 2:713, 3:66.
```

The new packet therefore includes 779 nonleaf cases. Its overlap with the parent's `4->9->7->0` packet is 36 trees, only 6 of them nonleaf. The resulting **773 nonleaf alternatives not containing that old packet** are a comparison with those literal masks, not a canonical registry increment or an exclusion newly independent of every historical method.

For root F2, **47,054 labelled primal trees do not contain this packet** and are not covered by this new theorem over B. They are unresolved alternatives of this certificate, not physical survivors. Other root choices are not covered by it. At theta0 their full U1 feasibility is already excluded by the parent's independent cover.

Reflection `(x,r,p,q,lambda)->(r,x,q,p,lambda)`, with `0<->5,1<->4,2<->3,8<->9`, transports the entire result to root F7 and path `3->9->4->5`. It gives a reflected domain, not automatic extra coverage on B.

## 7. Quantitative localization of a conditioned root hull

There is also a general analytic continuation tool. Let K be any compact convex polygon in `q.p=1`, and let `C_K` be its closed root-metric convex cone. For any SPD `M in C_K`, any `c` in that plane, and `R=max_{a in K}||a-c||`, its **actual** foot f obeys

\[
\boxed{(f-c)^TM(f-c)\le R^2\operatorname{tr}M,
\qquad
\|f-c\|\le R\sqrt{\operatorname{tr}M/\lambda_{\min}(M)}.}
\]

This is not claimed sharp. It quantifies when a small foot cell has a small hull-foot error.

Indeed, the supplied rank-one root-hull decomposition writes

\[
M=\alpha qq^T+\sum_j w_jw_j^T,
\quad\alpha\ge0,\quad w_j\cdot p_j=0\text{ for some }p_j\in K.
\]

Write `beta=f^TMf`. Since `q.f=q.c=1` and `Mf=beta*q`,

\[
\begin{aligned}
(f-c)^TM(f-c)
&=c^TMc-\beta\\
&\le\sum_j(w_j\cdot c)^2\\
&=\sum_j[w_j\cdot(c-p_j)]^2\\
&\le R^2\sum_j\|w_j\|^2
\le R^2\operatorname{tr}M.
\end{aligned}
\]

Here `beta=alpha+sum_j(w_j.f)^2>=alpha`. This uses the exact hull decomposition, not an assumption that its summands share one physical inverse.

Consequently, fix a closed arrow packet and a normalized metric domain `tr M=1, M>=epsilon*I`, `epsilon>0`. If no metric in that domain satisfies the packet with its actual foot in F, the feasible packet metrics form a compact set whose foot-image has positive distance d from F, unless that set is already empty. Any finite subdivision of F into cells of diameter `<d*sqrt(epsilon)` has **no root-hull/packet intersection in any cell**. Otherwise the displayed inequality, with `c in K subset F`, contradicts d.

This is a qualitative completeness statement for foot subdivision on a fixed uniformly positive metric domain. It supplies neither a computed d nor a universal cell bound, and does not assert termination of an unconditioned positive-margin search in the presence of singular limits. It also does not promote the present packet into a full S1/U1 cover. Its useful implication is that actual metric floors and progressively refined actual foot cells can remove convex-root false positives in a controlled way.

## 8. What was tried, useful failures, and next condition

The productive change was to stop searching for one aggregate whole-F2 stress once a strict root-hull arrow witness was found. A path scan first located candidates requiring foot subdivision; the decisive literal packet was then reduced to the two cells above. The original whole-facet numerical margin was negative, but that numerical event was never an exclusion or a physical witness. The exact two-atom construction now proves the limitation.

An initial finite-atom grid failed to find a strict witness. A finer deterministic grid found a rational three-atom witness; the simpler two-atom witness above was then checked independently and extended to H. The useful nonwinning three-atom construction is preserved as follows. With `e=1/1000000`, use **trace-normalized** `R(u,d,e)` atoms:

```
u=(e,e),       d=(22/25,1),  weight=77087/100000
u=(e,e),       d=(89/100,1), weight=26993/200000
u=(1-2e,e),    d=(1,3/20),  weight=18833/200000.
```

The weights sum to one. The locator reconstructs and exactly verifies all three positive arrow contractions; its report retains the entire matrix and foot. This is a root-hull control, not another physical-root survivor.

An unsplit Bernstein matrix test on a larger box failed at a coefficient. I did not interpret that as a body counterexample. The positive-endpoint box B and its single specified r subdivision pass all exact checks. Geometry checks initially involving the squared variable normal were replaced by fixed-sign normal-component checks, which prove the same planar orientation without an unnecessary square-induced coefficient loss.

The two-arrow subsystem `(81,10)` has not been classified over all physical root metrics; the displayed implication and three-arrow theorem do not require such a classification. No minimality claim is made. No complete all-obligation cover over B was obtained. Extra nonroot polar arrows, full primal trees, actual covariance restrictions, or further mixed identities can strengthen the whole-facet relaxation; the counterexample does not show they fail.

**Most useful continuation:** add the two-cell implication as an actual cofactor-foot branch, and cover the other genuine escape alternatives while retaining that same branch variable. The complete region H proves that rerunning arbitrary single whole-F2 nonnegative stress searches on this packet cannot succeed. With a justified uniform metric floor, the localization inequality gives a principled way to refine cells until these hull false positives disappear. Keep the remaining primal-root alternatives and nonroot polar conditions explicit; neither convex feasibility nor the successful two-cell packet proves S1/U1 existence or whole-shape exclusion.

## 9. Complete deterministic recovery capsule

The two complete source units below are all the computational inputs. Save each using the displayed name and its final LF. The exact verifier requires **CPython 3.13.5 and SymPy 1.14.0**. It uses no numerical optimizer or randomness. The optional discovery replay additionally uses **NumPy 2.3.5 and SciPy 1.17.0**, `method='highs'`, and `OPENBLAS_NUM_THREADS=1`. Its tolerances, 60-iteration ceiling, direction grid, atom grid, extraction threshold, and rational rounding rule are explicit in source. Its numerical cell results are not acceptance certificates.

Run with assertions enabled:

```sh
python -B willow_root_disjunction.py
OPENBLAS_NUM_THREADS=1 python -B willow_disjunction_locator.py
```

Expected terminal markers:

```
ACTUAL_H5_ROOT_HULL_GAP_AND_TWO_CELL_REPAIR_V1_PASS
WILLOW_ROOT_DISJUNCTION_DISCOVERY_REPLAY_COMPLETE
```

Observed exact pins:

| File | Bytes | SHA-256 |
|---|---:|---|
| `willow_root_disjunction.py` | 16273 | `7553f47dbbde60223c40525c332d48a6b5841134dd851e4a7ab63c1eaaaad2d3` |
| `willow_root_disjunction_report.json` | 129691 | `708ef7d92f45a37e9d946841a85c0960eb0fae10b6b16fd71887664e42fbd613` |
| `willow_disjunction_locator.py` | 4649 | `51b85de5495e00296dc46330adeed39d5ef9d741be62b1120ce1c375a9d683a3` |
| `willow_disjunction_locator_report.json` | 4223 | `d3cb5c53cd4bd0add068b3646a6c114053e7655610059a96bfcb66f107f1f0de` |

**Normal execution and a fresh-directory source-only execution of both programs were observed. Both regenerated reports were byte-identical; all four stderr files were empty.** The source-only directory initially contained only these two Python files. This is author execution of exact rational checks and the accompanying analytic proof, not coordinator replay or proof-assistant formalization. A platform producing different LP weights must recheck its rational atoms and record its own discovery-report pins; the exact exclusion proof does not depend on the LP output.

The main report contains every physical metric and inverse, all 204 primitive values, actual feet, all cell data, every scalar and matrix coefficient minimum, coefficient-array digests, and exhaustive overlap counts. The literal geometry and polynomial construction regenerate every coefficient; no coefficient array or certificate is a hash-only dependency.

### willow_root_disjunction.py

```python
#!/usr/bin/env python3
"""ACTUAL_H5_ROOT_HULL_GAP_AND_TWO_CELL_REPAIR_V1.
Run: python -B willow_root_disjunction.py
Exact rational acceptance only. Python 3.13.5; SymPy 1.14.0.
No external input, optimizer, saved certificate, or parent program is read.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb, lcm
from pathlib import Path
import hashlib, json
import sympy as S
R=S.Rational
PARENT='minimum-0266'
PARENT_SHA='c25bbc9175cc5da3e8b8eccfd35887b88123a91e51497e6a7b0e0490e7ab9e7e'
OBJECT='ACTUAL_H5_ROOT_HULL_GAP_AND_TWO_CELL_REPAIR_V1'
THETA=tuple(map(Q,('1/10','9/10','3/25','3/5','3/20')))
BOX=tuple(tuple(map(Q,p)) for p in (('1/10','1/5'),('1/100','9/10'),('1/100','3/25'),('1/100','3/5'),('29/200','31/200')))
HULL_BOX=tuple(tuple(map(Q,p)) for p in (('1/10','101/1000'),('899/1000','9/10'),('119/1000','3/25'),('599/1000','3/5'),('149/1000','151/1000')))
FACES=((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
       (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
ARROWS=((2,8),(8,1),(1,0))
CELLS=(
 (((Q(0),Q(0)),(Q(1,2),Q(0)),(Q(0),Q(1,2))), (17,40,10),Q(1,10),(70,118,67)),
 (((Q(1,2),Q(0)),(Q(1),Q(0)),(Q(0),Q(1)),(Q(0),Q(1,2))), (0,9,4),Q(1,4),(22,11,37,86)))
I=tuple(tuple(Q(i==j) for j in range(3)) for i in range(3))
ZERO=tuple(tuple(Q(0) for j in range(3)) for i in range(3))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(t,a):return tuple(t*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def transpose(A):return tuple(zip(*A))
def mv(A,v):return tuple(dot(row,v) for row in A)
def mm(A,B):return tuple(tuple(dot(row,col) for col in transpose(B)) for row in A)
def tr(A):return sum(A[i][i] for i in range(3))
def det(A):return dot(A[0],cross(A[1],A[2]))
def inv(A):
 d=det(A);assert d
 return tuple(tuple(x/d for x in row) for row in transpose((cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))))
def plus(A,B):return tuple(add(a,b) for a,b in zip(A,B))
def times(t,A):return tuple(scale(t,row) for row in A)
def sym(a,b):return tuple(tuple((a[i]*b[j]+b[i]*a[j])/2 for j in range(3)) for i in range(3))
def contract(A,B):return sum(A[i][j]*B[i][j] for i in range(3) for j in range(3))
def quad(v,A):return dot(v,mv(A,v))
def minors(A):
 return tuple(A[i][i] for i in range(3))+tuple(A[i][i]*A[j][j]-A[i][j]**2 for i,j in combinations(range(3),2))+(det(A),)
def serial(x):
 if isinstance(x,(Q,S.Rational)):return str(x)
 if isinstance(x,S.MatrixBase):return serial(x.tolist())
 if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [serial(t) for t in x]
 return x

def formulas(theta):
 x,r,p,q,la=theta;s=1-la
 basal=((R(1,4),0),(1-3*x/4,0),(1-p,p),(q,1-q),(0,1-3*r/4),(0,R(1,4)),(R(1,16),R(1,16)))
 z=tuple(S.Matrix((s*a,s*b,0)) for a,b in basal)+(S.Matrix((0,0,1)),S.Matrix((la,0,1)),S.Matrix((0,la,1)))
 area=(31-24*x*p-24*r*q)/64
 bx=R(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
 by=R(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
 D=la+2*area*s*s
 K=S.Matrix((3*s**3*bx/2+s*s*la*(1-3*x*p/4)/4+la*la/4,
             3*s**3*by/2+s*s*la*(1-3*r*q/4)/4+la*la/4,
             area*s*s/2+la/2+la*la/4))
 planar=(((0,-1),0,0,1),((p,p-3*x/4),s*p*(1-3*x/4),la*p,3),((1,1),s,la,4),
         ((q-3*r/4,q),s*q*(1-3*r/4),la*q,5),((-1,0),0,0,6),((-3,-1),-s/4,0,7),((-1,-3),-s/4,0,2))
 ns=[None]*9;hs=[None]*9;ns[0]=S.Matrix((0,0,-1));hs[0]=S.S(0);ns[8]=S.Matrix((0,0,1));hs[8]=S.S(1)
 for n,h,t,f in planar:ns[f]=S.Matrix((*n,h-t));hs[f]=h
 return z,D,K,ns,hs

def symbolic():
 var=S.symbols('x r p q la');z,D,K,ns,hs=formulas(var)
 dd=S.S(0);kk=S.zeros(3,1)
 for face in FACES:
  a=z[face[0]]
  for j in range(1,len(face)-1):
   b,c=z[face[j]],z[face[j+1]];d=a.dot(b.cross(c));dd+=d;kk+=d*(a+b+c)/4
 assert S.expand(dd-D)==0 and all(S.expand(t)==0 for t in kk-K)
 for f,face in enumerate(FACES):
  for i in face:assert S.expand(hs[f]-ns[f].dot(z[i]))==0
 return var,z,D,K,ns,hs

def geometry(theta=THETA):
 z,D,K,ns,hs=formulas(tuple(R(t) for t in theta))
 z=tuple(tuple(map(Q,a)) for a in z);D=Q(D);K=tuple(map(Q,K));ns=tuple(tuple(map(Q,a)) for a in ns);hs=tuple(map(Q,hs))
 g=scale(1/D,K);v=tuple(sub(a,g) for a in z)
 assert D>0
 for f,face in enumerate(FACES):
  for i in range(10):
   slack=hs[f]-dot(ns[f],z[i]);assert slack==0 if i in face else slack>0
 poles=tuple(scale(1/(h-dot(n,g)),n) for n,h in zip(ns,hs))
 assert all(h-dot(n,g)>0 for n,h in zip(ns,hs))
 hull=set()
 for i,j,k in combinations(range(10),3):
  n=cross(sub(z[j],z[i]),sub(z[k],z[i]));values=[dot(n,sub(a,z[i])) for a in z]
  if any(n) and (min(values)>=0 or max(values)<=0):hull.add(tuple(l for l,t in enumerate(values) if not t))
 assert hull=={tuple(sorted(f)) for f in FACES}
 ef={}
 for f,face in enumerate(FACES):
  for i,j in zip(face,face[1:]+face[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append(f)
 assert len(ef)==17 and all(len(a)==2 for a in ef.values())
 return dict(z=z,v=v,D=D,K=K,g=g,q=poles,edges=tuple(sorted(ef)),ef=ef)

def bernstein(expressions,var,box):
 """All tensor coefficients as integers over a common POSITIVE denominator."""
 pol=[S.Poly(S.expand(e),*var,domain=S.QQ) for e in expressions]
 deg=tuple(max(0,max(int(P.degree(v)) if P else 0 for P in pol)) for v in var)
 den=1
 for P in pol:
  for c in P.coeffs():den=lcm(den,int(c.q))
 data={powers+(i,):int(c*den) for i,P in enumerate(pol) for powers,c in P.terms() if c};factor=den
 for axis,(n,(lo,hi)) in enumerate(zip(deg,box)):
  lo,hi=Q(lo),Q(hi);width=hi-lo
  mat=[[sum((Q(comb(j,k)*comb(i,k),comb(n,k))*lo**(j-k)*width**k for k in range(min(i,j)+1)),Q(0)) for j in range(n+1)] for i in range(n+1)]
  den=1
  for row in mat:
   for c in row:den=lcm(den,c.denominator)
  mat=[[int(c*den) for c in row] for row in mat];factor*=den;out={}
  for key,c in data.items():
   j=key[axis]
   for i in range(n+1):
    d=mat[i][j]
    if d:
     k=key[:axis]+(i,)+key[axis+1:];out[k]=out.get(k,0)+c*d
  data=out
 return deg,data,factor

def scalar_check(name,e,var,box):
 deg,a,den=bernstein([e],var,box);values=[a.get(t+(0,),0) for t in product(*(range(d+1) for d in deg))]
 assert min(values)>0,(name,'nonpositive scalar coefficient',deg,min(values))
 return {'name':name,'box':box,'degrees':deg,'coefficients':len(values),'minimum':Q(min(values),den)}

def matrix_check(name,P,var,box):
 deg,a,den=bernstein(list(P),var,box);count=0;lowest=None;digest=hashlib.sha256()
 for t in product(*(range(d+1) for d in deg)):
  A=tuple(tuple(a.get(t+(3*i+j,),0) for j in range(3)) for i in range(3));assert A==transpose(A)
  m=minors(A);assert min(m)>0,(name,'nonpositive matrix coefficient',t)
  digest.update((','.join(map(str,(*t,*[u for row in A for u in row])))+'\n').encode())
  normalized=tuple(Q(u,den**(1 if k<3 else 2 if k<6 else 3)) for k,u in enumerate(m))
  lowest=normalized if lowest is None else tuple(min(x,y) for x,y in zip(lowest,normalized));count+=1
 return {'name':name,'box':box,'degrees':deg,'matrices':count,'positive_principal_minors':7*count,'minimum_principal_minors':lowest,'integer_coefficient_sha256':digest.hexdigest(),'coefficient_denominator':den}

def true_geometry_checks(var,z,D,K,ns,hs):
 checks=[scalar_check('six_volume',D,var,BOX)]
 for f,face in enumerate(FACES):
  checks.append(scalar_check('centred_height_%d'%f,D*hs[f]-ns[f].dot(K),var,BOX))
  for i in range(10):
   if i not in face:checks.append(scalar_check('support_%d_%d'%(f,i),hs[f]-ns[f].dot(z[i]),var,BOX))
  # A fixed-sign nonzero normal component avoids squaring variable normals.
  center=dict(zip(var,[R(a+b)/2 for a,b in BOX]));axis=None
  for k in range(3):
   sign=S.sign(ns[f][k].subs(center))
   if not sign:continue
   try:c=scalar_check('normal_component_%d_%d'%(f,k),sign*ns[f][k],var,BOX)
   except AssertionError:continue
   checks.append(c);axis=k;break
  assert axis is not None
  for i,j in zip(face,face[1:]+face[:1]):
   for k in face:
    if k not in (i,j):checks.append(scalar_check('facet_edge_%d_%d_%d_%d'%(f,i,j,k),sign*((z[j]-z[i]).cross(z[k]-z[i]))[axis],var,BOX))
 # All three normals at one vertex are uniformly independent (try in fixed order).
 center=dict(zip(var,[R(a+b)/2 for a,b in BOX]))
 for i in range(10):
  success=False
  for fs in combinations([f for f,face in enumerate(FACES) if i in face],3):
   e=S.Matrix.hstack(*(ns[f] for f in fs)).det();sign=S.sign(e.subs(center))
   if not sign:continue
   try:c=scalar_check('vertex_rank_%d_%s'%(i,str(fs)),sign*e,var,BOX)
   except AssertionError:continue
   checks.append(c);success=True;break
  assert success,('unverified vertex rank',i)
 return checks

def root_metric(u,d,epsilon=Q(1,10000)):
 G=tuple(tuple(d[i]*d[j]+epsilon*(i==j) for j in range(2)) for i in range(2))
 b=tuple(-dot(row,u) for row in G)
 return (G[0]+(b[0],),G[1]+(b[1],),(b[0],b[1],epsilon-dot(u,b)))

def atoms():
 A=root_metric((Q(1,200),Q(1,200)),(Q(7,8),Q(1)))
 B=times(Q(9,100),root_metric((Q(99,100),Q(1,200)),(Q(1),Q(3,20))))
 for M,u in ((A,(Q(1,200),Q(1,200))),(B,(Q(99,100),Q(1,200)))):
  assert min(minors(M))>0
  p=mv(inv(M),(Q(0),Q(0),Q(1)));p=scale(1/p[2],p)
  assert p==(*u,Q(1)) and min(u)>0 and sum(u)<1
 return A,B,times(Q(1,2),plus(A,B))

def census(B,M):
 assert min(minors(M))>0;N=inv(M);assert mm(M,N)==I
 dp={(i,j):dot(B['v'][i],mv(M,sub(B['v'][j],B['v'][i]))) for e in B['edges'] for i,j in (e,e[::-1])}
 dual=tuple(sorted(tuple(sorted(fs)) for fs in B['ef'].values()))
 dq={(i,j):dot(B['q'][i],mv(N,sub(B['q'][j],B['q'][i]))) for e in dual for i,j in (e,e[::-1])}
 assert len(dp)==len(dq)==34 and all(dp.values()) and all(dq.values())
 U=[i for i in range(10) if all(t<0 for (a,b),t in dp.items() if a==i)]
 stable=[i for i in range(9) if all(t<0 for (a,b),t in dq.items() if a==i)]
 saddles=[e for e in B['edges'] if max(dp[e],dp[e[::-1]],dq[tuple(B['ef'][e])],dq[tuple(B['ef'][e][::-1])])<0]
 assert len(stable)+len(U)-len(saddles)==2
 pole=B['q'][2];foot=scale(1/quad(pole,N),mv(N,pole))
 return {'M':M,'N':N,'S':stable,'U':U,'H':saddles,'zero_primitives':0,'physical_weak_points':0,
         'root2_foot_centred':foot,'root2_foot_raw':add(B['g'],foot),'packet_values':[dp[e] for e in ARROWS],
         'all_primal_rows':[(i,j,d) for (i,j),d in dp.items()],'all_polar_rows':[(i,j,d) for (i,j),d in dq.items()]}

def tree_overlap(edges):
 arrows=tuple(e for ij in edges for e in (ij,ij[::-1]));packet=sum(1<<arrows.index(e) for e in ARROWS)
 old=sum(1<<arrows.index(e) for e in ((4,9),(9,7),(7,0)))
 counts={};degrees={};total=0;nt=0;overlap=0;nonleaf_overlap=0
 ef={}
 for f,face in enumerate(FACES):
  for i,j in zip(face,face[1:]+face[:1]):ef.setdefault(tuple(sorted((i,j))),[]).append(f)
 assert set(ef)==set(edges) and all(len(fs)==2 for fs in ef.values())
 for E in combinations(range(17),9):
  adj=[[] for _ in range(10)];parent=list(range(10));good=True
  def find(i):
   while parent[i]!=i:i=parent[i]
   return i
  for k in E:
   i,j=edges[k];a,b=find(i),find(j)
   if a==b:good=False;break
   parent[a]=b;adj[i].append((j,2*k));adj[j].append((i,2*k+1))
  if not good:continue
  nt+=1
  dual=[[] for _ in range(9)]
  for k,e in enumerate(edges):
   if k not in E:
    f,g=ef[e];dual[f].append(g);dual[g].append(f)
  reached={2};queue=[2]
  for f in queue:
   for g in dual[f]:
    if g not in reached:reached.add(g);queue.append(g)
  assert len(reached)==9 and sum(map(len,dual))==16
  for root in range(10):
   queue=[root];seen={root};mask=0
   for j in queue:
    for i,k in adj[j]:
     if i not in seen:seen.add(i);queue.append(i);mask|=1<<(k^1)
   assert len(seen)==10 and mask.bit_count()==9
   if mask&packet!=packet:continue
   degree=sum(not (mask>>arrows.index((a,b))&1 or mask>>arrows.index((b,a))&1) for a,b in ((7,6),(6,0),(0,7)))
   counts[root]=counts.get(root,0)+1;degrees[degree]=degrees.get(degree,0)+1;total+=1
   if mask&old==old:overlap+=1;nonleaf_overlap+=degree>1
 assert nt==4879 and total==1736 and degrees=={1:957,2:713,3:66}
 assert overlap==36 and nonleaf_overlap==6
 return {'unrooted_trees':nt,'all_rooted_trees':10*nt,'packet_trees':total,'primal_roots':counts,
         'complementary_dual_root_degrees':degrees,'old_packet_overlap':overlap,'old_packet_nonleaf_overlap':nonleaf_overlap,
         'nonleaf_not_containing_old_packet':degrees[2]+degrees[3]-nonleaf_overlap}

def main():
 assert __debug__ and S.__version__=='1.14.0'
 var,z,D,K,ns,hs=symbolic();s=1-var[4];RR=tuple(D*a-K for a in z)
 C=(z[6]-z[7])*(z[6]-z[7]).T+(z[0]-z[7])*(z[0]-z[7]).T
 assert ns[2].dot(z[6]-z[7])==0 and ns[2].dot(z[0]-z[7])==0
 report={'object':OBJECT,'parent':PARENT,'parent_sha256':PARENT_SHA,'theta':THETA,'box':BOX,'hull_box':HULL_BOX,
         'faces':FACES,'arrows':ARROWS,'closed_foot_cells':CELLS,'geometry_checks':true_geometry_checks(var,z,D,K,ns,hs),'normal_checks':[],'matrix_checks':[]}
 for ci,(cell,weights,delta,lams) in enumerate(CELLS):
  assert all(w>=0 for w in weights) and sum(weights)>0 and delta>0 and min(lams)>=0
  U=S.zeros(3)
  for w,(i,j) in zip(weights,ARROWS):
   e=z[j]-z[i];U+=w*(RR[i]*e.T+e*RR[i].T)/2
  report['normal_checks'].append(scalar_check('cell_%d_normal'%ci,-(ns[2].T*U*ns[2])[0],var,BOX))
  foot=[RR[7]+a*(RR[6]-RR[7])+b*(RR[0]-RR[7]) for a,b in cell]
  for ei,(a,b,lam) in enumerate(zip(foot,foot[1:]+foot[:1],lams)):
   P=lam*(a*b.T+b*a.T)/2-D*U-delta*D**2*C
   boxes=[BOX]
   if (ci,ei)==(0,0):
    mid=Q(91,200);assert mid==(BOX[1][0]+BOX[1][1])/2
    boxes=[(BOX[0],(BOX[1][0],mid),*BOX[2:]),(BOX[0],(mid,BOX[1][1]),*BOX[2:])]
   for j,bb in enumerate(boxes):report['matrix_checks'].append(matrix_check('cell_%d_edge_%d_part_%d'%(ci,ei,j),P,var,bb))
 assert sum(c['matrices'] for c in report['matrix_checks'])==35000
 assert sum(c['positive_principal_minors'] for c in report['matrix_checks'])==245000
 A0,A1,Abar=atoms();B=geometry();H=transpose((sub(B['z'][6],B['z'][7]),sub(B['z'][0],B['z'][7]),B['v'][7]));Hi=inv(H)
 assert B['D']/6==Q(881291,9600000)
 assert B['g']==(Q(7368835529,28201312000),Q(3427883561,28201312000),Q(50317,153268))
 records=[census(B,mm(transpose(Hi),mm(A,Hi))) for A in (A0,A1,Abar)]
 assert records[0]['S']==[0,1,2,6] and records[0]['U']==[0,3]
 assert records[1]['S']==[0,2,4,6,7] and records[1]['U']==[1,4]
 assert records[2]['S']==[0,6] and records[2]['U']==[0,3,4] and records[2]['H']==[(3,4),(5,6),(8,9)]
 assert min(records[2]['packet_values'])>0
 assert plus(records[0]['M'],records[1]['M'])==times(2,records[2]['M'])
 p=mv(inv(Abar),(Q(0),Q(0),Q(1)));p=scale(1/p[2],p)
 assert p==(Q(2579129123323,2270929545200),-Q(558780327131,567732386300),Q(1))
 report['physical_controls']={'volume':B['D']/6,'centroid':B['g'],'gauge_H':H,'canonical_atoms':(A0,A1),'canonical_mean':Abar,'mean_foot':p,'records':records}
 # A polynomial canonical-frame numerator, checked against the actual moving frame.
 HF=D*hs[2]-ns[2].dot(K);V=[]
 for a in z:
  Bp=a[0]+3*a[1]+s*(a[2]-1)/4
  V.append(S.Matrix((16*(HF*a[1]-K[1]*Bp),4*(HF*(a[0]-a[1])-(K[0]-K[1])*Bp),s*(HF-D*Bp))))
 HD=S.Matrix.hstack(D*(z[6]-z[7]),D*(z[0]-z[7]),RR[7])
 for i in range(10):assert all(S.expand(t)==0 for t in HD*V[i]-s*HF*RR[i])
 mean=S.Matrix([[R(t) for t in row] for row in Abar]);margin=R(1,5000)
 report['hull_box_margin']=margin;report['hull_box_checks']=[]
 for i,j in ARROWS:
  expr=(V[i].T*mean*(V[j]-V[i]))[0]-margin*(s*HF)**2
  report['hull_box_checks'].append(scalar_check('strict_hull_arrow_%d_%d'%(i,j),expr,var,HULL_BOX))
 # Exact containment of the five-dimensional box of false positives.
 assert all(a<=c<d<=b for (a,b),(c,d) in zip(BOX,HULL_BOX))
 report['tree_coverage']=tree_overlap(B['edges'])
 report['scope']='Two closed foot cells exclude only the displayed packet at actual facet F2 over BOX. HULL_BOX admits two strict-root atoms whose mean satisfies all three arrows, not one physical root metric. No whole-shape or S1/U1 feasibility or exclusion is asserted.'
 raw=(json.dumps(serial(report),sort_keys=True,indent=2)+'\n').encode();path=Path('willow_root_disjunction_report.json');path.write_bytes(raw)
 source=Path(__file__).read_bytes();print(Path(__file__).name,len(source),hashlib.sha256(source).hexdigest())
 print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
 print(OBJECT+'_PASS')
if __name__=='__main__':main()
```

### willow_disjunction_locator.py

```python
#!/usr/bin/env python3
"""Discovery replay for the literal root2 packet; not an exclusion verifier.
OPENBLAS_NUM_THREADS=1 python -B willow_disjunction_locator.py
Companion willow_root_disjunction.py must be in the same directory.
"""
from itertools import product
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
import numpy as np
import scipy
from scipy.optimize import linprog
import willow_root_disjunction as W
assert np.__version__=='2.3.5' and scipy.__version__=='1.17.0' and __debug__
B=W.geometry();H=W.transpose((W.sub(B['z'][6],B['z'][7]),W.sub(B['z'][0],B['z'][7]),B['v'][7]));Hi=W.inv(H)
X=tuple(W.mv(Hi,v) for v in B['v']);T=tuple(W.sym(X[i],W.sub(X[j],X[i])) for i,j in W.ARROWS)
DIRECTIONS=[np.array(d,float)/np.linalg.norm(d) for d in product((-1,0,1),repeat=3) if any(d) and next(x for x in d if x)==1]
TRI=((Q(0),Q(0),Q(1)),(Q(1),Q(0),Q(1)),(Q(0),Q(1),Q(1)))

def dual(cell):
 TT=np.array(T,float);norm=np.linalg.norm(TT,axis=(1,2));TT/=norm[:,None,None]
 edges=[np.array(W.sym(p,r),float) for p,r in zip(cell,cell[1:]+cell[:1])];n=3;m=len(edges);rows=[]
 C=np.diag((1.,1.,0.))
 def row(d,k):
  a=np.zeros(n+m+1);a[:n]=np.einsum('i,aij,j->a',d,TT,d);a[n+k]=-d@edges[k]@d;a[-1]=d@C@d;return a
 for k in range(m):rows.extend(row(d,k) for d in DIRECTIONS)
 normal=np.zeros(n+m+1);normal[:n]=TT[:,2,2];rows.append(normal)
 eq=np.zeros((1,n+m+1));eq[0,:n]=1
 for iteration in range(60):
  res=linprog([0]*(n+m)+[-1],A_ub=rows,b_ub=np.zeros(len(rows)),A_eq=eq,b_eq=[1.],bounds=[(0,None)]*(n+m)+[(None,None)],method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
  if not res.success:return {'status':'UNRESOLVED_SOLVER','message':res.message}
  delta=float(res.x[-1])
  if delta<1e-7:return {'status':'NO_POSITIVE_LOCATED_MARGIN','margin':delta}
  A=np.einsum('a,aij->ij',res.x[:n],TT)+delta*C;bad=False
  for k,E in enumerate(edges):
   values,vectors=np.linalg.eigh(res.x[n+k]*E-A)
   if values[0]<-1e-8:rows.append(row(vectors[:,0],k));bad=True
  if not bad:return {'status':'NUMERICAL_CANDIDATE_ONLY','weights':(res.x[:n]/norm).tolist(),'multipliers':res.x[n:n+m].tolist(),'margin':delta,'iterations':iteration+1}
 return {'status':'UNRESOLVED_ITERATION_LIMIT'}

def finite_atoms(epsilon,denominator):
 # Same fine rational direction grid used in discovery; every atom is physical.
 e=epsilon
 feet=((e,e),(1-2*e,e),(e,1-2*e),(Q(1,3),Q(1,3)),(Q(1,2),e),(e,Q(1,2)),(Q(1,2)-e,Q(1,2)-e))
 directions=[(Q(1),Q(k,denominator)) for k in range(-denominator,denominator+1)]+[(Q(k,denominator),Q(1)) for k in range(1-denominator,denominator)]
 atoms=[];meta=[];values=[]
 for u in feet:
  for d in directions:
   A=W.root_metric(u,d,epsilon);N=W.times(1/W.tr(A),A)
   atoms.append(N);meta.append((u,d,epsilon));values.append([float(W.contract(N,t)) for t in T])
 values=np.array(values);n=len(atoms)
 # HiGHS defaults here, as in the original finite-atom discovery LP.
 res=linprog([0]*n+[-1],A_ub=np.column_stack((-values.T,np.ones(3))),b_ub=[0]*3,A_eq=[[1]*n+[0]],b_eq=[1],bounds=[(0,None)]*n+[(None,None)],method='highs')
 assert res.success
 selected=[(i,w) for i,w in enumerate(res.x[:-1]) if w>1e-8]
 weights=[Q(round(float(w)*10**6),10**6) for i,w in selected];total=sum(weights);weights=[w/total for w in weights]
 M=W.ZERO
 for (i,w),v in zip(selected,weights):M=W.plus(M,W.times(v,atoms[i]))
 assert min(W.minors(M))>0
 arrows=[W.contract(M,t) for t in T];assert min(arrows)>0
 p=W.mv(W.inv(M),(Q(0),Q(0),Q(1)));p=W.scale(1/p[2],p)
 return {'grid_epsilon':epsilon,'direction_denominator':denominator,'number_of_atoms':n,'selected':[(meta[i],w) for (i,_),w in zip(selected,weights)],'exact_mean':M,'exact_arrows':arrows,'mean_foot':p,'numerical_margin':float(res.x[-1])}

def main():
 report={'object':'WILLOW_ROOT_DISJUNCTION_DISCOVERY_REPLAY_V1','theta':W.THETA,'packet':W.ARROWS,'whole_facet':dual(TRI),
         'two_cells':[dual(tuple((*p,Q(1)) for p in cell)) for cell,weights,delta,lams in W.CELLS],
         'finite_atom_discovery':finite_atoms(Q(1,1000000),100),
         'status':'Numerical cell candidates need the separate exact verifier. The rational atom reconstruction is checked exactly; it is a convex average, not a physical root metric.'}
 raw=(json.dumps(W.serial(report),sort_keys=True,indent=2)+'\n').encode();path=Path('willow_disjunction_locator_report.json');path.write_bytes(raw)
 src=Path(__file__).read_bytes();print(Path(__file__).name,len(src),hashlib.sha256(src).hexdigest())
 print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
 print('WILLOW_ROOT_DISJUNCTION_DISCOVERY_REPLAY_COMPLETE')
if __name__=='__main__':main()
```

Convenience copies: complete sources and reports (`willow_disjunction_handoff.zip`), exact verifier (`willow_root_disjunction.py`), exact report (`willow_root_disjunction_report.json`), and discovery replay (`willow_disjunction_locator.py`). The complete inline source is sufficient without these files.
