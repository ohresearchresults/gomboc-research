# minimum-0255

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# H5_SEVEN_TURN_REFLECTION_JOINT_EXTENSION_V1

## 1. New theorem and certified H5 regions

**A reflection strictly weaker than the parent's containment C, combined with the seven actual basal vertices, excludes joint S1/U1 on five continuous H5 regions. The mechanism also crosses the gamma=1/3 barrier of C.** It uses the actual homogeneous centroid and one physical metric with its actual inverse. All conclusions include incidental weak equilibria.

Every genuine H5 body in the following union has **S≥2 or U≥2 for every SPD metric**:

| Region | x | r | p | q | Taper |
|---|---|---|---|---|---|
| BROAD_TURN | [1/10,9/10] | [1/10,9/10] | [1/5,1/2] | [1/5,1/2] | 0<lambda≤1/40 |
| WIDE_TURN | [1/5,4/5] | [1/5,4/5] | [1/5,1/2] | [1/5,1/2] | 0<lambda≤1/20 |
| DEEP_TURN | [2/5,3/5] | [2/5,3/5] | [3/10,1/2] | [3/10,1/2] | 0<lambda≤3/25 |
| SKEW_TURN | [1/2,3/5] | [5/8,29/40] | [13/40,17/40] | [9/20,11/20] | 0<lambda≤7/50 |
| CORE_TURN | [27/50,14/25] | [133/200,137/200] | [73/200,77/200] | [49/100,51/100] | 0<lambda≤17/100 |

Always retain p+q<1. The coordinate reflection x↔r, p↔q gives two additional reflected regions from SKEW_TURN and CORE_TURN; the first three boxes are already invariant. All displayed genuine upper and side boundaries are included. Lambda=0 and p+q=1 occur only in algebraic coefficient checks, not as asserted ten-vertex bodies.

The entire CORE_TURN subbox with

    33/200 ≤ lambda ≤ 17/100

has **gamma>1/3**. Consequently every body in that subbox is outside the parent's entire C-containment class, not merely outside its four previously certified rectangles. This is not a Hausdorff-error refinement or a new fixed-metric census.

The new turning argument establishes three strict conclusions on these regions: a basal U always exists; a nonbasal S always exists; and U1 forces the basal facet to be strictly stable. Thus U1 implies S≥2. It does **not** prove unrestricted U≥2 on these regions.

The portions extending past the previous BROAD/WIDE/DEEP cutoffs are new. The two skew boxes and their reflections have neither p nor q as large as 3/4, so they are outside the complementary all-taper covariance-atlas box and its reflection. All five boxes avoid the old x≥15/16 macro and its reflection, and the off-macro radius-2^-28 tubes. Intersections with older lower-dimensional slices are not counted as new registry entries. The accepted full-basal cutoff remains 1/300; hence the global residual taper remains **1/300<lambda<3/5**, outside the old exclusions and the new union. The minimum interval remains **34≤C_min≤622**, with no new attainer or canonical incidence/root count. The inherited residual interval and the distinction between a joint theorem and unrestricted U2 are literal parent premises. fileciteturn25file0L12-L22

## 2. Reading, parent authority, and execution status

I read the complete new journal and both complete literal parent payloads, including every source block, consecutively through line 2609/EOF. The journal is 376054 bytes, SHA-256 `3b0bb9ec490072cb84e06c61052b32cffb194078919968133e81e0b0c0d22d15`. Earlier unchanged sources remain accessible in this chat and were retained rather than unnecessarily reread.

The two registered parent JSON envelopes were reconstructed and their hashes matched exactly:

| Parent | Envelope bytes | SHA-256 |
|---|---:|---|
| minimum-0253 | 37319 | 0bf1ea8d44110e8f0f712137c4fc3bff5ff4f48962e0e3a5b4c3c79b6b14db45 |
| minimum-0254 | 44777 | 54910bbef02f3039f114fe487568a3710a65cbf08331a42511807f836c39c2d0 |

The normalized envelope uses the literal parent Markdown with one final LF and compact UTF-8 JSON for `{version:2,result_markdown:...}`. There is no source-identity conflict. The covariance atlas is used only to identify already closed scope, not regenerated or used as a mathematical premise of the new geometric proof. Its actual moving-covariance and conditioned-versus-unrestricted distinction remains intact. fileciteturn22file0L16-L69

No missing exact dependency is required for the result below. Its source is standalone. Exact arithmetic checks the complete scalar region certificates, actual moments, true hulls and same-inverse censuses. The continuous geometric proof is supplied here; it is not claimed to have been proof-assistant formalized.

## 3. Reflection plus finite turning: the general theorem

Let

    P=conv((B,0),(T,1)),   g=(c,gamma),   0<gamma<1/2,

where B,T are full-dimensional planar convex polygons and B has n true vertices. Write B_g and T_g for their centered copies in P-g. The theorem is valid at the specified interior reference g; in every H5 application below, g is specifically the actual uniform-volume centroid.

Choose 0<alpha<1 and put

    beta=gamma(1+alpha)/(1-gamma),
    kappa=alpha+beta,        r_*=beta/alpha.

Assume

    alpha ≥ 1-2gamma,
    alpha² ≥ gamma,
    r_* cos(pi/n)^n ≤ 1.                                      (T)

The two geometric hypotheses are:

    -alpha B_g-beta T_g ⊂ B_g,                                (R)

and, for every actual nonbasal pole q and every a∈T_g,

    q·a > -1.                                                 (A)

Poles are normalized by q·X≤1 on P-g. They are not recentered at the polar's own volume centroid. The containment R may be non-strict; A is strict.

**Theorem.** Under these hypotheses every SPD metric M, with N=M^-1, has a strict basal U and a strict nonbasal S. If U=1, the basal facet is strictly stable. In particular S=U=1 is impossible, including with additional physical weak contacts.

### The rational H5 specialization

For n≤7 it suffices to take

    1/4 ≤ gamma ≤ 4/9,
    alpha=gamma+1/4,
    beta=gamma(gamma+5/4)/(1-gamma).                           (R7)

Indeed

    alpha²-gamma=(gamma-1/4)²,
    kappa-1=3(gamma-1/4)/(1-gamma),
    kappa-r_*=(alpha²-gamma)/(alpha(1-gamma)),
    2alpha-(1+3alpha)gamma=1/2+gamma/4-3gamma².

