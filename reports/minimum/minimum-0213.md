# minimum-0213

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# HEX6_FULL_APICAL_CUT_HALF_BASE_STRIP_AND_ALL_KERNEL_CAP_CHAMBER_V7

## 1. Main result: the adjacent cap chamber, without a kernel box

**The entire prescribed q8·k≥0 projection chamber is now excluded at every root on an independent five-dimensional actual-completion cylinder.** Unlike V6, there is no small rectangle of kernel directions: every kernel satisfying the stated facet-sign conditions and every positive-definite planar metric are covered. The proof includes eight- and nine-corner shadows, both cap-tangency walls, and coincident interior projections.

Retain the literal changed six-pole atlas and labels in section3. The certified shape domain is

    3/4 ≤ x ≤ 17/20,
    13/20 ≤ y ≤ 3/4,
    1/200 ≤ z ≤ 1/10,
    0 < u < 1,
    0 < v ≤ 1/2.

These are SOURCE edge fractions. In particular v≤1/2 is not asserted to mean that X9 is a Euclidean midpoint after projective refilling. The complete open interval of the apical partial-cut fraction u is covered. The first three fractions vary independently, as does v.

Let M0 be any rank-two positive-semidefinite matrix. Suppose its kernel can be oriented by a nonzero vector k satisfying, for the ACTUAL outward facet poles,

    q0·k>0, q1·k<0, q2·k>0, q3·k>0,
    q4·k>0, q5·k>0, q6·k<0, q8·k≥0.

There is no restriction on q7·k. Then the actual true-edge weak-arrow graph has no arborescence toward ANY of its ten vertices. In fact it has at least two singleton sinks, hence at least two strict vertex-U tests under M0. Thus there is always a nonapical strict U test; apexU cannot be soleU in this sector.

The substantive strengthening is a **three-dimensional, kernel-independent escape-path obstruction**: throughout the cylinder, every one of the145 rooted paths on the two relevant boundary cycles has a negative selected primitive for every nonzero PSD matrix. The geometric cap-sign conditions are used only to show that any rooted rank-two system must supply one of these paths. This is NOT an exclusion of arbitrary full-rank U1 systems: a full-rank escape tree need not contain such a boundary path.

The theorem extends analytically to an explicit closed actual-coordinate neighborhood of radius10^-8 in the working frame, provided the perturbed uniformly filled body is own-centred, has the same true labelled lattice, and satisfies the corresponding actual facet-sign conditions. Its six poles need not remain fixed in this separately stated corollary.

Three actual nonwinning reciprocal pencils are preserved: two strict222/physicalweak000 pencils with respectively nine and eight shadow corners, and a strict233/physicalweak000 pencil whose rank-two limit identifies two NONADJACENT vertices in an INTERIOR fibre. No U1 or110 construction, whole-atlas exclusion, canonical counting change, or improvement of34≤Cmin≤622 is claimed. The interval is the supplied notebook’s current accepted interval.

## 2. Authority and evidence

Authoritative parent:

    minimum-0210
    SHA256 7090c27c162fd8ed30c044687187dcf869dadfd1b0a215be976c983a3ca7e469
    HEX6_UNEQUAL_TRANSVERSE_NINE_TEN_SHADOW_ALL_ROOTS_V6.

The complete current journal, literal parent and new octagon material were read. The parent model is retained, including the partial B3 cut through the existing B2, not substituted by the original integer hexagon or either degree-five body. The supplied parent explicitly identifies the adjacent q8-positive chamber as outside its coverage.

The coordinator’s different rooted planar octagon is important as a boundary of inference: strict −Q/3 containment and capped barycentric mean0 do not imply a centred homogeneous corner-only lift. The new result uses the actual volume moments of the ten-vertex atlas, not that octagon or an independent planar density.

The new family exclusion is an executed exact interval certificate plus the analytic arguments below. No numerical search failure is used as an exclusion. The recovery is autonomous and requires no unprovided parent code, optimizer or checkpoint. Internal exact arithmetic is not a proof-assistant formalization.

## 3. Exact actual body and centroid

### 3.1 Literal model

Use original physical coordinates

    p = (1/100000)*((60401,-32565),(80000,-20000),(0,60000),
         (-80000,80000),(-483861,-325040),(-447814,-355009));
    A=(0,0,1), qi=(pi,1),
    b=(2615613/500000,816129/250000,-3),
    Bi=[qi;q(i+1 mod6);b]^-1(1,1,1).

For cut fractions x,y,z,u,v set

    Y0=A; Y1=B1; Y2=B2; Y3=B4; Y4=B5;
    Y5=B0+x(A-B0); Y6=B0+y(B5-B0); Y7=B0+z(B1-B0);
    Y8=B3+u(A-B3); Y9=B3+v(B4-B3).

The nine maximal facet cycles, in their fixed order, are

    (0,4,6,5), (0,5,7,1), (0,1,2), (0,2,8),
    (0,8,9,3), (0,3,4), (4,3,9,2,1,7,6),
    (5,6,7), (9,8,2).

The17 genuine edges are

    01,02,03,04,05,08,12,17,28,29,34,39,46,56,57,67,89.

For U_i=Y_i−A, take the unique c with all ACTUAL denominators d_i=1+c·U_i positive for which

    X_i=A+U_i/d_i

has uniform-volume centroid0. This defines an exact algebraic body for rational fractions; rationality of c or X_i is not asserted.

The positive apex-fan triples are

    (4,3,9),(4,9,2),(4,2,1),(4,1,7),(4,7,6),(5,6,7),(9,8,2).

For T={i,j,k}, use v_T=det(U_i,U_j,U_k)/(6d_i d_j d_k). Then

    V=Σv_T,
    g=(1/(4V))Σv_T(A+X_i+X_j+X_k),
    E[XX^T]=(1/(20V))Σv_T[(Σ_{a∈{0,i,j,k}}X_a)(Σ_a X_a)^T
                                      +Σ_a X_aX_a^T].

Every determinant, centroid and covariance belongs to this SAME uniformly refilled body. The covariance is not the covariance of tetrahedral centroids.

An equivalent polynomial reconstruction is W=∏_{i=1}^9d_i and Z=Σ_T a_T∏_{i∉{0}∪T}d_i, where a_T=det(U_i,U_j,U_k)/6. The actual c is the unique positive-denominator solution of

    Z_x W−Z W_x=0,
    Z_y W−Z W_y=0,
    Z_z W−Z W_z−4ZW=0.

Here derivatives are with respect to c. Its volume is Z/W. No condition is imposed at removed virtual vertices.

### 3.2 Exact inclusion of the actual centroid over the cylinder

The reconstruction checks the multiaffine raw-volume identities at all32 Boolean cut corners,224 identities in total. The nonincident unnormalized support slacks are also multiaffine: all their corner coefficients are nonnegative and each of the56 nonincident slacks has a positive coefficient. Thus they are strictly positive on the open cube. The actual truncation construction gives the displayed lattice; an exhaustive supporting-triple audit, full-facet convexity check and two positive tetrahedral mass fans are additionally checked on a literal unequal source.

For the uniformly refilled star image,

    D_c g=−[5Cov(P)+(g−A)(g−A)^T].

The bracket is SPD on the positive-denominator domain, proving uniqueness. For each closed cut cell the verifier constructs a rational midpoint c0, a rational affine predictor c_pred(q)=c0+C(q−q_mid), and a rational preconditioner R. Five-variable automatic differentiation of the actual moment formula bounds g(c_pred(q),q) by the mean-value theorem.

