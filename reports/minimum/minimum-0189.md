# minimum-0189

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# ACTUAL_E17_QUADRILATERAL_BLIND_CONE_AND_SHARP_FACET_GAP_V1

## Result and exact scope

This direction now has an **actual own-centred (10,17,9) countercontrol to the mutual cofactor hierarchy**, not merely formal arrow matrices. Three specified genuine primal arrows and the complete four-arrow stable-root fan are independently strictly feasible at a pair with **rho = 8/91 and Delta = 225/91 > 0**, yet no reciprocal metric realizes those local signs. The sharp fixed-primal-metric root gap is **1/14**. An entire explicitly normalized metric box has the uniform obstruction **rho > 7/164**.

The stronger reusable results are an exact full-facet reciprocal-defect minimum, a genuine-edge mixed cubic identity, a complete affine classification of a three-arrow chain on a stable quadrilateral, and exclusion of a **true trapezoidal strict stable facet as a leaf of a selected complementary dual tree**. A second actual E17 body demonstrates why the trapezoid restriction cannot be replaced by arbitrary quadrilateral.

There is also a consequential negative result: even on one fixed actual own-centred body, a facet-only primal arrow system can have strictly feasible independent blind pairs with rho tending to zero. A positive uniform gap therefore needs metric compactness or constraints outside that facet.

**This is not an actual body with separately feasible complete U1 and S1 cones.** The main fixture is an affine image of the notebook's already all-SPD-U2-excluded bevel family. Its full primal U1 cone is therefore already empty; its newly verified LOCAL three-arrow cone is strictly nonempty. The complete polar S1 cone is not decided here. The new geometric lemmas apply beyond that affine family, but no whole E17 type, global rooted registry or complexity bound is newly closed. The accepted interval remains **34 <= C_min <= 622**. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

## 1. Evidence read and replayed

All three supplied files were read through EOF. No unselected archival payload or research connector was accessed. The new proofs do not rely on external search results.

| Supplied object | Bytes | SHA-256 |
|---|---:|---|
| Complete attached journal | 188236 | 2fdfabffd12a963575b16cbdc11bb25e0870d659e656021414a396f110fef3c9 |
| [internal-source-reference], proof | 11747 | 6e7e96d6cac760f6427523ec34836d79a9dcfe3016b16dbef2d4e5c49d2c4452 |
| [internal-source-reference], reciprocal_gap.py | 7736 | b7092044e73448f35b53f36f404c7e57c352bef9de904dea84a811a466ffd2d1 |

The journal-file hash refers to the complete delivered file, not its separately displayed internal working-memory hash. The full parent source was replayed with CPython 3.13.5, assertions enabled, using `python -B -S reciprocal_gap.py build` and then `check`. Outputs were byte-identical: JSON 7766 bytes, SHA-256 `7dd6c0bda600482c6ac92c536b11e4bbbe67df2235097e13d9547bd5aafe1a72`; stdout 389 bytes, SHA-256 `4271c3883c86e7414ceb9428ea0ead6d9173f672f99d919bd7386851c0295141`.

The inherited theorem used here is precisely that an independently feasible SPD pair with Delta > 0 survives all the specified mutual aggregate/cofactor operations, including weak limits. Its scope does not include additional mixed polynomial identities. :contentReference[oaicite:2]{index=2} The parent's directional defect inequality is retained, but the full-facet minimum below is new work in this handoff. :contentReference[oaicite:3]{index=3}

## 2. Exact full-facet reciprocal-defect minimum

Let P be any full-dimensional convex polytope at a specified interior origin. Let F be a true maximal facet with actual same-origin pole q, so q.x = 1 on F. Fix SPD M and define

\[
A=M^{-1},\qquad s=q^TAq,\qquad p_0=Aq/s,
\]
\[
d_F^2=\min_{p\in F}(p-p_0)^TM(p-p_0),\qquad z_F=s d_F^2.
\]

For an independent SPD N, the outgoing polar-root inequalities `q^TN(r-q) <= 0` for every actual neighbor r of q are equivalent to the foot `Nq/(q^TNq)` lying in the CLOSED actual polygon F. All inequalities are strict exactly when the foot lies in relint F: the neighboring supports give the actual edge halfspaces of the polygon.

**Sharp theorem:**

\[
\boxed{\min_{N\succ0:\,Nq/(q^TNq)\in F}\rho(M,N)
       =\frac{2z_F}{3+4z_F}.}
\]

The minimum is attained. For the strict root fan, the infimum is the same and is attained precisely when the closest point lies in relint F.

Here is an explicit minimizing lift for ANY prescribed p in the facet plane. Set `w=p-p0`, `z=s w^T M w`, `t0=3/(3+4z)`, and define

\[
\boxed{N_p=t_0\left[(1+2z)A-
 \frac{2z}{s}(Aq)(Aq)^T+w(Aq)^T+(Aq)w^T\right].}
\]

Then Np is SPD and

\[
\operatorname{tr}(MN_p)=3,\quad
\frac{N_pq}{q^TN_pq}=p,\quad
\rho(M,N_p)=\frac{2z}{3+4z},\quad
\Delta(M,N_p)=\frac9{3+4z}>0.
\]

**Proof.** Apply the physical linear change `y=M^(1/2)x`, and choose orthonormal coordinates with normal `u=M^(-1/2)q/sqrt(s)`. The facet height is `h=1/sqrt(s)`. Write the trace-normalized matrix S in tangent/normal blocks:

\[
S=M^{1/2}NM^{1/2}=\begin{pmatrix}T&b\\b^T&t\end{pmatrix},
\qquad\operatorname{tr}S=3.
\]

The prescribed foot condition gives `b=t v`, where v is the tangent displacement divided by h and `|v|^2=z`. Consequently

\[
\operatorname{tr}S^2\ge\frac{(3-t)^2}{2}+t^2(1+2z).
\]

Equality requires `T=((3-t)/2)I_2`. The minimum occurs at `t=t0=3/(3+4z)`, with `T=t0(1+2z)I_2`. Its Schur complement is `t0(1+z)/(1+2z)>0`, so the optimizer is genuinely SPD. Transforming back gives the displayed lift. The function `2z/(3+4z)` is strictly increasing, so minimizing over the real polygon proves the theorem. A boundary closest point is approached by interior points, proving the strict-root infimum statement.

**Universal actual-geometric blindness consequence.** Given ANY feasible primal metric M and ANY actual facet F, choose p in relint F. The lift supplies a strictly feasible complete dual ROOT fan with Delta > 0. Thus actual incidence, the actual centroid, and every root-fan sign still cannot by themselves make the cofactor hierarchy detect incompatibility between that root and the primal constraints. The primal system may be larger than the local example below, provided it is nonempty. This does NOT supply the escape arrows from the other dual vertices needed for S1.