The last concave quadratic has endpoint values 3/8 and 1/54 on [1/4,4/9], so r_*<2 throughout. Also alpha≤25/36<1. Finally,

    cos(pi/7)<901/1000,
    (901/1000)^7=482029410279032016301/10^21<1/2.

The source verifies this using exact Machin bounds for pi and the degree-four cosine upper bound at (333/106)/7. No numerical angle approximation is a proof premise.

For 1/4≤gamma<1/3, the parent's C reflection has coefficient

    alpha_C=gamma/(1-2gamma),

and

    alpha_C-(gamma+1/4)
      =2(gamma-1/4)(gamma+1/2)/(1-2gamma)≥0.

The reflections have the same fixed point, so C implies R7 by convex interpolation. The converse fails on an exact actual control below. The parent required C and did not use the seven-vertex turning budget. fileciteturn25file0L36-L64

## 4. Proof, including the two strict root conclusions

### 4.1 One physical coordinate system

Apply L with L^T L=M, subtract the actual Lg, and rotate so the two end planes are horizontal. This is a physical affine image of the same uniform body. Poles transform by L^-T, so their Euclidean metric is exactly the transported N=M^-1. No covariance whitening followed by a metric reset occurs.

Let h>0 be the physical separation of the planes, K=gamma h and H=(1-gamma)h. Basal points have height -K and top points height H. The coefficients and containments above are affine-invariant.

For fixed a∈T_g, the map

    F_a(b)=-alpha b-beta a

takes B_g into itself. Its fixed point is

    c_a=-[gamma/(1-gamma)]a.

Because 0<alpha<1, iteration puts c_a in B_g. It is in the relative interior: a supporting line through c_a, together with the negative homothety about c_a, would force the whole planar polygon into that line.

### 4.2 A basal strict U is unavoidable

Let b maximize squared norm on the basal polygon. If D_ba=b·(a-b)≥0 for any top vertex a, put t=beta/kappa∈(0,1). Then

    |b+t(a-b)|²=|b|²+2tD_ba+t²|a-b|²>|b|².

But F_a(b)=-kappa[b+t(a-b)] belongs to the base, and kappa≥1 by T. This contradicts maximality. Thus all its top derivatives are strictly negative. Its same-layer incident derivatives are also strictly negative by

    2D_bv=|v|²-|b|²-|v-b|²<0.

It is a true strict U. Norm ties elsewhere and unrelated weak contacts do not change this conclusion.

### 4.3 An outside basal foot would force an impossible half-turn

Assume U=1 and suppose the basal foot of the origin is not in relint B_g. Choose a top vertex a of maximum top norm. It is not the unique U, because a basal U has already been proved. All its same-layer derivatives are strictly negative, so a has a nonnegative escape along a true spoke to some basal vertex b.

Write a=(t,H), d=|t|. The escape gives

    t·b_H ≥ d²+Hh>d².

In particular d>0. Rotate horizontal coordinates so t=(d,0), whence b_x>d.

Consider the basal chord along that horizontal axis. It contains the negative interior point c_a,H. Since the foot 0 is not interior, its right endpoint R is at most 0. If L is its left endpoint, invariance under F_a gives

    -alpha L-beta d ≤ R ≤ 0,
    L ≥ -r_* d.

Thus the entire chord lies in [-r_*d,0]. The vertex b is off that chord. Its reflected point F_a(b) is in the opposite open half-plane and satisfies

    F_a(b)_x < -(alpha+beta)d=-kappa d.

Because kappa≥r_* and kappa≥1, that point has horizontal norm greater than both r_*d and d. Maximize horizontal norm on the opposite closed half of the basal polygon. A maximizer is off the separating chord, is a genuine basal vertex, and has radius rho>d. Its same-layer edge derivatives are strictly negative by local maximality. Every top derivative is bounded by

    rho d-rho²-Kh<0.

It is therefore a strict U. Under U1 this must be the root, and it is in the half-plane opposite b.

Now follow genuine nonnegative escape edges starting with a→b toward the unique U. Squared full physical norm strictly increases on every such edge. Immediately after a→b it exceeds the norm of every top vertex, so the remainder of the path stays in the basal polygon. There are at most n arrows in total: one top-to-base arrow and at most n-1 basal arrows.

Stop at the first subsequent crossing of the horizontal axis, truncating its last basal edge if necessary. The endpoint is on the negative-axis basal chord and has horizontal norm at most r_*d. Every horizontal arrow in the truncated chain is nonnegative; the first is strictly positive because its horizontal derivative is D_ab+Hh>0.

For any chain u_0,...,u_m with these horizontal arrows, let theta_j be its consecutive angles. Each theta_j<pi/2 and

    |u_0|/|u_m| ≤ product_j cos(theta_j),

with strict inequality here because the first arrow is strict. The start and endpoint are antipodal, so sum theta_j≥pi. Concavity of log cos gives

    product_j cos(theta_j) ≤ cos(pi/m)^m ≤ cos(pi/n)^n.

The last monotonicity follows from the positive derivative log cos x+x tan x for 0<x<pi/2. Chains with one or two arrows cannot make this half-turn at all. Consequently

    |u_m| > d/cos(pi/n)^n ≥ r_*d,

contradicting the chord bound. For H5, n=7 and the simpler contradiction is |u_m|>2d while the chord radius is less than 2d.

The basal foot must therefore lie in the relative interior. In the original Schur chart it is exactly c+gamma v. The basal facet is strictly stable, not merely weakly stable.

### 4.4 The actual inverse forces a nonbasal strict S

Set k=1-2gamma>0 and theta=k/alpha≤1. Convex interpolation of F_a(b) with c_a gives

    theta F_a(b)+(1-theta)c_a
       =-(1-2gamma)b-2gamma a ∈ B_g.                           (W)

Thus the weaker reflection W follows from R even when gamma>1/3.

Let q_B be the actual basal pole, and choose q of maximum norm among the nonbasal true poles. Put

    mu=min_{a∈T_g}q·a>-1,
    delta=1-gamma+gamma mu,
    u=(1-2gamma)/delta,       v=gamma(1+mu)/delta.

Then u,v>0 and u+v=1. Consider z=-u q-v q_B. For a top point, q_B·a=-(1-gamma)/gamma, so z·a≤1, with equality at a top vertex attaining mu. For b∈B_g, applying q to W with a minimizing top vertex gives

    (1-2gamma)q·b+2gamma mu≥-1,

