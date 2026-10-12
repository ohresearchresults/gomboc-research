# minimum-0210

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# HEX6_UNEQUAL_TRANSVERSE_NINE_TEN_SHADOW_ALL_ROOTS_V6

## 1. Main mathematical advance

**A genuinely unequal, seven-parameter sector of the fixed-six-pole atlas is now excluded from rank-two rooted feasibility at EVERY root, not only at apex0.** Every shadow in this sector has nine or ten true corners. The sector crosses a genuine projection-incidence wall, where one original vertex becomes a boundary-interior projected point. It is therefore outside the scope of the earlier six-corner theorem and is not a re-examination of its tangent-kernel boundary.

Use the unchanged labelled actual body P(x,y,z,u,v) defined in section3. The five cut parameters vary independently in the CLOSED box

    3/4  <= x <= 17/20,
    13/20 <= y <= 3/4,
    1/200 <= z <= 1/10,
    3/20 <= u <= 1/4,
    1/4 <= v <= 7/20.

Independently choose

    -77/100 <= s <= -73/100,
     53/100 <= t <= 57/100,

and define

    k=(-1,s,t),
    L=((s,1,0),(t,0,1)),
    M0=L^T H L,  H any symmetric positive-definite 2x2 matrix.

The theorem covers **all orientations and condition numbers of H**, including every finite weak-arrow boundary. For every actual body and every such M0:

1. No true-edge weak arborescence exists toward any of the ten labelled vertices.
2. The true weak-arrow graph has at least two strict unstable vertices in the singular quadratic-form test. This stronger vertex statement is justified here because no true edge collapses under L anywhere in the sector.
3. In particular, there is always a nonapical strict unstable vertex. An apically unstable metric is not a sole-U metric.

There is also a genuine SPD consequence: the compact normalized rank-two family has a uniform open neighborhood in which every SPD metric has at least two strict U vertices. **The width of that full-family SPD neighborhood is not computed.** Separately, two explicit actual bodies have complete reciprocal SPD pencils with strict222, physicalweak000, for every 0<epsilon<=1/100000.

The entire cut box is outside the old small-cut class because x>=3/4, and outside the deep almost-diagonal band because x-z>=13/20. The actual base pole satisfies q6·k<-1 throughout the certified sector, so these kernels are uniformly transverse to F6. No new seven-corner sharpness assertion, whole-atlas exclusion, U1 construction,110 attainer, or global complexity-bound change follows.

## 2. Source authority and evidence level

The authoritative parent is

    minimum-0209
    SHA256 adebd2f62354466c4f5cdadbb45aec998631c8d8854876b6c92411d83403ff1c
    HEX6_SIX_CORNER_SHADOW_OBSTRUCTION_AND_BASE_TANGENT_U2_V5.

The literal changed hexagon, partial cut through B2, ten labels, true facet cycles, and actual-centering construction are retained. They are not replaced by the original integer hexagon or either degree-five control. The parent supplies the same exact source model.

The new theorem is an **executed exact interval certificate of an entire closed parameter product**, together with analytic shadow and graph arguments. Floating stress discovery is not its proof. Its autonomous standard-library recovery constructs every predictor, validates the actual centroid, checks the shape and projection guards, verifies the positive-definite stresses, and exhausts the relevant rooted boundary paths.

The previous small-cut, deep-band and tangent-kernel exclusions are not dependencies of this new computational certificate. The full reconstruction below needs no parent source file, numerical checkpoint, solver or external package.

## 3. Exact actual geometry and uniform volume moments

### 3.1 Unchanged source model

Set

    p = 1/100000 * (
      (60401,-32565), (80000,-20000), (0,60000),
      (-80000,80000), (-483861,-325040), (-447814,-355009));
    A=(0,0,1), q_i=(p_i,1);
    b=(2615613/500000,816129/250000,-3);
    B_i=[q_i;q_((i+1) mod6);b]^-1(1,1,1).

For the independent fractions, define

    Y0=A;
    Y1=B1; Y2=B2; Y3=B4; Y4=B5;
    Y5=B0+x(A-B0);
    Y6=B0+y(B5-B0);
    Y7=B0+z(B1-B0);
    Y8=B3+u(A-B3);
    Y9=B3+v(B4-B3).