The sharp theorem turns a fixed-metric root check into a convex quadratic minimization over the genuine facet rather than independent treatment of its edge halfspaces.

## 3. Mixed identity on an actual edge

Take consecutive true vertices `x0=x`, `x1=x+e`, `x2=x+e+f` of F. Let r be the actual neighboring facet pole across the TRUE edge x0x1. Define

\[
\delta=1-r\cdot x_2>0,\quad
 a=x^TMe,\quad b=(x+e)^TMf,
\]
\[
m=e^TMe,\quad n=f^TMf,\quad k=e^TMf,
\quad\mathcal H=mn-k^2>0,\quad K=mb-k(a+m).
\]

For every physical reciprocal pair `N=alpha M^(-1)`, alpha > 0,

\[
\boxed{\mathcal H\,q^TN(r-q)=\delta(q^TNq)K.}\tag{C}
\]

This is homogeneous of degree two in M and one in N. It couples the actual cross-edge support slack to primal arrow values.

**Proof.** Let `w0=f-(k/m)e` and `h0=w0^TMw0=H/m`. The actual vector r-q pairs to zero with e, to -delta with f, and to zero with x. Since e,f,x are independent, these conditions give

\[
r-q=-\frac{\delta}{h_0}Mw_0+
       \frac{\delta K}{mh_0}q.
\]

Pair with Nq. The first term vanishes because `NM=alpha I` and `q.w0=0`, proving (C).

If K > 0, the true dual arrow across x0x1 is necessarily positive, so F cannot even have a closed-root foot. Every p in F also satisfies

\[
(p-p_0)^TMw_0\ge K/m,
\qquad z_F\ge\frac{sK^2}{m\mathcal H}.
\]

The first inequality is the actual support inequality `(r-q).p<=0`; the second is metric Cauchy-Schwarz. Thus any independent weak-root N obeys

\[
\boxed{\rho(M,N)\ge
\frac{2sK^2}{3m\mathcal H+4sK^2}.}\tag{D}
\]

This is a valid common-metric obstruction even where the separate cones and all mutual cofactor aggregates remain feasible.

## 4. Complete quadrilateral classification and trapezoid leaf obstruction

### 4.1 Exact endpoint-chain criterion

For a genuine quadrilateral F with cyclic vertices x0,x1,x2,x3, use the affine chart

\[
x_1=x_0+e,\quad x_2=x_0+e+f,\quad x_3=x_0+u e+v f.
\]

Strict convexity is exactly `u<1, v>0, v>u`. A trapezoid is characterized by `u=0` or `v=1`, including a parallelogram at `(u,v)=(0,1)`.

**Classification.** For this specified oriented chain, a physical SPD metric with F strictly stable and weak arrows `x0->x1->x2->x3` exists **if and only if**

\[
\boxed{u<0\quad\text{and}\quad v>1.}
\]

When these conditions hold, all three arrows can be made strictly positive. This applies to any actual facet at its fixed interior reference; it is not a free recentering statement.

**Necessity.** Strict stability makes the outgoing dual arrow across x0x1 negative. Equation (C), with a,b >= 0, gives K < 0, hence k > 0. Write the physical foot as `p0=x0+eta e+theta f`. If u >= 0, every interior point has eta,theta > 0, so

`0=p0^TMe=a+eta m+theta k>0`, a contradiction.

The third arrow is exactly

\[
c=(u-1)(a+m+k)+(v-1)(b+n).
\]

Since u<1 and a+m+k>0, c >= 0 is impossible for v <= 1.

**Sufficiency, with rational recovery formulas.** Put `r0=-u/v`, `t=r0/3`, and

\[
B_0=1-u+2t(v-1),\qquad
 d=1+\frac{tB_0}{2(v-u)}+
       \frac{(1-u)(1+t+t^2)}{v-1},
\]
\[
\theta=\frac{t}{2d},\quad\eta=-2t\theta,
\qquad G=\begin{pmatrix}1&t\\t&t^2+d\end{pmatrix}.
\]

G is SPD. The inequalities `theta>0`, `eta<1`, `eta>(u/v)theta`, and `(1-u)theta-(v-1)eta<v-u` put p=(eta,theta) strictly inside the actual quadrilateral. The first two arrows are

\[
a=t\theta>0,\qquad b=t/2+t^2\theta>0.
\]

The third satisfies `c >= (v-1)d-(1-u)(1+t+a)>0`, by the definition of d and `a=t^2/(2d)<t^2`.

Use the genuine linear frame with columns e,f,x0; it is invertible because the origin is not on F. In this frame F has height 1. The three-dimensional metric

\[
\widehat M=\begin{pmatrix}G&-Gp\\-p^TG&1+p^TGp\end{pmatrix}
\]

is SPD, has foot (p,1), and realizes all three arrows. Transform it back by congruence. The actual origin and volume centroid are unchanged by the metric choice.

### 4.2 Selected complementary trees

**Every true trapezoidal strict stable facet is forbidden as a leaf of a selected complementary dual tree.**

A dual leaf means exactly three of its four true boundary edges belong to the selected primal tree. They form a path. Orientation toward the global primal root has a unique local attachment vertex, producing an endpoint-root or internal-root case.

An endpoint-root case is the three-arrow chain above. A trapezoid has u=0 or v=1, so it is excluded.

For an internal-root case, relabel the path `x0->x1->x2<-x3`. If u=0, the first two arrows already contradict strict stability by the eta/theta argument. If v=1, the arrows `x0->x1` and `x3->x2` point in the same parallel direction e. Their sources have nonnegative e-projection in the physical metric, and their targets have strictly larger projection. Every interior point of F therefore has strictly positive e-projection, whereas its perpendicular foot has zero projection.

This covers weak selected primal arrows and incidental zeros elsewhere. The stable root is STRICT; the theorem is not a blanket exclusion of arbitrary weak-foot packets.

For the literal lattice below, exact enumeration gives **5440** primal spanning trees, of which **2252** make F0 a dual leaf. With all ten primal root labels and stable root F0 fixed, these are **22520 raw labelled domains**. The 16 patterns are four missing boundary edges times four attachment vertices. For EACH missing edge the counts for attachment vertices 0,1,2,3 are `(1291,1304,1175,1860)`. Endpoint-root and internal-root totals are both 11260.

