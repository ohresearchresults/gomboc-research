# minimum-0295

AI research report · 2026-09-28 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# AFFINE_DENSITY_CLIPPING_STATIONARITY_AND_TWO_ARC_REDUCTION_V1

## 1. Outcome, authority, and remaining status

I did not obtain a universal three-halves proof or a violating actual body. The main advance removes a genuine boundary obstruction in the affine-density problem: **even when the density vanishes on a supporting edge or at a marked-edge endpoint, every affine density direction is two-sided to first order if the support is clipped simultaneously.** The clipping is an actual convex-body operation, not a signed-measure relaxation. Thus all three affine density stationarity equations hold at a full joint maximum, without density-cone multipliers or exceptions at zero contacts.

I also obtain the exact second-order clipping correction, including the separate marked-endpoint term; a strict negative-density-Hessian condition at a disjoint zero edge; and a sharpening of the accepted conic reduction from at most four curved arcs to **at most two**. When two arcs lie on opposite sides of the marked edge, their common opposite line must be the density-zero line. This gives the explicit six-parameter actual-support system below. A separate reflection-symmetric, arbitrary-convex-floor family satisfies the full marked three-dimensional matrix inequality.

The new exact controls are nonviolating. They demonstrate genuine ascent through a formerly one-sided density boundary, verify both second-order corrections, and preserve an exact failed sign mechanism. None is an E17 exclusion or a class110 construction.

**Input audit.** I read the complete supplied journal through EOF, including the literal parent, and decoded and read its ten-source capsule. The journal is 354886 bytes, SHA-256 `9f492b9f579fe03e3a740d910b233487b2f0eab8d2e14fe40b58b988df8e2fa8`. The literal parent, reconstructed as its compact UTF-8 version-2 JSON envelope with the Markdown's terminating LF, is 45046 bytes and has the required SHA-256 `a1afff32561b16a73bf7a017e7ad3233330ac76bf67282f7cac952c02cc464a8`, assignment `minimum-0290`. No parent-identity conflict was found. I did not rerun the parent's acceptance program.

The later complete files identified as `[internal-source-reference]` and `[internal-source-reference]` are not separately attached. Their accepted attainment/conic and uniform-density statements are present in the journal; I use the former explicitly in Section 5 and the recorded normal/fibre results in Section 6. I do not claim to have recovered or replayed the absent later programs. The new clipping theorem and its exact verification are self-contained below.

## 2. Actual quantities and the operation

Let K be compact, convex, and full-dimensional in the plane. Let t be affine, nonnegative on K, with genuine whole edge e=K intersect {t=0}. Let ell be nonnegative affine, not identically zero, and assume B0>0. Use dσ=ds/|grad t| on e. For a nonconstant affine test centered under the ACTUAL law ell dx, so I>0, put

\[
V=\int_K\ell,\quad J=\int_Kt\ell,\quad m=J/V,\quad
\int_K\ell Y=0,\quad I=\int_K\ell Y^2,
\qquad B_j=\int_e\ell Y^j\,d\sigma.
\]

The two ratios are

\[
R=\frac{JB_2}{VI},\qquad
L=\frac{JB_1^2}{VB_0I}.
\]

These are precisely the actual planar side quantities in the literal parent. Its lift P={(x,z):x in K, 2|z|≤ell(x)} has volume V, centroid (g_ell,0), and marked lateral-facet mass alpha=mB0/V. The exact reduction of both three-dimensional constants to these side constants is an imported parent theorem, not repeated here. fileciteturn0file0L1093-L1116

For ANY affine ψ and either sign of a sufficiently small real s, define

\[
\ell_s=\ell+s\psi,\qquad K_s=K\cap\{\ell_s\ge0\},\qquad
 e_s=K_s\cap\{t=0\}.
\tag{2.1}
\]

The actual uniformly filled lift is

\[
P_s=\{(x,z):x\in K,\ 2|z|\le\ell(x)+s\psi(x)\}.
\tag{2.2}
\]

It is the intersection of convex constraints, hence convex. Its projection is K_s, its density on that projection is the affine ell_s, and e_s is its complete marked projected edge. The positive-part notation (ell+sψ)+ on the OLD K is only an integration identity; it is not being asserted to be affine on old K.

Set

\[
c_s=\frac{\int_{K_s}\ell_sY}{V_s},\qquad Y_s=Y-c_s,
\qquad m_s=\frac{\int_{K_s}t\ell_s}{V_s}.
\]

Then E_sY_s=0 exactly. Replacing t by t/m_s retains E_s(t/m_s)=1 exactly; J and coarea edge moments rescale inversely, so both ratios are unchanged. Thus the operation retains both required actual mean equalities after their permitted normalization. It does not recenter the facet separately.

Small s retains positive volume and positive marked area. K_s converges to K: contract K toward any fixed point with positive ell to obtain an interior approximation lying in K_s. The same argument along e shows e_s converges to the complete e. Combinatorics may change; this is not a same-lattice mechanical deformation theorem.

## 3. Two-sided first derivatives at every density boundary

### Theorem 1 — clipping costs only second order

For every bounded continuous f on K,

\[
\int_{K_s}f\ell_s=\int_Kf(\ell+s\psi)+O(s^2).
\tag{3.1}
\]

The corresponding whole-edge identity holds with e_s and e. These statements include density-zero edges and density-zero marked endpoints.

**Proof and quantitative error.** Suppose grad ell is nonzero; write D=diam K, M=max_K|ψ|, and δ=|s|M. The difference in (3.1) is supported in 0≤ell≤δ. Each ell-level chord has length at most D, so coarea gives

\[
\left|\int_Kf\big((\ell+s\psi)_+-(\ell+s\psi)\big)\right|
\le\frac{\|f\|_\infty D}{|\nabla\ell|}
       \int_0^\delta(\delta-r)\,dr
=\frac{\|f\|_\infty DM^2}{2|\nabla\ell|}s^2.
\tag{3.2}
\]

