# minimum-0197

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# OWN_CENTRED_E17_UNIVERSAL_PENTAGON_FACE_REALIZATION_V1

## 1. Main result and scope

**Every strictly convex pentagon in an affine plane not through the origin can be realized EXACTLY as the true polar face at a degree-five vertex of a uniformly filled, own-centred (V,E,F)=(10,17,9) polyhedron.** The realization uses one fixed combinatorial lattice, described below. The five poles need not be replaced by a projectively equivalent pentagon. The general exact construction is real-analytic/existential and need not have rational coordinates.

Moreover, there is a local **seven-dimensional family of own-centred completions with all five actual poles held fixed**. Near the explicit control, all thirteen coordinates of a coplanar pentagon—three for its plane and ten within the plane—can vary, with seven additional completion parameters. This is a full twenty-dimensional local own-centred realization chart for this lattice, not a statement about a canonical registry.

An autonomous rational control realizes the supplied OPEN minimal-four-arrow chamber. Its five poles are obtained from its ONE exact uniform-volume centroid. Every proper subsystem is strictly feasible, whereas the four consecutive true polar arrows are weakly impossible for every common SPD metric. Stronger additional controls make the distinguished degree-five primal vertex **strictly unstable in each of the four proper-subsystem realizations**. Thus the minimality phenomenon survives genuine E17 incidence, homogeneous centring, and this additional apical condition.

A closed actual-centroid cone is also certified: when the five raw side supports are the supplied ones and

`max(|gx|,|gy|) <= (1-gz)/500`,

the minimally infeasible chamber persists. Its effective tangent-metric obstruction is `some D_i < -(3/25)tr(H)`, while every retained arrow under the transported parent subsystem metrics exceeds 1/8. This conditional sector applies to any actual completion satisfying the stated incidence and centroid hypotheses, not just the one control.

**No own110 construction, full U1/S1 feasibility claim, all-orientation family exclusion, whole canonical type exclusion, or new global bound is obtained. The interval remains 34 ≤ C_min ≤ 622.** The new result resolves the realization question that was expressly left open in the supplied local material.

## 2. Evidence read and source authority

Both newly supplied mathematical materials and the complete new journal were read through EOF. The branch switch is respected: the earlier bevel-box remainder is completed and is not reopened. No research connector, unselected archive, or outside source is a dependency of this result.

| Delivered file | Bytes | SHA-256 |
|---|---:|---|
| COPLANAR_POLAR_PATH_TANGENT_REDUCTION_V1.md, [internal-source-reference] | 10759 | e1c694aba308253401e7e57173bce684930ad008b3d037816e1bc1c556cf50ed |
| PENTAGON_MINIMAL_FOUR_ARROW_AND_FIVE_SUPPORT_V1.md, [internal-source-reference] | 10938 | a2b8d8e0d6e06c2a7ece8b2f718c2542c87d571f79719c8c38eba38ae5b541a6 |
| Complete research-journal(20260923-032309).md | 231615 | ad06b0075fd61961d852cfd4386844479e30f58dae6f9344ea1bbf732a79ad76 |

The journal hash is for the delivered file, not its separately displayed internal memory hash. Its complete raw text has 846 logical lines. There is no missing exact dependency.

The pentagon material explicitly marks an initial malformed short code fence as superseded. Only its LAST complete recovery fence was extracted and executed. The resulting `pentagon_joint.py` is 3348 bytes, SHA-256 `2cb253d621a41356871c209332acfc48bb22a7d347ccd7bcdb1d6399232efc02`; its 2489-byte report has SHA-256 `fbf5e8f9d9f71ba4bd6385779443874a7265dabcd8c73eccc9020be9bdf28f7d`. The expected parent marker passed under CPython3.13.5. This recording blemish was not treated as a conflicting mathematical object.

The general realization theorem and the actual controls below are new work. The parent's tangent equivalence, local stress, and proper-subsystem data are mathematical starting points, not previously realized E17 geometry.

## 3. Exact realization of an arbitrary pentagon

### 3.1 A uniquely centred pyramid with the prescribed five poles

An invertible linear change of pole coordinates reduces the prescribed plane to `q_i=(p_i,1)`, with primal apex `A=e3`. Let C=conv(p0,...,p4) be any strictly convex planar pentagon. For s in int C define

`B_s=(C-s)^*={y : (p_i-s)·y<=1 for every i}`,

and `f(s)=Area(B_s)`. In angular coordinates, with h_C the support function,

\[
f(s)=\frac12\int_{S^1}(h_C(u)-s\cdot u)^{-2}\,d\theta,
\]
\[
\nabla f(s)=\int_{S^1}u(h_C(u)-s\cdot u)^{-3}\,d\theta
          =3\int_{B_s}y\,dy,
\]
\[
D^2f(s)=3\int_{S^1}uu^T(h_C(u)-s\cdot u)^{-4}\,d\theta\succ0.
\]

These identities follow directly by radial integration. Also f diverges at the boundary of C. Indeed, if D is the diameter of C, B_s contains the disk of radius 1/D. If `delta=h_C(u)-s·u` tends to zero, it also contains u/delta. The triangle joining that point to the two perpendicular disk points has area `1/(D delta)`. Therefore f has a unique interior minimizer s*, and the TRUE AREA centroid of B_s* is zero.

Set

`b*=(-3s*_x,-3s*_y,-3)`

and form the genuine pyramid

\[
K_0=\{x:q_i\cdot x\le1\ (0\le i<5),\ b_*\cdot x\le1\}.
\]

Its base is parametrized by

\[
x_{xy}=\tfrac43 y,\qquad z=-\tfrac13-s_*\cdot x_{xy},\qquad y\in B_{s_*}.
\]

The parametrization has a constant area Jacobian, so the base's actual area centroid is `(0,0,-1/3)`. Integrating the homothetic pyramid sections gives

`g(K0)=(A+3g(base))/4=0`.

All five lateral facets are true and irredundant; each consecutive pole pair gives a true apex edge. K0 has (6,10,6), with degree-five apex, and its actual poles at its own centroid are EXACTLY the prescribed q_i.

There is no choice of positive vertex masses here. The only centring operation was minimization of the explicitly integrated polar AREA. In fact this is the unique centred pyramid with these side poles and normalized support equations: centroid zero forces the base plane through −A/3, hence its last coefficient is −3; the remaining two coefficients must give the same unique minimizer s*.

