# material-72f925412639

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Regression-amplified normal floor and a whole-shear-box W-only exclusion

## 1. Result, actual object and scope

For the literal actual H5 body

    theta=(1/10,9/10,3/25,3/5,3/20),
    volume=881291/9600000,
    g=(7368835529/28201312000,
       3427883561/28201312000,
       50317/153268)=(c,gamma),

there is NO physical metric with joint proper S=U=1 throughout the following complete closed shear rectangle, with every tangential G>0 and every normal parameter eta>0 allowed:

    5394743689/4842328000 <= v_x <= 6240783049/4842328000,
   -2635398519/4842328000 <= v_y <= -1930365719/4842328000.

Equivalently, put k=1-2gamma, a9=(0,3/20), and p=2c-a9-kv. The rectangle is exactly

    2/25 <= p_x <= 7/50,
    23/100 <= p_y <= 7/25.                                  (BOX)

Its approximate shear intervals are [1.1140806011,1.2887980841] and [-.5442420503,-.3986441478]. All endpoints in the theorem are the displayed rationals, not these approximations.

The conclusion permits additional weak equilibria and weak escape arrows: it excludes joint S1/U1 itself, not only weak000. It is NOT an unrestricted U>=2 theorem, because it uses the joint spectral floor. It is NOT a whole-shape affine-orbit exclusion, a five-dimensional H5 shape box, an exclusion of all E17 incidences, or an improvement of the canonical construction. The global bracket remains34<=Cmin<=622; the full10/17/9 layer remains open.

The theorem combines two completely read accepted immutable results:

* minimum-0262, SHA2569d6d4bb7467bce10452f7713b241cc60dbd441bea84f7100c4bc37c967d53825: strict actual-chord theorem and the local tangential gate. Its analytic results are accepted; the author's new probe executions were unobserved. That execution qualification is not altered retrospectively.
* minimum-0261, SHA256c858f67518fd87fccd41d8bf201b5d9b2be0d809750afdcaeb410696e568b021: actual-covariance orthogonal factor<17/2, with author analytic proof and exact normal/cold execution. In particular a joint E17 metric obeys the exact floor ell=21600000000000/1085712665457541.

The new amplification, exact regional proof, and new233 diagnostic below are coordinator work. Their code was observed executing both normally and in a fresh source-only directory. No independent verification of the whole parent proof is claimed or required.

## 2. One physical metric and an amplified covariance normal inequality

Let Sigma be the actual uniform-volume covariance of a full-dimensional body at its specified actual centroid. Write a physical SPD metric in one fixed horizontal/normal chart as

    M=[[G,Gv],[v^T G,v^T Gv+eta]], G>0, eta>0.

Its inverse is exactly

    N=[[G^-1+vv^T/eta,-v/eta],[-v^T/eta,1/eta]].

There is no separately chosen polar metric. A linear physical realization changes the true uniform centroid and covariance by the corresponding linear maps; no independently assigned vertex weights are introduced.

Put

    z=Sigma_zz,
    m=Sigma_Hz/z,
    D=(Sigma^-1)_HH,
    w=v+m,
    t=z w^T D w,
    C_v=Sigma_HH+Sigma_Hz v^T+v Sigma_zH+z vv^T
       =D^-1+z ww^T.

Suppose the necessary actual-covariance floor is

    M >= ell tr(Sigma M) Sigma^-1, ell>0.                    (FLOOR)

For the current joint E17 problem the accepted rational ell above is valid with strict margin. Testing (FLOOR) on the ACTUAL physical vector x=(-v,1) gives

    x^T M x=eta,
    x^T Sigma^-1 x=(1+t)/z,
    tr(Sigma M)=tr(G C_v)+z eta.

It follows that ell_v:=ell(1+t)<1 and

    eta >= ell_v tr(G C_v)/[z(1-ell_v)].                     (AMP)

If ell_v>=1, (FLOOR) is already impossible for positive G,eta. With a strict floor the displayed eta inequality is strict, but the closed version suffices below.