which implies z·b≤1. Hence z lies in the actual polar, on a face dual to a true top vertex. That face contains no basal pole. Therefore z is in the convex hull of nonbasal poles and |z|≤|q|.

If q·(q_B-q)≥0, however,

    |z|²=|q|²+2v q·(q_B-q)+v²|q_B-q|²>|q|²,

a contradiction. So q has a strictly negative derivative toward q_B. Its derivatives toward all other nonbasal poles are strictly negative by norm maximality and distinctness. It is a strict U of the same-origin polar under the actual inverse metric.

Equivalently, Nq/(q^T Nq) lies in the relative interior of the corresponding nonbasal primal facet. That facet is a strict S. Under U1 it coexists with the basal strict S from Section 4.3, completing the joint exclusion.

All escape paths above allow zero derivatives. Strictness of the root conclusions comes from positive true edge lengths, the positive physical height, and the strict pole condition A. No weak-rest deletion or eta=0 contraction is used.

## 5. Exact actual-centroid region certificate

The literal H5 vertices are (sB_i,0), i=0,...,6, and (0,0,1),(lambda,0,1),(0,lambda,1), where s=1-lambda and

    B_i=(1/4,0),(1-3x/4,0),(1-p,p),(q,1-q),
        (0,1-3r/4),(0,1/4),(1/16,1/16).

The full nine maximal facet cycles and all seventeen true edges are reconstructed in the source. With D=6Vol(P), K=6 integral_P X, the actual moment equations are

    A=(31-24xp-24rq)/64,
    bx=509/3072-3xp/8+3x²p/32+xp²/8-rq²/8,
    by=509/3072-3rq/8+3r²q/32+rq²/8-xp²/8,
    D=lambda+2As²,
    Kx=3s³bx/2+s²lambda(1-3xp/4)/4+lambda²/4,
    Ky=3s³by/2+s²lambda(1-3rq/4)/4+lambda²/4,
    Kz=As²/2+lambda/2+lambda²/4,
    g=K/D.

The source independently derives these from the entire oriented boundary, and compares every control with a positive nine-tetrahedron apex fan. It also computes the actual second moments and covariance for the physical audits. No end-centroid weight is freely chosen.

For a true basal support n·b≤h, put t=max_T n·a. Its side plane has normal (n,h-t), offset h, and cleared actual pole denominator

    H_e=D h-n·K_xy-(h-t)Kz.

Write A0=4Kz+D and B0=4D, so alpha=A0/B0. The new reflection is certified by the 147 scalar polynomials

    R_eij=B0(D-Kz)h-(A0+B0)n·K_xy
           +A0(D-Kz)n·b_i+(A0+B0)Kz n·a_j ≥0.

They equal B0(D-Kz) times the actual basal support slack of the reflected point. The seven supports, their offsets and their top maxima are literal in the source.

Condition A is certified by the 21 polynomials

    T_ej=2H_e-D(t-n·a_j)>0.

The top pole has value 1 on the entire top triangle automatically. Together with seven positive H_e and the height guards 4Kz-D and 4D-9Kz, there are **177 required scalar polynomials per region**.

All five full boxes pass an exact tensor Bernstein check. Every polynomial except gamma_quarter has every coefficient strictly positive. The only zero coefficients are the five lambda=0 coefficients of 4Kz-D=lambda(1+lambda). All upper-taper coefficients are strictly positive. A separate polynomial 3Kz-D is checked on the CORE_TURN tail [33/200,17/100]; its verification box is explicitly retained in the report and is not confused with the full core column.

    Required full-box polynomial checks       885
    Additional above-third height check         1
    Complete inverse power reconstructions    886
    Exact Bernstein coefficients           890463
    Strictly positive coefficients         890458
    Zero coefficients                            5

Every Bernstein expansion is independently expanded back into its complete power coefficients. There is no sampling argument, numerical feasibility tolerance, or infeasible-cell pruning. The full coefficient arrays are regenerated by the source.

On the above-third tail the exact coefficient lower bound is

    3Kz-D ≥ 31035653/12800000000 >0.

Thus the whole tail has gamma>1/3. For any fixed top vertex, C would map the full basal polygon into itself with area factor [gamma/(1-2gamma)]²>1, which is impossible. The new coverage genuinely lies beyond C's geometric scope.

## 6. Exact actual controls, including a physical weak wall

These are nonattaining controls, not U1 or proper110 constructions. Each has exhaustive maximal-support recovery from all 120 vertex triples, the complete true facet/edge lattice, two agreeing actual-volume moment calculations, exact SPD M and N=M^-1, and all 68 true-edge primitives.

Use

    M_standard=((5,1,2),(1,3,-1),(2,-1,4)).

| Control | theta=(x,r,p,q,lambda) | Strict (S,U,H) | Physical weak points | Zero primitives |
|---|---|---|---:|---:|
| BELOW_R_NOT_C | (1/2,1/2,2/5,2/5,3/20) | (5,4,7) | 0 | 0 |
| ABOVE_THIRD | (11/20,27/40,3/8,1/2,1/6) | (4,4,6) | 0 | 0 |
| TURN_OUTSIDE_FOOT | same as ABOVE_THIRD | (2,3,3) | 0 | 0 |
| TURN_VE_WALL | same as ABOVE_THIRD | (2,3,3) | 1 VE | 1 |
| W_ONLY_RESIDUAL | (1/10,9/10,3/25,3/5,3/20) | (2,6,6) | 0 | 0 |

The first, second and fifth use M_standard. Across all five controls, 339 of the 340 primitives are nonzero; the remaining zero is a genuine physical VE, not an automatically rejected algebraic zero.

### R is strictly weaker than C on an actual body

BELOW_R_NOT_C has

    Vol=40523/384000,
    g=(9898673/51869440,9898673/51869440,51563/162092).

All R and A guards are positive, but C5_2_1=-3369209/102400000<0. Thus the extension is not merely a different certificate for the same C region.

### A genuine body above gamma=1/3

The three ABOVE/TURN controls share

    Vol=2563/27648,
    g=(63351/328064,53661/328064,3459/10252),
    alpha=3011/5126,
    beta=28145883/34820918.

Here 3gamma-1=125/10252>0. Their smallest new reflection guard is R3_1_1=671926169/81537269760>0, whereas C5_2_1=-62095/884736<0.

For TURN_OUTSIDE_FOOT take the small integer metric

    M=((49,-49,2),(-49,51,-3),(2,-3,1)).

