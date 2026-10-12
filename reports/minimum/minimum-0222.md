# minimum-0222

AI research report · 2026-09-24 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# HEX6_UNEQUAL_STAR_CENTRED_FULL_RANK_ALL_ROOT_PSD_BOX_V10

## 1. Result

**An entire genuinely unequal five-parameter STAR-centred region is now excluded for every physical metric and every unstable-root choice.** The region is

    B = [1/10,3/10] × [9/10,99/100] × [9/10,99/100]
        × [3/20,3/10] × [19/20,999/1000],

in the unchanged source-cut order `(x,y,z,u,v)`.

For every cut tuple in this CLOSED box, form the actual uniformly refilled, uniquely star-centred body specified below. It has the unchanged ten vertices, seventeen true edges and nine maximal facets. For **every nonzero PSD quadratic form**, its genuine weak-arrow graph has **no arborescence to any root**. Consequently, for **every SPD physical metric M**, the body has at least two STRICT unstable vertices. This includes arbitrary conditioning and all finite zero-arrow/physical-weak-contact strata. The singular conclusion is absence of rooted reachability, not a claim about singular strict-vertex counts.

The same exclusion holds in a CLOSED original-coordinate Euclidean vertex collar of radius **10^-8** around this entire family, restricted to genuine own-volume-centred bodies with the same labelled true face/edge lattice. That collar need not retain the six fixed poles.

The proof closes the full-rank interior alternative AND the singular-connected alternative on this region. It covers all **43,350 true rooted trees**, not the earlier 145 silhouette paths and not merely five-contact rays.

A preserved actual member attains U=2 under an explicit unbounded-conditioning reciprocal metric pencil. Its complete census is **S/U/H=2/2/2, physical weak000**. The pencil has one explicitly isolated harmless primitive-zero wall, which does not change its physical census. Thus it is a useful nonwinner, not U1 or110.

The box is disjoint from the listed small-cut and deep near-diagonal exclusions and from V7's source ranges: here x<=3/10 and y,z>=9/10, whereas V7 has x>=3/4. No statement about the rest of the five-cube, another whole incidence type, or the global minimum follows. The accepted global bracket remains34<=Cmin<=622.

## 2. Exact identity and actual geometry

Authority for the unchanged model is the literal parent

    minimum-0220
    SHA256 a0ff664d9ede90ff78b8b6b5d365997eef123d7dc6105b9e2078184ab2a587b4
    HEX6_PHYSICAL_FIVE_CONTACT_INTERIOR_FILTER_V9.

Its actual-centroid selector, labels and true lattice are retained. The new calculation does not use the raw-translated control's307 stencils or the distinct prismatoid's octagon systems. The supplied first-layer compactness theorem supplies no numerical constant to this certificate.

The literal original-frame inputs are

    p = 1/100000 * (
        (60401,-32565),(80000,-20000),(0,60000),
        (-80000,80000),(-483861,-325040),(-447814,-355009));
    A=(0,0,1), q_i=(p_i,1);
    b=(2615613/500000,816129/250000,-3);
    B_i=[q_i;q_(i+1 mod6);b]^-1(1,1,1).

For cuts in B, set

    Y0=A; Y1=B1; Y2=B2; Y3=B4; Y4=B5;
    Y5=B0+x(A-B0);
    Y6=B0+y(B5-B0);
    Y7=B0+z(B1-B0);
    Y8=B3+u(A-B3);
    Y9=B3+v(B4-B3).

The partial B3 cut still passes through the EXISTING B2. This is neither a second generic cut nor the original integer-hexagon control.

True outward facet cycles, in order F0 through F8, are

    (0,4,6,5), (0,5,7,1), (0,1,2), (0,2,8),
    (0,8,9,3), (0,3,4), (4,3,9,2,1,7,6),
    (5,6,7), (9,8,2).

The true edges are exactly

    01,02,03,04,05,08,12,17,28,29,34,39,46,56,57,67,89.

Write Ui=Yi-A, di=1+c·Ui, and

    Xi=A+Ui/di.

The actual c=c*(x,y,z,u,v) is the unique positive-ACTUAL-denominator root for which the newly uniformly filled body has volume centroid0. It is generally algebraic, not asserted rational. The rounded Newton predictor in the program is NOT substituted for this root.

### A factored positive fan

For integration only, I use the following seven apex-A triples:

    T=((4,3,2),(4,2,1),(4,1,7),(4,7,6),
       (5,6,7),(3,9,2),(9,8,2)).

This replaces a diagonal in the heptagonal base relative to V9's integration fan; it changes NO maximal facet or mechanical edge. Put ri=Bi-A and

    C=det(r5,r4,r2)/6, D=det(r5,r2,r1)/6,
    E0=det(r5,r1,r0)/6, G=det(r4,r3,r2)/6.

All four constants are strictly positive. The corresponding SOURCE tetrahedral volumes are exactly

    C, D, E0(1-z), E0 z(1-y), E0(1-x)yz,
    G(1-v), Gv(1-u).

The actual volume of a tetrahedron with indices i,j,k is its source volume divided by di dj dk. Its actual centroid is `(A+Xi+Xj+Xk)/4`; its second moment is `(SS^T+sum vv^T)/20`, where S is the sum of its four actual vertices.

Thus every moment used is a moment of ONE uniformly filled body. No cone mass, covariance or centroid coordinate is selected independently.

An equivalent exact algebraic selector is obtained by setting

    W=product(i=1,...,9) di,
    Z=sum_T a_T product(l notin {0,i,j,k}) dl,

with a_T the source volumes above. In the ORIGINAL frame c* is the positive-domain solution of

    (partial_c1 Z)W-Z(partial_c1 W)=0,
    (partial_c2 Z)W-Z(partial_c2 W)=0,
    (partial_c3 Z)W-Z(partial_c3 W)-4ZW=0.

Here the derivatives concern c, not the cut variables. V=Z/W. This specifies the exact body independently of an approximate coordinate printout.

## 3. Continuous proof, including the full metric boundary

### 3.1 Geometry and volume integrity

The verifier checks the factored volume identities and all source supporting-plane slacks at all32 corners of the closed source five-cube. This is an exact polynomial argument: the audited expressions are MULTIAFFINE, so those values are their Bernstein coefficients. Incidences vanish identically; every nonincidence slack has nonnegative coefficients and at least one positive coefficient, hence is strictly positive in the open cube.

Each proposed vertex is exposed by a positive combination of its incident supports, since no other label has all of those incidences. Each proposed facet has at least three true vertices, and its prescribed consecutive pairs are intersections with the adjacent proposed facets. These give the closed true boundary complex; there are no extra hull facets. An independent exhaustive supporting-triple calculation and strict polygon-cycle checks at the unequal central source verify its labelled realization directly. A second positive tetrahedral fan agrees exactly in volume, first moments and second moments at the rational predictor. That predictor is only a rational audit point, not the actual centre.

All target parameter bounds lie strictly between0 and1. Closed-cube merged-incidence controls enter only the polynomial identity audit, never the mechanical conclusion.

### 3.2 Exact enclosure of the SAME actual centroid root

Let g_t(c) be the genuine volume centroid after the star map at source tuple t. Differentiating the actual volume integrals gives

    D_c g_t(c) = -H_t(c),
    H_t(c)=5 Cov_actual(X)+(g_t(c)-A)(g_t(c)-A)^T >0.

Indeed, for Z=X-A the volume Jacobian is `(1+c·U)^-4`; differentiating its first moment gives `-5 E[ZZ^T]+4 E[Z]E[Z]^T`. Positive actual covariance supplies strict definiteness. The positive-denominator domain is convex, so this identity also gives uniqueness of a centroid root.

On each parameter cell the program constructs a rational affine predictor

    c_aff(t)=c0+C(t-t0),

a rational invertible preconditioner R, and a rational error radius eta. Automatic differentiation and outward-rounded dyadic interval arithmetic bound the residual `R g_t(c_aff(t))` and the derivative `I-RH_t(c)` on the WHOLE cell and its centre-error tube. Every accepted cell satisfies

    residual_bound + q*eta < eta,  q<1,

with all actual di and the volume strictly positive. Hence `c -> c+R g_t(c)` maps each corresponding closed centre cube into itself and is a contraction. It has a root there, and the positive-domain uniqueness identifies it with the actual c*. The argument quantifies over every independent cut in the cell, not just its midpoint.

The verifier uses80-bit dyadic outward bounds, exact Fraction predictors,60-bit predictor rounding and48-bit rational R/C rounding. These settings and all iteration limits are explicit in the recovered source. They are not assumed numerical accuracies: the final self-map and derivative inequalities are checked exactly.

### 3.3 True-arrow stresses

A fixed rational computational frame is

    T=((259/100,0,0),
       (429/100,39/10,0),
       (-673/100,-21/5,96/25)).

Write Xw=T X and Mw=T^-T M T^-1. Thus the physical primitive is unchanged. This is a coordinate gauge; it does not reset the physical metric.

For an unordered edge e define the positive factor

    f05=1-x, f08=1-u, f17=1-z, f39=1-v, f46=1-y;
    f_e=1 on every other true edge.

For either directed orientation put

    Aij=-sym[Xw_i (Xw_j-Xw_i)^T]/f_{ij}.

These are precisely normalized genuine arrow tensors. Exact cancellation of the five source edge factors is used before interval evaluation; no tiny-edge factor is lost or declared nonmechanical.