For a correction e∈[−eta,eta]^3 it checks that

    e ↦ e+R g(c_pred(q)+e,q)

maps that closed correction cube strictly into itself for EVERY cut in the cell. Brouwer gives a zero; strict monotonicity identifies the actual zero. All actual projective denominators remain positive on the same enclosure. This is not acceptance of a rounded Newton iterate as the centroid.

The calculation uses outward dyadic intervals with80 fractional bits. A fixed invertible working frame reduces cancellation:

    T=((27/10,0,0),(9/5,9/10,0),(-1/2,1/20,7/10)),
    X_work=T^T X_original, c_original=T c_work.

Consequently M_work=T^-1 M_original T^-T. The code transports geometry and physical control metrics consistently. It does not introduce a second density or an independently centred polar.

The closed proof box includes u=0,u=1 and v=0 only as algebraic/merged-incidence limits. The theorem’s actual10/17/9 members obey0<u<1 and0<v≤1/2. The finite v=1/2 endpoint and all displayed x,y,z endpoints are included.

## 4. True shadow incidence and all weak strata

For a raw outward support n·Y=h, write r=h−n·A. Under the star map its outward normal is n+r c, with positive actual support normalization. Thus the chamber conditions are conditions on genuine maximal facets, not integration triangles.

An edge with opposite signs on its two incident facet normals is a strict silhouette edge. Applying the true incidences gives

    q7·k>0: C9=(0,1,2,9,3,4,6,7,5), nine true corners;
    q7·k≤0: C8=(0,1,2,9,3,4,6,5), eight true corners.

For q7·k<0, vertex7 projects into the polygon interior. At q7·k=0, it projects into relint[p6,p5]. For q8·k>0, vertex8 projects into the interior. At q8·k=0, it projects into relint[p2,p9]. The latter replaces the former2–8–9 silhouette by the genuine edge2–9. Both equalities can be treated simultaneously.

At a cap wall the fibre through the projected middle vertex runs from that vertex to a point on the opposite true cap edge. This fibre segment is not thereby a mechanical edge. The only potentially tangent facets are7 and8; they are disjoint, so no genuine edge has both incident normals perpendicular to k. Hence **no true edge collapses anywhere in the stated chamber**, including both walls. Every true corner fibre is a singleton.

It is nevertheless possible for two nonadjacent interior-projected vertices to coincide. Section7 gives an exact actual example with p7=p8. Such a coincidence must not be converted into a zero-edge two-cycle.

## 5. Kernel-independent path obstruction and complete certificate

### 5.1 Reduction to145 boundary paths

Let M0=L^T H L, H>0. Because no true edge collapses, each weak true arrow gives strict projected-norm growth:

    |p_j|_H^2−|p_i|_H^2=2D_ij+|p_j−p_i|_H^2>0.

The weak true graph is therefore acyclic. Each strict radial-maximum corner of LP has a closed exposed fibre, since the pullback of its exposing functional is strictly decreasing along every genuine outgoing boundary edge of that fibre. A true rooted system would force just one such corner, containing its root.

At any other polygon corner at least one boundary arrow must be nonnegative. Both cannot be nonnegative, because the inward direction toward0 is a positive combination of the two incident boundary directions and has negative H-inner product with the corner. Following the weak arrows reaches the unique maximum. A spanning tree of a cycle is its boundary with one edge deleted, oriented toward the root.

There are8²=64 possibilities on C8 and9²=81 on C9, hence145. These are necessary projected boundary paths, not an enumeration of all true three-dimensional spanning trees. Interior projected points, including a projected origin, cannot add a competing corner root; genuine reachability is handled by the true graph argument.

### 5.2 Three-dimensional stresses

In the working frame define

    A_ij=−sym[X_i(X_j−X_i)^T],
    Q_row=(Σ w_ij A_ij)/(Σ w_ij), w_ij>0.

The complete44-row bank,145 integer-weighted terms, is literal in the autonomous recovered source. All row arrows are genuine edges. On each certified shape cell an explicitly verified subset of these rows satisfies

    Q_row−I3/100000 >0.

Every one of the145 boundary paths contains the support of at least one valid row. Therefore, for every nonzero PSD M_work,

    −(Σw_ij D_ij)/(Σw_ij)=tr(M_work Q_row)
                                  >tr(M_work)/100000.

At least one required weak arrow is negative. This excludes the path even for singular M, including all finite zero-arrow boundaries. Row applicability is **cell-dependent**; no individual copied row is assumed valid on the whole cylinder.

The completed cover has

    2626 closed five-dimensional leaves;
    5251 subdivision nodes, maximum depth16;
    75171 valid row/cell applications;
    300684 positive-definite sign-vertex matrices;
    902052 exact positive leading-minor checks.

Each failed parent test is replaced by BOTH closed halves. No part is pruned as numerically infeasible. The generator checks the binary-tree leaf identity, exact Kraft sum1 and exact volume coverage. All145 paths are checked in every leaf.

### 5.3 The useful new matrix-jet mechanism

Directly subtracting interval enclosures of nearly coincident transformed vertices loses the edge factor at cut limits. Instead, with e0=Y_j−Y_i and h=c·e0, the verifier uses the exact identity

    X_j−X_i=(d_i e0−U_i h)/(d_i d_j).

It differentiates this factorized expression, including the actual affine centring predictor, before building arrow derivatives. This retains vanishing true-edge factors without silently assuming that a small edge is zero.

The matrix Taylor enclosure has eight variables: five cuts and three independent centring-correction coordinates. The weighted derivatives of an ENTIRE row are added before taking interval absolute bounds. This preserves actual cancellations; it does not replace the centroid by independently adjustable moments. The straight segment from the midpoint/predictor origin to any actual corrected point remains in the verified positive-denominator enclosure.

For a symmetric interval matrix, the verifier checks four exact endpoint matrices indexed by sigma=(1,±1,±1): take diagonal lower endpoints, off-diagonal lower endpoints when sigma_i sigma_j>0 and upper endpoints otherwise. If all four are SPD, then every interval member is SPD. Indeed, for any vector z choose sigma from its component signs; its quadratic form is bounded below by that of the corresponding endpoint matrix. Each endpoint matrix is checked by all three Sylvester leading minors. The arithmetic is rational/integer with outward rounding, not floating eigenvalue testing.

The reduction in5.1 then proves the main all-root rank-two theorem. Since the true weak graph is acyclic and has no rooted arborescence, it has at least two singleton sinks. This is why a count of two strict singular U tests is justified here; no collapsed-edge SCC is being overlooked.

## 6. Explicit actual-geometry thickening

This is an analytic corollary, not an additional sampled box. Let X be any certified body. Let Y be another ACTUAL uniformly filled own-centred convex body with the same labelled maximal facets and true edges, and suppose

    max_i ||T^T(Y_i−X_i)||_2 ≤10^-8.

The six poles of Y are allowed to change in this corollary. Require the displayed sign chamber for Y’s own actual facet poles and its proposed rank-two kernel.

The source certificate bounds ||X_i||<18 in original coordinates. Since ||T||op≤||T||F<7/2, the working-frame vertices have norm below63, hence below64. For epsilon=10^-8,

    ||A_ij(Y)−A_ij(X)||op ≤4·64·epsilon+2epsilon² <1/200000.

The same bound holds for every normalized positive weighted row. Every row selected at X consequently remains greater than I3/200000 at Y. Every one of the145 paths is still excluded for all nonzero PSD metrics. The same true-silhouette argument excludes rooted rank-two systems at every root on Y.

