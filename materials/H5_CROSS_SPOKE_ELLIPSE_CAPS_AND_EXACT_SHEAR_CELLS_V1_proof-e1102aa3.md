# material-e1102aa3d0a8

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# H5 cross-spoke ellipse caps and exact fixed-G shear cells V1

## Authority and scope
This is a coordinator-authored continuation of the literal physical H5 normal-cone result minimum-0250, completely read in two pages with unchanged SHA-256 2cf87f1bc07e373e4dd87a52a48d1a91b98eb48ba17601cf28e76afe3e39c233. The parent's geometry is seven basal vertices and three top vertices, not two pentagons. Its 2316-certificate off-macro all-taper tube and exact fixed-shear G-disk decision are separate accepted author findings, not coordinator replays. The present contribution is a general cross-spoke cap identity, a necessary compact shear/normal-height enclosure, and the transposed exact decision over ALL shears at a FIXED rational shape and tangential metric G.

No whole-H5, whole-incidence, C34 exclusion, or attaining proper110 body is asserted. Global accepted 34 <= C_min <= 622 remains unchanged. A fixed-G nonexistence statement cannot be counted as an all-metric shape exclusion. No external novelty priority is asserted.

## 1. Setting and exact caps
Let a full-dimensional convex polytope have all vertices z_i=(x_i,h_i) in the two planes h_i in {0,1}; let its actual interior centre be g=(c,gamma), 0<gamma<1. Each level must contain a nondegenerate polygon. The argument itself permits any interior centre, but the application uses the actual homogeneous volume centroid. Let G be SPD and normalize tr G=1. Every full SPD metric has the unique representation

M = [[G,Gv],[v^T G,v^T G v+eta]], eta>0.

Define a_i=x_i-c, k_i=h_i-gamma, Y_i=a_i+k_i v. For a directed true edge i->j,
D_ij = Y_i^T G(Y_j-Y_i)+k_i(h_j-h_i)eta.

On a cross-layer edge put sigma=h_j-h_i, c_i=-k_i sigma>0,
r_i=-a_i/k_i, d_ij=-(x_j-x_i)/sigma,
m_ij=(r_i+d_ij)/2, rho_ij^2=(r_i-d_ij)^T G(r_i-d_ij)/4.
Then the EXACT identity is

D_ij/c_i = -(v-r_i)^T G(v-d_ij)-eta
          = rho_ij^2-(v-m_ij)^T G(v-m_ij)-eta.

The cross exit D_ij>=0 therefore cuts out a closed elliptic cap in (v,eta); a strict exit uses its interior. For a basal/top spoke the two directed ellipse disks have a common endpoint d=x_base-x_top. Moreover d=gamma*r_base+(1-gamma)*r_top. Thus their open disks are disjoint and externally tangent at d in the G geometry. This is also consistent with D_ij+D_ji=-|z_j-z_i|_M^2<0.

## 2. Why at least one cap is necessary for U1
In each layer choose a vertex maximizing |Y_i|_G^2 over that layer. Its same-layer neighbor derivatives are all strictly negative: for a distinct neighbor j,
2 Y_i^T G(Y_j-Y_i)=|Y_j|_G^2-|Y_i|_G^2-|Y_j-Y_i|_G^2<0.
There are consequently at least two same-layer sinks. If the full SPD body has exactly one strict unstable vertex, a sink in the other layer must have a nonnegative cross-layer true-edge derivative; otherwise it too would be a strict unstable vertex. Thus every U1 metric, including incidental weak contacts, belongs to at least one of the directed cross-edge caps in section 1. For literal H5 there are exactly seven undirected spokes and fourteen directed caps.

A shape- and G-specific rational enclosure follows. Set
H_G=max_cross (|r_i|_G^2+|d_ij|_G^2),
R_G=max_cross rho_ij^2.
Any cap point satisfies, writing u=v-m,
|v|_G^2+eta <= |m|_G^2+2|m|_G rho+rho^2
                <= 2(|m|_G^2+rho^2)=|r_i|_G^2+|d_ij|_G^2.
Therefore U1 NECESSARILY satisfies

0<eta<=R_G,  v^T G v+eta<=H_G.

This controls M_zz directly. As tr G=1, lambda_min(G)>=det G. Choose an integer B with B^2 det G>H_G. Then all U1 shears lie strictly inside [-B,B]^2. This cap bound needs neither a guessed conditioning limit nor a frozen-centroid approximation. It remains a necessary restriction, not an existence theorem. Its application below is for each fixed SPD G; no compactness of the coordinate v uniform over singular limits of G is asserted.

## 3. Exact finite decision at fixed rational shape and G
At eta=0 every same-layer directed derivative is an affine polynomial in v=(v1,v2). Divide each cross-layer derivative by its positive c_i: every resulting quadratic has the SAME quadratic part -v^T Gv. Literal H5 has twenty affine rows and fourteen quadratic rows.

The zero sets form a finite arrangement of lines and homothetic ellipses. Two quadratic equations subtract to a line. Hence pair intersections and vertical tangencies have abscissae of algebraic degree at most two. Build all critical abscissae: vertical lines, ellipse vertical tangencies, pair intersections, horizontal-box boundary intersections, and the two vertical box boundaries. Duplicate or extraneous events do not hurt completeness. Between successive critical abscissae choose a rational x. Intersect every curve with this vertical fiber, order its real roots exactly, and choose a rational y in each intervening open interval inside the box. Every open two-dimensional sign cell of the entire bounded arrangement is met. Outside the box U1 was already excluded by section 2.