Each frozen row consists of positive integers w_ij and has Wrow=sum w_ij. On a cell where the row is accepted, the verifier proves

    Qrow=(sum w_ij Aij)/Wrow > I/100.

Consequently, for every nonzero PSD Mw,

    sum w_ij D_ij(M)/f_ij < -(Wrow/100) tr(Mw) <0.

The arrows in that row cannot all be weak escapes under one metric.

Matrix enclosure is checked without floating point. For a symmetric interval matrix, choose each of the four sign patterns `(1,s2,s3)`. Use lower diagonal entries, lower off-diagonal entries when the sign product is positive, and upper entries otherwise. All three exact Sylvester minors of every such matrix are positive. For any vector v, its sign pattern selects a matrix whose quadratic value bounds the interval matrix from below. This proves positive definiteness for the entire interval enclosure, including its finite boundary.

### 3.4 Complete combinatorial and parameter coverage

Enumerating connected9-edge subsets of the17-edge graph gives4335 undirected spanning trees; an independent exact Kirchhoff determinant gives the same number. Orienting every tree toward each of the ten roots gives43,350 distinct rooted systems.

The353 frozen integer rows contain1195 positive terms; their support sizes are221 triples,128 four-arrow rows and4 five-arrow rows. The largest weight is81. A row covers a rooted tree only when EVERY directed arrow in that row belongs to that genuine tree.

A complete closed binary partition of B has1534 leaves,3067 total nodes and maximum depth19. The verifier reconstructs and checks the entire partition, both children at every split, and its exact total volume. Every leaf's accepted rows cover ALL43,350 rooted systems. There is no infeasibility-based removal of cells and no remaining leaf treated as a numerical failure.

Executed exact matrix checks:

    valid row/cell applications       536009
    symmetric interval sign vertices 2144036
    positive leading minors          6432108

This is why positive-definite interior components do not escape the result. No hypothesis about approaching rank two, being a five-contact ray, or containing a silhouette path is imposed.

For SPD M, any hypothetical sole strict U would give one nonnegative true escape at every nonroot. Strict norm growth makes the selected graph acyclic and rooted at that U. The exhaustive contradiction rules it out. Singular forms are covered at the graph level directly, so collapsed-edge SCCs cannot bypass the argument.

## 4. Explicit actual-coordinate collar

Every accepted cell also proves `||Xw_i||<10`. The fixed matrix obeys `||T||op<11`, checked by its rational squared Frobenius norm. Throughout B, every f_e>=1/1000.