The actual maximal facet cycles are

    F0=(0,4,6,5), F1=(0,5,7,1), F2=(0,1,2),
    F3=(0,2,8), F4=(0,8,9,3), F5=(0,3,4),
    F6=(4,3,9,2,1,7,6), F7=(5,6,7), F8=(9,8,2).

The true edges are

    01,02,03,04,05,08,12,17,28,29,34,39,46,56,57,67,89.

Thus every member of the theorem has exactly10/17/9, degree(0)=6 and degree(2)=4. All five fractions in the CLOSED theorem box are still strictly between0 and1. No merged-incidence boundary object is counted as a witness.

Put U_i=Y_i-A. For a parameter c define

    d_i=1+c·U_i,
    X_i=A+U_i/d_i.

The intended body is the newly uniformly filled convex hull of the X_i, at the unique positive-actual-denominator solution of its volume-centroid equations. It is not obtained by transporting the source centroid.

### 3.2 The actual fan

The seven positive apex-fan tetrahedra have nonapical triples

    (4,3,9), (4,9,2), (4,2,1), (4,1,7),
    (4,7,6), (5,6,7), (9,8,2).

For a triple T={i,j,k},

    v_T=det(U_i,U_j,U_k)/(6 d_i d_j d_k),
    V=sum_T v_T,
    g=(1/(4V)) sum_T v_T(A+X_i+X_j+X_k).

The second moment is the genuine tetrahedral second moment:

    E[XX^T]=(1/(20V)) sum_T v_T
      [(A+X_i+X_j+X_k)(A+X_i+X_j+X_k)^T
       +AA^T+X_iX_i^T+X_jX_j^T+X_kX_k^T].

In particular, the covariance is not replaced by the covariance of the tetrahedral centroids. The same determinants and denominators determine all moments.

The source verifier checks the factored multiaffine expressions for the seven raw volumes at all32 Boolean cut corners:224 exact equalities. Since both expressions are multiaffine, this proves the identities everywhere, rather than sampling their validity. The unnormalized support slacks are likewise multiaffine; their corner coefficients are nonnegative, and each of the56 nonincident slacks has a positive coefficient. They are therefore strictly positive throughout the open source cube. The elementary truncation geometry gives the displayed nondegenerate facet cycles. An exhaustive supporting-triple audit and two distinct positive tetrahedral fans are also checked on the literal unequal source used below.

### 3.3 Actual-centroid inclusion, not a rounded locator

For a uniformly refilled star image,

    D_c g=-Hc,
    Hc=5 Cov(P)+(g-A)(g-A)^T >0.

This follows by differentiating the projective volume and first-moment integrals. The positive-definite covariance makes g strictly monotone on the convex positive-denominator domain, so at most one centroid-zero parameter exists.

On each certificate cell the recovery constructs rational c0, a rational affine cut predictor C, and a rational preconditioner R. Write

    c_pred(q)=c0+C(q-q_mid),
    q=(x,y,z,u,v).

Automatic differentiation of the SAME actual moment formula encloses the five derivatives of g(c_pred(q),q). The mean-value formula bounds the residual throughout the cell. For the unknown correction r in [-eta,eta]^3, the verifier checks that

    r -> r+R g(c_pred(q)+r,q)

maps the entire correction cube strictly into itself, uniformly over every cut in that cell. Brouwer supplies a zero for each actual cut vector; strict monotonicity identifies it uniquely. All actual projective denominators are enclosed positively at the same time.

The proof uses outward dyadic intervals with80 fractional bits. No floating arithmetic determines a verification decision. Across the completed cover, the exact checks give

    every actual d_i >9/10;
    infinity-norm contraction bound <21/100;
    correction-cube self-map slack >1/10000;
    every actual vertex norm <18.

A fixed rational working-frame preconditioner is used only to reduce interval cancellation:

    T=((27/10,0,0),(9/5,9/10,0),(-1/2,1/20,7/10)),
    X'=T^T X, c=T c'.

All projection and mechanical quantities are transported back consistently. This is an invertible linear calculation frame, not a changed literal shape, a second centroid, or independent primal/polar metrics.

## 4. Exact nine-/ten-corner classification, including the wall