Arbitrary entries of the coordinate box are not asserted to form a centred realization. The actual centroid and true lattice are hypotheses. Separately, at each fixed actual member and each fixed rank-two metric in the chamber, the two strict U tests persist in a sufficiently small full-rank SPD neighborhood. No uniform numerical width over the whole open kernel chamber, and no exclusion of distant SPD components, is claimed.

## 7. Actual reciprocal controls, a wall, and an interior nonedge fibre

### 7.1 Two222 pencils on genuinely changed completions

Define exact algebraic bodies

    P9: (x,y,z,u,v)=(4/5,7/10,1/100,9/10,1/2),
    P8: (x,y,z,u,v)=(4/5,7/10,9/100,9/10,1/2).

These are not the V6 controls: the apical partial cut is now u=9/10, and the base-edge partial cut is v=1/2. Their actual uniform centroids are recomputed by the reconstruction above.

For both use

    s=−3/4, t=11/20, k=(−1,s,t),
    L=((s,1,0),(t,0,1)),
    H=((23403/500000,87/500),(87/500,1)), det H=1653/100000,
    M_e=L^T H L+e e1e1^T, 0<e≤1/100000.

Writing Hinv=H^-1, the ONE reciprocal metric is exactly

    N_e=((1/e,−s/e,−t/e),
         (−s/e,Hinv11+s²/e,Hinv12+st/e),
         (−t/e,Hinv12+st/e,Hinv22+t²/e)).

The determinant of M_e is e det H>0, and M_e N_e=I. Throughout BOTH complete positive intervals,

    S={4,6}, U={0,9}, H_saddle={29,34}, physicalweak000.

All68 actual edge primitives are nonzero. Each primal primitive is affine in e; e times each reciprocal polar primitive is affine in e. Exact endpoint signs agree strictly, proving the entire intervals, not only their sampled endpoints.

At e=0 the true weak graph has singleton sinks0 and9 and all34 primal primitives nonzero. Precisely{0,1,2,4,5,6,7,8} can reach0;3 and9 cannot. The set{3,9} is trapped: its complete outgoing boundary3→0,3→4,9→2,9→8 is strictly negative, while3→9 is positive. This identifies the actual remaining nonroot mechanism on these controls.

P9 has nine corners C9 with vertex8 interior; P8 has eight corners C8 with vertices7 and8 interior. The separate complete wall verifier proves that along the WHOLE cut interval z∈[1/100,9/100], with the other four cuts and k as above, all the required non7 facet signs remain strict, including q8·k>0. The endpoint q7 signs are opposite. Continuity of the unique actual centring parameter therefore supplies a genuine q7·k=0 body inside the positive-cap chamber, with unchanged10/17/9 lattice. No complete physical census is asserted along that cut-motion path; the222 interval theorem varies e on each fixed endpoint body.

The actual projected volume mean is0, but the uniform-AREA centroid of either shadow is not0. The exact report bounds its first coordinate below−1/50 and its second below−3/10. Thus substituting a uniformly filled polygon would move the reference point. The actual marginal is its real fibre-length density, up to the constant projection Jacobian.

### 7.2 Exact coincidence of two interior projected vertices

Take

    (x,y,z,u,v)=(4/5,7/10,1/20,999/1000,1/2),
    k=X8−X7,
    Pi=kk^T/(k^T k),
    M_e=I−Pi+ePi,
    N_e=I−Pi+Pi/e,
    0<e≤1/100000000.

This is an exact algebraic physical family, not a rational-coordinate claim. Pi²=Pi proves reciprocity and SPD for e>0. The actual-centroid and sign enclosures certify the whole interval:

    S={6,8}, U={1,4,9}, H_saddle={01,29,34}, physicalweak000,

with all68 primitives nonzero. The rank-two limit has the same three singleton sinks and all34 genuine primal primitives nonzero; every possible root has incomplete true reachability.

Here q7·k<0 and q8·k>0. There are exactly eight true shadow corners C8. Vertices7 and8 project to the SAME interior point, identically, because their difference is the kernel vector. They are not adjacent:78 is not a true edge. At7 all incident facet normal values are negative, and at8 all are positive. Hence k points strictly into the body from7 and −k points strictly into it from8. The exact fibre is the interior chord[X7,X8], not an exposed face and not a zero-arrow SCC. All corner fibres are singleton and no true edge collapses.

This control shows why both the exposed-fibre condition and the genuine-edge condition matter. A coincident pair of projected original vertices must not automatically be merged into a graph vertex or counted as a collapsed mechanical edge. It is also far from V6’s small kernel rectangle: normalizing the first component of k to−1 gives approximately(−1,1.5142,1.0982), quoted only for orientation; the exact input is X8−X7.

## 8. Preserved whole-cube method: a bounded actual core and two positive ears

The following positive fan identity is useful beyond the certified half-strip. It is valid on the ENTIRE open five-cut cube, independent of metric or shadow signs. It does not itself exclude U1.

Triangulate the actual heptagonal base by first cutting off triangle(3,9,2). Use the alternative positive apex fan

    (4,3,2),(4,2,1),(4,1,7),(4,7,6),(5,6,7),(3,9,2),(9,8,2).

Let R_i=B_i−A and define positive raw constants

    C=det(R5,R4,R2)/6, D=det(R5,R2,R1)/6,
    E=det(R5,R1,R0)/6, F=det(R0,R5,R1)/6,
    G=det(R4,R3,R2)/6.

The seven raw volumes are exactly

    C, D, E(1−z), Ez(1−y), F(1−x)yz, G(1−v), Gv(1−u).

Divide each by the three actual d_i of its triple to obtain the actual positive volumes after star centring. The first two tetrahedra form the bounded retained quadrilateral pyramid conv(A,X1,X2,X3,X4). The next three form the retained B0 ear; the last two form the retained B3 ear.

This is an exact positive decomposition of the SAME body. It uses no removed virtual vertex as a transformed integration vertex and remains valid when a released virtual pyramid crosses a projective horizon. It changes only integration diagonals, not mechanical edges. The raw constants above are in original coordinates; the recovery checks the identical formulas in its constant-Jacobian working frame.

Crucially, the physical core moves when c changes. Its volume fraction and centroid cannot be frozen while the cuts move. The identity supplies coupled actual positive moments, not independently selectable core/ear masses or an inherited pyramid equilibrium count. The wrapper verifies all224 multiaffine determinant identities exactly. The geometric fan proves the corresponding first- and second-moment decomposition as well.

## 9. Scope left open and most useful continuation

The proof covers the full u interval and half the normalized v interval, with three independent generic-cut coordinates and ALL kernel directions in the specified chamber. It is not merely another small seven-parameter box. The first three cut ranges are nevertheless real restrictions. The sector v>1/2, other generic-cut parameters, other side-sign chambers, and full-rank components not approaching this rank-two chamber remain unresolved.

I tried extending the same three-dimensional path-stress approach to the full0<u,v<1 square; no complete cover was obtained. This is an unfinished sufficient-certificate computation, not a counterexample and not an impossibility theorem outside the reported strip. Its exact larger-domain candidate is reconstructed by changing only the last BOX interval in the supplied source from(0,1/2) to(0,1); the44 rows and every other parameter are unchanged. No larger-domain execution is promoted here.

The retained-core/two-ear representation and factorized edge jets are useful for that continuation, particularly near cut limits where naive interval differences become poor. A stronger next step could exploit the q8·k sign in the mechanical inequalities rather than discard all kernel information as the present three-dimensional stresses do. Such coupling might close a larger domain even where this stronger kernel-free path obstruction does not suffice.