If an actual own-centred same-lattice body X' has `max_i ||X'_i-X_i||<=rho` in the ORIGINAL frame, the working displacement is at most delta=11rho. The operator-norm change in an unnormalized arrow tensor is at most

    4*10*delta+2delta^2.

After the positive f_e normalization, a normalized weighted row changes by at most1000 times this quantity. At rho=10^-8,

    1000[40(11rho)+2(11rho)^2] < 1/200.

The old margin1/100 therefore leaves a strict margin greater than1/200. The identical true-tree coverage applies to X'. This proves the closed10^-8 collar theorem, with no condition-number restriction.

The own-centroid and true-lattice hypotheses on X' are essential. Arbitrary independent coordinates in a box are not asserted to form a convex homogeneous body. The radius is stated in the literal original frame, not uniformly after arbitrary affine rescaling.

## 5. Preserved actual nonwinning body and complete reciprocal censuses

Take the exact cut tuple

    t*=(1/5,24/25,49/50,2/9,99/100).

It lies inside B. Its exact identity is the star-centred algebraic root specified above. In original coordinates c* is approximately `(0.058941053,-0.025206093,0.028111243)` and the actual volume is approximately0.872710253173. These decimals are descriptions, NOT reconstruction inputs.

The table lists working-frame metrics. On the literal actual body the pair is

    M_original=T^T M_work T,
    N_original=T^-1 M_work^-1 T^-T.

The source verifies these inverse identities exactly and evaluates all68 genuine primal/polar primitives at the SAME isolated centroid root.

| Working M | Strict stable facets | Strict unstable vertices | Strict saddle edges |
|---|---|---|---|
| I | 1,3,4,5,6,8 | 0,1,4,8,9 | 01,03,04,08,28,29,34,67,89 |
| diag(10000,100,1) | 3,5,6 | 0,4,8 | 04,08,28,34 |
| diag(1,100,10000) | 1,3 | 0,9 | 01,04 |
| ((20,2,1),(2,3,-1),(1,-1,1)) | 3,5,6 | 1,4,8 | 08,28,34,67 |

Every listed control has physical weak000 and all68 primitives nonzero:272 nonzero checks across the four controls. These are all the SAME actual geometry under different physical reciprocal pairs, not four substitute centroids.

### A complete full-rank222 pencil, with its harmless wall retained

For every real L>=100 use

    M_work(L)=diag(1,L,L^2),
    N_work(L)=diag(1,1/L,1/L^2).

Its strict census is always

    S={1,3}, U={0,9}, H={01,04}, physical weak000.

Put s=1/L. After multiplying each primal primitive by the positive s^2, both primal and polar primitive signs are quadratic in s. Exactly201 positive interval Bernstein guards certify the67 primitives other than D57 throughout0<=s<=1/100.

The remaining polynomial for the scaled D57 is strictly decreasing in s, positive at3/1000 and negative at1/300. It has exactly one zero s* in that interval, equivalently one finite L* in `(300,1000/3)`. At that wall D56>0 and the true polar primitive7->1>0. Thus the zero is harmless at its source AND on its edge packet. It is not VE, EF or VF. No physical census changes there; away from the wall all68 primitives are nonzero.

L=infinity is not counted as a physical member. The finite pencil shows that U=2 is attained in this newly excluded actual family even along unbounded-conditioning sequences. It supplies neither U1 nor110.

## 6. Discovery versus proof; remaining scope

Numerical discovery used the actual star-centroid equations, a fixed rational working frame and LP outer approximations of the smallest-eigenvalue maximization for convex combinations of true arrow tensors. It produced783 rows at t*. A genuine-tree set cover retained344; nine further rows were generated at corners of the proposed larger box. Failures of the smaller stencil set were discovery diagnostics, not feasible U1 systems.

Those numerical corner tests prove NO continuum statement. The result rests on the subsequent exact1534-cell centroid/PSD/true-tree certificate. Its standalone verifier imports only the standard library and performs no floating-point feasibility calculation. The complete optional numerical source is preserved as a second recovered unit, with CPython3.13.5, NumPy2.3.5, SciPy1.17.0 and OPENBLAS_NUM_THREADS=1. Its clean replay reproduced the frozen353-row byte string.

The exact source-only build was executed. A separate empty-directory recovery, build and check regenerated identical report bytes and identical build/check stdout. These are reproducibility executions of the supplied verifier, not an independently written full verifier or a proof-assistant formalization. The independent support-triple, second-fan and Kirchhoff checks have the narrower roles described above.

The entire fixed-six-pole five-cube is NOT closed. Outside B and its explicit collar, both actual U1 existence and further full-metric exclusions remain substantive questions. The new353 rows are continuation data, not automatically valid stresses on an enlarged region: actual centroid enclosure and row-domain verification must be repeated there. A failed row or a failed cover is not a witness. No canonical incidence/root-orbit count is subtracted, and no global complexity bound changes.

## 7. Complete source-only recovery capsule

Save the entire Python fence below as `recover_hex6_star_v10.py` with UTF-8/LF and a final LF. It contains BOTH complete source units, including all353 integer rows, the entire1534-leaf partition, literal geometry, centroid encloser, true-tree enumeration, PSD checks and all control inputs. No old sandbox, parent program or solver output is a verification dependency.

Required reconstruction and verification:

    python -B -S recover_hex6_star_v10.py fresh
    cd fresh
    python -B -S hex6_star_v10.py build > build.stdout
    python -B -S hex6_star_v10.py check > check.stdout
    cmp build.stdout check.stdout

Optional numerical regeneration, in a separate directory with the pinned NumPy/SciPy versions:

    OPENBLAS_NUM_THREADS=1 python hex6_v10_discover.py

Exact pins:

| Item | Bytes | SHA-256 |
|---|---:|---|
| recover_hex6_star_v10.py | 23342 | 10158fae7b95df053c281613d65b5b58a1389ab2d4fb4ce9be410812ab88ce6a |
| Decoded two-source JSON map | 35937 | ef977f344f9dbe0dca7bb5b02ecc56c4a7d3585713b8e6741662238038d5bd3e |
| hex6_star_v10.py | 27848 | 96780eab38878b1062359106ac65df4b0f7afb60c75cb853fa62ede62bdeaf43 |
| hex6_v10_discover.py | 7358 | 530e578159d9c791555b8530daeb76f8788280eea1ef5a24ed7a89915f371e13 |
| Embedded353-row JSON | 10365 | 8e26616c7dfe0d13f6e32500a9bf03374ed423413f11461786c1ba1c779598cd |
| Embedded complete partition JSON | 44186 | f702f89d5e1ed35319292c409fc2cbf446dcfc5ff0a549b0fd6adb31c3f7df97 |
| hex6_star_v10.json | 4929324 | db0499e25a7d9f3d873e3c5fefc7f992f325b3506dd1649e784fd8b796493eb6 |
| build.stdout = check.stdout | 730 | 81cb4e593ae1d3736601f6eba93255f4b2446686a0eb26385d0caae94710188e |

Expected terminal evidence includes

    CELLS_NODES_DEPTH 1534 3067 19
    INTEGER_ROWS_TERMS 353 1195
    TRUE_ROOTED_TREES 43350 PER_ROOT 4335
    ROW_APPLICATIONS_PD_VERTICES_MINORS 536009 2144036 6432108
    EVERY_NONZERO_PSD_ROOTED_SYSTEM_EXCLUDED_ALL_ROOTS_PASS
    ORIGINAL_COORDINATE_COLLAR_1E_MINUS8_PASS
    FULL_RANK_222_FOR_ALL_L_GE_100_ONE_HARMLESS_ZERO_NO_PHYSICAL_WEAK_PASS
    HEX6_STAR_V10_EXACT_RECOVERY_PASS

Convenience copies: complete recovery capsule (`recover_hex6_star_v10.py`) and exact regenerated report (`hex6_star_v10.json`). The literal capsule, not either link alone, is the durable handoff.

```python
#!/usr/bin/env python3
"""Recover the complete V10 exact verifier and optional numerical discovery.
CPython 3.13.5 standard library. Usage: python -B -S recover_hex6_star_v10.py DIR
"""
from pathlib import Path
import base64,hashlib,json,sys,zlib
MANIFEST={'hex6_star_v10.py': (27848, '96780eab38878b1062359106ac65df4b0f7afb60c75cb853fa62ede62bdeaf43'), 'hex6_v10_discover.py': (7358, '530e578159d9c791555b8530daeb76f8788280eea1ef5a24ed7a89915f371e13')}
PACK_BYTES=35937
PACK_SHA='ef977f344f9dbe0dca7bb5b02ecc56c4a7d3585713b8e6741662238038d5bd3e'
PAYLOAD=(
 'c-qCid3&--(m4G8`zdr16%-S3H%b!sec#PV2qG#jpn!Xl&;IKL6qDR%&dfE>_0F6-LU(m_b#--B^+NUOUsGWpWL1q**e&h3TOI!O'
 '@UI)|{YF*phoW>ZNL$P5piO1T_m}k7zu^DVdydyE++yKYWLdM+nkfq}D4IAHc}^27vSi^b5TBbDBux=Uma(`M-26tf<kGz$fL$!^'
 '{*sb4gw^7^qkVUQC@dk3IAvs6h(m=_4gk;M5Vc6MWxS9%O_U~<l`Kk{MU*UCLBX|&vUF#V^_MhO<fUb-0O~-xY7v(!S<x&RJ;B1M'
 'mW&Q0YJgx_UYvn=c?nvJ5USKlkw+U|(_vSfHU%^pkTvl7m!!YUR9T{?oC*Ob^`KHqkV_3YRS5d2BS`#9YBF>z7WVul@e58>E%}GP'
 'Bn!)`3t3ZHmLVJq*+Ds`qJsqKBVi2kL`l?GmQaPonBo`@HDoHXB#^M6g<~=VM@EMXXA#F1K$L2MnHFK83YH8pgjg)F<lRDM2+r9g'
 '?^qTvP*wm&GKzAhB0~&u4ljrclmSQs95G797#$E`dj=h&iTqLky*1KlRJa|%QA149k&%Zpf!6>!N!S5wc`|y0)pOtn)HO7ab20F&'
 '2--%GEXQ+exzPxeIb(zWK+8l`l%PcL0x_ft<bz(UB5V2OY9TCvWC@TO%a9SbpxFlA{2ihVRPP#sKNJTj08dkqL~K`3ZH!*)nFdLi'
 'KpM`~U@UG}m~um8m(Ec)LxWr$m~#>C;V(4fK5--RF6EV<2oQwJ&7EPEo5lZvB^rYm;nW#{o<M_OtDI-%I1T1luG+p7B|;<b@0*mH'
 'AlyrC58mJ_sq+z$$mpb=3D=a3FcP=_3*vQ|85(3idQ3EOPE2Lf*}T6;je=ByHxj;r?lSTF8%<`O-y1AnauZYUX9(C{Zm1&mkraLc'
 'Tq3Eafp{oyq>*YWM5vlVWKanJMN-Bqpbfm5=n+=Rm8`)80H-5_kXTU^zAK6?&=aFSsEI8#(v<`nxLan6hx&*iJQV2+z%CeFD+_G{'
 '_)d(-KMlkoGcymY0-$jVM$(qT1^2FlWh^U}J#~N@`6#Xcz=#^&jY#r88fyhO&J3*XJw^&qauC(ujypG^@b8A!?B5Kn-x}#OH4;9%'
 'VA{WJ>^~k5zg2mEsS?-eMs<?+#1PX%{%!StE9o;s(jgRh*`IUv-v;LXth5RM3KtOnzCd0tkUtmL3cRUvahozA*VL~%BoK=$LjNpR'
 '6jGqD4CvwC%DDfw49@`=jrvZN=G^}zY9wn{6{wpf=#jre&nvR3UX>xZ7y8vXeDS`zIq(NO(XW*L<bi1(oJ;9XG)$v$u0e*NnYf6E'
 '0-2Ovmx0e90jQeqje|rwIRjw11qANDfk3PZrT2_tX2Np$3zN--cwC5wg+S$i7eA4R(iTz$#goC!F?2fA^S_|p-;XZ+p_nj&8i?;L'
 'KeIw-<0ZiZ6KKF2qw&H)AbxF2h7cKMhAWz(N;zpF5I(&%;#HE~F9&V}#9m^89+SCHpza1@LI6)s0=ggl{3X?x>)Q4d?ScO@jfE9{'
 'UcqOA2zvY;nsWQRfnb27h%f}E++I|M0*XASKe=&E*m(7aec>Q32r!@&e<)1*K}sOt@k9_S>P?-Tl?%{9la#6I8W~N*n+zPggu@%8'
 '13}t%A3($cqZ6isv^R3^4d8b-;zp|xuNW9%Idg|WB!S314WT_0B*@|S>hBI8d~o1YcQEABlignWJ^+3rK~RwcQJjb;iwqPaR2LbI'
 'GfVxMLX-m36pbNuLeBZ%0Tv|c%@^^N0)Gk7MU%GRD+SsKdWfJY8kPOt(?N(X6HhV_y`KtF0mS(L6$0S!iKe{h*Gq-bZ<vZuKJ?_H'
 '{NUFQej^~41|@>vJpgcoz;6UVdLi<3N+(tY69{2MoUYyok(wD~!7*e3v|t*knW22f)cA#dcy*0m9)O&GLZqp*j#MxMr&H)nz<mNS'
 'Q^bq{ehe8+=b4l6AnMQvLXb8~K>;&3B9$gTK@X=}fD5oaUeqox;(#Bv4E<iW54GCd&P3a2C(zkzDvsN<hBYNXb|<N4L*0O%5^c~~'
 'mktp}DsVZ2IANsXMg%~ocu}>OoB$xlqqE(MWI<Ol(1GnFN$55rvm`G->r~*yLX8A8Id!Bq)RxhrNh(F9sVvh;Ueppw1H;*UB*E_y'
 'J{?G$vL~Gf=aI_7=Pe0-xA18LDlX?!`Ut|3?Da!QrX2nV7)tQ{J_6+%kAt&uk~a#lq(8{I&_cwi1XOzosOl0ge)uN<bR4jr38?I_'
 'dD~Nv%@EWBRp0mQ1Ik7P{{V5+A?WWAJ_BNNuEO_Q_EtxL2=tls?^1@|JutvLr3$<(jhGg2R8WJ>BC<C`1S!TdU&!c42clij`0&&Q'
 'gKZ#Kn~e7KY)DRAr-i-;Y}7~5hB_Jpr%hpxvcq_ySq2(kU$n)%pa%rYnpOTQfYfD=0+S6OK?WW$GN_9{VYhC}V3>Qj0&oXc5Qxza'
 'aYle!2GB{mFx9;uFj4i)lqIo#nY~`d&35~nv5IzF%obvXS)4fw5oXE0aIXNuse<2oKS}~_9PSDXfl3aqO11#-%Mg_#U_nqCykU~S'
 '+Zw!G(M8^S;RJ2M7`D7~>B}r^ckap<2AnO>aL~B>jyvF-fM@V$_Ua<wqdN}%kWK=ofalrkKQz&oW?`ok&UG&1s7Fnx9Mz$K_krbd'
 'r2uc4*JMQ>eLMr~BG4tI(`WR&cEJzqDq_|d4ReueQlI1+(?-3Uwy^YsjAfv;iNyi{!%z{pIa;F8gcYM(sT@g7z<hv#RvG5)rs6`d'
 'z(In$hvyAdiM$V&0%iu^9a1p107fL;m=vJ?^Z~=8fq4MK3zs@vkFQ6Mg##QjXg^{gG-fU><VomK#eM^tm|A5~?isJ)<|&VQ!+jn^'
 '7SHfJ_=R2bpl~ASpf~~)Wht#Fpc@=;y--llN}tg;XujLHk{!f_Bjpd9h%kE}n5D3sPDld`aPXhrQ2ou>04;*9H+rY__cIi<N)2Q^'
 '4Ef=yh9Nlun4-(-MiGdiyr)LOa5G^t9B3C3k)>#8EP``^sh1ZIObQJ!P=JhTq7INpe)f<2k#@;<FR7t>iD3{lwKV!1Rt_oy8i4mu'
 '4dx=xFcA=<%{)3DFrU+>mm=uTU%lSI*%_kt*WLiC0*-Bf&X9<ihXQrtHUqwa+~m(bg4&`1hxr_g?wJSt+>H!<HoqFV=gzz)=vOz~'
 '!gFWt@E)iskeDZ-qc_t2P)3{mFF2uzn1Bm1o`coGy8lq|WOm^h#m_D*iz*WjQ~(W1&j)P2;wgzlPd&F4z@x@Ou3mHYZy4(wX-39B'
 'VXdHX3>@RfJGdfd9$$h=I=wD^K>Guvt|2*16P7EJnhawt$r}>RyYhq^pryb+)1;B-kV?>$!^2O7DpEXNkrej40FYm+iObR<((aZu'
 'q8M@nFbQ=i@X<{4&%XDfBJa)}44%IUJ76r8!^<ibNf1VV=7($T1dW0^0cqUzBSU|u4J1PxF#v~^EYQkuY5am{Wa!@xNPhHSg@3kK'
 'yhs6Vz)=lEok63#K_!_a<R$~T3XGkmZ*MSbN?maL9HzTrtw1+O>`0IpSZfB=OEpPz)w&bIbTGF8POlS|yeK`~5PiJ{aDS%~JqmXa'
 'B(={Nc0?qjW@qkTICIF@^nW;U;x{i2;JUH2fk_b1-VzU&mlg|Qq}wTrFq(jw4F|QGdS|H!TS2jm#H~0I0P_F}U^ceg!ZJJ{M4V;I'
 'NuoN1mIOHG{0686O$KcO>{2yl18UHwf~l5~2=esJB)uBu1gCxEg9lCW$Oj*sGls|qFPiF*4}Li32$B!<CoCfFfu!gqup0~<>o}>G'
 '#VJ0Vg0P%npu<h-D9>Qfi6(XYCdj}moR(SSjmEs3ol`v1OQn(I2+VJjNwjdz?HEMmi|`7?63zHf0``?)HT@R>Q1eQ`U(f5S;nj$b'
 'vj<olyVh<RI>RV$B#y_7;cz2w*9p}SiTn+m4igc)?wISHk5b@lPp1wv>5f~i1ZhN=t%w`B$I#z|RY3<7y$|(w?$t1^!=J9<l_N}&'
 '7m)^aojt%23v4J+N3wilNg*k)sNzI&0|C>7y+spL?Ez1sLCOKRbo^A70l!2|MSv;=-8Fs+cg_U3WeD&r<Q))Cxc4avD%=iT$*QP{'
 'Tfw4lEUIY4Z$N{uz$9V9AuurLR49qCcJ<QNDov?gv}%OW5U?}ABv=tv0;e%vta??I0WyYQ5pNS$hFRPab?kYQP!GZG1uD}5v8%8H'
 '!QUD5fsjy`fv4g>T_>|xRx1X{EEZerZY6YgE1|nv3G8lB(9ueeXAc^vs?~~&F`o148nlPVRzPOBn1!fn5X7{G2s6&E8BhZosK}vn'
 '1ohPq_Y631%r6ccL?|NH&e$gTrpyg(3}ghBk8&LIO(RApvOEIa6$PyT-3H6OqPc{^jl_-WJsT>(*Q0KtoKEjWBb!&rdpbdSSzuf|'
 'o^KQZN?sg0S(yVp$6`2EU2izx2eN28$??kQ#dQf%B>AVwgKfZ~(`6uaJ43Nh2oRb}m|4G)BLwK=xR-SP1%ST3;`!pwqW4{Q9&Us&'
 '%n&Yr>N4|h2dvTK%z2FJ5`sn~vXYS7hSmTL!&9FhE|5OMT_P(83%|@C9(=DP>LlPfF-u+U;LG(687!e^P)of#V5JX;@gPT5STxo#'
 'w^hJyW2x6D)^s|Fxr^4DIRDnfiwr}wP_oXpcCpYDK~M=q|CPoU&`Oy3yaJI<LGyt;mLc=<^7?%(gZ7}s470%y)CXw@#<s!085srd'
 'v-7*CA0z<o!^!g*U2lYq09Q=TXdn`l`f%nuLX5ELOb7g$StJ>`hY-~R{Bs8vYCv_U@TGdadl!O4Kq%4*1pWcKH=?u=j9Sro6LYh0'
 'MJo=NYnb-{|D36XFRy3nzEk`=$yYQ3ybs_XU<)JuMz7g!5wJE24h!HQqd@^nim$KVbtIq~sa-1rOOWP?Dr`JJNivMz=L>j#wOIgA'
 '<QC#l&^K4EcjP!KbJ@B=+d{v9<S$#O=WXX-z@XcChCD%RbGW^1RIe{`%&9HjtQEmb03iDO1ryd86ja^h8RN?Z)z$9c>!sPixxTTq'
 'rf^Mr0R|d$=M=yS5tv8djRMyXu^zZEz`27Cod{k~ilpg|Bt9r4D0c??fVmMAFgiI&(-{ax46-RpZbf9M%j7`UliX`mVqnLhEn9W7'
 '(2RAOZ{|?K!Z>FnVGm66{QHQXQ4;F-A<zrROG5kgy4cUZ8y&b3W#n0z*#j&^!2!y^KNNg5$Z_LeWO&7`tRV>SpPuhzP^vM6%oMq3'
 'N~ap6z;cMP`!hT$u=r5`!7X0hz_@5mRN2DRX$Ccz-@wyjfu39f^GozE$_(z*0D*!#JS4RyDacaO20^{~>bi!3+cp@=(1XVA$V=z}'
 '4_=AETY%V=9qX>_7`d{Pk?1ugl2P;cl_=<(N|)T<eMac?0sFcHLlzi*88xZH!0w6`wwDz|w5|+ajHPAqx20t;)e!V%JQy8h5-FO3'
 'f(L;}H?4ORTt1em-V02HbQ+H{)1!;ly?40n!CW?2AQQHL=F95jb_;is;5Lh~Y6nU@GU%)g^dv9FehbZ`soZZC4Xs4W3&;ql<O^G4'
 'Yd~Jy`zci=FE;v@b?U!eg_ajiLd6Tw=auL!eBBye$M$+9TJO0IRWMFgzyXdGQ41U2%l-??ZAPMojjga>0Y@H8=im+?-t)sdet4J9'
 'kM{%hsU4iodG$#hMc_R_FEGY%M(5Y(b$B9&cFNFS2#NR1!XVeA{?jRjF=|IM1lapPG=M#boZnMv@apqlO2O{M8>IS50zR^^H!Cre'
 'Z`xc3N-jow>Ax;h6EJxlQ(#h${N&5{!aWfo|764rO9{u}`1Mm4YcSzfujVOeRG`soOjZK8)6WYCu*lypA)wQbXBkC%FQ^dnV;}L~'
 'ZX>qREz%fnV+xG<Df!JMzS3Ic#l;cviu(n!ZwN15dzrei5;>4(4@kW5=fOB-iD30nh8M(j@52mW3`5JglU_g<y?!t_*K-j8;4Kmc'
 '%pIHn3HTt{g}vo`3OIPUMa*^UqGRX+Fe+dld0AAT=0Cj5bI()yh`m<0GpJa_v#OozuZ9(q7zS<F1E0<8)s4VJ39}6MIWA-B_gB-*'
 '5cDKq3Y@IMnG|?~^F%~Gaw^A)d=w<ukOj6}-&g)X35aSBSZ^M8m;s0bP)D56P;l%SJTb`$Tzdyul+Hu);g`)fq`1wJGyFpyKE|sL'
 'Bj_t}@Swsq$a$zEMqOJuGrVrwIJ3bUni5I8p>bo0pZCd-m!zN`<`$QQiZKVcgICFx;s~F+KJPDB_^H6pRfGwz*{XNQO}juqZ>HJ;'
 'x`|)F=_qv2h5|yTFYv)-4_O=`j~*^{eA~f5^7><C7^G6X$JBF3C~%`XUaH`wT3+VbK%Wh=sZ__yFdd{S3*ZTxs1Aiz0CGRJDZT&u'
 'eaZ_ZpgJZ8UQ2irn)du*=5}?a<Dmpe5`k5uqb2O>;YUQM+ej7RBPcr;6@EIE$79Cq`<hz`%mMNO%od}B{elar7c^*ca<Q;zbsB4A'
 'mX{StP*ld})t8o85jx{QrUaGodi`L?NTS5UL|}B09#fHXZ3rGoK@Ub{;P8TLzA6Lewm=w}%a%K<F9S23BsEsJrNH1LKNkYePZSb1'
 ')(~%2+sUA`#3K2{rx4D5fTn<Uuuyp5fk${4gF$B>@pNX7SLgL6(?;S{jGYtRG+OETWnYtUY$V_n%Zn{s&;~U)sQu-<@0o<v^q`7B'
 '7+EyjurtC*s%f#xI3Y@zCrogtoR8LV@UsUMsgs|}R<bf;06_HGD%3Aa3qZkP(fjVRTa>e9i<42fr!aLXPJJ;qey$xb4CIlBS7^z|'
 'aITF-VvviDjYzs<sK8}2(xhVzhxnqip$>kyT6Op~`NzhTM&#9jk)_}o@p&H{m4H~UY%lu6!4t!l6o2NR+u?6e`UWs$-Q8w2f&@XQ'
 'gMpd|h}H)57SGCxI02(-!QcrCcE(`K3=my#&u|#wivy=SUhgkH90eDiMKA;|(C4FVa3(}uuMtu!dGRakg^sm(US*!t^mM<tPU^y8'
 '2qI9<>IPUCxV)_&(|Hm9-~mF{Lycj*Ma;njoI-ol$jw3sjCBDtlNF(zb<`Y4`Em>+BJI}He!(C4uhG}Pq0hl3*`2`6f9#q7U5X@&'
 'nlLX%ybSvX3A_>|gnnkcz3PkZFNmHO&^ih(h*Fo=8SvVS*SdoO)tO%>)cEz)bbtg*lYmmmo#&-!4+m}TEG`hhgL!~W`T?cOFH`_K'
 'd?>@Tw$#)}7yNCLZupY}XuRJPd6Q{sRGVp2IVMM)H4@^U?!Hk+L6O;&A}*1}1`VGJ_<S_@#U9s>o`D|M>sisEO-p&9FK+gzI)yYI'
 '^IZW(g)uy&sBc{89XI~HbD;AkkTK-MjdiOl;68@4lBEFkyUGygFfavYBs4xft4~cl@KC5RP4WClGNvzj(f_O%stBb1>9DNVqaSAU'
 'Qa;K}qv@m@A5SH(C!{YlJY`D3Gne64>II%g^}`dWaJTTq2h&k1NJA+A8ogiV(>R|zYc|ssQ<)-Q|DWAloo|#ugZ>d37OC>pxf=b='
 'S=Kjt%KAo6`Nz4MGWOUk6?C|_d^R7;B~hj-KqyfsMNJ}h`uw(ht&dzZbcHe6fw(L!;FC002VNg8$k31kFs}@>7(L(^!_&fL<S_Su'
 'yG+3((!5k*-~*Kbd|<qO!&f)qtLykG2wxrIt6%V;fx(=>KzX=!IIhRf1^IbZH423HN-vxGfd@1+9j^=+x`@Z{y$#>n=oRV$nDlMj'
 'IuOUoG6UFtu@<Ng@G}{$piE?Tz;A^zR^!O4E|aN>Y;+p_Mhgj*p_-6dDYI~&iUHk=A1YM&VzeNJ%UeaJa6=g$eu;UOfy*O_j|*e~'
 '%Svcp%(4MamtMt4<R)PJl&I31m!vF}t5o{F1pk4YJ3J2>1CQ9U+$=P4wK(8|XCm->^s^3@;lWaRb9*UhhfKYK7N6G}ZUj9`9#4dz'
 '+G7CjJ4;m(ERfe0d2C4qLeL+Za>^3eX*H^EBg<eWq#$X4xmXk+MQBTyL8okh%82r^0NmNrXH=J)&*)^sU5(ev_CJC>TOa0fx)h!f'
 '0uM9z;MNmNi+6+<ouIzBU=yTZ$LDo~hi^mgdK~E0)~~9q8`akJYU@9%#V6^FYN6=E({1p}6146Buo|-eV61}+2ZkYF3*j2t)hfbJ'
 'P$UMF=UhW4;^Dpb^6cXAFaC?i;e;`dKUf@|d5)UaQ?AD+m?lmxeiwwljAv;7UO~RzId{TdyZF57ghJ5Yc6l%;w7(wuytIc}4bp;P'
 '2n?CQTzVC>8Fu<Y2IApEACi#Ksfc97=P}QT&4hC<`1K_G1ODRyYFybh2>b>V{sI3%5Hyb&35vKyhY^^eD-V}Ib?!O&^H)4)5Ht-k'
 '5pZ^VpuIWQd3Jb06b)1VLOWEP#+eQ{AlU;g@=(Tl_eJd?J%W#1IGv|Y^5b-o1$FZIt3pH;@LDG#b9he5p``OduOIJ|V!8|k#;fEv'
 'CrNi#;9tscW^|_>s4OsF6Bi5uEU{p^4K);nI#T3CxLAUFmC}150mMVq1W{u3!3{(L9^Dd`n<Y-t4{+^G2e^<J>Ow@}V{-5a*qI~L'
 'MiSQ>fkirBWsL(;3;|F~!NkPWzn4c!?+^S#L8p%$D}um+@xYeweEBkAUM)n8U2zJW-OFGG&uLSYg2yS~6XS5;`77=alzEnO^admi'
 '@AYc>yFSx)IPlIZNHY5xC;@bp!|`f-Ir)ML!YWa(aeL?}tiU+FeAk3ZeMU_K4?>Yx`nbKQGSJaP8+I@v0M5NwH!wqlK(PRxP{37I'
 ';LJe8j#9(%tr|%Gf|@dbo)=gO9s>bB+rl*^@4Zntk-x|}Jh!G}dC(8cysTcl58p|L41rYw^#h8$8g#8zNa+pnVHk8|csRtBf(p@@'
 'VB`~nGGIPba^T|(=!EGMj}u9CF+X~6rF*DDFvEh?yU-3Yz)HFxD$^(c<)Iujs$DkGZ>5_+#C^d4PH5)hj3X>~gF!mThel(;GopRt'
 'pa4Hk^Kg;j*yHns{KClZ_4z>tP5Xm%C>-SJAxHC}P$Uou^CO3jJRD#MP_2V^%gKF3t34(C`@EFkZ#F`#)e6l$A7TG4ISY=tan2gb'
 'Y$of4HTCY<ZNp<<u(^BxqQBY^GI#2a6NPS*Wzq@XyDuI)onp4~a{k15o1>>rxt*W5dmRU?i1{iJp8m4T4Xd$YmiAgx!X!MlZ%%5v'
 'Vz19f)wMg^larhE8}ARUCas<KQJTF?)LGxtn50wNMm3UCJk@DCTU(XwLL#}8W1ZxoA{F!7H#xtGAM<-uQG-oYBc3gpthq-wwuMs&'
 'FpXrg*sr#$UEg@64paVszoLn>AjrYGi~X|l3C4HZ`)nxA_`o_So!%SyetBg}Klg~66`N1)7Ks9156tqnq?a8}ru#OkXp=qc%YB=@'
 'klwbu^@DTROs9z3qEmSi)9;DN2f52hTkj?=&>zvy<zaNQd+#dr?SP#$H;MLBDVrOuS1FguZ^(ht4`fTt+T+@_vlgmNa+zGbt=(l6'
 'RTPl7K4-?)*=+}8`51SLrGr@QclWtq-n|?82T#?ndThp7BL`b(#@3%j@~ss*wQ{{>a5>(!V|_VpO$6GsQ`;)Hv1o{Y;-eA4w|a{^'
 'gMpi5y2RJIsG?=6zAwhS?uAm1_{)pHmVe)QKHbA<Nx6v-Gdj=5QmS40Oy+!_w+Ht5w$`YM&E3W}IjIFtKA2m4(dj}Y%8d5uTydK('
 '<|3cZ9skMhYQ*N`t!r4T2T(<YBwblde1YvY;R$fzwR6*8iQ9Q4v<;4mHl-YGu9cWH4Ys*tFKIvcB2#N!8I=-4G5O}ShL%B_Gt3`S'
 's(cb!U;AOZ^s!GrN79wS%AHP3-)!&x@*Ap%EPkDCvsEkaj@iA9ynX0Q_9Jqy=9b0f{<wW^e#!wC9pei8FkE|6k_}H{mXbafk>o5B'
 'F5B#$?b|JPt9*5f!^C^-#FtuMlSP7AR9i#uX5u<|`u-rQsN7bgkJ{;xE=&@~T(3t==O537Adz<sN^!d_scCUm`s7Bvh1*r=@wr`)'
 '>)78{)5_q3IAolq?qv2A?-V@|UpqLt)#hsO@n$D(-A{C7AdHTl<%)EnifqmC?6dK?DO7rILTv3_Zz`OZrP+FAvfVz`?W=Nh>CTNG'
 'qj`JuNanvH6Yit_d31W$)lKk`vv+4PuG~GWQqfr^*$tP;?u{*Gm9>3IE2wK%d2n1Uaf^a#p|Np$2L5p65S<O#P}egf-J&ZX`@P40'
 '=A-LPO&>qRL2CFpTeo~pmx~y^vl}HI4r)rVGLEOdSS9P;WYf*#VR$QVZZp}X@0L$_W`(9wym?&SqKdrTlv+<t`q9E|_=|fE&iXyF'
 'rntSUNU1`UL+_Kw&FwMYvo@UXAJ62x<FVCM{!>V7OVX!j>vE<&p_#XJlkmyA{J_@VuY5;a!9&l7)pcbputGc;FQAH=D!+WRjR>#$'
 'v~4{04ubFS_+E9T_*zu>IOLwH_M@%a7^Xc$ZxQV>YG~4l`379zDA#>`iQe_&8+U%>UliACQLXyIi&(y&t869PfqP36es`x7^`VNC'
 '!MuLUX(}<VZT(5^cJ~>7f1@k5WKy-p#oaPIt~Lu@SKBoWr|rU9D*CZZWXr;IYD;aOY{l`!+P~dy`fran{y;OrHj>QqwqVc2tR8V('
 '7dzc)H`hlMr96?tq5HX$T!GN1ZI>mMqjIwMRQMd0{G?Z{x@LW^-=5e;teyCJyng=dZNi0pr{83badHy2b{9*wT7GmMY`I>x`YC0J'
 ';NT-jYtQwxFPrTT+(goi`zRUP-EP8UA>E_3w>aCYJ%6_3Se|>QdA2NeY42dy{&Ibcx1+UH>so`JKycl#tv#LiWN91EpS`|Pf#rsq'
 'wez-Z^ReAk*;9$Jy<}z>D>ZlS%#)l&71f(IE@pLoo<cyg5#{*ThwwyrY_s)vx~ZHFo<hSu&c>K!{rI#ZD&eoZHT@)iWXi=}CDSY~'
 'vI)<Q>!zFiRfu?NaBH$STg!P#4)s&E&sE$i&3A=3s_4iLW5L8T|9Q%YEw${c?@IRWGW7NV<cX8BV4#F=mzmVpV^94e?AiEmw-?{`'
 '`{nIkCR`CY{keRPHYVGmozL%V#iDoBlK1IkOR3pvlln&~Gf2Hxa37`R<MipV6<QS;*RUA-diIq1AJ(HcxEQZECSL8mkCnGfW{_q4'
 'zTpQK+OXY}HJUB7ot<!?d7Ef@n9AFG)!Uv|TAjU3UWwIU@{{o#aznB@vES^ASbMwGZDqJVY5jvow5{`5McUm|s_!4k%2RFCYJSv5'
 'YFg^q)LuU}^wN)VSgb1kU4Tw(ibSxHh&{1Sg{l;I5_j3h(0hP*cQ^LWo^Ggm+NN@q%`wq^JfVu-OSM)-$>!hQ^V?v<S{Tr!;3NMr'
 'r_~G}9v@O;ITTUV&OGT!sZ(j9C8X_W)hMruM3}t^4%!J{NLI=nzT4uD>igTHW~)TV@~Fn~-bz2%d|EWE*upx!0W!<nwp6wtM02yH'
 'A`EM9%TxHPTyxocw(zNXNY@_=*_72ukd+P-X)o4^oK;QUjQGcos=O(>Zwl_(yVg&RK9B6|qY_k~8;NK-R*f|_Y0bLr^H|rNV&q%>'
 'i4zj@7QfC+XgM<F_l3mm)?PT&j{Ht(mHJ$(GT%FcNp|wyeix&BPRk7TveG=*+U}KAC^*Bjz(7^~_C}LG(evj)^T-rpPjhm1JQPYY'
 'swhIs#3y({-hM6K%IR*N-%p2wdJ6LM#vzY)9FB|v0xgVu0UsUlM!dY=6B+YfemM5~gCl;-2gYL$7w|`hp7AKijfOs&_l<#T7zsHH'
 '^d?6yUCewg$J(qh&XCLTQ>fin=GkHSGcT)89_QD1YmGBsbLVKB+1u5U)#@dVT`n7|=HK7Bocd9I<gAY*VOyS*k8VP!h1GrXUAAhK'
 '=j=FGdCq53Sl&mcI&b<T_#z&~-T(Cc+dm%(`Gc0;Pdj1Ti3!$~tr|YoD#}S47lr4^-u+%|)cHjy8OJ6!H9kBCR@LV2^bbk^;HMc#'
 'Q=HG6+s0?$y)mDsgjiEv#kVSd^0_mmo2;;XtcItll=4>0wGl9?=szm)UjpM6{Y{C&?aAj{tM#q_%eu-f<m%1T6^y62)SHSjR*CY$'
 'JNDb3)j3~@Ex;cp<W+K!Rw#ayb47xGn|YSD0akvrHWWsoQa>1NK6WcaeHHRcT6g<NlzY8FBqh0qfrRLdYzH?j=i+(G1k1VE%BCta'
 ';kKcTdc7Wa+WYCqUMN?htT(>)rj^9*G#jk4opxvv)(*W1swk}O=lM%oFq9m4gQ5KDnU2pMTk+>wJ0AIr1>R2H&z1eg>r}cGKDO~q'
 'mCuSGJXgp2=Q+QaDgNz&3~YU=Mt;-H`RfsH-5$&x$$;YDNZ8Q}&QkqBcii>m<JNlHUY<QR)%s9zb^eDL|D%fRz2^$Q74!3vx=Y^1'
 'Z2N*OY^%LB!+fAQCY}R+JdYus{qGyXZWSwavCFIW_g0*?&ojy@-&|)zzTCZy@RiM~1fRg4Va@h@B$-C5!!%E^V};~WzRrm2g*{{2'
 'WBSytF@s8@eO!IDtg+Z<@Uh!(d26VmZn-Fuo@kQ(%;uW2zLFYtwmo-c9}=H3Q>kaSF1P$*Jq*3i)}I^sK!k{=a#)Buvmfje`a?YL'
 '1^2B#wiVGIt4)q@SFiaIZqbc3Ja>kJ<8Y}M&E&0<FNu2xUA{fUrlQrJ%k)TR(_J`dOv*bNyq9yQ98Jn8-erq^<!$0RaaayMZuU=y'
 '!`DrwTFGwb9b4Vmb8pgVx<CGsS!FJwiXOAtHa`-0zMQ;?w7$5T1zD;%Co4AXjjv?2JuXdCfpkVpmfm_Nr9iH~Zl89EQ2Q{G+QSAt'
 'jkl`Bm|78-)o__{y3>Md*gZWLv|QyFktbWF^4Y;2WoB#lI-hyvH0Ifo%zLwqy*1o+m7;XBka_Cx&-re06&}U?nbk5kKHA@tIlo$S'
 '(mii$N#^-vDNrCv#d=$u(#4hg?Y)v}9cVgEp2&DBcJ!fQsG|R}?0-}YRrKGKwS`D)>4qf+J$_PlMdxc~L|c_suhF?F@YzII=!+TK'
 'qvo0lN^~mtv7^_&nLoSp5sg>!*5@+6+m`n=xt+ZwBYboB+1z`boBoY*Sj4iERh%vEZ9Y!Eu`fpU>Cl_6bsp_U@6tAv`E=mPy#{3N'
 'RI*Z?z1QP{EAg~S+(v{%5moe*v-N`Cv8*3mi#Pu}v0rC0k8ibQdCJn^g0{;C?bDF$E9;47o#CCWxp@?{bnmUyEs)uHfvF$Mala}I'
 'v-03$E#!-x*)5l5d@)o}R86ORM|=HgAh!F3VezJTQ;wd-W&iPZWw*{e!H~>9?+&AApp@Hq8KN0}*9wzG!1@+tBX3HGth%O$uG_DD'
 'WHu|8zgzRKyJ~KdFK3ghBD<zTA2TcroyofF<Kn9votvq>^<(a-cIzUxrO=vwPJXq$*=eT2v6cRBm}|~Q&$4)uPk}&nS|hw4uF2Bv'
 'FKplKv75@lTDLMbso2?JVQ^06aA!BHq<zW5oSRIWLZaJYJcG>kaoMbK{$=xM?bdqr%;PW=DX}@JxL+(ot5LCjGguv;<iUv{1=l<i'
 'toxREF;FM`uEK#0_}hbG>&-32{F~JPyRP%HceLny)nnC}Coo7KU9x?!_GHtGR-q8;H+nX%9k6AS?dh|(#m@FN#x~6@_l2p{-52EH'
 'U<0IW6Ar0gk0Vo~zY1&mDe08Q-ATarh$=b-W;Bs3?N*7k+RY~vrEk}AOlpuPdvhk0o7kJtOn(f#dYiw}S=iRQgKz%aB+6;czZ#Tc'
 '8Nr`_O9|=5ZT{xa2zAx|SX^<dRO4Wa)uUmxCJ*vYs3I*9YW8d$ekwN)t7KgoZxUMC_t^3cQtLxKRDA4>2U6f8+PHDM^YMJY+$k3d'
 '9@o<{K8bF}hic~5<~{6^b9HNz2bIWhG-z+Ftzs#)D$Zqo8*K-KByJIHmp@{ySvu^Y(<JMO^hyy=ycq3AgcI4z7refN?LD&VcZ%KG'
 'zR65KDqZrap4;3`^U-ugW)s=|WVdo|t$8k#h>Ag}SZh3OgZ7?#w2&%QFa>-*VyTlyB_;KliVhmpuYfEKJ|cyF{b@Tmv||IWbkpHG'
 'Z#FX4YxIEPuYVK|ZHbeHvTM3jD$Rqo_hcJ8CzJZ1-^T<`Jl9U2J5?<A)P5v1R{|S3HY}}CMdI;T+gTHnh0xh;hVM>>w$k;ReKcsB'
 'weyp<I5_N_pAGeWwCa9(OZ~jl4jNr-d&kE<L$Bnw?9=$U9AO%hf>2q;I=;H+<c^B`aCZp0txH#`cH3;AiiG^Fl@FB(PknzIA$ul{'
 'XGdCqOMG~~cv3FUJ1%Kb?11TLd-FAl_=AKm?7R)sM}<bpSIo!#AM$fud#9PvbIBuD+w}YNd20`J<ZPS7UXW3OU-}w{X!9R*H*ebo'
 'q*iM1`7vv?xh9uO$Kz=$<NGR4#nfis4`i01oNMy6USzbU%iY>kQANI0Kki%)ysLW1X;<FfY_<q7_uVvn&QK}RIK@ffy_Jc5mfsrX'
 'sI5P;9(;D&I2hP0{H}E2ZGX%kwJ5z~0|D9f5lCg8T$$&@XXqn7KfT{tC(r48iN$@yJ$E_VqQo`2wQ#jP%SZZ!c(meV1zWjal>Kid'
 'u1D~$q;K$~*=}!I$AP_fd|rw<BLCQpI^)O3ou|^Vg{_mf-SfQ5z2}L;^Ax;BH_?6}S3)gE75&@hZ?yff?Y#Ya=J-~Fiia5Vnax0I'
 'cD0GUEk8exhxwK~h;;-!shzFA2B%DV^06BnyqVBvul&~XXGft~g3gW7qE?=lkH>6rSsW*A>xq(xS1V6SuO8B7fnnm%3xTwx(hS-T'
 '&ETlPDpe`-B;W9}j-PGz53}lG!rD<qDpQ&6!=L=yIDN3Dv|W@*$+s)Nk{e`qgJgN&y9vqTW;c>1*nCN?R3A&BY9ZP_^_w5bTuzC0'
 'TZ!@eaj=zJZq<|YL{@x{%!~&iI_If=1~qH>YldeNf#8g77kuSbdAgN-nTRjT-B?d7J?Xf=IL*Ii3!P0~<@1lJ@`=2pP4lJwtQQm1'
 't-PCUIcF$V$_d-DOHFlR^B(urd`t%XpU?g0;M?OARWx+l-6butj~+%9W{`*l!;i5gzaA8yD?Pi^DrfsAt6V?T21jP)^36uW^if_9'
 '8>xw>r+y^+^P19Zyl>bj*>U|57|)MPB`W>JDH5EgE*0g!I!~l83Vh@r=zjwLsAxQhj3b5p4PL<eRw5lcc8>x-u2p@FkvFD2dI(RU'
 '?(BM`_w3YP+0(U9lHDnVx58U!5GRg_k7OpNENtCCr<2YV*<F~pQ93vA;VG4EcI?l5c!w7rtnbMhi)7=6Sh%v>g6Mcvj-IsLe0v%d'
 'qt>y#ms7H%=A%8khz67K_pU3f`A<*b$ZDHT)zW2eT}<xm#ckT^obPtU=&T&W7B;MULo@L-JY>gP_o<$bhQF9pEX8PjCb4#I9+yhE'
 'l3(Ux<zg;3aVp2pl{M|GgzTNd+&8$9_M={_v1G@I-fH+we0uL|m0XF{E}l(nH@Uip^wn?6`Iz6j(qgwOpKpC=cp|g7#~$UMZ~dj+'
 '`|Yf=Z6<GtR+X=AJ`SgYsw|Rkd|dEbr`EMFkGH<Y)iF<s`(oFVpGAYr<Fq>Co%y`0>{3ug>As&3lKn0DCiiOoXu~!>d@aVO6Ju`<'
 '0vwo6^x_G@zFwqf9ov4UMF-i_&2!Azbspy>g|uZR{<mUr8g9(S!R6<^(CLwjs54V5jS`nv?BrjkUA@NMGqnos_8${A@wrY$zIO9!'
 'zU~UkPQn$QZ#h@OzPjlho4(WP<k}I_^{lW61h?tif_qK&x9;BIz?Q@%HWSOiyxvioY+=rp=I(U(v!8#Qw+?I}*L%wehrp@KE2Q-)'
 'F^bR90crp7{<H}SO6M_1iuRSq(-E0`rB&$5{=E!<E6s%KP<1}#r+&%9zE^g&V8)4;XzcIWHglC*W@`oaSFjfx#7~6c^$zW_TqAqz'
 '^dq0H4SQej!{?Gys@e7}d(u^UR;tHOW>xrDtq8`;a?Q7p>+5ZuX|A(cp}m*(WD`4()!G|-Tg=vjIb}4vb#L97%_sBjS`~V=)~=r='
 'wbAOtq-m{no2UJOt`Ma8cc;@iOcb9UMJ6XbJ_cmkcMvyKK|VPbkz9Tf9cDl2VmkYjvG$sidJS(@cngJ~w<p<;-S=HS`f>X7FY}R{'
 'ytGP^dQ%CgsYI{9`9}Heljf=ZlkVC2MGxD!$<R(07x8t;d=k4`(o&tsJ?q5PTGOJlRS75Z!=e)GSC`{b;#Stu{&@A!l0wOk{Z0dv'
 '=Cid}cXbn2qCzM`4wLTspm*DNtH#zlTZ@n0uH8$u85}F2t@<R973C0)<8_ANB!A;9A5!V}e!esbs(p?K$ud_N5#7VO7+!=F+oi<c'
 '1Fr_1P~#)dJ!b`JrR<F5$9yVXY2{me#sO~+VB3{+y&W&H%~rg@CP7vsonkZXQi*NED@8UAAF9<BTWhA+M776uXb)OsYyeQk!Ko8='
 'q?EVwLw742ilIPV$P72FI+v?2&R}?Hlk<$n!JvN>5k^7;Jcq)=@Gv+GjC{dBBoY#YG41t@LL)v%dji9V;Pr&UblA@gy<8w18u|e`'
 'P`?og3`XszGUrIS=QD*48bw2Oz%Zx|7!nmnM?Hs${58dQ@4YHRM{q&}!+0F$*ozx!#qo1u1kZCwlsYv&d4^XL+>HcYUak~DRSA4!'
 '!QC(%fQcgkmAD*)z~4VJjD!wC==UAm0d(F#5M<m<h5bmJ2&zWFlTuUea#8?ZkZ`w<xsi$@b)(Sf8*wp$anNPO_{sr(eaT#Ziuo7%'
 'Oi^X@7U-t|sPmBnN<V8rM)A=Q9nM%yrY@`2l(Ag>?F<%*d%-Zifbaa-B>emfWTC(zBs?ZUM*=^Nt<VAV`K9S&83=AZtOB7===kZ6'
 'co?7hxfdg<hUvr^E&va==24xdPw01)C}|{0-937Kjn831<cYzX7Gktn(ts$U&}G76p)$Xp-O)jeQ(TB0MkvdnoBJN64j)y~PvD?K'
 'dk{Bh-XBZ-tU!+^Mi}fR@9(|jpE1KzJDSQ|f@7HF6P_f}P_G%m6U?XiKxGPpA}-*L!%_6m=c5q(_vjLcWAYY$(R4n$^S#TLoH}RB'
 'VIO9%zsFC(h|XWc;1YV20Ez$veftJg!yhXy?WhI@{zU`<4adNuu+6Z&ZaTUUICK!-pz#Oq9`r*$%#ZLmfBJF=XqEGKM-Frv2sOfp'
 'Q-Z!D8j7GZJXe7QP<RxW{=wk(zRX`uVvb5MpalRu%I79Jc1mxK8-m<{KP)eA;70)FQG(*Gpigrg#(8p-WQv03c#YAQ3_SuGgobD^'
 'pU&S*7;K`9R^d~ctCfm66jB6Az?cD8B;gBeBt~N%bg&2$@C7}d2-I6s**L?C|A$WT!%xBBQ9zHA@Ozvz?F3*huam$}Fc6RlBZ5YO'
 'L%q1TaZ>;C?Zme;iTa0j2gb0MF#ZTgVz5oq-&m}(nTw%=3}C>>q<|sdfy$937WGot1CIj&+rTb4Wg<%FQ^`nd7!+E`tg#vNm(oQM'
 '|4?w4;*MnW{zXYDyAl)@4mULTAVwDOaG~Gm14cMtC{;_L6RNE7MHJ(AqIBb1K^9apf}xL4Bp#Kay*Qtj0jJ<s%dqOjf>TT%UQK06'
 'Ps9Cz{u)U?+Y6ch<AkRX)|e9|!hFb)Wl<n0bo+x5$>sp0O_^*-E8|5mw)A&+iqQDv*MaOIu-@paL<gzIMr|HcO<1P)z!p02{Yw^i'
 '!s2dPzF*gb?dgYJ8c7ATtjx8UjY5OY5Xc;lHp`VtT*9wl7?Off<Jh@yP|;CON)>?2aOhJ@0+2^J9)Mrra{Tp|<RI^Wa)53EimeG+'
 'Bmg-Bqls`_QwOVa=m$GZZD$z0(GR%n-A)lfZw(I`Q0mC@Fyh4OtkuC3(BV21(AyC3FZ8hl&=Zb$vUTkiR`V$~UP-a7Mmx>Y9+nQV'
 '5w;X>wera{TZ=cFh%mi$vQ%wCKQiBed5w5E-AXs0|LCADe1i7NTqa#AHQ7ovm2R@Bbgh+hASH&m`QpGs!0}2_UgxjrZkmE$bHThl'
 'Jbiwz2eZQ=8oooDDhAW1bQX{YJfJ2E=qxv{YldUffj$8@c{JB~W^{-_&}U9VW~I{rn*n_pzm8YRQA2fBTi5xQ!R&Z7VTJBlyjCma'
 'lkrx*T4}OiICs(w$o(c;&R41pQ$61m0I1E#`mO~`S$|LjS7f9?oqf<rl|i~uMUw)(rOke`l`gaCUb56qfp=r#(EK4A)kZ#>uK?Lf'
 'R;!H^cxt7=W2poLjZVX+w431{g>-RDR-q&UF=@7ec)Xy_R$d(VNW0?|9aAT%AF1tMQ*(}2^F<p58w~vfK`zf`CS0aRUayzUR2!(Z'
 'B{mBOhKH?I(rhl?D3{XBCX4t~0j$dPo1pJXY&RV*{v0nr_SrVgrpvV!WG|a7RTBU>QEh`Em(0a0*|ZrRP2JGg1oJV#bif|Akxo`o'
 '?|eh94|a)L3Wx_tAyD5Y9VpQ}?*QdRbiEKL#<D=euq@QjEbDl{n))y4UlhLU4rnHJB&x^(`6u_?Rabg=gsG?kbqGIEv>-PPJsFtL'
 'U3Jipf?;bH8)!+*;is;zyQ3_X&9Zi|c<<0llNZ4YeMg7xJd~wcOIH%5IM6NaGTX{E((zQ2p#hG@MnWN}Ko!fCcChHN|Mc*sGA02A'
 '?N|a2$h{CHc*=YQgRwxF0cr9Q#$g+&raSY@7ulU}#XDbR_YbbX1DpUxhy$+UN{3c?ado(p0oRs5Z5o9DIbc#Sf!Cr)D_{u}?m+xs'
 'UU@>HYXix9?1lX$#ZA?E?kMmdeFtW^mO4!5*_RpxeqrQIB1pbQ!5sMletjbfb#)(#ejQ5U0{#M?7SP?8+@Wv&i3_4Sx{c&=8Oack'
 'Y1Hcb?J|;Ad>cu+`G0vINfx00{W21C&C&H`B<ZGkO847!BtLE=(P2?V<_k&Cr`*Jl;@~G2K(VIMy?=BmiAj7=>rg8r|LB$yz18|{'
 '9T!COeSkvubx`QG4$6BUq3~kLKfkEsA^^YN*a0J-y7o>Yj$)va`2FBSw{n=1j!tw9$2rOO>e}E^KI47sL>Fz~q}Lz!Z0H~DpGkJd'
 'qa%iPwV(NDkBPh5_oJ5w6n+lQ&9>0By@)LQK)3w@*bE$!;5|s!ud;wC6#8Ta1;5*F(Xf#vc;zSbwFxNZLq+CBJf~``CKGXr076Q^'
 '@a{c~&?p~ORc5=rgZ{|{V+RKLQc)rqoiK!|I$?rADR}|+koW%k4k*%MV5Nd6!7PU+QrgV@sEIS+w5c%Mn9H2I1=(98f4ikFp~8Ur'
 'W{8%#w%@AkxZz0Mz|VvxdaxKK-~?q|mvncW0{_TgE}a0gh^;BUf~E-PTPHwq_?Z^e0KeQj5&nMf1jO{q-4g%{^d_MY4pm}8k}<E~'
 'ru`4++Y5S_1pVrX?>Z`nuAl(@h!$DC$94-C!8UlF;aw2S39(#XHbI!=jeO>LBOckMDi~CR_;IPkxBTn-BtTX7C`f_%-Uwg^fo&1K'
 '-x}dCUo-Kykm&wb-PJsQ(T3NQpd+iEW3PORx_UN{ci-Z#0?qc%L$K=l5Qkvp&LLNaC<N>9{LWp6VAbT2Y>vQ+f=$81Z!xA2&R=3n'
 'T?b%=*Mowxm%9J6_^Xgf=h&-omBAc-6;pa0ef1l)zmt1KFGl=;e*jw;?iY$-L^s{mU;_edtG?6$qrm*T;HwA)=;!Mot|(&MkB{B('
 '$W>sBFkL`yETx(SjeNKQq{w@5i39?E_zlLQWx*|nBM#0=EYLy3G3RAzE9@=P&0+z;;B*Xr_zgTbAZ%v~!s*V-g>@InGY9|nn8JVi'
 'aKID^lt!Y4QEu<Q4KMTEG!Wz!DL~2OzPxOoK|7we2o5}<n_xhjU%wTEEW)8t5l4Q}UC?~unB?+;(fvQDp%nJztn?(3a?^LORGi%m'
 'bx+I<=sCMZ_`_(4B!Rc2gW!Va3{X^9GiS7@6u|0vMG?5E2UrjQyuey;)Ft%AFABf<>XckB#98HoO7K0$jAJTJrmBOIS9nG0<QTz7'
 'K4XDX#i6(mwF5A53!p?KUT{3nf;&PvaO{A;gZVsbYaru*DZs$+U{0(4rq^Kh66A3c93^(gz?A*VgY+5&3};NXO{B!x-2FJ4JE$Fn'
 'IwLA<;T?G<H7|hnz>YE~5VkNV2Ouhhlr(;2Ja>_>6W8OWUoV;keawzO&IT?obgA*`roP5$EOi<I>vlWTA8<CebE2~39q<YcD|GG3'
 'B{t#}d0TFwPKiG>OK%qmsf2b8aU5ZGBGT`@=fJ`M7A5HoJ+~(228F`r80vVG5oZW|KNq~j4fp|`*Qh=&wyFlVmY}pze;gcUjbXx#'
 'C_yIXPqWj%baje9=Dpr~z($+V9R?JxOP^5l4vME7JqLhr0Nw#82lWd#K{}iWZPcj|?hFRbK-WH;gZ^>jF`OwHlSvd)EviSnkb#cE'
 '(f&}(3w=pYfGVrU^qx(gxc4p)(Jy=S-+93t<Sv5W+`+q$k8*=VFeSMQ`+@g;*MiDoY+RT@yFts~T>$vD4E*YQ)vwCHufUVWmt^2q'
 ';8W|@Z=hEig&su<(-%GFCeDr-40}Pr7#Ju32I(?o=xI1=7;p&h$K$)nC1UQ?MH)ccUPs+P5`&}=ReV-hc>fR%Q@m1+_pQthMilPn'
 'n5oq_gv9H>rPz(2^th!!%%~9@MX=lk$U)GLr4Gu{6#;OieF)423ULhMUyV6&A&g9cLq>b*V(otHJUy876h{97O1xe<1aL^AmGZMy'
 '#DTOS!t>=JyK`V`tV<9Xm#9@ExC@1e(6Ny)%=WoLd~bsx^qF|RlukJ)j0KKZvusDr#NAku(9)t%STK^Ec!VMkW4dUvWh0pqVQhp6'
 'u+HWP4R@%0P-SZ7KH9y^U+-~upRZfe!|9)ycWJ#*UjMyEcdF|zFZ%DJM~{%IM}yYmU(iUS{?xO&e%*-|^@{O0LD?%68!earWFgS4'
 'M?d=N59+vFHmlq)<+%$uaYs4P6%a7C(%D`Aql=C%$US@L3b4PaGz<*`#yoxiJt?Ay?8co<oUyt9B?Hugd>f?FCwPN-!jA|i!JYS7'
 'aqLwnJq+{#LBjq0g#4EMdfu@;4<KVFR(Bt-_HWNP(E=Zgz=cLF+L0ykmMji<gydBRGGx{iTO0?S!5bvV<HP$R`nHD#!%vttX5b9~'
 'W_KLE+d%)rm~WTGb$!hrW>Stux*X3};Cecw1ka%<2OK6FMNl1j7;!jgzFPxK)Oii_?<qSuVDLl715mklz_Wn@1gha354`CW?Jzt5'
 'x-bF4$nk)GDf4#1gRZ4M%{vjPY9(!ImZ8Z0NIkM<S%7qO(C^<t-Z%8MahO?Hq5B+g6!pAH;bmIOM38ZGGi>JWjJ^IJTm68RhyP4&'
 '&inqCjsNq#8j^Mg7fJPPEV#Y`d<(eaO8gWq3Z%=*2+-sJ-lVn=K+kBhz5zy^(@^9QVXS>W7Qjzs6-*vcd+?o-5DKeybQjGf95IqP'
 '3PxDMlNO8k0R0_6I53NLSd27p%2RH=5DNJ07O!^cuZkfCAUZBLi$r0Do%u2Vp$P+Q$LKEh4;Op=?Rtz**mpjbqbMjKy8j&O42#NN'
 '=)4I-5O*|n2Ny)|BGg?Za`iw5jI01m!ok?_#n%6&XJZ6X-7JTKLTTSj!;d+f6KyHtKu6cUo(3<r?L8x6kh^r{FKK3PNi+LOn%Ps*'
 '%zl!ldr20K`~Sg7vKT7#YW{Y1Q!Wb(c<d<H(7}1m`KBS$Nc-)cp})Dh=nu9H&W50IyYqOBTY~<JA#NClk3U$4f9h>PB6U<heXVcK'
 '7T|`-d>co2cIE>-`lYV0%;O!67t`e3A1&{0cQ(Dd-IeV{rgyi)OF37@clR4Na3v`5$^aW67>{yRi03}~zu>)DBSE)wu|Ovlew>9+'
 'lz)8MLEp{Nw<EuuC{#@63IE-OCG$Utl4SBK*fF;h7vD_y^_dFY&Q{vxbOUYfrt(dF6Si6@_4SQe@Se})(+xJ?WSePt9HOP0WzfL?'
 'Y)kfEpa0+g1D5_Rng'
)
def main():
 assert __debug__
 if len(sys.argv)!=2:raise SystemExit('python -B -S recover_hex6_star_v10.py DIR')
 dst=Path(sys.argv[1]);dst.mkdir(parents=True,exist_ok=True)
 raw=zlib.decompress(base64.b85decode(PAYLOAD))
 assert len(raw)==PACK_BYTES and hashlib.sha256(raw).hexdigest()==PACK_SHA
 files=json.loads(raw);assert set(files)==set(MANIFEST)
 for name,text in files.items():
  b=text.encode('utf-8');n,sha=MANIFEST[name]
  assert len(b)==n and hashlib.sha256(b).hexdigest()==sha
  p=dst/name
  if p.exists():assert p.read_bytes()==b,('different existing file',str(p))
  else:p.write_bytes(b)
  print(name,n,sha)
 print('HEX6_STAR_V10_TWO_COMPLETE_SOURCE_UNITS_RECOVERED')
if __name__=='__main__':main()
```