### 3.2 The incidence surgery that gives exactly E17

Let `B_i=q_i∩q_(i+1)∩{b·x=1}`, cyclically indexed. Start with the pyramid above and cut off the two NONADJACENT simple base vertices B0 and B2 by sufficiently small planes. Use three independently positive edge fractions at each cut. At B0 the new vertices are

`t0∈B0A`, `cminus∈B0B4`, `cplus∈B0B1`.

At B2 use the analogous three points on B2A, B2B1, B2B3. These are true simple-vertex truncations, each changing the f-vector by `(2,3,1)`. After both cuts the f-vector is **(10,16,8)**. The apex and all five side planes remain unchanged.

There is then a different, deliberately nongeneric cut. The side facet q1 is the strict quadrilateral `A,t0,cplus,B1`. Set

`cnew=(1-delta)cplus+delta cminus`, with delta>0 small,

and cut by the plane through **t0, B1, cnew**, removing cplus. This retains t0 and B1 as existing vertices, replaces cplus by cnew, and creates one new true edge t0B1 and one new triangular facet. It changes `(V,E,F)` by **(0,1,1)**, giving **(10,17,9)**.

For a direct validity proof, use the simple-vertex cone coordinates at cplus with axes

`t0-cplus`, `B1-cplus`, `cminus-cplus`.

The new plane is `alpha+beta+gamma/delta=1`; retain the side ≥1. The apex lies in gamma=0 but has alpha+beta>1 by strict convexity of the old quadrilateral. All other old vertices outside that side plane have gamma>0, and remain strictly retained for sufficiently small delta. The exact finite sufficient restriction is `delta<gamma/(1-alpha-beta)` whenever the denominator is positive, together with delta<1. Thus there is no unsupported generic-cut assertion and no diagonal silently promoted to an edge.

A generic THIRD simple-vertex truncation would instead produce (12,19,9). The cut through two existing vertices is the reason the construction hits the requested E17 layer.

### 3.3 Repair the ACTUAL centroid while fixing the five poles

Let the three coefficients of the base plane b vary coherently with the six edge fractions and delta. Every vertex in the construction is a rational analytic function of these parameters near a nondegenerate pyramid. A fixed oriented boundary triangulation gives analytic volume and first moments even at zero-cut limits: cells that collapse contribute zero, rather than becoming extra facets.

At the centred pyramid, with the five side planes held fixed, differentiating the actual base boundary gives

\[
D_b g=-\frac{Area(F_b)}{Vol(K_0)\,\|b\|}\,T_b,\qquad
T_b=\mathbb E_{F_b}[xx^T]\succ0.
\]

Indeed, the normal velocity is `-(delta b·x)/||b||`; differentiating the first volume moment gives the displayed matrix because g=0. T_b is positive definite: a nonzero linear functional cannot vanish on an open subset of a plane not through the origin.

The implicit-function theorem therefore repairs all THREE actual centroid coordinates by varying b, without moving any of the five side planes. One can first choose small positive truncations and repair the centroid at delta=0; invertibility persists. Then turn on sufficiently small positive delta and repair again. The finite strict incidence inequalities above persist under that coherent base adjustment. This avoids presuming a uniform valid ratio between two vanishing cut sizes.

The resulting E17 body has actual uniform centroid zero and the exact original q_i. Undoing the initial linear normalization proves the theorem for any prescribed affine plane not through the origin.

The same surgery and centring argument also works for an n-gonal pole face, n≥4, with f-vector `(n+5,2n+7,n+4)`, using cyclic neighbors at the two truncated vertices. The explicitly computed control in this handoff is n=5 only; the general count follows from the two truncations and the through-two-vertices cut just proved.

### 3.4 How much freedom remains

The six edge fractions and delta are seven independent completion parameters. Before centring, the base plane supplies three more. They are locally recoverable from the final facet configuration: the removed point cplus is the intersection of the base, the first truncation plane, and q1, even though it is no longer a vertex. The other fractions and delta are then recovered from their specified edge segments. The two new degree-four incidences say precisely that the last cut plane passes through B1 and t0.

Thus with the five poles fixed there are ten local realization parameters, and the full-rank actual centroid map removes exactly three: **a seven-dimensional completion fibre**. Allowing the coplanar pentagon to vary adds thirteen parameters. The final own-centred chart has dimension20; no local equation restricts the four affine shape moduli of a pentagon.

These exact fixed-pole completions are real; rationality of every completion is not claimed. Rational input planes and fractions are dense in the uncentred chart, however, and actual volume centring of a rational polytope is rational. Consequently any OPEN pentagonal chamber realized by the theorem also contains rational own-centred E17 examples. The next section gives one explicitly, rather than relying only on that density argument. No uniform numerical cut radius over all convex pentagons is asserted.

## 4. Complete rational actual control

Use the supplied planar pentagon

```
p0=(0,0), p1=(2,0), p2=(2,4), p3=(-2,5), p4=(-3,3).
```

Choose the rational base parameter `s=(-1/12,23/9)`, all six truncation fractions equal to1/4, and delta=1/4. **This s is not asserted to equal s*.** We compute the new centroid exactly and account for its effect on every pole.

The ten RAW vertices are

```
0=(0,0,1)
1=(16/25,0,-7/25)
2=(-48/113,24/113,-103/113)
3=(-48/89,-48/89,1)
4=(0,-9/23,1)
5=(-12/89,-1077/2047,1)
6=(192/2225,-870/2047,19/25)
7=(36/283,144/283,-365/283)
8=(2032/7075,144/283,-11389/7075)
9=(672/31979,17970/31979,-56527/31979).
```

The nine raw normalized support vectors n_f, with `n_f·Y<=1`, are

```
n0=(0,0,1)       n1=(2,0,1)       n2=(2,4,1)
n3=(-2,5,1)      n4=(-3,3,1)
n5=(1/4,-23/3,-3)
n6=(46/41,-46/41,23/41)
n7=(566/1579,3679/1579,283/1579)
n8=(167/88,-46/77,59/77).
```

The actual uniform volume and centroid are

```
V=123666516/327305065,
g=(-1680051656893/1222121891838875,
   -105667341927/59176428446935,
    191281237573/27463413299750).
```

Define `X_i=Y_i-g` ONCE. Its actual same-origin poles are, exactly,