This is stronger than the previous scalar consequence

    eta >= ell tr(G C_v)/[z(1-ell)],

by the factor (1+t)(1-ell)/[1-ell(1+t)], which is>1 whenever t>0. The old consequence tested only an inverse-coordinate diagonal after matrix inversion. The new consequence retains the actual shear and covariance regression through x=(-v,1). Passing (AMP) is still not equivalent to the full matrix floor or to the equilibrium system.

### Exact all-G local gate with amplification

For a parallel two-end body at raw levels0 and1 let H=1-gamma, k=1-2gamma, beta=c+gamma v, and

    Y_i=Z_i,H-c+(Z_i,z-gamma)v.

At a genuine top-to-base port a->b normalize Y_a^T G Y_a=1, set J=[Y_a Y_b], and put X=Y_a^T G Y_b, Y=Y_b^T G Y_b. For nonsingular J, tangential SPD is exactly Y>X^2. A weak true spoke with eta>0 requires X-1>=H eta and therefore X>1.

The accepted strict actual-chord theorem under W/A, gamma<=1/3, and at most7 basal vertices gives

    |kY_b+2gamma Y_a|_G^2 < tau_a(v)^2,
    tau_a(v)>1,
    2c-a_H-kv in relint B.

If other top vectors are u_j Y_a+w_j Y_b, its complete local top/spoke/chord conjunction is the open interval

    1<X<(tau_a-2gamma)/k,
    -1<u_j+w_j X<1 for w_j!=0,

with |u_j|<=1 for constant rows. Zero or collinear ports are excluded by the actual chord geometry as stated in the literal parent; no division by a zero chart determinant is licensed.

Let T=J^-1 C_v J^-T. Adding just (AMP) to that local packet is equivalent to positive value somewhere in its open interval of the strictly concave quadratic

    F_v(X)=z(1-ell_v)(X-1)
           -ell_v H(T11+2T12 X+T22 X^2).                    (GATE)

Necessity follows from tr(G C_v)=T11+2T12 X+T22 Y and Y>X^2, using T22>0. For sufficiency choose a sufficiently small epsilon>0, Gram[[1,X],[X,X^2+epsilon]], and eta between the amplified lower bound and (X-1)/H. This proves exact equivalence only for the DISPLAYED local scalar packet. It does not restore the discarded full matrix floor, other escape arrows, or the actual inverse-polar root conditions. Its negative value, however, is a rigorous port exclusion.

## 3. Actual W-only geometry and forced top alternatives

The complete recovery core reconstructs the exact ten vertices from the H5 theta above, all9 true maximal facets,17 true edges, the volume centroid, and covariance by tetrahedral volume integration. It independently recovers every maximal supporting face from all vertex triples. Its cyclic facets are

    (6,5,4,3,2,1,0), (8,7,0,1), (7,6,0), (1,2,8),
    (9,8,2,3), (9,3,4), (4,5,7,9), (6,7,5), (7,8,9).

The seven true top spokes are7->0,7->5,7->6,8->1,8->2,9->3,9->4. Facet triangulation diagonals are used only for integration, never as escape edges.

For the actual centered end polygons the accepted hypotheses are

    -k B_g-2gamma T_g subset B_g,                           (W)
    1+q_f.a>0 for every nonbasal actual pole q_f
                   and every top centered vertex a.       (A)

All147 W support slacks and24 A products are recomputed from this actual body. Their exact minima are

    min W=110813102889/11280524800000>0,
    min A=2625570322/3427883561>0.

The older stronger R7 test actually fails: its minimum tested slack is

    -219829127029851/14337547020800000<0.

Thus no R7 premise is smuggled into this theorem. Also1/4<gamma<1/3. W forces a basal proper U, while W/A forces a nonbasal proper S. Hence in a putative joint S1/U1 metric the basal foot is not in relint B, and every top norm-maximizer has a true nonnegative top-to-base escape to which the actual-chord theorem applies.