If ell is constant positive, there is no clipping for small s. If ell restricted to e is strictly positive, likewise there is no edge clipping. Otherwise it vanishes at exactly one endpoint p, since B0>0. With γ_e=|D_e ell|, where D_e uses a unit tangent, the analogous one-dimensional bound is

\[
\frac{\|f\|_\infty M^2}{2\gamma_e|\nabla t|}s^2.
\tag{3.3}
\]

This proves the result for either sign, including the actual entire shortened edge. Applying it to the finitely many raw monomials needed for the centroid and second moments proves differentiability of both centered ratios. ∎

Define

\[
\Phi_R=\frac tJ-\frac1V-\frac{Y^2}I-
             \frac{2B_1Y}{B_2V}.
\]

Direct differentiation, including c'_0=(int_K Yψ)/V, gives

\[
D_R(\psi):=\left.\frac d{ds}\log R_s\right|_0
=\int_K\Phi_R\psi+
  \frac{\int_eY^2\psi\,d\sigma}{B_2}.
\tag{3.4}
\]

For L>0, put

\[
\Phi_L=\frac tJ-\frac1V-\frac{Y^2}I-
             \frac{2B_0Y}{B_1V}.
\]

Then

\[
D_L(\psi)=\int_K\Phi_L\psi+
\int_e\left(\frac{2Y}{B_1}-\frac1{B_0}\right)\psi\,d\sigma.
\tag{3.5}
\]

The bulk integrals in (3.4)–(3.5) are UNWEIGHTED area integrals: ψ is the density perturbation. The leverage edge kernel is different from the strong kernel and must not be replaced by it.

**Consequence.** At any full joint local maximum of R, every affine ψ has D_R(ψ)=0. At any positive full joint local maximum of L, every affine ψ has D_L(ψ)=0. In particular, for an independent coordinate pair (t,Y), stationarity holds for ψ=1,t,Y even at every zero-density boundary. For the strong target,

\[
\int_Kt\Phi_R=0,\qquad
\int_KY\Phi_R+\frac{\int_eY^3d\sigma}{B_2}=0.
\tag{3.6}
\]

Scaling ψ=ell gives −1+1=0, a useful check. The journal's one-sided caveat concerns density changes on FIXED K. It remains correct in that class; (2.1) supplies a different admissible actual-body variation and removes that caveat for joint maximization. fileciteturn0file0L1028-L1031

This is also constructive. If d=(D_R(1),D_R(t),D_R(Y)) is nonzero, use ψ=d0+d1 t+d2 Y. Then D_R(ψ)=|d|²>0, so actual clipped lifts strictly improve R for all sufficiently small positive s. For rational polygonal input, including the affine functions, this ψ and every sufficiently small rational s give a reconstructible rational actual lift and rational actual centroid. The same statement holds for positive L using (3.5).

## 4. The exact second-order boundary term

The first-order repair does not license dropping boundary effects at the next order.

Let Γ=K intersect {ell=0}. For nonconstant ell and s decreasing to zero through positive values,

\[
\int_Kf(\ell+s\psi)_+
=\int_Kf(\ell+s\psi)
+\frac{s^2}{2|\nabla\ell|}
  \int_\Gamma f(-\psi)_+^2\,ds+o(s^2).
\tag{4.1}
\]

For negative s replace (−ψ)+² by ψ+². The Γ-integral is zero when Γ is empty or a point. No cubic error is asserted at a general curved point contact.

To prove (4.1), apply coarea with r=ell and rescale r=|s|u. The relevant cross-sections converge to Γ, while ψ and f converge uniformly on the shrinking strip. The integrand is dominated by the strip bound used in (3.2). Integration of (−u−ψ)+ over u≥0 gives (−ψ)+²/2. If Γ is a point, the chord lengths tend to zero, giving o(s²).

At a zero-density marked endpoint p the separate correction is

\[
\frac{s^2 f(p)(-\psi(p))_+^2}
 {2\gamma_e|\nabla t|}+o(s^2),
\tag{4.2}
\]

again with ψ+² for the other sign.

Let H_form(ψ) be the second derivative of log R obtained from the formal signed continuation on fixed K,e, with its algebraically recomputed mean. This formal calculation is NOT an admissible probability law; it only computes a Taylor coefficient. At density stationarity the two actual one-sided second derivatives are

\[
H_{\rm form}(\psi)+C_+(\psi),\qquad
H_{\rm form}(\psi)+C_-(\psi),
\tag{4.3}
\]

where

\[
C_+(\psi)=\frac1{|\nabla\ell|}\int_\Gamma\Phi_R(-\psi)_+^2ds
+\sum_{p\in e\cap\Gamma}
 \frac{Y(p)^2(-\psi(p))_+^2}{B_2\gamma_e|\nabla t|},
\tag{4.4}
\]

and C− replaces negative parts by positive parts. There is at most one endpoint in the sum. For leverage replace Φ_R by Φ_L and the edge coefficient Y(p)²/B2 by 2Y(p)/B1−1/B0; the latter need not be nonnegative.

For a compact formula, subtract (int_K ψ/V)ell from ψ, so int_K ψ=0. Define

\[
p=\frac{\int_KY\psi}{V},\quad j=\frac{\int_Kt\psi}{J},
\quad q=\frac{\int_KY^2\psi}{I},\quad E_i=\int_eY^i\psi\,d\sigma,
\quad d=\frac{E_2-2pB_1}{B_2}.
\]

Then

\[
H_{\rm form}=-j^2+q^2-d^2
+2p^2\left(\frac{B_0}{B_2}+\frac VI\right)-\frac{4pE_1}{B_2}.
\tag{4.5}
\]

At stationarity d=q−j, this becomes

\[
H_{\rm form}=2j(q-j)
+2p^2\left(\frac{B_0}{B_2}+\frac VI\right)-\frac{4pE_1}{B_2}.
\tag{4.6}
\]

For example, under the volume-fixed perturbation the central volume moment is I_s=I+s int Y²ψ−Vp²s², and the edge second moment is B2+s(E2−2pB1)+s²(p²B0−2pE1)+s³p²E0. These identities directly yield (4.5). The attached standalone verifier checks the complete algebra without numerical differentiation.