`q_f=n_f/(1-n_f·g)`.

The source checks this relation against every incident equality and nonincident strict support inequality. It independently reconstructs the ten vertices from all triples of the nine raw support planes.

The full outward maximal-facet cycles are

```
F0=(0,3,5,4)       F1=(0,4,1)       F2=(0,1,8,7)
F3=(0,7,9,2)       F4=(0,2,3)       F5=(1,6,5,3,2,9,8)
F6=(4,5,6)         F7=(7,8,9)       F8=(1,4,6).
```

The seventeen true edges are

```
01,02,03,04,07,14,16,18,23,29,35,45,46,56,78,79,89.
```

The degree sequence is `(5,4,3,3,4,3,3,3,3,3)`. The source exhausts supporting triples and merges coplanar triangles into the displayed maximal facets. Volume, first moment, and covariance agree between an interior-origin fan and an apex-0 fan, including flat selected cells. After centring, a fresh fan has exactly zero first moment.

The same-origin polar has (9,17,10). Its full maximal-face lattice is checked against primal vertex stars. In particular `(q0,q1,q2,q3,q4)` is its ENTIRE true pentagonal face at X0, not a five-point subset of a larger face. The four selected polar arrows correspond respectively to the genuine primal edges **04,01,07,02**; the unselected closing polar edge corresponds to03.

This is a nonpyramid E17 body with a heptagonal facet, not the six-vertex pyramid used in the existence proof.

## 5. Exact recentering and a closed obstruction chamber

Set

\[
h_0=1-g_z,\qquad t=(g_x,g_y)/h_0,\qquad
h_i(t)=1-p_i\cdot t,\qquad \widehat p_i=p_i/h_i(t).
\]

Then

\[
q_i=L_g(\widehat p_i,1),\qquad
L_g=\frac1{h_0}\begin{pmatrix}1&0&0\\0&1&0\\t_x&t_y&1\end{pmatrix}.
\]

This is the exact projective change of planar pole shape induced by the true centroid, followed by a common linear embedding. It is NOT an assertion that ordinary recentering preserves the affine shape of a polar face.

For the rational body,

```
tx=-3360103313786/2427219753533753,
ty=-100383974830650/55826054331276319,
```

so both absolute values are less than1/500.

For any t in that complete closed square define `e_i=phat_(i+1)-phat_i`, i=0,...,3. For the index triples (0,1,3) and (0,2,3), define positive circuits by

`r_i=cross(e_j,e_k), r_j=cross(e_k,e_i), r_k=cross(e_i,e_j)`,

with the unused coefficient zero. Set `lambda=r013/2+r023` and

\[
Q(t)=-\sum_{i=0}^3\lambda_i\,sym(\widehat p_i e_i^T).
\]

An exact rational interval certificate on a16×16 CLOSED grid proves throughout `|tx|,|ty|<=1/500`:

```
all hi>0; all four lambda_i>0; sum lambda_i<25;
all fifteen strict polygon convexity determinants>0;
Q(t)-3I2 is positive definite;
every one of the twelve retained arrows under the four parent Nj exceeds1/8.
```

There are39 guards per cell and **9984 strictly positive rational lower bounds**. The source evaluates sums, products, and reciprocals by exact enclosing interval arithmetic; repeated-variable dependence is conservatively retained, not numerically optimized away. All256 cells are used, without pruning. Their shared boundaries and the square's outer boundary are included. The smallest shifted guard lower bound is

`214389375166539/46614261955531688 >0`.

This certifies a continuum, not256 sampled pentagons. The cells, exact lower bounds and all underlying formulas regenerate from the capsule.

At t=0, lambda=(11,2,4,6) and Q=[[20,23],[23,44]], recovering the supplied local example. At the actual rational centroid, exact checks additionally give `19<Q00<20`, `307<det Q<308`, and every retained parent-metric arrow exceeds3/5.

For any physical N≻0, put `H=(L_g^T N L_g)_(1:2,1:2)≻0`. The exact same-origin stress is

\[
\sum_i\lambda_i\,sym\{q_i(q_{i+1}-q_i)^T\}
=-L_g\begin{pmatrix}Q(t)&0\\0&0\end{pmatrix}L_g^T.
\]

Consequently

\[
\sum_i\lambda_iD_i=-tr(HQ(t))<-3tr(H),
\]

and some selected arrow satisfies **`D_i<-(3/25)tr(H)`**. Thus all four WEAK arrows are impossible, including every finite weak-arrow wall. The certificate is nonzero rank-two NSD in three dimensions. It does not exclude a singular rank-one metric supported only in the unused normal direction; physical SPD is essential.

The same proof applies to ANY actual completion with these five raw support planes, their true cyclic incidences, and the displayed actual-centroid cone. No additional constraints on the other facets, fitted masses, or independently centred polar are substituted.

## 6. Physical strict proper-subsystem controls

The four original chart matrices are retained literally:

```
N0=((1,0,-20),(0,1,1),(-20,1,402))
N1=((2,-2,2),(-2,4,-19),(2,-19,147))
N2=((12,0,1),(0,2,1),(1,1,1))
N3=((1,0,1),(0,1,9),(1,9,83)).
```

Nj omits arrow j. For the ACTUAL body use

`N_actual,j=L_g^-T Nj L_g^-1`, `M_actual,j=N_actual,j^-1`.

Each is a genuine global physical metric pair on the same uniformly filled body. The retained arrows equal their chart evaluations exactly, not approximately. Every proper selected subset is included in one of these strictly feasible three-arrow subsystems.

| Omitted arrow | Actual strict (S,U,H) | Zero primitives | Physical weak points |
|---:|---:|---:|---:|
| 0 | (2,2,2) | 0 | 0 |
| 1 | (3,2,3) | 0 | 0 |
| 2 | (3,2,3) | 1 harmless | 0 |
| 3 | (2,2,2) | 0 | 0 |

The harmless zero for original N2 is the unselected polar0→4 primitive on true edge03; a positive primal primitive prevents a physical weak packet. It is not silently counted as a nonzero primitive. The additional exact chart perturbation

`N2sharp=N2+(e1e3^T+e3e1^T)/1000`

has leading minors `(12,24,4997999/500000)`, retains the same strict323 census and the required three positive arrows, and has ALL68 primitives nonzero. It too is preserved. With the Euclidean pair M=N=I the actual control has strict536, weak000, all68 primitives nonzero.