These counts apply to any realization of this lattice with F0 a trapezoid. They are NOT new whole-type or canonical-orbit counts. No arbitrary E17 candidate is asserted to select such a leaf, and no optional available chain is assumed to extend to a complementary pair. The signs are necessary only in the explicitly specified selected-tree domain.

## 5. Actual E17 fixture and strict blind witnesses

### 5.1 Actual body and complete true lattice

Start from these raw vertices, indexed 0 through 9:

```
(-1,-1/2,-1), (1,-1/2,-1), (1,1,-1), (-1,1,-1),
(-1,-1,-1/2), (1,-1,-1/2), (-1,-1,1), (1,-1,1),
(-1,1,1), (1,2,3).
```

Their actual uniform volume is 47/4 and actual centroid is

\[
g=(4/47,77/282,125/282).
\]

For any H>0 set `X_i=L_H(raw_i-g)`, where

\[
L_H=\begin{pmatrix}
1/2&-4/3&-10/1221\\
0&2/3&-3397/1221\\
0&0&-282H/407
\end{pmatrix}.
\]

The actual volume is `2209H/814`, and the actual COM is exactly zero. The distinguished true facet has

\[
X_0=(1/2,7/2,H),\quad X_1=(3/2,7/2,H),
\]
\[
X_2=(-1/2,9/2,H),\quad X_3=(-3/2,9/2,H).
\]

Thus e=(1,0,0), f=(-2,1,0); this is a genuine parallelogram, not a triangulation artifact.

All nine outward maximal facet cycles are

```
F0=(0,1,2,3)       F1=(0,4,5,1)       F2=(0,3,8,6,4)
F3=(1,5,7,9,2)     F4=(2,9,3)         F5=(3,9,8)
F6=(4,6,7,5)       F7=(6,9,7)         F8=(6,8,9).
```

All seventeen true edges are

```
(0,1),(0,3),(0,4),(1,2),(1,5),(2,3),(2,9),(3,8),(3,9),
(4,5),(4,6),(5,7),(6,7),(6,8),(6,9),(7,9),(8,9).
```

The source exhausts all supporting triple planes and merges coplanar triangles into maximal facets. It computes actual volume, centroid and covariance by both an origin fan and a vertex-9 fan, retaining selected zero-volume tetrahedra. Every pole uses the SAME actual origin. The polar is never independently centred.

### 5.2 Strict local feasibility in the blind cone

Take H=10, M0=I, and

\[
N_c=\frac1{91}\begin{pmatrix}99&0&0\\0&99&30\\0&30&75\end{pmatrix}.
\]

All three actual primal arrows `0->1->2->3` equal 1/2. Nc is SPD, with leading principal minors `99/91`, `9801/8281`, `645975/753571`.

The actual root pole and its neighbor across true edge 01 are

\[
q_0=(0,0,1/10),\qquad q_1=(0,-423/625,4211/12500).
\]

The full root fan goes to q1,q2,q3,q4. Its values at Nc are, in that order,

\[
-1269/455000,\quad-47/6188,\quad-141/15652,\quad-423/74438.
\]

Its foot is (0,4,10), strictly inside the real parallelogram. All seven local arrow forms have rank two and inertia (+,-,0), up to the sign used to state the root inequalities, and all are genuine primal or polar edges.

The diagnostics are

\[
\operatorname{tr}(M_0N_c)=3,\quad\rho=8/91,\quad\Delta=225/91>0.
\]

The SAME pair therefore survives the inherited complete cofactor hierarchy. However, for ANY SPD M satisfying the three weak primal arrows, the third arrow gives

\[
c=-a-m-k\ge0\quad\Longrightarrow\quad
k\le-a-m,\qquad K\ge(a+m)^2>0.
\]

Equation (C) forces q0->q1 positive at every reciprocal N, contradicting even the weak root fan.

At (I,Nc), the exact mixed-identity residual is

\[
\mathcal H q_0^TN_c(q_1-q_0)-\delta(q_0^TN_cq_0)K
=-1269/56875.
\]

At the physical pair (I,I), this residual is zero and `q0->q1=2961/125000>0`. This is an actual separation between independent feasibility and common-metric feasibility.

### 5.3 Sharp full-root gap versus one halfspace

At M=I,H=10 the physical foot is (0,0,10). The closest point of the closed true facet is X0, at squared distance 25/2. Its tangent displacement pairs positively, by 1/2 and 5/2, with the two generators e and f, proving the global polygon minimum.

Thus zF=1/8 and the sharp full-root minimum is **rho=1/14**. It is attained for the CLOSED root fan by

\[
N_v=\begin{pmatrix}15/14&0&3/70\\0&15/14&3/10\\3/70&3/10&6/7\end{pmatrix},
\qquad\Delta(I,N_v)=18/7.
\]

Its foot is the actual vertex X0. For the strict root fan, 1/14 is the nonattained infimum.

The single root halfspace across edge 01 instead has sharp bound **49/698**. After positive rescaling its sign form is

\[
B=\begin{pmatrix}0&0&0\\0&0&1/20\\0&1/20&-7/200\end{pmatrix},
\quad\operatorname{tr}B=-7/200,\quad\operatorname{tr}B^2=249/40000.
\]

Its optimizer is

\[
N_\ell=\frac1{698}\begin{pmatrix}747&0&0\\0&747&210\\0&210&600\end{pmatrix}.
\]

The foot (0,7/2,10) lies OUTSIDE the actual edge segment 01 and outside F. The improvement from 49/698 to 1/14 therefore comes from the complete genuine facet geometry, not a stronger treatment of the same isolated halfspace.

### 5.4 Entire nonempty metric cone with a positive gap

Normalize `lambda=tr(M)/3` and impose

\[
|M_{ij}/\lambda-\delta_{ij}|\le1/100.
\]

In the trace-three gauge the three arrows have lower bounds `(9/25,2/25,7/20)`. Their absolute symmetric-entry coefficient sums are `(14,42,15)`.

Throughout this entire closed box,

\[
m\ge99/100,\quad m\le101/100,\quad-k\ge197/100,
\quad\mathcal H\le(101/100)^2,\quad s\ge1/103,
\]
\[
K\ge27387/10000,\qquad
z_F\ge750047769/10612100300>7/100.
\]

Consequently every independently feasible weak-root N satisfies

\[
\boxed{\rho(M,N)>7/164.}
\]

The cone is nonempty and contains the strict blind witness (I,Nc). This is a uniform actual-geometric reciprocal-defect obstruction, not numerical infeasibility.

### 5.5 Physical censuses and preserved nonwinners