### A strict necessary Hessian condition at a disjoint zero edge

Suppose Γ is a positive-length edge disjoint from e, (t,Y) are independent, and the body is a full joint local maximum. Localized cap removal at any off-e extreme point gives Φ_R≥0 there: otherwise the cap lies where Φ_R<0, and deleting its positive ell-mass strictly increases R. This argument still works when ell vanishes at the extreme point; the cap's interior has positive ell.

On Γ, Φ_R is strictly concave if Y varies. If Y is constant there, independence makes t nonconstant and Φ_R is nonconstant affine. In either case nonnegative endpoint values imply Φ_R>0 throughout the relative interior. Therefore

\[
Q_\Gamma(\psi)=\frac1{|\nabla\ell|}\int_\Gamma\Phi_R\psi^2ds>0
\]

for every affine ψ not proportional to ell. Both one-sided maximum inequalities in (4.3), averaged, give

\[
H_{\rm form}(\psi)\le-\tfrac12 Q_\Gamma(\psi)<0.
\tag{4.7}
\]

Thus a disjoint zero-edge maximum must have a **strictly negative definite formal density Hessian on the two-dimensional quotient by scaling**. A nonnegative direction of (4.6) rules it out. This is a necessary condition, not an assertion that all candidate Hessians fail it.

## 5. From four parabolic arcs to two, and an actual six-parameter system

This section uses the accepted strong-attainment and nonsmooth-conic theorem recorded in the supplied journal: a hypothetical strong maximum R>3/2 is attained, is non-normal, and has finitely many straight pieces and arcs of the SAME parabola

\[
t=F(Y)=m+(J/I)Y^2+2m\eta Y,\qquad\eta=B_1/B_2,
\]

whose minimum is strictly positive. Every positive-density nonmarked straight edge meets an endpoint of the marked edge; there is at most one zero-density straight edge. This imported theorem does not assert weak-leverage attainment. fileciteturn0file0L1003-L1012

Normalize the marked edge to t=0, −1≤y≤1, using an affine reparametrization of the independent test. Write K between its lower convex graph L(y) and upper concave graph U(y).

An arc of the upward parabola can occur only on L. It cannot occur with y in [−1,1]: its supporting tangent at that point has positive t, whereas (0,y) is in e. Thus every arc is in y<−1 or y>1.

If the projection extends on BOTH sides of [−1,1], U(−1),U(1)>0. No point of the upper graph is a marked endpoint. Its boundary has no curved arcs, and every straight portion must therefore be zero-density. All those portions lie on the same affine zero line; hence U is one zero-density edge. No separate zero edge remains to split a lower wing. Each lower wing consequently contains at most one arc.

If the projection extends on only ONE side, distinct arcs on that lower wing can be separated only by a straight edge not meeting e. Such an edge must be the unique zero-density edge. There is at most one separator, hence at most two arcs. Adjacent arcs without a separating interval merge, since they lie on the same parabola.

**Conclusion:** every hypothetical supercritical strong maximizer has at most TWO positive-length parabolic arcs. With no density-zero edge it has at most ONE. This includes strictly positive densities and densities vanishing only at a point. It does not impose a vertex bound on arbitrary supports or assume polygonal localization.

### Opposite-side two-arc chart

When there is a nonempty curved arc on each side, the upper line is the density-zero line. After scaling density and t, the entire actual candidate has parameters

\[
a<u<-1<1<v<b,\qquad C>B^2,
\]

and

\[
f(y)=y^2+2By+C,\qquad
U(y)=(a+b+2B)y+C-ab,
\]

\[
S_L(y)=\frac{f(u)}{u+1}(y+1),\qquad
S_R(y)=\frac{f(v)}{v-1}(y-1).
\]

Its lower graph is, in order,

\[
L(y)=
\begin{cases}
f(y),&a\le y\le u,\\
S_L(y),&u\le y\le-1,\\
0,&-1\le y\le1,\\
S_R(y),&1\le y\le v,\\
f(y),&v\le y\le b.
\end{cases}
\tag{5.1}
\]

Require f'(u)≤S'_L and S'_R≤f'(v), with U≥L. These are coupled actual convexity conditions. At a maximizing positive-density stem the corresponding inequality is strict: a tangent stem has t−f<0 in its interior; rotating it upward about its marked endpoint removes negative-Φ mass and strictly improves R. The possible tiny extra cap near a tangency is higher order than the negative-work stem contribution.

The support and density are

\[
K=\{a\le y\le b,\ L(y)\le t\le U(y)\},\qquad
\ell=U(y)-t.
\tag{5.2}
\]

Thus the affine density is FORCED by geometry in this case, not an additional independently chosen function. The actual lift uses 2|z|≤U−t.

All raw weighted moments are reconstructed by the exact formula

\[
\mathcal M_{pq}=\sum_{[r,s],L}
\int_r^s y^q\left[
\frac{U(U^{p+1}-L^{p+1})}{p+1}
-\frac{U^{p+2}-L^{p+2}}{p+2}
\right]dy.
\tag{5.3}
\]

Here the sum is over the five pieces of (5.1). V=M00, J=M10, μ=M01/V, Y=y−μ, and I=M02−M01²/V. The whole-edge moments are B_j=int_{−1}^1 U(y)(y−μ)^jdy. The vertical variance is sum int(U−L)^4dy/(48V), and its marked moment is int_{−1}^1 U³dy/(12B0). These are the actual moments of one uniform body.

A supercritical candidate in this chart must satisfy simultaneously:

1. All three coefficients of f(y)−[m+(J/I)(y−μ)²+2mη(y−μ)] vanish.
2. D_R(1)=D_R(t)=D_R(y)=0, with one scaling dependence.
3. Both genuine stem rotations have zero work: int_u^{−1}(y+1)(U−S_L)Φ_R(S_L,y)dy=0 and int_1^v(y−1)(U−S_R)Φ_R(S_R,y)dy=0.
4. Optimization of the independent affine test imposes int_K ell tY/I+mη=0. This follows by varying Y toward t−m, which is also actually centered.
5. The two second-order inequalities (4.3), in particular (4.7), hold.