All critical and fiber roots of rational quadratics are ordered using primitive integer minimal polynomials and successively refined dyadic rational isolating intervals. No numerical feasibility or floating-point sign acceptance is used. A representative's thirty-four derivative signs are exact integer evaluations after clearing denominators.

At a generic representative all thirty-four signs are nonzero. A projected sink has only negative outgoing signs; positive exits at every other vertex strictly increase projected squared norm and hence lead to a sink. If exactly one sink exists, choose a positive outgoing edge for each other vertex. Take eta less than every chosen positive normalized cross derivative. The same-layer exits persist, cross exits stay positive, and the root's outgoing derivatives stay negative. This gives an exact genuine full-SPD U1 metric with a strict rooted escape tree. The program checks these original true-centroid derivatives directly.

Conversely a full-SPD U1 metric with a STRICT escape at every nonroot remains feasible on an open neighborhood of its shear when eta is contracted to zero: each cross derivative increases, within-layer derivatives are unchanged, and the root's within-layer derivatives remain negative; equivalently the one-root positive-exit pattern exists in a generic nearby shear at eta=0. More directly, for any such body first contract eta to a sufficiently small positive value, maintaining U1 by the parent's monotonic threshold theorem; all selected positive exits remain positive. Its root is still strictly unstable, and its strict inequalities persist under a small perturbation avoiding all zero curves. Consequently the complete open-cell test decides existence of STRICT-ESCAPE U1 for fixed G and shape.

An arbitrary U1 configuration supported only by zero same-layer exits is NOT decided by open-cell absence. Every weak-free proper110 configuration is covered: a nonroot with all outgoing D<=0 and at least one zero is itself a supporting-plane equilibrium at that vertex on the boundary of its normal cone, hence a forbidden extra weak contact. Thus proper110 gives strict positive exits at all nonroots. No all-weak-U1 exclusion is claimed from this algorithm.

## 4. Executed exact controls, outside the already summarized macro/reflection/tube
The companion self-contained source h5_shear_cells.py contains the literal nine facet cycles, actual determinant volume and centroid integration, support checks, the cap factorization, exact quadratic-root ordering, complete vertical decomposition, strict-tree recovery, and all three inputs. All inputs use 0<lambda<3/5 and are outside the notebook's named all-taper macro/reflection and the new tiny tube. This does not assert they were absent from every historical partial-tree exclusion.

A: theta=(13/20,3/4,4/5,1/10,3/10), G=diag(1/2,1/2). B=2; 335 critical abscissae,334 x-slabs,10089 open fiber samples. Sink histogram {2:2111,3:3456,4:2773,5:1204,6:510,7:35}.
B: theta=(1/5,2/5,2/3,1/4,1/5), G=[[1/3,1/6],[1/6,2/3]]. B=3;457 critical abscissae,456 x-slabs,15889 open fiber samples. Sink histogram {2:1410,3:4981,4:6241,5:2530,6:708,7:19}.
C: theta=(9/10,1/10,7/8,1/16,1/10), G=[[2/3,-1/3],[-1/3,1/3]]. B=4;341 critical abscissae,340 x-slabs,10287 open fiber samples. Sink histogram {2:6108,3:2869,4:990,5:282,6:38}.

All three exact verdicts are NO_STRICT_ESCAPE_U1_AT_ANY_SHEAR_OR_POSITIVE_ETA for their fixed shape and G. These are nonattaining controls for a new decision direction, not three all-G shape exclusions. The complete reports contain exact volume, centroid and rational H_G,R_G.

## 5. Recovery
Companion source: h5_shear_cells.py, 9742 bytes, SHA-256 d4c753c4f64df7da26027452e6dcb528f690255841021c854a5a642bb0a5f89b. Tested CPython 3.13.5, standard library only. It is preserved as a separate immutable exact source material; select BOTH this proof and that code for a computational successor. No other file is required.
Commands in an empty directory containing that literal source:
python -B -S h5_shear_cells.py A
python -B -S h5_shear_cells.py B
python -B -S h5_shear_cells.py C
Each ends H5_FIXED_G_SHEAR_CELLS_EXACT_PASS. Output JSON excludes timing, which is printed separately.
Expected outputs:
h5_shear_A.json 1019 bytes SHA-256 17d9bd6829e795a387d3fcf77153a4bb21400756bd18fbcd0238559359569326
h5_shear_B.json 971 bytes SHA-256 8f75ee1519eed260f9bbdf888629b2737420af17837ede0604a64ad7d7c863ab
h5_shear_C.json 1005 bytes SHA-256 3ea986897e04cce0c7dc0688d4c60591c889d9df31db5feddb148ca7dfdb3269

The coordinator executed these calculations. This is not independent verification of the parent atlas and not proof-assistant formalization. The next substantial connection is eliminating or geometrically controlling the remaining G cone, or obtaining an actual positive U1 pencil and auditing its full polar/weak census, rather than accumulating unrelated fixed-metric controls.