For a raw outward plane n·Y=h, let r=h-n·A. Its star-image outward normal, before positive support normalization, is

    n_star=n+r c.

The exact cell guards establish

    sign(q0·k,...,q6·k,q8·k)=(+,-,+,+,+,+,-,-),

while the sign of q7·k is deliberately unrestricted. They also establish the stronger base transversality q6·k<-1.

An edge is a strict silhouette edge when its two incident facet normals have opposite signs on k. Applying this to the true edge/facet incidences gives precisely the following possibilities:

    q7·k>0:
      Q=L P has10 corners, in cycle
      (0,1,2,8,9,3,4,6,7,5).

    q7·k<0:
      Q has9 corners, in cycle
      (0,1,2,8,9,3,4,6,5);
      vertex7 projects strictly inside Q.

    q7·k=0:
      Q has the same9 corners;
      vertex7 projects into relint[p6,p5].

Here p_i=LX_i. At the wall the triangle F7 projects to the boundary segment [p6,p5]. The fibre through p7 runs from vertex7 to a point in the relative interior of the genuine opposite edge56. It is not a new true mechanical edge.

There are **no collapsed true edges** in any of these cases. A collapsed edge would require k to be tangent to both incident facets, whereas at most F7 has zero normal value. Every true shadow corner therefore has a singleton true-vertex fibre. All ten projected original vertices remain distinct.

This classification uses actual supporting planes and the true graph. It does not declare an integration diagonal to be mechanical or infer a projection hull from a finite collection of locators.

## 5. All-root metric exclusion by eleven sparse actual stresses

### 5.1 Why boundary paths suffice here

Let H>0. Along a true weak arrow,

    |p_j|_H^2-|p_i|_H^2
       =2 p_i^T H(p_j-p_i)+|p_j-p_i|_H^2>0,

because no true edge collapses. Thus the true weak-arrow graph is acyclic.

If a true rooted system existed, its root would be uniquely farthest among all projected original vertices. Its projection must be a true corner of Q. Conversely, every strict radial-maximum corner of Q exposes a closed true fibre: all true arrows leaving that fibre are strictly negative. Therefore rooted feasibility forces Q to have just one strict radial-maximum corner.

At every other polygon corner, at least one boundary arrow must be nonnegative. Both cannot be nonnegative: the direction toward the interior origin is a positive combination of the two incident polygon-edge directions, and its dot product with that corner is negative. The resulting weak boundary graph is a path obtained by deleting one edge of the polygon cycle and orienting the remaining path toward the root.

There are9x9=81 such rooted paths for the nine-corner cycle and10x10=100 for the ten-corner cycle: **181 in total**. At the wall the nine-corner argument applies; vertex7 is not silently treated as a corner. This argument establishes rooted reachability, not merely a singular strict-U count.

### 5.2 Literal stress rows

For an actual projected directed edge define

    A_ij=-sym[p_i(p_j-p_i)^T].

For a row of positive integer weights, let

    Q_row=(sum w_ij A_ij)/(sum w_ij).

The complete row bank is below. Each triple is (source,target,weight).

    R1:  (3,4,912), (4,6,100000)
    R2:  (3,9,100000), (8,2,30227), (9,8,80028)
    R3:  (0,5,100000), (4,3,8389)
    R4:  (2,8,54144), (8,9,100000), (9,3,6653)
    R5:  (2,8,100000), (3,9,62853), (4,3,28552)
    R6:  (0,5,100000), (3,4,2776), (9,3,9356)
    R7:  (1,2,1515), (2,8,1358), (4,6,100000)
    R8:  (1,0,100000), (8,2,1305), (9,8,2098)
    R9:  (2,8,1000000), (6,5,385386), (9,3,51250)
    R10: (2,8,1000000), (4,3,223767), (8,9,975510)
    R11: (2,8,615088), (8,9,1000000), (9,3,208595)

There are11 rows and31 terms. All arrows are genuine primal edges.

The exact adaptive cover has

    515 closed seven-dimensional leaf cells;
    1029 total subdivision nodes;
    maximum bisection depth10;
    5441 valid row/cell applications;
    10882 positive interval Sylvester-minor guards.

On each cell, the verifier retains a subset of rows for which

    Q_row-(1/10000)I2 >0