The standalone source below evaluates this entire actual system at arbitrary rational parameters satisfying its strict chart guards. It does not prune a candidate for failing the desired three-halves conclusion. No resultant, CAD exhaustion, or universal infeasibility certificate for this six-parameter system is claimed. Same-side arcs separated by a zero-density chord and the one-arc configurations remain separate alternatives. Zero-length arcs and coincident joins are boundary alternatives; no division by their lengths is used to exclude them, and they remain in the one-arc or polygon cases.

## 6. A complete infinite-dimensional symmetric-floor subclass

Let H>0, b≥a>0, and let λ:[−b,b]→[0,H] be continuous, even, convex, with zero set exactly [−a,a]. Define

\[
K=\{(t,y):-b\le y\le b,\ \lambda(y)\le t\le H\},
\qquad\ell=H-t.
\tag{6.1}
\]

The marked whole edge is t=0, |y|≤a. The actual uniform lift has reflections y→−y and z→−z, so its covariance and marked second-moment matrices are diagonal in (t−m,y,z). The facet centroid has only its normal component.

The actual y marginal is ρ(y)=(H−λ(y))²/2. It is constant H²/2 on [−a,a]; every unit of outside mass has y²≥a². Consequently

\[
\operatorname{Var}_P(y)\ge a^2/3,
\qquad
\frac{\alpha E_Fy^2}{E_Py^2}\le\alpha\le3/4.
\tag{6.2}
\]

More precisely, if V_core=aH² and W=V−V_core, the ratio is at most alpha V/(V_core+3W). The facet-mass bound alpha≤3/4 is the recorded actual affine-density bound. fileciteturn0file0L1005-L1007

The normal entry is at most3/2 by the accepted universal normal theorem, and the z entry is at most10−5sqrt(3)<3/2 by the literal parent's arbitrary-support fibre theorem. Hence the complete marked three-dimensional matrix inequality holds for every body (6.1), and for every affine image of it. Leverage follows as well. The floor may have arbitrarily many knots, curved pieces, stems, or nonsmooth convex parts. This is not restricted to the previously certified two-parabolic-wing family, and it is not the parent's marked-end homothetic-profile theorem. Only the specified marked facet is asserted. fileciteturn0file0L948-L949 fileciteturn0file0L1244-L1254

## 7. Exact actual controls and a preserved failed sign mechanism

### 7.1 A genuinely mixed test improves through zero-edge clipping

For 99/100≤H≤1 use

\[
P_H=\{0\le t\le H,\ |y|\le(1+3t)/2,\ |z|\le(H-t)/2\}.
\]

This is the actual operation ψ=−1, H=1−s, on the parent support with ell=1−t. Its six vertices, in order, are

```
(0,-1/2,-H/2), (0,1/2,-H/2), (0,1/2,H/2),
(0,-1/2,H/2), (H,-(1+3H)/2,0), (H,(1+3H)/2,0).
```

The outward maximal cycles are `(3,2,1,0),(0,1,5,4),(2,3,4,5),(0,4,3),(1,2,5)`. The marked facet is the FIRST complete rectangle. This is true6/9/5, not a triangulation count.

The actual moments are

\[
V=H^2(H+1)/2,\quad g=(m,0,0),\quad
m=\frac{H(3H+2)}{6(H+1)},\quad
\alpha=\frac{3H+2}{3(H+1)^2},
\]

\[
\Sigma=\operatorname{diag}\left(
\frac{H^2(9H^2+24H+10)}{180(H+1)^2},
\frac{27H^3+45H^2+30H+10}{120(H+1)},
\frac{H^2(3H+5)}{120(H+1)}\right),
\quad T_F=\operatorname{diag}(m^2,1/12,H^2/12).
\]

For the independent mixed test Y=t+y/10−m,

\[
R(H)=\frac{10(3H+2)(900H^4+1200H^3+403H^2+6H+3)}
{3(H+1)^2(1881H^4+5016H^3+2225H^2+120H+30)}.
\]

R(1)=3925/3477, while

\[
R(99/100)=\frac{5757663371300000}{5093493846060783},\quad
R(99/100)-R(1)=\frac{9144065407175575}{5903359367584447497}>0.
\]

The actual logarithmic derivative at s=0 is250777/1819630>0. Exact negative Bernstein coefficients certify R'(H)<0 on the ENTIRE closed interval [99/100,1]; the displayed denominator is positive. Both controls are strictly below3/2. This is an actual ascent control, not a bound counterexample.

The source independently verifies every supporting facet, every genuine edge, the own centroid, covariance, all whole-facet moments, and a positive volume fan at H=1 and99/100. It also checks the zero-edge second-order correction, which here equals−249994/47885. Its sign need not be positive because this control is not stationary.

### 7.2 A zero marked endpoint contributes an indispensable second term

Start with K={t≥0,y≥0,t+y≤1}, ell=y. Perturb to ell=y−s and clip y≥s. Put H=1−s. The actual tetrahedron has vertices

```
(0,s,0), (H,s,0), (0,1,H/2), (0,1,-H/2)
```

and outward cycles `(0,2,3),(1,3,2),(0,1,2),(0,3,1)`, with first face marked. Its actual volume is H³/6, centroid (H/4,s+H/2,0), and

\[
\Sigma=H^2\begin{pmatrix}3/80&-1/40&0\\-1/40&1/20&0\\0&0&1/40\end{pmatrix},
\quad\alpha=3/4,\quad T_F=(5/3)\Sigma.
\]

For Y=t+2y−(5H/4+2s), the strong ratio is IDENTICALLY5/4 and leverage is5/132. At s=0, the formal fixed-support log-second derivative is58/11. The zero-edge bulk correction is−208/11, and the marked-endpoint correction is150/11. Their sum is zero, exactly matching the actual constant ratio. Dropping either boundary term gives the wrong answer. Both s=0 and1/100 receive complete true-hull and whole-facet audits.