### Stronger controls: the degree-five vertex is itself strict U

For each omitted arrow choose the following planar SPD H and an interior point f of the ACTUAL phat pentagon:

| Omit | H | f | Actual strict (S,U,H) |
|---:|---|---|---:|
| 0 | ((1,1/100),(1/100,1/10)) | (35/18,1/600) | (2,5,5) |
| 1 | ((1,-1/2),(-1/2,17/64)) | (31/25,149/60) | (2,4,4) |
| 2 | ((1,1/4),(1/4,5/64)) | (-1,8/3) | (3,3,4) |
| 3 | ((1,1/4),(1/4,65/16)) | (-1/20,2/25) | (2,3,3) |

Define, without omitted normal parameters,

\[
\widehat N=\begin{pmatrix}H&-Hf\\-f^TH&1+f^THf\end{pmatrix},\qquad
N=L_g^{-T}\widehat N L_g^{-1},\quad M=N^{-1}.
\]

The Schur complement is exactly1. The leading principal minors of the four chart matrices are respectively `(1,999/10000,999/10000)`, `(1,1/64,1/64)`, `(1,1/64,1/64)`, and `(1,4,4)`.

Every retained selected arrow is strictly positive, every f is strictly inside the true pentagon, and **X0 is strict U in all four full physical censuses**. All68 primitives are nonzero in each case. The exact arrow values, interior determinants, both metrics and complete censuses are in the reconstructed report.

The apical conclusion has a direct geometric proof: `Nhat^-1 e3=(f,1)`. Thus M X0 is in the interior of the cone generated by its five actual incident poles. Every actual outgoing primal edge has strictly negative pairing with that vector. No separate metric is used to impose apical instability.

These stronger four controls establish actual minimality even after adding this true-vertex condition. They do NOT have U=1, and the closed centroid cone in Section5 is not being claimed to preserve these four additional apical metrics at every point of the cone; their asserted robustness is local around the rational control.

## 7. A verified full-rank actual-centroid actuator at the rational control

The existential construction used a small-cut limit. There is also an exact rank certificate at the moderate fractions1/4 of the explicit body.

Vary the three coefficients of the raw base plane b, keeping the five side planes fixed and reconstructing all cut vertices with the six fixed fractions and delta. For each original base vertex,

`B_i=C_i^-1 1`, with rows `C_i=(q_i,q_(i+1),b)`,

so its exact derivative is

`D_b B_i=-(C_i^-1 e3) B_i^T`.

The derivatives of every new vertex are the specified affine combinations. Differentiate the actual oriented tetrahedral volume and first-moment sums, then use

`Dg=(DJ-g DV)/V`.

The resulting exact determinant is

```
-12518845279599059476099243208047046079/
 54283062336634823333455281277967884062500,
```

strictly between −1/4000 and −1/5000. The complete3×3 Jacobian, all ten vertex derivative matrices, and the differentiated actual moments regenerate from the source.

Therefore the seven completion parameters near THIS rational example can vary while solving `g(b,parameters)=g_main`. Subtract the CONSTANT g_main, rather than an independently chosen polar centre: all five actual poles remain exactly fixed. The implicit function theorem yields a genuine seven-dimensional own-centred fibre. All nonzero incidence and apical-witness signs persist on a sufficiently small open neighborhood. This provides actual local completion freedom at the supplied control, not just formal dimension counting at a collapsed pyramid.

## 8. Selected-tree relevance, limitations, and continuation

A literal topological polar spanning tree containing the forbidden path has rootF4 and parents

`(1,2,3,4,4,0,0,2,1)`.

Its selected edges are `01,05,06,12,18,23,27,34` in FACET labels. The complementary true primal tree has edges

`03,16,18,23,29,46,56,79,89` in VERTEX labels.

Both spanning-tree and complement properties are verified exactly. This is a **topological selected domain whose physical sign feasibility is excluded**, not a purported feasible complete continuation. No arbitrary S1/U1 candidate is asserted to contain that orientation, and the feasibility of unrelated complete trees is not decided.

The two consecutive quadrilateral windows, and indeed all proper three-arrow subsets, can therefore pass on actual homogeneous E17 geometry while the four-arrow pentagonal path fails. Checking only the separate elementary circuits or the two three-arrow windows is genuinely incomplete in the actual setting, not merely in an abstract planar relaxation. The original source had established that failure only locally.

The successful route was to separate exact prescribed-face realization from rational chamber realization. The first uses an actual polar-area centroid and a base-plane volume-centroid actuator. The second chooses moderate rational cuts, recomputes the true centroid, and proves that its projectively changed pole polygon remains in a certified chamber. Naively retaining the old polygon after recentering would have been wrong; three generic simple cuts would also have given the wrong f-vector. Neither shortcut is used.

Exact tangent-halfplane probes helped choose the additional small rational H/f data. The final source takes those literal inputs and verifies every actual assertion directly; no numerical feasibility result, failed probe, or optimization trajectory is used as proof. The original harmless-zero metric, its strict perturbation, the Euclidean control, and all four apical proper-subsystem controls are retained rather than discarded as nonwinners.

The unresolved global condition is now clear: **own-volume centring and E17 incidence alone do not prevent this local obstruction chamber**. To turn the gate into a global lower exclusion requires a necessary selected orientation, additional high-pair or common-metric conditions, or a coverage theorem over actual E17 incidences. The general five-versus-four support sharpness question remains the coordinator's separate direction. No part of this result supplies an own110 body or changes a global count.

A concrete continuation is to use the full twenty-dimensional local chart—thirteen freely prescribed face coordinates and seven actual completion parameters—to impose genuinely global sign conditions while keeping the minimal four-arrow mechanism explicit. The branch no longer needs an unproved claim that its pentagon can be realized at a homogeneous centroid.

## 9. Complete source-only recovery

The following lossless capsule contains the entire **18130-byte `pentagon_e17.py`**: every literal vertex/support construction, true maximal-hull and edge check, two actual moment fans and covariance audit, same-origin polar hull, both circuit and stress formulas, all9984 interval guards, all physical metrics and68-primitive censuses, the exact actual-centroid Jacobian, and the topological complement check. It needs no parent source, old report, library object, external solver, RNG, or network request.