Its leading minors are 49,98,41. Its Schur parameters are

    G=((49,-49),(-49,51)),
    v=(-45/98,-1/2),       eta=41/98,

and its actual basal foot is

    (613719/16075136,-153/29824),

strictly outside the base. Top vertex 8 is the unique top norm-maximizer, yet

    D_81=6430357/4294656>0.

Thus the shortcut that the top norm-maximizer must itself be U is false even in the newly excluded domain. The actual strict roots are S={2,4}, U={1,4,7}; the saddles are (2,3),(7,8),(7,9). This is consistent with the turning proof, not a counterexample to it. Exact characteristic-polynomial brackets also certify covariance-weighted condition greater than 400, illustrating that the new theorem is not restricted to the joint covariance cone.

For TURN_VE_WALL keep G and v, replace eta by

    eta*=4107656375/1533805056,

and set M_zz=57/98+eta*. Use the exact inverse of this new matrix. The same strict S/U/H labels remain, but D_81=0 and there is exactly one physical VE on edge (1,8), at centered point

    (-26021/984192,-53661/328064,6793/10252).

Every other primitive is nonzero. This wall is fully included by the new theorem.

### The W-only frontier is not silently closed

W_ONLY_RESIDUAL has

    Vol=881291/9600000,
    g=(7368835529/28201312000,
       3427883561/28201312000,
       50317/153268),

with gamma<1/3. All W and A guards are positive: their minima are respectively 267462321/20480000000 and 26463744507/1024000000000. But R0_3_2=-892247633238807/40960000000000000<0. Its new reflected point is

    (51458328098311,-4310375039801,0)/161297403984000,

which violates the true basal inequality y≥0.

This is an exact actual-centroid countercontrol to **W implying R7**. It is not a counterexample to the still-unresolved W-only U1-to-basal-foot implication: it has six strict U and two strict S. Its complete same-inverse census and all geometry are retained, rather than upgrading failure of the sufficient reflection to a mechanical possibility.

## 7. A new necessary lens for the remaining W-only joint problem

The same turning argument yields a useful residual constraint without R7. Assume W, n≤7, and 1/4<gamma≤1/3. Suppose U1 holds but the basal foot is outside or on the boundary. Let a be any top norm-maximizer and a→b any nonnegative true spoke escape. In physical horizontal coordinates put d=|a_H|, k=1-2gamma, beta0=2gamma, r0=beta0/k.

The W-reflected point -k b-beta0 a is in the opposite half-plane, while the axial basal chord has radius at most r0 d≤2d. If that reflected point had horizontal norm greater than r0 d, the opposite-half U and the forbidden seven-arrow half-turn would follow exactly as above. Hence necessarily

    |k b_H+beta0 a_H|² ≤ r0² |a_H|².                          (L)

Moreover a_H·b_H/|a_H|²≥1+Hh/d². The two horizontal vectors are not collinear, because b_x>d while the axial basal chord is nonpositive. Thus L gives the strict aspect requirement

    (4gamma-1)d² > (1-gamma)(1-2gamma)² h².                   (N)

In the original Schur coordinates, define

    Y_i=Z_i,xy-c+(Z_i,z-gamma)v,
    M=((G,Gv),(v^T G,v^T Gv+eta)).

Then L and N become

    |(1-2gamma)Y_b+2gamma Y_a|_G²
       ≤ [2gamma/(1-2gamma)]² |Y_a|_G²,
    (4gamma-1)|Y_a|_G²
       > (1-gamma)(1-2gamma)² eta.

These retain the actual g, the same G and shear, and positive physical eta. They are necessary for every such top-maximizer escape, not independently selectable port conditions. Under W and A, a joint S1/U1 candidate must have a non-interior basal foot because the nonbasal S already exists; thus these are necessary constraints on that remaining joint region. They are not a complete W-only exclusion or an eta=0 assertion.

The number seven is substantive in this argument. There is an exact eight-arrow planar half-turn with all derivatives strictly positive and endpoint norm less than twice the starting norm: start at (1,0), and successively multiply the complex coordinate by

    (1001/1000)(1+i t),   t=(1/2,1/3,1/2,1/3,1/2,1/3,1/2,1/3).

Its endpoint is the negative real number

    -(625/324)(1001/1000)^8,

whose magnitude is less than 2. This is a formal chain demonstrating the limitation of a naive seven-to-eight replacement, not a polyhedron or a counterexample to the geometric theorem. All nine vectors and eight derivatives are reconstructed exactly by the source.

## 8. What was tried, limits, and continuation

The original W two-half argument stalled because its basal chord can have radius greater than the top horizontal radius. The successful replacement allows that longer chord, forces only one reflected half to contain a U, and then uses the actual seven-vertex escape budget to rule out reaching that U. The inverse-polar reflection supplies the independent nonbasal S. This is why the new mechanism crosses gamma=1/3 without asserting unconditional basal U for arbitrary H5 shapes above that boundary.

The new R7 hypothesis is still stronger than W. The exact W_ONLY_RESIDUAL body preserves that distinction. Exploratory metric and free-reference polygon searches produced no audited U1 body and supply no exclusions. Larger trial boxes with failed scalar coefficient tests were not treated as mechanically feasible or infeasible. The accepted result is the general theorem and the five completely verified regions, not a conjectural full H5 closure.

The most useful continuation is the **same-inverse W-only problem with the necessary lens L and strict normal constraint N**, or a point-dependent reflection that uses only the actual top-maximizer escape ports. The current general theorem also permits other alpha values satisfying T; it does not require the particular linear choice alpha=gamma+1/4. Any further region must retain actual moments and genuine endpoints. The parent capped424 body with only top U remains outside the new reflection hypotheses and is not contradicted.

## 9. Complete recovery capsule

Save the following source exactly as `h5_seven_turn_reflection.py`, with its final LF. It is self-contained and contains every parameter box, actual control input, generator, geometric guard and verifier. No parent import, saved coefficient file, random seed, numerical optimizer, or omitted helper is needed. Tested environment: CPython 3.13.5 and SymPy 1.14.0; all acceptance arithmetic is exact.

Run in a fresh directory:

    python -B h5_seven_turn_reflection.py > h5_seven_turn_reflection.out