### 7.3 Exact failure of a tempting density-stationarity sign shortcut

I tried to make the new equation int_K t(t−f)=0 impossible by giving it a fixed sign on line-stationary one-wing supports. That shortcut fails even with f>0 everywhere and both exact unweighted line reactions.

Both controls have marked edge [−1,1], upper U=(y+1)/3, and far point (t,y)=(1,2). The lower graph is0 on[−1,1], a stem on[1,1+z], and f on[1+z,2].

For z=1/2, stem=(3/5)(y−1), f=(16y²−35y+21)/15, and

\[
\operatorname{Area}K=101/90,\qquad
\int_Kt(t-f)=57949/2835000>0.
\]

For z=9/10, stem=(521/543)(y−1), f=(400y²−819y+581)/543, and

\[
\operatorname{Area}K=16589/16290,\qquad
\int_Kt(t-f)=-20665591267/3362163147000<0.
\]

Both satisfy int_{−1}^2(y+1)(U−f)dy=0 and int_1^{1+z}(y−1)(stem−f)dy=0. These are actual convex supports, but f is NOT asserted to be their actual self-consistent centered parabola. They refute only this premature sign argument, not any moment inequality. The source reconstructs both completely.

### 7.4 Two exact curved lifts for continuation

The six-parameter chart is executed at `(a,u,v,b,B,C)=(-4,-3,3,4,0,1)` and `(-4,-3,3,5,1/5,1)`. These are rational-data convex semialgebraic uniform lifts, not polytopes. The source recovers their full volume covariance, actual centroid, marked whole-facet moments, all density/shape/stem/test residuals, and verifies the strict full marked three-halves gap for each.

The symmetric control has V=3056/5, g=(114155/16044,0,0),

\[
\Sigma=\operatorname{diag}(4365294919/257409936,
8453/4011,2759633/288792),\quad
\alpha=9703175/24515232,
\]

and T_F=diag(13031364025/257409936,1/3,289/12). For the horizontal test y, R=122825/1961952 and L=0.

The asymmetric control has V=320093/300, g=(42218573/4481302,313325/640186,0), alpha=37996715700/102459528649. Its y-centered ratios are

\[
R=\frac{300381554753701826681500}{3980553208943815912264197},\qquad
L=\frac{1070743638084147545438620}{35824978880494343210377773}.
\]

The complete matrices and residuals regenerate from the literal six parameters and source below; they are not unspecified external arrays. Neither fixture satisfies the full stationary system. The generic chart evaluator itself imposes no three-halves acceptance filter.

## 8. Evidence tier and the most useful continuation

The clipping, stationarity, second-order, two-arc, and symmetric-floor arguments are analytical. The computations verify algebraic differentiation, exact boundary corrections, actual finite hulls and moments, the interval ascent certificate, two exact failed-sign probes, and two actual curved controls. They do not verify the universal conjecture by sampling.

The next concentrated problem is the full self-consistent one/two-arc system with the NEW density equalities and boundary Hessian corrections. In the opposite-wing case the density is already forced to U−t; (5.1)–(5.3) and the supplied evaluator contain all exact data needed to continue. A candidate with a nonzero density gradient has an explicit actual clipping ascent; a disjoint zero-edge candidate with a nonnegative quotient-Hessian direction cannot maximize. The remaining one-wing and same-wing-zero-chord alternatives must still be treated, not assumed to reduce to the symmetric class.

No universal determination of R or L, no actual strict counterexample, no global weak-leverage attainment, and no mechanical minimum improvement is claimed.

## 9. Complete source-only recovery and executed pins

The following SINGLE standalone source is the durable computational capsule. Save it as `affine_density_clipping.py`, retaining its final LF. It contains every input, helper, actual hull audit, symbolic identity, and reconstruction rule used for the reported computed findings. It needs CPython3.13.5 and SymPy1.14.0, assertions enabled; there are no optimizer, seed, external file, archive, or old sandbox dependencies.

Run:

```sh
python -B affine_density_clipping.py > affine_density_clipping.log
sha256sum affine_density_clipping.py affine_density_clipping_report.json affine_density_clipping.log
```

Observed terminal output:

```text
ACTUAL_HULLS 6/9/5 6/9/5 4/6/4 4/6/4; WHOLE_FACETS 18
DENSITY_JETS_AND_BOTH_BOUNDARY_CORRECTIONS_PASS
ACTUAL_TWO_WING_CURVED_CONTROLS 2; FULL_MARKED_MOMENTS_PASS
REPORT 42100 fabbce6828d23f6311b4bb56a11fa2a5f7d3b20359571b83211e37d5d740ca57
AFFINE_DENSITY_CLIPPING_STATIONARITY_EXACT_PASS
```

Exact pins:

```text
affine_density_clipping.py: 12669 bytes
04f2d11e49a192e5d9e0cbd0bcd63dda99a5059e9d12bbb1e5a9baa9ddc58c99
affine_density_clipping_report.json: 42100 bytes
fabbce6828d23f6311b4bb56a11fa2a5f7d3b20359571b83211e37d5d740ca57
affine_density_clipping.log: 288 bytes
ebb8430ff1f3db87498ea491acb685f3f8ccf0943dbe248bfba253710ff321b8
```

Normal execution, a fresh directory containing ONLY the standalone source, and a separate losslessly decoded-source execution all completed. The source, report, and stdout were byte-identical across the three runs. This is current-worker exact execution, not a claimed coordinator replay or proof-assistant formalization. The report is an output, never an input.

Convenience copies supplement, but are not needed in place of, the complete inline source: [source and exact outputs](sandbox:/mnt/data/affine_density_clipping_capsule.zip), [standalone source](sandbox:/mnt/data/affine_next/affine_density_clipping.py), [exact report](sandbox:/mnt/data/affine_next/affine_density_clipping_report.json).