| Physical metric | Strict stable facets | Strict unstable vertices | Strict saddle edges | Physical weak points |
|---|---|---|---|---:|
| M=I | 2,3 | 3,9 | 3-9,5-7 | 0 |
| M=Nc^-1 | 0,2,3 | 1,3,9 | 0-3,1-2,3-9,5-7 | 0 |

All 68 primitives are nonzero in both controls. The independent pair (I,Nc) is NOT a physical metric pair and has no asserted physical census.

The capsule preserves H=1 and H=100 controls with exact moments, and the alternative strict blind matrix `[[1,0,0],[0,1,2/5],[0,2/5,1]]`, whose rho is 8/75 and Delta is 59/25. The sampled H controls have physical signatures 222 at I and 334 at Nc(H)^-1, weak000. No sampled census is promoted to a continuous theorem.

## 6. Fixed actual shape does not imply a uniform local gap

Fix an actual F, M, q and any primal arrows lying within F. For epsilon>0 set

\[
M_\varepsilon=\varepsilon M+(1-\varepsilon)qq^T/s,
\qquad s=q^TM^{-1}q.
\]

This is SPD: after whitening M its eigenvalues are epsilon,epsilon,1. Every within-facet arrow scales by epsilon because q.e=0. Moreover `M_epsilon^(-1)q=M^(-1)q`, so s and p0 stay fixed, while the squared tangent distance and z scale by epsilon. Lifting any fixed p in relint F gives

\[
\rho(M_\varepsilon,N_p(\varepsilon))
=\frac{2\varepsilon z}{3+4\varepsilon z}\longrightarrow0,
\qquad\Delta=\frac9{3+4\varepsilon z}>0.
\]

Therefore **no positive uniform normalized-defect floor over all SPD metrics follows from feasible facet-only primal signs and this root fan alone**, even with the whole actual body and its true COM fixed. This does not restore a reciprocal solution: the primal metric approaches a singular limit. Constraints on true edges leaving F need not survive this operation.

For the fixed H=10 body, take `M_epsilon=diag(epsilon,epsilon,1)` and

\[
N_c(\varepsilon)=\frac1{75+16\varepsilon}
\begin{pmatrix}
(75+24\varepsilon)/\varepsilon&0&0\\
0&(75+24\varepsilon)/\varepsilon&30\\
0&30&75
\end{pmatrix}.
\]

The three arrows equal epsilon/2, all four root arrows remain negative, and

\[
\rho=\frac{8\varepsilon}{75+16\varepsilon},\quad
\Delta=\frac{225}{75+16\varepsilon},\quad
\inf_{\text{root}}\rho=\frac{\varepsilon}{12+2\varepsilon}.
\]

Exact controls epsilon=1,1/10,1/100 and both associated physical censuses are preserved. They have signatures 222 and 334, weak000.

### Open candidate sector using accepted metric compactness

The notebook supplies the necessary joint-candidate bound `kappa(Sigma^(1/2) M Sigma^(1/2))<48`, with Sigma the ACTUAL volume covariance. This is inherited, not freshly replayed from its unselected original capsule. :contentReference[oaicite:4]{index=4}

For a general true quadrilateral let `w=x3-x2+e`. The third arrow is `c=-a-m-k+x2^T M w`. If some tau in (0,1] satisfies

\[
48\|\Sigma^{-1/2}x_2\|\|\Sigma^{-1/2}w\|
\le(1-\tau)e^T\Sigma^{-1}e,
\]

then every candidate metric has `x2^T M w <= (1-tau)m`. Three weak path arrows force `k<=-a-tau m` and `K>=tau m^2>0`, contradicting the root by (C). For tau<1 this supplies an explicit open shape sector around a parallelogram, with the displayed closed boundary also safe.

Set `E=e^T Sigma^-1 e`, `Fv=f^T Sigma^-1 f`, `Q=q^T Sigma q`. One further obtains

\[
z_F>z_0=\frac{\tau^2 QE^2}{2304F_v},\qquad
\rho>\frac{2z_0}{3+4z_0}.
\]

Indeed `H<=mn`, `K>=tau m^2`, and the covariance-gauge spectral ratio gives `s m^2/n > QE^2/(2304Fv)`.

This is conditional candidate-sector exclusion. Neither membership of the control matrices in the candidate cap nor coverage of every E17 quadrilateral is claimed.

## 7. Actual nontrapezoid sharpness control

Apply the positive projectivity

\[
Y=x/(1+x_1/4+x_2/5)
\]

to the ten raw vertices above, uniformly refill, and subtract the NEW actual centroid. All denominators are positive. The true (10,17,9) lattice is unchanged, but F0 is not a trapezoid.

The exact raw-image volume is `6815974520000/501096769173`, and its actual centroid is

```
(-956319634108060/2161630598426299,
 -601799320007230/2161630598426299,
  94557408739865/341310094488363).
```

For the genuine cyclic path `(1,2,3,0)`, the affine parameters and construction constants are

```
u=-10/13, v=19/13, t=10/57, d=169591/29754,
eta=-17400/3222229, theta=2610/169591.
```

The metric from Section 4.1, in the actual centred frame, gives positive path values

```
8700/3222229,
16198145/183667053,
124880482186/207727436943.
```

All four actual root arrows at the SAME inverse metric are strictly negative. The complete physical signature is **(S,U,H)=(6,3,7), weak000**, all 68 primitives nonzero. Stable facets are `[0,1,2,3,4,6]`, unstable vertices `[0,6,9]`, and saddle edges `[0,1],[1,5],[2,9],[3,9],[4,5],[4,6],[6,7]`.

This is an actual local common-metric realization, not a formal relaxation and not a global S1/U1 example. It proves that dropping the trapezoid/shape restriction is unsound. The complete rational metric, inverse, vertices, poles, covariance, primitive values and two-fan centroid audit are regenerated by the capsule.

## 8. Scientific effect and continuation

The work moved from embedding a many-arrow formal metric box to analyzing the actual polar-foot map. This produced the sharp full-facet formula, the mixed edge identity and the complete quadrilateral chain classification. The actual bevel fixture establishes strict local blind feasibility; the projectively refilled fixture supplies an actual reciprocal sharpness control. Normal stretching identifies why an unrestricted fixed-shape defect gap fails.

No complete independently feasible U1/S1 pair on an actual E17 body was found or asserted. The main fixture's full primal U1 cone is already empty by the supplied accepted family theorem; its local three-arrow cone is not empty. The new work must not be counted as another exclusion of that already closed family. The trapezoid-leaf theorem applies to arbitrary actual realizations satisfying its geometric hypothesis.