Expected pins:

    h5_seven_turn_reflection.py
    18109 bytes
    125da77daa965228d1486bad45fdf6dce556a54e6269aa08c0242d9741170d97

    h5_seven_turn_reflection_report.json
    38798182 bytes
    f9eb073f272a9ebb47e2a7b3946a632afecc0fbd04de631429b7c12fc48574ca

    h5_seven_turn_reflection.out
    619 bytes
    82aa8c2258f8471c04e4d5fa15aaee36d3331cfac97e017d2592bbeddbc5f407

The terminal marker is `H5_SEVEN_TURN_REFLECTION_JOINT_EXTENSION_V1_PASS`. The final source was executed normally and in a directory containing only that source; report and stdout were byte-identical. These are author executions, not a claimed coordinator replay. The report includes the complete coefficient vectors, inverse power checks, all true supports, actual moments, exact M/N pairs, all 340 physical primitives, the weak point, and the eight-arrow method-boundary chain.

Convenience copies supplement the complete inline recovery: [source](sandbox:/mnt/data/h5_seven_turn_reflection.py), [exact report](sandbox:/mnt/data/h5_seven_turn_reflection_report.json), [verification output](sandbox:/mnt/data/h5_seven_turn_reflection.out).

```python
#!/usr/bin/env python3
"""H5_SEVEN_TURN_REFLECTION_JOINT_EXTENSION_V1.
CPython 3.13.5 / SymPy 1.14.0. Self-contained, exact arithmetic only.
No parent import, saved coefficients, optimizer, or input file is required.
The geometric theorem and all endpoint qualifications are in the handoff.
"""
import hashlib
import itertools
import json
import sys
from fractions import Fraction as F
from math import comb
from pathlib import Path
import sympy as S

R = S.Rational
FACETS = ((6,5,4,3,2,1,0),(8,7,0,1),(7,6,0),(1,2,8),
          (9,8,2,3),(9,3,4),(4,5,7,9),(6,7,5),(7,8,9))
EDGES = tuple(sorted({tuple(sorted((f[i],f[(i+1)%len(f)])))
                      for f in FACETS for i in range(len(f))}))
EF = tuple(tuple(k for k,f in enumerate(FACETS) if a in f and b in f)
           for a,b in EDGES)
ARROWS = tuple(sorted((i,j) for a,b in EDGES for i,j in ((a,b),(b,a))))
DUAL = tuple(sorted((i,j) for a,b in EF for i,j in ((a,b),(b,a))))
SIDE_FACETS = (1,3,4,5,6,7,2)
x,r,p,q,l = VARS = S.symbols('x r p q l')
CASES = (
 ('BROAD_TURN',(('1/10','9/10'),('1/10','9/10'),('1/5','1/2'),('1/5','1/2'),('0','1/40'))),
 ('WIDE_TURN',(('1/5','4/5'),('1/5','4/5'),('1/5','1/2'),('1/5','1/2'),('0','1/20'))),
 ('DEEP_TURN',(('2/5','3/5'),('2/5','3/5'),('3/10','1/2'),('3/10','1/2'),('0','3/25'))),
 ('SKEW_TURN',(('1/2','3/5'),('5/8','29/40'),('13/40','17/40'),('9/20','11/20'),('0','7/50'))),
 ('CORE_TURN',(('27/50','14/25'),('133/200','137/200'),('73/200','77/200'),('49/100','51/100'),('0','17/100'))),
)
THETA_ABOVE = ('11/20','27/40','3/8','1/2','1/6')
STANDARD = ((5,1,2),(1,3,-1),(2,-1,4))
TURN = ((49,-49,2),(-49,51,-3),(2,-3,1))
WALL_ETA = R(4107656375,1533805056)
CONTROLS = (
 ('BELOW_R_NOT_C',('1/2','1/2','2/5','2/5','3/20'),STANDARD),
 ('ABOVE_THIRD',THETA_ABOVE,STANDARD),
 ('TURN_OUTSIDE_FOOT',THETA_ABOVE,TURN),
 ('TURN_VE_WALL',THETA_ABOVE,((49,-49,2),(-49,51,-3),(2,-3,R(57,98)+WALL_ETA))),
 ('W_ONLY_RESIDUAL',('1/10','9/10','3/25','3/5','3/20'),STANDARD),
)


def enc(v):
    if isinstance(v,S.MatrixBase):
        return [[str(v[i,j]) for j in range(v.cols)] for i in range(v.rows)]
    if isinstance(v,(S.Basic,F)):
        return str(v)
    if isinstance(v,dict):
        return {str(k):enc(a) for k,a in v.items()}
    if isinstance(v,(list,tuple)):
        return [enc(a) for a in v]
    return v


def pd(A):
    assert A == A.T
    mm=[S.factor(A[:k,:k].det()) for k in range(1,A.rows+1)]
    assert all(a>0 for a in mm)
    return mm


def vertices(theta):
    xx,rr,pp,qq,la=theta; ss=1-la
    B=((ss/4,0),(ss*(1-3*xx/4),0),(ss*(1-pp),ss*pp),
       (ss*qq,ss*(1-qq)),(0,ss*(1-3*rr/4)),(0,ss/4),(ss/16,ss/16))
    return tuple(S.Matrix((a,b,0)) for a,b in B)+(S.Matrix((0,0,1)),
           S.Matrix((la,0,1)),S.Matrix((0,la,1)))


def moments(z,apex=None):
    D=S.Integer(0); K=S.zeros(3,1); L=S.zeros(3); cells=[]
    o=S.zeros(3,1) if apex is None else z[apex]
    for f in FACETS:
        if apex is not None and apex in f:
            continue
        for j in range(1,len(f)-1):
            a,b,c=(z[k] for k in (f[0],f[j],f[j+1]))
            d=(a-o).dot((b-o).cross(c-o))
            if apex is not None:
                assert d>0
                cells.append((apex,f[0],f[j],f[j+1],d))
            t=o+a+b+c
            D+=d; K+=d*t/4
            L+=d*(t*t.T+sum((u*u.T for u in (o,a,b,c)),S.zeros(3)))/20
    return S.expand(D),K.applyfunc(S.expand),L.applyfunc(S.expand),cells


def bernstein(f,box):
    """Tensor conversion, then independently expand the full Bernstein basis."""
    po=S.Poly(f,*VARS); deg=tuple(map(int,po.degree_list()))
    cur={e:F(int(c.p),int(c.q)) for e,c in po.terms()}
    for i,(lo,hi) in enumerate(box):
        nxt={}
        for e,c in cur.items():
            for j in range(e[i]+1):
                ee=e[:i]+(j,)+e[i+1:]
                v=c*comb(e[i],j)*lo**(e[i]-j)*(hi-lo)**j
                nxt[ee]=nxt.get(ee,F(0))+v
        cur={e:c for e,c in nxt.items() if c}
    powers=cur.copy()
    for i,n in enumerate(deg):
        nxt={}
        for e,c in cur.items():
            for j in range(e[i],n+1):
                ee=e[:i]+(j,)+e[i+1:]
                v=c*F(comb(j,e[i]),comb(n,e[i]))
                nxt[ee]=nxt.get(ee,F(0))+v
        cur=nxt
    inds=tuple(itertools.product(*(range(n+1) for n in deg)))
    coeff=tuple(cur.get(e,F(0)) for e in inds)
    back=dict(zip(inds,coeff))
    for i,n in enumerate(deg):
        nxt={}
        for e,c in back.items():
            for j in range(e[i],n+1):
                ee=e[:i]+(j,)+e[i+1:]
                v=c*comb(n,e[i])*comb(n-e[i],j-e[i])*(-1)**(j-e[i])
                nxt[ee]=nxt.get(ee,F(0))+v
        back={e:c for e,c in nxt.items() if c}
    assert back==powers
    return deg,inds,coeff


def audit(z,g,poles,M,N):
    assert M*N==S.eye(3)
    X=tuple(a-g for a in z)
    P={(i,j):(X[i].T*M*(X[j]-X[i]))[0] for i,j in ARROWS}
    Q={(i,j):(poles[i].T*N*(poles[j]-poles[i]))[0] for i,j in DUAL}
    U=[i for i in range(10) if all(v<0 for (a,b),v in P.items() if a==i)]
    stable=[i for i in range(9) if all(v<0 for (a,b),v in Q.items() if a==i)]
    saddles=[]; weak={}
    for (i,j),(a,b) in zip(EDGES,EF):
        vals=(P[i,j],P[j,i],Q[a,b],Q[b,a])
        if max(vals)<0:
            saddles.append((i,j))
        if max(vals)<=0 and any(v==0 for v in vals):
            pp=next((X[k] for k,ll in ((i,j),(j,i)) if P[k,ll]==0),None)
            qq=next((N*poles[k]/(poles[k].T*N*poles[k])[0]
                     for k,ll in ((a,b),(b,a)) if Q[k,ll]==0),None)
            if pp is not None and qq is not None:
                assert pp==qq
            w=pp if pp is not None else qq; assert w is not None
            kind='VF' if pp is not None and qq is not None else ('VE' if pp is not None else 'EF')
            key=tuple(w)
            if key not in weak:
                weak[key]={'point':w,'kind':kind,'edges':[]}
            weak[key]['edges'].append((i,j))
            if kind=='VF':
                weak[key]['kind']='VF'
    assert len(stable)+len(U)-len(saddles)==2
    return {'S':stable,'U':U,'H':saddles,'weak':list(weak.values()),
            'counts':(len(stable),len(U),len(saddles)),
            'primal':[(i,j,P[i,j]) for i,j in ARROWS],
            'polar':[(i,j,Q[i,j]) for i,j in DUAL],
            'zero_primitives':sum(v==0 for v in tuple(P.values())+tuple(Q.values()))}


def model():
    ss=1-l; area=(31-24*x*p-24*r*q)/64
    bx=R(509,3072)-3*x*p/8+3*x*x*p/32+x*p*p/8-r*q*q/8
    by=R(509,3072)-3*r*q/8+3*r*r*q/32+r*q*q/8-x*p*p/8
    D=l+2*area*ss*ss
    K=S.Matrix((3*ss**3*bx/2+ss*ss*l*(1-3*x*p/4)/4+l*l/4,
                3*ss**3*by/2+ss*ss*l*(1-3*r*q/4)/4+l*l/4,
                area*ss*ss/2+l/2+l*l/4))
    z=vertices(VARS); DD,KK,LL,_=moments(z)
    assert S.expand(D-DD)==0 and (K-KK).applyfunc(S.expand)==S.zeros(3,1)
    assert S.expand(4*K[2]-D-l*(1+l))==0
    nh=(((0,-1),0,0),((p,p-3*x/4),ss*p*(1-3*x/4),l*p),
        ((1,1),ss,l),((q-3*r/4,q),ss*q*(1-3*r/4),l*q),
        ((-1,0),0,0),((-3,-1),-ss/4,0),((-1,-3),-ss/4,0))
    aa=4*K[2]+D; bb=4*D
    pol={'gamma_quarter':S.expand(4*K[2]-D),
         'gamma_four_ninths':S.expand(4*D-9*K[2])}
    oldC={}; weakW={}
    for e,(nn,hh,tt) in enumerate(nh):
        n3=S.Matrix((nn[0],nn[1],hh-tt))
        for j in FACETS[SIDE_FACETS[e]]:
            assert S.expand(n3.dot(z[j])-hh)==0
        H=S.expand(D*hh-n3.dot(K)); pol[f'H{e}']=H
        nk=nn[0]*K[0]+nn[1]*K[1]
        for i in range(7):
            for j in range(3):
                nb=nn[0]*z[i][0]+nn[1]*z[i][1]
                na=nn[0]*z[7+j][0]+nn[1]*z[7+j][1]
                pol[f'R{e}_{i}_{j}']=S.expand(bb*(D-K[2])*hh-(aa+bb)*nk
                                      +aa*(D-K[2])*nb+(aa+bb)*K[2]*na)
                oldC[f'C{e}_{i}_{j}']=S.expand((D-2*K[2])*hh-nk+K[2]*(nb+na))
                weakW[f'W{e}_{i}_{j}']=S.expand(D*hh-2*nk+(D-2*K[2])*nb+2*K[2]*na)
        for j in range(3):
            na=nn[0]*z[7+j][0]+nn[1]*z[7+j][1]
            pol[f'T{e}_{j}']=S.expand(2*H-D*(tt-na))
    assert len(pol)==177 and len(oldC)==len(weakW)==147
    return z,S.expand(D),K,LL,nh,pol,oldC,weakW


def certificates(pol,D,K):
    out=[]
    for name,rawbox in CASES:
        box=tuple(tuple(map(F,v)) for v in rawbox); use=pol.copy()
        if name=='CORE_TURN':
            use['above_third']=S.expand(3*K[2]-D)
        groups={};records=[]
        for key,f in use.items():
            check_box=box[:-1]+((F(33,200),F(17,100)),) if key=='above_third' else box
            deg,inds,co=bernstein(f,check_box)
            assert min(co)>=0 and max(co)>0
            if key!='gamma_quarter':
                assert min(co)>0,(name,key,min(co))
            top=[c for i,c in zip(inds,co) if i[-1]==deg[-1]]
            assert min(top)>0
            group=key if key.startswith('gamma') or key=='above_third' else key[0]
            if group not in groups:
                groups[group]={'polynomials':0,'coefficients':0,'zero':0,'minimum':None}
            g=groups[group];g['polynomials']+=1;g['coefficients']+=len(co)
            g['zero']+=sum(c==0 for c in co)
            g['minimum']=min(co) if g['minimum'] is None else min(g['minimum'],min(co))
            record={'polynomial':key,'degree':deg,'coefficients':co}
            if key=='above_third':record['verification_box']=check_box
            records.append(record)
        out.append({'name':name,'box':box,'groups':groups,'records':records,
                    'inverse_power_checks':len(records),
                    'coefficient_order':'lexicographic product(range(degree[i]+1),i=0..4)',
                    'mechanical_scope':'Only lambda>0, p+q<1 and genuine H5; closed collapsed faces are polynomial checks.'})
    return out


def algebra_and_turning():
    g,m=S.symbols('g m'); a=g+R(1,4); b=g*(1+a)/(1-g)
    k=a+b; rr=b/a; kw=1-2*g; rho=g/(1-g); theta=kw/a
    den=1-g+g*m; al=kw/den; be=g*(1+m)/den
    identities=(a*a-g-(g-R(1,4))**2,
      k-1-3*(g-R(1,4))/(1-g),
      k-rr-(a*a-g)/(a*(1-g)),
      2*a-(1+3*a)*g-(R(1,2)+g/4-3*g*g),
      theta*b+(1-theta)*rho-2*g, al+be-1,
      -al*m+be*(1-g)/g-1,
      -al*(-1-2*g*m)/(1-2*g)-be-1)
    assert all(S.factor(v)==0 for v in identities)
    f=R(1,2)+g/4-3*g*g
    assert f.subs(g,R(1,4))==R(3,8) and f.subs(g,R(4,9))==R(1,54)
    assert a.subs(g,R(4,9))==R(25,36)<1
    assert rr.subs(g,R(4,9))==R(244,125)<2
    def atan_bounds(d):
        z=F(1,d)
        s=sum(((-1)**j*z**(2*j+1)/F(2*j+1) for j in range(30)),F(0))
        t=s+z**61/F(61)
        return s,t
    lo5,hi5=atan_bounds(5);lo239,hi239=atan_bounds(239)
    pi_lo=16*lo5-4*hi239;pi_hi=16*hi5-4*lo239
    assert F(333,106)<pi_lo<pi_hi<F(22,7)
    t=F(333,742);c=1-t*t/2+t**4/24
    guard=F(1,2)-c**7;assert guard>0
    # An eight-arrow strictly increasing HALF-TURN; not a polyhedron.
    eps=F(1,1000);chain=[(F(1),F(0))];der=[]
    for slope in (F(1,2),F(1,3))*4:
        u,v=chain[-1];w=((1+eps)*(u-slope*v),(1+eps)*(v+slope*u))
        d=u*(w[0]-u)+v*(w[1]-v)
        assert d==eps*(u*u+v*v)>0
        chain.append(w);der.append(d)
    factor=F(625,324)*(1+eps)**8
    assert chain[-1]==(-factor,0) and 1<factor<2
    return {'reflection_identities':len(identities),'alpha':a,'beta':b,'radius_factor':rr,
            'radius_two_endpoint_gaps':(R(3,8),R(1,54)),
            'pi_lower':pi_lo,'cosine_upper':c,'half_minus_cosine_upper_seventh_power':guard,
            'eight_arrow_method_limit':{'scope':'Exact planar chain only, no hull, uniform centroid, equilibrium census or counterexample to the theorem.',
               'slopes':(F(1,2),F(1,3))*4,'epsilon':eps,'vectors':chain,
               'strict_derivatives':der,'terminal_to_initial_norm_ratio':factor}}


def control(data,nh,pol,oldC,weakW):
    name,rawtheta,mm=data;th=tuple(map(R,rawtheta));subs=dict(zip(VARS,th))
    xx,rr,pp,qq,la=th
    assert 0<xx<1 and 0<rr<1 and pp>0 and qq>0 and pp+qq<1 and 0<la<1
    z=vertices(th);assert len(set(map(tuple,z)))==10
    hull=set()
    for i,j,k in itertools.combinations(range(10),3):
        nn=(z[j]-z[i]).cross(z[k]-z[i])
        if nn==S.zeros(3,1):continue
        hh=[nn.dot(v-z[i]) for v in z]
        if max(hh)<=0 or min(hh)>=0:hull.add(tuple(t for t in range(10) if hh[t]==0))
    assert hull=={tuple(sorted(f)) for f in FACETS}
    D,K,L,_=moments(z);d2,k2,l2,cells=moments(z,7)
    assert D==d2 and K==k2 and L==l2 and len(cells)==9
    g=K/D;C=(L/D-g*g.T).applyfunc(S.factor);pd(C);poles=[];supports=[]
    for f in FACETS:
        v0,v1,v2=(z[i] for i in f[:3]);nn=(v1-v0).cross(v2-v0);hh=nn.dot(v0)
        slacks=[hh-nn.dot(v) for v in z]
        assert all(slacks[j]==0 if j in f else slacks[j]>0 for j in range(10))
        for j in range(len(f)):
            e=z[f[(j+1)%len(f)]]-z[f[j]]
            ee=z[f[(j+2)%len(f)]]-z[f[(j+1)%len(f)]]
            assert nn.dot(e.cross(ee))>0
        H=hh-nn.dot(g);assert H>0;poles.append(nn/H)
        supports.append({'normal':nn,'offset':hh,'vertex_slacks':slacks})
    for e,(nn,hh,tt) in enumerate(nh):
        n3=S.Matrix((nn[0],nn[1],hh-tt)).subs(subs);hh=S.sympify(hh).subs(subs)
        assert n3/(hh-n3.dot(g))==poles[SIDE_FACETS[e]]
    M=S.Matrix(mm);minors=pd(M);N=M.inv().applyfunc(S.factor);assert M*N==S.eye(3);pd(N)
    cc=audit(z,g,poles,M,N)
    G=M[:2,:2];v=G.inv()*M[:2,2];eta=S.factor(M[2,2]-(v.T*G*v)[0]);assert eta>0
    foot=g[:2,0]+g[2]*v
    values={k:S.factor(f.subs(subs)) for k,f in {**pol,**oldC,**weakW}.items()}
    minimum={c:min((values[k],k) for k in values if k.startswith(c)) for c in ('R','C','W','T','H')}
    assert minimum['W'][0]>0 and minimum['T'][0]>0 and minimum['H'][0]>0
    assert R(1,4)<g[2]<R(4,9) and minimum['C'][0]<0
    a=g[2]+R(1,4);b=g[2]*(1+a)/(1-g[2]);extra={}
    for prefix in ('R','C','W'):
        val,key=minimum[prefix];e,i,j=map(int,key[1:].split('_'))
        if prefix=='R':point=(1+a+b)*g-a*z[i]-b*z[7+j]
        elif prefix=='C':point=(g-g[2]*(z[i]+z[7+j]))/(1-2*g[2])
        else:point=2*g-(1-2*g[2])*z[i]-2*g[2]*z[7+j]
        assert point[2]==0
        nn,hh,tt=nh[e];nn=S.Matrix((nn[0],nn[1],0)).subs(subs);hh=S.sympify(hh).subs(subs)
        scale=4*D*(D-K[2]) if prefix=='R' else (D-2*K[2] if prefix=='C' else D)
        assert S.factor(scale*(hh-nn.dot(point))-val)==0
        extra[prefix+'_minimum_point']={'index':(e,i,j),'point':point,'normal':nn,'support':hh,
                                       'support_slack':hh-nn.dot(point),'cleared_guard':val}
    if name=='W_ONLY_RESIDUAL':
        assert g[2]<R(1,3) and minimum['R'][0]<0
        extra['scope']='Passes W and A below gamma=1/3, fails new R. This is a limitation of a sufficient criterion, not a U1 or 110 control.'
    else:
        assert minimum['R'][0]>0
        if name=='BELOW_R_NOT_C':assert g[2]<R(1,3)
        else:assert g[2]>R(1,3)
    norms=[((z[i]-g).T*M*(z[i]-g))[0] for i in range(10)]
    top=max(range(7,10),key=norms.__getitem__)
    extra['top_norm_maximizer']=top;extra['squared_vertex_norms']=norms
    extra['top_maximizer_derivatives']=[row for row in cc['primal'] if row[0]==top]
    if name.startswith('TURN_'):
        assert v==S.Matrix((R(-45,98),R(-1,2))) and foot[1]<0 and top==8
        assert cc['S']==[2,4] and cc['U']==[1,4,7] and cc['counts']==(2,3,3)
        d81=next(d for i,j,d in cc['primal'] if (i,j)==(8,1))
        if name=='TURN_OUTSIDE_FOOT':
            assert eta==R(41,98) and d81==R(6430357,4294656)>0
            intervals=((R(1,400),R(13,5000)),(R(83,1000),R(21,250)),(R(59,50),R(119,100)))
            zz=C*M;signs=[]
            for lo,hi in intervals:
                fl=S.factor((zz-lo*S.eye(3)).det());fh=S.factor((zz-hi*S.eye(3)).det())
                assert fl*fh<0;signs.append((fl,fh))
            assert intervals[2][0]/intervals[0][1]>400
            extra['covariance_metric_spectrum']={'intervals':intervals,'determinant_endpoints':signs,'condition_greater_than':400}
        else:
            assert eta==WALL_ETA and d81==0 and cc['zero_primitives']==1
            assert len(cc['weak'])==1 and cc['weak'][0]['kind']=='VE'
            assert cc['weak'][0]['edges']==[(1,8)] and cc['weak'][0]['point']==z[8]-g
    if name!='TURN_VE_WALL':assert cc['zero_primitives']==0 and not cc['weak']
    return {'name':name,'theta':th,'vertices':z,'facets':FACETS,'edges':EDGES,
            'exhaustive_maximal_hull':sorted(hull),'supports':supports,'positive_apex_fan':cells,
            'volume':D/6,'actual_centroid':g,'actual_covariance':C,'poles':poles,
            'M':M,'N':N,'leading_minors_M':minors,'G':G,'v':v,'eta':eta,'basal_foot':foot,
            'alpha':a,'beta':b,'census':cc,'geometric_minima':minimum,
            'all_geometric_guards':values,'extra':extra}


def main():
    assert S.__version__=='1.14.0'
    assert len(EDGES)==17 and len(ARROWS)==len(DUAL)==34 and all(len(a)==2 for a in EF)
    z,D,K,L,nh,pol,oldC,weakW=model()
    certs=certificates(pol,D,K);controls=[control(c,nh,pol,oldC,weakW) for c in CONTROLS]
    report={'identity':'H5_SEVEN_TURN_REFLECTION_JOINT_EXTENSION_V1',
            'environment':{'python':sys.version.split()[0],'sympy':S.__version__},
            'scope':'Every actual H5 body in the five stated regions and the reflected last two has S>=2 or U>=2 for every common SPD metric, including physical weak contacts. Not an unrestricted U>=2 or full-H5 theorem.',
            'algebra':algebra_and_turning(),'six_volume':D,'six_first_moment':K,
            'six_second_moment':L,'certificates':certs,'controls':controls,'status':'PASS'}
    raw=(json.dumps(enc(report),sort_keys=True,indent=2)+'\n').encode()
    path=Path('h5_seven_turn_reflection_report.json');path.write_bytes(raw)
    for c in certs:
        nc=sum(g['coefficients'] for g in c['groups'].values());nz=sum(g['zero'] for g in c['groups'].values())
        print(c['name'],'POLYNOMIALS',len(c['records']),'COEFFICIENTS',nc,'ZERO',nz)
    for c in controls:
        print(c['name'],c['census']['counts'],'WEAK',len(c['census']['weak']),'ZERO',c['census']['zero_primitives'])
    print(path.name,len(raw),hashlib.sha256(raw).hexdigest())
    print('H5_SEVEN_TURN_REFLECTION_JOINT_EXTENSION_V1_PASS')


if __name__=='__main__':
    main()
```