The universal realization and parameter-freedom theorems are proved analytically above. The source verifies the rational control, the complete closed centroid-cone certificate, and the actual Jacobian; it does not pretend to enumerate arbitrary pentagons or formalize the implicit-function theorem.

Executed environment: CPython3.13.5 standard library, assertions enabled; transport decoder zlib1.3.1. Original build/check and a separate source-only cold decode/build/check completed. Their report and stdout bytes matched exactly. The capsule was also extracted from the serialized handoff and decoded to the exact source. This is a source-only cold rebuild, not proof-assistant formalization or an independent mathematical referee.

Save the capsule as `recover_pentagon_e17.py` with its final newline and run

```sh
python -B -S recover_pentagon_e17.py fresh
cd fresh
python -B -S pentagon_e17.py build > build.stdout
python -B -S pentagon_e17.py check > check.stdout
cmp build.stdout check.stdout
```

| Object | Bytes | SHA-256 |
|---|---:|---|
| recover_pentagon_e17.py | 9918 | fdbcf433e9ed4b00179ab814bd9c37a163434e9cd45b56b0cc680280909e89e6 |
| decoded pentagon_e17.py | 18130 | cdf46290aadcf61f5127120a0e267d62c7041d227c047194f3fd86d775043f01 |
| pentagon_e17.json | 642186 | 4508e04c39162e00d5a3b50f4eabdab7504b20e9ab9e6e0b5e8c8145520d5517 |
| identical build/check stdout | 511 | 0c55344bd4186a5de10783db236264eefbc5d1e7b3c2969ffb195dae01739af5 |

Expected terminal output:


[Encoded source block omitted; the code in this passage is incomplete.]


Complete capsule:

```python
#!/usr/bin/env python3
"""Complete source-only recovery of the actual E17 pentagonal-face controls.
CPython 3.13.5 standard library. Usage: python -B -S recover_pentagon_e17.py fresh
"""
import base64
import hashlib
from pathlib import Path
import sys
import zlib

PAYLOAD = """
c-p-@YjfK;lHc_!nBBS)X+yRs`4LOT)O!3#oONu+b}~DoQ?V$Lk|;|gO;U=K+5GqGZU7`G$(d}`)lF(d5RV4B(dZ}WzrWd^XX*YR
jP`?QVI-@397pZi-~RTuGcTXJQzQNwHM}6o(>U~vOZ(VJ19uvJbMr8cjCg3c#w?7&8T1^+^R(fnY5dhl;;EY&2@G>bakN)EzbCjx
d(Up~9U58gM!uW+#xxwHZo29k!P50|BPFN+DvXkOZa^nv5v1WT^yGBWbhTIeoVlZ*BbRD4el;48#Z*pUAMYhAV=xb={=dC(;5{QQ
wP701jA06s0G!MSXGxsq#+9rv+|0NVeZo9Q^EjRseY|)E#G&~!W+Z9s&%IpqP27A87^t52@LH4Qv72F&dYxo(q{`VUtJUs#K2N5B
DSl^eVqUStvVev_HbCDn%_eJF%xuZu1Nd#U*dadJtZi9V?c?Rs!}a-N1(FUgmGDx87m0F2uxkL`W=+;;A@C-%nN8rabkJ;B7Q-Gb
XlE@k?*VJrC$tcFGW+0I_OW4oG`PuH^t1_>Y%JPrc0z3@>@6<csy*J{UEe-&^U7>Mf0*RTY_*{iw0yq5zk7I6XeGPQ2Y_g#xwm!^
1E@x-0E8A21PcJ0LH)rIJFuyuC_$G4xvVSm@aTxyhsP(_&^|goDPCG{+oDWh?4x7$_N{_*e2k^T6D+_o&woGXxJPYvNPE)+5-D8Y
vSTV81HLUun>Nmk|C!i+f;BMm2wD&1^BC*t{Rk;o`va*1`(y32YuA-czA{73CxRjqq)6&Uqrhy-{SGTtwVEHmDfNBRWdo~|2KhXV
3;}4lyP^?Gw!$&r!h||mG$fl3whd|gXo%-R7nkMhgLZN;2#2_$uOH_X@Y#F@{eA%4OXDo73^CoF-QOAXTK$F#KTxv!OqQBh*A%Tx
mTauEMXLt0RROxCuUKyY>$N&HBODsjAc8XIwmt|u>W!_n#vOzw;5P9o-f@uZM-+hyCNWjmNc{5@=daKe3AE$N_StO9c8OnvoH9?a
ho?xpGtdQu+?Lq_pe)y*i1EwK-eI&5MDe+xPuI;d5TJ%%V5P6agwt;A?3m&1#Ikm9gx>1*(tgkDmy1+9j8ygB@KBpyZ%W_5VX*f7
pF9u5sPS|WRLBK*3uK^<y2NwP1g}z5aVqiYz}n#M+4cj6wJFOaA}rhF^4V)=NYtlLzp)G1s=D<O2Cbn)gNfpR0mCp9o-H{gfSZ{!
rb7^i6KFCk7Zyfwnr*P)<|c;y-lV_27tfn}0ac>zxvaC9I6b?zoHg+Ue@V7-Ij3V#GiJP4km5P0FlW{;&4Tr2LiUa4)2X>cC}0U(
F30XX11&sHP#cHQ2o6>VD+lF13(`>lTel>0#*34w8-W=!biE*l<~a3(6nf7C!&`YUVh=3~BjUK`rPZZ={Lk+-fhn6X!b~?HOo3)(
fj)rs7=Qsx#l?X~fx86Su_e&ZV&e5#z5>d~>v919qvOR9tbQIq{g~r^i6+szn~iu+t6W))amlaCz5oW8n%M{_MwS+m58h6jI_Pky
>VM(Qj+|Yvmjn$bx;y5LF-_U{MzegwS+WsL<7Y~DQB%&SF^J|sZ8r}PG|uvk^QOcR$qB<ighrjz4YR;FqYVZEUV?R*n)TZlfWfXB
emD!FjBLg_j;1Z>!Qehu>l;Hoa6a$#<-YhCE8A$Hzz2bE(%3z)|7MwK(eAkZg#Q_Kdi|1hVf1&LM{MxM_9E~WjWx2$2K>wpYo`I=
ASIq*zjLzKU@{BIS!@XI8uX?u#65$x0+2m70ZZ67CvYgBVp3FuNF8;E;5ZaYisp1lnD~>ug*%-Gh(7cN9_Kxr3-^Ly0YR#YJ}u|#
IGhH?6C4S`Ia=mC3YNLrYYDaopn46v-^bPGZ#cbzUX%FXD5`7rI|J}8p0Qr871|UHphp+}R~SKyhEoP&2pRz+Ea3tLFTJt_I2){o
iBhv)YzDrzDh(D=7gt2|khQzhFawnsfOnDs>kzn(IHbU9YKc-L;<{MDaaK)Vv$Z#mfOE_p6W@ktm=NhuwIV1>Vx;7TRR}j|6yh!L
N3dl=NFnP5g$R0P!|GWpJBe*)1Eqk5Y={`_4tpKDZ*_t_m=u7!^QjW=@{|ZwWwBo0QfNMxC@I!j6s)zN73hqmR7~jQ3TRLqJ87;C
U6813n6VfayNIWN0Y_`NJB#7O=lqXu7J!)Yxzu&n;3jpwU^>l;gFXy5&@WM+tm~Yi1%izB84zS1H}OoC=bp9(Xf&apU0dw6u^_X@
6sB@4m}sC19u&YXInvm90aBF4!Ar)?n9*b)uBD7bBX|W8p_J9sb3;$I#q={NiZiy@KcJeN3oV~9Ist2NIyon!AeXkl3KWCDgDAYq
7mB{vOBC76Drk+hqRb@SbC?;NNCHCSFL)owzezN<&^SO$%H%W>E&&ltkh));LF}*0gx|A_3zw0h6VH|NXYCv@KbYn&7ZtdJFOrsS
#d9PPm%!u$4u0ZJhAX2d7}>&egeEr&)JBkjXubdwu$LYfthV)Ehkdl7B+#AqhCy>kXIpx0@(1l0P-tnwr|xXvyXe}myhDT}0xp@|
$bnzz1)8vb&}6}k1qlmUET6GF;fQq2Sn?k53oH^BP0zM`9`qSbV$us>=CS~$uT-gi!AyFho2>vfNc3SXg49~8QhoE;wgy;Io}hAw
r#@fyj{05v;nWeTK(YcIY0s=RA7N=R5(+Ao!xPx`jG%J-p^}3}8N4%Zo;yWAhX}+5Adja-C8tRk%;_NW2g@T4W#tdg{V)gO2g@Yz
Km>8rVaPqebX*#Y<jtuLC>jQ<3=O<t8h-<;L&@vTu$0&^`g>I=(HM}1`Y27rpZ|W218~+Jb?xc>`jw6-*OZ{ZnJd#;T|h#rf~*wC
!ZdB*Bk-+Vl5}WUwJIWe48{Zkb6CX23LrD;PvZcKP?HCvRL0=aa0ESOXhaVJYD&X6t#43E!q>f*h}rvNYjY~jRn!M*0fGQF4A3D3
sjMwOd&QVOQN}bFL%Af60#}jY(kc*UbWRREjIeZb*I03J@}WUH>2eg33Jr=E5SypmCde-cSxtw&kzD*99`TiCp_FJ5UdUd<CNC7-
AK*XO<?9kTOF1^fX0Oxkb3U~33HlIRi=2zvZlPJ4-H}uW6Cm@#>Mp%Ps|-N2j4aIqz}Y=9ohPSPlc9mb`GS0cA(~0xZPbA93nBjt
!H;t&H6YZ<2<AY4p!CQ@>kw@!>JN5ayy${c2M?<h)g^bB;|7^*0Lj|ID6iQyrD6|7=%{R4dR9jTC2;T1-d<ts26vSB0@!v6PKMTc
YS(~0Mw(KljseXOP|@EI|Kg}w)@uhrc3|=>GI<tZDW=_I_AxurxCLkD<{>*^ZTKgC>7TW6vQScF=s^6pEGliaO+f+BKb!2}JA+@F
evj$5MZfLu2;QHAk4G}_#p?R6h#c$$t%cC>N$ON^eGxeN3Rz!bdxFT?O|APY!Vw01uSm}4SGT|1%nhtzCQT-nzzUjR*B`8)>Nr)6
VX$!ou`K}xaNTMZ5V=IqfCJ1Laa>2MG}jDc)L5YxWDaVEB~z~)POG$r7ffYk_=v%Aa?{X_yZ{dv6Lvm_a}86|{>VMVt-yCj_E5E@
eGaO5lm@uWV8oIb*Y<)?gxH615egnq@<OMI3L7gB8wIz-OzK-$Yc|K|?F>&U2mr7uBaRWbSt%_r3Kao|T%)Pu_Ua1jdcXUE@3b6v
0j7gD!VBMq>P^mG2N9X1;SBtsF7Yxv6W4n#JOlEk!8%2eDE*(nXTgw!2#)MQhd!5aF?0l2)pNJH)N8^*t=B~L3j6d{?0XL;lKmnu
CWoTmOK;StH-JXHMr^3{8mV5xKD`k%*d<_<Vuh?&1uN!Z1uTn@R`xg!1rS;84yMY;4Y!G~7t2z*4#u1c!+>bT7L=JIoRq_cU5A{9
xV(Av*U*=L2_13T20a7iQ^1yzm?hf&A-0wZYbD^d!=SH$`~34mL<s6zkj7wlg3!m9RGD_d&Si8f5po_437n*(*;|4N!q`$Y5hj?x
L6~3qY5&M)?3PC$C0##^Mve$=aylkV5>-4{L1a~60w}DQo_JPqL5?`~SY(KigLDn^Z~>KsA=4^kstu{ZvTy|U)jSQjsUgEE$S@5V
<+4v>P~wj7=B}CJK^jY_HYxN(#jRxq4^C)OQT_=i|8KI32od5Q-HU)ppcyhr(gTqTyr1AnT<5U^@-N+$9_~}=R2!3UG8solJ>@-g
)A~CH(s+1gVO6uB$=FF@A}%vU0R|U)<}(WYb|3sD_1>a)i){IoI&@;yDfxizOd<j8m;eg<`>kCp+x?1_s^Rfc8noiKfm{iYz)IOc
LOkQpodBPc{;sH)$O<6Nerr8$aA0j@4O^R$c}xr#$;;~**aW$sGX0h1Nl}=*D2a(B+N&3mnp=>hsu@<vY&M?sDKMg9N=bLQ^MxZW
cAv@WiK^IQ@~q=~NC$qRMOF(HUOkjRdQgT@JVSp2kK-8hA-FqmE)ynBSHNHcvvOZ8_B9AcW9R~##6EG{K=w7vqae#1qF2W00SY@>
1j{gAITBm(fV1RHL6jKR=vIM51U7Y`OPptp!_E3MuCw|$#8@|;ImZd3Fn1g<0;fYZjoCQlw{ZlHELQAIV}4~$V~pRx8??z<B)}Mm
lo{ArSie{1I4m@=?03rLz?$(7IQgK9XF)!WeKGko9HJYe(m_iy!Lkr#1lS?q#wZ*tF@t&~*GH@#B#2r(<!3<ci>U?Zt^{3-l<V4E
!Vi;cgO@Qzw;eE*5FD3a)f`bUl5-SGE#NgI4Azj4i<JRmX)9AHYIxmk=qps+(^vbeo?@KpKbuc~h<L&kt~({J^a6{Oi{8<xKrNdD
!)Sd1UK*)4K_r@*%O$AwU{cEu7e8E+<c+0T2RNJ>o;$^y_CBo=9~wc^%_+7}X`hHBEXJ`r8-P<Of--(M&nU)s*leQZXdiXyG!<fA
BxB_DoHEUp21x)yRODm^@jNQhQD#Fx-EHlN!p`%4#5O8P)bB@H1eUBv6!cTB>pTKl5Mf8=gekx-<^?<N6QB0#pU^(V=)(&)KZ&aW
jkdJ|WpO>AZ8bj08v>uy4FM2LFPw4?06-T?^}e;M>ZR<_tJcK~w)Kih87_jg4ux9L0mvzhU2gQSp(4WSebg^$zk&Pl*4orD>uLG}
61mTBc#3eRpf!3+DTaO|Fs{s{mRN`7^h;L^85;muzcd-{2UG8)fMJbF1Cu1jm@*eezhnXN0C}E~1?0fcAayGILC~s!Gz5%U$(^WX
{N1<;m*DM<($Ggq>PGSon>UR!sHb2LGk|hqP&L4q^9Xaz7*xr|ZVElVf)R|ii8q~t+qhR%K9b|bgW)7j1O}qWa7cZFt6`(LoBECi
E6>ShrFEjKv<0(zU*8%UPIvd_luS3jRU1oN_XqH#@s|KbQSQ)vJ36tIvr$IGb%JXAh9MA};VrWxi%2An2~?Xcu-DLR!wXyoYs1&L
61z7J@FLbR#TW1@RpX?^Y`TO+ci2wEO*gOrkD$8II<{m;Dbh@k4%ppMX$(wjg$qmWwli_PcmU2ec(Zg*F)OYX;QsqT8ZKO<mAJ?f
j{~F)B^MeLyf$Vr#xEIqLB<d}W}zP#)CN>Xwh}iB5-#8a`DI9)JYjkFr(%{#pQJk|hLpi_7(_92y#-~^WT1)9Mb+@dKH3chCk?VB
jsS?fC$l9pLaC8T<^vDoWT1{>B~-WumMui!a9gfKk2=b1$?PxEB?{9@jsVEumo%uP3ZMynB0ZT1dTYshSj#4KuMB?M^s90$6TBKm
zEzoQ5p|+dk!UfhO?sAPLf6v-j8>&ibSzRVMP-p*@yoOd6`3zGE7n@@1S3d*-^CZ@?6kWVA9(K%5nR<%iv8{vkz@UU0pB792C!6I
<tMVIc;90)@7G;`$X^e}_q!S88S(!Gj#%_4MTl44x{G*9xz&YCpnloqPz6iF-XB<z_l&3e2Ud~ltfWY3J%$fc%d1Mb0=#1;^Q-AA
SH*B?awseUg=%@p$zK2fy2ikHD%8}Xm-ox-4h6g|m(?UHhF{|C6XL$W+!v@{e1R42a-5yIUwnXf8bKviCJ!^_3j#=b_ys{qLHUIf
H&D>9-WLjpI)4BY?TbaNO0<zwa6P<ZrTgaSWr?Zf<urW+qvgWsM`&B})OeC6w3Pt4ydOAu!<$u=Cj^$8y5M94DQ5VTz%4~82N-Cz
1SuLopz{2QJY(uVfv7%2U~=)rV#6@aa!2HwxAgd6si0=rrj)I}EN;>!Au2Yhd;*MV3b&Bmgi;Y)#q(5J17MIQK?(-eAX{a5Ff#zT
H1sltH*!O9+kLt+X701Ni8c=mv4*CRVaMF~EObGZ1YU6w9*!7bZJI&@pc!U^SuAqXRFrj=sB0fG`>m)uYEorobc3z}GE<hY-!VHn
P=lfFkSY&OVED#pO1rc2HuhmTv_T!-(rxu04?2Ps9$Dog2!j?*YzepAi&MX}_QCwk^T223dp5Mzu9H>hBqF-L`QGY2%j6g+FdRkq
);w<SVsvWAWGxDks1nn7FYhy=t$Ny`<1>LLo&0B%XtF_8h@M3c?<eo1(jucW5-yZ%v_++IK2(YyZ#YG0I&2A*5Jzg^67jA=CPS@a
Tb4+_Q7NXNYn6sepM>0UjMUFekP^W13|0w`ZZckFcrthq>Zkj(Vg#Xh!L=}vY+z+rUj>cynq9gAt@W_BNBr~*%{Q6M4%crQUWhEw
8!p*L8`mWBNn+5et3aoeml!H48_VdbY%ZJD0<CD0Hf2T|*tg=7$Tg_7u=gDJFOG9QWZ?Oxxr6awQ7WUsKx&n5S8*e;Jxo~JGQ@Pj
#2#?9GEE&w-+?4JbOEB)i->Ps*NbA!7TMtJkUl&?6B@sDpp>LAqgmTpzs8|PN^wd1>|l;Pji=-rtfbk@iwi!$a9rHTSXtdsRU>uB
O>Q?vpcxfcj+@AgIX6e3JNL&;HUjMl&ysE3rRfeb^P6TH=hmqTAFO#NxrGU7;c-+rzv2;Vmt?p5)wm`(*giQG;Dn=n+7e^i&Er$l
gL10VcJpn`SetK)qb;qbO%FR<_ppJrpRHd&WW#RNj2mUn7E)I^VTDw&i;5i0kX&4bLNS9EHGrTuA?4_9{vsYc#UqLWrQToXG!SJs
EYV}fFT&<fXS#C;LcP$Yg@}J<QT6ny_;Ba1<d9zoovtW+<hmsK{}DtNoNwPw;si>66=G`fikNz)Tezh>mDp&rc)j{93K@w5rhXJ5
w+fr*AIp~QLd2u&TMn*TR&|iX>c3W3UpX`#HH=JFDl6ZOzFGKBNzN$1^J%=67LkYTbw!O#{<E4`g}}wi6~=<oZWzvOG2}RlOo&=}
VI!9qVj5BGa<tm`JVJC?|3(7SOx1fzmg0_AuRXOb`hbIa(H<0AuiZIW5A0#O=xeX8Z*={Y^wVjx1VdR)U1jJxaP7cX`fVu0Ez3m}
)5I?YiK#%DML7u8lI^ci_yBytMN$l)H*8joBQ$)Q>rn{ZDz4O866%@|!73?7ys9NbolDaw@wTh`(qQn`$%GIpqK82K9|<1K0HS%I
r(z)rT8s3jCH%V|gt9QQd1g%UGg$oiHw~d{;L8tsv&4-e;iv>)+=5PbL-9VQXxAY0Vf!i{0=xNm4^Vf(_2Pe4F3)_kH1)iGgX4S6
@Wyc#M3m1GTpld*)ZI7@5*p3W!23I9$k6QFLM02V7Caoddb)&15Uqdzcocp~!F%!}5G`PGLQ!%p`G8=5>N^Z@ayfnvv2)UeV(*~O
54tb&U><NNE0_q8DmyB;F;SmWgnbd(2r2Li&`+BkQQ)BfRL)<1QbP@J*iMK=Rmwl@bq@M;2aP^S1p-OBS8qBYZa}|c6p%%Js-aX7
jlxJcGQZd~JR0B-RPSHVSA*iCx8e>DTi<?Cft3XW;G7j-g3w(04N1gL%!UZoj90b{JmU3y5svwpP0IqH$)C;d-8}YVPDz<!o3N@9
8q+pO&ov{A4*t;PP?!b>>RY8>B7tsrOK~koA}wd}U}!vZSLkg%Wx;F^_;`VY-!Q4aq|#jvTJSAV49$o`0m#bEQm_{Sn<*jfNE1Q5
mmwRnNb)$PfDH<yc?xTD&=6^Hk(7~^2sUmQBSH*U>=BY`g=6DUKp~GoF2y541^+gHfJ_(B=!_SPA}*(iEJdcOZE=B$yptJVNFP2(
E|T6$5P7j5h>r)?vsG7R1{0Krye?kpfvYJx{fWJvt&Rk_kg+mh{Vmmvr|+9k#6e`3(z6O^y(*Z6`m9eS<7LVM1Z19KLR9;P(sBG?
Fdt#^H{sR9P1ob={#tjyi%e_*V$iE=c_-9+Cns+YNUlJW%qi9TnoC4sodeXtr(WsZ6>NgGf)>`R_fKiSVUygo$^lUJLH+KxTj%`p
_UYmB!nw4MosZYI*B{Srocp_*vj^uMTF&0x-8v7KXE)b>oIPDb`HNj=0%M*?bDDc4(@I47K<@qww414Y@|~@~tWHM@>kV(=$9L)-
IH|Z!Qm4N>QD=1`Y2A`vFg{ZB?-E=_v;H6c{R+D50gfs+@vlhi`SV$lnR5HJ4Yn9cO6NIPW%MxvD0CzhZ&|zb|B33>o*aVL0`oD)
KUQJZE7KzQx?p1sGtMPS9n$4rQ{Yr*u*&hyuS*|s&|Ow#7GWRojI$iC?@@FFYd}@_au5hL9LMSp0sT3QS(we-+#A<PUqnEkv-79V
u#dQ>PY<6josVb#qK&;eJHLE-be?{@bH3c&eExU|HMfsW!3THO7ta0J<0IlALA|@Y{d|3U>0DgCd$_zjl)Qm}oU6Of56;=c!`*Mr
?c;^>2z>PTxIUgb-M|0+@%kJV@Njv4egANW#mCRTKK}mrbotSd1}Or#K7Vq4yFB|RaP4+L4|n&M59QcL=eO&p_X0_^!Y`K(PnZ8v
&_1ujIlsAk1b#2@J--9&@bEeBKA$~Y0Cmo80qG~_-Pyg<cJ2V2(>h#-A}M@z{V#xZb^YbixxYCBKn2(jXXkgnUZ26~IlKL5dwuxR
9nkUa9ns|c?&JN<<wu<I_U_4fync7<TwR_$UjKS?2{n#wH=Vl&=hwT>x3JpxxVjP&@kZp%0&zba*@?-&oU)gV-PYlesN5R|OFslt
0r|WZ(zPBK<v75cj)TY4aq1m$Tx<Ue(TvNG
"""

def main():
    if len(sys.argv)!=2:
        raise SystemExit('Usage: python -B -S recover_pentagon_e17.py fresh')
    data=zlib.decompress(base64.b85decode(''.join(PAYLOAD.split())))
    assert len(data)==18130
    assert hashlib.sha256(data).hexdigest()=='cdf46290aadcf61f5127120a0e267d62c7041d227c047194f3fd86d775043f01'
    folder=Path(sys.argv[1]);folder.mkdir(parents=True,exist_ok=True)
    target=folder/'pentagon_e17.py'
    if target.exists() and target.read_bytes()!=data:
        raise SystemExit('Refusing to overwrite different source bytes')
    target.write_bytes(data)
    print('EXACT_PENTAGON_E17_SOURCE_RECOVERED',len(data),hashlib.sha256(data).hexdigest())

if __name__=='__main__':main()
```

Optional convenience copies: decoded source (`pentagon_e17.py`), complete exact report (`pentagon_e17.json`), source-only recovery capsule (`recover_pentagon_e17.py`). The embedded capsule is sufficient without these links.