The concrete continuation is to attach (C), the affine quadrilateral test and the full-facet distance objective to surviving selected E17 domains, retaining all true outside-facet primal arrows and nonroot dual escapes. Exact trapezoidal root leaves can be discarded immediately; near-parallelogram sectors can use the actual covariance-gauge cap. Elsewhere, a positive defect floor must be established on a genuinely compact common-metric sector or using outside-facet constraints that block normal stretching. More cofactor aggregates cannot resolve the explicit blind pair.

There is no missing computational parent for the new result. Conditional use of the accepted kappa<48 theorem and selected-tree conventions is inherited from the supplied notebook, not represented as a fresh audit of unavailable sources. All new computations have self-contained exact inputs. Continuum claims are proved above; finite rational checks verify the actual controls and algebraic specializations, not an infinite family by sampling.

## 9. Complete source-only recovery capsule

The runnable capsule below contains, losslessly and in full, the complete 20521-byte `quad_blind.py` source. Compression is transport encoding only: no Library item, old sandbox, parent code or network request is required. The decoded source uses CPython 3.13.5 standard library, exact Fraction arithmetic, assertions enabled and no random numbers. The transport decoder was executed with zlib 1.3.1. Every hull input, metric, projectivity, fan integrator, true-feature audit, tree enumeration and report generator is included.

Save the capsule exactly as `recover_quad_blind.py`, retaining the final newline, and run:

```sh
python -B -S recover_quad_blind.py fresh
cd fresh
python -B -S quad_blind.py build > build.stdout
python -B -S quad_blind.py check > check.stdout
cmp build.stdout check.stdout
```

A separate reconstruction starting only from this encoded capsule was actually executed in a fresh directory. Regenerated report bytes and stdout matched the original execution. This is a source-only cold rebuild, not an independent mathematical verifier or proof-assistant formalization.

| Object | Bytes | SHA-256 |
|---|---:|---|
| recover_quad_blind.py | 9996 | 6538f4764b060cb30a5c8b84edc62bd27ae484c424bd2ca0274da1ddfd3aa21a |
| decoded quad_blind.py | 20521 | 8700b4c5d23cc9754fa178b7aee49599c3b77101f945e4b446dfd3088bfcf04b |
| quad_blind.json | 91047 | 0d05c55d6872bce5e5054f1dc4d0b0c5d32b23978d3d21a40c10d7ee2a7455e4 |
| build.stdout = check.stdout | 509 | 77977bf4631806cfcf1a7230d503a97b54cce80c1b31cd90d45a4335ef7dbfd2 |

Expected terminal output:


[Encoded source block omitted; the code in this passage is incomplete.]


Complete capsule:

```python
#!/usr/bin/env python3
"""Complete lossless source capsule; CPython 3.13.5 standard library.
Usage: python -B -S recover_quad_blind.py fresh
"""
import base64
import hashlib
from pathlib import Path
import sys
import zlib

PAYLOAD = """
c-oabe{-Wavj68(aQmtrV9N>E&d;~Gs%*xyle(EClVoo9&X1xnV4DPk2e9L0-hB7h-I73Hob07$Y>>KJtyZhm-IDxYe>+&^*})`A
4#H%uEnkXxnhf@S`Q?`jzgT&(HnNYk?<+6JqS!0K%!`?p&%JD^O+7y>v>=>@e!(;^3A7?xg}ovRL(N+SQL(>wc}wK9!M;7%Kh*L9
pu8;5;%Jh2*$dOcjprBI#|%EBG|8Ekq)-OUB+zn{ELT9}Tkg%mGr^hG`%UZJ6GQGKj*?)1`Jzo$Q5^iAKM(z<y<0B}lR{f&X*$)s
qHvG<zJE9vp4dmnr>FMesb@_lu4QZYpDy}`M|(%%ad>(Z9QmGqd}K|JhW+Ei{vh-LV{jB4pL(Z(KMe<#eKfI;f=M{-2gC5tAD#w%
e>gns@9$j|xi(F+1#k@ASuEpFi*oJy=0RKKVW4@rHVe~5SY(key9CnRn`Y@ko64SR(PEiql_(JHD~E|d97USOC5)dgV7NTO;~;(-
$6=k&Wx7fLk=HN1Vh%Ewb+_=kC!XhCj#cvYF;5fuoWJCIdwVdz+B)=&wRyIu!Cw{@t1Quq6?D{CcuV6e)7GXbAiW?kJf=<BfH&P2
6qL4M+6zcRdySSHRwC!C$!_G{d&s^AV5o_0=tXD4(Gk~^I6+#pG?=dz#-{U5bAFcQc?+`Pjcunh8TXx@2OsccJHQivw6M_P)r_#@
pD4Bwz~-Q`rNtVX*|hZv`OmP9c+F~kD>5$u2J2{XlovE;_`s-F9nUN~wOF+DXgn6p_`Dfk%A+$e9i?GM3N<X6&61p<OH7Kb6iV52
l&njvKsy&y=+(<}m;qW)>p%5w%m>{*2-+yuCCvX?5c-5*{dEM35Ntqj6k+>ev)8Cc-Z*mLABibKF#+GR&={2cUIrza=%=ThpO>T8
P%X=Wf7;(Qi|nm<?;tZ=bu9eubovNV*DnC)BE_mw|08eK<a#{*N?e;-1fznyJZfQ_huT-e;tKGn_QR<)v(-&hiYpvWY-wyW4gZ1I
{yn<8fnqc)hQ&1eXR2H!X<kHrZY*F)sEY>#wlJwb@RV=?ErAs1E&)>k==MrG7sIkNnRo)2CDWE>O{_okLO(+ceFfhu`2G;ag@<LG
qSx=N>T03iLCv7E>On2QX7d!@4N+ho82I^9^klw@<I-^Ak{ZXL6-%_PQ8ELjB3vz&v6qDT|7eRao56yy@HP=HCbYitB@rc(!jhQp
<H|ujCLHMEkDq&`;F<Qwv?mn5x<nX!EaET$RzMU3!4Li=K!K|@+TQi}5mbAPgU>Wx@FWY&5(m^GNkL7M7b8(f;h&!-(6Lom7S3_#
Ve%(}N?8#g?_*K5G<$RE!4i32J8DylC^3TE)P4n>{}p9}Z|}5<XdDogy$%e`%^7c=Pwk$KTEny+6pwq#DiP!gBZR<>ZcHHH1_cNe
CMy^>@QkQAA)BD;C?BXX5O9D3_IA!Iad?RfP=+utI2^AEgPB_OgSRW*az2ayTf>KmsSHeWBBCkZQU+?4Y5jII;2-s**#=sH{!ck;
@>N{m=sA_<fq0-HqFsqQPC>v37!puO;-aoWGe|jvVLhiOAfQ+hG1HL~qCxHB8-i7m1uq74Ckxk6x`HnGtBhPfXb_c#NHXm@O+u#0
f)e?89>L6e0Ee}q9+OJ$kEI2aq{$9O<z&MS5reI=6!Mg~0BaypW5ATYCKE2`Izt=mQ36h}q39;C38XjL-_A<`)XAbEBIY@X3D$+P
EgmOX=snd+5p>^MF2e*Y>!zqvY!kG2V%S!5^l(^_AoWR(@t!&jfq*hQ)Y*%6K{ZR%2iqZAB>LmDuGY9<R~Y>UhKVyBEy>wdw^3^(
T$disth1h7amCeMO2^<+lKRJ}GiJ?K!Ty^2s|2Q;(V^)yMGu1pa7ybVkuyu-)NFK(6ff)H7fl|si;n`o(igFq@p8uJne^%)`bdi0
STjw`es39Ws#WPW&7&e(huQ>U28hqV^Yx%hQR2rC#=$!E8fIy4oyK74fLV+*V43p6SXqyFEi@2iIcf$v3t&(2%jpaVBoDz*qiZ*o
#Uu`Q+nW$3g$uUDur!<yFyPWS^z6pkfHn{`7F)%|j8LEWTnuvZ<na4Zes{q)se3ffVKkc;Vi^+w3W<*?3+JRP!#7{NndZS!+gukU
|9;-^(Uxfh!-T9NI+MKD`Ki_+bT60Ex1^Pm6ENGHO_hWg$?mz}<ZTab+i=hrW5Xqd4oqR^V7S+|3O&6|tkMkhl%G_h22usmPtH#J
iho^AN}{urL#&F!Jm_2Mgc9AC9<p?<r3Q;|^FV-=CYO5MFgoM$He8lIi>N4l#&_PiGE(p|C^s;ygjH!fN`eZA_ZD1{UNE#%LhDDE
28sV7*KlqQI0>l7iB+ym)4Fd$80Pl6OIAr0Z+)S5YH<npvN+E+-0D<44yQGLI-JT7IZW~unVn@Cmkh(#wCXxKpcwisgd?Ak>kC~m
xHrqig}x(Na-63N)2w+n+|q69om`*|9?~+6W~nK98?0KIAvUQg{)EjX&E}?i|5;0`Brm)PI2+Jf)SO<z;P18g4Jht_++Nwd@HmBx
5CjJz679Ux3iW8KrMKE45pA{N1p$raGdK?*C(nNhxy=Gu{rJgLuaLVtAPy3X%o>zRpcn%l4YZAQr2#TDq0&Y-)Zz2W;hQ+zvsY^;
WvxfGj^a*ISL6z>Ix9*%vE@7nfs~Fx!^I0@75Ti0jpNmbylVBh@bu6wh@O*a2*IRbS*R4Wtuq!jSm1|UUuS?Q=IJ=iGH=$Tf+M^S
Mgpd?2R;Qx&SS@H>u4EBe}PaK_|dQ78`f_99=^F=!pk>|u9Nch6V?fBst4HEFjS6z=w!j+5t`OXZ{Ru1e{vHK98=UGymewXD#Ar>
z|?DyL=VQri9?PKlA$CYYPO{sYpKtwHE(E}E@0d!agirC&4MsPCV9Dx{bAq>9GveM-<H1CJ*Cbm8_`QBX&k+RGj)Iafe<uIS|^&v
Q|~;(K26i2^s{6x42GWwV-NV~dUZ?ceaD;#r4GOIl3X}3fai&#XQ6&eR_3{Ks^!(MSlvOKXQ^t>qN=c<Zg5}>y2H+^S(@_kxUf2g
VR!pb+M(pvqtk<zj`tlGX!v||4jSgVt38)>T@LpQk8dZNS~5*ERg-Bd(oMA#k}5oe8S91apzsEiO5#PB%b`MGxYo5ABF_#H+^K{r
y$R|6%d8=nH^?r*aWIufip|vN1I4e5+K}t#Y7+Uld;*1xX-X=LyAL=#>+#uu_Z*#XF`VQ#a2En7zKA~H0(Rc;KcsPdp|*wUEEX0t
l~|Zd;wqzB8b&2kSu&L+p;EFZb3Z_;1C)AC9Uf^uJ&D2z6d7I@9yxG;LWMfJCz8!|$<NE2CkL#Yw>%O{`Mkrs!iANXJ%a2sN1*fc
RJU1}=mXj46ZnRuPhX%7LkZ{!S}_!Zj^^m8VFu8C&7tleSO-g?9*C?VePd=&@CHTl5pBcW#UH?JnTTJ95H5@<3-uL0`<RNdan)>=
$mXHKW*nqfdxU=ifupPMB{GMzONfe&DC;wrOE83&|GNA<x+fpWV!RmYEjDC_9Mob1cEXO>kmDV)V|I$nDq=GFP(*kGcsRj_Az&P{
Lwr1fvSa>m!cJiVk3RffwP-SIfj*%HgXDnCz$fv7wBd7rWRbkuFtmbj&=!0iVk6K7|2&~j#5|@?-ZGzXlQeiS<`jHL&)j<!&Ne*B
v>au1VHnL?<U1pnGRT!dH^4E44CcLSn!N)KUdN{n8407U1+yihImfVjcnspAnKHuyO0YvI8$$QL8pp@1f6~V%yMIWJVzQDmEPzSW
pgBVnGinfwM!#>HwG9%Hx&O)s1E2<j)8i6OR$HtG5GQ>$w2sY=5UnuPYs%EEjhI_1FiA7vYtzaL5^$<SDbs4wUzf6HnBD{m(QM%<
Vy|)?J0)I$tW{B~1e;RkBJTGsP-c55J4Dh3B&?-<4Y4_~O=67kR+R*z=4l}jlMN9?KhHIq4b1?I8^ZPki3p+4yG7B;HE2#*uXYqi
-8?YLdb2HhY~){<2>wc_bu;x+xhhp)#e+v1U20m{F>_2=)h)1JrC%eYKRz3hs2W;&j9*f*D*Y5dgEk;h*Ao;@-=xqRv_Lsk%)KKj
CjeZEFv&^XI_uY>>8%{IRnIOz@?aCIEs;BZ<W9qwj4>N>a<JslXiIONf{CbWJB)AJ>~fR{uZxJ^IaV3+em51*%MgtznYj%Mg=bt(
$t}qLGdAeIh3LwK__RS!?x6qP#^D<-ovKTivVfLI4%Sx28C-g-<y)>DdVC}YRF*#C-ss+r?GhpLmaQ`|a9}7g_Nz_idb~<9*RI+G
PNT*(RwhG1Wr{GXc0h-vZgF24oPt-MNq3fFi7RphIbzMKy!te!jt<1yCGG6C>smUvgFbk!of>%eXegpNh&Q-Om5Gt>wTy`WhJq-j
s!A$6ii`qL799lZ`wIV~b-jCQI{2V=ZY_*1ELY~6JzT2}{NZ;04lT3EVq5RlJWg-vp@@8NRB894#SmHb+&vmK0WYT}O-wv&&<q(`
U<X^U$kc+E0&&Sbb>I#+Y%#4)OR<d~Rx<_`8B0;keE@)=Ts$jF9Y?X^TRZOC5ebht&2i=JI`z4!gu$xnrYn@-51o$<y3+IjZu4h&
fkjwfL(`E@vHBWc$;ZJLSfbUA=}0z9qX6n?<<|Xl?PZad_y|smFck9LbSU6UZJk7!Tj04VdUs0<%vb89AsFSS&4h)1?PH+eGtNqw
x!7kY!a0X=0BF4nY$S+IQ=oyqMs(~WovU;GIL*VrMMxyFZuAz1!1W6E3i~U@<2%dP6}zfuDs(y@=Mu~oEKK4$@N)i=N8mAVx-xUi
d&|WFVz}CcbnUyK31OCpZ(yUYpz+`*7GPl$?h_g>YfI}AvTCT*r>E>x==5&I7RpT^CBneMhj-yQ7|!8Cg5O$q8rJhGMh&*9WDb;^
0Q!eSrbz@;eq0+9r#WlTC+Q!Zvcsd3<HIfdnt?;JV+%(gD{2hbClKtkHm{5_w0_SK#%MtP0{Axp4#C!60skbxd2mKy*gI&77Af3W
?0x>~n37SOz0YbLv*ekFo;>J$gMU2i(b9FwU^+B7+Yt2@Ip|*yXETNAwE94AHT4dKBo=$K#}Gpvou1TYTsc>i%02{!__#H{B&-C0
$0JL?D*OC#BT)xdDc;ulxTf{PQz8Sdg_r?Nc)6r!NUYvLOr(~_eq?SA6GJijywy{aB*#0iLS9<xZEG8{3S#;WLo{5utK@rP2?^J&
S$zp+hi?cJ(;BpHZ@b2IL0V?RUbPsM7L=M9IfR&J8%y<@O1BA+f8Fgei3NYG=TS0?LwD}Q(|ifbE4Bnqz_oq`lGhb}^s@*GrnCg&
=g%e`JZ7Eo6W|IFt3hO|hs{*Jm?-+$n`@RO*DR4V1RnN8$|y;}`S6zED>xu79z@I1*ih2_-Xf%9@pOzn_6l@qm<CSXDoR3al|&Rc
Ewl6y&u_0oXkr@0F`16bn=kuBh&Bz9Fwb#&pqPjC^Z1%S_b_gWVSu73bO%Eh#?R<!-|T~Xn-W|5k|&;TjWT{<T=ipzq+F<DQn!OJ
Nf#Imr5S|;b{AE=L}r_|gpJIz;K@A&zw%-;?^#Vy1SJ_3$X!BAht-fp)H-b>f`C*l4L4(388`r8fVVRbB<kU-nQ@cEL<_<pCDtin
HB)*I=xVyEo~;s?RniI_)vc73fMT4&?z~kUPQKQ1SS9_o43<b2{^hLI?u^v9b~16wW0jWlRs&82;_kS!D|Mx0t`gSFTeT)&l>7@G
&)Pmm>A(1KIDR^Fy8P+v$=Q8|l0e9$jYSq5?DYV?Z6?oiDF<AJrZ^-?8<cpgjP?|Pi^{#-SZrgnO`mNBJm)HgPdy}#D3yf|ncUbx
L@;9X2m}-#bDE*0;X8ohY&@U=w0d%P#n$YVZwnGUu&`y`UwM8Gm0^WBIC@%_+b{UEQa8p|6y?h*yPg89ju>KYtE$VqC=ay@Y7xxH
2$qw~(63V%%tZuN3=cA>mQ_o$2y~w;n=Y~xxHG;wSntVg^6Y?TRwfhLMp||IouXr`dqPNP5$tZ!nM@9hK9;XcvugmH*)gEJ%MWjt
;9zBGKdL}zVE}kZ59v~MZH~~UlmQHxyprc~;akd(mo|ca&Hz>QsPPU*0rm)N)~`H<0yM8+&~`Tv%l`~_^2f8jxCQ{IUH)P_oTj?m
L5;0~*%cV4wxC0hB{?QZvEFQn$0Ai?V@ZukN(5y$pg5+eVs;nW>QGUa+U;-@(Y!drzYzLM8VX+7++_T*?Yz(%cLLU4yb9HGC32$C
>COl^ZIpD8`^C<Lsj{kZ(#m=U9!j%0?ixYoD<A3ItQnpYsc2ORN8z~QnGLWW_{9w*jxdNwoZz4VpEgd9O5as=dP~-5Q&heQ4_JAx
?~_(Oid(M#=wV4$K!+93Re-Ae4KA>CzY9UDw9Sl_*&VU)D#@R6wNvsuxVqH|swp3y@hKBNt$Qv^rhK@gS0`4>{(uiCb3fcQ)KOdD
1y7&jjgb{_3v4!MfZtkxGYSHNrf^#r2S=wdf*KksJT0?e<hM56Qaa(~ViPXc1!#c28P6tx13F8=mo957t$EkOmGW#jx(m9rLO$&@
+Ju3d&%yY*6f;K2G+L|{1`KtY1;V>636;w>uO3%}=P+5sCFoSQ8yKzKvYHP@1+I<&NBUmwqgc+41bP{efpnIu#tnsVnMW~ryEykm
q-7(9_y*K!by}47l>`=(-?pQkV1H$5dVayaGd086TvKrq7Q(5Hp!H6Q=|sXE7{`ZQ`$)c;?RZMu*2moU+c-^&7%8@pwlNkvcQGVa
eYuhGZe;jgV3>eUvS!sj0LroC#&X_HgOx(E`>@_`^_OdcJhJvf7XUCD#ek}Fun~V^^0q#gw$igMUH&Q=+A;OqFMnb3?ZUmT@~ZF9
ph(p;f0~U*bxFZ0U9rqvyqqmhV9LWp;?58EoAE|T(o@_xLFl6g4qR<}h)%F@<w(kCaZ1(YmBQ+#4PlKv2kCo_ePT2OqPp3vw^v<e
s!sbVxnedE*w7}U?@8_4CLLa#)EnIDQrRtJ5WrOl;uWFtl4lsYbhEu~3Ck0$Ef!7NZPLoy7U$Xzao~mL8~fte%Rpoue7wpH4HRjC
x9{W7Ta&#NSG*0A-=8c+<<CJwlO21R_OZ!MmEkGq$S|>63qd#$r+Mp7>QE7)^?c_Z9x;rY%=XqK7G%cZwB>dz@W{8tsl}2P;Jc*r
6fV)imons6)rzn-_^8$hNLoF3hgl)k8n+aTBr|yd3vc2ZvdJD%Hfx6>R!Se5(ph>L)99=y4*2S9g@>hA+t+73q(N|Jdv9!07h(Hd
3Y-tsp#o1HDxmWgRYA|*b^UKb_fp80o=Euv>t{Q!U_j+~g44#^2|~S*R(R4l;hZj8&#Vut`^PJdqUj7ZMQ|ixoLzV6fUI&hwi<Mt
Nn=BdD+4IH08x#)jLZ03<2u3cU;#(n=T4Sk@}n5W;c#d%SaJLGVO7Du)EwYdD$Ldn*SN_}rrxJ7yU4dP`lsNh3@mVS?BhdbpBxE4
2t-OL4rGy^y2rT;q?pew0I@C3MWaYFX-4Zg9wGx$u=__=<A7uw(`1E3kxNDYXt^MnsVo&zBG(jF#vomI5pH&pNSeNN640UU3JP0h
dX(@V{b*qKsJ40jx<J^R9}yR_13FBnyO?6*G=qQv`wr{o&)wIDxWGzji9}IdXr}YCJRi7ev;Vjs-tPWt4gXg<uP|D9;|6W}EvXHo
D*{_*dm2{-ke-}h^s57t+`xl3bPlKG9CdrXi(jNtaG#v+20l2IH|}8ZGagTGo}Q^+kEH&iS`XQ<&+J1H2BY)n#^OX1KUvYs58%NP
KRv(?`~!CVw26X8h_rD*`z8GQn8Dl>X$Amei+MDgv!^7S(N)FMQwjkv7O?E{5sx!kVoE;&7Un15t5dZ$ww*2#=@?3x<#Z9O)?bcJ
d&9?r6QV0AzjDe5(dqQTk+lXLVz1K~)DOZS;NLauOv#q0>UU%*KaVcoOx`BElxKV7q^|BBxENNyxS1D3E0|L<9%6dcC;hB?ZcIkd
76{pk(Dl=BI*oix)44c65QoDj)Bk~3`Wg1Gc_#yF@a6>ejOjW4Kn}Uo?lex*3|Zlv%jp*;ej0?vrt(`OnELpmLOztTujZE53N($)
zBr+nW@P_1`^vroPj=FhNU&xr<p3DlCjR5;OmMUoiD0%y_1s9q@w1f}|LGM<MVs41$90mNprel6M&9ZLGilUa`1}Q|KsH;GzthK6
Q<i|H%B9oL>F1Jku#fnINxIog%ih1_!2f6iW={W)etSt~X36H!6s7~!UyZp)_|HWMhzE)-IUxg&(yBl7A}V4CbM%YLhi@03-I0Cl
e*Jdw;qL15#lz?hN`Cu%b^XD;yty8^7w~ZZ>EiCz{djRXdT@WgxOM+&>n&-fDwBj;O1fYU)(8I3z^HBK<#O8%qQlm0z6SEHyorAH
PDTX{Nt0L=Y{0VH3_Li3Uam*_S#xP>Bboc@k_60e7p2ch@ABpgZVpEH^CJ;x-U1d^%D(g8Zh)SGOPnV0%f6<!E&!OcpRVFqY&1?o
k7w_fUX+RR585nFC-mc3e!R+Y%h8X$Xb}ec`cJV<^Ae{XCg=_P`KkS2wOHncm<XsICc}l<eF|UlbBxCz)`dA-ocGPH{=bQC?hDvz
*9U0fk6anLqO3?;FDJM<Gr$OlNpV*Db&37w45qR>c`3l<6I_a|fLO#s1Qu>!N~3!vc767<5L+cQnu`MWt(i8WUqZ`5`sFR@J#t5K
;T15y0=>K<n*h8rOCJ8XfoX7k?|!-X^Xdx}(ww;GljP#d$i2C{`u*zKy}kK7x_56c?(gfQ?jP>1E+5>_H<#rkyS=!&bMHRgxF_z-
KSy`&sojG2`{?@H6--9l7IeQ{{W*fk`R%u>OJ#Q6-Q4iWX>&UEu!YVapMWv<%Lv(Uf4lk96%1kfA3xvR+_}dB`=|~5;qKeWeYhKq
+|Q$nk1qL*?uVN%7grz>`v@=|z<yk}^;`(?`sVuK?&5az@0+U+?%n9}>h_Lgarp^o@Sa?c?%N1_q+Sa$0C+o+%vW-}r;a>~u0Pzn
xY61|hKv64=G!%JdWqcJAXg9Wh5PZ_=g;mp+r78lkE4tGtKUFWzukQJSB(HEU4lD$bk$dADigo$whxA<e|S`u@6W?c5JA9S7<9QD
RM~YA+jVIwxGt_Ot}A8(UugFJABo?om;
"""

def main():
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python -B -S recover_quad_blind.py fresh')
    data = zlib.decompress(base64.b85decode(''.join(PAYLOAD.split())))
    assert len(data) == 20521
    assert hashlib.sha256(data).hexdigest() == '8700b4c5d23cc9754fa178b7aee49599c3b77101f945e4b446dfd3088bfcf04b'
    folder = Path(sys.argv[1])
    folder.mkdir(parents=True,exist_ok=True)
    target = folder/'quad_blind.py'
    if target.exists() and target.read_bytes() != data:
        raise SystemExit('Refusing to overwrite a different quad_blind.py')
    target.write_bytes(data)
    print('EXACT_QUAD_BLIND_SOURCE_RECOVERED',len(data),hashlib.sha256(data).hexdigest())

if __name__ == '__main__':
    main()
```

Optional convenience copies: [decoded source](sandbox:/mnt/data/quad_blind/quad_blind.py), [exact report](sandbox:/mnt/data/quad_blind/quad_blind.json), [source capsule](sandbox:/mnt/data/quad_blind/recover_quad_blind.py). The embedded capsule is sufficient without these links.