On (BOX), every p is strictly inside B and beta_y<0. The necessary points for top7 and top8 are p+(0,3/20) and p+(-3/20,3/20), respectively. Their y coordinates exceed the true basal maximum17/50 by at least1/25. Consequently neither top7 nor top8 can be a top norm-maximizer in a joint candidate. Top9 must be a top norm-maximizer, leaving only the genuine ports9->3 and9->4.

### Port9->4: a nonsingular top chart removes an apparent chart singularity

Use J7=[Y9,Y7], not [Y9,Y4], and write Y4=c4 Y9+d4 Y7. On the entire rectangle the exact polynomial guards show

    det J7<0,
    c4+d4<1,
    c4-d4<1.

Thus c4+|d4|<1. Since |Y7|_G<=|Y9|_G=1 at a top9 maximum, Cauchy--Schwarz gives

    <Y9,Y4>_G <= c4+|d4|<1.

But the true spoke requires this quantity>=1+H eta>1. This is impossible. The proof remains valid where the port chart [Y9,Y4] is singular; that determinant actually changes sign across the chosen rectangle. The successful fixed top chart is a useful part of the mechanism, not an excluded boundary strip.

## 4. Port9->3: one exact Bernstein certificate over the full box

Let J=[Y9,Y3], Delta=det J, and Tn=adj(J) C_v adj(J)^T, so T=Tn/Delta^2. All these expressions use the actual moving shear but the fixed actual shape and its true Sigma.

The actual basal edge3->4 has outward normal and support

    n=(-51/800,51/100),  h=n.Z3,H.

Set

    d=-k n.Y9,
    s=h-n.p.

The verifier proves d>0,s>0,Delta>0 and1-ell_v>0 everywhere on (BOX). Since beta-Y9=p, that genuine support gives

    tau_9 <= 1+k s/d,
    X < (tau_9-2gamma)/k <= 1+s/d.

It is safe to enlarge the allowed X interval to [1,1+s/d]. Write X=1+u s/d,0<=u<=1, and Xn=d+u s. The polynomial

    P=ell_v H[Tn11 d^2+2Tn12 d Xn+Tn22 Xn^2]
      -z(1-ell_v)u s d Delta^2

is exactly -F_v(X) Delta^2 d^2. It has tensor degrees(6,6,2) in(p_x,p_y,u).

The exact source performs affine substitution from

    [2/25,7/50] x [23/100,7/25] x [0,1]

to the unit cube and converts the power coefficients to the tensor-product Bernstein basis using

    B_k=sum_{alpha<=k} c_alpha product_i binom(k_i,alpha_i)/binom(n_i,alpha_i).

ALL147 Bernstein coefficients are strictly greater than1/3000000; their computed minimum is approximately3.8186988876832965e-7. No mesh sampling, numerical optimizer, subdivision omission or approximate sign acceptance is used. Since Bernstein basis functions are nonnegative and sum to one, P>0 on the entire closed box. Thus F_v(X)<0 for every allowed X, contradicting the necessary gate.

The same exact arithmetic certifies16 other polynomial guards, including every basal support slack, the top7/8 point obstruction, the top-chart9/7 guards, and all denominators. The17 named checks are printed with their exact degree lists, coefficient counts and rational extrema. This finishes the proof for ALL G>0,eta>0 throughout (BOX), including its boundary and all weak-arrow alternatives.

## 5. Exact new nonwinner distinguishing this advance from older tests

A passing older packet is not a joint metric. The new verifier preserves a genuine rational example inside the box showing that the amplification does more than repackage the old scalar test or the two tangential condition conics.

Use p*=(1/10,6/25), v=(2c-a9-p*)/k, J=[Y9,Y3],

    Gram=[[1,1173/1000],[1173/1000,2821/1000]],
    G=J^-T Gram J^-1,
    eta=23/100.