holds throughout the complete simultaneous cut, kernel and validated-centroid enclosure. Every one of the181 rooted paths contains a retained row. The retained subset may vary between cells; it is NOT asserted that every listed row is valid everywhere.

For any retained row and any H>0,

    -(sum w_ij D_ij)/(sum w_ij)
       =tr(H Q_row) >(1/10000)tr H.

At least one selected arrow is strictly negative. This contradicts the weak inequalities of the rooted path. Thus all181 possibilities, and consequently every true rooted system at every root, are excluded.

The subdivision always replaces a box by its two closed halves. Exact Kraft sum1 and total box-volume equality are checked. No cell is discarded as numerically infeasible. All finite cut and kernel endpoints and the q7·k=0 wall are covered.

### 5.3 A physical neighborhood, with no invented numerical width

Normalize H>=0 by tr H=1. Rank-one H also cannot support a true rooted tree: the positive and negative extreme faces of its scalar projection are two disjoint closed weak-arrow sets. Hence the entire compact normalized family, including its rank-one boundary, is rooted-infeasible.

Let beta be minus the maximum, over that compact family and every rooted true spanning tree, of the minimum selected primitive. Then beta>0 by continuity and finite-tree compactness. Since all actual vertex norms are below18, changing M by E changes any primitive by at most648||E||op. Therefore every SPD matrix within beta/1296 of this normalized family has at least two strict U vertices.

This is a proved uniform-neighborhood existence statement. **Beta has not been numerically evaluated.** In particular, the1/10000 projected-stress margin is not misreported as a directly computed full three-dimensional neighborhood width. Nor does this neighborhood exclude SPD components staying away from the rank-two family.

## 6. Two exact actual222 pencils and a genuine projection wall

Take the two literal cut vectors

    P10: (4/5,7/10,1/100,1/5,3/10),
    P9:  (4/5,7/10,9/100,1/5,3/10).

Each denotes the unique algebraic actual-centred body from section3. Rational cut inputs do not imply rational star-centred coordinates.

For both bodies use

    s=-3/4, t=11/20,
    L=((s,1,0),(t,0,1)),
    H=((23403/500000,87/500),(87/500,1)),
    det H=1653/100000,
    M_epsilon=L^T H L+epsilon e1 e1^T,
    0<epsilon<=1/100000.

There is ONE reciprocal metric N_epsilon=M_epsilon^-1. If Hinv denotes H^-1, its exact expression is

    N_epsilon=((1/epsilon,-s/epsilon,-t/epsilon),
      (-s/epsilon,Hinv11+s^2/epsilon,Hinv12+st/epsilon),
      (-t/epsilon,Hinv12+st/epsilon,Hinv22+t^2/epsilon)).

The determinant of M_epsilon is epsilon det H>0, and the block construction proves SPD. At epsilon=1/100000 the complete literal pair is

    M=((1482307/8000000,121191/2000000,839/2000),
       (121191/2000000,23403/500000,87/500),
       (839/2000,87/500,1)),

    N=((100000,75000,-55000),
       (75000,93081250/1653,-783950/19),
       (-55000,-783950/19,2874019/95)).

The exact full physical censuses, valid for the ENTIRE stated positive epsilon interval, are

    P10: S={4,6}, U={0,9}, H={28,57}, physicalweak000.
    P9:  S={4,6}, U={0,9}, H={28,56}, physicalweak000.

All68 true-edge primitives are nonzero throughout each pencil. The proof uses the affine dependence of primal primitives on epsilon and of epsilon times each reciprocal polar primitive on epsilon. Their endpoint signs agree strictly, so no physical weak wall is omitted.

At epsilon0 the singular true graph has exactly the two singleton sinks0 and9 on both bodies. All34 singular primal primitives are nonzero. The complete set that can reach0 is exactly

    {0,1,2,5}.

Thus these controls explicitly fail rooted reachability; no collapsed two-cycle is hiding a supposedly successful system.

The validated sign of the unnormalized q7·k numerator is positive on P10 and negative on P9. Continuity of the unique actual-centering parameter proves that a genuine q7·k=0 body occurs between them while the ten-vertex lattice remains unchanged. At that wall vertex7 is boundary-interior in the shadow, as classified in section4. The all-root exclusion covers the wall. **No full physical census is asserted for the entire cut-interpolation path:** the two saddle labels already differ at its endpoints. The complete222/weak000 interval assertions concern epsilon on each of the two fixed actual bodies, not all intermediate z cuts.