```python
"""AFFINE_DENSITY_CLIPPING_STATIONARITY_V1.
Exact algebra and actual controls; Python 3.13.5 / SymPy 1.14.0.
Run with assertions: python -B affine_density_clipping.py
No input files, optimizer, random seed, saved hull or external source.
The arbitrary-convex-support clipping theorem is proved in the handoff.
"""
from pathlib import Path
from itertools import combinations
from math import comb
import hashlib,json
import sympy as S
Q=S.Rational
t,y,h,s=S.symbols('t y h s',real=True)
Z=S.zeros(3,1)

def simp(x):return S.factor(S.cancel(x))
def integ(f,x,a,b):
    p=S.Poly(S.expand(f),x)
    return simp(sum(c*(b**(k[0]+1)-a**(k[0]+1))/(k[0]+1) for k,c in p.terms()))
def derivlog(f):return simp(S.diff(f,s).subs(s,0)/f.subs(s,0))
def hesslog(f):
    return simp(S.diff(f,s,2).subs(s,0)/f.subs(s,0)-derivlog(f)**2)
def bernstein(f,x,a,b):
    u=S.Symbol('u');p=S.Poly(S.expand(f.subs(x,a+(b-a)*u)),u);d=p.degree()
    return [sum(p.nth(i)*Q(comb(k,i),comb(d,i)) for i in range(k+1)) for k in range(d+1)]

def jets():
    V,J,I,B0,B1,B2,A0,At,Ay,Ayy,E0,E1,E2=S.symbols('V J I B0 B1 B2 A0 At Ay Ayy E0 E1 E2',nonzero=True)
    vs=V+s*A0;js=J+s*At;mu=s*Ay/vs
    ii=I+s*Ayy-s*s*Ay*Ay/vs
    b0=B0+s*E0;b1=B1+s*E1-mu*b0
    b2=B2+s*E2-2*mu*(B1+s*E1)+mu*mu*b0
    D=At/J-A0/V-Ayy/I-2*B1*Ay/(B2*V)+E2/B2
    DL=At/J-A0/V-Ayy/I-2*B0*Ay/(B1*V)+2*E1/B1-E0/B0
    assert simp(derivlog(js*b2/(vs*ii))-D)==0
    assert simp(derivlog(js*b1*b1/(vs*b0*ii))-DL)==0
    j=At/J;q=Ayy/I;p=Ay/V;d=(E2-2*p*B1)/B2
    H=-j*j+q*q-d*d+2*p*p*(B0/B2+V/I)-4*p*E1/B2
    assert simp(hesslog((js*b2/(vs*ii)).subs(A0,0))-H)==0
    Hcrit=2*j*(q-j)+2*p*p*(B0/B2+V/I)-4*p*E1/B2
    assert simp(H.subs(E2,B2*(q-j)+2*p*B1)-Hcrit)==0
    return dict(strong_first=D,leverage_first=DL,strong_Hessian_V_fixed=H,
                strong_Hessian_at_stationarity=Hcrit)

def audit(points,faces):
    p=[S.Matrix(x) for x in points];normals=[]
    for f in faces:
        n=(p[f[1]]-p[f[0]]).cross(p[f[2]]-p[f[0]]);b=n.dot(p[f[0]])
        assert n.dot(n)>0
        assert all(b-n.dot(x)==0 if i in f else b-n.dot(x)>0 for i,x in enumerate(p))
        for j in range(len(f)):
            a,c,d=[p[f[(j+k)%len(f)]] for k in range(3)]
            assert n.dot((c-a).cross(d-c))>0
        normals.append((n,b))
    found=set()
    for a,b,c in combinations(range(len(p)),3):
        n=(p[b]-p[a]).cross(p[c]-p[a])
        if n==Z:continue
        val=[n.dot(x-p[a]) for x in p]
        if min(val)>=0 or max(val)<=0:found.add(tuple(i for i,v in enumerate(val) if v==0))
    assert found=={tuple(sorted(f)) for f in faces}
    edges=sorted({tuple(sorted((f[i],f[(i+1)%len(f)]))) for f in faces for i in range(len(f))})
    assert len(p)-len(edges)+len(faces)==2
    assert all(sum(a in f and b in f for f in faces)==2 for a,b in edges)
    o=sum(p,Z)/len(p);V=S.S.Zero;J=Z.copy();M=S.zeros(3);fan=[]
    for f in faces:
        for k in range(1,len(f)-1):
            ids=(f[0],f[k],f[k+1]);v=[o]+[p[i] for i in ids]
            vol=S.Matrix.hstack(*(x-o for x in v[1:])).det()/6;assert vol>0
            z=sum(v,Z);V+=vol;J+=vol*z/4
            M+=vol*(z*z.T+sum((x*x.T for x in v),S.zeros(3)))/20
            fan.append([ids,vol])
    g=J/V;C=M/V-g*g.T
    assert all(C[:k,:k].det()>0 for k in (1,2,3))
    facets=[]
    for f,(n,b) in zip(faces,normals):
        w=S.S.Zero;j=Z.copy();m=S.zeros(3)
        for k in range(1,len(f)-1):
            v=[p[i] for i in (f[0],f[k],f[k+1])];a,c,d=v
            mass=(c-a).cross(d-a).dot(n)/(2*n.dot(n));assert mass>0
            z=sum(v,Z);w+=mass;j+=mass*z/3
            m+=mass*(z*z.T+sum((x*x.T for x in v),S.zeros(3)))/12
        c=j/w-g;T=m/w-g*(j/w).T-(j/w)*g.T+g*g.T
        height=b-n.dot(g);alpha=w*height/V;pole=n/height
        assert height>0 and T*pole==c and pole.dot(c)==1
        facets.append(dict(cycle=f,normal=n,support=b,area_over_normal=w,
                           pole=pole,alpha=alpha,c=c,T=T))
    return dict(vertices=p,faces=facets,edges=edges,volume=V,centroid=g,Sigma=C,positive_fan=fan)

def six_vertex_control():
    w=1+3*t
    def data(H,upper):
        ell=H-t;V=integ(w*ell,t,0,upper);J=integ(t*w*ell,t,0,upper);mu=simp(J/V)
        ct=simp(integ(t*t*w*ell,t,0,upper)/V-mu*mu)
        cy=simp(integ(w**3*ell/12,t,0,upper)/V)
        cz=simp(integ(w*ell**3/12,t,0,upper)/V)
        B0=H;B1=-H*mu;B2=H*(mu*mu+Q(1,1200));I=V*(ct+cy/100)
        R=simp(J*B2/(V*I));L=simp(J*B1*B1/(V*B0*I))
        return V,J,mu,[ct,cy,cz],[B0,B1,B2],I,R,L
    V,J,mu,C,B,I,R,L=data(h,h)
    assert simp(V-h*h*(h+1)/2)==0
    assert R.subs(h,1)==Q(3925,3477)
    assert L.subs(h,1)==Q(15625,13908)
    p=simp(S.diff(R,h)).as_numer_denom()[0]
    bc=bernstein(p,h,Q(99,100),1);assert all(x<0 for x in bc)
    records=[]
    faces=[(3,2,1,0),(0,1,5,4),(2,3,4,5),(0,4,3),(1,2,5)]
    for H in [S.S.One,Q(99,100)]:
        r=1+3*H
        points=[(0,-Q(1,2),-H/2),(0,Q(1,2),-H/2),(0,Q(1,2),H/2),
                (0,-Q(1,2),H/2),(H,-r/2,0),(H,r/2,0)]
        a=audit(points,faces);cv=S.diag(*(x.subs(h,H) for x in C));m=mu.subs(h,H)
        assert a['volume']==V.subs(h,H) and a['centroid']==S.Matrix([m,0,0]) and a['Sigma']==cv
        F=a['faces'][0];T=S.diag(m*m,Q(1,12),H*H/12)
        assert F['T']==T and F['alpha']==m*H/a['volume']
        test=S.Matrix([1,Q(1,10),0])
        ratio=simp(F['alpha']*(test.T*T*test)[0]/(test.T*cv*test)[0])
        assert ratio==R.subs(h,H)<Q(3,2)
        a.update(marked_facet=0,test_linear_part=test,test_constant=-m,
                 R=ratio,L=L.subs(h,H),height_normalization=m)
        records.append(a)
    actual=R.subs(h,1-s);formal=data(1-s,1)[6]
    assert derivlog(actual)==derivlog(formal)==Q(250777,1819630)
    Y=t+y/10-mu.subs(h,1);b=[x.subs(h,1) for x in B]
    Phi=t/J.subs(h,1)-1/V.subs(h,1)-Y*Y/I.subs(h,1)-2*b[1]*Y/(b[2]*V.subs(h,1))
    correction=integ(Phi.subs(t,1),y,-2,2)
    assert simp(hesslog(actual)-hesslog(formal)-correction)==0
    gain=simp(R.subs(h,Q(99,100))-R.subs(h,1));assert gain>0
    return dict(symbolic_volume=V,symbolic_centroid_t=mu,symbolic_covariance=C,
                symbolic_R=R,symbolic_L=L,negative_derivative_Bernstein=bc,
                exact_gain=gain,log_derivative=derivlog(actual),
                formal_log_second=hesslog(formal),actual_log_second=hesslog(actual),
                zero_edge_correction=correction,controls=records)

def triangle_control():
    # Fixed K: t>=0,y>=0,t+y<=1. Density y-s. Actual support clips to y>=s.
    def it(f):return integ(integ(f,t,0,1-y),y,0,1)
    ell=y-s;raw=t+2*y;V=it(ell);J=it(t*ell);A=it(raw*ell);mu=simp(A/V)
    I=simp(it(raw*raw*ell)-A*A/V)
    B=[integ((y-s)*(2*y-mu)**j,y,0,1) for j in range(3)]
    formal=simp(J*B[2]/(V*I));assert derivlog(formal)==0
    assert hesslog(formal)==Q(58,11)
    vv=V.subs(s,0);jj=J.subs(s,0);ii=I.subs(s,0);bb=[simp(x.subs(s,0)) for x in B]
    Y=raw-Q(5,4);Phi=t/jj-1/vv-Y*Y/ii-2*bb[1]*Y/(bb[2]*vv)
    bulk=integ(Phi.subs(y,0),t,0,1);endpoint=Q(25,16)/bb[2]
    assert bulk==Q(-208,11) and endpoint==Q(150,11)
    assert hesslog(formal)+bulk+endpoint==0
    cov0=S.Matrix([[Q(3,80),-Q(1,40),0],[-Q(1,40),Q(1,20),0],[0,0,Q(1,40)]])
    faces=[(0,2,3),(1,3,2),(0,1,2),(0,3,1)];records=[]
    for eps in [S.S.Zero,Q(1,100)]:
        H=1-eps;points=[(0,eps,0),(H,eps,0),(0,1,H/2),(0,1,-H/2)]
        a=audit(points,faces);g=S.Matrix([H/4,eps+H/2,0]);C=H*H*cov0
        assert a['volume']==H**3/6 and a['centroid']==g and a['Sigma']==C
        F=a['faces'][0];assert F['alpha']==Q(3,4) and F['T']==Q(5,3)*C
        test=S.Matrix([1,2,0]);ratio=simp(F['alpha']*(test.T*F['T']*test)[0]/(test.T*C*test)[0])
        assert ratio==Q(5,4)
        a.update(marked_facet=0,test_linear_part=test,test_constant=-(test.T*g)[0],R=ratio,
                 L=Q(5,132),height_normalization=H/4)
        records.append(a)
    return dict(formal_ratio=formal,formal_log_second=Q(58,11),zero_edge_correction=bulk,
                marked_endpoint_correction=endpoint,actual_ratio=Q(5,4),controls=records)

def wing_sign_controls():
    out=[]
    for z in [Q(1,2),Q(9,10)]:
        A=4/(3*(z*z+1));L=(z*z+6*z-1)/(3*(z*z+1))
        B=-(9-z*z)/8;C=(9+z*z)/4-1;f=simp(A*(y*y+2*B*y+C));U=(y+1)/3
        pieces=[(-1,1,S.S.Zero),(1,1+z,L*(y-1)),(1+z,2,f)]
        assert 0<L<1 and S.discriminant(f,y)<0 and f.subs(y,2)==1
        assert simp(f.subs(y,1+z)-L*z)==0
        assert simp(integ((y+1)*(U-f),y,-1,2))==0
        assert simp(integ((y-1)*(L*(y-1)-f),y,1,1+z))==0
        Ft=simp(sum(integ((U**3-low**3)/3-f*(U**2-low**2)/2,y,a,b) for a,b,low in pieces))
        area=simp(sum(integ(U-low,y,a,b) for a,b,low in pieces))
        out.append(dict(join=z,parabola=f,stem=L*(y-1),pieces=pieces,area=area,Ft=Ft,
                        scope='Actual convex uniform support; f is NOT its self-consistent shape Phi.'))
    assert out[0]['Ft']==Q(57949,2835000)>0
    assert out[1]['Ft']==Q(-20665591267,3362163147000)<0
    return out


def two_wing_control(a,u,v,b,B,C):
    # Full six-parameter candidate chart, after scaling the parabola coefficient to one.
    a,u,v,b,B,C=map(S.Rational,(a,u,v,b,B,C))
    assert a<u<-1 and 1<v<b and C>B*B
    f=y*y+2*B*y+C;U=(a+b+2*B)*y+C-a*b
    SL=f.subs(y,u)*(y+1)/(u+1);SR=f.subs(y,v)*(y-1)/(v-1)
    assert S.diff(f,y).subs(y,u)<S.diff(SL,y)
    assert S.diff(SR,y)<S.diff(f,y).subs(y,v)
    pieces=[(a,u,f),(u,-1,SL),(-1,1,S.S.Zero),(1,v,SR),(v,b,f)]
    for lo,hi,L in pieces:
        assert U.subs(y,lo)>=L.subs(y,lo) and U.subs(y,hi)>=L.subs(y,hi)
    def areaint(g):
        return simp(sum(integ(integ(g,t,L,U),y,lo,hi) for lo,hi,L in pieces))
    ell=U-t;V=areaint(ell);J=areaint(t*ell);Jy=areaint(y*ell)
    mt=J/V;my=Jy/V;Y=y-my;I=areaint(ell*Y*Y)
    edge=[integ(U*Y**k,y,-1,1) for k in range(4)]
    eta=edge[1]/edge[2];alpha=mt*edge[0]/V
    phi=t/J-1/V-Y*Y/I-2*eta*Y/V
    factual=simp(mt+(J/I)*Y*Y+2*mt*eta*Y)
    density=[simp(areaint(phi*m)+integ(Y*Y*m.subs(t,0),y,-1,1)/edge[2])
             for m in [S.S.One,t,y]]
    stems=[simp(integ((y+1)*(U-SL)*phi.subs(t,SL),y,u,-1)),
           simp(integ((y-1)*(U-SR)*phi.subs(t,SR),y,1,v))]
    test=simp(areaint(ell*t*Y)/I+mt*eta)
    cov=S.Matrix([[areaint(ell*(t-mt)**2)/V,areaint(ell*(t-mt)*Y)/V,0],
                  [areaint(ell*(t-mt)*Y)/V,I/V,0],[0,0,areaint(ell**3)/(12*V)]])
    T=S.Matrix([[mt*mt,-mt*edge[1]/edge[0],0],
                [-mt*edge[1]/edge[0],edge[2]/edge[0],0],
                [0,0,integ(U**3,y,-1,1)/(12*edge[0])]])
    pole=S.Matrix([-1/mt,0,0]);cf=S.Matrix([-mt,edge[1]/edge[0],0])
    assert T*pole==cf and pole.dot(cf)==1
    gap=Q(3,2)*cov-alpha*T
    return dict(parameters=[a,u,v,b,B,C],parabola=f,upper=U,density=ell,pieces=pieces,
                volume=V,centroid=S.Matrix([mt,my,0]),Sigma=cov,marked_alpha=alpha,
                marked_T=T,marked_c=cf,marked_pole=pole,
                R=simp(J*edge[2]/(V*I)),L=simp(J*edge[1]**2/(V*edge[0]*I)),
                shape_coefficient_residuals=S.Poly(f-factual,y).all_coeffs(),
                density_residuals=density,stem_residuals=stems,test_residual=test,
                full_gap_leading_minors=[simp(gap[:k,:k].det()) for k in (1,2,3)],
                scope='Actual rational-data curved lift, not a polytope or stationary maximum.')

def encode(x):
    if isinstance(x,S.MatrixBase):return [[encode(v) for v in r] for r in x.tolist()]
    if isinstance(x,S.Basic):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def main():
    assert __debug__
    conics=[two_wing_control(-4,-3,3,4,0,1),two_wing_control(-4,-3,3,5,Q(1,5),1)]
    assert all(v>0 for r in conics for v in r['full_gap_leading_minors'])
    report=dict(theorem='AFFINE_DENSITY_CLIPPING_STATIONARITY_V1',
      parent='minimum-0290',
      parent_sha256='a1afff32561b16a73bf7a017e7ad3233330ac76bf67282f7cac952c02cc464a8',
      algebra=jets(),six_vertex=six_vertex_control(),triangle=triangle_control(),
      wing_sign_controls=wing_sign_controls(),
      two_wing_controls=conics,
      scope='Structural theorem and exact nonwinning controls; no universal 3/2 proof or counterexample, no mechanics claim.')
    blob=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    Path('affine_density_clipping_report.json').write_bytes(blob)
    print('ACTUAL_HULLS 6/9/5 6/9/5 4/6/4 4/6/4; WHOLE_FACETS 18')
    print('DENSITY_JETS_AND_BOTH_BOUNDARY_CORRECTIONS_PASS')
    print('ACTUAL_TWO_WING_CURVED_CONTROLS 2; FULL_MARKED_MOMENTS_PASS')
    print('REPORT',len(blob),hashlib.sha256(blob).hexdigest())
    print('AFFINE_DENSITY_CLIPPING_STATIONARITY_EXACT_PASS')
if __name__=='__main__':main()

```