Its actual top9 maximum is strict against both other top vertices. Its actual spoke9->3 is positive and its strict actual-chord lens passes. It also passes the OLD scalar normal floor with the SAME new rational ell used above, and both of the necessary tangential condition-conic tests

    det(C_v)det(G)-rho tr(C_v G)^2>0,
    det(D)det(G)-rho tr(D adj G)^2>0,
    rho=kappa/(1+kappa)^2,
    kappa=924733153857541/21600000000000.

Nevertheless it fails (AMP), and the full actual same-inverse audit gives

    (S,U,H)=(2,3,3), physical weak points0,
    stable facets[1,5], unstable vertices[3,6,7],
    all68 primitives nonzero.

This is a new exact diagnostic, NOT the literal parent's different p*=(1/10,13/50), Gram11/10 probe and NOT a110 attainer. The printed portrait uses the common scale normalization M/eta with Schur complement1 and inverse eta M^-1; the displayed G,eta recover the original metric exactly. This positive overall rescaling preserves its equilibrium census, and the two exact matrices are not conflated.

A separate complete height-sweep source, [internal-source-reference], computes the literal parent's older local probe in a fixed-G11=1 chart and obtains own222weak000 at its specified height, with S=[1,5],U=[3,6]. Its whole positive-height ray has6 positive primitive breakpoints and13 exact cells, no110. This newly observed coordinator computation does not retroactively claim an execution receipt for the author's original unobserved extension. It is a distinct complete recovery unit with an explicit common positive scale change and the unchanged literal parent input formulas.

## 6. Reproducible recovery and evidence boundary

The complete source inputs required for THIS regional theorem are exactly:

1. [internal-source-reference], save as lift_core.py:
   5750 bytes, SHA256a28576fb18443f2d0a10e06a2a82fa9e08132e29a7aefb4713f20da9d7577195.
2. [internal-source-reference], save as amplified_box.py:
   6774 bytes, SHA25683f3d8da0e88cb2f2bb06e6e44618fd8ec19dd53f7ed581e35468c73c5d368d8.

Environment observed: CPython3.13.5, SymPy1.14.0. Run with assertions enabled:

    python -B amplified_box.py > amplified_box_report.out

Expected output amplified_box_report.out:
10321 bytes, SHA2567a7929685b178fd4427bf27c390bcb3bf1d2b8a6f3f3d32f85d99657d776d1d0.
Expected terminal marker:

    AMPLIFIED_NORMAL_W_ONLY_MACRO_SHEAR_BOX_V1_PASS

Normal execution and a fresh-directory source-only execution were both observed by the coordinator, with matching report bytes and hashes. The core contains every exact coordinate and incidence formula, the full actual moment integration, the physical inverse and true-edge census. The second unit contains every non-default parameter, polynomial construction and Bernstein coefficient rule. There is no original-sandbox dependency, generated hidden checkpoint, missing old helper or numerical solver in acceptance. The analytic parent lemmas remain explicitly identified mathematical dependencies; the source files do not formally reprove their global theorems.

Optional separate exact height-sweep recovery uses the same lift_core.py plus [internal-source-reference] saved as height_sweep.py,5505 bytes,SHA2560f41ad93a9c9172b78cb7a5476b1c8ab0b5f74e19796ca8e7dd5a973bf804b88. Run python -B height_sweep.py > height_sweep_report.out. Output26964 bytes,SHA256f1ad256b46ee97589c7979365d955441821a3103d0d57c4647dffadab0063f29; terminal FIXED_SHEAR_COMMON_HEIGHT_CONICS_V1_PASS. Its normal and source-only runs were also observed.

The next useful problem is to extend the actual regression/chord coupling over the remaining compact shear polygons or add the remaining genuine basal and inverse-polar escape constraints. This result does not certify those remaining regions. In particular a positive local gate or a failed numerical optimization is never a physical surviving joint root system. The exact whole-root LMI theorem [internal-source-reference] offers a different complementary mechanism; its convex-hull limitation remains in force.