## 7. Exact countercontrol to a uniform-row shortcut

The choice of valid rows really must depend on the geometric cell. On the actual body with cuts

    (3/4,13/20,1/200,1/4,1/4)

and kernel

    (-1,-73/100,53/100),

the matrix of R4 satisfies

    (Q_R4)11 < -1/20.

Thus R4 is not a positive-definite stress on the whole box, despite its validity on many cells.

This failure is realized with a physical reciprocal pair, not just a formal matrix. Set

    H=diag(1,1/100),
    M=L^T H L+(1/100000)e1e1^T,
    N=M^-1.

The exact weighted sum of the three ACTUAL R4 primal primitives is greater than1/20. Nevertheless the complete physical census is

    S={4,6}, U={0,4,8}, H={01,05,39}, physicalweak000,

with all68 primitives nonzero. Other certified rows prevent a rooted system. This countercontrol explains why replacing the cellwise cover by a claim that all eleven rows work everywhere would be false. It is not a U1 counterexample to the theorem.

## 8. What remains genuinely open

The result closes a substantial transverse sector with the maximum possible ten shadow corners, a neighboring nine-corner stratum, and their actual wall. It does not classify all seven- or eight-corner shadows, and it does not settle seven-corner sharpness even in the weaker -Q/3 relaxation.

A concrete next geometric extension is the adjacent cap-sign chamber q8·k>0 with the same six side signs and q6·k<0. True incidence then removes vertex8 from the shadow: the boundary subpath2-8-9 is replaced by the genuine edge2-9. Depending on q7, the cycles have eight or nine corners. The present row bank and certificate do not claim coverage there. More distant completion parameters, other side-sign chambers, and full-rank metric components away from the singular boundary also remain open.

The reusable advance is the combination of an exact true-silhouette classification across a projection wall, actual-volume centroid inclusion on an independent cut domain, and sparse stresses covering every projected rooted path at every root. Neither a uniform planar density nor free tetrahedral masses enter the proof. S1, H0 and proper110 remain separate obligations; the supplied physical constructions are222 and233 nonwinners.

## 9. Complete source-only recovery and observed execution

Save the entire following fence as `recover_hex6_transverse_v6.py`, UTF-8/LF. It contains the full autonomous readable verifier, all geometry, all eleven rows, the exact adaptive cover generator, the actual-centroid inclusion calculation, all three controls, and every reconstruction parameter. No sandbox file is required as an input.

Environment actually used: CPython3.13.5, standard library, assertions enabled.

    python -B -S recover_hex6_transverse_v6.py build > build.out
    python -B -S recover_hex6_transverse_v6.py check > check.out
    cmp build.out check.out

`extract` writes the complete readable `hex6_transverse_all_v6.py` without executing it.

Exact pins:

    recover_hex6_transverse_v6.py:10937 bytes
    SHA256 c49f5b2aa073f54310812a9dd5d8aea47439fac36da9665ca1ff46d913b72946

    hex6_transverse_all_v6.py:20888 bytes
    SHA256 b6736e2df1dcfad568acaf0ebc540d6b4d390ca66e677d37665f1d29dcade3a6

    hex6_transverse_all_v6.json:774526 bytes
    SHA256 9230a6dd4ca9bbccfe71084cb390cbcc99cad4a8837607156a0a31c24ec8cdcb

    build.out=check.out:542 bytes
    SHA256 c66af0acf301ae8ebd28f46b24d54dd99dc6fffc4270ea94f1d339166d21921c

The complete exact build and check were executed. A fresh directory initially containing ONLY the final recovery wrapper then ran both commands. Its readable source, report, and stdout matched the original run byte-for-byte. This is author-executed source-only recovery, not an independently written verifier or proof-assistant formalization.


[Encoded source block omitted; the code in this passage is incomplete.]


Convenience copies, not dependencies of the handoff: complete recovery wrapper (`recover_hex6_transverse_v6.py`), readable autonomous verifier (`hex6_transverse_all_v6.py`), complete exact report (`hex6_transverse_all_v6.json`).