The supplied planar octagon does not alter these conclusions: its relaxed barycentric centring is weaker than actual homogeneous volume centring, and its no-lift theorem has only eight corner vertices. Our controls have ten true vertices, including the explicitly accounted interior projections. No claim is made that seven-corner planar existence is settled, that all eight-corner actual shadows are impossible, or that U1 would imply S1/H0/physicalweak000.

## 10. Complete recovery, exact inputs and observed status

The following wrapper contains the entire24021-byte autonomous readable source: geometry, centring, all44 literal stress rows, deterministic adaptive cover, matrix jets, all physical control inputs and full sign censuses. Save it as `recover_hex6_cap_v7.py`, UTF-8/LF. It needs only CPython3.13.5 standard library, assertions enabled:

    python -B -S recover_hex6_cap_v7.py build > build.out
    python -B -S recover_hex6_cap_v7.py check > check.out
    cmp build.out check.out

`extract` writes the readable source without running the cover. The supplementary wall unit below is complete and uses only that recovered source:

    python -B -S hex6_cap_wall_v7.py > wall.out

Pins:

    recover_hex6_cap_v7.py:13370 bytes
    SHA256 a659037f890a0ede0be0faf0ef88718518ff9fe7154b90a4202beddc86c6b5f5
    hex6_cap_sector_v7.py:24021 bytes
    SHA256 9610e0e8499d072b15932d76d38e184532ed52d91793d9fc0e02631ef2d76d89
    hex6_cap_sector_v7.json:3620884 bytes
    SHA256 c5eb3f969b9ba26c9add39930dbad2fad672af4761e57d52b613d8b4d51579e1
    wrapper build.out/check.out:686 bytes
    SHA256 eb9036f8571f347de9fe94a11637d9985b022096d071c957b050c086a46038fe
    hex6_cap_wall_v7.py:1653 bytes
    SHA256 90721ecbf5ae7a2bfb564cf14fdb1a60f4148cef1c94c51c2e182bd8f4ab203b
    hex6_cap_wall_v7.json:2595 bytes
    SHA256 61564c6ac9dd8161f4c67740d74f44eeb0d444cc616969450694ce8033e1e265
    wall.out:119 bytes
    SHA256 5e03d3517955e38a579017796a965f67a2e27f630af459d1b16ad86390323b15

The full exact build completed. A fresh directory initially containing only the wrapper reconstructed the readable source and identical full report, then checked the additional positive-core fan identities. The fresh source-only build AND the full rerun of the same verifier in check mode exited0; readable source, full report and686-byte stdout matched byte-for-byte. The wall unit was also executed again against the cold-decoded source and reproduced its exact report and stdout. These are author executions and same-verifier replays, not an independently written audit or proof-assistant verification.

Expected terminal markers include

    ALL_145_EIGHT_NINE_CORNER_ROOTED_PATHS_EXCLUDED_EVERY_NONZERO_PSD_PASS
    LEAVES_NODES_DEPTH 2626 5251 16
    PD_MATRIX_VERTICES_MINORS 300684 902052
    ACTUAL_PENCIL_CENSUSES [(2, 2, 2), (2, 2, 2), (2, 3, 3)]
    INTERIOR_NONEDGE_FIBRE_7_8_WITH_EIGHT_TRUE_SHADOW_CORNERS_PASS
    HEX6_CAP_SECTOR_V7_SOURCE_ONLY_EXACT_RECOVERY_PASS
    POSITIVE_RETAINED_CORE_TWO_EAR_FAN_224_EXACT_IDENTITIES_PASS

The report is a convenience output, not an input dependency. The complete source/input below, rather than the hashes or sandbox files alone, is the continuation unit.

### Autonomous recovery wrapper

```python
#!/usr/bin/env python3
"""Autonomous V7 exact recovery. CPython 3.13.5 stdlib, assertions enabled."""
import base64,hashlib,runpy,sys,zlib
from pathlib import Path
DATA=r"""
c-pmm{d3w%uki2u6@Jd0JJ_%!w)qa-Gm|E?$!VJ8grp~ZxQxfxCO8nFwjoLTod5lmw7dQwB<*?c+-3^)TGDE@l2+2L`R%vgPWrbk
&GnMCJJ(ijl!WfQ=D91)d!C02KZvyPa=q}~=()CXld0wf05S<ZHwl<_borc2mkX`FXVv$bTAcXvaJ*L<xSK$`x&Bb=?4Nz;X)6I#
d#}|7+BA4-IY8fu120)d&ZfP$de+A4aPI%dn+D!&uXH${YkuH`akyN>ni~aL<R)+p3@#&WxlSJ4$k+U5*AG1{TqHrXfk)o*0oV^?
z}YMP_S<izNwj>>CJ_vc=!6feWt3<iWP|3$+6Mvifa8*nSJBch$?JQd#p36fP2G430~638^p`A`^OPcVJPsGcVayPJ?Ii*f1qOHu
@DgrI?@zA>ykqtT+<Ny8Z%W?WjbrWfprkoYJYOcU<8Zw^UzS;U8kUU`$YKJI!bO-kjvfc|33Iv0#{7J_2w3Dk@(=Dj4h$fmg%gm~
;{gKg&6kY6ry+OQ7#;=yg+Q9iKj^N}8*>*CfWKHnS_Ghd(8oqk65#IMV*L<+_?J;-u)pu_`N3lOfTLYTJw?5y>$Pzn(AeJ}=OJMX
Anq9Crb)u@xI|W?bA2BM2Yjkw!0a#L#9erSK4yOy2T_o$qlGrEy6}9=!w}h&ji<T`G^=AAvI|7vY8tZZXdM_R)QE_4*@^0L5!_*q
DdkhWhPbSTv=p)cjn`wvoCJ2OHR3=)L@z<;d9~&$kcajB*G5>$k8s0jY!x{+x&kJV(@HvCYRgFj#IA2(5(W&X=D~e}JG?b=G9h-j
WJ~ZE1s=*Hn=I__cN2{cdwFMOJq(04ptzui0ZlnV8%4n-aN~!YZQ)gDY<t*WCc)jX1X*$Oun+ECZrVQRI6ikA>!N>g1>!K+KqA0c
z^UbMhH(<<9|!?}45n^jIB+{EArf?)A-G%f<+4*lSPQ70AuafiEeqa&0sFh{cf)+LUPD;whHr#1`CK=dQE6g#e$gzG^=cmIzOmb2
#{B+1XApnDU^ZX{8z#`6s?XX4rtyhAgTvImhbsW^85pTy`~wsD15HHHtUU>mNYF(>Z(0kn_lC95^H;59*YGO2;o)@^+kQ68H?{s7
w?K(ESufwxp;o?CzP&Qs*L0jX{v{nJ$W+G>6k6U=zCWb${ejAd@cuF>P>k0PAe5KF01$xy(_BD!T}@IHn6q6dwYN|_7eEr`ZXqR=
yzU5CFIvWNp#$9=TBFK%Xpd?xe8818V)DwwHd8!h^2)+COFWfg36h)~Nl5UF$*vSR$!xgT2t8Qvd9c9s@sSUQAM__9<24#pp(W(}
UNqiQqr12Z^o22^rjSM07|7)irVAVjJ(=Z!QQz+QB6v#lP~c@xXKZ2MoIei3(Qq~bM&Oe@4(~@CKN#M^!hm0Rh2MPmw7<#t#3tx<
o3QAX)ahS*M%NnB2_>Bn>C|>u5k8`BaV*8Dq|a!$I2Z|$(C8n9NFO#kGzO<3g4PULYQV$84(L3NCvZH)RR#3y1r-bn^(QtClbAOe
IA9+mExhkNah%Rxx^n1Gxv0gj*!%lW`LLyG!K!96@VS>f&kZaU%rfzx=-$QdSK@kw*Sg*^8>Yo-b-USW8cgpXFss>w!@$S4<W)^P
>8RUAr`~A^M4&(|jdsUsKufb}nqBl`ha5P7XY#``jNYFE$>6H0V++eMb7}P69}W=5ZduKiRcB4XJK%P#mSuOD-Bb;=I&|>9Fk18_
QBKZiC;FcQ)Cl<0Ly*#cw?+*5FywUPG_D2YJ{%r#9md>XE!L#bH(8rmbY(G{zHQc_?+)v-I$hOS1HK#Z4g3LIo3-G+2{hX9-33S+
X!nmLuQ3GJfv^84-02~^S4^RSYru*$(tD*u6E+!I2czm_cwmi;zk%j;{~GwEo{57l@z_8v=-VO=8n1A4b@3Nq>vg7enI^OZB&z|u
25rrHz0qmoeUoV|rgf}#r(@wgK-+-Ovdvc8zy{qGB)aWJy_HdDH@cSH$tb8U2*rdR3cU&%^@a_Eb2!a*SJ3DRn#~5N#+xL7&z5Cn
C@r&Yo6Q2F?N+zd#fBD<usdz5Zf6(;MlGg6M|R!r*txOQJN3Hg^jF3vX*8{N!_2y|TTQ!Z=X+^@2-{6;fX9sj3BhTj+cZ0kv=_i?
Tc*{@p>$hTyIapNb}-g#0hLz9SIg|Q+ERX2p;I~2opz^L&+`d(-V%I@PU@{rM^Ka)Tb)`vhJsv(Nf0;<tJyF+ub_x|YuKG`y+8t-
RwK_?v)wYgxoPUuyUlvzO~#s?R-@g{YpvP(3Cat`S}=aAp3{y-*Y4VRluo155scZ}<|dS((=sik46j*av)ip(Qs>$L(`mHLoCK||
ZGwds6un!p$Y#ef8#xMvu}PFxvsou`w8hj~Fqqa)Y@=(o?cC^_ZK>xwdJ!n~ZoS@V>{N8oZPV(&zrs8<+Z{1a0;O%W+ud%4v7?uE
*R+LQ3lPw+dZ+WNQ!8-V7U+YWS5v#yZojRjX5DP$IBT{|GdC7u#L7$#g$~MLHC_?2K<U&0sgZXk%|<h4we^+>GJBImyWR#Dv{MI#
NSk&8raP|<;5)l^{SAlIvSA_%{<z)-&)Cd)7jWRay^A0Tkw(4SDJX|+w^Cc#<&YXJv)w8xN5e9^jodN<Jk)dg1%AO&8fosFcpF@W
&<(4g8!1Wfd7wTyQFOs^H1fh~w!r(CZz*-R-NeA?jWxouO_<5Tv=(g3w%Vrs#`=e@2K+$Y=Ifnq!JC`iEp6<A;}J_pqo6t|O4By&
#!nVq+cNE(2W(o6h8n6>ka;%oolc{fTSU4LPqwVWteVYks`Jo~-Dowe+$>vG1N_@7)B0MkU9)B7jI#?-P2DPpqhYn`t*qC2w_&&I
Z<r0(dn@PdcTFpXQe8Wv(P_6@?L3KkvtyeWGQYpLm2n~l?-=N+)B!RMj0A^zxxU{hv$ECRx6Lxdb7iZJSB%=}9&Yj8+P4G%-DFq$
cG-Zu^ZM%W9HMOuw;{;Q!gLfMG<Gor#xE=1TBA4^B6ns}GhrH%*tKMxQXXo7h@ZYs&%baC$3-KA`A45#zyb{A3=b0QnjHe91j`yX
LL3_u#`|1Cp&)<^`zBz%A<UlxkyhlNV+tVh{^dIIAb-H@%bhP5cYN+XjC~j5ZninV;=_B)A4Gj%!?3h)&#;N=G%Ei;geJ(*-(!yd
e%Qc|CZz005LDujC79@^_w+CUgnW~QO?KK;C#-tzp6Dj<fm(7n=-;S(0$AFBsPa-NeSt&<YYI9+Vt?YIp)P>3vEO2pSnmR?s|))l
fQ?@TwAF?66F^H{n7aW@^}P8Lij7wWBc^_{oI^$(i@ASd&+I!}vkgyrU}(%^J`31{-SIC+*)+Qq-KuR2HWuGiud+cny!&pz_jkN{
HrNEepNz_L<vY8pZ18R^Yd3*^7x>|1f(aj^uD=J-Qs&7<rP=$=rA}hI(HpyQz;TMdV?E_NDqhcB#2njS6l<DPHAxb#vi}+9bD<dX
JQNn|mF6c#&szo)>Vs4X``KVW4EqqhQ4wwtOEXBY$b(2Z6M(0pG_rgM7KxsK1mnP4E__a9cHrx4+NIIU>+ZACU8>=HHF~~$XjQS8
;<2@OyvD~jMo;-i<mpgyWbMP`Nk6$}-&MwZ!+aR)7jE`Ga;&`7d)ItO7X;~KGO4T5SLnyMQ3cAOh(MCfGF>4FZ@2*2$2~ON2VrH^
1Rwz7-EiQ|s0vPRUjoE2&uSK%jR_JJ_Pa3=W+R>4EYBf~q{=t4R(79%LiMqaFmdp_631|{-;m`qF$to8_JZQUHGo3bh^7-BV#7Uh
^$l;oDaO7@whUNXO4>)s{nP%Jtd#c=wBe*skZD$A2m4=Y%?dIIA3$Em%i1A)7!@5`;CeRNHRP9LHL_8O(lTy5q-uD}KC%<`h54nU
!=sZv|M53z<thTB!%bZMA@osPKm)FjF2Siv9^DM#321|t8f9IoMv~)0n3}`xM0Z^3J)knr5W8k-w<lkgy))k7+G)Le*RYL)aTK^S
0FIMjh3gZpkS7MaGkOun;ut)7oQCs2LmQ$w^gJnGQ9P_hm1hQN<8~Dkj1Nenc?wR#g|sGRaLn^^MkfsuWn=tq3T0UYkA*>b2Dn*z
^2*Qv!FXp^c8@w8sut~YyC-+;qTi)3AghOG9{0SG*!zv#5T^EOy-31`pdUprbLI2kF<CBfo9e2dWkMAB+V@rs@B{^sdc{BVC#L-4
&iZ&Wtq!uMVu73lRMPJ5m1Gk1b7D^$q|-Zk$rlR!3L^*^?d<uW^+cV#)LmNjD>ATMoy1~iPCGfw@D)2s3&eC+DqUXnFLNrta-%>W
FQ25s!xdFo0Z8dPUJs!iCKkx5z|*ac!OZhPCx8qOnpodgFyos08jNQmH@s+by(E;Vr&K%NiRmXPOl?yL^d4dO-hDcQr@Ck25=A<F
gyQuRgDKoR;t_>vJH**bGIB|n&Cn@WVImac4b3RDmCz5|GY9`t&A4aYy;P0fomns?Q<zc|#G$`-=X|Kvo^7A*2T{1mEfiN`|D$qu
51*MPz3noI!L+kIceM%@z8;2|YTiKvPm-kmP?UfXBrd1@_&wak&Ph~JGAede`7$(Ln$RQ(9#%=ds*dCE)Z9a_-W~)_Fuy>b!T;Pw
iFc2T-fp|pBxGKwTq-!S?|buQW<b92j+^NYJBpi?a~mUNz`Hu(4<I{sf|1T5!BaIknc{@wWY?}vP`a=r<pzBJQnK4d34Sl|Nm5EM
Kt_<Ls_vkr0%P5c55qzd?*Jh6lG4R0eB*a+700NTy#S9BISQoA3J6FTXV9)7?ZP|>|GJYHV3cW6N*K>^9hV)Z--7%Z%mQjIS~fy3
)e}SdU`?qf;egr81%;(j?qGv*MY%oVC-x!R3{D~dc?ofvLOktBN;{y?+oXU$kk$-OEfBbhrx>a5(_RRA8tca2FRAGBFiwOoFmlH*
3S<P4Y=iMh3=)DuXR(YPK&bjx$|ymIL;aiB`pRddqv{ZI6!Ab>zuNX0whu;VGz%_ve{sqFI-G#Z7%}`dM-ZB;MmyI?p}MkfeZkP8
7ui!|Yd;i#jZ!WNcHFfeCOY!{Us`_?M9(rs!qXiO>v<BolS#M;kj-QoXp?XgXx=)B_cS~PSGP5987+b+#*=BA0I3Auz#PKlS$hnV
sX%gZMF=2tdxG^L#&dJpQqThx4DkS6AWrwW4*{s87Oz|{*ej`XKIj0x96^v$(pJkjOn?XeL!YqFI3QilBq>a+`@(1~lOo7aTPzbL
@yY0KF$dHl560<wwr$B^F%8^=i>U8cGnwpoQkFk(6~956Dz0u`WCxI<s$2w{AOS&A|D|0|0~q0YA#@A^BwvfyD>|?j&s}d8Ysqp+
rx3TM%Z2&Lrb}iJ69(EbHHr~VQH4cfAwr?&BH&l?OmxhrHKA<JhKdlwOtuH=KplZ{lR(lFe%X0DeEhq7oX+kL=63WSE*_ex9>9on
1+uqs=W7ryYPfvdKjyTNE4FUM#;w?_ZHR4Mv4sntVp~^il!~ogn>JI$rmospmD{KEiI8F=wF6HLvX&=M>vS%XD1>>9!TNn|vPRK^
3MZQP>|rY@e4yQdC}DQy&oG~4CejLFcGT+h;I8x!;G7%#%`z*uv6v@ndg8lD6+f)-f#v5_axvk>X++&#Lna=B&dG%us}B@5<d1~v
sf92Re-vHNJ-V7Obv`qBtJW}%C&J**IKZ_bT&x3(V88(i)er{qH4Ddtk&Lp19W)=NAJ6dNQU-UpvJ>ZfnCnlX<@aELV-UwjAW$i)
Bw)~KG*GdeDu|)e*ioP<6$Z*_NNMCu0kbD~!WI*fz?SpC<2I9=S={e_glya^2cw5f96cyNDE5SKik?0XF8zC$cl!6aMuU7I_=d-2
dNf+vg_Z=cL{9@ha#08Ifbv}w1X;qT{5vUX7{!UK-hd7+a}m<BssTv120FL1IKk0h_Wsyx=gn$iJ9t^Tu$UNS%@Sh4y2(;4Su8)+
`zow|<XtvA^PMP>Z)|DgOB8rU0$r#|GB>}Qs&JwKbEryxY*ayazrnJBz9@F=7^aN&A=Lk3=c0X<jyco3FPwj|Nx0B07ae|q<UU=8
F<{YiuG*0cD6iYH;^c%rE{jPR#N4(UOu86HxO+PNrDoe;UmP*596C{#cMP3R%u%JW^ceI0F`MAx%0($2;<KZ#M`!(k@R!WSV=cJ@
F!`1?!(8I>@cLwcISU2uq!WU|K`BeSGn??9h04dlH|{+Tqk~Zuz78UF=qsLutKAqHaGM#u4g{zY4_|s%vuKfd#|fS4K&jCHgfV)#
?lbjFltttuVPg=(vMhTB!Z>5Nz7!7V1O~Z>{xQ)dBLXxeMDj?(E=h*iG=W=Sj{%@j%JoMW(52OAmOdX2J`Hll22uLGuo8$lKp(bz
oIu5~|0tx<?2$&geEj<z7kF6V7xS^CXIB@08KuLsGwhIKHyI}|=+be2>v$5KNZKNhE*)uah9Lv|+{+fK<d8(q2g@0gg$SRkiiGF~
fiN3+@&ZU0^+OU5tU^@mVgC-I<#D*77b~d6cqL_VBM2=aR1Cc`6FC98-Q}zZu6QVEKTl?O2CRZkSdOSpE7H2ki<J0bqvMVidoprW
s9WP*-ERE6u=2B_3XJOZMg71W<(B;LXJP19Q^BVD3|LQD29rrze3)-<BYd^e4rH}#&iTxEx#wVr9fXOpfsB*wLJuykUoG~Pb_`3}
@h$Y;J3ii30D&NcDj*@p@_KI_a*UIE_aUPAKB4U9TU*aL@iUx{5XGN!+D8c4dM?Twg25v!P0vR=@_e=iiTb`8k3T0nzYkS|+H=tT
u;PbeT^4OVbs`rRe~yHNyV>Ft!mDj^wRH&Gq%;vT#{)e?LdUm7G2bKH@o}-yr!u7rcJpZRAAk3b53wqkKTmkvM^ObU+V;6MF}Ay<
idru)d2x>lWTB)#Rgw&-UK<2F69v{dup(6u2Rdwkl>(UxdGuBx$1M>|kBG$~^fM}yPHQ@GGjvClU^N_%s^WG`x9&(8$@pb?#@#Nj
yrL@|p({S{a*WJ?cxADC{;nxPw7{H`cv5A$7rS0ku}~~UP4nhlsn#r2t=Tq1BK1MyGF~P+>N=%?RY=^vt2K>R=uD+z&r!tHbY_IM
E(Grw?Fiu?AB$1u=0i@;95g<I!%0e2cq&zxL?!kicg^@BMNqx$<I^hK-OD?WT@Xk@eo<T1l*3%mga<g`;@YQcd@!a5E<G62gMXj~
WH^U;HS_89l&svmG4`fmzT8}eMy!P4n>J}A>j#<bNY(X&qUIK>&-tB*3<0`^lr==f>_OtQgoqEWyyYgqWzv*}y6~A?d9&po7jf+T
FOKWc<BRp!=*^d}?{M~};al6EF9nz8IXMZtGB?yTZ!Wl~<g6HG1*S(;XbY_E@Bbyxrt})#Yp8M>3aE%HDhmO|0<uQ1+oD0g6kl@6
(K=seOX5sl!`a1;z#(3$+)n^F-S&dTf?n+Mr$X6*IiJQ$&@d4FugX9^nlD8k94^M#ANS@pfUkiTQN>msXF?vpF}a+NMW|~E{Anoh
r=h~1R(IjUxL@M0R+(drEf(8_+E>lO;)yJK*+R5&41psf*z91A_*6ql`$3{HnlOBhN57k*W5w|=dvD-!FL+8Qw0;k&ONT$icLmSP
;HxxrZ^?Ujj_Kih!^mwJtX8<KNj8`6e=K}M8lUO_pp+5*hf`cW1gH@Om9qU`Tt?8_(P*4tHM7jJpt>ee_QqiXiQO99d9DOYm37Mh
h${!QD&}+v;T^}&l;a*6g{M3pqCz~(3zdF)bM^t>Ql|16z}7H|WiU1;w-Lg3ZJn?OH@XWK^i0SC<Fem=`%M(I7Qv&cDNuLIdEBG7
m=}KFYsnH@G2n*|0#V|1*U1vPT&`m*1_yiiax+z!@9;HGP@)aKEV?n$+&q14b3?CfGKjHNfj<)#<$4m7)Clqw@opF~=d6~vSYmAx
yLhqvNDq1_NVVJCf{D(yBcEt5>ZzLUMp5|gp^?1Yj8ZsxNTiQ@RJnaVY)d!#c5OhZoZ^4G{gg{lws+kjE4dPTd#YF5gu;EMLOFe-
lwu>40)&hi@E4Ldh~PFmUni5Ce2&vwE$2a;M(_(Z6%1zeN0~&Bl*o@nX}S0iLfl}%tx8mp;me^>on~cocqqBhs2gRx>L_1&`Ue0h
gjvXz2&Y4Y-noLYZc)EPYB+(2_m--WLa{_05UVA{B^S$tKifk<tV~^RZ)Hu1Ix>Wr<M6rE3g>Yd&BDbU+PPTJwk<qONTr5*4kUu<
2}T^8dLrvY`1s5I2ijJU2QS$M6KX8}07GJyifm=hA?Ci^3W7{J3Oxss>v$dOx9m^$nVsXT1rz=wI1mITZwm_~6M!F9f+1}Rzz|YN
WhIpUF{CA{7;_XqPIDA0JurR3?!@lIL~Ylp3ZhIWbqRRSV6qQZu-q_M3~`EYVVPkduFsT=+`@{(uqn&MQVQ4!)9)A-X8jz6KP828
qVOkD_)}4Ul@nwke3}@G*j8M{>AoVSs5@c&IJftB!-wH3x`q0>c_-A8@@Uz`N}<b@HpIwnknAATeTxpn;5+C{!H@&V?GEuH=xQ|#
M(>1+!0X|`LCqSe7T+HNTJ8=63wNVZzT7rQj4FQL7&ZKwV)e}~7DWeqkgywm!%p}#W{-h8Qwb7VMIpEqzKR*0o$%ErCO8H!oI7%%
5)SyY$u8Ns$v&|F;AcU!2q0N{S_NJb&@nJna8WMfFV_<BF7#>+hVY&pv1I4_p6`X%t|pZuarLW?+l%>2W24T9Yhc(Ax5U4-j}6BE
p&j;C9-84d?|*5AR9kh6R%pI3!`^sY0J+>{sOioiSdr_3mWYcgh@vtci}27BCJW6>G`(uwImVQ6e|lluim%lC%^mjtD~x^HW=x{!
UOX%h$|Hu~H}d<WJOUz0F~PyC-*yb-R`7WA4hP}wGVCaDA?^AR9sG#?-Y(Ju-M>pa8r3X2#a1FUj7I<AKis!FPr1ZhJybps@Jsx^
3rjOPf{pP`?ksIm!2I5B9NsO|8isT9O<HvRWJM<EA$CtF7*u6eDfcvRM+0Ao?HD7@hZe(pNB-d@$qfC%-g@PuMSV6osPX4{xCq>c
gI57ZgJ(t(4k~gEupy*Q5PNX)HQ{`@a3Ch*ncv~k{m^ExBW@fqI!<gdh-}FFa4(i#&Jp`UeC3I_#s~K_cO%vO4Vod0SYy)-U#%I5
%pHe#<^pG1*79Xo8!<PNt6GGzutkhlI8%uHl_wSU4yhl$a?Kh>FG(<truRR3Cnw_lk$S@{ysX{E8}Y)3ycXvuptrL#K#60zSFe>M
N$wSKqX)8vcscia$k`b{LDR_z!^_^~_FL{4LgTjYKa84BPGl+x7b2GwEtYCAK{<e_R<o{>>5_I5(wi(N5Y3;PTra%gF2@YlC!x$%
#Rb0Wkv_201L_mTGvoAT4dik$!vp!BJ{892R>oPvJj-Ruvs?o3fNu8FCqo>3prz8N)XDDP*(I)nThB@=+b3}YHbC@blf?xR5KOzs
v!pQP>Zh>&$r8wS%;7Ij;BuX$IR_=PdU`UVOW)$$AqL&AAEx*&fYmEe<l2F-$}(PyC`3r{iRDTxY{v9qgSAF%XtFMR=1!4_HG>Q=
pmUDU1u^%`ckHh!#|f~*@(y279u3<gLnXp5wroXRCr#MS&I;)o5mjkHnf4Rt<biZULkQ?XvIn@hCwmYrmTECa+doR+Ju~l_ewF}t
buIeY4LpM6+Eh@>kx!F;dYb)S6Ww9*4~TbOZY$LDD!S+&%f8gVD?PdAF|j|XxX8L;JGnB9eZ5|xzFt(CY$JD4>&}BgB0IIg{(e)e
ThL~SwmSZplx5O+S`a1vNRAUvU4IGg5|8(kN8Eev(X;g;gnk~>W9%9uJy5042e3P@l#e1nC(up2KI5E=jcEmJy$xKm@KDJ4a#3^r
dl&oFkXcPlzSbsc9Xc(Br|*)-rKT33SX)l$kkaY-b^q%0;tFX^!f_PrY1h**#sh(v`MR37oX_1A9z-MRxN$^t3TyRZrVWmc_DVl9
LV8;f&9+O1Td+nMp6`gwd$XC?x*B#cVr-96?V8Qx1ezGXFDROu&Dd;~LS$8i%dp^s05u#{;PZZj6@_2(MZL>tYXd;kb1uVwm=6dy
!*_X|%ZOcu@-y=~!ttQzfiMPqjs-q|e2+NyR`5UtWs|gjsz54aZ9|l#N*(><l-1q(zr!V^@E%N{M@L#5STXJ?+I2F2#HpuV3Qj+m
7%n4+bPt}FhqrBZ3uBe)mnvO3*NLPYLIf7ZPJoq6K*fS<Dev7Sd=~$}GZFmIFFZO?fG2Gz_@RTbym(5s2f?2=<3s)Z#VsqBjZtqN
xErd3^%hGXF3jG<4d?49pz?;S)A(Rk;+)jubU6=X`G(VbWaFBf&t8BqFel#sq0Z>%#g<PDf2)yG%ie0a0#=qYu#$K^hsbg36oz1>
$}Ld~Uy5H+5}c+-R*)V;!h#6C9hfm&-N~CcmXICde4IXWflUc#;YhV;mnW*lvL%{Q`3wPl#MRy2U6AO|0#QoU+B&I&tQzlH4JMeD
3=_~3${uuXqz=#HTO~7E#N?Hk+mI!@fW!o?snw8d;mL13|I!3d4Pz?RB6$eppVjNZvx8mqS#2ip=1VpWIkqDO+~xDRK3`U+p|Nj+
rc4q}ozWac;oUTUkB<c&;xKx9hG0}99s-%tD-l95(wUS$afPr3sYw-2!6TMYEnk68?d^ic{$7HgmD7`*s6+n^K|Dm*2auS64=!I`
U3|Ri4+dpMPifynsFlIWt02M^$C)o5gQ(090X$YEr&arT?KjwDzK*A4qHF@{&g18JFHZa*igJz%A_98tyi%cTafQElC4K3Njm2-7
NftP_3V5W#&+2CY#Zl(*YpA<`g)K^o!o0a%$qgFaWxjwV&+R?)GX7|-^Wo;~%sIR~Jvuydj&81<lf$zQ4!)A?46d(EFP+2lW9JY+
KJ~B8`v7uy=^ULLetzG-a=x_7438s0URZYHJEv~ie{MG3{fBR#H_78ud;0z|`1hoCtf0^z+szg)x6Q8U*=^5i*%QAL_;u4W8;w?{
ZFSndH|eyxzUxnXYizo<)f@-icFXH_>Tcb0+d-q%Ei-@l;D!s19!~6UiEXN@i@#Xj8FKn$;(Rj~X8}o_9NGeN?*ed>;-zYtkowtA
8sMAO^i~>fnvIxrqT);F78e?Z?g0~EF~}r{A*xU=gQ;AV7ZX>-w%q2*2kZ}S5`|BW`b}OU$jcKL7S$QjK#4(Q6wEiU%+QwD;2ExC
d@(`nmuaBuVly8%hRdpo4q_84htL?u@q_XD4u8iH518ONM9^?xYGeG1+q73I@3B0m&JCAoA%b{_ery;r8u3!(;2HXV=s&?KRQ_kb
S6rsW4wp4vT;qDao48!ZUlHE(*AJ^$mz!_`z@T}9IN>=KMjGP*Ik9n|1AnZ10M4RX{+~tJ*n{u|<_l=9IR1*TUf#hLc2pLp^>PE}
T#oo)wf7i>N#Km1VOn%#PQAAz1-jaUaN3v8!DbNz(^>LO+s1Z!e%!z8!^im!!#ldZ0kE6%(+?L{pPeIsxw<$#b}kRWw;3r(v`wqg
bo!?sPp+Nw)APP_bOEM%<y>7{T=x+k)Ys|X9-ZAB!)^ad|LUuAesTWq{?&zZIe0<vtbh2WKLChh_yqQ@PsHA_5csex3;<Fzrdr4f
$|HKs3n8DdvbHZzz{u=w3peZT^4R%&2m`)#fU)b-Bk1(=>G{PK`0qvqJ*1#$LsF6LN0&#&8^oDq|9@f@#VTCh!1?R+`otNW9>dI>
emoyImuEM`<c+-C`k*-!kHK4ZP}b-DkB8T%U-~a5Ps}l>z|rX$PVwMo(1(!^CGTaG_dx86rCEdRXuo--9ZR=62CIBfnGUT>MpQb5
%=V8z_MH!>@2~n!+v$kW3+=kTx&axS93Ef%C6#QjJ)-jq=f-k?kY$<9;q~?5DXJp09$kFCJnP?{UVnAoU);c=0;|aR$9@i#mLptW
2K}S!3tV2D!NtwhQQx^ZKl=(A4AOG0`bQU}!Nq=8dkgm=ASsYds$U!56HAV0+yi^}!#i-2ShNl4$9VzEalpJC2R)<Xln;c5Ed4*e
bq_c
"""
source=zlib.decompress(base64.b85decode(''.join(DATA.split())))
assert (len(source),hashlib.sha256(source).hexdigest())==(24021,'9610e0e8499d072b15932d76d38e184532ed52d91793d9fc0e02631ef2d76d89')
name='hex6_cap_sector_v7.py'
Path(name).write_bytes(source)
args=sys.argv[1:]
if args!=['extract']:
    assert args in (['build'],['check'])
    sys.argv=[name]+args
    d=runpy.run_path(name,run_name='__main__')
    report=Path('hex6_cap_sector_v7.json').read_bytes()
    assert (len(report),hashlib.sha256(report).hexdigest())==(3620884,'c5eb3f969b9ba26c9add39930dbad2fad672af4761e57d52b613d8b4d51579e1')
    # Additional positive retained-core/two-ear fan, on the whole open cube.
    # All determinant expressions are multiaffine; all Boolean corners give
    # a complete exact identity check, not a sampled positivity inference.
    T=((4,3,2),(4,2,1),(4,1,7),(4,7,6),(5,6,7),(3,9,2),(9,8,2))
    F=d['F']; _,_,c,e0,e1,e2,e3=d['VC']
    count=0
    for q in d['product']((F(0),F(1)),repeat=5):
        x,y,z,u,v=q
        expected=(c,e0,e1*(1-z),e1*z*(1-y),e2*(1-x)*y*z,e3*(1-v),e3*v*(1-u))
        U=tuple(d['sub'](p,d['A']) for p in d['source'](q))
        actual=tuple(d['det'](tuple(U[i] for i in ids))/6 for ids in T)
        assert expected==actual
        count+=7
    assert count==224
    print('POSITIVE_RETAINED_CORE_TWO_EAR_FAN_224_EXACT_IDENTITIES_PASS')
```

### Supplement: actual q7 wall inside q8>0

Save this complete unit as `hex6_cap_wall_v7.py` after extraction.

```python
#!/usr/bin/env python3
"""Supplement to the autonomous V7 source: an actual q7 wall inside q8>0."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import hex6_cap_sector_v7 as h
assert hashlib.sha256(Path(h.__file__).read_bytes()).hexdigest()=='9610e0e8499d072b15932d76d38e184532ed52d91793d9fc0e02631ef2d76d89'
box=tuple((F(a),F(b)) for a,b in (('4/5','4/5'),('7/10','7/10'),('1/100','9/100'),('9/10','9/10'),('1/2','1/2')))
k=tuple(map(F,('-1','-3/4','11/20')));kw=h.mv(h.TRANST,k)
ok,res=h.prepare(box);assert ok
X,c,ti,den,c0,R,C,eta,contraction,need=res
assert min(v.lo for v in den)>0 and eta>need
guards={}
for f,(n,a) in enumerate(h.raw_normals(h.source(ti))):
    if f==7:continue
    r=a-h.dot(n,h.A);support=a+r*h.dot(c,h.A)
    assert support.lo>0
    value=h.dot(h.add(n,h.scale(r,c)),kw)
    if f!=7:
        sign=-1 if f in (1,6) else 1
        assert (value*sign).lo>0
        guards[f]=value
ends=[]
for z in (F(1,100),F(9,100)):
    _,Q,_=h.actual_point((F(4,5),F(7,10),z,F(9,10),F(1,2)))
    ends.append(h.dot(Q[7],k))
assert ends[0].lo>0 and ends[1].hi<0
report=dict(box=box,kernel=k,c0=c0,C=C,R=R,eta=eta,contraction=contraction,selfmap_slack=eta-need,non7_normal_guards=guards,q7_endpoint_values=ends,conclusion='A genuine q7=0 shadow wall exists inside the q8>0 chamber, with the ten-vertex lattice unchanged. No full mechanical census on the cut path is asserted.')
b=(json.dumps(h.serial(report),sort_keys=True,separators=(',',':'))+'\n').encode()
Path('hex6_cap_wall_v7.json').write_bytes(b)
print('ACTUAL_Q7_WALL_INSIDE_POSITIVE_CAP8_CHAMBER_PASS')
print(len(b),hashlib.sha256(b).hexdigest())
```

Convenience copies only: recovery wrapper (`recover_hex6_cap_v7.py`), readable autonomous verifier (`hex6_cap_sector_v7.py`), exact full report (`hex6_cap_sector_v7.json`), wall verifier (`hex6_cap_wall_v7.py`).
